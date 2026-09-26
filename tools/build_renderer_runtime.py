#!/usr/bin/env python3
"""Stage canonical assets and generate Remotion runtime data.

Usage:
python tools/build_renderer_runtime.py \
  youtube-videos/THEMA/03_pipeline/timing/timeline.json \
  youtube-videos/THEMA/02_bildprompts/images \
  youtube-videos/THEMA/01_script/audio/final-voiceover.wav

The fixed renderer lives in renderer/. This tool never invents scene timing;
it only converts the already resolved timeline from seconds to frames.

Defense-in-depth rules:
- no individual image may be held longer than 7 seconds
- no image file may be reused by another scene
- Remotion visible text overlays are forbidden
- all final visible text must already be present in accepted Google-Flow images
"""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

FPS = 30
WIDTH = 1920
HEIGHT = 1080
MAX_SCENE_SECONDS = 7.0
ALLOWED_MOTIONS = {
    "static",
    "slow-push-in",
    "slow-pull-out",
    "pan-left",
    "pan-right",
}


def enforce_no_text_overlays(timeline_path: Path) -> None:
    project_dir = timeline_path.resolve().parents[2]
    overlay_path = project_dir / "03_pipeline" / "overlay-plan.json"
    if not overlay_path.is_file():
        return

    try:
        payload = json.loads(overlay_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"FEHLER: ungueltiges overlay-plan.json: {exc}")

    scene_entries = payload.get("scenes", [])
    if not isinstance(scene_entries, list):
        raise SystemExit("FEHLER: overlay-plan.json: scenes muss eine Liste sein.")

    non_empty: list[int] = []
    for scene_entry in scene_entries:
        if not isinstance(scene_entry, dict):
            raise SystemExit("FEHLER: overlay-plan.json enthaelt ungueltigen Szeneneintrag.")
        overlays = scene_entry.get("overlays", [])
        if not isinstance(overlays, list):
            raise SystemExit("FEHLER: overlay-plan.json: overlays muss eine Liste sein.")
        if overlays:
            non_empty.append(int(scene_entry.get("scene", 0)))

    if non_empty:
        raise SystemExit(
            "REMOTION-TEXT FAIL: sichtbare Text-Overlays sind hart deaktiviert. "
            "Alle Titel, Labels und Kapiteltexte muessen bereits korrekt aus Google Flow kommen. "
            f"Nicht-leere Overlay-Szenen: {non_empty}. Bilder in Flow korrigieren und overlay-plan.json leeren."
        )


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

    enforce_no_text_overlays(args.timeline)

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
    used_source_names: set[str] = set()

    for scene in scenes:
        scene_number = int(scene["scene"])
        source = args.images_dir / f"Bild_{scene_number:02d}.png"
        if not source.is_file():
            raise SystemExit(f"FEHLER: Renderer-Asset fehlt: {source}")
        if source.name in used_source_names:
            raise SystemExit(
                f"FEHLER: Bildasset wird mehrfach in der Timeline verwendet: {source.name}. "
                "Jede Szene braucht ein eindeutiges Bild."
            )
        used_source_names.add(source.name)

        start_seconds = float(scene["start"])
        end_seconds = float(scene["end"])
        scene_seconds = end_seconds - start_seconds
        if scene_seconds <= 0:
            raise SystemExit(f"FEHLER: Szene {scene_number} hat ungueltige Dauer {scene_seconds:.3f}s.")
        if scene_seconds > MAX_SCENE_SECONDS + 0.01:
            raise SystemExit(
                f"FEHLER: Szene {scene_number} / {source.name} steht {scene_seconds:.2f}s. "
                f"Maximal erlaubt sind {MAX_SCENE_SECONDS:.2f}s. Speech-Beat in neue eindeutige "
                "Szenen/Bilder teilen; Bild nicht duplizieren."
            )

        target = images_target / source.name
        shutil.copy2(source, target)

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
                "overlays": [],
            }
        )

    audio_target = audio_target_dir / "final-voiceover.wav"
    shutil.copy2(args.audio, audio_target)

    runtime = {
        "fps": FPS,
        "width": WIDTH,
        "height": HEIGHT,
        "durationSeconds": round(audio_duration, 3),
        "maxSceneSeconds": MAX_SCENE_SECONDS,
        "audioFile": "current/audio/final-voiceover.wav",
        "scenes": runtime_scenes,
    }

    generated_path = renderer_dir / "src" / "project.generated.ts"
    generated_path.parent.mkdir(parents=True, exist_ok=True)
    json_literal = json.dumps(runtime, ensure_ascii=False, indent=2)
    generated_path.write_text(
        "export type MotionType = 'static' | 'slow-push-in' | 'slow-pull-out' | 'pan-left' | 'pan-right';\n"
        "export type OverlayKind = 'heading' | 'keyword' | 'callout';\n"
        "export type OverlayPosition = 'top-left' | 'top-center' | 'bottom-left' | 'center';\n"
        "export type OverlayAnimation = 'fade-slide' | 'pop' | 'underline';\n\n"
        "export type OverlayRuntime = {\n"
        "  kind: OverlayKind;\n"
        "  text: string;\n"
        "  position: OverlayPosition;\n"
        "  animation: OverlayAnimation;\n"
        "  startFraction: number;\n"
        "  durationFraction: number;\n"
        "};\n\n"
        "export type SceneRuntime = {\n"
        "  scene: number;\n"
        "  file: string;\n"
        "  startFrame: number;\n"
        "  durationInFrames: number;\n"
        "  motion: MotionType;\n"
        "  overlays?: OverlayRuntime[];\n"
        "};\n\n"
        "export type ObjectTalkProject = {\n"
        "  fps: number;\n"
        "  width: number;\n"
        "  height: number;\n"
        "  durationSeconds: number;\n"
        "  maxSceneSeconds: number;\n"
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
    print("Remotion-Textoverlays: 0 (hart deaktiviert)")
    print(f"Dauer: {audio_duration:.2f}s")
    print(f"Maximale Bilddauer: {MAX_SCENE_SECONDS:.2f}s")
    print("Naechster Schritt: cd renderer && npm install && npm run render -- ../PFAD/final-video.mp4")


if __name__ == "__main__":
    main()
