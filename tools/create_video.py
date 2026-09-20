#!/usr/bin/env python3
"""Create a new YouTube project by copying youtube-videos/_TEMPLATE.

Usage:
python tools/create_video.py "was-passiert-mit-zucker-im-koerper"
"""

from __future__ import annotations

import argparse
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

    shutil.copytree(template, target)
    print(f"OK: neues Projekt erstellt: {target}")


if __name__ == "__main__":
    main()
