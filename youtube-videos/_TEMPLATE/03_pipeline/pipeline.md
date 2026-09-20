# Bild-Timing-Pipeline

Diese Datei beschreibt die **inhaltliche Zuordnung** zwischen Voiceover und Bildern.

Die echten Sekundenwerte werden erst nach der fertigen Audiodatei automatisch mit Whisper erzeugt.

## Grundregel

Jedes Bild beginnt bei einer eindeutigen gesprochenen Wortgruppe aus `01_script/script.txt` und endet beim Übergang zur nächsten Szene.

ChatGPT plant die Wortanker. Whisper liefert später die echten Zeitstempel.

## Dateien

- `pipeline.md` – menschenlesbare Szenenplanung
- `scene-map.json` – maschinenlesbare Wortanker
- `timing/whisper-words.json` – automatisch aus dem finalen Voiceover
- `timing/timeline.json` – endgültige Sekundenwerte für den Renderer
- `timing/subtitles.srt` – automatisch erzeugte Untertitel

## Format

| Szene | Bild | START-Anker | ENDE-Anker | Inhalt / Zweck |
|---|---|---|---|---|
| 01 | Bild_01 | „[eindeutige Wortgruppe]“ | „[eindeutige Wortgruppe]“ | Cover / Hook |
| 02 | Bild_02 | „[...]“ | „[...]“ | [...] |
| 03 | Bild_03 | „[...]“ | „[...]“ | [...] |

## Regeln für ChatGPT

Beim Erstellen der finalen Pipeline:

- START und ENDE müssen **1:1 aus `01_script/script.txt` stammen**
- bevorzugt eindeutige Wortgruppen mit etwa 5–12 Wörtern
- keine häufigen Einzelwörter als Anker
- keine Textlücken in der visuellen Erzählung
- jede Bildszene aus `02_bildprompts/Google-Flow-Agent-Prompt.md` genau einmal einplanen
- Reihenfolge der Bilder niemals verändern
- `Bild_01` startet bei 0 Sekunden und ist Cover-/Hook-Szene
- Wechsel an einer inhaltlich sinnvollen Stelle planen
- normale Bilddauer ungefähr 6–10 Sekunden
- möglichst keine Szene über 12 Sekunden

## Finale Planung

ChatGPT ersetzt diesen Bereich bei jedem Video vollständig.

### Szene 01 / Bild_01
- **START:** „[...]“
- **ENDE:** „[...]“
- **Zeigt:** [...]
- **Bewegung:** [langsamer Push-in / leichter Pan / Pull-out / statisch]

### Szene 02 / Bild_02
- **START:** „[...]“
- **ENDE:** „[...]“
- **Zeigt:** [...]
- **Bewegung:** [...]

[Fortsetzen bis zur letzten Szene.]

## Nach dem Voiceover

Antigravity führt aus:

```bash
python tools/transcribe_audio.py <AUDIO> <VIDEOORDNER>/03_pipeline/timing
python tools/build_timeline.py \
  <VIDEOORDNER>/03_pipeline/scene-map.json \
  <VIDEOORDNER>/03_pipeline/timing/whisper-words.json \
  <VIDEOORDNER>/03_pipeline/timing/timeline.json
```

Danach ist `timeline.json` die verbindliche technische Zeitbasis.

## Abschlussprüfung

Vor Freigabe prüfen:

1. Deckt die Planung das Skript vom Anfang bis zum Ende ab?
2. Existiert jede Bildnummer genau einmal?
3. Stimmen Bildnummern und Szenennummern exakt überein?
4. Ist jeder Bildwechsel inhaltlich sinnvoll?
5. Sind alle START-/ENDE-Anker exakt im Skript vorhanden?
6. Wurde nach dem Voiceover `timeline.json` erfolgreich erzeugt?
7. Gibt es keine fehlgeschlagenen oder unsicheren Anker-Matches?
