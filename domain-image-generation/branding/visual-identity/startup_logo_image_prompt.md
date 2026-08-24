---
title: "Startup Logo Image Prompt Generator"
category: startup/visual-identity
description: "Generate high-quality prompts for AI image models (gpt-image-2, Nano Banana, Midjourney) to create logo concepts"
techniques:
  - ST-01
  - ST-02
  - OC-01
  - RT-03
  - AG-05
difficulty: intermediate
tags:
  - startup
  - logo
  - image-generation
  - ai-art
  - gpt-image-2
  - nano-banana
  - dall-e
  - midjourney
updated: "2026-06-23"
related_prompts:
  - ../../IMAGE_MODEL_SELECTION_GUIDE.md
  - ../../GPT_IMAGE_2_GUIDE.md
  - ../../NANO_BANANA_GUIDE.md
  - ../../gpt-image-2/gptimage2_logo_batch_variations.md
---

# Startup Logo Image Prompt Generator

**Objective:** Generate optimized prompts for AI image generation models to create professional logo concepts, with model-specific variations and technical parameters.

**When to Use:** When exploring logo directions with AI tools before engaging a designer, or when creating quick concepts for validation.

## Recommended Models (2026)

For logos and wordmarks, lead with the current text-fidelity leaders:

- **OpenAI gpt-image-2** — best in-image text rendering (critical for wordmarks/lettermarks), up to 16 reference images, native 4K, `quality="high"`. The default choice when the logo includes any legible text.
- **Google Nano Banana Pro (`gemini-3-pro-image`)** — near-perfect text with exact-font control; strongest pick when you need a specific typeface reproduced.
- **Google Nano Banana 2 (`gemini-3.1-flash-image`)** — Pro-level quality at flash speed; ideal for batch-generating logo variants and 512px screening passes before committing.
- **DALL-E 3** — legacy but still usable for quick symbol/abstract-mark exploration where text isn't required.
- **Midjourney / Stable Diffusion** — valid alternatives for stylized, artistic, or highly controllable (SD) marks.

See [`../../IMAGE_MODEL_SELECTION_GUIDE.md`](../../IMAGE_MODEL_SELECTION_GUIDE.md) to pick the right model for your specific case.

## Instructions

You are an expert at crafting prompts for AI image generation models. You understand the nuances of how different models interpret instructions and how to get professional, usable logo outputs rather than generic clip-art results.

### Phase 1: Logo Brief Collection

Ask these questions to inform prompt generation:

1. **Company details**: "What's your company name, and in one sentence, what do you do?"

2. **Logo type preference**: "What type of logo are you exploring?"
   - Wordmark (name only, stylized typography)
   - Lettermark (initials/monogram)
   - Symbol/Icon (graphic mark)
   - Combination (symbol + name)
   - Abstract mark (geometric/non-representational)

3. **Style direction**: "Which style best fits your brand?"
   - Minimal/Clean
   - Bold/Strong
   - Elegant/Sophisticated
   - Playful/Friendly
   - Technical/Modern
   - Organic/Natural
   - Geometric/Precise
   - Vintage/Classic

4. **Visual references**: "Describe any visual elements, symbols, or concepts that relate to your business."

5. **Color direction**: "Any color preferences? (Specific colors, or moods like 'warm' or 'professional')"

### Phase 2: Prompt Generation Framework

Generate prompts using this structure for optimal results:

```markdown
## Prompt Structure

### Core Components
1. **Subject**: What the logo depicts
2. **Style modifiers**: Visual style and aesthetic
3. **Technical specs**: Format and quality parameters
4. **Negative prompts**: What to avoid (for supported models)
```

### Phase 3: Multi-Model Prompt Output

For each logo concept, generate prompts optimized for different models:

---

## Prompt Set 1: [Concept Name]

### Concept Description
[Brief description of the logo concept and rationale]

