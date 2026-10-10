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

## Veröffentlichungs-Export

Autoritativ: `EXPORT-STANDARD.md`

Jedes fertige Video braucht unter `04_export/`:
- finale YouTube-MP4
- `CAPTION-YOUTUBE.txt` mit Titel + Beschreibung + max. 5 Hashtags
- `UNTERTITEL-MIT-ZEITEN.txt` mit komplettem gesprochenem Script und echten Zeitabschnitten
- `UNTERTITEL-YOUTUBE.srt` als hochladbare externe YouTube-Untertiteldatei
- Renderbericht
- Quality-Scorecard
- Postmortem

Untertitel werden nicht eingebrannt. Sie werden nach der finalen Timeline automatisch erzeugt:

```text
final-voiceover.wav
→ Whisper
→ word-timings.json
→ timeline.json
→ tools/export_subtitles.py
→ UNTERTITEL-MIT-ZEITEN.txt + UNTERTITEL-YOUTUBE.srt
```

Zeitcodes niemals schätzen.

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
→ Postmortem
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
