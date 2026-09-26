#!/usr/bin/env python3
"""Validate Object-Talk V2 planning and accepted image-review state.

Usage:
  python tools/validate_planning_v2.py youtube-videos/MEIN-VIDEO
  python tools/validate_planning_v2.py youtube-videos/MEIN-VIDEO --phase2

Phase 1 fails closed when the script has no explicit hook beat, visible text is
not Flow-only, or Remotion text overlays are planned.

Phase 2 fails closed when accepted review JSON is not enough if the corresponding
final image asset is missing, visible text was not whitelist-checked, the cover
hook leaked into normal scenes, internal asset IDs appeared, scene novelty is
weak, or multiple retained variants exist for one normal scene.
"""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
from pathlib import Path

IMAGE_ID_RE = re.compile(r"^Bild_\d{2,}$")
PLACEHOLDER_RE = re.compile(r"\[[^\]]+\]|\b(?:TODO|TBD|PENDING)\b", re.IGNORECASE)
WEAK_OPENING_PREFIXES = (
    "in diesem video",
    "heute erklaeren wir",
    "heute erklären wir",
    "willkommen",
)


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"FEHLER: Datei fehlt: {path}")
    except json.JSONDecodeError as exc:
        raise SystemExit(f"FEHLER: ungueltiges JSON in {path}: {exc}")


def require_file(path: Path) -> None:
    if not path.is_file():
        raise SystemExit(f"FEHLER: Datei fehlt: {path}")


def fail(message: str) -> None:
    raise SystemExit(f"FEHLER: {message}")


def has_placeholder(value: object) -> bool:
    if isinstance(value, str):
        return bool(PLACEHOLDER_RE.search(value))
    if isinstance(value, list):
        return any(has_placeholder(item) for item in value)
    if isinstance(value, dict):
        return any(has_placeholder(item) for item in value.values())
    return False


def normalize_visible_text(value: str) -> str:
    value = unicodedata.normalize("NFKC", str(value)).casefold().replace("ß", "ss")
    return " ".join("".join(ch if ch.isalnum() else " " for ch in value).split())


def validate_no_remotion_text(project: Path) -> None:
    overlay_path = project / "03_pipeline" / "overlay-plan.json"
    if not overlay_path.is_file():
        return

    payload = load_json(overlay_path)
    scenes = payload.get("scenes", [])
    if not isinstance(scenes, list):
        fail("overlay-plan.json: scenes muss eine Liste sein")

    non_empty: list[int] = []
    for entry in scenes:
        if not isinstance(entry, dict):
            fail("overlay-plan.json enthaelt ungueltigen Szeneneintrag")
        overlays = entry.get("overlays", [])
        if not isinstance(overlays, list):
            fail("overlay-plan.json: overlays muss eine Liste sein")
        if overlays:
            non_empty.append(int(entry.get("scene", 0)))

    if non_empty:
        fail(
            "Remotion-Textoverlays sind deaktiviert. Alle sichtbaren Texte muessen aus Google Flow kommen. "
            f"Nicht-leere Overlay-Szenen: {non_empty}"
        )


