# GOOGLE FLOW AGENT – VIDEO 001

## VIDEO

**Thema:** Was passiert mit deinem Essen im Körper?

Du produzierst **genau 36 finale 16:9-Standbilder** für ein deutschsprachiges faceless YouTube-Erklärvideo über Verdauung.

Die Bilder müssen den Sprechertext sichtbar erklären. Dieses Video ist **keine Mascot-Show** und besitzt keine dauerhafte Apfel-/Food-Sprecherfigur.

---

# WICHTIGSTE REGEL

Die visuelle Priorität lautet:

```text
Verständlichkeit
→ fachlich plausible Darstellung
→ klare Blickführung
→ einheitlicher Stil
→ erst danach dekorative Elemente
```

Bevorzuge:

- anatomische Cutaways
- transparente Körperansichten
- Prozessbilder
- Organ-/Gewebe-/Zellvisualisierungen
- Makro-/Mikro-Zooms
- klare Vergleichs- und Transformationsbilder

Keine zufälligen niedlichen Food-Figuren als Presenter ergänzen.

---

# PHASE A – ZUERST AUSSCHLIESSLICH BILD_01

1. Lies diese gesamte Datei.
2. Erzeuge danach **nur `Bild_01`**.
3. Erzeuge noch kein anderes Bild.
4. Prüfe `Bild_01` vollständig.
5. Bei FAIL nur `Bild_01` neu erzeugen.
6. Erst bei PASS als `Bild_01.png` speichern.

`Bild_01` ist gleichzeitig:

- Cover-/Hook-Frame
- erster Shot
- **Master Style Frame für die komplette Episode**

---

# BILD_01 ALS VORLAGE FÜR ALLE WEITEREN BILDER

Ab `Bild_02` muss `Bild_01.png`, soweit Flow dies technisch unterstützt, bei jeder Generation als Style-/Continuity-Referenz verwendet werden.

Von `Bild_01` übernehmen:

- Rendergrad
- Verhältnis Animation/Realismus
- Lichtcharakter
- Farbtemperatur und Farbharmonie
- Materialien
- Kontrast
- Tiefenwirkung
- allgemeine Explainer-Bildsprache

Nicht übernehmen:

- konkrete Anatomie
- Motiv
- Pose
- Ort
- Labels

Jedes Bild muss seinen eigenen fachlich korrekten Inhalt zeigen, aber sichtbar aus derselben visuellen Welt stammen.

---

# PHASE B – DANACH NUR IN 5ER-BLÖCKEN

Nach `Bild_01`:

```text
Block 1: Bild_02–Bild_06
Block 2: Bild_07–Bild_11
Block 3: Bild_12–Bild_16
Block 4: Bild_17–Bild_21
Block 5: Bild_22–Bild_26
Block 6: Bild_27–Bild_31
Block 7: Bild_32–Bild_36
```

Innerhalb eines Blocks **jedes Bild trotzdem einzeln** erzeugen.

Ablauf pro Bild:

```text
Szene lesen
→ Bild_01 als Stilreferenz verwenden
→ genau EIN Bild erzeugen
→ prüfen
→ bei PASS korrekt benennen
→ bei FAIL Fehlerliste ergänzen
→ nächste Szene
```

Nach jedem Block zusätzlich prüfen, ob Licht, Renderstil, Farben und Explainer-Sprache noch zu `Bild_01` passen.

---

# PHASE C – FEHLER NICHT DEN GANZEN LAUF ABBRECHEN LASSEN

Wenn Flow bei einer Bildnummer technisch fehlschlägt, die Antwort abbricht oder ein Bild qualitativ unbrauchbar ist:

- Bildnummer exakt als `FEHLERHAFT` oder `FEHLT` notieren
- keine Ersatznummer vergeben
- mit der nächsten regulären Szene fortfahren

Beispiel:

```text
Bild_07 PASS
Bild_08 FEHLT
Bild_09 PASS

Recovery-Liste:
- Bild_08
```

---

# PHASE D – RECOVERY AM ENDE

Nach allen normalen Blöcken:

