# Produktionsplan – Pilot 005 Sauerstoff bis zur Zelle

## Thema
**Wie kommt Sauerstoff von der Lunge bis in eine einzelne Körperzelle?**

## Zweck
Erster kompletter Kurzpilot, der die neue **Clean Animated Biology Illustration** über mehrere biologische Ebenen testet:
- Lunge
- Lungenbläschen
- Blutgefäß
- rote Blutkörperchen / Hämoglobin
- Herz / Kreislauf
- Körperzelle
- Mitochondrium

## Harte Laufzeit
**Maximal 2:00 Minuten final.**

Planung:
- Script: 250 Wörter
- Voice: standardmäßig 1.10x
- Zielbereich final: ca. 1:25–1:50
- absolute Obergrenze: 2:00
- kein künstliches Strecken

## Bilder
- 22 eindeutige Bilder
- 16:9 / 1920×1080 Ziel
- überwiegend 4–6 Sekunden pro Bild
- kein Bild doppelt verwenden
- kein Bild länger als 7 Sekunden
- bei echter Voice-Timing-Abweichung Szenengrenzen anhand Whisper anpassen, aber keine Laufzeit über 2:00 erzeugen

## Bildwelt
Autoritativ:
- `bildwelt/BIOLOGY-ILLUSTRATION-WORLD.md`
- `bildwelt/FLOW-STYLE-BLOCK.txt`

Kurz:
- klare animierte Biologie-Illustration
- vereinfachte erkennbare Anatomie
- weiche organische Formen
- saubere Konturen
- weiche Verläufe und subtile Tiefe
- helle ruhige Hintergründe
- wenige wichtige Elemente
- 1 dominanter Prozess pro Bild
- 0–3 kurze deutsche Labels
- keine alte 2.5D-/Soft-3D-/Premium-3D-Bildwelt

## Phase 1
Fertig vorbereitet:
- `01_script/script.txt`
- `01_script/VOICEOVER-ZUM-KOPIEREN.txt`
- `05_info/claim-matrix.md`
- `05_info/mechanism-map.md`
- `05_info/phase1-scenes.json`
- `05_info/sentence-visual-plan.json`
- `02_bildprompts/label-plan.json`
- `02_bildprompts/Google-Flow-Agent-Prompt.md`
- `02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt`

## Phase 2
1. Voice aus `VOICEOVER-ZUM-KOPIEREN.txt` erzeugen.
2. Rohvoice später mit `prepare_audio.py --speed 1.10` kanonisieren.
3. In Google Flow `Bild_01` bis `Bild_22` einzeln erzeugen.
4. Pro Bild nur die freigegebenen deutschen Labels verwenden.
5. Jedes echte Bild auf Verständlichkeit, wissenschaftliche Plausibilität, Beschriftung und Stilkontinuität prüfen.
6. Nur ein finales Asset pro Bildnummer behalten.

## Phase 3
- finales Audio → Whisper → Worttimings
- Bilder exakt an Sprachabschnitte anpassen
- Remotion nur für Schnitt, Audio und dezente Push/Pan-Bewegung
- keine zusätzlichen Textoverlays
- finaler Render 1920×1080 / 30 fps
- FAIL, wenn Endlänge > 2:00

## Erfolgskriterien
- Zuschauer versteht den Weg: Lunge → Blut → Herz → Gewebe → Zelle → Mitochondrium
- alle Ebenen sehen wie dieselbe Illustrationswelt aus
- Bilder bleiben einfach und anschaulich
- keine überladenen Infografiken
- deutsche Labels korrekt
- wissenschaftliche Kernaussagen >= 8/10
- finaler Render maximal 120 Sekunden