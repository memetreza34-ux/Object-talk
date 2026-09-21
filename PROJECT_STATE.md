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

## Was jetzt vom Nutzer benötigt wird

### 1. Voice

```text
youtube-videos/000-pilot-zucker-im-blut/01_script/VOICEOVER-ZUM-KOPIEREN.txt
```

1:1 in die eigene Voice-KI geben und die rohe Audiodatei in `01_script/audio/` ablegen.

### 2. Zuerst nur Bild_01

Den Flow-Prompt vollständig verwenden. Flow muss zunächst ausschließlich `Bild_01` erzeugen und danach stoppen.

`Bild_01` gemeinsam prüfen. Erst nach akzeptiertem Stil werden die übrigen Bilder erzeugt.

### 3. Nach allen Bildern

ZIP mit exakt:

```text
Bild_01.png
...
Bild_26.png
```

in `02_bildprompts/bilder-zip/` ablegen.

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

Finale technische Test-QA:

```bash
python tools/qa_final.py \
  youtube-videos/000-pilot-zucker-im-blut/04_export/fertiges-video/final-video.mp4 \
  youtube-videos/000-pilot-zucker-im-blut/01_script/audio/final-voiceover.wav \
  --min-seconds 105
```

## Nächster Meilenstein

**Bild_01 des 26-Bilder-Piloten erzeugen und prüfen.**

Erst wenn dieses Bild die gewünschte hochwertige faceless 3D-Erklärwelt trifft, werden die restlichen 25 Bilder produziert.
