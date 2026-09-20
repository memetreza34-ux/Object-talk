# Audio-/Bild-Synchronisierung mit Whisper

## Warum Whisper gebraucht wird

Die Bildwechsel dürfen nicht anhand einer geschätzten Sprechgeschwindigkeit gesetzt werden. Nach der Voice-KI kann derselbe Text schneller oder langsamer gesprochen werden.

Deshalb wird die **fertige Audiodatei** nach ihrer Erstellung automatisch transkribiert. Wir verwenden dafür vorzugsweise `faster-whisper` mit Wort-Zeitstempeln.

## Ziel

Aus:

- `script.txt`
- fertigem Voiceover
- `scene-map.json`
- `Bild_01`, `Bild_02`, ...

entsteht eine exakte `timeline.json` mit Start- und Endzeiten für jedes Bild.

Beispiel:

```json
{
  "scene": 7,
  "image": "Bild_07.png",
  "start": 52.84,
  "end": 60.31,
  "start_anchor": "Jetzt gelangen die Nährstoffe ins Blut",
  "end_anchor": "im ganzen Körper verteilt"
}
```

## Ablauf in Phase 3

1. Antigravity findet die fertige Voiceover-Datei in `01_script/audio/`.
2. `tools/transcribe_audio.py` wird ausgeführt.
3. Whisper erzeugt Wort-Zeitstempel und speichert sie in `03_pipeline/timing/whisper-words.json`.
4. ChatGPT hat bereits in `scene-map.json` für jede Szene eindeutige Textanker festgelegt.
5. `tools/build_timeline.py` gleicht diese Textanker mit den Whisper-Wörtern ab.
6. Daraus wird `03_pipeline/timing/timeline.json` erzeugt.
7. Antigravity/Renderer benutzt ausschließlich diese echten Zeitwerte für die Bildwechsel.
8. Optional wird zusätzlich `subtitles.srt` für YouTube erzeugt.

## Scene-Map-Regel

Jede Szene erhält:

- `scene`
- `image`
- `start_anchor`
- `end_anchor`
- kurze inhaltliche Beschreibung

Die Anker müssen **wortwörtlich aus `script.txt` stammen**.

Sie sollen:

- eindeutig sein
- normalerweise 5–12 Wörter enthalten
- nicht mehrfach im Skript vorkommen
- keine umformulierten Varianten sein

## Wichtig

Die Textanker sind die semantische Planung von ChatGPT. Die echten Sekundenwerte entstehen erst **nach dem finalen Voiceover**.

Dadurch muss der Nutzer keine Zeitcodes von Hand setzen.

## Falls Whisper einen Anker nicht sicher findet

Reihenfolge der Fehlerbehebung:

1. mit einem längeren eindeutigen Anker erneut versuchen
2. Whisper-Modell von `small` auf `medium` erhöhen
3. bei weiterhin problematischer Stelle Zeitstempel manuell prüfen

Die Pipeline darf bei einem nicht gefundenen Anker nicht stillschweigend raten.

## Warum `faster-whisper`

Für diese Pipeline ist `faster-whisper` der Standard, weil wir vor allem brauchen:

- deutsche Transkription
- Wort-Zeitstempel
- lokale Ausführung
- gute Geschwindigkeit
- kein zwingendes externes API-Konto

Das Original-Whisper-Konzept bleibt gleich; `faster-whisper` ist hier nur die praktischere Implementierung.
