# GOOGLE FLOW – MASTERPROMPT TEMPLATE

## ROLE

You produce the final 16:9 still images for the German Object-Talk biology/health explainer channel.

The scene plan is already fixed. Do not add, remove, merge or reinterpret scenes.

## CANONICAL VISUAL WORLD

Use only:
- `bildwelt/BIOLOGY-ILLUSTRATION-WORLD.md`
- `bildwelt/FLOW-STYLE-BLOCK.txt`

Approved style:
**Clean Animated Biology Illustration**

Never revive historical 2.5D, Soft-3D, premium-3D or feature-animation styles.

## SHORT STYLE BLOCK

```text
Create a clean 16:9 animated biology illustration with simplified but recognizable anatomy, smooth organic shapes, clean outlines, soft gradients, subtle depth, bright calm background and clear biological colors. Keep the composition simple, visually attractive and immediately understandable. Use only 1–3 short German labels with clean pointer lines when labels are needed. No realistic tissue, no medical CGI, no glossy 3D, no clutter, no unnecessary text.
```

## IMAGE DESIGN

Each frame should normally contain:
- 2–5 central visible elements
- 1 dominant biological process or relationship
- 1–3 short German labels when useful

If a scene needs more information, split the explanation into another frame rather than making one frame complicated.

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

Do not make every image a centered object with three labels.

## LABELS

Prompt instructions: English.
Visible viewer-facing text: German only.

Labels:
- short
- clean sans-serif
- thin pointer line or arrow
- clearly connected to the correct structure
- no paragraphs
- no internal production names

Wrong spelling or wrong connection = regenerate/correct.

## GENERATION

Generate every image individually.

Final files:
```text
Bild_01.png
Bild_02.png
...
Bild_NN.png
```

Keep exactly one accepted final asset per image number.
Do not accumulate `v2`, `copy`, `final2`, `_A`, `_B` variants.

`Bild_01` is the cover/hook frame, but it is NOT automatically the style master for every later image.

The written channel style is the primary style authority. A future `assets/channel/STYLE_REFERENCE.png` may be used only if explicitly approved by the user.

## HARD FAILS

Regenerate if:
- biology is wrong
- main process is unclear
- image is too complex
- labels are wrong/unreadable
- photoreal medical look appears
- medical CGI appears
- glossy 3D appears
- feature-animation / toy / kids-book look appears
- corporate infographic look appears
- random icons appear
- internal asset names appear
- severe AI artifacts appear

---

# SCENES

ChatGPT replaces this section for each video.

### Bild_01 – Cover / Hook
```text
[SHORT ENGLISH SCENE PROMPT USING THE CANONICAL STYLE BLOCK]
```

### Bild_02
```text
[SHORT ENGLISH SCENE PROMPT USING THE CANONICAL STYLE BLOCK]
```

[Continue to Bild_NN]

## QA PER IMAGE

1. correct scene
2. 16:9
3. matches canonical illustration world
4. immediate clarity
5. low complexity
6. correct German labels
7. no random text
8. no major AI artifact
9. scientifically plausible
10. visibly different from neighboring scenes when required

Only when every required image passes QA and the final folder is complete: finished.
