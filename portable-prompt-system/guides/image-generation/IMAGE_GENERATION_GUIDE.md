# Image Generation Prompt Guide

**Purpose:** Authoritative guide for creating image generation prompts that actually produce usable results. Based on empirical testing of what works vs. what fails with AI image models.

**Key Insight:** Image models follow explicit geometry and enumerated layout rules better than abstract style preferences. Treat prompts as contracts with testable constraints, not suggestions.

---

## The 8 Core Techniques

### 1. Terminology Steering

**Problem:** Calling something a "card" triggers UI card tropes (rounded corners, shadows, gradients, floating panels).

**Solution:** Reframe artifacts using print/production terminology:

| Avoid (Triggers UI behaviors) | Use Instead (Triggers print behaviors) |
|-------------------------------|----------------------------------------|
| card | flat print artwork |
| badge | ink-on-paper layout |
| reference card | PDF export style |
| mockup | edge-to-edge print surface |
| design | literal printed content |

**Example:**
```
BAD: "Create a reference card for..."
GOOD: "Create FLAT PRINT ARTWORK representing the literal ink-on-paper content that will be sent directly to a printer."
```

---

### 2. Grid Forcing + Enumerated Slots

**Problem:** Vague layout instructions like "organize into sections" let models improvise poorly.

**Solution:** Specify exact grid geometry AND assign content to numbered slots.

**Grid Specification:**
```
GRID LAYOUT (MOST IMPORTANT):
- EXACTLY 2 ROWS x 3 COLUMNS
- TOTAL OF 6 BOXES PER CARD
- ALL BOXES MUST BE:
  - Equal width
  - Equal height
  - Evenly spaced
  - Perfectly aligned
- One item per box
- No box may span multiple rows or columns
- No empty boxes
- No combined items
- Boxes read left-to-right, top-to-bottom
```

**Slot Enumeration:**
```
BOX 1: [Content A]
BOX 2: [Content B]
BOX 3: [Content C]
BOX 4: [Content D]
BOX 5: [Content E]
BOX 6: [Content F]
```

This prevents merging content, duplicating items, rearranging priorities, or inventing "better" organization.

---

### 3. Constraint Redundancy

**Problem:** Models sometimes "obey once, forget later."

**Solution:** Repeat critical constraints at multiple levels:

1. **Global rules (policy)** - In the critical rules section
2. **Local rules (implementation)** - Within each section's specs
3. **Final checklist (self-audit)** - At the end as validation

**Example for "no gradients":**
```
CRITICAL OUTPUT RULES:
- NO gradients of any kind

DESIGN SYSTEM:
- Solid fills only
- No transparency
- No gradients

FINAL VALIDATION CHECK:
- Solid colors only
- No gradients
```

This defense-in-depth approach is surprisingly effective.

---

### 4. Negative Space Control

**Problem:** Models assume a scene with background, lighting, depth, "a thing sitting on a surface."

**Solution:** Explicitly control the space around and behind the content:

```
BACKGROUND:
- Solid white (#FFFFFF) ONLY
- No texture
- No vignette
- No fade
- NO background beyond the artwork edges

OUTPUT CONSTRAINTS:
- Edge-to-edge artwork (this IS the printed content)
- NO drop shadows
- NO lighting, gloss, bevel, or depth effects
```

This removes the "stage" where mockup-ness happens.

---

### 5. Allowed vs. Forbidden Distinction

**Problem:** Saying "don't make a spreadsheet table" can be interpreted as "don't align data in rows/columns."

**Solution:** Split clearly what's allowed vs. forbidden:

**Allowed (structured layouts):**
- Aligned columns/rows
- Subtle dividers
- Typographic hierarchy
- Designed tables with consistent spacing

**Forbidden (UI/software appearance):**
- Excel-like grid with cell boxes
- Spreadsheet sheet headers
- Software interface styling
- Table borders that look like applications

This gives the model permission to be structured without drifting into "software screenshot."

---

### 6. Physical Context Anchoring

**Problem:** Without real-world context, models optimize for "looks cool" not "actually usable."

