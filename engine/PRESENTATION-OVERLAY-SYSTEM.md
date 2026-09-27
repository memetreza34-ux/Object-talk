# Presentation / Remotion System – Object-Talk

## Ziel

Remotion ist Editor, Timing-Engine und **selektive Praesentationsschicht**.

Die biologischen Illustrationen bleiben der Hauptdarsteller. Remotion darf das Video strukturieren, aber nicht in eine PowerPoint-, Dashboard- oder Presenter-Optik verwandeln.

## Grundverhaeltnis

Standard fuer kuenftige Videos:
- **85–90 % reine Vollbild-Illustration**
- **10–15 % maximal selektive Remotion-Praesentation**

Die Prozentwerte sind eine Gestaltungsleitlinie, kein Zwang zu exakter mathematischer Auslastung. Wenn ein Video ohne Overlay klarer ist, bleiben die Overlays weg.

## Was Remotion-Text darf

Erlaubte Typen:

### 1. Zwischenueberschrift
Bei einem echten grossen Abschnitts- oder Mechanismuswechsel.

Beispiele:
- `1 · Aufnahme`
- `2 · Transport`
- `3 · Abgabe`

Regel:
- bevorzugt ueber der bereits sichtbaren naechsten Illustration
- kein eigener leerer Titelbildschirm als Standard
- normalerweise etwa 0.8–1.5 Sekunden sichtbar

### 2. Key-Fact
Nur fuer eine Aussage, die wirklich haengen bleiben soll.

Beispiele:
- `Sauerstoff reist nicht allein.`
- `Hämoglobin übernimmt den Transport.`

Regel:
- maximal 2–6 Woerter bevorzugt
- keine ganzen Voice-over-Saetze
- sparsam verwenden

### 3. Summary / Prozesszeile
Am Ende oder bei einem wichtigen Zwischenfazit.

Beispiel:
`Aufnahme → Transport → Abgabe`

Darf etwas laenger stehen, solange die Illustration sichtbar bleibt und nicht von Text verdraengt wird.

## Was Remotion-Text NICHT darf

- anatomische Standardlabels ersetzen
- Flow-Schreibfehler reparieren
- ganze Voice-over-Saetze zeigen
- dauerhafte Untertitel als Standard
- nach jedem Bild eine neue Ueberschrift erzeugen
- permanente obere/untere Balken
- Bilder dauerhaft verkleinern, um Text daneben zu stellen
- dauerhafte Rahmen-/Kartenlayouts
- grosse Textwaende
- interne Bildnummern, Dateinamen oder Prompttitel zeigen

Biologische Labels wie `Mitochondrium`, `Lungenbläschen`, `Blutkapillare` bleiben Teil der Google-Flow-Illustration.

## Richtwert nach Videolaenge

Fuer einen ca. 2-Minuten-Test:
- normalerweise 2–3 Zwischenueberschriften
- optional 1 Key-Fact oder 1 Summary

Fuer 5–8 Minuten:
- nur an echten Kapitel-/Mechanismuswechseln
- nicht automatisch in festen Zeitabstaenden
- lieber weniger starke als viele belanglose Einblendungen

## Overlay-Plan

Jedes neue Projekt kann `03_pipeline/overlay-plan.json` verwenden.

Ein leeres `scenes`-Array ist vollkommen gueltig.

Schema:

```json
{
  "status": "READY",
  "version": 2,
  "rules": {
    "full_frame_remains_default": true,
    "language": "de",
    "max_words_per_overlay": 6,
    "no_full_voiceover_sentences": true
  },
  "scenes": [
    {
      "scene": 8,
      "overlays": [
        {
          "kind": "heading",
          "text": "2 · Transport",
          "position": "top-left",
          "animation": "fade-slide",
          "startFraction": 0.04,
          "durationFraction": 0.28
        }
      ]
    }
  ]
}
```

Erlaubte `kind`:
- `heading`
- `keyword`
- `callout`

Erlaubte `position`:
- `top-left`
- `top-center`
- `bottom-left`
- `center`

Erlaubte `animation`:
- `fade-slide`
- `pop`
- `underline`

Pro Szene normalerweise maximal **ein** Overlay.

## Was Remotion weiterhin macht

- finales Audio einbinden
- Szenen nach echter Voice-Timeline schneiden
- sanfte Push-/Pull-Bewegungen
- leichte Pans
- statische Frames
- harte saubere Schnitte
- dezente nicht-textliche Uebergaenge
- selektive Praesentations-Overlays
- Rendering

## Kamerabewegung auf Standbildern

Bevorzugt:
- Push/Pull ca. 2–4 %
- Pan ca. 20–30 px bei 1080p
- weiche Ease-in/Ease-out-Bewegung
- Bewegungsrichtung folgt dem gezeigten Prozess
- bei bereits informationsreichen Bildern lieber `static`
- kein hektischer Zoom
- kein Shake
- kein Bounce
- keine Meme-Transition

## Flow vs. Remotion – klare Arbeitsteilung

### Google Flow
Erzeugt:
- die eigentliche Biologie-Illustration
- anatomische/biologische Labels
- Pfeile/Hinweislinien innerhalb der Illustration
- Cover-Titel, sofern fuer das Cover geplant

### Remotion
Erzeugt nur:
- Kapitel-/Zwischenueberschriften
- wenige Key-Facts
- Summary-/Prozesszeilen

## Bild bleibt Hauptdarsteller

Prioritaet:
1. starke Vollbild-Illustration
2. klarer sichtbarer biologischer Prozess
3. richtige Flow-Beschriftung
4. sinnvolle Bildabwechslung
5. ruhige Kamerabewegung
6. nur wenn es wirklich hilft: kurzes Remotion-Overlay

Remotion darf niemals eine schwache Bildidee mit Text retten.
