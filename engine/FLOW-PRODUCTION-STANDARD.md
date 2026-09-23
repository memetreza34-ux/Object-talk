# Flow Production Standard

Diese Datei definiert die verbindliche Produktionslogik für Google Flow.

## Ziel

Flow erzeugt konsistente, hochwertige Erklärbilder für den deutschen Object-Talk-Kanal. Die Bilder erklären den gesprochenen Inhalt sichtbar und gehören immer zur selben visuellen Welt.

Die freigegebene Kanalwelt ist zusätzlich beschrieben in:

```text
bildwelt/APPROVED-VISUAL-WORLD.md
```

## 1. Verbindliche Bildwelt

Der Kanal nutzt eine **stark stilisierte hochwertige 3D-Animationsfilm-Welt** mit klar erkennbarem Premium-Familienanimations-Look.

Verbindlich:

- deutlich animiert und stilisiert, nicht fotorealistisch
- weiche gerundete Formen
- vereinfachte, aber fachlich erkennbare Anatomie und Biologie
- warme filmische Beleuchtung
- klare Tiefenwirkung und hochwertige glatte 3D-Materialien
- freundlich, modern, familiengeeignet, aber nicht babyhaft
- echte Erklärbilder vor Mascot-/Presenter-Szenen
- keine Anime-, Comic-, Live-Action- oder medizinisch-fotorealistische Bildwelt
- kein Gore, keine Horror-Anatomie, kein Plastikspielzeug-Look
- keine nassen oder fleischig-realistischen Gewebetexturen

### Freigegebene Inside-the-Body-Welt

Für Körper-, Blut-, Organ-, Gewebe- und Zellbilder ist die freigegebene Grundsprache:

- Creme, Apricot, Amber und Orange als warme Basis
- tiefes Rot/Burgunder für Blut, Gefäße und rote Blutkörperchen
- weiche goldene Highlights
- dunklere warme Randbereiche für Tiefe
- blass Cyan/Türkis als klarer Sauerstoff-Kontrast
- glatte, hochwertige, leicht weiche Materialien statt medizinischer Oberflächentexturen
- Makro-/Mikro-Bilder mit deutlicher räumlicher Tiefe

Die genaue Fachfarbe eines Objekts darf angepasst werden. Renderstil, Licht, Materialgefühl und Stilisierungsgrad bleiben konstant.

Globaler Stilanker für Prompts:

```text
premium strongly stylized 3D animated educational film look, clearly animated and non-photorealistic, soft rounded forms, simplified but recognizable biology, warm amber-orange cinematic lighting, cream and burgundy material world, polished smooth surfaces, strong depth, clean visual storytelling, pale-cyan scientific accent particles, family-friendly and modern, no anime, no comic, no medical photorealism, no wet realistic tissue, no gore
```

## 2. Prompt-Sprache und sichtbarer Text

- **Prompt-Anweisungen an Google Flow immer auf Englisch.**
- **Jeder Text, der im fertigen Bild sichtbar ist, ausschließlich auf Deutsch.**
- Kein englischer sichtbarer Text.
- Kein KI-Gibberish.
- Keine langen Textblöcke oder Untertitel im Bild.

## 3. Beschriftungsregel – wichtige Dinge immer benennen

Jedes Bild muss die wichtigsten sichtbaren Strukturen oder Prozesse knapp beschriften.

Regel:

- normalerweise 1–3 kurze deutsche Labels pro Bild
- nur die wichtigsten Dinge, nicht alles beschriften
- Labels müssen eindeutig auf das richtige Objekt zeigen
- bevorzugt helle/weiße saubere Sans-Serif-Schrift
- kurze Szenen-/Prozessüberschrift kann oben im Bild stehen
- dünne Führungslinien für Labels bevorzugen
- bei Vergleichen sind kurze deutsche Marker wie `vorher`, `danach`, `mehr`, `weniger` erlaubt
- bei Prozessbildern können kurze Begriffe wie `Aufnahme`, `Transport`, `Speicherung` sinnvoll sein
- falsches, unlesbares oder englisches Label = Bild `FEHLERHAFT`
- wenn Flow einen Begriff wiederholt falsch schreibt: Bild sauber ohne den fehlerhaften Text erzeugen und exakt denselben deutschen Begriff später in Remotion als Overlay setzen

Das Ziel ist nicht möglichst viel Text, sondern sofortige Orientierung.

## 4. Bild_01 – Cover, Hook und Master Style Frame

`Bild_01` ist bei **jedem Video oder Reel gleichzeitig**:

1. Cover-/Hook-Bild
2. erster sichtbarer Shot
3. visuelle Referenz für die Episode
4. Master Style Frame für alle weiteren Bilder

Darum wird `Bild_01` ausführlicher beschrieben als alle anderen Szenen.

`Bild_01` muss:

