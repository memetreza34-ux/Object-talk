# Object-Talk

Produktionssystem fuer den deutschen YouTube-Kanal **Object-Talk / FoodSpricht**.

## Ziel

Deutschsprachige Erklaervideos ueber Ernaehrung, Gesundheit, menschlichen Koerper und Biologie.

Standard:
- normale Kanalvideos mindestens 5:00 Minuten
- 16:9 / 1920×1080 / 30 fps
- hohe visuelle Dichte aus generierten Standbildern
- wissenschaftlich plausibel und leicht verstaendlich
- wichtige sichtbare Dinge nur dann knapp beschriften, wenn es wirklich hilft

## Produktionsphase

Die interne Testphase `000–007` ist abgeschlossen.

Aktive reguläre Longform-Produktion:
`youtube-videos/009-longform-schlaf/`

Thema:
**Was passiert in deinem Körper, während du schläfst?**

Status: **Phase 1 vorbereitet, Medien ausstehend**.

Ziel:
- 6:00–7:00 Minuten
- 986 Wörter
- 77 eindeutige Illustrationen
- Hook → innere Uhr/Schlafdruck → Schlafphasen/Tiefschlaf → Gedächtnis/Immunsystem → REM → Morgen → Schluss
- vollständiger Export mit YouTube-Caption, MP4 und externen SRT-Untertiteln

## Verbindliche Bildwelt

**Clean Animated Biology Illustration**

Autoritativ:
- `bildwelt/BIOLOGY-ILLUSTRATION-WORLD.md`
- `bildwelt/FLOW-STYLE-BLOCK.txt`
- `engine/VISIBLE-TEXT-STANDARD.md`

Kernidee:
- moderne animierte Biologie-Illustrationen
- vereinfachte, erkennbare Anatomie
- weiche organische Formen
- saubere Konturen
- weiche Verlaeufe und subtile Schatten
- leichte Tiefe ohne 3D-CGI-Look
- helle ruhige Hintergruende
- klare biologische Farben
- **eine Hauptidee pro Bild**
- bevorzugt 2–4 wichtige sichtbare Elemente
- normale Bilder **0–2 kurze deutsche Labels**, nur wenn nötig

## Cover

Das Cover / erste Hook-Bild:
- genau ein sichtbarer Textblock
- nur Titel / Hook
- keine Anatomie-Labels
- keine Unterzeile
- keine Zusatzinfo

Zusatztext auf dem Cover = regenerieren.

## Textkontrast

- heller Hintergrund → dunkle Schrift
- dunkler Hintergrund → helle Schrift
- kein hell-auf-hell
- kein dunkel-auf-dunkel
- schlecht lesbarer Text = regenerieren

## Visual Storytelling

- ein dominanter Lehrpunkt pro Bild
- Prozesse, Ursache/Wirkung, Wege, Vergleiche und Massstabwechsel bevorzugen
- maximal zwei isolierte Einzelobjektbilder hintereinander
- wenn mehr erklaert werden muss: unwichtige Info weglassen oder neues Bild planen
- **lieber mehr einfache Bilder als ein ueberladenes Bild**
- ein Standbild normalerweise 3–6 Sekunden
- harte Obergrenze 7 Sekunden
- keine Bildduplikate zum Zeitfuellen

## Sichtbarer Text

Viewer-facing Text kommt ausschliesslich aus final akzeptierten Google-Flow-Bildern.

Normale Bilder:
- 0–2 Labels, maximal 2
- bevorzugt 0 oder 1
- Label bevorzugt 1–2 Woerter, maximal 3 Woerter
- keine ganzen Saetze
- keine dekorativen Anfuehrungszeichen

Niemals sichtbar:
- `Bild_01`, `Bild 01`, `IMAGE 01`
- `Szene 01`, `Scene 01`
- Dateinamen
- Asset-IDs
- Prompttitel
- Produktionshinweise

## Praesentationssystem

**100 % Vollbild-Illustration. Remotion erzeugt keinen sichtbaren Text.**

Remotion darf nur:
- Audio
- Timing
- leichte Push-/Pull-/Pan-Bewegungen
- statische Frames
- Schnitte
- dezente nicht-textliche Uebergaenge
- Rendering

Nicht erlaubt:
- Zwischenueberschriften
- Key-Facts
- Summary-Zeilen
- Kapiteltexte
- Callouts
- Untertitel/Captions als Standard
- Textkarten
- sichtbare Bild-/Szenennummern

`03_pipeline/overlay-plan.json` muss deaktiviert und leer bleiben.

## Referenz für Longform-Videos

Der erste erfolgreiche 6–7-Minuten-Film **008 Verdauung** dient als inhaltlich-technisches Beispiel für **schriftliche Bildwelt, Flow-Promptgliederung, szenische Planung, Antigravity/Remotion, Export und QA**. **Keine Bildvorlage oder Referenzdatei hochladen.** 009 Schlaf übernimmt diese Produktionsstruktur bis hin zu 77 Szenen und 13 Mechanismusabschnitten; nur der fachliche Inhalt wechselt. Details: `engine/LONGFORM-008-MASTERSTANDARD.md`.

## Verbindlicher Flow-Produktionsablauf

**3 eigenständige Cover → Nutzer wählt 1/2/3 → Bilder ab 02 in aufeinanderfolgenden 5er-Batches**. Nur EINE vollständig ausgefüllte Flow-Promptdatei (darin alle Szenen), dazu EIN Ordner `bilder-zip/`. Der Prompt erzwingt trotzdem die gestufte Generierung: drei Cover → Auswahl → jeweils höchstens fünf Bilder. Keine zusätzlichen Batchdateien. Interne Bildreviews und Labelpläne liegen in `05_info`, entpackte Bilder in `03_pipeline`. Vorgabe: `engine/FLOW-COVER-FIRST-WORKFLOW.md`.

## Drei Phasen

### Phase 1 – Creative Director
Thema → Recherche → Claim-Check → Mechanism Map → Script → Szenenplan → Informationsbudget → Label-Plan → kurze Flow-Prompts.

### Phase 2 – Google Flow
Jedes Bild einzeln erzeugen → Cover title-only pruefen → Beschriftung und Kontrast pruefen → Informationsdichte pruefen → interne Nummern ausschliessen → Bild-QA → finale Assets.

### Phase 3 – Antigravity + Tools + Remotion
Audio vorbereiten → Whisper → Timeline → Vollbild-Illustrationen + leichte Bildbewegung/Schnitt → Render → Final-QA.

## Goldene Regel

**Cover nur Titel. Ein Bild = eine Hauptidee. So wenig Text wie möglich. Hoher Kontrast. Lieber mehr Bilder als mehr Information in einem Frame.**


## Neuer einfacher Videoordner (ab 009)

Für neue Videos gibt es nur drei sichtbare Arbeitsordner: `01_script` (Fließtext + Audio), `02_bildprompts` (ein Flow-Prompt + Bilder-ZIP), `03_export` (VIDEO.mp4, COVER.png, YouTube-Caption, Untertitel mit echten Zeitstempeln). Alle technischen Details in verstecktem `.intern`. Das Cover ist NUR Thumbnail, nicht Videoszene. Vollständige Beschreibung: `engine/FLOW-COVER-FIRST-WORKFLOW.md`.
