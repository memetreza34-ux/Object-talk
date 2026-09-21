# GOOGLE FLOW – PILOT „ZUCKER IM BLUT“

## AUFGABE

Erzeuge genau **15 einzelne 16:9-Standbilder** für einen kurzen deutschen faceless YouTube-Erklärfilm.

Thema:
**Was passiert mit Zucker nach einem süßen Snack?**

Dieses Video ist ein Test der neuen Object-Talk-Bildwelt. Der Kanal ist **kein Mascot-/Presenter-Kanal**.

### Harte Regel

- Keine dauerhafte Apfel-, Keks-, Food- oder sonstige Cartoon-Sprecherfigur.
- Kein Bild darf nur aus „eine süße Figur steht irgendwo“ bestehen.
- In diesem Pilot braucht **keine einzige Szene eine anthropomorphe Food-Figur**.
- Die Bilder müssen den biologischen Prozess selbst erklären.

## VISUELLE DNA

Für ALLE Bilder gilt:

```text
high-quality semi-realistic 3D educational explainer style, faceless YouTube explainer visual language, premium animated educational series look, approximately 65–70 percent stylized animation and 30–35 percent believable realism, scientifically recognizable but simplified human anatomy and biology, warm cinematic lighting, clean composition, strong depth, believable materials, soft rounded forms, modern educational visual storytelling, family-friendly but not childish, clear process visualization, transparent body cutaways, organ cross-sections, macro-to-micro biology views, no gore, no disturbing medical realism, not photorealistic, not flat vector, not anime
```

Vermeide:

```text
mascot-heavy composition, random cute food character, presenter standing next to anatomy, plastic toy look, photorealistic surgery, gore, blood splatter, wet fleshy medical realism, horror anatomy, random laboratory props, cyberpunk, excessive neon, flat infographic dashboard, clutter, random English text, gibberish labels, unnecessary UI panels, deformed anatomy, duplicated organs, extra limbs, malformed hands, watermarks, logos
```

## TECHNIK

- 16:9 landscape
- mindestens 1920×1080
- jedes Bild einzeln
- Finalnamen exakt `Bild_01.png` bis `Bild_15.png`
- keine Collage mehrerer finaler Szenen in einer Datei, außer wenn eine Szene ausdrücklich eine integrierte Vergleichs-/Mehrschritt-Komposition verlangt
- genügend Rand für sanfte Push-ins/Pans in Remotion
- keine eingebrannten Untertitel

## LABEL-REGEL

Nur Labels verwenden, die bei der jeweiligen Szene ausdrücklich genannt sind.

- maximal 3 kurze deutsche Labels
- keine englischen Labels
- keine zusätzlichen Begriffe erfinden
- Pointer/Zuordnung muss korrekt sein
- bei falsch geschriebenem Text: Bild als FEHLERHAFT markieren und neu erzeugen
- wenn derselbe Textfehler wiederholt auftritt: eine saubere textfreie Version mit genügend Platz für späteres Remotion-Overlay erzeugen und die Bildnummer als `LABEL_OVERLAY_NÖTIG` notieren

## PRODUKTIONSABLAUF – NICHT ÜBERSPRINGEN

### PHASE A – NUR BILD_01

1. Lies zuerst die gesamte Datei.
2. Erzeuge danach **ausschließlich `Bild_01`**.
3. Erzeuge noch kein `Bild_02`.
4. Prüfe Bild_01:
   - erklärt es sofort Snack → Körper → Blut/Zelle?
   - hochwertige semi-realistische 3D-Erklärwelt?
   - keine Mascot-/Presenter-Dominanz?
   - plausible Anatomie?
   - klarer Fokus statt Bildchaos?
   - genügend Rand für Kamerabewegung?
5. Bei FAIL: nur `Bild_01` neu erzeugen.
6. Bei PASS: als `Bild_01.png` speichern.
7. **STOPPE danach und warte auf die Bestätigung des Nutzers.**

`Bild_01` ist danach der **Master Style Frame** der ganzen Episode.

