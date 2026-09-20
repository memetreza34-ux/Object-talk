#!/usr/bin/env python3
"""Stage canonical assets and generate Remotion runtime data.

Usage:
python tools/build_renderer_runtime.py \
  youtube-videos/THEMA/03_pipeline/timing/timeline.json \
  youtube-videos/THEMA/02_bildprompts/images \
  youtube-videos/THEMA/01_script/audio/final-voiceover.wav

The fixed renderer lives in renderer/. This tool never invents scene timing;
it only converts the already resolved timeline from seconds to frames.
"""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

FPS = 30
WIDTH = 1920
HEIGHT = 1080
ALLOWED_MOTIONS = {
    "static",
    "slow-push-in",
    "slow-pull-out",
    "pan-left",
    "pan-right",
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("timeline", type=Path)
    parser.add_argument("images_dir", type=Path)
    parser.add_argument("audio", type=Path)
    parser.add_argument(
        "--renderer-dir",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "renderer",
    )
    args = parser.parse_args()

    if not args.timeline.is_file():
        raise SystemExit(f"FEHLER: Timeline fehlt: {args.timeline}")
    if not args.images_dir.is_dir():
        raise SystemExit(f"FEHLER: Bilderordner fehlt: {args.images_dir}")
    if not args.audio.is_file():
        raise SystemExit(f"FEHLER: finales Audio fehlt: {args.audio}")

    timeline = json.loads(args.timeline.read_text(encoding="utf-8"))
    scenes = timeline.get("scenes", [])
    audio_duration = float(timeline.get("audio_duration", 0))
    if not scenes or audio_duration <= 0:
        raise SystemExit("FEHLER: ungueltige timeline.json.")

    renderer_dir = args.renderer_dir.resolve()
    public_current = renderer_dir / "public" / "current"
    images_target = public_current / "images"
    audio_target_dir = public_current / "audio"

    if public_current.exists():
        shutil.rmtree(public_current)
    images_target.mkdir(parents=True, exist_ok=True)
    audio_target_dir.mkdir(parents=True, exist_ok=True)

    runtime_scenes: list[dict] = []

    for scene in scenes:
        scene_number = int(scene["scene"])
        source = args.images_dir / f"Bild_{scene_number:02d}.png"
        if not source.is_file():
            raise SystemExit(f"FEHLER: Renderer-Asset fehlt: {source}")

        target = images_target / source.name
        shutil.copy2(source, target)

        start_seconds = float(scene["start"])
        end_seconds = float(scene["end"])
        start_frame = round(start_seconds * FPS)
        end_frame = round(end_seconds * FPS)
        duration_frames = max(1, end_frame - start_frame)
        motion = str(scene.get("motion") or "slow-push-in")
        if motion not in ALLOWED_MOTIONS:
            raise SystemExit(
                f"FEHLER: Szene {scene_number} nutzt unbekannte Bewegung {motion!r}."
            )

        runtime_scenes.append(
            {
                "scene": scene_number,
                "file": f"current/images/{source.name}",
                "startFrame": start_frame,
                "durationInFrames": duration_frames,
                "motion": motion,
            }
        )

    audio_target = audio_target_dir / "final-voiceover.wav"
    shutil.copy2(args.audio, audio_target)

    runtime = {
        "fps": FPS,
        "width": WIDTH,
        "height": HEIGHT,
        "durationSeconds": round(audio_duration, 3),
        "audioFile": "current/audio/final-voiceover.wav",
        "scenes": runtime_scenes,
    }

    generated_path = renderer_dir / "src" / "project.generated.ts"
    generated_path.parent.mkdir(parents=True, exist_ok=True)
    json_literal = json.dumps(runtime, ensure_ascii=False, indent=2)
    generated_path.write_text(
        "export type MotionType = 'static' | 'slow-push-in' | 'slow-pull-out' | 'pan-left' | 'pan-right';\n\n"
        "export type SceneRuntime = {\n"
        "  scene: number;\n"
        "  file: string;\n"
        "  startFrame: number;\n"
        "  durationInFrames: number;\n"
        "  motion: MotionType;\n"
        "};\n\n"
        "export type ObjectTalkProject = {\n"
        "  fps: number;\n"
        "  width: number;\n"
        "  height: number;\n"
        "  durationSeconds: number;\n"
        "  audioFile: string;\n"
        "  scenes: SceneRuntime[];\n"
        "};\n\n"
        f"export const project: ObjectTalkProject = {json_literal};\n",
        encoding="utf-8",
    )

    runtime_report = renderer_dir / "runtime-report.json"
    runtime_report.write_text(json.dumps(runtime, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"OK: Renderer-Runtime gebaut: {generated_path}")
    print(f"Szenen: {len(runtime_scenes)}")
    print(f"Dauer: {audio_duration:.2f}s")
    print("Naechster Schritt: cd renderer && npm install && npm run render -- ../PFAD/final-video.mp4")


if __name__ == "__main__":
    main()
