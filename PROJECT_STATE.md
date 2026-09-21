# Object-Talk – Project State

Letzte Aktualisierung: 21.09.2026

## Aktueller Stand

Aktiver Test:

```text
youtube-videos/001-pilot-sauerstoff-im-blut/
```

Thema:

**Wie kommt Sauerstoff von der Lunge bis in deine Zellen?**

Der frühere Zucker-Pilot bleibt als TEST 000 im Repository und dient als Vergleichsbasis. Der neue Pilot 001 testet dieselbe Pipeline mit den nach dem ersten Finalrender eingeführten Verbesserungen.

## Pilot-Laufzeit und Bilddichte

Pilot 001 ist ausdrücklich als interner Test markiert:

```text
youtube-videos/001-pilot-sauerstoff-im-blut/05_info/test-mode.json
```

Ziel:
- ungefähr 135 Sekunden
- akzeptabler Testbereich 115–160 Sekunden
- **28 Erklärbilder**
- überwiegend 3–6 Sekunden pro Bild
- normale Kanalvideos bleiben mindestens 300 Sekunden lang

## Was gegenüber Pilot 000 verbessert wurde

### 1. Flow-Bilder möglichst textfrei

Der erste Pilot zeigte, dass KI-generierter Text schnell englisch, inkonsistent oder unleserlich werden kann.

Darum gilt bei Pilot 001:

- Flow erzeugt die Bildwelt möglichst ohne Text
- keine eingebrannten Überschriften
- keine englischen Labels
- wichtige Wörter kommen kontrolliert aus Remotion

### 2. Selektive Überschriften und Keywords

`03_pipeline/overlay-plan.json` enthält nur ausgewählte Texte:

- `Sauerstoff auf Reisen`
- `Die Lungenbläschen`
- `Lunge → Blut`
- `Hämoglobin`
- `Zurück zum Herzen`
- `Sauerstoff wird frei`
- `Mitochondrien`
- `Kohlendioxid`
- `Von der Lunge bis zur Zelle`

Vollbild bleibt der Standard. Overlays dienen nur der Orientierung.

### 3. Feste visuelle Identität

Damit Moleküle/Strukturen nicht von Szene zu Szene ihr Aussehen wechseln:

- O₂ = immer dieselben blass-cyanfarbenen gepaarten Kugeln
- CO₂ = immer dieselbe lineare Drei-Kugel-Form mit dunkler Mitte
- rote Blutkörperchen = warmrote bikonkave Scheiben
- Hämoglobin = burgunderrote vereinfachte vierlappige Struktur innerhalb der roten Blutkörperchen

### 4. Mehr echte Maßstabswechsel

Der Pilot wechselt bewusst:

```text
Mensch
→ Atemwege
→ Alveole
→ Kapillare
→ rotes Blutkörperchen
→ Hämoglobin
→ Herz
→ Gefäß
→ Gewebe
→ Zelle
→ Mitochondrium
→ zurück zur Lunge
```

Dadurch soll das Video wie eine geführte Reise wirken und nicht wie eine reine Diashow.

## Pilot-Struktur

Phase 1 ist vorbereitet mit:

- finalem ca. 2–2,5-Minuten-Skript
- **28 semantischen Szenen**
- Recherche und Claim-Matrix
- `mechanism-map.md`
- vollständigem `sentence-visual-plan.json`
- textfreiem `label-plan.json`
- `image-review.json` für 28 Bilder
- vollständigem Google-Flow-Prompt mit 28 Einzelprompts
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
→ Bild_27–28 einzeln
→ Fehlerliste
→ Recovery-Pass
→ lückenlose ZIP Bild_01...Bild_28
```

Nutzerprompt:

```text
youtube-videos/001-pilot-sauerstoff-im-blut/02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt
```

Voice:

```text
youtube-videos/001-pilot-sauerstoff-im-blut/01_script/VOICEOVER-ZUM-KOPIEREN.txt
```

## V2-Checks

Vor Flow/Voice-Freigabe:

```bash
python tools/validate_planning_v2.py youtube-videos/001-pilot-sauerstoff-im-blut
```

Nach finaler Bildauswahl:

```bash
python tools/validate_planning_v2.py youtube-videos/001-pilot-sauerstoff-im-blut --phase2
```

Danach:

```bash
python tools/prepare_phase3.py youtube-videos/001-pilot-sauerstoff-im-blut
```

Finale technische Test-QA:

```bash
python tools/qa_final.py \
  youtube-videos/001-pilot-sauerstoff-im-blut/04_export/fertiges-video/final-video.mp4 \
  youtube-videos/001-pilot-sauerstoff-im-blut/01_script/audio/final-voiceover.wav \
  --min-seconds 115
```

## Nächster Meilenstein

**Pilot 001 in Google Flow starten und zunächst ausschließlich `Bild_01` erzeugen.**

Wenn `Bild_01` die gewünschte 3D-Erklärwelt trifft, werden die restlichen 27 Bilder mit genau diesem Stil produziert.