### PHASE B – NACH BESTÄTIGUNG

Verwende `Bild_01.png` bei jeder folgenden Generation als Style-/Continuity-Referenz, soweit Flow dies technisch unterstützt.

Übernehmen von Bild_01:
- Rendergrad
- Verhältnis Animation/Realismus
- Licht
- Materialgefühl
- Farbtemperatur
- Kontrast
- Tiefenwirkung
- allgemeine Erklärbild-Sprache

Nicht blind übernehmen:
- konkrete Anatomie
- Motiv
- Pose
- Bildaufbau
- Organe

Danach in Blöcken arbeiten:

```text
Block 1: Bild_02–Bild_06
Block 2: Bild_07–Bild_11
Block 3: Bild_12–Bild_15
```

Innerhalb jedes Blocks jedes Bild **einzeln** erzeugen und prüfen.

### FEHLERLISTE + RECOVERY

Wenn eine Generation fehlschlägt oder sichtbar schlecht ist:

- exakte Bildnummer notieren
- Status `FEHLERHAFT`, `FEHLT` oder `LABEL_OVERLAY_NÖTIG`
- nicht die ganze Produktion stoppen
- mit der nächsten regulären Nummer fortfahren

Nach allen normalen Blöcken:
- nur fehlende/fehlerhafte Nummern erneut erzeugen
- weiter Bild_01 als Style-Referenz verwenden
- Recovery wiederholen, bis alle 15 Bilder vollständig sind

Am Ende nur akzeptierte Bilder in die finale ZIP.

---

# SZENE 01 – BILD_01 – MASTER STYLE FRAME / HOOK

**Voice-over-Idee:** Süßer Snack → was passiert danach im Blut?

**Labels:** keine

**Prompt:**

```text
Create a powerful cinematic 16:9 educational hero frame for a faceless YouTube explainer about what happens to sugar after eating a sweet snack. Show an anonymous stylized human in three-quarter profile holding a simple cookie or small piece of chocolate near the mouth. The torso is partially transparent in a clean educational cutaway: the small intestine is clearly visible and visually connected to a magnified nearby blood vessel containing a few simplified glucose particles, which then visually connect toward a healthy body cell. The composition should communicate one journey: sweet snack → intestine → bloodstream → cell. Do not show a mascot, talking food, cartoon face, speech bubble, presenter or random character. The human is only context; the biological pathway is the main subject. Clean premium semi-realistic 3D educational animation, warm cinematic light, strong depth, scientifically recognizable simplified anatomy, family-friendly, no gore, no labels, no text, no UI dashboard. This image defines the exact lighting, materials, rendering quality, contrast and overall visual world for every later image.
```

**QA:** Muss wie der Start eines hochwertigen Erklärvideos wirken, nicht wie eine Kinderfigur vor einem Hintergrund.

---

# SZENE 02 – BILD_02 – MUND / SPEICHEL

**Labels:** keine

```text
Using Bild_01 as the style reference, create a 16:9 macro educational cutaway of the human mouth during chewing. Show a small piece of sweet food being mechanically broken into smaller pieces by the teeth and visibly mixed with a clean, subtle layer of saliva. The image should clearly explain physical breakdown and mixing, not just show a person eating. Use a clean anatomical cross-section with simplified but recognizable teeth, tongue and oral cavity. No mascot, no face on the food, no exaggerated gross saliva, no text, no gore. Same rendering quality, lighting language and material realism as Bild_01.
```

---

# SZENE 03 – BILD_03 – SPEISERÖHRE → MAGEN → DÜNNDARM

**Labels:** `Speiseröhre`, `Magen`, `Dünndarm`

```text
Using Bild_01 as the style reference, create a clean 16:9 transparent torso cutaway that visually traces one continuous digestive path from esophagus to stomach and then into the small intestine. A small food bolus should be visible at different points along the route in a single integrated educational composition, without making the stomach look like the final destination. The small intestine should be clearly emphasized as the next major stage. Add only three concise German labels with precise pointer lines: “Speiseröhre”, “Magen”, “Dünndarm”. No other text. No mascot, no presenter, no gore, no wet medical realism.
```

