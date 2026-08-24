---
title: Peer Preceptor 360 Feedback on a Shared Orientee
category: pacu/preceptor-evaluation
task_type: COMMUNICATE
audience: PACU preceptor submitting 360 feedback on an orientee they share with another primary preceptor
updated: "2026-04-16"
tags:
  - pacu
  - preceptor-evaluation
  - peer-feedback
  - 360
  - sbi
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-02
  - ED-02
  - DS-06
difficulty: intermediate
related_prompts:
  - prompts/pacu_orientee_evaluation_meta_prompt.md
  - prompts/pacu_preceptor_writing_orientee_evaluation.md
  - prompts/pacu_preceptor_calibration_facilitator.md
  - prompts/pacu_preceptor_approach_guide.md
references:
  - ASPAN Standards of Perianesthesia Nursing Practice
  - SBI feedback model (Center for Creative Leadership)
---

# Peer Preceptor 360 Feedback on a Shared Orientee

> Safety reminder: 360 feedback supplements, not replaces, the primary preceptor's evaluation. It does not substitute for facility sign-off documentation or patient-safety event reporting.

## Objective

Help a PACU preceptor submit useful 360 feedback on an orientee they share with another primary preceptor. Output is **Situation–Behavior–Impact (SBI)** feedback that is specific, vantage-pointed, bias-checked, and ready for the primary preceptor to synthesize alongside their own evidence.

## When to use

- You are a secondary preceptor, float, charge, or per-diem staff who has worked with the orientee but is not the primary preceptor.
- The primary preceptor has asked for 360 input, or your facility's orientation program includes multi-preceptor feedback.
- Output is actually going to help the orientee — not a box to check.

## What this prompt prevents

- Vague "great orientee" entries with no specifics.
- Personality labels ("shy," "too quiet," "arrogant") substituting for behavioral observation.
- Second-hand complaints passed along as your own observations.
- Anonymous potshots. If you wouldn't attach your name to it, don't submit it.

## Inputs

Ask one at a time.

- **Your relationship to the orientee:** {{secondary preceptor / charge / float / per-diem / cross-coverage / resource nurse}}
- **Frequency and recency of working together:** {{e.g., "Four shifts in the last six weeks — 03/15, 03/22, 04/02, 04/09"}}
- **Strengths you've observed firsthand:** 2–3 specific things.
- **Growth edges you've observed firsthand:** 1–2 things you'd want them to do differently. If your answer is "none," push back once — rare that a working colleague has none.
- **Specific examples** for each strength and each growth edge — shift date, case context, observed behavior.
- **Competency scaffold** from `pacu_orientee_evaluation_meta_prompt.md` — use it to scope your feedback to competencies you actually observed.
- **Your read on your own objectivity:** Is there anything about the working relationship (recent conflict, strong affinity, a rough code you were both in) that might color this?

## Audience / Scope

- **Primary user:** Peer preceptor submitting feedback.
- **Downstream consumer:** Primary preceptor synthesizing for `pacu_preceptor_writing_orientee_evaluation.md` and facilitator for `pacu_preceptor_calibration_facilitator.md`.
- **Scope:** Phase 1 PACU orientation only.

## Output requirements

```markdown
# Peer Preceptor 360 — {Orientee initials} — from {Peer role} — {Date}

> Safety reminder: 360 input, not sign-off. Primary preceptor owns the evaluation; facility protocol governs patient-safety reporting.

## Vantage Point (state honestly up front)
- Relationship: {secondary preceptor / charge / float / per-diem / cross-coverage}
- Frequency worked together: {high / medium / low}
- Recency: {last worked together = date}
- Shifts / cases worked together: {list with dates}
- Competencies I can actually speak to (from the scaffold): {list — omit what you didn't observe}

## Strengths (2–3 items, SBI each)
1. **{Short name for the strength.}**
   - Situation: {shift date, case context — e.g., "04/02 PM shift, post-laparoscopic chole with PONV"}
   - Behavior: {observable behavior only — what they actually did}
   - Impact: {what changed for the patient, team, handoff, or orientation pace}
2. ...

## Growth Edges (1–2 items, SBI each — phrased as desired changes, not labels)
1. **{Short name for the growth edge — named as a desired change.}**
   - Situation: {shift date, case context}
   - Behavior: {what you observed them do or not do}
   - Impact: {what changed or what was at risk}
   - Suggested change (optional): {specific, observable, next-phase-actionable}
2. ...

## A Note on My Objectivity
{One to two sentences. If nothing to flag, say so explicitly.}

## What I Am NOT Commenting On
{Competencies I did not observe enough to speak to — leave to the primary preceptor.}

## Sources / reference
- ASPAN *Standards of Perianesthesia Nursing Practice*, {relevant section (if anchoring a specific observation to a standard)}
- *Drain's PeriAnesthesia Nursing*, {chapter (if applicable)}
- Facility orientation program 360 / peer-feedback policy: {{per facility protocol}}
```

## Process (walk through before submitting)

### Step 1 — State vantage point
Every 360 submission opens with the peer's vantage point so the primary preceptor can weight it. If you worked two shifts together, say so — it's context, not a weakness.

### Step 2 — Convert every observation to SBI
For every strength and growth edge:
- **Situation:** When and where. Specific enough that the orientee would recognize it.
- **Behavior:** What the orientee actually did — observable, not your interpretation.
- **Impact:** What changed for the patient, the handoff, the team, or the orientation pace.

If you cannot produce a Situation and Behavior, cut the claim. Vague "great teammate" with no SBI is a downgrade, not feedback.

