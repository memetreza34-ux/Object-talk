# Presentation / Remotion System – Object-Talk

## Ziel

Remotion ist ausschliesslich Editor, Timing-Engine und Renderer.

**Remotion erzeugt keinen sichtbaren Text.**

Die final akzeptierten Google-Flow-Bilder bleiben zu 100 % die sichtbare Bildflaeche. Wenn Text fachlich notwendig ist, muss er bereits korrekt im Flow-Bild enthalten sein.

## Verbindlicher Kanalstandard

Fuer alle neuen Videos gilt:
- **100 % Vollbild-Illustration**
- keine Remotion-Textoverlays
- keine Zwischenueberschriften
- keine Key-Facts
- keine Summary-Zeilen
- keine Kapiteltexte
- keine Callouts
- keine Untertitel/Captions als Standard
- keine Textkarten
- keine UI-/PowerPoint-/Dashboard-Elemente

## Produktionsnummern sind niemals sichtbar

Interne Bezeichnungen duerfen nur in Produktionsdaten und Dateinamen vorkommen.

Niemals sichtbar im finalen Bild oder Video:
- `Bild_01`, `Bild_02`, `Bild 01`
- `IMAGE 01`
- `Szene 01`, `Scene 01`
- Dateinamen
- Asset-IDs
- Prompttitel
- Produktionshinweise

Wenn ein Flow-Bild eine solche interne Nummer sichtbar enthaelt, ist das Bild FAIL und muss regeneriert werden.

## Sichtbarer Text kommt nur aus Google Flow

Google Flow darf erzeugen:
- kurze deutsche biologische Labels
- Hinweislinien/Pfeile
- einen explizit geplanten Cover-Titel

Google Flow darf keine internen Produktionsnummern rendern.

Wenn Flow einen Begriff falsch schreibt, wird das Bild in Flow korrigiert oder neu erzeugt. Remotion darf falschen Flow-Text niemals reparieren oder ersetzen.

## Overlay-Plan

`03_pipeline/overlay-plan.json` bleibt aus Kompatibilitaetsgruenden bestehen, muss aber fuer neue Videos deaktiviert und leer sein:

```json
{
  "status": "DISABLED",
  "reason": "Remotion visible text is forbidden; all viewer-facing text must already be part of accepted Flow images.",
  "scenes": []
}
```

Ein nicht-leeres `scenes`-Array oder ein sichtbares Text-Overlay ist ein Hard FAIL.

## Was Remotion darf

- finales Audio einbinden
- Szenen nach der echten Voice-Timeline schneiden
- statische Bilder anzeigen
- sanfte Push-/Pull-Bewegungen
- leichte Pans
- harte saubere Schnitte
- sehr dezente nicht-textliche Uebergaenge
- Rendering

## Kamerabewegung auf Standbildern

Bevorzugt:
- Push/Pull ca. 2–4 %
- Pan ca. 20–30 px bei 1080p
- weiche Ease-in/Ease-out-Bewegung
- Bewegungsrichtung folgt dem gezeigten Prozess
- bei informationsreichen Bildern lieber `static`
- kein hektischer Zoom
- kein Shake
- kein Bounce
- keine Meme-Transition

## Was Remotion niemals darf

- Text zeichnen
- Kapitelnummern zeichnen
- Bildnummern zeichnen
- Szenennummern zeichnen
- biologische Labels zeichnen
- Titel erzeugen
- Captions oder Untertitel erzeugen
- Flow-Schreibfehler korrigieren
- Bilder verkleinern, um Text daneben zu setzen
- dauerhafte Rahmen, Karten oder Seitenleisten erzeugen

## Bild bleibt alleiniger sichtbarer Hauptdarsteller

Prioritaet:
1. starke Vollbild-Illustration
2. klarer sichtbarer biologischer Prozess
3. richtige Flow-Beschriftung
4. sinnvolle Bildabwechslung
5. ruhige Kamerabewegung
6. sauberes Audio und Timing

## Hard FAIL

Produktion stoppen bei:
- irgendeinem von Remotion erzeugten sichtbaren Text
- nicht-leerem Overlay-Plan
- sichtbarer interner Bild-/Szenennummer
- sichtbarem Dateinamen oder Asset-ID
- Text, der nicht bereits Bestandteil eines freigegebenen Flow-Bildes war

**Endregel: Remotion = Bilder + Bewegung + Audio + Schnitt + Render. Kein sichtbarer Text.**