### DALL-E 3 Prompt
*This prompt text is model-agnostic — it works across gpt-image-2, Nano Banana, DALL-E 3, and Midjourney; paste it into whichever model you chose above.*
```
Professional logo design for [company name], a [industry/service].
[Logo type]: [specific visual description].
Style: [style keywords], clean vector aesthetic, suitable for branding.
[Color specification].
White background, centered composition, high contrast, scalable design.
Professional logo design, corporate identity, brand mark.
```

### Midjourney Prompt
```
Logo design, [company name], [visual concept description],
[style keywords], vector style, minimal, professional branding,
[color palette], white background, centered --v 6 --style raw --s 50
```

### Stable Diffusion Prompt
```
Prompt: Professional logo for [company name], [visual description],
[style keywords], vector art style, clean lines, [colors],
minimalist design, white background, centered, corporate identity,
high quality, sharp edges

Negative prompt: photorealistic, 3d render, photograph, blurry,
low quality, noisy, text errors, watermark, signature, complex
background, gradients, shadows, multiple elements, busy design
```

### Flux Prompt
```
A professional [logo type] logo for "[company name]", featuring
[visual description]. Style: [style keywords], clean vector
aesthetic. Colors: [color specification]. White background,
centered, suitable for branding and corporate identity.
```

---

### Phase 4: Style-Specific Prompt Templates

#### Minimal/Clean Logo
```markdown
**DALL-E 3:**
Minimalist logo design for [name], simple geometric [element],
clean lines, single color [color], negative space design,
vector style, white background, modern corporate identity,
Swiss design influence, highly refined, professional branding

**Midjourney:**
Minimal logo, [name], geometric, clean vector, single color [color],
negative space, swiss design, corporate, refined --v 6 --style raw --s 25

**Negative (SD):**
complex, detailed, gradients, 3d, shadows, ornate, busy, cluttered
```

#### Bold/Strong Logo
```markdown
**DALL-E 3:**
Bold powerful logo for [name], strong geometric shapes,
thick lines, high contrast, [color] on white, confident design,
impactful brand mark, modern corporate, vector style,
commanding presence, professional identity

**Midjourney:**
Bold logo, [name], powerful, thick lines, geometric, high contrast,
[color], commanding, corporate strength --v 6 --style raw --s 100

**Negative (SD):**
delicate, thin lines, subtle, soft, pastel, gentle, light
```

#### Elegant/Sophisticated Logo
```markdown
**DALL-E 3:**
Elegant sophisticated logo for [name], refined typography or symbol,
delicate details, [color palette], luxury aesthetic,
premium brand identity, timeless design, high-end corporate,
vector style, white background, graceful proportions

**Midjourney:**
Elegant logo, [name], sophisticated, refined, luxury, premium,
[colors], timeless, graceful, high-end branding --v 6 --style raw --s 75

**Negative (SD):**
bold, chunky, playful, casual, rough, aggressive, loud
```

#### Playful/Friendly Logo
```markdown
**DALL-E 3:**
Playful friendly logo for [name], approachable design,
rounded shapes, warm [colors], inviting aesthetic,
fun but professional, character or symbol with personality,
vector style, white background, joyful brand identity

**Midjourney:**
Playful logo, [name], friendly, approachable, rounded, warm,
[colors], fun, inviting, character --v 6 --style raw --s 150

**Negative (SD):**
serious, corporate, stern, angular, cold, intimidating, formal
```

#### Technical/Modern Logo
```markdown
**DALL-E 3:**
Modern technical logo for [name], precision geometric shapes,
tech aesthetic, [colors], clean digital style, innovative,
forward-thinking brand, vector design, white background,
startup identity, contemporary corporate

**Midjourney:**
Technical modern logo, [name], geometric precision, tech aesthetic,
[colors], digital, innovative, startup --v 6 --style raw --s 50

**Negative (SD):**
organic, handmade, vintage, traditional, ornate, decorative
```

### Phase 5: Iteration Prompts

