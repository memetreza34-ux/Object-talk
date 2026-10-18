#!/usr/bin/env python3
"""Script-arc and Flow-register gate for new Object-Talk/Lebenslogik videos (011+).

Checks planning text only: the voice-over script is filled, follows
Hook -> Einleitung -> Hauptteil -> Schluss, is covered 1:1 by the scene plan,
and the single Flow prompt really contains every planned image. It does not
judge voice quality or finished Flow images. Older video projects are exempt.
"""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

PARTS = ("hook", "einleitung", "hauptteil", "schluss")
ARC_KEYS = ("hook_frage", "wendung", "payoff", "schluss_antwort")
PLACEHOLDER_RE = re.compile(r"\[[^\]]+\]|\b(?:TODO|TBD)\b")
VISIBLE_ID_RE = re.compile(r"\b(?:Bild|Szene|Scene|Image)[_\s-]?\d+\b", re.IGNORECASE)
TEMPLATE_REMNANTS = ("TITEL DES VIDEOS", "REGELN:")
WEAK_OPENINGS = (
    "hallo", "willkommen", "herzlich willkommen", "in diesem video",
    "heute erklaeren wir", "heute erklären wir", "heute schauen wir", "heute geht es",
)
FLOW_TEMPLATE_MARKERS = (
    "[VIDEO_ID]", "[EXAKTER COVER-TITEL]", "[COVER A", "[COVER B", "[COVER C",
    "[HIER alle Szenen", "[NN]", "Diesen Platzhalter",
)
FLOW_IMAGE_RE = re.compile(r"\bBild_(\d+)\b")


class ContentGateError(ValueError):
    pass


def is_gated(project: Path, policy: dict) -> bool:
    match = re.match(r"^(\d{3})-", project.name)
    if project.name == "_TEMPLATE" or not match:
        return False
    return int(match.group(1)) >= int(policy.get("effective_from_video", 11))


def words(text: str) -> list[str]:
    return re.findall(r"[0-9a-zäöüß]+", text.lower())


def first_divergence(expected: list[str], actual: list[str]) -> str:
    for i, (a, b) in enumerate(zip(expected, actual)):
        if a != b:
            break
    else:
        i = min(len(expected), len(actual))
    return (
        f"ab Wort {i + 1}: Skript '{' '.join(expected[i:i + 8])}' / "
        f"Szenen '{' '.join(actual[i:i + 8])}'"
    )


