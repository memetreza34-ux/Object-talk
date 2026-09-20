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
    ├── 02_bildprompts/
    │   ├── Google-Flow-Agent-Prompt.md
    │   └── bilder-zip/
    ├── 03_pipeline/
    │   ├── pipeline.md
    │   └── Antigravity-Prompt.md
    ├── 04_export/
    │   ├── YouTube-Caption.md
    │   └── fertiges-video/
    └── 05_info/
        └── Recherche.md
```

## Die 3 Produktionsphasen

### Phase 1 – ChatGPT
ChatGPT erstellt das komplette Produktionspaket:
- geeignetes Thema auswählen und im Themen-Gehirn prüfen
- Recherche und Faktenprüfung
- fertiges mindestens 5-minütiges Skript
- Skript **ohne Regieanweisungen**, damit es 1:1 in eine Voice-KI kopiert werden kann
- vollständigen Google-Flow-Agent-Prompt mit allen benötigten Bildern
- jede Bildszene nummerieren
- **Szene 01 / Bild 01 ist immer die Cover-Szene**
- genaue Bild-Timing-Pipeline erstellen: von welchem gesprochenen Wort bis zu welchem gesprochenen Wort welches Bild gezeigt wird
- Antigravity-Anweisung für den finalen Zusammenbau
- YouTube-Titel, Beschreibung und maximal 5 Hashtags

### Phase 2 – Nutzer + Google Flow
Der Nutzer produziert die Assets:
1. `script.txt` 1:1 in die Voice-KI kopieren.
2. Fertige Audiodatei in `01_script/audio/` legen.
3. `Google-Flow-Agent-Prompt.md` in Google Flow verwenden.
4. Der Flow-Agent erzeugt **jedes Bild einzeln**.
5. Nach jeder Generierung wird das Bild sofort passend umbenannt: `Bild_01`, `Bild_02`, `Bild_03` usw.
6. Alle Bilder werden gesammelt und als ZIP-Datei in `02_bildprompts/bilder-zip/` abgelegt.

### Phase 3 – Antigravity
Antigravity setzt das Video zusammen:
- nutzt die originale Audiodatei unverändert als Zeitbasis
- entpackt/verwendet alle nummerierten Bilder
- folgt exakt `03_pipeline/pipeline.md`
- zeigt jedes Bild genau an der Stelle, an der der zugehörige gesprochene Abschnitt beginnt
- beendet das Bild genau dort, wo der definierte Abschnitt endet
- nutzt dezente Zooms, Schwenks, Bewegungen und Übergänge, ohne Inhalte zu verfälschen
- exportiert das fertige Video nach `04_export/fertiges-video/`

## Wichtig
- Nur lange YouTube-Videos, mindestens 5 Minuten.
- Visuell nur Bilder; keine generierten Videoclips als notwendiger Bestandteil.
- Einheitliche Object-Talk- und Inside-the-Body-Bildwelt.
- Wissenschaftliche Bilder müssen verständlich und korrekt sein.
- Wichtige Strukturen werden auf Deutsch beschriftet.
- Keine unnötigen Beschriftungen.
- Ein Thema darf nicht unnötig wiederholt werden; vorher immer `THEMEN-GEHIRN.md` prüfen.

Der Ordner `_TEMPLATE` dient als Vorlage für jedes neue Video.