1. Recovery-Liste öffnen.
2. Nur die fehlenden/fehlerhaften Bilder erneut erzeugen.
3. Weiterhin `Bild_01` als Style-Referenz verwenden.
4. Jedes Recovery-Bild einzeln prüfen.
5. Wiederholen, bis alle 36 Bilder PASS sind.

---

# FESTE STYLE-DNA

```text
high-quality semi-realistic 3D educational explainer style, faceless YouTube explainer visual language, premium animated educational series look, consistent cinematic lighting, clean composition, scientifically recognizable but simplified anatomy and biology, strong visual clarity, process-focused explainer imagery, transparent body cutaways, cross-sections, macro-to-micro transitions, elegant German educational labels, family-friendly but not childish, clearly animated but not photorealistic, no mascot-heavy composition, no random cartoon focus, no clutter, no gore, no disturbing medical realism
```

Für alle Bilder vermeiden:

```text
do not make mascot-heavy scenes, do not add cute food presenters unless explicitly requested, do not turn the scene into a character standing next to anatomy, no random cartoon figures, no cluttered composition, no photorealistic medical photography, no live action, no surgery, no blood splatter, no horror anatomy, no wet fleshy realism, no English labels, no unreadable typography, no random text, no watermark, no brand logos
```

---

# BESCHRIFTUNGEN

Wenn `German labels` angegeben sind:

- exakt nur diese wichtigen Begriffe
- ausschließlich Deutsch
- saubere gut lesbare Sans-Serif-Schrift
- dünne klare Pointer-Linie/Pfeil
- richtige anatomische Zuordnung
- keine zusätzlichen Fantasiebegriffe

Falsche Schreibweise oder falscher Pointer = Bild FAIL → Recovery-Liste.

Wenn `German labels: none`, kein erklärender Text im Bild.

---

# TECHNISCH

Jedes finale Bild:

- 16:9 landscape
- mindestens 1920×1080 oder höher im gleichen Seitenverhältnis
- keine schwarzen Balken
- kein 9:16
- kein Quadrat
- Standbild, keine Videoausgabe
- Hauptmotiv mit sicherem Rand für späteren Zoom/Pan
- wichtige Labels nicht direkt am Rand

---

# IMAGE PROMPTS

## IMAGE 01 – COVER / HOOK / MASTER STYLE FRAME

**Final filename:** `Bild_01.png`

**Purpose:** Ein einfacher Bissen startet eine komplexe Reise durch den Körper und definiert gleichzeitig die gesamte Bildwelt.

**German labels:** none

**Prompt:**

```text
Create a powerful 16:9 cinematic master frame for a faceless educational YouTube explainer about what happens to food inside the human body. Show a bite of ordinary food entering a clean semi-transparent human upper body. Inside the body reveal a scientifically recognizable but simplified continuous digestive pathway from mouth to esophagus, stomach, small intestine and large intestine. The composition must immediately communicate that one simple bite begins a complex internal journey. Make the stomach visible but visually emphasize the long folded small intestine as an important later destination. No mascot, no presenter character, no cartoon food face. Establish the exact visual language for all later scenes: premium semi-realistic 3D educational explainer, clearly animated not photorealistic, elegant warm cinematic lighting, natural muted health-education colors, clean smooth biological materials, strong depth, uncluttered composition, readable visual hierarchy, family-friendly but not childish, no text, no labels, no gore.
```

---

## IMAGE 02 – DIE GESAMTE VERDAUUNGSREISE

**Final filename:** `Bild_02.png`

**Purpose:** Nahrung wird zerlegt, transportiert und vor allem im Dünndarm aufgenommen.

**German labels:** none

**Prompt:**

```text
Using Bild_01 as the exact style and continuity reference, create a 16:9 faceless educational explainer image showing the digestive journey through a semi-transparent human torso. Show food transforming from recognizable pieces into progressively smaller nutrient particles as it moves from mouth through esophagus and stomach into the small intestine. Show many small nutrient particles leaving the small intestine toward nearby vessels while the stomach is shown mainly mixing food. Make the contrast visually clear without text: the stomach prepares, the small intestine is the major absorption area. Same lighting, render quality, material language and color world as Bild_01. No mascot, no presenter, no labels, no gore.
```

