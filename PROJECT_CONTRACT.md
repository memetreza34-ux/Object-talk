# Object-Talk – Project Contract

Diese Datei ist die dauerhafte oberste Produktionsregel des Repositories. Bei Widerspruechen gilt zuerst eine ausdrueckliche aktuelle Nutzeranweisung, danach dieser Contract.

## Ziel

Object-Talk produziert deutschsprachige YouTube-Erklaervideos zu Ernaehrung, Gesundheit und Biologie.

Harte Grundregeln:

- normale Kanalvideos mindestens 5:00 Minuten
- Standardziel 5:30–8:00 Minuten
- 16:9, 1920×1080, 30 fps
- generierte Standbilder bleiben die visuelle Basis
- hohe visuelle Dichte statt langer statischer Bildhaltezeiten
- stark stilisierte hochwertige 3D-Animationsfilm-Welt, deutlich animiert statt fotorealistisch
- komplexe Vorgaenge visuell einfach und fachlich plausibel erklaeren
- wissenschaftlich relevante Aussagen pruefen
- keine unnoetige Themenwiederholung

## Interner Kurz-Pilot

Ein ausdruecklich markierter interner Test darf kuerzer sein, wenn `05_info/test-mode.json` mit `test_mode: true` vorhanden ist. Nur die Laufzeitregel darf abweichen; Wissenschafts-, Visual-, Sync- und QA-Regeln bleiben aktiv.

Aktueller Pilot:

```text
youtube-videos/001-pilot-sauerstoff-im-blut/
```

## Verbindliche Bildwelt

Der Kanal ist kein dauerhafter Mascot-/Presenter-Kanal. Die Biologie und der erklaerte Prozess sind der Hauptdarsteller.

Verbindlich:

- hochwertiger stilisierter 3D-Animationsfilm-Look
- weich, rund und klar animiert
- deutlich weniger realistisch als medizinische CGI
- vereinfachte, aber erkennbare Anatomie
- warme filmische Beleuchtung
- hochwertige matte/satinierte Materialien
- starke Tiefenwirkung
- familiengeeignet, aber nicht babyhaft
- keine Anime-, Comic-, Live-Action- oder fotorealistische Medizinoptik
- kein Gore und keine Horror-Anatomie

Personifizierte Lebensmittel oder Gegenstaende sind nur erlaubt, wenn sie die Szene wirklich verstaendlicher machen. Molekuele, Organe und Zellen werden nicht automatisch personifiziert.

## Reference-First ist Pflicht

Stiltreue wird nicht mehr nur durch Textprompts erzwungen.

Referenzreihenfolge:

1. `assets/channel/STYLE_REFERENCE.png` – kanalweite visuelle Referenz, sobald freigegeben
2. `Bild_01.png` – konkrete Episode-/Continuity-Referenz
3. wiederkehrende Objekt-/Character-Referenzen
4. konkreter Szenenprompt

Ein Textsatz wie `Using Bild_01 as the exact style reference` zaehlt nicht als tatsaechliche visuelle Referenz. Wenn Flow Referenzbilder/Ingredients unterstuetzt, muessen die benoetigten Referenzen wirklich angehaengt werden.

Solange `STYLE_REFERENCE.png` noch nicht existiert, darf `Bild_01` im dokumentierten Bootstrap-Modus aus der schriftlichen Kanal-DNA erzeugt werden. Nach Freigabe muss `Bild_01.png` als echte visuelle Referenz an alle Folgebilder angehaengt werden.

Details:

```text
engine/FLOW-PRODUCTION-STANDARD.md
engine/FLOW-AGENT-INSTRUCTIONS.md
engine/STYLE-REFERENCE-SYSTEM.md
```

## Flow erzeugt Bilder, Remotion erzeugt Schrift

Standardmaessig sind Flow-Bilder textfrei.

- keine eingebrannten Labels
- keine KI-Pfeile
- keine KI-Typografie
- kein Cover-Hook direkt aus Flow

Deutsche Beschriftungen bleiben wichtiger Teil der Erklaerung, werden aber deterministisch spaeter gerendert.

Quelle pro Video:

```text
02_bildprompts/label-plan.json
```

Cover-Hook und zusaetzliche Overlays werden im Remotion-/Overlay-System gesetzt.

Nur eine aktuelle ausdrueckliche Nutzeranweisung darf Text direkt in Flow-Bilder zurueckbringen.

## Bild_01 – Cover-Grundbild + erster Shot + Master Style Frame

`Bild_01` ist gleichzeitig:

1. Cover-Grundbild
2. erster Shot
3. Master Style Frame
4. Referenz fuer alle weiteren Bilder

Darum gilt:

- Bild_01 besonders praezise planen
- Thema und visuelle Reise auf einen Blick verstaendlich
- Rendergrad, Licht, Materialien, Farbwelt, Tiefenwirkung und Anatomie-Vereinfachung definieren
- ruhige Negativflaeche fuer spaeteren Hook vorsehen, wenn sinnvoll
- Bild selbst textfrei halten
- wenn moeglich 2–4 Varianten erzeugen und die beste visuell pruefen

