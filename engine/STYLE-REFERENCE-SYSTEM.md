# Style-Reference-System

## Ziel

Der Kanal darf seinen Look nicht bei jedem Video neu erfinden.

Die aktuell freigegebene Bildwelt ist textuell festgelegt in:

```text
bildwelt/APPROVED-VISUAL-WORLD.md
```

Sobald zusätzlich ein einzelnes sauberes, vom Nutzer ausgewähltes Flow-Bild ohne Browser-UI als finale Bildreferenz vorliegt, wird genau eine kanalweite Master-Referenz verwendet:

```text
assets/channel/STYLE_REFERENCE.png
```

Diese Datei ist kein Szenenbild und kein fertiges Thumbnail. Sie ist ausschließlich der dauerhafte visuelle Kanalanker.

## Verbindliche Kanal-DNA

Die freigegebene Kanalwelt ist:

- stark stilisierte hochwertige 3D-Animationsfilm-Optik
- deutlich animiert statt fotorealistisch
- weiche gerundete Formen
- vereinfachte, aber erkennbare Anatomie
- warme filmische Beleuchtung
- hochwertige glatte Materialien und klare Tiefenwirkung
- Inside-the-Body-Grundwelt mit Creme/Apricot/Amber/Orange + tiefem Rot/Burgunder
- Cyan/Türkis als deutlicher Sauerstoff-Kontrast
- freundlich und modern, nicht babyhaft
- kein medizinischer Fotorealismus
- kein Anime-/Comic-Look
- keine nassen, fleischigen oder eklig realistischen Gewebetexturen

Details und Typografie-Regeln: `bildwelt/APPROVED-VISUAL-WORLD.md`.

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

Sobald `STYLE_REFERENCE.png` vorhanden ist, muss der Flow-Agent sie bei **jedem** Bild als `style-only` Referenz laden.

Referenzreihenfolge:

1. `bildwelt/APPROVED-VISUAL-WORLD.md` → schriftliche Kanal-DNA
2. `assets/channel/STYLE_REFERENCE.png` → kanalweite visuelle Referenz, sobald vorhanden
3. `Bild_01.png` der aktuellen Episode → konkrete Episode-/Continuity-Referenz
4. Character Reference → nur Identität einer wiederkehrenden Figur
5. frühere Szenenreferenz → nur Kontinuität von Ort/Objekt/Komposition, wenn nötig

`Bild_01` bleibt immer der Master Style Frame der jeweiligen Episode und wird zuerst allein freigegeben.

## Bild_01 muss die Welt konkretisieren

`Bild_01` legt für die Episode fest:

- exakte Lichtstimmung
- konkrete Farbbalance
- Materialglanz und Oberflächenweichheit
- Detailgrad
- Kameratiefe
- Label-/Typografie-Gefühl
- Stilisierungsgrad von Organen, Gewebe, Zellen und Partikeln

Nach der Freigabe müssen Folgegenerationen sichtbar dieselbe Welt übernehmen. Ein Bild, das plötzlich realistischer, flacher, cartooniger oder anders beleuchtet wirkt, ist `FAIL`.

## Wiederkehrende Figuren und Objekte

Für wiederkehrende Figuren können eigene freigegebene Referenzen unter `assets/channel/characters/` liegen. Sie ersetzen niemals die Style Reference und niemals die Episode-Referenz Bild_01.

Wiederkehrende biologische Objekte und Symbole müssen ebenfalls stabil bleiben, z. B. O₂, CO₂, rote Blutkörperchen, Hämoglobin und Mitochondrien.

## Inside-the-Body

Die Master-Referenz gilt auch für anatomische und mikroskopische Bilder. Keine Gesichter auf Organe, Zellen oder Moleküle, außer eine konkrete Szene verlangt ausdrücklich eine personifizierte Lernfigur.

Die wissenschaftliche Struktur bleibt verständlich; Stilisierung darf Fachlichkeit nicht zerstören.

## Solange noch kein sauberes STYLE_REFERENCE.png vorliegt

Die Bildwelt ist bereits **textuell freigegeben und gelockt**.

Bis ein einzelnes sauberes Referenzbild exportiert wurde:

- `bildwelt/APPROVED-VISUAL-WORLD.md` ist autoritativ
- `Bild_01` jeder Episode besonders sorgfältig erzeugen und freigeben
- `Bild_01` danach für alle weiteren Bilder derselben Episode als exakte Stilvorlage nutzen
- keinen Browser-Screenshot oder eine Collage als `STYLE_REFERENCE.png` verwenden

Nach Freigabe eines sauberen Referenzbildes darf `STYLE_REFERENCE.png` nur auf ausdrücklichen Nutzerwunsch ersetzt werden.

## QA

Vor Akzeptanz eines Flow-Bildes prüfen:

1. Gehört der Renderstil sichtbar zur gleichen Serie?
2. Bleibt die Szene deutlich stilisierte 3D-Animation statt Fotorealismus?
3. Sind Materialien, Licht und Formensprache konsistent?
4. Passen warme Grundfarben und Objekt-Akzentfarben zur Kanalwelt?
5. Gibt es keinen unerwünschten Drift zu Anime, Comic oder medizinischer CGI?
6. Sind wiederkehrende Symbole/Objekte erkennbar dieselben?
7. Ist die Anatomie trotz Stil verständlich?
8. Sind die wichtigsten sichtbaren Dinge knapp auf Deutsch beschriftet?
9. Gibt es keinen englischen sichtbaren Text?

Bei FAIL nur die betroffene Szene neu erzeugen.