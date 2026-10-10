# Bild-Timing-Pipeline

Diese Datei ist die für Menschen lesbare Übersicht der geplanten Bildzuordnung.

Die maschinenlesbare Szene-Quelle liegt in:

```text
scene-map.json
```

Die echten Sekundenwerte entstehen erst nach dem finalen Voiceover in:

```text
timing/timeline.json
```

## Grundregel

Phase 1 legt für jede Szene einen **vollständigen wortwörtlichen Sprachabschnitt** (`speech_section`) aus `01_script/script.txt` fest.

Die Abschnitte müssen das gesamte Script:

- vom ersten bis zum letzten gesprochenen Wort
- in richtiger Reihenfolge
- ohne Lücken
- ohne Überlappungen

abdecken.

Nicht Satz für Satz mechanisch wechseln. Entscheidend sind echte **visuelle Sinnwechsel**:

- Ein Satz darf mehrere Bilder bekommen, wenn sich die visuelle Aussage wirklich ändert.
- Mehrere Sätze dürfen ein Bild teilen, wenn sie dieselbe visuelle Aussage erklären.

## Keine geschätzten Sekunden in Phase 1

Phase 1 schreibt **keine finalen Zeitcodes**.

Nach der Voice-Erzeugung:

1. `final-voiceover.wav` wird mit faster-whisper transkribiert.
2. Die komplette ASR-Ausgabe wird streng gegen `script.txt` ausgerichtet.
3. Jedes Scriptwort erhält eine echte Zeit.
4. `scene-map.json` wird exakt auf diese Wörter gemappt.
5. Daraus entsteht `timing/timeline.json`.

## Szenenformat

### Szene 01 / Bild_01

- **Sprachabschnitt:** „[vollständiger exakter Abschnitt aus script.txt]“
- **Startanker:** „[exakter Anfang dieses Abschnitts]“
- **Endanker:** „[exaktes Ende dieses Abschnitts]“
- **Zeigt:** [visuelle Aufgabe]
- **Labels:** [wichtige deutsche Labels oder keine]
- **Bewegung:** `slow-push-in`
- **Funktion:** Cover / Hook

### Szene 02 / Bild_02

- **Sprachabschnitt:** „[...]“
- **Startanker:** „[...]“
- **Endanker:** „[...]“
- **Zeigt:** [...]
- **Labels:** [...]
- **Bewegung:** `pan-left`

[Fortsetzen bis zur letzten Szene.]

## Erlaubte Bewegungen

- `static`
- `slow-push-in`
- `slow-pull-out`
- `pan-left`
- `pan-right`

Bewegung darf das Bild nicht verzerren und keine Beschriftung aus dem Frame schieben.

## Regeln für ChatGPT

Beim Erstellen der finalen Planung:

- `speech_section` ausschließlich 1:1 aus `script.txt`
- jede Szene beginnt exakt beim nächsten noch nicht verwendeten Scriptwort
- jede Szene endet exakt vor Beginn der nächsten
- keine Textlücken
- keine Überlappungen
- `scene-map.json` und `05_info/phase1-scenes.json` müssen dieselben Szenengrenzen besitzen
- jede Szene hat exakt ein `Bild_XX`
- `Bild_01` = Cover-/Hook-Szene
- Bildwechsel nach Bedeutung, nicht nach starrer Satzanzahl
- ein neues biologisches Konzept bekommt rechtzeitig ein neues Bild
- ein Bild darf nicht schon ein späteres Konzept verraten, bevor es im Voiceover eingeführt wird

## Technische Validierung

Vor Phase 2:

```bash
python tools/validate_phase1.py \
  01_script/script.txt \
  05_info/phase1-scenes.json \
  03_pipeline/scene-map.json
```

Nur bei `PHASE-1 PASS` weiterarbeiten.

## Finale Timeline

`timing/timeline.json` enthält später für jede Szene:

- `scene`
- `image`
- `speech_section`
- echte `start`-Sekunde
- echte `end`-Sekunde
- `duration`
- `motion`

Diese Datei wird in Phase 3 automatisch erzeugt und niemals per Hand geschätzt.
