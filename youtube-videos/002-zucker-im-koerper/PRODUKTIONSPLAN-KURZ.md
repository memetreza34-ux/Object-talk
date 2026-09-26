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
1. Textfreie `STYLE_REFERENCE.png` anhaengen, falls vorhanden.
2. Falls sie fehlt, zuerst eine textfreie `EPISODE_STYLE_REFERENCE.png` erzeugen. Sie ist nur Produktionsreferenz und kein finales Szenenbild.
3. Danach nur Bild_01 als Cover erzeugen.
4. Bis zu 3 klar verschiedene Covervarianten sind erlaubt.
5. Nutzer wählt genau 1 Cover.
6. Alle nicht gewählten Covervarianten löschen/verwerfen.
7. **Bild_01 mit Titel NICHT als Referenz für Bild_02–Bild_35 verwenden.**
8. Für alle normalen Szenen ausschließlich die textfreie Style-Referenz anhängen.
9. Jede normale Szene einzeln erzeugen und genau 1 finales Bild behalten.
10. Kein Bild zweimal verwenden.
11. Keine sichtbaren Bildnummern, Asset-IDs, Dateinamen oder Promptüberschriften.
12. Sichtbarer Text ausschließlich aus `label-plan.json`.
13. Die Cover-Hook „So verarbeitet dein Körper Zucker“ ist nach Bild_01 vollständig verboten.

## 3. Bildwelt

- moderne stilisierte 2.5D / Soft-3D Educational Illustration
- etwa 80 % animierte Illustration / 20 % Soft-3D-Tiefe
- kein Photorealismus / Medical-CGI
- hell und freundlich
- eine dominante Aussage pro Bild
- etwa 20–35 % wichtiger Mechanismusbilder dürfen gezielt einen zusätzlichen sinnvollen Detailpunkt enthalten
- maximal zwei isolierte Einzelobjektbilder direkt hintereinander
- danach bevorzugt Prozess, Weg, Ursache/Wirkung, Vergleich oder Kontextwechsel
- ähnliche Übersichten nicht wiederholen; bei erneutem Thema Maßstab, Zustand, Richtung oder Zweck klar ändern

Semantische Farben für diesen Pilot:
- Glukose = Türkis/Cyan mit warm-goldenem Akzent
- Insulin = Blau
- Glukagon = Violett
- Gefäße = Coral-Rot
- Leber/Pankreas/Darm = Peach/Coral/Orange
- Glykogen = Amber/Gold
- ATP = Gelb/Gold
- Fettzelle = Apricot/Gelb

## 4. Informations- und Kapitelhinweise

Zusätzliche kurze Orientierung im Schnitt kommt aus:

`03_pipeline/overlay-plan.json`

Dort sind nur wenige einmalige Story-Beats geplant, z. B.:
- „Aufnahme im Dünndarm“
- „Jetzt kommt Insulin“
- „Glukose wird Energie“
- „Nutzen oder speichern“
- „Zwischen den Mahlzeiten“

Diese Hinweise dürfen die Cover-Hook nie wiederholen und keine Flow-Labels doppeln.

## 5. Schnitt

- keine Standbild-Holds über 7 Sekunden
- meistens 3–6 Sekunden pro Bild
- keine künstlichen Pausen zur Laufzeitverlängerung
- harte saubere Schnitte als Standard
- leichte Push/Pull/Pan-Bewegungen
- keine aggressiven Ken-Burns-Effekte
- letzter Shot endet eng mit dem Voiceover

## 6. Finale Assets

Finale Bildfolge exakt:

`Bild_01.png` bis `Bild_35.png`

Keine Alternativen, keine FAIL-Versionen, kein v2/final2/copy/A/B/C.
Textfreie Style-Referenzen liegen außerhalb dieses finalen nummerierten Sets.

## 7. Inhaltlicher Fokus

Reise:

`Nahrung → Mund/Magen → Dünndarm → Glukose → Blut → Pfortader/Leber → Bauchspeicheldrüse/Insulin → Zellaufnahme → ATP → Glykogen → längerfristiger Energieüberschuss/Fett → Glukagon → Leber gibt Glukose frei`

Bewusst keine Diabetes-/Therapieberatung und keine unnötig detaillierte Biochemie.

## 8. Erfolgskriterien

- Cover-Hook exakt einmal: nur Bild_01
- kein sichtbares `Bild_XX`
- keine doppelten Bilder
- nur ein Cover im finalen Set
- texttragendes Cover nie als Folge-Szenenreferenz
- Voice 1.10x und keine langen TTS-Pausen
- hohe, aber kontrollierte visuelle Dichte
- etwa 20–35 % Mechanismusbilder mit einem sinnvollen Zusatzdetail
- keine drei monotonen Einzelobjekt-Portraits am Stück
- keine überladenen Textbilder
- 35 klar unterschiedliche Lernbeats
- Bild_30 und Bild_33 visuell klar verschieden
- Finale ist neue Zusammenfassung, nicht Wiederholung des Covers
