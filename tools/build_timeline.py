#!/usr/bin/env python3
"""Build an exact scene timeline from strict script word timings.

Usage:
python tools/build_timeline.py \
  youtube-videos/THEMA/03_pipeline/scene-map.json \
  youtube-videos/THEMA/03_pipeline/timing/word-timings.json \
  youtube-videos/THEMA/03_pipeline/timing/timeline.json

Every scene must contain the exact spoken `speech_section` from script.txt.
The program maps those sections sequentially to the aligned script words and FAILS
on any gap, overlap, mismatch, ambiguous creative fallback, or scene that is too
long for the channel's visual-density standard.

Default pacing rule:
- no normal scene may remain on one image for more than 7.0 seconds
- if a spoken section is longer, split it into additional UNIQUE scenes/images
- never solve a long section by duplicating the same image asset
"""

from __future__ import annotations

import argparse
import json
import unicodedata
from pathlib import Path

DEFAULT_MAX_SCENE_SECONDS = 7.0


def normalize_token(value: str) -> str:
    value = unicodedata.normalize("NFKC", str(value)).lower().replace("ß", "ss")
    return "".join(ch for ch in value if ch.isalnum())


def normalized_tokens(text: str) -> list[str]:
    return [
        token
        for token in (normalize_token(raw) for raw in str(text).strip().split())
        if token
    ]


def prefix_matches(section: list[str], anchor: list[str]) -> bool:
    return bool(anchor) and len(anchor) <= len(section) and section[: len(anchor)] == anchor


