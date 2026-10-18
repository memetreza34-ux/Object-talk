"""One storyboard must produce consistent, gap-free Phase-1 files; invalid scenes must fail."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from build_phase1_package import StoryboardError, build
from export_chapters import chapter_lines, insert_into_caption


def scene(i, **overrides):
    data = {
        "speech": f"Satz Nummer {i} erklärt den Magen.", "cat": "cutaway" if i % 2 else "macro",
        "frame": "none", "scale": "Organ", "motion": "slow-push-in", "labels": ["Magen"] if i % 3 == 0 else [],
        "visual": "Large clean cutaway of a coral stomach with soft folds and one clear process highlighted.",
        "shows": "The stomach wall visibly changes.", "goal": "Lernziel", "claims": ["C01"], "para": i % 5 == 0,
    }
    data.update(overrides)
    return data


def storyboard(scenes):
    return {
        "format": "storyboard-v2", "status": "READY", "video_id": "099-test", "working_title": "Test",
        "youtube": {"title": "Testtitel", "description": "Beschreibung.", "hashtags": ["#a", "#b"]},
        "cover": {"title": "Test?", "options": ["one", "two", "three"]},
        "flow": {"continuity_key": "key"},
        "chapters": [
            {"title": "Kapitel A", "function": "observation", "misconception": "x", "scenes": scenes[:12]},
            {"title": "Kapitel B", "function": "path", "misconception": "y", "scenes": scenes[12:]},
        ],
    }


class BuildPackageTests(unittest.TestCase):
    def make(self, sb):
        tmp = Path(tempfile.mkdtemp()) / "099-test"
        (tmp / ".intern" / "05_info").mkdir(parents=True)
        (tmp / ".intern" / "05_info" / "storyboard-source.json").write_text(json.dumps(sb), encoding="utf-8")
        return tmp

    def test_build_writes_consistent_files(self):
        project = self.make(storyboard([scene(i) for i in range(1, 25)]))
        build(project)
        script = (project / "01_script" / "script.txt").read_text(encoding="utf-8")
        phase = json.loads((project / ".intern" / "05_info" / "phase1-scenes.json").read_text(encoding="utf-8"))
        joined = " ".join(s["speech_section"] for s in phase["scenes"])
        self.assertEqual(script.split(), joined.split())
        self.assertEqual(phase["scenes"][0]["image"], "Bild_01")
        self.assertTrue(phase["scenes"][12]["chapter_start"])
        prompt = (project / "02_bildprompts" / "GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt").read_text(encoding="utf-8")
        self.assertIn("exactly one visible text block", prompt)
        self.assertIn("Bild_24.png", prompt)
        plan = json.loads((project / ".intern" / "05_info" / "sentence-visual-plan.json").read_text(encoding="utf-8"))
        self.assertEqual(plan["items"][0]["function"], "hook")

    def test_invalid_motion_and_overlong_scene_fail(self):
        scenes = [scene(i) for i in range(1, 25)]
        scenes[3]["motion"] = "slow-pull-back"
        scenes[4]["speech"] = "Wort " * 25
        with self.assertRaises(StoryboardError) as ctx:
            build(self.make(storyboard(scenes)))
        self.assertIn("motion", str(ctx.exception))
        self.assertIn("Wörter", str(ctx.exception))


class ChapterTests(unittest.TestCase):
    def test_chapters_use_real_times_and_replace_block(self):
        scenes = [{"chapter": "A", "chapter_start": True}, {"chapter": "A"}, {"chapter": "B", "chapter_start": True},
                  {"chapter": "C", "chapter_start": True}]
        timeline = [{"start": 0.4, "end": 20}, {"start": 20, "end": 41}, {"start": 41, "end": 75}, {"start": 75, "end": 130}]
        lines = chapter_lines(scenes, timeline)
        self.assertEqual(lines, ["0:00 A", "0:41 B", "1:15 C"])
        caption = "TITEL\nx\n\nKAPITEL\nwird später gesetzt\n\nHASHTAGS\n#a\n"
        self.assertIn("0:41 B", insert_into_caption(caption, lines))
        self.assertNotIn("wird später gesetzt", insert_into_caption(caption, lines))

    def test_too_short_chapter_fails(self):
        scenes = [{"chapter": "A", "chapter_start": True}, {"chapter": "B", "chapter_start": True},
                  {"chapter": "C", "chapter_start": True}]
        timeline = [{"start": 0, "end": 5}, {"start": 5, "end": 40}, {"start": 40, "end": 80}]
        with self.assertRaises(SystemExit):
            chapter_lines(scenes, timeline)


if __name__ == "__main__":
    unittest.main()
