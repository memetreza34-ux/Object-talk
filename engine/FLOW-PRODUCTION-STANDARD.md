# Flow Production Standard

Diese Datei definiert die verbindliche Produktionslogik fuer Google Flow.

## 1. Grundprinzip: Referenz zuerst

Object-Talk darf Stiltreue nicht nur durch Text behaupten.

Referenzreihenfolge:

1. `assets/channel/STYLE_REFERENCE.png` – kanalweite Style-Referenz, sobald freigegeben
2. `Bild_01.png` – Episode-Style- und Continuity-Referenz
3. optionale Objekt-/Character-Referenzen unter `assets/channel/references/` bzw. `assets/channel/characters/`
4. konkreter Szenenprompt

Ein Satz wie `Using Bild_01 as the exact style reference` ersetzt niemals das tatsaechliche Anhaengen von `Bild_01.png` als visueller Referenz in Flow.

Solange `STYLE_REFERENCE.png` fehlt:

- nur `Bild_01` darf ohne kanalweite Bildreferenz erzeugt werden
- `Bild_01` wird besonders streng geprueft
- nach Freigabe muss `Bild_01.png` als echtes Ingredient/Reference an jede Folgegeneration angehaengt werden

## 2. Dauerhafte Flow-Agent-Instructions

Dauerhafte Regeln stehen in:

```text
engine/FLOW-AGENT-INSTRUCTIONS.md
```

Der Video-Prompt beschreibt vor allem den konkreten Bildinhalt, die exakten deutschen Texte und die Komposition.

## 3. Verbindliche Bildwelt

Die Kanalwelt ist eine **helle, freundliche, hochwertige 3D-Animationsfilm-Welt**.

Verbindlich:

- premium stilisierte 3D-Feature-Animation
- deutlich animiert, nicht fotorealistisch
- hell und freundlich als Standard
- weiche gerundete skulptierte Formen
- matte/satinierte Premium-Materialien
- warmes Hauptlicht, weiches Fill-Light, dezentes Rim-Light
- klare Tiefenwirkung und klare Silhouetten
- frische kontrollierte Farben: Creme, Apricot, Coral, warmes Rot, Himmelblau, Teal
- Biologie fachlich erkennbar, aber klar vereinfacht
- keine erzwungenen Gesichter auf Molekuelen, Organen oder Zellen

Harte Verbote:

- kosmische / Weltraum-artige Optik
- Galaxie-, Nebel- oder Sternenhintergruende
- dunkle violette Mikrowelt als Default
- Sci-Fi-Tunnel / Neon-Labor
- Medical-CGI / Anatomiesoftware
- realistische Haut/Poren
- nasse Gewebetexturen
- Corporate-Stock-3D
- billiger Toy-Look
- Anime / Comic
- Gore / Horror

## 4. Sichtbarer Text ist Teil der Erklaerung

Flow-Bilder sind **nicht mehr standardmaessig textfrei**.

Verbindlich:

- sichtbarer Text ausschliesslich Deutsch
- `Bild_01` muss eine kurze starke deutsche Hook enthalten
- normale Szenen erhalten normalerweise 1–3 kurze deutsche Labels
- Labelbegriffe kommen aus `02_bildprompts/label-plan.json`
- nur die wichtigsten Strukturen/Prozesse beschriften
- gut lesbare Sans-Serif-Typografie
- keine Textwaende
- keine englischen sichtbaren Woerter

### Text-Recovery

Wenn Flow einen Begriff falsch schreibt:

1. gleiche Szene mit exakt hervorgehobenem Begriff regenerieren
2. maximal einen weiteren Text-Versuch
3. bei wiederholtem Fehler sauberes Bild mit freier Labelzone erzeugen
4. exakt denselben deutschen Begriff spaeter in Remotion setzen

Der Remotion-Fallback ist eine Fehlerbehandlung, nicht der Standard. Das finale Video darf nie die geplanten deutschen Labels verlieren.

## 5. Bild_01

`Bild_01` ist immer:

1. Cover
2. erster Shot
3. Episode-Master-Style-Frame
4. Referenz fuer alle weiteren Bilder

Ablauf:

1. kompletten Auftrag lesen
2. vorhandene `STYLE_REFERENCE.png` tatsaechlich anhaengen, falls vorhanden
3. ausschliesslich `Bild_01` erzeugen
4. 2–4 Varianten erzeugen, wenn moeglich
5. beste Variante visuell pruefen
6. bei FAIL regenerieren
7. bei PASS als `Bild_01.png` speichern
8. genau einmal Nutzerfreigabe einholen

`Bild_01` ist FAIL, wenn:

- die deutsche Hook fehlt oder falsch geschrieben ist
- es kosmisch, duester oder Sci-Fi-artig wirkt
- es wie Medical-CGI, Anatomiesoftware oder Stock-3D aussieht
- es babyhaft oder billig wirkt
- das Thema nicht sofort erkennbar ist

