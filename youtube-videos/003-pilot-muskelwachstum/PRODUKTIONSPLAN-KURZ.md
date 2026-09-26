# Produktionsplan – Pilot 003 Muskelwachstum

## Ziel

Neuer echter Pipeline-Test nach dem Review von Pilot 002.

Thema: **Wie wächst ein Muskel?**

Geplant:
- 35 eindeutige Bilder
- 16:9 / 1920×1080 / 30 fps
- ca. 329 Wörter Voiceover
- Voice-Verarbeitung 1.10x
- lange TTS-Pausen vor Whisper/Timeline komprimieren
- erwartete Endlänge ungefähr 2:05–2:30, abhängig vom Roh-TTS

## 1. Voice

`01_script/VOICEOVER-ZUM-KOPIEREN.txt` 1:1 in die Voice-KI übernehmen.

Roh-Audio nach:
`01_script/audio/`

Phase 3 verarbeitet es mit `tools/prepare_audio.py --speed 1.10`.
Das verarbeitete `final-voiceover.wav` ist die einzige Timing-Quelle.

## 2. Google Flow

Kanonischer Prompt:
`02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt`

Style-Referenz-Prompt:
`02_bildprompts/STYLE-REFERENCE-PROMPT.txt`

Ablauf:
1. Nur Bild_01 als Cover erzeugen.
2. Bis zu 3 klar verschiedene Covervarianten erlaubt.
3. Nutzer wählt genau 1 Cover.
4. Ungewählte Covervarianten löschen/verwerfen.
5. Danach eine **textfreie** `EPISODE_STYLE_REFERENCE.png` erzeugen.
6. Bild_02–Bild_35 ausschließlich mit dieser textfreien Referenz erzeugen.
7. Das texttragende Cover niemals als Follow-up-Referenz anhängen.
8. Jede normale Szene einzeln erzeugen und genau 1 finales Bild behalten.
9. Kein Bild zweimal verwenden.
10. Keine sichtbaren Bildnummern, Asset-IDs, Dateinamen oder Promptüberschriften.
11. Sichtbarer Text ausschließlich aus `label-plan.json`.
12. Die Cover-Hook **„So wächst dein Muskel“** darf nach Bild_01 niemals wieder sichtbar sein.

## 3. Bildwelt

- moderne stilisierte 2.5D / Soft-3D Educational Illustration
- etwa 80 % animierte Illustration / 20 % Soft-3D-Tiefe
- kein Photorealismus / Medical-CGI
- hell und freundlich
- ein dominanter Lehrpunkt pro Bild
- ca. 20–35 % wichtiger Mechanismusbilder dürfen einen zusätzlichen sinnvollen Detailpunkt enthalten
- maximal zwei isolierte Einzelobjekt-Portraits hintereinander

Semantische Farben:
- Muskel/Muskelfaser = Coral / Salmon / Rot-Orange
- Spannung = warmes Orange-Rot
- Zell-Signale = Cyan / Blau
- Aminosäuren = Türkis / Cyan
- Proteinaufbau = Gold
- Myofibrillen = tieferes Rot / Burgunder
- Erholung = Soft-Blau / Teal
- Progression = Gold / Orange
- Hintergrund = Creme / Beige / helles Blau

## 4. Inhaltliche Reise

`Widerstand → Spannung → Zell-Signal → Proteinsynthese → Aminosäuren → Myofibrillen → Querschnitt/Hypertrophie → Satellitenzellen → Ernährung/Erholung/Schlaf → Muskelkater-Mythos → Anpassung → Progression → Zusammenfassung`

Wichtige fachliche Leitplanken:
- Muskelwachstum nicht als reines „Mikroriss-Reparatur“-Modell darstellen.
- Muskelkater ist kein verlässlicher Indikator für Wachstum.
- Protein nicht als alleinige Ursache darstellen.
- kein Supplement-, Mengen- oder Therapie-Rat.

## 5. Schnitt

- keine Standbild-Holds über 7 Sekunden
- meistens 3–6 Sekunden pro Bild
- keine künstlichen Pausen zur Laufzeitverlängerung
- harte saubere Schnitte als Standard
- leichte Push/Pull/Pan-Bewegungen
- keine aggressiven Ken-Burns-Effekte
- letzter Shot endet eng mit dem Voiceover
- Kapiteloverlays nur aus `03_pipeline/overlay-plan.json`, jede Formulierung maximal einmal

## 6. Finale Assets

Finale Bildfolge exakt:
`Bild_01.png` bis `Bild_35.png`

Keine Alternativen, keine FAIL-Versionen, kein v2/final2/copy/A/B/C.

Zusätzlich für die Produktion:
- `EPISODE_STYLE_REFERENCE.png` ist eine Referenzdatei und gehört NICHT in die nummerierte finale Bildfolge.

## 7. Erfolgskriterien

- Cover-Hook nur einmal am Anfang
- kein sichtbares `Bild_XX`
- keine doppelten Bilder
- nur ein Cover im finalen Set
- Bild_02+ wirklich mit textfreier Referenz erzeugt
- Voice 1.10x und keine langen TTS-Pausen
- mindestens 35 klar unterschiedliche Lernbeats
- Mechanismusbilder nicht zu leer
- ähnliche Nachbarszenen klar unterschiedlich
- Finale ist neue Zusammenfassung, nicht Wiederholung des Covers
