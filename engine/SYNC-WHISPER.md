# Audio-/Bild-Synchronisierung mit Whisper

## Grundidee

Bildwechsel werden niemals anhand geschätzter Sprechgeschwindigkeit gesetzt.

Die kreative Szenenaufteilung entsteht **vorher** in Phase 1. Jede Szene besitzt einen vollständigen, wortwörtlichen `speech_section` aus `script.txt`.

Nach der Voice-Erzeugung liefert `faster-whisper` nur die echten Wortzeiten des finalen Audios.

## Warum zwei Schritte nötig sind

ASR kann einzelne Wörter anders segmentieren als das Script. Deshalb wird nicht direkt auf ungeprüfte Whisper-Phrasen vertraut.

Die Pipeline arbeitet so:

```text
script.txt
+ final-voiceover.wav
↓
faster-whisper Rohtranskription mit Wortzeiten
↓
strikte Script↔ASR-Ausrichtung
↓
word-timings.json mit exakt den Script-Wörtern
↓
scene-map.json mit vollständigen speech_section-Abschnitten
↓
exakte sequenzielle Zuordnung
↓
timeline.json
```

## Schritt 1 – kanonisches Audio

Whisper läuft ausschließlich auf:

```text
01_script/audio/final-voiceover.wav
```

Diese Datei wird mit `tools/prepare_audio.py` aus der rohen Voice-KI-Datei erzeugt.

Keine spätere Geschwindigkeitsänderung nach Whisper.

## Schritt 2 – Transkription + strikte Ausrichtung

```bash
python tools/transcribe_audio.py \
  youtube-videos/THEMA/01_script/audio/final-voiceover.wav \
  youtube-videos/THEMA/01_script/script.txt \
  youtube-videos/THEMA/03_pipeline/timing
```

Erzeugt:

```text
whisper-raw.json
word-timings.json
subtitles.srt
```

`whisper-raw.json` ist die echte ASR-Ausgabe.

`word-timings.json` enthält dagegen die **exakten Wörter aus `script.txt`**, nachdem sie streng mit dem erkannten Audio ausgerichtet wurden.

Erlaubt sind nur technisch eindeutig normalisierbare Gruppierungen, z. B. wenn Whisper ein zusammengesetztes Wort anders segmentiert. Inhaltliche Abweichungen führen zu FAIL.

## Kein Fuzzy-Fallback

Verboten:

- einen ähnlich klingenden Abschnitt irgendwo im Audio auswählen
- bei nicht gefundenem Text einen ungefähren Zeitpunkt schätzen
- Szene anhand der Gesamttextlänge proportional verteilen
- still über ein ausgelassenes oder zusätzlich gesprochenes Wort hinweggehen

Wenn Script und Audio nicht vollständig zusammenpassen:

1. prüfen, ob wirklich die finale Voice-Datei verwendet wird
2. prüfen, ob `script.txt` exakt dem gesprochenen Text entspricht
3. bei korrektem Text mit besserem Whisper-Modell erneut versuchen, z. B. `--model medium`
4. wenn es weiterhin scheitert: Stelle manuell prüfen und Ursache beheben

## Schritt 3 – Szenen auf echte Wortzeiten mappen

```bash
python tools/build_timeline.py \
  youtube-videos/THEMA/03_pipeline/scene-map.json \
  youtube-videos/THEMA/03_pipeline/timing/word-timings.json \
  youtube-videos/THEMA/03_pipeline/timing/timeline.json
```

Jede Szene in `scene-map.json` enthält:

- `scene`
- `image`
- `speech_section`
- `start_anchor`
- `end_anchor`
- `visual_task`
- `motion`

`build_timeline.py` geht **sequenziell** durch das gesamte Script. Jede `speech_section` muss exakt am nächsten noch nicht verwendeten Scriptwort beginnen.

Dadurch entstehen automatisch:

- keine Lücken
- keine Überlappungen
- keine Mehrdeutigkeiten bei wiederholten Wörtern
- kein falscher Treffer weiter hinten im Audio

## Sichtbare Szenenzeiten

Szene 01 startet bei `0.0` Sekunden, damit `Bild_01` sofort sichtbar ist.

Bei allen weiteren Szenen beginnt das neue Bild beim ersten gesprochenen Wort der zugehörigen `speech_section`.

Die vorige Szene bleibt während einer natürlichen Sprechpause sichtbar, bis das nächste gesprochene Segment beginnt.

Die letzte Szene bleibt bis zum Ende des finalen Audios sichtbar.

## Toolwahl

Standard ist `faster-whisper` mit `word_timestamps=True`. Die Library unterstützt Wort-Zeitstempel direkt. Das ist für diese Pipeline entscheidend.

Standardmodell: `small`.

Bei schwierigen Fachbegriffen kann `medium` verwendet werden.

## Goldene Regel

**Phase 1 entscheidet WAS zu welcher Sprachpassage gehört. Whisper entscheidet nur WANN diese bereits festgelegte Sprachpassage im echten Audio stattfindet.**