---

## IMAGE 03 – ZÄHNE ZERKLEINERN

**Final filename:** `Bild_03.png`

**Purpose:** Mechanische Verdauung beginnt im Mund.

**German labels:** `Mund`, `Zähne`

**Prompt:**

```text
Using Bild_01 as style reference, create a clean 16:9 educational 3D cross-section of a human mouth during chewing. Show normal teeth mechanically breaking a small piece of food into smaller pieces. Keep jaw, tongue and oral cavity recognizable but simplified. Use a close explanatory camera angle that makes the crushing action obvious. Add only the German labels “Mund” and “Zähne” with precise clean pointer lines. Same premium semi-realistic explainer rendering and cinematic light as Bild_01, no gore, no extra text.
```

---

## IMAGE 04 – SPEICHEL MACHT DEN BISSEN SCHLUCKBAR

**Final filename:** `Bild_04.png`

**German labels:** `Speichel`

**Prompt:**

```text
Using Bild_01 as style reference, create a 16:9 educational close-up inside the mouth. Show chewed food being mixed with clean visible saliva and forming into one soft moist food bolus on the tongue, ready to swallow. The visual must explain lubrication and bolus formation without looking gross. Add one German label “Speichel” pointing to the saliva. Same materials, light and render world as Bild_01, no extra text.
```

---

## IMAGE 05 – STÄRKEVERDAUUNG BEGINNT

**Final filename:** `Bild_05.png`

**German labels:** `Stärke`, `Enzym`

**Prompt:**

```text
Using Bild_01 as style reference, create a 16:9 microscopic educational 3D visualization showing a long simplified starch carbohydrate chain being acted on by several enzyme molecules so the long structure begins breaking into shorter pieces. Keep it conceptual rather than pretending to show an exact molecular formula. Add only “Stärke” and “Enzym” in German with correct pointers. Same clean premium educational render language as Bild_01, no extra text.
```

---

## IMAGE 06 – SCHLUCKEN UND KEHLDECKEL

**Final filename:** `Bild_06.png`

**German labels:** `Kehldeckel`, `Luftröhre`, `Speiseröhre`

**Prompt:**

```text
Using Bild_01 as style reference, create a clean 16:9 sagittal cutaway of a human head and neck during swallowing. Show a food bolus moving into the esophagus while the epiglottis closes the entrance toward the trachea. Keep the anatomy scientifically recognizable and immediately understandable. Add exactly “Kehldeckel”, “Luftröhre” and “Speiseröhre” in German with precise pointer lines. No gore, no surgical realism, same style as Bild_01.
```

---

## IMAGE 07 – PERISTALTIK

**Final filename:** `Bild_07.png`

**German labels:** `Speiseröhre`, `Peristaltik`

**Prompt:**

```text
Using Bild_01 as style reference, create a 16:9 upper-body cutaway focused on the esophagus. Show a food bolus inside and a visible ring-like muscular contraction wave following behind it while the tube ahead is relaxed. The image must clearly explain active transport rather than simple gravity. Add exactly “Speiseröhre” and “Peristaltik”. Same premium faceless 3D explainer look as Bild_01.
```

---

## IMAGE 08 – DIE MUSKELWELLE SCHIEBT DEN BISSEN

**Final filename:** `Bild_08.png`

**German labels:** `Muskelwelle`

**Prompt:**

```text
Using Bild_01 as style reference, create a detailed 16:9 close-up cross-section of one esophagus segment. Put a food bolus in the center, show the wall contracted tightly immediately behind it and relaxed/open in front. Make the forward-pushing mechanism unmistakable. Add one German label “Muskelwelle” pointing to the contracted ring. Clean scientific presentation, same style as Bild_01.
```

---

## IMAGE 09 – EINTRITT IN DEN MAGEN

**Final filename:** `Bild_09.png`

**German labels:** `Speiseröhre`, `Magen`

**Prompt:**

