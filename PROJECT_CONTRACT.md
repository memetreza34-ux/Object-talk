# Object-Talk – Project Contract

Diese Datei ist die dauerhafte oberste Produktionsregel des Repositories. Bei Widersprüchen gilt zuerst eine ausdrückliche aktuelle Nutzeranweisung, danach dieser Contract.

## Ziel

Object-Talk produziert deutschsprachige YouTube-Erklärvideos zu Ernährung, Gesundheit und Biologie.

Harte Grundregeln:

- normale Kanalvideos mindestens 5:00 Minuten
- Standardziel 5:30–8:00 Minuten
- 16:9, 1920×1080, 30 fps
- generierte Standbilder bleiben die visuelle Basis
- hohe visuelle Dichte statt langer statischer Bildhaltezeiten
- stark stilisierte hochwertige 3D-Animationsfilm-Welt, deutlich animiert statt fotorealistisch
- komplexe Vorgänge visuell einfach und fachlich plausibel erklären
- wichtige sichtbare Strukturen in jedem Bild knapp beschriften
- sichtbarer Text immer Deutsch
- Flow-Prompt-Anweisungen immer Englisch
- keine unnötige Themenwiederholung

## Interner Kurz-Pilot

Normale veröffentlichte Videos bleiben mindestens 5:00 Minuten lang.

Ein ausdrücklich markierter interner Test darf kürzer sein, wenn `05_info/test-mode.json` mit `test_mode: true` vorhanden ist. Nur die Laufzeitregel darf abweichen; Wissenschafts-, Visual-, Sync- und QA-Regeln bleiben aktiv.

Aktueller Pilot:

```text
youtube-videos/001-pilot-sauerstoff-im-blut/
```

## Verbindliche Bildwelt

Der Kanal ist kein Mascot-/Presenter-Kanal. Die Biologie und der erklärte Prozess sind der Hauptdarsteller.

Die verbindliche Welt ist:

- hochwertiger stilisierter 3D-Animationsfilm-Look
- weich, rund und klar animiert
- deutlich weniger realistisch als medizinische CGI
- vereinfachte, aber erkennbare Anatomie
- warme filmische Beleuchtung
- hochwertige Materialien, starke Tiefenwirkung
- freundlich und familiengeeignet, aber nicht babyhaft
- keine Anime-, Comic-, Live-Action- oder fotorealistische Medizinoptik
- kein Gore und keine Horror-Anatomie

Standard-Bildtypen:

- anatomische Cutaways
- transparente Körperansichten
- Prozessdarstellungen
- Organ-, Gewebe-, Zell- und Organellvisualisierungen
- Mikro-/Makro-Wechsel
- Vorher-/Nachher- und Vergleichsbilder
- Ursache → Prozess → Folge

Personifizierte Lebensmittel oder Figuren sind nur erlaubt, wenn sie eine Szene wirklich verständlicher machen. Sie sind nie der dauerhafte Standard.

## Beschriftung und sichtbarer Text

**Jedes Bild benennt die wichtigsten sichtbaren Dinge.**

Regeln:

- normalerweise 1–3 kurze deutsche Labels
- nur Schlüsselstrukturen oder Schlüsselprozesse beschriften
- Labels eindeutig zuordnen
- keine Textwände
- keine englischen sichtbaren Wörter
- kein KI-Gibberish
- fehlerhaftes Label = Bild regenerieren
- wenn Flow einen Begriff wiederholt falsch schreibt, textfreie Variante erzeugen und exakt denselben deutschen Begriff später in Remotion ergänzen

Zusätzliche Überschriften/Keywords dürfen in Remotion animiert werden. Details: `engine/PRESENTATION-OVERLAY-SYSTEM.md`.

## Bild_01 – Cover + Hook + Master Style Frame

`Bild_01` ist bei jedem Video oder Reel gleichzeitig:

1. Cover-/Hook-Bild
2. erster Shot
3. Master Style Frame
4. Stilreferenz für alle weiteren Bilder

Darum gilt für Bild_01 eine Sonderregel:

- der Prompt für Bild_01 ist ausführlicher und präziser als die restlichen Bildprompts
- Thema und visuelle Reise müssen auf einen Blick verständlich sein
- Bild_01 definiert Rendergrad, Stilisierung, Licht, Materialien, Farbwelt, Tiefenwirkung und Anatomie-Vereinfachung
- Bild_01 enthält eine **kurze starke deutsche Hook-Zeile**, die sagt, worum es im Video/Reel geht
- Hook normalerweise 3–7 Wörter und höchstens zwei kurze Zeilen
- keine irreführende Clickbait-Aussage
- zusätzlich nur die wichtigsten Labels

Nach Freigabe muss Google Flow Bild_01 als Style-/Continuity-Referenz für alle weiteren Bilder verwenden, soweit technisch möglich.

## Google-Flow-Prompt-Sprache

- Anweisungen/Prompts an Flow: **Englisch**
- sichtbare Texte, Hook, Labels, Callouts: **Deutsch**

Szenenprompts nach Bild_01 sind bewusst kompakt:

- so kurz wie möglich, so genau wie nötig
- meistens 2–5 Sätze
- Szene + sichtbarer Prozess + Komposition + deutsche Labels
- globalen Stilblock nicht in jedem Einzelprompt vollständig wiederholen

