#!/usr/bin/env python3
"""Validate Object-Talk V2 planning files without changing legacy projects.

Usage:
  python tools/validate_planning_v2.py youtube-videos/MEIN-VIDEO
  python tools/validate_planning_v2.py youtube-videos/MEIN-VIDEO --phase2

This validator is intentionally standalone so Video 001 and the existing Phase-3
pipeline remain compatible. New V2 projects should pass it before moving on.
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


def validate_phase2(project: Path, expected_image_ids: set[str]) -> None:
    review_path = project / "02_bildprompts" / "image-review.json"
    require_file(review_path)
    review = load_json(review_path)
    if str(review.get("status", "")).upper() == "TEMPLATE":
        fail("image-review.json steht noch auf TEMPLATE")
    entries = review.get("images")
    if not isinstance(entries, list) or not entries:
        fail("image-review.json enthaelt keine Bildreviews")

    reviewed: set[str] = set()
    for entry in entries:
        if not isinstance(entry, dict):
            fail("image-review.json enthaelt ungueltigen Eintrag")
        image_id = entry.get("image_asset_id")
        if image_id not in expected_image_ids:
            fail(f"Bildreview referenziert unbekanntes Bild: {image_id}")
        reviewed.add(image_id)
        if entry.get("decision") != "ACCEPT":
            fail(f"{image_id}: Bild ist nicht ACCEPT")
        score = entry.get("overall_score")
        if not isinstance(score, (int, float)) or score < 8.0:
            fail(f"{image_id}: overall_score muss mindestens 8.0 sein")
        if entry.get("ai_artifact_check") != "PASS":
            fail(f"{image_id}: AI-Artefakt-Check nicht bestanden")
        scientific = entry.get("scientific_accuracy")
        if not isinstance(scientific, (int, float)) or scientific < 8.0:
            fail(f"{image_id}: scientific_accuracy muss mindestens 8.0 sein")

    missing = expected_image_ids - reviewed
    if missing:
        fail(f"Bildreviews fehlen fuer: {sorted(missing)}")

    print(f"V2-PHASE-2-REVIEW-PASS: {project}")
    print(f"  akzeptierte Bildreviews: {len(reviewed)}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("project", help="Pfad zum Video-Projekt")
    parser.add_argument("--phase2", action="store_true", help="zusaetzlich finale Bildreviews pruefen")
    args = parser.parse_args()

    project = Path(args.project).resolve()
    if not project.is_dir():
        fail(f"Projektordner nicht gefunden: {project}")

    expected = validate_phase1(project)
    if args.phase2:
        validate_phase2(project, expected)


if __name__ == "__main__":
    main()