```text
Using Bild_01 as style reference, create a 16:9 cutaway of the lower esophagus connecting to the stomach. Show the bolus arriving at the junction and the ring-like lower esophageal sphincter relaxed/open so food can enter the stomach. Add only “Speiseröhre” and “Magen”. Clean recognizable simplified anatomy, same light/material language as Bild_01.
```

---

## IMAGE 10 – WAS DER MAGEN MACHT

**Final filename:** `Bild_10.png`

**German labels:** `Magen`, `Magensäure`, `Enzyme`

**Prompt:**

```text
Using Bild_01 as style reference, create a clean 16:9 stomach cross-section. Show muscular stomach walls churning semi-liquid food, controlled stomach acid around it and simplified digestive enzyme particles acting on food fragments. Make mixing and chemical digestion visually clear without gross realism. Add exactly “Magen”, “Magensäure” and “Enzyme”. Same premium explainer style as Bild_01.
```

---

## IMAGE 11 – CHYMUS ZUM DÜNNDARM

**Final filename:** `Bild_11.png`

**German labels:** `Magen`, `Chymus`, `Dünndarm`

**Prompt:**

```text
Using Bild_01 as style reference, create a 16:9 cutaway showing stomach connected to the beginning of the small intestine. Show semi-liquid partially digested food inside the stomach and only a small controlled portion passing through the outlet into the small intestine. Add exactly “Magen”, “Chymus” and “Dünndarm”. Same clean semi-realistic 3D explainer world as Bild_01.
```

---

## IMAGE 12 – DER ZWÖLFFINGERDARM

**Final filename:** `Bild_12.png`

**German labels:** `Magen`, `Zwölffingerdarm`

**Prompt:**

```text
Using Bild_01 as style reference, create a strong 16:9 educational frame focusing on the stomach and the C-shaped first section of the small intestine. Show acidic chyme entering the duodenum with a subtle warm-orange cue only within the chyme. Add exactly “Magen” and “Zwölffingerdarm”. Same premium explainer rendering as Bild_01.
```

---

## IMAGE 13 – BICARBONAT

**Final filename:** `Bild_13.png`

**German labels:** `Bauchspeicheldrüse`, `Bicarbonat`

**Prompt:**

```text
Using Bild_01 as style reference, create a 16:9 3D educational view of the pancreas beside the duodenum. Show a pancreatic duct delivering a clean stream containing simplified bicarbonate particles into acidic chyme. Visually show the harsh acidic cue becoming calmer after mixing, without numerical pH values. Add exactly “Bauchspeicheldrüse” and “Bicarbonat”. Same style as Bild_01.
```

---

## IMAGE 14 – VERDAUUNGSENZYME DER BAUCHSPEICHELDRÜSE

**Final filename:** `Bild_14.png`

**German labels:** `Bauchspeicheldrüse`, `Verdauungsenzyme`

**Prompt:**

```text
Using Bild_01 as style reference, create a 16:9 3D educational scene showing the pancreas delivering digestive enzymes through its duct into the small intestine. Inside the intestine show visually distinct simplified groups representing carbohydrates, fats and proteins being processed by different enzyme particles. Add exactly “Bauchspeicheldrüse” and “Verdauungsenzyme”. No implication that one enzyme digests everything. Same style as Bild_01.
```

---

## IMAGE 15 – LEBER, GALLENBLASE UND DÜNNDARM

**Final filename:** `Bild_15.png`

**German labels:** `Leber`, `Gallenblase`, `Dünndarm`

**Prompt:**

```text
Using Bild_01 as style reference, create a clear 16:9 anatomy frame showing liver, gallbladder and nearby duodenum. Show the bile pathway from liver to gallbladder and from the gallbladder through the bile duct into the small intestine. Add exactly “Leber”, “Gallenblase” and “Dünndarm”. Keep organ positions plausible and clean, same style as Bild_01.
```

---

## IMAGE 16 – GALLE UND FETTTRÖPFCHEN

**Final filename:** `Bild_16.png`

**German labels:** `Galle`, `Fetttröpfchen`

**Prompt:**

