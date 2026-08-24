---
title: "Clinical Decision Algorithm / Triage Flowchart - Image Generation Prompt"
category: medical-education
description: "Template-driven image generation prompt for creating a clinical decision algorithm or triage flowchart with decision nodes and yes/no branches, where the user supplies every node, criterion, and branch from expert-verified sources"
tags:
  - medical
  - clinical-algorithm
  - flowchart
  - triage
  - decision-tree
  - diagram
  - education
  - image-generation
updated: "2026-06-23"
---

# Clinical Decision Algorithm / Triage Flowchart - Image Generation Prompt

**Purpose:** Generate a clean, flat clinical decision algorithm or triage flowchart — start node → decision diamonds with yes/no (or branch) outcomes → action/terminal nodes — for educators and clinical reference. Every node, decision criterion, branch label, and connection comes ONLY from expert-verified source material (published algorithm, institutional protocol, current guideline). The image model lays out and renders the supplied logic; it does not invent decision criteria, thresholds, branches, or actions.

**Format:** Single flat print artwork, top-to-bottom decision flow, lecture-slide / protocol-poster / pocket-reference ready (default 2400 x 3000 px portrait at 300 DPI; adjustable).

**See Also:**
- [IMAGE_GENERATION_GUIDE.md](../IMAGE_GENERATION_GUIDE.md) — the 8 core techniques used in this prompt
- [medical_anatomy_physiology_diagram.md](medical_anatomy_physiology_diagram.md) — labeled anatomy/physiology diagrams
- [medical_procedure_step_diagram.md](medical_procedure_step_diagram.md) — step-by-step illustrated procedures
- [medical_pathophysiology_mechanism_diagram.md](medical_pathophysiology_mechanism_diagram.md) — disease-mechanism flow diagrams
- [pacu_infographic_image_prompt.md](pacu_infographic_image_prompt.md) — clinical workflow infographic

---

> ⚠️ **MEDICAL-SAFETY NOTICE — READ BEFORE USE**
> Image models are **NOT reliable about clinical decision logic.** They invent thresholds, alter criteria, drop branches, misroute yes/no paths, and fabricate actions — producing an authoritative-looking flowchart that encodes unsafe logic. This prompt is a **layout-and-rendering tool**, not a source of clinical-decision truth. **Every node, criterion, threshold, branch label, and action must be supplied by the user from expert-verified sources (published algorithm, current guideline, institutional protocol) and must be checked by a subject-matter expert (clinician, the protocol owner, or qualified educator) before any instructional or clinical-reference use.** Numbers and thresholds are especially high-risk — verify each one. For clinical deployment, validate against the governing protocol and consider a **professional medical illustrator** for publication-grade output. This diagram is an educational/reference aid, not a substitute for clinical judgment.

---

## Image Generation Prompt (Production-Ready) — TEMPLATE

Replace every `[PLACEHOLDER]` with your own expert-verified content before generating. A worked EXAMPLE follows the template.

