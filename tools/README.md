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

## Phase 1 validieren

Nach finalem Script und Szenenplan:

```bash
python tools/validate_phase1.py \
  youtube-videos/THEMA/01_script/script.txt \
  youtube-videos/THEMA/05_info/phase1-scenes.json \
  youtube-videos/THEMA/03_pipeline/scene-map.json
```

Der Validator verlangt:

- lückenlose Szenennummerierung
- vollständige Sprachabdeckung
- keine Lücke oder Überlappung
- `phase1-scenes.json` und `scene-map.json` identisch in ihren kreativen Szenengrenzen
- korrekte `Bild_XX`-Zuordnung

## Empfohlen: komplette Phase-3-Vorbereitung mit einem Befehl

Sobald rohe Voice-Datei und Flow-ZIP vorhanden sind:

```bash
python tools/prepare_phase3.py youtube-videos/THEMA
```

Dieser Befehl führt automatisch die folgenden Schritte in fester Reihenfolge aus.

### 1. Audio kanonisieren

```bash
python tools/prepare_audio.py RAW_AUDIO FINAL_WAV
```

Erzeugt `final-voiceover.wav` mit 48 kHz, 1.0× Geschwindigkeit und unserem kontrollierten Lautheitsstandard. Interne Sprechpausen werden nicht künstlich komprimiert.

### 2. Flow-ZIP sicher importieren

```bash
python tools/import_flow_zip.py SCENE_MAP BILDER_ZIP OUTPUT_IMAGES_DIR
```

Wichtig:

- keine Zuordnung nach ZIP-Reihenfolge
- nur explizite `Bild_XX`-/Szenennummer zählt
- Duplikat oder fehlende Nummer = FAIL
- Ausgabe wird kanonisch `Bild_01.png`, `Bild_02.png`, ...

### 3. Bilder technisch validieren

```bash
python tools/validate_assets.py SCENE_MAP OUTPUT_IMAGES_DIR
```

Prüft unter anderem:

- lückenlose Bildfolge
- ungefähr 16:9
- Mindestauflösung
- technische Lesbarkeit

### 4. Whisper + strikte Script-Ausrichtung

```bash
python tools/transcribe_audio.py \
  FINAL_WAV \
  script.txt \
  03_pipeline/timing
```

Erzeugt:

```text
whisper-raw.json
word-timings.json
subtitles.srt
```

`word-timings.json` besteht aus den **exakten Script-Wörtern** mit den echten Audiozeiten. Wenn Script und Audio nicht vollständig ausgerichtet werden können, wird abgebrochen.

Bei Bedarf:

```bash
python tools/transcribe_audio.py FINAL_WAV script.txt TIMING_DIR --model medium
```

### 5. Timeline bauen

```bash
python tools/build_timeline.py \
  03_pipeline/scene-map.json \
  03_pipeline/timing/word-timings.json \
  03_pipeline/timing/timeline.json
```

Jede vollständige `speech_section` wird sequenziell auf echte Wortzeiten abgebildet. Keine Fuzzy-Suche, keine geschätzten Sekunden.

### 6. Feste Remotion-Runtime bauen

```bash
python tools/build_renderer_runtime.py \
  03_pipeline/timing/timeline.json \
  02_bildprompts/images \
  01_script/audio/final-voiceover.wav
```

Danach:

```bash
cd renderer
npm run studio
npm run render -- ../youtube-videos/THEMA/04_export/fertiges-video/final-video.mp4
```

## Finale technische QA

```bash
python tools/qa_final.py \
  youtube-videos/THEMA/04_export/fertiges-video/final-video.mp4 \
  youtube-videos/THEMA/01_script/audio/final-voiceover.wav
```

Prüft:

- mindestens 5:00 Minuten
- 1920×1080
- ungefähr 30 fps
- Audio vorhanden
- Video endet nicht vor dem Voiceover

Danach bleibt noch der visuelle menschliche/agentische Sichtcheck nach `engine/VISUAL-QUALITY-GATE.md`.

## Goldene Regel

Bei Unsicherheit oder Inkonsistenz: **FAIL statt raten**.
