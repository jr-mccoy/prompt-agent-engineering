# Image to Children's Coloring Book Page

**Source:** Prompting Guides Repository

**Category:** Image Generation / Coloring Book

## Prompt

```
TASK: Transform the uploaded image into a CHILDREN'S COLORING BOOK PAGE.

================================================
WHAT THIS IS (PHYSICAL CONTEXT)
================================================

This is a COLORING BOOK PAGE for children ages 4-10.
It will be PRINTED on paper.
Children will COLOR IT IN with crayons, markers, or colored pencils.

This is NOT a finished illustration.
This is NOT a grayscale version.
This is NOT a sketch or draft.
This is PURE LINE ART ready for a child to color.

================================================
CRITICAL OUTPUT RULES (NON-NEGOTIABLE)
================================================

OUTPUT FORMAT:
- EXACTLY ONE IMAGE
- Black line art on pure white background
- Print-ready coloring page

LINE ART REQUIREMENTS:
- BLACK OUTLINES ONLY (#000000)
- NO filled areas - all interior spaces must be WHITE
- NO shading, hatching, or crosshatching
- NO gradients of any kind
- NO gray tones - pure black lines only
- NO colored elements whatsoever

If any shading, gray areas, or filled regions appear, the output is INCORRECT.

OUTLINE SPECIFICATIONS:
- Line weight: BOLD (thick enough for children to stay inside)
- Minimum line thickness: 2-3 points
- All shapes must have CLOSED outlines (no gaps)
- Clean, smooth lines (not sketchy or rough)

BACKGROUND:
- Pure white (#FFFFFF) ONLY
- No texture
- No patterns
- No border decorations unless simple

================================================
SIMPLIFICATION RULES
================================================

Transform the source image by:

1. SIMPLIFY complex details into child-friendly shapes
   - Reduce fine textures to simple patterns or remove entirely
   - Convert realistic features to cartoon-friendly versions
   - Remove unnecessary background clutter

2. CREATE CLEAR COLORABLE REGIONS
   - Each area should be large enough for a child to color
   - Minimum region size: approximately 0.5 inch when printed
   - Distinct, well-separated shapes

3. MAINTAIN RECOGNIZABILITY
   - Keep the main subject clearly identifiable
   - Preserve key features that make the subject recognizable
   - Simplify but do not distort beyond recognition

4. AGE-APPROPRIATE CONTENT
   - Friendly, approachable appearance
   - No scary, violent, or inappropriate elements
   - Suitable for children ages 4-10

================================================
WHAT TO PRESERVE FROM SOURCE IMAGE
================================================

- Main subject(s) and their basic form
- Key identifying features
- Overall composition and layout
- Relative proportions (simplified)

================================================
WHAT TO REMOVE/CHANGE FROM SOURCE IMAGE
================================================

- All color information (convert to outlines only)
- Complex textures (simplify to patterns or remove)
- Realistic shading (remove entirely)
- Fine details (simplify or omit)
- Busy backgrounds (simplify dramatically)
- Photorealistic rendering (convert to line art)

================================================
DESIGN CONSTRAINTS (REPEATED FOR EMPHASIS)
================================================

MANDATORY:
- Black outlines only
- White interior spaces only
- Bold, clean lines
- Closed shapes
- Child-appropriate simplification

FORBIDDEN:
- Any filled/colored areas
- Any gray tones or shading
- Any gradients
- Thin, delicate lines
- Open/broken outlines
- Overly complex details
- Scary or inappropriate content

================================================
OUTPUT SPECIFICATIONS
================================================

DIMENSIONS:
- Standard coloring page: 8.5 x 11 inches (letter size)
- Resolution: 300 DPI minimum
- Orientation: Match source image (portrait or landscape)

MARGINS:
- Safe zone: 0.5 inch margin from all edges
- Main content centered within safe zone

================================================
FINAL VALIDATION CHECK
================================================

Before finalizing, verify:

- [ ] Pure black lines only (no gray, no color)
- [ ] All interior areas are pure white (ready to color)
- [ ] NO shading, gradients, or filled regions
- [ ] Lines are bold enough for children
- [ ] All shapes have closed outlines
- [ ] Subject is clearly recognizable
- [ ] Content is age-appropriate
- [ ] Details are simplified for coloring
- [ ] Colorable regions are large enough
- [ ] Background is clean/simplified

If ANY shading, filled area, or gray tone appears, the output is INCORRECT.
If ANY line is too thin for a child to color within, the output is INCORRECT.

================================================
PROCESS THE UPLOADED IMAGE NOW
================================================

Transform the uploaded image following all rules above.
Output: A single black-and-white line art coloring page.
```

## Usage Notes

- **Purpose:** Convert any uploaded image (photo, illustration, artwork) into a printable children's coloring book page
- **Input:** User uploads an image
- **Output:** Black line art on white background, ready for printing and coloring
- **Target Audience:** Children ages 4-10
- **Print Size:** 8.5 x 11 inches at 300 DPI

## Techniques Used

| Technique | Application |
|-----------|-------------|
| Terminology Steering | "coloring book page", "line art", "print-ready" instead of "convert" or "filter" |
| Constraint Redundancy | "NO shading" repeated in 3+ sections |
| Negative Space Control | Pure white background, no texture/patterns |
| Physical Context Anchoring | Explicit description of how children will use it |
| Deliverables Locking | Exact dimensions, DPI, single image output |
| Allowed vs Forbidden | Clear lists of what to include/exclude |
| Validation Checklist | Final verification block |

## Model-Specific Notes

### gpt-image-2 (OpenAI, primary)
Current OpenAI flagship image model. Set `quality="high"` so the converted line art keeps crisp, closed outlines. Put the line-art rules under a CONSTRAINTS block. Do NOT pass `input_fidelity` (disabled in gpt-image-2). The "if X appears, the output is INCORRECT" phrasing is reliable here.

### Nano Banana (Google Gemini, primary)
Current Google image family — `gemini-3-pro-image` (Nano Banana Pro) and `gemini-3.1-flash-image` (Nano Banana 2). Use Markdown structure and ALL-CAPS `MUST`/`NEVER`; specify `#000000` lines on `#FFFFFF`. Nano Banana Pro's realism bias can sneak in shading — add "flat line art only, NO rendering, NO depth." Iterate conversationally ("remove all gray shading, keep every region white") rather than regenerating.

### DALL-E 3 / ChatGPT (legacy)
Add to prompt if needed: `"Coloring book style, line art, black outlines, no shading, children's activity page"`

### Midjourney (legacy)
```
[prompt content] --ar 8.5:11 --v 6 --style raw --s 25
--no shading gradient gray color fill texture realistic
```
The `--no color shading` flag is the key lever for clean line art in Midjourney.

### Stable Diffusion (legacy)
Use a **lineart ControlNet** for the cleanest closed outlines.
Positive: `"coloring book page, line art, black outlines, white background, simple, bold lines, children's coloring page"`
Negative: `"shading, gradient, gray, color, filled, realistic, detailed, texture, complex"`

## Variations

### Simpler Version (Ages 2-4)
Add to SIMPLIFICATION RULES:
```
- Maximum of 10-15 distinct colorable regions
- Extra-bold outlines (3-4 point minimum)
- Very simple shapes only
- No small details
```

### More Detailed Version (Ages 8-12)
Add to SIMPLIFICATION RULES:
```
- Allow moderate detail
- Line weight can be slightly finer (1.5-2 points)
- More colorable regions permitted
- Can include simple patterns within shapes
```
