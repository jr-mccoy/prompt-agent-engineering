---
title: PACU Orientation Skill Acquisition Timeline
category: pacu/orientation-curriculum
task_type: CREATE
audience: PACU educator or preceptor mapping expected cueing-decay across orientation
updated: "2026-05-15"
tags:
  - pacu
  - orientation
  - skill-acquisition
  - cueing-decay
  - benner
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - ED-02
  - DS-06
difficulty: advanced
related_prompts:
  - prompts/pacu_orientation_curriculum_designer.md
  - prompts/pacu_orientee_weekly_learning_plan.md
  - prompts/pacu_preceptor_orientation_pacing_diagnostic.md
  - prompts/pacu_orientee_evaluation_meta_prompt.md
references:
  - ASPAN Standards of Perianesthesia Nursing Practice
  - Drain's PeriAnesthesia Nursing Practice (7th ed.)
  - Benner, P. — From Novice to Expert
---

# PACU Orientation Skill Acquisition Timeline

> Safety reminder: This is an expected-trajectory tool, not a target the orientee must hit. Actual cueing-decay varies by orientee, case mix, and exposure. Verify against facility orientation framework before using to anchor expectations.

## Objective

Produce a **skill-by-skill cueing-decay timeline** showing expected sign-off levels (Independent / With Cues / With Direction / Not Yet) by week for each PACU competency, adapted to the orientee's background and the orientation length. Used to calibrate expectations — preceptors can tell when an orientee is on, ahead of, or behind the typical curve.

## Inputs

- **Orientation length:** {{N weeks}}
- **Orientee background:** {{new-grad | experienced med-surg | experienced ICU | experienced ED | experienced L&D | float refresh | cross-specialty transfer}}
- **Competency list (default or facility-supplied):** {{paste or use ASPAN default}}
- **Known compressors / expanders:** {{e.g., prior PALS/TNCC, no peds rotation, condensed timeline}}

## Audience / Scope

- **Primary:** Preceptor or educator setting expectations at orientation kickoff.
- **Secondary:** `pacu_preceptor_orientation_pacing_diagnostic.md` uses this as the reference curve.
- **Scope:** Phase 1 PACU orientation timeline. Not a sign-off threshold (the evaluation suite produces those).

## Output requirements

```markdown
# Skill Acquisition Timeline — {Background}, {N} weeks

> Safety reminder: Expected trajectory only — orientees vary. Use as a calibration tool, not a sign-off gate.

## Reading the table

- **Independent (I):** performs reliably without cue; reasoning explicit on debrief.
- **With Cues (C):** performs with brief situational cue; usually internalizes after.
- **With Direction (D):** performs only with step-by-step guidance.
- **Not Yet (N):** not expected this week.

## Cueing-decay grid

| Competency | Wk 0 | Wk 1 | Wk 2 | Wk 3 | Wk 4 | Wk {…} | Wk N |
|---|---|---|---|---|---|---|---|
| Airway & breathing management | N | D | D | C | C | … | I |
| Hemodynamic assessment & intervention | N | D | D | C | C | … | I |
| Oxygenation & ventilation | N | D | D | C | C | … | I |
| Post-op pain management | N | D | C | C | C | … | I |
| PONV recognition & escalation | N | D | C | C | I | … | I |
| Emergence & delirium assessment | N | N | D | D | C | … | I |
| Regional / neuraxial block assessment | N | N | D | D | C | … | I |
| Handoff communication (inbound) | N | D | C | C | I | … | I |
| Handoff communication (outbound) | N | D | C | C | I | … | I |
| Family communication & discharge teaching | N | N | D | C | C | … | I |
| Clinical judgment in ambiguity | N | N | D | D | D | … | I |
| Documentation accuracy | N | D | C | C | I | … | I |
| Team collaboration & role recognition | N | D | C | C | I | … | I |

(Adjust columns to match orientation length exactly.)

## Background-specific adjustments

Paragraph naming exactly which cells shift earlier or later because of background:
- For experienced ICU RN: airway, hemodynamics, oxygenation, documentation may shift one column earlier; regional block, emergence phenomena, family communication, and clinical judgment in PACU-specific ambiguity stay on the default curve (ICU-halo risk — flag if the orientee or preceptor assumes these will compress too).
- For new-grad: handoff communication may stay at D one week longer; judgment-in-ambiguity often the slowest curve.
- For cross-specialty transfer (L&D, ED, OR): name which axes transfer and which don't.

## How to use this timeline

- **At kickoff:** review with orientee. Frame as "what's typical, not what you must hit."
- **Mid-orientation:** compare orientee's current cueing-decay to the row for the current week. Use `pacu_preceptor_orientation_pacing_diagnostic.md` for the gap analysis.
- **At sign-off:** the timeline is not the sign-off rubric. The evaluation suite produces the rubric. Use the timeline only to contextualize trajectory.

## What this timeline is not

- Not a contract with the orientee.
- Not a sign-off rubric (use `pacu_orientee_evaluation_meta_prompt.md`).
- Not a comparison-across-orientees tool — show only this orientee's row.
- Not an HR document.

## Sources / reference

- ASPAN *Standards* — competency scope.
- Benner — novice-to-expert framing for the cueing-decay concept.
```

