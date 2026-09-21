# Object-Talk – Project Contract

Diese Datei ist die dauerhafte oberste Produktionsregel des Repositories. Bei Widersprüchen gilt zuerst eine ausdrückliche aktuelle Nutzeranweisung, danach dieser Contract.

## Ziel

Object-Talk produziert ausschließlich lange deutschsprachige YouTube-Erklärvideos zu Ernährung, Gesundheit und Biologie.

Harte Grundregeln:

- finales Video mindestens 5:00 Minuten
- Standardziel 5:30–8:00 Minuten
- 16:9, 1920×1080, 30 fps
- narrative Bildwelt ausschließlich aus Standbildern; Bewegung entsteht im Schnitt/Remotion
- einheitliche hochwertige semi-realistische 3D-Explainer-Bildwelt
- komplexe Vorgänge müssen visuell einfach und nachvollziehbar erklärt werden
- biologische Inhalte vereinfachen, aber nicht fachlich verfälschen
- wichtige Strukturen knapp und auf Deutsch beschriften
- keine unnötigen Wiederholungen bereits produzierter Themen

## Interner Kurz-Pilot – einzige Laufzeit-Ausnahme

Die 5-Minuten-Regel bleibt für normale veröffentlichte Kanalvideos bestehen.

Ein **ausdrücklich als interner Test markiertes Projekt** darf kürzer sein, wenn im Projekt eine Datei

```text
05_info/test-mode.json
```

mit `test_mode: true` vorhanden ist.

Für solche Piloten gilt:

- Zweck ist ausschließlich Pipeline-, Stil-, Flow-, Sync- oder Render-Test
- Zielbereich muss im Projekt selbst dokumentiert sein
- der Test zählt nicht automatisch als veröffentlichtes Thema
- `qa_final.py` darf nur für diesen Test mit einem ausdrücklich angegebenen `--min-seconds` unter 300 ausgeführt werden
- normale Videos verwenden weiterhin den Standardwert 300 Sekunden
- ein Testprojekt darf keine globale Longform-Regel still auf kürzere Videos umstellen

Aktueller Pilot:

```text
youtube-videos/000-pilot-zucker-im-blut/
```

Ziel ca. 120 Sekunden; akzeptabler interner Testbereich 105–150 Sekunden.

## Verbindliche Bildwelt – Faceless Explainer zuerst

Der Kanal ist **kein Mascot-/Presenter-Kanal**. Die Bilder sollen in erster Linie erklären.

Priorität jedes Bildes:

1. Verständnis des gesprochenen Inhalts
2. fachlich plausible Darstellung
3. klare visuelle Führung
4. konsistenter Kanalstil
5. erst danach dekorative oder emotionale Elemente

Standard-Bildtypen sind:

- anatomische Cutaways
- transparente Körperansichten
- Prozessdarstellungen
- Organ-, Gewebe- und Zellvisualisierungen
- Mikro-/Makro-Zooms
- Vorher-/Nachher- und Vergleichsbilder
- klare Ursache→Prozess→Folge-Darstellungen
- didaktische 3D-Explainer-Kompositionen

Personifizierte Lebensmittel oder Object-Talk-Figuren sind **nicht** der Standard und dürfen nicht als dauerhafte Sprecherfigur vor dem eigentlichen Erklärbild stehen.

Sie sind nur erlaubt, wenn eine konkrete Szene dadurch wirklich verständlicher wird. Richtwert pro Video:

- etwa 70 % direkte Erklärbilder
- etwa 20 % Prozess-/Vergleichsbilder
- maximal etwa 10 % optionale Character-/Guide-Momente

Diese Prozentwerte sind Qualitätsrichtwerte, keine starre Quote. Entscheidend ist immer der Erklärwert.

## Verbindlicher Google-Flow-Ablauf

Google Flow arbeitet fail-tolerant und blockweise.

### A – Master Style Frame

