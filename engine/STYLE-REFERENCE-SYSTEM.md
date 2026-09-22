# Style-Reference-System

## Ziel

Der Kanal darf seinen Look nicht bei jedem Video neu erfinden. Sobald der Nutzer eine Bildwelt ausdrücklich als final akzeptiert, wird genau eine Master-Referenz verwendet:

```text
assets/channel/STYLE_REFERENCE.png
```

Diese Datei ist kein Szenenbild und kein fertiges Thumbnail. Sie ist ausschließlich der dauerhafte visuelle Kanalanker.

## Verbindliche Kanal-DNA

Die Referenz soll die neue Kanalwelt sichern:

- stark stilisierte hochwertige 3D-Animationsfilm-Optik
- deutlich animiert statt fotorealistisch
- weiche gerundete Formen
- vereinfachte, aber erkennbare Anatomie
- warme filmische Beleuchtung
- hochwertige Materialien und klare Tiefenwirkung
- freundlich und modern, nicht babyhaft
- kein medizinischer Fotorealismus
- kein Anime-/Comic-Look

## Was die Master-Referenz definiert

Sie definiert:

- Grad der Stilisierung
- Rendergrad
- Formensprache
- Materialgefühl
- Lichtcharakter
- Farbharmonie
- Tiefenwirkung
- allgemeines Qualitätsniveau
- visuelle Sprache für Labels und Callouts

Sie definiert nicht automatisch:

- konkrete Figur
- konkretes Lebensmittel
- Pose
- Ort
- Kamerawinkel
- Anatomie
- konkrete Beschriftung
- Szeneninhalt

## Verwendung in Google Flow

Sobald die Datei vorhanden ist, muss der Flow-Agent sie bei **jedem** Bild als `style-only` Referenz laden.

Referenzreihenfolge:

1. `STYLE_REFERENCE.png` → langfristige Kanal-DNA
2. `Bild_01.png` der aktuellen Episode → konkrete Episode-/Continuity-Referenz
3. Character Reference → nur Identität einer wiederkehrenden Figur
4. frühere Szenenreferenz → nur Kontinuität von Ort/Objekt/Komposition, wenn nötig

`Bild_01` bleibt trotzdem immer der Master Style Frame der jeweiligen Episode und wird zuerst allein freigegeben.

## Wiederkehrende Figuren

Für wiederkehrende Figuren können eigene freigegebene Referenzen unter `assets/channel/characters/` liegen. Sie ersetzen niemals die Style Reference und niemals die Episode-Referenz Bild_01.

## Inside-the-Body

Die Master-Referenz gilt auch für anatomische und mikroskopische Bilder. Keine Gesichter auf Organe, Zellen oder Moleküle, außer eine konkrete Szene verlangt ausdrücklich eine personifizierte Lernfigur.

Die wissenschaftliche Struktur bleibt verständlich; Stilisierung darf Fachlichkeit nicht zerstören.

## Fehlt die Referenz?

Solange der Nutzer noch keine kanalweite Master-Referenz freigegeben hat:

- schriftliche Bildweltregeln verwenden
- Bild_01 jeder Episode besonders sorgfältig erzeugen und freigeben
- Bild_01 danach für alle weiteren Bilder derselben Episode als Vorlage nutzen
- nicht behaupten, der langfristige Kanalstil sei bereits endgültig gelockt

Nach Freigabe darf `STYLE_REFERENCE.png` nur auf ausdrücklichen Nutzerwunsch ersetzt werden.

## QA

Vor Akzeptanz eines Flow-Bildes prüfen:

1. Gehört der Renderstil sichtbar zur gleichen Serie?
2. Bleibt die Szene deutlich stilisierte 3D-Animation statt Fotorealismus?
3. Sind Materialien, Licht und Formensprache konsistent?
4. Gibt es keinen unerwünschten Drift zu Anime, Comic oder medizinischer CGI?
5. Sind wiederkehrende Symbole/Objekte erkennbar dieselben?
6. Ist die Anatomie trotz Stil verständlich?
7. Sind die wichtigsten sichtbaren Dinge knapp auf Deutsch beschriftet?
8. Gibt es keinen englischen sichtbaren Text?

Bei FAIL nur die betroffene Szene neu erzeugen.
