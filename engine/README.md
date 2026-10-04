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
- `VISIBLE-TEXT-STANDARD.md`

Die alte 2.5D-/Soft-3D- und Premium-3D-Logik darf nicht reaktiviert werden.

## Visuelles Prinzip

- vereinfachte, erkennbare Biologie
- saubere animierte Illustration
- weiche organische Formen
- klare Konturen
- weiche Verlaeufe und leichte Tiefe
- helle ruhige Hintergruende
- **eine Hauptidee pro Bild**
- bevorzugt 2–4 wichtige sichtbare Elemente
- normale Bilder **0–2 kurze deutsche Labels**, nur wenn wirklich sinnvoll
- unterschiedliche Kompositionen statt wiederholter Objektportraits
- lieber mehr einfache Bilder als ein ueberladenes Bild

## Cover

Cover / `Bild_01`:
- genau ein sichtbarer Textblock
- nur Titel / Hook
- keine Anatomie-Labels
- keine Unterzeile
- keine Zusatzinfo

Zusatztext auf dem Cover = FAIL.

## Textkontrast

- heller Hintergrund → dunkle Schrift
- dunkler Hintergrund → helle Schrift
- kein light-on-light / dark-on-dark
- Text in ruhiger negativer Flaeche bevorzugen

Schlecht lesbarer Text = FAIL.

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

## Aktive Produktion

`youtube-videos/008-longform-verdauung/`

Thema: **Was passiert mit Essen in deinem Koerper?**

Status: **erstes regulaeres Longform-Video**

Ziel:
- 6–7 Minuten
- ca. 1.110 Woerter Voiceover
- 77 eindeutige Bilder
- komplette Verdauungsreise von Mund bis Enddarm
- wissenschaftlich gepruefte Trennung von Blut- und Lymphweg
- Hook → Einleitung → kausaler Hauptteil → Schluss

Die Testphase `000–007` bleibt als historische Lernbasis erhalten, ist aber nicht mehr aktive Produktion.

## Produktionsablauf

```text
Themen-Gehirn + Themen-Score
→ Recherche + Claim-Matrix
→ Mechanism Map
→ Script
→ Satz-Visual-Plan
→ semantische Szenen
→ Informationsbudget pruefen
→ Label-Plan
→ kurze Flow-Prompts
→ Google Flow Bild fuer Bild
→ Cover/Textkontrast/Informationsdichte-QA
→ Audio + Whisper
→ exakte Szenen-Timeline
→ Remotion / Render ohne sichtbaren Editor-Text
→ technischer + visueller Final-QA
→ Postmortem
```

## Wichtige Dateien

- `SCRIPT-STANDARD.md`
- `PLANNING-V2.md`
- `VISIBLE-TEXT-STANDARD.md`
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

**Cover nur Titel. Ein Bild = eine Hauptidee. 0–2 Labels. Hoher Textkontrast. Lieber mehr Bilder als mehr Text. Kein sichtbarer Remotion-Text.**
