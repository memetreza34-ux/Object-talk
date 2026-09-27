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

Die kanonische Spezifikation liegt hier:

`bildwelt/BIOLOGY-ILLUSTRATION-WORLD.md`

Der kurze Flow-Styleblock liegt hier:

`bildwelt/FLOW-STYLE-BLOCK.txt`

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

Diese Bildwelt muss Muskel, Blut, Zellen, Nerven, Organe, Gewebe, Molekuele, Verdauung, Kreislauf, Immunsystem und weitere Biologie-Themen tragen koennen.

## Was nicht mehr gilt

Nicht reaktivieren:
- fruehere 2.5D-/Soft-3D-Regeln
- fruehere Premium-3D-/Feature-Animation-Regeln
- historische Pilot-Bildwelten als Kanalstandard
- alte Style-Reference-Logiken

## Visual Storytelling

Unabhaengig vom konkreten Motiv:
- ein dominanter Lehrpunkt pro Bild
- Prozesse, Ursache/Wirkung, Wege, Vergleiche und Massstabwechsel bevorzugen
- maximal zwei isolierte Einzelobjektbilder hintereinander
- Bilder nicht ueberladen
- wenn mehr erklaert werden muss: neues Bild statt mehr Kleinteile
- ein Standbild normalerweise 3–6 Sekunden
- harte Obergrenze 7 Sekunden

## Text im Bild

Biologische Beschriftungen kommen aus Google Flow:
- viewer-facing Text nur Deutsch
- normalerweise 1–3 kurze Labels
- saubere Hinweislinien/Pfeile
- keine Textwaende
- keine internen Assetnamen/Szenennummern

## Praesentationssystem

Die Illustrationen bleiben fast immer vollformatig.

Kanalstandard:
- ca. **85–90 % reine Vollbild-Illustration**
- maximal ca. **10–15 % selektive Remotion-Praesentation**

Remotion darf sparsam ergaenzen:
- Zwischenueberschriften bei echten Abschnittswechseln
- kurze Key-Facts
- eine Summary-/Prozesszeile

Dabei gilt:
- normalerweise 2–6 Woerter
- keine ganzen Voice-over-Saetze
- keine anatomischen Labels ersetzen
- keine dauerhaften Rahmen, Seitenleisten oder PowerPoint-/Dashboard-Layouts
- Zwischenueberschriften bevorzugt kurz ueber der bereits sichtbaren naechsten Illustration

Fuer ein ca. 2-Minuten-Video normalerweise 2–3 Zwischenueberschriften plus optional 1 Key-Fact/Summary.

Details:
`engine/PRESENTATION-OVERLAY-SYSTEM.md`

## Aktueller Pilot

`youtube-videos/005-pilot-sauerstoff-zelle/`

Thema: **Wie kommt Sauerstoff von der Lunge bis in eine einzelne Koerperzelle?**

Testvorgaben:
- maximal 2:00 Minuten final
- 250 Woerter Script
- 22 eindeutige Bilder
- testet Lunge, Blut, Herz, Zelle und Mitochondrium in derselben neuen Bildwelt

## Drei Phasen

### Phase 1 – Creative Director
Thema → Recherche → Claim-Check → Mechanism Map → Script → Satz-Visual-Plan → Szenenplan → Label-Plan → kurze Flow-Prompts → selektive Praesentationspunkte planen.

### Phase 2 – Google Flow
Jedes Bild einzeln erzeugen → Beschriftung pruefen → Bild-QA → finale Assets.

### Phase 3 – Antigravity + Tools + Remotion
Audio vorbereiten → Whisper → Timeline → Vollbild-Illustrationen + leichte Bildbewegung/Schnitt + wenige Zwischenueberschriften/Key-Facts/Summary → Render → Final-QA.

## Goldene Regel

**Vollbild-Illustration ist Standard. Remotion ergaenzt selten und gezielt.**
