#!/usr/bin/env python3
"""Build every Phase-1 file of a new video from ONE storyboard source.

Usage:
  python tools/build_phase1_package.py youtube-videos/VIDEO

Input (single source of truth, written by the creative director):
  .intern/05_info/storyboard-source.json   (format "storyboard-v2")

Outputs (derived, never edit by hand – edit the storyboard and rebuild):
  01_script/script.txt                          voice-over text, 1:1 copyable
  02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt
  03_export/CAPTION-YOUTUBE.txt                 draft; chapters get real times later
  .intern/VOICEOVER-ZUM-KOPIEREN.txt
  .intern/05_info/phase1-scenes.json
  .intern/05_info/sentence-visual-plan.json
  .intern/05_info/label-plan.json
  .intern/05_info/TITEL-UND-COVER-OPTIONEN.md
  .intern/03_pipeline/ANTIGRAVITY-PROMPT-ZUM-KOPIEREN.txt

Why: in video 010 the derived JSON files were filled mechanically (visual_type
rotating through eight values, learning_goal = copied sentence, 24 invalid
motion names). One authored storyboard prevents such drift.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from script_quality import THRESHOLDS, estimate_seconds

ROOT = Path(__file__).resolve().parents[1]

MAX_SCENE_SECONDS_ESTIMATE = THRESHOLDS["max_scene_seconds_estimate"]
CATEGORIES = {
    "mechanism", "cutaway", "macro", "educational_comparison", "food_structure",
    "process_path", "everyday_context", "human_action", "transition",
}
FRAMINGS = {"none", "hands_or_crop", "partial_person", "whole_person"}
MOTIONS = {"static", "slow-push-in", "slow-pull-out", "pan-left", "pan-right"}
SCALES = {"Alltag", "Lebensmittel", "Körper", "Organ", "Gewebe", "Zelle", "Molekül"}
FUNCTIONS = {"hook", "observation", "trigger", "path", "comparison", "threshold", "wirkung", "result", "transition", "bridge"}
MAX_SCENE_WORDS = 19
MAX_LABELS = 2
MAX_LABEL_WORDS = 3

CANONICAL_STYLE = (
    "Clean Animated Biology Illustration: simplified but recognizable anatomy, smooth organic forms, "
    "clean outlines, soft gradients, subtle depth, bright calm backgrounds, clear biological colors, "
    "low complexity, one dominant biological idea per frame."
)
CANONICAL_NEGATIVE = (
    "No photoreal medical imagery, no medical CGI, no glossy 3D, no feature-animation/Pixar look, "
    "no toy/kids-book look, no corporate infographic, no clutter, no gore, no random icons, no unnecessary text."
)


class StoryboardError(ValueError):
    pass


def words(text: str) -> int:
    return len(str(text).split())


def load_storyboard(project: Path) -> dict:
    path = project / ".intern" / "05_info" / "storyboard-source.json"
    if not path.is_file():
        raise StoryboardError(f"Storyboard fehlt: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("format") != "storyboard-v2":
        raise StoryboardError("storyboard-source.json braucht format=storyboard-v2")
    if str(data.get("status", "")).upper() != "READY":
        raise StoryboardError("Storyboard ist noch Vorlage: status auf READY setzen, wenn alle Szenen geschrieben sind")
    return data


def flat_scenes(storyboard: dict) -> list[tuple[dict, dict]]:
    result = []
    for chapter in storyboard.get("chapters", []):
        for scene in chapter.get("scenes", []):
            result.append((chapter, scene))
    return result


def validate(storyboard: dict) -> list[tuple[dict, dict]]:
    pairs = flat_scenes(storyboard)
    if len(pairs) < 20:
        raise StoryboardError("zu wenige Szenen für ein Longform-Video")
    errors = []
    for chapter in storyboard["chapters"]:
        if chapter.get("function") not in FUNCTIONS:
            errors.append(f"Kapitel {chapter.get('title')!r}: ungültige function")
        if not str(chapter.get("misconception", "")).strip():
            errors.append(f"Kapitel {chapter.get('title')!r}: misconception fehlt")
    for index, (chapter, scene) in enumerate(pairs, 1):
        tag = f"Szene {index}"
        for key in ("speech", "cat", "frame", "scale", "motion", "visual", "shows", "goal"):
            if not str(scene.get(key, "")).strip():
                errors.append(f"{tag}: Feld {key} fehlt")
        if scene.get("cat") not in CATEGORIES:
            errors.append(f"{tag}: ungültige cat {scene.get('cat')!r}")
        if scene.get("frame") not in FRAMINGS:
            errors.append(f"{tag}: ungültiges frame {scene.get('frame')!r}")
        if scene.get("motion") not in MOTIONS:
            errors.append(f"{tag}: ungültige motion {scene.get('motion')!r}")
        if scene.get("scale") not in SCALES:
            errors.append(f"{tag}: ungültige scale {scene.get('scale')!r}")
        if words(scene.get("speech", "")) > MAX_SCENE_WORDS:
            errors.append(f"{tag}: {words(scene['speech'])} Wörter > {MAX_SCENE_WORDS} (Standbild > 7 s)")
        seconds = estimate_seconds(scene.get("speech", ""))
        if seconds > MAX_SCENE_SECONDS_ESTIMATE:
            errors.append(f"{tag}: geschätzt {seconds} s Sprechzeit > {MAX_SCENE_SECONDS_ESTIMATE} s; teilen oder kürzen")
        if len(str(scene.get("visual", ""))) < 60:
            errors.append(f"{tag}: Bildbeschreibung zu unkonkret")
        labels = scene.get("labels", [])
        if not isinstance(labels, list) or len(labels) > MAX_LABELS:
            errors.append(f"{tag}: maximal {MAX_LABELS} Labels")
        for label in labels if isinstance(labels, list) else []:
            if words(label) > MAX_LABEL_WORDS or re.search(r"(?i)\b(bild|szene|scene|image)[_\s-]?\d", label):
                errors.append(f"{tag}: Label {label!r} ungültig")
        if not scene.get("claims"):
            errors.append(f"{tag}: claims fehlen")
    if errors:
        raise StoryboardError("\n- " + "\n- ".join(errors))
    if not storyboard.get("cover", {}).get("title") or len(storyboard["cover"].get("options", [])) != 3:
        raise StoryboardError("cover.title und genau drei cover.options sind Pflicht")
    return pairs


def build_script(pairs: list[tuple[dict, dict]]) -> str:
    paragraphs, current = [], []
    for chapter, scene in pairs:
        current.append(scene["speech"].strip())
        if scene.get("para"):
            paragraphs.append(" ".join(current))
            current = []
    if current:
        paragraphs.append(" ".join(current))
    return "\n\n".join(paragraphs) + "\n"


def scene_difference(prev: dict | None, scene: dict, nxt: dict | None) -> str:
    parts = []
    if prev:
        changed = [k for k in ("cat", "scale", "frame") if prev.get(k) != scene.get(k)]
        parts.append("zum vorherigen Bild: " + (", ".join(changed) + " wechseln" if changed else "neuer Bildinhalt bei gleicher Bildart"))
    if nxt:
        changed = [k for k in ("cat", "scale", "frame") if nxt.get(k) != scene.get(k)]
        parts.append("zum nächsten Bild: " + (", ".join(changed) + " wechseln" if changed else "neuer Bildinhalt bei gleicher Bildart"))
    return "; ".join(parts) or "erstes Bild"


def label_phrase(labels: list[str]) -> str:
    # Placement and contrast rules are stated once in TEXT RULES; keeps the single prompt short enough for Flow.
    if not labels:
        return "TEXT: none."
    return "TEXT: " + " | ".join(labels)


def build_flow_prompt(sb: dict, pairs: list[tuple[dict, dict]]) -> str:
    n = len(pairs)
    cover = sb["cover"]
    flow = sb.get("flow", {})
    lines = [
        f"LEBENSLOGIK | {sb['video_id']} | ONE COMPLETE GOOGLE FLOW PROMPT (text only, no uploads)",
        "",
        f"German YouTube explainer: {sb['working_title']}",
        "Generate still images only, 16:9. The file names below (Bild_XX.png) are INTERNAL production metadata for "
        "saving only. NEVER render production metadata, file names, image or scene numbers, these instructions or any "
        "English words visibly in an image.",
        "",
        "WORKFLOW",
        "1. First create exactly THREE separate cover candidates (three single images, never a collage). Do not ask for "
        "uploads, ZIPs, the script or permission first.",
        '2. Show all three and ask only: "Welches Cover wählst du – 1, 2 oder 3?" Then STOP and wait.',
        "3. The chosen cover is saved separately as COVER.png (YouTube thumbnail). It is NOT a video scene, not Bild_01, "
        "not part of the ZIP and never a style reference.",
        f"4. Right after the choice, without any further question, generate Bild_01–Bild_05 as five separate images, then "
        f"Bild_06–Bild_10 and so on in batches of five until Bild_{n:02d}. Never request all scenes in one batch. If a "
        "platform limit interrupts you, name the exact resume point and continue when the user writes weiter.",
        f"5. Finally zip ONLY Bild_01.png–Bild_{n:02d}.png (no cover). Never claim an image or ZIP exists unless it was "
        "really generated.",
        "",
        "CANONICAL STYLE FOR EVERY IMAGE (inherited from approved video 008)",
        CANONICAL_STYLE,
        CANONICAL_NEGATIVE,
        "",
        "ILLUSTRATION-FIRST ART DIRECTION (Bildregie V2)",
        "- Show the biology itself: organ cutaways, tissue cross-sections, macro views, food interiors, signal pathways "
        "and clear two-state comparisons. People appear only as hands or cropped details unless the scene says "
        "otherwise; adults always fully clothed.",
        "- The main subject fills about two thirds of the frame; one clear focal point; 2–4 key elements; calm negative space.",
        "- Vary the camera from scene to scene: extreme close-up, medium, wide; subject left, right or centered; "
        "cutaway, top view, side view. Neighbouring images must never look alike.",
        "- Rich harmonious palette (coral, salmon, amber, gold, teal, aquamarine, sky blue, leaf green, restrained violet) "
        "on soft gradient backgrounds that change with each scene; never a long row of identical pale mint frames. "
        "Soft layered shading, fine warm outlines, gentle depth, no CGI gloss.",
        "- A chart is allowed only as one clean organic curve or ribbon when a scene asks for it; no dashboards, icon "
        "grids or UI cards.",
        "",
        "COLOR & CONTINUITY KEY FOR THIS VIDEO (identical in every image)",
        flow.get("continuity_key", ""),
        "",
        "TEXT RULES",
        f'- COVER: exactly one visible text block: the German title {cover["title"]} in correct spelling, large bold '
        "clean sans-serif, nothing else (no subtitle, no labels, no numbers, no logos, no quotation marks).",
        "- NORMAL SCENES: each scene ends with TEXT: followed by its only allowed German labels (separated by |). "
        "Render exactly those words (max 2 labels, correct spelling, no quotation marks), each placed close to the "
        "structure it names, thin pointer line only if needed. TEXT: none means no text, letters or numerals at all – "
        "also none on clocks, packages, screens or books.",
        "- Contrast: light background → dark text; dark background → light text. Text sits in calm negative space. "
        "Weak contrast, misspelling or extra text = regenerate.",
        "",
        "SCIENCE & SAFETY",
        "Non-fiction educational illustrations, simplified but anatomically plausible. No gore, no wet realistic tissue, "
        "no body shaming, no brand logos, no sensational medical claims. " + flow.get("topic_safety", "") +
        " If Flow refuses an image, name it and continue with the next; never try to bypass a policy.",
        "",
        "QUALITY CHECK AFTER EVERY BATCH OF FIVE",
        "Each image matches its scene, shows one main idea, stays in the same visual world, differs in composition from "
        "its neighbours, has exactly the listed labels, no leaked metadata or numbers, strong contrast and no AI "
        "artefacts (extra fingers, melted text, impossible anatomy). Replace failures before continuing.",
        "",
        "THREE COVER OPTIONS (exactly one text block each: " + cover["title"] + ")",
    ]
    for index, option in enumerate(cover["options"], 1):
        lines.append(f"COVER {index}: {option}")
    lines += ["", f"SCENE REGISTER – {n} normal video images, generate in batches of five", ""]
    for index, (chapter, scene) in enumerate(pairs, 1):
        if (index - 1) % 5 == 0:
            last = min(index + 4, n)
            lines.append(f"— Batch Bild_{index:02d}–Bild_{last:02d} —")
        lines.append(f"Bild_{index:02d}.png — {scene['visual'].strip()} {label_phrase(scene.get('labels', []))}")
        if index % 5 == 0 or index == n:
            lines.append("")
    lines += [
        f"FINAL CHECK: exactly {n} different accepted normal images Bild_01.png–Bild_{n:02d}.png (no cover inside), "
        "each 16:9. Cover downloaded separately as COVER.png. No MP4, no subtitles, no extra prompt files.",
        "",
    ]
    return "\n".join(lines)


def build_phase1_scenes(sb: dict, pairs: list[tuple[dict, dict]]) -> dict:
    scenes = []
    previous_chapter = None
    for index, (chapter, scene) in enumerate(pairs, 1):
        scenes.append({
            "scene": index,
            "image": f"Bild_{index:02d}",
            "chapter": chapter["title"],
            "chapter_start": chapter is not previous_chapter,
            "speech_section": scene["speech"].strip(),
            "visual_task": scene["visual"].strip(),
            "explanation_visible": scene["shows"].strip(),
            "visual_category": scene["cat"],
            "human_framing": scene["frame"],
            "scale_level": scene["scale"],
            "motion": scene["motion"],
            "labels_de": list(scene.get("labels", [])),
            "labels": list(scene.get("labels", [])),
        })
        previous_chapter = chapter
    return {
        "status": "READY",
        "video_id": sb["video_id"],
        "title": sb["youtube"]["title"],
        "generated_from": "storyboard-source.json",
        "rules": {
            "source": "01_script/script.txt",
            "coverage": "complete-no-gaps-no-overlaps",
            "scene_boundaries": "semantic-visual-beats-from-storyboard",
            "one_main_idea_per_frame": True,
            "prefer_more_images_over_overloaded_frame": True,
            "omit_nonessential_information": True,
            "max_labels_per_normal_image": MAX_LABELS,
            "cover_title_only": True,
            "cover_extra_labels_forbidden": True,
            "text_contrast_required": True,
            "remotion_text_overlays_allowed": False,
            "production_ids_visible_in_images": False,
            "cover_is_scene": False,
            "cover_output": "03_export/COVER.png",
            "visual_mix_v2": True,
        },
        "scenes": scenes,
    }


def build_sentence_plan(pairs: list[tuple[dict, dict]]) -> dict:
    items = []
    flat = [scene for _, scene in pairs]
    for index, (chapter, scene) in enumerate(pairs, 1):
        prev = flat[index - 2] if index > 1 else None
        nxt = flat[index] if index < len(flat) else None
        items.append({
            "id": f"SV_{index:03d}",
            "voiceover_text": scene["speech"].strip(),
            "function": "hook" if index == 1 else scene.get("function", chapter["function"]),
            "learning_goal": scene["goal"].strip(),
            "claim_ids": list(scene["claims"]),
            "scale_level": scene["scale"],
            "new_image_required": True,
            "image_asset_id": f"Bild_{index:02d}",
            "visual_type": scene["cat"],
            "visible_change": scene["shows"].strip(),
            "scene_difference": scene_difference(prev, scene, nxt),
            "labels": list(scene.get("labels", [])),
            "misconception_to_avoid": scene.get("misconception", chapter["misconception"]).strip(),
        })
    return {
        "status": "READY",
        "source_script": "01_script/script.txt",
        "generated_from": "storyboard-source.json",
        "rules": {
            "each_spoken_sentence_or_logical_block_has_visual_plan": True,
            "image_ids_match_phase1_scenes": True,
            "no_estimated_final_timestamps_in_phase1": True,
        },
        "items": items,
    }


def build_label_plan(pairs: list[tuple[dict, dict]]) -> dict:
    return {
        "status": "READY",
        "generated_from": "storyboard-source.json",
        "rules": {
            "language": "de", "prompt_language": "en", "max_labels_per_image": MAX_LABELS,
            "max_words_per_label": MAX_LABEL_WORDS, "prefer_no_label_when_self_explanatory": True,
            "labels_generated_in_flow": True, "regenerate_if_label_wrong": True,
            "cover_title_only": True, "cover_exactly_one_visible_text_block": True,
            "cover_extra_labels_forbidden": True, "text_contrast_required": True,
            "light_background_requires_dark_text": True, "dark_background_requires_light_text": True,
            "no_decorative_quotation_marks": True, "no_asset_ids_visible": True,
            "no_scene_numbers_visible": True, "no_file_names_visible": True,
            "remotion_visible_text_allowed": False, "remotion_text_fallback_allowed": False,
            "cover_is_scene": False, "cover_output": "03_export/COVER.png",
        },
        "images": [
            {"image_asset_id": f"Bild_{i:02d}", "mode": "scene",
             "allowed_visible_text": list(s.get("labels", [])), "labels": list(s.get("labels", []))}
            for i, (_, s) in enumerate(pairs, 1)
        ],
    }


def build_caption(sb: dict) -> str:
    yt = sb["youtube"]
    hashtags = " ".join(yt.get("hashtags", [])[:5])
    return (
        f"TITEL\n{yt['title']}\n\nBESCHREIBUNG\n{yt['description'].strip()}\n\n"
        "KAPITEL\nDie Kapitelzeiten werden nach dem finalen Render aus der echten Timeline eingesetzt "
        "(python tools/export_chapters.py VIDEOORDNER). Keine geschätzten Zeiten.\n\n"
        f"HASHTAGS\n{hashtags}\n"
    )


def build_options_md(sb: dict) -> str:
    yt, cover = sb["youtube"], sb["cover"]
    out = [f"# Titel- und Coveroptionen – {sb['video_id']}", "",
           f"**Empfohlener YouTube-Titel:** {yt['title']}", "", "Alternativen (für spätere A/B-Tests):"]
    out += [f"- {t}" for t in yt.get("title_alternatives", [])]
    out += ["", f"**Covertext (einziger Textblock):** {cover['title']}", "",
            "Covertext ergänzt den Titel, wiederholt ihn nicht. Alle drei Cover haben denselben Text, damit nur die "
            "Bildidee verglichen wird. Tipp: Die zwei nicht gewählten Cover lokal behalten und mit YouTube "
            "„Testen und vergleichen“ gegen das Hauptcover testen, sobald die Funktion im Kanal verfügbar ist.", ""]
    out += [f"- Cover {i}: {o}" for i, o in enumerate(cover["options"], 1)]
    loops = sb.get("open_loops", [])
    if loops:
        out += ["", "## Geplante Open Loops (Spannungsbögen)"]
        out += [f"- Szene {l['setup_scene']} → Auflösung Szene {l['payoff_scene']}: {l.get('question', '')}" for l in loops]
    return "\n".join(out) + "\n"


def repo_relative(project: Path) -> str:
    try:
        return project.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return project.as_posix()


def build_antigravity(sb: dict, n: int, rel: str) -> str:
    vid = sb["video_id"]
    return f"""ANTIGRAVITY-AUFTRAG – PHASE 3 – {vid}

