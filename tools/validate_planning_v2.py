#!/usr/bin/env python3
"""Validate Object-Talk planning and accepted image-review state.

Usage:
  python tools/validate_planning_v2.py youtube-videos/MEIN-VIDEO
  python tools/validate_planning_v2.py youtube-videos/MEIN-VIDEO --phase2

Current channel rules:
- Clean Animated Biology Illustration is the canonical image world.
- biological labels are generated in Google Flow.
- full-frame illustration remains the default presentation.
- sparse Remotion headings/key-facts/summaries are allowed through overlay-plan.json.
- Remotion must never repair biological labels or turn the video into a text-heavy layout.
"""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
from pathlib import Path

IMAGE_ID_RE = re.compile(r"^Bild_\d{2,}$")
ASSET_ID_TEXT_RE = re.compile(r"\b(?:Bild[_ ]?\d+|Scene[_ ]?\d+|Image[_ ]?\d+)\b", re.IGNORECASE)
PLACEHOLDER_RE = re.compile(r"\[[^\]]+\]|\b(?:TODO|TBD|PENDING)\b", re.IGNORECASE)
WEAK_OPENING_PREFIXES = (
    "in diesem video",
    "heute erklaeren wir",
    "heute erklären wir",
    "willkommen",
)
ALLOWED_OVERLAY_KINDS = {"heading", "keyword", "callout"}
ALLOWED_OVERLAY_POSITIONS = {"top-left", "top-center", "bottom-left", "center"}
ALLOWED_OVERLAY_ANIMATIONS = {"fade-slide", "pop", "underline"}
MAX_OVERLAY_WORDS = 6


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"FEHLER: Datei fehlt: {path}")
    except json.JSONDecodeError as exc:
        raise SystemExit(f"FEHLER: ungueltiges JSON in {path}: {exc}")


def require_file(path: Path) -> None:
    if not path.is_file():
        raise SystemExit(f"FEHLER: Datei fehlt: {path}")


def fail(message: str) -> None:
    raise SystemExit(f"FEHLER: {message}")


def has_placeholder(value: object) -> bool:
    if isinstance(value, str):
        return bool(PLACEHOLDER_RE.search(value))
    if isinstance(value, list):
        return any(has_placeholder(item) for item in value)
    if isinstance(value, dict):
        return any(has_placeholder(item) for item in value.values())
    return False


def normalize_visible_text(value: str) -> str:
    value = unicodedata.normalize("NFKC", str(value)).casefold().replace("ß", "ss")
    return " ".join("".join(ch if ch.isalnum() else " " for ch in value).split())


def word_count(text: str) -> int:
    return len([part for part in text.strip().split() if part])


def extract_label_texts(labels: object, image_id: str) -> list[str]:
    if not isinstance(labels, list):
        fail(f"{image_id}: labels muss eine Liste sein")
    if len(labels) > 3:
        fail(f"{image_id}: maximal 3 biologische Labels sind erlaubt")

    result: list[str] = []
    for label in labels:
        if isinstance(label, str):
            text = label.strip()
        elif isinstance(label, dict):
            text = str(label.get("text", "")).strip()
            if label.get("fallback_overlay") is True:
                fail(f"{image_id}: Remotion darf kein Fallback fuer falsche Flow-Labels sein")
        else:
            fail(f"{image_id}: ungueltiger Label-Eintrag")

        if not text:
            fail(f"{image_id}: leerer Labeltext")
        if ASSET_ID_TEXT_RE.search(text):
            fail(f"{image_id}: interner Asset-/Szenenname darf nicht sichtbar sein: {text!r}")
        result.append(text)
    return result


