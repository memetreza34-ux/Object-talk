"""Tests that new videos get a filled, well-structured script and a complete Flow scene register."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from phase1_content_gate import check_flow_register, check_script_structure, ContentGateError


POLICY = {
    "effective_from_video": 11,
    "word_range": [900, 1200],
    "hook_max_words": 60,
    "intro_max_share": 0.20,
    "main_min_share": 0.60,
    "schluss_share_range": [0.04, 0.15],
}
HOOK = "Hast du dich schon mal gefragt, warum du kurz nach dem Essen wieder Hunger hast? Die Antwort steckt nicht nur im Magen."
INTRO = "Dein Gehirn sammelt Signale aus Magen, Darm und Blut und entscheidet daraus, ob du satt bist. " * 6
MAIN = "Der Magen dehnt sich, Nerven melden die Dehnung, und der Darm schickt Botenstoffe los, die das Gehirn bremsen. " * 40
END = "Satt sein bedeutet also mehr als ein voller Magen: Viele Signale arbeiten zusammen und halten dich unterschiedlich lange satt. " * 4
ARC = {
    "hook_frage": "Warum hast du kurz nach dem Essen wieder Hunger?",
    "wendung": "Hunger entsteht nicht nur im Magen, sondern im Zusammenspiel vieler Signale.",
    "payoff": "Wir verfolgen die Signale von Magen und Darm bis ins Gehirn.",
    "schluss_antwort": "Wie lange du satt bleibst, haengt von mehreren Signalen und deiner Mahlzeit ab.",
}


def build(parts=None, arc=ARC):
    parts = parts or [("hook", HOOK), ("einleitung", INTRO), ("hauptteil", MAIN), ("schluss", END)]
    scenes = [
        {"scene": i + 1, "image": f"Bild_{i + 1:02d}", "script_part": part, "speech_section": speech.strip()}
        for i, (part, speech) in enumerate(parts)
    ]
    script = "\n\n".join(speech.strip() for _, speech in parts)
    return script, {"script_arc": dict(arc), "scenes": scenes}


def flow_for(n):
    return "COVER RULE: exactly one visible text block.\nNot a flat vector diagram, not clip-art.\n" + "\n".join(
        f"{i:02d} / Bild_{i:02d}.png | cutaway scene" for i in range(1, n + 1)
    )


class ScriptStructureTests(unittest.TestCase):
    def test_old_010_is_not_retroactively_blocked(self):
        self.assertIn("HISTORISCHES", check_script_structure(Path("010-longform-hunger"), "", {}, POLICY))
        self.assertIn("HISTORISCHES", check_flow_register(Path("010-longform-hunger"), {}, "", POLICY))

    def test_good_script_passes(self):
        script, data = build()
        self.assertIn("PASS", check_script_structure(Path("011-next-video"), script, data, POLICY))

    def test_unfilled_template_script_fails(self):
        _, data = build()
        template = Path(__file__).resolve().parents[2] / "youtube-videos/_TEMPLATE/01_script/script.txt"
        with self.assertRaisesRegex(ContentGateError, "Vorlagentext"):
            check_script_structure(Path("011-next-video"), template.read_text(encoding="utf-8"), data, POLICY)

    def test_scene_gap_fails(self):
        script, data = build()
        data["scenes"][2]["speech_section"] = data["scenes"][2]["speech_section"][:-80]
        with self.assertRaisesRegex(ContentGateError, "nicht exakt"):
            check_script_structure(Path("011-next-video"), script, data, POLICY)

    def test_missing_schluss_fails(self):
        script, data = build([("hook", HOOK), ("einleitung", INTRO), ("hauptteil", MAIN + END)])
        with self.assertRaisesRegex(ContentGateError, "schluss"):
            check_script_structure(Path("011-next-video"), script, data, POLICY)

    def test_wrong_order_fails(self):
        script, data = build([("hook", HOOK), ("hauptteil", MAIN), ("einleitung", INTRO), ("schluss", END)])
        with self.assertRaisesRegex(ContentGateError, "Reihenfolge"):
            check_script_structure(Path("011-next-video"), script, data, POLICY)

    def test_weak_opening_and_long_hook_fail(self):
        script, data = build([("hook", "Hallo und willkommen! " + HOOK), ("einleitung", INTRO),
                              ("hauptteil", MAIN), ("schluss", END)])
        with self.assertRaisesRegex(ContentGateError, "schwachem Intro"):
            check_script_structure(Path("011-next-video"), script, data, POLICY)
        script, data = build([("hook", HOOK * 4), ("einleitung", INTRO), ("hauptteil", MAIN), ("schluss", END)])
        with self.assertRaisesRegex(ContentGateError, "Hook"):
            check_script_structure(Path("011-next-video"), script, data, POLICY)

    def test_too_short_script_and_missing_arc_fail(self):
        script, data = build([("hook", HOOK), ("einleitung", INTRO), ("hauptteil", MAIN[:2000]), ("schluss", END)])
        with self.assertRaisesRegex(ContentGateError, "Woerter"):
            check_script_structure(Path("011-next-video"), script, data, POLICY)
        script, data = build(arc={**ARC, "schluss_antwort": "[Antwort]"})
        with self.assertRaisesRegex(ContentGateError, "schluss_antwort"):
            check_script_structure(Path("011-next-video"), script, data, POLICY)


class FlowRegisterTests(unittest.TestCase):
    def test_complete_register_passes(self):
        _, data = build()
        self.assertIn("PASS", check_flow_register(Path("011-next-video"), data, flow_for(4), POLICY))

    def test_missing_image_and_template_text_fail(self):
        _, data = build()
        with self.assertRaisesRegex(ContentGateError, "Bild_04"):
            check_flow_register(Path("011-next-video"), data, flow_for(3), POLICY)
        with self.assertRaisesRegex(ContentGateError, "ungeplante"):
            check_flow_register(Path("011-next-video"), data, flow_for(5), POLICY)
        template = Path(__file__).resolve().parents[2] / "youtube-videos/_TEMPLATE/02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt"
        with self.assertRaisesRegex(ContentGateError, "Platzhalter"):
            check_flow_register(Path("011-next-video"), data, template.read_text(encoding="utf-8"), POLICY)

    def test_missing_depth_line_fails(self):
        _, data = build()
        flat = flow_for(4).replace("Not a flat vector diagram, not clip-art.\n", "")
        with self.assertRaisesRegex(ContentGateError, "Tiefenzeile"):
            check_flow_register(Path("011-next-video"), data, flat, POLICY)


if __name__ == "__main__":
    unittest.main()