## 6. Folgegenerationen

Nach Freigabe von `Bild_01` gilt fuer jedes weitere Bild:

- `STYLE_REFERENCE.png` anhaengen, wenn vorhanden
- `Bild_01.png` immer anhaengen
- relevante Objekt-/Character-Referenzen anhaengen
- Szene einzeln erzeugen
- exakte deutsche Labels aus dem Szenenprompt verwenden

## 7. Szenenprompt-Schema

Jeder Prompt folgt dieser Reihenfolge:

```text
1. SUBJECT
2. VISIBLE PROCESS / CHANGE
3. SPATIAL LAYOUT
4. CAMERA / SCALE
5. STYLE CONTINUITY
6. REQUIRED GERMAN TEXT
7. FORBIDDEN ELEMENTS
```

Beispiel:

```text
Create a bright 16:9 premium 3D animated-film macro cross-section. One large rounded alveolus fills the left side and one narrow capillary fills the right side. Show four pale-cyan paired O2 molecules crossing the thin central barrier from alveolus to blood; keep deep-red biconcave red blood cells only inside the capillary. Camera: close 3/4 macro cutaway with the barrier in sharp focus. Match the attached references for rounded materials and warm friendly lighting. Add the exact German labels “Sauerstoff” and “Blut” in clean readable sans-serif type with minimal leader lines. No cosmic background, no sci-fi glow, no medical CGI, no faces, no English text.
```

Vermeiden:

- `beautiful world` ohne konkrete Komposition
- `cinematic` als Ersatz fuer Kamerabeschreibung
- dunkle Plum-/Navy-Welten als automatischer Hintergrund
- abstrakte Mikro-Welten, die wie Weltraum aussehen

## 8. Wiederkehrende visuelle Elemente

Fuer Pilot 001:

- O2 = zwei verbundene blass-cyanfarbene Kugeln, gesichtslos
- CO2 = neutral-violett/graue Drei-Kugel-Form, gesichtslos
- rote Blutkoerperchen = tiefe warmrote bikonkave Scheiben, gesichtslos
- Haemoglobin = burgunderrote vereinfachte Struktur
- Mitochondrien = wiedererkennbarer konsistenter Organell-Look

Akzeptierte Referenzen werden unter `assets/channel/references/` gespeichert und bei relevanten Szenen angehaengt.

## 9. Produktion in 5er-Bloecken

Nach Freigabe von Bild_01:

```text
Bild_02–06
Bild_07–11
Bild_12–16
Bild_17–21
...
```

Jedes Bild wird einzeln erzeugt und bewertet.

Nach jedem Block intern pruefen:

- Referenzen tatsaechlich verwendet
- heller Premium-Animationslook erhalten
- kein kosmischer/dunkler Drift
- gleiche Material-/Licht-/Farbwelt
- wiederkehrende Objekte konsistent
- fachlich plausibel
- geforderte deutsche Labels vorhanden und korrekt
- kein englischer sichtbarer Text

## 10. Visuelle QA ist echt, nicht nur JSON

`image-review.json` darf erst nach Sichtpruefung des tatsaechlichen Bildes aktualisiert werden.

Pflichtkriterien:

- scientific_accuracy
- voiceover_match
- immediate_clarity
- style_continuity
- composition
- label_accuracy
- ai_artifact_check
- scene_difference
- overall_score

Score unter 8/10, fehlender Text, falsches Deutsch oder klarer Fach-/Stilfehler = Regeneration.

## 11. Recovery

Bei FAIL:

1. Bildnummer behalten
2. konkreten Fehlergrund notieren
3. Prompt nur am Fehler nachschaerfen
4. bis zu 3 automatische Neuversuche
5. keine Ersatznummern erfinden

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
- nur akzeptierte Varianten
- 16:9
- die geplanten deutschen Texte sind entweder korrekt im Flow-Bild oder exakt als dokumentierter Remotion-Fallback vorgesehen

## 13. Harte Verbote

Flow darf niemals:

- eine nur erwaehnte Referenz als angehaengte Referenz behandeln
- die Kanal-DNA ignorieren
- einen neuen Stil pro Szene erfinden
- kosmische, duestere oder Sci-Fi-Mikrowelten als Standard erzeugen
- in Fotorealismus oder Medical-CGI driften
- Molekuele/Organe/Zellen ohne Grund personifizieren
- die deutsche Cover-Hook weglassen
- wichtige geplante deutsche Labels grundlos weglassen
- englische sichtbare Texte erzeugen
- nach Bild_01 weitere Freigaben verlangen
- Szenen erfinden, loeschen oder zusammenlegen
- fehlgeschlagene Bilder vergessen
