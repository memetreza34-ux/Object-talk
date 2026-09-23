# Flow Production Standard

Diese Datei definiert die verbindliche Produktionslogik fuer Google Flow.

## 1. Grundprinzip: Referenz zuerst

Object-Talk darf den visuellen Stil nicht nur durch Text beschreiben und hoffen, dass Flow ihn reproduziert.

Verbindliche Referenzreihenfolge:

1. `assets/channel/STYLE_REFERENCE.png` – kanalweite Style-Referenz, sobald freigegeben
2. `Bild_01.png` – Episode-Style- und Continuity-Referenz
3. optionale Objekt-/Character-Referenzen unter `assets/channel/references/` bzw. `assets/channel/characters/`
4. erst danach der konkrete Szenenprompt

Ein Satz wie `Using Bild_01 as the exact style reference` ersetzt **niemals** das tatsaechliche Anhaengen von `Bild_01` als visueller Referenz in Flow.

Solange `STYLE_REFERENCE.png` noch fehlt, gilt Bootstrap-Modus:

- nur `Bild_01` darf ohne kanalweite Bildreferenz erzeugt werden
- `Bild_01` wird besonders streng geprueft
- nach Freigabe muss `Bild_01` als echtes Bild-Ingredient/Referenz an jede Folgegeneration angehaengt werden
- keine Massenproduktion von Folgeframes nur auf Basis textlicher Stilregeln

## 2. Dauerhafte Flow-Agent-Instructions

Die dauerhafte Verhaltenslogik liegt in:

```text
engine/FLOW-AGENT-INSTRUCTIONS.md
```

Sie enthaelt Kanal-DNA, Verbote, Referenzregeln, QA und Produktionsablauf.

Der jeweilige Video-Prompt soll diese Regeln nicht als langen Stilroman wiederholen. Er beschreibt primaer den konkreten Bildinhalt.

## 3. Kanal-DNA

Oberste schriftliche Stilreferenz:

```text
bildwelt/OBJECT-TALK-CHANNEL-DNA.md
```

Verbindlich:

- hochwertige stilisierte 3D-Feature-Animation
- deutlich animiert und nicht fotorealistisch
- weiche gerundete skulptierte Formen
- matte/satinierte Premium-Materialien
- warme filmische Beleuchtung
- weiches Rim-Light
- starke Tiefenwirkung
- kontrollierte kraeftige Farben
- Biologie fachlich erkennbar, aber klar vereinfacht
- keine erzwungenen Gesichter auf Molekuelen, Organen oder Zellen

Harte Verbote:

- Medical-CGI
- Anatomiesoftware-Look
- realistische Haut/Poren
- nasse Gewebetexturen
- Corporate-Stock-3D
- billiger Toy-Look
- Anime
- Comic
- Gore/Horror
- Stilwechsel zwischen Szenen

## 4. Flow erzeugt Visuals, Remotion erzeugt Text

Flow-Bilder sind standardmaessig **textfrei**.

Flow darf nicht mehr fuer jede Szene deutsche Labels, Pfeile oder Erklaertexte rendern. Dadurch werden Rechtschreibfehler, KI-Gibberish, falsche Pointer und unnoetige Regenerationen vermieden.

Verbindlich:

- Hook von `Bild_01` wird in Remotion gesetzt
- Labels kommen aus `02_bildprompts/label-plan.json`
- Flow-Prompt enthaelt normalerweise `No text, no labels, no typography, no arrows.`
- nur wenn eine aktuelle ausdrueckliche Nutzeranweisung Text direkt im Bild verlangt, darf davon abgewichen werden

## 5. Bild_01

`Bild_01` ist immer:

1. Cover-Grundbild
2. erster Shot
3. Episode-Master-Style-Frame
4. Referenz fuer alle weiteren Bilder

Ablauf:

1. kompletten Auftrag lesen
2. vorhandene `STYLE_REFERENCE.png` tatsaechlich als visuelle Referenz anhaengen, falls vorhanden
3. ausschliesslich `Bild_01` erzeugen
4. 2–4 Varianten erzeugen, wenn technisch moeglich
5. beste Variante visuell pruefen
6. bei FAIL regenerieren
7. bei PASS als `Bild_01.png` speichern
8. genau einmal Nutzerfreigabe einholen

FAIL, wenn Bild_01 wie Medical-CGI, Anatomiesoftware, Corporate-Stock-3D, billige Kinderanimation, Fotorealismus oder ein anderer Kanalstil aussieht.

## 6. Folgegenerationen

Nach Freigabe von `Bild_01` gilt fuer **jedes** weitere Bild:

- `STYLE_REFERENCE.png` anhaengen, wenn vorhanden
- `Bild_01.png` immer anhaengen
- relevante wiederkehrende Objekt-/Character-Referenzen anhaengen, falls vorhanden
- dann erst den konkreten Szenenprompt ausfuehren

