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

    def test_plain_words_unchanged(self):
        self.assertEqual(normalize_token("Magen,"), "magen")
        self.assertEqual(normalize_token("Straße"), "strasse")

    def test_number_to_words_samples(self):
        self.assertEqual(number_to_words(21), "einundzwanzig")
        self.assertEqual(number_to_words(1000), "tausend")
        self.assertEqual(number_to_words(2100), "zweitausendhundert")


if __name__ == "__main__":
    unittest.main()
