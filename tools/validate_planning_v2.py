#!/usr/bin/env python3
"""Validate Object-Talk V2 planning and accepted image-review state.

Usage:
  python tools/validate_planning_v2.py youtube-videos/MEIN-VIDEO
  python tools/validate_planning_v2.py youtube-videos/MEIN-VIDEO --phase2

Phase 2 fails closed: accepted review JSON is not enough if the corresponding
final image asset is missing, visible text was not whitelist-checked, internal
asset IDs appeared, or multiple retained variants exist for one normal scene.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

IMAGE_ID_RE = re.compile(r"^Bild_\d{2,}$")
PLACEHOLDER_RE = re.compile(r"\[[^\]]+\]|\b(?:TODO|TBD|PENDING)\b", re.IGNORECASE)


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


def validate_phase1(project: Path) -> set[str]:
    mechanism = project / "05_info" / "mechanism-map.md"
    sentence_plan_path = project / "05_info" / "sentence-visual-plan.json"
    label_plan_path = project / "02_bildprompts" / "label-plan.json"
    scenes_path = project / "05_info" / "phase1-scenes.json"

    for path in (mechanism, sentence_plan_path, label_plan_path, scenes_path):
        require_file(path)

    mechanism_text = mechanism.read_text(encoding="utf-8")
    if PLACEHOLDER_RE.search(mechanism_text):
        fail(f"Mechanism Map enthaelt noch Platzhalter: {mechanism}")

    sentence_plan = load_json(sentence_plan_path)
    if str(sentence_plan.get("status", "")).upper() == "TEMPLATE":
        fail("sentence-visual-plan.json steht noch auf TEMPLATE")
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

    planned_ids: set[str] = set()
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

        if image_id == "Bild_01":
            hook = entry.get("hook_text")
            if not isinstance(hook, str) or not hook.strip():
                fail("Bild_01: deutsche Cover-Hook fehlt im label-plan.json")
            if labels:
                fail("Bild_01: Cover darf keine zusaetzlichen Anatomie-Labels enthalten")
        elif len(labels) > 2:
            print(f"WARNUNG: {image_id} nutzt 3 Labels; 0–2 sind bevorzugt.")

        for label in labels:
            if not isinstance(label, dict):
                fail(f"{image_id}: Label-Eintrag ist ungueltig")
            if "text" not in label or "fallback_overlay" not in label:
                fail(f"{image_id}: Label braucht mindestens text und fallback_overlay")
            if has_placeholder(label):
                fail(f"{image_id}: Label enthaelt Platzhalter")
            text = label.get("text")
            if not isinstance(text, str) or not text.strip():
                fail(f"{image_id}: Labeltext fehlt")

    if planned_ids != scene_image_ids:
        missing_labels = scene_image_ids - planned_ids
        extra_labels = planned_ids - scene_image_ids
        fail(
            f"Label-Plan muss exakt alle Szenen abdecken. Fehlend={sorted(missing_labels)}, "
            f"extra={sorted(extra_labels)}"
        )

    print(f"V2-PHASE-1-PASS: {project}")
    print(f"  Satz-/Visual-Items: {len(items)}")
    print(f"  geplante Szenen/Bilder: {len(scene_image_ids)}")
    print("  sichtbarer Text ist whitelist-basiert; normale Bilder 0–2 Labels bevorzugt")
    return scene_image_ids


def validate_reference_policy(project: Path) -> None:
    repo_root = Path(__file__).resolve().parents[1]
    channel_config_path = repo_root / "config" / "channel.json"
    require_file(channel_config_path)
    config = load_json(channel_config_path)
    visual = config.get("visual_identity", {})
    flow = config.get("flow_prompting", {})
    labels = config.get("labels", {})

    if flow.get("textual_reference_mentions_do_not_count_as_attachment") is not True:
        fail("config/channel.json muss textliche Referenz-Erwaehnungen als unzureichend markieren")
    if flow.get("attach_bild_01_on_every_followup") is not True:
        fail("config/channel.json muss Bild_01 als echte Referenz fuer Folgebilder verlangen")
    if flow.get("visible_text_in_generated_images") is not True:
        fail("sichtbarer deutscher Text muss fuer Flow-Bilder aktiviert sein")
    if flow.get("cover_hook_generated_by_flow") is not True:
        fail("Bild_01 muss die deutsche Cover-Hook bereits in Flow erhalten")
    if labels.get("render_in_flow") is not True:
        fail("wichtige deutsche Labels muessen standardmaessig direkt in Flow erzeugt werden")
    if labels.get("final_video_must_contain_required_labels") is not True:
        fail("finales Video muss alle geplanten deutschen Labels enthalten")

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
        if entry.get("no_visible_asset_id") != "PASS":
            fail(f"{image_id}: Asset-/Bild-/Szenennummer ist sichtbar oder ungeprueft")
        if entry.get("single_retained_asset_for_scene") != "PASS":
            fail(f"{image_id}: mehrere retained Varianten vorhanden oder ungeprueft")

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
    print("  Whitelist, keine sichtbaren Asset-IDs und genau ein retained Asset pro Szene bestaetigt")


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
