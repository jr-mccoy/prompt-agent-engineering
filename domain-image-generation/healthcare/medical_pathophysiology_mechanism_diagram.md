---
title: "Pathophysiology / Disease-Mechanism Flow Diagram - Image Generation Prompt"
category: medical-education
description: "Template-driven image generation prompt for creating a disease-mechanism flow diagram (cause -> mechanism -> effect) where the user supplies every node and causal link from expert-verified sources"
tags:
  - medical
  - pathophysiology
  - mechanism
  - diagram
  - flow-diagram
  - disease-mechanism
  - education
  - image-generation
updated: "2026-06-23"
---

# Pathophysiology / Disease-Mechanism Flow Diagram - Image Generation Prompt

**Purpose:** Generate a clean, flat, directional flow diagram of a disease mechanism — a chain from **cause/trigger → mechanism/intermediate steps → clinical effect/signs** — for students and educators. Every node, label, and causal arrow comes ONLY from expert-verified source material. The image model lays out and renders the supplied chain; it does not invent mechanisms, intermediate steps, or causal links.

**Format:** Single flat print artwork, directional node-and-arrow flow (top-to-bottom or left-to-right), lecture-slide / handout / study-poster ready (default 2400 x 3000 px portrait at 300 DPI; adjustable).

**See Also:**
- [IMAGE_GENERATION_GUIDE.md](../IMAGE_GENERATION_GUIDE.md) — the 8 core techniques used in this prompt
- [medical_anatomy_physiology_diagram.md](medical_anatomy_physiology_diagram.md) — labeled anatomy/physiology diagrams
- [medical_procedure_step_diagram.md](medical_procedure_step_diagram.md) — step-by-step illustrated procedures
- [medical_clinical_algorithm_flowchart.md](medical_clinical_algorithm_flowchart.md) — clinical decision / triage flowcharts
- [pacu_infographic_image_prompt.md](pacu_infographic_image_prompt.md) — clinical workflow infographic

---

> ⚠️ **MEDICAL-SAFETY NOTICE — READ BEFORE USE**
> Image models are **NOT reliable about disease mechanisms.** They invent intermediate steps, draw causal arrows that do not exist, oversimplify or reverse relationships, and mislabel nodes — all while looking authoritative. This prompt is a **layout-and-rendering tool**, not a source of pathophysiology truth. **Every node, label, and causal link must be supplied by the user from expert-verified sources (current textbook, review article, vetted curriculum) and must be checked by a subject-matter expert (clinician, pathophysiologist, qualified educator) before any instructional use.** For high-stakes or publication-grade illustration, commission a **professional medical illustrator** and validate the mechanism against the literature.

---

## Image Generation Prompt (Production-Ready) — TEMPLATE

Replace every `[PLACEHOLDER]` with your own expert-verified content before generating. A worked EXAMPLE follows the template.

