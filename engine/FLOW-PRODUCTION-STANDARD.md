# Flow Production Standard – Object-Talk

## 1. Stil

Verbindliche Bildwelt:
**Clean Animated Biology Illustration**

Nutze:
- `bildwelt/BIOLOGY-ILLUSTRATION-WORLD.md`
- `bildwelt/FLOW-STYLE-BLOCK.txt`
- `engine/VISIBLE-TEXT-STANDARD.md`

Keine historischen 2.5D-, Soft-3D- oder Premium-3D-Regeln verwenden.

## 2. Prompt-Schema

Prompts kurz halten:

```text
[CANONICAL STYLE BLOCK]

[SCENE: konkrete biologische Struktur]
[PROCESS: genau eine sichtbare Hauptidee]
[LABELS: 0–2 exakte deutsche Begriffe, nur wenn noetig]
[TEXT CONTRAST: hell→dunkel / dunkel→hell]
[AVOID: nur die wichtigsten Fehler]
```

## 3. Bildkomplexitaet

Pro Bild bevorzugt:
- 1 Hauptaussage / 1 Hauptprozess
- 2–4 zentrale Elemente
- 0–2 Labels

Wenn ein Bild zu komplex wird:
1. unwichtige Information weglassen, oder
2. in mehrere Bilder aufteilen.

**Mehr einfache Bilder sind besser als ein ueberladenes Bild.**

## 4. Cover

Das Cover / `Bild_01` darf genau einen sichtbaren Textblock enthalten:
- nur Titel / Hook
- keine Anatomie-Labels
- keine Unterzeile
- keine Zusatzinfo
- keine Pfeiltexte

Zusatztext auf dem Cover = regenerieren.

## 5. Vielfalt

Abwechseln zwischen:
- Cutaway
- Querschnitt
- Makro
- Zell-Innenansicht
- Transportweg
- Ursache/Wirkung
- Vergleich
- Vorher/Nachher
- Massstabswechsel
- Alltag + biologische Einblendung

Nicht immer dieselbe zentrierte Objektkomposition verwenden.

## 6. Labels

Labels direkt in Flow erzeugen.

Pflicht:
- Deutsch
- normal: 0–2 Labels, maximal 2
- bevorzugt 0 oder 1, wenn die Szene schon klar ist
- 1–2 Woerter bevorzugt, maximal 3 Woerter
- keine ganzen Saetze
- keine dekorativen Anfuehrungszeichen
- eindeutige Hinweislinie/Pfeil nur wenn noetig
- nur wirklich relevante Begriffe

Falsche Schreibweise, falsche Zuordnung, unnoetiges Label oder unlesbare Schrift = regenerieren.

## 7. Textkontrast

- heller Hintergrund → dunkle Schrift
- dunkler Hintergrund → helle Schrift
- kein hell-auf-hell
- kein dunkel-auf-dunkel
- Text bevorzugt in ruhiger negativer Flaeche platzieren

Schwacher Kontrast = regenerieren.

## 8. Generation

- jedes Bild einzeln erzeugen
- pro finaler Bildnummer genau ein akzeptiertes Asset behalten
- keine Bildduplikate verwenden
- fehlgeschlagenes Bild ersetzen, nicht Varianten sammeln
- Produktionsnummern nur als Dateinamen/Metadaten nutzen, niemals sichtbar rendern

## 9. Referenz

Die schriftliche Bildwelt ist die oberste Stilautoritaet.

Eine spaetere `assets/channel/STYLE_REFERENCE.png` darf nur als zusaetzlicher visueller Anker genutzt werden, nachdem der Nutzer sie explizit freigegeben hat.

`Bild_01` ist nicht automatisch Style-Master fuer die gesamte Episode.

## 10. Hard Fails

Regenerieren bei:
- falscher Biologie
- unklarem Hauptprozess
- mehr als einer konkurrierenden Hauptidee im selben Frame
- zu hoher Komplexitaet
- mehr als 2 Labels im normalen Bild
- Label mit mehr als 3 Woertern
- Zusatztext auf dem Cover
- schwachem Textkontrast
- hellem Text auf hellem Hintergrund
- dunklem Text auf dunklem Hintergrund
- unnoetigem Text
- fotorealem Medizin-Look
- Medical-CGI
- glossy 3D
- Kinderbuch-/Spielzeug-Look
- Corporate-Infografik
- random Icons
- sichtbaren internen Assetnamen
- schwerem KI-Artefakt

## 11. QA-Ziel

Ein akzeptiertes Bild soll wirken wie ein sauberer Frame aus derselben animierten Biologie-Serie und innerhalb etwa einer Sekunde grob erfassbar sein.

**Cover nur Titel. Ein Bild = eine Hauptidee. So wenig Text wie moeglich.**
