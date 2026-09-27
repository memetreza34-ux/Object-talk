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
- full-frame illustration remains the default presentation
- Remotion text is allowed only as sparse headings, keywords or callouts
- biological/anatomical labels remain part of the accepted Google-Flow images
- no full voice-over sentences or text-heavy presentation overlays
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
MAX_OVERLAY_WORDS = 6
MAX_OVERLAY_PRESENTATION_SHARE = 0.15
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


def _word_count(text: str) -> int:
    return len([part for part in text.strip().split() if part])


def load_overlay_plan(timeline_path: Path) -> dict[int, list[dict]]:
    """Load and validate sparse presentation overlays.

    The overlay plan is optional. Empty scenes means pure full-frame illustration.
    """
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

    overlays_by_scene: dict[int, list[dict]] = {}

    for scene_entry in scene_entries:
        if not isinstance(scene_entry, dict):
            raise SystemExit("FEHLER: overlay-plan.json enthaelt ungueltigen Szeneneintrag.")

        scene_number = int(scene_entry.get("scene", 0))
        if scene_number <= 0:
            raise SystemExit("FEHLER: overlay-plan.json enthaelt ungueltige Szenennummer.")

        overlays = scene_entry.get("overlays", [])
        if not isinstance(overlays, list):
            raise SystemExit("FEHLER: overlay-plan.json: overlays muss eine Liste sein.")
        if len(overlays) > 1:
            raise SystemExit(
                f"REMOTION-PRAESENTATION FAIL: Szene {scene_number} hat mehr als ein Overlay. "
                "Vollbild-Illustration bleibt Standard; pro Szene maximal ein kurzes Overlay."
            )

        cleaned: list[dict] = []
        for overlay in overlays:
            if not isinstance(overlay, dict):
                raise SystemExit(
                    f"FEHLER: Szene {scene_number} enthaelt einen ungueltigen Overlay-Eintrag."
                )

            kind = str(overlay.get("kind", "heading"))
            text = str(overlay.get("text", "")).strip()
            position = str(overlay.get("position", "top-left"))
            animation = str(overlay.get("animation", "fade-slide"))
            start_fraction = float(overlay.get("startFraction", 0.04))
            duration_fraction = float(overlay.get("durationFraction", 0.28))

            if kind not in ALLOWED_OVERLAY_KINDS:
                raise SystemExit(
                    f"FEHLER: Szene {scene_number}: unbekannter Overlay-Typ {kind!r}."
                )
            if position not in ALLOWED_OVERLAY_POSITIONS:
                raise SystemExit(
                    f"FEHLER: Szene {scene_number}: unbekannte Overlay-Position {position!r}."
                )
            if animation not in ALLOWED_OVERLAY_ANIMATIONS:
                raise SystemExit(
                    f"FEHLER: Szene {scene_number}: unbekannte Overlay-Animation {animation!r}."
                )
            if not text:
                raise SystemExit(f"FEHLER: Szene {scene_number}: Overlay-Text ist leer.")
            if _word_count(text) > MAX_OVERLAY_WORDS:
                raise SystemExit(
                    f"REMOTION-PRAESENTATION FAIL: Szene {scene_number}: {text!r} hat mehr als "
                    f"{MAX_OVERLAY_WORDS} Woerter. Nur kurze Zwischenueberschriften/Key-Facts/Summaries."
                )
            if not 0 <= start_fraction < 1:
                raise SystemExit(
                    f"FEHLER: Szene {scene_number}: startFraction muss zwischen 0 und <1 liegen."
                )
            if not 0 < duration_fraction <= 1:
                raise SystemExit(
                    f"FEHLER: Szene {scene_number}: durationFraction muss zwischen >0 und 1 liegen."
                )
            if start_fraction + duration_fraction > 1.001:
                raise SystemExit(
                    f"FEHLER: Szene {scene_number}: Overlay reicht ueber das Szenenende hinaus."
                )

            cleaned.append(
                {
                    "kind": kind,
                    "text": text,
                    "position": position,
                    "animation": animation,
                    "startFraction": start_fraction,
                    "durationFraction": duration_fraction,
                }
            )

        if cleaned:
            overlays_by_scene[scene_number] = cleaned

    return overlays_by_scene


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

    overlays_by_scene = load_overlay_plan(args.timeline)
    valid_scene_numbers = {int(scene["scene"]) for scene in scenes}
    unknown_overlay_scenes = sorted(set(overlays_by_scene) - valid_scene_numbers)
    if unknown_overlay_scenes:
        raise SystemExit(
            "FEHLER: overlay-plan.json referenziert Szenen, die nicht in timeline.json existieren: "
            f"{unknown_overlay_scenes}"
        )

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
    overlay_visible_seconds = 0.0
    overlay_count = 0

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

        scene_overlays = overlays_by_scene.get(scene_number, [])
        for overlay in scene_overlays:
            overlay_visible_seconds += scene_seconds * float(overlay["durationFraction"])
            overlay_count += 1

        runtime_scenes.append(
            {
                "scene": scene_number,
                "file": f"current/images/{source.name}",
                "startFrame": start_frame,
                "durationInFrames": duration_frames,
                "motion": motion,
                "overlays": scene_overlays,
            }
        )

    if audio_duration > 0:
        overlay_share = overlay_visible_seconds / audio_duration
        if overlay_share > MAX_OVERLAY_PRESENTATION_SHARE + 0.001:
            raise SystemExit(
                "REMOTION-PRAESENTATION FAIL: Text-Overlays belegen zu viel Laufzeit. "
                f"Aktuell {overlay_share * 100:.1f}%, maximal {MAX_OVERLAY_PRESENTATION_SHARE * 100:.0f}%. "
                "Vollbild-Illustration muss Hauptdarsteller bleiben."
            )
    else:
        overlay_share = 0.0

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
            "fullFrameDefault": True,
            "overlayCount": overlay_count,
            "overlayVisibleSeconds": round(overlay_visible_seconds, 3),
            "overlayShare": round(overlay_share, 4),
            "maxOverlayShare": MAX_OVERLAY_PRESENTATION_SHARE,
        },
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
        "  presentation?: {\n"
        "    fullFrameDefault: boolean;\n"
        "    overlayCount: number;\n"
        "    overlayVisibleSeconds: number;\n"
        "    overlayShare: number;\n"
        "    maxOverlayShare: number;\n"
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
    print(f"Remotion-Praesentations-Overlays: {overlay_count}")
    print(f"Overlay-Anteil der Laufzeit: {overlay_share * 100:.1f}%")
    print(f"Dauer: {audio_duration:.2f}s")
    print(f"Maximale Bilddauer: {MAX_SCENE_SECONDS:.2f}s")
    print("Naechster Schritt: cd renderer && npm install && npm run render -- ../PFAD/final-video.mp4")


if __name__ == "__main__":
    main()
