# Object-Talk – Project State

Letzte Aktualisierung: 26.09.2026

## Aktiver Produktionspilot

```text
youtube-videos/002-zucker-im-koerper/
```

Thema:

**Was passiert mit Zucker in deinem Körper?**

Cover-Hook:

**„So verarbeitet dein Körper Zucker“**

## Review des ersten Pilot-002-Renders

Der echte Render wurde geprüft. Die Bildwelt selbst ist brauchbar und bleibt bestehen. Die wichtigsten neuen Fehler waren:
- Cover-Hook tauchte in mehreren normalen Szenen erneut als große Überschrift auf
- Ursache: texttragendes Cover wurde als Style-Referenz weitergereicht und Flow übernahm Typografie/Komposition
- einige Bildfolgen wirkten zu ähnlich oder zu leer
- an wichtigen Mechanismusstellen fehlte gelegentlich ein zusätzlicher visueller Hinweis / Kapitelcue
- wiederkehrende Zustände wie Blutzucker wurden zu ähnlich komponiert

Diese Fehler sind jetzt als Pipeline-Regeln gehärtet.

## Neue Referenzlogik

Ab sofort:
1. textfreie kanalweite `STYLE_REFERENCE.png` verwenden, wenn vorhanden
2. sonst vor dem Cover eine textfreie `EPISODE_STYLE_REFERENCE.png` erzeugen
3. Cover `Bild_01` darf den Titel tragen
4. **Bild_01 wird NICHT mehr als Style-Referenz für Bild_02+ verwendet**
5. normale Szenen erhalten nur die textfreie Style-Referenz

Pilot-002-Prompt dafür:

```text
youtube-videos/002-zucker-im-koerper/02_bildprompts/STYLE-REFERENCE-PROMPT.txt
```

Ablage der Episode-Referenz:

```text
youtube-videos/002-zucker-im-koerper/02_bildprompts/references/EPISODE_STYLE_REFERENCE.png
```

## Cover-Hook-Hard-Lock

Die Hook **„So verarbeitet dein Körper Zucker“** darf exakt nur auf `Bild_01` erscheinen.

Für Bild_02–Bild_35 ist sie Hard FAIL:
- keine Wiederholung als Titel
- keine Kapitelüberschrift mit derselben Hook
- keine dekorative Hintergrundschrift
- keine nahezu identische Kurzfassung

`tools/validate_planning_v2.py` prüft jetzt bereits in Phase 1, dass die Cover-Hook nur einmal in der sichtbaren Text-Whitelist vorkommt.

## Visuelle Dichte / Abwechslung

Weiterhin:
- 35 eindeutige Bilder
- kein Bildasset doppelt in der Timeline
- max. 7 Sekunden pro Bild
- Voice 1.10x + Pausenkompression

Neu verschärft:
- ein dominanter Lehrpunkt pro Bild
- ca. 20–35 % wichtiger Mechanismusbilder dürfen EINEN sinnvollen Zusatzdetailpunkt haben
- maximal zwei isolierte Einzelobjekt-Portraits direkt hintereinander
- danach Prozess / Weg / Ursache-Wirkung / Vergleich / Kontext bevorzugen
- gleiche Übersichtskomposition später nicht wiederholen
- wiederkehrende Themen müssen neuen Maßstab, Zustand, Richtung oder visuellen Zweck zeigen

Bild-QA verlangt künftig zusätzlich:
- `visual_novelty >= 8/10`
- `information_value >= 8/10`
- `cover_hook_isolated = PASS`
- für Bild_02+ `text_free_reference_used = PASS`

## Zusätzliche Information im Schnitt

Pilot 002 besitzt jetzt einen sparsamen Kapitel-Overlay-Plan:

```text
youtube-videos/002-zucker-im-koerper/03_pipeline/overlay-plan.json
```

Einmalige Story-Beats:
- Aufnahme im Dünndarm
- Jetzt kommt Insulin
- Glukose wird Energie
- Nutzen oder speichern
- Zwischen den Mahlzeiten

Diese Overlays sind absichtlich kurz, wiederholen die Cover-Hook nicht und sollen keine Textwände erzeugen.

## Aktuelle Bildwelt

Verbindliche Richtung:

**moderne stilisierte 2.5D / Soft-3D Educational Illustration**

Leitidee:

**80 % animierte Illustration + 20 % Soft-3D-Tiefe + 0 % Medical-CGI.**

Die Bildwelt wird nicht erneut grundsätzlich geändert.

## Semantische Farben Pilot 002

- Glukose = Türkis/Cyan mit warm-goldenem Akzent
- Insulin = Blau
- Glukagon = Violett
- Blutgefäße = Coral-Rot
- Organe = Peach/Coral/Orange
- Glykogen = Amber/Gold
- ATP = warmes Gelb/Gold
- Fettzelle = Apricot/Gelb
- Hintergrund = Creme / helles Blau / weiches Beige

## Asset-Regeln

Cover:
- bis zu 3 Varianten vor Auswahl
- Nutzer wählt genau 1
- alle anderen Covervarianten danach löschen
- final genau ein `Bild_01.png`

Normale Bilder:
- genau ein retained asset pro Bildnummer
- FAIL ersetzt dieselbe Nummer
- keine v2/final2/copy/A/B/C-Versionen
- keine doppelten Bildassets
- sichtbarer Text nur nach `label-plan.json`
- interne Nummern/Dateinamen/Prompttitel nie sichtbar

## Pilot 002 – wichtige Dateien

```text
PROJECT_CONTRACT.md
engine/FLOW-AGENT-INSTRUCTIONS.md
engine/FLOW-PRODUCTION-STANDARD.md
config/channel.json
tools/validate_planning_v2.py
youtube-videos/002-zucker-im-koerper/02_bildprompts/STYLE-REFERENCE-PROMPT.txt
youtube-videos/002-zucker-im-koerper/02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt
youtube-videos/002-zucker-im-koerper/02_bildprompts/label-plan.json
youtube-videos/002-zucker-im-koerper/02_bildprompts/image-review.json
youtube-videos/002-zucker-im-koerper/03_pipeline/overlay-plan.json
youtube-videos/002-zucker-im-koerper/03_pipeline/ANTIGRAVITY-PROMPT-ZUM-KOPIEREN.txt
```

## Nächster echter Test

1. textfreie Episode-Style-Referenz erzeugen
2. Covervarianten daraus erzeugen, genau 1 behalten
3. Bild_02–Bild_35 nur mit textfreier Referenz erzeugen
4. bei jedem Bild Hook-Leak + Text-Whitelist + Novelty prüfen
5. Phase 3 mit dem neuen Overlay-Plan rendern
6. finalen Render erneut ansehen und vergleichen