1. Zuerst wird ausschließlich `Bild_01` erzeugt.
2. `Bild_01` wird vollständig geprüft.
3. Erst nach PASS wird es als `Bild_01.png` akzeptiert.
4. `Bild_01` ist gleichzeitig Cover, erster Shot und **Master Style Frame**.
5. Für jede spätere Szene muss `Bild_01` als Style-/Continuity-Referenz verwendet werden, soweit Google Flow dies technisch zulässt.
6. Die Referenz überträgt Stil, Rendergrad, Licht, Materialien, Farbharmonie und Bildsprache – nicht automatisch Motiv oder Anatomie.

### B – Produktion in 5er-Blöcken

Nach `Bild_01` werden die restlichen Bilder in 5er-Blöcken bearbeitet:

```text
Bild_02–Bild_06
Bild_07–Bild_11
Bild_12–Bild_16
...
```

Innerhalb jedes Blocks wird trotzdem jedes Bild einzeln erzeugt, geprüft und benannt. Es wird niemals ein Sammelbild mit mehreren Szenen erzeugt.

### C – Fehlerliste statt Produktionsabbruch

Wenn eine Generation technisch fehlschlägt oder das Bild qualitativ durchfällt:

- Bildnummer auf eine Fehlerliste setzen
- Nummer nicht verlieren oder neu vergeben
- mit dem restlichen regulären Durchlauf fortfahren
- den gesamten Job nicht wegen einer einzelnen fehlgeschlagenen Generation abbrechen

### D – Recovery-Pass

Nach dem regulären Durchlauf werden alle fehlenden oder fehlerhaften Bildnummern gezielt erneut erzeugt.

Recovery wird wiederholt, bis `Bild_01.png` bis `Bild_NN.png` lückenlos in akzeptierter Qualität vorhanden sind.

### E – Finale ZIP

Die finale ZIP darf ausschließlich die akzeptierten finalen Bilder enthalten:

- lückenlose Nummerierung
- keine Duplikate
- keine verworfenen Varianten
- keine temporären Dateien

Details: `engine/FLOW-PRODUCTION-STANDARD.md`.

## Nutzer-Dateien

Alle Inhalte, die der Nutzer selbst öffnen und in ein externes Tool kopieren soll, müssen zusätzlich als normale `.txt`-Datei vorliegen.

Pflicht pro Video:

```text
01_script/VOICEOVER-ZUM-KOPIEREN.txt
02_bildprompts/GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt
03_pipeline/ANTIGRAVITY-PROMPT-ZUM-KOPIEREN.txt
04_export/YOUTUBE-TITEL-BESCHREIBUNG-ZUM-KOPIEREN.txt
```

Diese Dateien dürfen inhaltlich nicht von den zugehörigen kanonischen Projektdateien abweichen. Interne technische Dateien dürfen weiterhin `.md`, `.json`, `.py` usw. verwenden.

Details: `engine/USER-FILES-STANDARD.md`.

## Drei Phasen

### Phase 1 – ChatGPT / Creative Director

ChatGPT erstellt vor jeder Medienproduktion vollständig:

1. Themenprüfung gegen `THEMEN-GEHIRN.md`
2. Recherche und Claim-Check
3. finales gesprochenes `script.txt`
4. identisches `VOICEOVER-ZUM-KOPIEREN.txt`
5. semantischen Szenenplan aus exakt dem finalen Skript
6. vollständigen Google-Flow-Agent-Prompt nach dem faceless Explainer-Standard
7. identisches `GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt`
8. `scene-map.json` mit lückenloser Sprachabdeckung
9. Antigravity-/Editor-Anweisung
10. `ANTIGRAVITY-PROMPT-ZUM-KOPIEREN.txt`
11. YouTube-Titel, Beschreibung und maximal 5 Hashtags
12. `YOUTUBE-TITEL-BESCHREIBUNG-ZUM-KOPIEREN.txt`

Phase 1 erzeugt keine finalen Flow-Bilder und keine geschätzten Zeitcodes.

Phase 1 ist erst vollständig, wenn alle vier Nutzer-`.txt`-Dateien aktuell vorhanden sind.

### Phase 2 – Nutzer + Voice-KI + Google Flow

Der Nutzer:

1. kopiert `VOICEOVER-ZUM-KOPIEREN.txt` 1:1 in die gewählte Voice-KI
2. legt das rohe Voiceover in `01_script/audio/`
3. kopiert `GOOGLE-FLOW-PROMPT-ZUM-KOPIEREN.txt` vollständig in Google Flow
4. lässt zuerst nur `Bild_01` als Master Style Frame erzeugen
5. danach werden die restlichen Bilder blockweise nach `engine/FLOW-PRODUCTION-STANDARD.md` produziert
6. fehlgeschlagene Generationen kommen auf die Recovery-Liste
7. am Ende werden alle fehlenden/fehlerhaften Bilder gezielt neu erzeugt
8. alle finalen Bilder werden als ZIP in `02_bildprompts/bilder-zip/` abgelegt

Google Flow darf keine Szenengrenzen neu erfinden.

### Phase 3 – Antigravity + Tools + Remotion

Phase 3 ist technisch, nicht kreativ. Wenn der Nutzer Antigravity manuell beauftragt, wird `ANTIGRAVITY-PROMPT-ZUM-KOPIEREN.txt` verwendet.

Phase 3:

1. Audio kanonisch vorbereiten
2. Flow-ZIP sicher importieren
3. Assets validieren
4. finales Audio mit Whisper transkribieren
5. Whisper-Ausgabe streng gegen `script.txt` ausrichten
6. `scene-map.json` exakt auf Wort-Zeitstempel abbilden
7. `timeline.json` erzeugen
8. Runtime für Remotion bauen
9. Standbilder mit dezenten Push-ins, Pull-outs und Pans inszenieren
10. rendern
11. technische QA durchführen
12. finales Video + Untertitel + Renderbericht exportieren

Phase 3 darf Skript, wissenschaftliche Aussage, Bildreihenfolge oder Szenengrenzen nicht still verändern.

Nach erfolgreichem Export nutzt der Nutzer `YOUTUBE-TITEL-BESCHREIBUNG-ZUM-KOPIEREN.txt` für YouTube Studio.

## Autoritative Reihenfolge

1. aktuelle ausdrückliche Nutzeranweisung
2. `PROJECT_CONTRACT.md`
3. `PROJECT_STATE.md` für aktuellen Arbeitsstand
4. `config/*.json`
5. `engine/*.md`
6. `bildwelt/*.md`
7. `THEMEN-GEHIRN.md`
8. projektspezifische Dateien

## Fail-closed

Die technische Pipeline soll bei nicht eindeutig auflösbaren Widersprüchen stoppen statt raten.

Insbesondere kein automatisches Weiterarbeiten bei:

- Script und gesprochenes Audio stimmen nicht überein
- fehlenden oder doppelten Bildnummern im finalen Asset-Satz
- falschem Seitenverhältnis
- unklarer Szenenzuordnung
- nicht gefundenen Wortankern
- wissenschaftlich ungeklärten Kernbehauptungen
- sichtbar falschen biologischen Beschriftungen

Ein einzelner **Google-Flow-Generierungsfehler während Phase 2 ist dagegen kein globaler Blocker**. Er wird über Fehlerliste + Recovery-Pass behandelt.

## Visuelle Konstanz

`Bild_01` jedes Videos ist zunächst der projektinterne Master Style Frame für dieses Video.

Sobald zusätzlich eine finale kanalweite Referenz ausdrücklich akzeptiert und als `assets/channel/STYLE_REFERENCE.png` gespeichert wurde, gilt:

```text
kanalweite STYLE_REFERENCE = langfristige Kanal-DNA
Bild_01 des aktuellen Videos = konkrete Episode-/Continuity-Referenz
```

Beide Referenzen dürfen Stil und Kontinuität sichern, aber niemals falsche Anatomie aus einer Referenz ungeprüft übernehmen.

## Themen-Gedächtnis

Vor jeder neuen Produktion wird `THEMEN-GEHIRN.md` geprüft und aktualisiert. Ein bereits behandelter Kernmechanismus darf nicht nur unter neuem Titel erneut produziert werden.
