---
title: PACU Preceptor Orientation Pacing Diagnostic
category: pacu/orientation-curriculum
task_type: ANALYZE
audience: PACU primary preceptor mid-orientation, diagnosing whether the orientee is ahead, on, or behind pace
updated: "2026-05-15"
tags:
  - pacu
  - orientation
  - pacing
  - diagnostic
  - preceptor
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - QA-02
  - ED-02
difficulty: advanced
related_prompts:
  - prompts/pacu_orientation_skill_acquisition_timeline.md
  - prompts/pacu_orientation_topic_sequencing_optimizer.md
  - prompts/pacu_background_specific_pathway_adapter.md
  - prompts/pacu_preceptor_debrief.md
  - prompts/pacu_orientee_evaluation_meta_prompt.md
references:
  - ASPAN Standards of Perianesthesia Nursing Practice
  - Benner, P. — From Novice to Expert
---

# PACU Preceptor Orientation Pacing Diagnostic

> Safety reminder: Diagnostic surfaces pacing concerns. It does not replace formal evaluation, sign-off decisions, or HR processes. Use the v2 Preceptor Evaluation Suite for formal evaluation.

## Objective

Produce a **pacing diagnostic** mid-orientation: is the orientee ahead, on, or behind expected pace, on which axes, and by how much? Output drives `pacu_orientation_topic_sequencing_optimizer.md` (re-sequence next 2–3 weeks) or surfaces the need for a formal mid-orientation evaluation.

## Inputs

- **Current week / total weeks:** {{e.g., Week 5 of 10}}
- **Expected cueing-decay row from skill-acquisition timeline:** {{paste row for current week}}
- **Observed cueing-decay state by competency:** {{from rolling debrief log and recent shifts}}
- **Background-specific adjustments applied:** {{paste from pathway adapter}}
- **Open commitments from prior debriefs:** {{from rolling log}}
- **Any specific concerning shift events:** {{e.g., missed BP trend, late escalation — describe by behavior, not character}}

## Audience / Scope

- **Primary:** Primary preceptor (the one who runs the diagnostic).
- **Secondary:** Educator (gets the summary).
- **Scope:** Pacing only. Formal evaluation: `pacu_orientee_evaluation_meta_prompt.md` + downstream evaluation suite.

## Output requirements

```markdown
# Pacing Diagnostic — Wk {n} of {N}

> Safety reminder: Pacing only. Not a formal evaluation. Not an HR document.

**Background context:** {one line with declared background + applied adjustments}

## Headline

One sentence: "On pace overall." / "Ahead on {axes}, on pace on {axes}, behind on {axes}." / "Behind across multiple foundations — recommend mid-orientation evaluation."

## Axis-by-axis comparison

| Competency | Expected this week | Observed | Delta | Concern level |
|---|---|---|---|---|
| Airway & breathing | I | I | 0 | none |
| Hemodynamics | C | C | 0 | none |
| PONV | I | C | -1 | watch |
| Emergence | C | D | -1 | watch |
| Regional block | C | D | -1 | watch |
| Judgment in ambiguity | D | D | 0 | on pace, but absolute level low |
| Handoff inbound | I | I | 0 | none |
| (etc.) |  |  |  |  |

Use the **I / C / D / N** scale; delta is in scale-positions (+ = ahead, − = behind).

## Pattern read (3–5 sentences)

What story do the deltas tell? Examples:
- "Foundations are on pace; PACU-distinctive content (emergence, regional) is one column behind, consistent with declared cross-specialty transfer pattern."
- "Ahead on documentation and basics; behind on judgment-in-ambiguity, which is the long-tail competency — expected, not alarming yet."
- "Behind on three foundations and PACU-distinctive content — concerning; recommend mid-orientation evaluation now, not at Wk 8."

## Bias check

Run through the bias list before concluding:
- **ICU-halo:** am I generalizing strong airway/hemo performance to other axes?
- **Confidence-as-competence:** is the orientee speaking fluently in places where cueing-decay is actually still high?
- **Conflict-aversion leniency:** am I rating "on pace" because I don't want to start a hard conversation?
- **Recency / one-bad-shift:** am I rating "behind" based on the last shift rather than the multi-shift trend?
- **ICU-tenure / prior-unit halo or anti-halo:** am I letting prior unit reputation shape my read?
- **License-pathway bias:** do not consider — this is a "do not" reminder, not a question to answer.

State which biases applied and how you adjusted.

## Recommendation

One of:
- **Stay course:** continue current pathway; debrief themes carry forward.
- **Re-sequence next 2–3 weeks:** run `pacu_orientation_topic_sequencing_optimizer.md`.
- **Adjust pathway adaptation:** run `pacu_background_specific_pathway_adapter.md` with new evidence.
- **Trigger mid-orientation evaluation:** run `pacu_orientee_evaluation_meta_prompt.md` for the mid-orientation evaluation type.
- **Trigger remediation conversation:** see Preceptor Evaluation Suite v2.

State the recommendation clearly and the trigger that produced it.

## What this diagnostic is not

- Not a formal evaluation.
- Not a sign-off recommendation.
- Not an HR document.
- Not shareable outside the preceptor / educator relationship without orientee awareness.

## Sources / reference

- ASPAN *Standards* — competency framework.
- Benner — cueing-decay framing.
- Facility orientation program for evaluation triggers.
```

