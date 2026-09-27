#!/usr/bin/env python3
"""Validate Object-Talk V2 planning and accepted image-review state.

Usage:
  python tools/validate_planning_v2.py youtube-videos/MEIN-VIDEO
  python tools/validate_planning_v2.py youtube-videos/MEIN-VIDEO --phase2

Current channel contract:
- Clean Animated Biology Illustration is the canonical image world.
- Viewer-facing text may only come from accepted Google-Flow images.
- Production IDs such as Bild_01 / Szene 01 / filenames are metadata only and must never be visible.
- Remotion visible text is forbidden; overlay-plan.json must be empty/disabled.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

IMAGE_ID_RE = re.compile(r"^Bild_\d{2,}$")
PLACEHOLDER_RE = re.compile(r"\[[^\]]+\]|\b(?:TODO|TBD|PENDING)\b", re.IGNORECASE)
VISIBLE_INTERNAL_ID_RE = re.compile(
    r"\b(?:Bild[_\s-]?\d+|Image[_\s-]?\d+|Scene[_\s-]?\d+|Szene[_\s-]?\d+)\b",
    re.IGNORECASE,
)
WEAK_OPENING_PREFIXES = (
    "in diesem video",
    "heute erklaeren wir",
    "heute erklären wir",
    "willkommen",
)


def fail(message: str) -> None:
    raise SystemExit(f"FEHLER: {message}")


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"Datei fehlt: {path}")
    except json.JSONDecodeError as exc:
        fail(f"ungueltiges JSON in {path}: {exc}")


def require_file(path: Path) -> None:
    if not path.is_file():
        fail(f"Datei fehlt: {path}")


def has_placeholder(value: object) -> bool:
    if isinstance(value, str):
        return bool(PLACEHOLDER_RE.search(value))
    if isinstance(value, list):
        return any(has_placeholder(item) for item in value)
    if isinstance(value, dict):
        return any(has_placeholder(item) for item in value.values())
    return False


def label_texts(labels: object) -> list[str]:
    if not isinstance(labels, list):
        return []
    result: list[str] = []
    for item in labels:
        if isinstance(item, str):
            result.append(item)
        elif isinstance(item, dict) and isinstance(item.get("text"), str):
            if item.get("fallback_overlay") is True:
                fail("Remotion darf niemals Label-Fallback sein")
            result.append(item["text"])
        else:
            fail(f"ungueltiger Label-Eintrag: {item!r}")
    return result


def validate_global_contract(project: Path) -> None:
    repo_root = Path(__file__).resolve().parents[1]
    config_path = repo_root / "config" / "channel.json"
    require_file(config_path)
    config = load_json(config_path)

    visual = config.get("visual_identity", {})
    flow = config.get("flow_prompting", {})
    labels = config.get("labels", {})
    presentation = config.get("presentation", {})
    remotion = config.get("remotion", {})

    if visual.get("approved_channel_style") != "Clean Animated Biology Illustration":
        fail("config/channel.json: falsche kanonische Bildwelt")
    if visual.get("written_spec_is_authoritative") is not True:
        fail("config/channel.json: schriftliche Bildwelt muss autoritativ sein")
    if flow.get("never_render_asset_ids_or_scene_numbers") is not True:
        fail("config/channel.json muss sichtbare Asset-/Szenennummern verbieten")
    if labels.get("remotion_text_overlays_allowed") is not False:
        fail("config/channel.json muss Remotion-Textoverlays deaktivieren")
    if labels.get("remotion_is_fallback_for_failed_ai_text") is not False:
        fail("Remotion darf kein Text-Fallback fuer Flow sein")
    if presentation.get("full_frame_illustration_share_target") != "100%":
        fail("Praesentation muss auf 100% Vollbild-Illustration gesetzt sein")
    if presentation.get("remotion_visible_text_allowed") is not False:
        fail("Praesentation muss sichtbaren Remotion-Text verbieten")
    if presentation.get("asset_ids_visible_in_final_video") is not False:
        fail("Asset-IDs muessen im finalen Video unsichtbar sein")
    if presentation.get("scene_numbers_visible_in_final_video") is not False:
        fail("Szenennummern muessen im finalen Video unsichtbar sein")
    if remotion.get("text_strategy") != "NO_VISIBLE_TEXT":
        fail("Remotion text_strategy muss NO_VISIBLE_TEXT sein")
    if remotion.get("text_generation_allowed") is not False:
        fail("Remotion-Textgenerierung muss hart deaktiviert sein")
    if remotion.get("text_overlay_allowed") is not False:
        fail("Remotion-Textoverlays muessen hart deaktiviert sein")
    if remotion.get("overlay_plan_must_be_empty") is not True:
        fail("Remotion overlay_plan_must_be_empty muss true sein")

    overlay_path = project / "03_pipeline" / "overlay-plan.json"
    if overlay_path.is_file():
        overlay = load_json(overlay_path)
        scenes = overlay.get("scenes", [])
        if not isinstance(scenes, list):
            fail("overlay-plan.json: scenes muss eine Liste sein")
        if scenes:
            fail("overlay-plan.json muss leer bleiben; Remotion sichtbarer Text ist verboten")
        status = str(overlay.get("status", "")).upper()
        if status not in {"DISABLED", "TEMPLATE", ""}:
            fail("overlay-plan.json muss DISABLED sein")


def validate_phase1(project: Path) -> set[str]:
    script_path = project / "01_script" / "script.txt"
    mechanism_path = project / "05_info" / "mechanism-map.md"
    sentence_plan_path = project / "05_info" / "sentence-visual-plan.json"
    scenes_path = project / "05_info" / "phase1-scenes.json"
    label_plan_path = project / "02_bildprompts" / "label-plan.json"
    flow_prompt_path = project / "02_bildprompts" / "GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt"

    for path in (
        script_path,
        mechanism_path,
        sentence_plan_path,
        scenes_path,
        label_plan_path,
        flow_prompt_path,
    ):
        require_file(path)

    validate_global_contract(project)

    mechanism_text = mechanism_path.read_text(encoding="utf-8")
    if PLACEHOLDER_RE.search(mechanism_text):
        fail("Mechanism Map enthaelt noch Platzhalter")

    flow_prompt_text = flow_prompt_path.read_text(encoding="utf-8").lower()
    if "never" not in flow_prompt_text or "production" not in flow_prompt_text:
        fail("Flow-Prompt muss Produktions-IDs ausdruecklich als unsichtbar markieren")

    sentence_plan = load_json(sentence_plan_path)
    if str(sentence_plan.get("status", "")).upper() in {"TEMPLATE", "PENDING", ""}:
        fail("sentence-visual-plan.json ist nicht READY")
    items = sentence_plan.get("items")
    if not isinstance(items, list) or not items:
        fail("sentence-visual-plan.json enthaelt keine Items")

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

    first = items[0]
    if not isinstance(first, dict) or str(first.get("function", "")).lower() != "hook":
        fail("Der erste Sentence-Visual-Beat muss function='hook' besitzen")
    first_text = str(first.get("voiceover_text", "")).strip().lower()
    if not first_text:
        fail("Hook-Text fehlt")
    if any(first_text.startswith(prefix) for prefix in WEAK_OPENING_PREFIXES):
        fail("Script startet mit schwachem Intro statt Neugier-Hook")

    sentence_image_ids: set[str] = set()
    for index, item in enumerate(items, start=1):
        if not isinstance(item, dict):
            fail(f"Sentence-Visual-Item {index} ist kein Objekt")
        missing = required_item_keys - item.keys()
        if missing:
            fail(f"Sentence-Visual-Item {index} fehlen Felder: {sorted(missing)}")
        if has_placeholder(item):
            fail(f"Sentence-Visual-Item {index} enthaelt Platzhalter")
        image_id = item.get("image_asset_id")
        if not isinstance(image_id, str) or not IMAGE_ID_RE.match(image_id):
            fail(f"ungueltige image_asset_id in Item {index}: {image_id!r}")
        sentence_image_ids.add(image_id)
        labels = item.get("labels", [])
        if not isinstance(labels, list) or len(labels) > 3:
            fail(f"Sentence-Visual-Item {index}: maximal 3 Labels")

    scene_payload = load_json(scenes_path)
    if str(scene_payload.get("status", "")).upper() in {"TEMPLATE", "PENDING", ""}:
        fail("phase1-scenes.json ist nicht READY")
    scenes = scene_payload.get("scenes")
    if not isinstance(scenes, list) or not scenes:
        fail("phase1-scenes.json enthaelt keine Szenen")

    rules = scene_payload.get("rules", {})
    if not isinstance(rules, dict):
        fail("phase1-scenes.json: rules muss Objekt sein")
    if rules.get("remotion_text_overlays_allowed") is not False:
        fail("phase1-scenes.json muss remotion_text_overlays_allowed=false setzen")
    if rules.get("production_ids_visible_in_images") is not False:
        fail("phase1-scenes.json muss sichtbare Produktions-IDs verbieten")

    scene_ids: list[str] = []
    for index, scene in enumerate(scenes, start=1):
        if not isinstance(scene, dict):
            fail(f"phase1-scenes.json: Szene {index} ist ungueltig")
        if int(scene.get("scene", 0)) != index:
            fail(f"phase1-scenes.json: erwartete Szene {index}")
        expected_id = f"Bild_{index:02d}"
        if scene.get("image") != expected_id:
            fail(f"Szene {index}: erwartetes {expected_id}, gefunden {scene.get('image')!r}")
        labels_de = scene.get("labels_de", [])
        if not isinstance(labels_de, list) or len(labels_de) > 3:
            fail(f"Szene {index}: labels_de darf maximal 3 Eintraege enthalten")
        scene_ids.append(expected_id)

    scene_id_set = set(scene_ids)
    if len(scene_id_set) != len(scene_ids):
        fail("phase1-scenes.json enthaelt doppelte Bild-IDs")
    if sentence_image_ids - scene_id_set:
        fail(f"Sentence-Visual-Bilder fehlen im Szenenplan: {sorted(sentence_image_ids - scene_id_set)}")

    label_plan = load_json(label_plan_path)
    if str(label_plan.get("status", "")).upper() in {"TEMPLATE", "PENDING", ""}:
        fail("label-plan.json ist nicht READY")
    label_rules = label_plan.get("rules", {})
    if not isinstance(label_rules, dict):
        fail("label-plan.json: rules muss Objekt sein")
    if label_rules.get("no_asset_ids_visible") is not True:
        fail("label-plan.json muss no_asset_ids_visible=true setzen")
    if label_rules.get("remotion_visible_text_allowed") is not False:
        fail("label-plan.json muss Remotion sichtbaren Text verbieten")
    if label_rules.get("remotion_text_fallback_allowed") is not False:
        fail("label-plan.json muss Remotion-Text-Fallback verbieten")

    entries = label_plan.get("images")
    if not isinstance(entries, list):
        fail("label-plan.json: images muss Liste sein")

    planned: set[str] = set()
    for entry in entries:
        if not isinstance(entry, dict):
            fail("label-plan.json enthaelt ungueltigen Eintrag")
        image_id = entry.get("image_asset_id")
        if image_id not in scene_id_set:
            fail(f"Label-Plan referenziert unbekanntes Bild: {image_id}")
        if image_id in planned:
            fail(f"Label-Plan enthaelt doppelten Eintrag fuer {image_id}")
        planned.add(image_id)

        allowed = entry.get("allowed_visible_text", [])
        if not isinstance(allowed, list):
            fail(f"{image_id}: allowed_visible_text muss Liste sein")
        if any(not isinstance(text, str) or not text.strip() for text in allowed):
            fail(f"{image_id}: allowed_visible_text enthaelt ungueltigen Text")
        if any(VISIBLE_INTERNAL_ID_RE.search(text) for text in allowed):
            fail(f"{image_id}: interne Produktions-ID steht in allowed_visible_text")

        texts = label_texts(entry.get("labels", []))
        if len(texts) > 3:
            fail(f"{image_id}: maximal 3 Labels erlaubt")
        if any(VISIBLE_INTERNAL_ID_RE.search(text) for text in texts):
            fail(f"{image_id}: internes Produktions-ID-Label ist verboten")

        if image_id != "Bild_01" and sorted(texts) != sorted(allowed):
            fail(f"{image_id}: Labels und allowed_visible_text stimmen nicht ueberein")

    if planned != scene_id_set:
        fail(
            f"Label-Plan muss exakt alle Bilder abdecken. Fehlend={sorted(scene_id_set - planned)}, "
            f"extra={sorted(planned - scene_id_set)}"
        )

    test_mode_path = project / "05_info" / "test-mode.json"
    if test_mode_path.is_file():
        test_mode = load_json(test_mode_path)
        expected_images = test_mode.get("expected_images")
        if expected_images is not None and int(expected_images) != len(scene_ids):
            fail(f"test-mode.json expected_images={expected_images}, geplant sind {len(scene_ids)}")

    print(f"V2-PHASE-1-PASS: {project}")
    print(f"  Szenen/Bilder: {len(scene_id_set)}")
    print("  Remotion sichtbarer Text: 0 (hart deaktiviert)")
    print("  Produktions-IDs im finalen Bild: verboten")
    return scene_id_set


def validate_phase2(project: Path, expected_ids: set[str]) -> None:
    review_path = project / "02_bildprompts" / "image-review.json"
    images_dir = project / "02_bildprompts" / "images"
    require_file(review_path)
    if not images_dir.is_dir():
        fail(f"finaler Bilderordner fehlt: {images_dir}")

    review = load_json(review_path)
    status = str(review.get("status", "")).upper()
    if status in {"TEMPLATE", "PENDING_IMAGES", "PENDING", ""}:
        fail(f"image-review.json ist noch nicht final: status={status or 'LEER'}")

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
        "complexity_control",
        "label_accuracy",
        "overall_score",
    )

    for entry in entries:
        if not isinstance(entry, dict):
            fail("image-review.json enthaelt ungueltigen Eintrag")
        image_id = entry.get("image_asset_id")
        if image_id not in expected_ids:
            fail(f"Bildreview referenziert unbekanntes Bild: {image_id}")
        if image_id in reviewed:
            fail(f"mehrfacher retained Review fuer {image_id}")
        reviewed.add(image_id)

        require_file(images_dir / f"{image_id}.png")

        if entry.get("decision") != "ACCEPT":
            fail(f"{image_id}: Bild ist nicht ACCEPT")
        if entry.get("ai_artifact_check") != "PASS":
            fail(f"{image_id}: AI-Artefakt-Check nicht bestanden")
        if entry.get("visible_text_whitelist") != "PASS":
            fail(f"{image_id}: sichtbarer Text nicht gegen Whitelist bestanden")
        if entry.get("no_visible_asset_id") != "PASS":
            fail(f"{image_id}: sichtbare Asset-/Bildnummer nicht ausgeschlossen")
        if entry.get("no_visible_scene_number") != "PASS":
            fail(f"{image_id}: sichtbare Szenennummer nicht ausgeschlossen")
        if entry.get("no_visible_filename_or_prompt_heading") != "PASS":
            fail(f"{image_id}: sichtbarer Dateiname/Prompttitel nicht ausgeschlossen")
        if entry.get("single_retained_asset_for_scene") != "PASS":
            fail(f"{image_id}: single retained asset check nicht bestanden")

        for key in numeric_min_8:
            value = entry.get(key)
            if not isinstance(value, (int, float)) or value < 8.0:
                fail(f"{image_id}: {key} muss mindestens 8.0 sein")

        scene_difference = entry.get("scene_difference")
        if isinstance(scene_difference, str):
            if scene_difference.upper() not in {"PASS", "OK"}:
                fail(f"{image_id}: scene_difference nicht bestanden")
        elif isinstance(scene_difference, (int, float)):
            if scene_difference < 8.0:
                fail(f"{image_id}: scene_difference muss mindestens 8.0 sein")
        else:
            fail(f"{image_id}: scene_difference fehlt")

    if reviewed != expected_ids:
        fail(f"Bildreviews fehlen fuer: {sorted(expected_ids - reviewed)}")

    actual = {path.stem for path in images_dir.glob("Bild_*.png")}
    if actual != expected_ids:
        fail(
            f"finaler Bilderordner stimmt nicht mit Planung ueberein. "
            f"Fehlend={sorted(expected_ids - actual)}, extra={sorted(actual - expected_ids)}"
        )

    print(f"V2-PHASE-2-PASS: {project}")
    print(f"  akzeptierte Bilder: {len(reviewed)}")
    print("  keine sichtbaren Produktions-IDs bestaetigt")
    print("  Remotion-Text bleibt deaktiviert")


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
