---
title: PACU Preceptor Approach Guide — Preparing to Evaluate an Orientee
category: pacu/preceptor-evaluation
task_type: IMPROVE
audience: PACU preceptor preparing to write a mid-orientation or final sign-off evaluation
updated: "2026-04-16"
tags:
  - pacu
  - preceptor-evaluation
  - preparation
  - bias
  - evidence
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-02
  - ED-02
  - DS-06
difficulty: advanced
related_prompts:
  - prompts/pacu_orientee_evaluation_meta_prompt.md
  - prompts/pacu_preceptor_writing_orientee_evaluation.md
  - prompts/pacu_preceptor_debrief.md
  - prompts/pacu_preceptor_calibration_facilitator.md
  - prompts/pacu_preceptor_difficult_conversation_guide.md
  - prompts/pacu_orientee_remediation_plan.md
references:
  - ASPAN Standards of Perianesthesia Nursing Practice
  - Drain's PeriAnesthesia Nursing Practice (7th ed.)
  - ASPAN Core Curriculum for PeriAnesthesia Nursing Practice
  - Cognitive bias literature on rater effects (recency, halo, similar-to-me)
---

# PACU Preceptor Approach Guide — Preparing to Evaluate an Orientee

> Safety reminder: This is preparation coaching, not the evaluation. It does not substitute for facility sign-off documentation or patient-safety event reporting.

## Objective

Walk a PACU preceptor through the preparation that happens **before** they draft an orientee evaluation — consolidating shift-by-shift evidence, auditing nursing-specific biases, surprise-checking critical feedback, and rehearsing delivery. Output is a written prep artifact the preceptor brings to the drafting step (`pacu_preceptor_writing_orientee_evaluation.md`).

## When to use

- You are about to write a mid-orientation checkpoint or a final sign-off narrative.
- You have not yet started drafting. Stop. Run this first.
- Do **not** use this to write the evaluation itself — that's a separate prompt.

## Inputs

Ask one at a time. Do not proceed until each is answered concretely.

- **Orientee identifier:** {{initials or placeholder}} — use consistently throughout.
- **Orientation phase & evaluation type:** {{Week 0–2 / Week 2–6 / Week 6–10 / final sign-off / probationary extension}}
- **Orientee background:** {{new-grad RN / experienced RN transitioning / float-pool / cross-specialty transfer}}
- **Time you've precepted them:** {{weeks, approximate hours, approximate shifts}}
- **Current instinct:** In one sentence, what sign-off disposition are you leaning toward? (Advance / extend / remediation)
- **Evidence sources you already have:** Debrief summaries (`pacu_preceptor_debrief.md` rolling log), competency self-assessments, charting review, code/event documentation, peer preceptor input, handoff observations.
- **Evidence sources you haven't reviewed yet:** Which of the above exist but you haven't consolidated?
- **Scaffold from `pacu_orientee_evaluation_meta_prompt.md`:** {{paste or reference}}

## Audience / Scope

- **Primary:** PACU preceptor preparing a formal orientee evaluation.
- **Secondary:** Educator or charge nurse validating the preceptor's readiness to evaluate.
- **Scope:** Phase 1 PACU orientation. For post-orientation staff review, defer to facility HR tooling.

## Output requirements

Produce a single written artifact the preceptor pastes into their drafting session:

```markdown
# Evaluation Prep — {Orientee initials} — {Phase / type} — {Date}

> Safety reminder: Prep only. Verify against facility orientation program and ASPAN Standards before drafting.

## 1. Evidence Inventory (fight recency bias)

Build a shift-by-shift or week-by-week grid across the full phase being evaluated.

| Week / Shift | Cases / context | Orientee behavior observed (specific) | Cueing level | Citation (debrief date, chart, event) |
|---|---|---|---|---|
| ... | ... | ... | Independent / With Cues / With Direction / Not Yet | ... |

Flag explicitly any week with **`GAP`** (no evidence captured). Ask yourself why — was it a light schedule, or were you not documenting?
Flag explicitly any claim you want to make with no citation as **`UNSUPPORTED`**. Either go get evidence (name the source) or cut the claim.

## 2. Bias Audit (PACU-adapted)

For each bias, record your finding and the adjustment you'll make.

| Bias | Question to ask yourself | Finding | Adjustment |
|---|---|---|---|
| Recency | Can I name three concrete things from the first half of the phase without checking notes? | | |
| Halo / Horns | Is one strong impression (great save, rough shift) coloring everything? | | |
| Similar-to-me | Am I rewarding traits that are about familiarity (same school, same prior unit, same personality style) rather than PACU performance? | | |
| Leniency / Severity | How does my proposed disposition compare to what I've given other orientees at this phase? | | |
| Central tendency | If every competency is "With Cues," is that accurate or safer than the evidence supports? | | |
| Idiosyncratic rater | Am I rating a competency low because I'm strong at it and hold a higher bar than the role requires? | | |
| Attribution | When something went wrong, did I attribute it to the orientee's character? When it went right, to the situation? | | |
| **ICU-halo** (PACU-specific) | Am I assuming ICU-background competence transfers to PACU-specific physiology (emergence, neuraxial assessment, PONV escalation)? | | |
| **One-bad-shift recency** | Is one rough shift coloring the whole phase? | | |
| **"I trained them so they must be ready"** | Am I advancing this orientee because I want my teaching to have worked, rather than because the evidence supports it? | | |
| **Conflict-aversion leniency** | Am I softening my disposition to avoid extending orientation and the friction that creates? | | |
| **License-pathway / prior-unit bias** | Am I reading BSN-vs-ASN or ICU-vs-floor background as a performance signal? It is not. | | |

## 3. "Tempted to say but can't support" test

List three things you're tempted to write that you cannot back with a specific, datable, observable example. For each:
- Go get evidence (name the source), or
- Cut the claim.

Do not keep a claim because "the whole unit knows it." Name the source.

## 4. Surprise Check (no-surprises principle)

For every major piece of feedback you plan to include:
- Has this been delivered in a prior debrief (`pacu_preceptor_debrief.md`) or real-time cueing on shift? [Y/N]
- Would the orientee recognize it if they read the sentence cold?
- If no — this is a first-time-feedback landmine. Plan to deliver it in a 1:1 **before** the written evaluation lands, or use `pacu_preceptor_difficult_conversation_guide.md` to structure that conversation.

## 5. Delivery Prep

- Draft 2–3 conversation openers for the evaluation 1:1. Tone: honest, calm, not apologetic.
- Identify the **single hardest sentence** in the evaluation. Write the exact wording. Say it out loud.
- Anticipate orientee reactions (defensive, emotional, dismissive, blindsided, grateful) and a brief plan for each.
- What you will **not** negotiate in the 1:1: sign-off disposition, patient-safety events, rubric criteria, escalation expectations.

## Ready-to-draft check
- [ ] Evidence grid covers the full phase (not just the last 2 weeks).
- [ ] At least one bias identified and at least one framing revised.
- [ ] Every claim I plan to write has a specific example attached.
- [ ] No critical feedback in this evaluation will be new to the orientee.
- [ ] I know the hardest sentence and can say it out loud.

## Sources / reference
- ASPAN *Standards of Perianesthesia Nursing Practice*, {relevant sections}
- *Drain's PeriAnesthesia Nursing*, {relevant chapters}
- Facility orientation program document (where applicable).
```

## Must / Must not

**Must:**
- Require a specific observable example for every claim.
- Surface gaps and biases by name, not hints.
- Push back if the preceptor's instinct is not supported by the evidence they've consolidated.
- Treat "I've been with them every shift, trust me" as insufficient — consolidate the evidence grid anyway.
- Verify every concern has been raised in a prior debrief before it lands in writing.
- Name escalation partners by role (charge, CRNA, anesthesiologist on call, rapid response), never by name.

**Must not:**
- Draft the evaluation itself — that's `pacu_preceptor_writing_orientee_evaluation.md`.
- Reference age, race, sex, disability, religion, national origin, pregnancy, or other protected characteristics.
- Infer medical or family circumstances ("seems burned out," "must be distracted by things at home") — refer the orientee to the facility EAP if concern exists.
- Use personality labels as feedback ("shy," "arrogant," "too passive," "aggressive") — translate to observable behavior.
- Reference license pathway (BSN/ASN/LPN-bridge) or prior unit as performance signal.
- Invent doses, equipment specifics, pager numbers, or facility protocols — defer to `{{per facility protocol}}`.
- Coach the preceptor to soften critical feedback into meaninglessness. Honest and kind, not honest or kind.
- Document medication errors that have not been reported through the facility's incident-reporting system — a remediation plan is not a substitute for a patient-safety event report.

