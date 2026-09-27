# Object-Talk – Project Contract

Diese Datei ist die dauerhafte oberste Produktionsregel des Repositories. Bei Widerspruechen gilt zuerst eine ausdrueckliche aktuelle Nutzeranweisung, danach dieser Contract.

## Ziel

Object-Talk produziert deutschsprachige YouTube-Erklaervideos zu Ernaehrung, Gesundheit, menschlichem Koerper und Biologie.

Harte Grundregeln:
- normale Kanalvideos mindestens 5:00 Minuten, sofern der Nutzer nicht bewusst einen kuerzeren Testpilot bestellt
- Standardziel 5:30–8:00 Minuten
- 16:9, 1920×1080, 30 fps
- generierte Standbilder bleiben die visuelle Basis
- hohe visuelle Dichte statt langer statischer Bildhaltezeiten
- komplexe Vorgaenge visuell einfach und fachlich plausibel erklaeren
- wissenschaftlich relevante Aussagen pruefen

## Script-Standard – Neugier zuerst

Die ersten 5–10 Sekunden muessen sofort Neugier erzeugen.

Bevorzugt:
- direkte Zuschauerfrage
- ueberraschende Aussage
- Mythos / Fehlannahme
- Alltagsraetsel
- klarer Kontrast

Opening:
1. Hook
2. unerwartete Antwort / Wendung
3. klares Payoff-Versprechen innerhalb der ersten ca. 15 Sekunden

Autoritativ: `engine/SCRIPT-STANDARD.md`

## Audio-/Pacing-Standard

Sofern nichts anderes beschlossen wird:
- finales Voiceover 1.10x
- lange TTS-Pausen vor Whisper/Timeline komprimieren
- finales verarbeitetes `final-voiceover.wav` ist die Timing-Quelle
- Video nicht durch Pausen oder lange Bild-Holds kuenstlich strecken

## Visuelle Dichte / Bildwechsel

- ein Standbild normalerweise etwa 3–6 Sekunden
- harte Obergrenze 7.0 Sekunden
- bei mehreren Lehrbeats neue eindeutige Szene planen
- dasselbe Bild nicht wiederverwenden, um Zeit zu fuellen
- ein dominanter Lehrpunkt pro Bild
- Prozesse, Beziehung, Ursache/Wirkung, Wege, Vergleiche, Vorher/Nachher und Kontext bevorzugen
- maximal zwei isolierte Einzelobjekt-Portraits direkt hintereinander
- benachbarte Szenen sollen sich in mindestens zwei visuellen Dimensionen unterscheiden

## VERBINDLICHE KANAL-BILDWELT

Seit 27.09.2026 gilt kanalweit:

**Clean Animated Biology Illustration**

Autoritativ:
- `bildwelt/BIOLOGY-ILLUSTRATION-WORLD.md`
- `bildwelt/FLOW-STYLE-BLOCK.txt`

Kernregeln:
- animierte Biologie-Illustration statt Render-Look
- vereinfachte, fachlich erkennbare Anatomie
- weiche organische Formen
- saubere Konturen
- weiche Farbverlaeufe und subtile Schatten
- leichte Tiefe ohne 3D-CGI-Wirkung
- helle ruhige Hintergruende
- starke, klar getrennte biologische Farben
- wenige wichtige Elemente
- ein klarer biologischer Prozess oder Zusammenhang pro Bild
- normalerweise 1–3 kurze deutsche Labels fuer wichtige Strukturen

Die Bildwelt muss fuer Muskel, Blut, Zellen, Nerven, Organe, Gewebe, Molekuele, Verdauung, Kreislauf, Immunsystem und weitere Biologie-Themen funktionieren.

## Komplexitaet

Ein Bild soll innerhalb etwa einer Sekunde grob verstanden werden koennen.

Bevorzugt:
- 2–5 zentrale sichtbare Elemente
- 1 Hauptprozess
- 1–3 Labels
- klare Blickfuehrung

Wenn mehr Inhalt noetig ist, wird ein neues Bild geplant statt das vorhandene zu ueberladen.

## Beschriftungen

