# Object-Talk

Produktionssystem für den YouTube-Kanal **Object-Talk / FoodSpricht**.

## Ziel

Normale Kanalvideos sind lange deutschsprachige YouTube-Erklärvideos über:

- Ernährung
- Gesundheit
- menschlichen Körper
- Biologie

Normaler Produktionsstandard:

- mindestens **5:00 Minuten**
- 16:9 / 1920×1080 / 30 fps
- narrative Visuals aus generierten Standbildern
- hochwertige faceless 3D-Explainer-Bildwelt
- komplexe Vorgänge visuell einfach erklären
- wichtige biologische Strukturen knapp auf Deutsch beschriften
- wissenschaftlich prüfen
- keine unnötige Themenwiederholung

## Aktueller interner Pilot

Aktiv ist derzeit:

```text
youtube-videos/000-pilot-zucker-im-blut/
```

Thema:

**Was passiert mit Zucker nach einem süßen Snack?**

Dieser Pilot ist absichtlich nur ungefähr **2 Minuten** lang und testet die neue V2-Pipeline. Er ist über `05_info/test-mode.json` ausdrücklich als interner Test markiert und ändert die 5-Minuten-Regel für normale Kanalvideos nicht.

Der frühere Verdauungs-Pilot wurde auf Nutzerwunsch gelöscht.

## Repo-Gehirn

Neue Chats/Agenten sollen nicht von alter Chat-Erinnerung abhängig sein.

Vor Arbeit lesen:

1. `PROJECT_CONTRACT.md` – oberste dauerhafte Projektregeln
2. `PROJECT_STATE.md` – aktueller Arbeitsstand
3. `AGENTS.md` – Aufgaben und Phasengrenzen für Agenten
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
- Mikro-/Makro-Zooms
- Vorher-/Nachher- und Vergleichsbilder
- Ursache→Prozess→Folge-Darstellungen

Personifizierte Lebensmittel oder Object-Talk-Figuren sind nur optional und dürfen nur eingesetzt werden, wenn sie eine konkrete Erklärung wirklich verbessern.

Im aktuellen Zucker-Pilot wird bewusst **gar keine anthropomorphe Food-Sprecherfigur benötigt**.

## V2-Planung

Neue Projekte aus `_TEMPLATE` erhalten:

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
→ Label-Plan
→ Flow-Bilder
→ Einzelbild-Review ≥ 8/10
→ echtes Audio + Worttimings
→ Render
→ Qualitäts-Scorecard
→ Postmortem
```

Wissenschaftliche Sicherheit unter **8/10** ist ein harter Blocker.

Prüfen:

```bash
python tools/validate_planning_v2.py youtube-videos/THEMA
python tools/validate_planning_v2.py youtube-videos/THEMA --phase2
```

## Style-Anker

`Bild_01` jedes Videos ist:

- Cover-/Hook-Frame
- erster Shot
- Master Style Frame für diese Episode

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
→ semantischer Szenenplan
→ Label-Plan
→ Google-Flow-Prompt
→ scene-map.json
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
→ strikte Script↔Audio-Ausrichtung
→ word-timings.json
→ timeline.json
→ Remotion
→ Render
→ Final-QA
→ Scorecard
→ Postmortem
```

## Aktueller Pilot – nächster Schritt

1. `youtube-videos/000-pilot-zucker-im-blut/01_script/VOICEOVER-ZUM-KOPIEREN.txt` für die Voice verwenden.
2. `youtube-videos/000-pilot-zucker-im-blut/02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt` in Flow geben.
3. Flow muss **zuerst nur `Bild_01`** erzeugen und danach stoppen.
4. Nach Stilfreigabe folgen `Bild_02` bis `Bild_15`.

## Test-QA

Normale Final-QA bleibt bei 300 Sekunden.

Nur beim dokumentierten 2-Minuten-Pilot:

```bash
python tools/qa_final.py \
  youtube-videos/000-pilot-zucker-im-blut/04_export/fertiges-video/final-video.mp4 \
  youtube-videos/000-pilot-zucker-im-blut/01_script/audio/final-voiceover.wav \
  --min-seconds 105
```

## Goldene Regel

**Nicht raten.** Wenn Script, Audio, Bildnummer, Szenengrenze oder wissenschaftliche Kernaussage nicht eindeutig ist, stoppt die technische Pipeline und der konkrete Fehler wird behoben.
