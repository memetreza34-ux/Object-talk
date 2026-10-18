#!/usr/bin/env python3
"""Validate Object-Talk V2 planning and accepted image-review state.

Usage:
  python tools/validate_planning_v2.py youtube-videos/MEIN-VIDEO
  python tools/validate_planning_v2.py youtube-videos/MEIN-VIDEO --phase2

Current channel contract:
- Clean Animated Biology Illustration is the canonical image world.
- Viewer-facing text may only come from accepted Google-Flow images.
- Cover contains exactly one visible text block: title only.
- Normal frames use 0-2 labels maximum; each label max 3 words.
- Visible text must have strong contrast; information density must stay low.
- Production IDs such as Bild_01 / Szene 01 / filenames are metadata only and must never be visible.
- Remotion visible text is forbidden; overlay-plan.json must be empty/disabled.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from urllib.parse import quote
from improvement_loop import check_next
from script_quality import check_project as check_script_quality, ScriptQualityError
from visual_storyboard_gate import check_visual_mix, VisualMixError

IMAGE_ID_RE = re.compile(r"^Bild_\d{2,}$")
PLACEHOLDER_RE = re.compile(r"\[[^\]]+\]|\b(?:TODO|TBD|PENDING)\b", re.IGNORECASE)
VISIBLE_INTERNAL_ID_RE = re.compile(
    r"\b(?:Bild[_\s-]?\d+|Image[_\s-]?\d+|Scene[_\s-]?\d+|Szene[_\s-]?\d+)\b",
    re.IGNORECASE,
)
WEAK_OPENING_PREFIXES = (
    "in diesem video",
    "heute erklaeren wir",
    "heute erklären wir",
    "willkommen",
)
MAX_NORMAL_LABELS = 2
MAX_LABEL_WORDS = 3
ALLOWED_MOTIONS = {"static", "slow-push-in", "slow-pull-out", "pan-left", "pan-right"}


def is_new_video(project: Path) -> bool:
    match = re.match(r"^(\d{3})-", project.name)
    return bool(match) and int(match.group(1)) >= 11


def fail(message: str) -> None:
    raise SystemExit(f"FEHLER: {message}")


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"Datei fehlt: {path}")
    except json.JSONDecodeError as exc:
        fail(f"ungueltiges JSON in {path}: {exc}")


def require_file(path: Path) -> None:
    if not path.is_file():
        fail(f"Datei fehlt: {path}")


def has_placeholder(value: object) -> bool:
    if isinstance(value, str):
        return bool(PLACEHOLDER_RE.search(value))
    if isinstance(value, list):
        return any(has_placeholder(item) for item in value)
    if isinstance(value, dict):
        return any(has_placeholder(item) for item in value.values())
    return False


def word_count(text: str) -> int:
    return len([part for part in str(text).strip().split() if part])


def label_texts(labels: object) -> list[str]:
    if not isinstance(labels, list):
        return []
    result: list[str] = []
    for item in labels:
        if isinstance(item, str):
            text = item.strip()
        elif isinstance(item, dict) and isinstance(item.get("text"), str):
            if item.get("fallback_overlay") is True:
                fail("Remotion darf niemals Label-Fallback sein")
            text = item["text"].strip()
        else:
            fail(f"ungueltiger Label-Eintrag: {item!r}")
        if not text:
            fail("leerer Labeltext ist ungueltig")
        if word_count(text) > MAX_LABEL_WORDS:
            fail(f"Label {text!r} hat mehr als {MAX_LABEL_WORDS} Woerter")
        result.append(text)
    return result


def validate_global_contract(project: Path) -> None:
    repo_root = Path(__file__).resolve().parents[1]
    config_path = repo_root / "config" / "channel.json"
    require_file(config_path)
    config = load_json(config_path)

    visual = config.get("visual_identity", {})
    flow = config.get("flow_prompting", {})
    labels = config.get("labels", {})
    cover = config.get("cover", {})
    presentation = config.get("presentation", {})
    remotion = config.get("remotion", {})

    if visual.get("approved_channel_style") != "Clean Animated Biology Illustration":
        fail("config/channel.json: falsche kanonische Bildwelt")
    if visual.get("written_spec_is_authoritative") is not True:
        fail("config/channel.json: schriftliche Bildwelt muss autoritativ sein")
    if flow.get("never_render_asset_ids_or_scene_numbers") is not True:
        fail("config/channel.json muss sichtbare Asset-/Szenennummern verbieten")
    if int(flow.get("max_labels_per_image", 99)) != MAX_NORMAL_LABELS:
        fail(f"config/channel.json: max_labels_per_image muss {MAX_NORMAL_LABELS} sein")
    if int(flow.get("max_words_per_label", 99)) != MAX_LABEL_WORDS:
        fail(f"config/channel.json: max_words_per_label muss {MAX_LABEL_WORDS} sein")
    if flow.get("prefer_no_label_when_self_explanatory") is not True:
        fail("config/channel.json muss unnoetige Labels vermeiden")
    if flow.get("cover_exactly_one_visible_text_block") is not True:
        fail("config/channel.json muss Cover auf exakt einen sichtbaren Textblock begrenzen")
    if flow.get("cover_title_only") is not True:
        fail("config/channel.json muss Cover title-only setzen")
    if flow.get("cover_extra_labels_forbidden") is not True:
        fail("config/channel.json muss Cover-Zusatzlabels verbieten")
    if flow.get("text_contrast_required") is not True:
        fail("config/channel.json muss starken Textkontrast verlangen")
    if flow.get("light_background_requires_dark_text") is not True:
        fail("config/channel.json muss dunkle Schrift auf hellem Hintergrund verlangen")
    if flow.get("dark_background_requires_light_text") is not True:
        fail("config/channel.json muss helle Schrift auf dunklem Hintergrund verlangen")
    if labels.get("remotion_text_overlays_allowed") is not False:
        fail("config/channel.json muss Remotion-Textoverlays deaktivieren")
    if labels.get("remotion_is_fallback_for_failed_ai_text") is not False:
        fail("Remotion darf kein Text-Fallback fuer Flow sein")
    if int(labels.get("max_per_image_guideline", 99)) != MAX_NORMAL_LABELS:
        fail(f"config/channel.json: labels.max_per_image_guideline muss {MAX_NORMAL_LABELS} sein")
    if int(labels.get("max_words_per_label", 99)) != MAX_LABEL_WORDS:
        fail(f"config/channel.json: labels.max_words_per_label muss {MAX_LABEL_WORDS} sein")
    if labels.get("text_contrast_required") is not True:
        fail("config/channel.json: Label-Kontrast muss Pflicht sein")
    if cover.get("title_only") is not True:
        fail("config/channel.json: cover.title_only muss true sein")
    if int(cover.get("visible_text_blocks", 99)) != 1:
        fail("config/channel.json: Cover muss exakt einen sichtbaren Textblock erlauben")
    if cover.get("extra_labels_allowed") is not False:
        fail("config/channel.json: Cover darf keine Zusatzlabels erlauben")
    if cover.get("text_contrast_required") is not True:
        fail("config/channel.json: Cover-Textkontrast muss Pflicht sein")
    if presentation.get("full_frame_illustration_share_target") != "100%":
        fail("Praesentation muss auf 100% Vollbild-Illustration gesetzt sein")
    if presentation.get("remotion_visible_text_allowed") is not False:
        fail("Praesentation muss sichtbaren Remotion-Text verbieten")
    if presentation.get("asset_ids_visible_in_final_video") is not False:
        fail("Asset-IDs muessen im finalen Video unsichtbar sein")
    if presentation.get("scene_numbers_visible_in_final_video") is not False:
        fail("Szenennummern muessen im finalen Video unsichtbar sein")
    if remotion.get("text_strategy") != "NO_VISIBLE_TEXT":
        fail("Remotion text_strategy muss NO_VISIBLE_TEXT sein")
    if remotion.get("text_generation_allowed") is not False:
        fail("Remotion-Textgenerierung muss hart deaktiviert sein")
    if remotion.get("text_overlay_allowed") is not False:
        fail("Remotion-Textoverlays muessen hart deaktiviert sein")
    if remotion.get("overlay_plan_must_be_empty") is not True:
        fail("Remotion overlay_plan_must_be_empty muss true sein")

    overlay_path = ((project / ".intern" / "03_pipeline" / "overlay-plan.json") if (project / ".intern" / "03_pipeline").is_dir() else (project / "03_pipeline" / "overlay-plan.json"))
    if overlay_path.is_file():
        overlay = load_json(overlay_path)
        scenes = overlay.get("scenes", [])
        if not isinstance(scenes, list):
            fail("overlay-plan.json: scenes muss eine Liste sein")
        if scenes:
            fail("overlay-plan.json muss leer bleiben; Remotion sichtbarer Text ist verboten")
        status = str(overlay.get("status", "")).upper()
        if status not in {"DISABLED", "TEMPLATE", ""}:
            fail("overlay-plan.json muss DISABLED sein")


def validate_phase1(project: Path) -> set[str]:
    script_path = project / "01_script" / "script.txt"
    internal_dir = (project / ".intern") if (project / ".intern" / "05_info").is_dir() else project
    simplified = internal_dir != project
    mechanism_path = internal_dir / "05_info" / "mechanism-map.md"
    sentence_plan_path = internal_dir / "05_info" / "sentence-visual-plan.json"
    scenes_path = internal_dir / "05_info" / "phase1-scenes.json"
    label_plan_path = internal_dir / "05_info" / "label-plan.json"
    if not label_plan_path.is_file():  # backwards compatibility: older video projects
        label_plan_path = project / "02_bildprompts" / "label-plan.json"
    flow_prompt_path = project / "02_bildprompts" / "GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt"

    for path in (
        script_path,
        mechanism_path,
        sentence_plan_path,
        scenes_path,
        label_plan_path,
        flow_prompt_path,
    ):
        require_file(path)

    validate_global_contract(project)

    mechanism_text = mechanism_path.read_text(encoding="utf-8")
    if PLACEHOLDER_RE.search(mechanism_text):
        fail("Mechanism Map enthaelt noch Platzhalter")

    flow_prompt_text = flow_prompt_path.read_text(encoding="utf-8").lower()
    if "never" not in flow_prompt_text or "production" not in flow_prompt_text:
        fail("Flow-Prompt muss Produktions-IDs ausdruecklich als unsichtbar markieren")
    if "exactly one visible text block" not in flow_prompt_text:
        fail("Flow-Prompt muss Cover auf exakt einen sichtbaren Textblock begrenzen")
    if "dark" not in flow_prompt_text or "light" not in flow_prompt_text:
        fail("Flow-Prompt muss Textkontrast hell/dunkel ausdruecklich regeln")

    sentence_plan = load_json(sentence_plan_path)
    if str(sentence_plan.get("status", "")).upper() in {"TEMPLATE", "PENDING", ""}:
        fail("sentence-visual-plan.json ist nicht READY")
    items = sentence_plan.get("items")
    if not isinstance(items, list) or not items:
        fail("sentence-visual-plan.json enthaelt keine Items")

    required_item_keys = {
        "id",
        "voiceover_text",
        "function",
        "learning_goal",
        "claim_ids",
        "scale_level",
        "new_image_required",
        "image_asset_id",
        "visual_type",
        "visible_change",
        "scene_difference",
        "labels",
        "misconception_to_avoid",
    }

    first = items[0]
    if not isinstance(first, dict) or str(first.get("function", "")).lower() != "hook":
        fail("Der erste Sentence-Visual-Beat muss function='hook' besitzen")
    first_text = str(first.get("voiceover_text", "")).strip().lower()
    if not first_text:
        fail("Hook-Text fehlt")
    if any(first_text.startswith(prefix) for prefix in WEAK_OPENING_PREFIXES):
        fail("Script startet mit schwachem Intro statt Neugier-Hook")

    sentence_image_ids: set[str] = set()
    for index, item in enumerate(items, start=1):
        if not isinstance(item, dict):
            fail(f"Sentence-Visual-Item {index} ist kein Objekt")
        missing = required_item_keys - item.keys()
        if missing:
            fail(f"Sentence-Visual-Item {index} fehlen Felder: {sorted(missing)}")
        if has_placeholder(item):
            fail(f"Sentence-Visual-Item {index} enthaelt Platzhalter")
        image_id = item.get("image_asset_id")
        if not isinstance(image_id, str) or not IMAGE_ID_RE.match(image_id):
            fail(f"ungueltige image_asset_id in Item {index}: {image_id!r}")
        sentence_image_ids.add(image_id)
        labels_for_item = item.get("labels", [])
        if not isinstance(labels_for_item, list) or len(labels_for_item) > MAX_NORMAL_LABELS:
            fail(f"Sentence-Visual-Item {index}: maximal {MAX_NORMAL_LABELS} Labels")
        for label in labels_for_item:
            if not isinstance(label, str) or not label.strip():
                fail(f"Sentence-Visual-Item {index}: ungueltiges Label")
            if word_count(label) > MAX_LABEL_WORDS:
                fail(f"Sentence-Visual-Item {index}: Label {label!r} hat mehr als {MAX_LABEL_WORDS} Woerter")

    scene_payload = load_json(scenes_path)
    if str(scene_payload.get("status", "")).upper() in {"TEMPLATE", "PENDING", ""}:
        fail("phase1-scenes.json ist nicht READY")
    scenes = scene_payload.get("scenes")
    if not isinstance(scenes, list) or not scenes:
        fail("phase1-scenes.json enthaelt keine Szenen")

    rules = scene_payload.get("rules", {})
    if simplified and rules.get("cover_is_scene") is not False:
        fail("Im neuen 3-Ordner-Format muss das Cover SEPARAT vom Video liegen")
    if not isinstance(rules, dict):
        fail("phase1-scenes.json: rules muss Objekt sein")
    if rules.get("remotion_text_overlays_allowed") is not False:
        fail("phase1-scenes.json muss remotion_text_overlays_allowed=false setzen")
    if rules.get("production_ids_visible_in_images") is not False:
        fail("phase1-scenes.json muss sichtbare Produktions-IDs verbieten")
    if rules.get("one_main_idea_per_frame") is not True:
        fail("phase1-scenes.json muss one_main_idea_per_frame=true setzen")
    if int(rules.get("max_labels_per_normal_image", 99)) != MAX_NORMAL_LABELS:
        fail(f"phase1-scenes.json muss max_labels_per_normal_image={MAX_NORMAL_LABELS} setzen")
    if rules.get("cover_title_only") is not True:
        fail("phase1-scenes.json muss cover_title_only=true setzen")
    if rules.get("text_contrast_required") is not True:
        fail("phase1-scenes.json muss text_contrast_required=true setzen")

    scene_ids: list[str] = []
    for index, scene in enumerate(scenes, start=1):
        if not isinstance(scene, dict):
            fail(f"phase1-scenes.json: Szene {index} ist ungueltig")
        if int(scene.get("scene", 0)) != index:
            fail(f"phase1-scenes.json: erwartete Szene {index}")
        expected_id = f"Bild_{index:02d}"
        if scene.get("image") != expected_id:
            fail(f"Szene {index}: erwartetes {expected_id}, gefunden {scene.get('image')!r}")
        labels_de = scene.get("labels_de", [])
        if not isinstance(labels_de, list) or len(labels_de) > MAX_NORMAL_LABELS:
            fail(f"Szene {index}: labels_de darf maximal {MAX_NORMAL_LABELS} Eintraege enthalten")
        for label in labels_de:
            if not isinstance(label, str) or not label.strip():
                fail(f"Szene {index}: ungueltiges Label")
            if word_count(label) > MAX_LABEL_WORDS:
                fail(f"Szene {index}: Label {label!r} hat mehr als {MAX_LABEL_WORDS} Woerter")
        if index == 1 and labels_de and not simplified:
            fail("Cover-Szene darf keine labels_de enthalten")
        scene_ids.append(expected_id)

    scene_id_set = set(scene_ids)
    if len(scene_id_set) != len(scene_ids):
        fail("phase1-scenes.json enthaelt doppelte Bild-IDs")
    if sentence_image_ids - scene_id_set:
        fail(f"Sentence-Visual-Bilder fehlen im Szenenplan: {sorted(sentence_image_ids - scene_id_set)}")

    label_plan = load_json(label_plan_path)
    if str(label_plan.get("status", "")).upper() in {"TEMPLATE", "PENDING", ""}:
        fail("label-plan.json ist nicht READY")
    label_rules = label_plan.get("rules", {})
    if not isinstance(label_rules, dict):
        fail("label-plan.json: rules muss Objekt sein")
    if label_rules.get("no_asset_ids_visible") is not True:
        fail("label-plan.json muss no_asset_ids_visible=true setzen")
    if label_rules.get("remotion_visible_text_allowed") is not False:
        fail("label-plan.json muss Remotion sichtbaren Text verbieten")
    if label_rules.get("remotion_text_fallback_allowed") is not False:
        fail("label-plan.json muss Remotion-Text-Fallback verbieten")
    if int(label_rules.get("max_labels_per_image", 99)) != MAX_NORMAL_LABELS:
        fail(f"label-plan.json muss max_labels_per_image={MAX_NORMAL_LABELS} setzen")
    if int(label_rules.get("max_words_per_label", 99)) != MAX_LABEL_WORDS:
        fail(f"label-plan.json muss max_words_per_label={MAX_LABEL_WORDS} setzen")
    if label_rules.get("cover_title_only") is not True:
        fail("label-plan.json muss cover_title_only=true setzen")
    if label_rules.get("cover_exactly_one_visible_text_block") is not True:
        fail("label-plan.json muss Cover auf exakt einen sichtbaren Textblock begrenzen")
    if label_rules.get("text_contrast_required") is not True:
        fail("label-plan.json muss text_contrast_required=true setzen")
    if label_rules.get("prefer_no_label_when_self_explanatory") is not True:
        fail("label-plan.json muss unnoetige Labels vermeiden")

    if simplified and label_rules.get("cover_is_scene") is not False:
        fail("Bildlabel-Plan muss Cover außerhalb der Videoszenen speichern")
    entries = label_plan.get("images")
    if not isinstance(entries, list):
        fail("label-plan.json: images muss Liste sein")

    planned: set[str] = set()
    for entry in entries:
        if not isinstance(entry, dict):
            fail("label-plan.json enthaelt ungueltigen Eintrag")
        image_id = entry.get("image_asset_id")
        if image_id not in scene_id_set:
            fail(f"Label-Plan referenziert unbekanntes Bild: {image_id}")
        if image_id in planned:
            fail(f"Label-Plan enthaelt doppelten Eintrag fuer {image_id}")
        planned.add(image_id)

        allowed = entry.get("allowed_visible_text", [])
        if not isinstance(allowed, list):
            fail(f"{image_id}: allowed_visible_text muss Liste sein")
        if any(not isinstance(text, str) or not text.strip() for text in allowed):
            fail(f"{image_id}: allowed_visible_text enthaelt ungueltigen Text")
        if any(VISIBLE_INTERNAL_ID_RE.search(text) for text in allowed):
            fail(f"{image_id}: interne Produktions-ID steht in allowed_visible_text")

        texts = label_texts(entry.get("labels", []))
        if len(texts) > MAX_NORMAL_LABELS:
            fail(f"{image_id}: maximal {MAX_NORMAL_LABELS} Labels erlaubt")
        if any(VISIBLE_INTERNAL_ID_RE.search(text) for text in texts):
            fail(f"{image_id}: internes Produktions-ID-Label ist verboten")

        if simplified and image_id == "Bild_01" and entry.get("mode") in {"cover", "cover-hook"}:
            fail("Bild_01 muss eine normale Szene sein, nicht das Cover")
        if image_id == "Bild_01" and not simplified:
            if texts:
                fail("Bild_01/Cover darf keine Labels enthalten")
            if len(allowed) != 1:
                fail("Bild_01/Cover muss exakt einen sichtbaren Textblock enthalten")
            if entry.get("mode") not in {"cover", "cover-hook"}:
                fail("Bild_01 muss als cover/cover-hook markiert sein")
        else:
            if len(allowed) > MAX_NORMAL_LABELS:
                fail(f"{image_id}: maximal {MAX_NORMAL_LABELS} sichtbare Labeltexte erlaubt")
            if sorted(texts) != sorted(allowed):
                fail(f"{image_id}: Labels und allowed_visible_text stimmen nicht ueberein")

    if planned != scene_id_set:
        fail(
            f"Label-Plan muss exakt alle Bilder abdecken. Fehlend={sorted(scene_id_set - planned)}, "
            f"extra={sorted(planned - scene_id_set)}"
        )

    test_mode_path = internal_dir / "05_info" / "test-mode.json"
    if test_mode_path.is_file():
        test_mode = load_json(test_mode_path)
        expected_images = test_mode.get("expected_images")
        if expected_images is not None and int(expected_images) != len(scene_ids):
            fail(f"test-mode.json expected_images={expected_images}, geplant sind {len(scene_ids)}")

    print(f"V2-PHASE-1-PASS: {project}")
    print(f"  Szenen/Bilder: {len(scene_id_set)}")
    print("  Cover: exakt ein Textblock / title-only")
    print(f"  Normale Labels: maximal {MAX_NORMAL_LABELS}, je maximal {MAX_LABEL_WORDS} Woerter")
    print("  Textkontrast: Pflicht")
    print("  Remotion sichtbarer Text: 0 (hart deaktiviert)")
    print("  Produktions-IDs im finalen Bild: verboten")
    return scene_id_set


def validate_phase2(project: Path, expected_ids: set[str]) -> None:
    internal_dir = (project / ".intern") if (project / ".intern" / "05_info").is_dir() else project
    simplified = internal_dir != project
    review_path = internal_dir / "05_info" / "image-review.json"
    images_dir = internal_dir / "03_pipeline" / "images"
    if not review_path.is_file():  # backwards compatibility: older video projects
        review_path = project / "02_bildprompts" / "image-review.json"
        images_dir = project / "02_bildprompts" / "images"
    require_file(review_path)
    if not images_dir.is_dir():
        fail(f"finaler Bilderordner fehlt: {images_dir}")
    if simplified and not (project / "03_export" / "COVER.png").is_file():
        fail("Cover fehlt separat unter 03_export/COVER.png; NICHT als Bild_01 einsetzen")

    review = load_json(review_path)
    status = str(review.get("status", "")).upper()
    if status in {"TEMPLATE", "PENDING_IMAGES", "PENDING", ""}:
        fail(f"image-review.json ist noch nicht final: status={status or 'LEER'}")

    entries = review.get("images")
    if not isinstance(entries, list) or not entries:
        fail("image-review.json enthaelt keine Bildreviews")

    reviewed: set[str] = set()
    numeric_min_8 = (
        "scientific_accuracy",
        "voiceover_match",
        "immediate_clarity",
        "style_continuity",
        "composition",
        "complexity_control",
        "label_accuracy",
        "overall_score",
    )
    required_pass_fields = (
        "visible_text_whitelist",
        "text_contrast",
        "information_density",
        "label_count",
        "label_readability",
        "no_unnecessary_text",
        "no_visible_asset_id",
        "no_visible_scene_number",
        "no_visible_filename_or_prompt_heading",
        "single_retained_asset_for_scene",
        "ai_artifact_check",
    )

    for entry in entries:
        if not isinstance(entry, dict):
            fail("image-review.json enthaelt ungueltigen Eintrag")
        image_id = entry.get("image_asset_id")
        if image_id not in expected_ids:
            fail(f"Bildreview referenziert unbekanntes Bild: {image_id}")
        if image_id in reviewed:
            fail(f"mehrfacher retained Review fuer {image_id}")
        reviewed.add(image_id)

        require_file(images_dir / f"{image_id}.png")

        if entry.get("decision") != "ACCEPT":
            fail(f"{image_id}: Bild ist nicht ACCEPT")

        for field in required_pass_fields:
            if entry.get(field) != "PASS":
                fail(f"{image_id}: {field} muss PASS sein")

        if image_id == "Bild_01" and not simplified:
            if entry.get("cover_title_only") != "PASS":
                fail("Bild_01: cover_title_only muss PASS sein")
            if entry.get("cover_exactly_one_visible_text_block") != "PASS":
                fail("Bild_01: cover_exactly_one_visible_text_block muss PASS sein")

        for key in numeric_min_8:
            value = entry.get(key)
            if not isinstance(value, (int, float)) or value < 8.0:
                fail(f"{image_id}: {key} muss mindestens 8.0 sein")

        scene_difference = entry.get("scene_difference")
        if isinstance(scene_difference, str):
            if scene_difference.upper() not in {"PASS", "OK"}:
                fail(f"{image_id}: scene_difference nicht bestanden")
        elif isinstance(scene_difference, (int, float)):
            if scene_difference < 8.0:
                fail(f"{image_id}: scene_difference muss mindestens 8.0 sein")
        else:
            fail(f"{image_id}: scene_difference fehlt")

    if reviewed != expected_ids:
        fail(f"Bildreviews fehlen fuer: {sorted(expected_ids - reviewed)}")

    actual = {path.stem for path in images_dir.glob("Bild_*.png")}
    if actual != expected_ids:
        fail(
            f"finaler Bilderordner stimmt nicht mit Planung ueberein. "
            f"Fehlend={sorted(expected_ids - actual)}, extra={sorted(actual - expected_ids)}"
        )

    print(f"V2-PHASE-2-PASS: {project}")
    print(f"  akzeptierte Bilder: {len(reviewed)}")
    print("  Separate cover / title-only, Textkontrast und Informationsdichte bestaetigt" if simplified else "  Cover title-only, Textkontrast und Informationsdichte bestaetigt")
    print("  keine sichtbaren Produktions-IDs bestaetigt")
    print("  Remotion-Text bleibt deaktiviert")



def print_phase1_tablet_links(project: Path) -> None:
    """Print the two clickable copy links after *validated* Phase 1, not a generic repo link.

    This helper is private to technical tools; it does not add user-facing files.
    """
    repository_root = Path(__file__).resolve().parents[1]
    try:
        relative_project = project.resolve().relative_to(repository_root).as_posix()
    except ValueError:
        print("PHASE-1-HANDOFF: Projekt ausserhalb dieses Repositories; keine GitHub-Links geraten.")
        return
    if relative_project.startswith("examples/"):
        print("PHASE-1-HANDOFF: Musterbeispiel, keine Produktion. Keine Direktlinks ausgeben.")
        return
    script = project / "01_script" / "script.txt"
    flow_prompt = project / "02_bildprompts" / "GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt"
    if not script.is_file() or not flow_prompt.is_file():
        print("PHASE-1-HANDOFF: Skript oder Flow-Datei fehlt. Keine Direktlinks ausgeben.")
        return

    prefix = "https://github.com/memetreza34-ux/Object-talk/blob/main/"
    script_url = prefix + quote(relative_project + "/01_script/script.txt", safe="/")
    flow_url = prefix + quote(relative_project + "/02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt", safe="/")
    print()
    print("PHASE-1-HANDOFF (in Chat-Antwort IMMER beide anklickbaren Links ausgeben):")
    print(f"[Google-Flow-Prompt öffnen]({flow_url})")
    print(f"[Voice-over-Skript öffnen]({script_url})")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("project", help="Pfad zum Video-Projekt")
    parser.add_argument("--phase2", action="store_true", help="zusaetzlich finale Bildreviews und Assets pruefen")
    args = parser.parse_args()

    project = Path(args.project).resolve()
    if not project.is_dir():
        fail(f"Projektordner nicht gefunden: {project}")

    try:
        improvement_status = check_next(project)
    except ValueError as exc:
        fail(str(exc))
    print(f"IMPROVEMENT-PRIORITY: {improvement_status}")
    expected = validate_phase1(project)
    # New episodes only: enforce the 010 feedback on visual planning before Phase-1 links.
    scene_plan = project / ".intern" / "05_info" / "phase1-scenes.json"
    if scene_plan.is_file():
        try:
            channel_config = load_json(Path(__file__).resolve().parents[1] / "config" / "channel.json")
            prompt = (project / "02_bildprompts" / "GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt").read_text(encoding="utf-8")
            visual_status = check_visual_mix(
                project, load_json(scene_plan), prompt, channel_config.get("visual_storytelling_v2", {})
            )
        except (VisualMixError, FileNotFoundError, UnicodeError) as exc:
            fail(f"Neue Bildregie: {exc}")
        print(f"ILLUSTRATION-FIRST: {visual_status}")
        if is_new_video(project):
            # 010 shipped 24 motion names the renderer does not know; catch that in Phase 1, not at render time.
            bad = sorted({str(s.get("motion")) for s in load_json(scene_plan).get("scenes", []) if s.get("motion") not in ALLOWED_MOTIONS})
            if bad:
                fail(f"phase1-scenes.json: unbekannte Kamerabewegungen {bad}; erlaubt sind {sorted(ALLOWED_MOTIONS)}")
    try:
        print(f"SKRIPT-QUALITÄT: {check_script_quality(project)}")
    except (ScriptQualityError, ValueError) as exc:
        fail(f"Skript-Qualität: {exc}")
    print_phase1_tablet_links(project)
    if args.phase2:
        validate_phase2(project, expected)


if __name__ == "__main__":
    main()
