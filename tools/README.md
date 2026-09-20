# Tools

Diese Hilfstools werden in Phase 3 von Antigravity verwendet.

## Benötigt

### Python

```bash
python -m pip install -r tools/requirements.txt
```

### FFmpeg

`ffmpeg` und `ffprobe` müssen im System verfügbar sein. Sie dienen für technische Audio-/Video-Prüfung und den finalen Export bzw. als Hilfstool für den Renderer.

Prüfen:

```bash
ffmpeg -version
ffprobe -version
```

## 1. Voiceover transkribieren

```bash
python tools/transcribe_audio.py \
  youtube-videos/THEMA/01_script/audio/voiceover.mp3 \
  youtube-videos/THEMA/03_pipeline/timing
```

Erzeugt:

- `whisper-words.json`
- `subtitles.srt`

Standardmodell: `small`.

Falls ein sauberes deutsches Voiceover nicht zuverlässig erkannt wird:

```bash
python tools/transcribe_audio.py AUDIO OUTPUT --model medium
```

## 2. Szenen-Timeline bauen

```bash
python tools/build_timeline.py \
  youtube-videos/THEMA/03_pipeline/scene-map.json \
  youtube-videos/THEMA/03_pipeline/timing/whisper-words.json \
  youtube-videos/THEMA/03_pipeline/timing/timeline.json
```

`timeline.json` ist danach die verbindliche Zeitbasis für Antigravity/Remotion.

## Grundsatz

Bei fehlenden oder unsicher gefundenen Wortankern muss die Pipeline stoppen. Sie darf niemals automatisch erfundene Zeitpunkte einsetzen.