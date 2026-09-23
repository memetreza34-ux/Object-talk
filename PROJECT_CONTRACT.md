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
- **helle, freundliche, hochwertige 3D-Animationsfilm-Welt**
- komplexe Vorgaenge visuell einfach und fachlich plausibel erklaeren
- wichtige sichtbare Dinge knapp auf Deutsch beschriften
- wissenschaftlich relevante Aussagen pruefen

## Interner Kurz-Pilot

Ein ausdruecklich markierter interner Test darf kuerzer sein, wenn `05_info/test-mode.json` mit `test_mode: true` vorhanden ist. Nur die Laufzeitregel darf abweichen.

Aktueller Pilot:

```text
youtube-videos/001-pilot-sauerstoff-im-blut/
```

## Verbindliche Bildwelt

Der Kanal ist kein dauerhafter Mascot-/Presenter-Kanal. Die Biologie und der erklaerte Prozess sind der Hauptdarsteller.

Verbindlich:

- hochwertige stilisierte 3D-Feature-Animation
- klar animiert, nicht fotorealistisch
- hell, freundlich und leicht lesbar als Standard
- weiche, gerundete Formen
- matte/satinierte Premium-Materialien
- warmes Hauptlicht + weiches Fill-Light + dezentes Rim-Light
- klare Tiefenwirkung
- frische kontrollierte Farben wie Creme, Apricot, Coral, warmes Rot, Himmelblau und Teal
- vereinfachte, aber erkennbare Anatomie
- familiengeeignet, aber nicht babyhaft

Harte Stilverbote:

- kosmische / Weltraum-artige Bildwelten
- Galaxie-, Nebel- oder Sternenhintergruende
- dunkle violette Sci-Fi-Mikrowelt als Default
- Neon-Labor / Sci-Fi-Tunnel
- Medical-CGI / Anatomiesoftware
- nasse realistische Gewebeoptik
- Corporate-Stock-3D
- billiger Toy-Look
- Anime / Comic
- Gore / Horror

Personifizierte Lebensmittel oder Gegenstaende sind nur erlaubt, wenn sie die Szene wirklich verstaendlicher machen. Molekuele, Organe und Zellen werden nicht automatisch personifiziert.

## Reference-First ist Pflicht

Referenzreihenfolge:

1. `assets/channel/STYLE_REFERENCE.png` – kanalweite visuelle Referenz, sobald freigegeben
2. `Bild_01.png` – konkrete Episode-/Continuity-Referenz
3. wiederkehrende Objekt-/Character-Referenzen
4. konkreter Szenenprompt

Ein Textsatz wie `Using Bild_01 as the exact style reference` zaehlt nicht als tatsaechliche visuelle Referenz. Benoetigte Referenzen muessen wirklich angehaengt werden.

Solange `STYLE_REFERENCE.png` noch nicht existiert, darf `Bild_01` im dokumentierten Bootstrap-Modus aus der schriftlichen Kanal-DNA erzeugt werden. Nach Freigabe muss `Bild_01.png` als echte visuelle Referenz an alle Folgebilder angehaengt werden.

Details:

```text
engine/FLOW-PRODUCTION-STANDARD.md
engine/FLOW-AGENT-INSTRUCTIONS.md
engine/STYLE-REFERENCE-SYSTEM.md
```

## Sichtbarer Text ist Pflicht

Flow-Bilder sind **nicht standardmaessig textfrei**.

### Bild_01 / Cover

- kurze starke deutsche Hook direkt im Bild
- normalerweise 3–7 Woerter
- Cover ohne Text = FAIL

### Normale Bilder

- normalerweise 1–3 kurze deutsche Labels
- Begriffe aus `02_bildprompts/label-plan.json`
- nur wichtige Strukturen/Prozesse beschriften
- klare Sans-Serif-Typografie
- keine Textwaende
- kein englischer sichtbarer Text

