---
title: PACU Escalation — Who to Call by Role Visual — Image Meta-Prompt
category: pacu/image-generation
target_models:
  - nano-banana
  - dall-e-3
updated: "2026-05-15"
tags:
  - pacu
  - image-generation
  - escalation
  - role-reference
---

# Image Meta-Prompt: PACU Escalation — Who to Call by Role

> Safety reminder: Reference visual — names roles, not individuals. Facility-specific contact numbers / pagers / extensions are NOT shown by design and must be added by the facility at print time.

## What this meta-prompt produces

A **flat-print "who to call by role" reference** mapping common PACU scenarios to the appropriate escalation partner by role. Designed for 8.5 × 11 portrait single-page reference or 8.5 × 5.5 portrait pocket card.

## INPUTS block

- **Scenario set:** {{user-supplied list of scenarios; or use the default PACU scenario set below}}
- **Format:** {{single-page 8.5x11 portrait | pocket card 8.5x5.5}}
- **Color tokens:**
  - **Stable scenario:** teal #0f766e
  - **Watch scenario:** amber #b45309
  - **Emergency scenario:** red #b91c1c

## Default scenario set

(Used if user does not supply one. Editable.)

- Post-spinal hypotension trending across cycles
- Sustained desaturation despite supplemental O2
- New bradycardia + hypotension
- Severe post-op pain unresponsive to ordered analgesic
- Persistent PONV with hemodynamic effect
- Suspected residual neuromuscular blockade
- Emergence delirium escalating
- Wound bleeding beyond expected
- Allergic reaction onset
- Code Blue / cardiopulmonary arrest
- Equipment failure
- Family-conflict situation requiring de-escalation
- Bay reassignment / overcapacity
- Medication question / reconciliation issue

---

## READY-TO-PASTE IMAGE PROMPT

```
Generate one (1) flat reference card — NOT a directory UI, NOT a phone app, NOT an EHR mockup.

SUBJECT: PACU escalation reference — scenarios to escalation partner by role.

PHYSICAL CONTEXT: 8.5x11 portrait single-page reference (or 8.5x5.5 portrait pocket card if compressed). Flat print artwork.

CRITICAL OUTPUT RULES:
- One image, portrait, 300 DPI.
- Pure white #FFFFFF background. No gradient. No shadow.
- Flat vector. No 3D. No bevel. No glow.
- High-contrast sans-serif text.
- No watermarks.
- NO contact numbers, pagers, phone extensions, or named staff. Role labels only.

LAYOUT (enumerated):
- TITLE BAND top, full width. Fill teal {{stable}}. White bold 20pt: "PACU Escalation — Who to Call by Role".
- SUBTITLE 11pt dark slate: "Role labels only. Add facility-specific contact at print time."
- TABLE: 3 columns:
  - Column 1 (~45%): Scenario, 11pt regular.
  - Column 2 (~30%): Primary escalation role, 11pt bold.
  - Column 3 (~25%): Concurrent / secondary roles, 10pt regular.
- Each row colored by urgency band on the left edge: 6px teal (stable), 6px amber (watch), 6px red (emergency).
- Rows include the scenarios from the input list. Default rows:
  - Post-spinal hypotension trending → "CRNA or anesthesiologist on call" / "charge nurse if pace shifts"
  - Sustained desaturation → "Anesthesiologist on call" / "respiratory therapist"
  - Bradycardia + hypotension → "Anesthesiologist on call" / "charge nurse, rapid response criteria"
  - Severe pain unresponsive → "CRNA or anesthesiologist on call" / "surgeon if surgical cause suspected"
  - Persistent PONV with hemodynamics → "CRNA or anesthesiologist on call"
  - Residual neuromuscular blockade → "Anesthesiologist on call now" / "respiratory therapist"
  - Emergence delirium escalating → "Anesthesiologist on call" / "charge nurse"
  - Wound bleeding → "Surgeon (call surgical team)" / "charge nurse, anesthesia if hemodynamics shift"
  - Allergic reaction onset → "Anesthesiologist on call now" / "pharmacy after stabilization"
  - Code Blue → "Rapid response / Code team per facility activation" / "charge nurse"
  - Equipment failure → "Charge nurse" / "biomed per facility, respiratory therapist if airway equipment"
  - Family conflict → "Charge nurse" / "social work per facility availability"
  - Bay reassignment / overcapacity → "Charge nurse"
  - Medication question / reconciliation → "Pharmacy consult" / "anesthesia or surgeon by role if order-specific"
- LEGEND bottom-left: 3 color swatches "Stable (teal) / Watch (amber) / Emergency (red)". 10pt.
- FOOTER STRIP bottom. 9pt gray. Text: "Roles only. Facility-specific contact added by unit. Escalation per facility protocol."

TYPOGRAPHY: sans-serif throughout. Title 20pt bold. Subtitle 11pt. Column headers (implicit / not labeled) 11pt bold. Scenario rows 11pt regular. Primary role 11pt bold. Secondary 10pt regular. Legend 10pt. Footer 9pt gray.

COLOR PALETTE (strict):
- Background white.
- Text black or dark slate.
- Title band teal, white text.
- Urgency edge bands: teal (stable), amber (watch), red (emergency).
- No other colors.

ALLOWED: tabular layout, urgency edge bands, legend, footer caveat.

FORBIDDEN: contact numbers, pagers, extensions, named individuals, phone or chat UI styling, dashboard, animation, drop shadow, gradient, bevel, glow, photographic elements, watermarks. NO emoji or icon. NO facility-named protocols on the card itself.

VALIDATION CHECKLIST:
1. One image, portrait, 300 DPI.
2. Title + subtitle present.
3. Three-column table covering scenarios + primary role + secondary roles.
4. Urgency edge bands on each row.
5. Legend with 3 swatches.
6. NO contact numbers, pagers, extensions, named staff anywhere.
7. Footer caveat present.
```

---

## Model-specific notes

**Nano Banana** — table layouts with row coloring render reliably; verify no pager numbers got generated.
**DALL·E 3** — at risk of generating fake pager numbers or "ext. 1234" — explicitly check output for any digits in the role column.
**Midjourney** — not recommended for role-reference tables.

## Variants

- Pocket card 8.5x5.5: drop secondary roles column; primary role only.
- Ambulatory PACU variant: replace some scenarios (e.g., wound bleeding → "early discharge concern").
- Bilingual variant: add Spanish for role labels (use validated medical Spanish source).
