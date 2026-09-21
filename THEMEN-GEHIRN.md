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
| 004 | IDEE | Ernährung | Was macht Zucker im Körper? | spätere Longform: Aufnahme, Blutzucker, Insulin, Energie und Überschuss deutlich tiefer | Testpilot 000 behandelt nur Grundkette |
| 005 | IDEE | Kreislauf | Wie transportiert Blut Sauerstoff? | rote Blutkörperchen, Lunge, Herz und Gewebe | – |
| 006 | IDEE | Immunsystem | Wie bekämpft der Körper Bakterien? | angeborene Immunabwehr vereinfacht erklären | – |
| 007 | IDEE | Ernährung | Was passiert nach einer proteinreichen Mahlzeit? | Verdauung von Protein, Aminosäuren und Nutzung im Körper | – |
| 008 | IDEE | Schlaf | Was passiert im Körper, während wir schlafen? | Gehirn, Erholung, Gedächtnis, Hormone und Schlafphasen als Überblick | – |
| 009 | IDEE | Muskeln | Wie wächst ein Muskel? | Belastung, Reparatur, Proteinbiosynthese stark vereinfacht | – |
| 010 | IDEE | Gehirn | Wie entsteht eine Erinnerung? | Verarbeitung, Synapsen und Gedächtnisbildung vereinfacht | 003 teilweise |

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
- 5er-Blöcke + Recovery testen
- Whisper/Remotion/QA in kurzer Form testen

Inhaltlich behandelt der Test nur diese Grundkette:

`Snack → Dünndarm → Glukose → Blut → Betazellen/Insulin → Zellen/Glykogenspeicher`

**Dieser Test blockiert Thema 004 nicht.** Eine spätere 5–8-Minuten-Longform darf das Thema umfassender, mit zusätzlichen Mechanismen und höherer Erklärtiefe behandeln.

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

Die Datenbank soll nach und nach diese Bereiche abdecken:

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
