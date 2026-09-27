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

Die Praesentationsregel ist verbindlich:
- **100 % Vollbild-Illustration**
- Remotion erzeugt **keinen sichtbaren Text**
- keine Zwischenueberschriften, Key-Facts, Summary-Zeilen, Kapiteltexte oder Callouts
- biologische Labels bleiben direkt in Google Flow
- interne Bild-/Szenennummern, Dateinamen und Asset-IDs duerfen niemals sichtbar sein

## Pilot 006 – Zweck

Pilot 006 testet die neue Bildwelt ueber mehrere biologische Motive:
- Hautquerschnitt
- kleines Blutgefaess
- Blutplaettchen
- Fibrin / Gerinnsel
- Immunzellen
- Fibroblast / Kollagen
- neue Blutgefaesse
- Hautzellen / Re-Epithelialisierung
- Gewebe-Umbau / Narbe

## Harte Testvorgaben

- final maximal 2:00 Minuten
- Script: ca. 213 Woerter
- bevorzugte Laufzeit ca. 1:20–1:55 bei Standard-Voice-Verarbeitung
- 22 eindeutige Bilder
- 16:9 / 1920×1080 / 30 fps
- Voice standardmaessig 1.10x
- kein Bild laenger als 7 Sekunden
- kein Bild doppelt verwenden
- 0 Remotion-Textelemente
- 0 sichtbare Produktions-IDs

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
- deaktivierter leerer Overlay-Plan
- Antigravity-/Phase-3-Prompt
- Testmodus mit harter 120-Sekunden-Obergrenze

## Praesentationssystem fuer Pilot 006

Remotion darf nur:
- Bilder vollformatig anzeigen
- Timing nach dem finalen Voiceover anwenden
- leichte Push-/Pull-/Pan-Bewegungen ausfuehren
- schneiden
- dezente nicht-textliche Uebergaenge verwenden
- Audio einbinden
- rendern

Remotion darf keinerlei sichtbaren Text erzeugen.

## Naechster Produktionsschritt

Phase 2:
1. Voice aus `01_script/VOICEOVER-ZUM-KOPIEREN.txt` erzeugen.
2. `Bild_01` bis `Bild_22` mit dem fertigen Flow-Prompt einzeln erzeugen.
3. Bei jedem Bild pruefen: Dateiname/Asset-ID nur intern; keine sichtbare Bild-/Szenennummer im Bild.
4. Bilder gegen `image-review.json` und `label-plan.json` pruefen.
5. Danach Audio + Bilder in Phase 3 synchronisieren und ohne Text-Overlays rendern.

## Fruehere Piloten

`005-pilot-sauerstoff-zelle` bleibt als erfolgreicher vorheriger Test erhalten.
`004-pilot-muskelkater` bleibt als aeltere Produktionshistorie erhalten.
