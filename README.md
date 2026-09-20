# Object-Talk

Produktionssystem für den YouTube-Kanal **Object-Talk / FoodSpricht**.

## Ziel

Wir produzieren lange deutschsprachige YouTube-Erklärvideos über:

- Ernährung
- Gesundheit
- menschlichen Körper
- Biologie

Jedes Video:

- mindestens **5:00 Minuten**
- 16:9 / 1920×1080 / 30 fps
- narrative Visuals ausschließlich aus generierten Standbildern
- hochwertige faceless 3D-Explainer-Bildwelt
- komplexe Vorgänge visuell einfach erklären
- wichtige biologische Strukturen knapp auf Deutsch beschriften
- wissenschaftlich prüfen
- keine unnötige Themenwiederholung

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

Alle Bilder müssen wie dieselbe hochwertige semi-realistische 3D-Erklärserie wirken.

## Style-Anker

`Bild_01` jedes Videos ist:

- Cover-/Hook-Frame
- erster Shot
- Master Style Frame für diese Episode

Nach erfolgreicher Erstellung wird `Bild_01` bei allen weiteren Flow-Generierungen als Style-/Continuity-Referenz verwendet, soweit technisch möglich.

Zusätzlich kann langfristig eine kanalweite Referenz existieren:

```text
assets/channel/STYLE_REFERENCE.png
```

Dann gilt:

```text
STYLE_REFERENCE.png = langfristige Kanal-DNA
Bild_01.png = Episode-/Continuity-Referenz
```

Siehe `engine/STYLE-REFERENCE-SYSTEM.md` und `engine/FLOW-PRODUCTION-STANDARD.md`.

## Flow-Produktion

Google Flow arbeitet nicht mehr als ein großer Durchlauf.

```text
zuerst nur Bild_01
→ Bild_01 prüfen und als Master Style Frame akzeptieren
→ danach Bilder in 5er-Blöcken
→ innerhalb jedes Blocks jedes Bild einzeln
→ Fehlernummern sammeln
→ am Ende Recovery-Pass
→ erst bei lückenlosem PASS-Bildsatz ZIP erstellen
```

Ein einzelner Flow-Generierungsfehler beendet also nicht mehr automatisch die gesamte Bildproduktion.

## Themen-Gedächtnis

Vor jeder Produktion muss `THEMEN-GEHIRN.md` geprüft werden.

Ein neues Video darf keinen bereits behandelten Kernmechanismus nur unter einem anderen Titel wiederholen.

## Drei Phasen

### Phase 1 – ChatGPT

```text
Thema
→ Recherche
→ Claim-Check
→ finales script.txt
→ semantischer Szenenplan
→ Google-Flow-Prompt
→ scene-map.json
→ YouTube-Metadaten
```

Phase 1 entscheidet **was** zu welchem Sprachabschnitt gehört, aber keine finalen Sekundenwerte.

### Phase 2 – Nutzer + Voice-KI + Google Flow

```text
VOICEOVER-ZUM-KOPIEREN.txt → Voice-KI → rohe Audiodatei
GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt
→ nur Bild_01
→ Master Style Frame
→ 5er-Blöcke
→ Recovery-Pass
→ Bilder-ZIP
```

### Phase 3 – Antigravity + Tools + Remotion

```text
rohes Audio
→ final-voiceover.wav
→ Flow-ZIP sicher importieren
→ Bilder validieren
→ faster-whisper
→ strikte Script↔Audio-Ausrichtung
→ word-timings.json
→ exakte speech_section-Zuordnung
→ timeline.json
→ feste Remotion-Runtime
→ Render
→ Final-QA
```

Komplette Vorbereitung:

```bash
python -m pip install -r tools/requirements.txt
python tools/prepare_phase3.py youtube-videos/THEMA
```

## Repository-Bereiche

```text
PROJECT_CONTRACT.md
PROJECT_STATE.md
AGENTS.md
THEMEN-GEHIRN.md
config/
assets/channel/
bildwelt/
engine/
tools/
renderer/
youtube-videos/
```

## Engine

Wichtige globale Regeln:

- `engine/PRODUKTIONSREGELN.md`
- `engine/FLOW-PRODUCTION-STANDARD.md`
- `engine/SCRIPT-STANDARD.md`
- `engine/AUDIO-REGELN.md`
- `engine/SYNC-WHISPER.md`
- `engine/STYLE-REFERENCE-SYSTEM.md`
- `engine/FACT-CHECK-STANDARD.md`
- `engine/PHASE-GATES.md`
- `engine/VISUAL-QUALITY-GATE.md`

## Tools

Unter anderem:

- `create_video.py` – neues Projekt aus Template
- `validate_phase1.py` – vollständige semantische Script-Abdeckung prüfen
- `prepare_audio.py` – kanonisches finales Audio
- `import_flow_zip.py` – sichere Bildübernahme nach expliziten Nummern
- `validate_assets.py` – technische Bildprüfung
- `transcribe_audio.py` – faster-whisper + strikte Script-Ausrichtung
- `build_timeline.py` – Szenen auf echte Wortzeiten mappen
- `build_renderer_runtime.py` – feste Remotion-Runtime vorbereiten
- `prepare_phase3.py` – komplette Phase-3-Vorbereitung
- `qa_final.py` – finaler technischer Video-Check

## Goldene Regel

**Nicht raten.** Wenn Script, Audio, Bildnummer, Szenengrenze oder wissenschaftliche Kernaussage nicht eindeutig ist, stoppt die technische Pipeline und der konkrete Fehler wird behoben.

Ein einzelner Flow-Generierungsfehler wird dagegen über Fehlerliste + Recovery-Pass behandelt.