def validate_phase1(project: Path) -> set[str]:
    mechanism = project / "05_info" / "mechanism-map.md"
    sentence_plan_path = project / "05_info" / "sentence-visual-plan.json"
    label_plan_path = project / "02_bildprompts" / "label-plan.json"
    scenes_path = project / "05_info" / "phase1-scenes.json"

    for path in (mechanism, sentence_plan_path, label_plan_path, scenes_path):
        require_file(path)

    validate_no_remotion_text(project)

    mechanism_text = mechanism.read_text(encoding="utf-8")
    if PLACEHOLDER_RE.search(mechanism_text):
        fail(f"Mechanism Map enthaelt noch Platzhalter: {mechanism}")

    sentence_plan = load_json(sentence_plan_path)
    if str(sentence_plan.get("status", "")).upper() == "TEMPLATE":
        fail("sentence-visual-plan.json steht noch auf TEMPLATE")
    items = sentence_plan.get("items")
    if not isinstance(items, list) or not items:
        fail("sentence-visual-plan.json enthaelt keine Items")

    first_item = items[0]
    if not isinstance(first_item, dict) or str(first_item.get("function", "")).lower() != "hook":
        fail("Der erste Sentence-Visual-Beat muss function='hook' besitzen")
    first_text = str(first_item.get("voiceover_text", "")).strip()
    if not first_text:
        fail("Der Hook-Text fehlt")
    normalized_first = normalize_visible_text(first_text)
    if any(normalized_first.startswith(normalize_visible_text(prefix)) for prefix in WEAK_OPENING_PREFIXES):
        fail("Script startet mit einem schwachen Schulbuch-/Intro-Opening statt einem Neugier-Hook")

    required_item_keys = {
        "id",
        "voiceover_text",
        "function",
        "learning_goal",
        "claim_ids",
        "scale_level",
        "new_image_required",
        "image_asset_id",
        "visual_type",
        "visible_change",
        "scene_difference",
        "labels",
        "misconception_to_avoid",
    }
    sentence_image_ids: set[str] = set()
    for index, item in enumerate(items, start=1):
        if not isinstance(item, dict):
            fail(f"Sentence-Visual-Item {index} ist kein Objekt")
        missing = required_item_keys - item.keys()
        if missing:
            fail(f"Sentence-Visual-Item {index} fehlen Felder: {sorted(missing)}")
        if has_placeholder(item):
            fail(f"Sentence-Visual-Item {index} enthaelt Platzhalter")
        image_id = item["image_asset_id"]
        if not isinstance(image_id, str) or not IMAGE_ID_RE.match(image_id):
            fail(f"ungueltige image_asset_id in Item {index}: {image_id!r}")
        sentence_image_ids.add(image_id)

    scene_payload = load_json(scenes_path)
    scenes = scene_payload.get("scenes")
    if not isinstance(scenes, list) or not scenes:
        fail("phase1-scenes.json enthaelt keine Szenen")

    scene_rules = scene_payload.get("rules", {})
    if isinstance(scene_rules, dict) and scene_rules.get("remotion_text_overlays_allowed") is not False:
        fail("phase1-scenes.json muss remotion_text_overlays_allowed=false setzen")

    scene_image_ids_list = [
        scene.get("image")
        for scene in scenes
        if isinstance(scene, dict) and isinstance(scene.get("image"), str)
    ]
    scene_image_ids = set(scene_image_ids_list)
    if len(scene_image_ids) != len(scene_image_ids_list):
        fail("phase1-scenes.json enthaelt doppelte image-IDs")

    expected_ids = {f"Bild_{index:02d}" for index in range(1, len(scenes) + 1)}
    if scene_image_ids != expected_ids:
        fail(
            "phase1-scenes.json muss lueckenlose eindeutige Bildnummern enthalten: "
            f"erwartet {sorted(expected_ids)}, gefunden {sorted(scene_image_ids)}"
        )

    missing_in_scenes = sentence_image_ids - scene_image_ids
    if missing_in_scenes:
        fail(f"Sentence-Visual-Bilder fehlen in phase1-scenes.json: {sorted(missing_in_scenes)}")

    label_plan = load_json(label_plan_path)
    if str(label_plan.get("status", "")).upper() == "TEMPLATE":
        fail("label-plan.json steht noch auf TEMPLATE")
    images = label_plan.get("images")
    if not isinstance(images, list):
        fail("label-plan.json: images muss eine Liste sein")

    rules = label_plan.get("rules", {})
    if not isinstance(rules, dict):
        fail("label-plan.json: rules muss ein Objekt sein")
    if rules.get("fallback_to_overlay_if_ai_text_wrong") is not False:
        fail("label-plan.json darf keinen Remotion-Text-Fallback erlauben")
    if rules.get("remotion_text_overlays_allowed") is not False:
        fail("label-plan.json muss remotion_text_overlays_allowed=false setzen")
    if rules.get("flow_is_final_visible_text_source") is not True:
        fail("label-plan.json muss Google Flow als finale sichtbare Textquelle festlegen")

    cover_entry = next(
        (entry for entry in images if isinstance(entry, dict) and entry.get("image_asset_id") == "Bild_01"),
        None,
    )
    if not isinstance(cover_entry, dict):
        fail("label-plan.json: Bild_01/Cover-Eintrag fehlt")
    cover_hook = cover_entry.get("hook_text")
    if not isinstance(cover_hook, str) or not cover_hook.strip():
        fail("Bild_01: deutsche Cover-Hook fehlt im label-plan.json")
    normalized_cover_hook = normalize_visible_text(cover_hook)

    planned_ids: set[str] = set()
    hook_whitelist_occurrences = 0

    for entry in images:
        if not isinstance(entry, dict):
            fail("label-plan.json enthaelt einen ungueltigen Eintrag")
        image_id = entry.get("image_asset_id")
        if image_id not in scene_image_ids:
            fail(f"Label-Plan referenziert unbekanntes Bild: {image_id}")
        if image_id in planned_ids:
            fail(f"Label-Plan enthaelt doppelten Eintrag fuer {image_id}")
        planned_ids.add(image_id)

        labels = entry.get("labels", [])
        if not isinstance(labels, list) or len(labels) > 3:
            fail(f"{image_id}: 0 bis 3 kurze deutsche Labels sind erlaubt")

        allowed_visible_text = entry.get("allowed_visible_text")
        if not isinstance(allowed_visible_text, list):
            fail(f"{image_id}: allowed_visible_text muss als explizite Whitelist vorhanden sein")
        if any(not isinstance(text, str) or not text.strip() for text in allowed_visible_text):
            fail(f"{image_id}: allowed_visible_text enthaelt leeren/ungueltigen Text")

        normalized_allowed = [normalize_visible_text(text) for text in allowed_visible_text]
        hook_whitelist_occurrences += sum(text == normalized_cover_hook for text in normalized_allowed)

        if image_id == "Bild_01":
            if labels:
                fail("Bild_01: Cover darf keine zusaetzlichen Anatomie-Labels enthalten")
            if normalized_allowed != [normalized_cover_hook]:
                fail("Bild_01: Whitelist muss exakt nur die Cover-Hook enthalten")
        else:
            if "hook_text" in entry:
                fail(f"{image_id}: normale Szene darf kein hook_text-Feld besitzen")
            if normalized_cover_hook in normalized_allowed:
                fail(f"{image_id}: Cover-Hook darf nach Bild_01 niemals in der Text-Whitelist stehen")
            if any(
                normalized_cover_hook and (
                    text.startswith(normalized_cover_hook)
                    or normalized_cover_hook.startswith(text)
                )
                and len(text.split()) >= 3
                for text in normalized_allowed
            ):
                fail(f"{image_id}: normale Szene enthaelt eine nahezu identische Cover-Hook")
            if len(labels) > 2:
                print(f"WARNUNG: {image_id} nutzt 3 Labels; 0–2 sind bevorzugt.")

        label_texts = [label.get("text") for label in labels if isinstance(label, dict)]
        if sorted(normalize_visible_text(text) for text in label_texts if isinstance(text, str)) != sorted(
            normalize_visible_text(text) for text in allowed_visible_text
        ) and image_id != "Bild_01":
            fail(f"{image_id}: allowed_visible_text muss exakt den geplanten Labels entsprechen")

        for label in labels:
            if not isinstance(label, dict):
                fail(f"{image_id}: Label-Eintrag ist ungueltig")
            if "text" not in label or "fallback_overlay" not in label:
                fail(f"{image_id}: Label braucht mindestens text und fallback_overlay")
            if label.get("fallback_overlay") is not False:
                fail(f"{image_id}: fallback_overlay muss false sein; Remotion-Text ist verboten")
            if has_placeholder(label):
                fail(f"{image_id}: Label enthaelt Platzhalter")
            text = label.get("text")
            if not isinstance(text, str) or not text.strip():
                fail(f"{image_id}: Labeltext fehlt")

    if hook_whitelist_occurrences != 1:
        fail(
            "Cover-Hook muss im gesamten label-plan exakt einmal als erlaubter sichtbarer Text vorkommen "
            f"(gefunden: {hook_whitelist_occurrences})"
        )

    if planned_ids != scene_image_ids:
        missing_labels = scene_image_ids - planned_ids
        extra_labels = planned_ids - scene_image_ids
        fail(
            f"Label-Plan muss exakt alle Szenen abdecken. Fehlend={sorted(missing_labels)}, "
            f"extra={sorted(extra_labels)}"
        )

    print(f"V2-PHASE-1-PASS: {project}")
    print(f"  Hook-Beat: {first_text}")
    print(f"  Satz-/Visual-Items: {len(items)}")
    print(f"  geplante Szenen/Bilder: {len(scene_image_ids)}")
    print("  Flow ist einzige sichtbare Textquelle; Remotion-Textoverlays sind deaktiviert")
    return scene_image_ids


