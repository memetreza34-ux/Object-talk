# Object-Talk – Planning V2

Diese Datei ergänzt die bestehende Longform-Pipeline, ohne Video 001 oder bestehende Projekte rückwirkend zu brechen. Sie gilt verbindlich für **neu angelegte Projekte ab V2**. `PROJECT_CONTRACT.md` bleibt die oberste Regel.

## Ziel

Recherche, Skript und Bilder werden nicht getrennt geplant. Jeder wichtige Satz muss bereits vor Google Flow eine eindeutige visuelle Funktion, ein Lernziel und eine fachlich passende Bildidee besitzen.

## 1. Mechanism Map

Jedes neue Video erhält:

```text
05_info/mechanism-map.md
```

Darin wird der zentrale Mechanismus vor dem finalen Skript in 3–12 klaren Schritten beschrieben:

```text
Ausgangszustand → Auslöser → Weg/Verarbeitung → Wirkung → Ergebnis
```

Für jeden Schritt werden festgehalten:

- fachliche Kernaussage
- zugehörige Claim-ID(s)
- was der Zuschauer sichtbar verstehen soll
- geeignete Maßstabsebene: Lebensmittel / Mensch / Organ / Gewebe / Blut / Zelle / Organell / Molekül
- mögliche Fehlinterpretation, die vermieden werden muss

Ein Video darf mehrere Untermechanismen besitzen, aber es braucht eine klar erkennbare Hauptkette.

## 2. Satz-Visual-Plan

Jedes neue Projekt erhält:

```text
05_info/sentence-visual-plan.json
```

Jeder gesprochene Satz oder logisch untrennbare Satzblock besitzt mindestens:

- `id`
- `voiceover_text`
- `function`
- `learning_goal`
- `claim_ids`
- `scale_level`
- `new_image_required`
- `image_asset_id`
- `visual_type`
- `visible_change`
- `scene_difference`
- `labels`
- `misconception_to_avoid`

Erlaubte `function`-Werte:

```text
observation
trigger
path
comparison
threshold
wirkung
result
```

Erlaubte `visual_type`-Werte:

```text
single-image
cutaway
transparent-body
macro-detail
comparison
two-in-one
three-in-one
four-in-one
before-after
scale-transition-frame
```

## 3. Kein Bild nur als Dekoration

Vor jedem Bildprompt muss beantwortet sein:

1. Was sagt das Voice-over konkret?
2. Welches Objekt oder welche Struktur trägt die Aussage?
3. Was verändert sich sichtbar?
4. Wo beginnt der Prozess?
5. Wo endet er?
6. Was darf der Zuschauer nicht falsch verstehen?
7. Warum ist genau diese Perspektive geeignet?
8. Wie unterscheidet sich das Bild sichtbar vom vorherigen und nächsten Bild?

Ein schönes Themenbild ohne klaren Erklärwert wird nicht produziert.

## 4. Bild-IDs und Szenenkontinuität

Jedes geplante Bild erhält genau eine stabile ID:

```text
Bild_01
Bild_02
Bild_03
...
```

Diese ID bleibt in allen Projektdateien identisch: Satz-Visual-Plan, `phase1-scenes.json`, Flow-Prompt, `scene-map.json`, Label-Plan und Bildreview.

Bestehende Nummerierungs- und Recovery-Regeln bleiben unverändert.

## 5. Label-Plan

Jedes neue Projekt erhält:

```text
02_bildprompts/label-plan.json
```

Pro Bild werden nur die wirklich nötigen deutschen Labels festgelegt. Richtwert:

- 0–3 Labels pro Bild
- kurze Fachbegriffe statt ganzer Sätze
- offensichtliche Objekte nicht unnötig beschriften
- exakte Schreibweise vor der Generierung festlegen
- bei falscher KI-Schrift muss exakt derselbe Begriff später als Overlay ersetzt werden

Jeder Eintrag enthält:

- `image_asset_id`
- `mode`: `required` oder `optional`
- `labels`
- `target`
- `reason`
- `fallback_overlay`

## 6. Bildreview

Jedes neue Projekt erhält:

```text
02_bildprompts/image-review.json
```

Jedes akzeptierte Bild wird einzeln geprüft. Mindestziel: **8/10**.

Pflichtkriterien:

- fachlich korrekt oder plausibel vereinfacht
- exakte Voice-over-Aussage sichtbar
- Hauptmotiv sofort verständlich
- Stil-/Episode-Kontinuität vorhanden
- richtige Maßstabsebene
- Labels korrekt
- keine störenden KI-Artefakte
- keine unnötige Textlast
- Szene unterscheidet sich sinnvoll von Nachbarbildern

Ein starkes Nachbarbild gleicht kein schwaches Einzelbild aus.

## 7. Character-Regel

Der bestehende Contract bleibt unverändert: Object-Talk ist kein dauerhafter Mascot-/Presenter-Kanal.

Personifizierte Lebensmittel sind nur dann erlaubt, wenn sie den Lerninhalt verbessern. Der Mechanismus muss immer auch ohne eine Sprecherfigur verständlich bleiben.

## 8. Kompatibilität

- Video 001 bleibt unverändert und darf mit seinem bestehenden Phase-1-Stand weiterlaufen.
- Neue V2-Dateien werden automatisch von `_TEMPLATE` in zukünftige Projekte kopiert.
- Bestehende Phase-3-Tools werden nicht verändert.
- Keine V2-Datei darf bestehende Script-, Audio-, Bildnummern- oder Timeline-Daten still überschreiben.
