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

## Phasen dürfen nicht vermischt werden

### Phase 1 – Creative Director

Darf:
- recherchieren
- Fakten prüfen
- Skript schreiben
- Szenen festlegen
- Flow-Prompts schreiben
- Metadaten schreiben

Darf nicht:
- geschätzte finale Sekundenzeiten als Wahrheit setzen
- Audioänderungen erfinden
- finale Flow-Bilder vortäuschen

### Phase 2 – Nutzer + Medienerzeugung

Google Flow erzeugt ausschließlich die von Phase 1 vorgegebenen Bilder. Jedes Bild einzeln. Keine neue Szenenlogik.

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

## Fail-closed

Wenn Script, Audio, Szene oder Bildzuordnung nicht eindeutig zusammenpassen: STOP und Fehler melden. Nicht raten.

## Wichtig bei Gesundheit/Biologie

Jede überprüfbare Kernbehauptung wird intern in `05_info/claim-matrix.md` dokumentiert. Vereinfachung ist erlaubt, fachliche Verfälschung nicht.

## Google Flow

- `STYLE_REFERENCE.png` immer als style-only Anchor laden, sobald vorhanden
- pro Szene genau ein finales Bild
- Szene 01 / Bild_01 = Cover-/Hook-Szene
- keine Massenproduktion ohne Einzelprüfung
- sichtbare deutsche Beschriftungen exakt prüfen

## Timing

Finale Zeitbasis ist ausschließlich das kanonisch vorbereitete Voiceover.

Reihenfolge:

`raw Voice → prepare_audio.py → final-voiceover.wav → transcribe_audio.py → word-timings.json → build_timeline.py → timeline.json`

Kein Renderer darf eigene Zeitpunkte aus Textlänge schätzen, solange echte Wortzeiten verfügbar sind.
