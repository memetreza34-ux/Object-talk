# Engine

Dieser Ordner enthaelt die globalen Produktionsregeln fuer Object-Talk-YouTube-Videos.

## Zweck

Die Engine sorgt dafuer, dass Recherche, Script, Planung, Bildproduktion, Audio, Timing und QA nicht bei jedem Video neu erfunden werden.

## Verbindliche Bildwelt

Kanalweit gilt:

**Clean Animated Biology Illustration**

Autoritativ:
- `../bildwelt/BIOLOGY-ILLUSTRATION-WORLD.md`
- `../bildwelt/FLOW-STYLE-BLOCK.txt`

Die alte 2.5D-/Soft-3D- und Premium-3D-Logik darf nicht reaktiviert werden.

## Visuelles Prinzip

- vereinfachte, erkennbare Biologie
- saubere animierte Illustration
- weiche organische Formen
- klare Konturen
- weiche Verlaeufe und leichte Tiefe
- helle ruhige Hintergruende
- wenige wichtige Elemente
- ein klarer Prozess pro Bild
- 1–3 kurze deutsche Labels, wenn sinnvoll
- unterschiedliche Kompositionen statt wiederholter Objektportraits

## Praesentationssystem

**100 % Vollbild-Illustration. Remotion erzeugt keinen sichtbaren Text.**

Remotion darf nur:
- Audio
- Timing
- statische Frames
- leichte Push-/Pull-/Pan-Bewegungen
- Schnitte
- dezente nicht-textliche Uebergaenge
- Rendering

Viewer-facing Text kommt ausschliesslich aus den akzeptierten Flow-Bildern. Produktions-IDs, Bildnummern, Szenennummern und Dateinamen bleiben immer unsichtbar.

Autoritativ: `PRESENTATION-OVERLAY-SYSTEM.md`

## Aktiver Testpilot

`youtube-videos/007-pilot-gaensehaut/`

Thema: **Warum bekommst du Gänsehaut?**

Pilot 007 ist ein dokumentierter Kurztest mit harter finaler Obergrenze von 2:00 Minuten. Er testet Hautoberflaeche, Hautquerschnitt, Nervensignal, sympathisches Nervensystem, Haarfollikel, Haaraufrichtemuskel und Tierfell in derselben Bildwelt. Remotion erzeugt dabei keinerlei sichtbaren Text.

## Produktionsablauf

```text
Themen-Gehirn + Themen-Score
→ Recherche + Claim-Matrix
→ Mechanism Map
→ Script
→ Satz-Visual-Plan
→ semantische Szenen
→ Label-Plan
→ kurze Flow-Prompts
→ Google Flow Bild fuer Bild
→ Bild-QA
→ Audio + Whisper
→ exakte Szenen-Timeline
→ Remotion / Render ohne sichtbaren Editor-Text
→ technischer + visueller Final-QA
→ Postmortem
```

## Wichtige Dateien

- `SCRIPT-STANDARD.md`
- `PLANNING-V2.md`
- `FACT-CHECK-STANDARD.md`
- `AUDIO-REGELN.md`
- `SYNC-WHISPER.md`
- `PHASE-GATES.md`
- `QUALITY-SCORECARD.md`
- `POSTMORTEM-STANDARD.md`
- `FLOW-AGENT-INSTRUCTIONS.md`
- `FLOW-PRODUCTION-STANDARD.md`
- `PRESENTATION-OVERLAY-SYSTEM.md`

## V2-Pruefung

```bash
python tools/validate_planning_v2.py youtube-videos/MEIN-VIDEO
python tools/validate_planning_v2.py youtube-videos/MEIN-VIDEO --phase2
```

## Goldene Regel

**Schoene Vollbild-Illustration + Voice + dezente Bewegung. Kein sichtbarer Remotion-Text und keine sichtbaren Produktionsnummern.**
