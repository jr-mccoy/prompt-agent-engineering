---
title: PACU Handoff SBAR Cue Card (Inbound + Outbound) — Image Meta-Prompt
category: pacu/image-generation
target_models:
  - nano-banana
  - dall-e-3
updated: "2026-05-15"
tags:
  - pacu
  - image-generation
  - handoff
  - sbar
  - reference-card
---

# Image Meta-Prompt: PACU Handoff SBAR Cue Card

> Safety reminder: Cue card is a memory aid — actual handoff content depends on patient and facility protocol. Does not substitute for direct communication.

## What this meta-prompt produces

A **two-sided pocket cue card** with SBAR scaffolding for inbound (OR → PACU) and outbound (PACU → floor / ICU / home) handoffs. Designed for 8.5 × 5.5 portrait, double-sided.

## INPUTS block

- **Card sides:** {{front = inbound, back = outbound | front only | back only}}
- **Facility-specific SBAR variant elements (optional):** {{paste any facility-supplied additions}}
- **Color tokens:**
  - **Inbound side heading:** teal #0f766e
  - **Outbound side heading:** amber #b45309
  - **Section dividers:** light gray #e5e7eb

---

## READY-TO-PASTE IMAGE PROMPT (Inbound side)

```
Generate one (1) flat reference card — NOT a UI handoff tool, NOT an EHR screenshot, NOT a chat-app mockup.

SUBJECT: PACU inbound handoff SBAR cue card (OR → PACU).

PHYSICAL CONTEXT: 8.5x5.5 portrait pocket card, double-sided print, flat print artwork.

CRITICAL OUTPUT RULES:
- One image, 8.5x5.5 portrait, 300 DPI.
- Pure white #FFFFFF background. No gradient. No shadow.
- Flat vector. No 3D. No bevel. No glow.
- High-contrast sans-serif text.
- No watermarks.

LAYOUT:
- TITLE BAND top, full width. Fill teal {{inbound heading}}. White bold 18pt: "INBOUND HANDOFF — Receiving from OR".
- SUBTITLE 10pt dark slate: "Cue card — verify completeness against facility protocol."
- SBAR SCAFFOLD as 4 stacked panels, each ~22% of remaining height:
  - "S — Situation" panel (light gray divider above). 11pt label bold + 10pt cues:
    - Patient identifier (per facility ID protocol)
    - Procedure performed + duration
    - Anesthesia type (general / regional / MAC) and reversal status if applicable
  - "B — Background" panel:
    - Relevant pre-op history (allergies, prior PACU events, airway concerns)
    - Pre-op vitals baseline
    - Intra-op significant events (estimated blood loss range qualitatively, transfusion if applicable)
  - "A — Assessment" panel:
    - Current vital signs trend qualitatively
    - Airway status (extubated / LMA / supplemental O2)
    - Pain level on arrival
    - PONV risk and prophylaxis given
    - Lines, drains, dressings present
  - "R — Recommendation" panel:
    - Anticipated next 30 min watch-fors
    - Pending orders to confirm
    - Escalation partner by role (CRNA or anesthesiologist on call)
- FOOTER STRIP bottom. 9pt gray. Text: "Cue card. Verify all items per facility protocol. Educational aid."

TYPOGRAPHY: sans-serif throughout. Title 18pt bold. Subtitle 10pt. Panel labels 11pt bold. Cues 10pt regular. Footer 9pt gray.

COLOR PALETTE (strict):
- Background white.
- Text black or dark slate.
- Title band teal {{inbound}}, white text.
- Panel dividers light gray.
- No other colors.

ALLOWED: stacked SBAR panels, panel labels, bullet cues, footer caveat.

FORBIDDEN: 3D card, EHR mockup, chat-bubble styling, animation, drop shadow, gradient, bevel, glow, photographic elements, watermarks. NO invented dose values, NO invented vital-sign thresholds. NO facility-named protocols. Escalation by role only.

VALIDATION CHECKLIST:
1. One image, 8.5x5.5 portrait, 300 DPI.
2. Title band shows INBOUND HANDOFF.
3. Four SBAR panels (S/B/A/R) with labels.
4. Cues are role-based and qualitative — no invented numbers.
5. Footer caveat present.
```

---

## READY-TO-PASTE IMAGE PROMPT (Outbound side)

Same layout, with these substitutions:
- Title band fills amber {{outbound heading}}: "OUTBOUND HANDOFF — Transferring from PACU".
- SBAR panels adapted:
  - **S — Situation:** patient ID per facility ID protocol; procedure done; destination unit/role.
  - **B — Background:** relevant intra-op + PACU events qualitatively; allergies; lines/drains/dressings.
  - **A — Assessment:** discharge-readiness criteria status per facility protocol; pain level + last analgesic timing qualitatively; PONV status; ambulation/voiding status as appropriate to destination.
  - **R — Recommendation:** pending follow-up items, family teaching status, anticipated next-shift watch-fors, escalation pathway from receiving role.
- Footer caveat unchanged.
- Same FORBIDDEN list. Same VALIDATION CHECKLIST adapted to OUTBOUND.

---

## Model-specific notes

**Nano Banana** — clean two-sided card output; print at 300 DPI; trim to 8.5x5.5 with bleed if printing.
**DALL·E 3** — outbound side may compress panels; consider widening to 5.5x8.5 if needed.
**Midjourney** — stylizes; not recommended.

## Variants

- Pediatric SBAR variant: add age-banded weight-based cue ("weight known? confirm if peds-dose patient"); explicitly defer dosing to "per provider order."
- Ambulatory PACU outbound variant: add escort + transport readiness cues.
- Bilingual variant: add Spanish-language version of panel labels (use validated medical Spanish source; do not auto-translate).
