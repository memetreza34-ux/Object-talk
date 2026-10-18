#!/usr/bin/env python3
"""Write YouTube chapter marks with REAL times from the final timeline.

Usage:
  python tools/export_chapters.py youtube-videos/VIDEO

Inputs:  .intern/05_info/phase1-scenes.json (chapter / chapter_start per scene)
         .intern/03_pipeline/timing/timeline.json (real scene start times)
Output:  KAPITEL block inside 03_export/CAPTION-YOUTUBE.txt
         .intern/05_info/YOUTUBE-KAPITEL.txt (copy for reference)

YouTube rules: first chapter at 0:00, at least three chapters, each >= 10 s.
Chapters improve navigation and search snippets; times are never estimated.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

MIN_CHAPTER_SECONDS = 10.0


def clock(seconds: float) -> str:
    total = int(seconds)
    minutes, secs = divmod(total, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours}:{minutes:02d}:{secs:02d}" if hours else f"{minutes}:{secs:02d}"


def chapter_lines(scenes: list[dict], timeline: list[dict]) -> list[str]:
    if len(scenes) != len(timeline):
        raise SystemExit("KAPITEL FAIL: phase1-scenes und timeline haben unterschiedlich viele Szenen.")
    marks = []
    for scene, timed in zip(scenes, timeline):
        if scene.get("chapter_start"):
            marks.append((0.0 if not marks else float(timed["start"]), str(scene.get("chapter", "")).strip()))
    if len(marks) < 3:
        raise SystemExit("KAPITEL FAIL: YouTube braucht mindestens drei Kapitel.")
    end_of_video = float(timeline[-1]["end"])
    for index, (start, title) in enumerate(marks):
        end = marks[index + 1][0] if index + 1 < len(marks) else end_of_video
        if not title:
            raise SystemExit(f"KAPITEL FAIL: Kapitel {index + 1} ohne Titel.")
        if end - start < MIN_CHAPTER_SECONDS:
            raise SystemExit(f"KAPITEL FAIL: Kapitel {title!r} ist kürzer als {MIN_CHAPTER_SECONDS:.0f} s.")
    return [f"{clock(start)} {title}" for start, title in marks]


def insert_into_caption(caption: str, lines: list[str]) -> str:
    block = "KAPITEL\n" + "\n".join(lines) + "\n\n"
    if re.search(r"(?ms)^KAPITEL\n.*?\n\n(?=HASHTAGS)", caption):
        return re.sub(r"(?ms)^KAPITEL\n.*?\n\n(?=HASHTAGS)", lambda _: block, caption)
    if "HASHTAGS" in caption:
        return caption.replace("HASHTAGS", block + "HASHTAGS", 1)
    return caption.rstrip() + "\n\n" + block


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("project", type=Path)
    args = parser.parse_args()
    project = args.project
    scenes_path = project / ".intern" / "05_info" / "phase1-scenes.json"
    timeline_path = project / ".intern" / "03_pipeline" / "timing" / "timeline.json"
    caption_path = project / "03_export" / "CAPTION-YOUTUBE.txt"
    for path in (scenes_path, timeline_path, caption_path):
        if not path.is_file():
            raise SystemExit(f"KAPITEL FAIL: Datei fehlt: {path}")
    scenes = json.loads(scenes_path.read_text(encoding="utf-8")).get("scenes", [])
    if not any(scene.get("chapter_start") for scene in scenes):
        print("KAPITEL: keine Kapitelplanung in phase1-scenes.json – übersprungen.")
        return
    timeline = json.loads(timeline_path.read_text(encoding="utf-8")).get("scenes", [])
    lines = chapter_lines(scenes, timeline)
    caption_path.write_text(insert_into_caption(caption_path.read_text(encoding="utf-8"), lines), encoding="utf-8")
    (project / ".intern" / "05_info" / "YOUTUBE-KAPITEL.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"OK: {len(lines)} Kapitel mit echten Zeiten in {caption_path}")


if __name__ == "__main__":
    main()
