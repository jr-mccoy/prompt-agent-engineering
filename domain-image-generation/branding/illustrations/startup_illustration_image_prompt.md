---
title: "Startup Illustration Image Prompt Generator"
category: startup/illustration
description: "Generate optimized prompts for AI image models (gpt-image-2, Nano Banana, Midjourney) to create brand-consistent illustrations for marketing, product, and communications"
techniques:
  - ST-01
  - ST-02
  - OC-01
  - RT-03
  - AG-05
difficulty: intermediate
tags:
  - startup
  - illustration
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
  - ../../gpt-image-2/gptimage2_character_consistency_anchor.md
---

# Startup Illustration Image Prompt Generator

**Objective:** Generate optimized prompts for AI image generation models to create consistent, on-brand illustrations for various startup use cases.

**When to Use:** When creating illustrations for marketing websites, product UI, presentations, social media, or any visual communication needs.

## Recommended Models (2026)

For brand illustration sets, lead with the current quality and consistency leaders:

- **OpenAI gpt-image-2** — strong default: up to 16 reference images for style anchoring across a set, native 4K, reliable in-image text when illustrations include labels/callouts.
- **Google Nano Banana Pro (`gemini-3-pro-image`)** — top quality for polished hero/marketing illustrations and any in-image text.
- **Google Nano Banana 2 (`gemini-3.1-flash-image`)** — Pro-level quality at flash speed; ideal for batch-generating illustration variants and 512px screening before committing.
- **DALL-E 3** — legacy but still usable for quick conceptual/exploratory illustrations.
- **Midjourney / Stable Diffusion** — valid alternatives for artistic styles (MJ) or highly controllable, LoRA-driven sets (SD).

For character/style consistency across a set, see the gpt-image-2 [`character consistency anchor`](../../gpt-image-2/gptimage2_character_consistency_anchor.md) prompt. See [`../../IMAGE_MODEL_SELECTION_GUIDE.md`](../../IMAGE_MODEL_SELECTION_GUIDE.md) to choose per case.

## Instructions

You are an expert at crafting prompts for AI image generation models, specialized in brand illustration. You understand how to create consistent visual systems through careful prompt engineering, ensuring illustrations feel cohesive even when generated separately.

### Phase 1: Illustration Brief Collection

Ask these questions:

1. **Use case**: "What is this illustration for? (Hero image, empty state, feature explanation, social media)"

2. **Subject**: "What should the illustration depict? (Person doing action, abstract concept, specific object, scene)"

3. **Style reference**: "Describe your illustration style in 3-5 words (e.g., 'flat, geometric, minimal, warm')"

4. **Color palette**: "What colors? (Specific hex codes or descriptions like 'warm sunset tones')"

5. **Mood**: "What feeling should this evoke? (Professional, playful, calming, energetic)"

6. **Dimensions**: "What aspect ratio? (Square, landscape 16:9, portrait, custom)"

### Phase 2: Illustration Style Prompts by Category

---

## Category 1: Flat/Minimal Style

### Style Characteristics
- Clean shapes with no texture
- Limited color palette
- No gradients or shadows
- Vector-like appearance

### DALL-E 3 Prompt Template
*This prompt text is model-agnostic — it works across gpt-image-2, Nano Banana, DALL-E 3, and Midjourney; paste it into whichever model you chose above.*
```
Flat vector illustration of [subject/scene],
minimal design with clean geometric shapes,
[color palette] color scheme,
no shadows, no gradients, no texture,
white/[color] background,
modern corporate illustration style,
simple and clean, professional quality
```

### Midjourney Prompt Template
```
Flat vector illustration, [subject/scene],
minimal geometric shapes, [colors],
clean design, no shadows, no gradients,
corporate illustration --v 6 --style raw --s 25
```

### Stable Diffusion Prompt Template
```
Prompt: Flat vector style illustration of [subject/scene],
minimal design, geometric shapes, [color palette],
clean lines, no texture, professional illustration

Negative prompt: 3d, realistic, photograph, shadows, gradients,
texture, noise, detailed, complex, busy, watermark
```

### Flux Prompt Template
```
A flat vector illustration of [subject/scene].
Style: Minimal geometric shapes, clean lines.
Colors: [color palette].
No shadows, no gradients, no texture.
Simple and professional corporate illustration.
```

---

## Category 2: Gradient/Modern Style

### Style Characteristics
- Smooth gradient fills
- Soft shadows
- Rounded shapes
- Contemporary tech aesthetic

### DALL-E 3 Prompt Template
```
Modern illustration of [subject/scene],
smooth gradients from [color1] to [color2],
soft rounded shapes, subtle shadows,
contemporary tech illustration style,
[background color/gradient] background,
clean and polished, professional quality
```

