"""Tests that the next video's actual planning does not drift into repeated human portraits."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from visual_storyboard_gate import check_visual_mix, VisualMixError


POLICY = {
    "effective_from_video": 11,
    "min_explanatory_scene_share": 0.65,
    "max_human_centered_scene_share": 0.20,
    "max_whole_person_scene_share": 0.10,
}
FLOW = "ILLUSTRATION-FIRST: make mechanisms, organic cutaways, macroscopic structure, richer harmonious color"


def build(kinds, whole=None, rules=None):
    whole = set(whole or [])
    return {"rules": {"visual_mix_v2": True, **(rules or {})}, "scenes": [
        {"scene": i + 1, "visual_category": kind,
         "human_framing": "whole_person" if i in whole else "none",
         "visual_task": "Beautiful precise large-scale hand-drawn cutaway illustrating the actual process",
         "explanation_visible": "An organ signal clearly changes and triggers the next visible state."}
        for i, kind in enumerate(kinds)
    ]}


class VisualStoryboardTests(unittest.TestCase):
    def test_old_010_is_not_retroactively_blocked(self):
        result = check_visual_mix(Path("010-longform-hunger"), {}, "", {})
        self.assertIn("HISTORISCHES", result)

    def test_good_storyboard_passes(self):
        kinds = (["mechanism", "cutaway", "macro", "educational_comparison",
                  "food_structure", "process_path"] * 5)
        kinds[0] = "everyday_context"
        kinds[7] = "human_action"
        data = build(kinds, whole=[7])
        self.assertIn("PASS", check_visual_mix(Path("011-next-video"), data, FLOW, POLICY))

    def test_missing_metadata_fails(self):
        data = build(["cutaway"] * 8)
        del data["scenes"][2]["visual_category"]
        with self.assertRaisesRegex(VisualMixError, "visual_category"):
            check_visual_mix(Path("011-next-video"), data, FLOW, POLICY)

    def test_many_people_fail(self):
        kinds = ["mechanism", "human_action", "cutaway", "human_action"] * 6
        data = build(kinds)
        with self.assertRaisesRegex(VisualMixError, "zu wenige Erklaerbilder|zu viele Menschen"):
            check_visual_mix(Path("011-next-video"), data, FLOW, POLICY)

    def test_repeated_whole_people_fail(self):
        kinds = ["mechanism", "cutaway", "macro", "educational_comparison",
                 "food_structure", "process_path"] * 5
        data = build(kinds, whole=[2, 3])
        with self.assertRaisesRegex(VisualMixError, "zwei Ganzkoerper"):
            check_visual_mix(Path("011-next-video"), data, FLOW, POLICY)

    def test_exception_requires_user_approval(self):
        kinds = ["mechanism", "cutaway", "macro", "human_action"] * 6
        data = build(kinds)
        data["rules"]["visual_mix_exception_reason"] = "This unusually behavior-centered episode demonstrates real interpersonal situations instead of intracellular processes, so people are scientifically necessary to show the topic clearly."
        with self.assertRaises(VisualMixError):
            check_visual_mix(Path("011-next-video"), data, FLOW, POLICY)
        data["rules"]["visual_mix_exception_approved_by_user"] = True
        result = check_visual_mix(Path("011-next-video"), data, FLOW, POLICY)
        self.assertIn("WARN", result)


if __name__ == "__main__":
    unittest.main()
