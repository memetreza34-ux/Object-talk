# Flow Production Standard

Diese Datei definiert die verbindliche Produktionslogik fuer Google Flow.

## 1. Grundprinzip: Referenz zuerst

Referenzreihenfolge:

1. `assets/channel/STYLE_REFERENCE.png` – kanalweite Style-Referenz, sobald freigegeben
2. `Bild_01.png` – Episode-Style- und Continuity-Referenz
3. optionale Objekt-/Character-Referenzen
4. konkreter Szenenprompt

Ein Satz wie `Using Bild_01 as the exact style reference` ersetzt niemals das tatsaechliche Anhaengen von `Bild_01.png` in Flow.

Solange `STYLE_REFERENCE.png` fehlt:
- nur `Bild_01` darf ohne kanalweite Bildreferenz erzeugt werden
- Bild_01 wird besonders streng geprueft
- nach Freigabe muss Bild_01 bei jeder Folgegeneration wirklich angehaengt werden

## 2. Dauerhafte Flow-Agent-Instructions

Dauerhafte Regeln stehen in:

```text
engine/FLOW-AGENT-INSTRUCTIONS.md
```

Der Video-Prompt beschreibt den konkreten Bildinhalt, exakten deutschen Text und die Komposition.

## 3. Verbindliche Bildwelt

Die Kanalwelt ist eine **helle, freundliche, hochwertige theatrale 3D-Animationsfilm-Welt**.

Verbindlich:
- premium 3D-Feature-Animation
- deutlich animiert, nicht fotorealistisch
- weich gerundete skulptierte Formen
- matte/satinierte Premium-Materialien
- warmes Hauptlicht, weiches Fill-Light, dezentes Rim-Light
- klare Vordergrund-/Mittelgrund-/Hintergrundstaffelung
- gezielte Kamera statt flacher Diagramm-Ansicht
- frische Farben: Creme, Apricot, Coral, warmes Rot, Himmelblau, Teal
- Biologie fachlich erkennbar, aber vereinfacht
- biologische Strukturen normalerweise gesichtslos

### Menschen-Regel

Menschen sind **nicht** die Standard-Bildsprache.

Flow darf nicht automatisch erzeugen:
- Kind oder Erwachsener als Presenter
- sichtbares Gesicht als Hauptmotiv
- Mensch neben isolierten Organen
- transparenter Oberkoerper als Cover-Hero
- Anatomie-Torso / Mannequin / Schulmodell
- frontal aufgeschnittenen Koerper als Lehrtafel

Wenn menschlicher Kontext wissenschaftlich noetig ist, nur als vereinfachte gesichtslose Silhouette oder partielle Huelle im Hintergrund. Organ/Prozess bleibt Hauptmotiv.

### Poster-Regel

Harter FAIL:
- Anatomieposter
- Schulbuchgrafik
- medizinische Lehrtafel
- flache Infografik
- isolierte Organstuecke auf neutralem Hintergrund
- Dashboard-/Kartenlayout

Jedes Bild soll wie ein Filmframe inszeniert sein: Perspektive, Tiefenstaffelung, Licht, Vordergrundueberlagerung und klare Blickfuehrung.

### Weitere harte Verbote

- kosmische / Weltraum-artige Optik
- Galaxie-/Nebelhintergruende
- dunkle violette Mikrowelt als Default
- Sci-Fi-Tunnel / Neon-Labor
- Medical-CGI / Anatomiesoftware
- realistische Haut/Poren
- nasse Gewebetexturen
- Corporate-Stock-3D
- billiger Toy-Look
- Anime / Comic
- Gore / Horror

## 4. Sichtbarer Text

Flow-Bilder enthalten den geplanten deutschen Text.

Verbindlich:
- sichtbarer Text ausschliesslich Deutsch
- `Bild_01` mit kurzer starker Hook
- normale Szenen normalerweise 1–3 kurze Labels
- Begriffe aus `02_bildprompts/label-plan.json`
- saubere Sans-Serif-Typografie
- keine Textwaende
- kein englischer sichtbarer Text

### Text-Recovery

Bei falscher Schreibweise:
1. gleiche Szene mit exakt hervorgehobenem Begriff regenerieren
2. maximal einen weiteren Text-Versuch
3. dann sauberes Bild mit freier Labelzone erzeugen
4. denselben deutschen Begriff spaeter exakt in Remotion setzen

## 5. Bild_01

`Bild_01` ist Cover, erster Shot, Episode-Master-Style-Frame und Referenz fuer alle Folgebilder.

