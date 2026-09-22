# AGENTS.md – Object-Talk Repository

Diese Datei ist der Bootstrap für ChatGPT, Antigravity, Codex und andere Repository-Agenten.

## Vor jeder Arbeit lesen

1. `PROJECT_CONTRACT.md`
2. `PROJECT_STATE.md`
3. `config/channel.json`
4. `config/video.json`
5. `THEMEN-GEHIRN.md`
6. `engine/README.md`
7. relevante `engine/*.md`
8. relevante `bildwelt/*.md`
9. Dateien des aktuellen YouTube-Projekts

Für V2-Projekte zusätzlich zwingend:

- `engine/PLANNING-V2.md`
- `engine/VISUAL-EXPLANATION-SYSTEM.md`
- `engine/PRESENTATION-OVERLAY-SYSTEM.md`
- `engine/QUALITY-SCORECARD.md`
- `engine/POSTMORTEM-STANDARD.md`

Aktiver Testpilot:

```text
youtube-videos/001-pilot-sauerstoff-im-blut/
```

## Phasen dürfen nicht vermischt werden

### Phase 1 – Creative Director

Darf:
- recherchieren und Fakten prüfen
- Mechanism Map erstellen
- Skript schreiben
- Satz-Visual-Plan und Szenen festlegen
- Label-Plan erstellen
- Flow-Prompts schreiben
- `overlay-plan.json` erstellen
- Metadaten schreiben

Muss:
- jede Szene als echtes Erklärbild planen
- pro Bild die wichtigsten 1–3 deutschen Labels festlegen
- Bild_01 als Cover + Hook + Master Style Frame besonders detailliert planen
- Flow-Anweisungen auf Englisch schreiben
- sichtbare Hook-/Label-Texte ausschließlich auf Deutsch planen
- Folgeprompts nach Bild_01 kompakt halten: so kurz wie möglich, so genau wie nötig

Darf nicht:
- geschätzte finale Sekundenzeiten als Wahrheit setzen
- Audioänderungen erfinden
- finale Flow-Bilder vortäuschen
- die Bildwelt spontan in Realismus, Anime oder Comic verschieben

### Phase 2 – Nutzer + Medienerzeugung

Google Flow erzeugt ausschließlich die von Phase 1 vorgegebenen Bilder.

Verbindlich:

- `Bild_01` zuerst allein erzeugen
- Bild_01 ist Cover-/Hook-Bild und Master Style Frame
- Bild_01 enthält eine kurze starke deutsche Hook-Zeile zum Thema
- Bild_01 nach Nutzerfreigabe als Style-/Continuity-Referenz für alle weiteren Bilder verwenden
- danach Produktion in 5er-Blöcken
- innerhalb jedes Blocks jedes Bild einzeln erzeugen und prüfen
- alle wichtigen sichtbaren Strukturen knapp auf Deutsch beschriften
- kein englischer sichtbarer Text
- fehlerhafte Schrift oder Anatomie = Regeneration bzw. sauberer Remotion-Fallback
- Fehlerliste + Recovery statt Nummern zu verlieren

Jedes finale V2-Bild wird in `02_bildprompts/image-review.json` einzeln bewertet. Klare Fachfehler, falsche Labels oder Score unter 8/10 führen zu Regeneration.

### Phase 3 – Editor / Antigravity

Darf:
- Nutzerassets importieren
- Audio normalisieren
- Whisper ausführen
- Timings auflösen
- Assets validieren
- Remotion vorbereiten
- vorhandenen `overlay-plan.json` technisch anwenden
- fehlerhafte Flow-Schrift durch exakt geplante deutsche Labels ersetzen
- rendern und QA durchführen

Darf nicht:
- Script umschreiben
- Bildideen austauschen
- Szenengrenzen kreativ neu wählen
- fehlende Fakten erfinden
- fehlende Bilder still ersetzen
- spontane Marketingtexte erfinden

Nach dem Finalrender: `quality-scorecard.md` und `postmortem.md` ausfüllen.

## Fail-closed

Wenn Script, Audio, Szene oder Bildzuordnung nicht eindeutig zusammenpassen: STOP und Fehler melden. Nicht raten.

## Gesundheit/Biologie

Kernbehauptungen in `05_info/claim-matrix.md` dokumentieren. Vereinfachung ist erlaubt, fachliche Verfälschung nicht. Wissenschaftliche Sicherheit unter 8/10 ist harter Blocker.

## Verbindliche visuelle Welt

- premium stark stilisierte 3D-Animationsfilm-Welt
- weich, rund, warm, filmisch
- deutlich animiert statt fotorealistisch
- vereinfachte, erkennbare Anatomie
- familienfreundlich, nicht babyhaft
- keine medizinische Foto-/CGI-Realistik
- kein Anime, Comic, Gore oder Horror-Look
- echte Erklärbilder vor Mascot-/Presenter-Szenen

## Google Flow

- Prompt-Anweisungen: Englisch
- sichtbarer Text: Deutsch
- pro Szene genau ein finales Bild
- Bild_01 = Cover + deutscher Hook + Episode-Style-Anchor
- Bild_01 möglichst ausführlich beschreiben
- Folgeprompts kompakt: meist 2–5 Sätze
- wichtige Dinge in jedem Bild beschriften
- `STYLE_REFERENCE.png` zusätzlich als style-only Anchor laden, sobald vorhanden
- keine Massenproduktion ohne Einzelprüfung
- 5er-Blöcke + Recovery

Details: `engine/FLOW-PRODUCTION-STANDARD.md`.

## Presentation / Overlays

- Vollbild bleibt Standard
- wichtige deutsche Labels gehören zur Erklärsprache
- zusätzliche Überschriften/Keywords nur mit echtem Mehrwert
- ruhige Animationen: Fade, Slide, leichte Scale-in-Bewegung, Unterstreichung, Callout
- keine Bounce-/Shake-/Meme-Effekte

Details: `engine/PRESENTATION-OVERLAY-SYSTEM.md`.

## Timing

Finale Zeitbasis ist ausschließlich das kanonisch vorbereitete Voiceover:

`raw Voice → prepare_audio.py → final-voiceover.wav → transcribe_audio.py → word-timings.json → build_timeline.py → timeline.json`

Kein Renderer schätzt Zeitpunkte aus Textlänge, wenn echte Wortzeiten verfügbar sind.

## V2-Prüfung

```bash
python tools/validate_planning_v2.py youtube-videos/MEIN-VIDEO
python tools/validate_planning_v2.py youtube-videos/MEIN-VIDEO --phase2
```

Für dokumentierte Kurztests QA-Mindestdauer ausdrücklich setzen. Ohne Override bleibt 300 Sekunden Standard.
