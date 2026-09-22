# Object-Talk – Project State

Letzte Aktualisierung: 22.09.2026

## Aktueller Stand

Aktiver Test:

```text
youtube-videos/001-pilot-sauerstoff-im-blut/
```

Thema:

**Wie kommt Sauerstoff von der Lunge bis in deine Zellen?**

Pilot 001 testet die verbesserte visuelle Welt und den neuen Flow-Standard.

## Pilot-Laufzeit und Bilddichte

- ungefähr 135 Sekunden
- akzeptabler Testbereich 115–160 Sekunden
- **28 Erklärbilder**
- überwiegend 3–6 Sekunden pro Bild
- normale Kanalvideos bleiben mindestens 300 Sekunden lang

## Verbindliche neue Bildwelt

Die frühere zu realistische/semi-realistische Richtung ist verworfen.

Ab jetzt:

- **stark stilisierte hochwertige 3D-Animationsfilm-Welt**
- deutlich animiert statt fotorealistisch
- weiche gerundete Formen
- vereinfachte, erkennbare Anatomie
- warme filmische Beleuchtung
- hochwertige Materialien und starke Tiefenwirkung
- freundlich und familiengeeignet, nicht babyhaft
- kein Anime, kein Comic, keine medizinische Foto-/CGI-Realistik
- kein Gore

## Text- und Prompt-Regel

- Flow-Prompt-Anweisungen: **Englisch**
- jeder sichtbare Text im Bild: **Deutsch**
- jedes Bild: normalerweise 1–3 wichtige deutsche Labels
- keine englischen sichtbaren Wörter
- keine langen Textblöcke
- falsches Flow-Label = Regeneration oder exakt geplanter Remotion-Fallback

## Bild_01 – neue Pflicht

`Bild_01` ist immer:

- Cover
- erster Shot
- Master Style Frame
- Vorlage für alle restlichen Bilder

Bild_01 wird besonders ausführlich beschrieben und enthält eine kurze starke deutsche Hook-Zeile zum Thema.

Für Pilot 001:

```text
So reist Sauerstoff durch deinen Körper
```

Bild_01 wird zuerst allein erzeugt. Erst nach Nutzerfreigabe geht es weiter.

## Folgeprompts

Nach Bild_01 gilt:

- Prompt so kurz wie möglich, so genau wie nötig
- normalerweise 2–5 englische Sätze
- Szene + sichtbarer Prozess + Komposition + deutsche Labels
- globalen Stilblock nicht ständig wiederholen
- `Bild_01.png` immer als Style-/Continuity-Referenz verwenden

## Feste visuelle Identität

- O₂ = blass-cyanfarbene gepaarte Kugeln
- CO₂ = klar unterscheidbare lineare Drei-Kugel-Form
- rote Blutkörperchen = warmrote bikonkave Scheiben
- Hämoglobin = burgunderrote vereinfachte vierlappige Struktur innerhalb roter Blutkörperchen

## Flow-Ablauf

```text
nur Bild_01
→ Bild_01 prüfen
→ Nutzerfreigabe
→ Bild_02–06 einzeln
→ Block-QA
→ Bild_07–11 einzeln
→ Block-QA
→ Bild_12–16 einzeln
→ Block-QA
→ Bild_17–21 einzeln
→ Block-QA
→ Bild_22–26 einzeln
→ Block-QA
→ Bild_27–28 einzeln
→ Fehlerliste
→ Recovery-Pass
→ lückenlose ZIP Bild_01...Bild_28
```

## Pilot-Struktur

Phase 1 enthält:

- finales Skript
- 28 semantische Szenen
- Recherche und Claim-Matrix
- Mechanism Map
- Satz-Visual-Plan
- Label-Plan mit deutschen Schlüsselbegriffen pro Bild
- Google-Flow-Prompt mit ausführlichem Bild_01 und kompakten Folgeprompts
- Scene Map
- reduzierten Overlay-Plan ohne doppelten Cover-Hook
- Antigravity-Prompt
- YouTube-Metadaten
- Quality-Scorecard und Postmortem

## Nutzerdateien

Flow:

```text
youtube-videos/001-pilot-sauerstoff-im-blut/02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt
```

Voice:

```text
youtube-videos/001-pilot-sauerstoff-im-blut/01_script/VOICEOVER-ZUM-KOPIEREN.txt
```

## V2-Checks

```bash
python tools/validate_planning_v2.py youtube-videos/001-pilot-sauerstoff-im-blut
python tools/validate_planning_v2.py youtube-videos/001-pilot-sauerstoff-im-blut --phase2
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

**Google Flow bekommt den aktualisierten Prompt und erzeugt zuerst ausschließlich Bild_01.**

Nur wenn Bild_01 die gewünschte stark stilisierte 3D-Animationswelt, den deutschen Cover-Hook und die wichtigsten Labels sauber trifft, werden die restlichen 27 Bilder erzeugt.
