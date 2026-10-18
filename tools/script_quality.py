#!/usr/bin/env python3
"""Measurable retention/script-quality gate for new videos (011+).

Background (Kanal-Analyse 2026-10): scripts 008-010 were correct but read like
a careful textbook: 1-5 concrete numbers in ~1000 words, 21-27 hedge words per
1000 words, repeated "Das bedeutet nicht ..." disclaimers and no open loop that
keeps viewers waiting for a payoff. This gate measures exactly those weaknesses.
It cannot judge humour or storytelling; a human/agent review stays mandatory.

Usage:
  python tools/script_quality.py youtube-videos/VIDEO          # report + gate
  python tools/script_quality.py --text path/to/script.txt      # report only
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

HEDGE_RE = re.compile(
    r"\b(kann|können|könnte|könnten|manchmal|oft|oftmals|häufig|häufiger|meist|meistens|unter anderem|"
    r"verschiedene|verschiedener|bestimmte|bestimmten|eher|teilweise|normalerweise|möglicherweise|"
    r"bei manchen|manche|manchen|mancher|manches|mitunter|gewisse|gewissen|eventuell|vielleicht|"
    r"wahrscheinlich|gelegentlich|unter umständen|tendenziell)\b",
    re.IGNORECASE,
)
DISCLAIMER_RE = re.compile(
    r"(das bedeutet nicht|bedeutet aber nicht|das heißt nicht|nicht automatisch|kein magischer|"
    r"keine einzelne|dabei geht es nicht|es geht also nicht|aber vorsicht|wichtig ist dabei nicht|"
    r"kein wundermittel|keine garantie|ohne falsche versprechen|nicht als schlecht abzustempeln)",
    re.IGNORECASE,
)
# Real German numerals only (no -mäßig, winzig, maximal, Jahrhundert ...). "ein"/"eine" alone is an article.
_UNIT = r"(?:ein|zwei|drei|vier|fünf|sechs|sieben|acht|neun)"
_BELOW_100 = (
    r"(?:zwei|drei|vier|fünf|sechs|sieben|acht|neun|zehn|elf|zwölf|(?:drei|vier|fünf|sech|sieb|acht|neun)zehn|"
    r"(?:" + _UNIT + r"und)?(?:zwanzig|dreißig|vierzig|fünfzig|sechzig|siebzig|achtzig|neunzig))"
)
_BELOW_1000 = (
    r"(?:(?:" + _UNIT + r"|elf|zwölf|(?:drei|vier|fünf|sech|sieb|acht|neun)zehn)?hundert(?:" + _BELOW_100
    + r"|eins?)?|" + _BELOW_100 + r")"
)
NUMBER_WORD_RE = re.compile(
    r"^(?:\d[\d.,]*%?|"
    r"(?:" + _BELOW_1000 + r")?tausend(?:" + _BELOW_1000 + r")?|" + _BELOW_1000 + r"|"
    r"(?:" + _BELOW_100 + r"|hundert|tausend)mal|"
    r"viertel|vierteln|hälfte|drittel|doppelt)$",
    re.IGNORECASE,
)
# unit words count only when no numeral stands directly before them ("fünfzehn Prozent" = one number)
UNIT_WORD_RE = re.compile(r"^(prozent|millionen?|milliarden?|billionen?)$", re.IGNORECASE)
WEAK_OPENINGS = ("in diesem video", "heute erklären wir", "heute erklaeren wir", "willkommen", "hallo")

THRESHOLDS = {
    "max_hedges_per_1000_words": 18.0,
    "max_disclaimer_phrases": 2,
    "min_concrete_numbers": 6,
    "min_questions": 3,
    "max_avg_sentence_words": 14.0,
    "max_sentences_over_22_words": 3,
    "min_open_loop_distance_scenes": 15,
    "max_scene_words": 19,
    "max_scene_seconds_estimate": 6.3,
}

# Calibrated on the real 010 render (1044 words -> 368.9 s after 1.10x voice and pause compression).
SECONDS_PER_CHAR = 0.0388
SECONDS_PER_WORD = 0.1036
SECONDS_PER_SENTENCE_END = 0.216


def estimate_seconds(speech: str) -> float:
    """Rough spoken duration of one scene; the hard 7 s limit is checked again on the real timeline."""
    total = 0.0
    for word in str(speech).split():
        total += len(word) * SECONDS_PER_CHAR + SECONDS_PER_WORD
        if word.endswith((".", "?", "!")):
            total += SECONDS_PER_SENTENCE_END
    return round(total, 2)


class ScriptQualityError(ValueError):
    pass


def analyze(text: str) -> dict:
    words = text.split()
    sentences = [s for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s.strip()]
    clean = [re.sub(r"[^\wäöüÄÖÜß%-]", "", w) for w in words]
    numbers = []
    for index, word in enumerate(clean):
        if word and NUMBER_WORD_RE.match(word):
            numbers.append(word)
        elif word and UNIT_WORD_RE.match(word) and not (index and NUMBER_WORD_RE.match(clean[index - 1] or "")):
            numbers.append(word)
    hedges = HEDGE_RE.findall(text)
    n_words = max(1, len(words))
    return {
        "words": len(words),
        "sentences": len(sentences),
        "avg_sentence_words": round(len(words) / max(1, len(sentences)), 1),
        "sentences_over_22_words": sum(1 for s in sentences if len(s.split()) > 22),
        "hedges": len(hedges),
        "hedges_per_1000_words": round(len(hedges) / n_words * 1000, 1),
        "disclaimer_phrases": len(DISCLAIMER_RE.findall(text)),
        "concrete_numbers": len(numbers),
        "questions": text.count("?"),
        "first_sentence": sentences[0] if sentences else "",
    }


def gate(metrics: dict, storyboard: dict | None) -> list[str]:
    t = THRESHOLDS
    failed = []
    if metrics["first_sentence"].strip().lower().startswith(WEAK_OPENINGS):
        failed.append("schwacher Einstieg (Begrüßung / 'In diesem Video')")
    if metrics["hedges_per_1000_words"] > t["max_hedges_per_1000_words"]:
        failed.append(f"zu viele Absicherungswörter: {metrics['hedges_per_1000_words']}/1000 (max {t['max_hedges_per_1000_words']})")
    if metrics["disclaimer_phrases"] > t["max_disclaimer_phrases"]:
        failed.append(f"zu viele Disclaimer-Floskeln: {metrics['disclaimer_phrases']} (max {t['max_disclaimer_phrases']}); Einschränkung einmal klar sagen")
    if metrics["concrete_numbers"] < t["min_concrete_numbers"]:
        failed.append(f"zu wenig konkrete Zahlen/Vergleiche: {metrics['concrete_numbers']} (min {t['min_concrete_numbers']})")
    if metrics["questions"] < t["min_questions"]:
        failed.append(f"zu wenig Fragen an den Zuschauer: {metrics['questions']} (min {t['min_questions']})")
    if metrics["avg_sentence_words"] > t["max_avg_sentence_words"]:
        failed.append(f"Sätze zu lang: Ø {metrics['avg_sentence_words']} Wörter")
    if metrics["sentences_over_22_words"] > t["max_sentences_over_22_words"]:
        failed.append(f"{metrics['sentences_over_22_words']} Sätze über 22 Wörter")
    if storyboard is not None:
        scenes = [s for ch in storyboard.get("chapters", []) for s in ch.get("scenes", [])]
        loops = storyboard.get("open_loops")
        if not isinstance(loops, list) or not loops:
            failed.append("kein Open Loop geplant (storyboard open_loops: Frage früh stellen, spät auflösen)")
        else:
            for loop in loops:
                setup, payoff = loop.get("setup_scene"), loop.get("payoff_scene")
                if not (isinstance(setup, int) and isinstance(payoff, int) and 1 <= setup < payoff <= len(scenes)):
                    failed.append(f"Open Loop ungültig: {loop!r}")
                elif payoff - setup < t["min_open_loop_distance_scenes"]:
                    failed.append(f"Open Loop zu kurz ({setup}->{payoff}); Auflösung muss deutlich später kommen")
        for index, scene in enumerate(scenes, 1):
            if len(str(scene.get("speech", "")).split()) > t["max_scene_words"]:
                failed.append(f"Szene {index}: mehr als {t['max_scene_words']} Wörter (>7 s Standbild)")
            seconds = estimate_seconds(scene.get("speech", ""))
            if seconds > t["max_scene_seconds_estimate"]:
                failed.append(f"Szene {index}: geschätzt {seconds} s Sprechzeit (max {t['max_scene_seconds_estimate']} s); teilen oder kürzen")
    return failed


def check_project(project: Path) -> str:
    match = re.match(r"^(\d{3})-", project.name)
    if project.name == "_TEMPLATE" or not match or int(match.group(1)) <= 10:
        return "HISTORISCHES VIDEO: Skript-Qualitätsgate nicht rückwirkend angewendet"
    script = project / "01_script" / "script.txt"
    storyboard_path = project / ".intern" / "05_info" / "storyboard-source.json"
    if not script.is_file():
        raise ScriptQualityError(f"script.txt fehlt: {script}")
    if not storyboard_path.is_file():
        raise ScriptQualityError("storyboard-source.json (format storyboard-v2) fehlt")
    storyboard = json.loads(storyboard_path.read_text(encoding="utf-8"))
    if storyboard.get("format") != "storyboard-v2":
        raise ScriptQualityError("storyboard-source.json muss format=storyboard-v2 haben")
    metrics = analyze(script.read_text(encoding="utf-8"))
    failed = gate(metrics, storyboard)
    if failed:
        raise ScriptQualityError("; ".join(failed))
    return (
        f"PASS: {metrics['words']} Wörter, {metrics['concrete_numbers']} Zahlen, {metrics['questions']} Fragen, "
        f"{metrics['hedges_per_1000_words']} Absicherungen/1000 W., {metrics['disclaimer_phrases']} Disclaimer, "
        f"Ø {metrics['avg_sentence_words']} W./Satz, {len(storyboard.get('open_loops', []))} Open Loop(s)"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("project", nargs="?", type=Path)
    parser.add_argument("--text", type=Path, help="nur Messwerte für eine beliebige Skriptdatei")
    args = parser.parse_args()
    if args.text:
        metrics = analyze(args.text.read_text(encoding="utf-8"))
        print(json.dumps(metrics, ensure_ascii=False, indent=2))
        problems = gate(metrics, None)
        print("Hinweise:" if problems else "Messwerte im Zielbereich.")
        for problem in problems:
            print(f"- {problem}")
        return
    if not args.project:
        parser.error("Projektordner oder --text angeben")
    try:
        print(check_project(args.project.resolve()))
    except ScriptQualityError as exc:
        raise SystemExit(f"SKRIPT-QUALITÄT FAIL: {exc}")


if __name__ == "__main__":
    main()
