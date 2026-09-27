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

## Aktiver Testpilot

`youtube-videos/005-pilot-sauerstoff-zelle/`

Thema: **Wie kommt Sauerstoff von der Lunge bis in eine einzelne Koerperzelle?**

Pilot 005 ist ein dokumentierter Kurztest mit harter finaler Obergrenze von 2:00 Minuten und testet die neue Bildwelt ueber Lunge, Blut, Herz, Zelle und Mitochondrium.

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
→ Remotion / Render
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

## V2-Pruefung

```bash
python tools/validate_planning_v2.py youtube-videos/MEIN-VIDEO
python tools/validate_planning_v2.py youtube-videos/MEIN-VIDEO --phase2
```

## Goldene Regel

**Schoene Illustration + sofort verstaendliche Biologie + wenig Komplexitaet + klare Beschriftung.**
