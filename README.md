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
- viraler Object-Talk-Look + verständliche Inside-the-Body-Biologie
- einheitliche semi-realistische 3D-Animationswelt
- wichtige biologische Strukturen knapp auf Deutsch beschriftet
- wissenschaftlich geprüft
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

### 1. Viral Object-Talk

Sprechende Lebensmittel/Objekte mit großen Augen, klarer Mimik und starker Persönlichkeit.

### 2. Inside-the-Body

Verständliche 3D-Darstellungen von Organen, Blut, Zellen, Nervensystem und biologischen Prozessen.

Beide Ebenen müssen wie dieselbe Animationsserie wirken.

Nach finaler Nutzerfreigabe wird ein dauerhafter Style Anchor verwendet:

```text
assets/channel/STYLE_REFERENCE.png
```

Siehe `engine/STYLE-REFERENCE-SYSTEM.md`.

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
script.txt → Voice-KI → rohe Audiodatei
Google-Flow-Prompt → Bild_01 → Bild_02 → ... → Bilder-ZIP
```

`Bild_01` ist immer Cover-/Hook-Szene und erster Shot.

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

**Nicht raten.** Wenn Script, Audio, Bildnummer, Szenengrenze oder wissenschaftliche Kernaussage nicht eindeutig ist, stoppt die Pipeline und der konkrete Fehler wird behoben.