- sichtbarer Text nur Deutsch
- normalerweise 1–3 kurze Labels
- Labels nur fuer wichtige Strukturen oder Prozesse
- klare Sans-Serif-Schrift
- duenne saubere Hinweislinien oder Pfeile
- keine Textwaende
- keine internen Assetnamen, Szenennummern, Dateinamen oder Promptueberschriften

Die Labels werden fuer diese Bildwelt direkt in Google Flow erzeugt. Falsche Schrift oder falsche Zuordnung = Bild neu erzeugen/korrigieren.

Remotion erzeugt fuer neue Videos keinen sichtbaren Text, sofern der Nutzer nichts anderes anordnet.

## Harte Stilverbote

- fotorealistischer Medizin-Look
- Medical-CGI / Anatomiesoftware-Look
- glossy Plastik-3D
- Pixar-/Feature-Film-Look als Standard
- Spielzeug-/Kinderbuch-Look
- sterile Corporate-Stock-Grafik
- ueberladene Infografik
- leere weisse Studioflaeche als Standard
- random Icons ohne Lehrfunktion
- zu viele Labels/Pfeile
- Gore / Horror / nasses Gewebe
- unnoetige Kleinststrukturen

## Bildtypen / Vielfalt

Erlaubt und erwuenscht sind stark unterschiedliche Kompositionen innerhalb derselben Bildwelt:
- Cutaway
- Querschnitt
- Makro-Nahaufnahme
- Zell-Innenansicht
- Prozess
- Transportweg
- Ursache → Wirkung
- Vorher / Nachher
- Vergleich
- Massstabswechsel Koerper → Organ → Gewebe → Zelle
- einfache Alltagsszene mit biologischem Fokus

Nicht alle Bilder duerfen wie ein zentriertes Einzelobjekt mit drei Labels aussehen.

## Prompt-Standard

Prompts fuer Flow bleiben kurz:
1. kanonischer Styleblock
2. konkrete Szene
3. sichtbarer Prozess
4. 1–3 deutsche Labels
5. kurze Negativregel

Prompt-Anweisungen auf Englisch, sichtbare Texte Deutsch.

## Referenzsystem

Die schriftliche Bildwelt ist die oberste Stilautoritaet.

`assets/channel/STYLE_REFERENCE.png` darf spaeter als zusaetzlicher visueller Anker genutzt werden, sobald der Nutzer ein einzelnes sauberes Referenzbild explizit akzeptiert hat. Die Bildreferenz darf die schriftlichen Regeln nicht ueberschreiben.

Das Cover `Bild_01` wird nicht automatisch als Stilanker fuer alle Folgebilder verwendet.

## Asset-Hygiene

- pro finaler Bildnummer genau ein retained Asset
- FAIL wird ersetzt, nicht dauerhaft gesammelt
- keine Bildduplikate fuer mehrere Szenen
- keine Luecken im finalen nummerierten Set

## Drei Phasen

### Phase 1 – Creative Director
Recherche → Claim-Check → Script → Mechanism Map → Satz-Visual-Plan → Szenenplan → Label-Plan → kurze Flow-Prompts.

### Phase 2 – Google Flow
Bild fuer Bild erzeugen → Labels pruefen → wissenschaftliche/visuelle QA → finale eindeutige Assets.

### Phase 3 – Antigravity + Tools + Remotion
Audio kanonisieren → Whisper → Timeline → leichte Bildbewegung/Schnitt → Render → Final-QA.

## Autoritative Reihenfolge

1. aktuelle ausdrueckliche Nutzeranweisung
2. `PROJECT_CONTRACT.md`
3. `bildwelt/BIOLOGY-ILLUSTRATION-WORLD.md`
4. `PROJECT_STATE.md`
5. `config/channel.json`
6. aktuelle Engine-Regeln
7. aktuelles Projekt
8. historische Piloten nur als Lern-/Fehlerhistorie

## Goldene Regel

**Schoene animierte Illustration + sofort verstaendliche Biologie + wenig Komplexitaet + klare deutsche Beschriftung + sichtbarer Prozess.**