## Must / Must not

**Must:**
- Use the **I / C / D / N** scale consistently — no other tokens.
- Match column count to orientation length exactly.
- Adapt cell values to the orientee's background visibly.
- Frame as "expected typical" not "required by week."
- Label ICU-halo risk explicitly when background is ICU.

**Must not:**
- Treat the timeline as a sign-off gate.
- Compare orientees to each other.
- Use the timeline to project the orientee's competency on a single shift (cueing-decay is a multi-shift signal).
- Reference protected characteristics or license pathway.
- Fabricate Benner's specific stage timelines (his model frames cueing-decay; we don't quote week-counts from his work).

## Quality signals

- A preceptor can look at the Week 4 column and answer "What should I expect today?" in one read.
- ICU-transfer and new-grad timelines visibly differ row-by-row.
- An orientee can read it without feeling like a deadline list.

## Verification

- [ ] Column count = orientation length.
- [ ] Scale tokens (I / C / D / N) consistent throughout.
- [ ] Background adjustments paragraph names at least 3 concrete shifts.
- [ ] ICU-halo risk flagged when background is ICU.
- [ ] Timeline framed as expected-typical, not contractual.
- [ ] Safety reminder + FPP sections present.

## False-Positive Prevention

- **No fabricated Benner stage week-counts** — Benner frames cueing-decay; do not assign specific weeks to his stages.
- **No invented ASPAN-supplied trajectory data.**
- **No facility-specific scope-of-practice claims.**
- **No comparison-to-other-orientees data.**
- **No invented competency thresholds** ("must be at C by Week 4 to advance").
- **No invented patient-acuity tiers** as competency progression triggers.
- **No protected-characteristic or license-pathway adjustments to the curve.**

## Worked Example

<details>
<summary>Example: 10-week orientation, experienced ICU RN, ortho-heavy unit (click to expand, abbreviated)</summary>

```markdown
## Cueing-decay grid

| Competency | Wk 0 | Wk 1 | Wk 2 | Wk 3 | Wk 4 | Wk 5 | Wk 6 | Wk 7 | Wk 8 | Wk 9 | Wk 10 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Airway & breathing | N | D | C | C | C | I | I | I | I | I | I |
| Hemodynamic assessment | N | D | C | C | C | I | I | I | I | I | I |
| Oxygenation & ventilation | N | D | C | C | I | I | I | I | I | I | I |
| Post-op pain | N | D | D | C | C | C | I | I | I | I | I |
| PONV | N | D | C | C | I | I | I | I | I | I | I |
| Emergence & delirium | N | N | D | D | C | C | C | I | I | I | I |
| Regional block | N | N | D | D | C | C | C | C | I | I | I |
| Handoff inbound | N | D | C | C | I | I | I | I | I | I | I |
| Handoff outbound | N | D | C | C | I | I | I | I | I | I | I |
| Family comms | N | N | D | C | C | C | I | I | I | I | I |
| Judgment in ambiguity | N | N | D | D | D | C | C | C | I | I | I |
| Documentation | N | D | C | C | I | I | I | I | I | I | I |
| Team collab | N | D | C | C | I | I | I | I | I | I | I |

## Background-specific adjustments

Airway, hemodynamics, oxygenation, handoffs, documentation, and team collaboration are accelerated one column earlier than the default curve because this orientee carries 4 years of ICU practice in titration, monitoring, and SBAR. Emergence phenomena, regional block resolution, and family communication in the post-anesthesia context stay on the default curve — these are PACU-distinctive and do not transfer from ICU. ICU-halo risk is highest at Week 4: airway/hemodynamics will appear independent, which is true, but emergence and regional block competencies will still be at C — preceptor should not generalize the I to the whole orientee.
```

Notes: scale consistent, columns = 11 (W0–W10), ICU-halo risk explicit, default curve and adjusted curve visibly different.
</details>

## Self-check

- [ ] Scale I/C/D/N consistent.
- [ ] Column count matches orientation length.
- [ ] Background adjustments named concretely.
- [ ] ICU-halo flagged when relevant.
- [ ] Frame "typical, not contractual."
- [ ] FPP section passed.
