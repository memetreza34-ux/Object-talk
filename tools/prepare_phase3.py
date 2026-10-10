#!/usr/bin/env python3
"""Prepare one Object-Talk project for deterministic rendering.

Usage:
python tools/prepare_phase3.py youtube-videos/THEMA [--model small]

Required order:
raw voice -> canonical 1.10x pause-compressed voice -> safe Flow ZIP import ->
asset validation -> strict Whisper/script alignment -> exact scene timeline ->
external subtitle export -> Remotion runtime.

The raw TTS file is never a valid timing source.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

EXPECTED_SPEED = 1.10


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


def validate_existing_final_audio(final_audio: Path) -> None:
    report_path = final_audio.with_suffix(".audio-report.json")
    if not report_path.is_file():
        raise SystemExit(
            "PHASE-3 PREP FAIL: final-voiceover.wav existiert, aber der Audio-Report fehlt. "
            "Audio erneut mit tools/prepare_audio.py erzeugen."
        )
    try:
        report = json.loads(report_path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise SystemExit(f"PHASE-3 PREP FAIL: Audio-Report unlesbar: {exc}") from exc

    speed = float(report.get("speed_multiplier") or 0)
    if abs(speed - EXPECTED_SPEED) > 0.005:
        raise SystemExit(
            f"PHASE-3 PREP FAIL: bestehendes finales Audio ist {speed:.3f}x; "
            f"erwartet {EXPECTED_SPEED:.2f}x. Audio neu vorbereiten."
        )
    if report.get("internal_silence_compression") is not True:
        raise SystemExit(
            "PHASE-3 PREP FAIL: bestehendes finales Audio hat keine bestaetigte Pausenkompression."
        )
    if report.get("timing_source_policy") != "processed-audio-is-authoritative":
        raise SystemExit(
            "PHASE-3 PREP FAIL: Audio-Report markiert das verarbeitete Audio nicht als Timing-Quelle."
        )


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
    simplified = (project / ".intern" / "05_info" / "phase1-scenes.json").is_file()
    internal_dir = project / ".intern" if simplified else project
    pipeline_dir = internal_dir / "03_pipeline"
    images_dir = pipeline_dir / "images" if simplified else ((project / "03_pipeline" / "images") if (project / "05_info" / "label-plan.json").is_file() else (prompt_dir / "images"))
    timing_dir = pipeline_dir / "timing"
    scene_map = pipeline_dir / "scene-map.json"
    phase1_scenes = internal_dir / "05_info" / "phase1-scenes.json"
    final_audio = audio_dir / "final-voiceover.wav"

    for required in (script, phase1_scenes):
        if not required.is_file():
            raise SystemExit(f"PHASE-3 PREP FAIL: notwendige Datei fehlt: {required}")

    run(
        [
            sys.executable,
            "tools/generate_scene_map.py",
            str(phase1_scenes),
            str(scene_map),
        ],
        repo_root,
    )

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

    if raw_audio_candidates:
        raw_audio = exactly_one(raw_audio_candidates, "rohe Voice-Datei")
        run(
            [
                sys.executable,
                "tools/prepare_audio.py",
                str(raw_audio),
                str(final_audio),
                "--speed",
                f"{EXPECTED_SPEED:.2f}",
            ],
            repo_root,
        )
    elif final_audio.is_file():
        validate_existing_final_audio(final_audio)
        print(f"\nKanonisches Audio validiert: {final_audio}")
    else:
        raise SystemExit(
            "PHASE-3 PREP FAIL: weder rohe Voice-Datei noch gueltiges final-voiceover.wav gefunden."
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

    # External YouTube subtitle package: readable timed script + uploadable SRT.
    # Uses only the final timeline; timestamps are never guessed.
    run(
        [
            sys.executable,
            "tools/export_subtitles.py",
            str(project),
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

    print("\nPHASE-3 PREP PASS")
    print(f"Voice-Speed: {EXPECTED_SPEED:.2f}x, Pausenkompression validiert.")
    print("Untertitel-Export aus finaler Timeline erstellt.")
    print("Renderer-Runtime ist vorbereitet. Jetzt Preview/Render in renderer/ ausfuehren.")


if __name__ == "__main__":
    main()
