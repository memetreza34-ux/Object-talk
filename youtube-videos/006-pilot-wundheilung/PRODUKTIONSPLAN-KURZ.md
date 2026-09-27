# Produktionsplan – Pilot 006 Wundheilung

## Thema
**Was passiert in deinem Körper, wenn du dich schneidest?**

## Ziel
Zweiter End-to-End-Test der neuen **Clean Animated Biology Illustration** plus selektiver Remotion-Präsentation.

## Umfang
- maximal 2:00 Minuten final
- ca. 213 Wörter Voiceover
- 22 eindeutige Bilder
- 16:9 / 1920×1080 / 30 fps
- Voice-Verarbeitung 1.10x
- Zielbereich ungefähr 1:20–1:55, abhängig vom TTS
- über 120 Sekunden = Hard FAIL

## Biologische Reise
Hautschnitt → beschädigtes Gefäß → Gefäßverengung → Blutplättchen → Fibrin → Gerinnsel → Immunzellen → Aufräumen → Fibroblast/Kollagen → neue Gefäße → Hautzellen → geschlossene Haut → Umbau/Narbe.

## Bildwelt
Autoritativ:
- `bildwelt/BIOLOGY-ILLUSTRATION-WORLD.md`
- `bildwelt/FLOW-STYLE-BLOCK.txt`

Pflicht:
- saubere animierte Biologie-Illustration
- vereinfachte erkennbare Anatomie
- helle ruhige Hintergründe
- wenige wichtige Elemente
- ein Hauptprozess pro Bild
- 1–3 kurze deutsche Labels, wenn sinnvoll
- keine alte 2.5D-/Premium-3D-/Medical-CGI-Welt

## Google Flow
- `02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt` verwenden
- jedes Bild einzeln erzeugen
- exakt `Bild_01` bis `Bild_22`
- sichtbare biologische Labels nur aus `label-plan.json`
- falsche Schrift/Zuordnung = regenerieren
- keine Bildduplikate

## Remotion-Präsentation
Vollbild-Illustration bleibt Standard.

Geplant sind nur:
- Szene 2: `1 · Blut stoppen`
- Szene 11: `2 · Aufräumen`
- Szene 14: `3 · Reparieren`
- Szene 22: `Stoppen → Aufräumen → Aufbauen → Verstärken`

Keine anatomischen Labels mit Remotion ergänzen. Keine dauerhaften Textleisten oder Rahmen.

## Audio / Timing
1. Voice aus `VOICEOVER-ZUM-KOPIEREN.txt` erzeugen.
2. `tools/prepare_audio.py --speed 1.10`.
3. finales `final-voiceover.wav` ist Master-Timeline.
4. Whisper-Wortzeiten aus finalem Audio.
5. keine Szene länger als 7 Sekunden; bei Bedarf echten Speech-Beat weiter teilen statt Bild zu duplizieren.

## Erfolgskriterien
- Video <= 120 Sekunden
- Hook sofort verständlich
- Wundheilung wissenschaftlich plausibel und einfach erklärt
- 22 unterschiedliche Illustrationen
- Bildwelt bleibt über Blut, Zellen, Haut und Gewebe konsistent
- keine überladenen Bilder
- Remotion-Text bleibt deutlich untergeordnet
- Kapitelüberschriften helfen der Orientierung
- finaler Summary-Frame funktioniert als klarer Abschluss
