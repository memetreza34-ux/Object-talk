#!/usr/bin/env python3
"""Export human-readable timed script and YouTube SRT from final timeline.json.

Usage:
  python tools/export_subtitles.py youtube-videos/VIDEO

Required input:
  03_pipeline/timing/timeline.json

Outputs:
  04_export/UNTERTITEL-MIT-ZEITEN.txt
  04_export/UNTERTITEL-YOUTUBE.srt

The timeline is the only timing authority. No timestamps are guessed.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def format_clock(seconds: float, milliseconds: bool = False) -> str:
    total_ms = max(0, int(round(float(seconds) * 1000)))
    hours, rem = divmod(total_ms, 3_600_000)
    minutes, rem = divmod(rem, 60_000)
    secs, ms = divmod(rem, 1000)
    if milliseconds:
        return f"{hours:02d}:{minutes:02d}:{secs:02d},{ms:03d}"
    if hours:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    return f"{minutes:02d}:{secs:02d}"


def clean_text(value: object) -> str:
    return " ".join(str(value or "").split())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("project", type=Path, help="Video project folder")
    args = parser.parse_args()

    project = args.project
    timeline_path = project / "03_pipeline" / "timing" / "timeline.json"
    export_dir = project / "04_export"

    if not timeline_path.is_file():
        raise SystemExit(
            f"FEHLER: finale timeline.json fehlt: {timeline_path}\n"
            "Untertitel duerfen nicht mit geschaetzten Zeitcodes erzeugt werden."
        )

    payload = json.loads(timeline_path.read_text(encoding="utf-8"))
    scenes = payload.get("scenes", [])
    if not isinstance(scenes, list) or not scenes:
        raise SystemExit("FEHLER: timeline.json enthaelt keine Szenen.")

    export_dir.mkdir(parents=True, exist_ok=True)

    readable_lines = [
        "KOMPLETTES SCRIPT MIT ZEITABSCHNITTEN",
        "",
        "Quelle: finale timeline.json / finales Voiceover",
        "Zeitcodes sind nicht geschaetzt.",
        "",
    ]
    srt_blocks: list[str] = []

    previous_end = 0.0
    for index, scene in enumerate(scenes, start=1):
        try:
            start = float(scene["start"])
            end = float(scene["end"])
        except (KeyError, TypeError, ValueError):
            raise SystemExit(f"FEHLER: Szene {index} hat ungueltige Start-/Endzeit.")

        text = clean_text(scene.get("speech_section"))
        if not text:
            raise SystemExit(f"FEHLER: Szene {index} hat keinen speech_section.")
        if start < 0 or end <= start:
            raise SystemExit(f"FEHLER: Szene {index} hat ungueltiges Zeitfenster {start}-{end}.")
        if index > 1 and start < previous_end - 0.02:
            raise SystemExit(f"FEHLER: Untertitel-Zeitfenster ueberlappen bei Szene {index}.")

        readable_lines.append(f"{format_clock(start)}–{format_clock(end)}  {text}")
        srt_blocks.append(
            f"{index}\n"
            f"{format_clock(start, milliseconds=True)} --> {format_clock(end, milliseconds=True)}\n"
            f"{text}\n"
        )
        previous_end = end

    readable_path = export_dir / "UNTERTITEL-MIT-ZEITEN.txt"
    srt_path = export_dir / "UNTERTITEL-YOUTUBE.srt"

    readable_path.write_text("\n\n".join(readable_lines) + "\n", encoding="utf-8")
    srt_path.write_text("\n".join(srt_blocks), encoding="utf-8")

    print(f"OK: {readable_path}")
    print(f"OK: {srt_path}")
    print(f"Untertitelabschnitte: {len(scenes)}")


if __name__ == "__main__":
    main()
