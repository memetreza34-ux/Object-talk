# Object-Talk – Biology Illustration World

Status: **KANONISCH / FREIGEGEBEN**

Diese Datei definiert die verbindliche, vollständig textbasierte Biologie-Bildwelt. Google Flow benötigt keinerlei hochgeladene Vorlage.

Zusaetzlich verbindlich fuer sichtbaren Text und Informationsdichte:
`engine/VISIBLE-TEXT-STANDARD.md`

## Kernidee

Object-Talk nutzt **klare animierte Biologie-Illustrationen**.

Die Bilder sollen aussehen wie hochwertige Frames aus einer modernen animierten Biologie-Erklaerserie: anschaulich, sauber, freundlich, fachlich erkennbar und sofort lesbar.

Die Bildwelt muss Muskel, Blut, Zellen, Nerven, Organe, Gewebe, Molekuele, Verdauung, Kreislauf, Immunsystem und andere Biologie-Themen in derselben visuellen Sprache darstellen koennen.

## Feste visuelle Sprache

- 16:9
- illustrierter Animationslook, kein Render-Look
- vereinfachte, fachlich erkennbare Anatomie
- weiche organische Formen
- saubere Konturen
- weiche Farbverlaeufe und subtile Schatten
- leichte raeumliche Tiefe, ohne wie 3D-CGI auszusehen
- helle, ruhige Hintergruende; bevorzugt sehr helles Blau, Mint, Creme oder andere sanfte Flaechen
- kraeftige, klar getrennte biologische Farben
- **ein dominanter Lehrpunkt pro Bild**
- wenige wichtige Elemente statt Detailueberladung
- wichtige Prozesse sichtbar machen, nicht nur Objekte zeigen

## Beschriftungen

Beschriftungen sind eine Hilfe, nicht der Hauptinhalt.

- viewer-facing Text nur Deutsch
- normale Bilder: **0–2 kurze Labels**, maximal 2
- bevorzugt 0 oder 1 Label, wenn die Szene visuell bereits klar ist
- Label bevorzugt 1–2 Woerter, maximal 3 Woerter
- nur wirklich wichtige Strukturen oder Prozesse beschriften
- klare Sans-Serif-Schrift
- keine dekorativen Anfuehrungszeichen um Labels
- duenne saubere Hinweislinien oder Pfeile nur wenn noetig
- Labels muessen eindeutig zur richtigen Struktur zeigen
- keine Textwaende
- keine englischen Labels
- keine internen Bildnummern, Dateinamen oder Prompttitel

### Textkontrast – HARD RULE

- heller Hintergrund → dunkle Schrift
- dunkler Hintergrund → helle Schrift
- niemals helle Schrift auf hellem Hintergrund
- niemals dunkle Schrift auf dunklem Hintergrund
- Text bevorzugt in ruhiger negativer Flaeche platzieren
- wenn der Hintergrund hinter dem Text zu unruhig ist, Textposition verschieben

Schwacher Kontrast oder schwer lesbarer Text = **FAIL / neu generieren**.

## Cover – HARD RULE

Das Cover / erste Hook-Bild darf genau **einen sichtbaren Textblock** enthalten:

- nur den geplanten Titel / Hook
- keine Anatomie-Labels
- keine Unterzeile
- keine Zusatzinfo
- keine Pfeiltexte

Jeder weitere sichtbare Text auf dem Cover = **FAIL / neu generieren**.

## Komplexitaetsregel

Ein Bild muss innerhalb etwa einer Sekunde grob verstanden werden koennen.

Bevorzugt:
- 2–4 zentrale sichtbare Elemente
- 1 Hauptprozess / 1 Hauptaussage
- 0–2 Labels
- klare Blickfuehrung

Wenn mehr erklaert werden muss:
1. unwichtige Information weglassen, oder
2. den Beat auf mehrere Bilder aufteilen.

**Mehr einfache Bilder sind besser als ein ueberladenes Bild.**

## Erlaubte Bildtypen

Die Bildwelt bleibt gleich, aber die Komposition darf stark variieren:

- Organ- oder Gewebe-Cutaway
- Querschnitt
- Makro-Nahaufnahme
- Zell-Innenansicht
- Prozessszene
- Transportweg
- Ursache → Wirkung
- Vorher / Nachher
- Vergleich
- Koerper → Organ → Gewebe → Zelle Massstabswechsel
- einfache Alltagsszene mit biologischem Fokus

Die Bilder sollen NICHT alle wie ein Objekt in der Mitte mit zwei Labels aussehen.

## Farbprinzip

Farben duerfen je nach Thema variieren, muessen aber biologisch klar lesbar bleiben.

