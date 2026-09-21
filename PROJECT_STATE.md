# Object-Talk – Project State

Letzte Aktualisierung: 21.09.2026

## Aktueller Stand

Aktiver Test:

```text
youtube-videos/000-pilot-zucker-im-blut/
```

Thema:

**Was passiert mit Zucker nach einem süßen Snack?**

Der Pilot ist ein kompakter End-to-End-Test der neuen V2-Architektur und der faceless 3D-Erklärbildwelt.

## Pilot-Laufzeit und Bilddichte

Der Pilot ist ausdrücklich als interner Test markiert:

```text
05_info/test-mode.json
```

Ziel:
- ungefähr 120 Sekunden
- akzeptabler Testbereich 105–150 Sekunden
- **26 Erklärbilder**
- Zielrhythmus im Mittel ungefähr 4–5 Sekunden pro Bild
- normale Kanalvideos bleiben mindestens 300 Sekunden lang

Die hohe Bilddichte ist jetzt bewusst Teil des Formats: Das Voice-over soll sichtbar mit neuen Zuständen, Maßstäben, Prozessen und Vergleichen mitgehen. Lange Standzeiten dürfen nicht nur durch Zoom/Pan kaschiert werden.

## Verbindliche visuelle Richtung

Für diesen Pilot besonders streng:

- **kein Mascot-/Presenter-Video**
- kein Apfel, Keks oder anderes Lebensmittel steht einfach als Sprecher herum
- keine anthropomorphe Food-Figur ist für irgendeine der 26 Szenen nötig
- echte Erklärbilder dominieren vollständig
- Anatomie, Dünndarm, Darmzotten, Darmwand, Blut, Bauchspeicheldrüse, Betazellen, Insulin, Zellen, Muskel und Leber zeigen den Mechanismus
- jedes Bild muss eine neue sichtbare Aussage liefern
- `Bild_01` ist Master Style Frame

## Präsentation / Text / Animation

Nach Auswertung des ersten vollständigen Piloten ist zusätzlich festgelegt:

- die aktuelle warme semi-realistische 3D-Welt bleibt bestehen
- **kein Anime-/Comic-Umbau**
- generierte Bilder bleiben grundsätzlich Vollbild
- das Video soll trotzdem nicht wie eine Diashow wirken
- ausgewählte Szenen erhalten kurze animierte Überschriften, Schlüsselwörter oder Callouts in Remotion
- Überschriften werden bevorzugt im Editor erzeugt statt von Flow in das Bild geschrieben
- komplette Voice-over-Sätze werden nicht auf das Bild gelegt
- das Bild bleibt immer der Hauptdarsteller

Globale Regel:

```text
engine/PRESENTATION-OVERLAY-SYSTEM.md
```

Der Renderer unterstützt jetzt optional:

```text
03_pipeline/overlay-plan.json
```

Der aktuelle Pilot besitzt bereits einen selektiven Overlay-Plan mit kurzen Überschriften u. a. bei Dünndarm, Blutzucker, Bauchspeicheldrüse, Insulin, Muskelzellen und Glykogenspeicherung.

## Pilot-Struktur

Phase 1 ist vorbereitet mit:

- überarbeitetem ca. 2-Minuten-Skript
- **26 semantischen Szenen**
- Recherche und Claim-Matrix
- `mechanism-map.md`
- vollständigem `sentence-visual-plan.json`
- vollständigem `label-plan.json`
- `image-review.json` für 26 Bilder
- vollständigem Google-Flow-Prompt mit 26 Einzelprompts
- `scene-map.json`
- `overlay-plan.json`
- Antigravity-Prompt
- YouTube-Metadaten
- Quality-Scorecard und Postmortem-Vorlage

## Flow-Ablauf

```text
nur Bild_01
→ Bild_01 vollständig prüfen
→ Nutzer bestätigt Master Style Frame
→ Bild_02–06 einzeln
→ Bild_07–11 einzeln
→ Bild_12–16 einzeln
→ Bild_17–21 einzeln
→ Bild_22–26 einzeln
→ Fehlerliste
→ Recovery-Pass
→ lückenlose ZIP Bild_01...Bild_26
```

Der komplette Nutzerprompt liegt hier:

```text
youtube-videos/000-pilot-zucker-im-blut/02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt
```

## V2-Checks

Vor Flow/Voice-Freigabe:

```bash
python tools/validate_planning_v2.py youtube-videos/000-pilot-zucker-im-blut
```

Nach finaler Bildauswahl:

```bash
python tools/validate_planning_v2.py youtube-videos/000-pilot-zucker-im-blut --phase2
```

Danach:

```bash
python tools/prepare_phase3.py youtube-videos/000-pilot-zucker-im-blut
```

`build_renderer_runtime.py` erkennt `03_pipeline/overlay-plan.json` automatisch. Wenn kein Overlay-Plan vorhanden ist, bleibt das bisherige Full-Image-Verhalten vollständig kompatibel.

Finale technische Test-QA:

```bash
python tools/qa_final.py \
  youtube-videos/000-pilot-zucker-im-blut/04_export/fertiges-video/final-video.mp4 \
  youtube-videos/000-pilot-zucker-im-blut/01_script/audio/final-voiceover.wav \
  --min-seconds 105
```

## Nächster Meilenstein

**Pilot erneut mit der neuen Overlay-/Presentation-Ebene rendern und vergleichen.**

Ziel ist nicht mehr Animation um ihrer selbst willen, sondern mehr visuelle Führung: Vollbild + hohe Bilddichte + wenige gezielte animierte Überschriften/Schlüsselwörter.