def validate_channel_config(repo_root: Path) -> None:
    config_path = repo_root / "config" / "channel.json"
    require_file(config_path)
    config = load_json(config_path)

    visual = config.get("visual_identity", {})
    flow = config.get("flow_prompting", {})
    labels = config.get("labels", {})
    presentation = config.get("presentation", {})
    remotion = config.get("remotion", {})

    if not isinstance(visual, dict) or not str(visual.get("status", "")).startswith("APPROVED"):
        fail("config/channel.json: visuelle Kanalwelt ist nicht als APPROVED markiert")
    if visual.get("approved_channel_style") != "Clean Animated Biology Illustration":
        fail("config/channel.json: falsche oder fehlende kanonische Bildwelt")
    if visual.get("written_spec_is_authoritative") is not True:
        fail("config/channel.json: schriftliche Bildwelt muss autoritativ sein")
    if visual.get("final_image_generation_allowed") is not True:
        fail("config/channel.json: finale Bildgeneration ist nicht freigegeben")

    for key in ("canonical_spec", "flow_style_block"):
        rel = visual.get(key)
        if not isinstance(rel, str) or not rel.strip() or not (repo_root / rel).is_file():
            fail(f"config/channel.json: {key} fehlt oder zeigt auf keine Datei")

    if flow.get("instruction_language") != "en":
        fail("Flow-Prompt-Anweisungen muessen Englisch sein")
    if flow.get("visible_text_language") != "de":
        fail("sichtbarer Viewer-Text muss Deutsch sein")
    if flow.get("labels_generated_in_flow") is not True:
        fail("biologische Labels muessen in Google Flow erzeugt werden")
    if flow.get("generate_each_image_individually") is not True:
        fail("Bilder muessen einzeln erzeugt werden")
    if flow.get("duplicate_image_reuse_allowed") is not False:
        fail("Bildduplikate duerfen nicht als Szenenersatz erlaubt sein")

    if labels.get("language") != "de":
        fail("Label-Sprache muss de sein")
    if int(labels.get("max_per_image_guideline", 99)) > 3:
        fail("max_per_image_guideline darf hoechstens 3 sein")
    if "GOOGLE_FLOW" not in str(labels.get("final_rendering_strategy", "")):
        fail("biologische Labels muessen final aus Google Flow kommen")

    if presentation.get("keep_illustration_full_frame_by_default") is not True:
        fail("Vollbild-Illustration muss Praesentationsstandard bleiben")
    if presentation.get("biology_labels_remain_in_flow") is not True:
        fail("Praesentationssystem darf biologische Labels nicht aus Flow herausverlagern")

    if remotion.get("text_strategy") != "SELECTIVE_HEADINGS_KEYFACTS_SUMMARY_ONLY":
        fail("Remotion-Textstrategie muss selektiv auf Headings/Key-Facts/Summary begrenzt sein")
    if int(remotion.get("max_words_per_overlay", 99)) > MAX_OVERLAY_WORDS:
        fail(f"Remotion-Overlay darf hoechstens {MAX_OVERLAY_WORDS} Woerter erlauben")
    if remotion.get("full_voiceover_sentences_forbidden") is not True:
        fail("ganze Voice-over-Saetze muessen in Remotion verboten sein")


def validate_overlay_plan(project: Path, scene_numbers: set[int]) -> int:
    overlay_path = project / "03_pipeline" / "overlay-plan.json"
    if not overlay_path.is_file():
        return 0

    payload = load_json(overlay_path)
    scenes = payload.get("scenes", [])
    if not isinstance(scenes, list):
        fail("overlay-plan.json: scenes muss eine Liste sein")

    overlay_count = 0
    used_scenes: set[int] = set()

    for entry in scenes:
        if not isinstance(entry, dict):
            fail("overlay-plan.json enthaelt ungueltigen Szeneneintrag")
        scene = int(entry.get("scene", 0))
        if scene not in scene_numbers:
            fail(f"overlay-plan.json referenziert unbekannte Szene: {scene}")
        if scene in used_scenes:
            fail(f"overlay-plan.json enthaelt Szene {scene} mehrfach")
        used_scenes.add(scene)

        overlays = entry.get("overlays", [])
        if not isinstance(overlays, list):
            fail(f"overlay-plan.json Szene {scene}: overlays muss eine Liste sein")
        if len(overlays) > 1:
            fail(f"Szene {scene}: maximal ein selektives Remotion-Overlay erlaubt")

        for overlay in overlays:
            if not isinstance(overlay, dict):
                fail(f"Szene {scene}: ungueltiger Overlay-Eintrag")
            kind = str(overlay.get("kind", ""))
            text = str(overlay.get("text", "")).strip()
            position = str(overlay.get("position", ""))
            animation = str(overlay.get("animation", ""))
            try:
                start = float(overlay.get("startFraction"))
                duration = float(overlay.get("durationFraction"))
            except (TypeError, ValueError):
                fail(f"Szene {scene}: startFraction/durationFraction ungueltig")

            if kind not in ALLOWED_OVERLAY_KINDS:
                fail(f"Szene {scene}: ungueltiger Overlay-Typ {kind!r}")
            if position not in ALLOWED_OVERLAY_POSITIONS:
                fail(f"Szene {scene}: ungueltige Overlay-Position {position!r}")
            if animation not in ALLOWED_OVERLAY_ANIMATIONS:
                fail(f"Szene {scene}: ungueltige Overlay-Animation {animation!r}")
            if not text:
                fail(f"Szene {scene}: Overlay-Text ist leer")
            if word_count(text) > MAX_OVERLAY_WORDS:
                fail(f"Szene {scene}: Overlay hat mehr als {MAX_OVERLAY_WORDS} Woerter")
            if ASSET_ID_TEXT_RE.search(text):
                fail(f"Szene {scene}: interner Asset-/Szenenname im Overlay")
            if not 0 <= start < 1 or not 0 < duration <= 1 or start + duration > 1.001:
                fail(f"Szene {scene}: ungueltige Overlay-Zeitfraktionen")
            overlay_count += 1

    return overlay_count


