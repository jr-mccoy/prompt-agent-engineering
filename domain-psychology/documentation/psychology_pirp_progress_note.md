---
title: "PIRP-Format Progress Note Drafter"
category: psychology/documentation
description: "Draft a PIRP-format (Problem / Intervention / Response / Plan) progress note that anchors the encounter to the presenting clinical problem rather than to a behavior or a goal."
techniques:
  - ST-04
  - DT-02
  - QA-04
  - CM-02
difficulty: intermediate
tags:
  - progress-note
  - pirp
  - problem-anchored
  - golden-thread
intended_use: model-testing
updated: "2026-05-08"
related_prompts:
  - domain-psychology/documentation/psychology_birp_progress_note.md
  - domain-psychology/documentation/psychology_girp_progress_note.md
---

# PIRP-Format Progress Note Drafter

## Objective

Produce a problem-anchored progress note in **PIRP** format (**Problem / Intervention / Response / Plan**). Where GIRP starts at the goal level and BIRP starts at observable behavior, PIRP starts at the clinical problem the session is targeting — typically the diagnosis-linked problem statement from the treatment plan.

The note must:

1. Open with the active clinical problem(s) addressed — verbatim from the treatment plan's problem list — in **Problem**.
2. Document evidence-based interventions tagged to those problems in **Intervention**.
3. Document observable client response in **Response**.
4. Specify next steps in **Plan**.
5. Include a Presentation / MSE block so observational data and risk reassessment are not lost.

PIRP is common in IOP/PHP, CCBHC, and SUD programs where problem-list anchoring is required by funder.

## When to Use

- Payer/program requires PIRP.
- Treatment-plan format leads with a problem list (rather than a goal hierarchy).
- Program needs problem→intervention→response→plan traceability per session.

## Inputs / Context

- Session metadata (date, duration, modality, CPT/HCPCS, ICD-10, POS, treatment-plan goals/objectives addressed).
- **Verbatim text** of the active problem(s) from the treatment plan with their problem numbers and target review dates.
- Raw session content (client report, clinician observation, interventions, responses).
- MSE observations and outcome-measure scores.
- Risk indicators and any actions taken.
- Substance-use status if applicable.

## Constraints

### Must

- Output four labeled sections in order: **Problem**, **Intervention**, **Response**, **Plan**, with a **Presentation / MSE** block immediately after Problem.
- Quote the problem statement(s) verbatim under **Problem**, with problem number and most recent review date.
- Tag every Intervention to a specific problem number; interventions that don't map must be flagged `[off-problem: rationale]`.
- Each Intervention has a paired observable Response.
- Risk reassessment present in Presentation / MSE; risk actions in Intervention; risk follow-through in Plan.
- Billing block with CPT/HCPCS, time/units, and medical-necessity sentence.

### Must Not

- Do not paraphrase problem statements; quote verbatim.
- Do not omit Presentation / MSE.
- Do not log interventions without observable responses.
- Do not fabricate content; flag missing inputs.

## Instructions

1. Identify missing inputs.
2. Quote the active problem(s) verbatim under **Problem** with problem number and review date.
3. Add **Presentation / MSE** block: appearance, behavior, statements (quoted), MSE, measure scores, risk indicators, substance-use status.
4. Draft **Intervention** as bulleted list; each bullet names technique, gives concrete description, tags `[Problem #N]`.
5. Draft **Response** as parallel list of observable responses.
6. Draft **Plan** with next session, homework, coordination, medication, safety, clinician follow-up.
7. Append billing block.
8. Run verification.

## Output Format

```
=== PROGRESS NOTE (PIRP) ===

Client: [Initials/MRN]    DOB: [age, gender, pronouns]
Date of Service: [YYYY-MM-DD]    Time In/Out: [HH:MM–HH:MM]    Duration: [N min]
Place of Service: [POS]    Modality: [in-person | telehealth]
Code(s) billed: [CPT/HCPCS]    ICD-10: [codes]

PROBLEM
- Problem #X (last reviewed [YYYY-MM-DD]): "[Verbatim problem statement from treatment plan]"
- Problem #Y (last reviewed [YYYY-MM-DD]): "[Verbatim problem statement]"
Today's focus: [Problem #X primary; Problem #Y addressed briefly via psychoeducation.]

PRESENTATION / MSE
[Appearance, behavior, statements quoted; speech; mood (quoted); affect; TP; TC; cognition; insight; judgment.]
[Outcome measures: PHQ-9 = X (prior X / YYYY-MM-DD); GAD-7 = X; AUDIT = X.]
[Risk indicators: SI/HI/NSSI status as reported/observed.]
[Substance-use status if applicable: last use, intoxication / withdrawal, drug-screen results.]

INTERVENTION
- [Named technique #1 — concrete description] [Problem #X]
- [Named technique #2 — concrete description] [Problem #Y]
- [Risk-related action if applicable.]

RESPONSE
- [Observable response to Intervention #1.]
- [Observable response to Intervention #2.]
- [Response to risk-related action if applicable.]

PLAN
- Next session: [date / frequency / rationale if changing].
- Homework: [specific, measurable, review point].
- Coordination: [collateral contacts, referrals, ROI status, dates].
- Medication: [coordination notes].
- Safety: [safety plan status; means restriction; emergency contacts].
- Clinician follow-up: [tasks with target dates].

BILLING
[Code] x [units/minutes], POS [##]. Medical necessity: [one sentence tying active problem to today's interventions].

Clinician: [name, credentials, license #, signature, date/time]
```

## Verification

- [ ] Problem section quotes problem statement(s) verbatim with numbers and review dates.
- [ ] Presentation / MSE block present.
- [ ] Every Intervention tagged to a Problem (or flagged off-problem).
- [ ] Every Intervention has an observable Response.
- [ ] Risk reassessed and actioned where indicated.
- [ ] Plan items specific and measurable.
- [ ] CPT/HCPCS, time, medical necessity consistent.
- [ ] Gaps flagged; nothing fabricated.
