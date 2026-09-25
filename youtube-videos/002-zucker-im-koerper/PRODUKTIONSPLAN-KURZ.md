# Produktionsplan – Pilot 002 Zucker

## Ziel

Neuer echter Pipeline-Test nach dem Sauerstoff-Postmortem.

Thema: **Was passiert mit Zucker in deinem Körper?**

Geplant:
- 35 eindeutige Bilder
- 16:9 / 1920×1080 / 30 fps
- Voiceover mit 352 Wörtern
- Voice-Verarbeitung standardmäßig 1.10x
- lange TTS-Pausen vor Whisper/Timeline komprimieren
- erwartete Endlänge ungefähr 2:05–2:25, abhängig vom Roh-TTS

## 1. Voice

`01_script/VOICEOVER-ZUM-KOPIEREN.txt` 1:1 in die Voice-KI übernehmen.

Roh-Audio nach:

`01_script/audio/`

Phase 3 verarbeitet es mit `tools/prepare_audio.py --speed 1.10`.

Das verarbeitete `final-voiceover.wav` ist die einzige Timing-Quelle.

## 2. Google Flow

Kanonischer Prompt:

`02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt`

Dauerhafte Regeln:

`engine/FLOW-AGENT-INSTRUCTIONS.md`

Ablauf:
1. Nur Bild_01 als Cover erzeugen.
2. Bis zu 3 klar verschiedene Covervarianten sind erlaubt.
3. Nutzer wählt genau 1 Cover.
4. Alle nicht gewählten Covervarianten löschen/verwerfen.
5. Gewähltes Bild_01 als echte visuelle Referenz für Bild_02–Bild_35 anhängen.
6. Jede normale Szene einzeln erzeugen und genau 1 finales Bild behalten.
7. Kein Bild zweimal verwenden.
8. Keine sichtbaren Bildnummern, Asset-IDs, Dateinamen oder Promptüberschriften.
9. Sichtbarer Text ausschließlich aus `label-plan.json`.

## 3. Bildwelt

- moderne stilisierte 2.5D / Soft-3D Educational Illustration
- etwa 80 % animierte Illustration / 20 % Soft-3D-Tiefe
- kein Photorealismus / Medical-CGI
- hell und freundlich
- eine dominante Aussage pro Bild
- wichtige Mechanismusbilder dürfen gezielt einen zusätzlichen sinnvollen Detailpunkt enthalten

Neue semantische Farben für diesen Pilot:
- Glukose = Türkis/Cyan mit warm-goldenem Akzent
- Insulin = Blau
- Glukagon = Violett
- Gefäße = Coral-Rot
- Leber/Pankreas/Darm = Peach/Coral/Orange
- Glykogen = Amber/Gold
- ATP = Gelb/Gold
- Fettzelle = Apricot/Gelb

## 4. Schnitt

- keine Standbild-Holds über 7 Sekunden
- meistens 3–6 Sekunden pro Bild
- keine künstlichen Pausen zur Laufzeitverlängerung
- harte saubere Schnitte als Standard
- leichte Push/Pull/Pan-Bewegungen
- keine aggressiven Ken-Burns-Effekte
- letzter Shot endet eng mit dem Voiceover

## 5. Finale Assets

Finale Bildfolge exakt:

`Bild_01.png` bis `Bild_35.png`

Keine Alternativen, keine FAIL-Versionen, kein v2/final2/copy/A/B/C.

## 6. Inhaltlicher Fokus

Reise:

`Nahrung → Mund/Magen → Dünndarm → Glukose → Blut → Pfortader/Leber → Bauchspeicheldrüse/Insulin → Zellaufnahme → ATP → Glykogen → längerfristiger Energieüberschuss/Fett → Glukagon → Leber gibt Glukose frei`

Bewusst keine Diabetes-/Therapieberatung und keine unnötig detaillierte Biochemie.

## 7. Erfolgskriterien

- kein sichtbares `Bild_XX`
- keine doppelten Bilder
- nur ein Cover im finalen Set
- Voice 1.10x und keine langen TTS-Pausen
- mehr visuelle Dichte als Pilot 001
- keine überladenen Textbilder
- 35 klar unterschiedliche Lernbeats
- Finale ist neue Zusammenfassung, nicht Wiederholung des Covers
