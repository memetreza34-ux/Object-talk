# Flow Production Standard – Object-Talk

## 1. Stil

Verbindliche Bildwelt:
**Clean Animated Biology Illustration**

Nutze:
- `bildwelt/BIOLOGY-ILLUSTRATION-WORLD.md`
- `bildwelt/FLOW-STYLE-BLOCK.txt`
- `engine/VISIBLE-TEXT-STANDARD.md`

Keine historischen 2.5D-, Soft-3D- oder Premium-3D-Regeln verwenden.

## VERBINDLICHE STILKOPIE AUS VIDEO 008

Originaler Flow-Stilblock aus Video 008, wortgleich benutzen:

`Clean Animated Biology Illustration: simplified but recognizable anatomy, smooth organic forms, clean outlines, soft gradients, subtle depth, bright calm backgrounds, clear biological colors, low complexity, one dominant biological idea per frame.`

Originale Ausschlussregel:

`No photoreal medical imagery, no medical CGI, no glossy 3D, no feature-animation/Pixar look, no toy/kids-book look, no corporate infographic, no clutter, no gore, no random icons, no unnecessary text.`

Jedes Folgebild soll im selben hellen, sanft schattierten biomedizinischen Zeichenstil bleiben. Der 008-Stil wird ausschließlich durch den ausführlichen unveränderten Textblock und konkrete Biologie-Szenen übertragen. Keine alten JPGs und kein Cover als Referenzbilder. Bei Themen mit Nacht/Traum kein dunkles Comic-/Neon-Look-and-Feel zulassen. **Wenn die Themenästhetik den Illustrationsstil überschreibt: Image QA FAIL.**

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


## COVER-FIRST-WORKFLOW – HARTE PRODUKTIONSREIHENFOLGE

Autoritativ: `engine/FLOW-COVER-FIRST-WORKFLOW.md`.

**GENAU EINE vollständige Flow-Promptdatei im sichtbaren Ordner, plus EIN ZIP-Ablageordner.** Derselbe Prompt enthält drei Cover und das vollständige Szenenregister. Flow erzeugt erst drei Cover, zeigt sie und wartet auf Nutzerwahl 1/2/3; erst danach Bilder 02+ intern in Fünfergruppen, ohne weitere Promptdateien oder generische Rückfragen. Alle 85 Szenen dürfen im Prompt beschrieben stehen, werden aber NIE in einem einzigen Bildgenerierungs-Batch angefordert. Dateinummern nur Metadaten. Finale Bilder-ZIP unter `02_bildprompts/bilder-zip`, interne QA in `05_info`, entpackte Bilder in `03_pipeline/images`.

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

## 9. Textbasierte Stilkonstanz ohne Vorlagen
Google Flow generiert genauso wie beim bewährten Video 008 **ohne Bildvorlage**. Ein einziger Textprompt definiert Kontur, Form, Schatten, Farbkontrast, Bildtiefe, Kamerasprache, Beschriftung und jede biologische Hauptaktion. Keine hochgeladenen Referenzbilder, Original-008-Frames, Stil-ZIPs oder ausgewählte Cover als Image-to-Image-Vorlage. Jede fertige Szene visuell kontrollieren und abweichende Bilder erneut generieren.
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


## Textbasierte Reproduzierbarkeit
Die erfolgreiche Verdauungsproduktion arbeitete ohne Bildvorlagen. Die Serienkonsistenz wird künftig über denselben ausführlichen 008-Styleblock und konkretisierte Szenenbeschreibungen hergestellt, nie durch Uploads. Mehr Abwechslung: große verbundene Organe, Gewebe-Querschnitte, Zellumgebung, Kapillaren und Prozesse statt leerer Einzelobjekt-Tafeln. Generative Ausgaben sind nicht pixelgenau deterministisch.
