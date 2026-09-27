# Produktionsplan – Pilot 006 Wundheilung

## Thema
**Was passiert in deinem Körper, wenn du dich schneidest?**

## Ziel
End-to-End-Test der **Clean Animated Biology Illustration** mit rein bildbasierter Remotion-Phase.

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
- intern exakt `Bild_01.png` bis `Bild_22.png` speichern
- **Bildnummern sind nur Dateinamen und dürfen niemals im Bild sichtbar sein**
- sichtbare biologische Labels nur aus `label-plan.json`
- keine sichtbaren Szenennummern, Dateinamen, Asset-IDs oder Prompttitel
- falsche Schrift/Zuordnung/interne Nummer im Bild = regenerieren
- keine Bildduplikate

## Remotion – nur Bilder, kein Text

Remotion erzeugt keinerlei sichtbaren Text.

Verboten:
- Zwischenüberschriften
- Key-Facts
- Summary-Zeilen
- Kapiteltexte
- Callouts
- Untertitel
- anatomische Labels
- sichtbare Bild-/Szenennummern

Remotion darf nur:
- Vollbild-Illustrationen anzeigen
- Audio einbinden
- Timing anwenden
- leichte Push/Pull/Pan-Bewegung
- schneiden
- dezente nicht-textliche Übergänge
- rendern

`03_pipeline/overlay-plan.json` bleibt deaktiviert und leer.

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
- 0 sichtbare Remotion-Textelemente
- 0 sichtbare Produktionsnummern/-IDs
- finaler Summary-Frame funktioniert rein visuell als klarer Abschluss