```text
Using Bild_01 as style reference, create a 16:9 microscopic explainer inside the small intestine. Show one large dietary-fat cluster on one side, bile interacting with it in the center, and many smaller fat droplets on the other side. Make emulsification clear without implying that bile chemically digests fat. Add exactly “Galle” and “Fetttröpfchen”. Same visual world as Bild_01.
```

---

## IMAGE 17 – NÄHRSTOFFE WERDEN KLEINER

**Final filename:** `Bild_17.png`

**German labels:** `Kohlenhydrate`, `Einfachzucker`, `Proteine`, `Aminosäuren`, `Fette`

**Prompt:**

```text
Using Bild_01 as style reference, create a clean 16:9 transformation explainer with three clearly separated visual pathways: long carbohydrate structure becoming small simple-sugar particles; folded protein becoming many amino-acid units; large dietary-fat structures becoming smaller digestion products. Avoid fake chemical formulas. Add exactly the German labels “Kohlenhydrate”, “Einfachzucker”, “Proteine”, “Aminosäuren” and “Fette”. Same premium render language as Bild_01.
```

---

## IMAGE 18 – ZERLEGE- UND SORTIERPRINZIP

**Final filename:** `Bild_18.png`

**German labels:** none

**Prompt:**

```text
Using Bild_01 as style reference, create a 16:9 faceless educational analogy visualizing digestion as a breakdown-and-sorting process. Show large food structures entering a clean abstract processing pathway, passing through several simple breakdown stages and emerging as small organized nutrient building blocks that can pass through a selective barrier into transport channels. The analogy must clarify transformation and sorting without becoming a literal factory scene. No mascot, no presenter character, no text, no labels. Same cinematic materials, lighting and explanatory clarity as Bild_01.
```

---

## IMAGE 19 – DARMZOTTEN

**Final filename:** `Bild_19.png`

**German labels:** `Dünndarm`, `Darmzotten`

**Prompt:**

```text
Using Bild_01 as style reference, create a 16:9 educational cutaway transitioning from a section of small intestine into a magnified view of its inner wall. Show folds and many finger-like villi covering the surface, clearly proving the wall is not smooth. Add exactly “Dünndarm” and “Darmzotten”. Same premium clean biology style as Bild_01.
```

---

## IMAGE 20 – GROSSE OBERFLÄCHE

**Final filename:** `Bild_20.png`

**German labels:** `Darmzotten`

**Prompt:**

```text
Using Bild_01 as style reference, create a 16:9 macro view of the small-intestine surface densely covered with villi. Show many nutrient particles approaching the expanded surface so the benefit of the projections becomes visually obvious compared with a flat wall. Add one label “Darmzotten”. Same clean semi-realistic explainer style as Bild_01.
```

---

## IMAGE 21 – NÄHRSTOFFE GELANGEN INS BLUT

**Final filename:** `Bild_21.png`

**German labels:** `Darmzotte`, `Blutgefäß`

**Prompt:**

```text
Using Bild_01 as style reference, create a detailed 16:9 cross-section of one intestinal villus. Show its outer surface and a network of tiny blood capillaries inside. Show small nutrient particles crossing from the intestinal side through the surface into the blood capillary network with an unmistakable direction of movement. Add exactly “Darmzotte” and “Blutgefäß”. No faces, no gore, same style as Bild_01.
```

---

## IMAGE 22 – BLUT TRANSPORTIERT ZUR LEBER

**Final filename:** `Bild_22.png`

**German labels:** `Blut`, `Leber`

**Prompt:**

```text
Using Bild_01 as style reference, create a 16:9 body cutaway linking small intestine to liver through blood transport. Show nutrient particles entering vessels near the intestine and traveling with flowing red blood cells toward the liver. Add exactly “Blut” and “Leber”. Keep flow direction clear and the scene uncluttered, same style as Bild_01.
```

---

## IMAGE 23 – FETTE UND LYMPHE

**Final filename:** `Bild_23.png`

**German labels:** `Lymphgefäß`

**Prompt:**

```text
Using Bild_01 as style reference, create a 16:9 microscopic cross-section of an intestinal villus emphasizing its central lymphatic vessel. Show fat-derived particles entering that lymphatic vessel and visually distinguish it from nearby blood capillaries. Add exactly “Lymphgefäß”. Same premium clean educational biology style as Bild_01.
```

