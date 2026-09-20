# Object-Talk – Project State

Letzte Aktualisierung: 20.09.2026

## Aktueller Stand

Die Longform-Grundarchitektur ist vollständig genug für den ersten echten End-to-End-Piloten.

Zusätzlich ist jetzt **Video 001 – „Was passiert mit deinem Essen im Körper?“** in Phase 1 vollständig vorbereitet.

Vorhanden:

- `PROJECT_CONTRACT.md` als oberste dauerhafte Projektregel
- `AGENTS.md` als Bootstrap für neue Chats/Agenten
- maschinenlesbare `config/channel.json` und `config/video.json`
- `THEMEN-GEHIRN.md` gegen Themenwiederholungen
- `engine/THEMEN-STRATEGIE.md` für systematische Longform-Themenauswahl
- `engine/SCRIPT-STANDARD.md` für Hook, Einleitung, Hauptteil, rhetorische Mittel, Schluss und Visual-First-Scriptwriting
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
- deterministische Erzeugung der `scene-map.json` aus Phase 1
- exakte Scene-Map→Timeline-Zuordnung ohne Fuzzy-Fallback
- feste wiederverwendbare Remotion-Runtime
- ein Befehl für die Phase-3-Vorbereitung
- finale technische Video-QA + Renderbericht

## Video 001 – Stand

Projekt:

```text
youtube-videos/001-was-passiert-mit-essen-im-koerper/
```

Phase 1 enthält:

- recherchiertes Thema
- Claim-Matrix
- finales Voiceover-Skript
- 36 semantische Bildszenen
- exakte Sprachabschnitte pro Szene
- vollständigen Google-Flow-Agent-Prompt für `Bild_01` bis `Bild_36`
- menschenlesbare Bild↔Skript-Pipeline
- Antigravity-Phase-3-Anweisung
- YouTube-Titel, Beschreibung und 5 Hashtags

Nächster Schritt des Nutzers:

1. `01_script/script.txt` 1:1 in die eigene Voice-KI geben.
2. finale Audio-Datei in `01_script/audio/` legen.
3. `02_bildprompts/Google-Flow-Agent-Prompt.md` vollständig in Google Flow verwenden.
4. finale ZIP mit `Bild_01.png` bis `Bild_36.png` in `02_bildprompts/bilder-zip/` legen.

Danach kann Phase 3 automatisch vorbereitet werden.

## Technischer Fast Path

Nach Phase 2:

```bash
python -m pip install -r tools/requirements.txt
python tools/prepare_phase3.py youtube-videos/001-was-passiert-mit-essen-im-koerper
```

Danach:

```bash
cd renderer
npm install
npm run studio
npm run render -- ../youtube-videos/001-was-passiert-mit-essen-im-koerper/04_export/fertiges-video/final-video.mp4
```

Finale QA vom Repo-Root:

```bash
python tools/qa_final.py \
  youtube-videos/001-was-passiert-mit-essen-im-koerper/04_export/fertiges-video/final-video.mp4 \
  youtube-videos/001-was-passiert-mit-essen-im-koerper/01_script/audio/final-voiceover.wav
```

## Noch vom Nutzer bereitzustellen

### 1. Finale Voice

Die konkrete Stimme erstellt der Nutzer selbst. Für Video 001 fehlt deshalb aktuell nur das echte Voiceover.

### 2. Google-Flow-Bilder

Der komplette Prompt ist vorhanden; die 36 finalen Bilder müssen vom Nutzer in Google Flow erzeugt und als ZIP abgelegt werden.

### 3. Physische Style-Reference optional nach Pilot

Der gewünschte Look ist schriftlich festgelegt. Nach dem Pilot kann das beste akzeptierte Originalbild zusätzlich dauerhaft als:

```text
assets/channel/STYLE_REFERENCE.png
```

gespeichert werden, damit Flow bei späteren Videos einen echten visuellen Style-Anchor erhält.

## Nächster Produktionsmeilenstein

**Video 001 Phase 2 durchführen und anschließend end-to-end rendern.**

Erst der echte Pilot zeigt, ob Bildrhythmus, Voice, Motion-Stärke und Label-Lesbarkeit in der Praxis optimal sind. Diese Punkte werden danach auf Basis des tatsächlichen Ergebnisses feinjustiert.