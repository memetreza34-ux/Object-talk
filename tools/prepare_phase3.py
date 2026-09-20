#!/usr/bin/env python3
"""Prepare one Object-Talk project for deterministic rendering.

Usage:
python tools/prepare_phase3.py youtube-videos/THEMA [--model small]

This command performs all non-render Phase-3 preparation in the required order:
raw voice -> canonical voice -> safe Flow ZIP import -> asset validation ->
strict Whisper/script alignment -> exact scene timeline -> Remotion runtime.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def run(command: list[str], cwd: Path) -> None:
    print("\n> " + " ".join(command))
    result = subprocess.run(command, cwd=cwd)
    if result.returncode != 0:
        raise SystemExit(f"PHASE-3 PREP FAIL: command exited with {result.returncode}")


def exactly_one(paths: list[Path], label: str) -> Path:
    if len(paths) != 1:
        listing = ", ".join(path.name for path in paths) or "<keine>"
        raise SystemExit(f"PHASE-3 PREP FAIL: erwartet genau eine {label}; gefunden: {listing}")
    return paths[0]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("project_dir", type=Path)
    parser.add_argument("--model", default="small")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    project = args.project_dir.resolve()
    if not project.is_dir():
        raise SystemExit(f"PHASE-3 PREP FAIL: Projektordner fehlt: {project}")

    script = project / "01_script" / "script.txt"
    audio_dir = project / "01_script" / "audio"
    prompt_dir = project / "02_bildprompts"
    zip_dir = prompt_dir / "bilder-zip"
    images_dir = prompt_dir / "images"
    pipeline_dir = project / "03_pipeline"
    timing_dir = pipeline_dir / "timing"
    scene_map = pipeline_dir / "scene-map.json"
    phase1_scenes = project / "05_info" / "phase1-scenes.json"
    final_audio = audio_dir / "final-voiceover.wav"

    for required in (script, scene_map, phase1_scenes):
        if not required.is_file():
            raise SystemExit(f"PHASE-3 PREP FAIL: notwendige Datei fehlt: {required}")

    if not audio_dir.is_dir():
        raise SystemExit(f"PHASE-3 PREP FAIL: Audioordner fehlt: {audio_dir}")
    if not zip_dir.is_dir():
        raise SystemExit(f"PHASE-3 PREP FAIL: ZIP-Ordner fehlt: {zip_dir}")

    run(
        [
            sys.executable,
            "tools/validate_phase1.py",
            str(script),
            str(phase1_scenes),
            str(scene_map),
        ],
        repo_root,
    )

    raw_audio_candidates = [
        path
        for path in audio_dir.iterdir()
        if path.is_file()
        and path.suffix.lower() in {".mp3", ".wav", ".m4a", ".aac", ".flac", ".ogg"}
        and path.name != "final-voiceover.wav"
    ]

    if final_audio.is_file() and not raw_audio_candidates:
        print(f"\nKanonisches Audio bereits vorhanden: {final_audio}")
    else:
        raw_audio = exactly_one(raw_audio_candidates, "rohe Voice-Datei")
        run(
            [sys.executable, "tools/prepare_audio.py", str(raw_audio), str(final_audio)],
            repo_root,
        )

    zip_file = exactly_one(sorted(zip_dir.glob("*.zip")), "Google-Flow-ZIP")
    run(
        [
            sys.executable,
            "tools/import_flow_zip.py",
            str(scene_map),
            str(zip_file),
            str(images_dir),
        ],
        repo_root,
    )

    run(
        [sys.executable, "tools/validate_assets.py", str(scene_map), str(images_dir)],
        repo_root,
    )

    timing_dir.mkdir(parents=True, exist_ok=True)
    run(
        [
            sys.executable,
            "tools/transcribe_audio.py",
            str(final_audio),
            str(script),
            str(timing_dir),
            "--model",
            args.model,
        ],
        repo_root,
    )

    word_timings = timing_dir / "word-timings.json"
    timeline = timing_dir / "timeline.json"
    run(
        [
            sys.executable,
            "tools/build_timeline.py",
            str(scene_map),
            str(word_timings),
            str(timeline),
        ],
        repo_root,
    )

    run(
        [
            sys.executable,
            "tools/build_renderer_runtime.py",
            str(timeline),
            str(images_dir),
            str(final_audio),
        ],
        repo_root,
    )

    source_srt = timing_dir / "subtitles.srt"
    subtitle_dir = project / "04_export" / "subtitles"
    subtitle_dir.mkdir(parents=True, exist_ok=True)
    if source_srt.is_file():
        shutil.copy2(source_srt, subtitle_dir / "subtitles.srt")

    print("\nPHASE-3 PREP PASS")
    print("Renderer-Runtime ist vorbereitet. Jetzt Preview/Render in renderer/ ausfuehren.")


if __name__ == "__main__":
    main()
