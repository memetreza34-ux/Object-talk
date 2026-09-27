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
- final presentation is 100% full-frame illustration
- Remotion visible text overlays are forbidden
- overlay-plan.json must be empty/disabled
- all viewer-facing text must already be part of accepted Google-Flow images
- production asset IDs and scene numbers must never be rendered visibly
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
    """Fail closed if any Remotion text overlay is planned."""
    project_dir = timeline_path.resolve().parents[2]
    overlay_path = project_dir / "03_pipeline" / "overlay-plan.json"
    if not overlay_path.is_file():
        return

    try:
        payload = json.loads(overlay_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"FEHLER: ungueltiges overlay-plan.json: {exc}")

    scenes = payload.get("scenes", [])
    if not isinstance(scenes, list):
        raise SystemExit("FEHLER: overlay-plan.json: scenes muss eine Liste sein.")

    non_empty: list[int] = []
    for entry in scenes:
        if not isinstance(entry, dict):
            raise SystemExit("FEHLER: overlay-plan.json enthaelt ungueltigen Szeneneintrag.")
        overlays = entry.get("overlays", [])
        if not isinstance(overlays, list):
            raise SystemExit("FEHLER: overlay-plan.json: overlays muss eine Liste sein.")
        if overlays:
            non_empty.append(int(entry.get("scene", 0)))

    if non_empty or scenes:
        raise SystemExit(
            "REMOTION-TEXT FAIL: sichtbare Text-Overlays sind hart deaktiviert. "
            "Remotion darf nur Bilder, Bewegung, Audio, Schnitt und Render erzeugen. "
            "Alle viewer-facing Texte muessen bereits korrekt im akzeptierten Flow-Bild enthalten sein. "
            f"Nicht-leere Overlay-Szenen: {non_empty or [entry.get('scene', 0) for entry in scenes if isinstance(entry, dict)]}."
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
        "presentation": {
            "fullFrameIllustration": True,
            "visibleRemotionText": False,
            "textOverlayCount": 0,
        },
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
        "  maxSceneSeconds: number;\n"
        "  audioFile: string;\n"
        "  presentation: {\n"
        "    fullFrameIllustration: boolean;\n"
        "    visibleRemotionText: false;\n"
        "    textOverlayCount: 0;\n"
        "  };\n"
        "  scenes: SceneRuntime[];\n"
        "};\n\n"
        f"export const project: ObjectTalkProject = {json_literal};\n",
        encoding="utf-8",
    )

    runtime_report = renderer_dir / "runtime-report.json"
    runtime_report.write_text(json.dumps(runtime, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"OK: Renderer-Runtime gebaut: {generated_path}")
    print(f"Szenen: {len(runtime_scenes)}")
    print("Remotion sichtbarer Text: 0 (hart deaktiviert)")
    print("Praesentation: 100% Vollbild-Illustration")
    print(f"Dauer: {audio_duration:.2f}s")
    print(f"Maximale Bilddauer: {MAX_SCENE_SECONDS:.2f}s")
    print("Naechster Schritt: cd renderer && npm install && npm run render -- ../PFAD/final-video.mp4")


if __name__ == "__main__":
    main()