```
TASK: Generate a SINGLE FLAT PRINT ARTWORK IMAGE representing a pathophysiology flow diagram of [DISEASE/PROCESS — e.g., "the development of type 2 diabetes hyperglycemia"].

IMPORTANT REAL-WORLD CONTEXT:
This is a teaching flow diagram for [AUDIENCE — e.g., "second-year medical students"].
It is shown on a lecture slide / printed as a handout or study poster.
It must show a clear directional causal chain: cause -> mechanism -> effect.

This is NOT a UI card.
This is NOT a product mockup.
This is NOT a photorealistic render.
This image represents a flat, labeled node-and-arrow flow diagram.

CONTENT AUTHORITY (CRITICAL):
- Render ONLY the nodes and the causal arrows listed below.
- Do NOT invent, add, rename, reroute, or omit any node or causal link.
- Do NOT add mechanisms, mediators, or effects not explicitly listed.
- Do NOT change the direction of any arrow.
- If a node or link cannot be rendered faithfully, draw a node reading "STEP PENDING EXPERT VERIFICATION" rather than guessing.

================================================
CRITICAL OUTPUT RULES (NON-NEGOTIABLE)
================================================

- Output EXACTLY ONE IMAGE.
- The image must be a SINGLE flat rectangle.
- Orientation: [PORTRAIT / LANDSCAPE].
- NO rounded outer corners (node boxes use sharp 90-degree corners only).
- NO drop shadows.
- NO gradients (flat color fills only).
- NO photorealistic anatomy/cell/organ rendering.
- NO background scene beyond the artwork edges.

If any gradient, shadow, photorealistic render, invented node, or reversed/added arrow appears, the output is incorrect.

================================================
PHYSICAL SIZE & CANVAS
================================================

- Size: [WIDTH] x [HEIGHT] inches (default 8 x 10 portrait)
- Resolution: [PIXELS] at 300 DPI (default 2400 x 3000 px)
- Background: Solid white (#FFFFFF) ONLY. No texture, vignette, or fade.

================================================
FLOW LAYOUT (MOST IMPORTANT)
================================================

- Direction: [TOP-TO-BOTTOM / LEFT-TO-RIGHT].
- Each node = a sharp-cornered rectangular box with verbatim label text inside.
- Color-code by stage (solid fills, no gradients):
  - CAUSE / TRIGGER nodes = [HEX, e.g., #FEE2E2 light red]
  - MECHANISM / INTERMEDIATE nodes = [HEX, e.g., #FEF3C7 light amber]
  - EFFECT / CLINICAL SIGN nodes = [HEX, e.g., #DBEAFE light blue]
- Connect nodes with solid directional arrows (single triangle head) ONLY along the listed links.
- Optional small "+" or "−" arrow labels ONLY if specified (increase/decrease).
- Branching/converging arrows allowed ONLY where the link list specifies them.

================================================
ENUMERATED NODES (RENDER EXACTLY THESE — NO MORE, NO LESS)
================================================

NODE 1 [CAUSE]: [verbatim label]
NODE 2 [MECHANISM]: [verbatim label]
NODE 3 [MECHANISM]: [verbatim label]
NODE 4 [MECHANISM]: [verbatim label]
NODE 5 [EFFECT]: [verbatim label]
NODE 6 [EFFECT]: [verbatim label]
[continue for every node — number and stage-tag them all]

================================================
ENUMERATED CAUSAL LINKS (DRAW EXACTLY THESE ARROWS — NO MORE, NO LESS)
================================================

LINK A: NODE 1 -> NODE 2   [optional label: "leads to" / "+" / "−"]
LINK B: NODE 2 -> NODE 3
LINK C: NODE 3 -> NODE 4
LINK D: NODE 4 -> NODE 5
LINK E: NODE 4 -> NODE 6
[continue for every link — list every arrow explicitly with its direction]

DO NOT add arrows not listed. DO NOT reverse any arrow. DO NOT add nodes not listed.

================================================
TITLE & LEGEND
================================================

- Top title band (solid [HEX], white text): "[DISEASE/PROCESS] — Pathophysiology"
- Optional legend (small): CAUSE = [color], MECHANISM = [color], EFFECT = [color]
- Optional bottom caption (small text): "[ONE-LINE SUMMARY OR SOURCE LINE]"

================================================
TYPOGRAPHY
================================================

- Title: bold, ~22 pt
- Node labels: regular/semibold, ~12-14 pt, minimum 10 pt
- Arrow labels: ~10 pt
- Clean clinical sans-serif (Roboto, Open Sans, or similar)
- High contrast dark text on light node fills

================================================
DESIGN SYSTEM (STRICT)
================================================

- Solid fills only, no gradients, no transparency.
- Sharp 90-degree corners on all node boxes, bands, and legend.
- Arrows: solid lines with a single clear triangular head; consistent weight; minimal crossing.
- Allowed graphic elements: node boxes, directional arrows, arrow labels, title/legend/caption bands.
- Forbidden: photorealistic cells/organs, 3D depth, glossy effects, decorative scenery, watermark text, invented nodes/arrows, reversed arrows.

================================================
FINAL VALIDATION CHECK
================================================

- One image only
- [Orientation] orientation, flow runs [direction]
- Exactly the listed nodes present (count them); none invented, none omitted
- Exactly the listed arrows present, all in the correct direction; none added, none reversed
- Stage color-coding applied correctly (cause/mechanism/effect)
- Flat node-and-arrow artwork, solid fills only
- No gradients, no shadows, no rounded outer corners
- No photorealistic rendering
- Title (and legend if specified) present
```

---

## EXAMPLE FILL — REPLACE WITH EXPERT-VERIFIED CONTENT

> The following is an **illustrative, intentionally simplified example only**, to show the shape of a completed template. **Do not treat it as an authoritative or complete mechanism.** Confirm every node, link, and arrow direction against a verified reference and have a subject-matter expert review before instructional use.

