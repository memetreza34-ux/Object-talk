# Antigravity – Phase 3 – 2-Minuten-Pilot / 26 Bilder

Projekt:

`youtube-videos/000-pilot-zucker-im-blut/`

## Zweck

Interner Test der neuen V2-Pipeline mit **hoher visueller Dichte**. Erwartet werden genau 26 finale Bilder. Script, wissenschaftliche Aussagen, Bildreihenfolge und Szenengrenzen dürfen nicht kreativ verändert werden.

Erwartet:
- exaktes Script in `01_script/script.txt`
- genau `Bild_01.png` bis `Bild_26.png`
- `Bild_01` = Master Style Frame
- `05_info/test-mode.json` erlaubt 105–150 Sekunden
- echte Wortzeiten bestimmen die finale Dauer jeder Szene

## Harte Grenzen

Nicht:
- Script umschreiben
- Szenen zusammenlegen
- Szenen teilen
- Bilder austauschen
- Reihenfolge ändern
- fehlende Bilder still ersetzen
- Mascot-/Presenter-Elemente ergänzen
- die hohe Bilddichte durch wenige lange Standbilder wieder reduzieren

## Vorbereitung

Vom Repo-Root:

```bash
python -m pip install -r tools/requirements.txt
python tools/validate_planning_v2.py youtube-videos/000-pilot-zucker-im-blut --phase2
python tools/prepare_phase3.py youtube-videos/000-pilot-zucker-im-blut
```

Bei FAIL stoppen und den konkreten Fehler beheben.

## Remotion

```bash
cd renderer
npm install
npm run studio
```

Nach Sichtprüfung:

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

## Sichtprüfung

Zusätzlich prüfen:
- alle 26 Bilder vorhanden und korrekt nummeriert
- Bilder wechseln mit der echten Sprache, nicht nach pauschalem Zeitraster
- im schnellen Hook keine unnötig langen Holds
- normale Erklärbilder meist ungefähr 4–6 Sekunden, sofern die echten Wortzeiten dazu passen
- keine Mascot-/Presenter-Dominanz
- Labels korrekt
- Anatomie plausibel
- Nachbarbilder unterscheiden sich sichtbar
- Bild_01-Stil bleibt über die Episode erkennbar
- keine schwarzen Frames

Danach `quality-scorecard.md` und `postmortem.md` anhand des echten Renders ausfüllen.
