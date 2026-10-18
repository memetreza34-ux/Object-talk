"""The retention gate must catch the measured weaknesses of 008-010 and pass a concrete script."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from script_quality import analyze, estimate_seconds, gate

HEDGY = (
    "Hunger kann viele Ursachen haben. Manchmal hängt er oft mit verschiedenen Faktoren zusammen. "
    "Das bedeutet nicht, dass etwas falsch ist. Bestimmte Lebensmittel können eher helfen. "
    "Das bedeutet aber nicht automatisch, dass sie wirken. Aber Vorsicht: Es gibt keine Garantie. "
) * 6
CONCRETE = (
    "Du isst ein Croissant. Warum bist du eine Stunde später hungrig? In einem Versuch mit achtunddreißig "
    "Lebensmitteln schnitten Kartoffeln fast siebenmal besser ab. Rund fünfzehn Prozent weniger aß man nach "
    "einem Apfel. Was steckt dahinter? Zwei Nächte mit vier Stunden Schlaf erhöhten Ghrelin um "
    "achtundzwanzig Prozent. Und der Nachtisch? Den klären wir am Ende."
)


def storyboard(setup=2, payoff=30, scene_text="Kurzer Satz."):
    scenes = [{"speech": scene_text} for _ in range(40)]
    return {"chapters": [{"scenes": scenes}], "open_loops": [{"setup_scene": setup, "payoff_scene": payoff}]}


class ScriptQualityTests(unittest.TestCase):
    def test_hedgy_textbook_script_fails(self):
        problems = gate(analyze(HEDGY), None)
        joined = " ".join(problems)
        self.assertIn("Absicherungswörter", joined)
        self.assertIn("Disclaimer", joined)
        self.assertIn("Zahlen", joined)

    def test_concrete_script_passes_text_checks(self):
        self.assertEqual(gate(analyze(CONCRETE), None), [])

    def test_open_loop_needs_distance(self):
        self.assertEqual(gate(analyze(CONCRETE), storyboard(2, 30)), [])
        problems = gate(analyze(CONCRETE), storyboard(2, 6))
        self.assertTrue(any("Open Loop zu kurz" in p for p in problems))
        problems = gate(analyze(CONCRETE), {"chapters": [{"scenes": [{"speech": "a"}] * 40}]})
        self.assertTrue(any("kein Open Loop" in p for p in problems))

    def test_long_scene_is_flagged(self):
        long_text = "Sättigungshormone " * 18
        problems = gate(analyze(CONCRETE), storyboard(scene_text=long_text))
        self.assertTrue(any("Sprechzeit" in p for p in problems))
        self.assertLess(estimate_seconds("Du isst ein Croissant."), 2.0)


if __name__ == "__main__":
    unittest.main()