```
TASK: Generate a SINGLE FLAT PRINT ARTWORK IMAGE representing a pathophysiology flow diagram of left-sided heart failure leading to pulmonary congestion (simplified teaching version).

AUDIENCE: nursing students. Lecture slide + handout. Direction: top-to-bottom.

ENUMERATED NODES (EXAMPLE — VERIFY):
NODE 1 [CAUSE]: Decreased left ventricular contractility
NODE 2 [MECHANISM]: Reduced left ventricular stroke volume
NODE 3 [MECHANISM]: Increased left atrial pressure
NODE 4 [MECHANISM]: Increased pulmonary venous / capillary pressure
NODE 5 [EFFECT]: Fluid leaks into alveoli (pulmonary edema)
NODE 6 [EFFECT]: Dyspnea and crackles

ENUMERATED LINKS (EXAMPLE — VERIFY):
LINK A: NODE 1 -> NODE 2
LINK B: NODE 2 -> NODE 3
LINK C: NODE 3 -> NODE 4
LINK D: NODE 4 -> NODE 5
LINK E: NODE 5 -> NODE 6

TITLE: "LEFT-SIDED HEART FAILURE — Pathophysiology (Simplified)"
CAPTION: "EXAMPLE — REPLACE WITH EXPERT-VERIFIED CONTENT"

[All CRITICAL OUTPUT RULES, DESIGN SYSTEM, and FINAL VALIDATION CHECK from the template above still apply.]
```

---

## Simplified Prompt (If Full Prompt Misbehaves)

```
Create ONE flat pathophysiology flow diagram for [DISEASE/PROCESS], flowing [top-to-bottom / left-to-right].

CRITICAL RULES:
- White background, sharp-cornered node boxes, solid directional arrows
- Color stages: CAUSE=light red, MECHANISM=light amber, EFFECT=light blue
- Sharp corners, NO gradients, NO shadows, NO photorealism
- This is a FLAT NODE-AND-ARROW DIAGRAM, not a mockup or photo

RENDER ONLY THESE NODES (verbatim, do not invent or omit):
1.[CAUSE] ... 2.[MECH] ... 3.[MECH] ... 4.[EFFECT] ...

DRAW ONLY THESE ARROWS (exact direction, do not reverse or add):
1->2, 2->3, 3->4

Title bar: "[DISEASE] — Pathophysiology".
If any node/arrow is invented, reversed, or omitted, it is WRONG.
```

---

## Why This Prompt Works

This prompt applies the 8 core techniques from [IMAGE_GENERATION_GUIDE.md](../IMAGE_GENERATION_GUIDE.md):

1. **Terminology Steering** — "flat node-and-arrow flow diagram" instead of "render," steering away from photorealistic cell/organ art.
2. **Grid Forcing + Enumerated Slots** — the **enumerated NODE list and separate LINK list** are the flow-diagram equivalent of numbered slots; they lock exactly which nodes exist and exactly which arrows connect them, preventing invented mechanisms or reversed causality.
3. **Constraint Redundancy** — "no invented nodes/arrows," "no reversed arrows," and "no gradients" repeat across content-authority, design system, and validation check.
4. **Negative Space Control** — solid white background, no scene, no depth.
5. **Allowed vs. Forbidden Distinction** — allows node boxes, directional arrows, labels, bands; forbids photoreal cells/organs and any unlisted/reversed arrow.
6. **Physical Context Anchoring** — "lecture slide / handout / study poster for [audience]" sets density and flow direction.
7. **Deliverables Locking** — EXACTLY ONE IMAGE, locked orientation/dimensions and flow direction.
8. **Validation Checklist** — final self-audit including node-count and arrow-direction checks.

---

## Anti-Fabrication / Expert-Review Section

**Why this matters most for mechanisms:** The whole value of a pathophysiology diagram is the *causal structure* — which step causes which, and in which direction. Image models are especially prone to inventing plausible intermediate steps, adding spurious arrows, and reversing cause and effect, producing a diagram that teaches the wrong mechanism while looking correct.

**Rules enforced by this prompt:**
- The model draws **only** the enumerated nodes and **only** the enumerated arrows, in the **specified direction**.
- No invented mediators, no added/removed/reversed links.
- Unrenderable items become a flagged placeholder, never a guess.
- No photorealism (which can make an invented mechanism look authoritative).

