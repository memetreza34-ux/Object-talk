#!/usr/bin/env python3
"""Validate Object-Talk V2 planning and accepted image-review state.

Usage:
  python tools/validate_planning_v2.py youtube-videos/MEIN-VIDEO
  python tools/validate_planning_v2.py youtube-videos/MEIN-VIDEO --phase2

Phase 2 intentionally fails closed: accepted review JSON is not enough if the
corresponding final image asset is missing or review fields are incomplete.
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

    scenes = load_json(scenes_path).get("scenes")
    if not isinstance(scenes, list) or not scenes:
        fail("phase1-scenes.json enthaelt keine Szenen")
    scene_image_ids = {
        scene.get("image") for scene in scenes if isinstance(scene, dict) and isinstance(scene.get("image"), str)
    }
    missing_in_scenes = sentence_image_ids - scene_image_ids
    if missing_in_scenes:
        fail(f"Sentence-Visual-Bilder fehlen in phase1-scenes.json: {sorted(missing_in_scenes)}")

    label_plan = load_json(label_plan_path)
    if str(label_plan.get("status", "")).upper() == "TEMPLATE":
        fail("label-plan.json steht noch auf TEMPLATE")
    images = label_plan.get("images")
    if not isinstance(images, list):
        fail("label-plan.json: images muss eine Liste sein")
    for entry in images:
        if not isinstance(entry, dict):
            fail("label-plan.json enthaelt einen ungueltigen Eintrag")
        image_id = entry.get("image_asset_id")
        if image_id not in scene_image_ids:
            fail(f"Label-Plan referenziert unbekanntes Bild: {image_id}")
        labels = entry.get("labels", [])
        if not isinstance(labels, list) or len(labels) > 3:
            fail(f"{image_id}: maximal 3 Labels erlaubt")
        for label in labels:
            if not isinstance(label, dict):
                fail(f"{image_id}: Label-Eintrag ist ungueltig")
            for key in ("text", "target", "reason", "fallback_overlay"):
                if key not in label:
                    fail(f"{image_id}: Label-Feld fehlt: {key}")
            if has_placeholder(label):
                fail(f"{image_id}: Label enthaelt Platzhalter")

    print(f"V2-PHASE-1-PASS: {project}")
    print(f"  Satz-/Visual-Items: {len(items)}")
    print(f"  referenzierte Bilder: {len(sentence_image_ids)}")
    return scene_image_ids


def validate_reference_policy(project: Path) -> None:
    repo_root = Path(__file__).resolve().parents[1]
    channel_config_path = repo_root / "config" / "channel.json"
    require_file(channel_config_path)
    config = load_json(channel_config_path)
    visual = config.get("visual_identity", {})
    flow = config.get("flow_prompting", {})

    if flow.get("textual_reference_mentions_do_not_count_as_attachment") is not True:
        fail("config/channel.json muss textliche Referenz-Erwaehnungen als unzureichend markieren")
    if flow.get("attach_bild_01_on_every_followup") is not True:
        fail("config/channel.json muss Bild_01 als echte Referenz fuer Folgebilder verlangen")
    if config.get("labels", {}).get("render_in_flow") is not False:
        fail("Flow-Labels muessen deaktiviert sein; Labels werden in Remotion gerendert")

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
        "overall_score",
    )

    for entry in entries:
        if not isinstance(entry, dict):
            fail("image-review.json enthaelt ungueltigen Eintrag")
        image_id = entry.get("image_asset_id")
        if image_id not in expected_image_ids:
            fail(f"Bildreview referenziert unbekanntes Bild: {image_id}")
        reviewed.add(image_id)

        image_path = images_dir / f"{image_id}.png"
        require_file(image_path)

        if entry.get("decision") != "ACCEPT":
            fail(f"{image_id}: Bild ist nicht ACCEPT")
        if entry.get("ai_artifact_check") != "PASS":
            fail(f"{image_id}: AI-Artefakt-Check nicht bestanden")

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

    extra_pngs = {path.stem for path in images_dir.glob("Bild_*.png")} - expected_image_ids
    if extra_pngs:
        fail(f"unerwartete finale Bilddateien: {sorted(extra_pngs)}")

    print(f"V2-PHASE-2-REVIEW-PASS: {project}")
    print(f"  akzeptierte Bildreviews: {len(reviewed)}")
    print("  finale PNG-Dateien vorhanden und Review-Felder >= 8/10")


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
