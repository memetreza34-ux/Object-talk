# Antigravity – Phase 3 – 2-Minuten-Pilot

Projekt:

`youtube-videos/000-pilot-zucker-im-blut/`

## Zweck

Dies ist ein **interner ca. 2-Minuten-Test** der neuen V2-Pipeline. Keine inhaltlichen oder kreativen Änderungen vornehmen.

Erwartet:
- exaktes Script in `01_script/script.txt`
- genau 15 finale Bilder `Bild_01.png` bis `Bild_15.png`
- Bild_01 ist der Master Style Frame
- `05_info/test-mode.json` erlaubt für diesen Pilot 105–150 Sekunden statt der normalen 300-Sekunden-Longform-Grenze

## Harte Grenzen

Nicht:
- Script umschreiben
- Szenen zusammenlegen/teilen
- neue Bilder erfinden
- Bildreihenfolge verändern
- wissenschaftliche Aussagen verstärken
- fehlende Bilder still ersetzen
- Mascot-/Presenter-Elemente ergänzen

## Vorbereitung

Vom Repo-Root:

```bash
python -m pip install -r tools/requirements.txt
python tools/validate_planning_v2.py youtube-videos/000-pilot-zucker-im-blut --phase2
python tools/prepare_phase3.py youtube-videos/000-pilot-zucker-im-blut
```

Wenn einer dieser Schritte FAIL meldet: stoppen und den konkreten Fehler beheben.

## Remotion

```bash
cd renderer
npm install
npm run studio
```

Nach Sichtprüfung rendern:

```bash
npm run render -- ../youtube-videos/000-pilot-zucker-im-blut/04_export/fertiges-video/final-video.mp4
```

## Test-QA

Vom Repo-Root:

```bash
python tools/qa_final.py \
  youtube-videos/000-pilot-zucker-im-blut/04_export/fertiges-video/final-video.mp4 \
  youtube-videos/000-pilot-zucker-im-blut/01_script/audio/final-voiceover.wav \
  --min-seconds 105
```

Dieser Override gilt nur für diesen Testpilot. Normale Kanalvideos bleiben bei mindestens 300 Sekunden.

## Sichtprüfung

Zusätzlich prüfen:
- richtige Erklärbilder statt Presenter/Mascot
- Bildwechsel passen zur echten Sprache
- kein Bild unnötig lange statisch
- Labels korrekt
- Anatomie plausibel
- Bild_01-Stil bleibt erkennbar
- keine schwarzen Frames

Danach Scorecard und Postmortem auf Basis des echten Renders ausfüllen.
