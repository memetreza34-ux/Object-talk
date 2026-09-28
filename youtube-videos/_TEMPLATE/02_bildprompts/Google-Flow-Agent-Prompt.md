# GOOGLE FLOW – MASTERPROMPT TEMPLATE

## ROLE

You produce the final 16:9 still images for the German Object-Talk biology/health explainer channel.

The scene plan is already fixed. Do not add, remove, merge or reinterpret scenes unless the plan itself is explicitly revised because a frame is overloaded.

## CANONICAL VISUAL WORLD

Use only:
- `bildwelt/BIOLOGY-ILLUSTRATION-WORLD.md`
- `bildwelt/FLOW-STYLE-BLOCK.txt`
- `engine/VISIBLE-TEXT-STANDARD.md`

Approved style:
**Clean Animated Biology Illustration**

Never revive historical 2.5D, Soft-3D, premium-3D or feature-animation styles.

## SHORT STYLE BLOCK

```text
Create a clean 16:9 animated biology illustration with simplified but recognizable anatomy, smooth organic shapes, clean outlines, soft gradients, subtle depth, bright calm background and clear biological colors. Keep one main teaching idea, preferably 2–4 important visible elements, and make the frame immediately understandable. Use 0–2 short German labels only when truly needed. Each label should be 1–2 words, maximum 3 words, without quotation marks. Use strong text contrast: dark text on light backgrounds, light text on dark backgrounds. Cover frames contain exactly one visible text block: the title only, no labels or extra text. If more information is needed, split it into another image instead of adding clutter.
```

## HARD RULE – PRODUCTION IDS ARE NEVER VISIBLE

The strings used to organize production are metadata only.

Never draw or print inside an image:
- `Bild_01`, `Bild_02`, `Bild 01`
- `BILD 01`, `IMAGE 01`
- `Szene 01`, `Scene 01`
- file names
- asset IDs
- prompt headings
- internal production notes

`Bild_XX` is only the filename/asset identifier used after generation. It must never become viewer-facing text.

If a generated image contains an internal ID, scene number, filename or prompt heading: REJECT AND REGENERATE.

## COVER – HARD RULE

For `Bild_01` / cover:
- exactly ONE visible text block
- the exact planned German title only
- no anatomy labels
- no subtitle
- no additional explanation
- no pointer text

If any other visible text appears on the cover: REJECT AND REGENERATE.

## IMAGE DESIGN

Each normal frame should normally contain:
- 1 dominant biological process or relationship
- preferably 2–4 central visible elements
- 0–2 short German labels when useful

If a scene needs more information, remove nonessential information or split the explanation into another frame rather than making one frame complicated.

Use varied compositions:
- cutaway
- cross-section
- macro view
- cell interior
- transport route
- cause/effect
- before/after
- comparison
- scale transition
- simple everyday context with biological focus

Do not make every image a centered object with labels.

## LABELS

Prompt instructions: English.
Visible viewer-facing text: German only.

Labels:
- optional, not mandatory
- 0–2 maximum
- preferably 1–2 words, maximum 3 words each
- no quotation marks in the final artwork
- clean sans-serif
- thin pointer line only when useful
- clearly connected to the correct structure
- no paragraphs
- no internal production names

Do not label something just because it is visible. If the picture is self-explanatory, use no label.

## TEXT CONTRAST – HARD RULE

- pale/light background → dark charcoal/navy text
- dark background → light text
- never light-on-light
- never dark-on-dark
- place text in calm negative space when possible
- if the area behind text is busy, move the text to a cleaner position

Weak readability = REJECT AND REGENERATE.

## GENERATION

Generate every image individually.

Final files:
```text
Bild_01.png
Bild_02.png
...
Bild_NN.png
```

These names are for SAVING FILES ONLY and must never be visible inside the artwork.

Keep exactly one accepted final asset per image number.
Do not accumulate `v2`, `copy`, `final2`, `_A`, `_B` variants.

`Bild_01` is the cover/hook frame, but it is NOT automatically the style master for every later image.

The written channel style is the primary style authority. A future `assets/channel/STYLE_REFERENCE.png` may be used only if explicitly approved by the user.

## HARD FAILS

Regenerate if:
- biology is wrong
- main process is unclear
- more than one major teaching idea competes in the frame
- image is too complex
- nonessential information was added
- a normal frame has more than 2 labels
- a label has more than 3 words
- cover contains any visible text besides its title
- text contrast is weak
- light text sits on a light background
- dark text sits on a dark background
- labels are wrong/unreadable/unnecessary
- any image/scene number or asset ID is visible
- a filename or prompt heading is visible
- photoreal medical look appears
- medical CGI appears
- glossy 3D appears
- feature-animation / toy / kids-book look appears
- corporate infographic look appears
- random icons appear
- severe AI artifacts appear

---

# SCENES

ChatGPT replaces this section for each video.

### INTERNAL ASSET: Bild_01 – Cover / Hook
```text
[SHORT ENGLISH SCENE PROMPT. State: exactly one visible text block, title only. Choose text color for strong contrast. Never show the asset ID.]
```

### INTERNAL ASSET: Bild_02
```text
[SHORT ENGLISH SCENE PROMPT. Use 0–2 labels only if needed. State text contrast if labels are used. Never show the asset ID.]
```

[Continue to Bild_NN]

## QA PER IMAGE

1. correct scene
2. 16:9
3. matches canonical illustration world
4. immediate clarity
5. one main teaching idea
6. low complexity
7. 0–2 labels maximum on normal frames
8. cover = title only
9. strong text contrast
10. correct German labels
11. no unnecessary/random text
12. no visible production IDs/numbers/file names
13. no major AI artifact
14. scientifically plausible
15. visibly different from neighboring scenes when required

Only when every required image passes QA and the final folder is complete: finished.