---

# SZENE 04 – BILD_04 – KOHLENHYDRATE → GLUKOSE

**Label:** `Glukose`

```text
Using Bild_01 as the style reference, create a 16:9 close educational view inside the small intestine showing a simplified biological transformation: larger carbohydrate structures are being broken into much smaller sugar building blocks. Make clear that glucose is one of the resulting absorbable simple sugars without implying that every carbohydrate becomes only glucose. Use a scientifically simplified educational molecular representation, not a chemistry textbook diagram. Show one group of the small resulting particles labeled clearly in German: “Glukose”. No extra labels, no mascot, no factory imagery, no random machines, no neon sci-fi look.
```

---

# SZENE 05 – BILD_05 – DURCH DIE DARMWAND INS BLUT

**Labels:** `Darmwand`, `Blutgefäß`

```text
Using Bild_01 as the style reference, create a 16:9 macro cutaway of a small-intestinal villus and intestinal wall. Show simplified glucose particles moving from the intestinal lumen across the epithelial barrier into a small capillary blood vessel. The direction must be visually unmistakable: intestine → through the wall → blood. Add exactly two concise German labels with accurate pointer lines: “Darmwand” and “Blutgefäß”. No extra text. Keep the tissue clean and stylized, not fleshy or gross. No mascot, no person standing next to the anatomy.
```

---

# SZENE 06 – BILD_06 – BLUTZUCKER STEIGT

**Labels:** keine

```text
Using Bild_01 as the style reference, create a clear 16:9 educational comparison within one continuous blood-vessel composition. On the left, show a baseline amount of simplified glucose particles moving with red blood cells. On the right, after intestinal absorption, show visibly more glucose particles in the same type of vessel. The viewer should understand “more glucose is now in the blood” without numbers, medical thresholds, charts or diagnosis graphics. Keep the comparison elegant and cinematic, not a dashboard. No labels, no mascot, no warning colors.
```

---

# SZENE 07 – BILD_07 – BAUCHSPEICHELDRÜSE / INSULIN

**Labels:** `Bauchspeicheldrüse`, `Insulin`

```text
Using Bild_01 as the style reference, create a 16:9 educational torso cutaway with the pancreas clearly highlighted in its correct anatomical region. Include a tasteful magnified inset showing a simplified pancreatic islet / beta-cell area releasing insulin signal particles toward a nearby blood vessel. The visual message is: beta cells in the pancreas release insulin into the blood when glucose availability rises. Add exactly two German labels: “Bauchspeicheldrüse” pointing to the pancreas and “Insulin” pointing to the released signal particles. No face on the organ, no anthropomorphic pancreas, no cartoon scientist, no extra text.
```

---

# SZENE 08 – BILD_08 – INSULIN IST EIN SIGNAL

**Labels:** `Insulin`, `Glukose`

```text
Using Bild_01 as the style reference, create a 16:9 macro educational view of a body cell beside a small blood vessel. Show insulin as a signal interacting with the cell surface, while glucose particles can then move from the blood side into the cell through a simplified membrane transport pathway. The image must communicate that insulin is a signal, not a creature or particle that physically eats, grabs or carries glucose. Add only two German labels: “Insulin” for the signal and “Glukose” for the sugar particles. No lock-and-key toy metaphor, no mascot, no sci-fi control panel, no extra labels.
```

---

# SZENE 09 – BILD_09 – MUSKELZELLE / ENERGIE

**Labels:** keine

```text
Using Bild_01 as the style reference, create a 16:9 close educational view of healthy skeletal muscle fibers and muscle cells receiving glucose from a nearby capillary. Show the glucose entering the tissue and being used in a simplified way to support cellular energy production, represented by a subtle warm energy glow inside the muscle cells. Do not turn energy into cartoon lightning or magical sparks. No labels, no mascot, no bodybuilder cliché, no medical gore.
```

---

# SZENE 10 – BILD_10 – SPEICHERUNG ALS GLYKOGEN

