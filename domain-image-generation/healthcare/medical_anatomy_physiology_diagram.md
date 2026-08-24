---
title: "Labeled Anatomy / Physiology Educational Diagram - Image Generation Prompt"
category: medical-education
description: "Template-driven image generation prompt for creating a labeled anatomy or physiology educational diagram (student/educator use) where the user supplies the structure and all labels from expert-verified sources"
tags:
  - medical
  - anatomy
  - physiology
  - diagram
  - labeled-diagram
  - education
  - image-generation
updated: "2026-06-23"
---

# Labeled Anatomy / Physiology Educational Diagram - Image Generation Prompt

**Purpose:** Generate a clean, flat, labeled anatomy or physiology teaching diagram for students and educators. The diagram renders a structure the user/educator specifies, with labels drawn ONLY from expert-verified source material. The image model does not invent anatomy, labels, or relationships — it lays out and renders supplied content.

**Format:** Single flat print artwork, portrait or landscape, lecture-slide / handout / poster ready (default 2400 x 3000 px portrait at 300 DPI; adjustable).

**See Also:**
- [IMAGE_GENERATION_GUIDE.md](../IMAGE_GENERATION_GUIDE.md) — the 8 core techniques used in this prompt
- [medical_procedure_step_diagram.md](medical_procedure_step_diagram.md) — step-by-step illustrated procedure sequences
- [medical_pathophysiology_mechanism_diagram.md](medical_pathophysiology_mechanism_diagram.md) — disease-mechanism flow diagrams
- [medical_clinical_algorithm_flowchart.md](medical_clinical_algorithm_flowchart.md) — clinical decision / triage flowcharts
- [pacu_infographic_image_prompt.md](pacu_infographic_image_prompt.md) — clinical workflow infographic

---

> ⚠️ **MEDICAL-SAFETY NOTICE — READ BEFORE USE**
> Image models are **NOT anatomically reliable.** They routinely produce plausible-looking but incorrect structures, extra/missing parts, distorted proportions, and mislabeled features. This prompt is a **layout-and-rendering tool**, not a source of anatomical truth. **All structures, labels, and relationships must be supplied by the user from expert-verified sources and must be checked by a subject-matter expert (anatomist, physiologist, clinician, or qualified educator) before any instructional use.** For high-stakes or clinical-grade illustration (textbooks, board materials, patient consent, surgical reference), commission a **professional medical illustrator** — do not ship raw AI output.

---

## Image Generation Prompt (Production-Ready) — TEMPLATE

Replace every `[PLACEHOLDER]` with your own expert-verified content before generating. A worked EXAMPLE follows the template.

