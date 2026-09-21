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

Für V2-Projekte zusätzlich zwingend lesen:

- `engine/PLANNING-V2.md`
- `engine/VISUAL-EXPLANATION-SYSTEM.md`
- `engine/PRESENTATION-OVERLAY-SYSTEM.md`
- `engine/QUALITY-SCORECARD.md`
- `engine/POSTMORTEM-STANDARD.md`

Aktiver Testpilot:

```text
youtube-videos/000-pilot-zucker-im-blut/
```

Wenn ein Projekt `05_info/test-mode.json` mit `test_mode: true` besitzt, gilt die dort dokumentierte kurze Testlaufzeit. Nur die Laufzeitregel darf abweichen; alle anderen wissenschaftlichen, visuellen und technischen Qualitätsregeln bleiben aktiv.

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
- selektiven `overlay-plan.json` für kurze Remotion-Überschriften/Schlüsselwörter erstellen
- Metadaten schreiben

Darf nicht:
- geschätzte finale Sekundenzeiten als Wahrheit setzen
- Audioänderungen erfinden
- finale Flow-Bilder vortäuschen
- jede Szene aus Gewohnheit mit Text versehen

Für V2-Projekte gilt: Erst Mechanismus und Satz-Visual-Plan klären, dann finale Bildprompts schreiben. Kein Bild darf nur dekorativ sein.

### Phase 2 – Nutzer + Medienerzeugung

Google Flow erzeugt ausschließlich die von Phase 1 vorgegebenen Bilder. Jedes Bild einzeln. Keine neue Szenenlogik.

`Bild_01` wird zuerst allein erzeugt und als Master Style Frame geprüft. Erst danach folgen 5er-Blöcke. Fehlerhafte Generierungen kommen auf die Recovery-Liste.

Jedes finale V2-Bild wird in `02_bildprompts/image-review.json` einzeln bewertet. Klare Fachfehler, falsche Labels oder ein Score unter 8/10 führen zu Regeneration statt nachträglichem Kaschieren.

Große Überschriften und wiederkehrende Schlüsselbegriffe sollen bevorzugt **nicht** in Flow eingebrannt werden, sondern sauber über Remotion kommen.

### Phase 3 – Editor / Antigravity

Darf:
- Nutzerassets finden/importieren
- Audio normalisieren
- Whisper ausführen
- Timings auflösen
- Assets validieren
- Remotion vorbereiten
- vorhandenen `overlay-plan.json` technisch anwenden
- rendern und QA durchführen

Darf nicht:
- Script umschreiben
- Bildideen austauschen
- Szenengrenzen kreativ neu wählen
- fehlende wissenschaftliche Fakten erfinden
- fehlende Bilder still ersetzen
- einen fachlich fehlenden Mechanismus erst im Schnitt erfinden
- Mascot-/Presenter-Elemente ergänzen, wenn sie in Phase 1 nicht vorgesehen sind
- spontan neue Überschriften oder Marketingtexte erfinden, die nicht im Overlay-Plan stehen

Nach dem echten Finalrender werden `04_export/quality-scorecard.md` und `04_export/postmortem.md` ausgefüllt. Dauerhafte Lehren werden bevorzugt in bestehende Regeldateien integriert; keine neue Lock-Datei für jede Kleinigkeit.

## Fail-closed

Wenn Script, Audio, Szene oder Bildzuordnung nicht eindeutig zusammenpassen: STOP und Fehler melden. Nicht raten.

## Wichtig bei Gesundheit/Biologie

Jede überprüfbare Kernbehauptung wird intern in `05_info/claim-matrix.md` dokumentiert. Vereinfachung ist erlaubt, fachliche Verfälschung nicht.

Wissenschaftliche Sicherheit unter 8/10 ist bei der V2-Scorecard ein harter Blocker.

## Google Flow

- `STYLE_REFERENCE.png` immer als style-only Anchor laden, sobald vorhanden
- pro Szene genau ein finales Bild
- Szene 01 / Bild_01 = Cover-/Hook-Szene + Episode-Style-Anchor
- keine Massenproduktion ohne Einzelprüfung
- sichtbare deutsche Beschriftungen exakt prüfen
- bei falscher KI-Schrift denselben freigegebenen Begriff später als Editor-Overlay ersetzen
- echte Erklärbilder vor Mascot-/Presenter-Bildern

## Presentation / Overlays

- Vollbild bleibt der visuelle Standard
- aktuelle semi-realistische 3D-Welt beibehalten; kein Anime-/Comic-Umbau
- kurze Überschriften nur an echten Mechanismus-/Kapitelwechseln
- Schlüsselwörter sparsam
- keine kompletten Voice-over-Sätze auf dem Bild
- Overlay-Animationen ruhig: Fade, Slide, leichte Scale-in-Bewegung, Unterstreichung, Callout
- keine Bounce-/Shake-/Meme-Effekte

Details: `engine/PRESENTATION-OVERLAY-SYSTEM.md`.

## Timing

Finale Zeitbasis ist ausschließlich das kanonisch vorbereitete Voiceover.

Reihenfolge:

`raw Voice → prepare_audio.py → final-voiceover.wav → transcribe_audio.py → word-timings.json → build_timeline.py → timeline.json`

Kein Renderer darf eigene Zeitpunkte aus Textlänge schätzen, solange echte Wortzeiten verfügbar sind.

## V2-Prüfung

```bash
python tools/validate_planning_v2.py youtube-videos/MEIN-VIDEO
```

Nach finaler Bildauswahl:

```bash
python tools/validate_planning_v2.py youtube-videos/MEIN-VIDEO --phase2
```

Der Validator ist separat und verändert die technische Phase-3-Pipeline nicht.

Für dokumentierte Kurztests muss die finale QA den Test-Mindestwert ausdrücklich setzen, z. B. beim aktuellen Pilot:

```bash
python tools/qa_final.py VIDEO VOICEOVER --min-seconds 105
```

Ohne Override bleibt die Standard-Mindestdauer 300 Sekunden.