Details: `engine/FLOW-PRODUCTION-STANDARD.md`.

## Verbindlicher Google-Flow-Ablauf

### A – zuerst nur Bild_01

1. kompletten Auftrag lesen
2. ausschließlich `Bild_01` erzeugen
3. Bild_01 auf Stil, Hook, Anatomie, deutsche Schrift und Komposition prüfen
4. bei FAIL nur Bild_01 regenerieren
5. bei PASS als `Bild_01.png` speichern
6. STOPP und Nutzerfreigabe abwarten

### B – Produktion in 5er-Blöcken

Nach Freigabe:

```text
Bild_02–Bild_06
Bild_07–Bild_11
Bild_12–Bild_16
Bild_17–Bild_21
Bild_22–Bild_26
Bild_27–Bild_31
...
```

Jedes Bild trotzdem einzeln erzeugen, prüfen und benennen. Nach jedem Block Stil-/Nummerierungscheck.

### C – Fehlerliste

Fehlerhafte oder fehlende Bilder behalten ihre Nummer und kommen auf die Recovery-Liste. Der reguläre Durchlauf wird nicht wegen eines einzelnen Flow-Fehlers abgebrochen.

### D – Recovery

Nach dem Hauptdurchlauf nur fehlende/fehlerhafte Bildnummern erneut erzeugen, bis alles lückenlos PASS ist.

### E – finale ZIP

Nur akzeptierte finale Bilder, lückenlose Nummerierung, keine Varianten oder Temp-Dateien.

## Nutzer-Dateien

Pflicht pro Video:

```text
01_script/VOICEOVER-ZUM-KOPIEREN.txt
02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt
03_pipeline/ANTIGRAVITY-PROMPT-ZUM-KOPIEREN.txt
04_export/YOUTUBE-TITEL-BESCHREIBUNG-ZUM-KOPIEREN.txt
```

Kopierdateien müssen inhaltlich mit ihren kanonischen Projektdateien übereinstimmen.

## Drei Phasen

### Phase 1 – ChatGPT / Creative Director

Erstellt:

1. Themenprüfung
2. Recherche und Claim-Check
3. Mechanism Map
4. finales `script.txt`
5. identisches Voiceover zum Kopieren
6. Satz-Visual-Plan
7. semantischen Szenenplan
8. Label-Plan für jedes Bild
9. Google-Flow-Prompt mit ausführlichem Bild_01 und kompakten Folgeprompts
10. `scene-map.json`
11. optionalen `overlay-plan.json`
12. Antigravity-Anweisung
13. YouTube-Titel/Beschreibung

Keine geschätzten finalen Zeitcodes als Wahrheit.

### Phase 2 – Nutzer + Voice-KI + Google Flow

1. Voiceover 1:1 erzeugen
2. Audio ablegen
3. kompletten Flow-Prompt verwenden
4. zuerst nur Bild_01
5. Bild_01 freigeben
6. restliche Bilder in 5er-Blöcken
7. Einzelbild-QA
8. Recovery
9. finale ZIP

Flow darf keine Szenengrenzen neu erfinden.

### Phase 3 – Antigravity + Tools + Remotion

1. Audio kanonisch vorbereiten
2. Bilder sicher importieren
3. Assets validieren
4. Voice mit Whisper transkribieren
5. Script ↔ Audio streng ausrichten
6. Timeline erzeugen
7. Remotion-Runtime bauen
8. Bilder dezent bewegen
9. geplante deutsche Overlays/Callouts anwenden
10. rendern
11. technische und visuelle QA
12. Scorecard + Postmortem

Phase 3 darf Script, wissenschaftliche Aussagen, Bildreihenfolge oder Szenengrenzen nicht still verändern.

## Autoritative Reihenfolge

1. aktuelle ausdrückliche Nutzeranweisung
2. `PROJECT_CONTRACT.md`
3. `PROJECT_STATE.md`
4. `config/*.json`
5. `engine/*.md`
6. `bildwelt/*.md`
7. `THEMEN-GEHIRN.md`
8. projektspezifische Dateien

## Fail-closed

Bei echten Widersprüchen nicht raten. Stoppen bei:

- Script/Audio stimmen nicht überein
- fehlenden oder doppelten finalen Bildnummern
- falschem Seitenverhältnis
- unklarer Szenenzuordnung
- nicht gefundenen Wortankern
- wissenschaftlich ungeklärten Kernbehauptungen
- sichtbar falschen biologischen Beschriftungen

Ein einzelner Flow-Generierungsfehler ist kein globaler Blocker; dafür gibt es Fehlerliste + Recovery.

## Visuelle Konstanz

`Bild_01` ist immer Episode-Style-Anchor. Sobald eine kanalweite Referenz ausdrücklich akzeptiert und als `assets/channel/STYLE_REFERENCE.png` gespeichert wurde, gilt:

```text
STYLE_REFERENCE = langfristige Kanal-DNA
Bild_01 = konkrete Episode-/Continuity-Referenz
```

Stilreferenzen dürfen nie fachlich falsche Anatomie erzwingen.

## Themen-Gedächtnis

Vor jeder neuen Produktion `THEMEN-GEHIRN.md` prüfen und aktualisieren. Bereits behandelte Kernmechanismen nicht nur unter neuem Titel wiederholen.
