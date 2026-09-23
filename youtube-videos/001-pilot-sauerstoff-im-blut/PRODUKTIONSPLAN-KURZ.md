# Produktionsplan – Pilot 001 Sauerstoff

Ziel: erster echter kleiner Object-Talk-Pilot mit ungefähr 2–2,5 Minuten Laufzeit und 28 Bildern.

## 1. Voice erzeugen

Datei öffnen:

```text
01_script/VOICEOVER-ZUM-KOPIEREN.txt
```

Den Text 1:1 in die Voice-KI übernehmen. Das finale Audio danach in:

```text
01_script/audio/
```

ablegen.

## 2. Google Flow starten

Datei öffnen:

```text
02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt
```

Den kompletten Prompt in Flow verwenden.

Zuerst ausschließlich:

```text
Bild_01
```

erzeugen.

Bild_01 ist:
- Cover
- Hook
- erster Shot
- Master Style Frame

Nur wenn Bild_01 die freigegebene stark stilisierte 3D-Animationsfilm-Welt sauber trifft, weiterarbeiten.

## 3. Restliche Bilder produzieren

Bild_01 bei jeder weiteren Generation als exakte Style-/Continuity-Referenz verwenden.

Reihenfolge:

```text
Bild_02–06
Bild_07–11
Bild_12–16
Bild_17–21
Bild_22–26
Bild_27–28
```

Jedes Bild einzeln erzeugen und direkt prüfen.

Prüfen:
- gleicher Stil wie Bild_01
- kein Drift in Fotorealismus
- wichtige Labels nur Deutsch
- Anatomie/Prozess verständlich
- keine groben KI-Artefakte

Fehlerhafte Nummern auf Recovery-Liste setzen und später gezielt neu erzeugen.

## 4. Bilder exportieren

Final akzeptierte Bilder lückenlos als:

```text
Bild_01.png
...
Bild_28.png
```

bereitstellen und als ZIP in:

```text
02_bildprompts/bilder-zip/
```

ablegen.

## 5. Phase 3 starten

Sobald Voice + alle 28 Bilder vorhanden sind:

```bash
python tools/validate_planning_v2.py youtube-videos/001-pilot-sauerstoff-im-blut --phase2
python tools/prepare_phase3.py youtube-videos/001-pilot-sauerstoff-im-blut
```

Danach den technischen Prompt verwenden:

```text
03_pipeline/ANTIGRAVITY-PROMPT-ZUM-KOPIEREN.txt
```

Antigravity/Remotion übernimmt dann:
- Audioaufbereitung
- Whisper-Worttimings
- exakte Szenen-Timeline
- Bildimport
- dezente Bewegung
- geplante Overlays
- Render
- QA

## 6. Ergebnis

Zieldatei:

```text
04_export/fertiges-video/final-video.mp4
```

Der 10-Bilder-Mini-Test 002 wird vorerst übersprungen.