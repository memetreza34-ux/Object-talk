# Engine

Dieser Ordner enthaelt die globalen Produktionsregeln fuer Object-Talk-YouTube-Videos.

## Zweck

Die Engine sorgt dafuer, dass Recherche, Script, Planung, Audio, Timing und QA nicht bei jedem Video neu erfunden werden.

Sie definiert weiterhin:
- Themenauswahl und Abgrenzung
- neugiergetriebenes Scriptwriting
- Mechanism Map und Satz-Visual-Planung
- Longform-Laenge und Testausnahmen
- semantischen Bildrhythmus
- wissenschaftliche Pruefung
- Voice-/Audio-Standard
- Whisper-/Script-Synchronisierung
- Asset-Hygiene
- QA und Postmortem

## WICHTIG: KEINE AKTIVE BILDWELT

Alle bisherigen kanalweiten Bildwelt-Definitionen wurden am 27.09.2026 entfernt.

Die Engine legt aktuell NICHT fest:
- 2D / 2.5D / 3D
- Renderstil
- Character-Look
- Anatomie-Look
- Farbpalette
- Materialien
- Licht
- Kameraaesthetik
- Style Reference
- finale Text-/Overlay-Strategie

Historische Piloten koennen alte Stilregeln enthalten. Sie sind keine Autoritaet fuer die neue Bildwelt.

## Aktiver Testpilot

`youtube-videos/004-pilot-muskelkater/`

Die inhaltliche Planung bleibt bestehen. Finale Bildproduktion ist pausiert, bis eine neue Bildwelt getestet und vom Nutzer freigegeben wurde.

## Aktueller Produktionsablauf

```text
Themen-Gehirn + Themen-Score
→ Recherche + Claim-Matrix
→ Mechanism Map
→ Script
→ Satz-Visual-Plan
→ semantische Szenen
→ Label-/Textbedarf
→ PHASE-1-PASS
→ STYLE GATE
→ neue Bildwelt testen und freigeben
→ danach Medienproduktion
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
- `FLOW-AGENT-INSTRUCTIONS.md` – aktuell mit Style-Gate statt festem Stil

## V2-Pruefung

```bash
python tools/validate_planning_v2.py youtube-videos/MEIN-VIDEO
python tools/validate_planning_v2.py youtube-videos/MEIN-VIDEO --phase2
```

## Goldene Regel

**Keine historische Bildwelt als Standard reaktivieren. Neue Bildwelt erst testen und ausdruecklich freigeben.**
