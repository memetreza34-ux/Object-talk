# AGENTS.md – Object-Talk Repository

Diese Datei ist der Bootstrap fuer ChatGPT, Antigravity, Codex und andere Repository-Agenten.

## Vor jeder Arbeit lesen

1. `PROJECT_CONTRACT.md`
2. `PROJECT_STATE.md`
3. `config/channel.json`
4. `config/video.json`
5. `THEMEN-GEHIRN.md`
6. `engine/README.md`
7. `engine/FLOW-AGENT-INSTRUCTIONS.md` bei Flow-/Bildarbeit
8. relevante `engine/*.md`
9. relevante `bildwelt/*.md`
10. Dateien des aktuellen YouTube-Projekts

Fuer V2-Projekte zusaetzlich:

- `engine/PLANNING-V2.md`
- `engine/VISUAL-EXPLANATION-SYSTEM.md`
- `engine/PRESENTATION-OVERLAY-SYSTEM.md`
- `engine/QUALITY-SCORECARD.md`
- `engine/POSTMORTEM-STANDARD.md`

Aktiver Testpilot:

```text
youtube-videos/001-pilot-sauerstoff-im-blut/
```

## Phase 1 – Creative Director

Darf:

- recherchieren und Fakten pruefen
- Mechanism Map erstellen
- Skript schreiben
- Satz-Visual-Plan und Szenen festlegen
- Label-Plan erstellen
- Flow-Szenenprompts schreiben
- `overlay-plan.json` erstellen
- Metadaten schreiben

Muss:

- jede Szene als echtes Erklaerbild planen
- pro Bild 1–3 wichtige deutsche Labels im `label-plan.json` planen
- fuer Bild_01 eine kurze deutsche Cover-Hook planen
- Bild_01 als Cover + erster Shot + Master Style Frame besonders detailliert planen
- Flow-Anweisungen auf Englisch schreiben
- sichtbaren Text ausschliesslich auf Deutsch planen
- Szenenprompt mit Subject, Process, Spatial Layout, Camera/Scale, Continuity, Required German Text und Forbidden Elements planen
- echte visuelle Referenzen vor Textbeschreibungen priorisieren
- die helle Premium-3D-Animationsfilm-Welt erhalten

Darf nicht:

- wichtige deutsche Labels grundlos weglassen
- Cover ohne Hook planen
- Textprompts als Ersatz fuer angehaengte Bildreferenzen behandeln
- die Bildwelt in kosmische, dunkle, Sci-Fi-, Medical-, Anime- oder Comic-Optik verschieben
- finale Flow-Bilder vortaeuschen

## Phase 2 – Nutzer + Medienerzeugung

Google Flow erzeugt ausschliesslich die von Phase 1 vorgegebenen Bilder.

Verbindlich:

- dauerhafte Regeln aus `engine/FLOW-AGENT-INSTRUCTIONS.md` verwenden
- `Bild_01` zuerst allein erzeugen
- `STYLE_REFERENCE.png` als echte Bildreferenz anhaengen, sobald vorhanden
- nach Freigabe `Bild_01.png` bei jeder Folgegeneration wirklich als visuelle Referenz/Ingredient anhaengen
- ein Satz wie `Using Bild_01 as reference` reicht nicht
- jedes Bild einzeln erzeugen und visuell pruefen
- Bild_01 enthaelt die deutsche Cover-Hook direkt im Bild
- normale Bilder enthalten 1–3 kurze deutsche Labels aus `label-plan.json`
- sichtbarer Text ausschliesslich Deutsch
- falsche Flow-Schreibweise zuerst regenerieren
- Remotion nur als exakter Text-Fallback bei wiederholtem KI-Schriftfehler
- Fehlerliste + Recovery statt Nummern zu verlieren

Jedes finale V2-Bild wird in `02_bildprompts/image-review.json` nach Sichtpruefung bewertet. Fachfehler, kosmischer/dunkler Stil, falsche Labels, Artefakte oder ein zentraler Score unter 8/10 fuehren zu Regeneration.

