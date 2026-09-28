# Object-Talk – Planning V2

Diese Datei gilt verbindlich fuer neue Projekte. `PROJECT_CONTRACT.md` bleibt die oberste Regel.

Zusaetzlich verbindlich:
`engine/VISIBLE-TEXT-STANDARD.md`

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
9. Welche Information kann weggelassen werden, ohne das Lernziel zu verlieren?
10. Braucht das Bild ueberhaupt ein Label?

Ein schoenes Themenbild ohne klaren Erklaerwert wird nicht produziert.

## 5. Visual-Storytelling-Mix

- mindestens etwa 60 % der normalen Explainerframes zeigen Prozess, Beziehung, Weg, Ursache/Wirkung, Vergleich, Vorher/Nachher oder Kontext
- maximal zwei isolierte Einzelobjekt-Portraits hintereinander
- danach Prozess-/Beziehungs-/Kontextbild
- benachbarte Szenen unterscheiden sich in mindestens zwei Dimensionen
- gleiche Uebersichtskomposition nicht ohne echten neuen Zweck wiederholen
- verschiedene Bildtypen nutzen: Cutaway, Querschnitt, Makro, Zell-Innenansicht, Transportweg, Vergleich, Massstabswechsel, Alltagsszene

## 6. Informationsbudget / Komplexitaetsplanung

Die freigegebene Bildwelt ist bewusst einfach.

Pro Bild bevorzugt:
- **1 Hauptaussage / 1 Hauptprozess**
- 2–4 zentrale sichtbare Elemente
- **0–2 kurze Labels**

Wenn ein Beat mehr verlangt:
1. unwichtige Information weglassen, oder
2. den Speech-Beat auf mehrere Bilder teilen.

**Mehr einfache Bilder sind besser als ein ueberladenes Bild.**

Ein Bildplan ist FAIL, wenn mehrere unabhaengige Lehrziele in einen Frame gepresst werden, obwohl sie sinnvoll getrennt werden koennen.

## 7. Bild-IDs

Jedes geplante Bild erhaelt genau eine stabile ID:
`Bild_01`, `Bild_02`, `Bild_03`, ...

Die ID ist Produktionsmetadaten und darf nie sichtbar im Bild erscheinen.

## 8. Cover-Regel

`Bild_01` ist das Cover-/Hook-Bild.

Es darf genau einen sichtbaren Textblock haben:
- nur den geplanten Titel / Hook
- keine Anatomie-Labels
- keine Unterzeile
- keine Zusatzinfo
- keine Pfeiltexte

Der Label-Plan fuer `Bild_01` muss deshalb `labels: []` und genau einen Eintrag in `allowed_visible_text` enthalten.

## 9. Label-Plan

Jedes Projekt erhaelt `02_bildprompts/label-plan.json`.

Regeln:
- viewer-facing Text nur Deutsch
- normale Bilder: **0–2 Labels, maximal 2**
- bevorzugt 0 oder 1, wenn das Bild bereits eindeutig ist
- Label bevorzugt 1–2 Woerter, maximal 3 Woerter
- nur wichtige Strukturen/Prozesse beschriften
- keine ganzen Voiceover-Saetze
- keine dekorativen Anfuehrungszeichen
- keine internen Nummern, Dateinamen oder Prompttitel
- Label muss eindeutig auf die richtige Struktur zeigen
- heller Hintergrund → dunkle Schrift
- dunkler Hintergrund → helle Schrift

Biologische Labels werden standardmaessig in Google Flow direkt im Bild erzeugt.

## 10. Prompt-Plan

Prompts muessen kurz bleiben.

Schema:
1. `bildwelt/FLOW-STYLE-BLOCK.txt`
2. konkrete Szene
3. sichtbarer Prozess
4. 0–2 exakte deutsche Labels nur wenn notwendig
5. Textkontrast / Platzierung
6. kurze Negativregel

Kein langer Style-Roman pro Szene.

Cover-Prompt muss explizit enthalten:
`Exactly one visible text block: the title only. No labels, no subtitle, no extra text.`

## 11. Remotion

Remotion erzeugt keinen sichtbaren Text.

`03_pipeline/overlay-plan.json` bleibt leer / `DISABLED`.

Remotion ist nur fuer:
- Audio
- Timing
- leichte Push-/Pull-/Pan-Bewegungen
- Schnitte
- dezente nicht-textliche Uebergaenge
- Render

## 12. Bildreview

Pflichtkriterien:
- scientific_accuracy >= 8/10
- voiceover_match >= 8/10
- immediate_clarity >= 8/10
- style_continuity >= 8/10
- composition >= 8/10
- complexity_control >= 8/10
- label_accuracy >= 8/10
- visible_text_whitelist = PASS
- text_contrast = PASS
- information_density = PASS
- label_count = PASS
- label_readability = PASS
- no_unnecessary_text = PASS
- no_visible_asset_id = PASS
- no_visible_scene_number = PASS
- no_visible_filename_or_prompt_heading = PASS
- single_retained_asset_for_scene = PASS
- ai_artifact_check = PASS
- scene_difference bestanden
- overall_score >= 8/10

Cover zusaetzlich:
- cover_title_only = PASS

## 13. Referenzsystem

Die schriftliche Bildwelt ist die oberste Stilautoritaet:
`bildwelt/BIOLOGY-ILLUSTRATION-WORLD.md`

Eine spaetere `assets/channel/STYLE_REFERENCE.png` ist nur zusaetzlicher visueller Anker nach Nutzerfreigabe.

Das Cover `Bild_01` ist nicht automatisch Style-Master fuer alle Folgeframes.

## 14. Schreib- und Produktionsprozess

1. Thema und Zuschauerfrage definieren
2. Quellen/Kernclaims pruefen
3. Mechanism Map bauen
4. mindestens 3 Hook-Varianten schreiben
5. staerkste Hook waehlen
6. Hook → Wendung → Payoff schreiben
7. komplettes Script glaetten
8. Script auf Visualisierbarkeit pruefen
9. Satz-Visual-Plan erstellen
10. fuer jeden Beat eine Hauptidee festlegen
11. ueberladene Beats auf mehrere Bilder teilen
12. Visual-Mix und Nachbarschaftsunterschiede pruefen
13. Label-Plan mit 0–2 Labels schreiben
14. Cover title-only pruefen
15. kurze Flow-Prompts aus dem kanonischen Styleblock bauen
16. Bilder einzeln erzeugen und Textkontrast/Informationsdichte pruefen
17. Phase 3 rendert nur Bilder + Voice + Bewegung

## 15. Hard FAIL

Planung/Produktion stoppen bei:
- schwachem / schulbuchartigem Einstieg
- Scriptbeat ohne klaren visuellen Zweck
- drei oder mehr isolierten Objektportraits hintereinander
- zu vielen fast gleichen Kompositionen
- mehr als einer konkurrierenden Hauptidee im Bild
- ueberladenem Bildplan
- mehr als 2 Labels in einem normalen Bild
- Zusatztext auf dem Cover
- Label mit mehr als 3 Woertern
- schwachem Textkontrast
- unnoetigen Labels oder Nebeninformationen
- internen Assetnamen als sichtbarem Text
- irgendeinem Remotion-Text
- alter 2.5D-/Premium-3D-Bildwelt statt der freigegebenen Illustrationswelt
