#!/usr/bin/env python3
"""Safely import numbered Google Flow images from a ZIP into a canonical folder.

Images are assigned ONLY by their explicit scene/image number in the filename,
never by ZIP order.

Final Flow ZIPs are strict: every image file must map to exactly one expected
Bild_XX number. Extra cover variants, rejected attempts, v2/copy files or
unnumbered image files make the import FAIL instead of being silently ignored.

Usage:
python tools/import_flow_zip.py SCENE_MAP FLOW_ZIP OUTPUT_IMAGES_DIR
"""

from __future__ import annotations

import argparse
import io
import json
import re
import shutil
import zipfile
from pathlib import Path

from PIL import Image

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}
NUMBER_PATTERNS = [
    re.compile(r"(?i)bild[_\-\s]*0*(\d+)"),
    re.compile(r"(?i)image[_\-\s]*0*(\d+)"),
    re.compile(r"(?i)scene[_\-\s]*0*(\d+)"),
    re.compile(r"(?i)szene[_\-\s]*0*(\d+)"),
]


def detect_number(filename: str) -> int | None:
    stem = Path(filename).stem
    for pattern in NUMBER_PATTERNS:
        match = pattern.search(stem)
        if match:
            return int(match.group(1))
    return None


def safe_member_name(name: str) -> bool:
    path = Path(name)
    return not path.is_absolute() and ".." not in path.parts


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("scene_map", type=Path)
    parser.add_argument("zip_file", type=Path)
    parser.add_argument("output_dir", type=Path)
    args = parser.parse_args()

    if not args.scene_map.is_file():
        raise SystemExit(f"FEHLER: scene-map fehlt: {args.scene_map}")
    if not args.zip_file.is_file():
        raise SystemExit(f"FEHLER: ZIP fehlt: {args.zip_file}")

    data = json.loads(args.scene_map.read_text(encoding="utf-8"))
    scenes = data.get("scenes", data if isinstance(data, list) else [])
    expected = {int(scene["scene"]) for scene in scenes}
    if expected != set(range(1, len(scenes) + 1)):
        raise SystemExit("FEHLER: scene-map besitzt keine lueckenlosen Szenennummern.")

    found: dict[int, tuple[str, bytes]] = {}
    ignored_non_images: list[str] = []
    unexpected_images: list[str] = []

    with zipfile.ZipFile(args.zip_file, "r") as archive:
        for member in archive.infolist():
            if member.is_dir():
                continue
            if not safe_member_name(member.filename):
                raise SystemExit(f"FEHLER: unsicherer ZIP-Pfad: {member.filename}")

            suffix = Path(member.filename).suffix.lower()
            if suffix not in IMAGE_EXTENSIONS:
                ignored_non_images.append(member.filename)
                continue

            number = detect_number(Path(member.filename).name)
            if number is None or number not in expected:
                unexpected_images.append(member.filename)
                continue

            if number in found:
                raise SystemExit(
                    f"PHASE-2 FAIL: mehrere ZIP-Dateien behaupten Bild_{number:02d} zu sein: "
                    f"{found[number][0]!r} und {member.filename!r}. "
                    "Nur eine finale Version pro Bildnummer ist erlaubt; Cover-Alternativen und FAIL-Versionen vor ZIP loeschen."
                )

            found[number] = (member.filename, archive.read(member))

    if unexpected_images:
        listing = "\n- ".join(unexpected_images)
        raise SystemExit(
            "PHASE-2 FAIL: ZIP enthaelt zusaetzliche/unnumerierte Bilddateien. "
            "Finale ZIP darf nur die erwarteten Bild_XX-Dateien enthalten.\n- " + listing
        )

    missing = sorted(expected - set(found))
    if missing:
        formatted = ", ".join(f"Bild_{number:02d}" for number in missing)
        raise SystemExit(f"PHASE-2 FAIL: folgende Bilder fehlen in der ZIP: {formatted}")

    if len(found) != len(expected):
        raise SystemExit(
            f"PHASE-2 FAIL: erwartet {len(expected)} eindeutige Bilder, gefunden {len(found)}."
        )

    if args.output_dir.exists():
        shutil.rmtree(args.output_dir)
    args.output_dir.mkdir(parents=True, exist_ok=True)

    imported: list[dict] = []
    for number in sorted(found):
        source_name, raw = found[number]
        target = args.output_dir / f"Bild_{number:02d}.png"
        try:
            with Image.open(io.BytesIO(raw)) as image:
                image = image.convert("RGB")
                image.save(target, format="PNG", optimize=True)
                width, height = image.size
        except Exception as exc:
            raise SystemExit(f"FEHLER: {source_name} ist kein lesbares Bild: {exc}") from exc

        imported.append(
            {
                "scene": number,
                "source": source_name,
                "target": target.name,
                "width": width,
                "height": height,
            }
        )

    report = {
        "source_zip": args.zip_file.name,
        "expected_count": len(expected),
        "imported_count": len(imported),
        "images": imported,
        "ignored_non_image_files": ignored_non_images,
        "unexpected_image_files": unexpected_images,
        "assignment_rule": "explicit-number-only-never-zip-order",
        "final_zip_policy": "exactly-one-image-per-expected-number-no-extra-images",
    }
    report_path = args.output_dir.parent / "flow-import-report.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"OK: {len(imported)} eindeutige Bilder nach {args.output_dir} importiert.")
    print(f"OK: {report_path}")


if __name__ == "__main__":
    main()