def validate_reference_policy(project: Path) -> None:
    repo_root = Path(__file__).resolve().parents[1]
    channel_config_path = repo_root / "config" / "channel.json"
    require_file(channel_config_path)
    config = load_json(channel_config_path)
    visual = config.get("visual_identity", {})
    flow = config.get("flow_prompting", {})
    labels = config.get("labels", {})
    remotion = config.get("remotion", {})

    if flow.get("textual_reference_mentions_do_not_count_as_attachment") is not True:
        fail("config/channel.json muss textliche Referenz-Erwaehnungen als unzureichend markieren")
    if flow.get("attach_bild_01_on_every_followup") is not False:
        fail("config/channel.json muss das texttragende Bild_01 als Folge-Szenenreferenz deaktivieren")
    if flow.get("never_use_text_bearing_cover_as_followup_reference") is not True:
        fail("config/channel.json muss texttragende Cover als Follow-up-Referenz verbieten")
    if flow.get("require_text_free_reference_for_followups") is not True:
        fail("config/channel.json muss eine textfreie Referenz fuer Follow-up-Szenen verlangen")
    if flow.get("cover_hook_unique_to_bild_01") is not True:
        fail("config/channel.json muss die Cover-Hook exklusiv auf Bild_01 beschraenken")
    if flow.get("cover_hook_forbidden_after_bild_01") is not True:
        fail("config/channel.json muss Cover-Hook nach Bild_01 verbieten")
    if flow.get("visible_text_in_generated_images") is not True:
        fail("sichtbarer deutscher Text muss fuer Flow-Bilder aktiviert sein")
    if flow.get("cover_hook_generated_by_flow") is not True:
        fail("Bild_01 muss die deutsche Cover-Hook bereits in Flow erhalten")
    if labels.get("render_in_flow") is not True:
        fail("wichtige deutsche Labels muessen direkt in Flow erzeugt werden")
    if labels.get("remotion_text_overlays_allowed") is not False:
        fail("config/channel.json muss Remotion-Textoverlays deaktivieren")
    if labels.get("remotion_is_fallback_for_failed_ai_text") is not False:
        fail("Remotion darf kein Text-Fallback fuer Flow sein")
    if labels.get("flow_text_is_final_visual_text_source") is not True:
        fail("Google Flow muss finale sichtbare Textquelle sein")
    if labels.get("final_video_must_contain_required_labels") is not True:
        fail("finales Video muss alle geplanten deutschen Labels enthalten")
    if labels.get("cover_hook_must_never_repeat_as_normal_scene_text") is not True:
        fail("Label-Konfiguration muss Cover-Hook-Wiederholung in Normalbildern verbieten")
    if remotion.get("text_generation_allowed") is not False or remotion.get("text_overlay_allowed") is not False:
        fail("config/channel.json muss Remotion-Textgenerierung und Textoverlays hart deaktivieren")

    style_rel = visual.get("style_reference")
    if visual.get("clean_style_reference_asset_present") is True:
        if not isinstance(style_rel, str) or not (repo_root / style_rel).is_file():
            fail("clean_style_reference_asset_present=true, aber STYLE_REFERENCE-Datei fehlt")
    elif visual.get("style_reference_required_after_lock") is True:
        if visual.get("bootstrap_without_channel_reference_allowed") is not True:
            fail("STYLE_REFERENCE fehlt und Bootstrap-Modus ist nicht ausdruecklich erlaubt")


