---
title: "Automotive Image Advertising Prompt Builder"
category: advertising/image-generation
description: "Interview-driven meta-prompt for generating print-safe and screen-safe advertising image prompts for automotive."
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
  - automotive
  - campaign-creative
  - print-ready
updated: "2026-10-06"
related_prompts:
  - domain-image-generation/IMAGE_GENERATION_GUIDE.md
  - domain-presentations/visual-planning/visual_frontier_map.md
  - domain-presentations/visual-planning/visual_qa_harness.md
  - domain-presentations/visual-planning/visual_workflow_router.md
---

**Objective:** Generate a high-compliance advertising image prompt for **Automotive** campaigns using an interview-first workflow and strict print/screen output constraints.

## Interview Intake (required before prompt generation)

Collect and confirm all fields before drafting the final image prompt:
1. **Product/Offer:** `vehicle launch, lease special, dealership promotion`
2. **Audience:** `new car buyers, lease renewers, local shoppers`
3. **Key Message:** `Performance + safety + offer urgency`
4. **Palette Direction:** `bold red/black/silver palette`
5. **Primary CTA:** `Book a test drive`
6. Channel split: print, screen, or both.
7. Format targets: poster, flyer, social feed, story, display ad, billboard, or handout.

If any required field is missing, ask concise follow-up questions first.

## Instructions

### 1) Build the Core Prompt Contract
Write the generated image prompt as a contract with these mandatory blocks:
- ROLE + purpose
- campaign context for automotive
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
- **SV-16 Physical Context Anchoring:** include realistic usage context for automotive advertising collateral.
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

1. **A ticked checklist can still show the wrong car.** "Interview inputs reflected accurately"
   passes because the model name is in the headline while the rendered vehicle has another trim,
   body style, wheel design, or paint colour. Name the advertised configuration (model year, trim,
   colour, wheels) in the prompt; if intake said only "vehicle launch", ask for it.
2. **Offer figures are never filled by the model.** A blank offer slot comes back as "$299/mo",
   "0.9% APR", or "$0 down". Payment, APR, term, and mileage text is copied from intake or the slot
   is removed; a supplied offer goes to `campaign/adcampaign_claims_compliance_review.md` for its
   disclosure questions, not treated as finished here.
3. **Ratings and awards are claims, not ornament.** Safety-rating stars, "Best in Class", award
   seals, and manufacturer or dealer logos appear only when the user supplies them.
4. **Scenes imply capability.** Rock-crawling terrain, a towed trailer, or a racetrack backdrop says
   what the vehicle can do; use one only when the key message and the configuration support it.
5. **Plates and badges carry text too.** Licence plates stay blank; trim badges on the body must
   read the advertised trim or be omitted.
6. **Verify before handing over:** list every string the prompt and each model variant asks to be
   rendered (headline, offer, CTA, plate, badge, disclaimer) and match each character-for-character
   to an intake answer; then compare the vehicle description to the intake configuration field by
   field. Any unmatched string or attribute fails, whatever the form checklist says.

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