Flow darf niemals behaupten, eine Referenz zu verwenden, die technisch nicht angehaengt wurde.

## 7. Szenenprompt-Schema

Jeder Folgeprompt folgt dieser Reihenfolge:

```text
1. SUBJECT
2. VISIBLE PROCESS / CHANGE
3. SPATIAL LAYOUT
4. CAMERA / SCALE
5. CONTINUITY REQUIREMENTS
6. FORBIDDEN ELEMENTS
```

Beispiel:

```text
16:9 macro cross-section. One large rounded alveolus fills the left side and one narrow capillary fills the right side. Show exactly four pale-cyan paired O2 molecules crossing the thin central barrier from alveolus to blood; keep deep-red biconcave red blood cells only inside the capillary. Camera: close 3/4 macro cutaway with the barrier in sharp focus. Match the attached references for materials, lighting, palette and shape language. No faces, no mascot, no wet tissue, no medical CGI, no text, no labels, no arrows.
```

Vermeiden:

- `beautiful world`
- `premium hero composition` ohne konkrete Komposition
- `cinematic` als Ersatz fuer Kamerabeschreibung
- unklare Begriffe ohne raeumliche Anweisung

## 8. Wiederkehrende visuelle Elemente

Wiederkehrende Elemente muessen stabil aussehen.

Fuer Pilot 001 insbesondere:

- O2 = zwei verbundene blass-cyanfarbene Kugeln, gesichtslos
- CO2 = neutral-violett/graue Drei-Kugel-Form, gesichtslos
- rote Blutkoerperchen = tiefe warmrote bikonkave Scheiben, gesichtslos
- Haemoglobin = burgunderrote vereinfachte Struktur
- Mitochondrien = wiedererkennbarer konsistenter Organell-Look

Wenn fuer ein wiederkehrendes Element eine akzeptierte Referenz vorliegt, wird sie unter `assets/channel/references/` gespeichert und fuer relevante Szenen angehaengt.

## 9. Produktion in 5er-Bloecken

Nach Freigabe von Bild_01:

```text
Bild_02–06
Bild_07–11
Bild_12–16
Bild_17–21
...
```

Innerhalb jedes Blocks wird jedes Bild **einzeln** erzeugt und bewertet.

Nach jedem Block intern pruefen:

- Referenzen tatsaechlich verwendet
- gleicher Object-Talk-Look
- gleiche Materialwelt
- gleiche Lichtlogik
- gleiche Farbwelt
- wiederkehrende Objekte konsistent
- fachlich plausibel
- kein Realismus- oder Stock-3D-Drift
- keine ungewollte Schrift im Bild

Danach automatisch mit dem naechsten Block fortfahren.

## 10. Visuelle QA ist echt, nicht nur JSON

`image-review.json` darf erst nach Sichtpruefung des tatsaechlichen generierten Bildes aktualisiert werden.

Ein Zahlenwert oder `decision: ACCEPT` ohne Bildsichtung ist ungueltig.

Pflichtkriterien:

- scientific_accuracy
- voiceover_match
- immediate_clarity
- style_continuity
- composition
- ai_artifact_check
- scene_difference
- overall_score

Score unter 8/10 oder klarer Fach-/Stilfehler = Regeneration.

## 11. Recovery

Bei FAIL:

1. Bildnummer notieren
2. Fehlergrund konkret notieren
3. regulären Lauf fortsetzen, wenn sinnvoll
4. am Ende Recovery-Pass
5. Prompt nur am konkreten Fehler nachschaerfen
6. bis zu 3 automatische Neuversuche pro fehlerhafter Szene
7. keine Ersatznummern erfinden

## 12. Finaler Bilderordner

Am Ende genau einen finalen Ordner erstellen:

```text
<video-id>_bilder/
```

Darin ausschliesslich:

```text
Bild_01.png
Bild_02.png
...
Bild_NN.png
```

Regeln:

- keine Luecken
- jede Nummer genau einmal
- keine Namen wie `final2`, `neu`, `copy`, `v3`
- nur akzeptierte Varianten
- 16:9
- keine eingebrannten Flow-Labels, sofern nicht ausdruecklich angeordnet

Zusaetzlich eine ZIP desselben Ordners erstellen.

## 13. Harte Verbote

Flow darf niemals:

- eine nur erwaehnte Referenz als tatsaechlich angehaengte Referenz behandeln
- die Kanal-DNA ignorieren
- einen neuen Stil pro Szene erfinden
- in Fotorealismus oder Medical-CGI driften
- realistische Haut/Gewebe erzeugen
- zufaellige Character-Designs erzeugen
- Molekuele/Organe/Zellen ohne konkreten Grund personifizieren
- Labels oder Text standardmaessig direkt in Bilder schreiben
- nach Bild_01 weitere Freigaben verlangen
- Szenen erfinden, loeschen oder zusammenlegen
- fehlgeschlagene Bilder vergessen
