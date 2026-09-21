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

Für **neu angelegte V2-Projekte** zusätzlich zwingend lesen:

- `engine/PLANNING-V2.md`
- `engine/VISUAL-EXPLANATION-SYSTEM.md`
- `engine/QUALITY-SCORECARD.md`
- `engine/POSTMORTEM-STANDARD.md`

Video 001 und andere bereits bestehende Projekte dürfen nicht allein wegen fehlender V2-Dateien rückwirkend blockiert oder umgebaut werden.

## Phasen dürfen nicht vermischt werden

### Phase 1 – Creative Director

Darf:
- recherchieren
- Fakten prüfen
- Mechanism Map erstellen
- Skript schreiben
- Satz-Visual-Plan erstellen
- Szenen festlegen
- Label-Plan erstellen
- Flow-Prompts schreiben
- Metadaten schreiben

Darf nicht:
- geschätzte finale Sekundenzeiten als Wahrheit setzen
- Audioänderungen erfinden
- finale Flow-Bilder vortäuschen

Für neue V2-Projekte gilt: Erst Mechanismus und Satz-Visual-Plan klären, dann finale Bildprompts schreiben. Kein Bild darf nur dekorativ sein.

### Phase 2 – Nutzer + Medienerzeugung

Google Flow erzeugt ausschließlich die von Phase 1 vorgegebenen Bilder. Jedes Bild einzeln. Keine neue Szenenlogik.

Jedes finale V2-Bild wird zusätzlich in `02_bildprompts/image-review.json` einzeln bewertet. Klare Fachfehler, falsche Labels oder ein Score unter 8/10 führen zu Regeneration statt nachträglichem Kaschieren.

### Phase 3 – Editor / Antigravity

Darf:
- Nutzerassets finden/importieren
- Audio normalisieren
- Whisper ausführen
- Timings auflösen
- Assets validieren
- Remotion vorbereiten
- rendern und QA durchführen

Darf nicht:
- Script umschreiben
- Bildideen austauschen
- Szenengrenzen kreativ neu wählen
- fehlende wissenschaftliche Fakten erfinden
- fehlende Bilder still ersetzen
- einen fachlich fehlenden Mechanismus erst im Schnitt erfinden

Nach dem echten Finalrender werden `04_export/quality-scorecard.md` und `04_export/postmortem.md` ausgefüllt. Dauerhafte Lehren werden bevorzugt in bestehende Regeldateien integriert; keine neue Lock-Datei für jede Kleinigkeit.

## Fail-closed

Wenn Script, Audio, Szene oder Bildzuordnung nicht eindeutig zusammenpassen: STOP und Fehler melden. Nicht raten.

## Wichtig bei Gesundheit/Biologie

Jede überprüfbare Kernbehauptung wird intern in `05_info/claim-matrix.md` dokumentiert. Vereinfachung ist erlaubt, fachliche Verfälschung nicht.

Wissenschaftliche Sicherheit unter 8/10 ist bei der V2-Scorecard ein harter Blocker.

## Google Flow

- `STYLE_REFERENCE.png` immer als style-only Anchor laden, sobald vorhanden
- pro Szene genau ein finales Bild
- Szene 01 / Bild_01 = Cover-/Hook-Szene
- keine Massenproduktion ohne Einzelprüfung
- sichtbare deutsche Beschriftungen exakt prüfen
- bei falscher KI-Schrift denselben freigegebenen Begriff später als Editor-Overlay ersetzen

## Timing

Finale Zeitbasis ist ausschließlich das kanonisch vorbereitete Voiceover.

Reihenfolge:

`raw Voice → prepare_audio.py → final-voiceover.wav → transcribe_audio.py → word-timings.json → build_timeline.py → timeline.json`

Kein Renderer darf eigene Zeitpunkte aus Textlänge schätzen, solange echte Wortzeiten verfügbar sind.

## V2-Prüfung

Nur für neue V2-Projekte:

```bash
python tools/validate_planning_v2.py youtube-videos/MEIN-VIDEO
```

Nach finaler Bildauswahl zusätzlich:

```bash
python tools/validate_planning_v2.py youtube-videos/MEIN-VIDEO --phase2
```

Der Validator ist absichtlich separat und verändert die bestehende Video-001-/Phase-3-Pipeline nicht.