def validate_phase1(project: Path) -> set[str]:
    repo_root = Path(__file__).resolve().parents[1]
    validate_channel_config(repo_root)

    mechanism = project / "05_info" / "mechanism-map.md"
    sentence_plan_path = project / "05_info" / "sentence-visual-plan.json"
    label_plan_path = project / "02_bildprompts" / "label-plan.json"
    scenes_path = project / "05_info" / "phase1-scenes.json"
    flow_prompt_txt = project / "02_bildprompts" / "GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt"

    for path in (mechanism, sentence_plan_path, label_plan_path, scenes_path, flow_prompt_txt):
        require_file(path)

    mechanism_text = mechanism.read_text(encoding="utf-8")
    if PLACEHOLDER_RE.search(mechanism_text):
        fail(f"Mechanism Map enthaelt noch Platzhalter: {mechanism}")

    sentence_plan = load_json(sentence_plan_path)
    if str(sentence_plan.get("status", "")).upper() in {"", "TEMPLATE", "PENDING"}:
        fail("sentence-visual-plan.json ist noch nicht READY")
    items = sentence_plan.get("items")
    if not isinstance(items, list) or not items:
        fail("sentence-visual-plan.json enthaelt keine Items")

    first_item = items[0]
    if not isinstance(first_item, dict) or str(first_item.get("function", "")).lower() != "hook":
        fail("Der erste Sentence-Visual-Beat muss function='hook' besitzen")
    first_text = str(first_item.get("voiceover_text", "")).strip()
    if not first_text:
        fail("Der Hook-Text fehlt")
    normalized_first = normalize_visible_text(first_text)
    if any(normalized_first.startswith(normalize_visible_text(prefix)) for prefix in WEAK_OPENING_PREFIXES):
        fail("Script startet mit schwachem Schulbuch-/Intro-Opening statt Neugier-Hook")

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
        if not isinstance(item.get("labels"), list) or len(item.get("labels", [])) > 3:
            fail(f"Sentence-Visual-Item {index}: maximal 3 Labels")

    scene_payload = load_json(scenes_path)
    scenes = scene_payload.get("scenes")
    if not isinstance(scenes, list) or not scenes:
        fail("phase1-scenes.json enthaelt keine Szenen")

    scene_image_ids_list: list[str] = []
    scene_numbers: set[int] = set()
    for index, scene in enumerate(scenes, start=1):
        if not isinstance(scene, dict):
            fail(f"phase1-scenes.json: Szene {index} ist ungueltig")
        number = int(scene.get("scene", 0))
        image_id = scene.get("image")
        if number != index:
            fail(f"phase1-scenes.json: erwartete Szene {index}, gefunden {number}")
        if not isinstance(image_id, str) or image_id != f"Bild_{index:02d}":
            fail(f"Szene {index}: erwartetes Bild_{index:02d}, gefunden {image_id!r}")
        labels_de = scene.get("labels_de", [])
        if not isinstance(labels_de, list) or len(labels_de) > 3:
            fail(f"Szene {index}: labels_de darf maximal 3 Eintraege enthalten")
        scene_numbers.add(number)
        scene_image_ids_list.append(image_id)

    scene_image_ids = set(scene_image_ids_list)
    if len(scene_image_ids) != len(scene_image_ids_list):
        fail("phase1-scenes.json enthaelt doppelte Bild-IDs")
    if sentence_image_ids - scene_image_ids:
        fail(f"Sentence-Visual-Bilder fehlen in phase1-scenes.json: {sorted(sentence_image_ids - scene_image_ids)}")

    test_mode_path = project / "05_info" / "test-mode.json"
    if test_mode_path.is_file():
        test_mode = load_json(test_mode_path)
        expected_images = test_mode.get("expected_images")
        if expected_images is not None and int(expected_images) != len(scenes):
            fail(f"test-mode.json expected_images={expected_images}, geplant sind aber {len(scenes)} Szenen")
        hard_max = test_mode.get("hard_fail_over_seconds")
        if hard_max is not None and float(hard_max) <= 0:
            fail("test-mode.json: hard_fail_over_seconds muss >0 sein")

    label_plan = load_json(label_plan_path)
    if str(label_plan.get("status", "")).upper() in {"", "TEMPLATE", "PENDING"}:
        fail("label-plan.json ist noch nicht READY")
    images = label_plan.get("images")
    if not isinstance(images, list):
        fail("label-plan.json: images muss eine Liste sein")
    rules = label_plan.get("rules", {})
    if not isinstance(rules, dict):
        fail("label-plan.json: rules muss ein Objekt sein")
    if rules.get("language") != "de":
        fail("label-plan.json: language muss de sein")

    planned_ids: set[str] = set()
    cover_hook: str | None = None

    for entry in images:
        if not isinstance(entry, dict):
            fail("label-plan.json enthaelt ungueltigen Eintrag")
        image_id = entry.get("image_asset_id")
        if image_id not in scene_image_ids:
            fail(f"Label-Plan referenziert unbekanntes Bild: {image_id}")
        if image_id in planned_ids:
            fail(f"Label-Plan enthaelt doppelten Eintrag fuer {image_id}")
        planned_ids.add(image_id)

        label_texts = extract_label_texts(entry.get("labels", []), str(image_id))
        allowed = entry.get("allowed_visible_text", label_texts)
        if not isinstance(allowed, list) or any(not isinstance(text, str) or not text.strip() for text in allowed):
            fail(f"{image_id}: allowed_visible_text muss eine Liste nichtleerer Texte sein")
        if any(ASSET_ID_TEXT_RE.search(text) for text in allowed):
            fail(f"{image_id}: interner Asset-/Szenenname in allowed_visible_text")

        if image_id == "Bild_01":
            if label_texts:
                fail("Bild_01: Cover darf keine zusaetzlichen biologischen Labels enthalten")
            explicit_hook = str(entry.get("hook_text", "")).strip()
            if explicit_hook:
                cover_hook = explicit_hook
            elif len(allowed) == 1:
                cover_hook = allowed[0].strip()
            else:
                fail("Bild_01: genau eine deutsche Cover-Hook muss geplant sein")
            if len(allowed) != 1 or normalize_visible_text(allowed[0]) != normalize_visible_text(cover_hook):
                fail("Bild_01: allowed_visible_text muss exakt die Cover-Hook enthalten")
        else:
            if cover_hook and any(normalize_visible_text(text) == normalize_visible_text(cover_hook) for text in allowed):
                fail(f"{image_id}: Cover-Hook darf nicht erneut als Flow-Text erscheinen")
            if sorted(normalize_visible_text(text) for text in label_texts) != sorted(
                normalize_visible_text(text) for text in allowed
            ):
                fail(f"{image_id}: allowed_visible_text muss den biologischen Labels entsprechen")

    if planned_ids != scene_image_ids:
        fail(
            f"Label-Plan muss exakt alle Szenen abdecken. Fehlend={sorted(scene_image_ids - planned_ids)}, "
            f"extra={sorted(planned_ids - scene_image_ids)}"
        )

    overlay_count = validate_overlay_plan(project, scene_numbers)

    flow_prompt_text = flow_prompt_txt.read_text(encoding="utf-8")
    if "Clean Animated Biology Illustration" not in flow_prompt_text and "animated biology illustration" not in flow_prompt_text.lower():
        fail("Google-Flow-Prompt verweist nicht erkennbar auf die freigegebene Bildwelt")

    print(f"V2-PHASE-1-PASS: {project}")
    print(f"  Hook-Beat: {first_text}")
    print(f"  Satz-/Visual-Items: {len(items)}")
    print(f"  geplante Szenen/Bilder: {len(scene_image_ids)}")
    print(f"  selektive Remotion-Overlays: {overlay_count}")
    print("  biologische Labels: Google Flow; Praesentations-Text: nur selektiv via Remotion")
    return scene_image_ids


