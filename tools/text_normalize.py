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
- canonical forms: "ein" (not "eins"), "hundert"/"tausend" (not "einhundert"/"eintausend")
- four-digit numbers 1100-1999 are read as years ("neunzehnhundertfuenfundneunzig")
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
    if 1100 <= n <= 1999:  # years: 1995 -> neunzehnhundertfünfundneunzig
        century, rest = divmod(n, 100)
        return _TEENS[century] + "hundert" + (_below_hundred(rest) if rest else "")
    if n < 1000:
        return _below_thousand(n)
    thousands, rest = divmod(n, 1000)
    prefix = ("" if thousands == 1 else _below_thousand(thousands)) + "tausend"
    return prefix + (_below_thousand(rest) if rest else "")


def _canonical_words(value: str) -> str:
    value = value.replace("einhundert", "hundert").replace("eintausend", "tausend")
    if value.endswith("eins"):  # "eins", "GLP-eins" == "1", "GLP-1"; applied to both sides alike
        return value[:-1]
    return value


def normalize_token(value: str) -> str:
    value = unicodedata.normalize("NFKC", str(value)).lower().replace("ß", "ss")
    for symbol, word in _SYMBOLS.items():
        value = value.replace(symbol, word)
    value = "".join(ch for ch in value if ch.isalnum())
    value = _DIGITS_RE.sub(lambda match: number_to_words(int(match.group(0))), value)
    return _canonical_words(value)