def validate_phase2(project: Path, expected_image_ids: set[str]) -> None:
    validate_reference_policy(project)

    review_path = project / "02_bildprompts" / "image-review.json"
    images_dir = project / "02_bildprompts" / "images"
    require_file(review_path)
    if not images_dir.is_dir():
        fail(f"finaler Bilderordner fehlt: {images_dir}")

    review = load_json(review_path)
    status = str(review.get("status", "")).upper()
    if status in {"TEMPLATE", "PENDING_IMAGES", "PENDING"}:
        fail(f"image-review.json ist noch nicht final: status={status or 'LEER'}")
    if has_placeholder(review):
        fail("image-review.json enthaelt noch TODO/TBD/PENDING-Werte")

    entries = review.get("images")
    if not isinstance(entries, list) or not entries:
        fail("image-review.json enthaelt keine Bildreviews")

    reviewed: set[str] = set()
    numeric_min_8 = (
        "scientific_accuracy",
        "voiceover_match",
        "immediate_clarity",
        "style_continuity",
        "composition",
        "visual_novelty",
        "information_value",
        "label_accuracy",
        "overall_score",
    )

    for entry in entries:
        if not isinstance(entry, dict):
            fail("image-review.json enthaelt ungueltigen Eintrag")
        image_id = entry.get("image_asset_id")
        if image_id not in expected_image_ids:
            fail(f"Bildreview referenziert unbekanntes Bild: {image_id}")
        if image_id in reviewed:
            fail(f"image-review.json enthaelt mehrfachen retained Review fuer {image_id}")
        reviewed.add(image_id)

        image_path = images_dir / f"{image_id}.png"
        require_file(image_path)

        if entry.get("decision") != "ACCEPT":
            fail(f"{image_id}: Bild ist nicht ACCEPT")
        if entry.get("ai_artifact_check") != "PASS":
            fail(f"{image_id}: AI-Artefakt-Check nicht bestanden")
        if entry.get("visible_text_whitelist") != "PASS":
            fail(f"{image_id}: sichtbarer Text wurde nicht gegen Whitelist bestanden")
        if entry.get("cover_hook_isolated") != "PASS":
            fail(f"{image_id}: Cover-Hook-Isolation nicht bestanden")
        if entry.get("no_visible_asset_id") != "PASS":
            fail(f"{image_id}: Asset-/Bild-/Szenennummer ist sichtbar oder ungeprueft")
        if entry.get("single_retained_asset_for_scene") != "PASS":
            fail(f"{image_id}: mehrere retained Varianten vorhanden oder ungeprueft")
        if image_id != "Bild_01" and entry.get("text_free_reference_used") != "PASS":
            fail(f"{image_id}: textfreie Style-Referenz fuer Follow-up-Szene nicht bestaetigt")

        for key in numeric_min_8:
            value = entry.get(key)
            if not isinstance(value, (int, float)) or value < 8.0:
                fail(f"{image_id}: {key} muss mindestens 8.0 sein")

        scene_difference = entry.get("scene_difference")
        if isinstance(scene_difference, str):
            if scene_difference.upper() not in {"PASS", "OK"}:
                fail(f"{image_id}: scene_difference nicht bestanden: {scene_difference}")
        elif isinstance(scene_difference, (int, float)):
            if scene_difference < 8.0:
                fail(f"{image_id}: scene_difference muss mindestens 8.0 sein")
        else:
            fail(f"{image_id}: scene_difference fehlt oder ist ungueltig")

    missing = expected_image_ids - reviewed
    if missing:
        fail(f"Bildreviews fehlen fuer: {sorted(missing)}")

    final_pngs = list(images_dir.glob("Bild_*.png"))
    stems = [path.stem for path in final_pngs]
    if len(stems) != len(set(stems)):
        fail("finaler Bilderordner enthaelt doppelte Bildstems")

    actual_png_ids = set(stems)
    extra_pngs = actual_png_ids - expected_image_ids
    missing_pngs = expected_image_ids - actual_png_ids
    if extra_pngs:
        fail(f"unerwartete finale Bilddateien: {sorted(extra_pngs)}")
    if missing_pngs:
        fail(f"fehlende finale Bilddateien: {sorted(missing_pngs)}")

    print(f"V2-PHASE-2-REVIEW-PASS: {project}")
    print(f"  akzeptierte eindeutige Bildreviews: {len(reviewed)}")
    print("  Hook-Isolation, Flow-Text, textfreie Referenzen, visuelle Neuheit und Informationswert bestaetigt")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("project", help="Pfad zum Video-Projekt")
    parser.add_argument("--phase2", action="store_true", help="zusaetzlich finale Bildreviews und Assets pruefen")
    args = parser.parse_args()

    project = Path(args.project).resolve()
    if not project.is_dir():
        fail(f"Projektordner nicht gefunden: {project}")

    expected = validate_phase1(project)
    if args.phase2:
        validate_phase2(project, expected)


if __name__ == "__main__":
    main()