**Solution:** Provide explicit physical usage context:

```
IMPORTANT REAL-WORLD CONTEXT:
These are badge buddies.
They are worn BEHIND a nurse's ID badge.
They must be LANDSCAPE (wider than tall).
They are quick-glance clinical references.

This is NOT a UI card.
This is NOT a product mockup.
This is NOT an illustration.

These images represent the literal ink-on-paper artwork sent directly to a printer.
```

This constrains dimensions, density, and purpose appropriately.

---

### 7. Deliverables Locking

**Problem:** Models may produce single images when multiples needed, or wrong dimensions.

**Solution:** Lock deliverables with absolute specificity:

```
CRITICAL OUTPUT RULES (NON-NEGOTIABLE):
- Output EXACTLY TWO IMAGES
- Image 1 = BADGE BUDDY A (FRONT)
- Image 2 = BADGE BUDDY B (BACK)
- Each image must be a SINGLE flat rectangle
- Orientation: LANDSCAPE (horizontal)

PHYSICAL SIZE & CANVAS:
Badge buddy size:
- 4.5 inches wide x 2.75 inches tall
- Landscape orientation
- Resolution: 1350 x 825 px at 300 DPI
```

---

### 8. Validation Checklist

**Problem:** Models drift from requirements during generation.

**Solution:** Add a final self-audit block that acts as implicit re-evaluation:

```
FINAL VALIDATION CHECK:
- Two images only
- Landscape orientation
- 2 rows x 3 columns per card
- Equal-sized boxes
- One drug per box
- Flat print artwork
- Solid colors only
- No gradients
- No rounded corners
- No UI or mockup styling
- Optimized for instant badge-level glance

If any gradient, shadow, or rounded corner appears, the output is incorrect.
```

---

## Anti-Patterns to Avoid

### Rounded Corners = UI Trigger

**BAD:** `4px rounded corners on category blocks`

Rounded corners trigger UI card associations. Use sharp 90-degree corners for print materials.

**GOOD:**
```
ALL SHAPES:
- Rectangular only
- Sharp 90-degree corners only
```

### Vague Layout Instructions

**BAD:** `Organize content into color-coded category blocks stacked vertically`

**GOOD:**
```
EXACTLY 2 ROWS x 3 COLUMNS
BOX 1: [specific content]
BOX 2: [specific content]
...
```

### Single-Level Constraints

**BAD:** Saying "no gradients" once

**GOOD:** Saying "no gradients" in global rules, design system, and validation checklist

### Missing Orientation Lock

**BAD:** `Portrait orientation` (without explicit dimension lock)

**GOOD:**
```
- 4.5 inches wide x 2.75 inches tall
- Landscape orientation (horizontal)
- Resolution: 1350 x 825 px at 300 DPI
```

---

## Template: Print-Ready Reference Card

Use this template for badge buddies, pocket cards, and similar print materials:

