# Object-Talk

Produktionssystem fuer den deutschen YouTube-Kanal **Object-Talk / FoodSpricht**.

## Ziel

Deutschsprachige Erklaervideos ueber Ernaehrung, Gesundheit, menschlichen Koerper und Biologie.

Standard:
- normale Kanalvideos mindestens 5:00 Minuten
- dokumentierte Testpiloten duerfen kuerzer sein
- 16:9 / 1920×1080 / 30 fps
- hohe visuelle Dichte aus generierten Standbildern
- wissenschaftlich plausibel und leicht verstaendlich
- wichtige sichtbare Dinge nur dann knapp beschriften, wenn es wirklich hilft

## Verbindliche Bildwelt

Seit 27.09.2026 gilt:

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
- sichtbare Prozesse statt dekorativer Objektportraits

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
- Text bevorzugt in ruhiger negativer Flaeche

Schlecht lesbarer Text = regenerieren.

## Visual Storytelling

- ein dominanter Lehrpunkt pro Bild
- Prozesse, Ursache/Wirkung, Wege, Vergleiche und Massstabwechsel bevorzugen
- maximal zwei isolierte Einzelobjektbilder hintereinander
- Bilder nicht ueberladen
- wenn mehr erklaert werden muss: unwichtige Info weglassen oder neues Bild planen
- **lieber mehr einfache Bilder als ein ueberladenes Bild**
- ein Standbild normalerweise 3–6 Sekunden
- harte Obergrenze 7 Sekunden

## Sichtbarer Text

Viewer-facing Text kommt ausschliesslich aus den final akzeptierten Google-Flow-Bildern.

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

Bild-/Szenennummern bleiben reine Produktionsmetadaten.

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

Details: `engine/PRESENTATION-OVERLAY-SYSTEM.md`.

## Aktueller Pilot

`youtube-videos/007-pilot-gaensehaut/`

Thema: **Warum bekommst du Gänsehaut?**

Testvorgaben:
- maximal 2:00 Minuten final
- ca. 190 Woerter Script
- 20 eindeutige Bilder
- Haut, Nervensignal, sympathisches Nervensystem, Haarfollikel, Haaraufrichtemuskel und Tierfell
- Cover nur Titel
- normale Bilder max. 2 Labels
- hoher Textkontrast
- niedrige Informationsdichte
- 100 % Vollbild-Illustration
- 0 sichtbare Remotion-Textelemente
- 0 sichtbare Produktionsnummern

## Drei Phasen

### Phase 1 – Creative Director
Thema → Recherche → Claim-Check → Mechanism Map → Script → Satz-Visual-Plan → Szenenplan → Informationsbudget → Label-Plan → kurze Flow-Prompts.

### Phase 2 – Google Flow
Jedes Bild einzeln erzeugen → Cover title-only prüfen → Beschriftung und Kontrast prüfen → Informationsdichte prüfen → interne Nummern im Bild ausschliessen → Bild-QA → finale Assets.

### Phase 3 – Antigravity + Tools + Remotion
Audio vorbereiten → Whisper → Timeline → Vollbild-Illustrationen + leichte Bildbewegung/Schnitt → Render → Final-QA.

## Goldene Regel

**Cover nur Titel. Ein Bild = eine Hauptidee. So wenig Text wie möglich. Hoher Kontrast. Lieber mehr Bilder als mehr Information in einem Frame.**