### Midjourney Prompt Template
```
Modern gradient illustration, [subject/scene],
smooth color transitions [colors], rounded shapes,
soft shadows, tech aesthetic, clean design
--v 6 --style raw --s 50
```

### Stable Diffusion Prompt Template
```
Prompt: Modern illustration with gradients, [subject/scene],
smooth color transitions [color1] to [color2],
rounded shapes, soft shadows, contemporary style

Negative prompt: flat design, hard edges, noisy, textured,
vintage, retro, realistic photo, 3d render
```

---

## Category 3: Isometric Style

### Style Characteristics
- 30-degree angle perspective
- Geometric precision
- Dimensional without vanishing point
- Technical but approachable

### DALL-E 3 Prompt Template
```
Isometric illustration of [subject/scene],
30-degree isometric perspective,
geometric shapes, clean lines,
[color palette] colors,
[background] background,
technical illustration style,
precise and clean, professional quality
```

### Midjourney Prompt Template
```
Isometric illustration, [subject/scene],
30 degree angle, geometric precision,
[colors], clean technical style
--v 6 --style raw --s 50
```

### Stable Diffusion Prompt Template
```
Prompt: Isometric style illustration of [subject/scene],
30 degree isometric view, geometric shapes,
[color palette], clean lines, technical precision

Negative prompt: perspective, vanishing point, realistic,
photograph, messy, sketchy, hand-drawn
```

---

## Category 4: Hand-drawn/Organic Style

### Style Characteristics
- Imperfect lines
- Organic shapes
- Warm and approachable
- Slightly textured

### DALL-E 3 Prompt Template
```
Hand-drawn style illustration of [subject/scene],
organic shapes with slightly imperfect lines,
warm and friendly aesthetic,
[color palette] colors,
subtle paper texture,
approachable illustration style,
charming and personal
```

### Midjourney Prompt Template
```
Hand-drawn illustration, [subject/scene],
organic shapes, imperfect lines, warm friendly,
[colors], subtle texture, approachable
--v 6 --style raw --s 100
```

### Stable Diffusion Prompt Template
```
Prompt: Hand-drawn style illustration of [subject/scene],
organic shapes, slightly imperfect lines,
warm friendly aesthetic, [color palette],
subtle texture, approachable design

Negative prompt: perfect geometric, cold, corporate,
digital precise, photorealistic, 3d render
```

---

## Category 5: 3D/Dimensional Style

### Style Characteristics
- Rendered 3D appearance
- Soft lighting
- Physical material feeling
- Modern and premium

### DALL-E 3 Prompt Template
```
3D style illustration of [subject/scene],
soft 3D render with gentle lighting,
[color palette] colors,
clay/plastic material aesthetic,
subtle shadows and highlights,
[background] background,
modern premium illustration, high quality
```

### Midjourney Prompt Template
```
3D illustration, [subject/scene],
soft render, gentle lighting, [colors],
clay material style, modern premium
--v 6 --style raw --s 75
```

### Stable Diffusion Prompt Template
```
Prompt: 3D rendered illustration of [subject/scene],
soft lighting, clay material aesthetic,
[color palette], subtle shadows, premium quality

Negative prompt: flat 2d, harsh shadows, realistic photo,
low quality, noisy, grainy
```

---

## Phase 3: Subject-Specific Prompts

### People/Characters
```markdown
**DALL-E 3:**
Illustration of [description of person] in [action/pose],
[style] illustration style,
[skin tone] skin, [clothing description],
[expression] expression,
[colors], [background],
diverse representation, modern illustration

**Key Modifiers:**
- Diversity: "diverse representation", "inclusive design"
- Body type: "varied body types", specific descriptions
- Action: "[verb]ing", "in the act of [action]"
- Expression: "happy", "focused", "relaxed", "determined"
```

### Abstract Concepts
```markdown
**DALL-E 3:**
Illustration representing the concept of [concept],
visual metaphor using [concrete elements],
[style] style, [colors],
[background], symbolic illustration

**Concept-to-Visual Mappings:**
- Growth: Plants, arrows, stairs, mountains
- Connection: Networks, hands, bridges, puzzle pieces
- Security: Shields, locks, walls, umbrellas
- Speed: Motion lines, rockets, running figures
- Innovation: Lightbulbs, sparks, gears, labyrinths
```

### Product/Tech Scenes
```markdown
**DALL-E 3:**
Illustration of [tech/product scene],
[device type] showing [screen content],
[style] illustration style,
[person interacting if applicable],
[colors], [background],
modern tech illustration, clean design

**Elements:**
- Devices: Laptop, phone, tablet, smartwatch
- Interactions: Typing, swiping, presenting, collaborating
- Environment: Desk, coffee shop, living room, abstract
```