```
TASK: Generate [NUMBER] SEPARATE FLAT PRINT ARTWORK IMAGE(S) representing [DESCRIPTION OF WHAT IT IS].

IMPORTANT REAL-WORLD CONTEXT:
[Describe what this is, how it's used, who uses it]
This is NOT a UI card.
This is NOT a product mockup.
This is NOT an illustration.
These images represent the literal ink-on-paper artwork sent directly to a printer.

================================================
CRITICAL OUTPUT RULES (NON-NEGOTIABLE)
================================================

- Output EXACTLY [N] IMAGE(S)
- [If multiple: Image 1 = X, Image 2 = Y, etc.]
- Each image must be a SINGLE flat rectangle
- Orientation: [LANDSCAPE/PORTRAIT] ([horizontal/vertical])
- NO rounded outer corners
- NO drop shadows
- NO gradients of any kind
- NO lighting, gloss, bevel, or depth effects
- NO background beyond the artwork edges

If any gradient, shadow, or rounded corner appears, the output is incorrect.

================================================
PHYSICAL SIZE & CANVAS
================================================

Size:
- [X] inches wide x [Y] inches tall
- [Orientation] orientation
- Resolution: [pixels] at 300 DPI
- Edge-to-edge artwork (this IS the printed insert)

Background:
- Solid white (#FFFFFF) ONLY
- No texture
- No vignette
- No fade

================================================
GRID LAYOUT (MOST IMPORTANT)
================================================

[DESCRIBE EXACT GRID]:
- EXACTLY [N] ROWS x [M] COLUMNS
- TOTAL OF [N*M] BOXES
- ALL BOXES MUST BE:
  - Equal width
  - Equal height
  - Evenly spaced
  - Perfectly aligned
- One item per box
- No spanning, no empty boxes

[ENUMERATE SLOTS]:
BOX 1: [Content]
BOX 2: [Content]
...

================================================
DESIGN SYSTEM (STRICT)
================================================

ALL SHAPES:
- Rectangular only
- Sharp 90-degree corners only
- Solid fills only
- No transparency
- No gradients

[SECTION-SPECIFIC RULES]

TYPOGRAPHY ONLY - NO ICON GRAPHICS (unless specifically needed).
Allowed symbols (text only): [list allowed symbols]

================================================
TYPOGRAPHY
================================================

- [Element]: [Weight], [Size]
- Minimum text size: [X] pt
- Clean sans-serif
- High contrast

================================================
CONTENT SECTIONS
================================================

[HEADER SECTION]
[Fill color, text specs]

[BODY SECTIONS - enumerate each]

[FOOTER SECTION]
[Fill color, text specs]

================================================
FINAL VALIDATION CHECK
================================================

- [Number] images only
- [Orientation] orientation
- [Grid spec]
- Equal-sized boxes
- [Content constraint]
- Flat print artwork
- Solid colors only
- No gradients
- No rounded corners
- No UI or mockup styling
- [Use-case optimization]
```

---

## Template: Complex Infographic

For multi-column, time-sequenced, or workflow infographics:

```
TASK: Create [DESCRIPTION] infographic showing [WORKFLOW/PROCESS].

PHYSICAL CONTEXT:
[What this is, size, how used]

================================================
CRITICAL OUTPUT RULES
================================================

[Same structure as above - deliverables, dimensions, constraints]

================================================
COLUMN LAYOUT
================================================

[Number]-column vertical structure:
- Column 1 ([X]% width): [NAME] - [Color] zone (#[HEX] background)
- Column 2 ([X]% width): [NAME] - [Color] zone (#[HEX] background)
[etc.]

Header section (top [X]%): [Color] band with [text color]
Footer section (bottom [X]%): [Color] band with [text color]

================================================
COMPONENTS
================================================

[DETAIL EACH SECTION with specific content]

================================================
CONSTRAINTS (REPEATED)
================================================

- NO gradients - solid colors only
- All text minimum [X]pt
- High contrast: minimum 4.5:1 ratio
- [Font specification]
- Line icons only if needed
- No decorative elements
- Bleed area: [X]" on all sides
- Safe zone: [X]" margin from edges
- Print-ready: CMYK color space, 300 DPI

================================================
VISUAL HIERARCHY
================================================

1. Primary attention: [Elements]
2. Secondary attention: [Elements]
3. Tertiary attention: [Elements]
4. Background: [Elements]

================================================
FINAL VALIDATION CHECK
================================================

[Enumerate all constraints to verify]
```

---

## Troubleshooting Common Failures

### Problem: AI creates mockup with shadows/3D

**Add to prompt:**
```
This is FLAT PRINT ARTWORK.
NOT a product mockup.
NOT a 3D render.
NO shadows.
NO depth.
Just the flat printed surface viewed straight-on.
```

### Problem: AI adds rounded corners

**Add to prompt:**
```
ALL corners must be sharp 90-degree angles.
NO rounded corners anywhere.
Rounded corners = rendering error.
```

### Problem: AI creates gradient backgrounds

**Add to prompt:**
```
SOLID colors ONLY.
If any gradient appears in any element, the output is incorrect.
Gradients are forbidden in: backgrounds, fills, headers, footers, boxes, all elements.
```

### Problem: Content is merged or reorganized