```
TASK: Generate a SINGLE FLAT PRINT ARTWORK IMAGE representing a labeled educational anatomy/physiology diagram of [SUBJECT — e.g., "the human heart, anterior view"].

IMPORTANT REAL-WORLD CONTEXT:
This is a teaching diagram for [AUDIENCE — e.g., "first-year nursing students"].
It will be printed in a handout / shown on a lecture slide / posted as a study poster.
It must be readable and clearly labeled.

This is NOT a UI card.
This is NOT a product mockup.
This is NOT a photorealistic render.
This image represents flat, labeled educational line-and-fill artwork.

CONTENT AUTHORITY (CRITICAL):
- Render ONLY the structures and labels listed below.
- Do NOT invent, add, rename, or relocate any anatomical structure or label.
- Do NOT add extra parts, vessels, organs, or text not explicitly listed.
- If a listed structure cannot be drawn faithfully, leave a clearly labeled callout box reading "STRUCTURE PENDING EXPERT VERIFICATION" rather than guessing.

================================================
CRITICAL OUTPUT RULES (NON-NEGOTIABLE)
================================================

- Output EXACTLY ONE IMAGE.
- The image must be a SINGLE flat rectangle.
- Orientation: [PORTRAIT / LANDSCAPE].
- NO rounded outer corners.
- NO drop shadows.
- NO gradients (flat shading only; simple solid fills per region).
- NO photorealistic skin/tissue rendering, NO glossy 3D organ render.
- NO background scene beyond the artwork edges.

If any gradient, shadow, photorealistic render, or unlabeled invented structure appears, the output is incorrect.

================================================
PHYSICAL SIZE & CANVAS
================================================

- Size: [WIDTH] x [HEIGHT] inches (default 8 x 10 portrait)
- Resolution: [PIXELS] at 300 DPI (default 2400 x 3000 px)
- Background: Solid white (#FFFFFF) ONLY. No texture, vignette, or fade.

================================================
DIAGRAM STYLE
================================================

- Style: clean educational illustration / textbook line art with flat color fills.
- Distinct regions filled with flat, muted, high-contrast colors (one solid color per region, no shading gradients).
- Crisp black outlines on all structures.
- Consistent line weight.
- Anatomically neutral, schematic clarity preferred over artistic flourish.

================================================
CENTRAL ILLUSTRATION
================================================

Subject: [SUBJECT and VIEW — e.g., "human heart, anterior (front) external view"]
Orientation/position: [e.g., "upright, apex pointing down-left, as in standard anatomical position"]
Color scheme for regions:
- [REGION 1] = [HEX color]
- [REGION 2] = [HEX color]
- [REGION 3] = [HEX color]
(add as many as needed)

================================================
ENUMERATED LABELS (RENDER EXACTLY THESE — NO MORE, NO LESS)
================================================

Each label = a short straight leader line from the structure to a text label placed in the margin or beside the structure. Labels do NOT overlap the illustration. Use clean sans-serif, high contrast.

LABEL 1: [STRUCTURE NAME] — points to [location description]
LABEL 2: [STRUCTURE NAME] — points to [location description]
LABEL 3: [STRUCTURE NAME] — points to [location description]
LABEL 4: [STRUCTURE NAME] — points to [location description]
LABEL 5: [STRUCTURE NAME] — points to [location description]
[continue for every label — number them all]

DO NOT add any label not in this list.
DO NOT omit any label in this list.

================================================
TITLE & CAPTION
================================================

- Top title band (solid [HEX], white text): "[DIAGRAM TITLE]"
- Optional subtitle (smaller): "[VIEW / SYSTEM / LEVEL]"
- Bottom caption strip (small text): "[OPTIONAL ONE-LINE PHYSIOLOGY NOTE OR SOURCE LINE]"

================================================
TYPOGRAPHY
================================================

- Title: bold, ~24 pt
- Labels: regular, ~12-14 pt, minimum 10 pt
- Clean clinical sans-serif (Roboto, Open Sans, or similar)
- High contrast black/dark text on light backgrounds

================================================
DESIGN SYSTEM (STRICT)
================================================

- Solid fills only, no gradients, no transparency.
- Sharp rectangular corners on the title band, caption strip, and any callout boxes.
- Leader lines: thin solid straight or single-elbow lines, no curves crossing each other.
- Allowed graphic elements: the illustrated structure, leader lines, label text, title/caption bands, optional simple legend.
- Forbidden: photographic backgrounds, 3D depth, glossy organs, decorative scenery, watermark text, invented structures.

================================================
FINAL VALIDATION CHECK
================================================

- One image only
- [Orientation] orientation
- Exactly the listed labels present (count them), none invented, none omitted
- Leader lines clear and non-overlapping
- Flat educational artwork, solid fills only
- No gradients, no shadows, no rounded outer corners
- No photorealistic / 3D organ rendering
- No background scene
- Title and caption present as specified
```

---

## EXAMPLE FILL — REPLACE WITH EXPERT-VERIFIED CONTENT

> The following is an **illustrative example only**, to show the shape of a completed template. **Do not use these labels as authoritative.** Confirm every structure and label against a verified anatomy reference and have a subject-matter expert review before instructional use.

