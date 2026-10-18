#!/usr/bin/env python3
"""Transcribe final voiceover and strictly align word times to script.txt.

Usage:
python tools/transcribe_audio.py \
  youtube-videos/THEMA/01_script/audio/final-voiceover.wav \
  youtube-videos/THEMA/01_script/script.txt \
  youtube-videos/THEMA/03_pipeline/timing

The program FAILS if the spoken audio cannot be aligned to the final script.
It never invents missing word timings.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import unicodedata
from pathlib import Path

from faster_whisper import WhisperModel

from text_normalize import normalize_token  # digits/number words/% share one canonical form

MAX_GROUP = 4


def tokenize(text: str) -> list[dict]:
    result: list[dict] = []
    for raw in text.strip().split():
        normalized = normalize_token(raw)
        if normalized:
            result.append({"text": raw, "normalized": normalized})
    return result


def group_text(tokens: list[dict], index: int, count: int) -> str:
    return "".join(token["normalized"] for token in tokens[index : index + count])


def find_exact_grouping(
    script_tokens: list[dict],
    asr_words: list[dict],
    script_index: int,
    asr_index: int,
) -> tuple[int, int] | None:
    matches: list[tuple[float, int, int]] = []

    for script_count in range(1, MAX_GROUP + 1):
        if script_index + script_count > len(script_tokens):
            break
        script_combined = group_text(script_tokens, script_index, script_count)

        for asr_count in range(1, MAX_GROUP + 1):
            if asr_index + asr_count > len(asr_words):
                break
            asr_combined = group_text(asr_words, asr_index, asr_count)
            if script_combined == asr_combined:
                cost = script_count + asr_count + abs(script_count - asr_count) * 0.25
                matches.append((cost, script_count, asr_count))

    if not matches:
        return None

    matches.sort(key=lambda item: item[0])
    _, script_count, asr_count = matches[0]
    return script_count, asr_count


def align_script_to_asr(script_tokens: list[dict], asr_words: list[dict]) -> list[dict]:
    aligned: list[dict] = []
    script_index = 0
    asr_index = 0

    while script_index < len(script_tokens) and asr_index < len(asr_words):
        grouping = find_exact_grouping(script_tokens, asr_words, script_index, asr_index)
        if grouping is None:
            script_context = " ".join(
                token["text"] for token in script_tokens[script_index : script_index + 8]
            )
            asr_context = " ".join(
                token["text"] for token in asr_words[asr_index : asr_index + 8]
            )
            raise ValueError(
                "Strikte Script/Audio-Ausrichtung fehlgeschlagen bei "
                f"Script-Wort {script_index + 1} / Whisper-Wort {asr_index + 1}. "
                f"Script: {script_context!r} | Whisper: {asr_context!r}. "
                "Es wurden keine Zeiten geraten."
            )

        script_count, asr_count = grouping
        script_group = script_tokens[script_index : script_index + script_count]
        asr_group = asr_words[asr_index : asr_index + asr_count]

        one_to_one = (
            script_count == asr_count
            and all(
                script_group[i]["normalized"] == asr_group[i]["normalized"]
                for i in range(script_count)
            )
        )

        if one_to_one:
            for script_token, asr_word in zip(script_group, asr_group):
                item = {
                    "text": script_token["text"],
                    "start": asr_word["start"],
                    "end": asr_word["end"],
                    "alignment": "exact",
                }
                if asr_word.get("probability") is not None:
                    item["probability"] = asr_word["probability"]
                aligned.append(item)
        else:
            span_start = float(asr_group[0]["start"])
            span_end = float(asr_group[-1]["end"])
            span_duration = max(0.001, span_end - span_start)
            weights = [max(1, len(token["normalized"])) for token in script_group]
            total_weight = sum(weights)
            probabilities = [
                float(word["probability"])
                for word in asr_group
                if word.get("probability") is not None
            ]
            probability = sum(probabilities) / len(probabilities) if probabilities else None
            cumulative = 0

            for index, script_token in enumerate(script_group):
                start = span_start + span_duration * cumulative / total_weight
                cumulative += weights[index]
                end = (
                    span_end
                    if index == len(script_group) - 1
                    else span_start + span_duration * cumulative / total_weight
                )
                item = {
                    "text": script_token["text"],
                    "start": round(start, 3),
                    "end": round(max(start + 0.001, end), 3),
                    "alignment": "grouped-exact-text",
                }
                if probability is not None:
                    item["probability"] = round(probability, 4)
                aligned.append(item)

        script_index += script_count
        asr_index += asr_count

    if script_index != len(script_tokens) or asr_index != len(asr_words):
        remaining_script = " ".join(
            token["text"] for token in script_tokens[script_index : script_index + 8]
        )
        remaining_asr = " ".join(
            token["text"] for token in asr_words[asr_index : asr_index + 8]
        )
        raise ValueError(
            "Script/Audio-Laengenabweichung nach strikter Ausrichtung. "
            f"Rest Script: {remaining_script or '<keiner>'!r} | "
            f"Rest Whisper: {remaining_asr or '<keiner>'!r}. Keine Zeiten wurden geraten."
        )

    return aligned


def srt_time(seconds: float) -> str:
    milliseconds = max(0, round(seconds * 1000))
    hours, remainder = divmod(milliseconds, 3_600_000)
    minutes, remainder = divmod(remainder, 60_000)
    secs, ms = divmod(remainder, 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{ms:03d}"


def write_srt(words: list[dict], path: Path) -> None:
    blocks: list[list[dict]] = []
    current: list[dict] = []

    for word in words:
        current.append(word)
        sentence_end = bool(re.search(r"[.!?][\"')\]]?$", word["text"]))
        duration = current[-1]["end"] - current[0]["start"]
        if len(current) >= 8 or (sentence_end and len(current) >= 3) or duration >= 4.5:
            blocks.append(current)
            current = []

    if current:
        blocks.append(current)

    lines: list[str] = []
    for index, block in enumerate(blocks, start=1):
        text = " ".join(item["text"] for item in block)
        lines.extend(
            [
                str(index),
                f"{srt_time(block[0]['start'])} --> {srt_time(block[-1]['end'])}",
                text,
                "",
            ]
        )

    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("audio", type=Path, help="Kanonisches finales Voiceover")
    parser.add_argument("script", type=Path, help="Exakt gesprochene script.txt")
    parser.add_argument("output_dir", type=Path, help="Zielordner fuer Timing-Dateien")
    parser.add_argument("--model", default="small", help="z. B. small, medium, large-v3")
    parser.add_argument("--language", default="de")
    parser.add_argument("--device", default="cpu", help="cpu oder cuda")
    parser.add_argument("--compute-type", default="int8")
    args = parser.parse_args()

    if not args.audio.is_file():
        raise SystemExit(f"Audio nicht gefunden: {args.audio}")
    if not args.script.is_file():
        raise SystemExit(f"Script nicht gefunden: {args.script}")

    script_text = args.script.read_text(encoding="utf-8").replace("\r", "").strip()
    if not script_text:
        raise SystemExit("script.txt ist leer.")

    script_tokens = tokenize(script_text)
    if not script_tokens:
        raise SystemExit("script.txt enthaelt keine ausrichtbaren Woerter.")

    args.output_dir.mkdir(parents=True, exist_ok=True)

    model = WhisperModel(args.model, device=args.device, compute_type=args.compute_type)
    prompt_words = " ".join(token["text"] for token in script_tokens[:180])
    segments_iter, info = model.transcribe(
        str(args.audio),
        language=args.language,
        word_timestamps=True,
        vad_filter=True,
        beam_size=5,
        initial_prompt=prompt_words,
    )

    raw_segments: list[dict] = []
    asr_words: list[dict] = []

    for segment in segments_iter:
        segment_words: list[dict] = []
        for word in segment.words or []:
            if word.start is None or word.end is None:
                continue
            normalized = normalize_token(word.word)
            if not normalized:
                continue
            item = {
                "text": str(word.word).strip(),
                "normalized": normalized,
                "start": round(float(word.start), 3),
                "end": round(float(word.end), 3),
                "probability": (
                    round(float(word.probability), 4)
                    if word.probability is not None
                    else None
                ),
            }
            asr_words.append(item)
            segment_words.append(item)

        raw_segments.append(
            {
                "start": round(float(segment.start), 3),
                "end": round(float(segment.end), 3),
                "text": segment.text.strip(),
                "words": segment_words,
            }
        )

    if not asr_words:
        raise SystemExit("Whisper hat keine Wort-Zeitstempel erzeugt.")

    raw_payload = {
        "source_audio": args.audio.name,
        "language": info.language,
        "language_probability": round(float(info.language_probability), 4),
        "duration": round(float(info.duration), 3),
        "model": args.model,
        "segments": raw_segments,
        "words": asr_words,
    }
    raw_path = args.output_dir / "whisper-raw.json"
    raw_path.write_text(json.dumps(raw_payload, ensure_ascii=False, indent=2), encoding="utf-8")

    try:
        aligned_words = align_script_to_asr(script_tokens, asr_words)
    except ValueError as exc:
        raise SystemExit(f"TIMING FAIL: {exc}") from exc

    script_sha256 = hashlib.sha256(script_text.encode("utf-8")).hexdigest()
    aligned_payload = {
        "source_audio": args.audio.name,
        "source_script": args.script.name,
        "script_sha256": script_sha256,
        "language": args.language,
        "duration": round(float(info.duration), 3),
        "model": args.model,
        "word_count": len(aligned_words),
        "alignment": "strict-script-to-whisper",
        "words": aligned_words,
    }

    timings_path = args.output_dir / "word-timings.json"
    timings_path.write_text(
        json.dumps(aligned_payload, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    srt_path = args.output_dir / "subtitles.srt"
    write_srt(aligned_words, srt_path)

    print(f"OK: {raw_path}")
    print(f"OK: {timings_path}")
    print(f"OK: {srt_path}")
    print(f"Woerter exakt ausgerichtet: {len(aligned_words)}")
    print(f"Dauer: {aligned_payload['duration']:.2f} Sekunden")

    if aligned_payload["duration"] < 300:
        raise SystemExit("TIMING FAIL: Finales Voiceover ist kuerzer als 5:00 Minuten.")


if __name__ == "__main__":
    main()
