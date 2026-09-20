# Object-Talk – Project State

Letzte Aktualisierung: 20.09.2026

## Aktueller Stand

Die Longform-Grundarchitektur ist jetzt vollständig genug für einen echten End-to-End-Piloten.

Vorhanden:

- `PROJECT_CONTRACT.md` als oberste dauerhafte Projektregel
- `AGENTS.md` als Bootstrap für neue Chats/Agenten
- maschinenlesbare `config/channel.json` und `config/video.json`
- `THEMEN-GEHIRN.md` gegen Themenwiederholungen
- erste Fach-Bildwelt `bildwelt/gehirn.md`
- globales Style-Reference-System
- Ordner für freigegebene Character References
- YouTube-Projektvorlage
- 3-Phasen-Workflow mit harten Phase-Gates
- wissenschaftlicher Fact-Check-Standard + Claim-Matrix
- semantische Phase-1-Szenen statt automatischem Satz-für-Satz-Schnitt
- vollständige `speech_section` pro Szene
- Google-Flow-Agent-Prompt mit Einzelbild-QA
- sichere ZIP-Übernahme ausschließlich nach Bildnummern
- technische Bildvalidierung
- kanonische Audioaufbereitung vor Whisper
- `faster-whisper` mit Wort-Zeitstempeln
- strikte vollständige Script↔Audio-Ausrichtung
- exakte Scene-Map→Timeline-Zuordnung ohne Fuzzy-Fallback
- feste wiederverwendbare Remotion-Runtime
- ein Befehl für die Phase-3-Vorbereitung
- finale technische Video-QA + Renderbericht

## Technischer Fast Path

Nach Phase 2:

```bash
python -m pip install -r tools/requirements.txt
python tools/prepare_phase3.py youtube-videos/THEMA
```

Danach:

```bash
cd renderer
npm install
npm run studio
npm run render -- ../youtube-videos/THEMA/04_export/fertiges-video/final-video.mp4
```

Finale QA:

```bash
python tools/qa_final.py \
  youtube-videos/THEMA/04_export/fertiges-video/final-video.mp4 \
  youtube-videos/THEMA/01_script/audio/final-voiceover.wav
```

## Noch vom Nutzer zu entscheiden / bereitzustellen

### 1. Finale STYLE_REFERENCE

Noch fehlt die dauerhaft akzeptierte echte Kanalreferenzdatei:

```text
assets/channel/STYLE_REFERENCE.png
```

Sie wird erst gespeichert, wenn der Nutzer einen finalen Object-Talk-/Inside-the-Body-Look ausdrücklich akzeptiert.

Bis dahin gelten die schriftlichen Bildweltregeln, aber der Kanalstil wird nicht als endgültig gelockt bezeichnet.

### 2. Finale Kanalstimme

Die konkrete Voice-KI bzw. Stimme ist noch nicht dauerhaft festgelegt.

Der technische Audiostandard ist davon unabhängig fertig. Sobald eine Stimme im Pilot überzeugt, kann sie als Kanalstimme festgeschrieben werden.

## Nächster Produktionsmeilenstein

**Video 001 vollständig end-to-end produzieren.**

```text
Thema
→ Recherche + Claim-Matrix
→ finales Script
→ semantische Szenen
→ Phase-1-PASS
→ Voice + Flow-Bilder
→ Phase-2-PASS
→ Whisper + strikte Script-Ausrichtung
→ Timeline
→ Remotion
→ Final-QA
→ Export
```

Erst der echte Pilot zeigt, ob Bildrhythmus, Voice, Motion-Stärke und Label-Lesbarkeit in der Praxis optimal sind. Diese vier Dinge sollen danach feinjustiert werden, statt vorab weiter theoretisch überoptimiert zu werden.
