# Antigravity-Prompt

Du bist in **Phase 3**. Deine Aufgabe ist ausschließlich der technische Zusammenbau des bereits geplanten Object-Talk-YouTube-Videos.

## Vor dem Start lesen

Vom Repository-Root zuerst:

1. `PROJECT_CONTRACT.md`
2. `PROJECT_STATE.md`
3. `AGENTS.md`
4. `config/video.json`
5. `engine/PHASE-GATES.md`
6. `engine/SYNC-WHISPER.md`
7. `engine/VISUAL-QUALITY-GATE.md`
8. Dateien des aktuellen Videoordners

## Harte Regel

Phase 3 ist **nicht kreativ**.

Du darfst nicht:

- das Script umschreiben
- Szenen neu einteilen
- Bildideen austauschen
- fehlende Bilder erfinden
- die Bildreihenfolge ändern
- Wortzeiten schätzen
- Voiceover beschleunigen oder verlangsamen
- wissenschaftliche Texte oder Labels neu erfinden

Bei einem Fehler: STOP statt raten.

## Eingaben

Im aktuellen Projekt werden erwartet:

```text
01_script/script.txt
01_script/audio/<eine rohe Voice-Datei>
02_bildprompts/bilder-zip/<eine Google-Flow-ZIP>
03_pipeline/scene-map.json
05_info/phase1-scenes.json
```

## Ein Befehl für die komplette Vorbereitung

Vom Repository-Root:

```bash
python -m pip install -r tools/requirements.txt
python tools/prepare_phase3.py youtube-videos/THEMA
```

Falls das kleine Whisper-Modell bei einem Fachbegriff keine strikte Ausrichtung erreicht:

```bash
python tools/prepare_phase3.py youtube-videos/THEMA --model medium
```

Dieser Vorbereitungsschritt muss in genau dieser Reihenfolge erledigen:

1. `validate_phase1.py` – Script und semantische Szenen lückenlos prüfen
2. `prepare_audio.py` – rohe Voice in `final-voiceover.wav` kanonisieren
3. `import_flow_zip.py` – Flow-ZIP sicher nach expliziten Bildnummern importieren
4. `validate_assets.py` – Bildnummern, Auflösung und Format prüfen
5. `transcribe_audio.py` – faster-whisper + Wort-Zeitstempel
6. **gesamtes Audio streng gegen `script.txt` ausrichten**
7. `build_timeline.py` – exakte `speech_section` jeder Szene auf echte Wortzeiten mappen
8. `build_renderer_runtime.py` – feste Remotion-Runtime mit diesen Zeiten vorbereiten
9. `subtitles.srt` nach `04_export/subtitles/` kopieren

Ergebnis der Timing-Stufe:

```text
03_pipeline/timing/
├── whisper-raw.json
├── word-timings.json
├── timeline.json
└── subtitles.srt
```

`timeline.json` ist die verbindliche technische Quelle für alle Bildwechsel.

## Wichtig zu Whisper

Whisper allein entscheidet **nicht** über Szenen.

Phase 1 hat die Szenengrenzen bereits über komplette `speech_section`-Abschnitte festgelegt. Whisper liefert nur die echten Zeiten des finalen Audios.

Wenn erkannter Text und `script.txt` nicht streng zusammenpassen, muss die Pipeline fehlschlagen. Keine Fuzzy-Zuordnung und keine geratenen Sekunden verwenden.

## Bilder

Nach dem sicheren ZIP-Import liegen die technischen Bilder hier:

```text
02_bildprompts/images/
├── Bild_01.png
├── Bild_02.png
├── Bild_03.png
└── ...
```

Die ZIP-Reihenfolge ist bedeutungslos. Nur die explizite Bildnummer zählt.

## Fester Renderer

Verwende den vorhandenen Renderer unter:

```text
renderer/
```

Erfinde pro Video keinen neuen Editor.

Einmalig bzw. nach Dependency-Änderung:

```bash
cd renderer
npm install
```

Preview:

```bash
npm run studio
```

Render:

```bash
npm run render -- ../youtube-videos/THEMA/04_export/fertiges-video/final-video.mp4
```

Der Renderer verwendet:

- 1920×1080
- 30 fps
- das vollständige `final-voiceover.wav`
- die exakte Timeline
- ausschließlich die erlaubten dezenten Bildbewegungen

## Erlaubte Standbild-Bewegungen

- `static`
- `slow-push-in`
- `slow-pull-out`
- `pan-left`
- `pan-right`

Kein hektisches Wackeln, keine aggressiven Zooms und keine Bewegung, die wissenschaftliche Inhalte verfälscht.

## Übergänge

Standard ist ein sauberer harter Schnitt. Keine Effekt-Transition nur um Aktivität vorzutäuschen.

## Beschriftungen

Vorhandene deutsche Beschriftungen:

- nicht verdecken
- nicht abschneiden
- ausreichend lange lesbar halten

Keine neuen biologischen Behauptungen im Schnitt ergänzen.

## Finale QA

Nach Render:

```bash
python tools/qa_final.py \
  youtube-videos/THEMA/04_export/fertiges-video/final-video.mp4 \
  youtube-videos/THEMA/01_script/audio/final-voiceover.wav
```

Danach `04_export/render-report.md` ausfüllen und zusätzlich einen visuellen Sichtcheck machen.

## Fertig nur bei PASS

Ein Video ist erst fertig, wenn:

- mindestens 5:00 Minuten
- 1920×1080 / 30 fps
- Audio vollständig
- alle geplanten Bilder verwendet
- Bildwechsel zur Sprache passen
- keine Szenenlücke oder Überschneidung
- Labels lesbar
- kein grober KI-Fehler sichtbar
- technischer QA-Check PASS
- visueller Sichtcheck PASS

Finale Datei:

```text
04_export/fertiges-video/final-video.mp4
```
