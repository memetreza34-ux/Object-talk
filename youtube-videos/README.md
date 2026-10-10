# Object-Talk – YouTube-Videos

## Ab Video 009: nur drei sichtbare Ordner

```text
youtube-videos/VIDEOORDNER/
├── 01_script/
│   ├── script.txt                        ← gesprochener Fließtext
│   └── audio/                            ← Audio hier ablegen
├── 02_bildprompts/
│   ├── GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt
│   └── bilder-zip/                       ← fertige Bilder-ZIP
└── 03_export/
    ├── VIDEO.mp4                         ← entsteht nach Render
    ├── COVER.png                         ← separates YouTube-Cover
    ├── CAPTION-YOUTUBE.txt               ← Titel und Beschreibung
    └── UNTERTITEL-MIT-ZEITEN.txt          ← echtes Audio-Timing
```

Die Pipeline, Recherche, QA und weitere Dateien liegen unter `.intern/` und sind keine sichtbaren Nutzer-Arbeitsdateien. Alte Videos bis 008 behalten ihren historischen Aufbau. Das ausgewählte Cover gehört NIE als Bild_01 in die Videotimeline: Bild_01 ist die erste normale Videoszene.

## Pflicht-Antwort unmittelbar nach fertiger Phase 1

Nach erfolgreicher Überprüfung: **immer sofort zwei direkt anklickbare Links in der Chat-Antwort, gut sichtbar für Smartphone/Tablet.**

**[Google-Flow-Prompt öffnen](https://github.com/memetreza34-ux/Object-talk/blob/main/youtube-videos/009-longform-schlaf/02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt)**

**[Voice-over-Skript öffnen](https://github.com/memetreza34-ux/Object-talk/blob/main/youtube-videos/009-longform-schlaf/01_script/script.txt)**

Die oben stehenden URLs sind nur ein **funktionierendes Beispiel für Video 009**. Bei JEDEM neuen Video die zwei echten Pfade des gerade fertigen Videoordners einsetzen; niemals blind das Video-009-Beispiel wiederholen. Vor Ausgabe sicherstellen, dass beide fertigen Dateien im Repo existieren. Die Links öffnen direkt GitHub-Dateiansichten zum Kopieren, nicht automatisch die Google-Flow-Anwendung.

Auch `python tools/validate_planning_v2.py youtube-videos/VIDEOORDNER` gibt nach erfolgreicher Phase-1-Prüfung diese zwei aktuellen Links aus. Ein allgemeiner Repo-Link oder ein Pfad ohne Anklickbarkeit genügt NICHT.

## Ablauf

1. Videoordner mit `python tools/create_video.py "THEMA"` vorbereiten.
2. Recherche + vollständiges natürliches `script.txt` und EINEN ausgefüllten Flow-Prompt erstellen.
3. Technische Planung in `.intern/` erstellen und Phase 1 validieren.
4. Dem Nutzer **zwei Direktlinks** zum Skript und Flow-Prompt senden. Er kann auf Tablet oder Computer anfangen.
5. Flow generiert drei Cover; Nutzer wählt, dann normales `Bild_01`–`Bild_05`, danach Fünfergruppen. Separates Cover ist kein Videoszenenbild.
6. Nutzer legt Audio unter `01_script/audio/`, Bilder-ZIP unter `02_bildprompts/bilder-zip/` ab.
7. Pipeline erzeugt MP4, separates Cover, individuelle YouTube-Caption und exakte Zeit-Untertitel. Keine geratenen Zeitstempel.

Produktionsstandard: `../engine/FLOW-COVER-FIRST-WORKFLOW.md`.
