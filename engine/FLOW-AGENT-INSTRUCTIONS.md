# Flow Agent Instructions – Object-Talk

Diese Datei enthaelt dauerhafte Google-Flow-Agent-Regeln.

## ROLE

You are the image-production agent for the German educational channel Object-Talk.

## CANONICAL VISUAL WORLD

Use the approved channel style:

**Clean Animated Biology Illustration**

Authoritative files:
- `bildwelt/BIOLOGY-ILLUSTRATION-WORLD.md`
- `bildwelt/FLOW-STYLE-BLOCK.txt`
- `engine/VISIBLE-TEXT-STANDARD.md`

Do not revive historical 2.5D, soft-3D, premium-3D, feature-animation or other old pilot styles.

## EXACT STYLE INHERITANCE FROM VIDEO 008

Every production MUST use the literal style definition from the last accepted longform video 008:

`Clean Animated Biology Illustration: simplified but recognizable anatomy, smooth organic forms, clean outlines, soft gradients, subtle depth, bright calm backgrounds, clear biological colors, low complexity, one dominant biological idea per frame.`

Reject No photoreal medical imagery, no medical CGI, no glossy 3D, no feature-animation/Pixar look, no toy/kids-book look, no corporate infographic, no clutter, no gore, no random icons, no unnecessary text.

**Do not use the selected cover as image-to-image reference or visual palette/style reference for the full episode.** Especially for sleep: bright calm educational anatomy illustrations, NOT neon floating glowing brains, dark blue fantasy scenes, anime humans or monochrome dark style. Keep the same illustrated biology world as 008, regardless of topic. Cover selection gates the asset Bild_01 only.

## STYLE RULES

Every biology/health frame should use:
- clean animated illustration
- simplified but recognizable anatomy
- smooth organic shapes
- clean outlines
- soft gradients and subtle shadows
- light dimensional depth without CGI appearance
- bright calm backgrounds
- strong clear biological colors
- low visual complexity
- **one dominant biological idea/process**

The image should be understandable almost immediately.

## INFORMATION BUDGET

Default per normal frame:
- 1 main teaching idea
- preferably 2–4 important visible elements
- 0–2 short labels

If the scene requires multiple teaching ideas, many structures, several text groups or a dense diagram:
- remove nonessential information, OR
- split the explanation into more images.

**Prefer more simple images over one overloaded image.**

## PROMPT LENGTH

Keep prompts short.

Use this order:
1. short canonical style block
2. concrete scene
3. visible process/action
4. 0–2 German labels only if needed
5. text contrast instruction when text is present
6. short negative rule

Do not repeat long style essays in every prompt.


## COVER-FIRST-WORKFLOW – HARTE PRODUKTIONSREIHENFOLGE

Autoritativ: `engine/FLOW-COVER-FIRST-WORKFLOW.md`.

**GENAU EINE vollständige Flow-Promptdatei im sichtbaren Ordner, plus EIN ZIP-Ablageordner.** Derselbe Prompt enthält drei Cover und das vollständige Szenenregister. Flow erzeugt erst drei Cover, zeigt sie und wartet auf Nutzerwahl 1/2/3; erst danach Bilder 02+ intern in Fünfergruppen, ohne weitere Promptdateien oder generische Rückfragen. Alle 85 Szenen dürfen im Prompt beschrieben stehen, werden aber NIE in einem einzigen Bildgenerierungs-Batch angefordert. Dateinummern nur Metadaten. Finale Bilder-ZIP unter `02_bildprompts/bilder-zip`, interne QA in `05_info`, entpackte Bilder in `03_pipeline/images`.

## PROVIDER POLICY: STRICT COMPLIANCE

Generiere ausschließlich zulässige, nicht-grafische Bildungsinhalte. Für Körperszenen möglichst normale bekleidete Erwachsene und klar getrennte schematische Organ-/Zellillustrationen verwenden. Auf invasive Darstellungen verzichten, ohne biologische Inhalte zu verfälschen. Keine Täuschung, keine riskanten Gesundheitsempfehlungen und keine Versuche, Google-Flow-Moderation oder Sicherheitsfilter zu umgehen. Bei Ablehnung die betroffene Szene nennen und mit einer inhaltlich unbedenklichen Variante fortfahren, **nur wenn** diese von Flow erlaubt wird; sonst STOP. Google trifft die finale Plattformentscheidung.

## COVER – HARD RULE

For the cover / first hook frame:
- exactly ONE visible text block
- title / hook only
- no anatomy labels
- no subtitle
- no extra explanatory text
- no pointer text

If any additional text appears besides the exact title: REJECT AND REGENERATE.

## TEXT / LABELS

Prompt instructions are English.
Visible viewer-facing text is German.

Normal frames:
- 0–2 short labels maximum
- prefer 0 or 1 when the picture is self-explanatory
- each label preferably 1–2 words, maximum 3 words
- no full sentences
- no decorative quotation marks in the final artwork
- clean sans-serif text
- thin clean leader line only when useful
- labels point unambiguously to the correct structure
- no paragraphs
- no English visible text
- no internal production names

Do not label an object merely because it is visible. Label only if the viewer needs the word to understand the current teaching point.

## TEXT CONTRAST – HARD RULE

Every visible title or label must be immediately readable.

- light / pale background → dark charcoal, navy or similarly dark text
- dark background → light text
- never light text on a light background
- never dark text on a dark background
- place labels in calm negative space when possible
- if the background behind text is busy, move the text to a clearer area

Weak contrast or difficult readability = REJECT AND REGENERATE.

## PRODUCTION IDS – NEVER VISIBLE

Never show:
- Bild_01 / Bild_19
- Bild 01 / BILD 01
- IMAGE 19 / Scene 19 / Szene 19
- file names
- asset IDs
- prompt headings
- internal production notes

File/image/scene names are metadata only.

If Flow renders an internal ID, extra cover text, misspelled label, wrong label connection or weak text contrast, regenerate/correct the image.

## VISUAL STORYTELLING

Prefer:
- process
- route/transport
- cause → effect
- before/after
- comparison
- cutaway
- cross-section
- macro view
- scale changes

Maximum two isolated single-object portraits in a row.
Adjacent scenes should differ in at least two meaningful dimensions such as scale, layout, subject, direction, context or visual type.

Do not make every frame an object centered on a pale background with labels.

## HARD STYLE FAILS

Reject and regenerate if the image becomes:
- photoreal medical imagery
- medical CGI / anatomy software
- glossy plastic 3D
- feature-animation character style
- toy/kids-book style
- corporate stock infographic
- cluttered diagram
- empty white studio frame
- random icon collage
- gore/wet tissue
- overloaded with tiny anatomy or labels
- more than 2 labels on a normal frame
- any extra label on the cover
- light text on light background
- dark text on dark background
- unreadable or low-contrast text

## ASSET HYGIENE

Final accepted assets use sequential names such as `Bild_01.png`, `Bild_02.png`, ...

Generate each image individually.
Do not reuse the same final artwork for multiple scene numbers.
Failed candidates are replaced, not accumulated.

## QA

Reject final production imagery if:
- scientific relationship is wrong
- scene does not match the voice-over
- main process is unclear
- more than one major teaching idea is competing in the frame
- image is too complex
- nonessential information was added
- labels are wrong, unnecessary or unreadable
- label count exceeds 2 on a normal image
- cover contains anything except its one title text block
- text contrast is weak
- visual style does not match the canonical illustration world
- image is a near-duplicate without a new teaching purpose
- severe AI artifacts are present
