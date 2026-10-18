# Themen-Gehirn

Diese Datei ist das **Gedächtnis für alle langen YouTube-Videos** des Kanals **Lebenslogik** (technischer Repo-Name Object-Talk).

## Zweck

Bevor ein neues Video-Thema ausgewählt wird, muss diese Datei geprüft werden.

Ziele:

- keine Themen doppelt produzieren
- keine fast identischen Videos mit nur anderem Titel erstellen
- bereits behandelte Teilfragen erkennen
- neue Themen sinnvoll aufeinander aufbauen
- langfristig eine breite Bibliothek zu Ernährung, Gesundheit und Biologie entwickeln

## Regel für normale neue Themen

Ein normales Kanalvideo darf nur gewählt werden, wenn es:

1. noch nicht produziert wurde
2. nicht nur eine umformulierte Version eines bestehenden Videos ist
3. genug Inhalt für mindestens **5 Minuten** bietet
4. mit Bildern verständlich erklärt werden kann
5. zum Kanalbereich Ernährung, Gesundheit oder Biologie passt
6. einen klaren Lernwert besitzt

Interne `TEST`-Piloten sind davon ausgenommen, wenn sie ausschließlich Pipeline/Stil prüfen und über `05_info/test-mode.json` ausdrücklich gekennzeichnet sind. Sie reservieren ein Thema nicht automatisch für die spätere Longform-Produktion.

## Status-System

- `IDEE` = vorgemerkt, aber noch nicht produziert
- `IN ARBEIT` = normales Kanalvideo aktuell in Produktion
- `FERTIG` = normales Video vollständig geplant/produziert
- `VERWORFEN` = bewusst nicht weiterverfolgt
- `TEST` = interner Pipeline-/Stilpilot; zählt nicht automatisch als veröffentlichtes Thema

## Themen-Datenbank

