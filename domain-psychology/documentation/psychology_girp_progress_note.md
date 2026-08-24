---
title: "GIRP-Format Progress Note Drafter"
category: psychology/documentation
description: "Draft a GIRP-format (Goal / Intervention / Response / Plan) progress note that anchors every line of the note to a numbered treatment-plan goal."
techniques:
  - ST-04
  - DT-02
  - QA-04
  - CM-02
difficulty: intermediate
tags:
  - progress-note
  - girp
  - goal-anchored
  - golden-thread
intended_use: model-testing
updated: "2026-05-08"
related_prompts:
  - domain-psychology/documentation/psychology_birp_progress_note.md
  - domain-psychology/documentation/psychology_pirp_progress_note.md
  - domain-psychology/documentation/psychology_initial_treatment_plan.md
---

# GIRP-Format Progress Note Drafter

## Objective

Produce a goal-anchored progress note in **GIRP** format (**Goal / Intervention / Response / Plan**). GIRP is structurally similar to BIRP but replaces "Behavior" with "Goal," forcing the clinician to lead with the treatment-plan goal that the session served. The format is favored when payers or programs want the golden thread pinned to the very first line of the note.

The note must:

1. State the treatment-plan goal(s) addressed at the top of the note in **Goal** — verbatim from the active treatment plan.
2. Document evidence-based interventions delivered in **Intervention**, each tagged to one of the stated goals.
3. Document observable client response in **Response**.
4. Specify next steps in **Plan**.
5. Include a separate Behavioral / MSE block so observable presentation is not lost.

## When to Use

- Payer or program contract requires GIRP.
- Treatment-plan compliance audits emphasize golden-thread documentation.
- Programs transitioning from BIRP to a goal-first variant.

## Inputs / Context

- Session metadata (date, duration, modality, code, ICD-10, place of service).
- **Verbatim text** of treatment-plan goals being worked today (with goal numbers and target dates).
- Raw session content: client report, clinician observations, interventions, responses.
- MSE observations and outcome-measure scores.
- Risk indicators and any actions taken.

## Constraints

### Must

- Output four labeled sections in order: **Goal**, **Intervention**, **Response**, **Plan**, plus a brief **Presentation / MSE** block immediately after Goal so observational data is preserved.
- Quote the active treatment-plan goal(s) verbatim under **Goal** with goal number and target date.
- Tag every Intervention to a specific Goal number. Interventions that don't map to a goal must either be re-described to fit a goal or flagged as `[off-goal: rationale]`.
- Each Intervention has a paired observable Response.
- Risk reassessment present and located in Presentation / MSE; risk actions in Intervention.
- Plan specifies next session, homework, coordination, medication, safety, clinician follow-up.

### Must Not

- Do not paraphrase treatment-plan goals; quote them verbatim.
- Do not log interventions with no observable response — if the response was unclear, document that.
- Do not omit a Presentation / MSE block under the assumption that "the EHR has an MSE field."
- Do not fabricate; flag missing inputs.

## Instructions

1. Identify missing inputs.
2. Quote the active treatment-plan goal(s) verbatim under **Goal**, each with its goal number, status, and target date.
3. Add **Presentation / MSE** block: appearance, behavior, mood (quoted), affect, MSE elements, measure scores, risk indicators.
4. Draft **Intervention** as a bulleted list; each bullet names the technique, gives a 1-line concrete description, and tags `[Goal #N]`.
5. Draft **Response** as a parallel bulleted list with one observable client response per intervention.
6. Draft **Plan** with next session, homework, coordination, medication, safety, clinician follow-up.
7. Append billing block.
8. Run verification.

## Output Format

```
=== PROGRESS NOTE (GIRP) ===

Client: [Initials/MRN]    DOB: [age, gender, pronouns]
Date of Service: [YYYY-MM-DD]    Time In/Out: [HH:MM–HH:MM]    Duration: [N min]
Place of Service: [POS]    Modality: [in-person | telehealth]
Code(s) billed: [CPT/HCPCS]    ICD-10: [codes]

GOAL
- Goal #X (target [YYYY-MM-DD]): "[Verbatim goal text from treatment plan]"
- Goal #Y (target [YYYY-MM-DD]): "[Verbatim goal text]"
Status this session: [Goal #X — partial progress evident; Goal #Y — addressed via psychoeducation, no behavioral change yet.]

PRESENTATION / MSE
[Appearance, behavior, statements quoted; speech; mood (quoted); affect; thought process; thought content; cognition; insight; judgment.]
[Outcome measures: PHQ-9 = X (prior X on YYYY-MM-DD); GAD-7 = X; ...]
[Risk indicators as reported/observed: SI/HI/NSSI status; substance-use status if applicable.]

INTERVENTION
- [Named technique #1 — concrete description] [Goal #X]
- [Named technique #2 — concrete description] [Goal #Y]
- [Risk-related action if applicable: safety plan review, means restriction conversation, warm handoff.]

RESPONSE
- [Observable response to Intervention #1.]
- [Observable response to Intervention #2.]
- [Response to risk-related action if applicable.]

PLAN
- Next session: [date / frequency / rationale if changing].
- Homework: [specific, measurable, with review point].
- Coordination: [collateral contacts, referrals, dates, ROI status].
- Medication: [coordination notes].
- Safety: [safety plan status; means restriction; emergency contacts].
- Clinician follow-up: [tasks with target dates].

BILLING
[Code] x [units/minutes], POS [##]. Medical necessity: [one sentence tying active diagnosis to goal worked].

Clinician: [name, credentials, license #, signature, date/time]
```

## Verification

- [ ] Goal section quotes treatment-plan goal(s) verbatim with numbers and target dates.
- [ ] Presentation / MSE block present.
- [ ] Every Intervention is tagged to a Goal (or flagged off-goal with rationale).
- [ ] Every Intervention has a corresponding observable Response.
- [ ] Risk reassessed and actioned where indicated.
- [ ] Plan items specific and measurable.
- [ ] CPT/HCPCS, time, and medical necessity consistent.
- [ ] Gaps flagged; nothing fabricated.
