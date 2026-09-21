#!/usr/bin/env python3
"""Stage canonical assets and generate Remotion runtime data.

Usage:
python tools/build_renderer_runtime.py \
  youtube-videos/THEMA/03_pipeline/timing/timeline.json \
  youtube-videos/THEMA/02_bildprompts/images \
  youtube-videos/THEMA/01_script/audio/final-voiceover.wav

The fixed renderer lives in renderer/. This tool never invents scene timing;
it only converts the already resolved timeline from seconds to frames.

If `03_pipeline/overlay-plan.json` exists next to the project, short editorial
headlines/keywords are attached to the corresponding scenes. Missing overlay
plans are allowed and keep the legacy full-image-only behavior.
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
ALLOWED_OVERLAY_KINDS = {"heading", "keyword", "callout"}
ALLOWED_OVERLAY_POSITIONS = {"top-left", "top-center", "bottom-left", "center"}
ALLOWED_OVERLAY_ANIMATIONS = {"fade-slide", "pop", "underline"}


def load_overlay_plan(timeline_path: Path) -> dict[int, list[dict]]:
    project_dir = timeline_path.resolve().parents[2]
    overlay_path = project_dir / "03_pipeline" / "overlay-plan.json"
    if not overlay_path.is_file():
        return {}

    try:
        payload = json.loads(overlay_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"FEHLER: ungueltiges overlay-plan.json: {exc}")

    scene_entries = payload.get("scenes", [])
    if not isinstance(scene_entries, list):
        raise SystemExit("FEHLER: overlay-plan.json: scenes muss eine Liste sein.")

    result: dict[int, list[dict]] = {}
    for scene_entry in scene_entries:
        if not isinstance(scene_entry, dict):
            raise SystemExit("FEHLER: overlay-plan.json enthaelt ungueltigen Szeneneintrag.")
        scene_number = int(scene_entry.get("scene", 0))
        overlays = scene_entry.get("overlays", [])
        if scene_number <= 0 or not isinstance(overlays, list):
            raise SystemExit("FEHLER: overlay-plan.json enthaelt ungueltige scene/overlays-Werte.")

        clean: list[dict] = []
        for overlay in overlays:
            if not isinstance(overlay, dict):
                raise SystemExit(f"FEHLER: Szene {scene_number}: Overlay muss ein Objekt sein.")

            kind = str(overlay.get("kind", "heading"))
            text = str(overlay.get("text", "")).strip()
            position = str(overlay.get("position", "top-left"))
            animation = str(overlay.get("animation", "fade-slide"))
            start_fraction = float(overlay.get("start_fraction", 0.05))
            duration_fraction = float(overlay.get("duration_fraction", 0.55))

            if kind not in ALLOWED_OVERLAY_KINDS:
                raise SystemExit(f"FEHLER: Szene {scene_number}: unbekannter Overlay-Typ {kind!r}.")
            if position not in ALLOWED_OVERLAY_POSITIONS:
                raise SystemExit(f"FEHLER: Szene {scene_number}: unbekannte Overlay-Position {position!r}.")
            if animation not in ALLOWED_OVERLAY_ANIMATIONS:
                raise SystemExit(f"FEHLER: Szene {scene_number}: unbekannte Overlay-Animation {animation!r}.")
            if not text or len(text) > 60:
                raise SystemExit(f"FEHLER: Szene {scene_number}: Overlay-Text fehlt oder ist zu lang.")
            if not 0 <= start_fraction < 1:
                raise SystemExit(f"FEHLER: Szene {scene_number}: start_fraction muss zwischen 0 und 1 liegen.")
            if not 0 < duration_fraction <= 1:
                raise SystemExit(f"FEHLER: Szene {scene_number}: duration_fraction muss >0 und <=1 sein.")

            clean.append(
                {
                    "kind": kind,
                    "text": text,
                    "position": position,
                    "animation": animation,
                    "startFraction": start_fraction,
                    "durationFraction": duration_fraction,
                }
            )
        result[scene_number] = clean

    return result


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

    overlay_plan = load_overlay_plan(args.timeline)

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
                "overlays": overlay_plan.get(scene_number, []),
            }
        )

    unknown_overlay_scenes = set(overlay_plan) - {int(scene["scene"]) for scene in scenes}
    if unknown_overlay_scenes:
        raise SystemExit(
            f"FEHLER: overlay-plan.json referenziert unbekannte Szenen: {sorted(unknown_overlay_scenes)}"
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
        "  audioFile: string;\n"
        "  scenes: SceneRuntime[];\n"
        "};\n\n"
        f"export const project: ObjectTalkProject = {json_literal};\n",
        encoding="utf-8",
    )

    runtime_report = renderer_dir / "runtime-report.json"
    runtime_report.write_text(json.dumps(runtime, ensure_ascii=False, indent=2), encoding="utf-8")

    overlay_count = sum(len(scene.get("overlays", [])) for scene in runtime_scenes)
    print(f"OK: Renderer-Runtime gebaut: {generated_path}")
    print(f"Szenen: {len(runtime_scenes)}")
    print(f"Overlays: {overlay_count}")
    print(f"Dauer: {audio_duration:.2f}s")
    print("Naechster Schritt: cd renderer && npm install && npm run render -- ../PFAD/final-video.mp4")


if __name__ == "__main__":
    main()