**Required workflow:**
1. Source every node, link, and arrow direction from a verified reference (current textbook, review, vetted curriculum).
2. Fill both the NODE list and the LINK list; mark any uncertain item explicitly.
3. Generate.
4. **Expert review (mandatory):** a clinician/pathophysiologist/qualified educator verifies every node label, every causal link, every arrow direction, and that no step was invented, omitted, or reversed — and that the simplification level is appropriate (not misleading).
5. For publication-grade or board-prep use, route to a **professional medical illustrator** and validate against the literature.

**Verification Checklist (complete before instructional use):**
- [ ] Every node and link was sourced from an expert-verified reference (not the model)
- [ ] Exactly the listed nodes appear; none invented, none omitted
- [ ] Exactly the listed arrows appear, each in the correct direction; none added, none reversed
- [ ] No spurious intermediate step or mediator introduced
- [ ] Cause/mechanism/effect staging (and color-coding) is correct
- [ ] Any simplification is faithful and not misleading
- [ ] Node labels match the source text verbatim
- [ ] **Nodes, links, and arrow directions verified by a subject-matter expert before instructional use**
- [ ] For high-stakes/publication-grade use: professional medical illustrator engaged

---

## Model-Specific Notes

For mechanism diagrams, **accurate in-node text plus correct arrow direction are the key model differentiators.** Lead with the models strongest at in-image text and structured flow.

### gpt-image-2 (OpenAI, flagship) — RECOMMENDED for mechanism diagrams
- Set `quality="high"` for legible node labels and clean arrowheads.
- Map to the 5-section structure (Scene / Subject / Key Details / Use Case / Constraints): NODE list + LINK list under Key Details; print/anti-fabrication block under Constraints.
- Strong at multi-box layouts with distinct text — well suited to 6–12 node chains.
- Do NOT pass `input_fidelity` (disabled). See [GPT_IMAGE_2_GUIDE.md](../GPT_IMAGE_2_GUIDE.md).

### Nano Banana Pro (gemini-3-pro-image) — RECOMMENDED for mechanism diagrams
- Near-perfect text rendering; name exact fonts/weights for node-label consistency.
- Use a **system prompt** to lock "flat node-and-arrow, only listed nodes/arrows, no reversed arrows, no photorealism" across regenerations.
- **Search grounding** may help with mechanism accuracy — but treat grounded output as a draft for expert review, never as a verified source.
- Markdown-structured prompts (NODE/LINK lists) parse natively.

### DALL-E 3 (legacy)
Add: `"Flat pathophysiology flow chart, labeled boxes connected by directional arrows, color-coded stages, schematic, no photorealism, white background"`. Often miscounts boxes/arrows and may reroute flow — verify node count and every arrow direction.

### Midjourney (legacy)
```
flat pathophysiology flow diagram, [DISEASE], labeled boxes, directional arrows, color-coded stages,
schematic, white background,
--ar 4:5 --v 6 --style raw --s 25
--no photorealistic 3d cells organs gloss shadow gradient rounded corners scenery
```
Note: Midjourney garbles in-image text and rarely respects exact node/arrow structure — best for visual styling, with the actual chain assembled in a diagramming tool.

### Stable Diffusion (legacy)
Negative prompt: `"photograph, 3d render, realistic cells, organs, blurry, gradient, shadow, rounded corners, scenery, watermark, garbled text, extra arrows, reversed arrows"`. Poor at exact flow structure — expect to build the chain manually.

---

## Troubleshooting

### Problem: Model invents intermediate steps or extra arrows
**Add:** `"Draw ONLY the nodes in the NODE list and ONLY the arrows in the LINK list. Any extra node or arrow is a rendering error."`

### Problem: Arrows point the wrong way / cause and effect reversed
**Add:** `"Arrow directions are fixed: [restate each LINK]. Do not reverse any arrow. A reversed arrow is incorrect."`

### Problem: Node labels garbled
**Switch model** to gpt-image-2 or Nano Banana Pro, or add labels in a diagramming tool. Also: `"Each node label must read EXACTLY as written."`

### Problem: Photorealistic cells/organs appear inside nodes
**Add:** `"Nodes are plain color-filled boxes with text only. No illustrations inside nodes. No photorealistic cells or organs anywhere."`

### Problem: Stages not color-coded
**Add:** `"Color each node by its stage tag: CAUSE=[hex], MECHANISM=[hex], EFFECT=[hex]. Solid fills only."`

---

*Updated: 2026-06-23 — Template-driven; nodes, causal links, and arrow directions require expert verification (image models are not mechanistically reliable).*