Beispiele:
- Blut / Muskel: Rot-, Korall-, Lachs- und warme Rosa-Toene
- Gefaesse / Fluessigkeiten / Sauerstoffwege: Blau- und Tuerkis-Toene
- Nerven / Signale: Gelb, Orange oder Cyan als Akzent
- Zellstrukturen: klar getrennte, harmonische Farben
- Warnung / Belastung: gezieltes Orange-Rot

Keine starre Palette erzwingen, wenn sie der fachlichen Lesbarkeit schadet.

## Harte Verbote

- fotorealistischer Medizin-Look
- Medical-CGI / Anatomiesoftware-Look
- glossy Plastik-3D
- Pixar-/Feature-Film-Character-Look als Standard
- Spielzeug-/Kinderbuch-Look
- sterile Corporate-Stock-Grafik
- ueberladene Infografik
- weisser leerer Studiohintergrund als Standard
- random Icons ohne Erklaerfunktion
- zu viele Pfeile oder Labels
- schwacher Textkontrast
- helle Schrift auf hellem Hintergrund
- dunkle Schrift auf dunklem Hintergrund
- Zusatzlabels auf dem Cover
- Gore / Horror / nasses Gewebe
- komplexe Kleinststrukturen, die fuer den Lehrpunkt nicht gebraucht werden

## Prompt-Grundform

Prompts sollen kurz bleiben.

1. kurze Style-Zeile
2. konkrete biologische Szene
3. sichtbarer Prozess
4. 0–2 deutsche Labels nur wenn noetig
5. klare Textkontrast-Anweisung
6. kurze Negativregel

Der kanonische kurze Styleblock steht in `bildwelt/FLOW-STYLE-BLOCK.txt`.

## Bildwelt ohne hochgeladene Vorlagen
Die schriftliche Bildwelt, der unveränderte 008-Styleblock und die konkreten Szenenbeschreibungen steuern jede Google-Flow-Generierung. Wie beim Verdauungsfilm 008 **keine Referenzbilder hochladen oder anfordern**, auch nicht das ausgewählte Cover. Cover wählen = `Bild_01` festlegen. Alle Folgebilder im gleichen Textstil neu generieren.
## Qualitaetskriterium

Ein gutes Object-Talk-Bild ist:

**schoene Illustration + sofort verstaendliche Biologie + eine Hauptidee + wenig Text + hoher Kontrast + keine unnoetigen Details.**

## Freigegebenes Longform-Referenzvideo – 008 Verdauung (HARTE STILBINDUNG)

Der **exakt ursprüngliche Stilblock aus dem erfolgreichen Video 008** lautet:

> Clean Animated Biology Illustration: simplified but recognizable anatomy, smooth organic forms, clean outlines, soft gradients, subtle depth, bright calm backgrounds, clear biological colors, low complexity, one dominant biological idea per frame.

Fehlstile aus Video 008:

> No photoreal medical imagery, no medical CGI, no glossy 3D, no feature-animation/Pixar look, no toy/kids-book look, no corporate infographic, no clutter, no gore, no random icons, no unnecessary text.

Dieser Stilblock bleibt auch bei Themen wie Schlaf, Träumen oder nächtlichen Körperprozessen dominant: überwiegend helle, ruhige Illustrationshintergründe, hochwertige gezeichnete biologische Formen, zarte Schatten und klare Farben. **Kein neuer dunkler Neon-, Anime-, Sci-Fi- oder glühende-Gehirne-Stil.** Nacht wird nur in einzelnen Kontextbildern durch dezente Farb-/Lichtakzente angedeutet. Menschliche Figuren dürfen ergänzen, biologische Illustration bleibt das Hauptmotiv.

Das gewählte Cover ist ausschließlich das erste Endbild. Gleicher Look für Folgebilder entsteht aus der wiederholten schriftlichen Stilbeschreibung, nicht durch Bildvorlagen.

QA-Hard-Fail: Bei dunklem Neon-/Comic-/Schlafposter-Stil nicht akzeptieren; mit dem verbindlichen textbasierten 008-Stilblock neu generieren.


## Konkrete Textbeschreibung des bewährten Looks
Aus dem erfolgreichen Verdauungsfilm übernehmen wir als **Textregeln**: große bildfüllende Organ-/Zell-/Gewebeszenen, zusammenhängende biologisch plausible Strukturen, warme feine Gewebekonturen, weiche mehrschichtige Schattierung, lebendige sanfte Türkis-/Mint-/Creme-/Blautöne, warme Korall-/Rotakzente und variierende Maßstäbe. Jede Szene zeigt einen klaren Vorgang und eine eigene Perspektive. Google Flow erhält dabei keine alten Bilder, keinen Originalfilm und kein Cover als Referenz.
