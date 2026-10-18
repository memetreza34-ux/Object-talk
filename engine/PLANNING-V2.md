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

Jedes neue Projekt erhaelt `.intern/05_info/sentence-visual-plan.json`.

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

## Neue verbindliche Bildregie ab Video 011 – mehr echte Erklärillustrationen

**Die Bildwelt bleibt Clean Animated Biology Illustration wie beim bewährten Verdauungsvideo – die BILDIDEE wird wesentlich besser.** Nicht jede Voice-Zeile mit einer Person, Küche oder einem beliebigen Teller bebildern. Zeige stattdessen die Sache, die der Zuschauer gerade VERSTEHEN soll. Beispiele:

- Hunger-Signal: vergrößerter Magen-Darm-Gehirn-Signalweg, KEINE Person vor dem Kühlschrank als Standard.
- Eiweiß/Sättigung: schön illustrierte Proteinquelle und dazu leicht verständliche innere Verdauungs-/Sättigungswirkung, nicht nur ein Mann mit Schüssel.
- Ballaststoffe: klarer Querschnitt von Fasern, Wasserbindung und Darm, statt weiterer Gemüsetisch-Aufnahme.
- Ganzer Apfel vs. Saft: essbarer Anschnitt, Faserstruktur, Flüssigkeit und eine optisch direkte Gegenüberstellung.
- Für Alltagstipps: Hände/Teilansicht, aussagekräftige Lebensmittel, echte Vorher/Nachher-Komposition oder kurzer visueller Ursache→Wirkung-Ablauf.

**Bildmix für neue lange Biologie-/Ernährungs-/Gesundheitsvideos:** Ziel mindestens 65 % erklärende Illustrationen (Makro, Querschnitt, Prozess, Funktionsweg, Mechanismus, lehrreicher Vergleich); höchstens 20 % menschenzentrierte Alltagsszenen, davon höchstens 10 % Ganzkörper-Mensch. Das sind PLANUNGSGRENZEN, nicht die Behauptung, dass ein fertiges Flow-Bild gut geworden ist. Bei anderen Themen können begründete Ausnahmen notwendig sein. Nach echten Flow-Bildern nochmals visuell prüfen.

**Mehr Farben, gleiche Welt:** helle Mint-/Creme-/Türkis-Basis bleibt ein Element, aber nicht 72 gleiche blasse Hintergründe. Je nach biologischem Vorgang bewusst kräftiges Korallrot, warmes Orange, Goldgelb, sattes Blau, Aquamarin, frisches Grün oder zurückhaltendes Violett nutzen. Farbakzente führen das Auge zur wichtigen Sache; keine grelle Leuchtreklame, kein einheitlicher Neonlook. Licht/Schatten, perspektivische Tiefe, klare hochwertige Illustration und große miteinander verbundene Formen statt flacher generischer Stockgrafik.

**Variantenreiches Erklären:** organische Cutaways, anatomische Ausschnitte, Schichten, geführte Wege, Lebensmittel-Innenstruktur, Vergrößerung, klarer 2-Zustandsvergleich, Vorher/Nachher, einfache visuelle Metapher mit wissenschaftlichem Bezug. Pro Szene nur eine Hauptidee, 2–4 lesbare relevante Elemente und 0–2 kurze passende deutsche Labels. Bild darf auch ein klares vollflächiges Schema/Diagramm sein, WENN es anschaulicher erklärt als eine Figur. Szenen kompositorisch wechseln; nicht alle mittig und nicht immer gleiche Vogelperspektive.

**Promptpflicht:** pro normalem Bild `VISUAL CATEGORY`, `HUMAN FRAMING`, `WHAT CHANGES VISIBLY`, konkretes Motiv/Prozess + ggf. 0–2 Labels planen. Die Ausgabe soll diese technischen Felder NIEMALS als Text im Bild darstellen. Fehlt der Erklärnutzen, neu konzipieren. Ganze Menschen nur bei echtem psychologischem/Alltags-Lernzweck, nicht als Füllmotiv.

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

Das YouTube-Cover ist **eine separate Datei `03_export/COVER.png`, niemals `Bild_01`**, niemals Teil der Szenen-ZIP oder Videotimeline. Es wird in Google Flow aus drei eigenständigen Varianten gewählt und zeigt genau einen sichtbaren Titeltext. Die nummerierten Video-Szenen beginnen direkt mit normalem `Bild_01`, ohne Cover-Schrift.
## 9. Label-Plan

Jedes neue Projekt erhaelt `.intern/05_info/label-plan.json`.

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

`.intern/03_pipeline/overlay-plan.json` bleibt leer / `DISABLED`.

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

Keine Bildvorlagen oder externen Stilreferenzen im Google-Flow-Workflow.

Das separate Cover ist niemals Style-Upload für die nachfolgenden Bilder.

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

## 16. Storyboard-v2 als einzige Quelle – Pflicht ab Video 011

Analyse 10/2026: Die Planungsdateien von 010 wurden mechanisch befüllt. `visual_type` rotierte durch acht Werte, `learning_goal` war der kopierte Satz, 24 Kamerabewegungen waren ungültig, und der Antigravity-Prompt blieb die Vorlage. Darum gilt:

1. Der Creative Director schreibt **eine** Datei: `.intern/05_info/storyboard-source.json` (`format: storyboard-v2`). Die Vorlage liegt in `youtube-videos/_TEMPLATE/.intern/05_info/storyboard-source.json`.
2. Pro Szene: `speech` (exakter Sprechtext, max. 19 Wörter / ca. 6,3 s), `cat` (visual category), `frame` (human framing), `scale`, `motion` (nur static, slow-push-in, slow-pull-out, pan-left, pan-right), `visual` (konkrete englische Bildkomposition), `shows` (was sichtbar erklärt wird), `goal` (deutsches Lernziel), `labels` (0–2), `claims`, `para` (Absatz danach).
3. Pro Kapitel: zuschauerfreundlicher `title` (wird zum YouTube-Kapitel), `function`, `misconception`.
4. Video-weit: `youtube` (Titel, 3 Alternativen, Beschreibung, Hashtags), `cover` (Text + 3 Optionen), `flow.continuity_key` (Farbcode/Leitmotiv), `open_loops` (setup_scene → payoff_scene).
5. Danach **nur** `python tools/build_phase1_package.py youtube-videos/VIDEO` ausführen. Skript, Flow-Prompt, phase1-scenes, sentence-visual-plan, label-plan, Caption-Entwurf und Antigravity-Auftrag werden erzeugt. Abgeleitete Dateien nie von Hand ändern.
6. Danach `python tools/validate_planning_v2.py youtube-videos/VIDEO` (inkl. Bildregie-, Bewegungs- und Skriptqualitäts-Gate).

Referenzbeispiele (nur Vorlage, keine Produktion): `examples/storyboard-v2/901-beispiel-hunger/` und `examples/storyboard-v2/902-beispiel-verdauung/`.
