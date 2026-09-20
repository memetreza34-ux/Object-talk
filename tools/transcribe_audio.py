#!/usr/bin/env python3
"""Transkribiert das finale Voiceover mit faster-whisper und erzeugt Wort-Zeitstempel.

Beispiel:
python tools/transcribe_audio.py \
  youtube-videos/MEIN-THEMA/01_script/audio/voiceover.mp3 \
  youtube-videos/MEIN-THEMA/03_pipeline/timing
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from faster_whisper import WhisperModel


def srt_time(seconds: float) -> str:
    milliseconds = max(0, round(seconds * 1000))
    hours, remainder = divmod(milliseconds, 3_600_000)
    minutes, remainder = divmod(remainder, 60_000)
    secs, ms = divmod(remainder, 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{ms:03d}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("audio", type=Path, help="Fertige Voiceover-Datei")
    parser.add_argument("output_dir", type=Path, help="Zielordner für Timing-Dateien")
    parser.add_argument("--model", default="small", help="z. B. small, medium, large-v3")
    parser.add_argument("--language", default="de")
    parser.add_argument("--device", default="cpu", help="cpu oder cuda")
    parser.add_argument("--compute-type", default="int8")
    args = parser.parse_args()

    if not args.audio.exists():
        raise SystemExit(f"Audio nicht gefunden: {args.audio}")

    args.output_dir.mkdir(parents=True, exist_ok=True)

    model = WhisperModel(
        args.model,
        device=args.device,
        compute_type=args.compute_type,
    )

    segments_iter, info = model.transcribe(
        str(args.audio),
        language=args.language,
        word_timestamps=True,
        vad_filter=True,
        beam_size=5,
    )

    segments = []
    words = []

    for segment in segments_iter:
        segment_words = []
        if segment.words:
            for word in segment.words:
                if word.start is None or word.end is None:
                    continue
                item = {
                    "word": word.word.strip(),
                    "start": round(float(word.start), 3),
                    "end": round(float(word.end), 3),
                    "probability": round(float(word.probability), 4)
                    if word.probability is not None
                    else None,
                }
                words.append(item)
                segment_words.append(item)

        segments.append(
            {
                "start": round(float(segment.start), 3),
                "end": round(float(segment.end), 3),
                "text": segment.text.strip(),
                "words": segment_words,
            }
        )

    payload = {
        "source_audio": args.audio.name,
        "language": info.language,
        "language_probability": round(float(info.language_probability), 4),
        "duration": round(float(info.duration), 3),
        "model": args.model,
        "segments": segments,
        "words": words,
    }

    json_path = args.output_dir / "whisper-words.json"
    json_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    srt_lines = []
    for index, segment in enumerate(segments, start=1):
        srt_lines.extend(
            [
                str(index),
                f"{srt_time(segment['start'])} --> {srt_time(segment['end'])}",
                segment["text"],
                "",
            ]
        )

    srt_path = args.output_dir / "subtitles.srt"
    srt_path.write_text("\n".join(srt_lines), encoding="utf-8")

    print(f"OK: {json_path}")
    print(f"OK: {srt_path}")
    print(f"Dauer: {payload['duration']:.2f} Sekunden")

    if payload["duration"] < 300:
        print("WARNUNG: Das Voiceover ist kürzer als 5:00 Minuten.")


if __name__ == "__main__":
    main()
