# Object-Talk – Project State

Letzte Aktualisierung: 23.09.2026

## Aktueller Stand

Aktiver Test:

```text
youtube-videos/001-pilot-sauerstoff-im-blut/
```

Thema:

**Wie kommt Sauerstoff von der Lunge bis in deine Zellen?**

Pilot 001 ist der aktuelle kleine Testfilm für die freigegebene Bildwelt und den Flow-/Remotion-Workflow.

## Status der Bildwelt

**FREIGEGEBEN.**

Nach dem aktuellen Google-Flow-Test wurde die neue Bildwelt vom Nutzer akzeptiert und im Repository verankert:

```text
bildwelt/APPROVED-VISUAL-WORLD.md
```

Die frühere zu realistische/semi-realistische Richtung ist verworfen.

Ab jetzt:

- stark stilisierte hochwertige 3D-Animationsfilm-Welt
- klar animiert statt fotorealistisch
- weiche gerundete Formen
- warme Creme-/Apricot-/Amber-/Orange-Grundwelt
- tiefe Rot-/Burgundertöne für Blut und Gefäße
- blass Cyan/Türkis als Sauerstoff-Kontrast
- glatte hochwertige Materialien, keine nassen realistischen Gewebetexturen
- starke filmische Tiefenwirkung
- vereinfachte, erkennbare Anatomie
- kein Anime, kein Comic, keine medizinische Foto-/CGI-Realistik
- kein Gore

Ein sauber exportiertes Einzelbild als kanalweite `assets/channel/STYLE_REFERENCE.png` fehlt noch. Ein Browser-Screenshot oder eine Collage wird dafür ausdrücklich nicht verwendet. Bis dahin sind die schriftliche Bildwelt + `Bild_01` jeder Episode autoritativ.

## Pilot-Laufzeit und Bilddichte

- ungefähr 135 Sekunden
- akzeptabler Testbereich 115–160 Sekunden
- 28 Erklärbilder
- überwiegend 3–6 Sekunden pro Bild
- normale Kanalvideos bleiben mindestens 300 Sekunden lang

## Text- und Prompt-Regel

- Flow-Prompt-Anweisungen: Englisch
- jeder sichtbare Text im Bild: Deutsch
- jedes Bild: normalerweise 1–3 wichtige deutsche Labels
- kurze helle/weiße Sans-Serif-Überschriften und dünne Führungslinien bevorzugt
- keine englischen sichtbaren Wörter
- keine langen Textblöcke
- falsches Flow-Label = Regeneration oder exakt geplanter Remotion-Fallback

## Bild_01 – Pflicht

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
- jedes Folgeframe muss sichtbar wie derselbe Film wirken

## Feste visuelle Identität

- O₂ = blass-cyanfarbene gepaarte Kugeln/Partikel
- CO₂ = klar unterscheidbare konsistente Darstellung
- rote Blutkörperchen = warmrote bikonkave Scheiben
- Hämoglobin = burgunderrote vereinfachte Struktur innerhalb roter Blutkörperchen

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

## Ist der kleine Pilot produktionsbereit?

**Ja – Phase 1 ist produktionsbereit.**

Vorhanden:

- finales Skript
- Voiceover-Kopierdatei
- 28 semantische Szenen
- Recherche und Claim-Matrix
- Mechanism Map
- Satz-Visual-Plan
- Label-Plan
- Google-Flow-Prompt
- Scene Map
- Overlay-Plan
- Antigravity-Prompt
- YouTube-Metadaten
- Quality-Scorecard und Postmortem

Noch nicht vorhanden und deshalb noch kein fertiger Render möglich:

1. finales Voice-Audio in `01_script/audio/`
2. akzeptierte final exportierte Flow-Bilder `Bild_01.png` bis `Bild_28.png`
3. ausgefüllte Einzelbild-Reviews nach echter Bildauswahl

Damit ist der nächste reale Produktionsschritt **nicht weitere Planung**, sondern Medienproduktion.

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

Vor Medienproduktion:

```bash
python tools/validate_planning_v2.py youtube-videos/001-pilot-sauerstoff-im-blut
```

Nach finaler Bildauswahl:

```bash
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

1. `Bild_01` im freigegebenen Look final erzeugen und akzeptieren.
2. Danach restliche Flow-Bilder blockweise mit Bild_01 als exakter Stilreferenz erzeugen.
3. Voice-Audio erzeugen und ablegen.
4. Danach Phase 3 / Remotion starten.
