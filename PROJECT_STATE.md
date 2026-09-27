# Object-Talk – Project State

Letzte Aktualisierung: 27.09.2026

## Aktiver Produktionspilot

`youtube-videos/005-pilot-sauerstoff-zelle/`

Thema:
**Wie kommt Sauerstoff von der Lunge bis in eine einzelne Koerperzelle?**

## STATUS

Die neue kanalweite Bildwelt ist freigegeben:

**Clean Animated Biology Illustration**

Autoritativ:
- `bildwelt/BIOLOGY-ILLUSTRATION-WORLD.md`
- `bildwelt/FLOW-STYLE-BLOCK.txt`

## Pilot 005 – Zweck

Pilot 005 ist ein kurzer End-to-End-Test der neuen Bildwelt über mehrere biologische Maßstaebe:
- Lunge
- Lungenblaeschen
- Blutkapillare
- rotes Blutkoerperchen / Haemoglobin
- Herz / Kreislauf
- Koerperzelle
- Mitochondrium

## Harte Testvorgaben

- final maximal 2:00 Minuten
- Script: 250 Woerter
- erwartete finale Laufzeit ca. 1:25–1:50 bei Standard-Voice-Verarbeitung
- 22 eindeutige Bilder
- 16:9 / 1920×1080 / 30 fps
- Voice standardmaessig 1.10x
- kein Bild laenger als 7 Sekunden
- kein Bild doppelt verwenden

## Phase 1 Status

Vorbereitet:
- finales Script
- Voiceover-Zum-Kopieren
- Claim-Matrix
- Mechanism Map
- 22 semantische Szenen
- Sentence-Visual-Plan
- Label-Plan
- Google-Flow-Masterprompt
- Bild-QA-Template
- Testmodus mit harter 120-Sekunden-Obergrenze

## Bildwelt-Regeln fuer Pilot 005

- klare animierte Biologie-Illustration
- vereinfachte erkennbare Anatomie
- weiche organische Formen
- saubere Konturen
- weiche Farbverlaeufe und subtile Tiefe
- helle ruhige Hintergruende
- klare biologische Farben
- wenige wichtige Elemente pro Bild
- ein dominanter Lehrpunkt pro Bild
- normalerweise 0–3 kurze deutsche Labels
- unterschiedliche Kompositionen und Massstaebe
- keine alte 2.5D-/Soft-3D-/Premium-3D-Bildwelt

## Naechster Produktionsschritt

Phase 2:
1. Voice aus `01_script/VOICEOVER-ZUM-KOPIEREN.txt` erzeugen.
2. `Bild_01` bis `Bild_22` mit dem fertigen Flow-Prompt einzeln erzeugen.
3. Bilder gegen `image-review.json` und `label-plan.json` pruefen.
4. Danach Audio + Bilder in Phase 3 synchronisieren und final rendern.

## Pilot 004

`youtube-videos/004-pilot-muskelkater/` bleibt als vorheriger Test erhalten, ist aber nicht mehr der aktive Produktionspilot.
