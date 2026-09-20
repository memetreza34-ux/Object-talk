# YouTube-Videos

Dieser Ordner enthält **alle langen YouTube-Videos** des Kanals.

## Grundregel

Jedes Video bekommt **einen eigenen Themenordner** nach diesem Schema:

```text
youtube-videos/
└── THEMA-DES-VIDEOS/
    ├── 01_script/
    │   ├── script.txt
    │   └── audio/
    │       └── voiceover.mp3 oder voiceover.wav
    │
    ├── 02_bildprompts/
    │   ├── Google-Flow-Agent-Prompt.md
    │   └── bilder-zip/
    │       └── bilder.zip
    │
    ├── 03_pipeline/
    │   ├── pipeline.md
    │   ├── scene-map.json
    │   ├── Antigravity-Prompt.md
    │   └── timing/
    │       ├── whisper-words.json
    │       ├── timeline.json
    │       └── subtitles.srt
    │
    ├── 04_export/
    │   ├── YouTube-Caption.md
    │   ├── fertiges-video/
    │   │   └── final-video.mp4
    │   └── subtitles/
    │       └── subtitles.srt
    │
    └── 05_info/
        └── Recherche.md
```

## Die 3 Produktionsphasen

### Phase 1 – ChatGPT

ChatGPT erstellt das komplette Produktionspaket:

- geeignetes Thema auswählen und im Themen-Gehirn prüfen
- Recherche und Faktenprüfung
- fertiges mindestens 5-minütiges Skript
- `script.txt` ohne Regieanweisungen, damit es 1:1 in eine Voice-KI kopiert werden kann
- vollständigen Google-Flow-Agent-Prompt mit allen benötigten Bildern
- jede Bildszene nummerieren
- **Szene 01 / Bild_01 ist immer die Cover-/Hook-Szene**
- `pipeline.md` mit exakten gesprochenen Wortgruppen pro Szene
- `scene-map.json` mit denselben Wortankern für die automatische Synchronisierung
- Antigravity-Anweisung für den finalen Zusammenbau
- YouTube-Titel, Beschreibung und maximal 5 Hashtags

### Phase 2 – Nutzer + Voice-KI + Google Flow

Der Nutzer produziert die Assets:

1. `script.txt` 1:1 in die Voice-KI kopieren.
2. Fertige Audiodatei in `01_script/audio/` legen.
3. `Google-Flow-Agent-Prompt.md` in Google Flow verwenden.
4. Der Flow-Agent erzeugt **jedes Bild einzeln**.
5. Nach jeder Generierung wird das Bild sofort passend umbenannt: `Bild_01`, `Bild_02`, `Bild_03` usw.
6. Alle Bilder werden gesammelt und als ZIP-Datei in `02_bildprompts/bilder-zip/` abgelegt.

### Phase 3 – Antigravity + Whisper + Renderer

Antigravity automatisiert den Zusammenbau:

1. Voiceover und Bilder prüfen.
2. Bilder-ZIP entpacken.
3. `tools/transcribe_audio.py` ausführen.
4. `faster-whisper` erzeugt exakte **Wort-Zeitstempel** des finalen Voiceovers.
5. `tools/build_timeline.py` verbindet diese Zeiten mit `scene-map.json`.
6. Es entsteht `03_pipeline/timing/timeline.json` mit echten Start-/Endzeiten jeder Szene.
7. Erst danach wird das Video gerendert.
8. Dezente Zooms, Push-ins, Schwenks und saubere Übergänge auf die Standbilder anwenden.
9. Finales Video nach `04_export/fertiges-video/final-video.mp4` exportieren.
10. Whisper-Untertitel nach `04_export/subtitles/subtitles.srt` kopieren.

## Warum Whisper?

Eine Voice-KI spricht nie garantiert mit exakt derselben Geschwindigkeit. Deshalb werden die Bildwechsel **nicht nach geschätzten Sekunden** gesetzt.

ChatGPT definiert in Phase 1 die richtigen Textstellen. Nach dem finalen Audio ermittelt Whisper die echten Zeiten dieser Wörter. So erscheinen die Bilder nicht zu früh oder zu spät.

Details: `../engine/SYNC-WHISPER.md`

## Globale Produktionsregeln

Siehe:

- `../engine/PRODUKTIONSREGELN.md`
- `../engine/SYNC-WHISPER.md`
- `../engine/VISUAL-QUALITY-GATE.md`

## Wichtig

- Nur lange YouTube-Videos, mindestens 5 Minuten.
- Visuell ausschließlich Standbilder als notwendige Assets.
- Einheitliche Object-Talk- und Inside-the-Body-Bildwelt.
- Wissenschaftliche Bilder müssen verständlich und korrekt sein.
- Wichtige Strukturen werden auf Deutsch beschriftet.
- Keine unnötigen Beschriftungen.
- Ein Thema darf nicht unnötig wiederholt werden; vorher immer `THEMEN-GEHIRN.md` prüfen.
- Technische Zeitcodes werden erst nach dem finalen Voiceover erzeugt.

Der Ordner `_TEMPLATE` dient als Vorlage für jedes neue Video.