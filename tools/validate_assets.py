#!/usr/bin/env python3
"""Prüft nummerierte Bilder gegen scene-map.json vor dem Render."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image

ALLOWED_EXTENSIONS = (".png", ".jpg", ".jpeg", ".webp")


def find_image(images_dir: Path, base_name: str) -> list[Path]:
    matches = []
    for ext in ALLOWED_EXTENSIONS:
        candidate = images_dir / f"{base_name}{ext}"
        if candidate.exists():
            matches.append(candidate)
    return matches


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("scene_map", type=Path)
    parser.add_argument("images_dir", type=Path)
    args = parser.parse_args()

    data = json.loads(args.scene_map.read_text(encoding="utf-8"))
    scenes = data.get("scenes", data if isinstance(data, list) else [])

    if not scenes:
        raise SystemExit("FEHLER: Keine Szenen in scene-map.json gefunden.")
    if not args.images_dir.exists():
        raise SystemExit(f"FEHLER: Bilderordner fehlt: {args.images_dir}")

    errors = []
    warnings = []

    expected_numbers = list(range(1, len(scenes) + 1))
    actual_numbers = [int(scene["scene"]) for scene in scenes]
    if actual_numbers != expected_numbers:
        errors.append(
            f"Szenennummern nicht lückenlos: erwartet {expected_numbers}, gefunden {actual_numbers}"
        )

    for scene in scenes:
        number = int(scene["scene"])
        expected_image = f"Bild_{number:02d}"
        declared_image = scene.get("image", "")

        if declared_image != expected_image:
            errors.append(
                f"Szene {number}: image muss {expected_image!r} sein, ist aber {declared_image!r}."
            )

        matches = find_image(args.images_dir, expected_image)
        if not matches:
            errors.append(f"Szene {number}: {expected_image} fehlt.")
            continue
        if len(matches) > 1:
            errors.append(
                f"Szene {number}: mehrere Dateien für {expected_image}: "
                + ", ".join(p.name for p in matches)
            )
            continue

        path = matches[0]
        try:
            with Image.open(path) as img:
                width, height = img.size
        except Exception as exc:
            errors.append(f"{path.name}: Bild kann nicht gelesen werden: {exc}")
            continue

        if width < 1280 or height < 720:
            errors.append(
                f"{path.name}: Auflösung zu klein ({width}x{height}); mindestens 1280x720."
            )

        aspect = width / height
        target = 16 / 9
        if abs(aspect - target) > 0.03:
            errors.append(
                f"{path.name}: falsches Seitenverhältnis ({width}x{height}); erwartet ungefähr 16:9."
            )

        if width < 1920 or height < 1080:
            warnings.append(
                f"{path.name}: unter Zielauflösung 1920x1080 ({width}x{height})."
            )

    print(f"Geprüfte Szenen: {len(scenes)}")

    if warnings:
        print("\nWARNUNGEN:")
        for warning in warnings:
            print(f"- {warning}")

    if errors:
        print("\nFEHLER:")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    print("\nOK: Alle benötigten Bilder sind vorhanden und technisch verwendbar.")


if __name__ == "__main__":
    main()