```
TASK: Generate a SINGLE FLAT PRINT ARTWORK IMAGE representing a clinical decision algorithm / triage flowchart for [CLINICAL QUESTION — e.g., "initial triage of suspected sepsis"].

IMPORTANT REAL-WORLD CONTEXT:
This is a clinical decision reference for [AUDIENCE — e.g., "ED triage nurses / medical students"].
It is shown on a slide / printed as a protocol poster or pocket reference.
It must show clear decision points with explicit yes/no (or labeled) branches.

This is NOT a UI card.
This is NOT a product mockup.
This is NOT a photorealistic render.
This image represents a flat, labeled flowchart (boxes, diamonds, arrows).

CONTENT AUTHORITY (CRITICAL):
- Render ONLY the nodes, decision criteria, branch labels, and connections listed below.
- Do NOT invent, add, rename, reroute, or omit any node, criterion, threshold, branch, or action.
- Do NOT change any numeric threshold or cutoff.
- Do NOT add clinical advice, drugs, doses, or actions not explicitly listed.
- If a node or branch cannot be rendered faithfully, draw it reading "CRITERION PENDING EXPERT VERIFICATION" rather than guessing.

================================================
CRITICAL OUTPUT RULES (NON-NEGOTIABLE)
================================================

- Output EXACTLY ONE IMAGE.
- The image must be a SINGLE flat rectangle.
- Orientation: [PORTRAIT / LANDSCAPE].
- NO rounded outer corners (process boxes use sharp 90-degree corners; decision diamonds are the only non-rectangular shape).
- NO drop shadows.
- NO gradients (flat color fills only).
- NO photorealistic rendering.
- NO background scene beyond the artwork edges.

If any gradient, shadow, photorealistic render, invented criterion, altered threshold, or misrouted branch appears, the output is incorrect.

================================================
PHYSICAL SIZE & CANVAS
================================================

- Size: [WIDTH] x [HEIGHT] inches (default 8 x 10 portrait)
- Resolution: [PIXELS] at 300 DPI (default 2400 x 3000 px)
- Background: Solid white (#FFFFFF) ONLY. No texture, vignette, or fade.

================================================
FLOWCHART SHAPE CONVENTIONS (STRICT)
================================================

- START / END node = sharp-cornered rectangle (or pill if specified), fill [HEX].
- PROCESS / ACTION node = sharp-cornered rectangle, fill [HEX, e.g., #DBEAFE light blue].
- DECISION node = DIAMOND, fill [HEX, e.g., #FEF3C7 light amber], containing a yes/no question.
- TERMINAL / DISPOSITION node = sharp-cornered rectangle, fill by urgency:
  - Emergent/escalate = [HEX, e.g., #FEE2E2 light red] with thick red border.
  - Routine = [HEX, e.g., #DCFCE7 light green].
- Connect with solid directional arrows (single triangle head).
- Each decision diamond MUST have its branches LABELED ("YES" / "NO" or the specified labels) next to the outgoing arrows.

================================================
FLOW LAYOUT
================================================

- Direction: TOP-TO-BOTTOM (with left/right branches off decision diamonds).
- One entry (START) node at top.
- Decisions arranged so YES and NO paths are visually distinct and clearly labeled.
- Arrows do not cross ambiguously; label every branch.

================================================
ENUMERATED NODES (RENDER EXACTLY THESE — NO MORE, NO LESS)
================================================

NODE 1 [START]: [verbatim text]
NODE 2 [DECISION]: [verbatim yes/no question, including any exact threshold]
NODE 3 [PROCESS/ACTION]: [verbatim text]
NODE 4 [DECISION]: [verbatim yes/no question]
NODE 5 [TERMINAL — urgency]: [verbatim disposition]
NODE 6 [TERMINAL — urgency]: [verbatim disposition]
[continue for every node — number and type-tag them all]

================================================
ENUMERATED CONNECTIONS & BRANCH LABELS (DRAW EXACTLY THESE — NO MORE, NO LESS)
================================================

CONN A: NODE 1 -> NODE 2
CONN B: NODE 2 --YES--> NODE 5
CONN C: NODE 2 --NO--> NODE 3
CONN D: NODE 3 -> NODE 4
CONN E: NODE 4 --YES--> NODE 6
CONN F: NODE 4 --NO--> [NODE or "return to NODE x"]
[continue for every connection — list direction and branch label explicitly]

DO NOT add connections not listed. DO NOT swap YES/NO routing. DO NOT alter thresholds.

================================================
TITLE & LEGEND
================================================

- Top title band (solid [HEX], white text): "[ALGORITHM TITLE]"
- Optional source/version line (small): "[GUIDELINE / PROTOCOL NAME & VERSION]"
- Optional shape legend: rectangle = action, diamond = decision, red box = escalate.
- Optional bottom disclaimer strip (small text): "Educational reference. Follow current institutional protocol. Not a substitute for clinical judgment."

================================================
TYPOGRAPHY
================================================

- Title: bold, ~22 pt
- Node text: regular/semibold, ~12-14 pt, minimum 10 pt
- Branch labels (YES/NO): bold, ~12 pt
- Clean clinical sans-serif (Roboto, Open Sans, or similar)
- High contrast dark text on light fills

================================================
DESIGN SYSTEM (STRICT)
================================================

- Solid fills only, no gradients, no transparency.
- Sharp 90-degree corners on all rectangles, bands, and legend; diamonds only for decisions.
- Arrows: solid lines with a single clear triangular head; consistent weight; every decision branch labeled.
- Allowed graphic elements: process boxes, decision diamonds, terminal boxes, directional arrows, branch labels, title/legend/disclaimer bands.
- Forbidden: photorealistic imagery, 3D depth, glossy effects, decorative scenery, watermark text, invented nodes/branches, altered thresholds, unlabeled decision branches.

================================================
FINAL VALIDATION CHECK
================================================

- One image only
- [Orientation] orientation, flow runs top-to-bottom
- Exactly the listed nodes present (count them); none invented, none omitted
- Exactly the listed connections present, correctly routed; every decision branch labeled (YES/NO)
- No numeric threshold altered
- Decision nodes are diamonds; action/terminal nodes are sharp rectangles
- Urgency color-coding correct (escalate vs routine)
- Flat flowchart artwork, solid fills only
- No gradients, no shadows, no rounded outer corners
- No photorealistic rendering
- Title (and disclaimer strip if specified) present
```