| Nr. | Status | Hauptbereich | Thema | Kernaussage / Abgrenzung | Überschneidet sich mit |
|---:|---|---|---|---|---|
| 001 | FERTIG (gerendert, 008) | Verdauung | Was passiert mit Essen im Körper? | erstes reguläres Longform-Video; kompletter Weg Mund → Speiseröhre → Magen → Dünndarm → Blut/Lymphe → Dickdarm/Enddarm | – |
| 002 | IDEE | Zellbiologie | Was ist eine menschliche Zelle? | Aufbau und wichtigste Zellbestandteile verständlich erklären | – |
| 003 | IDEE | Gehirn | Wie kommunizieren Nervenzellen? | Neuron, elektrisches Signal, Synapse, Neurotransmitter | – |
| 004 | IDEE | Ernährung | Was macht Zucker im Körper? | spätere Longform: Aufnahme, Blutzucker, Insulin, Energie und Überschuss deutlich tiefer | Testpiloten 000/002 behandeln nur die Grundkette |
| 005 | IDEE | Kreislauf | Wie transportiert Blut Sauerstoff? | spätere Longform: Sauerstofftransport deutlich tiefer, ggf. Sättigung, Belastung, Regulation | Testpiloten 001/005 behandeln nur die Grundreise |
| 006 | IDEE | Immunsystem | Wie bekämpft der Körper Bakterien? | angeborene Immunabwehr vereinfacht erklären | Pilot 006 berührt Immunzellen nur im Kontext Wundheilung |
| 007 | IDEE | Ernährung | Was passiert nach einer proteinreichen Mahlzeit? | Verdauung von Protein, Aminosäuren und Nutzung im Körper | Testpilot 003 berührt Protein nur als Baustoff für Muskelanpassung |
| 008 | IN ARBEIT | Schlaf | Was passiert im Körper, während wir schlafen? | Gehirn, Erholung, Gedächtnis, Hormone und Schlafphasen als Überblick | – |
| 009 | IDEE | Muskeln | Wie wächst ein Muskel? | spätere Longform: Training, Hypertrophie, Proteinsynthese, Ernährung, Regeneration und Progression deutlich tiefer | Testpilot 003 behandelt nur vereinfachte Grundkette |
| 010 | IDEE | Gehirn | Wie entsteht eine Erinnerung? | Verarbeitung, Synapsen und Gedächtnisbildung vereinfacht | 003 teilweise |
| 011 | IDEE | Haut | Wie heilt eine Wunde? | spätere Longform: Hämostase, Entzündung, Proliferation, Remodeling und Narbenbildung deutlich tiefer | Testpilot 006 behandelt nur die vereinfachte Grundkette |
| 012 | IDEE | Haut/Nervensystem | Warum bekommen wir Gänsehaut? | spätere Longform könnte Thermoregulation, autonome Reaktionen und emotionale Piloerektion vertiefen | Testpilot 007 behandelt nur die kurze Grundkette |
| 013 | FERTIG (gerendert, 010) | Ernährung / Sättigung | Warum bist du nach dem Essen schnell wieder hungrig? | 010: Magen-Gehirn-Signale, Protein, Ballaststoffe, Getränke, Snacks, Schlaf/Stress und praxistaugliche Mahlzeitideen | 008 erklärt den Verdauungsweg, 010 dagegen Hunger und Sättigung |
| 014 | IN ARBEIT | Ernährung / Sättigung | Warum du kurz nach dem Essen schon wieder Hunger hast (V2) | Neuauflage von 010 auf Nutzerwunsch: Ghrelin-Kalender, Dehnung vs. Darmhormone (CCK, GLP-1, PYY), sechs Gründe mit Studien (Esstempo, Saft, Sattmacher/Blutzucker-Dips, stark verarbeitet, Schlaf, Appetit/Nachtisch), fünf Tipps; Projekt `011-longform-hunger-v2` | ersetzt Projekt `010-longform-hunger` als Kanalversion; Projekt `012-longform-verdauung-v2` verlinkt darauf |
| 015 | IN ARBEIT | Verdauung | Die Reise einer Pizza durch deinen Körper (V2) | Neuauflage von 008 auf Nutzerwunsch: fünf Stationen mit Pizza-Farbcode, Tennisplatz-Mythos, zwei Wege Blut/Lymphe, 9 Liter, 38 Billionen Bakterien, Woraus besteht der Rest und warum braun; Projekt `012-longform-verdauung-v2` | ersetzt Projekt `008-longform-verdauung` als Kanalversion; Projekt `011-longform-hunger-v2` verlinkt darauf |

## Aktive Longform-Produktion

**Aktiv (Stand 18.10.2026):** Thema 014 → Projekt `youtube-videos/011-longform-hunger-v2/` und Thema 015 → Projekt `youtube-videos/012-longform-verdauung-v2/`, beide Phase 1 PASS, Medien ausstehend. Die folgenden Abschnitte zu 010, 001 und 009 sind historisch.

### 010 – Warum du nach dem Essen so schnell wieder Hunger hast? (historisch, gerendert)

Projekt: `youtube-videos/010-longform-hunger/`. **Damaliger Phase-1-Stand (inzwischen gerendert, 368,9 s):** 1.044 gesprochene Wörter, 72 einfache bildspezifische Szenen, ein Google-Flow-Prompt mit drei separaten Coverentwürfen vor Nutzerwahl. Kein neuer Verdauungsfilm, sondern Hunger-/Sättigungsmechanismen mit alltagstauglichen Tipps. Wissenschaftliche Einschränkungen beachten, keine Abnehmgarantien. Quelle/Planung `010/.intern/05_info/`. Nutzername des Kanals: **Lebenslogik** (GitHub-Projekt weiterhin Object-Talk).


### 001 – Was passiert mit Essen im Körper?

Projekt:

```text
youtube-videos/008-longform-verdauung/
```

Status: `FERTIG` (gerendert; Neuauflage als Thema 015 / Projekt 012)

