GOOGLE FLOW – PILOT 001 „SAUERSTOFF VON DER LUNGE BIS ZUR ZELLE“

Diese Datei spiegelt die Produktionsregeln fuer:

```text
youtube-videos/001-pilot-sauerstoff-im-blut/02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt
```

Verwende zuerst die dauerhaften Agent Instructions aus:

```text
engine/FLOW-AGENT-INSTRUCTIONS.md
engine/FLOW-PRODUCTION-STANDARD.md
```

Danach gilt fuer diesen Pilot:

- zuerst nur `Bild_01`
- nur `Bild_01` darf bis zu 3 Cover-Varianten haben
- Nutzer waehlt genau 1 Cover; alle anderen Cover-Kandidaten danach loeschen/verwerfen
- wenn vorhanden `STYLE_REFERENCE.png` als echte visuelle Referenz anhaengen
- nach Freigabe das eine `Bild_01.png` bei jeder Generation von `Bild_02` bis `Bild_35` als echtes Reference/Ingredient anhaengen
- fuer normale Szenen genau einen Kandidaten pro Versuch und genau ein retained asset pro Bildnummer
- FAIL-Version derselben Nummer ersetzen, nicht zusaetzlich sammeln
- dasselbe Bild niemals fuer zwei Szenen verwenden
- keine textlichen Referenzsaetze als Ersatz fuer echte Attachments behandeln
- moderne stilisierte 2.5D / Soft-3D Educational Illustration
- 80 % animierte Illustration / 20 % Soft-3D-Tiefe / 0 % Medical-CGI
- keine kosmische, dunkle, Sci-Fi- oder medizinisch-realistische Bildwelt
- pro Bild ein dominanter Lehrpunkt; wichtige Mechanismus-/Zusammenfassungsbilder duerfen einen sinnvollen Zusatzdetailpunkt haben

## Sichtbarer Text – strikte Whitelist

- `Bild_01` darf sichtbar NUR die Hook „So reist Sauerstoff durch deinen Körper“ enthalten
- normale Bilder duerfen sichtbar NUR die im kanonischen Szenenprompt aufgelisteten Labels enthalten
- kein erfundener Titel / kein Extra-Erklaertext
- kein englischer sichtbarer Text
- interne Produktionsnamen sind niemals Bildtext

Hard FAIL wenn sichtbar:
- `Bild 19`
- `Bild_19`
- `BILD_12 – O2 BINDET`
- `Scene 19`
- `IMAGE 19`
- Dateiname / Asset-ID / Prompt-Ueberschrift

Flow-Textfehler zuerst regenerieren; Remotion nur als exakter Fallback.

## Objekt-Lock

- kein O2-Guide und kein O2-Maskottchen
- O2 = Cyan/Tuerkis, gesichtslos
- CO2 = weiches Violett, gesichtslos
- rote Blutkoerperchen = tiefes warmes Rot
- Haemoglobin = Burgunder
- Organe/Zellen stark stilisiert und gesichtslos

Die vollstaendigen **35 eindeutigen Szenenprompts** und die ALLOWED_VISIBLE_TEXT-Whitelist stehen kanonisch in:

```text
youtube-videos/001-pilot-sauerstoff-im-blut/02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt
```

Bei Aenderungen immer die kanonische TXT-Datei zuerst aktualisieren und diese Datei danach synchron halten.