---

## IMAGE 24 – AUS ESSEN WERDEN BAUSTEINE

**Final filename:** `Bild_24.png`

**German labels:** none

**Prompt:**

```text
Using Bild_01 as style reference, create a cinematic 16:9 concept scene showing the transformation from food into usable body resources: food enters a simplified digestive pathway, small nutrient particles cross the intestinal barrier into circulation, then reach healthy body cells and muscle tissue. Use subtle visual cues for energy and repair without fantasy effects. No mascot, no presenter, no text. Same style as Bild_01.
```

---

## IMAGE 25 – DÜNNDARM ZUM DICKDARM

**Final filename:** `Bild_25.png`

**German labels:** `Dünndarm`, `Dickdarm`

**Prompt:**

```text
Using Bild_01 as style reference, create a 16:9 anatomy frame showing the end of the small intestine connecting into the large intestine. Show remaining contents moving into the colon and clean simplified water molecules moving from colon contents across the wall toward nearby circulation. Add exactly “Dünndarm” and “Dickdarm”. Same clean style as Bild_01.
```

---

## IMAGE 26 – DAS DARMMIKROBIOM

**Final filename:** `Bild_26.png`

**German labels:** `Darmmikrobiom`

**Prompt:**

```text
Using Bild_01 as style reference, create a fascinating 16:9 microscopic 3D educational scene representing the colon microbiome. Show varied simplified bacterial forms living near the intestinal environment with diverse shapes and sizes but no human faces or monster features. Add exactly “Darmmikrobiom”. Keep it scientifically respectful and visually clean, same render world as Bild_01.
```

---

## IMAGE 27 – BAKTERIEN UND BALLASTSTOFFE

**Final filename:** `Bild_27.png`

**German labels:** `Ballaststoffe`, `Bakterien`

**Prompt:**

```text
Using Bild_01 as style reference, create a 16:9 microscopic colon scene showing stylized bacteria processing larger plant-fiber particles that remain after human digestion. Make it clear the bacteria are processing fiber, not attacking body tissue. Add exactly “Ballaststoffe” and “Bakterien”. Same style as Bild_01.
```

---

## IMAGE 28 – STOFFWECHSELPRODUKTE

**Final filename:** `Bild_28.png`

**German labels:** `Stoffwechselprodukte`

**Prompt:**

```text
Using Bild_01 as style reference, create a 16:9 microscopic visualization near the colon wall. Show gut bacteria processing fiber and releasing small distinct metabolite particles that move toward nearby intestinal cells. Do not imply a universal health benefit or magical effect. Add exactly “Stoffwechselprodukte”. Same clean scientific style as Bild_01.
```

---

## IMAGE 29 – FERMENTATION

**Final filename:** `Bild_29.png`

**German labels:** `Fermentation`

**Prompt:**

```text
Using Bild_01 as style reference, create a 16:9 three-step microscopic process: fiber-like carbohydrate material near gut bacteria, bacterial processing, then small resulting metabolite particles moving toward colon epithelial cells. Keep chemistry conceptual and do not invent molecular formulas. Add exactly “Fermentation” over the bacterial processing step with a clear pointer. Same style as Bild_01.
```

---

## IMAGE 30 – MIKROBIOME SIND UNTERSCHIEDLICH

**Final filename:** `Bild_30.png`

**German labels:** none

**Prompt:**

```text
Using Bild_01 as style reference, create a 16:9 comparison image with two neutral simplified human silhouettes, each connected to a magnified view of their colon microbiome. Show clearly different mixtures and relative abundances of bacterial shapes without implying that one microbiome is good and the other bad. No text or labels. Same premium explainer style as Bild_01.
```

---

## IMAGE 31 – WASSERENTZUG UND ENDDARM

**Final filename:** `Bild_31.png`

**German labels:** `Dickdarm`, `Enddarm`

**Prompt:**

```text
Using Bild_01 as style reference, create a clean 16:9 cutaway of large intestine and rectum. Show intestinal content gradually becoming more solid as water is removed along the colon and remaining stool stored in the rectum in a highly simplified non-gross way. Add exactly “Dickdarm” and “Enddarm”. Same educational style as Bild_01.
```

