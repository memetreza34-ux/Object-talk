# Flow Production Standard

Diese Datei definiert die verbindliche Produktionslogik für Google Flow.

## Ziel

Flow erzeugt konsistente, hochwertige Erklärbilder für den deutschen Object-Talk-Kanal. Die Bilder erklären den gesprochenen Inhalt sichtbar und gehören immer zur selben visuellen Welt.

Die freigegebene Kanalwelt ist zusätzlich beschrieben in:

```text
bildwelt/APPROVED-VISUAL-WORLD.md
```

## 1. Verbindliche Bildwelt

Der Kanal nutzt eine **stark stilisierte Premium-3D-Animationsfilm-Welt**.

### Stilgewichtung

- 85–90 % Animation/Stilisierung
- 10–15 % Realismus nur zur fachlichen Erkennbarkeit

Verbindlich:

- eindeutig animierter Feature-Film-Look
- nicht fotorealistisch
- weiche, gerundete, skulptierte Formen
- vereinfachte, aber erkennbare Anatomie
- glatte Premium-Materialien
- keine realistische Haut oder Poren
- keine nassen, faserigen oder fleischigen Gewebetexturen
- klare Farbfelder statt medizinischer Mikrotextur
- filmische Lichtführung mit Rim-Light und atmosphärischer Tiefe
- starke räumliche Staffelung
- bewusstes Production Design
- modernes hochwertiges Color Grading
- nicht babyhaft, nicht spielzeughaft, nicht Corporate-Stock-3D
- echte Erklärbilder vor Mascot-/Presenter-Szenen

### Inside-the-Body-Welt

Körper-, Blut-, Organ-, Gewebe- und Zellbilder müssen **zuerst wie Animation und erst danach wie Anatomie** aussehen.

Bevorzugt:

- Coral, Apricot, Amber, Rot/Burgunder
- tiefe Navy-/Pflaumen-/Anthrazit-Hintergründe
- blass Cyan/Türkis für O₂
- neutral-violett/grau für CO₂
- glatte, weich modellierte Oberflächen
- klare, große Formen
- saubere animierte Tunnel-/Cutaway-Welten

Verboten:

- realistisch transparenter menschlicher Torso
- realistische Haut, Adern oder Organgewebe
- medizinische CGI-Software-Optik
- Fleisch-/Geweberealismus
- matschige Braunwelt

Globaler Stilanker für Prompts:

```text
premium highly stylized 3D feature-animation educational film, 85-90 percent stylized and only minimally realistic for recognizability, clearly animated and non-photorealistic, soft rounded sculpted forms, smooth clean materials, simplified anatomy, bold readable shapes, controlled cinematic lighting, soft rim light, atmospheric depth, sophisticated color grading, warm coral-apricot-burgundy palette with deep navy or plum contrast, pale-cyan oxygen accents, designed animated world, no realistic skin, no realistic tissue, no medical CGI, no wet flesh texture, no corporate stock 3D, no toy look, no anime, no comic, no gore
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
3. visuelle Referenz der Episode
4. Master Style Frame für alle weiteren Bilder

Bild_01 muss die **beste visuelle Qualität der Episode** zeigen.

Pflicht:

- Thema sofort verständlich
- deutlich animierter Film-Look
- kein realistischer Mensch
- Hauptmotiv groß und präsent
- bevorzugt faceless/stilisierte Figur oder stilisierter Torso/Cutaway
- keine realistisch transparente Haut
- filmischer Hintergrund mit Tiefe
- klare Lichtführung
- Hook maximal zwei kurze Zeilen
- Hook niemals über Hauptmotiv
- standardmäßig keine kleinen Labels auf dem Cover
- auch ohne Text starkes Key Visual

Harte FAIL-Kriterien:

- medizinischer CGI-Look
- realistischer menschlicher Torso
- realistische Haut oder Gewebetextur
- Corporate-3D-Stock-Look
- billiger Toy-Look
- blasser Beige-Hintergrund
- Figur zu klein
- Schulbuch-/PowerPoint-Wirkung
- Titel kollidiert mit Motiv
- flache Beleuchtung

## 5. EINZIGER FREIGABEPUNKT: Bild_01

1. Flow liest den kompletten Auftrag.
2. Flow erzeugt ausschließlich `Bild_01`.
3. Noch kein `Bild_02`.
4. Bild_01 intern prüfen.
5. Bei FAIL Bild_01 selbstständig neu erzeugen.
6. Bei PASS als `Bild_01.png` speichern.
7. **Genau hier einmal den Nutzer um Freigabe bitten.**

Wichtig:

> Nach der Freigabe von `Bild_01` darf Flow den Nutzer **nicht mehr fragen**, ob es mit dem nächsten Block weitermachen soll.

Die Bild_01-Freigabe ist die einzige normale Rückfrage im gesamten Bilderlauf.

## 6. Nach Bild_01: vollautomatisch bis zum Ende

Sobald der Nutzer Bild_01 freigibt:

- ohne weitere Rückfragen fortfahren
- Bild_02 bis Bild_NN vollständig erzeugen
- jedes Bild einzeln generieren
- Bild_01 bei jeder Generation als Style-/Continuity-Referenz verwenden
- 5er-Blöcke nur als **interne QA-Struktur** verwenden
- nach einem Block NICHT stoppen
- nicht fragen: „Soll ich weitermachen?“
- nicht auf Freigaben zwischen Blöcken warten

Nur bei einem echten technischen Blocker, der nach mehreren automatischen Versuchen nicht lösbar ist, darf Flow stoppen und berichten.

## 7. Bild_01 als Vorlage für alle weiteren Bilder

Von Bild_01 übernehmen:

- Renderstil
- Stilisierungsgrad
- Lichtlogik
- Color Grading
- Materialqualität
- Formensprache
- Anatomie-Vereinfachung
- wiederkehrende Symbole

Folgeframes müssen aussehen, als kämen sie aus demselben Animationsfilm und Renderprozess.

Stilabweichung = automatische Regeneration.

## 8. Szenenprompts – kurz, aber vollständig

Nach Bild_01:

- etwa 2–5 Sätze
- konkrete Szene
- sichtbarer Prozess
- wichtigste Perspektive
- deutsche Labels
- nicht den kompletten Stilblock wiederholen

Jeder Folgeprompt beginnt sinngemäß mit:

```text
Using Bild_01 as the exact style reference, keep the same highly stylized premium 3D feature-animation world, the same smooth materials, color grading, lighting logic and anatomy simplification. Keep it clearly animated, never medical-realistic.
```

## 9. Produktion in 5er-Blöcken – nur intern

Nach Freigabe von Bild_01:

```text
Block 1: Bild_02–Bild_06
Block 2: Bild_07–Bild_11
Block 3: Bild_12–Bild_16
Block 4: Bild_17–Bild_21
Block 5: Bild_22–Bild_26
Block 6: Bild_27–...
```

Wichtig:

- jedes Bild einzeln generieren
- nach jedem Bild Einzel-QA
- nach jedem Block Stil-/Nummerierungscheck
- **danach automatisch sofort mit dem nächsten Block fortfahren**
- niemals fünf finale Szenen als Sammelbild erzeugen

Block-QA prüft:

- deutlich animierte Welt
- gleiche Lichtlogik
- gleiche Materialqualität
- gleiche Farbdramaturgie
- O₂-Cyan stabil
- keine Medical-CGI-/Stock-3D-/Toy-Drift
- keine realistische Haut/Gewebetextur
- keine zu leeren Hintergründe

## 10. Fehlerliste und Recovery

Bei technischem oder qualitativem FAIL:

1. Bildnummer notieren
2. Status `FEHLERHAFT` oder `FEHLT`
3. Nummer nicht neu vergeben
4. regulären Durchlauf fortsetzen
5. nach allen Blöcken Recovery-Pass
6. fehlerhafte Szene automatisch neu erzeugen
7. bis zu 3 automatische Versuche pro fehlender/fehlerhafter Szene

Erst wenn ein technischer Blocker auch danach nicht lösbar ist, darf Flow den Nutzer informieren.

## 11. Verbindliche Endausgabe

Am Ende muss Flow **einen fertigen Bilderordner** erstellen:

```text
<video-id>_bilder/
```

Darin ausschließlich die final akzeptierten Dateien:

```text
Bild_01.png
Bild_02.png
...
Bild_NN.png
```

Regeln:

- korrekte zweistellige Nummerierung
- keine Lücken
- keine doppelten Nummern
- keine Varianten wie `final2`, `neu`, `copy`, `v3`
- keine verworfenen Bilder im finalen Ordner
- Dateiformat PNG
- 16:9

Zusätzlich eine ZIP-Datei erstellen:

```text
<video-id>_bilder.zip
```

Die ZIP enthält exakt denselben finalen Bilderordner.

## 12. Finale Prüfung

Vor Abschluss:

- alle Bilder lückenlos vorhanden
- jede Nummer genau einmal
- Animationsfilm-Look durchgehend stabil
- keine medizinisch-realistische Szene
- keine realistische Haut/Gewebetextur
- normale Szenen sinnvoll beschriftet
- alle sichtbaren Texte deutsch und korrekt
- keine offensichtlichen Anatomie-/KI-Fehler
- keine Mascot-/Presenter-Dominanz
- finaler Ordner und ZIP vorhanden

Danach erst meldet Flow: **fertig**.

## Harte Abschlussregel

Flow darf niemals:

- Script ändern
- Szenen erfinden, entfernen oder zusammenlegen
- Bildnummern neu interpretieren
- nach Bild_01 weitere normale Freigaben verlangen
- nach jedem 5er-Block fragen, ob es weitermachen soll
- aus der Animationswelt in Realismus, medizinische CGI, Anime, Comic oder Stock-3D driften
- englische sichtbare Texte erzeugen
- fehlgeschlagene Bilder vergessen