Ablauf:
1. Agent Instructions laden
2. STYLE_REFERENCE anhaengen, falls vorhanden
3. nur Bild_01 erzeugen
4. 3 Varianten erzeugen, wenn moeglich
5. automatisch alle ungeeigneten Varianten verwerfen
6. beste PASS-Variante zeigen
7. genau einmal Nutzerfreigabe einholen

### Bild_01 Hard FAIL

- deutsche Hook fehlt/falsch
- Kind/Erwachsener/Presenter sichtbar
- sichtbares Gesicht als Hero
- Torso-Mannequin / transparenter Oberkoerper dominiert
- Anatomieposter-/Schulbuchkomposition
- kosmisch / dunkel / Sci-Fi
- Medical-CGI / Anatomiesoftware / Stock-3D
- babyhaft / billig
- Thema nicht sofort erkennbar

Bei Biologie-Covern ist der biologische Prozess selbst der Hero.

## 6. Folgegenerationen

Nach Freigabe von Bild_01:
- STYLE_REFERENCE anhaengen, wenn vorhanden
- Bild_01 immer anhaengen
- relevante Objekt-/Character-Referenzen anhaengen
- jede Szene einzeln erzeugen
- exakte deutsche Labels verwenden
- Filmframe-Komposition und Kameratiefe beibehalten

## 7. Szenenprompt-Schema

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
Create a bright 16:9 premium animated-feature macro scene. One large rounded alveolus fills the left foreground and one narrow capillary curves through the right midground. Show four paired pale-cyan O2 molecules crossing the thin barrier from alveolus to blood; keep deep-red biconcave red blood cells only inside the capillary. Camera: close 3/4 macro with clear foreground and background depth. Match the attached reference for materials, lighting and palette. Add the exact German labels “Sauerstoff” and “Blut”. No human presenter, no anatomy poster, no cosmic background, no medical CGI, no English text.
```

## 8. Wiederkehrende Elemente Pilot 001

- O2 = zwei verbundene blass-cyanfarbene Kugeln, gesichtslos
- CO2 = neutral-violett/graue Drei-Kugel-Form, gesichtslos
- rote Blutkoerperchen = tiefe warmrote bikonkave Scheiben, gesichtslos
- Haemoglobin = burgunderrote vereinfachte Struktur
- Mitochondrien = konsistenter Organell-Look

Akzeptierte Referenzen unter `assets/channel/references/` speichern und bei relevanten Szenen anhaengen.

## 9. Produktion in 5er-Bloecken

Nach Bild_01:

```text
Bild_02–06
Bild_07–11
Bild_12–16
Bild_17–21
...
```

Jedes Bild einzeln erzeugen und bewerten.

Interne Block-QA:
- Referenzen wirklich verwendet
- Filmframe statt Poster
- keine Menschen-Presenter / Torso-Mannequins
- heller Premium-Animationslook
- kein kosmischer/dunkler Drift
- gleiche Material-/Licht-/Farbwelt
- wiederkehrende Objekte konsistent
- fachlich plausibel
- deutsche Labels korrekt
- kein englischer sichtbarer Text

## 10. Echte visuelle QA

`image-review.json` erst nach Sichtpruefung des tatsaechlichen Bildes aktualisieren.

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

Jeder zentrale Score mindestens 8/10. Mensch-/Torso-/Poster-Hard-Fails koennen nicht durch einen Durchschnittsscore ausgeglichen werden.

## 11. Recovery

Bei FAIL:
1. Bildnummer behalten
2. konkreten Fehler notieren
3. Prompt nur am Fehler nachschaerfen
4. bis zu 3 automatische Neuversuche
5. keine Ersatznummern erfinden

## 12. Finaler Bilderordner

```text
<video-id>_bilder/
```

Darin nur `Bild_01.png` bis `Bild_NN.png`, lueckenlos, 16:9 und nur akzeptierte Varianten.

## 13. Harte Verbote

Flow darf niemals:
- eine nur erwaehnte Referenz als angehaengte Referenz behandeln
- Human-Presenter / Kind / sichtbares Gesicht zum Standard machen
- Torso-Mannequins oder Anatomieposter als Kanalstil akzeptieren
- einen neuen Stil pro Szene erfinden
- kosmische oder Sci-Fi-Mikrowelten als Standard erzeugen
- in Fotorealismus oder Medical-CGI driften
- Molekuele/Organe/Zellen ohne Grund personifizieren
- die deutsche Cover-Hook weglassen
- wichtige Labels grundlos weglassen
- englischen sichtbaren Text erzeugen
- nach Bild_01 weitere Freigaben verlangen
