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

Do not revive historical 2.5D, soft-3D, premium-3D, feature-animation or other old pilot styles.

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
- one dominant biological idea/process

The image should be understandable almost immediately.

## PROMPT LENGTH

Keep prompts short.

Use this order:
1. short canonical style block
2. concrete scene
3. visible process/action
4. 1–3 German labels
5. short negative rule

Do not repeat long style essays in every prompt.

## TEXT / LABELS

Prompt instructions are English.
Visible viewer-facing text is German.

Default:
- 1–3 short labels when useful
- clean sans-serif text
- thin clean leader lines or arrows
- labels point unambiguously to the correct structure
- no paragraphs
- no English visible text
- no internal production names

Never show:
- Bild_01 / Bild_19
- IMAGE 19 / Scene 19
- file names
- asset IDs
- prompt headings

If Flow misspells a label or connects it to the wrong structure, regenerate/correct the image.

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

Do not make every frame an object centered on a pale background with three labels.

## COMPLEXITY

Prefer:
- 2–5 central visible elements
- 1 main process
- 1–3 labels

If more information is required, split it into another frame instead of adding more tiny details.

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
- image is too complex
- labels are wrong or unreadable
- visual style does not match the canonical illustration world
- image is a near-duplicate without a new teaching purpose
- severe AI artifacts are present