**Add to prompt:**
```
BOX 1 must contain EXACTLY: [content]
BOX 2 must contain EXACTLY: [content]
[enumerate all slots]
Do NOT combine items.
Do NOT reorganize.
Do NOT omit any item.
```

### Problem: Wrong number of outputs

**Add to prompt:**
```
Generate EXACTLY [N] separate images.
NOT [N-1]. NOT [N+1]. EXACTLY [N].
```

### Problem: Wrong orientation or dimensions

**Add to prompt:**
```
LANDSCAPE means wider than tall.
Exact dimensions: [W] x [H] inches = [pixels] at 300 DPI.
If the image is taller than wide, the output is incorrect.
```

---

## Model-Specific Notes

### Nano Banana (Gemini 2.5 Flash Image)

**What it is:** Google's image generation model, colloquially named "Nano Banana" after its codename on LMArena. Launched August 2025. Fast generations, good for basic image creation and editing.

**Key advantages:**
- **32,768 token context window** (vs. CLIP's 77, T5's 512) — supports extremely detailed prompts
- **Trained on Markdown and JSON** — structured prompts are natively effective
- **Autoregressive architecture** — superior text rendering within images
- **Conversational editing** — upload or generate an image, then request natural language changes

**Prompting techniques:**
- **Use Markdown formatting** — dashed lists, section headers, and structured blocks improve parsing
- **Use ALL CAPS** for critical constraints — `MUST` and `NEVER` in caps improves adherence
- **Specify hex color codes** — use `#9F2B68` instead of generic color names like "magenta"
- **Reference photography terminology** — "85mm lens at f/2.8," "three-point lighting," "golden hour," "rule of thirds"
- **Reference professional standards** — "Pulitzer Prize winning cover photo" elevates quality
- **JSON character definitions** work well — provide detailed JSON objects (~2600 tokens) describing specific attributes
- **Provide reference images** — 17 reference images dramatically outperform 2 for character consistency
- **Iterate, don't regenerate** — if an image is 80% right, ask for specific changes rather than starting from scratch
- **Add imperfections for realism** — subtle flaws make outputs feel less "AI-generated"

**What doesn't work:**
- Style transfer on existing images is unreliable
- "Do not include any text" alone is insufficient — add compositional instructions to prevent decorative text
- Vague prompts produce generic results — be explicit about composition, framing, and subject

### Nano Banana Pro (Gemini 3 Pro Image)

**What it is:** The advanced version released November 2025. Uses Gemini 3 Pro as its text encoder with mandatory "Thinking" reasoning before generation.

**Key differences from base Nano Banana:**
- **2K output (4MP)** vs. base model's 1K (1MP), with optional 4K
- **Near-perfect text rendering** — specify exact fonts (Times New Roman, Roboto, Fira Code)
- **Search grounding** — integrates Google Search for factually accurate infographics and diagrams
- **System prompts** — now functional for consistent constraint enforcement across multiple generations
- **Few-shot design** — accepts up to 14 reference images
- **Improved style transfer** — handles Ghibli-style and other artistic conversions

**Prompting techniques unique to Pro:**
- **Name exact fonts and weights** — the model reliably renders specified typography
- **Use system prompts** — place style/constraint information in system prompts for consistency across variations
- **Leverage grid generation** — supports multi-image layouts (2x2, 4x4, up to 8x8) where each subimage can be distinct
- **Use for text-heavy visuals** — infographics, diagrams with labels, and typographic compositions
- **Stop using 2023-era prompts** — the model understands natural language and structural components natively

**Limitations to know:**
- **Realism bias** — the Thinking process tends to push outputs toward realism, potentially undermining surreal or absurdist goals
- **Variable latency** — 20 seconds to over a minute, especially during peak hours
- **Character reference adherence** — may default to canonical versions of known characters despite reference images

### DALL-E 3
Add: `"Graphic design flat lay, reference card design, typography-focused, print material"`

### Midjourney
```
[prompt content]
--ar [ratio] --v 6 --style raw --s 25
```
Add negative prompt: `--no badge lanyard clip holder 3d mockup photo gradient shadow rounded`

