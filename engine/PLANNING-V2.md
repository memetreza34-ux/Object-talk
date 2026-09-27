# Object-Talk – Planning V2

Diese Datei gilt verbindlich fuer neue Projekte. `PROJECT_CONTRACT.md` bleibt die oberste Regel.

## Ziel

Recherche, Skript und Bilder werden gemeinsam geplant. Jeder wichtige Speech-Beat braucht bereits vor der Medienproduktion eine eindeutige visuelle Funktion, ein Lernziel und eine fachlich passende Bildidee.

## 1. Script zuerst richtig aufbauen

Vor dem finalen Szenenplan muss das Skript `engine/SCRIPT-STANDARD.md` bestehen.

Pflicht fuer den Einstieg:
- Satz 1 ist ein starker Hook
- bevorzugt direkte Frage, ueberraschende Aussage, Mythos, Alltagsraetsel oder Kontrast
- innerhalb von 1–2 Saetzen folgt eine Wendung / unerwartete Antwort
- innerhalb der ersten ca. 15 Sekunden ist der Payoff klar
- keine Schulbuch-Einleitung

## 2. Mechanism Map

Jedes neue Video erhaelt `05_info/mechanism-map.md`.

Der zentrale Mechanismus wird in klaren Schritten beschrieben:
`Ausgangszustand → Ausloeser → Weg/Verarbeitung → Wirkung → Ergebnis`

Fuer jeden Schritt:
- fachliche Kernaussage
- Claim-ID(s), falls vorhanden
- sichtbares Lernziel
- Massstabsebene
- moegliche Fehlinterpretation

## 3. Satz-Visual-Plan

Jedes neue Projekt erhaelt `05_info/sentence-visual-plan.json`.

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

- mindestens etwa 60 % der normalen Explainerframes zeigen Prozess, Beziehung, Weg, Ursache/Wirkung, Vergleich, Vorher/Nachher oder Kontext
- maximal zwei isolierte Einzelobjekt-Portraits hintereinander
- danach Prozess-/Beziehungs-/Kontextbild
- benachbarte Szenen unterscheiden sich in mindestens zwei Dimensionen
- gleiche Uebersichtskomposition nicht ohne echten neuen Zweck wiederholen
- verschiedene Bildtypen nutzen: Cutaway, Querschnitt, Makro, Zell-Innenansicht, Transportweg, Vergleich, Massstabswechsel, Alltagsszene

## 6. Komplexitaetsplanung

Die freigegebene Bildwelt ist bewusst einfach.

Pro Bild bevorzugt:
- 2–5 zentrale sichtbare Elemente
- 1 Hauptprozess
- 1–3 kurze Labels

Wenn ein Beat mehr verlangt, in mehrere Bilder teilen statt ein Bild zu ueberladen.

## 7. Bild-IDs

Jedes geplante Bild erhaelt genau eine stabile ID:
`Bild_01`, `Bild_02`, `Bild_03`, ...

Die ID ist Produktionsmetadaten und darf nie sichtbar im Bild erscheinen.

## 8. Label-Plan

Jedes Projekt erhaelt `02_bildprompts/label-plan.json`.

Regeln:
- viewer-facing Text nur Deutsch
- normalerweise 1–3 kurze Labels
- nur wichtige Strukturen/Prozesse beschriften
- keine ganzen Voiceover-Saetze
- keine internen Nummern, Dateinamen oder Prompttitel
- Label muss eindeutig auf die richtige Struktur zeigen

Biologische Labels werden standardmaessig in Google Flow direkt im Bild erzeugt.

## 9. Prompt-Plan

Prompts muessen kurz bleiben.

Schema:
1. `bildwelt/FLOW-STYLE-BLOCK.txt`
2. konkrete Szene
3. sichtbarer Prozess
4. exakte deutsche Labels
5. kurze Negativregel

Kein langer Style-Roman pro Szene.

## 10. Remotion-Praesentationsplan

Jedes neue Projekt prueft nach dem Szenenplan, ob wenige Praesentationspunkte helfen.

Datei:
`03_pipeline/overlay-plan.json`

Grundregel:
- Vollbild-Illustration bleibt Standard
- ca. 85–90 % ohne zusaetzliche Remotion-Texte
- Remotion nur fuer echte Strukturierung

Geeignet:
- Zwischenueberschrift bei grossem Abschnittswechsel
- sehr kurzer Key-Fact
- Summary-/Prozesszeile

Nicht geeignet:
- anatomische Labels
- Text fuer jede Szene
- ganze Voice-over-Saetze
- dauerhafte Rahmen/Balken/Seitenlayouts

Fuer ca. 2 Minuten normalerweise:
- 2–3 Zwischenueberschriften
- optional 1 Key-Fact oder Summary

Zwischenueberschrift bevorzugt auf der bereits sichtbaren naechsten Illustration fuer etwa 0.8–1.5 Sekunden.

## 11. Bildreview

Pflichtkriterien:
- scientific_accuracy >= 8/10
- voiceover_match >= 8/10
- immediate_clarity >= 8/10
- style_continuity >= 8/10
- composition >= 8/10
- visual_novelty >= 8/10
- information_value >= 8/10
- complexity_control >= 8/10
- labels_correct = PASS
- no_visible_asset_id = PASS
- single_retained_asset_for_scene = PASS
- ai_artifact_check = PASS
- scene_difference bestanden
- overall_score >= 8/10

## 12. Referenzsystem

Die schriftliche Bildwelt ist die oberste Stilautoritaet:
`bildwelt/BIOLOGY-ILLUSTRATION-WORLD.md`

Eine spaetere `assets/channel/STYLE_REFERENCE.png` ist nur zusaetzlicher visueller Anker nach Nutzerfreigabe.

Das Cover `Bild_01` ist nicht automatisch Style-Master fuer alle Folgeframes.

## 13. Schreib- und Produktionsprozess

1. Thema und Zuschauerfrage definieren
2. Quellen/Kernclaims pruefen
3. Mechanism Map bauen
4. mindestens 3 Hook-Varianten schreiben
5. staerkste Hook waehlen
6. Hook → Wendung → Payoff schreiben
7. komplettes Script glaetten
8. Script auf Visualisierbarkeit pruefen
9. Satz-Visual-Plan erstellen
10. Visual-Mix und Nachbarschaftsunterschiede pruefen
11. Label-Plan schreiben
12. kurze Flow-Prompts aus dem kanonischen Styleblock bauen
13. wenige sinnvolle Remotion-Praesentationspunkte in `overlay-plan.json` planen
14. Bilder einzeln erzeugen und pruefen
15. Phase 3 baut Vollbild-Illustrationen + selektive Overlays

## 14. Hard FAIL

Planung/Produktion stoppen bei:
- schwachem / schulbuchartigem Einstieg
- Scriptbeat ohne klaren visuellen Zweck
- drei oder mehr isolierten Objektportraits hintereinander
- zu vielen fast gleichen Kompositionen
- ueberladenem Bildplan
- mehr Labels als fuer das Verstaendnis noetig
- internen Assetnamen als sichtbarem Text
- Remotion-Text auf fast jeder Szene
- dauerhafter PowerPoint-/Dashboard-Aufteilung statt Vollbild-Illustration
- alter 2.5D-/Premium-3D-Bildwelt statt der freigegebenen Illustrationswelt