---

## EXAMPLE FILL — REPLACE WITH EXPERT-VERIFIED CONTENT

> The following is an **illustrative, intentionally simplified example only**, to show the shape of a completed template. **Do not treat it as an authoritative, complete, or current algorithm.** Confirm every node, criterion, threshold, and branch against the governing published algorithm/protocol and have a subject-matter expert review before any use.

```
TASK: Generate a SINGLE FLAT PRINT ARTWORK IMAGE representing a clinical decision flowchart for "simplified adult choking response (responsive patient)".

AUDIENCE: basic life support students. Slide + poster. Direction: top-to-bottom.

ENUMERATED NODES (EXAMPLE — VERIFY AGAINST CURRENT GUIDELINE):
NODE 1 [START]: Patient appears to be choking
NODE 2 [DECISION]: Can the patient cough, speak, or breathe?
NODE 3 [PROCESS/ACTION]: Encourage continued coughing; stay with patient and monitor
NODE 4 [PROCESS/ACTION]: Deliver abdominal thrusts (or back blows per protocol)
NODE 5 [DECISION]: Is the obstruction relieved?
NODE 6 [TERMINAL — routine]: Monitor; arrange evaluation as indicated
NODE 7 [TERMINAL — emergent]: Patient unresponsive: activate emergency response, begin CPR

ENUMERATED CONNECTIONS (EXAMPLE — VERIFY):
CONN A: NODE 1 -> NODE 2
CONN B: NODE 2 --YES (effective cough)--> NODE 3
CONN C: NODE 2 --NO (ineffective)--> NODE 4
CONN D: NODE 4 -> NODE 5
CONN E: NODE 5 --YES--> NODE 6
CONN F: NODE 5 --NO--> NODE 7

TITLE: "ADULT CHOKING — Responsive Patient (Simplified)"
DISCLAIMER: "EXAMPLE — REPLACE WITH EXPERT-VERIFIED CONTENT. Follow current guideline/protocol. Not a substitute for clinical judgment or certified training."

[All CRITICAL OUTPUT RULES, SHAPE CONVENTIONS, DESIGN SYSTEM, and FINAL VALIDATION CHECK from the template above still apply.]
```

---

## Simplified Prompt (If Full Prompt Misbehaves)

