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
- wichtige sichtbare Dinge knapp auf Deutsch beschriften

## Verbindliche Bildwelt

Seit 27.09.2026 gilt:

**Clean Animated Biology Illustration**

Autoritativ:
- `bildwelt/BIOLOGY-ILLUSTRATION-WORLD.md`
- `bildwelt/FLOW-STYLE-BLOCK.txt`

Kernidee:
- moderne animierte Biologie-Illustrationen
- vereinfachte, erkennbare Anatomie
- weiche organische Formen
- saubere Konturen
- weiche Verlaeufe und subtile Schatten
- leichte Tiefe ohne 3D-CGI-Look
- helle ruhige Hintergruende
- klare biologische Farben
- wenige wichtige Elemente
- sichtbare Prozesse statt dekorativer Objektportraits
- normalerweise 1–3 kurze deutsche Labels

## Visual Storytelling

- ein dominanter Lehrpunkt pro Bild
- Prozesse, Ursache/Wirkung, Wege, Vergleiche und Massstabwechsel bevorzugen
- maximal zwei isolierte Einzelobjektbilder hintereinander
- Bilder nicht ueberladen
- wenn mehr erklaert werden muss: neues Bild statt mehr Kleinteile
- ein Standbild normalerweise 3–6 Sekunden
- harte Obergrenze 7 Sekunden

## Sichtbarer Text

Viewer-facing Text kommt ausschliesslich aus den final akzeptierten Google-Flow-Bildern.

Erlaubt:
- kurze deutsche biologische Labels
- Hinweislinien/Pfeile
- geplanter Cover-Titel

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

`youtube-videos/006-pilot-wundheilung/`

Thema: **Was passiert in deinem Koerper, wenn du dich schneidest?**

Testvorgaben:
- maximal 2:00 Minuten final
- ca. 213 Woerter Script
- 22 eindeutige Bilder
- Haut, Blutgefaesse, Blutplaettchen, Fibrin, Immunzellen, Kollagen und Gewebeumbau
- 100 % Vollbild-Illustration
- 0 sichtbare Remotion-Textelemente

## Drei Phasen

### Phase 1 – Creative Director
Thema → Recherche → Claim-Check → Mechanism Map → Script → Satz-Visual-Plan → Szenenplan → Label-Plan → kurze Flow-Prompts.

### Phase 2 – Google Flow
Jedes Bild einzeln erzeugen → Beschriftung pruefen → interne Nummern im Bild ausschliessen → Bild-QA → finale Assets.

### Phase 3 – Antigravity + Tools + Remotion
Audio vorbereiten → Whisper → Timeline → Vollbild-Illustrationen + leichte Bildbewegung/Schnitt → Render → Final-QA.

## Goldene Regel

**Bilder + Voice + dezente Bewegung. Remotion macht keinen sichtbaren Text. Interne Nummern bleiben unsichtbar.**
