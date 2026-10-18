#!/usr/bin/env python3
"""Validate semantic scene planning against the final spoken script.

Usage:
python tools/validate_phase1.py SCRIPT PHASE1_SCENES SCENE_MAP

The validator requires complete, sequential, gap-free coverage of script.txt and
ensures that the technical scene-map did not silently change Phase-1 decisions.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from text_normalize import normalize_token  # same canonical form as transcribe_audio.py

ALLOWED_MOTIONS = {
    "static",
    "slow-push-in",
    "slow-pull-out",
    "pan-left",
    "pan-right",
}


def tokens(text: str) -> list[str]:
    return [token for token in (normalize_token(x) for x in str(text).split()) if token]


def load_scenes(path: Path) -> list[dict]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    scenes = payload.get("scenes", payload if isinstance(payload, list) else [])
    if not scenes:
        raise SystemExit(f"PHASE-1 FAIL: keine Szenen in {path}")
    return scenes


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("script", type=Path)
    parser.add_argument("phase1_scenes", type=Path)
    parser.add_argument("scene_map", type=Path)
    args = parser.parse_args()

    for path in (args.script, args.phase1_scenes, args.scene_map):
        if not path.is_file():
            raise SystemExit(f"PHASE-1 FAIL: Datei fehlt: {path}")

    script_text = args.script.read_text(encoding="utf-8").strip()
    script_tokens = tokens(script_text)
    if not script_tokens:
        raise SystemExit("PHASE-1 FAIL: script.txt ist leer.")

    phase_scenes = load_scenes(args.phase1_scenes)
    map_scenes = load_scenes(args.scene_map)

    if len(phase_scenes) != len(map_scenes):
        raise SystemExit(
            f"PHASE-1 FAIL: Phase-1 hat {len(phase_scenes)} Szenen, scene-map aber {len(map_scenes)}."
        )

    cursor = 0
    errors: list[str] = []

    for index, (phase, mapped) in enumerate(zip(phase_scenes, map_scenes), start=1):
        expected_image = f"Bild_{index:02d}"
        if int(phase.get("scene", -1)) != index or int(mapped.get("scene", -1)) != index:
            errors.append(f"Szene {index}: Szenennummer stimmt nicht.")
        if phase.get("image") != expected_image or mapped.get("image") != expected_image:
            errors.append(f"Szene {index}: Bild muss {expected_image} sein.")

        phase_text = str(phase.get("speech_section", "")).strip()
        mapped_text = str(mapped.get("speech_section", "")).strip()
        phase_tokens = tokens(phase_text)
        mapped_tokens = tokens(mapped_text)
        if not phase_tokens:
            errors.append(f"Szene {index}: speech_section fehlt.")
            continue
        if phase_tokens != mapped_tokens:
            errors.append(f"Szene {index}: scene-map veraendert die Phase-1 speech_section.")

        expected_slice = script_tokens[cursor : cursor + len(phase_tokens)]
        if phase_tokens != expected_slice:
            errors.append(
                f"Szene {index}: speech_section beginnt nicht exakt am naechsten Scriptwort."
            )
        cursor += len(phase_tokens)

        if str(phase.get("visual_task", "")).strip() != str(mapped.get("visual_task", "")).strip():
            errors.append(f"Szene {index}: visual_task wurde zwischen Phase 1 und scene-map veraendert.")

        motion = str(mapped.get("motion", phase.get("motion", "slow-push-in")))
        if motion not in ALLOWED_MOTIONS:
            errors.append(f"Szene {index}: unbekannte Bewegung {motion!r}.")

    if cursor != len(script_tokens):
        errors.append(
            f"Szenen decken {cursor} von {len(script_tokens)} Scriptwoertern ab; Vollabdeckung fehlt."
        )

    if errors:
        print("PHASE-1 FAIL")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    print("PHASE-1 PASS")
    print(f"Scriptwoerter: {len(script_tokens)}")
    print(f"Szenen: {len(phase_scenes)}")
    print("Vollstaendige lueckenlose Sprachabdeckung bestaetigt.")


if __name__ == "__main__":
    main()