Projekt: {rel}/
Ziel: finales YouTube-Video aus Voice + {n} akzeptierten Google-Flow-Bildern. Skript, Bildreihenfolge und Szenengrenzen NICHT kreativ verändern.

VORAUSSETZUNGEN (vom Nutzer abgelegt)
- Rohe Voice-Datei (mp3/m4a/wav) in 01_script/audio/
- Genau eine Flow-ZIP mit Bild_01.png bis Bild_{n:02d}.png in 02_bildprompts/bilder-zip/
- Gewähltes Cover als 03_export/COVER.png (NICHT Teil des Videos)

ABLAUF
1. python tools/validate_planning_v2.py {rel}
2. python tools/prepare_phase3.py {rel}
   (Voice 1.10x + Pausenkompression → ZIP-Import → Asset-Check → Whisper-Ausrichtung → timeline.json → Untertitel → Kapitel → Renderer-Runtime)
3. Bild-QA aller {n} Bilder in .intern/05_info/image-review.json eintragen (nur echte Sichtprüfung), dann
   python tools/validate_planning_v2.py {rel} --phase2
4. Rendern in renderer/ (1920x1080, 30 fps, h264/aac); danach python tools/qa_final.py <MP4> 01_script/audio/final-voiceover.wav
5. Video komplett ansehen. Verbesserungsbericht nach engine/CONTINUOUS-IMPROVEMENT.md in .intern/05_info/improvement-review.json.