## Quality signals

- The preceptor walks away with an evidence grid, a bias-audit record, a surprise-check log, and a rehearsed hardest sentence.
- At least one framing was revised by the bias audit.
- No feedback item will be new to the orientee when they read the written evaluation.

## Verification

Before handing the prep artifact to the drafting step, verify:

- [ ] Evidence grid has shift-level or week-level rows for the full phase, not just recent shifts.
- [ ] Every **`GAP`** row and every **`UNSUPPORTED`** claim has an explicit disposition (go get evidence, or cut).
- [ ] Bias audit has a Finding and an Adjustment filled in for each row — blank rows do not count as "clean."
- [ ] At least one first-time-feedback risk is identified and has a plan (deliver live first, or run difficult-conversation prep).
- [ ] The hardest sentence is written verbatim (not paraphrased, not softened) and has been said out loud.

## False-Positive Prevention

Do **not** fabricate:

- **No invented shift dates, times, or observations.** If the preceptor did not give the evidence, do not generate it.
- **No invented orientee demographics, prior-unit details, or license-pathway inferences.**
- **No speculation about the orientee's medical, mental-health, or family circumstances.** EAP by role only.
- **No invented facility policies, HR process specifics, or timelines.**
- **No invented ASPAN chapter/section citations.** Mark `{{confirm}}` if unknown.
- **No personality labels in any output cell** — translate to observable behavior before it lands in the grid.
- **No references to age, race, sex, disability, religion, national origin, pregnancy, license pathway, or prior unit as performance signals.**
- **No invented disposition norms** ("at our facility, Week 6 new-grads are usually at X level") — facility-specific, defer to facility.

## Worked Example

<details>
<summary>Example: Bias-audit snippet for a preceptor leaning "Extend" on a Week 8 orientee (click to expand)</summary>

```markdown
## 2. Bias Audit (PACU-adapted)

| Bias | Question to ask yourself | Finding | Adjustment |
|---|---|---|---|
| Recency | Three concrete first-half items without notes? | Yes — Week 3 PONV save, Week 4 handoff template, Week 5 SBAR to CRNA. Clean. | None needed on recency. |
| Halo / Horns | Is one impression coloring everything? | The rough Week 7 residual-blockade case is coloring Week 8. | Re-read Weeks 5–6 notes before drafting Week 8's rating. |
| Similar-to-me | Rewarding familiarity? | No affinity or aversion flags. | — |
| ICU-halo | Is prior-ICU background being read as PACU-ready? | Orientee is new-grad; not applicable. | — |
| One-bad-shift recency | One rough shift dominating? | **Yes.** Week 7 residual-blockade case was rough, but isolated. Competency over 7 weeks is trending toward "With Cues." | Flag Week 7 as a specific growth edge, not a disposition driver. Revisit Extend vs Advance on strength of Weeks 3–6 pattern. |
| "I trained them" | Advancing because my teaching worked? | No pressure either direction. | — |
| Conflict-aversion leniency | Softening to avoid friction? | **Possibly.** Extending feels less awkward than documenting "With Cues" and the family-communication gap. | Do not let awkwardness set the disposition. Evidence, not friction, sets it. |
| License-pathway / prior-unit | Using BSN/ASN or prior unit? | Not applicable (new-grad). | — |
```

Notes: two biases explicitly flagged, adjustments name specific actions, preceptor has a concrete checkpoint (revisit after re-reading Weeks 5–6) before disposition is finalized.
</details>

## Self-check

- [ ] All four inputs captured before starting.
- [ ] Evidence grid covers the full phase with shift-/week-level granularity.
- [ ] Bias audit includes PACU-specific biases (ICU-halo, one-bad-shift, "I trained them," conflict-aversion, license-pathway).
- [ ] Unsupported claims either evidenced or cut.
- [ ] Every feedback item has been previously delivered or has a plan to be delivered live first.
- [ ] Hardest sentence drafted verbatim.
- [ ] No protected-characteristic references.
- [ ] Safety reminder at top.
- [ ] Verification section passed.
- [ ] False-Positive Prevention section passed — no invented observations, personality labels, or facility policies.
