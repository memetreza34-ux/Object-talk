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

## Phasen duerfen nicht vermischt werden

### Phase 1 – Creative Director

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
- pro Bild die wichtigsten deutschen Labels im `label-plan.json` planen
- Bild_01 als Cover-Grundbild + erster Shot + Master Style Frame besonders detailliert planen
- Flow-Anweisungen auf Englisch schreiben
- Szenenprompt mit Subject, Process, Spatial Layout, Camera/Scale, Continuity und Forbidden Elements planen
- echte visuelle Referenzen vor Textbeschreibungen priorisieren

Darf nicht:
- Flow-Labels standardmaessig einplanen
- Textprompts als Ersatz fuer tatsaechlich angehaengte Bildreferenzen behandeln
- geschätzte finale Sekundenzeiten als Wahrheit setzen
- Audioaenderungen erfinden
- finale Flow-Bilder vortaeuschen
- die Bildwelt spontan in Realismus, Anime oder Comic verschieben

### Phase 2 – Nutzer + Medienerzeugung

Google Flow erzeugt ausschliesslich die von Phase 1 vorgegebenen Bilder.

Verbindlich:

- dauerhafte Regeln aus `engine/FLOW-AGENT-INSTRUCTIONS.md` verwenden
- `Bild_01` zuerst allein erzeugen
- `STYLE_REFERENCE.png` als echte Bildreferenz anhaengen, sobald vorhanden
- nach Freigabe `Bild_01.png` bei jeder Folgegeneration wirklich als visuelle Referenz/Ingredient anhaengen
- ein Satz wie `Using Bild_01 as reference` reicht nicht
- jedes Bild einzeln erzeugen und visuell pruefen
- Flow-Bilder standardmaessig textfrei
- deutsche Hook/Labels spaeter ueber Remotion
- Fehlerliste + Recovery statt Nummern zu verlieren

Jedes finale V2-Bild wird in `02_bildprompts/image-review.json` nach Sichtpruefung des echten Bildes bewertet. Klare Fachfehler, falscher Stil, Artefakte oder ein zentraler Score unter 8/10 fuehren zu Regeneration.

### Phase 3 – Editor / Antigravity

Darf:
- Nutzerassets importieren
- Audio normalisieren
- Whisper ausfuehren
- Timings aufloesen
- Assets validieren
- Remotion vorbereiten
- `label-plan.json` und `overlay-plan.json` technisch anwenden
- Cover-Hook und deutsche Labels sauber rendern
- rendern und QA durchfuehren

Darf nicht:
- Script umschreiben
- Bildideen austauschen
- Szenengrenzen kreativ neu waehlen
- fehlende Fakten erfinden
- fehlende Bilder still ersetzen
- spontane Marketingtexte erfinden

Nach dem Finalrender: `quality-scorecard.md` und `postmortem.md` ausfuellen.

## Fail-closed

Wenn Script, Audio, Szene oder Bildzuordnung nicht eindeutig zusammenpassen: STOP und Fehler melden. Nicht raten.

Ebenfalls FAIL:

- Folgegeneration behauptet Referenznutzung, ohne dass die Referenz wirklich angehaengt wurde
- `image-review.json` ist ACCEPT, aber finale `Bild_XX.png` fehlt
- Review enthaelt PENDING/TODO/TBD
- Flow hat ungewollte Schrift oder KI-Gibberish ins Bild gesetzt

## Gesundheit/Biologie

Kernbehauptungen in `05_info/claim-matrix.md` dokumentieren. Vereinfachung ist erlaubt, fachliche Verfaelschung nicht. Wissenschaftliche Sicherheit unter 8/10 ist harter Blocker.

## Verbindliche visuelle Welt

- premium stark stilisierte 3D-Animationsfilm-Welt
- weich, rund, warm, filmisch
- deutlich animiert statt fotorealistisch
- vereinfachte, erkennbare Anatomie
- familienfreundlich, nicht babyhaft
- keine medizinische Foto-/CGI-Realistik
- kein Anime, Comic, Gore oder Horror-Look
- echte Erklaerbilder vor Mascot-/Presenter-Szenen
- Molekuele/Organe/Zellen normalerweise gesichtslos

## Google Flow

- Prompt-Anweisungen: Englisch
- Bilder: standardmaessig ohne Text
- pro Szene genau ein finales Bild
- Bild_01 = Cover-Grundbild + Episode-Style-Anchor
- Bild_01 nach Freigabe als echtes visuelles Ingredient fuer jedes Folgebild
- `STYLE_REFERENCE.png` zusaetzlich als style-only Anchor laden, sobald vorhanden
- keine Massenproduktion ohne Einzelpruefung
- 5er-Bloecke + Recovery

Details: `engine/FLOW-PRODUCTION-STANDARD.md`.

## Presentation / Overlays

- Vollbild bleibt Standard
- wichtige deutsche Labels kommen aus `02_bildprompts/label-plan.json`
- Hook/Labels/Callouts werden in Remotion sauber gesetzt
- keine Bounce-/Shake-/Meme-Effekte

## Timing

Finale Zeitbasis ist ausschliesslich das kanonisch vorbereitete Voiceover:

`raw Voice → prepare_audio.py → final-voiceover.wav → transcribe_audio.py → word-timings.json → build_timeline.py → timeline.json`

Kein Renderer schaetzt Zeitpunkte aus Textlaenge, wenn echte Wortzeiten verfuegbar sind.

## V2-Pruefung

```bash
python tools/validate_planning_v2.py youtube-videos/MEIN-VIDEO
python tools/validate_planning_v2.py youtube-videos/MEIN-VIDEO --phase2
```

`--phase2` verlangt echte finale PNG-Dateien und vollstaendige Review-Werte.
