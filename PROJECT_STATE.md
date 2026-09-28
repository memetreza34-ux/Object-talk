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
- `engine/VISIBLE-TEXT-STANDARD.md`

## Neue harte Bild-/Textregeln

Seit 28.09.2026 gilt zusaetzlich verbindlich:

- **Cover = genau ein sichtbarer Textblock, nur Titel/Hook**
- keine Anatomie-Labels, Unterzeile oder Zusatzinfo auf dem Cover
- normale Bilder: **0–2 Labels, maximal 2**
- Label bevorzugt 1–2 Woerter, maximal 3 Woerter
- wenn ein Bild ohne Label klar ist: **kein Label**
- heller Hintergrund → dunkle Schrift
- dunkler Hintergrund → helle Schrift
- schwacher Kontrast = FAIL / neu generieren
- eine Hauptidee / ein Hauptprozess pro Bild
- bevorzugt 2–4 zentrale sichtbare Elemente
- wenn ein Frame zu viel Inhalt braucht: Information weglassen oder **mehr Bilder planen**
- keine dekorativen Anfuehrungszeichen um Labels

Die Präsentationsregel bleibt verbindlich:
- **100 % Vollbild-Illustration**
- Remotion erzeugt **keinen sichtbaren Text**
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

Der Pilot wurde nach Sichtung eines ersten Renders nochmals vereinfacht:
- Cover title-only
- deutlich weniger Labels
- stärkere Kontrastregeln
- mehrere selbsterklärende Bilder jetzt komplett ohne Text

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
- Cover nur Titel
- maximal 2 Labels pro normalem Bild
- Textkontrast muss PASS sein
- Informationsdichte muss PASS sein

## Phase 1 Status

Vorbereitet / aktualisiert:
- finales Script
- Voiceover-Zum-Kopieren
- Claim-Matrix
- Mechanism Map
- 20 semantische Szenen
- Sentence-Visual-Plan
- vereinfachter Label-Plan
- überarbeiteter Google-Flow-Prompt
- überarbeiteter Google-Flow-Agent-Prompt
- Bild-QA mit Kontrast-/Dichte-Gates
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
2. Die 20 Flow-Bilder mit dem **überarbeiteten** `02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt` einzeln erzeugen.
3. Cover prüfen: exakt nur `Warum Gänsehaut?`, kein weiterer Text.
4. Bei jedem normalen Bild prüfen: max. 2 Labels, hoher Kontrast, keine unnötigen Infos.
5. Bei jedem Bild prüfen: Dateiname/Asset-ID nur intern; keine sichtbare Bild-/Szenennummer.
6. Bilder gegen `image-review.json` und `label-plan.json` prüfen.
7. Danach Audio + Bilder in Phase 3 synchronisieren und ohne Text-Overlays rendern.

## Frühere Piloten

`006-pilot-wundheilung` bleibt als vorheriger Test erhalten.
`005-pilot-sauerstoff-zelle` bleibt als früherer Test erhalten.
`004-pilot-muskelkater` bleibt als ältere Produktionshistorie erhalten.
