---
title: PACU Medication → Reversal Chart — Image Meta-Prompt
category: pacu/image-generation
target_models:
  - nano-banana
  - dall-e-3
updated: "2026-04-14"
tags:
  - pacu
  - image-generation
  - pharmacology
  - reversal
---

# Image Meta-Prompt: Anesthetic Medications & Reversal Agents Chart

> Safety reminder: Reference only — every reversal dose, interval, and sequence is governed by provider order and facility protocol. Chart leaves specifics as "per order".

## What this meta-prompt produces

A **four-column reference poster**: Drug Class · Example Agent · Reversal / Antagonist · What to Watch For After Reversal. Doses are deliberately NOT rendered (per-order); this keeps the poster facility-agnostic and prevents dangerous memorization. Designed for 11 × 8.5 inch landscape poster.

## INPUTS block

- **Classes to include (default 6):** {{opioids, benzodiazepines, non-depolarizing NMBAs, depolarizing NMBA (succ) — no reversal, anticholinergics, sedatives/hypnotics}}
- **Canvas:** 11 × 8.5 landscape, 300 DPI.
- **Accent colors:** teal #0f766e header; amber #b45309 "watch-for" stripe; red #b91c1c for explicit "no reversal" or "residual effect" cautions.

---

## READY-TO-PASTE IMAGE PROMPT

```
Generate one (1) flat reference poster — NOT a medication package photo, NOT a pharmacy app screenshot, NOT a UI table.

SUBJECT: four-column reference chart of common PACU-relevant anesthetic drug classes with their reversal or antagonist agents and post-reversal watch-fors.

PHYSICAL CONTEXT: 11x8.5 inch landscape poster for PACU wall and orientation binder. Flat print artwork. No photography.

CRITICAL OUTPUT RULES:
- One image. Landscape 11:8.5.
- Pure white #FFFFFF background. No gradient. No shadow. No photographic pill / vial imagery.
- Flat vector. No 3D. No bevel. No glow.
- High-contrast sans-serif text.
- No watermarks.

LAYOUT (enumerated):
- TITLE BAR top. Fill teal {{header accent}}. White bold 24pt: "Anesthesia Meds → Reversal — PACU Reference".
- SUBTITLE below title, 12pt gray centered: "Doses are NOT on this chart by design. Every dose is per provider order and facility protocol."
- COLUMN HEADERS row: "Class" | "Example Agent" | "Reversal / Antagonist" | "Watch For After Reversal".
- ROW 1 — Opioids. Example: morphine / fentanyl / hydromorphone (generic names only, comma separated). Reversal: naloxone. Watch For: resedation as naloxone wears off (shorter half-life than most opioids); pain rebound; respiratory status.
- ROW 2 — Benzodiazepines. Example: midazolam. Reversal: flumazenil. Watch For: resedation; seizure risk in chronic benzodiazepine users; recurrent respiratory depression.
- ROW 3 — Non-depolarizing NMBAs. Example: rocuronium, vecuronium, cisatracurium. Reversal: sugammadex (steroidal NMBAs) or neostigmine + glycopyrrolate/atropine. Watch For: residual block / recurarization (TOF monitoring per facility); bradycardia with neostigmine.
- ROW 4 — Depolarizing NMBA. Example: succinylcholine. Reversal: none — DIRECT REVERSAL NOT AVAILABLE. Watch For: prolonged block with pseudocholinesterase deficiency; hyperkalemia; malignant hyperthermia triggers. Row flagged with red {{escalate accent}} left stripe 3pt.
- ROW 5 — Anticholinergics (when co-administered). Example: glycopyrrolate, atropine. Reversal: none — wear off. Watch For: tachycardia, dry mouth, urinary retention, confusion (esp. elderly with atropine).
- ROW 6 — Sedatives / hypnotics (IV induction). Example: propofol, etomidate, ketamine. Reversal: none — wear off. Watch For: emergence delirium (ketamine); adrenal effect concern (etomidate, per source); hypotension on redosing.
- Alternating row fills white / light gray #F3F4F6.
- "Watch For After Reversal" column has amber {{watch accent}} left stripe 3pt on every row (except depolarizing NMBA row which gets red stripe).
- FOOTER STRIP bottom. 9pt gray. Text: "Doses per order. Reversal timing, sequence, and monitoring per facility protocol. Not a substitute for clinical judgment or pharmacy reference."

TYPOGRAPHY: sans-serif throughout. Title 24pt bold. Subtitle 12pt. Column headers 13pt bold. Body 11pt.

COLOR PALETTE (strict):
- Background white.
- Text black.
- Title bar teal {{header}}.
- Row alt #F3F4F6.
- Watch stripe amber {{watch}}.
- Escalate stripe red {{escalate}} — ONLY on the depolarizing NMBA row.
- No other colors.

ALLOWED: clean columns, accent stripes, sans-serif text, ordered rows.

FORBIDDEN: pill / vial / syringe photographs, branded drug packaging, dose numbers anywhere (no milligrams, no micrograms, no mL), 3D, gradient, drop shadow, bevel, glow, UI chrome, stock medical imagery, watermarks.

VALIDATION CHECKLIST (must pass before returning):
1. One image, 11x8.5 landscape, 300 DPI.
2. Six rows in the order: Opioids, Benzodiazepines, Non-depolarizing NMBA, Depolarizing NMBA, Anticholinergics, Sedatives/Hypnotics.
3. Zero dose numbers anywhere on the poster.
4. Row 4 (depolarizing NMBA) has red left stripe; all others have amber stripe.
5. Subtitle present and says doses are per order.
6. Footer caveat present.
7. No product photography or branded packaging.
```

---

## Model-specific notes

**Nano Banana** — reliably suppresses dose numbers if the FORBIDDEN block explicitly bans "milligrams, micrograms, mL". Keep that list verbatim.
**DALL·E 3** — occasionally inserts drug package imagery; repeat "no pill, no vial, no syringe, no branded packaging".
**Midjourney** — not recommended; tends to add photographic drug imagery.

## Variants

- Pediatric version — same structure, add Weight-Based footer ("all peds doses are weight-based, per order") and flag succinylcholine additional peds cautions.
- Sugammadex-only facility version — simplify Row 3 to single reversal agent and expand Watch-For to include residual block if sugammadex dose is insufficient per TOF.
