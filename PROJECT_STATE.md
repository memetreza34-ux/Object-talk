# Object-Talk – Project State

Letzte Aktualisierung: 21.09.2026

## Aktueller Stand

Das frühere aktive Video

```text
youtube-videos/001-was-passiert-mit-essen-im-koerper/
```

wurde auf ausdrücklichen Nutzerwunsch aus dem aktiven Repository entfernt.

Aktiver Test ist jetzt:

```text
youtube-videos/000-pilot-zucker-im-blut/
```

Thema:

**Was passiert mit Zucker nach einem süßen Snack?**

Ziel dieses Piloten ist nicht ein veröffentlichungsfertiges Longform-Video, sondern ein kompakter End-to-End-Test der neuen V2-Architektur und der neuen Bildwelt.

## Pilot-Laufzeit

Der Pilot ist ausdrücklich als interner Test markiert:

```text
05_info/test-mode.json
```

Ziel:
- ungefähr 120 Sekunden
- akzeptabler interner Testbereich 105–150 Sekunden
- normale Kanalvideos bleiben mindestens 300 Sekunden lang

`tools/qa_final.py` unterstützt dafür jetzt einen expliziten `--min-seconds`-Parameter. Ohne diesen Parameter bleibt die normale 300-Sekunden-Grenze bestehen.

## Verbindliche visuelle Richtung

Für diesen Pilot besonders streng:

- **kein Mascot-/Presenter-Video**
- kein Apfel, Keks oder anderes Lebensmittel steht einfach als Sprecher herum
- keine anthropomorphe Food-Figur ist für irgendeine der 15 Szenen nötig
- echte Erklärbilder dominieren vollständig
- Anatomie, Darmwand, Blut, Bauchspeicheldrüse, Zelle, Muskel und Leber zeigen den Mechanismus
- Bilder müssen etwas erklären, nicht nur das Thema dekorieren
- `Bild_01` ist Master Style Frame

## Pilot-Struktur

Phase 1 ist vorbereitet mit:

- finalem ca. 2-Minuten-Skript
- 15 semantischen Szenen
- Recherche und Claim-Matrix
- `mechanism-map.md`
- `sentence-visual-plan.json`
- `label-plan.json`
- `image-review.json`
- vollständigem Google-Flow-Prompt
- `scene-map.json`
- Antigravity-Prompt
- YouTube-Metadaten
- Quality-Scorecard und Postmortem-Vorlage

## Flow-Ablauf

Der Pilot benutzt den neuen Standard:

```text
nur Bild_01
→ Bild_01 vollständig prüfen
→ Nutzer bestätigt Master Style Frame
→ Bild_02–06 einzeln
→ Bild_07–11 einzeln
→ Bild_12–15 einzeln
→ Fehlerliste
→ Recovery-Pass
→ lückenlose ZIP Bild_01...Bild_15
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
Bild_15.png
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

**Bild_01 des neuen Piloten erzeugen und prüfen.**

Erst wenn dieses Bild die gewünschte hochwertige faceless 3D-Erklärwelt trifft, werden die restlichen 14 Bilder produziert.
