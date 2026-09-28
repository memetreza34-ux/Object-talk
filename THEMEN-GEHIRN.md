# Themen-Gehirn

Diese Datei ist das **Gedächtnis für alle langen YouTube-Videos** des Object-Talk-/FoodSpricht-Kanals.

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
| 001 | IDEE | Verdauung | Was passiert mit Essen im Körper? | mögliche spätere Longform; kompletter Weg Mund bis Ausscheidung | – |
| 002 | IDEE | Zellbiologie | Was ist eine menschliche Zelle? | Aufbau und wichtigste Zellbestandteile verständlich erklären | – |
| 003 | IDEE | Gehirn | Wie kommunizieren Nervenzellen? | Neuron, elektrisches Signal, Synapse, Neurotransmitter | – |
| 004 | IDEE | Ernährung | Was macht Zucker im Körper? | spätere Longform: Aufnahme, Blutzucker, Insulin, Energie und Überschuss deutlich tiefer | Testpiloten 000/002 behandeln nur die Grundkette |
| 005 | IDEE | Kreislauf | Wie transportiert Blut Sauerstoff? | spätere Longform: Sauerstofftransport deutlich tiefer, ggf. Sättigung, Belastung, Regulation | Testpiloten 001/005 behandeln nur die Grundreise |
| 006 | IDEE | Immunsystem | Wie bekämpft der Körper Bakterien? | angeborene Immunabwehr vereinfacht erklären | Pilot 006 berührt Immunzellen nur im Kontext Wundheilung |
| 007 | IDEE | Ernährung | Was passiert nach einer proteinreichen Mahlzeit? | Verdauung von Protein, Aminosäuren und Nutzung im Körper | Testpilot 003 berührt Protein nur als Baustoff für Muskelanpassung |
| 008 | IDEE | Schlaf | Was passiert im Körper, während wir schlafen? | Gehirn, Erholung, Gedächtnis, Hormone und Schlafphasen als Überblick | – |
| 009 | IDEE | Muskeln | Wie wächst ein Muskel? | spätere Longform: Training, Hypertrophie, Proteinsynthese, Ernährung, Regeneration und Progression deutlich tiefer | Testpilot 003 behandelt nur vereinfachte Grundkette |
| 010 | IDEE | Gehirn | Wie entsteht eine Erinnerung? | Verarbeitung, Synapsen und Gedächtnisbildung vereinfacht | 003 teilweise |
| 011 | IDEE | Haut | Wie heilt eine Wunde? | spätere Longform: Hämostase, Entzündung, Proliferation, Remodeling und Narbenbildung deutlich tiefer | Testpilot 006 behandelt nur die vereinfachte Grundkette |
| 012 | IDEE | Haut/Nervensystem | Warum bekommen wir Gänsehaut? | spätere Longform könnte Thermoregulation, autonome Reaktionen und emotionale Piloerektion vertiefen | Testpilot 007 behandelt nur die kurze Grundkette |

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

Inhaltlich behandelt der Test vereinfacht:

`Kälte/Emotion → Nervensystem → sympathisches Signal → Haaraufrichtemuskel → Haar richtet sich auf → Haut hebt sich → Gänsehaut`

Zusatzkontext:
`dichtes Tierfell → größere Luftschicht / größere Körperkontur; beim Menschen deutlich schwächerer Nutzen`

**Dieser Test blockiert Thema 012 nicht.** Eine spätere Longform darf autonome Reaktionen und Thermoregulation deutlich tiefer erklären.

## Bereits produzierte normale Videos

Noch keine.

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