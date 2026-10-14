# Engine

Dieser Ordner enthaelt die globalen Produktionsregeln fuer Object-Talk-YouTube-Videos.

## Zweck

Die Engine sorgt dafuer, dass Recherche, Script, Planung, Bildproduktion, Audio, Timing, Export und QA nicht bei jedem Video neu erfunden werden.

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

Separates Cover (nicht `Bild_01`):
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

## Veröffentlichungs-Export

Ab neuen Videos nach `EXPORT-STANDARD.md`: `03_export/` mit genau `VIDEO.mp4`, `COVER.png`, `CAPTION-YOUTUBE.txt`, `UNTERTITEL-MIT-ZEITEN.txt`. Alle technischen SRT/QA/Scorecard/Postmortem-Dateien nach `.intern/`. Zeitcodes nur aus echtem finalem Audio.

## Höchste Priorität: Verbesserung nach jedem Video

`CONTINUOUS-IMPROVEMENT.md` verpflichtet zur echten Sichtung, Ursachenanalyse, 2–5 umgesetzten und überprüften globalen Verbesserungen und zur Übernahme der Lessons in die nächste Phase 1. Technische Prüfung: `tools/improvement_loop.py`. Kein neuer sichtbarer Nutzerordner.

## Bewährte Longform-Referenz

Für reguläre 6–7-Minuten-Videos gilt `engine/LONGFORM-008-MASTERSTANDARD.md`. Video 008 Verdauung zeigt das bewährte reine Textprompt-Verfahren für Flow-Stil, 77 Szenen, 13 Mechanismus-Abschnitte, ausführlichen Remotion-Prompt, Export und QA. Keine visuellen Stilvorlagen. 009 nutzt denselben Aufbau für Schlaf.

## Aktive Produktion

`youtube-videos/009-longform-schlaf/`

Thema: **Was passiert in deinem Körper, während du schläfst?**

Status: **Longform 009 / Phase 1 erstellt / Medien ausstehend**.

- 6–7 Minuten Ziel; 986 Wörter; 77 individuelle Flow-Bilder.
- Themen: Schlafdruck, innere Uhr, Schlafstadien, Herz, Hormone, Gedächtnis, Immunsystem und REM.
- Erstes Cover kurz, nur Titel; Farb-/Lichtvariation; kein überladener Mehrfachprozess.
- Vorheriger Longform-Film: 008 Verdauung.

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
→ zeitcodierte Untertitel exportieren
→ Remotion / Render ohne sichtbaren Editor-Text
→ technischer + visueller Final-QA
→ YouTube-Exportpaket vervollstaendigen
→ Postmortem + dauerhafte Repo-Fixes + Improvement-Ledger + Lessons im nächsten Video
```

## Wichtige Dateien

- `SCRIPT-STANDARD.md`
- `PLANNING-V2.md`
- `VISIBLE-TEXT-STANDARD.md`
- `EXPORT-STANDARD.md`
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

**Cover nur Titel. Ein Bild = eine Hauptidee. 0–2 Labels. Hoher Textkontrast. Kein sichtbarer Remotion-Text. Export = MP4 + Caption + echte zeitcodierte Untertitel + QA.**
