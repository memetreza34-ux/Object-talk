# AGENTS.md – Object-Talk Repository

Diese Datei ist der Bootstrap fuer ChatGPT, Antigravity, Codex und andere Repository-Agenten.

## Vor jeder Arbeit lesen

1. `PROJECT_CONTRACT.md`
2. `bildwelt/BIOLOGY-ILLUSTRATION-WORLD.md`
3. `PROJECT_STATE.md`
4. `config/channel.json`
5. `config/video.json`
6. `THEMEN-GEHIRN.md`
7. `engine/README.md`
8. `engine/SCRIPT-STANDARD.md`
9. `engine/PLANNING-V2.md`
10. `engine/PRESENTATION-OVERLAY-SYSTEM.md`
11. relevante Dateien des aktuellen YouTube-Projekts

Aktiver Testpilot steht in `PROJECT_STATE.md`.

## VERBINDLICHE BILDWELT

Kanalweit gilt:

**Clean Animated Biology Illustration**

Autoritativ:
- `bildwelt/BIOLOGY-ILLUSTRATION-WORLD.md`
- `bildwelt/FLOW-STYLE-BLOCK.txt`

Nicht reaktivieren:
- alte 2.5D-/Soft-3D-Regeln
- alte Premium-3D-/Feature-Animation-Regeln
- historische Pilot-Stile als Kanalstandard
- alte Style-Reference-Systeme

## Bildprinzip

Jedes normale Biologie-/Gesundheitsbild soll:
- wie ein sauberer Frame aus einer animierten Biologie-Erklaerserie wirken
- vereinfachte, fachlich erkennbare Anatomie zeigen
- weiche organische Formen, klare Konturen, weiche Verlaeufe und leichte Tiefe verwenden
- hell und uebersichtlich bleiben
- wenige wichtige Elemente zeigen
- einen klaren Prozess/Zusammenhang sichtbar machen
- normalerweise 1–3 kurze deutsche Labels enthalten

Komplexitaet klein halten. Wenn ein Bild zu viel erklaeren muesste, neue Szene planen.

## Prompting

Flow-Anweisungen auf Englisch.
Viewer-facing Text nur Deutsch.

Prompts kurz halten:
1. kanonischer Styleblock
2. konkrete Szene
3. Prozess
4. 1–3 Labels, nur wenn noetig
5. kurze Negativregel

Keine langen Style-Romane in jedem Szenenprompt.

## HARTE UNSICHTBARKEITSREGEL FUER PRODUKTIONS-IDs

Interne Nummern duerfen nur in Dateien/Planung existieren.

Niemals sichtbar rendern:
- `Bild_01`, `Bild_02`, `Bild 01`
- `IMAGE 01`
- `Szene 01`, `Scene 01`
- Dateinamen
- Asset-IDs
- Prompttitel
- Produktionshinweise

Jeder Flow-Prompt muss klarstellen: **Bild-/Szenennummern sind reine Produktionsmetadaten und duerfen nicht Teil des Bildes werden.**

Wenn eine interne Nummer im Bild sichtbar ist: REGENERATE.

## Phase 1 – Creative Director

Muss:
- Fakten pruefen
- Mechanism Map erstellen
- starken Neugier-Hook schreiben
- jeden Speech-Beat als echtes Erklaerbild planen
- Prozesse, Beziehungen, Wege, Ursache/Wirkung, Vergleiche und Massstabwechsel bevorzugen
- maximal zwei isolierte Einzelobjektbilder hintereinander zulassen
- sichtbaren Erklaerwert und Unterschied zu Nachbarbildern definieren
- Labels auf 1–3 kurze wichtige Begriffe begrenzen
- **keine Remotion-Texte oder Text-Overlays planen**

## Phase 2 – Google Flow

- jedes Bild einzeln erzeugen
- kanonischen Styleblock verwenden
- biologische Labels direkt im Bild erzeugen
- falsche Labels/Schreibweise korrigieren oder regenerieren
- interne Bild-/Szenennummern niemals sichtbar machen
- pro finaler Bildnummer genau ein akzeptiertes Asset behalten
- keine alte Pilot-Bildwelt als Referenz verwenden

## Phase 3 – Editor / Antigravity / Remotion

Grundsatz:
**100 % Vollbild-Illustration. Remotion erzeugt keinen sichtbaren Text.**

Remotion ist nur fuer:
- Audio
- Timing
- leichte Zoom-/Pan-Bewegungen
- statische Frames
- Schnitte
- dezente nicht-textliche Uebergaenge
- Rendering

Remotion darf NICHT erzeugen:
- Zwischenueberschriften
- Key-Facts
- Summary-Zeilen
- Kapiteltexte
- Callouts
- Untertitel/Captions als Standard
- anatomische Labels
- Textkarten
- sichtbare Bild-/Szenennummern
- irgendeinen sonstigen viewer-facing Text

`03_pipeline/overlay-plan.json` muss leer/deaktiviert bleiben.

## Timing

`raw Voice → prepare_audio.py → final-voiceover.wav → transcribe_audio.py → word-timings.json → build_timeline.py → timeline.json`

Standard:
- Voice 1.10x
- lange Pausen komprimieren
- kein Standbild ueber 7 Sekunden
- kein Bildasset doppelt verwenden

## Fail-closed

STOP bei:
- schwachem Script-Hook
- Script/Audio-Mismatch
- fehlenden/doppelten Bildern
- wissenschaftlich falscher Kernaussage
- ueberladenem Bild
- unleserlichen/falschen Labels
- sichtbarer interner Bild-/Szenennummer
- altem 2.5D-/3D-Look statt der freigegebenen Illustrationswelt
- drei oder mehr isolierten Objektportraits hintereinander
- nicht-leerem Remotion-Textoverlay
- irgendeinem von Remotion erzeugten sichtbaren Text