HARTE REGELN
- 100 % Vollbild-Illustration. Remotion erzeugt KEINEN sichtbaren Text; .intern/03_pipeline/overlay-plan.json bleibt DISABLED mit scenes: [].
- Nur erlaubte Bewegungen: static, slow-push-in, slow-pull-out, pan-left, pan-right. Kein Bild länger als 7 Sekunden, kein Bild doppelt.
- Cover ist nur Thumbnail, nie Anfangsszene. Bild_01 ist die erste Videoszene.
- Zeitcodes niemals schätzen: Untertitel und Kapitel kommen nur aus der finalen timeline.json.

EXPORT – GENAU VIER SICHTBARE DATEIEN IN 03_export/
- VIDEO.mp4
- COVER.png
- CAPTION-YOUTUBE.txt (Titel, Beschreibung, Kapitel mit echten Zeiten, max. 5 Hashtags)
- UNTERTITEL-MIT-ZEITEN.txt
Alles Technische (SRT, Renderbericht, QA, timeline.json) nur unter .intern/.
"""


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def neighbour_warnings(pairs: list[tuple[dict, dict]]) -> list[str]:
    """PLANNING-V2 §5: neighbours should differ; identical category+scale+framing is only a hint, not a fail."""
    flat = [scene for _, scene in pairs]
    return [
        f"Bild_{i:02d}/Bild_{i + 1:02d}"
        for i in range(1, len(flat))
        if all(flat[i - 1].get(k) == flat[i].get(k) for k in ("cat", "scale", "frame"))
    ]


STALE_TEMPLATE_NOTE = (
    "# Veraltete Vorlage\n\nDiese Datei stammt aus der alten Projektvorlage und gilt nicht. Der gültige Phase-3-Auftrag "
    "steht in `ANTIGRAVITY-PROMPT-ZUM-KOPIEREN.txt` (erzeugt von `tools/build_phase1_package.py`).\n"
)


def build(project: Path) -> str:
    sb = load_storyboard(project)
    if sb.get("video_id") != project.name:
        raise StoryboardError(
            f"video_id {sb.get('video_id')!r} muss dem Ordnernamen {project.name!r} entsprechen "
            "(sonst zeigen Antigravity-Befehle und Links auf das falsche Projekt)"
        )
    pairs = validate(sb)
    script = build_script(pairs)
    info = project / ".intern" / "05_info"
    write(project / "01_script" / "script.txt", script)
    write(project / ".intern" / "VOICEOVER-ZUM-KOPIEREN.txt", script)
    write(project / "02_bildprompts" / "GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt", build_flow_prompt(sb, pairs))
    write(project / "03_export" / "CAPTION-YOUTUBE.txt", build_caption(sb))
    write(info / "phase1-scenes.json", json.dumps(build_phase1_scenes(sb, pairs), ensure_ascii=False, indent=2) + "\n")
    write(info / "sentence-visual-plan.json", json.dumps(build_sentence_plan(pairs), ensure_ascii=False, indent=2) + "\n")
    write(info / "label-plan.json", json.dumps(build_label_plan(pairs), ensure_ascii=False, indent=2) + "\n")
    write(info / "TITEL-UND-COVER-OPTIONEN.md", build_options_md(sb))
    write(project / ".intern" / "03_pipeline" / "ANTIGRAVITY-PROMPT-ZUM-KOPIEREN.txt", build_antigravity(sb, len(pairs), repo_relative(project)))
    for stale in ("Antigravity-Prompt.md", "pipeline.md"):  # template leftovers that contradict the generated brief
        if (project / ".intern" / "03_pipeline" / stale).is_file():
            write(project / ".intern" / "03_pipeline" / stale, STALE_TEMPLATE_NOTE)
    total_words = words(script)
    labelled = sum(1 for _, s in pairs if s.get("labels"))
    similar = neighbour_warnings(pairs)
    hint = f"; Hinweis: {len(similar)} Nachbarpaare mit gleicher Bildart/Maßstab/Ausschnitt ({', '.join(similar[:6])}{' …' if len(similar) > 6 else ''}) – Bildbeschreibung deutlich unterscheiden" if similar else ""
    return f"OK: {len(pairs)} Szenen, {total_words} Wörter, {labelled} Bilder mit Labels -> {project.name}{hint}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("project", type=Path)
    args = parser.parse_args()
    try:
        print(build(args.project.resolve()))
    except StoryboardError as exc:
        raise SystemExit(f"STORYBOARD FAIL: {exc}")


if __name__ == "__main__":
    main()
