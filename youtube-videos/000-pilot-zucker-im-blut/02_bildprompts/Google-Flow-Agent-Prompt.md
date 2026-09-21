# GOOGLE FLOW – PILOT „ZUCKER IM BLUT“ – 26-BILDER-VERSION

## AUFGABE

Erzeuge genau **26 einzelne 16:9-Standbilder** für einen kurzen deutschen faceless YouTube-Erklärfilm.

Thema:
**Was passiert mit Zucker nach einem süßen Snack?**

Dieser Pilot testet bewusst eine **hohe visuelle Dichte**. Das Format lebt davon, dass die Erklärung sichtbar mit dem Voice-over fortschreitet. 26 Bilder für ungefähr 2 Minuten sind Absicht. Trotzdem gilt: kein Füllbild und kein Bildwechsel ohne neue sichtbare Aussage.

## HARTE FORMATREGEL

- Kein Mascot-/Presenter-Kanal.
- Keine dauerhafte Apfel-, Keks-, Food- oder Cartoon-Sprecherfigur.
- Für diesen Pilot wird **keine anthropomorphe Food-Figur benötigt**.
- Ein Bild muss einen biologischen Zustand, Weg, Vergleich oder Mechanismus sichtbar erklären.
- Nicht einfach „ein Keks steht vor einem Körper“ erzeugen.
- Jede neue Szene muss sich sichtbar vom vorherigen Bild unterscheiden.
- Die Bilder sollen wie eine zusammenhängende hochwertige Erklärserie wirken.

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
- Finalnamen exakt `Bild_01.png` bis `Bild_26.png`
- keine Sammelgenerierung mehrerer finaler Bilder in einer Datei
- integrierte Vergleichskompositionen sind erlaubt, wenn sie ausdrücklich verlangt werden
- genug Rand für dezente Push-ins/Pans in Remotion
- keine eingebrannten Untertitel

## LABEL-REGEL

Nur Labels verwenden, die bei der jeweiligen Szene ausdrücklich genannt sind.

- maximal 3 kurze deutsche Labels
- keine englischen Labels
- keine zusätzlichen Begriffe
- Pointer/Zuordnung muss eindeutig sein
- falsch geschriebenes Label = Bild FEHLERHAFT
- wenn derselbe Textfehler wiederholt auftritt: saubere textfreie Version mit Platz für späteres Remotion-Overlay erzeugen und `LABEL_OVERLAY_NÖTIG` notieren

## PRODUKTIONSABLAUF – NICHT ÜBERSPRINGEN

### PHASE A – NUR BILD_01

1. Lies zuerst die gesamte Datei.
2. Erzeuge danach **ausschließlich `Bild_01`**.
3. Noch kein `Bild_02`.
4. Prüfe `Bild_01` vollständig:
   - hochwertiger faceless Explainer-Look?
   - biologische Reise klar?
   - kein Mascot-/Presenter-Fokus?
   - plausible Anatomie?
   - sauberer Fokus?
   - genug Rand für Bewegung?
5. Bei FAIL: nur `Bild_01` neu erzeugen.
6. Bei PASS: als `Bild_01.png` speichern.
7. **STOPPE danach und warte auf die Bestätigung des Nutzers.**

`Bild_01` ist danach der **Master Style Frame** der Episode.

### PHASE B – NACH BESTÄTIGUNG

Verwende `Bild_01.png` bei jeder folgenden Generation als Style-/Continuity-Referenz, soweit Flow dies technisch unterstützt.

Von `Bild_01` übernehmen:
- Rendergrad
- Animation/Realismus-Verhältnis
- Licht
- Materialien
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
- Labels

Danach in 5er-Blöcken:

```text
Block 1: Bild_02–Bild_06
Block 2: Bild_07–Bild_11
Block 3: Bild_12–Bild_16
Block 4: Bild_17–Bild_21
Block 5: Bild_22–Bild_26
```

