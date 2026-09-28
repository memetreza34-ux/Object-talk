# Object-Talk – Project State

Letzte Aktualisierung: 28.09.2026

## Aktiver Produktionspilot

`youtube-videos/007-pilot-gaensehaut/`

Thema:
**Warum bekommst du Gänsehaut?**

## STATUS

Die kanalweite Bildwelt ist freigegeben:

**Clean Animated Biology Illustration**

Autoritativ:
- `bildwelt/BIOLOGY-ILLUSTRATION-WORLD.md`
- `bildwelt/FLOW-STYLE-BLOCK.txt`

Die Präsentationsregel ist verbindlich:
- **100 % Vollbild-Illustration**
- Remotion erzeugt **keinen sichtbaren Text**
- keine Zwischenüberschriften, Key-Facts, Summary-Zeilen, Kapiteltexte oder Callouts
- biologische Labels bleiben direkt in Google Flow
- interne Bild-/Szenennummern, Dateinamen und Asset-IDs dürfen niemals sichtbar sein

## Pilot 007 – Zweck

Pilot 007 testet die Bildwelt über:
- menschliche Hautoberfläche
- Hautquerschnitt
- Temperaturfühler / sensorischen Reiz
- Nervensignal
- Gehirn als vereinfachten Steuerkontext
- sympathisches Nervensystem
- Haarfollikel
- Haaraufrichtemuskel
- Tierfell / Luftschicht
- Kälte und starke Gefühle als unterschiedliche Auslöser

## Harte Testvorgaben

- final maximal 2:00 Minuten
- Script: ca. 190 Wörter
- bevorzugte Laufzeit ca. 1:20–1:55 bei Standard-Voice-Verarbeitung
- 20 eindeutige Bilder
- 16:9 / 1920×1080 / 30 fps
- Voice standardmäßig 1.10x
- kein Bild länger als 7 Sekunden
- kein Bild doppelt verwenden
- 0 Remotion-Textelemente
- 0 sichtbare Produktions-IDs

## Phase 1 Status

Vorbereitet:
- finales Script
- Voiceover-Zum-Kopieren
- Claim-Matrix
- Mechanism Map
- 20 semantische Szenen
- Sentence-Visual-Plan
- Label-Plan
- Google-Flow-Prompt
- Google-Flow-Agent-Prompt
- Bild-QA-Template
- deaktivierter leerer Overlay-Plan
- Antigravity-/Phase-3-Prompt
- Testmodus mit harter 120-Sekunden-Obergrenze

## Präsentationssystem für Pilot 007

Remotion darf nur:
- Bilder vollformatig anzeigen
- Timing nach dem finalen Voiceover anwenden
- leichte Push-/Pull-/Pan-Bewegungen ausführen
- schneiden
- dezente nicht-textliche Übergänge verwenden
- Audio einbinden
- rendern

Remotion darf keinerlei sichtbaren Text erzeugen.

## Nächster Produktionsschritt

Phase 2:
1. Voice aus `01_script/VOICEOVER-ZUM-KOPIEREN.txt` erzeugen.
2. Die 20 Flow-Bilder mit `02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt` einzeln erzeugen.
3. Bei jedem Bild prüfen: Dateiname/Asset-ID nur intern; keine sichtbare Bild-/Szenennummer im Bild.
4. Bilder gegen `image-review.json` und `label-plan.json` prüfen.
5. Danach Audio + Bilder in Phase 3 synchronisieren und ohne Text-Overlays rendern.

## Frühere Piloten

`006-pilot-wundheilung` bleibt als vorheriger Test erhalten.
`005-pilot-sauerstoff-zelle` bleibt als früherer Test erhalten.
`004-pilot-muskelkater` bleibt als ältere Produktionshistorie erhalten.