def suffix_matches(section: list[str], anchor: list[str]) -> bool:
    return bool(anchor) and len(anchor) <= len(section) and section[-len(anchor) :] == anchor


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("scene_map", type=Path)
    parser.add_argument("word_timings", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument(
        "--max-scene-seconds",
        type=float,
        default=DEFAULT_MAX_SCENE_SECONDS,
        help=(
            "Maximale Dauer eines einzelnen Bildes. Standard: 7.0s. "
            "Laengere Sprachabschnitte muessen in neue eindeutige Bilder geteilt werden."
        ),
    )
    args = parser.parse_args()

    if args.max_scene_seconds <= 0:
        raise SystemExit("--max-scene-seconds muss groesser als 0 sein.")
    if not args.scene_map.is_file():
        raise SystemExit(f"scene-map.json fehlt: {args.scene_map}")
    if not args.word_timings.is_file():
        raise SystemExit(f"word-timings.json fehlt: {args.word_timings}")

    scene_data = json.loads(args.scene_map.read_text(encoding="utf-8"))
    scenes = scene_data.get("scenes", scene_data if isinstance(scene_data, list) else [])
    timing_data = json.loads(args.word_timings.read_text(encoding="utf-8"))
    words = timing_data.get("words", [])
    audio_duration = float(timing_data.get("duration", 0))

    if not scenes:
        raise SystemExit("scene-map.json enthaelt keine Szenen.")
    if not words:
        raise SystemExit("word-timings.json enthaelt keine Woerter.")
    if audio_duration <= 0:
        raise SystemExit("word-timings.json enthaelt keine gueltige Audiodauer.")

    expected_scene_numbers = list(range(1, len(scenes) + 1))
    actual_scene_numbers = [int(scene.get("scene", -1)) for scene in scenes]
    if actual_scene_numbers != expected_scene_numbers:
        raise SystemExit(
            f"Szenennummern muessen lueckenlos sein: erwartet {expected_scene_numbers}, "
            f"gefunden {actual_scene_numbers}"
        )

    timing_tokens = [normalize_token(word.get("text", "")) for word in words]
    if any(not token for token in timing_tokens):
        raise SystemExit("word-timings.json enthaelt ein nicht normalisierbares Wort.")

    resolved: list[dict] = []
    cursor = 0

    for index, scene in enumerate(scenes):
        scene_number = int(scene["scene"])
        expected_image = f"Bild_{scene_number:02d}"
        if scene.get("image") != expected_image:
            raise SystemExit(
                f"Szene {scene_number}: image muss {expected_image!r} sein, "
                f"ist aber {scene.get('image')!r}."
            )

        speech_section = str(scene.get("speech_section", "")).strip()
        section_tokens = normalized_tokens(speech_section)
        if not section_tokens:
            raise SystemExit(f"Szene {scene_number}: speech_section fehlt oder ist leer.")

        end_cursor = cursor + len(section_tokens)
        if end_cursor > len(words):
            raise SystemExit(
                f"Szene {scene_number}: speech_section reicht ueber das Ende des Audioscripts hinaus."
            )

        actual_tokens = timing_tokens[cursor:end_cursor]
        if actual_tokens != section_tokens:
            expected_preview = " ".join(section_tokens[:12])
            actual_preview = " ".join(actual_tokens[:12])
            raise SystemExit(
                f"Szene {scene_number}: speech_section stimmt nicht exakt mit dem naechsten "
                f"Scriptabschnitt ueberein. Erwartet: {expected_preview!r} | "
                f"Timing: {actual_preview!r}. Keine Position wurde geraten."
            )

        start_anchor = str(scene.get("start_anchor", "")).strip()
        end_anchor = str(scene.get("end_anchor", "")).strip()
        start_anchor_tokens = normalized_tokens(start_anchor)
        end_anchor_tokens = normalized_tokens(end_anchor)

        if start_anchor_tokens and not prefix_matches(section_tokens, start_anchor_tokens):
            raise SystemExit(
                f"Szene {scene_number}: start_anchor ist kein exakter Anfang von speech_section."
            )
        if end_anchor_tokens and not suffix_matches(section_tokens, end_anchor_tokens):
            raise SystemExit(
                f"Szene {scene_number}: end_anchor ist kein exaktes Ende von speech_section."
            )

        start_time = 0.0 if index == 0 else float(words[cursor]["start"])
        last_spoken_end = float(words[end_cursor - 1]["end"])

        resolved.append(
            {
                "scene": scene_number,
                "image": expected_image,
                "description": scene.get("description", ""),
                "visual_task": scene.get("visual_task", ""),
                "motion": scene.get("motion", "slow-push-in"),
                "speech_section": speech_section,
                "start_anchor": start_anchor,
                "end_anchor": end_anchor,
                "start_word_index": cursor,
                "end_word_index": end_cursor - 1,
                "start": round(start_time, 3),
                "last_spoken_end": round(last_spoken_end, 3),
            }
        )
        cursor = end_cursor

    if cursor != len(words):
        remaining = " ".join(word["text"] for word in words[cursor : cursor + 16])
        raise SystemExit(
            "Die Szenen decken das finale Script nicht vollstaendig ab. "
            f"Erstes nicht zugeordnetes Material: {remaining!r}"
        )

    overlong: list[dict] = []
    for index, scene in enumerate(resolved):
        if index + 1 < len(resolved):
            scene["end"] = resolved[index + 1]["start"]
        else:
            scene["end"] = round(audio_duration, 3)

        scene["duration"] = round(scene["end"] - scene["start"], 3)
        if scene["duration"] <= 0:
            raise SystemExit(
                f"Szene {scene['scene']}: ungueltige Dauer {scene['duration']} Sekunden."
            )
        if scene["duration"] > args.max_scene_seconds:
            overlong.append(scene)

    if overlong:
        details = "\n".join(
            f"- Szene {scene['scene']} / {scene['image']}: {scene['duration']:.2f}s"
            for scene in overlong
        )
        raise SystemExit(
            "TIMELINE FAIL: Einzelne Bilder stehen zu lange. Das erzeugt Diashow-Gefuehl.\n"
            f"Maximal erlaubt: {args.max_scene_seconds:.2f}s pro Bild.\n"
            f"{details}\n"
            "Loesung: den jeweiligen speech_section semantisch teilen und fuer jeden Teil ein "
            "NEUES eindeutiges Bild mit neuer fortlaufender Bildnummer planen. Nie dasselbe Bild "
            "duplizieren oder zweimal verwenden."
        )

    result = {
        "source_scene_map": args.scene_map.name,
        "source_word_timings": args.word_timings.name,
        "script_sha256": timing_data.get("script_sha256"),
        "audio_duration": round(audio_duration, 3),
        "fps": 30,
        "scene_count": len(resolved),
        "mapping": "strict-sequential-speech-section",
        "max_scene_seconds": args.max_scene_seconds,
        "visual_density_policy": "split-long-sections-into-unique-images",
        "scenes": resolved,
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"OK: {args.output}")
    print(f"Szenen: {len(resolved)}")
    print(f"Audio: {audio_duration:.2f} Sekunden")
    print(f"Maximale Bilddauer: {args.max_scene_seconds:.2f}s")


if __name__ == "__main__":
    main()