Innerhalb jedes Blocks jedes Bild **einzeln** erzeugen und sofort prüfen.

### FEHLERLISTE + RECOVERY

Bei technischem oder qualitativem FAIL:

- exakte Bildnummer notieren
- Status `FEHLERHAFT`, `FEHLT` oder `LABEL_OVERLAY_NÖTIG`
- Nummer nicht neu vergeben
- regulären Durchlauf fortsetzen
- nach allen normalen Blöcken nur die Fehlerbilder erneut erzeugen
- weiter `Bild_01` als Style-Referenz nutzen
- Recovery wiederholen, bis alle 26 Bilder vollständig sind

---

# SZENE 01 – BILD_01

**Voice-over:** Du isst einen süßen Snack, zum Beispiel einen Keks oder ein Stück Schokolade.

**Labels:** keine

**Prompt:**
```text
Create a cinematic 16:9 master style frame for a premium faceless educational explainer. Show a realistic but stylized cookie or small piece of chocolate in the foreground near an anonymous human, while a clean semi-transparent torso reveals the small intestine and a subtle magnified blood vessel. The biological pathway should already be hinted at, but the snack is not a character and does not have a face. The human is context only. Make the biology the visual hero. Warm cinematic lighting, strong depth, clean premium 3D materials, scientifically recognizable simplified anatomy, no text, no labels, no mascot, no presenter pose, no gore. This image defines the exact render quality, color temperature, lighting, material language and overall visual world for all later images.
```

# SZENE 02 – BILD_02

**Voice-over:** Kurz danach beginnt sich zu verändern, was in deinem Blut passiert.

**Labels:** keine

```text
Using Bild_01 as the style reference, create a macro 16:9 view inside a healthy blood vessel before the main post-meal rise. Show red blood cells and only a modest baseline amount of simplified glucose particles moving in plasma. The image should feel calm and normal, not dangerous or medical-drama-like. No numbers, no charts, no labels, no warning colors, no mascot. This is a teaser that something in the blood is about to change.
```

# SZENE 03 – BILD_03

**Voice-over:** Aber wie kommt der Zucker überhaupt vom Essen bis zu deinen Zellen?

**Labels:** keine

```text
Using Bild_01 as the style reference, create one elegant macro-to-micro educational composition that visually previews the route from a sweet snack to the digestive tract, then to a blood vessel, then to a healthy body cell. The route should read naturally from left to right and feel like one cinematic 3D scene, not a dashboard. Do not imply direct absorption from the stomach. No labels, no mascot, no presenter, no UI cards.
```

# SZENE 04 – BILD_04

**Voice-over:** Im Mund wird der Snack zuerst zerkleinert und mit Speichel vermischt.

**Labels:** keine

```text
Using Bild_01 as the style reference, create a 16:9 anatomical mouth cutaway during chewing. Show a small sweet food piece being mechanically broken by the teeth and mixed with a subtle, clean layer of saliva. The visual must explain breakdown and mixing, not merely show someone eating. Simplified recognizable oral anatomy, no gross saliva, no labels, no mascot, no text.
```

# SZENE 05 – BILD_05

**Voice-over:** Beim Schlucken wandert der Nahrungsbrei durch die Speiseröhre in den Magen.

**Labels:** `Speiseröhre`

```text
Using Bild_01 as the style reference, create a 16:9 side cutaway of the throat and upper torso showing swallowed food moving through the esophagus toward the stomach. The path must be anatomically clear and directional. Add exactly one concise German label with a clean pointer: “Speiseröhre”. No other text, no mascot, no implication that gravity alone drives transport.
```

# SZENE 06 – BILD_06

**Voice-over:** Der Magen ist dabei vor allem eine Zwischenstation und nicht der wichtigste Aufnahmeort für Zucker.

**Labels:** `Magen`

