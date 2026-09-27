# Object-Talk – Project State

Letzte Aktualisierung: 27.09.2026

## Aktiver Produktionspilot

`youtube-videos/006-pilot-wundheilung/`

Thema:
**Was passiert in deinem Körper, wenn du dich schneidest?**

## STATUS

Die kanalweite Bildwelt ist freigegeben:

**Clean Animated Biology Illustration**

Autoritativ:
- `bildwelt/BIOLOGY-ILLUSTRATION-WORLD.md`
- `bildwelt/FLOW-STYLE-BLOCK.txt`

Die Präsentationsregel ist ebenfalls verbindlich:
- ca. 85–90 % Vollbild-Illustration
- maximal ca. 10–15 % selektive Remotion-Präsentation
- Remotion nur für wenige Zwischenüberschriften, Key-Facts oder Summarys
- biologische Labels bleiben in Google Flow

## Pilot 006 – Zweck

Pilot 006 testet die neue Bildwelt und das neue Präsentationssystem über mehrere biologische Motive:
- Hautquerschnitt
- kleines Blutgefäß
- Blutplättchen
- Fibrin / Gerinnsel
- Immunzellen
- Fibroblast / Kollagen
- neue Blutgefäße
- Hautzellen / Re-Epithelialisierung
- Gewebe-Umbau / Narbe

## Harte Testvorgaben

- final maximal 2:00 Minuten
- Script: ca. 213 Wörter
- bevorzugte Laufzeit ca. 1:20–1:55 bei Standard-Voice-Verarbeitung
- 22 eindeutige Bilder
- 16:9 / 1920×1080 / 30 fps
- Voice standardmäßig 1.10x
- kein Bild länger als 7 Sekunden
- kein Bild doppelt verwenden
- Overlay-Anteil maximal 15 % der Laufzeit

## Phase 1 Status

Vorbereitet:
- finales Script
- Voiceover-Zum-Kopieren
- Claim-Matrix mit medizinischen Quellen
- Mechanism Map
- 22 semantische Szenen
- Sentence-Visual-Plan
- Label-Plan
- Google-Flow-Prompt
- Google-Flow-Agent-Prompt
- Bild-QA-Template
- selektiver Remotion-Overlay-Plan
- Antigravity-/Phase-3-Prompt
- Testmodus mit harter 120-Sekunden-Obergrenze

## Geplante Remotion-Struktur

- Szene 2: `1 · Blut stoppen`
- Szene 11: `2 · Aufräumen`
- Szene 14: `3 · Reparieren`
- Szene 22: `Stoppen → Aufräumen → Aufbauen → Verstärken`

Alle übrigen Szenen bleiben reine Vollbild-Illustration mit höchstens dezenter Bildbewegung.

## Nächster Produktionsschritt

Phase 2:
1. Voice aus `01_script/VOICEOVER-ZUM-KOPIEREN.txt` erzeugen.
2. `Bild_01` bis `Bild_22` mit dem fertigen Flow-Prompt einzeln erzeugen.
3. Bilder gegen `image-review.json` und `label-plan.json` prüfen.
4. Danach Audio + Bilder in Phase 3 synchronisieren und mit dem selektiven Overlay-Plan rendern.

## Frühere Piloten

`005-pilot-sauerstoff-zelle` bleibt als erfolgreicher vorheriger Test erhalten.
`004-pilot-muskelkater` bleibt als ältere Produktionshistorie erhalten.
