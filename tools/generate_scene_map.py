#!/usr/bin/env python3
"""Generate scene-map.json deterministically from Phase-1 semantic scenes.

Usage:
python tools/generate_scene_map.py PHASE1_SCENES OUTPUT

No creative decisions are made here. The tool copies scene boundaries, speech,
visual tasks, labels and motion from Phase 1 and derives exact prefix/suffix
anchors from the spoken section.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("phase1_scenes", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--anchor-words", type=int, default=8)
    args = parser.parse_args()

    if not args.phase1_scenes.is_file():
        raise SystemExit(f"PHASE-1 FAIL: Datei fehlt: {args.phase1_scenes}")

    payload = json.loads(args.phase1_scenes.read_text(encoding="utf-8"))
    scenes = payload.get("scenes", [])
    if not scenes:
        raise SystemExit("PHASE-1 FAIL: phase1-scenes.json enthält keine Szenen.")

    out_scenes = []
    for index, scene in enumerate(scenes, start=1):
        expected_image = f"Bild_{index:02d}"
        if int(scene.get("scene", -1)) != index:
            raise SystemExit(f"PHASE-1 FAIL: Szene {index} hat falsche Szenennummer.")
        if scene.get("image") != expected_image:
            raise SystemExit(
                f"PHASE-1 FAIL: Szene {index} muss image={expected_image!r} besitzen."
            )

        speech = str(scene.get("speech_section", "")).strip()
        words = speech.split()
        if not words:
            raise SystemExit(f"PHASE-1 FAIL: Szene {index} hat keine speech_section.")

        n = max(3, min(args.anchor_words, len(words)))
        out_scenes.append(
            {
                "scene": index,
                "image": expected_image,
                "start_anchor": " ".join(words[:n]),
                "end_anchor": " ".join(words[-n:]),
                "speech_section": speech,
                "visual_task": scene.get("visual_task", ""),
                "description": scene.get("visual_task", ""),
                "motion": scene.get("motion", "slow-push-in"),
                "labels": scene.get("labels", []),
            }
        )

    result = {
        "video_id": payload.get("video_id"),
        "title": payload.get("title"),
        "generated_from": args.phase1_scenes.name,
        "mapping": "deterministic-copy-of-phase1",
        "scenes": out_scenes,
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"OK: {args.output}")
    print(f"Szenen: {len(out_scenes)}")


if __name__ == "__main__":
    main()
