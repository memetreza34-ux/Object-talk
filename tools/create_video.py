#!/usr/bin/env python3
"""Create a new YouTube project by copying youtube-videos/_TEMPLATE.

Usage:
python tools/create_video.py "was-passiert-mit-zucker-im-koerper"
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path


def slugify(value: str) -> str:
    replacements = {"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss"}
    value = value.strip().lower()
    for source, target in replacements.items():
        value = value.replace(source, target)
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("topic", help="Thema oder gewuenschter Ordner-Slug")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    template = repo_root / "youtube-videos" / "_TEMPLATE"
    slug = slugify(args.topic)
    if not slug:
        raise SystemExit("FEHLER: ungueltiger Themenname.")

    target = repo_root / "youtube-videos" / slug
    if not template.is_dir():
        raise SystemExit(f"FEHLER: Template fehlt: {template}")
    if target.exists():
        raise SystemExit(f"FEHLER: Projekt existiert bereits: {target}")

    # Seed the next production with permanent lessons AND the last verified video.
    # Never mark them applied before the script, image plan and prompt were checked.
    ledger_path = repo_root / "engine" / "IMPROVEMENT-LEDGER.json"
    ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
    lesson_items = ledger.get("permanent_lessons", []) + ledger.get("next_video_lessons", [])
    if not lesson_items:
        raise SystemExit("FEHLER: keine Verbesserungsregeln im zentralen Ledger.")
    if len({item["id"] for item in lesson_items}) != len(lesson_items):
        raise SystemExit("FEHLER: doppelte Lesson-ID im zentralen Ledger.")
    shutil.copytree(template, target)
    manifest_path = target / ".intern" / "05_info" / "improvement-applied.json"
    if not manifest_path.is_file():
        raise SystemExit("FEHLER: Template ohne Improvement-Nachweis, Projekt nicht Phase-1-fertig.")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["status"] = "PENDING"
    manifest["source_review_video"] = ledger.get("latest_reviewed_video")
    manifest["lessons"] = [
        {"id": item["id"], "implemented_as": "", "evidence_files": [], "verification": ""}
        for item in lesson_items
    ]
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"OK: neues Projekt erstellt: {target}")
    print(f"VERBESSERUNGS-PFLICHT: {len(lesson_items)} aktive Lessons vor Phase 1 nachweisbar anwenden.")


if __name__ == "__main__":
    main()
