---
title: "Fashion Image Advertising Prompt Builder"
category: advertising/image-generation
description: "Interview-driven meta-prompt for generating print-safe and screen-safe advertising image prompts for fashion."
techniques:
  - SV-03
  - ST-02
  - SV-11
  - SV-12
  - SV-13
  - SV-14
  - SV-15
  - SV-16
  - SV-17
  - SV-18
difficulty: intermediate
tags:
  - advertising
  - image-generation
  - fashion
  - campaign-creative
  - print-ready
updated: "2026-10-06"
related_prompts:
  - domain-image-generation/IMAGE_GENERATION_GUIDE.md
  - domain-presentations/visual-planning/visualplan_capability_frontier_map.md
  - domain-presentations/visual-planning/visualplan_visual_qa_harness.md
  - domain-presentations/visual-planning/visualplan_modality_router.md
---

**Objective:** Generate a high-compliance advertising image prompt for **Fashion** campaigns using an interview-first workflow and strict print/screen output constraints.

## Interview Intake (required before prompt generation)

Collect and confirm all fields before drafting the final image prompt:
1. **Product/Offer:** `seasonal drop, capsule collection, retail promotion`
2. **Audience:** `style-conscious shoppers`
3. **Key Message:** `Limited release and identity expression`
4. **Palette Direction:** `black/ivory/accent palette`
5. **Primary CTA:** `Shop the drop`
6. Channel split: print, screen, or both.
7. Format targets: poster, flyer, social feed, story, display ad, billboard, or handout.

If any required field is missing, ask concise follow-up questions first.

## Instructions

### 1) Build the Core Prompt Contract
Write the generated image prompt as a contract with these mandatory blocks:
- ROLE + purpose
- campaign context for fashion
- exact deliverables list
- canvas dimensions and orientation
- layout geometry with numbered content slots
- typography and color system
- allowed vs forbidden styling
- anti-UI and anti-mockup constraints
- final validation checklist

### 2) Apply All 8 Image Techniques
Embed every technique explicitly:
- **SV-11 Terminology Steering:** use "flat print artwork", "ink-on-paper layout", and "edge-to-edge print surface".
- **SV-12 Grid Forcing + Enumerated Slots:** lock exact grid and numbered slots.
- **SV-13 Constraint Redundancy:** repeat no-gradients/no-shadows rules in global rules, design rules, and checklist.
- **SV-14 Negative Space Control:** enforce solid background and ban scene lighting.
- **SV-15 Allowed vs Forbidden Distinction:** define structured layout allowed, UI chrome forbidden.
- **SV-16 Physical Context Anchoring:** include realistic usage context for fashion advertising collateral.
- **SV-17 Deliverables Locking:** exact image count, dimensions, orientation, and DPI.
- **SV-18 Validation Checklist:** pass/fail checklist ending with explicit failure conditions.

### 3) Print/Screen Output Lock (mandatory)
The generated prompt must include BOTH modes unless user requests one mode only:
- **Print lock:** CMYK-safe palette guidance, 300 DPI, bleed-safe margins, sharp corners, no transparency artifacts.
- **Screen lock:** RGB/hex palette, pixel dimensions per channel, no UI-container framing, edge-to-edge export.

### 4) Anti-UI + Anti-Mockup Constraints (mandatory)
Include all of the following in final prompt:
- Not a software interface.
- Not a dashboard.
- Not a card UI.
- Not a device mockup.
- No hands, desks, screens, or environmental staging.
- No rounded-corner app tiles.
- No faux browser chrome.

### 5) Redundant Visual Prohibitions (mandatory)
State in at least three sections:
- No gradients.
- No drop shadows.
- No glassmorphism.
- No bevel, emboss, glow, lens flare, vignette, or depth effects.

### 6) Model-Specific Output Section (mandatory)
After generating the base prompt, append adaptation notes for:
- **DALL-E:** plain-language constraints first, then deliverables and checklist.
- **Midjourney:** compact syntax; include `--ar`, style restraint, and exclusion terms.
- **Stable Diffusion:** include positive prompt, negative prompt, sampler guidance, and CFG range.
- **Gemini:** keep instruction hierarchy explicit and include a final compliance checklist.

### 7) Final Validation Checklist (mandatory)
The generated prompt must end with a checklist confirming:
- Interview inputs reflected accurately.
- Output mode(s) locked (print/screen).
- Grid + slot numbering present.
- CTA appears exactly once in the primary focal slot.
- No UI/mockup styling.
- No gradients/shadows (repeated).
- Deliverable count and dimensions are exact.

## False-Positive Prevention

1. **The rendered garment must be the garment in the drop.** The checklist passes on layout while
   the image shows another cut, fabric, print, or colourway. Describe the actual pieces (silhouette,
   material, colour names) from intake; if intake says only "seasonal drop", ask which pieces.
2. **Bodies shown imply the size range.** Models in sizes or fits the collection does not come in
   misstate who can buy it; ask what size range ships before describing figures.
3. **"Limited release" invites invented scarcity.** "Only 100 made", "48 hours only", and "-40%"
   are rendered only as supplied, and a discount keeps its stated basis next to the figure.
4. **Marks on the clothing are claims of origin.** Invented labels, monograms, or collaboration
   names stay off the garment; ask the user to avoid patterns that resemble another house's
   signature print, and raise any doubt about one as a counsel question.
5. **Verify before handing over:** read the garment description in the Final Image Prompt against
   intake attribute by attribute (piece, colour, fabric, fit), then match each rendered string,
   including any swing-tag or label text, to its intake answer verbatim.

## Output Format

Return in this exact structure:
1. `## Intake Summary`
2. `## Final Image Prompt`
3. `## Model-Specific Variants (DALL-E / Midjourney / Stable Diffusion / Gemini)`
4. `## Validation Checklist`
5. `## Revision Options (3 focused improvements)`

## Quality Guardrails

**Do:**
- Keep constraints concrete, measurable, and testable.
- Use explicit dimensions and slot numbering.
- Keep messaging hierarchy to one hero claim + one CTA.

**Don't:**
- Add speculative brand claims not supplied in intake.
- Replace user CTA with an invented CTA.
- Drift into UI product-shot or lifestyle mockup framing.

## Technique Coverage Confirmation

This prompt enforces all 8 image techniques: **SV-11, SV-12, SV-13, SV-14, SV-15, SV-16, SV-17, SV-18**.
