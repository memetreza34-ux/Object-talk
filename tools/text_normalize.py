#!/usr/bin/env python3
"""Shared token normalisation for strict script/audio alignment.

Whisper often writes spoken German numbers as digits ("15 Prozent", "2014",
"GLP-1"), while the voice-over script spells them out ("fünfzehn Prozent").
Without a common form, the strict aligner fails and agents start avoiding
concrete numbers in scripts. This module maps both sides to one canonical
spelling. It is only used for COMPARISON; displayed text never changes.

Rules:
- lowercase, NFKC, ß -> ss, keep letters/digits only
- "%" -> "prozent"
- every digit run (0-999999) -> German number word (canonical form)
- separators between digits are spoken: "2-3" -> "zwei bis drei", "2,5" -> "zwei komma fuenf",
  "1.500" -> "1500", "20:15" -> "zwanzig uhr fuenfzehn"
- canonical forms: "ein" (not "eins"), "hundert" (not "einhundert"), leading "tausend" (not "eintausend")
- 1100-1999 compare equal in both spoken forms: "fuenfzehnhundert" == "tausendfuenfhundert" == "1500"
"""

from __future__ import annotations

import re
import unicodedata

_UNITS = ["null", "ein", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun"]
_TEENS = {
    10: "zehn", 11: "elf", 12: "zwölf", 13: "dreizehn", 14: "vierzehn",
    15: "fünfzehn", 16: "sechzehn", 17: "siebzehn", 18: "achtzehn", 19: "neunzehn",
}
_TENS = {
    2: "zwanzig", 3: "dreissig", 4: "vierzig", 5: "fünfzig",
    6: "sechzig", 7: "siebzig", 8: "achtzig", 9: "neunzig",
}
_DIGITS_RE = re.compile(r"\d+")
_SYMBOLS = {"%": " prozent ", "€": " euro ", "°": " grad "}
_SEPARATORS = (
    (re.compile(r"(?<=\d)\.(?=\d{3}(?!\d))"), ""),        # 1.500 -> 1500 (thousands separator)
    (re.compile(r"(?<=\d)\s*[-–]\s*(?=\d)"), " bis "),   # 2-3 -> 2 bis 3
    (re.compile(r"(?<=\d),(?=\d)"), " komma "),            # 2,5 -> 2 komma 5
    (re.compile(r"(?<=\d):00\b"), " uhr "),                # 20:00 -> 20 uhr
    (re.compile(r"(?<=\d):(?=\d)"), " uhr "),              # 20:15 -> 20 uhr 15
)
_YEAR_FORM_RE = re.compile(r"(elf|zwölf|dreizehn|vierzehn|fünfzehn|sechzehn|siebzehn|achtzehn|neunzehn)hundert")
_YEAR_TO_THOUSAND = {
    "elf": "", "zwölf": "zwei", "dreizehn": "drei", "vierzehn": "vier", "fünfzehn": "fünf",
    "sechzehn": "sechs", "siebzehn": "sieben", "achtzehn": "acht", "neunzehn": "neun",
}


def _below_hundred(n: int) -> str:
    if n < 10:
        return _UNITS[n]
    if n < 20:
        return _TEENS[n]
    tens, unit = divmod(n, 10)
    if unit == 0:
        return _TENS[tens]
    return _UNITS[unit] + "und" + _TENS[tens]


def _below_thousand(n: int) -> str:
    hundreds, rest = divmod(n, 100)
    prefix = ""
    if hundreds:
        prefix = ("" if hundreds == 1 else _UNITS[hundreds]) + "hundert"
    if rest == 0:
        return prefix or "null"
    return prefix + _below_hundred(rest)


def number_to_words(n: int) -> str:
    """Canonical German spelling for 0..999999 (comparison form, not display form)."""
    if n < 0 or n > 999_999:
        return str(n)
    if n < 1000:
        return _below_thousand(n)
    thousands, rest = divmod(n, 1000)
    prefix = ("" if thousands == 1 else _below_thousand(thousands)) + "tausend"
    return prefix + (_below_thousand(rest) if rest else "")


def _canonical_words(value: str) -> str:
    # "neunzehnhundert..." (year reading) and "tausendneunhundert..." are the same number
    value = _YEAR_FORM_RE.sub(lambda m: "tausend" + _YEAR_TO_THOUSAND[m.group(1)] + "hundert", value)
    value = value.replace("einhundert", "hundert")
    # only a LEADING "eintausend" means 1000; inside "hunderteintausend" (101000) the "ein" is a real digit
    value = re.sub(r"^eintausend", "tausend", value)
    if value.endswith("eins"):  # "eins", "GLP-eins" == "1", "GLP-1"; applied to both sides alike
        return value[:-1]
    return value


def normalize_token(value: str) -> str:
    value = unicodedata.normalize("NFKC", str(value)).lower().replace("ß", "ss")
    for symbol, word in _SYMBOLS.items():
        value = value.replace(symbol, word)
    for pattern, spoken in _SEPARATORS:
        value = pattern.sub(spoken, value)
    value = "".join(ch for ch in value if ch.isalnum())
    value = _DIGITS_RE.sub(lambda match: number_to_words(int(match.group(0))), value)
    return _canonical_words(value)