Nach Freigabe wird Bild_01 bei jeder Folgegeneration als echte visuelle Referenz genutzt.

## Google-Flow-Prompt-Sprache

- Flow-Anweisungen: Englisch
- sichtbarer Text im finalen Video: Deutsch
- Flow-Bilder selbst: standardmaessig textfrei

Szenenprompts nach Bild_01 folgen:

```text
SUBJECT
→ VISIBLE PROCESS
→ SPATIAL LAYOUT
→ CAMERA / SCALE
→ CONTINUITY REFERENCES
→ FORBIDDEN ELEMENTS
```

Keine langen Stilromane als Ersatz fuer echte Referenzen.

## Verbindlicher Google-Flow-Ablauf

### A – zuerst nur Bild_01

1. dauerhafte Agent Instructions laden
2. `STYLE_REFERENCE.png` anhaengen, falls vorhanden
3. ausschliesslich `Bild_01` erzeugen
4. echte Resultate visuell pruefen
5. bei FAIL regenerieren
6. beste PASS-Variante als `Bild_01.png` speichern
7. genau einmal Nutzerfreigabe abwarten

### B – Produktion in 5er-Bloecken

Nach Freigabe:

```text
Bild_02–Bild_06
Bild_07–Bild_11
Bild_12–Bild_16
Bild_17–Bild_21
Bild_22–Bild_26
...
```

Jedes Bild trotzdem einzeln erzeugen, pruefen und benennen. Bei jeder Generation `Bild_01.png` wirklich anhaengen; `STYLE_REFERENCE.png` zusaetzlich, sobald vorhanden.

### C – Fehlerliste

Fehlerhafte oder fehlende Bilder behalten ihre Nummer und kommen auf die Recovery-Liste.

### D – Recovery

Nach dem Hauptdurchlauf nur fehlende/fehlerhafte Bildnummern erneut erzeugen. Promptkorrektur muss den konkreten Fehler adressieren.

### E – finale ZIP

Nur akzeptierte finale Bilder, lueckenlose Nummerierung, keine Varianten oder Temp-Dateien.

## Echte Bild-QA

`image-review.json` ist kein Selbstzweck.

Es darf erst nach Sichtpruefung des tatsaechlichen Bildes aktualisiert werden. Eine manuell oder automatisch eingetragene Zahl ohne Bildsichtung ist keine gueltige QA.

Pflicht:

- scientific_accuracy >= 8/10
- voiceover_match >= 8/10
- immediate_clarity >= 8/10
- style_continuity >= 8/10
- composition >= 8/10
- ai_artifact_check = PASS
- scene_difference bestanden
- overall_score >= 8/10
- entsprechende finale `Bild_XX.png` existiert

## Drei Phasen

### Phase 1 – Creative Director

Erstellt:

1. Themenpruefung
2. Recherche und Claim-Check
3. Mechanism Map
4. finales Script
5. Satz-Visual-Plan
6. semantischen Szenenplan
7. Label-Plan
8. praezise Flow-Szenenprompts
9. scene-map.json
10. overlay-plan.json
11. Metadaten

### Phase 2 – Nutzer + Voice-KI + Google Flow

1. Voiceover 1:1 erzeugen
2. Flow Agent Instructions setzen
3. Bild_01 erzeugen und freigeben
4. Bild_01 als echte visuelle Referenz nutzen
5. restliche Bilder einzeln in 5er-Bloecken erzeugen
6. echte Einzelbild-QA
7. Recovery
8. finale ZIP

Flow darf keine Szenengrenzen neu erfinden.

### Phase 3 – Antigravity + Tools + Remotion

1. Audio kanonisch vorbereiten
2. Bilder sicher importieren
3. Assets validieren
4. Voice mit Whisper transkribieren
5. Script ↔ Audio streng ausrichten
6. Timeline erzeugen
7. deutsche Labels/Hook/Overlays aus den Plaenen rendern
8. Remotion-Runtime bauen
9. Bilder dezent bewegen
10. rendern
11. technische und visuelle QA
12. Scorecard + Postmortem

Phase 3 darf Script, wissenschaftliche Aussagen, Bildreihenfolge oder Szenengrenzen nicht still veraendern.

## Autoritative Reihenfolge

1. aktuelle ausdrueckliche Nutzeranweisung
2. `PROJECT_CONTRACT.md`
3. `PROJECT_STATE.md`
4. `config/*.json`
5. `engine/*.md`
6. `bildwelt/*.md`
7. `THEMEN-GEHIRN.md`
8. projektspezifische Dateien

## Fail-closed

Bei echten Widerspruechen nicht raten. Stoppen bei:

- Script/Audio stimmen nicht ueberein
- fehlenden oder doppelten finalen Bildnummern
- falschem Seitenverhaeltnis
- unklarer Szenenzuordnung
- wissenschaftlich ungeklärten Kernbehauptungen
- sichtbar falscher biologischer Darstellung
- behaupteter Referenznutzung ohne tatsaechlich angehaengte Referenz
- Phase-2-Review ohne vorhandene finale Bilddatei

Ein einzelner Flow-Generierungsfehler ist kein globaler Blocker; dafuer gibt es Fehlerliste + Recovery.