```
Create ONE flat clinical decision flowchart for [CLINICAL QUESTION], flowing top-to-bottom.

CRITICAL RULES:
- White background; rectangles = actions, DIAMONDS = decisions, red box = escalate, green box = routine
- Every decision diamond has LABELED YES/NO branches
- Sharp corners (diamonds excepted), NO gradients, NO shadows, NO photorealism
- This is a FLAT FLOWCHART, not a mockup or photo

RENDER ONLY THESE NODES (verbatim, with exact thresholds; do not invent/alter/omit):
1.[START]... 2.[DECISION]... 3.[ACTION]... 4.[DECISION]... 5.[TERMINAL]...

DRAW ONLY THESE CONNECTIONS (exact routing & labels; do not swap YES/NO):
1->2, 2--YES-->5, 2--NO-->3, 3->4, ...

Title bar: "[ALGORITHM]". Disclaimer strip: "Educational reference; follow current protocol."
If any criterion/threshold is altered, a branch is misrouted, or a node is invented, it is WRONG.
```

---

## Why This Prompt Works

This prompt applies the 8 core techniques from [IMAGE_GENERATION_GUIDE.md](../IMAGE_GENERATION_GUIDE.md):

1. **Terminology Steering** — "flat labeled flowchart (boxes, diamonds, arrows)" instead of "render," steering away from UI/photoreal tropes.
2. **Grid Forcing + Enumerated Slots** — the **enumerated NODE list plus a separate CONNECTION/branch-label list** are the flowchart equivalent of numbered slots; they lock exactly which decision nodes, thresholds, branches, and actions exist, and how YES/NO routes — preventing invented criteria or misrouted branches.
3. **Constraint Redundancy** — "no invented criteria," "no altered thresholds," "label every branch," "no gradients" repeat across content-authority, shape conventions, design system, and validation check.
4. **Negative Space Control** — solid white background, no scene, no depth.
5. **Allowed vs. Forbidden Distinction** — allows process boxes, decision diamonds, terminal boxes, labeled arrows, bands; forbids photoreal imagery, unlabeled branches, altered thresholds, and any unlisted node/connection.
6. **Physical Context Anchoring** — "protocol poster / pocket reference / slide for [audience]" sets density, flow direction, and the not-a-substitute-for-judgment disclaimer.
7. **Deliverables Locking** — EXACTLY ONE IMAGE, locked orientation/dimensions and top-to-bottom flow.
8. **Validation Checklist** — final self-audit including node count, branch-label, and threshold-integrity checks.

---

## Anti-Fabrication / Expert-Review Section

**Why this matters most for algorithms:** A clinical algorithm's value is its *exact logic and exact numbers*. A model that quietly changes a threshold (e.g., a cutoff value), swaps a YES/NO branch, or invents an action can encode dangerous guidance in a diagram that looks official. Numeric thresholds and branch routing are the highest-risk elements here.

**Rules enforced by this prompt:**
- The model renders **only** the enumerated nodes and **only** the enumerated connections, with branch labels and thresholds **verbatim**.
- No invented criteria, no altered thresholds, no swapped YES/NO routing, no added actions/drugs/doses.
- Unrenderable items become a flagged placeholder, never a guess.
- A standing disclaimer marks the artifact as an educational/reference aid, not clinical authority.

**Required workflow:**
1. Source every node, criterion, threshold, branch label, and action from the governing published algorithm / current guideline / institutional protocol.
2. Fill both the NODE list and the CONNECTION list verbatim; mark any uncertain item explicitly.
3. Generate.
4. **Expert review (mandatory):** a clinician / the protocol owner / qualified educator verifies every node, every criterion and exact threshold, every branch routing (YES/NO), and that nothing was invented, altered, omitted, or misrouted.
5. For clinical deployment or publication, validate against the governing protocol and consider a **professional medical illustrator** for the final artifact.

**Verification Checklist (complete before instructional or clinical-reference use):**
- [ ] Every node, criterion, and threshold was sourced from an expert-verified algorithm/protocol (not the model)
- [ ] Exactly the listed nodes appear; none invented, none omitted
- [ ] Exactly the listed connections appear, correctly routed; every decision branch labeled (YES/NO)
- [ ] **Every numeric threshold/cutoff matches the source exactly** (highest-risk check)
- [ ] No YES/NO branch is swapped or misrouted
- [ ] No action, drug, dose, or advice was added beyond the source
- [ ] Decision nodes are diamonds; action/terminal nodes are rectangles; urgency color-coding correct
- [ ] Disclaimer present (educational/reference; follow current protocol; not a substitute for clinical judgment)
- [ ] **Nodes, criteria, thresholds, and branch routing verified by a subject-matter expert before use**
- [ ] For clinical deployment/publication: validated against governing protocol; professional medical illustrator considered

