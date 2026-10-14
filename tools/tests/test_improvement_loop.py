"""Safety tests for mandatory next-video learning gates."""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import improvement_loop as loop


class ImprovementLoopTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "engine").mkdir()
        self.ledger_path = self.root / "engine" / "IMPROVEMENT-LEDGER.json"
        self.ledger = {
            "schema_version": 1,
            "latest_reviewed_video": None,
            "permanent_lessons": [{"id": "BASE-CLARITY", "rule": "One clear biological action"}],
            "next_video_lessons": [],
            "history": [],
        }
        self.ledger_path.write_text(json.dumps(self.ledger), encoding="utf-8")
        self.project = self.root / "youtube-videos" / "010-new-video"
        (self.project / ".intern" / "05_info").mkdir(parents=True)
        (self.project / "01_script").mkdir()
        (self.project / "01_script" / "script.txt").write_text("Beispiel", encoding="utf-8")
        self.manifest = self.project / ".intern" / "05_info" / "improvement-applied.json"
        self.root_patch = patch.object(loop, "ROOT", self.root)
        self.ledger_patch = patch.object(loop, "LEDGER", self.ledger_path)
        self.root_patch.start()
        self.ledger_patch.start()

    def tearDown(self):
        self.ledger_patch.stop()
        self.root_patch.stop()
        self.tmp.cleanup()

    def test_incomplete_next_video_is_blocked(self):
        self.manifest.write_text(json.dumps({
            "status": "PENDING", "source_review_video": None, "lessons": []
        }), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Phase 1"):
            loop.check_next(self.project)

    def test_complete_next_video_passes_and_missing_evidence_fails(self):
        record = {"id": "BASE-CLARITY",
                  "implemented_as": "The first script beat explains just one clear biological action",
                  "verification": "Reviewed each visual beat against the script and final prompt",
                  "evidence_files": ["youtube-videos/010-new-video/01_script/script.txt"]}
        self.manifest.write_text(json.dumps({
            "status": "APPLIED", "source_review_video": None, "lessons": [record]
        }), encoding="utf-8")
        self.assertIn("PASS", loop.check_next(self.project))
        record["evidence_files"] = ["not-a-real-file.md"]
        self.manifest.write_text(json.dumps({
            "status": "APPLIED", "source_review_video": None, "lessons": [record]
        }), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "existiert nicht"):
            loop.check_next(self.project)

    def build_review(self):
        (self.root / "engine" / "new-guideline.md").write_text("Changed instructions", encoding="utf-8")
        (self.root / "tools" ).mkdir(exist_ok=True)
        (self.root / "tools" / "new-check.py").write_text("print('verified')", encoding="utf-8")
        return {
            "status": "VERIFIED",
            "video_id": "010-new-video",
            "reviewed_final_video": True,
            "media_evidence": {
                "source": "Original uploaded final video inspected personally",
                "runtime_seconds": 362.4,
                "reviewed_sections": "Entire video reviewed from beginning through final closing scene",
                "cover_source": "Original final thumbnail inspected at small size",
                "audio_source": "Original supplied voice-over compared with final video",
            },
            "reviewer": "Human-reviewed with assistant help",
            "strengths": ["Understandable digestion breakdown scene",
                          "Clear audio pacing during the final summary"],
            "problems": [
                {"at": "00:15 frame Bild_03", "problem": "Unclear microscopic pathway",
                 "root_cause": "Image prompt contained too many tiny structures"},
                {"at": "01:25 frame Bild_19", "problem": "Text was too faint on pale blue",
                 "root_cause": "Prompt failed to enforce dark text on pale background"},
                {"at": "03:15 frame Bild_42", "problem": "Scene held for too many seconds",
                 "root_cause": "Pacing validator did not constrain image duration"},
            ],
            "fixes": [
                {"id": "FIX-CLARITY-010", "problem": "Too many small anatomical objects",
                 "root_cause": "Earlier visual grammar was overly detailed",
                 "change": "Enforced single event and large connected anatomy",
                 "repo_files": ["engine/new-guideline.md"],
                 "verification": {"result": "PASS", "method": "Visually tested on three biology scenes"}},
                {"id": "FIX-CONTRAST-010", "problem": "Light text appeared on a pale ground",
                 "root_cause": "Earlier label contrast instruction was ambiguous",
                 "change": "Introduced a text-background contrast check",
                 "repo_files": ["tools/new-check.py"],
                 "verification": {"result": "PASS", "method": "Tested generated high and low contrast cases"}},
            ],
        }

    def test_register_rejects_unverified_video(self):
        report = self.build_review()
        report["reviewed_final_video"] = False
        (self.project / ".intern" / "05_info" / "improvement-review.json").write_text(
            json.dumps(report), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "nicht nachweisbar"):
            loop.register_review(self.project)

    def test_review_updates_ledger_and_next_video_duties(self):
        report = self.build_review()
        (self.project / ".intern" / "05_info" / "improvement-review.json").write_text(
            json.dumps(report), encoding="utf-8")
        self.assertIn("REGISTERED", loop.register_review(self.project))
        ledger = json.loads(self.ledger_path.read_text(encoding="utf-8"))
        self.assertEqual(ledger["latest_reviewed_video"], "010-new-video")
        self.assertEqual(len(ledger["next_video_lessons"]), 2)
        with self.assertRaisesRegex(ValueError, "schon registriert"):
            loop.register_review(self.project)


if __name__ == "__main__":
    unittest.main()