## Must / Must not

**Must:**
- Use **I / C / D / N** scale tokens.
- Run the bias check explicitly before concluding.
- Tie the recommendation to a downstream prompt.
- Distinguish "behind in absolute level" from "behind relative to expected pace" — they call for different actions.
- State that the diagnostic is not a formal evaluation.

**Must not:**
- Conflate pacing with sign-off decision.
- Project a single concerning event as the full pacing picture.
- Reference protected characteristics.
- Use license pathway or RN tenure as a pacing signal.
- Generate the diagnostic without the bias check.
- Fabricate concerning events not in the input.

## Quality signals

- Two preceptors running this on the same inputs converge on the same headline.
- The bias check produces at least one named adjustment.
- The recommendation is concrete enough to act on in the next preceptor shift plan.

## Verification

- [ ] Scale tokens I/C/D/N used.
- [ ] Every axis has Expected, Observed, Delta, Concern.
- [ ] Pattern-read sentences interpret the deltas, not just list them.
- [ ] Bias check completed with named adjustments.
- [ ] Recommendation ties to a downstream prompt.
- [ ] "Not a formal evaluation" statement present.
- [ ] Safety + FPP sections present.

## False-Positive Prevention

- **No invented shift events** — only use events the user pasted.
- **No invented prior-debrief commitments.**
- **No invented competency thresholds** ("must close a 2-position gap in 2 weeks or remediate").
- **No invented Benner stage timings.**
- **No protected-characteristic content** in the pattern read or bias check answers.
- **No license-pathway-based pacing interpretation.**
- **No prior-unit-reputation-based pacing claims** — flag as bias, not as input.
- **No invented HR triggers** — defer to facility orientation program.

## Worked Example

<details>
<summary>Example: Wk 5 of 10, experienced ICU RN, foundations strong, PACU-distinctive lagging (click to expand)</summary>

```markdown
# Pacing Diagnostic — Wk 5 of 10

**Background context:** Experienced ICU RN, 4 yrs. Pathway adapter compressed airway/hemo/SBAR/documentation; preserved emergence/regional/family/judgment.

## Headline

Ahead on foundations; on pace on emergence and family; behind one position on regional block; recommend re-sequence next 2 weeks.

## Axis-by-axis

| Competency | Expected | Observed | Delta | Concern |
|---|---|---|---|---|
| Airway | I | I | 0 | none |
| Hemo | I | I | 0 | none |
| PONV | I | I | 0 | none |
| Emergence | C | C | 0 | none |
| Regional | C | D | -1 | watch |
| Judgment | D | D | 0 | on pace |
| Handoffs | I | I | 0 | none |
| Family | C | C | 0 | none |
| Documentation | I | I | 0 | none |

## Pattern read

ICU-transfer pattern is holding: foundations accelerated as compression predicted; PACU-distinctive content stayed near default curve. One axis (regional block) is one position behind — most likely explanation is exposure: only 3 spinal recoveries so far this orientation. This is exposure-driven pacing, not competency-driven.

## Bias check

- ICU-halo: checked — foundations Independent appears genuine, not generalized.
- Confidence-as-competence: checked on regional — orientee speaks fluently about pathophys but cueing-decay says D. Confidence is outpacing competence on regional specifically. Adjustment: keep current rating, do not lift to C until cueing-decay observed.
- Conflict-aversion: no — this read is concrete with no soft language.
- Recency: averaged across last 4 shifts.
- License pathway: not used.

## Recommendation

Re-sequence: run `pacu_orientation_topic_sequencing_optimizer.md` to advance regional block content to Wk 6, leveraging Mon ortho-spinal day. No mid-orientation evaluation needed yet.
```

Notes: scale tokens consistent, bias check produced named adjustment, recommendation specific.
</details>

## Self-check

- [ ] Scale tokens used.
- [ ] Every axis has 4 columns.
- [ ] Pattern read interprets, doesn't list.
- [ ] Bias check completed.
- [ ] Recommendation ties to downstream prompt.
- [ ] "Not a formal evaluation" stated.
- [ ] FPP section passed.
