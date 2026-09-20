# Antigravity-Prompt

Diesen Prompt verwendet Antigravity in Phase 3 für den finalen Zusammenbau.

---

Du setzt ein vollständiges YouTube-Erklärvideo aus **einer fertigen Voiceover-Audiodatei und nummerierten Standbildern** zusammen.

## Eingaben

Verwende:
- das finale Voiceover aus `01_script/audio/`
- die Bilder aus der ZIP-Datei in `02_bildprompts/bilder-zip/`
- die exakte Bildzuordnung aus `03_pipeline/pipeline.md`

## Wichtigste Regel

Die Audiodatei ist die **verbindliche Zeitbasis**.

Ändere, kürze, beschleunige oder verlangsame das Voiceover nicht.

## Bildzuordnung

Folge `pipeline.md` exakt.

Für jede Szene:
1. Suche im gesprochenen Audio die dort angegebene START-Wortgruppe.
2. Blende das zugehörige Bild exakt an dieser Stelle ein.
3. Lasse es bis zur angegebenen ENDE-Wortgruppe sichtbar.
4. Wechsle danach ohne unnötige Verzögerung zum nächsten Bild.
5. Verändere niemals die Reihenfolge der Bildnummern.

Beispiel:

```text
Szene 07 = Bild_07
START: „Jetzt gelangt die Glukose ins Blut“
ENDE: „und wird im ganzen Körper verteilt“
```

`Bild_07` muss genau für diesen gesprochenen Abschnitt verwendet werden.

## Visuelle Bewegung

Da das Video ausschließlich aus Standbildern besteht, erzeuge dezente Bewegung durch:
- langsame Push-ins
- langsame Zoom-outs
- sanfte horizontale oder vertikale Kamerafahrten
- leichte Fokusbewegungen, wenn sinnvoll
- saubere, kurze Übergänge

Vermeide:
- hektische Zooms
- unnötiges Wackeln
- dauernde Effekte
- Bewegungen, die vom Inhalt ablenken
- starke Verzerrung der Bilder

Die Bewegung soll den Eindruck eines hochwertigen Erklärvideos erzeugen, nicht den eines Slideshows.

## Beschriftungen

Wenn ein Bild bereits deutsche biologische Beschriftungen enthält:
- nicht verdecken
- nicht abschneiden
- genügend Zeit zum Lesen lassen

Keine neuen wissenschaftlichen Behauptungen oder Beschriftungen erfinden.

## Szene 01

`Bild_01` ist die Cover-/Einstiegsszene und muss direkt mit Beginn des Voiceovers sichtbar sein.

## Audio

- Voiceover vollständig erhalten
- keine Worte entfernen
- keine Worte hinzufügen
- Audio nicht verschieben
- Musik nur verwenden, wenn sie ausdrücklich als Asset vorhanden oder freigegeben ist
- Voiceover muss jederzeit klar verständlich bleiben

## Export

Exportiere das finale Video in 16:9 als hochwertige YouTube-Datei nach:

```text
04_export/fertiges-video/
```

## Abschlusskontrolle

Vor dem Export prüfen:
- Video beginnt mit Bild_01
- alle Bilder wurden verwendet
- keine Bildnummer fehlt
- Reihenfolge stimmt
- Bildwechsel entsprechen den START-/ENDE-Wortgruppen
- kein Bild erscheint deutlich zu früh oder zu spät
- vollständiges Voiceover ist vorhanden
- keine leeren Frames
- keine schwarzen Balken
- Beschriftungen sind sichtbar
- Export ist vollständig und abspielbar
