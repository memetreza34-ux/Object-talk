#!/usr/bin/env python3
"""Erzeugt aus scene-map.json und Whisper-Wortzeiten eine exakte Bild-Timeline.

Die Scene-Map wird in Phase 1 von ChatGPT erstellt. Die echten Sekundenwerte
werden erst nach dem finalen Voiceover berechnet.

Beispiel:
python tools/build_timeline.py \
  youtube-videos/MEIN-THEMA/03_pipeline/scene-map.json \
  youtube-videos/MEIN-THEMA/03_pipeline/timing/whisper-words.json \
  youtube-videos/MEIN-THEMA/03_pipeline/timing/timeline.json
"""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
from pathlib import Path

from rapidfuzz import fuzz


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKC", text).lower()
    text = text.replace("ß", "ss")
    text = re.sub(r"[^a-z0-9äöü]+", " ", text)
    return " ".join(text.split())


def normalized_tokens(text: str) -> list[str]:
    value = normalize(text)
    return value.split() if value else []


def find_anchor(
    words: list[dict],
    phrase: str,
    min_index: int = 0,
    threshold: float = 75.0,
) -> dict:
    target_tokens = normalized_tokens(phrase)
    if not target_tokens:
        raise ValueError("Leerer Textanker")

    normalized_words = [normalize(item["word"]) for item in words]
    target = " ".join(target_tokens)
    target_len = len(target_tokens)

    best = None
    min_window = max(1, target_len - 2)
    max_window = target_len + 2

    for start in range(max(0, min_index), len(words)):
        for window_len in range(min_window, max_window + 1):
            end = start + window_len
            if end > len(words):
                continue
            candidate = " ".join(w for w in normalized_words[start:end] if w)
            score = fuzz.ratio(target, candidate)
            if best is None or score > best["score"]:
                best = {
                    "start_index": start,
                    "end_index": end - 1,
                    "score": round(float(score), 2),
                    "candidate": candidate,
                }

    if best is None or best["score"] < threshold:
        score = best["score"] if best else 0
        candidate = best["candidate"] if best else ""
        raise ValueError(
            f"Anker nicht sicher gefunden ({score}%): {phrase!r}. "
            f"Bester Treffer: {candidate!r}"
        )

    best["start"] = float(words[best["start_index"]]["start"])
    best["end"] = float(words[best["end_index"]]["end"])
    return best


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("scene_map", type=Path)
    parser.add_argument("whisper_json", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--threshold", type=float, default=75.0)
    args = parser.parse_args()

    scenes = json.loads(args.scene_map.read_text(encoding="utf-8"))
    whisper = json.loads(args.whisper_json.read_text(encoding="utf-8"))

    if isinstance(scenes, dict):
        scenes = scenes.get("scenes", [])

    if not scenes:
        raise SystemExit("scene-map.json enthält keine Szenen.")

    words = whisper.get("words", [])
    duration = float(whisper.get("duration", 0))
    if not words:
        raise SystemExit("Keine Whisper-Wortzeiten gefunden.")

    resolved = []
    cursor = 0

    for idx, scene in enumerate(scenes):
        start_anchor = scene.get("start_anchor", "").strip()
        end_anchor = scene.get("end_anchor", "").strip()

        start_match = find_anchor(
            words,
            start_anchor,
            min_index=cursor,
            threshold=args.threshold,
        )

        end_match = find_anchor(
            words,
            end_anchor,
            min_index=start_match["start_index"],
            threshold=args.threshold,
        )

        if end_match["end_index"] < start_match["start_index"]:
            raise ValueError(f"Ungültige Ankerreihenfolge in Szene {scene.get('scene')}")

        start_time = 0.0 if idx == 0 else round(start_match["start"], 3)

        resolved.append(
            {
                "scene": scene["scene"],
                "image": scene["image"],
                "description": scene.get("description", ""),
                "start_anchor": start_anchor,
                "end_anchor": end_anchor,
                "start": start_time,
                "anchor_end": round(end_match["end"], 3),
                "start_match_score": start_match["score"],
                "end_match_score": end_match["score"],
            }
        )

        cursor = start_match["start_index"] + 1

    # Die sichtbaren Szenen werden lückenlos aneinandergelegt:
    # Ende einer Szene = Start der nächsten Szene.
    for index, scene in enumerate(resolved):
        if index + 1 < len(resolved):
            scene["end"] = resolved[index + 1]["start"]
        else:
            scene["end"] = round(duration, 3)

        scene["duration"] = round(scene["end"] - scene["start"], 3)
        if scene["duration"] <= 0:
            raise ValueError(f"Ungültige Dauer in Szene {scene['scene']}")

    result = {
        "audio_duration": round(duration, 3),
        "scene_count": len(resolved),
        "scenes": resolved,
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"OK: {args.output}")
    print(f"Szenen: {len(resolved)}")
    print(f"Audio: {duration:.2f} Sekunden")

    long_scenes = [s for s in resolved if s["duration"] > 12]
    if long_scenes:
        print("WARNUNG: Szenen über 12 Sekunden:")
        for scene in long_scenes:
            print(f"  Szene {scene['scene']}: {scene['duration']:.2f}s")


if __name__ == "__main__":
    main()
