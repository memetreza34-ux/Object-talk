# YouTube-Videos

Dieser Ordner enthält alle langen Object-Talk-YouTube-Videos.

## Neues Projekt

```bash
python tools/create_video.py "THEMA"
```

Dadurch wird `_TEMPLATE` in einen neuen Themenordner kopiert.

# Wichtige Nutzer-Regel

Alles, was der Nutzer **selbst öffnen und in ein anderes Tool kopieren** soll, wird zusätzlich als normale `.txt`-Datei bereitgestellt.

Der Nutzer soll dafür nicht auf `.md`, `.json` oder interne Agentendateien angewiesen sein.

Pflicht pro Video:

```text
01_script/VOICEOVER-ZUM-KOPIEREN.txt
02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt
03_pipeline/ANTIGRAVITY-PROMPT-ZUM-KOPIEREN.txt
04_export/YOUTUBE-TITEL-BESCHREIBUNG-ZUM-KOPIEREN.txt
```

Details: `../engine/USER-FILES-STANDARD.md`

## Feste Projektstruktur

```text
youtube-videos/THEMA/
├── 01_script/
│   ├── script.txt                            # technische Originalquelle
│   ├── VOICEOVER-ZUM-KOPIEREN.txt           # Nutzerdatei für die Voice-KI
│   └── audio/
│       ├── <rohes Voiceover aus der Voice-KI>
│       └── final-voiceover.wav              # Phase 3 erzeugt
│
├── 02_bildprompts/
│   ├── Google-Flow-Agent-Prompt.md           # interne/kanonische Promptdatei
│   ├── GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt  # Nutzerdatei für Google Flow
│   ├── bilder-zip/
│   │   └── bilder.zip                       # Nutzer legt Flow-ZIP hier ab
│   └── images/
│       ├── Bild_01.png                      # Phase 3 importiert kanonisch
│       ├── Bild_02.png
│       └── ...
│
├── 03_pipeline/
│   ├── pipeline.md
│   ├── scene-map.json
│   ├── Antigravity-Prompt.md                 # interne/kanonische Agentdatei
│   ├── ANTIGRAVITY-PROMPT-ZUM-KOPIEREN.txt  # Nutzerdatei für Antigravity
│   └── timing/
│       ├── whisper-raw.json
│       ├── word-timings.json
│       ├── timeline.json
│       └── subtitles.srt
│
├── 04_export/
│   ├── YouTube-Caption.md                    # interne/kanonische Metadaten
│   ├── YOUTUBE-TITEL-BESCHREIBUNG-ZUM-KOPIEREN.txt
│   ├── render-report.md
│   ├── fertiges-video/
│   │   └── final-video.mp4
│   └── subtitles/
│       └── subtitles.srt
│
└── 05_info/
    ├── Recherche.md
    ├── claim-matrix.md
    └── phase1-scenes.json
```

# Phase 1 – ChatGPT / Creative Director

Vor jeder Produktion:

1. `THEMEN-GEHIRN.md` prüfen.
2. Thema recherchieren.
3. Kernbehauptungen in `claim-matrix.md` prüfen.
4. finales gesprochenes `script.txt` schreiben.
5. `VOICEOVER-ZUM-KOPIEREN.txt` mit exakt demselben Sprechertext erstellen.
6. semantische Bildszenen in `phase1-scenes.json` festlegen.
7. gesamte Sprache lückenlos auf die Szenen verteilen.
8. `scene-map.json` mit denselben `speech_section`-Grenzen erstellen.
9. vollständigen `Google-Flow-Agent-Prompt.md` mit genau einem Bild pro Szene erstellen.
10. denselben vollständigen Inhalt zusätzlich als `GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt` bereitstellen.
11. `Bild_01` immer als Cover-/Hook-Szene planen.
12. vollständigen `Antigravity-Prompt.md` vorbereiten.
13. denselben Nutzerauftrag zusätzlich als `ANTIGRAVITY-PROMPT-ZUM-KOPIEREN.txt` bereitstellen.
14. YouTube-Titel, Beschreibung und maximal 5 Hashtags vorbereiten.
15. diese zusätzlich als `YOUTUBE-TITEL-BESCHREIBUNG-ZUM-KOPIEREN.txt` bereitstellen.

Wichtig:

- `script.txt` bleibt die technische Quelle für Validator, Whisper und Timeline.
- Alle Nutzer-`.txt`-Dateien müssen inhaltlich mit ihren kanonischen Dateien übereinstimmen.
- Phase 1 ist erst vollständig, wenn alle vier Nutzer-`.txt`-Dateien vorhanden sind.

