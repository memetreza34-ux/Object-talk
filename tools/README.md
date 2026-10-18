# Tools

Diese Tools automatisieren die technischen Teile der Object-Talk-Longform-Pipeline.

## Voraussetzungen

### Python

```bash
python -m pip install -r tools/requirements.txt
```

### FFmpeg

`ffmpeg` und `ffprobe` müssen in PATH verfügbar sein:

```bash
ffmpeg -version
ffprobe -version
```

### Remotion

Für Preview und Render:

```bash
cd renderer
npm install
```

## Neues Video anlegen

```bash
python tools/create_video.py "Was passiert mit Zucker im Koerper"
```

Das kopiert `youtube-videos/_TEMPLATE` in einen neuen Themenordner. Bestehende Projekte werden nicht überschrieben.

## V2-Planung validieren

Vor der Medienproduktion:

```bash
python tools/validate_planning_v2.py youtube-videos/THEMA
```

Geprüft werden unter anderem:
- vollständige `mechanism-map.md`
- vollständiger `sentence-visual-plan.json`
- stabile `Bild_XX`-IDs
- Übereinstimmung mit `phase1-scenes.json`
- vollständiger Label-Plan
- normale Bilder maximal 2 Labels
- Labels maximal 3 Wörter
- Cover title-only
- Textkontrast-Regeln
- keine offenen Template-/PENDING-Werte
- ab Video 011 (`tools/phase1_content_gate.py`): `script.txt` ausgefüllt, 900–1200 Wörter, Hook → Einleitung → Hauptteil → Schluss über `script_part` je Szene und `script_arc`, `speech_section`-Texte decken das Skript 1:1 ab, und der Flow-Prompt enthält jedes geplante `Bild_XX` ohne Vorlagenreste

Nach der finalen Bildauswahl:

```bash
python tools/validate_planning_v2.py youtube-videos/THEMA --phase2
```

Zusätzlich geprüft:
- jedes erwartete Bild besitzt ein Review
- `decision` ist `ACCEPT`
- Gesamtscore mindestens 8,0/10
- wissenschaftliche Genauigkeit mindestens 8,0/10
- AI-Artefakt-Check bestanden
- Textkontrast und Informationsdichte bestanden

## Phase 1 technisch validieren

```bash
python tools/validate_phase1.py \
  youtube-videos/THEMA/01_script/script.txt \
  youtube-videos/THEMA/05_info/phase1-scenes.json \
  youtube-videos/THEMA/03_pipeline/scene-map.json
```

## Empfohlen: komplette Phase-3-Vorbereitung mit einem Befehl

Sobald rohe Voice-Datei und Flow-ZIP vorhanden sind:

```bash
python tools/prepare_phase3.py youtube-videos/THEMA
```

Dieser Befehl führt automatisch aus:

### 1. Audio kanonisieren

`tools/prepare_audio.py`

Erzeugt `final-voiceover.wav` mit dem kanalweiten Voice-Standard.

### 2. Flow-ZIP sicher importieren

`tools/import_flow_zip.py`

Keine Zuordnung nach ZIP-Reihenfolge; nur explizite `Bild_XX`-IDs zählen.

### 3. Bilder technisch validieren

`tools/validate_assets.py`

### 4. Whisper + strikte Script-Ausrichtung

`tools/transcribe_audio.py`

Erzeugt unter anderem:

```text
03_pipeline/timing/whisper-raw.json
03_pipeline/timing/word-timings.json
03_pipeline/timing/subtitles.srt
```

`word-timings.json` enthält die exakten Script-Wörter mit echten Audiozeiten.

### 5. Timeline bauen

`tools/build_timeline.py`

Erzeugt:

```text
03_pipeline/timing/timeline.json
```

Jede `speech_section` wird sequenziell auf echte Wortzeiten abgebildet. Keine geschätzten Sekunden.

### 6. Veröffentlichungs-Untertitel automatisch exportieren

`prepare_phase3.py` ruft automatisch auf:

```bash
python tools/export_subtitles.py youtube-videos/THEMA
```

Erzeugt/überschreibt:

```text
04_export/UNTERTITEL-MIT-ZEITEN.txt
04_export/UNTERTITEL-YOUTUBE.srt
```

`UNTERTITEL-MIT-ZEITEN.txt` enthält das komplette gesprochene Script mit Zeitabschnitten, z. B.:

```text
00:00–00:06  Hast du dich schon mal gefragt, ...
00:06–00:12  Danach passiert ...
```

`UNTERTITEL-YOUTUBE.srt` ist direkt als externe Untertiteldatei bei YouTube hochladbar.

Wichtig:
- Untertitel werden nicht in das Video eingebrannt.
- Zeitcodes werden niemals geschätzt.
- finale `timeline.json` ist die Timing-Quelle.

### 7. Feste Remotion-Runtime bauen

`tools/build_renderer_runtime.py`

Danach:

```bash
cd renderer
npm run studio
npm run render -- ../youtube-videos/THEMA/04_export/fertiges-video/[VIDEO-ID]-YOUTUBE.mp4
```

## Export-Paket für zukünftige Videos

Verbindlich ist `engine/EXPORT-STANDARD.md`. **Im sichtbaren `03_export/` stehen nach Fertigstellung genau diese vier Dateien**:

```text
03_export/
  VIDEO.mp4
  COVER.png
  CAPTION-YOUTUBE.txt
  UNTERTITEL-MIT-ZEITEN.txt
```

Keine anderen Dateien und kein `fertiges-video/`-Unterordner. `UNTERTITEL-YOUTUBE.srt`, `render-report.md`, `quality-scorecard.md`, `postmortem.md` und sonstige technische Outputs liegen ausschließlich unter `.intern/`. Vor dem Render keine Platzhalter-MP4 erzeugen. Alle Zeitcodes aus der finalen Audio-Timeline, niemals schätzen.

**Aktuelle Befehle für neue Videoordner:**

```bash
python tools/prepare_phase3.py youtube-videos/THEMA
python tools/export_subtitles.py youtube-videos/THEMA
cd renderer
npm run render -- ../youtube-videos/THEMA/03_export/VIDEO.mp4
```

Die weiter oben genannten `04_export`-Pfade beschreiben ausschließlich den älteren, unveränderten 008-Projektaufbau. **Nicht** für neue Produktionen verwenden.

## Finale technische QA

```bash
python tools/qa_final.py \
  youtube-videos/THEMA/04_export/fertiges-video/[VIDEO-ID]-YOUTUBE.mp4 \
  youtube-videos/THEMA/01_script/audio/final-voiceover.wav
```

Danach bleiben visueller Sichtcheck, Scorecard und Postmortem.

## Goldene Regel

Bei Unsicherheit oder Inkonsistenz: **FAIL statt raten**.


## NEUE PROJEKTE ab 009 – vereinfachte Ordner (Vorlage)

`01_script/script.txt` + `01_script/audio/`; `02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt` + `bilder-zip/`; `03_export/VIDEO.mp4`, `COVER.png`, `CAPTION-YOUTUBE.txt`, `UNTERTITEL-MIT-ZEITEN.txt`. Alles Technische `.intern/03_pipeline/` und `.intern/05_info/`; das SRT liegt versteckt unter `.intern/UNTERTITEL-YOUTUBE.srt`.

Das YouTube-Cover ist kein `Bild_01` und wird nicht ins MP4 aufgenommen. Der erste Szenenframe `Bild_01.png` ist ein normaler erzählender biologischer Vorgang. Alt-Videos 008 und früher werden nicht rückwirkend geändert.
