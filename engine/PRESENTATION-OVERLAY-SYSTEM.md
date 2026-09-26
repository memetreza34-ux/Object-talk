# Presentation / Remotion System – Object-Talk

## Ziel

Remotion ist Editor und Timing-Engine, nicht Text-Designer.

Die sichtbaren Texte eines Videos kommen aus Google Flow und sind bereits Bestandteil der final akzeptierten Bilder.

## Harte Regel: kein Remotion-Text

Remotion darf fuer neue Object-Talk-Videos **keinen sichtbaren Text erzeugen**.

Verboten:
- Kapitelueberschriften
- Keywords
- Callout-Texte
- Label-Fallbacks
- Untertitel / Captions als Standard
- Cover-Hook
- nachtraegliche Korrektur von Flow-Schrift
- ganze Voice-over-Saetze

Wenn Flow einen Begriff falsch schreibt, wird das Bild in Flow regeneriert oder dort korrigiert. Ein falsches Bild wird nicht durch Remotion repariert.

`overlay-plan.json` muss daher fuer neue Projekte leer sein:

```json
{
  "status": "DISABLED",
  "reason": "All visible text is generated in Google Flow",
  "scenes": []
}
```

Ein nicht-leeres Text-Overlay ist ein Hard FAIL.

## Was Remotion weiterhin darf

- finales Audio einbinden
- Szenen nach echter Voice-Timeline schneiden
- sanfte Push-/Pull-Bewegungen
- leichte Pans
- statische Frames
- harte saubere Schnitte
- sehr dezente nicht-textliche Uebergaenge
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

## Text-Verantwortung liegt bei Flow

Google Flow erzeugt:
- Cover-Titel
- kurze deutsche Labels
- seltene Kapitel-/Vergleichsbegriffe, wenn explizit geplant

Alle Texte sind bereits vor der Generation in `label-plan.json` whitelisted.

Das Bild wird nur akzeptiert, wenn die sichtbare Schrift korrekt ist.

## Bild bleibt Hauptdarsteller

Ein Bild muss den Mechanismus auch ohne zusaetzliche Editor-Overlays verstaendlich machen.

Prioritaet:
1. starke Bildidee
2. klare Prozessdarstellung
3. richtige Flow-Beschriftung
4. sinnvolle Bildabwechslung
5. ruhige Kamerabewegung

Remotion darf niemals eine schwache Bildidee mit Text retten.