Ziel:
- erstes reguläres Longform-Video nach Abschluss der Testphase
- 6–7 Minuten
- ca. 1.110 Wörter Script
- 77 eindeutige Bilder
- kompletter Verdauungsweg mit Aufnahme und Weitertransport der Nährstoffe
- saubere Trennung von Blutweg und Lymphweg
- klare Einleitung, kausaler Hauptteil und vollständiger Schluss

Abgrenzung:
- behandelt den gesamten Verdauungsweg als Überblick
- spätere Videos können einzelne Teilthemen wie Zucker, Protein, Mikrobiom oder Leber deutlich tiefer behandeln

## Longform-Produktion 009 – Schlaf

Projekt: `youtube-videos/009-longform-schlaf/`

**Status: IN ARBEIT – Phase 1 nach Video 008 neu aufgebaut.** 6–7 Minuten geplant; 986 Wörter und 77 verschiedene Bilder. Schlafdruck/Adenosin, circadiane Uhr/Melatonin, NREM-Stufen/Tiefschlaf, Kreislauf/Hormone, Gedächtnis, Immunsystem, REM/Träume und zyklischer Verlauf. Wissenschaftlicher Rahmen NIH/NHLBI/NICHD/CDC. Kein Video zu Schlafstörungen oder individuellem Therapierat.

## Interne Tests

### TEST 000 – Zucker im Blut

Projekt:

```text
youtube-videos/000-pilot-zucker-im-blut/
```

Status: `TEST`

Zweck:
- ca. 2 Minuten
- V2-Mechanism-Map testen
- Satz-Visual-Plan testen
- echte faceless Erklärbilder statt Mascot testen
- Bild_01 als Style-Anker testen
- hohe Bilddichte testen
- Whisper/Remotion/QA in kurzer Form testen

Inhaltlich behandelt der Test nur diese Grundkette:

`Snack → Dünndarm → Glukose → Blut → Betazellen/Insulin → Zellen/Glykogenspeicher`

**Dieser Test blockiert Thema 004 nicht.**

### TEST 001 – Sauerstoff von der Lunge bis zur Zelle

Projekt:

```text
youtube-videos/001-pilot-sauerstoff-im-blut/
```

Status: `TEST`

Zweck:
- ca. 2–2,5 Minuten
- zweite End-to-End-Runde
- Sauerstoffreise als komplexere Maßstabskette
- Bilddichte, Flow, Whisper, Remotion und QA testen

Inhaltlich behandelt der Test nur diese Grundkette:

`Einatmen → Alveolen → O₂ ins Blut → Hämoglobin/RBC → linkes Herz → Gewebe/Kapillare → Zelle/Mitochondrium → CO₂ zurück zur Lunge`

**Dieser Test blockiert Thema 005 nicht.**

### TEST 002 – Zucker im Körper

Projekt:

```text
youtube-videos/002-zucker-im-koerper/
```

Status: `TEST`

Zweck:
- ca. 2–2,5 Minuten
- 35 eindeutige Visual-Beats
- 1.10x-Voice und Pausenkompression testen
- Text-Whitelist und eindeutige Bildnummern testen
- damalige 2.5D/Soft-3D-Bildwelt testen
- Cover-Hook-Leak und visuelle Wiederholungen im echten Render erkennen

Inhaltlich behandelt der Test vereinfacht:

`Nahrung → Dünndarm → Glukose → Blut/Leber → Insulin → Zellaufnahme/ATP → Glykogen/Fett → Glukagon`

**Dieser Test blockiert Thema 004 nicht.**

### TEST 003 – Muskelwachstum

Projekt:

```text
youtube-videos/003-pilot-muskelwachstum/
```

Status: `TEST`