---

## Model-Specific Notes

For decision flowcharts, **exact in-node text (especially numeric thresholds) and correct branch routing are the key model differentiators.** Lead with the models strongest at in-image text and structured logic.

### gpt-image-2 (OpenAI, flagship) — RECOMMENDED for decision flowcharts
- Set `quality="high"` for legible criteria, thresholds, and YES/NO labels.
- Map to the 5-section structure (Scene / Subject / Key Details / Use Case / Constraints): NODE list + CONNECTION list under Key Details; print/anti-fabrication block under Constraints.
- Strong at distinct text per shape and consistent diamond/box conventions.
- Do NOT pass `input_fidelity` (disabled). See [GPT_IMAGE_2_GUIDE.md](../GPT_IMAGE_2_GUIDE.md).

### Nano Banana Pro (gemini-3-pro-image) — RECOMMENDED for decision flowcharts
- Near-perfect text rendering; name exact fonts/weights for node and threshold legibility.
- Use a **system prompt** to lock "flat flowchart, diamonds=decisions, label every branch, verbatim thresholds, only listed nodes/connections" across regenerations.
- **Search grounding** may help draft logic — but treat grounded output as a draft for expert review; never let it override the source protocol or alter thresholds.
- Markdown-structured prompts (NODE/CONNECTION lists) parse natively.

### DALL-E 3 (legacy)
Add: `"Flat clinical decision flowchart, decision diamonds with labeled YES/NO branches, action boxes, directional arrows, schematic, no photorealism, white background"`. Frequently miscounts nodes, drops branch labels, and may alter text/numbers — verify every threshold and branch.

### Midjourney (legacy)
```
flat clinical decision flowchart, [TOPIC], decision diamonds, labeled yes/no branches, action boxes,
directional arrows, color-coded urgency, white background,
--ar 4:5 --v 6 --style raw --s 25
--no photorealistic 3d gloss shadow gradient rounded corners scenery
```
Note: Midjourney garbles in-image text and rarely preserves exact logic/thresholds — best for styling, with the actual flowchart built in a diagramming tool.

### Stable Diffusion (legacy)
Negative prompt: `"photograph, 3d render, realistic, blurry, gradient, shadow, rounded corners, scenery, watermark, garbled text, wrong numbers, unlabeled branches, extra nodes"`. Poor at exact decision logic — expect to build the flowchart manually.

---

## Troubleshooting

### Problem: Model alters a threshold or number
**Add:** `"Reproduce every number/threshold EXACTLY as written: [restate each threshold]. Any changed number is a rendering error."` Then verify against the source.

### Problem: YES/NO branches swapped or unlabeled
**Add:** `"Every decision diamond must have its outgoing arrows labeled. Routing is fixed: [restate each CONN with its label]. Do not swap YES and NO."`

### Problem: Invented criteria, actions, or drugs/doses
**Add:** `"Render ONLY the listed nodes and connections. Do not add criteria, actions, drugs, or doses not in the list."`

### Problem: Decision nodes drawn as rectangles
**Add:** `"Decision nodes MUST be diamonds. Only decisions are diamonds; all other nodes are sharp rectangles."`

### Problem: Node text garbled
**Switch model** to gpt-image-2 or Nano Banana Pro, or build the chart in a diagramming tool. Also: `"Each node's text must read EXACTLY as written."`

### Problem: Missing disclaimer / looks like clinical authority
**Add:** `"Include the bottom disclaimer strip verbatim: 'Educational reference. Follow current institutional protocol. Not a substitute for clinical judgment.'"`

---

*Updated: 2026-06-23 — Template-driven; nodes, criteria, thresholds, and branch routing require expert verification (image models are not clinically reliable). Educational/reference aid only — not a substitute for clinical judgment.*
