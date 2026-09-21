# ANTIGRAVITY – PILOT 001 „SAUERSTOFF VON DER LUNGE BIS ZUR ZELLE“

Arbeite ausschließlich technisch nach dem Repository.

Projekt:

```text
youtube-videos/001-pilot-sauerstoff-im-blut/
```

## Ziel

- interner ca. 2–2,5-Minuten-Test
- 28 Bilder
- hohe visuelle Dichte
- Vollbild-3D-Erklärbilder bleiben dominant
- selektive Remotion-Überschriften/Keywords aus `03_pipeline/overlay-plan.json`
- keine Anime-/Comic-Effekte
- keine dauerhaften Untertitelblöcke
- keine kreative Neuzuordnung von Szenen

## Vorbereitung

Vom Repo-Root:

```bash
python -m pip install -r tools/requirements.txt
python tools/validate_planning_v2.py youtube-videos/001-pilot-sauerstoff-im-blut
python tools/prepare_phase3.py youtube-videos/001-pilot-sauerstoff-im-blut
```

`prepare_phase3.py` muss:

1. `scene-map.json` deterministisch aus `phase1-scenes.json` erzeugen
2. Script/Scene-Map validieren
3. Voice kanonisieren
4. ZIP `Bild_01.png` bis `Bild_28.png` importieren
5. Bilder technisch validieren
6. Whisper-Worttimings erzeugen
7. Script strikt gegen Audio ausrichten
8. exakte Timeline bauen
9. Renderer-Runtime inklusive `overlay-plan.json` vorbereiten

## Overlay-Regel

`03_pipeline/overlay-plan.json` ist autoritativ.

- nur dort definierte Overlays
- Text exakt übernehmen
- deutsche Rechtschreibung nicht verändern
- Overlays erscheinen erst passend zum gesprochenen Begriff
- keine zusätzlichen Sätze oder Captions erfinden
- Vollbild bleibt Hauptdarsteller

## Render

```bash
cd renderer
npm install
npm run studio
npm run render -- ../youtube-videos/001-pilot-sauerstoff-im-blut/04_export/fertiges-video/final-video.mp4
```

## QA

Vom Repo-Root:

```bash
python tools/qa_final.py \
  youtube-videos/001-pilot-sauerstoff-im-blut/04_export/fertiges-video/final-video.mp4 \
  youtube-videos/001-pilot-sauerstoff-im-blut/01_script/audio/final-voiceover.wav \
  --min-seconds 115
```

Danach visuellen QA nach `engine/VISUAL-QUALITY-GATE.md` durchführen.

Besonders prüfen:

- O₂ bleibt visuell über alle Szenen identisch
- CO₂ bleibt visuell identisch und klar von O₂ unterscheidbar
- rote Blutkörperchen und Hämoglobin bleiben konsistent
- keine englischen oder zufälligen Texte in Flow-Bildern
- Overlay-Texte liegen nicht über zentraler Anatomie
- kein Bild steht unnötig lange nur mit Zoom
- letzte Szene endet exakt mit dem Voice-over

Bei Konflikt: FAIL statt raten.
