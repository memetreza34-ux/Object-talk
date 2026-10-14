#!/usr/bin/env python3
"""Evidence-based post-video improvements. No assumed renders or fake scores.

Commands:
  python tools/improvement_loop.py register youtube-videos/VIDEO
  python tools/improvement_loop.py check-next youtube-videos/NEW_VIDEO
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "engine" / "IMPROVEMENT-LEDGER.json"
ALLOWED_FIX_PREFIXES = ("engine/", "tools/", "bildwelt/", "config/", "youtube-videos/_TEMPLATE/", "AGENTS.md", "PROJECT_CONTRACT.md")
LEGACY_MAX = 9


def failure(message: str) -> None:
    raise ValueError("IMPROVEMENT-GATE FAIL: " + message)


def load(path: Path) -> dict:
    if not path.is_file():
        failure(f"fehlende Datei {path}")
    try:
        obj = json.loads(path.read_text(encoding="utf-8"))
    except (ValueError, OSError) as exc:
        failure(f"unlesbares JSON {path}: {exc}")
    if not isinstance(obj, dict):
        failure(f"JSON muss Objekt sein: {path}")
    return obj


def meaningful(value: object, minimum: int = 12) -> bool:
    return isinstance(value, str) and len(value.strip()) >= minimum


def safe_repo_file(value: object) -> Path:
    if not isinstance(value, str) or not value or value.startswith("/"):
        failure("ungueltiger Dateipfad im Nachweis")
    target = (ROOT / value).resolve()
    if not target.is_relative_to(ROOT) or not target.is_file():
        failure(f"Nachweisdatei existiert nicht im Repo: {value}")
    return target


def check_next(project: Path) -> str:
    """Gate only new video projects; existing 000-009 remain untouched."""
    if project.name == "_TEMPLATE":
        return "TEMPLATE: kein Verbesserungs-Gate"
    prefix = re.match(r"^(\d{3})-", project.name)
    if prefix and int(prefix.group(1)) <= LEGACY_MAX:
        return "HISTORISCHES VIDEO: nicht rueckwirkend blockieren"

    ledger = load(LEDGER)
    manifest = load(project / ".intern" / "05_info" / "improvement-applied.json")
    if manifest.get("status") != "APPLIED":
        failure("vor Phase 1 zuerst .intern/05_info/improvement-applied.json vervollstaendigen")
    source = ledger.get("latest_reviewed_video")
    if manifest.get("source_review_video") != source:
        failure(f"falsche Referenz: aktuelles Review ist {source!r}")
    required = {
        row.get("id") for row in ledger.get("permanent_lessons", []) + ledger.get("next_video_lessons", [])
        if isinstance(row, dict)
    }
    if not required:
        failure("Ledger enthaelt keine verbindlichen Lessons")
    rows = manifest.get("lessons")
    if not isinstance(rows, list):
        failure("lessons muss eine Liste sein")
    index = {}
    for row in rows:
        if not isinstance(row, dict) or not isinstance(row.get("id"), str):
            failure("ungueltiger Lesson-Nachweis")
        if row["id"] in index:
            failure(f"duplizierte Lesson: {row['id']}")
        index[row["id"]] = row
    for lesson_id in sorted(required):
        row = index.get(lesson_id)
        if row is None:
            failure(f"vererbte Verbesserung fehlt: {lesson_id}")
        if not meaningful(row.get("implemented_as"), 20):
            failure(f"{lesson_id}: konkrete Anwendung im neuen Video fehlt")
        if not meaningful(row.get("verification"), 12):
            failure(f"{lesson_id}: konkrete Verifikation fehlt")
        paths = row.get("evidence_files")
        if not isinstance(paths, list) or not paths:
            failure(f"{lesson_id}: echte Dateinachweise fehlen")
        for name in paths:
            safe_repo_file(name)
    return f"PASS: {len(required)} vererbte Verbesserungen vor neuer Phase 1 nachgewiesen"


def register_review(project: Path) -> str:
    """Register only a manually reviewed real final video with implemented fixes."""
    project = project.resolve()
    if not project.is_relative_to(ROOT / "youtube-videos") or project.name == "_TEMPLATE":
        failure("nur ein echter youtube-videos/VIDEOORDNER darf registriert werden")
    review = load(project / ".intern" / "05_info" / "improvement-review.json")
    if review.get("status") != "VERIFIED" or review.get("reviewed_final_video") is not True:
        failure("Finalvideo wurde nicht nachweisbar als VERIFIED gesichtet")
    if review.get("video_id") != project.name:
        failure("video_id stimmt nicht mit Videoordner ueberein")
    media = review.get("media_evidence")
    if not isinstance(media, dict):
        failure("Mediennachweis fehlt")
    for key in ("source", "reviewed_sections", "cover_source", "audio_source"):
        if not meaningful(media.get(key)):
            failure(f"reale Medienpruefung fehlt: {key}")
    if not isinstance(media.get("runtime_seconds"), (int, float)) or media["runtime_seconds"] <= 0:
        failure("echte Filmlaenge fehlt")
    if not meaningful(review.get("reviewer"), 3):
        failure("verantwortliche sichtende Person/Agent fehlt")
    strengths = review.get("strengths")
    problems = review.get("problems")
    fixes = review.get("fixes")
    if not isinstance(strengths, list) or len(strengths) < 2 or not all(meaningful(v) for v in strengths):
        failure("zwei konkrete belegte Staerken fehlen")
    if not isinstance(problems, list) or len(problems) < 3:
        failure("mindestens drei analysierte Schwachstellen fehlen")
    for issue in problems:
        if not isinstance(issue, dict) or not all(meaningful(issue.get(k)) for k in ("at", "problem", "root_cause")):
            failure("Fehler braucht reale Zeitstelle/Bild, Problem und Ursache")
    if not isinstance(fixes, list) or not 2 <= len(fixes) <= 5:
        failure("zwei bis fuenf echte Korrekturen benoetigt")
    ids = set()
    for fix in fixes:
        if not isinstance(fix, dict):
            failure("Fix muss JSON-Objekt sein")
        fix_id = fix.get("id")
        if not isinstance(fix_id, str) or not re.fullmatch(r"[A-Z0-9_-]{4,50}", fix_id) or fix_id in ids:
            failure("Fix-IDs muessen eindeutig und stabil sein")
        ids.add(fix_id)
        for key in ("problem", "root_cause", "change"):
            if not meaningful(fix.get(key), 20):
                failure(f"{fix_id}: {key} unkonkret")
        paths = fix.get("repo_files")
        if not isinstance(paths, list) or not paths:
            failure(f"{fix_id}: keine geaenderte Regel/Tooldatei")
        for path in paths:
            if not isinstance(path, str) or not path.startswith(ALLOWED_FIX_PREFIXES):
                failure(f"{fix_id}: globaler Fix muss in kanonischem Regel-/Codebereich liegen: {path}")
            safe_repo_file(path)
        verification = fix.get("verification")
        if not isinstance(verification, dict) or verification.get("result") != "PASS" or not meaningful(verification.get("method"), 20):
            failure(f"{fix_id}: echter bestandener Test / Review erforderlich")
    ledger = load(LEDGER)
    history = ledger.get("history", [])
    if not isinstance(history, list) or any(row.get("video") == project.name for row in history if isinstance(row, dict)):
        failure("Video schon registriert (nicht ueberschreiben)")
    previous = ledger.get("latest_reviewed_video")
    ledger["history"] = history + [{"video": project.name, "preceding_review": previous, "fix_ids": sorted(ids)}]
    ledger["latest_reviewed_video"] = project.name
    ledger["next_video_lessons"] = [
        {"id": fix["id"], "rule": fix["change"], "source": project.name}
        for fix in fixes
    ]
    LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return f"REGISTERED: {project.name}, {len(fixes)} getestete Verbesserungen in neue Videos vererbt"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("register", "check-next"))
    parser.add_argument("video", type=Path)
    args = parser.parse_args()
    try:
        result = register_review(args.video) if args.command == "register" else check_next(args.video.resolve())
    except ValueError as exc:
        raise SystemExit(str(exc))
    print(result)


if __name__ == "__main__":
    main()
