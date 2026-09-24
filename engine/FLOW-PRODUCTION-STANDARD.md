# Flow Production Standard

Diese Datei definiert die verbindliche Produktionslogik fuer Google Flow.

## 1. Referenz zuerst

Referenzreihenfolge:

1. `assets/channel/STYLE_REFERENCE.png`
2. `Bild_01.png`
3. Objekt-/Character-Referenzen
4. konkreter Szenenprompt

Ein Satz wie `Using Bild_01 as reference` ersetzt niemals das echte Anhaengen von `Bild_01.png`.

Solange `STYLE_REFERENCE.png` fehlt:
- nur `Bild_01` darf ohne kanalweite Bildreferenz entstehen
- Bild_01 wird besonders streng geprueft
- danach muss Bild_01 bei jeder Folgegeneration wirklich angehaengt werden

## 2. Dauerhafte Flow-Regeln

```text
engine/FLOW-AGENT-INSTRUCTIONS.md
bildwelt/OBJECT-TALK-CHANNEL-DNA.md
bildwelt/EXPLAINER-STYLE-LOCK.md
```

## 3. Verbindliche Explainer-Bildwelt

Fuer Biologie-/Erklaerszenen gilt:

**moderne stilisierte 2.5D / Soft-3D Educational Illustration**

Leitidee:

**80 % animierte Illustration + 20 % Soft-3D-Tiefe + 0 % Medical-CGI.**

Verbindlich:
- klar animiert / illustriert
- nicht fotorealistisch
- weich gerundete vereinfachte Formen
- matte bis leicht satinierte Oberflaechen
- weiche Farbverlaeufe
- subtile Schatten
- leichte Tiefenstaffelung
- ruhige helle Hintergruende
- eine Hauptaussage pro Bild
- wenige Objekte
- Klarheit wichtiger als Detailreichtum

Semantische Farben:
- O2 = Cyan / Tuerkis
- rote Blutkoerperchen = tiefes warmes Rot
- Blutgefaesse = Coral / Rot
- Organe = Peach / Coral
- Muskelzellen = Orange / Apricot
- CO2 = weiches Violett
- ATP = warmes Gelb / Gold
- Hintergrund = Creme / helles Blau / weiches Beige

Harte Stilverbote:
- Photorealismus
- Medical-CGI / Anatomiesoftware
- nasses Fleisch / Gewebe
- Mikroskop-Fotorealismus
- dunkle violette Sci-Fi-Mikrowelt
- Weltraum / Galaxy
- Human-Presenter
- Torso-Mannequin
- ueberladene Infografik
- billiger Toy-Look

## 4. Object-Talk Character Mode

Fuer sprechende Lebensmittel / Alltagsobjekte bleibt der hochwertige stilisierte 3D-Character-Look erlaubt.

Dieser Modus darf nicht automatisch auf Organe, Molekuele und Zellen uebertragen werden.

## 5. Sichtbarer Text

Cover:
- nur die festgelegte deutsche Hook
- keine Anatomie-Labels

Normale Szenen:
- 0–2 kurze deutsche Labels bevorzugt
- maximal 3 bei echtem Bedarf
- keine Textwaende
- kein englischer sichtbarer Text

Bei falscher Flow-Schreibweise:
1. regenerieren
2. maximal einen weiteren Text-Versuch
3. danach exakter Remotion-Fallback

## 6. Bild_01

`Bild_01` ist Cover, erster Shot, Episode-Master-Frame und Referenz fuer Folgebilder.

Ablauf:
1. Agent Instructions laden
2. STYLE_REFERENCE anhaengen, falls vorhanden
3. nur Bild_01 erzeugen
4. 3 Varianten, wenn moeglich
5. ungeeignete Varianten automatisch verwerfen
6. beste PASS-Variante zeigen
7. genau einmal Nutzerfreigabe

Bild_01 Hard FAIL:
- Hook fehlt / falsch
- Zusatzlabels auf Cover
- photorealistisch / medizinisch
- Mensch / Presenter / Torso-Mannequin
- kosmisch / Sci-Fi
- ueberladen
- Thema nicht sofort erkennbar

## 7. Folgegenerationen

Nach Freigabe:
- STYLE_REFERENCE anhaengen, wenn vorhanden
- Bild_01 immer anhaengen
- relevante Objekt-/Character-Referenzen anhaengen
- jede Szene einzeln erzeugen
- pro Szene genau eine Hauptaussage
- semantische Farben stabil halten
- nur notwendige Labels verwenden

## 8. Szenenprompt-Schema

```text
1. ONE TEACHING IDEA
2. MAIN SUBJECT
3. START / END
4. MOVEMENT / CHANGE
5. SIMPLE SPATIAL LAYOUT
6. SOFT-3D STYLE CONTINUITY
7. REQUIRED GERMAN TEXT
8. FORBIDDEN ELEMENTS
```

Beispiel:

```text
Create a modern stylized 2.5D / soft-3D educational illustration. One large simplified rounded alveolus fills the left side and one smooth coral-red capillary runs along the right side. Show five cyan oxygen particles crossing the thin barrier from the alveolus into the blood. Keep deep-red blood cells only inside the vessel. Use matte surfaces, soft gradients, subtle shadows and a light cream / soft-blue background. Add only the German labels “Sauerstoff” and “Blut”. No photorealism, no medical CGI, no wet tissue, no human presenter, no cosmic background.
```

## 9. Wiederkehrende Elemente Pilot 001

- O2 = Cyan / Tuerkis
- CO2 = weiches Violett
- rote Blutkoerperchen = tiefes warmes Rot
- Haemoglobin = Burgunder
- Gefaesse = Coral / Rot
- Organe = Peach / Coral
- Muskelzellen = Apricot / Orange
- ATP = Gelb / Gold

Akzeptierte Referenzen unter `assets/channel/references/` speichern und bei relevanten Szenen anhaengen.

## 10. QA

`image-review.json` erst nach Sichtpruefung des echten Bildes aktualisieren.

Pflichtkriterien:
- scientific_accuracy
- voiceover_match
- immediate_clarity
- style_continuity
- composition
- label_accuracy, wenn Labels vorgesehen
- ai_artifact_check
- scene_difference
- overall_score

Jeder zentrale Score mindestens 8/10.

Hard FAIL kann nicht durch Durchschnittsscore ausgeglichen werden.

## 11. Recovery

Bei FAIL:
1. gleiche Bildnummer behalten
2. konkreten Fehler notieren
3. nur diesen Fehler im Prompt korrigieren
4. bis zu 3 Neuversuche

## 12. Finaler Bilderordner

```text
<video-id>_bilder/
```

Nur akzeptierte `Bild_01.png` bis `Bild_NN.png`, lueckenlos und 16:9.

## 13. Harte Verbote

Flow darf niemals:
- nur erwaehnte Referenzen als angehaengt behandeln
- Explainer-Szenen in Medical-CGI oder Photorealismus driften lassen
- mehrere Lehrziele unnoetig in ein Bild packen
- semantische Farben grundlos aendern
- Cover-Zusatzlabels erzeugen
- nach Bild_01 weitere Freigaben verlangen
