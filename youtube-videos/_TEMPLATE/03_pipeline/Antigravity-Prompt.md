# Antigravity-Prompt

Diesen Prompt verwendet Antigravity in Phase 3 für den finalen Zusammenbau.

---

Du setzt ein vollständiges YouTube-Erklärvideo aus **einer fertigen Voiceover-Audiodatei und nummerierten Standbildern** zusammen.

## Eingaben

Verwende:

- finales Voiceover aus `01_script/audio/`
- Bilder aus der ZIP-Datei in `02_bildprompts/bilder-zip/`
- Szenenplanung aus `03_pipeline/pipeline.md`
- maschinenlesbare Anker aus `03_pipeline/scene-map.json`
- globale Regeln aus `engine/PRODUKTIONSREGELN.md`
- Qualitätsprüfung aus `engine/VISUAL-QUALITY-GATE.md`

## Wichtigste Regel

Die fertige Audiodatei ist die **verbindliche Zeitbasis**.

Voiceover niemals kürzen, beschleunigen, verlangsamen oder inhaltlich verändern, damit Bilder besser passen.

## Schritt 1 – Assets vorbereiten

1. Finde die finale Voiceover-Datei.
2. Entpacke die Bilder-ZIP.
3. Prüfe, dass `Bild_01` bis zum letzten geplanten Bild lückenlos vorhanden sind.
4. Prüfe 16:9 und ausreichende Bildauflösung.
5. Stoppe bei fehlenden Bildern oder falscher Nummerierung und melde den Fehler, statt zu raten.

## Schritt 2 – Audio exakt analysieren

Installiere bei Bedarf die Abhängigkeiten aus:

```text
tools/requirements.txt
```

Führe dann `tools/transcribe_audio.py` auf dem finalen Voiceover aus.

Zielordner:

```text
03_pipeline/timing/
```

Erwartete Ergebnisse:

```text
whisper-words.json
subtitles.srt
```

Whisper/faster-whisper muss mit **Wort-Zeitstempeln** arbeiten.

Wenn die erkannte Audiodauer unter 300 Sekunden liegt, nicht final rendern. Das Video erfüllt dann die Mindestlänge nicht.

## Schritt 3 – Exakte Szenenzeiten erzeugen

Führe `tools/build_timeline.py` mit folgenden Dateien aus:

```text
03_pipeline/scene-map.json
03_pipeline/timing/whisper-words.json
```

Erzeuge:

```text
03_pipeline/timing/timeline.json
```

Wenn ein Textanker nicht sicher gefunden wird, **nicht schätzen**. Stoppe und melde exakt, welche Szene bzw. welcher Anker problematisch ist.

`timeline.json` ist danach die verbindliche technische Quelle für sämtliche Bildwechsel.

## Schritt 4 – Video bauen

Baue das Video anhand der exakten Start-/Endzeiten aus `timeline.json`.

Regeln:

- Szene 01 / `Bild_01` startet exakt bei 0 Sekunden.
- Jedes weitere Bild startet bei seinem Timeline-Zeitpunkt.
- Keine Lücken zwischen den Bildern.
- Keine Überlappungen.
- Das letzte Bild endet exakt mit dem Voiceover.
- Bildreihenfolge niemals verändern.

## Standbild-Bewegung

Da ausschließlich Standbilder verwendet werden, erzeuge dezente Bewegung:

- langsamer Push-in
- langsamer Pull-out
- sanfter horizontaler oder vertikaler Pan
- leichter Crop-/Fokuswechsel
- sehr subtile Parallax-Wirkung nur wenn technisch sauber

Nicht verwenden:

- hektische Zooms
- starkes Wackeln
- zufällige Effektbewegungen
- Bildverzerrungen
- künstliche Animation biologischer Inhalte, die im Originalbild nicht vorgesehen ist

## Übergänge

Standard:

- sauberer harter Schnitt
- oder sehr kurzer weicher Übergang

Keine auffälligen Effekt-Transitions ohne inhaltlichen Grund.

## Beschriftungen

Vorhandene deutsche Beschriftungen im Bild:

- niemals verdecken
- niemals abschneiden
- genügend groß lassen
- keine neuen wissenschaftlichen Texte erfinden

## Audio

- Voiceover vollständig erhalten
- keine Wörter hinzufügen oder entfernen
- keine zeitliche Verschiebung
- Musik nur verwenden, wenn ausdrücklich freigegeben oder als Asset vorhanden
- Sprache muss jederzeit klar verständlich bleiben

## Technische Umsetzung

Bevorzugt einen reproduzierbaren Renderer verwenden, z. B. **Remotion** für Timeline, Kamerabewegungen und Render. **FFmpeg/ffprobe** darf für Audio-/Videoanalyse, Encoding und technische Prüfungen verwendet werden.

Entscheidend ist nicht das Tool, sondern dass `timeline.json` exakt eingehalten wird.

## Export

Finale Datei:

```text
04_export/fertiges-video/final-video.mp4
```

Standard:

- 1920×1080
- 16:9
- 30 fps
- H.264
- AAC

Kopiere zusätzlich die erzeugte Untertiteldatei nach:

```text
04_export/subtitles/subtitles.srt
```

## Abschlusskontrolle

Vor finaler Freigabe die komplette Prüfung aus `engine/VISUAL-QUALITY-GATE.md` durchführen.

Besonders prüfen:

- Video mindestens 5:00 Minuten
- beginnt mit `Bild_01`
- alle Bilder verwendet
- keine Nummer fehlt
- Reihenfolge korrekt
- Bildwechsel stimmen mit `timeline.json` überein
- keine schwarzen Frames
- keine abgeschnittenen Labels
- Voiceover vollständig
- Export vollständig und abspielbar