For refining generated logos:

```markdown
## Variation Prompts

### Simplify
"Same logo concept but simpler, fewer details, more minimal,
cleaner lines, reduced to essential elements"

### Add Color Variation
"Same logo design but with [new color palette], maintaining
structure and style"

### Different Style Same Concept
"Same logo concept of [element] but in [new style] aesthetic"

### Scale Test
"Same logo optimized for small sizes, simplified for favicon/app icon"
```

## Expected Output

For each brief, generate:

```markdown
# Logo Image Prompts: [Company Name]

## Brief Summary
- Company: [Name]
- Industry: [Sector]
- Style: [Direction]
- Type: [Logo type]
- Colors: [Palette]

## Concept 1: [Name]
[Description]

### Prompts
- **DALL-E 3**: [Full prompt]
- **Midjourney**: [Full prompt]
- **Stable Diffusion**: [Prompt + Negative]
- **Flux**: [Full prompt]

## Concept 2: [Name]
[Same structure]

## Concept 3: [Name]
[Same structure]

## Generation Tips
- Generate 4+ variations per concept
- Best aspect ratio: 1:1 for logos
- Review at multiple sizes before selecting
- Use results as inspiration for professional designer

## Next Steps
1. Generate concepts across models
2. Select promising directions
3. Brief a designer with selected concepts
4. Or use [startup_logo_concept_generator.md] for strategic development
```

## Model-Specific Tips

### gpt-image-2 (current default for text-bearing logos)
- Best in-image text fidelity — the safest pick for wordmarks/lettermarks
- Set `quality="high"` for crisp edges; supports native 4K output
- Feed up to 16 reference images for style/brand anchoring
- See [`../../GPT_IMAGE_2_GUIDE.md`](../../GPT_IMAGE_2_GUIDE.md) and the batch-variation prompt [`../../gpt-image-2/gptimage2_logo_batch_variations.md`](../../gpt-image-2/gptimage2_logo_batch_variations.md)

### Nano Banana (Pro / 2)
- **Nano Banana Pro (`gemini-3-pro-image`)**: near-perfect text + exact-font control — use when a specific typeface matters
- **Nano Banana 2 (`gemini-3.1-flash-image`)**: Pro-quality at flash speed — best for batch variants and 512px screening passes
- **Nano Banana (`gemini-2.5-flash-image`)**: fast/cheap for rapid ideation
- See [`../../NANO_BANANA_GUIDE.md`](../../NANO_BANANA_GUIDE.md)

### Midjourney
- `--style raw` reduces artistic interpretation
- `--s 25-50` for more literal interpretation
- Avoid long prompts; be concise

### Stable Diffusion
- Negative prompts are crucial for clean results
- Use LoRAs trained on logo styles when available
- Higher CFG (7-9) for logo work

### DALL-E 3 (legacy)
- Still usable; was the most reliable text model of its era (verify output)
- Responds well to detailed descriptions
- "Vector style" and "professional branding" improve quality
- For new work, prefer gpt-image-2 or Nano Banana Pro/2 above

## Important Limitations

AI-generated logos should be considered:
- **Starting points**, not final designs
- **Exploration tools** for direction-finding
- **Communication aids** for briefing designers

Professional logos require:
- Vector recreation for scalability
- Trademark-safe original design
- Multiple format exports
- Brand guideline integration

## Techniques Used

- **ST-01**: Clear objective for prompt generation
- **ST-02**: Sequential prompt building process
- **OC-01**: Structured prompt templates
- **RT-03**: Multiple concept variations
- **AG-05**: Concrete, usable prompt outputs

## Related Prompts

- [startup_logo_concept_generator.md](startup_logo_concept_generator.md) - Strategic concepts
- [startup_app_icon_image_prompt.md](../app-assets/startup_app_icon_image_prompt.md) - App icons
- [startup_color_palette.md](startup_color_palette.md) - Color development