Vor Phase 2:

```bash
python tools/validate_phase1.py \
  youtube-videos/THEMA/01_script/script.txt \
  youtube-videos/THEMA/05_info/phase1-scenes.json \
  youtube-videos/THEMA/03_pipeline/scene-map.json
```

Nur bei `PHASE-1 PASS` weiter.

# Phase 2 – Nutzer + Voice-KI + Google Flow

Der Nutzer:

1. öffnet `01_script/VOICEOVER-ZUM-KOPIEREN.txt` und kopiert den Inhalt 1:1 in die Voice-KI
2. legt genau eine rohe Voice-Datei unter `01_script/audio/` ab
3. öffnet `02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt` und kopiert den vollständigen Inhalt in Google Flow
4. Flow erzeugt jedes Bild streng einzeln
5. Szene 01 = `Bild_01` = Cover/Hook
6. nach jedem Bild Einzel-QA
7. finale Bilder als eine ZIP unter `02_bildprompts/bilder-zip/` ablegen

Die kreative Szeneinteilung darf in Phase 2 nicht verändert werden.

# Phase 3 – Antigravity + Tools + Remotion

Wenn der Nutzer Antigravity manuell beauftragt, verwendet er:

```text
03_pipeline/ANTIGRAVITY-PROMPT-ZUM-KOPIEREN.txt
```

Empfohlener Vorbereitungsschritt vom Repository-Root:

```bash
python -m pip install -r tools/requirements.txt
python tools/prepare_phase3.py youtube-videos/THEMA
```

Dieser Befehl:

1. validiert Phase 1
2. erzeugt kanonisches `final-voiceover.wav`
3. importiert die Flow-ZIP sicher nach Bildnummern
4. validiert die Bilder
5. transkribiert das finale Audio mit faster-whisper
6. richtet die komplette Transkription streng gegen `script.txt` aus
7. erzeugt echte Wort-Zeitstempel
8. mappt komplette `speech_section`-Abschnitte auf die echten Zeiten
9. erzeugt `timeline.json`
10. baut die feste Remotion-Runtime
11. kopiert die Untertitel in den Exportordner

## Render

```bash
cd renderer
npm install
npm run studio
npm run render -- ../youtube-videos/THEMA/04_export/fertiges-video/final-video.mp4
```

## Finale QA

```bash
python tools/qa_final.py \
  youtube-videos/THEMA/04_export/fertiges-video/final-video.mp4 \
  youtube-videos/THEMA/01_script/audio/final-voiceover.wav
```

Danach `04_export/render-report.md` ausfüllen und den finalen Sichtcheck durchführen.

Für YouTube verwendet der Nutzer anschließend:

```text
04_export/YOUTUBE-TITEL-BESCHREIBUNG-ZUM-KOPIEREN.txt
```

# Warum Whisper?

ChatGPT entscheidet in Phase 1 **welche Sprachpassage zu welchem Bild gehört**.

Whisper entscheidet erst nach dem echten Voiceover **wann genau diese Wörter gesprochen werden**.

Dadurch muss kein Agent Sekunden schätzen. Die gesamte Script↔Audio-Ausrichtung ist fail-closed: bei nicht erklärbarer Abweichung stoppt die Pipeline.

# Globale Regeln

Siehe:

- `../PROJECT_CONTRACT.md`
- `../PROJECT_STATE.md`
- `../AGENTS.md`
- `../engine/USER-FILES-STANDARD.md`
- `../engine/PHASE-GATES.md`
- `../engine/PRODUKTIONSREGELN.md`
- `../engine/AUDIO-REGELN.md`
- `../engine/SYNC-WHISPER.md`
- `../engine/STYLE-REFERENCE-SYSTEM.md`
- `../engine/FACT-CHECK-STANDARD.md`
- `../engine/VISUAL-QUALITY-GATE.md`

## Harte Kanalregeln

- nur lange YouTube-Erklärvideos
- mindestens 5:00 Minuten
- 16:9 / 1920×1080 / 30 fps
- narrative Visuals nur Standbilder
- viraler Object-Talk + verständliche Inside-the-Body-Welt
- wichtige biologische Strukturen auf Deutsch beschriften
- keine erfundenen Gesundheitswirkungen
- keine Themen unnötig wiederholen
- keine geratenen Audio-/Bild-Zeitpunkte