- das Thema auf einen Blick vermitteln
- die bestmögliche Version der gewünschten 3D-Animationswelt festlegen
- Hauptmotive, Licht, Materialien, Farbstimmung, Tiefenwirkung und Anatomie-Vereinfachung klar definieren
- die kanaltypische warme 3D-Welt sichtbar etablieren
- eine **kurze starke deutsche Hook-Zeile** enthalten, die das Thema des Videos/Reels verständlich macht
- Hook-Text meist 3–7 Wörter, maximal zwei kurze Zeilen
- keine Clickbait-Aussage enthalten, die das Video fachlich nicht einlöst
- zusätzlich nur die wirklich wichtigsten deutschen Labels tragen

Beispiele für Cover-Hooks:

- `So reist Sauerstoff durch deinen Körper`
- `Was Zucker in deinem Blut macht`
- `So arbeitet dein Dünndarm`

## 5. Phase A – zuerst nur Bild_01

1. Flow liest den kompletten Auftrag.
2. Flow erzeugt **ausschließlich `Bild_01`**.
3. Noch kein `Bild_02`.
4. Bild_01 wird geprüft auf:
   - Thema und Hook sofort verständlich
   - gewünschter stark stilisierter 3D-Animationsfilm-Look
   - warme freigegebene Kanalwelt getroffen
   - keine zu realistische Darstellung
   - plausible Anatomie
   - korrekte deutsche Schrift
   - saubere Komposition und Bewegungsrand
5. Bei FAIL wird nur Bild_01 neu erzeugt.
6. Bei PASS als `Bild_01.png` speichern.
7. Danach STOPP und auf Nutzerfreigabe warten.

## 6. Bild_01 als Vorlage für alle weiteren Bilder

Nach Freigabe muss Flow `Bild_01.png` bei jeder weiteren Generation als Style-/Continuity-Referenz verwenden, soweit technisch möglich.

Von Bild_01 übernehmen:

- Renderstil
- Grad der Stilisierung
- Licht und Farbtemperatur
- Materialgefühl
- Kontrast und Tiefenwirkung
- Formensprache
- Anatomie-Vereinfachung
- Typografie-/Label-Gefühl
- wiederkehrende visuelle Symbole

Nicht blind übernehmen:

- konkrete Pose
- Motiv
- Bildaufbau
- fachlich falsche Anatomie

Wiederkehrende Dinge müssen gleich aussehen, z. B. Sauerstoff, Glukose, Insulin, rote Blutkörperchen, Hämoglobin oder Mitochondrien.

**Harte Konsistenzregel:** Folgeframes müssen aussehen, als kämen sie aus demselben Film, demselben Renderprozess und derselben Beleuchtung. Stilabweichung = Regeneration.

## 7. Szenenprompts – kurz, aber vollständig

Nach Bild_01 sollen die einzelnen Szenenprompts **so kurz wie möglich und so genau wie nötig** sein.

Normaler Szenenprompt:

- etwa 2–5 Sätze
- konkrete Szene
- sichtbarer Prozess
- wichtigste Komposition/Perspektive
- benötigte deutsche Labels
- keine Wiederholung des kompletten globalen Stilblocks

Beispiel:

```text
Using Bild_01 as the exact style reference, create a 16:9 close-up of an alveolus beside a small capillary. Show pale-cyan oxygen particles crossing the thin barrier into the blood where red blood cells are visible. Keep the transfer direction immediately clear. Add only the German labels “Lungenbläschen”, “Sauerstoff” and “Blutgefäß”.
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

- jedes Bild innerhalb des Blocks einzeln erzeugen
- nach jedem Bild Einzel-QA
- nach jedem 5er-Block kurzer Stil-/Nummerierungscheck
- erst danach nächster Block
- niemals fünf finale Szenen als ein Sammelbild erzeugen

Block-QA prüft zusätzlich:

- warme Lichtwelt stabil
- Materialglanz/Weichheit stabil
- Rot-/Burgunder-Grundwelt stabil, sofern fachlich passend
- O₂-Cyan stabil
- gleiche Typografie-/Label-Sprache
- kein Drift in Realismus oder billigen Cartoon-Look

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
- alle wichtigen Strukturen sinnvoll beschriftet
- alle sichtbaren Texte deutsch und korrekt
- keine zufälligen englischen Texte
- keine starken Stilbrüche
- keine offensichtlichen Anatomie-/KI-Fehler
- keine unbeabsichtigte Mascot-/Presenter-Dominanz
- keine Szene wirkt plötzlich fotorealistischer als der Rest

Erst danach finale ZIP erstellen.

## Harte Abschlussregel

Flow darf niemals:

- Script ändern
- Szenen erfinden, entfernen oder zusammenlegen
- Bildnummern neu interpretieren
- aus der festgelegten 3D-Animationswelt in Realismus, Anime oder Comic driften
- englische sichtbare Texte erzeugen
- fehlgeschlagene Bilder vergessen
