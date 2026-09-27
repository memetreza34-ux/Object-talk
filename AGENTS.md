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
4. 1–3 Labels
5. kurze Negativregel

Keine langen Style-Romane in jedem Szenenprompt.

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
- nach dem Szenenplan wenige sinnvolle Remotion-Praesentationspunkte planen

## Phase 2 – Google Flow

- jedes Bild einzeln erzeugen
- kanonischen Styleblock verwenden
- biologische Labels direkt im Bild erzeugen
- falsche Labels/Schreibweise korrigieren oder regenerieren
- pro finaler Bildnummer genau ein akzeptiertes Asset behalten
- keine alte Pilot-Bildwelt als Referenz verwenden

## Phase 3 – Editor / Antigravity / Remotion

Grundsatz:
**Vollbild-Illustration bleibt Hauptdarsteller. Remotion strukturiert nur selektiv.**

Ziel:
- ca. 85–90 % reine Vollbild-Illustration
- maximal ca. 10–15 % selektive Praesentations-Overlays

Remotion ist fuer:
- Audio
- Timing
- leichte Zoom-/Pan-Bewegungen
- Schnitte
- dezente Uebergaenge
- wenige Zwischenueberschriften
- wenige Key-Facts
- optionale Summary-/Prozesszeile
- Rendering

Remotion-Text:
- nur Deutsch
- normalerweise 2–6 Woerter
- pro Szene maximal ein Overlay
- keine ganzen Voice-over-Saetze
- keine biologischen Flow-Labels ersetzen
- keine dauerhaften Rahmen/Seitenleisten/PowerPoint-Layouts
- Zwischenueberschrift bevorzugt kurz ueber der bereits sichtbaren naechsten Illustration

Fuer ca. 2 Minuten normalerweise 2–3 Zwischenueberschriften plus optional 1 Key-Fact/Summary.

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
- altem 2.5D-/3D-Look statt der freigegebenen Illustrationswelt
- drei oder mehr isolierten Objektportraits hintereinander
- zu vielen Remotion-Texten
- dauerhafter UI-/PowerPoint-Praesentation statt Vollbild-Illustration