Wenn Flow einen deutschen Begriff falsch schreibt, wird zuerst regeneriert. Nur bei wiederholtem Fehler wird exakt dieser Begriff spaeter in Remotion ersetzt. Das finale Video darf die geplanten Labels niemals verlieren.

## Bild_01 – Cover + erster Shot + Master Style Frame

`Bild_01` ist gleichzeitig:

1. Cover
2. erster Shot
3. Master Style Frame
4. Referenz fuer alle weiteren Bilder

Darum gilt:

- Thema und visuelle Reise auf einen Blick verstaendlich
- heller Premium-3D-Animationsfilm-Look
- deutsche Hook direkt sichtbar
- keine kosmische / dunkle / medizinische Optik
- wenn moeglich 2–4 Varianten erzeugen und die beste visuell pruefen

Nach Freigabe wird Bild_01 bei jeder Folgegeneration als echte visuelle Referenz genutzt.

## Google-Flow-Prompt-Sprache

- Flow-Anweisungen: Englisch
- sichtbarer Text: Deutsch

Szenenprompts nach Bild_01 folgen:

```text
SUBJECT
→ VISIBLE PROCESS
→ SPATIAL LAYOUT
→ CAMERA / SCALE
→ CONTINUITY REFERENCES
→ REQUIRED GERMAN TEXT
→ FORBIDDEN ELEMENTS
```

## Verbindlicher Google-Flow-Ablauf

### A – zuerst nur Bild_01

1. dauerhafte Agent Instructions laden
2. `STYLE_REFERENCE.png` anhaengen, falls vorhanden
3. ausschliesslich `Bild_01` erzeugen
4. echte Resultate auf Stil, Anatomie und deutsche Hook pruefen
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

Jedes Bild einzeln erzeugen, pruefen und benennen. Bei jeder Generation `Bild_01.png` wirklich anhaengen. Die vorgesehenen deutschen Labels muessen im Bild vorhanden sein oder als dokumentierter Text-Fallback markiert werden.

### C – Fehlerliste und Recovery

Fehlerhafte oder fehlende Bilder behalten ihre Nummer. Nach dem Hauptdurchlauf werden nur diese Bilder erneut erzeugt. Promptkorrektur muss den konkreten Fehler adressieren.

### D – finale ZIP

Nur akzeptierte finale Bilder, lueckenlose Nummerierung, keine Varianten oder Temp-Dateien.

## Echte Bild-QA

`image-review.json` darf erst nach Sichtpruefung des tatsaechlichen Bildes aktualisiert werden.

Pflicht:

- scientific_accuracy >= 8/10
- voiceover_match >= 8/10
- immediate_clarity >= 8/10
- style_continuity >= 8/10
- composition >= 8/10
- label_accuracy >= 8/10
- ai_artifact_check = PASS
- scene_difference bestanden
- overall_score >= 8/10
- finale `Bild_XX.png` existiert

Kosmischer/dunkler Stil-Drift, fehlende deutsche Labels oder falsche Schreibweise = FAIL.

## Drei Phasen

### Phase 1 – Creative Director

Erstellt Recherche, Claim-Check, Mechanism Map, Script, Satz-Visual-Plan, Szenenplan, Label-Plan, Flow-Szenenprompts, scene-map.json, overlay-plan.json und Metadaten.

### Phase 2 – Nutzer + Voice-KI + Google Flow

1. Voiceover 1:1 erzeugen
2. Flow Agent Instructions setzen
3. Bild_01 mit deutscher Hook erzeugen und freigeben
4. Bild_01 als echte visuelle Referenz nutzen
5. restliche Bilder einzeln mit deutschen Labels erzeugen
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
- wichtige Labels fehlen oder sind falsch geschrieben
- kosmischer/dunkler/medizinischer Stil-Drift
- Phase-2-Review ohne vorhandene finale Bilddatei

Ein einzelner Flow-Generierungsfehler ist kein globaler Blocker; dafuer gibt es Fehlerliste + Recovery.
