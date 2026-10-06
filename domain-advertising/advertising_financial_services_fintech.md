---
title: "Fintech Image Advertising Prompt Builder"
category: advertising/image-generation
description: "Interview-driven meta-prompt for generating print-safe and screen-safe advertising image prompts for fintech."
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
  - financial
  - campaign-creative
  - print-ready
updated: "2026-10-06"
related_prompts:
  - domain-image-generation/IMAGE_GENERATION_GUIDE.md
  - domain-presentations/visual-planning/visualplan_capability_frontier_map.md
  - domain-presentations/visual-planning/visualplan_visual_qa_harness.md
  - domain-presentations/visual-planning/visualplan_modality_router.md
---

**Objective:** Generate a high-compliance advertising image prompt for **Fintech** campaigns using an interview-first workflow and strict print/screen output constraints.

## Interview Intake (required before prompt generation)

Collect and confirm all fields before drafting the final image prompt:
1. **Product/Offer:** `banking app, payment card, fintech feature launch`
2. **Audience:** `digitally active adults and small businesses`
3. **Key Message:** `Control money with trust and speed`
4. **Palette Direction:** `deep blue/mint/white palette`
5. **Primary CTA:** `Open your account`
6. Channel split: print, screen, or both.
7. Format targets: poster, flyer, social feed, story, display ad, billboard, or handout.

If any required field is missing, ask concise follow-up questions first.

## Instructions

### 1) Build the Core Prompt Contract
Write the generated image prompt as a contract with these mandatory blocks:
- ROLE + purpose
- campaign context for fintech
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
- **SV-16 Physical Context Anchoring:** include realistic usage context for fintech advertising collateral.
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

1. **Rates and returns are the slot a model fills first.** "4.50% APY", "earn up to 5% cashback",
   "$0 fees", and "returns of 12%" look like ordinary headline copy. Copy a rate or fee only from
   intake with its effective date; any supplied rate goes to
   `campaign/adcampaign_claims_compliance_review.md` for its qualifying-text questions.
2. **Protection badges and regulator marks are never decoration.** Deposit-insurance badges,
   "insured", licence numbers, regulator logos, and "bank-grade security" padlocks appear only when
   the user supplies the exact mark; whether the product may display it is a question for counsel,
   not something this prompt decides.
3. **Growth imagery implies performance.** Even outside a UI frame, a rising line, stacked coins, or
   a large balance figure suggests returns; include one only when the key message is about growth
   and the claim is substantiated.
4. **Card art carries text.** No card numbers, cardholder names, or expiry dates; payment-network
   logos only from supplied files.
5. **Verify before handing over:** list every numeral, percent sign, currency symbol, logo, and
   badge in the Final Image Prompt and each variant, and map each to an intake answer and date. A
   badge or rate without one fails, however clean the form checklist looks.

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
