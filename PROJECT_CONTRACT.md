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
- komplexe Vorgaenge visuell einfach und fachlich plausibel erklaeren
- wichtige sichtbare Dinge knapp auf Deutsch beschriften
- wissenschaftlich relevante Aussagen pruefen

## Zwei verbindliche Bildmodi

### A. Object-Talk Character Mode

Fuer sprechende Lebensmittel und Alltagsgegenstaende:

- hochwertiger stilisierter 3D-Character-Look
- klare Objektform
- expressive Augen / Brauen / Mund
- freundlich, modern, animiert
- nicht fotorealistisch

### B. Educational Explainer Mode

Fuer Biologie, Koerper, Organe, Zellen und Prozesse:

**moderne stilisierte 2.5D / Soft-3D Educational Illustration**

Leitidee:

**80 % animierte Illustration + 20 % Soft-3D-Tiefe + 0 % Medical-CGI.**

Autoritative Details:

```text
bildwelt/OBJECT-TALK-CHANNEL-DNA.md
bildwelt/EXPLAINER-STYLE-LOCK.md
```

## Educational Explainer – harte Stilregeln

Verbindlich:

- klar animiert / illustriert, nicht realistisch
- weiche gerundete vereinfachte Formen
- matte bis leicht satinierte Oberflaechen
- weiche Farbverlaeufe
- subtile Schatten und leichte Tiefenstaffelung
- ruhige helle Hintergruende
- eine Hauptaussage pro Bild
- wenige Objekte
- visuelle Klarheit vor Detailgrad
- vereinfachte, aber erkennbare Anatomie

Semantische Farben:

- O2 / Sauerstoff = Cyan / Tuerkis
- rote Blutkoerperchen = tiefes warmes Rot
- Blutgefaesse = Coral / Rot
- Organe = Peach / Coral
- Muskelzellen = Orange / Apricot
- CO2 = weiches Violett
- ATP / Energie = warmes Gelb / Gold
- Hintergrund = Creme / helles Blau / weiches Beige

Harte Stilverbote:

- Photorealismus
- Medical-CGI / Anatomiesoftware
- nasses realistisches Gewebe
- Mikroskop-Fotorealismus
- kosmische / Weltraum-artige Welten
- Sci-Fi-Tunnel / Neon-Labor
- dunkle violette Mikrowelt als Standard
- Anatomie-Mannequins / Torso-Modelle
- Corporate-Stock-3D
- billiger Toy-Look
- Gore / Horror
- ueberladene Infografik

## Menschen-Regel

Der Kanal ist kein Presenter-Kanal.

Menschen nur, wenn fachlich noetig, dann:
- stark vereinfacht
- gesichtslos
- sekundaer

Biologische Strukturen werden nicht automatisch personifiziert.

## Reference-First ist Pflicht

Referenzreihenfolge:

1. `assets/channel/STYLE_REFERENCE.png` – kanalweite visuelle Referenz, sobald freigegeben
2. `Bild_01.png` – konkrete Episode-/Continuity-Referenz
3. wiederkehrende Objekt-/Character-Referenzen
4. konkreter Szenenprompt

Ein Textsatz wie `Using Bild_01 as the exact style reference` zaehlt nicht als echte Referenz. Benoetigte Referenzen muessen wirklich angehaengt werden.

Solange `STYLE_REFERENCE.png` fehlt, darf `Bild_01` im dokumentierten Bootstrap-Modus aus der schriftlichen Kanal-DNA erzeugt werden. Nach Freigabe muss `Bild_01.png` als echte visuelle Referenz an alle Folgebilder angehaengt werden.

## Sichtbarer Text

### Cover / Bild_01

- kurze starke deutsche Hook direkt im Bild
- normalerweise 3–7 Woerter
- **keine zusaetzlichen Anatomie-Labels**
- Cover ohne Text = FAIL

### Normale Bilder

- 0–2 kurze deutsche Labels bevorzugt
- maximal 3 nur wenn fachlich wirklich noetig
- Begriffe aus `02_bildprompts/label-plan.json`
- keine Textwaende
- kein englischer sichtbarer Text

Wenn Flow einen deutschen Begriff falsch schreibt, wird zuerst regeneriert. Nur bei wiederholtem Fehler wird exakt dieser Begriff spaeter in Remotion ersetzt.

## Bild_01 – Cover + erster Shot + Master Style Frame

