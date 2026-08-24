---
title: PACU Drug Monograph — Naloxone (Opioid Reversal)
category: pacu/pharmacology
task_type: LEARN
audience: PACU orientee (any phase) or preceptor for huddle
updated: "2026-07-07"
tags:
  - pacu
  - pharmacology
  - naloxone
  - opioid-reversal
  - respiratory-depression
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-02
  - ED-02
  - DS-06
difficulty: intermediate
related_prompts:
  - pacu_opioid_induced_respiratory_depression.md
  - pacu_medication_profile.md
  - pacu_red_flag_card.md
references:
  - Drain's PeriAnesthesia Nursing Practice (7th ed.) — pharmacology and respiratory chapters
  - ASPAN Standards of Perianesthesia Nursing Practice
  - Hospital pharmacy monograph (facility-specific; confirm current version)
---

# Naloxone — PACU Drug Monograph

> Safety reminder: Naloxone is titrated **to adequate respiration, not to full consciousness** — every dose, dilution, and interval is per provider order and facility protocol; this monograph states no doses. Its duration is often shorter than the opioid it reverses, so re-sedation surveillance is mandatory. See `../SAFETY_PREAMBLE.md`.

## Objective

Produce a PACU-focused reference on naloxone that teaches titrate-to-respiration reversal, the re-sedation window, and the harms of over-reversal — with all pharmacology framed as provider-ordered.

## Inputs

- **Facility protocol name for opioid reversal:** {{e.g., unit reversal protocol / order set}}
- **Sedation scale used on your unit:** {{POSS | RASS | facility scale}}
- **Higher-risk populations on your unit:** {{OSA/obesity, older adults, renal impairment, opioid-tolerant/dependent, cardiac}}

## Audience

- Orientee at any phase — core PACU safety pharmacology; pairs with the OIRD deep dive.
- Preceptor building a pain-safety or reversal huddle.

## Output requirements

```markdown
# Naloxone — PACU Profile

> Safety reminder: Titrate to respiration, not to consciousness. All dosing per order. Watch for re-sedation.

## Class & mechanism
- Class: opioid receptor antagonist (competitive antagonist at the mu-opioid receptor).
- How it works: competitively displaces opioid from mu receptors, reversing opioid-induced respiratory depression and sedation — and, unavoidably, analgesia.

## When it's used in PACU
- Opioid-induced respiratory depression / clinically significant oversedation, given per order once sedation-first cues and hypoventilation are recognized (see the OIRD deep dive).

## What you want to see vs what you watch for
- Want to see: return of adequate spontaneous respiration and rousability — enough breathing, not full arousal.
- Watch for: acute withdrawal and sudden severe pain, agitation, hypertension/tachycardia, nausea/vomiting; rarely, negative-pressure pulmonary edema or dysrhythmia from an abrupt sympathetic surge.

## Onset / duration (per pharmacy monograph)
- Rapid IV onset; **duration is frequently shorter than the reversed opioid** — defer specific figures to the monograph. The clinical consequence, not a number, is the teaching point: re-sedation is expected.

## Dose
- Per order — titrated in small increments to restore adequate respiration. This monograph states no doses, dilutions, or concentrations.

## Monitoring in PACU
- Reassess sedation level, respiratory rate/pattern, and SpO₂ **after each titrated increment** (per order interval), because effect builds with titration.
- Specific assessment: rousability + depth/rate of breathing + airway patency — not the SpO₂ number alone (on supplemental O₂ SpO₂ lags).
- Extended, heightened sedation + respiratory monitoring after apparent recovery, per facility interval, for the re-sedation window.

## Re-sedation watch (critical)
- Because naloxone often wears off before the opioid does, the patient can re-sedate after looking recovered. Continued monitoring after reversal is required, not optional.

## Cautions / interactions in PACU
- Opioid-tolerant / dependent patients: reversal can precipitate acute withdrawal — titrate carefully per order.
- Cardiac / hypertensive patients: abrupt reversal and pain/sympathetic surge can stress the cardiovascular system.
- The reversal also removes analgesia — anticipate a pain-management plan per provider.

## Red flags that require escalation
- Rising sedation with hypoventilation, or any apnea → call {anesthesia provider by role}; rapid response / code per facility for apnea or unresponsiveness.
- Post-reversal pulmonary edema (pink frothy sputum, respiratory distress), chest pain, or dysrhythmia → call {provider by role} immediately.

## Common orientee mistakes
- Pushing too much too fast, aiming for a wide-awake patient — producing severe pain, agitation, and a sympathetic surge.
- Treating one dose as the end of the problem and standing down monitoring.
- Being reassured by a "normal" SpO₂ on oxygen while sedation is still deepening.

## Teaching pearls
- The endpoint is breathing, not conversation.
- After naloxone, keep watching — re-sedation is the rule, not the exception.

## Sources
- *Drain's PeriAnesthesia Nursing*, pharmacology / respiratory chapters
- Hospital pharmacy monograph (facility-specific; confirm current version)
```

## Must / Must not

**Must:**
- Frame reversal as titrate-to-respiration with an explicit re-sedation watch.
- Name the over-reversal harms (pain, sympathetic surge, rare NPPE).
- Keep every dose/dilution/interval as "per order."

**Must not:**
- No naloxone/opioid doses, dilutions, concentrations, or titration numbers.
- No invented onset/duration figures — defer to monograph, keep the clinical consequence.
- No nurse-initiated dosing decisions (provider-scope).
- No invented facility protocol or pager path.

## Quality signals

- Orientee titrates toward adequate breathing and continues monitoring for re-sedation.
- Orientee anticipates pain and a sympathetic response after reversal.

## Verification

- [ ] Titrate-to-respiration (not to consciousness) stated explicitly.
- [ ] Re-sedation window taught as mandatory continued monitoring.
- [ ] Over-reversal harms named.
- [ ] Monitoring block has a reassess interval + specific assessment.
- [ ] Red flags link trigger → escalation role.
- [ ] No doses/dilutions/concentrations anywhere.

## False-Positive Prevention

Do **not** fabricate or invent:

- **No naloxone/opioid doses, dilutions, concentrations, or titration increments.** Per order only.
- **No invented onset/duration figures.** Defer to pharmacy monograph; keep the "shorter than the opioid" consequence.
- **No invented incidence statistics** for withdrawal, NPPE, or dysrhythmia — describe qualitatively.
- **No invented facility protocols or pager paths.**
- **No fabricated chapter/monograph citations.** Mark `{{confirm}}`.
- **No scope creep** — the decision to give and how much to give is provider-scope.

## Worked Example

<details>
<summary>Example: framing the re-sedation window for an orientee (click to expand)</summary>

```markdown
## Re-sedation watch

Your patient got naloxone per order for deepening sedation and shallow breathing after a long-acting opioid. Ten minutes later she's breathing well and talking — the instinct is to relax.

Don't. The opioid outlasts the naloxone here, so she can slide back into sedation and hypoventilation as the reversal wears off. Keep the heightened sedation + respiratory monitoring going per facility interval, keep BVM at the bedside, and be ready to call the provider and re-dose per order if she re-sedates.
```

Notes: titrate-to-respiration honored, re-sedation framed as expected, no doses stated, escalation by role.
</details>

## Self-check

- [ ] Titrate-to-respiration + re-sedation watch taught.
- [ ] Over-reversal harms named.
- [ ] Monitoring block has interval + specific assessment.
- [ ] Red flags have escalation role.
- [ ] Safety reminder at top.
- [ ] No invented doses/dilutions/onset/duration/facility specifics.
- [ ] Verification + False-Positive Prevention passed.