---

## IMAGE 32 – NERVEN UND HORMONE STEUERN MIT

**Final filename:** `Bild_32.png`

**German labels:** `Nerven`, `Hormone`

**Prompt:**

```text
Using Bild_01 as style reference, create a 16:9 semi-transparent torso showing the digestive tract together with a simplified nerve network and subtle signaling particles representing hormones. Show nerves communicating with digestive organs and hormone signals traveling through circulation toward digestive targets. Add exactly “Nerven” and “Hormone”. Same style as Bild_01, no magical control effects.
```

---

## IMAGE 33 – SEHEN UND RIECHEN BEREITET VOR

**Final filename:** `Bild_33.png`

**German labels:** `Speicheldrüsen`

**Prompt:**

```text
Using Bild_01 as style reference, create a 16:9 educational scene showing a normal person noticing and smelling an appetizing meal before taking a bite. Use a clean semi-transparent side cutaway of the head to show the salivary glands becoming active and releasing a small amount of saliva. Keep the person secondary to the physiological explanation and avoid exaggerated drooling. Add exactly “Speicheldrüsen”. Same style as Bild_01.
```

---

## IMAGE 34 – RECAP MUND, SPEISERÖHRE, MAGEN

**Final filename:** `Bild_34.png`

**German labels:** `Mund`, `Speiseröhre`, `Magen`

**Prompt:**

```text
Using Bild_01 as style reference, create a 16:9 recap using one coherent human upper-body cutaway with three connected stages: food being chewed in the mouth, the bolus moving down the esophagus through a contraction wave, and the stomach mixing its contents. Add exactly “Mund”, “Speiseröhre” and “Magen”. Clear continuous visual flow, same style as Bild_01.
```

---

## IMAGE 35 – RECAP DÜNNDARM, BLUT, LYMPHE, DICKDARM

**Final filename:** `Bild_35.png`

**German labels:** `Dünndarm`, `Blut`, `Lymphe`, `Dickdarm`

**Prompt:**

```text
Using Bild_01 as style reference, create a 16:9 recap centered on the intestines. Show small intestine breaking down and absorbing nutrient particles, some entering blood, fat-derived particles entering a lymphatic route, and remaining material continuing into the large intestine where water is recovered. Keep all pathways visually connected and directionally clear. Add exactly “Dünndarm”, “Blut”, “Lymphe” and “Dickdarm”. Same style as Bild_01.
```

---

## IMAGE 36 – FINALE

**Final filename:** `Bild_36.png`

**German labels:** none

**Prompt:**

```text
Using Bild_01 as the exact style reference, create a cinematic 16:9 final educational hero frame showing the complete journey from food to usable body material. Show one bite entering the digestive system, being broken down into smaller nutrient particles, those particles entering circulation, and finally reaching healthy body cells and muscle tissue associated with energy, growth and repair. The composition should visually close the journey in one coherent arc. No mascot, no presenter character, no text, no labels. Match Bild_01 in rendering, lighting, color harmony, material language and overall faceless explainer quality.
```

---

# FINALER QUALITY CHECK

Vor der ZIP-Ausgabe prüfe jedes finale Bild:

1. richtige Bildnummer?
2. 16:9 horizontal?
3. passt exakt zum vorgesehenen Inhalt?
4. erklärt es wirklich etwas oder ist es nur Dekoration?
5. gleiche visuelle Welt wie `Bild_01`?
6. Anatomie plausibel?
7. kein unnötiger Mascot-/Presenter-Fokus?
8. deutsche Labels exakt richtig?
9. Pointer richtig zugeordnet?
10. keine zufälligen Texte?
11. keine groben KI-Artefakte?
12. genug Rand für Zoom/Pan?

Danach Recovery-Liste vollständig abarbeiten.

Erst fertig, wenn exakt `Bild_01.png` bis `Bild_36.png` lückenlos als akzeptierte Bilder vorliegen. Danach ausschließlich diese finalen Bilder als ZIP bereitstellen.