### Step 3 — PACU-adapted bias check
Ask explicitly:
- **Recency:** Is my feedback only about the last shift? Can I surface earlier?
- **Halo / horns:** Is one strong impression (a great save, a rough code) coloring everything?
- **Similar-to-me:** Am I rewarding or penalizing things that are about similarity to me, not PACU performance?
- **ICU-halo / prior-unit bias:** Am I reading the orientee's prior-unit background as a signal of PACU competence?
- **One-bad-shift recency:** Did one rough shift dominate my draft?
- **Retaliation / friendship:** Am I softening or sharpening based on the personal relationship?

If a real bias surfaces, adjust. If you can't adjust honestly, decline to submit and tell the primary preceptor why.

### Step 4 — Kindness and utility check
Re-read the draft. Ask:
- If I received this wording, would it be useful?
- Would I be willing to have my name attached, even if the process is anonymous?
- If no — rewrite.

### Step 5 — Scope honestly
If you didn't observe PONV escalation, don't comment on PONV escalation. List what you're **not** commenting on under "What I Am NOT Commenting On" — that's useful information for the primary preceptor.

## Must / Must not

**Must:**
- State vantage point, frequency, and recency.
- Use SBI structure for every strength and growth edge.
- Run the PACU-adapted bias check.
- Name growth edges as desired changes, not labels.
- Cite shift dates, case contexts, and observed behaviors.
- Explicitly list competencies you did **not** observe.

**Must not:**
- Use personality labels ("shy," "arrogant," "too passive," "aggressive," "nice," "difficult"). Translate to behavior.
- Submit anonymous potshots.
- Reference age, race, sex, disability, religion, national origin, pregnancy, or other protected characteristics.
- Speculate about medical or family circumstances.
- Comment on something you did not directly observe (don't pass along the unit's rumor as your observation).
- Reference license pathway (BSN/ASN/LPN-bridge) as a signal.
- Include patient-identifying information (MRN, full name, date of birth, room number).
- Document medication errors that haven't been reported through the facility's incident-reporting system.
- Let a recent conflict or strong affinity drive the draft.
- Submit feedback you couldn't defend in a direct conversation with the orientee.

## Quality signals

- Every strength and growth edge has Situation, Behavior, Impact anchored to a specific shift.
- Vantage point is stated honestly; low frequency is acknowledged.
- Growth edges are phrased as desired changes, actionable for the orientee next phase.
- At least one bias was audited and either adjusted or explicitly found clean.
- Peer has explicitly scoped what they can **not** speak to.

## Verification

Before submitting, verify:

- [ ] Vantage-point block states relationship + frequency + recency + dated shifts.
- [ ] Every strength and every growth edge has Situation + Behavior + Impact, each anchored to a dated shift.
- [ ] Growth edges are phrased as desired changes, not labels.
- [ ] "Competencies I can actually speak to" is scoped to what you observed; "What I Am NOT Commenting On" lists what you can't.
- [ ] Bias check has a finding AND an adjustment (or explicit "nothing to adjust — here's why").
- [ ] You would be comfortable attaching your name to the submission.

## False-Positive Prevention

Do **not** fabricate:

- **No invented shift dates, times, cases, or observations.** If you did not see it, do not write it.
- **No second-hand observations passed as your own.** If the rumor is the unit's, flag it to the primary preceptor separately — do not put it in a 360.
- **No personality labels** ("shy," "arrogant," "nice," "difficult," "too quiet"). Translate to what the orientee did or said.
- **No references to age, race, sex, disability, religion, national origin, pregnancy, license pathway, or prior unit as signals.**
- **No speculation about medical, mental-health, or family circumstances.**
- **No patient-identifying information** (MRN, full name, full DOB, room number).
- **No invented competency rubric weights or facility-specific thresholds.**
- **No anonymous potshots.** If you wouldn't defend the sentence in a direct conversation with the orientee, cut it.

## Worked Example

<details>
<summary>Example: SBI growth edge from a secondary preceptor, 4 shared shifts (click to expand)</summary>

```markdown
## Growth Edges (1–2 items, SBI each — phrased as desired changes, not labels)

1. **Verbalize a differential before completing the PACU checklist when vitals trend.**
   - Situation: 04/02 PM shift, post-laparoscopic chole patient, bay 4; BP trended 118/74 → 108/68 → 102/62 across first three cycles of admission assessment.
   - Behavior: Orientee continued through the standard PACU admission checklist (lines, Foley check, incisions) without verbalizing the BP trend. When I asked, "what's the trend telling you?", they correctly named post-spinal vasodilation plus possible residual volume depletion, and then escalated appropriately.
   - Impact: Cue-recognition lagged ~3 minutes behind what the pattern already showed; escalation was still within a safe window but slower than it needed to be.
   - Suggested change: When any vital drifts outside expected range during admission, verbalize a two-item differential before completing the rest of the checklist. Observable by any preceptor on 3 of 4 shifts next phase.
```

Notes on what makes this Tier 1: Situation is specific to a single shift + bay; Behavior is observable; Impact is stated without catastrophizing ("still within a safe window" is honest); suggested change is measurable.
</details>

## Self-check

- [ ] Vantage point stated honestly up front.
- [ ] Every strength and growth edge uses SBI with shift/date anchors.
- [ ] No personality labels.
- [ ] No protected-characteristic references; no medical or family speculation.
- [ ] No patient-identifying information.
- [ ] PACU-adapted bias check run; adjustment noted or explicit "nothing to adjust."
- [ ] "What I Am NOT Commenting On" is explicit.
- [ ] I would be comfortable with my name attached to this feedback.
- [ ] Safety reminder at top.
- [ ] Verification section passed.
- [ ] False-Positive Prevention section passed — no invented observations, second-hand observations, or personality labels.