```
TASK: Generate a SINGLE FLAT PRINT ARTWORK IMAGE representing a labeled educational anatomy diagram of the human heart, anterior (external front) view.

AUDIENCE: first-year nursing students. Used as a lecture-slide and printed study handout.

CENTRAL ILLUSTRATION:
Subject: human heart, anterior external view, upright, apex pointing down and to the viewer's right.
Color scheme:
- Right atrium / right ventricle (deoxygenated side) = #BFDBFE (light blue)
- Left atrium / left ventricle (oxygenated side) = #FECACA (light red)
- Great vessels = neutral #E5E7EB with red/blue tint per oxygenation

ENUMERATED LABELS (EXAMPLE — VERIFY):
LABEL 1: Superior vena cava — points to upper-right great vessel
LABEL 2: Aorta (aortic arch) — points to top central arching vessel
LABEL 3: Pulmonary trunk — points to vessel emerging from right ventricle
LABEL 4: Right atrium — points to upper-right chamber
LABEL 5: Right ventricle — points to lower-right chamber
LABEL 6: Left atrium — points to upper-left chamber
LABEL 7: Left ventricle — points to lower-left chamber (apex)
LABEL 8: Inferior vena cava — points to lower-right entering vessel

TITLE: "THE HUMAN HEART — Anterior View"
SUBTITLE: "External chambers and great vessels"
CAPTION: "EXAMPLE — REPLACE WITH EXPERT-VERIFIED CONTENT"

[All CRITICAL OUTPUT RULES, DESIGN SYSTEM, and FINAL VALIDATION CHECK from the template above still apply.]
```

---

## Simplified Prompt (If Full Prompt Misbehaves)

```
Create ONE flat, labeled educational anatomy diagram of [SUBJECT, VIEW].

CRITICAL RULES:
- [Portrait/Landscape], white background, flat textbook line art with solid color fills
- Sharp corners, NO gradients, NO shadows, NO 3D/photorealistic organ render
- This is a FLAT TEACHING DIAGRAM, not a mockup or photo

RENDER ONLY THESE LABELED STRUCTURES (leader line + margin text label, do not invent or omit any):
1. [STRUCTURE] 2. [STRUCTURE] 3. [STRUCTURE] 4. [STRUCTURE] 5. [STRUCTURE]

Title bar: "[TITLE]". Do NOT add any structure or label not listed.
If any invented structure, gradient, or 3D render appears, it is WRONG.
```

---

## Why This Prompt Works

This prompt applies the 8 core techniques from [IMAGE_GENERATION_GUIDE.md](../IMAGE_GENERATION_GUIDE.md):

1. **Terminology Steering** — "flat print artwork" / "educational line-and-fill artwork" instead of "render," avoiding glossy 3D-organ tropes.
2. **Grid Forcing + Enumerated Slots** — the **enumerated LABEL 1…N list** is the diagram equivalent of numbered slots; it locks exactly which structures appear and prevents invented anatomy.
3. **Constraint Redundancy** — "no invented structures," "no gradients," and "no 3D render" appear in the content-authority block, design system, and final validation check.
4. **Negative Space Control** — solid white background, no scene, no depth.
5. **Allowed vs. Forbidden Distinction** — explicitly allows the illustration + leader lines + labels + bands; forbids photographic backgrounds, glossy organs, and invented text.
6. **Physical Context Anchoring** — "lecture slide / handout / study poster for [audience]" constrains density and readability.
7. **Deliverables Locking** — EXACTLY ONE IMAGE, locked orientation and dimensions.
8. **Validation Checklist** — final self-audit including a label-count check.

---

## Anti-Fabrication / Expert-Review Section

**Why this matters most for anatomy:** Image models hallucinate structures with high visual confidence. An AI heart may have the wrong number of vessels, a mirrored layout, or labels pointing to the wrong chamber — and it will look polished. Polish is not accuracy.

**Rules enforced by this prompt:**
- The model renders **only** the enumerated labels; it must not add or rename structures.
- Unrenderable structures become a flagged placeholder, never a guess.
- No photorealistic rendering (which masks anatomical errors as "detail").

**Required workflow:**
1. Source every structure and label from a verified anatomy/physiology reference (textbook, atlas, vetted curriculum).
2. Fill the template; mark any uncertain item explicitly.
3. Generate.
4. **Expert review (mandatory):** an anatomist, physiologist, clinician, or qualified educator verifies that every structure, proportion, spatial relationship, and label is correct.
5. For textbooks, board prep, patient-facing, or any clinical-grade use, route to a **professional medical illustrator** instead of shipping AI output.