**Labels:** `Leber`, `Muskel`, `Glykogen`

```text
Using Bild_01 as the style reference, create a clean integrated 16:9 two-part educational composition showing liver tissue on one side and skeletal muscle tissue on the other. Show some glucose particles being converted into compact branched storage clusters representing glycogen inside both tissues. Do not imply that liver glycogen and muscle glycogen have identical physiological roles; this image only explains storage. Add exactly three German labels: “Leber”, “Muskel”, “Glykogen”. The composition must feel like one cinematic explainer image, not a dashboard or card layout. No mascot.
```

---

# SZENE 11 – BILD_11 – WIEDER RICHTUNG AUSGANGSBEREICH

**Labels:** keine

```text
Using Bild_01 as the style reference, create a 16:9 time-progression comparison of the same type of blood vessel. At the beginning of the visual flow, show many glucose particles after absorption. Later in the same left-to-right composition, show fewer circulating glucose particles as tissues take up and store glucose. Do not show a fixed time, a medical target value, a diagnosis curve or a guaranteed exact trajectory. The message is simply movement back toward the earlier range. No labels, no warning colors, no mascot.
```

---

# SZENE 12 – BILD_12 – RECAP 1: SNACK → DARM → BLUT

**Labels:** keine

```text
Using Bild_01 as the style reference, create a clean 16:9 integrated recap image with three visually connected stages, not separate UI cards: a small sweet snack being eaten, a simplified small-intestine cutaway where carbohydrates become small sugar particles, and glucose entering a blood vessel. Use natural directional composition from left to right. No text, no mascot, no arrows with words, no unrelated organs. This must summarize only the first half of the mechanism already explained.
```

---

# SZENE 13 – BILD_13 – RECAP 2: INSULIN → ZELLE / SPEICHER

**Labels:** keine

```text
Using Bild_01 as the style reference, create a 16:9 integrated recap of the second half of the mechanism: pancreas releases insulin signal into blood, insulin signaling supports glucose movement into a body cell, and some glucose is represented as stored in liver or muscle tissue. Keep the three stages visually connected in one premium biological explainer composition. No new process beyond what was already explained. No labels, no mascot, no person presenting the diagram.
```

---

# SZENE 14 – BILD_14 – REAKTION IST NICHT IMMER IDENTISCH

**Labels:** keine

```text
Using Bild_01 as the style reference, create a 16:9 educational variability scene. Show two different realistic meal compositions on the left and two anonymous stylized human silhouettes on the right, with subtle schematic blood-glucose response shapes behind them that differ in height and timing but contain no numbers and no medical thresholds. The purpose is only to show that meal composition and individual factors can change how fast and how strongly blood glucose responds. Do not mark one person or meal as good, bad, healthy, unhealthy or diabetic. No labels, no red warning symbols, no mascot.
```

---

# SZENE 15 – BILD_15 – FINALE GESAMTREISE

**Labels:** keine

```text
Using Bild_01 as the style reference, create a cinematic final 16:9 hero explainer image that summarizes the complete journey in one elegant macro-to-micro composition: sweet food → small intestine → glucose entering blood → insulin signaling → glucose reaching a healthy body cell. Make the route visually readable from left to right with depth and scale transitions, without turning it into a flat infographic. The biological process is the hero. No mascot, no talking food, no presenter, no text, no random labels, no extra organs. Same premium semi-realistic 3D visual world as Bild_01.
```

---

# ABSCHLUSSPRÜFUNG

Vor ZIP-Ausgabe prüfen:

- genau 15 akzeptierte Bilder
- `Bild_01.png` bis `Bild_15.png`
- keine Lücken
- keine Duplikate
- alle 16:9
- Bild_01 als klarer Style-Anchor erkennbar
- keine unbeabsichtigte Mascot-/Presenter-Szene
- jede Szene erklärt den vorgesehenen biologischen Schritt
- keine falschen deutschen Labels
- keine schweren Anatomie- oder KI-Artefakte

Erst dann finale ZIP erstellen.
