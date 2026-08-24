---
title: PACU Topic Primer (1-Page)
category: pacu/education
task_type: CREATE
audience: Phase 1 PACU orientee (week 1–2)
updated: "2026-04-16"
tags:
  - pacu
  - primer
  - orientee
techniques:
  - ST-01
  - ST-02
  - RT-02
  - ED-02
  - DS-06
difficulty: beginner
related_prompts:
  - ../../domain-healthcare-clinical/prompts/nursing_pacu_prioritization_rule.md
  - ../../domain-healthcare-clinical/prompts/nursing_pacu_shift_structure.md
  - prompts/pacu_red_flag_card.md
  - prompts/pacu_complication_deep_dive.md
references:
  - Drain's PeriAnesthesia Nursing Practice (7th ed.)
  - ASPAN Standards of Perianesthesia Nursing Practice
  - ASPAN Core Curriculum for PeriAnesthesia Nursing Practice
---

# PACU Topic Primer — 1-Page

> Safety reminder: Educational primer only — verify specifics against facility protocol and provider order.

## Objective

Produce a **one-page primer** on a single PACU topic, written for a brand-new orientee who has never seen this topic on shift. The primer gives them just enough context to participate in a huddle, ask good questions, and recognize the topic when it appears at the bedside.

## Inputs to paste in

- **Topic:** {{topic}}
- **Why user is making this primer:** {{context — e.g., orientee rotating to GYN next week}}
- **Source chapters available:** {{e.g., Drain's Ch. 32 Gyn Surgery; Core Curriculum Regional Anesthesia}}

## Audience

- PACU orientee, week 1–2.
- May not yet know the baseline vocabulary; define jargon on first use.
- Reads at the end of a shift; attention budget ~5 minutes.

## Output requirements

Produce exactly this structure, ≤ 1 page (≈ 500 words):

```markdown
# {Topic} — Orientation Primer

> Safety reminder: Educational aid only — verify against facility protocol at the bedside.

## What this is
[1–2 sentences — the plainest possible definition]

## Why it matters in PACU
[1 paragraph — a realistic bedside situation]

## The 5 things to know
1. ...
2. ...
3. ...
4. ...
5. ...

## Watch-fors (red flags)
- {trigger} → {what you do} → call {role}
- {trigger} → {action} → call {role}
- {trigger} → {action} → call {role}

## Questions to ask your preceptor
- ...
- ...
- ...

## One sentence to carry to your next shift
[memorable takeaway]

## Sources
- *Drain's PeriAnesthesia Nursing*, Ch. XX: {title}
- {additional}
```

## Must / Must not

**Must:**
- Exactly 5 items in "The 5 things to know" — no more, no less.
- At least 3 red-flag rows with trigger → action → call.
- ≥ 3 preceptor-facing questions the orientee can actually ask.
- Cite sources by chapter title.

**Must not:**
- No invented doses, thresholds, or facility-specific equipment.
- No jargon without first-use definition.
- No more than one page / 500 words.

## Quality signals

- An orientee reading this could walk into a huddle and ask an informed question within 5 minutes.
- Every red flag could be acted on without further lookup.
- Nothing in the output is memorable only if the reader already knew it.

## Verification

Before returning, re-read the primer once and confirm:

- [ ] Every factual claim (numeric threshold, monitoring interval, pharmacologic behavior) either cites a source chapter or is qualitative ("trending down," "new onset"). No unsourced numbers.
- [ ] "Call {role}" in every red-flag row resolves to a PACU-appropriate escalation partner (CRNA, anesthesiologist on call, surgeon, charge nurse, rapid response) — never a named person, pager, or phone number.
- [ ] Would a preceptor familiar with this topic read the primer, circle zero items as "invented or wrong," and hand it to an orientee without edits? If not, revise.
- [ ] No facility-specific equipment, pager paths, or room numbers.

## False-Positive Prevention

Do **not** fabricate any of the following — even if the output "needs" them to feel complete. When source is unclear, leave placeholders or reference facility protocol explicitly.

- **No invented doses, concentrations, or dilutions.** If the source chapter gives a range, quote the range with citation. Otherwise write "{per provider order}" or "per facility protocol."
- **No invented vital-sign or lab thresholds** (SpO₂ cutoffs, MAP targets, temperature limits, urine output minimums). Use qualitative cues ("trending down," "persistently below baseline") unless the source gives a number.
- **No invented facility-specific equipment**, bag sizes, syringe concentrations, or device brand names. Describe generically ("bag-valve-mask," "infusion pump").
- **No invented pager extensions, phone numbers, room numbers, or staff names.** Use role labels only.
- **No fabricated citations.** If the chapter number or section is unknown, write `{{confirm chapter in Drain's / Core Curriculum}}` rather than guessing.
- **No fabricated statistics or incidence rates.** If the source does not supply a number, describe the pattern qualitatively.

## Worked Example

<details>
<summary>Example: Topic = "Post-Spinal Hypotension" (click to expand)</summary>

```markdown
# Post-Spinal Hypotension — Orientation Primer

> Safety reminder: Educational aid only — verify against facility protocol at the bedside.

## What this is
A drop in blood pressure after a spinal (intrathecal) anesthetic — caused by the block's effect on sympathetic outflow below the block level.

## Why it matters in PACU
A patient arrives from OR after a spinal for cesarean or lower-extremity surgery, looks fine for the first 10 minutes, then their BP starts drifting down as you're charting admission. Catching the trend before the classic "feels dizzy" complaint is the skill.

## The 5 things to know
1. The block causes vasodilation below the block level → less venous return → lower preload → lower BP.
2. Higher blocks (T4 and above) also blunt cardiac sympathetic input → bradycardia can accompany the hypotension.
3. Fluid status at OR exit matters — a dry patient looks fine until they're not.
4. Position changes (head-up transfer, reverse-Trendelenburg) can unmask hypotension rapidly.
5. Resolution is gradual as the block recedes — watch for 2+ hours, not 20 minutes.

## Watch-fors (red flags)
- BP trending down across two consecutive cycles → reposition (legs up if ordered), recheck → call CRNA or anesthesiologist on call
- New bradycardia + hypotension → call anesthesiologist on call now, prepare for escalation per facility
- Altered mentation / nausea coincident with BP drop → call CRNA, prepare anti-emetic per order, recheck ASAP

## Questions to ask your preceptor
- How do you anticipate which patients are likely to drop post-spinal?
- What does our unit's protocol say about fluid bolus vs vasopressor timing?
- What level block did this patient have, and what's the expected timeline to resolution?

## One sentence to carry to your next shift
Post-spinal hypotension is a trend to catch early — watch two cycles, act on the second drift, not the first complaint.

## Sources
- *Drain's PeriAnesthesia Nursing*, Ch. on Regional Anesthesia / Neuraxial Block Management
- ASPAN *Core Curriculum for PeriAnesthesia Nursing Practice* — regional anesthesia module
```

Notes on what makes this example Tier 1: five items exactly, red flags all trigger → action → call-by-role, no numeric thresholds invented (all qualitative), preceptor questions are specific and askable, sources cited by chapter title not invented number.
</details>

## Self-check before returning

- [ ] ≤ 500 words.
- [ ] Five list items exactly.
- [ ] Red flags have action + call role.
- [ ] Jargon defined on first use.
- [ ] Sources cited by chapter.
- [ ] Safety reminder present.
- [ ] Verification section passed.
- [ ] False-Positive Prevention section passed — no invented doses, thresholds, equipment, or citations.
