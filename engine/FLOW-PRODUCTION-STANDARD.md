# Flow Production Standard

Diese Datei definiert die verbindliche Produktionslogik für Google Flow.

## Ziel

Flow erzeugt konsistente, hochwertige Erklärbilder für den deutschen Object-Talk-Kanal. Die Bilder erklären den gesprochenen Inhalt sichtbar und gehören immer zur selben visuellen Welt.

Die freigegebene Kanalwelt ist zusätzlich beschrieben in:

```text
bildwelt/APPROVED-VISUAL-WORLD.md
```

## 1. Verbindliche Bildwelt

Der Kanal nutzt eine **stark stilisierte, filmische Premium-3D-Animationswelt**.

Verbindlich:

- klar animiert, nicht fotorealistisch
- weiche, skulptierte Formen
- vereinfachte, aber fachlich erkennbare Anatomie und Biologie
- hochwertige glatte Materialien
- kontrollierte filmische Beleuchtung mit klarer Lichtführung
- starke Tiefenwirkung und räumliche Staffelung
- bewusstes Production Design statt leerer Standardhintergründe
- modernes hochwertiges Color Grading
- nicht babyhaft, nicht spielzeughaft, nicht Corporate-Stock-3D
- echte Erklärbilder vor Mascot-/Presenter-Szenen
- keine Anime-, Comic-, Live-Action- oder medizinisch-fotorealistische Bildwelt
- kein Gore, keine Horror-Anatomie, keine nassen realistischen Gewebetexturen

### Freigegebene Inside-the-Body-Welt

Für Körper-, Blut-, Organ-, Gewebe- und Zellbilder:

- Creme, Apricot, Amber und Orange als warme Basis
- tiefes Rot/Burgunder für Blut, Gefäße und rote Blutkörperchen
- goldene Highlights
- dunklere warme Randbereiche für Tiefe
- blass Cyan/Türkis als klarer Sauerstoff-Kontrast
- glatte, hochwertige Materialien statt medizinischer Oberflächen
- Makro-/Mikro-Bilder mit deutlicher räumlicher Tiefe

Globaler Stilanker für Prompts:

```text
premium cinematic stylized 3D animated educational film, clearly non-photorealistic, sculpted soft forms, simplified but recognizable biology, polished premium materials, controlled dramatic cinematic lighting, subtle rim light, volumetric depth, sophisticated color grading, strong visual hierarchy, designed environment, warm amber-cream-burgundy palette with pale-cyan oxygen accents, modern high-end educational animation, no corporate stock 3D, no toy look, no medical realism, no wet tissue, no anime, no comic, no gore
```

## 2. Prompt-Sprache und sichtbarer Text

- Prompt-Anweisungen an Google Flow immer auf Englisch.
- Jeder sichtbare Text im fertigen Bild ausschließlich auf Deutsch.
- Kein englischer sichtbarer Text.
- Kein KI-Gibberish.
- Keine langen Textblöcke oder Untertitel im Bild.

## 3. Beschriftungsregel

Normale Erklärszenen:

- normalerweise 1–3 kurze deutsche Labels
- nur die wichtigsten Dinge beschriften
- Labels eindeutig zuordnen
- helle/weiße saubere Sans-Serif-Schrift
- dünne Führungslinien
- falsches, unlesbares oder englisches Label = Bild FEHLERHAFT
- wenn Flow Schrift wiederholt falsch rendert: textfreie Version + identischer Begriff später in Remotion

### Ausnahme Bild_01 / Cover

Bild_01 braucht standardmäßig **keine kleinen Anatomie-Labels**, wenn das Motiv visuell eindeutig ist. Ein gutes Cover soll nicht wie eine Infografik aussehen.

## 4. Bild_01 – Cover, Hook und Master Style Frame

`Bild_01` ist:

1. Cover-/Hook-Bild
2. erster sichtbarer Shot
3. visuelle Referenz für die Episode
4. Master Style Frame für alle weiteren Bilder

Bild_01 muss die **beste visuelle Qualität der Episode** zeigen.

Pflicht:

- Thema auf einen Blick verständlich
- Hauptmotiv groß und präsent, ungefähr 50–65 % der Bildhöhe
- keine winzige Figur in viel leerer Fläche
- kein weißer/beiger Präsentationsbanner
- filmischer Hintergrund mit Tiefe und Licht, aber nicht überladen
- klare Lichtführung und hochwertiges Color Grading
- Überschrift maximal zwei kurze Zeilen
- Überschrift in ruhigem, bewusst gestaltetem Bereich mit gutem Kontrast
- Überschrift niemals über Gesicht, Organ oder Hauptprozess
- standardmäßig keine kleinen Labels auf dem Cover
- das Bild muss auch ohne Text als starkes Key Visual funktionieren

Harte FAIL-Kriterien für Bild_01:

