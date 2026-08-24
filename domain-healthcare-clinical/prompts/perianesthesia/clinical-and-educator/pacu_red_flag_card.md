---
title: PACU Red-Flag Card (Pocket)
category: pacu/quick-reference
task_type: CREATE
audience: Phase 1 PACU nurse at the bedside
updated: "2026-04-16"
tags:
  - pacu
  - red-flag
  - pocket-card
techniques:
  - ST-01
  - ST-03
  - RT-02
  - ED-02
  - DS-06
difficulty: beginner
related_prompts:
  - ../../domain-healthcare-clinical/prompts/nursing_quick_reference_handbook_creator_prompt.md
  - ../../domain-healthcare-clinical/prompts/nursing_sbar_clinical_escalation.md
  - prompts/pacu_topic_primer.md
  - prompts/pacu_complication_deep_dive.md
references:
  - Drain's PeriAnesthesia Nursing Practice (7th ed.)
  - ASPAN Standards of Perianesthesia Nursing Practice
  - ASPAN Core Curriculum for PeriAnesthesia Nursing Practice
---

# PACU Red-Flag Card — Pocket

> Safety reminder: Recognition aid only — clinical judgment and facility escalation policy override this card.

## Objective

Produce a **single-topic red-flag card** sized to print at 4 × 6 inches (index-card format). Each row is actionable in < 10 seconds at the bedside.

## Inputs

- **Topic / scenario:** {{e.g., "Post-op hypotension", "PONV escalation", "Residual NMB"}}
- **Surgery or anesthesia context (optional):** {{e.g., "post spinal", "post general with neuromuscular blockade"}}
- **Source chapters:** {{...}}

## Audience

- PACU nurse, any experience level, at the bedside.
- Reads while standing, often while simultaneously assessing a patient.

## Output requirements

```markdown
# {Topic} — Red Flags (Pocket Card)

> Safety reminder: Recognition aid only — escalate per facility protocol.

## Trigger → Action → Call
| If you see... | Do this now | Call |
|---|---|---|
| ... | ... | ... |
| ... | ... | ... |
| ... | ... | ... |
| ... | ... | ... |
| ... | ... | ... |

## Before you call — have these ready (SBAR)
- **S** — situation (one sentence).
- **B** — surgery, anesthesia, pertinent Hx.
- **A** — current VS, exam finding, what you've already done.
- **R** — what you're asking for.

## Don't-miss pearls
- ...
- ...
- ...

## Sources
- ...
```

## Must / Must not

**Must:**
- 5–8 trigger/action/call rows. Each row actionable in one sentence.
- SBAR reminder block.
- 2–4 "don't-miss pearls" — the subtle cues that separate this red flag from its common mimic.
- Cite sources by chapter.

**Must not:**
- No paragraph prose — this is a table, not an essay.
- No invented thresholds — if a value is not in source, state the cue qualitatively ("trending down", "new onset").
- No facility-specific pagers, rooms, or equipment.

## Quality signals

- A nurse can read any row and act in < 10 seconds.
- The "call" role is explicit (anesthesia, surgeon, rapid response, etc.) — never a name.
- SBAR takes < 30 seconds to populate mentally.

## Verification

Before returning, verify:

- [ ] Every row's "Do this now" is a single, physically achievable action at the bedside (not a sequence, not a decision tree).
- [ ] Every "Call" is a role a PACU nurse could identify without looking up a name.
- [ ] Any numeric threshold in the card can be cited to a specific source chapter; if not, it is reframed qualitatively.
- [ ] Don't-miss pearls describe the cue that separates this red flag from its mimic, not just restate the red flag.
- [ ] Card physically fits a 4×6 in index-card format when printed (word budget suggests yes).

## False-Positive Prevention

Do **not** fabricate:

- **No invented numeric thresholds** (BP cutoffs, SpO₂ limits, HR ranges, urine output minimums). If the source chapter doesn't give a number, write "trending down," "persistent," or "new onset."
- **No invented doses** in the SBAR or pearls sections.
- **No facility-specific pager numbers, extensions, room assignments, rapid-response codes, or crash-cart contents.** Use role labels and "per facility protocol."
- **No invented equipment brand names or supply specifics** (specific bag-valve-mask model, suction canister brand).
- **No fabricated incidence or "most common cause" claims** without a source.
- **No invented chapter numbers.** Mark `{{confirm chapter}}` if unknown.

## Worked Example

<details>
<summary>Example: Topic = "Post-Op Hypotension, Post-General with NMB" (click to expand, abbreviated)</summary>

```markdown
# Post-Op Hypotension (Post-General w/ NMB) — Red Flags (Pocket Card)

> Safety reminder: Recognition aid only — escalate per facility protocol.

## Trigger → Action → Call
| If you see... | Do this now | Call |
|---|---|---|
| BP trending down across two consecutive cycles | Raise legs (per position order), recheck manually | Anesthesiologist / CRNA by role |
| New bradycardia with hypotension | Stop triggering stimulus, prepare atropine per order | Anesthesiologist on call |
| Altered mentation + BP drop | Position safely, open airway assessment | Rapid response, CRNA |
| Bleeding at surgical site + BP drop | Reinforce dressing, elevate if ordered, do not remove original | Surgeon on call |
| SpO₂ drift + shallow breathing + BP drop | Support airway, assess head-lift | Anesthesiologist, prepare reversal |

## Before you call — have these ready (SBAR)
- **S** — "Patient in bay 3, post-op, BP trending down over last two cycles."
- **B** — surgery type, anesthesia type, reversal status, fluids hung.
- **A** — current VS, what you've already done (position, O2), response.
- **R** — what you need (eval, orders, bedside presence).

## Don't-miss pearls
- Hypotension after general + NMB isn't always fluid — check for residual blockade driving shallow breathing first.
- Bradycardia + hypotension suggests high block level or vagal — escalate faster than isolated hypotension.
- Sudden BP drop + bleeding dressing = assume surgical site until proven otherwise.

## Sources
- *Drain's PeriAnesthesia Nursing*, Ch. on Cardiovascular Assessment in PACU
- ASPAN *Core Curriculum* — hemodynamics module
```

Notes: five rows, all actionable in one sentence, all thresholds qualitative, calls by role, pearls separate this red flag from its mimics.
</details>

## Self-check

- [ ] Table has 5–8 rows.
- [ ] Every row has trigger + action + call.
- [ ] SBAR block present.
- [ ] ≥ 2 pearls.
- [ ] No invented thresholds; all numeric values sourced.
- [ ] Safety reminder at top.
- [ ] Verification section passed.
- [ ] False-Positive Prevention section passed — no invented thresholds, doses, or facility specifics.