Zweck:
- ca. 2:05–2:30 Minuten
- 35 eindeutige Visual-Beats
- Hook-Isolation testen
- textfreie Episode-Style-Referenz testen
- stärkere visuelle Abwechslung testen
- informationsreichere Mechanismusbilder ohne Textwand testen
- Muskelkater-/Mikroriss-Mythos fachlich sauber vermeiden

Inhaltlich behandelt der Test vereinfacht:

`Widerstand → mechanische Spannung → Zell-Signal → Proteinsynthese → Aminosäuren → Myofibrillen → Hypertrophie → Erholung → Progression`

**Dieser Test blockiert Thema 009 nicht.** Eine spätere Longform darf Muskelwachstum deutlich tiefer erklären.

### TEST 004 – Muskelkater

Projekt:

```text
youtube-videos/004-pilot-muskelkater/
```

Status: `TEST`

Zweck:
- verzögerten Muskelkater verständlich erklären
- stärkeren Frage-Hook testen
- hohe visuelle Abwechslung über Alltag, Muskel, Nerven und Zeitverlauf testen
- Laktat-Mythos und Trainingsqualitäts-Mythos sauber vermeiden
- Übergang von alter Bildwelt zur später neu definierten Kanalwelt dokumentieren

Inhaltlich behandelt der Test vereinfacht:

`ungewohnte/exzentrische Belastung → strukturelle Beanspruchung → Reparatur-/Entzündungsprozesse → sensibilisierte Schmerzrezeptoren → verzögerter Schmerz → Anpassung`

### TEST 005 – Sauerstoff bis zur Zelle

Projekt:

```text
youtube-videos/005-pilot-sauerstoff-zelle/
```

Status: `TEST`

Zweck:
- erster kompletter Test der **Clean Animated Biology Illustration**
- maximal 2:00 Minuten
- 22 eindeutige Bilder
- neue Bildwelt über Lunge, Blut, Herz, Zelle und Mitochondrium testen
- einfache biologische Beschriftungen direkt in Flow testen

Inhaltlich behandelt der Test vereinfacht:

`Einatmen → Lungenbläschen → Sauerstoff ins Blut → Hämoglobin → Herz/Kreislauf → Kapillare → Zelle → Mitochondrium`

**Dieser Test blockiert Thema 005 nicht.** Eine spätere Longform darf Sauerstofftransport deutlich tiefer behandeln.

### TEST 006 – Wundheilung

Projekt:

```text
youtube-videos/006-pilot-wundheilung/
```

Status: `TEST`

Zweck:
- maximal 2:00 Minuten
- 22 eindeutige Bilder
- Clean Animated Biology Illustration über Haut, Blut, Gerinnung, Immunzellen und Gewebereparatur testen
- 100 % Vollbild-Illustration mit 0 sichtbarem Remotion-Text
- verständliche biologische Prozesskette ohne Detailüberladung testen

Inhaltlich behandelt der Test vereinfacht:

`Schnitt → Gefäßverletzung/Verengung → Blutplättchen → Fibrinnetz/Gerinnsel → Immunzellen/Aufräumen → Fibroblasten/Kollagen → neue Gefäße → Hautschluss → Remodeling/Narbe`

**Dieser Test blockiert Thema 011 nicht.** Eine spätere Longform darf Wundheilung wesentlich tiefer und mit weiteren Einflussfaktoren erklären.

### TEST 007 – Gänsehaut

Projekt:

```text
youtube-videos/007-pilot-gaensehaut/
```

Status: `TEST`

Zweck:
- maximal 2:00 Minuten
- 20 eindeutige Bilder
- Clean Animated Biology Illustration über Haut, Nervensignal, Haarfollikel, Haaraufrichtemuskel und Tierfell testen
- Kälte und starke Gefühle als unterschiedliche Auslöser derselben lokalen Piloerektionsreaktion erklären
- 100 % Vollbild-Illustration mit 0 sichtbarem Remotion-Text
- sichtbare Produktionsnummern konsequent verhindern
- **nach erstem Render dauerhafte Text-/Dichte-Lehren festlegen:** Cover nur Titel, normale Bilder max. 2 Labels, hoher Textkontrast, unnötige Beschriftungen weglassen, überladene Beats auf mehrere Bilder teilen

