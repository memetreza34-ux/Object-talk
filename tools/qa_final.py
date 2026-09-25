#!/usr/bin/env python3
"""Technical final-video QA for Object-Talk.

Usage:
python tools/qa_final.py FINAL_VIDEO [FINAL_VOICEOVER]
python tools/qa_final.py FINAL_VIDEO [FINAL_VOICEOVER] --min-seconds 105

Normal channel videos use the default minimum of 300 seconds. A shorter minimum
must be passed explicitly for a documented internal test pilot.

Requires ffprobe. When a voiceover is supplied, ffmpeg is also used to audit
long silent gaps. The canonical audio report created by prepare_audio.py is
checked as well, so a render cannot silently fall back to unprocessed 1.00x TTS.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
from fractions import Fraction
from pathlib import Path

DEFAULT_MIN_DURATION = 300.0
TARGET_WIDTH = 1920
TARGET_HEIGHT = 1080
TARGET_FPS = 30.0
DEFAULT_EXPECTED_SPEED = 1.10
DEFAULT_MAX_VOICE_PAUSE = 0.50
SILENCE_THRESHOLD_DB = -35


def ffprobe_json(ffprobe: str, path: Path) -> dict:
    result = subprocess.run(
        [
            ffprobe,
            "-v",
            "error",
            "-show_streams",
            "-show_format",
            "-of",
            "json",
            str(path),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(result.stdout)


def parse_fps(value: str) -> float:
    try:
        return float(Fraction(value))
    except Exception:
        return 0.0


def detect_silence_durations(ffmpeg: str, path: Path, minimum: float) -> list[float]:
    process = subprocess.run(
        [
            ffmpeg,
            "-hide_banner",
            "-i",
            str(path),
            "-af",
            f"silencedetect=noise={SILENCE_THRESHOLD_DB}dB:d={minimum:.3f}",
            "-f",
            "null",
            "-",
        ],
        capture_output=True,
        text=True,
    )
    text = f"{process.stdout}\n{process.stderr}"
    return [float(value) for value in re.findall(r"silence_duration:\s*([0-9.]+)", text)]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("video", type=Path)
    parser.add_argument("voiceover", type=Path, nargs="?")
    parser.add_argument(
        "--min-seconds",
        type=float,
        default=DEFAULT_MIN_DURATION,
        help="Explizite Mindestdauer. Standard: 300s; nur fuer dokumentierte Tests absenken.",
    )
    parser.add_argument(
        "--expected-speed",
        type=float,
        default=DEFAULT_EXPECTED_SPEED,
        help="Erwarteter prepare_audio-Speed-Multiplikator. Standard: 1.10.",
    )
    parser.add_argument(
        "--max-voice-pause",
        type=float,
        default=DEFAULT_MAX_VOICE_PAUSE,
        help="Maximal erlaubte stille Voice-Pause. Standard: 0.50s.",
    )
    args = parser.parse_args()

    if args.min_seconds <= 0:
        raise SystemExit("FINAL-QA FAIL: --min-seconds muss groesser als 0 sein.")
    if args.expected_speed <= 0:
        raise SystemExit("FINAL-QA FAIL: --expected-speed muss groesser als 0 sein.")
    if args.max_voice_pause <= 0:
        raise SystemExit("FINAL-QA FAIL: --max-voice-pause muss groesser als 0 sein.")

    if not args.video.is_file():
        raise SystemExit(f"FINAL-QA FAIL: Video fehlt: {args.video}")
    if args.video.stat().st_size == 0:
        raise SystemExit("FINAL-QA FAIL: Video ist leer.")

    ffprobe = shutil.which("ffprobe")
    if not ffprobe:
        raise SystemExit("FINAL-QA FAIL: ffprobe wurde nicht in PATH gefunden.")

    data = ffprobe_json(ffprobe, args.video)
    streams = data.get("streams", [])
    video_streams = [stream for stream in streams if stream.get("codec_type") == "video"]
    audio_streams = [stream for stream in streams if stream.get("codec_type") == "audio"]
    errors: list[str] = []
    warnings: list[str] = []

    if len(video_streams) != 1:
        errors.append(f"Erwartet 1 Videostream, gefunden {len(video_streams)}.")
    if not audio_streams:
        errors.append("Kein Audiostream gefunden.")

    duration = float(data.get("format", {}).get("duration") or 0)
    if duration < args.min_seconds:
        errors.append(
            f"Video ist nur {duration:.2f}s lang; mindestens {args.min_seconds:.2f}s erforderlich."
        )

    if video_streams:
        stream = video_streams[0]
        width = int(stream.get("width") or 0)
        height = int(stream.get("height") or 0)
        fps = parse_fps(stream.get("avg_frame_rate") or stream.get("r_frame_rate") or "0/1")
        if (width, height) != (TARGET_WIDTH, TARGET_HEIGHT):
            errors.append(
                f"Falsche Aufloesung: {width}x{height}; erwartet {TARGET_WIDTH}x{TARGET_HEIGHT}."
            )
        if abs(fps - TARGET_FPS) > 0.05:
            errors.append(f"Falsche Framerate: {fps:.3f} fps; erwartet ca. 30 fps.")

    voice_duration = None
    voice_pause_durations: list[float] = []
    audio_report: dict | None = None

    if args.voiceover:
        if not args.voiceover.is_file():
            errors.append(f"Voiceover fuer Vergleich fehlt: {args.voiceover}")
        else:
            voice_data = ffprobe_json(ffprobe, args.voiceover)
            voice_duration = float(voice_data.get("format", {}).get("duration") or 0)
            difference = duration - voice_duration
            if difference < -0.25:
                errors.append(
                    f"Video endet {abs(difference):.2f}s vor dem Voiceover; Sprache koennte fehlen."
                )
            elif difference > 1.0:
                warnings.append(
                    f"Video ist {difference:.2f}s laenger als das Voiceover. Unnoetigen Schluss-Hold pruefen."
                )

            report_path = args.voiceover.with_suffix(".audio-report.json")
            if not report_path.is_file():
                errors.append(
                    "Audio-Report fehlt. Das finale Voiceover muss mit tools/prepare_audio.py erzeugt werden."
                )
            else:
                try:
                    audio_report = json.loads(report_path.read_text(encoding="utf-8"))
                except Exception as exc:
                    errors.append(f"Audio-Report ist unlesbar: {exc}")
                else:
                    actual_speed = float(audio_report.get("speed_multiplier") or 0)
                    if abs(actual_speed - args.expected_speed) > 0.005:
                        errors.append(
                            f"Voice-Speed ist {actual_speed:.3f}x; erwartet {args.expected_speed:.2f}x."
                        )
                    if audio_report.get("internal_silence_compression") is not True:
                        errors.append("Voiceover wurde nicht mit interner Pausenkompression erzeugt.")
                    if audio_report.get("timing_source_policy") != "processed-audio-is-authoritative":
                        errors.append(
                            "Audio-Report bestaetigt nicht, dass das verarbeitete Audio die Timing-Quelle ist."
                        )

            ffmpeg = shutil.which("ffmpeg")
            if not ffmpeg:
                errors.append("ffmpeg fehlt; lange Voice-Pausen koennen nicht geprueft werden.")
            else:
                voice_pause_durations = detect_silence_durations(
                    ffmpeg, args.voiceover, args.max_voice_pause
                )
                if voice_pause_durations:
                    longest = max(voice_pause_durations)
                    total = sum(voice_pause_durations)
                    errors.append(
                        f"Voiceover enthaelt {len(voice_pause_durations)} Pause(n) >= "
                        f"{args.max_voice_pause:.2f}s; laengste {longest:.2f}s, gesamt {total:.2f}s. "
                        "Pausen vor Timeline/Render erneut komprimieren."
                    )

    report = {
        "video": args.video.name,
        "duration_seconds": round(duration, 3),
        "minimum_required_seconds": round(args.min_seconds, 3),
        "voiceover_duration_seconds": round(voice_duration, 3) if voice_duration is not None else None,
        "expected_voice_speed": args.expected_speed,
        "max_voice_pause_seconds": args.max_voice_pause,
        "detected_long_voice_pauses_seconds": [round(value, 3) for value in voice_pause_durations],
        "audio_report": audio_report,
        "errors": errors,
        "warnings": warnings,
        "status": "FAIL" if errors else "PASS",
    }
    report_path = args.video.with_suffix(".qa.json")
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    if warnings:
        print("WARNUNGEN:")
        for warning in warnings:
            print(f"- {warning}")

    if errors:
        print("FEHLER:")
        for error in errors:
            print(f"- {error}")
        print(f"Bericht: {report_path}")
        raise SystemExit(1)

    print("FINAL-QA PASS")
    print(f"Video: {duration:.2f}s")
    print(f"Mindestdauer fuer diesen Lauf: {args.min_seconds:.2f}s")
    if args.voiceover:
        print(f"Voice-Speed: {args.expected_speed:.2f}x")
        print(f"Max. Voice-Pause: {args.max_voice_pause:.2f}s")
    print(f"Bericht: {report_path}")


if __name__ == "__main__":
    main()