### Stable Diffusion
Negative prompt: `"badge, lanyard, clip, holder, 3d, mockup, photo, gradient, shadow, rounded corners, depth, lighting, gloss, bevel"`

### ChatGPT / GPT-4o / GPT-5 / GPT Image 2
These models respond well to:
- Explicit grid enumeration
- Repeated constraints
- "If X appears, the output is incorrect" language
- Physical context anchoring

**For gpt-image-2 specifically** (OpenAI's flagship image model, released April 2026):
- Set `quality="high"` for print-ready text-heavy artifacts (badge buddies, infographics, worksheets).
- The 5-section structure (Scene / Subject / Key Details / Use Case / Constraints) maps cleanly onto print-ready prompts — put the print-specific block under CONSTRAINTS.
- `input_fidelity` is disabled in gpt-image-2 — do not pass it.
- For full prompting details see **[GPT_IMAGE_2_GUIDE.md](GPT_IMAGE_2_GUIDE.md)**.

---

## Quality Checklist for Image Generation Prompts

Before finalizing any image generation prompt, verify:

- [ ] Uses print terminology, not UI terminology
- [ ] Specifies exact grid (NxM) if applicable
- [ ] Enumerates content slots explicitly
- [ ] Repeats critical constraints at 3+ levels
- [ ] Controls negative space and background
- [ ] Distinguishes allowed vs. forbidden structures
- [ ] Provides physical context (size, usage, who)
- [ ] Locks deliverables (count, orientation, dimensions)
- [ ] Includes validation checklist at end
- [ ] Avoids rounded corners (or explicitly allows with rationale)
- [ ] Uses "if X appears, output is incorrect" language for critical constraints

---

## Technique Cross-Reference

Each of the 8 core techniques in this guide has a corresponding entry in the [`MASTER_TECHNIQUE_INDEX.md`](../../techniques/MASTER_TECHNIQUE_INDEX.md) under the SV (Specialized Visual) family:

| # | Technique | Code | Master Index Entry |
|---|-----------|------|--------------------|
| 1 | Terminology Steering | **SV-11** | Reframe artifact names using print/production terminology |
| 2 | Grid Forcing + Enumerated Slots | **SV-12** | Exact grid geometry with individually numbered content slots |
| 3 | Constraint Redundancy | **SV-13** | Repeat critical constraints at 3+ structural levels |
| 4 | Negative Space Control | **SV-14** | Explicitly control background and surrounding space |
| 5 | Allowed vs. Forbidden Distinction | **SV-15** | Split visual instructions into allowed/forbidden categories |
| 6 | Physical Context Anchoring | **SV-16** | Real-world usage context (dimensions, who, how) |
| 7 | Deliverables Locking | **SV-17** | Lock count, orientation, dimensions, resolution |
| 8 | Validation Checklist | **SV-18** | Final self-audit block with pass/fail criteria |

**Related SV techniques** (general visual/interview patterns):
- **SV-01** Visual Output Specification — General layout requirements (use SV-12 for grid-specific layouts)
- **SV-05** Printable Worksheet Output Format — Print-ready educational materials
- **SV-07** Calculation Specification in Layout — Embedded formulas for dashboard visuals

For technique combination guidance, see [`USE_CASE_LOOKUP.md`](../../techniques/USE_CASE_LOOKUP.md) → "Visual Output & Image Generation Tasks."

---

## Summary

The difference between prompts that work and prompts that fail comes down to **specificity and constraint enforcement**:

1. **Be explicit** - Exact grids, enumerated slots, locked dimensions
2. **Be redundant** - Repeat constraints at multiple levels
3. **Be negative** - Say what NOT to do as much as what to do
4. **Be physical** - Anchor to real-world usage context
5. **Be testable** - End with validation checklist

Image models optimize for what they think you want. The techniques in this guide help you communicate exactly what you actually need.

---

*Based on empirical testing with ChatGPT 5.2 image generation, January 2026*
*Updated with Nano Banana and Nano Banana Pro prompting techniques, February 2026*