def validate_phase2(project: Path, expected_image_ids: set[str]) -> None:
    review_path = project / "02_bildprompts" / "image-review.json"
    images_dir = project / "02_bildprompts" / "images"
    require_file(review_path)
    if not images_dir.is_dir():
        fail(f"finaler Bilderordner fehlt: {images_dir}")

    review = load_json(review_path)
    status = str(review.get("status", "")).upper()
    if status in {"", "TEMPLATE", "PENDING_IMAGES", "PENDING"}:
        fail(f"image-review.json ist noch nicht final: status={status or 'LEER'}")
    if has_placeholder(review):
        fail("image-review.json enthaelt noch TODO/TBD/PENDING-Werte")

    entries = review.get("images")
    if not isinstance(entries, list) or not entries:
        fail("image-review.json enthaelt keine Bildreviews")

    reviewed: set[str] = set()
    required_scores = (
        "scientific_accuracy",
        "voiceover_match",
        "immediate_clarity",
        "style_continuity",
        "composition",
        "complexity_control",
        "overall_score",
    )

    for entry in entries:
        if not isinstance(entry, dict):
            fail("image-review.json enthaelt ungueltigen Eintrag")
        image_id = entry.get("image_asset_id")
        if image_id not in expected_image_ids:
            fail(f"Bildreview referenziert unbekanntes Bild: {image_id}")
        if image_id in reviewed:
            fail(f"image-review.json enthaelt mehrfachen Review fuer {image_id}")
        reviewed.add(image_id)

        require_file(images_dir / f"{image_id}.png")

        if entry.get("decision") != "ACCEPT":
            fail(f"{image_id}: Bild ist nicht ACCEPT")
        if entry.get("ai_artifact_check") != "PASS":
            fail(f"{image_id}: AI-Artefakt-Check nicht bestanden")
        if entry.get("labels_correct") not in {"PASS", True}:
            fail(f"{image_id}: Label-Korrektheit nicht bestanden")
        if entry.get("no_visible_asset_id") not in {"PASS", True}:
            fail(f"{image_id}: interner Assetname sichtbar oder ungeprueft")
        if entry.get("single_retained_asset_for_scene") not in {"PASS", True}:
            fail(f"{image_id}: mehrere retained Varianten vorhanden oder ungeprueft")

        for key in required_scores:
            value = entry.get(key)
            if not isinstance(value, (int, float)) or value < 8.0:
                fail(f"{image_id}: {key} muss mindestens 8.0 sein")

        for optional_score in ("visual_novelty", "information_value", "label_accuracy"):
            if optional_score in entry:
                value = entry.get(optional_score)
                if not isinstance(value, (int, float)) or value < 8.0:
                    fail(f"{image_id}: {optional_score} muss mindestens 8.0 sein")

        scene_difference = entry.get("scene_difference")
        if isinstance(scene_difference, str):
            if scene_difference.upper() not in {"PASS", "OK"}:
                fail(f"{image_id}: scene_difference nicht bestanden")
        elif isinstance(scene_difference, (int, float)):
            if scene_difference < 8.0:
                fail(f"{image_id}: scene_difference muss mindestens 8.0 sein")
        else:
            fail(f"{image_id}: scene_difference fehlt")

    missing = expected_image_ids - reviewed
    if missing:
        fail(f"Bildreviews fehlen fuer: {sorted(missing)}")

    actual_png_ids = {path.stem for path in images_dir.glob("Bild_*.png")}
    if actual_png_ids != expected_image_ids:
        fail(
            f"Finaler Bilderordner muss exakt die Pflichtbilder enthalten. "
            f"Fehlend={sorted(expected_image_ids - actual_png_ids)}, "
            f"extra={sorted(actual_png_ids - expected_image_ids)}"
        )

    print(f"V2-PHASE-2-REVIEW-PASS: {project}")
    print(f"  akzeptierte eindeutige Bildreviews: {len(reviewed)}")
    print("  Stil, Komplexitaet, Label-Korrektheit und Bild-Eindeutigkeit bestaetigt")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("project", help="Pfad zum Video-Projekt")
    parser.add_argument("--phase2", action="store_true", help="zusaetzlich finale Bildreviews und Assets pruefen")
    args = parser.parse_args()

    project = Path(args.project).resolve()
    if not project.is_dir():
        fail(f"Projektordner nicht gefunden: {project}")

    expected = validate_phase1(project)
    if args.phase2:
        validate_phase2(project, expected)


if __name__ == "__main__":
    main()