```text
Using Bild_01 as the style reference, create a clean 16:9 stomach cutaway showing food material inside the stomach and the outlet continuing toward the small intestine. The stomach should read visually as a processing/transit station, not as the main place where glucose enters the bloodstream. Add only the German label “Magen”. No extra labels, no mascot, no wet or disturbing medical realism.
```

# SZENE 07 – BILD_07

**Voice-over:** Entscheidend wird es im Dünndarm.

**Labels:** `Dünndarm`

```text
Using Bild_01 as the style reference, create a 16:9 transparent torso cutaway with the small intestine clearly emphasized while the stomach and other organs remain visually secondary. Make it instantly obvious that the explanation is now moving to the small intestine. Add only the German label “Dünndarm”. No mascot, no text blocks, no clutter.
```

# SZENE 08 – BILD_08

**Voice-over:** Dort werden viele Kohlenhydrate in kleinere Zuckerbausteine zerlegt.

**Labels:** `Kohlenhydrate`

```text
Using Bild_01 as the style reference, create a 16:9 educational close view inside the small intestine showing larger carbohydrate structures being broken into visibly smaller sugar building blocks. Use a clean simplified biochemical visual language rather than a textbook formula or factory metaphor. Add only the German label “Kohlenhydrate” pointing to the larger starting structures. No mascot, no machines, no neon sci-fi.
```

# SZENE 09 – BILD_09

**Voice-over:** Einer dieser Bausteine ist Glukose.

**Labels:** `Glukose`

```text
Using Bild_01 as the style reference, create a 16:9 macro educational view of several small absorbable sugar building blocks after carbohydrate digestion, with glucose clearly highlighted as one of them. Do not imply that every carbohydrate becomes only glucose. Add exactly one German label: “Glukose”. No chemical formula required, no extra text, no mascot.
```

# SZENE 10 – BILD_10

**Voice-over:** Sie erreicht die Oberfläche der Darmwand mit ihren vielen Falten und Zotten.

**Labels:** `Darmzotten`

```text
Using Bild_01 as the style reference, create a 16:9 macro view of the inner surface of the small intestine showing folds and many intestinal villi in a clean premium 3D educational style. The image should communicate a large absorptive surface without looking fleshy or grotesque. Add only the German label “Darmzotten”. No mascot, no random cells floating outside the tissue.
```

# SZENE 11 – BILD_11

**Voice-over:** Von dort kann Glukose durch die Darmzellen in kleine Blutgefäße gelangen.

**Labels:** `Darmwand`, `Blutgefäß`

```text
Using Bild_01 as the style reference, create a 16:9 cross-section through an intestinal villus and intestinal wall. Show simplified glucose particles moving from the intestinal side across the epithelial cell layer into a small capillary. The direction intestine → through the wall → blood must be unmistakable. Add exactly two German labels with precise pointers: “Darmwand” and “Blutgefäß”. No mascot, no hole-through-wall shortcut, no gore.
```

# SZENE 12 – BILD_12

**Voice-over:** Jetzt befindet sich mehr Glukose im Blut als kurz zuvor. Genau das meint man vereinfacht, wenn man sagt: Der Blutzucker steigt.

**Labels:** keine

```text
Using Bild_01 as the style reference, create one integrated 16:9 before/after comparison of the same type of blood vessel. On the left show the earlier baseline amount of glucose particles; on the right show visibly more glucose particles after intestinal absorption. Keep red blood cells consistent. No values, no diagnosis curve, no danger colors, no labels, no mascot. The sole message is: more glucose is now present in the blood.
```

# SZENE 13 – BILD_13

**Voice-over:** Darauf reagieren Betazellen in der Bauchspeicheldrüse.

**Labels:** `Bauchspeicheldrüse`, `Betazellen`

```text
Using Bild_01 as the style reference, create a 16:9 transparent torso cutaway with the pancreas correctly located and clearly highlighted. Include a tasteful magnified inset of a pancreatic islet area with beta cells as the responsive cell group. Add exactly two German labels: “Bauchspeicheldrüse” and “Betazellen”. No anthropomorphic organ, no face, no cartoon scientist, no extra text.
```

