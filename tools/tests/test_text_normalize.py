"""Spelled-out script numbers must align with Whisper digits (no guessed timings)."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from text_normalize import normalize_token, number_to_words


def joined(text: str) -> str:
    return "".join(normalize_token(part) for part in text.split())


class TextNormalizeTests(unittest.TestCase):
    def test_digits_equal_number_words(self):
        pairs = [
            ("15", "fünfzehn"),
            ("38", "achtunddreißig"),
            ("2014", "zweitausendvierzehn"),
            ("500", "fünfhundert"),
            ("100", "einhundert"),
            ("100", "hundert"),
            ("1", "eins"),
            ("30", "dreißig"),
            ("1995", "neunzehnhundertfünfundneunzig"),
        ]
        for digits, words in pairs:
            with self.subTest(digits=digits):
                self.assertEqual(normalize_token(digits), normalize_token(words))

    def test_percent_and_acronyms_group_like_the_aligner(self):
        self.assertEqual(joined("15%"), joined("fünfzehn Prozent"))
        self.assertEqual(joined("GLP-1"), joined("GLP eins"))
        self.assertEqual(joined("GLP-1"), joined("GLP-eins"))

    def test_ranges_decimals_thousands_and_years(self):
        self.assertEqual(joined("2-3"), joined("zwei bis drei"))
        self.assertEqual(joined("1–2"), joined("ein bis zwei"))
        self.assertEqual(joined("2,5"), joined("zwei Komma fünf"))
        self.assertEqual(normalize_token("1.500"), normalize_token("1500"))
        self.assertEqual(normalize_token("1500"), normalize_token("tausendfünfhundert"))
        self.assertEqual(normalize_token("1500"), normalize_token("fünfzehnhundert"))
        self.assertEqual(normalize_token("1100"), normalize_token("tausendeinhundert"))
        self.assertNotEqual(joined("2,5"), joined("fünfundzwanzig"))
        self.assertNotEqual(joined("1-2"), joined("zwölf"))
        self.assertNotEqual(normalize_token("201000"), normalize_token("200000"))

    def test_plain_words_unchanged(self):
        self.assertEqual(normalize_token("Magen,"), "magen")
        self.assertEqual(normalize_token("Straße"), "strasse")

    def test_number_to_words_samples(self):
        self.assertEqual(number_to_words(21), "einundzwanzig")
        self.assertEqual(number_to_words(1000), "tausend")
        self.assertEqual(number_to_words(2100), "zweitausendhundert")


if __name__ == "__main__":
    unittest.main()
