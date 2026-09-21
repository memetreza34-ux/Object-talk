# Object-Talk – Project State

Letzte Aktualisierung: 21.09.2026

## Aktueller Stand

Die Longform-Grundarchitektur ist vollständig genug für den ersten echten End-to-End-Piloten.

Zusätzlich ist jetzt **Video 001 – „Was passiert mit deinem Essen im Körper?“** in Phase 1 vollständig vorbereitet und der Flow-Workflow wurde nach dem ersten Praxistest überarbeitet.

Am 21.09.2026 wurde außerdem eine **nicht rückwirkende V2-Planungs- und QA-Schicht** ergänzt. Sie übernimmt die wichtigsten stabilen Prinzipien aus dem separaten Erklärkanal-System, ohne dessen visuelle Markenwelt, starre Shortform-Regeln oder bestehende Dateien zu kopieren.

Vorhanden:

- `PROJECT_CONTRACT.md` als oberste dauerhafte Projektregel
- `AGENTS.md` als Bootstrap für neue Chats/Agenten
- maschinenlesbare `config/channel.json` und `config/video.json`
- `THEMEN-GEHIRN.md` gegen Themenwiederholungen
- `engine/THEMEN-STRATEGIE.md` für systematische Longform-Themenauswahl
- `engine/SCRIPT-STANDARD.md` für Hook, Einleitung, Hauptteil, rhetorische Mittel, Schluss und Visual-First-Scriptwriting
- `engine/PLANNING-V2.md` für Mechanism Map, Satz-Visual-Plan, stabile Bild-IDs, Label-Plan und Bildreview
- `engine/VISUAL-EXPLANATION-SYSTEM.md` für echte visuelle Erklärfunktionen und Maßstabsketten
- `engine/QUALITY-SCORECARD.md` für gewichtete Freigabe; Wissenschaft unter 8/10 blockiert
- `engine/POSTMORTEM-STANDARD.md` für dauerhaftes Lernen aus jedem echten Finalrender
- `tools/validate_planning_v2.py` als separater, nicht destruktiver V2-Validator
- V2-Dateien im `_TEMPLATE` für alle neu angelegten Videos
- `engine/FLOW-PRODUCTION-STANDARD.md` für faceless Explainer-Bildwelt, Master Style Frame, 5er-Blöcke und Recovery
- erste Fach-Bildwelt `bildwelt/gehirn.md`
- globales Style-Reference-System
- YouTube-Projektvorlage
- 3-Phasen-Workflow mit harten Phase-Gates
- wissenschaftlicher Fact-Check-Standard + Claim-Matrix
- semantische Phase-1-Szenen statt automatischem Satz-für-Satz-Schnitt
- vollständige `speech_section` pro Szene
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

## V2-Kompatibilitätsregel

Die neue V2-Schicht gilt für **neu aus `_TEMPLATE` angelegte Projekte**.

Sie erzeugt zusätzlich:

```text
05_info/mechanism-map.md
05_info/sentence-visual-plan.json
02_bildprompts/label-plan.json
02_bildprompts/image-review.json
04_export/quality-scorecard.md
04_export/postmortem.md
```

Prüfung:

```bash
python tools/validate_planning_v2.py youtube-videos/THEMA
python tools/validate_planning_v2.py youtube-videos/THEMA --phase2
```

**Video 001 wird nicht rückwirkend umgebaut oder blockiert.** Seine bestehenden Dateien, Szenen, Flow-Prompts, Nummern und Phase-3-Pipeline bleiben unverändert nutzbar.

## Verbindliche visuelle Richtung

Nach dem ersten Flow-Test ist festgelegt:

- **kein Mascot-/Presenter-Kanal**
- keine dauerhafte Apfel-/Food-Sprecherfigur
- direkte Erklärbilder sind Standard
- anatomische Cutaways, transparente Körperansichten, Prozesse, Organe, Gewebe, Zellen und Vergleiche dominieren
- personifizierte Objekte nur selten und nur mit echtem didaktischem Mehrwert
- komplexe Vorgänge sollen mit möglichst einer klaren visuellen Hauptaussage pro Bild erklärt werden

`config/channel.json` wurde an diese Contract-Regel angeglichen, damit Agenten nicht mehr zwischen „Object-Talk als Presenter“ und „Faceless Explainer zuerst“ widersprüchliche Signale erhalten.

`Bild_01` jeder Episode ist:

- Cover-/Hook-Bild
- erster Shot
- **Master Style Frame für alle weiteren Bilder der Episode**

## Verbindlicher Flow-Ablauf

```text
zuerst ausschließlich Bild_01
→ Bild_01 vollständig prüfen
→ Bild_01 als Style-/Continuity-Referenz verwenden
→ Bild_02–06 einzeln produzieren
→ Block-QA
→ Bild_07–11 einzeln produzieren
→ usw.
→ technische/qualitative Fehlschläge auf Recovery-Liste
→ nach allen normalen Blöcken Recovery-Pass
→ erst bei lückenlosem Bild_01...Bild_NN-Satz ZIP erstellen
```

Ein einzelner Flow-Fehler beendet also nicht mehr den gesamten Produktionslauf.

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
- komplett überarbeiteten Google-Flow-Agent-Prompt für faceless Explainer-Visuals
- `Bild_01` als Master Style Frame
- 5er-Block-Workflow
- Fehlerliste + Recovery-Pass
- menschenlesbare Bild↔Skript-Pipeline
- Antigravity-Phase-3-Anweisung
- YouTube-Titel, Beschreibung und 5 Hashtags

Die Nutzerkopie ist synchron:

```text
02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt
```

## Nächster Schritt des Nutzers

1. `01_script/VOICEOVER-ZUM-KOPIEREN.txt` 1:1 in die eigene Voice-KI geben.
2. finale Audio-Datei in `01_script/audio/` legen.
3. `02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt` vollständig in Google Flow verwenden.
4. Flow soll **zuerst nur `Bild_01`** erstellen.
5. Erst nach akzeptiertem `Bild_01` die weiteren Bilder in 5er-Blöcken erzeugen.
6. Fehlgeschlagene Bildnummern am Ende im Recovery-Pass erneut erzeugen.
7. finale ZIP mit `Bild_01.png` bis `Bild_36.png` in `02_bildprompts/bilder-zip/` legen.

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

Die konkrete Stimme erstellt der Nutzer selbst. Für Video 001 fehlt deshalb aktuell das echte Voiceover.

### 2. Google-Flow-Bilder

Der neue komplette Prompt ist vorhanden; die 36 finalen Bilder müssen in Google Flow erzeugt und als ZIP abgelegt werden.

### 3. Kanalweite physische Style-Reference optional nach Pilot

Für Video 001 übernimmt `Bild_01` bereits die Rolle der Episode-Referenz.

Nach dem Pilot kann das beste dauerhaft akzeptierte Originalbild zusätzlich als:

```text
assets/channel/STYLE_REFERENCE.png
```

gespeichert werden. Dann bleibt `Bild_01` weiterhin die konkrete Episode-/Continuity-Referenz.

## Nächster Produktionsmeilenstein

**Video 001 mit dem neuen Flow-System erneut durch Phase 2 führen und anschließend end-to-end rendern.**

Erst der echte Pilot zeigt, ob Bildrhythmus, Motion-Stärke und Label-Lesbarkeit in der Praxis optimal sind. Diese Punkte werden danach auf Basis des tatsächlichen Ergebnisses feinjustiert.