# SZENE 14 – BILD_14

**Voice-over:** Sie geben das Hormon Insulin in den Blutkreislauf ab.

**Labels:** `Insulin`

```text
Using Bild_01 as the style reference, create a 16:9 macro educational view of pancreatic beta cells releasing insulin into a nearby small blood vessel. Make the release direction from beta cells → blood visually clear. Add exactly one German label: “Insulin” pointing to the released signal particles. No glucose-eating imagery, no mascot, no extra text.
```

# SZENE 15 – BILD_15

**Voice-over:** Insulin verteilt sich mit dem Blut im Körper.

**Labels:** `Insulin`

```text
Using Bild_01 as the style reference, create a 16:9 bloodstream macro showing insulin signal particles travelling with the circulation among red blood cells. Insulin should be visually distinct from glucose but not magical or mechanical. Add exactly one German label: “Insulin”. No transport-vehicle metaphor, no mascot, no UI arrows with text.
```

# SZENE 16 – BILD_16

**Voice-over:** Es ist kein Zuckerfresser, sondern ein Signalstoff.

**Labels:** `Insulin`

```text
Using Bild_01 as the style reference, create a 16:9 macro view of a healthy target-cell membrane beside a capillary. Show insulin interacting with a receptor at the cell surface as a signal, while glucose particles are still outside the cell. Add only the German label “Insulin”. No lock-and-key toy aesthetic, no insulin grabbing or carrying glucose, no mascot.
```

# SZENE 17 – BILD_17

**Voice-over:** An vielen Zellen hilft dieses Signal dabei, die Aufnahme von Glukose zu erhöhen.

**Labels:** `Glukose`

```text
Using Bild_01 as the style reference, create the next 16:9 step at the cell membrane: after insulin signaling, simplified glucose transporters are available at the membrane and glucose particles move from the blood side into the target cell. Add only the German label “Glukose”. Do not imply every cell in the human body requires insulin for glucose uptake. No mascot, no sci-fi portal.
```

# SZENE 18 – BILD_18

**Voice-over:** Besonders gut lässt sich das an Muskelzellen zeigen.

**Labels:** `Muskel`

```text
Using Bild_01 as the style reference, create a 16:9 transparent-body or tissue-context view that highlights healthy skeletal muscle as a concrete insulin-responsive target tissue. Show nearby capillaries feeding the muscle tissue. Add only the German label “Muskel”. No bodybuilder pose, no fitness advertisement, no mascot.
```

# SZENE 19 – BILD_19

**Voice-over:** Dort kann Glukose in die Zelle gelangen und für die Energiegewinnung genutzt werden.

**Labels:** keine

```text
Using Bild_01 as the style reference, create a 16:9 macro view inside healthy skeletal muscle tissue. Show glucose entering muscle cells and then participating in a simplified cellular energy-use scene with a subtle warm energy cue. Do not turn energy into lightning bolts or magic. No labels, no mascot, no claim that glucose becomes energy in one single step.
```

# SZENE 20 – BILD_20

**Voice-over:** Nicht jede Glukose muss sofort verbraucht werden.

**Labels:** keine

```text
Using Bild_01 as the style reference, create a 16:9 integrated two-path educational composition showing that absorbed glucose does not all have the same immediate fate: one visual path represents current cellular use, while another path remains available for storage. Make it one coherent cinematic scene rather than a dashboard. No labels, no mascot, no percentages or fixed ratios.
```

# SZENE 21 – BILD_21

**Voice-over:** Ein Teil kann in Leber und Muskeln als Glykogen gespeichert werden.

**Labels:** `Leber`, `Muskel`, `Glykogen`