## Phase 3 – Editor / Antigravity

Darf:

- Nutzerassets importieren
- Audio normalisieren
- Whisper ausfuehren
- Timings aufloesen
- Assets validieren
- Remotion vorbereiten
- `label-plan.json` und `overlay-plan.json` technisch anwenden
- nur fehlerhafte oder fehlende Flow-Schrift exakt ersetzen
- rendern und QA durchfuehren

Darf nicht:

- Script umschreiben
- Bildideen austauschen
- Szenengrenzen kreativ neu waehlen
- fehlende Fakten erfinden
- fehlende Bilder still ersetzen
- geplante deutsche Labels entfernen

Nach dem Finalrender: `quality-scorecard.md` und `postmortem.md` ausfuellen.

## Fail-closed

Wenn Script, Audio, Szene oder Bildzuordnung nicht eindeutig zusammenpassen: STOP und Fehler melden. Nicht raten.

Ebenfalls FAIL:

- Folgegeneration behauptet Referenznutzung, ohne dass die Referenz wirklich angehaengt wurde
- `image-review.json` ist ACCEPT, aber finale `Bild_XX.png` fehlt
- Review enthaelt PENDING/TODO/TBD
- Cover-Hook fehlt oder ist falsch geschrieben
- wichtige deutsche Labels fehlen, sind falsch oder Englisch
- Bild driftet in kosmische, dunkle, Sci-Fi-, Medical- oder Stock-Optik

## Gesundheit/Biologie

Kernbehauptungen in `05_info/claim-matrix.md` dokumentieren. Vereinfachung ist erlaubt, fachliche Verfaelschung nicht. Wissenschaftliche Sicherheit unter 8/10 ist harter Blocker.

## Verbindliche visuelle Welt

- helle Premium-3D-Animationsfilm-Welt
- weich, rund, freundlich und hochwertig
- deutlich animiert statt fotorealistisch
- vereinfachte, erkennbare Anatomie
- warmes Licht + weiches Fill-Light
- familienfreundlich, nicht babyhaft
- keine kosmische / Weltraum-artige Optik
- keine dunkle violette Sci-Fi-Mikrowelt als Standard
- keine medizinische Foto-/CGI-Realistik
- kein Anime, Comic, Gore oder Horror-Look
- echte Erklaerbilder vor Mascot-/Presenter-Szenen
- Molekuele/Organe/Zellen normalerweise gesichtslos

## Google Flow

- Prompt-Anweisungen: Englisch
- sichtbarer Text: Deutsch
- pro Szene genau ein finales Bild
- Bild_01 = Cover + deutscher Hook + Episode-Style-Anchor
- Bild_01 nach Freigabe als echtes visuelles Ingredient fuer jedes Folgebild
- `STYLE_REFERENCE.png` zusaetzlich als style-only Anchor laden, sobald vorhanden
- normale Bilder: 1–3 kurze deutsche Labels
- keine Massenproduktion ohne Einzelpruefung
- 5er-Bloecke + Recovery

Details: `engine/FLOW-PRODUCTION-STANDARD.md`.

## Presentation / Overlays

- Vollbild bleibt Standard
- wichtige deutsche Labels kommen aus `02_bildprompts/label-plan.json`
- Remotion ersetzt Flow-Schrift nur, wenn sie falsch/fehlend ist
- keine Bounce-/Shake-/Meme-Effekte

## Timing

Finale Zeitbasis ist ausschliesslich das kanonisch vorbereitete Voiceover:

`raw Voice → prepare_audio.py → final-voiceover.wav → transcribe_audio.py → word-timings.json → build_timeline.py → timeline.json`

## V2-Pruefung

```bash
python tools/validate_planning_v2.py youtube-videos/MEIN-VIDEO
python tools/validate_planning_v2.py youtube-videos/MEIN-VIDEO --phase2
```

`--phase2` verlangt echte finale PNG-Dateien, vollstaendige Review-Werte und `label_accuracy >= 8/10`.
