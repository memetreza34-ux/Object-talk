#!/usr/bin/env python3
"""Create the canonical final voiceover used for Whisper and rendering.

Requirements: ffmpeg and ffprobe in PATH.

Usage:
python tools/prepare_audio.py RAW_AUDIO FINAL_WAV
python tools/prepare_audio.py RAW_AUDIO FINAL_WAV --speed 1.10 --min-seconds 100

Production defaults intentionally make the narration tighter:
- playback speed: 1.10x
- long internal pauses are compressed, not allowed to remain as dead air
- short natural micro-pauses are preserved
- controlled loudness normalization is applied last

The processed WAV is the ONLY voice file that Whisper, timeline building and
Remotion may use. Never build timings from the raw TTS file and then render a
separately sped-up version.
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
DEFAULT_SPEED = 1.10
DEFAULT_SILENCE_THRESHOLD_DB = -35.0
DEFAULT_LONG_PAUSE_SECONDS = 0.45
DEFAULT_KEEP_PAUSE_SECONDS = 0.12


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
    parser.add_argument(
        "--speed",
        type=float,
        default=DEFAULT_SPEED,
        help="Narrationsgeschwindigkeit. Produktionsstandard: 1.10.",
    )
    parser.add_argument(
        "--silence-threshold-db",
        type=float,
        default=DEFAULT_SILENCE_THRESHOLD_DB,
        help="Schwellwert fuer stille Abschnitte in dB. Standard: -35.",
    )
    parser.add_argument(
        "--long-pause-seconds",
        type=float,
        default=DEFAULT_LONG_PAUSE_SECONDS,
        help="Pausen ab dieser Dauer werden komprimiert. Standard: 0.45s.",
    )
    parser.add_argument(
        "--keep-pause-seconds",
        type=float,
        default=DEFAULT_KEEP_PAUSE_SECONDS,
        help="Restpause nach Kompression. Standard: 0.12s.",
    )
    parser.add_argument(
        "--min-seconds",
        type=float,
        default=0.0,
        help="Optionale projektspezifische Mindestdauer nach Verarbeitung.",
    )
    args = parser.parse_args()

    if not args.input.is_file():
        raise SystemExit(f"FEHLER: Eingabe fehlt: {args.input}")
    if not 0.5 <= args.speed <= 2.0:
        raise SystemExit("FEHLER: --speed muss zwischen 0.5 und 2.0 liegen.")
    if args.long_pause_seconds <= 0:
        raise SystemExit("FEHLER: --long-pause-seconds muss groesser als 0 sein.")
    if not 0 <= args.keep_pause_seconds < args.long_pause_seconds:
        raise SystemExit(
            "FEHLER: --keep-pause-seconds muss >= 0 und kleiner als --long-pause-seconds sein."
        )
    if args.min_seconds < 0:
        raise SystemExit("FEHLER: --min-seconds darf nicht negativ sein.")

    ffmpeg = require_binary("ffmpeg")
    ffprobe = require_binary("ffprobe")
    args.output.parent.mkdir(parents=True, exist_ok=True)

    raw_duration = probe_duration(ffprobe, args.input)
    threshold = f"{args.silence_threshold_db:g}dB"
    silence_filter = (
        "silenceremove="
        f"start_periods=1:start_duration=0.05:start_threshold={threshold}:start_silence=0.03:"
        f"stop_periods=-1:stop_duration={args.long_pause_seconds:.3f}:"
        f"stop_threshold={threshold}:stop_silence={args.keep_pause_seconds:.3f}:detection=rms"
    )
    audio_filter = (
        f"{silence_filter},"
        f"atempo={args.speed:.4f},"
        f"loudnorm=I={TARGET_LUFS}:TP={TARGET_TRUE_PEAK}:LRA=7"
    )

    command = [
        ffmpeg,
        "-y",
        "-i",
        str(args.input),
        "-vn",
        "-af",
        audio_filter,
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
    if args.min_seconds and duration < args.min_seconds:
        args.output.unlink(missing_ok=True)
        raise SystemExit(
            f"PHASE-2 FAIL: finales Voiceover ist nur {duration:.2f}s lang; "
            f"mindestens {args.min_seconds:.2f}s fuer diesen Lauf erforderlich."
        )

    report = {
        "input": args.input.name,
        "output": args.output.name,
        "raw_duration_seconds": round(raw_duration, 3),
        "duration_seconds": round(duration, 3),
        "sample_rate_hz": SAMPLE_RATE,
        "target_integrated_lufs": TARGET_LUFS,
        "target_true_peak_db": TARGET_TRUE_PEAK,
        "speed_multiplier": args.speed,
        "internal_silence_compression": True,
        "silence_threshold_db": args.silence_threshold_db,
        "long_pause_threshold_seconds": args.long_pause_seconds,
        "retained_pause_seconds": args.keep_pause_seconds,
        "timing_source_policy": "processed-audio-is-authoritative",
    }
    report_path = args.output.with_suffix(".audio-report.json")
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"OK: {args.output}")
    print(f"OK: {report_path}")
    print(f"Rohdauer: {raw_duration:.2f}s")
    print(f"Finaldauer: {duration:.2f}s")
    print(f"Tempo: {args.speed:.2f}x")


if __name__ == "__main__":
    main()