`Bild_01` ist gleichzeitig:

1. Cover
2. erster Shot
3. Master Style Frame
4. Referenz fuer alle weiteren Bilder

Darum gilt:

- Thema und visuelle Reise auf einen Blick verstaendlich
- gleicher Soft-3D-Explainer-Stil wie normale Szenen
- darf kraeftiger / kontrastreicher komponiert sein
- deutsche Hook direkt sichtbar
- keine zusaetzlichen Labels
- keine medizinische / kosmische / realistische Optik

## Google-Flow-Prompt-Sprache

- Flow-Anweisungen: Englisch
- sichtbarer Text: Deutsch

Szenenprompts nach Bild_01 folgen:

```text
SUBJECT
→ VISIBLE PROCESS
→ SPATIAL LAYOUT
→ SCALE / DEPTH
→ CONTINUITY REFERENCES
→ REQUIRED GERMAN TEXT
→ FORBIDDEN ELEMENTS
```

## Google-Flow-Ablauf

### A – zuerst nur Bild_01

1. dauerhafte Agent Instructions laden
2. `STYLE_REFERENCE.png` anhaengen, falls vorhanden
3. ausschliesslich `Bild_01` erzeugen
4. echte Resultate auf Stil, Klarheit, Anatomie und deutsche Hook pruefen
5. bei FAIL regenerieren
6. beste PASS-Variante als `Bild_01.png` speichern
7. genau einmal Nutzerfreigabe abwarten

### B – Produktion

Nach Freigabe:

- jede Szene einzeln erzeugen
- `Bild_01.png` bei jeder Generation wirklich anhaengen
- pro Bild eine Hauptaussage
- semantische Farben stabil halten
- nur notwendige Labels verwenden

### C – Recovery

Fehlerhafte oder fehlende Bilder behalten ihre Nummer. Nach dem Hauptdurchlauf werden nur diese Bilder erneut erzeugt.

## Echte Bild-QA

`image-review.json` darf erst nach Sichtpruefung des tatsaechlichen Bildes aktualisiert werden.

Pflicht:

- scientific_accuracy >= 8/10
- voiceover_match >= 8/10
- immediate_clarity >= 8/10
- style_continuity >= 8/10
- composition >= 8/10
- label_accuracy >= 8/10, falls Labels vorgesehen sind
- ai_artifact_check = PASS
- scene_difference bestanden
- overall_score >= 8/10
- finale `Bild_XX.png` existiert

Hard FAIL:

- photorealistischer / medizinischer Drift
- zu viele Inhalte gleichzeitig
- unklare Prozessrichtung
- fehlende / falsche notwendige Labels
- kosmischer / Sci-Fi-Stil
- behauptete Referenznutzung ohne echte Referenz

## Drei Phasen

### Phase 1 – Creative Director

Erstellt Recherche, Claim-Check, Script, Szenenplan, Label-Plan, Flow-Szenenprompts, scene-map.json, overlay-plan.json und Metadaten.

### Phase 2 – Nutzer + Voice-KI + Google Flow

1. Voiceover 1:1 erzeugen
2. Flow Agent Instructions setzen
3. Bild_01 mit deutscher Hook erzeugen und freigeben
4. Bild_01 als echte visuelle Referenz nutzen
5. restliche Bilder einzeln erzeugen
6. echte Einzelbild-QA
7. Recovery
8. finale ZIP

### Phase 3 – Antigravity + Tools + Remotion

1. Audio vorbereiten
2. Bilder importieren und validieren
3. Whisper + Script-Ausrichtung
4. Timeline erzeugen
5. nur fehlerhafte/fehlende KI-Texte exakt aus Label-/Overlay-Plan ersetzen
6. Remotion bauen und rendern
7. Final-QA, Scorecard und Postmortem

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

Stoppen bei:

- Script/Audio stimmen nicht ueberein
- fehlenden oder doppelten finalen Bildnummern
- falschem Seitenverhaeltnis
- unklarer Szenenzuordnung
- wissenschaftlich ungeklärten Kernbehauptungen
- sichtbar falscher biologischer Darstellung
- behaupteter Referenznutzung ohne angehaengte Referenz
- Cover ohne deutsche Hook
- photorealistischem / Medical-CGI-Stil-Drift
- Phase-2-Review ohne vorhandene finale Bilddatei
