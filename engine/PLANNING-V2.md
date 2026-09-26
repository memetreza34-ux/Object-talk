# Object-Talk – Planning V2

Diese Datei gilt verbindlich fuer neue Projekte. `PROJECT_CONTRACT.md` bleibt die oberste Regel.

## Ziel

Recherche, Skript und Bilder werden gemeinsam geplant. Jeder wichtige Speech-Beat braucht bereits vor Google Flow eine eindeutige visuelle Funktion, ein Lernziel und eine fachlich passende Bildidee.

## 1. Script zuerst richtig aufbauen

Vor dem finalen Szenenplan muss das Skript `engine/SCRIPT-STANDARD.md` bestehen.

Pflicht fuer den Einstieg:
- Satz 1 ist ein starker Hook
- bevorzugt direkte Frage, ueberraschende Aussage, Mythos, Alltagsraetsel oder Kontrast
- besonders geeignet: `Hast du dich schon mal gefragt, warum ...?`
- innerhalb von 1–2 Saetzen folgt eine Wendung / unerwartete Antwort
- innerhalb der ersten ca. 15 Sekunden ist der Payoff klar
- keine Schulbuch-Einleitung

## 2. Mechanism Map

Jedes neue Video erhaelt:

```text
05_info/mechanism-map.md
```

Darin wird der zentrale Mechanismus vor dem finalen Skript in 3–12 klaren Schritten beschrieben:

```text
Ausgangszustand → Ausloeser → Weg/Verarbeitung → Wirkung → Ergebnis
```

Fuer jeden Schritt werden festgehalten:
- fachliche Kernaussage
- Claim-ID(s), falls vorhanden
- was der Zuschauer sichtbar verstehen soll
- Massstabsebene
- moegliche Fehlinterpretation

## 3. Satz-Visual-Plan

Jedes neue Projekt erhaelt:

```text
05_info/sentence-visual-plan.json
```

Jeder Speech-Beat besitzt mindestens:
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

Der erste Eintrag muss `function: hook` besitzen.

## 4. Kein Bild nur als Dekoration

Vor jedem Bildprompt beantworten:
1. Was sagt das Voiceover konkret?
2. Was muss sichtbar passieren?
3. Was ist Ursache und was Folge?
4. Wo beginnt und endet der Prozess?
5. Welcher Massstab ist am klarsten?
6. Was darf der Zuschauer nicht falsch verstehen?
7. Warum ist genau diese Perspektive geeignet?
8. Wie unterscheidet sich das Bild sichtbar vom vorherigen UND naechsten Bild?

Ein schoenes Themenbild ohne klaren Erklaerwert wird nicht produziert.

## 5. Visual-Storytelling-Mix

Der Kanal darf nicht aus aehnlichen Objektportraits bestehen.

Verbindlich:
- mindestens etwa 60 % der normalen Explainerframes zeigen Prozess, Beziehung, Weg, Ursache/Wirkung, Vergleich, Vorher/Nachher oder Kontext
- maximal zwei isolierte Einzelobjekt-Portraits hintereinander
- danach muss ein Prozess-/Beziehungs-/Kontextbild folgen
- benachbarte Szenen unterscheiden sich in mindestens zwei Dimensionen: Kameramassstab, Layout, Hauptmotiv, Richtung, Kontext oder Visual-Typ
- gleiche Uebersichtskomposition nicht spaeter erneut verwenden, ausser ein echter Vorher/Nachher-Vergleich verlangt es
- ca. 20–35 % wichtiger Mechanismusframes duerfen genau einen sinnvollen Zusatzdetailpunkt tragen

## 6. Bild-IDs und Szenenkontinuitaet

Jedes geplante Bild erhaelt genau eine stabile ID:

```text
Bild_01
Bild_02
Bild_03
...
```

Die ID bleibt in allen Projektdateien identisch.

Die ID ist reine Produktionsmetadaten und darf nie sichtbar im Bild erscheinen.

## 7. Label-Plan – Flow ist die einzige Textquelle

Jedes neue Projekt erhaelt:

```text
02_bildprompts/label-plan.json
```

Pro Bild werden nur wirklich noetige deutsche Texte freigegeben.

Richtwert:
- Cover: exakte Hook und sonst nichts
- normale Bilder: 0–2 kurze Labels bevorzugt
- maximal 3 nur bei echtem Bedarf
- keine ganzen Voiceover-Saetze
- keine internen Nummern / Dateinamen / Prompttitel
- Cover-Hook nach Bild_01 verboten

Wichtig:
- Google Flow erzeugt den final sichtbaren Text
- falsche Flow-Schrift wird in Flow regeneriert oder korrigiert
- `fallback_overlay` darf fuer neue Projekte nicht auf Remotion verweisen
- Remotion-Text ist verboten

## 8. Overlay-Plan

Neue Projekte verwenden keine Remotion-Textoverlays.

`03_pipeline/overlay-plan.json` muss so aussehen:

```json
{
  "status": "DISABLED",
  "reason": "All visible text is generated in Google Flow",
  "scenes": []
}
```

Nicht-leere Overlays sind ein Hard FAIL.

## 9. Bildreview

Jedes neue Projekt erhaelt:

```text
02_bildprompts/image-review.json
```

Pflichtkriterien pro akzeptiertem Bild:
- scientific_accuracy >= 8/10
- voiceover_match >= 8/10
- immediate_clarity >= 8/10
- style_continuity >= 8/10
- composition >= 8/10
- visual_novelty >= 8/10
- information_value >= 8/10
- visible_text_whitelist = PASS
- cover_hook_isolated = PASS
- no_visible_asset_id = PASS
- single_retained_asset_for_scene = PASS
- ai_artifact_check = PASS
- scene_difference bestanden
- overall_score >= 8/10

Ein starkes Nachbarbild gleicht kein schwaches Einzelbild aus.

## 10. Reference-First

Normale Szenen nutzen nur textfreie Stilreferenzen:
1. `STYLE_REFERENCE.png`
2. `EPISODE_STYLE_REFERENCE.png`
3. Objekt-/Character-Referenzen
4. Szenenprompt

Das texttragende `Bild_01` wird nicht als Follow-up-Style-Referenz verwendet.

## 11. Schreib- und Produktionsprozess

```text
1. Thema und Zuschauerfrage definieren
2. Quellen/Kernclaims pruefen
3. Mechanism Map bauen
4. mindestens 3 Hook-Varianten schreiben
5. staerkste Hook waehlen
6. Hook → Wendung → Payoff schreiben
7. komplettes Script glätten
8. Script auf Visualisierbarkeit pruefen
9. Satz-Visual-Plan erstellen
10. Visual-Mix und Nachbarschaftsunterschiede pruefen
11. Label-Plan fuer Flow schreiben
12. Flow-Prompts erstellen
13. overlay-plan.json leer lassen
14. erst danach Phase 2 starten
```

## 12. Hard FAIL

Planung stoppen bei:
- schwachem / schulbuchartigem Einstieg
- erstem Beat ohne Hook-Funktion
- Scriptbeat ohne klaren visuellen Zweck
- drei oder mehr isolierten Objektportraits hintereinander
- zu vielen fast gleichen Kompositionen
- geplantem Remotion-Text
- Flow-Text ausserhalb der Whitelist
- Cover-Hook nach Bild_01
- texttragendem Cover als Follow-up-Referenz
