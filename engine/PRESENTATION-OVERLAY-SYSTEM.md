# Presentation-Overlay-System – Object-Talk

## Ziel

Die Bildwelt bleibt hochwertig, semi-realistisch und 3D. Das Video soll aber nicht wie eine reine Diashow wirken.

Darum gilt ab jetzt:

- **Vollbild bleibt der Standard.** Das generierte Erklärbild füllt den ganzen Frame.
- Remotion darf darüber gezielte grafische Ebenen legen: kurze Überschriften, einzelne Schlüsselwörter, Labels, Linien und kleine Hervorhebungen.
- Die Bilder selbst werden **nicht** in Anime-, Comic- oder Cartoon-Stil umgestellt.
- „Mehr Animation“ bedeutet: bessere Inszenierung, Text-/Label-Animationen und visuelle Führung – nicht eine neue Bildwelt.

## 1. Verhältnis Vollbild zu Overlay

Richtwert pro Video:

- ca. **65–75 %** der Szenen: reines Vollbild ohne große Textüberschrift
- ca. **20–30 %**: kurze Überschrift oder Schlüsselwort-Overlay
- ca. **10–15 %**: zusätzliche grafische Erklärung wie Callout, Vergleichsmarkierung oder animiertes Label

Die Werte sind keine starre Quote. Ein Overlay braucht immer einen Erklärgrund.

## 2. Erlaubte Overlay-Typen

### A – Kapitel-/Mechanismus-Überschrift

2–5 Wörter, z. B.:

- `Der Dünndarm`
- `Blutzucker steigt`
- `Insulin ist ein Signal`
- `Speicherung als Glykogen`

Einsatz:

- bei einem echten neuen Abschnitt
- bei einer wichtigen Erkenntnis
- bei einem starken Übergang Organ → Zelle → Wirkung

Nicht in jeder Szene.

### B – Schlüsselwort

1–3 Wörter, kurz eingeblendet, passend zum gerade gesprochenen Begriff.

Beispiele:

- `Glukose`
- `Insulin`
- `Darmzotten`
- `Glykogen`

### C – Animiertes Label / Callout

Wenn Google Flow Text schlecht rendert oder ein Begriff besonders wichtig ist, darf Remotion das Label sauber über das Bild legen.

Regeln:

- kurze deutsche Begriffe
- eindeutige Zuordnung
- kein langer Erklärungstext
- nicht über die wichtigste Anatomie legen

### D – Vergleichs- oder Prozessmarker

Kurze visuelle Marker wie:

- `vorher` / `danach`
- `mehr` / `weniger`
- `Aufnahme`
- `Speicherung`

Nur wenn sie den Vergleich deutlich schneller verständlich machen.

## 3. Was NICHT erlaubt ist

- dauerhafte Untertitel als eingebrannter Textblock
- komplette Voice-over-Sätze im Bild
- große PowerPoint-Flächen
- Karten-/Dashboard-Look ohne Grund
- Anime-/Comic-Schrift
- hektische Textsprünge
- mehr als zwei Zeilen pro Overlay
- mehr als ungefähr sechs Wörter in einer Überschrift
- Text in jeder Szene nur damit „mehr passiert“

## 4. Animationssprache

Overlays werden in Remotion ruhig animiert.

Bevorzugt:

- Fade-in + leichte Bewegung nach oben
- sanfter Slide-in
- kurze Scale-in-Bewegung
- dezente Unterstreichung / Accent-Line
- animierte Pointer-/Callout-Linie
- kurzer Highlight-Pulse bei Schlüsselbegriffen

Verboten:

- Bounce
- Shake
- aggressive Zooms
- Meme-Text
- hektische Popups
- animeartige Speedlines oder Comic-Effekte

## 5. Timing

Überschriften sollen nicht die ganze Szene permanent dominieren.

Richtwerte:

- Kapitelüberschrift: ca. 1,8–3,5 Sekunden
- Schlüsselwort: ca. 1–2,5 Sekunden
- Label/Callout: so lange wie für die Zuordnung nötig

Overlay-Timing folgt der echten Audio-Timeline und darf nicht vor dem gesprochenen Begriff erscheinen.

## 6. Bild bleibt Hauptdarsteller

Das Vollbild muss auch ohne Overlay verständlich bleiben.

Das Overlay darf:

- Orientierung geben
- einen Begriff benennen
- einen Vergleich verdeutlichen
- den Blick führen

Es darf **nicht** eine schwache Bildidee retten.

## 7. Text entsteht bevorzugt im Editor

Wichtige Überschriften und wiederkehrende Schlüsselbegriffe werden bevorzugt in Remotion erzeugt statt von Google Flow direkt ins Bild gerendert zu werden.

Vorteile:

- korrekte deutsche Rechtschreibung
- einheitliche Typografie
- wiederverwendbare Animation
- bessere Lesbarkeit
- kein KI-Gibberish

Flow-Labels bleiben erlaubt, wenn sie korrekt erzeugt wurden. Bei wiederholten Textfehlern wird eine textfreie Bildversion verwendet und das Label in Remotion ergänzt.

## 8. Pilot „Zucker im Blut“

Für den aktuellen 26-Bilder-Pilot wird eine eigene Datei verwendet:

```text
03_pipeline/overlay-plan.json
```

Sie definiert nur ausgewählte Szenen mit Überschriften oder Schlüsselwörtern. Alle anderen Szenen bleiben Vollbild.

## 9. Qualitätsregel

Ein Overlay ist nur gut, wenn es mindestens eine dieser Fragen verbessert:

1. Wo sind wir gerade?
2. Was ist der wichtigste Begriff?
3. Was verändert sich?
4. Was soll der Zuschauer jetzt behalten?

Wenn keine Frage dadurch klarer wird: Overlay weglassen.
