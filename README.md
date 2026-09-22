# Object-Talk

Produktionssystem für den deutschen YouTube-Kanal **Object-Talk / FoodSpricht**.

## Ziel

Normale Kanalvideos sind lange deutschsprachige Erklärvideos über Ernährung, Gesundheit, menschlichen Körper und Biologie.

Standard:

- mindestens 5:00 Minuten
- 16:9 / 1920×1080 / 30 fps
- hohe visuelle Dichte aus generierten Standbildern
- stark stilisierte hochwertige 3D-Animationsfilm-Welt
- deutlich animiert statt fotorealistisch
- wichtige sichtbare Strukturen knapp auf Deutsch beschriften
- Flow-Prompt-Anweisungen auf Englisch
- sichtbarer Text im Bild ausschließlich Deutsch
- wissenschaftlich prüfen
- keine unnötige Themenwiederholung

## Aktueller interner Pilot

```text
youtube-videos/001-pilot-sauerstoff-im-blut/
```

Thema:

**Wie kommt Sauerstoff von der Lunge bis in deine Zellen?**

Pilot 001 ist absichtlich nur ungefähr 2–2,5 Minuten lang und nutzt 28 Erklärbilder. Er testet die neue visuelle Welt und ändert die 5-Minuten-Regel für normale Videos nicht.

## Verbindliche Bildwelt

- premium stilisierte 3D-Animationsfilm-Optik
- weiche gerundete Formen
- vereinfachte, aber erkennbare Anatomie
- warme filmische Beleuchtung
- hochwertige Materialien und starke Tiefenwirkung
- freundlich, modern, familiengeeignet
- kein medizinischer Fotorealismus
- kein Anime, Comic, Gore oder Horror-Look
- kein dauerhafter Mascot-/Presenter-Fokus

Der Kanal lebt von echten Erklärbildern: Cutaways, transparente Körperansichten, Organ-/Gewebe-/Zellansichten, Prozessbilder, Vergleiche und Mikro-/Makro-Wechsel.

## Beschriftung

Jedes Bild soll die wichtigsten sichtbaren Dinge benennen.

Richtwert:

- 1–3 kurze deutsche Labels
- nur Schlüsselstrukturen oder Schlüsselprozesse
- eindeutige Zuordnung
- keine Textwände
- kein englischer sichtbarer Text
- fehlerhafte KI-Schrift = Regeneration oder exakt geplanter Remotion-Fallback

## Bild_01 – Cover + Hook + Master Style Frame

`Bild_01` ist bei jedem Video oder Reel:

- Cover
- erster Shot
- Master Style Frame
- Stilvorlage für alle weiteren Bilder

Darum wird Bild_01 besonders ausführlich beschrieben. Es enthält eine kurze starke deutsche Hook-Zeile zum Thema, normalerweise 3–7 Wörter.

Flow erzeugt zuerst ausschließlich Bild_01. Nach Nutzerfreigabe wird Bild_01 als Style-/Continuity-Referenz für alle restlichen Bilder verwendet.

## Flow-Prompts

- Prompt-Anweisungen immer Englisch
- sichtbare Hook-/Label-Texte immer Deutsch
- Bild_01 ausführlich
- Folgeprompts so kurz wie möglich, so genau wie nötig
- meist 2–5 Sätze pro Folgebild
- Szene + sichtbarer Prozess + Komposition + deutsche Labels
- globalen Stilblock nicht in jedem Prompt wiederholen

Details: `engine/FLOW-PRODUCTION-STANDARD.md`.

## 5er-Blöcke

Nach freigegebenem Bild_01:

```text
Bild_02–06
Bild_07–11
Bild_12–16
Bild_17–21
Bild_22–26
Bild_27–31
...
```

Jedes Bild innerhalb eines Blocks wird einzeln erzeugt und geprüft. Nach jedem Block folgt ein kurzer Stil-/Nummerierungscheck. Fehler kommen auf die Recovery-Liste.

## Präsentation / Remotion