def check_script_structure(project: Path, script_text: str, scene_payload: dict, policy: dict) -> str:
    """Fail unfilled, unstructured or uncovered scripts for video 011 onward."""
    if not is_gated(project, policy):
        return "HISTORISCHES VIDEO: Skript-Gate nicht rueckwirkend angewendet"

    text = script_text.strip()
    if not text:
        raise ContentGateError("01_script/script.txt ist leer")
    if PLACEHOLDER_RE.search(text) or any(marker in text for marker in TEMPLATE_REMNANTS):
        raise ContentGateError("Skript enthaelt noch Vorlagentext, Platzhalter oder Regieanweisungen")
    if VISIBLE_ID_RE.search(text):
        raise ContentGateError("Skript enthaelt Bild-/Szenennummern; nur gesprochener Text ist erlaubt")

    script_words = words(text)
    low, high = policy.get("word_range", [900, 1200])
    if not low <= len(script_words) <= high:
        raise ContentGateError(
            f"Skript hat {len(script_words)} Woerter, Longform-Ziel {low}-{high} (ca. 6-7 Minuten bei 1.10x)"
        )
    if text.lower().startswith(WEAK_OPENINGS):
        raise ContentGateError("Skript startet mit schwachem Intro statt Neugier-Hook")

    arc = scene_payload.get("script_arc")
    if not isinstance(arc, dict):
        raise ContentGateError("script_arc fehlt in phase1-scenes.json (hook_frage, wendung, payoff, schluss_antwort)")
    for key in ARC_KEYS:
        value = arc.get(key)
        if not isinstance(value, str) or len(value.strip()) < 20 or PLACEHOLDER_RE.search(value):
            raise ContentGateError(f"script_arc.{key}: konkreter Satz fehlt")

    scenes = scene_payload.get("scenes")
    if not isinstance(scenes, list) or not scenes:
        raise ContentGateError("Keine Szenen fuer Skript-Pruefung")
    part_words: Counter = Counter()
    covered: list[str] = []
    last_rank = 0
    for i, scene in enumerate(scenes, 1):
        if not isinstance(scene, dict):
            raise ContentGateError(f"Szene {i} ist kein Objekt")
        part = scene.get("script_part")
        if part not in PARTS:
            raise ContentGateError(f"Szene {i}: script_part muss einer von {list(PARTS)} sein")
        rank = PARTS.index(part)
        if i == 1 and part != "hook":
            raise ContentGateError("Szene 1 muss script_part='hook' haben")
        if rank < last_rank:
            raise ContentGateError(f"Szene {i}: '{part}' nach '{PARTS[last_rank]}' – Reihenfolge Hook → Einleitung → Hauptteil → Schluss")
        last_rank = rank
        speech = scene.get("speech_section")
        if not isinstance(speech, str) or not speech.strip():
            raise ContentGateError(f"Szene {i}: speech_section fehlt")
        section = words(speech)
        covered.extend(section)
        part_words[part] += len(section)
    missing = [part for part in PARTS if not part_words[part]]
    if missing:
        raise ContentGateError(f"Skriptteile fehlen im Szenenplan: {missing}")
    if covered != script_words:
        raise ContentGateError(
            "speech_section-Texte decken script.txt nicht exakt, lueckenlos und ohne Doppelung ab, "
            + first_divergence(script_words, covered)
        )

    total = len(script_words)
    hook_max = int(policy.get("hook_max_words", 60))
    intro_max = float(policy.get("intro_max_share", 0.20))
    main_min = float(policy.get("main_min_share", 0.60))
    end_low, end_high = policy.get("schluss_share_range", [0.04, 0.15])
    shares = {part: part_words[part] / total for part in PARTS}
    failed = []
    if part_words["hook"] > hook_max:
        failed.append(f"Hook {part_words['hook']} Woerter (max {hook_max}; Payoff muss frueh kommen)")
    if shares["hook"] + shares["einleitung"] - 1e-9 > intro_max:
        failed.append(f"Hook+Einleitung {shares['hook'] + shares['einleitung']:.0%} (max {intro_max:.0%})")
    if shares["hauptteil"] + 1e-9 < main_min:
        failed.append(f"Hauptteil {shares['hauptteil']:.0%} (min {main_min:.0%})")
    if not end_low - 1e-9 <= shares["schluss"] <= end_high + 1e-9:
        failed.append(f"Schluss {shares['schluss']:.0%} (Ziel {end_low:.0%}-{end_high:.0%})")
    if failed:
        raise ContentGateError("Skriptaufbau unausgewogen: " + "; ".join(failed))

    return (
        f"PASS: {total} Woerter; Hook {part_words['hook']}, Einleitung {part_words['einleitung']}, "
        f"Hauptteil {part_words['hauptteil']}, Schluss {part_words['schluss']} Woerter; "
        "Szenen decken das Skript 1:1 ab. Hook-/Schlussqualitaet trotzdem inhaltlich pruefen."
    )


def check_flow_register(project: Path, scene_payload: dict, flow_prompt_text: str, policy: dict) -> str:
    """Fail Flow prompts that are still template text or miss planned images (011+)."""
    if not is_gated(project, policy):
        return "HISTORISCHES VIDEO: Flow-Register-Gate nicht rueckwirkend angewendet"
    leftovers = [marker for marker in FLOW_TEMPLATE_MARKERS if marker in flow_prompt_text]
    if leftovers:
        raise ContentGateError(f"Flow-Prompt enthaelt noch Vorlagen-Platzhalter: {leftovers}")
    scenes = scene_payload.get("scenes")
    if not isinstance(scenes, list) or not scenes:
        raise ContentGateError("Keine Szenen fuer Flow-Register-Pruefung")
    expected = {f"{i:02d}" for i in range(1, len(scenes) + 1)}
    found = set(FLOW_IMAGE_RE.findall(flow_prompt_text))
    missing = sorted(expected - found)
    extra = sorted(found - expected)
    if missing:
        raise ContentGateError(f"Flow-Prompt fehlt Szenenauftrag fuer Bild_{', Bild_'.join(missing)}")
    if extra:
        raise ContentGateError(f"Flow-Prompt enthaelt ungeplante Bilder Bild_{', Bild_'.join(extra)}")
    return f"PASS: alle {len(scenes)} geplanten Bilder stehen im einen Flow-Prompt, keine Vorlagenreste"


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("video", type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    video = args.video if args.video.is_absolute() else root / args.video
    payload = json.loads((video / ".intern/05_info/phase1-scenes.json").read_text(encoding="utf-8"))
    script = (video / "01_script/script.txt").read_text(encoding="utf-8")
    prompt = (video / "02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt").read_text(encoding="utf-8")
    policy = json.loads((root / "config/channel.json").read_text(encoding="utf-8"))["script_structure_v2"]
    try:
        print(check_script_structure(video, script, payload, policy))
        print(check_flow_register(video, payload, prompt, policy))
    except ContentGateError as e:
        raise SystemExit(f"PHASE-1-INHALT FAIL: {e}")


if __name__ == "__main__":
    main()
