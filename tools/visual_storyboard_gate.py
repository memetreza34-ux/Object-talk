#!/usr/bin/env python3
"""Required art-direction gate for new Object-Talk/Lebenslogik videos (011+).

This checks storyboard *planning metadata*, not finished Flow image quality.
Older completed video projects are intentionally exempt.
"""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

CATEGORIES = {
    "mechanism", "cutaway", "macro", "educational_comparison",
    "food_structure", "process_path", "everyday_context",
    "human_action", "transition",
}
HUMAN_FRAMING = {"none", "hands_or_crop", "partial_person", "whole_person"}
EXPLAINING = {
    "mechanism", "cutaway", "macro", "educational_comparison",
    "food_structure", "process_path",
}
HUMAN_CENTERED = {"everyday_context", "human_action"}


class VisualMixError(ValueError):
    pass


def check_visual_mix(project: Path, scene_payload: dict, flow_prompt_text: str, policy: dict) -> str:
    """Fail unclear/person-heavy storyboards for video 011 onward."""
    match = re.match(r"^(\d{3})-", project.name)
    if project.name == "_TEMPLATE" or not match or int(match.group(1)) <= 10:
        return "HISTORISCHES VIDEO: Bildregie-V2-Gate nicht rueckwirkend angewendet"
    if policy.get("effective_from_video") != 11:
        raise VisualMixError("visual_storytelling_v2 muss ab Video 011 aktiviert sein")
    rules = scene_payload.get("rules")
    if not isinstance(rules, dict) or rules.get("visual_mix_v2") is not True:
        raise VisualMixError("Bildregie V2 fehlt in phase1-scenes.json (rules.visual_mix_v2=true)")
    text = flow_prompt_text.lower()
    if not ("illustration-first" in text or "bildregie v2" in text):
        raise VisualMixError("Flow-Prompt muss den neuen Illustration-First-Stil aus der Vorlage enthalten")

    scenes = scene_payload.get("scenes")
    if not isinstance(scenes, list) or not scenes:
        raise VisualMixError("Keine Szenen fuer Bildregie-Pruefung")
    counts = Counter()
    used_categories = set()
    last_human = 0
    last_whole = 0
    for i, scene in enumerate(scenes, 1):
        if not isinstance(scene, dict):
            raise VisualMixError(f"Szene {i} ist kein Objekt")
        category = scene.get("visual_category")
        framing = scene.get("human_framing")
        visible = scene.get("explanation_visible")
        prompt = scene.get("visual_task")
        if category not in CATEGORIES or framing not in HUMAN_FRAMING:
            raise VisualMixError(
                f"Szene {i}: gueltige visual_category und human_framing sind Pflicht"
            )
        if not isinstance(visible, str) or len(visible.strip()) < 24:
            raise VisualMixError(f"Szene {i}: erklaerender sichtbarer Vorgang fehlt")
        if not isinstance(prompt, str) or len(prompt.strip()) < 35:
            raise VisualMixError(f"Szene {i}: konkrete Bildkomposition fehlt")
        used_categories.add(category)
        if category in EXPLAINING:
            counts["explaining"] += 1
        is_human_centered = category in HUMAN_CENTERED
        is_whole = framing == "whole_person"
        if is_human_centered:
            counts["human_centered"] += 1
        if is_whole:
            counts["whole"] += 1
        last_human = last_human + 1 if is_human_centered else 0
        last_whole = last_whole + 1 if is_whole else 0
        if last_human >= 3:
            raise VisualMixError(f"Szene {i}: drei menschenzentrierte Alltagsszenen hintereinander")
        if last_whole >= 2:
            raise VisualMixError(f"Szene {i}: zwei Ganzkoerper-Personenszenen direkt nacheinander")
    if len(scenes) >= 25 and len(used_categories & EXPLAINING) < 4:
        raise VisualMixError("Szenen-Mix zu einfoermig: mindestens vier verschiedene erklaerende Bildarten")

    n = len(scenes)
    min_explain = float(policy.get("min_explanatory_scene_share", 0.65))
    max_human = float(policy.get("max_human_centered_scene_share", 0.20))
    max_whole = float(policy.get("max_whole_person_scene_share", 0.10))
    failed = []
    if counts["explaining"] / n + 1e-9 < min_explain:
        failed.append(f"zu wenige Erklaerbilder {counts['explaining']}/{n} (Ziel >= {min_explain:.0%})")
    if counts["human_centered"] / n - 1e-9 > max_human:
        failed.append(f"zu viele Menschen-Alltagsszenen {counts['human_centered']}/{n} (Limit {max_human:.0%})")
    if counts["whole"] / n - 1e-9 > max_whole:
        failed.append(f"zu viele Ganzkoerper-Personenszenen {counts['whole']}/{n} (Limit {max_whole:.0%})")

    if failed:
        reason = rules.get("visual_mix_exception_reason")
        approved = rules.get("visual_mix_exception_approved_by_user")
        if not (isinstance(reason, str) and len(reason.strip()) >= 100 and approved is True):
            raise VisualMixError("; ".join(failed) + ". Bei thematisch notwendiger Abweichung: dokumentierte Nutzerfreigabe erforderlich.")
        return "WARN: schriftlich begruendete und vom Nutzer freigegebene Ausnahme: " + "; ".join(failed)

    return (
        f"PASS: {n} Szenen; {counts['explaining']} Erklaerbilder, "
        f"{counts['human_centered']} Menschen-Alltag, {counts['whole']} Ganzkoerper, "
        f"{len(used_categories & EXPLAINING)} erklaerende Bildtypen. "
        "Metadaten-Gate; generierte Bilder separat visuell pruefen."
    )


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("video", type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    video = args.video
    if not video.is_absolute():
        video = root / video
    payload = json.loads((video / ".intern/05_info/phase1-scenes.json").read_text(encoding="utf-8"))
    prompt = (video / "02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt").read_text(encoding="utf-8")
    policy = json.loads((root / "config/channel.json").read_text(encoding="utf-8"))["visual_storytelling_v2"]
    try:
        print(check_visual_mix(video, payload, prompt, policy))
    except VisualMixError as e:
        raise SystemExit(f"BILDREGIE FAIL: {e}")


if __name__ == "__main__":
    main()
