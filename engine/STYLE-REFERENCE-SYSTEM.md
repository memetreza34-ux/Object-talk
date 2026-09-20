# Style-Reference-System

## Ziel

Der Kanal darf seinen Look nicht bei jedem Video neu erfinden. Sobald der Nutzer eine Bildwelt ausdrücklich als final akzeptiert, wird genau eine Master-Referenz verwendet:

```text
assets/channel/STYLE_REFERENCE.png
```

Diese Datei ist kein Szenenbild und kein fertiges Thumbnail. Sie ist ausschließlich der dauerhafte visuelle Kanalanker.

## Was die Master-Referenz definiert

Sie definiert:

- Verhältnis Animation / Realismus
- Rendergrad
- Formensprache
- Materialgefühl
- Augen- und Gesichtsdetail bei Object-Talk-Figuren
- Lichtcharakter
- Farbharmonie
- Tiefenwirkung
- allgemeines Qualitätsniveau

Sie definiert nicht automatisch:

- konkrete Figur
- konkretes Lebensmittel
- Pose
- Ort
- Kamerawinkel
- Anatomie
- Beschriftung
- Szeneninhalt

## Verwendung in Google Flow

Sobald die Datei vorhanden ist, muss der Flow-Agent sie bei **jedem** Bild als `style-only` Referenz laden.

Referenzreihenfolge:

1. `STYLE_REFERENCE.png` → immer Stil
2. Character Reference → nur Identität einer wiederkehrenden Figur
3. frühere Szenenreferenz → nur Kontinuität von Ort/Objekt/Komposition, wenn nötig

Eine Charakterreferenz ersetzt niemals die Style Reference.

## Wiederkehrende Figuren

Für wiederkehrende Food-Charaktere können eigene freigegebene Referenzen unter diesem Ordner liegen:

```text
assets/channel/characters/
```

Empfohlene Namen:

```text
apple.png
yogurt.png
egg.png
potato.png
broccoli.png
```

Nur tatsächlich vom Nutzer akzeptierte Originalbilder werden dort gespeichert. Keine künstlichen Platzhalter als echte Referenzen ausgeben.

## Inside-the-Body

Die Master-Referenz gilt auch für anatomische und mikroskopische Bilder. Dort werden jedoch keine Gesichter auf Organe, Zellen oder anatomische Strukturen übertragen, außer eine konkrete Szene verlangt ausdrücklich eine personifizierte Lernfigur.

Die wissenschaftliche Struktur bleibt erkennbar und korrekt; nur Rendergrad, Licht, Materialwelt und allgemeine Animationssprache werden aus der Referenz übernommen.

## Fehlt die Referenz?

Solange der Nutzer noch keine Master-Referenz freigegeben hat:

- bestehende schriftliche Bildweltregeln verwenden
- nicht behaupten, der Kanalstil sei bereits endgültig gelockt
- keine beliebige Generation still als neue Master-Referenz festlegen

Nach Freigabe darf `STYLE_REFERENCE.png` nur auf ausdrücklichen Nutzerwunsch ersetzt werden.

## QA

Vor Akzeptanz eines Flow-Bildes prüfen:

1. Gehört Rendergrad sichtbar zur gleichen Serie?
2. Sind Object-Talk-Figuren ähnlich stark stilisiert?
3. Sind Materialien und Licht konsistent?
4. Ist die Szene nicht plötzlich fotorealistisch oder deutlich cartoonhafter?
5. Sind wiederkehrende Figuren erkennbar dieselben?
6. Ist die Anatomie trotz Stil noch verständlich?
7. Sind deutsche Labels korrekt, falls vorhanden?

Bei FAIL nur die betroffene Szene neu erzeugen.
