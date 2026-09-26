# Produktionsplan – Pilot 003 Muskelwachstum

## Ziel

Pipeline-Test mit den Verbesserungen aus den echten Render-Reviews.

Thema: **Wie wächst ein Muskel?**

Geplant:
- 35 eindeutige Bilder
- 16:9 / 1920×1080 / 30 fps
- Voice-Verarbeitung 1.10x
- lange TTS-Pausen vor Whisper/Timeline komprimieren
- kein Standbild über 7 Sekunden
- keine doppelten Bildassets

## 1. Script / Voice

`01_script/VOICEOVER-ZUM-KOPIEREN.txt` 1:1 in die Voice-KI übernehmen.

Der Einstieg folgt jetzt zwingend:

**Hook → Wendung → Payoff**

Pilot-003-Hook:

`Hast du dich schon mal gefragt, warum deine Muskeln durch Training überhaupt größer werden?`

Direkte Wendung:

`Das Überraschende: Sie wachsen nicht während der Wiederholung selbst – das Training setzt zuerst nur einen Reiz.`

Roh-Audio nach:
`01_script/audio/`

Phase 3 verarbeitet es mit `tools/prepare_audio.py --speed 1.10`.
`final-voiceover.wav` ist die einzige Timing-Quelle.

## 2. Google Flow

Kanonischer Prompt:
`02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt`

Style-Referenz-Prompt:
`02_bildprompts/STYLE-REFERENCE-PROMPT.txt`

Ablauf:
1. textfreie Episode-Style-Referenz erzeugen bzw. kanalweite textfreie Referenz nutzen
2. Bild_01 als Cover erzeugen
3. bis zu 3 Covervarianten erlaubt
4. Nutzer wählt genau 1 Cover
5. ungewählte Cover löschen/verwerfen
6. Bild_02–Bild_35 nur mit textfreier Referenz erzeugen
7. texttragendes Cover niemals als Follow-up-Referenz verwenden
8. jede normale Szene einzeln erzeugen und genau 1 finales Bild behalten
9. kein Bild zweimal verwenden
10. keine sichtbaren Bildnummern, Asset-IDs, Dateinamen oder Promptüberschriften
11. sichtbarer Text ausschließlich aus `label-plan.json`
12. Cover-Hook nach Bild_01 verboten
13. wenn Flow Text falsch schreibt: Bild in Flow korrigieren/regenerieren
14. kein späterer Remotion-Text-Fallback

## 3. Bildwelt

- moderne stilisierte 2.5D / Soft-3D Educational Illustration
- etwa 80 % animierte Illustration / 20 % Soft-3D-Tiefe
- kein Photorealismus / Medical-CGI
- hell und freundlich
- ein dominanter Lehrpunkt pro Bild
- ca. 20–35 % wichtiger Mechanismusbilder dürfen einen zusätzlichen sinnvollen Detailpunkt enthalten

## 4. Visuelle Abwechslung

- mindestens etwa 60 % der normalen Bilder zeigen Prozess, Beziehung, Ursache/Wirkung, Weg, Vergleich, Vorher/Nachher oder Kontext
- maximal zwei isolierte Einzelobjekt-Portraits hintereinander
- benachbarte Szenen unterscheiden sich in mindestens zwei Punkten: Maßstab, Layout, Hauptmotiv, Prozessrichtung, Kontext oder Visual-Typ
- ähnliche Muskelquerschnitt-/Zell-/Myofibrillenbilder nicht mehrfach fast identisch verwenden
- schwaches/zu leeres Bild in Flow verbessern, nicht mit Editor-Text retten

## 5. Inhaltliche Reise

`Widerstand → Spannung → Zell-Signal → Proteinsynthese → Aminosäuren → Myofibrillen → Querschnitt/Hypertrophie → Satellitenzellen → Ernährung/Erholung/Schlaf → Muskelkater-Mythos → Anpassung → Progression → Zusammenfassung`

Fachliche Leitplanken:
- Muskelwachstum nicht als reines „Mikroriss-Reparatur“-Modell darstellen
- Muskelkater ist kein verlässlicher Indikator für Wachstum
- Protein nicht als alleinige Ursache darstellen
- kein Supplement-, Mengen- oder Therapie-Rat

## 6. Remotion / Schnitt

Remotion darf nur:
- Audio
- Timing
- sanfte Push/Pull/Pan-Bewegungen
- Schnitte
- dezente nicht-textliche Übergänge
- Rendern

Remotion darf **keinen sichtbaren Text** erzeugen.

`03_pipeline/overlay-plan.json` ist deaktiviert und muss leer bleiben.

Weitere Schnittregeln:
- keine Standbild-Holds über 7 Sekunden
- meistens 3–6 Sekunden pro Bild
- keine künstlichen Pausen zur Laufzeitverlängerung
- harte saubere Schnitte als Standard
- keine aggressiven Ken-Burns-Effekte
- letzter Shot endet eng mit dem Voiceover

## 7. Finale Assets

Finale Bildfolge exakt:
`Bild_01.png` bis `Bild_35.png`

Keine Alternativen, keine FAIL-Versionen, kein v2/final2/copy/A/B/C.

`EPISODE_STYLE_REFERENCE.png` ist Referenzdatei und gehört NICHT in die nummerierte finale Bildfolge.

## 8. Erfolgskriterien

- starker neugiergetriebener Script-Hook
- Cover-Hook nur einmal am Anfang
- Remotion-Textoverlays = 0
- alle sichtbaren Texte korrekt aus Google Flow
- kein sichtbares `Bild_XX`
- keine doppelten Bilder
- nur ein Cover im finalen Set
- Bild_02+ mit textfreier Referenz erzeugt
- Voice 1.10x und keine langen TTS-Pausen
- 35 klar unterschiedliche Lernbeats
- Mechanismusbilder nicht zu leer
- ähnliche Nachbarszenen klar unterschiedlich
- Finale ist neue Zusammenfassung, nicht Wiederholung des Covers
