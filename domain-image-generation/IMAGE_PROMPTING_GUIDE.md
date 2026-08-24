# Comprehensive Image Prompting Guide

**Purpose:** A complete reference for crafting effective prompts across all AI image generation models and visual output types — from photorealistic renders to structured diagrams to print-ready materials.

**Audience:** Anyone writing prompts for AI image generators (ChatGPT/DALL-E, Midjourney, Stable Diffusion, Nano Banana, Flux, Ideogram, etc.)

**Relationship to Other Guides:**
- **[IMAGE_GENERATION_GUIDE.md](IMAGE_GENERATION_GUIDE.md)** — Focused guide for print-ready materials (badge buddies, worksheets, reference cards) with 8 constraint-enforcement techniques
- **[VIDEO_GENERATION_GUIDE.md](VIDEO_GENERATION_GUIDE.md)** — Video generation with Veo 3 / 3.1
- **This guide** — Broad coverage of all image prompting scenarios, from creative photography to technical diagrams

---

## Table of Contents

1. [How Image Models Read Prompts](#1-how-image-models-read-prompts)
2. [The 5-Layer Prompt Framework](#2-the-5-layer-prompt-framework)
3. [Subject Types and How to Prompt Them](#3-subject-types-and-how-to-prompt-them)
4. [Composition and Camera Control](#4-composition-and-camera-control)
5. [Style and Aesthetic Direction](#5-style-and-aesthetic-direction)
6. [Color Control](#6-color-control)
7. [Text in Images](#7-text-in-images)
8. [Multi-Element and Layout Prompting](#8-multi-element-and-layout-prompting)
9. [Structured Visual Outputs](#9-structured-visual-outputs)
10. [Print-Ready Materials](#10-print-ready-materials)
11. [Negative Prompting and Constraint Enforcement](#11-negative-prompting-and-constraint-enforcement)
12. [Iterative Refinement Workflows](#12-iterative-refinement-workflows)
13. [Model-Specific Strategies](#13-model-specific-strategies)
14. [Prompt Templates by Use Case](#14-prompt-templates-by-use-case)
15. [Common Failures and Fixes](#15-common-failures-and-fixes)
16. [Quality Checklist](#16-quality-checklist)

---

## 1. How Image Models Read Prompts

Understanding how models process prompts prevents the most common mistakes.

### Token Priority and Attention

Different models weight prompt tokens differently:

| Model Family | Token Handling | Implication |
|-------------|---------------|-------------|
| **DALL-E 3 / GPT Image** | LLM rewrites your prompt internally before generating | Natural language works well; the model "interprets" intent |
| **Midjourney** | Front-loaded attention — early words matter most | Put the most important subject/style first |
| **Stable Diffusion / Flux** | CLIP-based encoding with ~77 token limit (SD 1.5) or T5 encoder (SDXL/Flux) | Be concise; use prompt weighting syntax |
| **Nano Banana** | 32K token context, Markdown-aware | Structured prompts with headers and lists work natively |
| **Nano Banana Pro** | Full LLM reasoning ("Thinking") before generation | Detailed natural language + structural specifications |
| **Ideogram** | Strong text rendering, style-first attention | Lead with style, embed text instructions explicitly |

### Key Principle: Specificity Beats Abstraction

Every image model performs better with concrete, specific language than with abstract descriptions.

```
WEAK: "A beautiful landscape"
BETTER: "Rolling green hills under a stormy sky at golden hour"
BEST: "Rolling emerald hills with wildflowers, dramatic cumulonimbus clouds
       backlit by low golden sun, long shadows across the valley,
       shot on 35mm film, Fujifilm Velvia color saturation"
```

The progression adds: **subject detail → environment → lighting → medium → color reference**.

### The Three Pillars of Image Prompting

Every effective image prompt addresses three questions:

1. **WHAT** — Subject, objects, characters, text content
2. **HOW** — Style, medium, technique, aesthetic, camera settings
3. **WHERE** — Environment, composition, spatial relationships, background

Weak prompts answer only one. Strong prompts answer all three with specificity.

---

## 2. The 5-Layer Prompt Framework

Build prompts layer by layer. Each layer adds precision:

### Layer 1: Subject Core
*What is the main subject?*

```
A red fox sitting on a moss-covered log
```

### Layer 2: Environment and Context
*Where is the subject? What surrounds it?*

```
A red fox sitting on a moss-covered log in a misty Pacific Northwest forest,
morning dew on ferns, soft diffused light filtering through old-growth canopy
```

### Layer 3: Style and Medium
*What does it look like? What artistic tradition?*

```
A red fox sitting on a moss-covered log in a misty Pacific Northwest forest,
morning dew on ferns, soft diffused light filtering through old-growth canopy,
nature documentary photography, National Geographic style,
shot with Canon EOS R5, 200mm telephoto lens at f/2.8
```

### Layer 4: Technical Specifications
*Camera, lighting, color, aspect ratio*

```
...
shallow depth of field, bokeh background,
natural color palette with rich greens and warm amber tones,
high dynamic range, 16:9 aspect ratio
```

### Layer 5: Constraints and Refinement
*What to avoid, what to emphasize*

```
...
No human elements. No text or watermarks.
The fox should be the clear focal point with eyes in sharp focus.
Avoid overly saturated or artificial-looking colors.
```

### Complete Prompt (All 5 Layers)

```
A red fox sitting on a moss-covered log in a misty Pacific Northwest forest,
morning dew on ferns, soft diffused light filtering through old-growth canopy.
Nature documentary photography, National Geographic style,
shot with Canon EOS R5, 200mm telephoto lens at f/2.8,
shallow depth of field, bokeh background.
Natural color palette with rich greens and warm amber tones,
high dynamic range, 16:9 aspect ratio.
No human elements. No text or watermarks.
The fox should be the clear focal point with eyes in sharp focus.
```

---

## 3. Subject Types and How to Prompt Them

Different subjects require different prompting strategies.

### People and Portraits

**Key challenge:** Avoiding the "AI look" — waxy skin, symmetrical features, vacant expressions.

**Effective techniques:**
- Specify **age, ethnicity, body type** for diversity and realism
- Reference **specific emotions** rather than generic expressions: "wry half-smile" not "happy"
- Add **imperfections** for realism: "subtle laugh lines," "slightly windswept hair," "freckles across the nose"
- Reference **photography genres**: "candid street portrait," "editorial fashion," "environmental portrait"
- Specify **eye direction** and **body language**: "looking slightly off-camera," "relaxed shoulders, one hand in pocket"

```
Environmental portrait of a middle-aged Black woman, civil engineer,
standing on a construction site at dawn. She wears a hard hat and high-vis vest,
arms crossed with quiet confidence. Slight smile, crow's feet around eyes.
Shot on medium format digital, 85mm equivalent, f/2.8.
Natural morning light, construction cranes silhouetted in background.
Documentary photography style, slightly desaturated warm tones.
```

### Landscapes and Environments

**Key challenge:** Generic, postcard-quality outputs.

**Effective techniques:**
- Specify **time of day** and **season**: "late October, 4pm, low autumn sun"
- Add **weather conditions**: "scattered alto-cumulus, humidity haze on the horizon"
- Reference **specific locations** or geological features: "basalt columnar formations," "sandstone arches"
- Include **atmospheric effects**: "volumetric fog," "crepuscular rays," "heat shimmer"
- Specify **focal depth**: "foreground wildflowers in soft focus, mid-ground river sharp, distant mountains slightly hazy"

### Objects and Products

**Key challenge:** Floating-in-void syndrome or overly staged product photography.

**Effective techniques:**
- Specify **surface and material**: "matte ceramic with a subtle speckle glaze"
- Define **lighting setup**: "softbox key light from upper left, fill card from right, black background"
- Add **context objects** for scale and lifestyle: "next to a steaming cup of coffee on a reclaimed wood desk"
- Specify **camera angle**: "45-degree elevated angle," "eye-level hero shot"

### Animals and Nature

**Effective techniques:**
- Specify **species precisely**: "red-tailed hawk (Buteo jamaicensis)" not just "hawk"
- Include **behavioral description**: "mid-pounce," "grooming," "alert with ears forward"
- Reference **wildlife photography** conventions: "hide photography," "eye-level with subject"

### Architecture and Interiors

**Effective techniques:**
- Specify **architectural style**: "Brutalist concrete," "Art Deco revival," "Japanese minimalist"
- Include **human scale elements**: "a person walking through the atrium for scale"
- Reference **architectural photography**: "two-point perspective," "tilt-shift miniature effect"
- Specify **time of day for lighting**: "blue hour exterior with warm interior lights glowing"

---

## 4. Composition and Camera Control

### Framing and Angle

| Term | Effect | When to Use |
|------|--------|-------------|
| **Extreme close-up** | Fills frame with detail (eye, texture) | Texture, emotion, detail |
| **Close-up** | Head and shoulders | Portraits, product hero shots |
| **Medium shot** | Waist up | Conversational, editorial |
| **Full shot** | Entire body/object in frame | Fashion, full product |
| **Wide shot** | Subject small in environment | Landscapes, architecture, context |
| **Bird's eye / overhead** | Looking straight down | Flat lays, maps, food photography |
| **Worm's eye** | Looking straight up | Dramatic, powerful, architectural |
| **Dutch angle** | Tilted horizon | Tension, unease, dynamic energy |
| **Over-the-shoulder** | Framed past another element | Depth, narrative, POV |

### Lens Simulation

Specifying lens focal length changes the feel dramatically:

| Focal Length | Character | Best For |
|-------------|-----------|----------|
| **14-24mm** | Wide, distorted edges, expansive | Landscapes, architecture, dramatic |
| **35mm** | Natural perspective, slight wide | Street photography, environmental |
| **50mm** | Closest to human eye | Documentary, natural feel |
| **85mm** | Slight compression, flattering | Portraits, products |
| **135mm** | Compressed background, isolation | Fashion, sports, wildlife |
| **200mm+** | Heavy compression, stacked layers | Wildlife, abstract compression |

```
Example: "Shot with 24mm wide-angle lens at f/11, deep depth of field,
everything from foreground rocks to distant mountains in sharp focus"

vs.

"Shot with 200mm telephoto at f/2.8, extremely shallow depth of field,
subject isolated against creamy bokeh background"
```

### Composition Rules

Reference these explicitly when composition matters:

- **Rule of thirds** — "Subject positioned at the left third intersection point"
- **Leading lines** — "Road converging toward the vanishing point, drawing the eye to the subject"
- **Frame within frame** — "Viewed through an archway / doorway / window frame"
- **Negative space** — "Subject small in frame with expansive empty sky above"
- **Symmetry** — "Perfect bilateral symmetry reflected in the still water"
- **Golden ratio / spiral** — "Composition following the golden spiral, focal point at the spiral's origin"

---

## 5. Style and Aesthetic Direction

### Photography Styles

| Style | Key Descriptors |
|-------|----------------|
| **Documentary** | "candid, unposed, available light, grain, slightly imperfect framing" |
| **Editorial / Fashion** | "high-end, carefully lit, styled, bold color palette, magazine-worthy" |
| **Street** | "decisive moment, urban context, natural light, candid, 35mm" |
| **Fine Art** | "intentional, conceptual, gallery-quality print, deliberate composition" |
| **Commercial / Product** | "clean, bright, hero lighting, isolated or lifestyle context" |
| **Photojournalism** | "raw, authentic, decisive moment, unmanipulated, story-driven" |

### Illustration and Art Styles

| Style | Key Descriptors |
|-------|----------------|
| **Flat design** | "geometric, solid colors, no gradients, minimal shadows, vector-like" |
| **Watercolor** | "soft edges, color bleeding, paper texture, organic shapes, transparent washes" |
| **Oil painting** | "visible brushstrokes, rich impasto, warm palette, gallery canvas texture" |
| **Line art / Ink** | "black ink on white, cross-hatching, clean outlines, stippling" |
| **Isometric** | "30-degree angle, no perspective distortion, technical illustration, cutaway" |
| **Pixel art** | "8-bit or 16-bit aesthetic, limited palette, dithering, grid-aligned" |
| **Collage** | "mixed media, cut-paper elements, layered textures, found materials" |
| **Retro / Vintage** | "1960s/70s poster aesthetic, limited screen print palette, halftone dots, aged paper" |
| **Anime / Manga** | "cel-shaded, expressive eyes, dynamic poses, speed lines" |

### Referencing Artistic Traditions

Use specific references rather than generic style words:

```
WEAK: "artistic style"
BETTER: "in the style of a mid-century travel poster"
BEST: "mid-century travel poster aesthetic, limited 4-color screen print palette,
       bold geometric shapes, hand-lettered title, slightly worn and faded print texture,
       reminiscent of WPA National Parks posters from the 1930s-40s"
```

### Style Mixing

Combine styles for unique results:

```
"Photorealistic subject with watercolor environment bleeding at the edges"
"Technical blueprint precision for the structure, painterly clouds behind it"
"Flat vector illustration foreground elements, photographic landscape background"
```

---

## 6. Color Control

### Specifying Colors

Be explicit about color. Models interpret color names inconsistently.

| Approach | Example | Reliability |
|----------|---------|-------------|
| **Color name** | "red" | Low — which red? |
| **Descriptive color** | "burnt sienna" | Medium — subjective |
| **Hex code** | "#C0392B" | High (Nano Banana, Ideogram) |
| **Pantone reference** | "Pantone 186 C" | Medium — model may not know exact value |
| **Reference object** | "the red of a fire truck" | High — anchors to known visual |
| **Color temperature** | "warm golden tones" | Medium — directional, not precise |

### Color Palette Strategies

```
MONOCHROMATIC:
"Color palette: various shades and tints of deep teal (#006D77),
ranging from near-black (#002428) to pale aqua (#E0F4F5)"

COMPLEMENTARY:
"Color palette limited to deep navy (#1B2838) and warm amber (#F2A900)
with white (#FFFFFF) for contrast"

ANALOGOUS:
"Warm palette: sunset orange (#FF6B35), coral (#FF8C61),
golden yellow (#FFB347), transitioning across the composition"

SPECIFIC BRAND COLORS:
"Use only these exact colors:
- Primary: #2563EB (blue)
- Secondary: #10B981 (green)
- Accent: #F59E0B (amber)
- Background: #F8FAFC (off-white)
- Text: #1E293B (near-black)"
```

### Lighting and Color Temperature

| Lighting | Color Temperature | Mood |
|----------|------------------|------|
| **Golden hour** | Warm (3000-4000K) | Nostalgic, romantic, soft |
| **Blue hour** | Cool (7000-10000K) | Calm, melancholy, cinematic |
| **Overcast** | Neutral (5500-6500K) | Even, documentary, soft |
| **Tungsten** | Very warm (2700K) | Intimate, indoor, cozy |
| **Fluorescent** | Cool green cast | Clinical, institutional |
| **Neon** | Mixed vivid colors | Urban, nightlife, cyberpunk |
| **Candlelight** | Very warm, flickering | Intimate, historical, dramatic |

---

## 7. Text in Images

Text rendering has improved dramatically. Here is how to get it right.

### Which Models Render Text Well

| Model | Text Capability | Notes |
|-------|----------------|-------|
| **Nano Banana Pro** | Near-perfect | Specify exact fonts (Times New Roman, Roboto, Fira Code) |
| **Ideogram 2/3** | Excellent | Purpose-built for text in images |
| **DALL-E 3 / GPT Image** | Good | Simple text works; complex text may have errors |
| **Flux** | Good | Long text blocks can drift |
| **Midjourney v6+** | Moderate | Short text only; use `--style raw` |
| **Stable Diffusion** | Poor-Moderate | Requires ControlNet or specific models |
| **Nano Banana (base)** | Good | Markdown-formatted text instructions work well |

### Text Prompting Techniques

**1. Explicit quoting** — Always put desired text in quotes:
```
The sign reads "OPEN 24 HOURS" in bold red letters
```

**2. Character-level specification** (for critical text):
```
The word "CAFÉ" — C, A with accent, F, E — in serif font on the awning
```

**3. Font specification** (Nano Banana Pro, Ideogram):
```
Title text: "Annual Report 2026" in Garamond Bold, 48pt, centered,
dark navy (#1B2838) on white
```

**4. Text placement anchoring:**
```
Title centered in the top 15% of the image
Subtitle directly below, 20% smaller
Body text in the bottom third, left-aligned with 10% margin
```

**5. Avoiding unwanted text:**
```
Do NOT include any text, lettering, words, labels, or watermarks in the image.
Fill any areas where text might appear with the background pattern instead.
```

---

## 8. Multi-Element and Layout Prompting

### Spatial Relationships

Be explicit about how elements relate:

```
VAGUE: "A cat and a dog"
SPECIFIC: "A tabby cat sitting on the left side of the frame,
a golden retriever lying down on the right,
both facing toward the center,
approximately 3 feet apart on a hardwood floor"
```

### Grid-Based Layouts

For structured multi-element outputs, specify exact grids:

```
LAYOUT: 2x2 grid, each cell contains one product photo
- TOP LEFT: Red sneaker, 45-degree angle
- TOP RIGHT: Blue sneaker, matching angle
- BOTTOM LEFT: Green sneaker, matching angle
- BOTTOM RIGHT: Black sneaker, matching angle
All on matching white backgrounds, consistent lighting across all four
```

### Panel and Sequence Layouts

For comics, storyboards, or step-by-step visuals:

```
4-panel horizontal strip, equal panel sizes, thin black borders:
Panel 1: Character approaches a door (wide shot)
Panel 2: Hand reaching for the doorknob (close-up)
Panel 3: Door swings open, bright light (medium shot from behind)
Panel 4: Character steps into a vast library (wide establishing shot)
Consistent character design across all panels.
```

### Collage and Composite Layouts

```
Magazine-style mood board layout on white background:
- Large hero image (60% of space, top): Coastal cliff at sunset
- Three smaller images (bottom row, equal width):
  - Left: Close-up of sea foam on sand
  - Center: Lighthouse silhouette
  - Right: Weathered wooden boat
Consistent warm golden color grading across all images.
Thin white borders between images. No text.
```

---

## 9. Structured Visual Outputs

For diagrams, dashboards, infographics, and data visualizations — visual outputs that communicate information rather than tell a story.

### The TASK-STYLE-LAYOUT-COMPONENTS-CONSTRAINTS Pattern

This is the proven structure used across all 56 Nano Banana visualization prompts in this repository:

```
TASK: [What to generate — be specific]

STYLE: [Visual aesthetic and design tradition]

LAYOUT: [Spatial organization — grid, columns, flow direction]

COMPONENTS:
- [Element 1 with specifications]
- [Element 2 with specifications]
- [Element 3 with specifications]

CONSTRAINTS:
- [What must NOT happen]
- [Spacing, alignment, readability rules]
- [Technical requirements]

SOURCE MATERIAL:
[User's data or content to visualize]

INTERPRETATION:
[Who the audience is and what they should take away]
```

### Diagram Types and How to Prompt Them

#### Architecture and System Diagrams

```
TASK: Generate a cloud architecture diagram.

STYLE: Modern cloud diagramming conventions (AWS/GCP icon style).

LAYOUT: Layered left-to-right flow:
  Layer 1 (left): Client tier — browsers, mobile apps
  Layer 2: API Gateway and load balancers
  Layer 3: Service mesh — microservices
  Layer 4: Data tier — databases, caches
  Layer 5 (right): Infrastructure — monitoring, logging

COMPONENTS:
- Service boxes with rounded corners and subtle shadows
- Directional arrows showing data flow (labeled with protocols)
- Cloud provider logo badges on each service
- Color-coded zones: blue for compute, green for data, orange for edge

CONSTRAINTS:
- No overlapping connection lines
- Equal spacing between layers
- Minimum 12pt text for all labels
- Arrows must show direction clearly
```

#### Flowcharts and Process Diagrams

```
TASK: Create a decision flowchart for [process].

STYLE: Clean technical diagram, black and white with one accent color.

LAYOUT: Top-to-bottom flow with horizontal branches for decisions.

COMPONENTS:
- Rounded rectangles for process steps
- Diamonds for decision points (Yes/No branches)
- Arrows with labels on decision branches
- Start (green circle) and End (red circle) markers

CONSTRAINTS:
- Maximum 3 levels of branching
- All text must be readable at 50% zoom
- Consistent shape sizes
- No crossing lines — reroute if necessary
```

#### Dashboards and KPI Displays

```
TASK: Build a KPI dashboard layout.

STYLE: Enterprise BI aesthetic, dark theme, data-ink ratio optimized.

LAYOUT: 12-column grid:
  Row 1 (top 20%): 4 KPI summary cards
  Row 2 (middle 50%): 2 charts side by side
  Row 3 (bottom 30%): Data table

COMPONENTS:
- KPI cards: metric name, current value, trend arrow, % change
- Left chart: Line chart showing 12-month trend
- Right chart: Stacked bar chart showing category breakdown
- Table: Top 10 items with sortable columns

CONSTRAINTS:
- All charts share a consistent color palette
- Numbers must be large enough to read at presentation distance
- Use data-ink ratio principles — no chart junk, no 3D effects
```

#### Timelines

```
TASK: Create a historical timeline.

STYLE: Clean editorial infographic.

LAYOUT: Horizontal timeline with alternating above/below event cards.

COMPONENTS:
- Central horizontal line with year markers
- Event cards with: date, title, 1-sentence description
- Connecting lines from timeline to cards
- Optional: small icon or image per event

CONSTRAINTS:
- Equal spacing between time periods (not proportional to actual time gaps)
- Cards must not overlap
- Consistent card size
- Maximum 8-10 events for readability
```

#### Comparison Matrices

```
TASK: Create a feature comparison matrix.

STYLE: Clean, readable grid. Corporate presentation quality.

LAYOUT: Table format:
  - Column 1: Feature names (left-aligned)
  - Columns 2-N: Products/options (centered)
  - Header row: Product names with logos

COMPONENTS:
- Check marks (green) and X marks (red) for boolean features
- Progress bars or ratings for scaled features
- Category group headers in gray bands
- Summary row at bottom

CONSTRAINTS:
- All columns equal width (except feature name column)
- Alternating row backgrounds for readability
- Header row visually distinct (darker background)
- No more than 5 comparison columns
```

---

## 10. Print-Ready Materials

For badge buddies, reference cards, worksheets, posters, and any output going to a physical printer.

> **Detailed guide:** See [IMAGE_GENERATION_GUIDE.md](IMAGE_GENERATION_GUIDE.md) for the complete 8-technique system.

### Quick Reference: The 8 Core Techniques

| # | Technique | One-Line Summary |
|---|-----------|-----------------|
| 1 | **Terminology Steering** | Say "flat print artwork" not "card" |
| 2 | **Grid Forcing + Enumerated Slots** | Explicit NxM grid with BOX 1, BOX 2... |
| 3 | **Constraint Redundancy** | Repeat "no gradients" at 3+ structural levels |
| 4 | **Negative Space Control** | Ban backgrounds, shadows, mockup staging |
| 5 | **Allowed vs. Forbidden** | Structured layouts OK, UI appearance forbidden |
| 6 | **Physical Context Anchoring** | "Worn behind a nurse's ID badge" |
| 7 | **Deliverables Locking** | Exact count, dimensions, resolution, orientation |
| 8 | **Validation Checklist** | Final self-audit block with pass/fail criteria |

### When to Use Print Techniques vs. Creative Techniques

| Scenario | Approach |
|----------|----------|
| Badge buddy, pocket reference card | Full 8-technique system |
| Educational worksheet for printing | 8-technique system + educational content structure |
| Marketing poster | Lighter constraints — focus on style, composition, brand colors |
| Social media graphic | Style-forward, with text rendering + brand constraints |
| Infographic poster | Hybrid — layout constraints from print, style from creative |
| Logo design | Creative techniques with specific deliverable constraints |

### Print Specifications Reference

| Format | Dimensions | Resolution | Notes |
|--------|-----------|------------|-------|
| Badge buddy (CR80) | 4.5" x 2.75" | 1350 x 825 px @ 300 DPI | Landscape, behind ID badge |
| Letter (US) | 8.5" x 11" | 2550 x 3300 px @ 300 DPI | Standard worksheets |
| A4 (International) | 8.27" x 11.69" | 2481 x 3507 px @ 300 DPI | Standard worksheets |
| Poster (18x24) | 18" x 24" | 5400 x 7200 px @ 300 DPI | Wall displays |
| Social (Instagram) | 1080 x 1080 px | 72 DPI screen | Square format |
| Social (Story) | 1080 x 1920 px | 72 DPI screen | 9:16 vertical |
| Presentation slide | 1920 x 1080 px | 72 DPI screen | 16:9 widescreen |

---

## 11. Negative Prompting and Constraint Enforcement

### Negative Prompting by Model

**Midjourney:**
```
--no text watermark gradient shadow blur
```

**Stable Diffusion / Flux:**
```
Negative prompt: "blurry, low quality, distorted, watermark, text,
deformed hands, extra fingers, cropped, out of frame"
```

**DALL-E 3 / GPT Image:**
No dedicated negative prompt field. Use natural language:
```
Do NOT include any text, watermarks, or signatures.
Avoid blurry or out-of-focus elements.
No distorted anatomy.
```

**Nano Banana / Nano Banana Pro:**
Use explicit constraint blocks:
```
CONSTRAINTS:
- NO gradients of any kind
- NO rounded corners
- NO drop shadows
- NO 3D effects or depth

If any gradient, shadow, or rounded corner appears, the output is incorrect.
```

### The "If X, Then Incorrect" Pattern

This self-audit language is surprisingly effective across all models:

```
If the image contains any text or lettering, the output is incorrect.
If any face appears distorted or has more than 5 fingers per hand, regenerate.
If the background is not solid white (#FFFFFF), the output is incorrect.
```

### Constraint Redundancy Strategy

For critical constraints, repeat at three structural levels:

```
LEVEL 1 — RULES (policy):
"CRITICAL: No gradients anywhere in the image."

LEVEL 2 — SPECIFICATIONS (implementation):
"Background: Solid navy #1E3A5F. Header fill: Solid white.
All fills must be solid single colors."

LEVEL 3 — VALIDATION (audit):
"FINAL CHECK:
- Verify: all fills are solid colors
- Verify: no gradients appear in any element
- If any gradient is present, output is incorrect"
```

---

## 12. Iterative Refinement Workflows

### The 80/20 Rule

If the first generation is 80%+ correct, **refine rather than regenerate**.

### Conversational Refinement (Nano Banana, ChatGPT, Midjourney)

```
Generation 1: "Create a dashboard layout for quarterly sales data"
→ Result: Good layout, but colors are wrong

Refinement: "Keep the exact same layout and composition.
Change the color scheme to: navy (#1B2838) headers,
teal (#0D9488) for positive metrics, coral (#EF4444) for negative metrics.
Keep everything else identical."
```

### Seed Preservation (Midjourney, Stable Diffusion)

Use the same seed value to maintain composition while changing details:

```
First: portrait of a woman in a garden --seed 12345
Refinement: portrait of a woman in a garden, autumn lighting --seed 12345
```

### Variation Strategy

```
APPROACH 1 — Style variations:
"Generate 4 variations of this logo concept:
1. Minimalist flat design
2. Gradient modern
3. Vintage letterpress
4. Geometric abstract"

APPROACH 2 — Color variations:
"Same design in 4 palettes:
1. Professional (navy/white)
2. Energetic (orange/teal)
3. Luxury (black/gold)
4. Friendly (soft blue/coral)"

APPROACH 3 — Compositional variations:
"Same subject, 4 compositions:
1. Centered, symmetrical
2. Rule of thirds, subject left
3. Close-up detail
4. Wide establishing shot"
```

### Progressive Refinement Workflow

```
Step 1: Rough concept (focus on composition and subject)
Step 2: Refine style and color palette
Step 3: Add detail and text elements
Step 4: Polish — fix specific issues, adjust contrast/lighting
Step 5: Final output at target resolution
```

---

## 13. Model-Specific Strategies

### Nano Banana Family (Google Gemini Image Models)

Google's Nano Banana family includes three models with different speed/quality tradeoffs. For the comprehensive guide, see [NANO_BANANA_GUIDE.md](NANO_BANANA_GUIDE.md). For production prompts, see [nano-banana/](nano-banana/).

**Nano Banana** (`gemini-2.5-flash-image`) — The original. 32K tokens, Markdown-aware, autoregressive text rendering. Best for budget-sensitive batch work, diagrams, dashboards, educational visuals.

**Nano Banana Pro** (`gemini-3-pro-image`) — Full LLM reasoning ("Thinking") before generation, near-perfect text rendering, Google Search grounding, system prompts, 14 references (6 object + 5 character + 3 style). Best for text-heavy visuals, factual infographics, hard compositions.

**Nano Banana 2** (`gemini-3.1-flash-image`) — Pro-level quality at Flash speed. 14 references (10 object + 4 character), 512px output for cheap screening (6–20 candidates), extreme aspect ratios (1:4, 4:1, 1:8, 8:1). Best for fast ideation, storyboards, multi-reference composites, Veo keyframes.

**Shared prompting tips (all three):**
- Use **narrative prompt style** — tell the model what you want in natural language, not keyword lists
- Use **ALL CAPS** for critical constraints: `MUST`, `NEVER`, `EXACTLY`
- Specify **hex color codes** directly: `#9F2B68` not "magenta"
- Reference **photography terminology** for photorealistic outputs: "85mm at f/2.8, three-point lighting"
- **Iterate, don't regenerate** — if 80% right, request specific changes
- Add **imperfections** for realism in photorealistic outputs

**Pro/NB2-specific tips:**
- **Name exact fonts and weights**: "Roboto Bold 24pt" — Pro renders them accurately
- **Use system prompts** (Pro) for consistent style across multiple generations
- **Role-separated references** (Pro, NB2): character refs in character slots, object refs in object slots, style refs in style slots (Pro only)
- **512px screening** (NB2): generate 6 candidates at `quality="standard"`, select, then produce at `quality="high"`
- **Search grounding** (Pro): `tools=[{"google_search": {}}]` for factual data verification

**What doesn't work across the family:**
- Style transfer on existing images is unreliable
- "Do not include any text" alone is insufficient — add compositional instructions
- Vague prompts produce generic results
- Thinking process (Pro) biases toward realism — state style commitment up front
- Known characters may default to canonical versions despite reference images

**Note:** Preview model IDs (`*-preview`) were deprecated June 25, 2026. Use the stable IDs above.

### GPT Image 2 (OpenAI, April 2026)

**Context:** OpenAI's flagship image model. Native thinking mode, 95%+ text rendering accuracy, web search during generation, up to 16 reference images, native 4K output, 1:3 to 3:1 aspect ratios. Released April 21, 2026 (snapshot `gpt-image-2-2026-04-21`).

**Best for:** Almost everything — photorealism, editing, infographics, marketing visuals with verbatim copy, multi-image compositing, character consistency. Default to this unless cost/throughput dominate.

**Prompting tips:**
- Use the **5-section structure**: Scene / Subject / Key Details / Use Case / Constraints.
- Set `quality="high"` for any in-image text, dense infographics, or identity-sensitive portraits.
- Wrap **EXACT TEXT** in quotes; specify font style, hex color, placement; spell hard words letter-by-letter.
- Reference up to **16 images by index and role** ("Image 1: face — preserve identity. Image 2: garment.").
- For edits, use **change/preserve sentences** with "ONLY" and a stated failure condition.
- Block **realism bias** (thinking mode favors realism) by stating style commitment up front.
- Use `n=4` for batch variations; don't ask the prompt for "4 variants."

**What's different from gpt-image-1.5:**
- `input_fidelity` parameter is **disabled** — high fidelity is the default.
- Reference image cap is **16** (was 8).
- Aspect ratio range is **1:3 to 3:1** (was 1:2 to 2:1).
- Native **4K** output (above 2560×1440 is experimental — fall back to 2K + external upscale for production).

**Limitations:**
- 4K output above 2560×1440 is flagged experimental; variability increases.
- Streaming, function calling, and structured outputs are not supported.
- No seed control for exact reproducibility.

**Comprehensive guide:** [GPT_IMAGE_2_GUIDE.md](GPT_IMAGE_2_GUIDE.md). **Production prompts:** [gpt-image-2/](gpt-image-2/).

### DALL-E 3 / GPT Image 1 (legacy)

**Best for:** Backward-compatibility flows. For new work, prefer `gpt-image-2`.

**Prompting tips:**
- Write **natural, descriptive paragraphs** — the model rewrites prompts internally
- Be specific about what you want, not how to generate it
- For structured layouts, add: `"Graphic design flat lay, print material"`
- Use **iterative conversation** to refine outputs
- Specify **aspect ratio** explicitly: "wide landscape format" or "tall portrait"

**Limitations:**
- Cannot control the internal prompt rewrite directly
- May add elements not requested (overinterpretation)
- No seed control for reproducibility
- Lower text rendering accuracy than gpt-image-2

### Midjourney v6+

**Best for:** Aesthetic quality, artistic styles, cinematic images, texture.

**Prompting tips:**
- **Front-load important elements** — first words get highest attention
- Use `--style raw` to reduce Midjourney's aesthetic bias
- Use `--s` (stylize) parameter: 0 = literal, 100 = default, 1000 = maximum artistic
- Use `--ar` for aspect ratio: `--ar 16:9`, `--ar 1:1`, `--ar 9:16`
- Use `--no` for negative prompts: `--no text watermark blur`
- Reference **specific art movements**: "Art Nouveau," "Bauhaus," "De Stijl"
- Use `--chaos` (0-100) for variation: higher = more diverse results

**Prompt structure:**
```
[subject], [environment], [style], [lighting], [camera]
--ar 16:9 --v 6 --style raw --s 50
--no text watermark blur gradient
```

### Stable Diffusion / SDXL / Flux

**Best for:** Full control, ControlNet for composition, inpainting, specific styles via LoRAs.

**Prompting tips:**
- **Prompt weighting** with parentheses: `(important element:1.4)` or `((very important))`
- **Quality boosters**: "masterpiece, best quality, highly detailed, sharp focus"
- Keep prompts under token limit (77 for SD 1.5, much more for SDXL/Flux with T5)
- Use **negative prompts** extensively for quality control
- **ControlNet** for precise composition: Canny edges, depth maps, pose estimation
- **LoRAs** for specific styles, characters, or concepts

**Prompt structure:**
```
Positive: [quality boosters], [subject], [environment], [style], [lighting]
Negative: [everything to avoid]
Steps: 30-50, CFG: 7-9, Sampler: DPM++ 2M Karras
```

### Ideogram 2 / 3

**Best for:** Text-in-image, logos, typography, graphic design.

**Prompting tips:**
- **Lead with style/type**: "Typographic poster," "Logo design," "Infographic"
- **Quote exact text** you want rendered
- Supports **magic prompt** mode for enhanced interpretation
- Excellent at **graphic design** layouts and compositions
- Use **style reference** images for consistency

---

## 14. Prompt Templates by Use Case

### Template: Photorealistic Portrait

```
[Role/occupation] portrait of a [age] [ethnicity] [gender],
[specific physical details and expression].
[Clothing and accessories].
[Setting/environment with specific details].
[Lighting setup]: [key light], [fill], [background].
Shot on [camera/lens], [aperture], [focal length].
[Photography style] style, [color grading].
[Aspect ratio].
No [things to exclude].
```

### Template: Product / Commercial Photography

```
[Product name/type] product photography.
[Product details: material, color, size].
[Surface/setting]: [specific surface material and color].
[Composition]: [angle, distance, arrangement].
[Lighting]: [setup, direction, quality].
[Props/context objects] for lifestyle context.
[Background]: [specific background treatment].
Clean commercial photography, [brand aesthetic].
[Aspect ratio]. [Resolution if needed].
```

### Template: Illustration / Concept Art

```
[Art style] illustration of [subject].
[Scene description with environment].
[Color palette]: [specific colors or mood].
[Artistic references]: [tradition, era, or artist influence].
[Composition]: [arrangement, focal point, visual flow].
[Texture/medium]: [brush style, paper texture, finish].
[Mood/atmosphere]: [emotional tone].
[Aspect ratio].
```

### Template: Structured Diagram (Nano Banana)

```
TASK: [Specific visual to generate].

STYLE: [Design tradition and aesthetic].

LAYOUT: [Exact spatial organization].
[Grid specification if applicable]

COMPONENTS:
- [Element 1]: [exact specifications]
- [Element 2]: [exact specifications]
- [Element 3]: [exact specifications]

CONSTRAINTS:
- [Spacing/alignment rules]
- [Readability requirements]
- [Things to avoid]

SOURCE MATERIAL:
[Content to visualize — paste data, text, or description here]

INTERPRETATION:
[Who reads this and what they should understand at a glance]
```

### Template: Print-Ready Reference Card

> See [IMAGE_GENERATION_GUIDE.md](IMAGE_GENERATION_GUIDE.md) → "Template: Print-Ready Reference Card" for the full template with all 8 constraint techniques.

### Template: Social Media Graphic

```
[Platform] graphic, [dimensions].
[Layout type]: [hero image / split / text-overlay / carousel slide].

CONTENT:
- Headline: "[exact text]"
- Subtext: "[exact text]"
- [Visual element description]

STYLE:
- Brand colors: [hex codes]
- Font style: [bold sans-serif / elegant serif / etc.]
- Mood: [energetic / professional / playful / etc.]

CONSTRAINTS:
- Text must be readable at mobile size
- Safe zone: keep critical content away from edges (10% margin)
- [Platform-specific constraints]
```

### Template: Logo Concept

```
Logo design for [brand name]: "[EXACT TEXT TO RENDER]"

BRAND CONTEXT:
- Industry: [industry]
- Values: [2-3 brand values]
- Target audience: [demographic]

STYLE:
- [Minimalist / Bold / Playful / Luxurious / Technical]
- Mark type: [Wordmark / Lettermark / Icon+wordmark / Abstract / Mascot]
- Color: [Primary color(s) with hex codes]

CONSTRAINTS:
- Must work at 32px (favicon) and 300px+ (hero)
- Must work in single color (black or white)
- No gradients in the mark itself
- Clean, reproducible vector-style output

OUTPUT:
- Logo centered on white background
- Generous padding around the mark
- No background texture or effects
```

---

## 15. Common Failures and Fixes

### Anatomy and Proportion Errors

**Problem:** Extra fingers, distorted hands, impossible poses.

**Fixes:**
- Specify hand positions explicitly: "hands clasped behind back," "right hand holding a coffee cup"
- Add: "anatomically correct proportions, natural hand positions"
- Crop hands out of frame if not critical: "waist-up portrait, hands not visible"
- For Stable Diffusion: use negative prompt "deformed, extra limbs, mutated hands, extra fingers"

### The "AI Look" (Overprocessed, Plastic Skin)

**Problem:** Portraits that look obviously AI-generated.

**Fixes:**
- Add imperfections: "subtle skin texture, visible pores, natural blemishes"
- Reference specific film stocks: "Kodak Portra 400 color science"
- Add grain: "fine film grain, not oversharpened"
- Reduce saturation: "slightly desaturated, natural color palette"
- Specify non-symmetrical framing: "subject slightly off-center, candid composition"

### Generic / Boring Compositions

**Problem:** Subject centered, eye-level, plain background.

**Fixes:**
- Specify composition: "rule of thirds, subject positioned at left intersection"
- Add depth: "foreground element slightly out of focus, middle ground subject sharp, background receding"
- Change angle: "low angle looking up, dramatic perspective"
- Add environment: "contextual setting with specific environmental details"

### Text Rendering Errors

**Problem:** Misspelled, garbled, or missing text.

**Fixes:**
- Quote text exactly and spell it out character by character for critical words
- Use models with good text rendering (Nano Banana Pro, Ideogram)
- Keep text short — fewer words = fewer errors
- Use post-processing to overlay text on a clean image region

### Unwanted Elements Appearing

**Problem:** Watermarks, extra objects, unexpected people, floating UI elements.

**Fixes:**
- Add explicit negatives: "No watermarks, no signatures, no text overlays, no UI elements"
- For Midjourney: `--no watermark text signature border frame`
- Be exhaustive in listing what you don't want
- Simplify the prompt — overly complex prompts can trigger hallucinated elements

### Color Inconsistency

**Problem:** Colors don't match specifications.

**Fixes:**
- Use hex codes: "#2563EB" instead of "blue"
- Provide a color reference: "the exact blue of the Twitter/X logo"
- Use color temperature: "warm palette, nothing cooler than 4000K"
- For brand consistency, list every allowed color and state "no other colors"

### Layout Drift in Structured Outputs

**Problem:** Grid elements merge, reorganize, or disappear.

**Fixes:**
- Enumerate every slot: "BOX 1: [content], BOX 2: [content]..."
- Repeat the grid spec: "EXACTLY 2 rows x 3 columns" in rules AND validation
- Add: "Do NOT combine elements. Do NOT reorganize. Follow assignments exactly."
- Use the constraint redundancy pattern (3 levels)

---

## 16. Quality Checklist

### For All Image Prompts

- [ ] **Subject is specific** — concrete nouns, not abstract concepts
- [ ] **Environment is defined** — not floating in void (unless intended)
- [ ] **Style is referenced** — photography genre, art style, or design tradition
- [ ] **Technical specs included** — aspect ratio, resolution, orientation
- [ ] **Constraints stated** — what NOT to include
- [ ] **Composition directed** — camera angle, framing, focal point
- [ ] **Color controlled** — palette defined or referenced
- [ ] **Tested with target model** — different models need different approaches

### Additional Checks for Structured Outputs

- [ ] **Grid explicitly defined** — exact NxM with equal sizing rules
- [ ] **Content enumerated** — every slot has assigned content
- [ ] **Constraints repeated** at 3+ structural levels
- [ ] **Validation checklist** included at end
- [ ] **"If X, output is incorrect"** language for critical constraints

### Additional Checks for Print Materials

- [ ] **Print terminology used** — "flat print artwork" not "card"
- [ ] **Physical context provided** — real-world usage described
- [ ] **Exact dimensions specified** — inches, pixels, DPI
- [ ] **Background controlled** — solid color or explicit specification
- [ ] **UI triggers avoided** — no rounded corners, no drop shadows, no gradients (unless intended)

---

## Appendix: Prompt Length Guidelines by Model

| Model | Sweet Spot | Max Useful | Notes |
|-------|-----------|------------|-------|
| **Midjourney** | 60-150 words | ~300 words | Front-loads attention |
| **DALL-E 3** | 50-200 words | ~500 words | Rewritten internally |
| **Stable Diffusion 1.5** | 30-77 tokens | 77 tokens | CLIP encoder limit |
| **SDXL / Flux** | 50-200 words | ~500 words | T5 encoder, much more capacity |
| **Nano Banana** | 100-500 words | 32K tokens | Structured Markdown optimal |
| **Nano Banana Pro** | 200-2000 words | 32K tokens | Detailed natural language + structure |
| **Ideogram** | 50-200 words | ~500 words | Text instructions can be longer |

---

## Appendix: Cross-Reference to Repository Resources

| Need | Resource |
|------|----------|
| Print-ready materials (badge buddies, worksheets) | [IMAGE_GENERATION_GUIDE.md](IMAGE_GENERATION_GUIDE.md) |
| Video generation | [VIDEO_GENERATION_GUIDE.md](VIDEO_GENERATION_GUIDE.md) |
| 56 ready-made Nano Banana visualization prompts | [visualizations/](visualizations/) |
| 45 educational worksheet generators | [worksheet-generators/](worksheet-generators/) |
| Branding and visual identity prompts | [branding/](branding/) |
| Healthcare infographic prompts | [healthcare/](healthcare/) |
| Prompt engineering techniques (250 techniques) | [techniques/MASTER_TECHNIQUE_INDEX.md](../techniques/MASTER_TECHNIQUE_INDEX.md) |
| Visual output technique codes (SV family) | SV-11 through SV-18 in Master Index |

---

*Created: 2026-02-26*
*Based on empirical testing across ChatGPT, Midjourney v6, Stable Diffusion XL, Flux, Nano Banana, Nano Banana Pro, and Ideogram 3*
