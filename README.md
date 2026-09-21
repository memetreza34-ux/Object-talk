# Object-Talk

Produktionssystem für den YouTube-Kanal **Object-Talk / FoodSpricht**.

## Ziel

Normale Kanalvideos sind lange deutschsprachige YouTube-Erklärvideos über Ernährung, Gesundheit, menschlichen Körper und Biologie.

Normaler Produktionsstandard:

- mindestens **5:00 Minuten**
- 16:9 / 1920×1080 / 30 fps
- narrative Visuals aus generierten Standbildern
- hochwertige faceless 3D-Explainer-Bildwelt
- komplexe Vorgänge visuell einfach erklären
- wichtige biologische Strukturen verständlich darstellen
- wissenschaftlich prüfen
- keine unnötige Themenwiederholung

## Aktueller interner Pilot

Aktiv ist derzeit:

```text
youtube-videos/001-pilot-sauerstoff-im-blut/
```

Thema:

**Wie kommt Sauerstoff von der Lunge bis in deine Zellen?**

Dieser zweite Pilot ist absichtlich nur ungefähr **2–2,5 Minuten** lang. Er testet die Verbesserungen aus dem ersten Zucker-Pilot und ändert die 5-Minuten-Regel für normale Kanalvideos nicht.

Pilot 001 nutzt **28 echte Erklärbilder**. Ein neues Bild kommt nur, wenn sich Ort, Maßstab, Zustand, Prozess oder zentrale visuelle Aussage ändert.

## Was Pilot 001 zusätzlich testet

- Flow-Bilder möglichst **textfrei**
- Überschriften und Keywords kontrolliert in **Remotion** statt KI-Text im Bild
- feste visuelle Identität für **O₂, CO₂, rote Blutkörperchen und Hämoglobin**
- starke Maßstabswechsel von Mensch → Lunge → Alveole → Blut → Hämoglobin → Herz → Gewebe → Zelle → Mitochondrium
- Vollbild bleibt Hauptdarsteller; Text-Overlays nur gezielt
- keine Mascot-/Presenter-Figur

Selektive Overlays werden über:

```text
03_pipeline/overlay-plan.json
```

definiert.

Globale Overlay-Regeln:

```text
engine/PRESENTATION-OVERLAY-SYSTEM.md
```

## Repo-Gehirn

Neue Chats/Agenten sollen nicht von alter Chat-Erinnerung abhängig sein.

Vor Arbeit lesen:

1. `PROJECT_CONTRACT.md`
2. `PROJECT_STATE.md`
3. `AGENTS.md`
4. `config/channel.json`
5. `config/video.json`
6. `THEMEN-GEHIRN.md`
7. relevante `engine/*.md`
8. relevante `bildwelt/*.md`
9. aktuelles Video-Projekt

## Visuelles Kernprinzip

Der Kanal ist **kein Mascot-/Presenter-Format**.

Standard sind echte Erklärbilder:

- anatomische Cutaways
- transparente Körperansichten
- Prozessdarstellungen
- Organ-, Gewebe- und Zellvisualisierungen
- Mikro-/Makro-Übergänge
- Vorher-/Nachher- und Vergleichsbilder
- Ursache→Prozess→Folge-Darstellungen

Personifizierte Objekte sind nur erlaubt, wenn sie eine konkrete Erklärung wirklich verbessern.

## Bildrhythmus

Richtwerte:

- Hook: meist 2–4 Sekunden
- normale Erklärbilder: meist 4–6 Sekunden
- komplexe Mikroprozesse: oft 3–5 Sekunden
- ruhige Übersichten: meist 6–8 Sekunden
- über 8 Sekunden nur mit bewusstem Grund

Keine Füllbilder. Lange Standzeiten dürfen nicht nur mit Zoom/Pan kaschiert werden.

## Präsentation / Text

Die 3D-Welt bleibt bestehen; sie wird **nicht** in Anime-, Comic- oder Cartoon-Stil umgebaut.

Richtwert:

- ca. 65–75 % reine Vollbilder
- ca. 20–30 % kurze Überschrift/Keyword
- zusätzliche grafische Hilfen nur bei echtem Erklärwert

Wichtige Texte werden bevorzugt im Editor erzeugt, damit Rechtschreibung, Stil und Timing kontrollierbar bleiben.

## V2-Planung

Neue Projekte erhalten:

```text
05_info/mechanism-map.md
05_info/sentence-visual-plan.json
02_bildprompts/label-plan.json
02_bildprompts/image-review.json
04_export/quality-scorecard.md
04_export/postmortem.md
```

Ablauf:

```text
Recherche + Claims
→ Mechanism Map
→ Visual-First-Skript
→ Satz-Visual-Plan
→ semantische Szenen
→ Flow-Bilder
→ Einzelbild-Review ≥ 8/10
→ Voice + Worttimings
→ Remotion + selektive Overlays
→ Render
→ Qualitäts-Scorecard
→ Postmortem
```

Wissenschaftliche Sicherheit unter **8/10** ist ein harter Blocker.

## Style-Anker

`Bild_01` jedes Videos ist:

- Cover-/Hook-Frame
- erster Shot
- Master Style Frame der Episode

Flow erzeugt zuerst nur `Bild_01`. Erst nach akzeptiertem Bild_01 folgen die nächsten Bilder in 5er-Blöcken. Fehlerhafte Generationen werden gesammelt und am Ende im Recovery-Pass erneut erzeugt.

## Drei Phasen

### Phase 1 – ChatGPT

```text
Thema
→ Recherche
→ Claim-Check
→ Mechanism Map
→ finales script.txt
→ Satz-Visual-Plan
→ Szenenplan
→ Flow-Prompt
→ scene-map.json
→ overlay-plan.json
→ Metadaten
```

### Phase 2 – Nutzer + Voice-KI + Google Flow

```text
VOICEOVER-ZUM-KOPIEREN.txt → Voice-KI
GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt
→ nur Bild_01
→ Style-Freigabe
→ 5er-Blöcke
→ Einzelbild-Review
→ Recovery-Pass
→ Bilder-ZIP
```

### Phase 3 – Antigravity + Tools + Remotion

```text
rohes Audio
→ final-voiceover.wav
→ Flow-ZIP importieren
→ Assets validieren
→ faster-whisper
→ Script↔Audio-Ausrichtung
→ timeline.json
→ overlay-plan.json einlesen
→ Remotion
→ Render
→ Final-QA
→ Scorecard
→ Postmortem
```

## Aktueller Pilot – nächster Schritt

1. `youtube-videos/001-pilot-sauerstoff-im-blut/01_script/VOICEOVER-ZUM-KOPIEREN.txt` für die Voice verwenden.
2. `youtube-videos/001-pilot-sauerstoff-im-blut/02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt` in Flow geben.
3. Flow muss **zuerst nur `Bild_01`** erzeugen und danach stoppen.
4. Nach Stilfreigabe folgen `Bild_02` bis `Bild_28` in den festgelegten Blöcken.

## Test-QA

Normale Final-QA bleibt bei 300 Sekunden.

Nur beim dokumentierten Pilot 001:

```bash
python tools/qa_final.py \
  youtube-videos/001-pilot-sauerstoff-im-blut/04_export/fertiges-video/final-video.mp4 \
  youtube-videos/001-pilot-sauerstoff-im-blut/01_script/audio/final-voiceover.wav \
  --min-seconds 115
```

## Goldene Regel

**Nicht raten.** Wenn Script, Audio, Bildnummer, Szenengrenze oder wissenschaftliche Kernaussage nicht eindeutig ist, stoppt die technische Pipeline und der konkrete Fehler wird behoben.