Inhaltlich behandelt der Test vereinfacht:

`Kälte/Emotion → Nervensystem → sympathisches Signal → Haaraufrichtemuskel → Haar richtet sich auf → Haut hebt sich → Gänsehaut`

Zusatzkontext:
`dichtes Tierfell → größere Luftschicht / größere Körperkontur; beim Menschen deutlich schwächerer Nutzen`

**Dieser Test blockiert Thema 012 nicht.** Eine spätere Longform darf autonome Reaktionen und Thermoregulation deutlich tiefer erklären.

## Bereits produzierte normale Videos

- Thema 001 „Was passiert mit Essen im Körper?“ – Projekt `008-longform-verdauung`, gerendert (Neuauflage: Thema 015)
- Thema 013 „Warum bist du nach dem Essen schnell wieder hungrig?“ – Projekt `010-longform-hunger`, gerendert (Neuauflage: Thema 014)
- Thema 008 Schlaf – Projekt `009-longform-schlaf`, laut Repo-Historie vom Nutzer hochgeladen und gesichtet

Der frühere Verdauungs-Pilot wurde auf Nutzerwunsch gelöscht und zählt nicht als produziert oder reserviert.

## Themen, die wir nicht doppelt machen dürfen

Erst normale Videos mit Status `FERTIG` reservieren ihren behandelten Kernmechanismus verbindlich.

Interne `TEST`-Videos werden nur als Lern-/Pipelinehistorie geführt und dürfen später in einer deutlich tieferen Longform-Version erneut behandelt werden.

## Vorgehen bei jedem normalen neuen Video

1. Diese Datei lesen.
2. Prüfen, was bereits `IN ARBEIT` oder `FERTIG` ist.
3. Neues Thema auswählen oder eine vorhandene `IDEE` verwenden.
4. Prüfen, ob das Thema mindestens 5 Minuten trägt.
5. Abgrenzung zu ähnlichen Themen definieren.
6. Status auf `IN ARBEIT` setzen.
7. Nach Fertigstellung auf `FERTIG` setzen.
8. Wichtige behandelte Teilfragen ergänzen.

## Langfristige Themenbereiche

- Ernährung
- Verdauung
- Stoffwechsel
- Zellen
- Gehirn
- Nervensystem
- Herz und Kreislauf
- Blut
- Atmung
- Immunsystem
- Muskeln
- Knochen
- Hormone
- Schlaf
- Vitamine
- Mineralstoffe
- Darmmikrobiom
- Haut
- Leber
- Nieren
- Lebensmittel und ihre Wirkung im Körper

Die Liste wird laufend erweitert. Normale Kanalvideos bleiben Longform; kurze Projekte sind nur ausdrücklich gekennzeichnete interne Tests.

## Neuauflagen auf Nutzerwunsch (18.10.2026)

Eine Neuauflage ist **kein** Duplikat im Sinne der Doppelungsregel, wenn der Nutzer sie ausdrücklich verlangt und das alte Video unverändert bleibt. 011 (Hunger V2) und 012 (Verdauung V2 „Die Reise einer Pizza“) sind die neuen Kanalversionen von 010 und 008. Begründung und Messwerte: `engine/KANAL-ANALYSE-2026-10.md`.

### Themenvorschläge mit starkem Hook (IDEE, vor Auswahl prüfen)
- Was Kaffee in deinem Körper macht – Minute für Minute (Adenosin)
- Was passiert, wenn du 24 Stunden nichts isst? (Glykogen → Fettverbrennung)
- Wie dein Körper Fett verbrennt – und wo es hingeht (größtenteils als CO₂ ausgeatmet)
- Warum du nach dem Essen müde wirst
- Was Alkohol in deinem Körper macht