Vollbild bleibt Standard. Zusätzlich sind kurze deutsche Überschriften, Keywords, Callouts und Vergleichsmarker erlaubt, wenn sie echten Erklärwert haben.

Keine doppelten Texte: Wenn Flow ein korrektes Label bereits im Bild trägt, soll Remotion denselben Begriff nicht unnötig erneut darüberlegen.

Details: `engine/PRESENTATION-OVERLAY-SYSTEM.md`.

## Repo-Gehirn

Vor Arbeit lesen:

1. `PROJECT_CONTRACT.md`
2. `PROJECT_STATE.md`
3. `AGENTS.md`
4. `config/channel.json`
5. `config/video.json`
6. `THEMEN-GEHIRN.md`
7. relevante `engine/*.md`
8. relevante `bildwelt/*.md`
9. aktuelles Video-Projekt

## Bildrhythmus

- Hook: meist 2–4 Sekunden
- normale Erklärbilder: meist 4–6 Sekunden
- komplexe Mikroprozesse: oft 3–5 Sekunden
- ruhige Übersichten: meist 6–8 Sekunden
- über 8 Sekunden nur mit bewusstem Grund

Keine Füllbilder. Lange Standzeiten dürfen nicht nur mit Zoom/Pan kaschiert werden.

## V2-Planung

Neue Projekte erhalten:

```text
05_info/mechanism-map.md
05_info/sentence-visual-plan.json
02_bildprompts/label-plan.json
02_bildprompts/image-review.json
04_export/quality-scorecard.md
04_export/postmortem.md
```

Ablauf:

```text
Recherche + Claims
→ Mechanism Map
→ Visual-First-Skript
→ Satz-Visual-Plan
→ semantische Szenen
→ Label-Plan
→ Flow: nur Bild_01
→ Nutzerfreigabe
→ 5er-Blöcke
→ Einzelbild-Review ≥ 8/10
→ Recovery
→ Voice + Worttimings
→ Remotion
→ Render
→ Qualitäts-Scorecard
→ Postmortem
```

Wissenschaftliche Sicherheit unter 8/10 ist harter Blocker.

## Drei Phasen

### Phase 1 – ChatGPT

```text
Thema
→ Recherche
→ Claim-Check
→ Mechanism Map
→ finales script.txt
→ Satz-Visual-Plan
→ Szenenplan
→ Label-Plan
→ Flow-Prompt
→ scene-map.json
→ overlay-plan.json
→ Metadaten
```

### Phase 2 – Nutzer + Voice-KI + Google Flow

```text
VOICEOVER-ZUM-KOPIEREN.txt → Voice-KI
GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt
→ nur Bild_01
→ Style-/Cover-Freigabe
→ 5er-Blöcke
→ Einzelbild-Review
→ Recovery-Pass
→ Bilder-ZIP
```

### Phase 3 – Antigravity + Tools + Remotion

```text
Audio vorbereiten
→ Flow-ZIP importieren
→ Assets validieren
→ faster-whisper
→ Script↔Audio-Ausrichtung
→ timeline.json
→ overlay-plan.json
→ Remotion
→ Render
→ Final-QA
→ Scorecard
→ Postmortem
```

## Aktueller Pilot – nächster Schritt

1. `youtube-videos/001-pilot-sauerstoff-im-blut/01_script/VOICEOVER-ZUM-KOPIEREN.txt` für die Voice verwenden.
2. `youtube-videos/001-pilot-sauerstoff-im-blut/02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt` vollständig in Flow geben.
3. Flow erzeugt **zuerst nur `Bild_01`** und stoppt.
4. Erst nach Freigabe folgen Bild_02 bis Bild_28 in den festgelegten Blöcken.

## Goldene Regel

**Nicht raten.** Wenn Script, Audio, Bildnummer, Szenengrenze oder wissenschaftliche Kernaussage nicht eindeutig ist, stoppt die technische Pipeline und der konkrete Fehler wird behoben.