- generischer Corporate-3D-Stock-Look
- spielzeughafte/niedliche Standardfigur
- blasser beiger Hintergrund ohne Tiefe
- Figur zu klein
- Bild wirkt wie Schulbuch/PowerPoint
- Titel wirkt wie separat aufgeklebter Banner
- Titel kollidiert mit Hauptmotiv
- schwacher Kontrast oder gleichmäßige flache Beleuchtung

## 5. Phase A – zuerst nur Bild_01

1. Flow liest den kompletten Auftrag.
2. Flow erzeugt ausschließlich `Bild_01`.
3. Noch kein `Bild_02`.
4. Prüfen:
   - starkes Key Visual?
   - Premium-3D statt Stock-3D?
   - Hauptmotiv groß genug?
   - filmische Tiefe/Licht?
   - Cover-Layout sauber?
   - Hook korrektes Deutsch?
   - keine Textkollision?
   - keine zu realistische Darstellung?
5. Bei FAIL nur Bild_01 regenerieren.
6. Bei PASS als `Bild_01.png` speichern.
7. STOPP und auf Nutzerfreigabe warten.

## 6. Bild_01 als Vorlage für alle weiteren Bilder

Nach Freigabe muss Flow `Bild_01.png` bei jeder weiteren Generation als Style-/Continuity-Referenz verwenden, soweit technisch möglich.

Von Bild_01 übernehmen:

- Renderstil
- Grad der Stilisierung
- Lichtlogik
- Color Grading
- Materialqualität
- Kontrast und Tiefenwirkung
- Formensprache
- Anatomie-Vereinfachung
- wiederkehrende visuelle Symbole

Nicht blind übernehmen:

- konkrete Pose
- Motiv
- Bildaufbau
- fachlich falsche Anatomie

Folgeframes müssen aussehen, als kämen sie aus demselben Film, Renderprozess und Lichtsetup. Stilabweichung = Regeneration.

## 7. Szenenprompts – kurz, aber vollständig

Nach Bild_01:

- etwa 2–5 Sätze
- konkrete Szene
- sichtbarer Prozess
- wichtigste Komposition/Perspektive
- benötigte deutsche Labels
- nicht den kompletten Stilblock wiederholen

Jeder Folgeprompt beginnt sinngemäß mit:

```text
Using Bild_01 as the exact style reference, keep the same premium cinematic stylized 3D world, the same lighting logic, material quality, color grading and anatomy simplification.
```

## 8. Produktion in 5er-Blöcken

Nach Freigabe von Bild_01:

```text
Block 1: Bild_02–Bild_06
Block 2: Bild_07–Bild_11
Block 3: Bild_12–Bild_16
Block 4: Bild_17–Bild_21
Block 5: Bild_22–Bild_26
Block 6: Bild_27–Bild_31
...
```

Wichtig:

- jedes Bild einzeln generieren
- nach jedem Bild Einzel-QA
- nach jedem 5er-Block Stil-/Nummerierungscheck
- nie fünf finale Szenen als Sammelbild erzeugen

Block-QA prüft:

- gleiche Lichtlogik
- gleiche Materialqualität
- gleiche Color-Grading-Anmutung
- O₂-Cyan stabil
- keine Stock-3D-/Toy-Drift
- keine zu leeren Hintergründe
- kein Drift in Fotorealismus

## 9. Fehlerliste und Recovery

Bei technischem oder qualitativem FAIL:

1. Bildnummer notieren
2. Status `FEHLERHAFT` oder `FEHLT`
3. Nummer nicht neu vergeben
4. regulären Durchlauf fortsetzen
5. nach allen Blöcken Recovery-Pass

Recovery wird wiederholt, bis alle Bildnummern lückenlos PASS sind.

## 10. Finale Prüfung vor ZIP

- `Bild_01.png` bis `Bild_NN.png` lückenlos
- jede Nummer genau einmal
- 16:9
- keine verworfenen Varianten
- Bild_01-Stil über die gesamte Episode klar erkennbar
- normale Szenen sinnvoll beschriftet
- alle sichtbaren Texte deutsch und korrekt
- keine zufälligen englischen Texte
- keine starken Stilbrüche
- keine offensichtlichen Anatomie-/KI-Fehler
- keine Mascot-/Presenter-Dominanz
- keine Szene wirkt wie Corporate-Stock-3D oder billiges Spielzeug-Rendering

Erst danach finale ZIP erstellen.

## Harte Abschlussregel

Flow darf niemals:

- Script ändern
- Szenen erfinden, entfernen oder zusammenlegen
- Bildnummern neu interpretieren
- aus der festgelegten 3D-Animationswelt in Realismus, Anime, Comic oder Stock-3D driften
- englische sichtbare Texte erzeugen
- fehlgeschlagene Bilder vergessen
