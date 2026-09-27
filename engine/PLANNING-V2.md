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
- ca. 20–35 % wichtiger Mechanismusframes duerfen einen sinnvollen Zusatzdetailpunkt tragen

## 6. Bild-IDs

Jedes geplante Bild erhaelt genau eine stabile ID:
`Bild_01`, `Bild_02`, `Bild_03`, ...

Die ID ist Produktionsmetadaten und darf nie sichtbar im Bild erscheinen.

## 7. Text-/Label-Plan

Jedes neue Projekt darf einen `02_bildprompts/label-plan.json` erhalten.

Inhaltlich planen:
- welche Begriffe wirklich sichtbar sein muessen
- viewer-facing Text nur Deutsch
- keine internen Nummern, Dateinamen oder Prompttitel
- keine Textwaende

WICHTIG: Ob finaler Text im Bildgenerator oder spaeter im Editor erzeugt wird, ist aktuell noch NICHT festgelegt und wird zusammen mit der neuen Bildwelt entschieden.

## 8. Overlay-Plan

Keine dauerhafte globale Regel, solange die neue Bildwelt nicht festgelegt ist. Text-Overlays duerfen weder automatisch erzwungen noch automatisch verboten werden. Die Entscheidung faellt mit dem neuen visuellen System.

## 9. Bildreview

Unabhaengige Pflichtkriterien:
- scientific_accuracy >= 8/10
- voiceover_match >= 8/10
- immediate_clarity >= 8/10
- composition >= 8/10
- visual_novelty >= 8/10
- information_value >= 8/10
- no_visible_asset_id = PASS
- single_retained_asset_for_scene = PASS
- ai_artifact_check = PASS
- scene_difference bestanden
- overall_score >= 8/10

Style-spezifische Kriterien wie `style_continuity` werden nach Auswahl der neuen Bildwelt konkretisiert.

## 10. Referenzsystem

Aktuell OFFEN.

Keine alte Regel fuer `STYLE_REFERENCE.png`, `EPISODE_STYLE_REFERENCE.png` oder `Bild_01` als Stilanker automatisch uebernehmen.
Das neue Referenzsystem wird erst nach Auswahl und Test der neuen Bildwelt definiert.

## 11. Schreib- und Produktionsprozess

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
11. Label-/Textbedarf planen
12. STYLE GATE pruefen
13. erst nach Style-Freigabe Generierungs-Prompts finalisieren

## 12. Hard FAIL

Planung stoppen bei:
- schwachem / schulbuchartigem Einstieg
- erstem Beat ohne Hook-Funktion
- Scriptbeat ohne klaren visuellen Zweck
- drei oder mehr isolierten Objektportraits hintereinander
- zu vielen fast gleichen Kompositionen
- internen Assetnamen als sichtbarem Text
- Versuch, eine historische Bildwelt vor neuer Nutzerfreigabe wieder als Kanalstandard einzusetzen