```text
Using Bild_01 as the style reference, create a 16:9 integrated educational composition showing liver tissue and skeletal muscle tissue storing some glucose as compact branched glycogen structures. Add exactly three German labels: “Leber”, “Muskel”, “Glykogen”. Do not imply liver glycogen and muscle glycogen have identical physiological roles; show only the shared concept of storage. No dashboard cards, no mascot.
```

# SZENE 22 – BILD_22

**Voice-over:** So bleibt nicht die gesamte zusätzlich aufgenommene Glukose dauerhaft im Blut.

**Labels:** keine

```text
Using Bild_01 as the style reference, create a 16:9 blood-vessel macro after tissues have begun using and storing glucose. Compared with the earlier post-absorption image, visibly fewer free glucose particles remain in circulation, while red blood cells and vessel style remain consistent. No labels, no zero-glucose state, no claim that insulin removes all glucose, no mascot.
```

# SZENE 23 – BILD_23

**Voice-over:** Mit der Zeit bewegt sich der Blutzucker deshalb wieder in Richtung seines vorherigen Bereichs.

**Labels:** keine

```text
Using Bild_01 as the style reference, create a 16:9 time-progression comparison in one continuous blood-vessel composition: a higher amount of glucose after eating transitions toward an amount closer to the earlier baseline. Use no clock, no numbers, no medical thresholds and no guaranteed curve shape. No labels, no warning colors, no mascot.
```

# SZENE 24 – BILD_24

**Voice-over:** Das passiert nicht bei jeder Mahlzeit gleich schnell oder gleich stark.

**Labels:** keine

```text
Using Bild_01 as the style reference, create a 16:9 variability scene showing two different realistic meal compositions and two subtly different schematic blood-glucose response shapes. The shapes may differ in height and timing but must contain no numbers or diagnostic thresholds. Do not label one meal as good or bad. No mascot, no medical warning symbols.
```

# SZENE 25 – BILD_25

**Voice-over:** Zusammensetzung der Mahlzeit, Menge und individuelle Faktoren spielen dabei eine Rolle.

**Labels:** keine

```text
Using Bild_01 as the style reference, create a second 16:9 variability scene focused on individual factors and amount: show several anonymous stylized people with different portion sizes or meal contexts, accompanied by subtle non-numeric response shapes that differ slightly. The purpose is only to show that amount, meal composition and individual factors can influence the response. No healthy/unhealthy labels, no diabetes judgment, no mascot.
```

# SZENE 26 – BILD_26

**Voice-over:** Die ganze Kette lautet also: Snack, Verdauung, Glukose, Blut, Insulin, Zelle und Speicherung. Entscheidend ist nicht eine einzelne Station, sondern das Zusammenspiel vom Dünndarm bis zu den Körperzellen.

**Labels:** keine

```text
Using Bild_01 as the style reference, create a cinematic final 16:9 hero explainer image that unifies the complete mechanism in one readable macro-to-micro journey: sweet snack → small intestine → glucose entering blood → pancreas/beta-cell insulin response → glucose entering a target cell → some glucose stored in liver and muscle. The composition should flow naturally from left to right with depth and scale transitions, not UI cards. The biological process is the hero. No mascot, no presenter, no text, no random labels, no new process that was not explained.
```

# ABSCHLUSSPRÜFUNG

Vor der ZIP-Ausgabe:

- genau 26 akzeptierte Bilder
- lückenlos `Bild_01.png` bis `Bild_26.png`
- jede Nummer genau einmal
- 16:9
- keine Temp-/Fehlervarianten
- Bild_01-Stil über die Episode erkennbar
- keine unbeabsichtigte Mascot-/Presenter-Szene
- jedes Bild erklärt den vorgesehenen Sprachabschnitt
- Nachbarbilder unterscheiden sich sichtbar und sinnvoll
- alle deutschen Labels korrekt
- keine groben Anatomie- oder KI-Fehler

Erst danach die finale ZIP erstellen.
