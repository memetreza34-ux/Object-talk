#!/usr/bin/env python3
"""Create the canonical final voiceover used for Whisper and rendering.

Requirements: ffmpeg and ffprobe in PATH.

Usage:
python tools/prepare_audio.py RAW_AUDIO FINAL_WAV

The script does NOT change speed and does NOT remove internal pauses. It only
converts the file to a consistent 48 kHz WAV and applies controlled loudness
normalization for the production pipeline.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from pathlib import Path

TARGET_LUFS = -16
TARGET_TRUE_PEAK = -1.0
SAMPLE_RATE = 48000
MIN_DURATION = 300.0


def require_binary(name: str) -> str:
    path = shutil.which(name)
    if not path:
        raise SystemExit(f"FEHLER: {name} wurde nicht in PATH gefunden.")
    return path


def probe_duration(ffprobe: str, path: Path) -> float:
    result = subprocess.run(
        [
            ffprobe,
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "json",
            str(path),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    payload = json.loads(result.stdout)
    return float(payload["format"]["duration"])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path, help="Rohes Voiceover aus der Voice-KI")
    parser.add_argument("output", type=Path, help="Ziel: final-voiceover.wav")
    args = parser.parse_args()

    if not args.input.is_file():
        raise SystemExit(f"FEHLER: Eingabe fehlt: {args.input}")

    ffmpeg = require_binary("ffmpeg")
    ffprobe = require_binary("ffprobe")
    args.output.parent.mkdir(parents=True, exist_ok=True)

    command = [
        ffmpeg,
        "-y",
        "-i",
        str(args.input),
        "-vn",
        "-af",
        f"loudnorm=I={TARGET_LUFS}:TP={TARGET_TRUE_PEAK}:LRA=7",
        "-ar",
        str(SAMPLE_RATE),
        "-acodec",
        "pcm_s16le",
        str(args.output),
    ]

    process = subprocess.run(command)
    if process.returncode != 0:
        raise SystemExit("FEHLER: ffmpeg Audioaufbereitung fehlgeschlagen.")

    duration = probe_duration(ffprobe, args.output)
    if duration < MIN_DURATION:
        args.output.unlink(missing_ok=True)
        raise SystemExit(
            f"PHASE-2 FAIL: finales Voiceover ist nur {duration:.2f}s lang; "
            f"mindestens {MIN_DURATION:.0f}s erforderlich. Script sinnvoll erweitern und Audio neu erzeugen."
        )

    report = {
        "input": args.input.name,
        "output": args.output.name,
        "duration_seconds": round(duration, 3),
        "sample_rate_hz": SAMPLE_RATE,
        "target_integrated_lufs": TARGET_LUFS,
        "target_true_peak_db": TARGET_TRUE_PEAK,
        "speed_multiplier": 1.0,
        "internal_silence_compression": False,
    }
    report_path = args.output.with_suffix(".audio-report.json")
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    print(f"OK: {args.output}")
    print(f"OK: {report_path}")
    print(f"Dauer: {duration:.2f}s")


if __name__ == "__main__":
    main()