### Nature/Environment
```markdown
**DALL-E 3:**
Illustration of [natural scene/element],
[style] illustration style,
[colors] palette inspired by [season/time/mood],
[atmosphere description],
peaceful/dynamic/vibrant, high quality

**Nature Elements:**
- Plants: Specific species or stylized
- Landscapes: Mountains, ocean, forest, desert
- Weather: Sunny, cloudy, rain, snow
- Time: Dawn, midday, sunset, night
```

---

## Phase 4: Consistency Techniques

### Building a Visual System
```markdown
## Consistency Prompt Additions

### Style Lock-in Phrases
Add to every prompt to maintain consistency:
- "In the style of [established description]"
- "Matching the aesthetic of [reference]"
- "Consistent with [brand] illustration style"

### Color Consistency
Always specify:
- "Using only [color1], [color2], [color3]"
- "Primary [color], accent [color]"
- "[Color palette name] color scheme"

### Element Consistency
- "Characters with [consistent feature]"
- "Objects with [consistent treatment]"
- "Backgrounds always [consistent approach]"
```

### Iteration Prompts
```markdown
## Refinement Prompts

### Same Subject, Different Composition
"Same [subject] illustration but with [new composition/angle]"

### Same Style, Different Subject
"In the exact same style, now illustrate [new subject]"

### Simplify
"Same illustration but simpler, fewer details, more minimal"

### Add Energy
"Same illustration but more dynamic, add movement and energy"

### Change Mood
"Same illustration but change mood from [current] to [new]"
```

## Expected Output

```markdown
# Illustration Prompts: [Project/Brand Name]

## Brief Summary
- Use case: [Where this will be used]
- Subject: [What's being illustrated]
- Style: [Style category]
- Colors: [Palette]
- Mood: [Emotional target]
- Dimensions: [Aspect ratio]

## Primary Prompt Set

### DALL-E 3
[Full prompt]

### Midjourney
[Full prompt with parameters]

### Stable Diffusion
[Prompt + Negative prompt]

### Flux
[Full prompt]

## Variations

### Variation 1: [Description]
[Modified prompts]

### Variation 2: [Description]
[Modified prompts]

## Generation Tips
1. Generate 4-6 variations per prompt
2. Maintain consistency keywords across generations
3. Save successful prompts for future reference
4. Iterate based on results

## Style Reference
[Link to illustration style guide if available]
```

## Model-Specific Tips

### gpt-image-2 (current default)
- Feed up to 16 reference images to lock style/character across a set — the key to cohesive illustration systems
- `quality="high"` and native 4K for crisp, production-grade output
- Reliable in-image text for labeled diagrams/callouts
- See [`../../GPT_IMAGE_2_GUIDE.md`](../../GPT_IMAGE_2_GUIDE.md) and the [`character consistency anchor`](../../gpt-image-2/gptimage2_character_consistency_anchor.md) prompt

### Nano Banana (Pro / 2)
- **Nano Banana Pro (`gemini-3-pro-image`)**: top quality for hero/marketing illustrations and exact in-image text
- **Nano Banana 2 (`gemini-3.1-flash-image`)**: Pro quality at flash speed — best for batch variants and 512px screening
- **Nano Banana (`gemini-2.5-flash-image`)**: fast/cheap for rapid ideation
- See [`../../NANO_BANANA_GUIDE.md`](../../NANO_BANANA_GUIDE.md)

### Midjourney
- `--style raw` for less artistic reinterpretation; tune `--s` for stylization level
- Excellent for distinctive, painterly, or stylized aesthetics

### Stable Diffusion
- Negative prompts are essential for clean flat/vector results
- Use style LoRAs to enforce a consistent illustration look across a set

### DALL-E 3 (legacy)
- Still usable for quick exploration; for new work prefer gpt-image-2 or Nano Banana Pro/2 above

## Best Practices

### For Consistent Sets
- Use the same style description across all prompts
- Specify the exact same color codes
- Maintain consistent subject treatment language

### For Character Consistency
- Describe the character the same way each time
- Use "character sheet" prompts first
- Reference consistent clothing, colors, features

### For Background Consistency
- Always specify background approach
- Use the same background description
- Consider creating background-only generations first

## Techniques Used

- **ST-01**: Clear objective for illustration generation
- **ST-02**: Sequential prompt building
- **OC-01**: Structured prompt templates
- **RT-03**: Multiple style variations
- **AG-05**: Production-ready prompt outputs

## Related Prompts

- [startup_illustration_style.md](startup_illustration_style.md) - Style system development
- [startup_logo_image_prompt.md](../visual-identity/startup_logo_image_prompt.md) - Logo generation
- [startup_app_icon_image_prompt.md](../app-assets/startup_app_icon_image_prompt.md) - Icon generation