**Verification Checklist (complete before instructional use):**
- [ ] Every label was sourced from an expert-verified reference (not the model)
- [ ] Exactly the listed labels appear; none invented, none omitted
- [ ] Each leader line points to the correct structure
- [ ] Proportions and spatial relationships are anatomically plausible and correct
- [ ] No extra/duplicate/mirrored structures were introduced
- [ ] Orientation/view matches the intended teaching point
- [ ] **Anatomy, labels, and relationships verified by a subject-matter expert before instructional use**
- [ ] For high-stakes/clinical-grade use: professional medical illustrator engaged

---

## Model-Specific Notes

For labeled diagrams, **text-label accuracy is the single biggest model differentiator.** Lead with the models that render in-image text reliably.

### gpt-image-2 (OpenAI, flagship) — RECOMMENDED for labeled diagrams
- Set `quality="high"` for crisp leader-line labels and titles.
- Map the template onto the 5-section structure (Scene / Subject / Key Details / Use Case / Constraints): put the enumerated labels under Key Details and the print/anti-fabrication block under Constraints.
- Best-in-class at rendering many short text labels without garbling — ideal when the diagram has 8–15 labels.
- Do NOT pass `input_fidelity` (disabled). See [GPT_IMAGE_2_GUIDE.md](../GPT_IMAGE_2_GUIDE.md).

### Nano Banana Pro (gemini-3-pro-image) — RECOMMENDED for labeled diagrams
- Near-perfect text rendering; name exact fonts/weights for label consistency.
- Use a **system prompt** to lock the "flat textbook line art, no invented structures, no 3D render" constraints across regenerations.
- **Search grounding** can help with factual layout — but it does not replace expert review; treat grounded output as a draft, not a source.
- Markdown-structured prompts (the template above) parse natively.

### DALL-E 3 (legacy)
Add: `"Educational anatomy diagram, textbook illustration style, flat color regions, clear leader-line labels, no 3D, no photorealism, white background"`. Weaker at rendering many distinct labels accurately — verify every label.

### Midjourney (legacy)
```
flat educational anatomy diagram, [SUBJECT] [VIEW], textbook line art, flat color fills,
clear labels with leader lines, white background,
--ar 4:5 --v 6 --style raw --s 25
--no 3d render photorealistic gloss shadow gradient rounded corners scenery
```
Note: Midjourney frequently garbles in-image text — best for the illustration, with labels added afterward in a layout tool.

### Stable Diffusion (legacy)
Negative prompt: `"photograph, 3d render, glossy organ, realistic tissue, blurry, gradient, shadow, rounded corners, scenery, watermark, garbled text, extra organs"`. Generally poor at accurate in-image labels — expect to add labels manually.

---

## Troubleshooting

### Problem: Model invents extra structures or vessels
**Add:** `"Render ONLY the listed structures. Any structure not in the LABEL list is a rendering error. Do not add vessels, parts, or text."`

### Problem: Labels are garbled or misspelled
**Switch model** to gpt-image-2 or Nano Banana Pro, or generate the unlabeled illustration and add labels in a layout tool. Also: `"Spell every label EXACTLY as written. Each label is a separate text element."`

### Problem: Glossy 3D / photorealistic organ
**Add:** `"Flat textbook line art with solid color fills ONLY. NOT a 3D render. NOT photorealistic. Crisp black outlines, flat shading."`

### Problem: Leader lines cross / labels overlap the illustration
**Add:** `"Place all text labels in the margins. Leader lines must not cross each other. No label overlaps the illustration."`

### Problem: Wrong view or mirrored layout
**Add:** `"Orientation: [explicit view]. The [named structure] must be on the [left/right]. A mirrored layout is incorrect."` Then verify with an expert.

---

*Updated: 2026-06-23 — Template-driven; anatomical accuracy requires expert verification (image models are not anatomically reliable).*
