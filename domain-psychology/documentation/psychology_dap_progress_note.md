---
title: "DAP-Format Psychotherapy Progress Note Drafter"
category: psychology/documentation
description: "Convert raw session notes into a DAP-format (Data / Assessment / Plan) progress note with rigorous separation of objective and subjective data inside the Data block."
techniques:
  - ST-04
  - DT-02
  - QA-04
  - CM-02
difficulty: intermediate
tags:
  - progress-note
  - dap
  - psychotherapy-documentation
  - golden-thread
intended_use: model-testing
updated: "2026-05-08"
related_prompts:
  - domain-psychology/documentation/psychology_soap_progress_note.md
  - domain-psychology/documentation/psychology_birp_progress_note.md
  - domain-psychology/documentation/psychology_initial_treatment_plan.md
---

# DAP-Format Psychotherapy Progress Note Drafter

## Objective

Produce a complete DAP-format progress note (**Data / Assessment / Plan**) that:

1. Combines subjective and objective material in a single **Data** block while keeping the source of evidence labeled.
2. Reserves **Assessment** for clinical reasoning, formulation, response-to-treatment, and risk impression.
3. Uses **Plan** for next session, homework, coordination, medication, and safety follow-through.
4. Maintains the golden thread linking session content to treatment-plan goals and supports the billed CPT code.

DAP is most common in community mental health, IOP/PHP, school-based, and case-management settings.

## When to Use

- The clinician's organization documents in DAP rather than SOAP.
- Sessions where data and observation are tightly interwoven and a SOAP split feels artificial (process-oriented, group, or short check-in encounters).
- When converting an existing SOAP note to DAP for a new EHR.

## Inputs / Context

- Session metadata (date, duration, modality, CPT, ICD-10, treatment-plan goals addressed).
- Raw session content: client statements, clinician observations, interventions performed, client response.
- MSE elements observed.
- Outcome measures with current and prior scores.
- Risk content (SI / HI / NSSI / substance / abuse) with what was assessed and any actions.
- Homework reviewed and assigned.

## Constraints

### Must

- Output exactly three labeled sections in order: **Data**, **Assessment**, **Plan**.
- Inside **Data**, organize content as: (a) client report (subjective), (b) clinician observation / MSE / measures (objective), (c) interventions delivered with named techniques, (d) client response to each intervention.
- Use evidence-based intervention names (cognitive restructuring, behavioral activation, exposure, DBT skill name, MI reflection type, etc.).
- Document risk reassessment in **Data** (what was asked / observed) and risk formulation in **Assessment** (what it means clinically).
- Tie at least one intervention to a numbered treatment-plan goal.
- Include billing line that justifies the CPT code with medical-necessity rationale.

### Must Not

- Do not collapse Data into a narrative that loses the client-report vs clinician-observation distinction — label or tag the source.
- Do not move clinical reasoning into Data; reasoning belongs in Assessment.
- Do not omit risk content or substitute euphemisms.
- Do not invent details not supplied by the clinician; flag missing inputs as `[clinician input required: ...]`.

## Instructions

1. Identify and list any missing inputs before drafting.
2. Build **Data** in four labeled sub-blocks: *Client report*, *Clinician observation / MSE / measures*, *Interventions delivered*, *Client response*. Each sub-block is 2–6 lines.
3. Build **Assessment**: 3–6 sentences covering progress on goals, current diagnostic impression, response-to-treatment, risk formulation, and trajectory.
4. Build **Plan**: next session, homework, coordination, medication, safety, clinician follow-up.
5. Append billing block with CPT, duration, medical-necessity sentence.
6. Run verification.

## Output Format

```
=== PROGRESS NOTE (DAP) ===

Client: [Initials/MRN]    DOB: [age, gender, pronouns]
Date of Service: [YYYY-MM-DD]    Time In/Out: [HH:MM–HH:MM]    Duration: [N min]
Modality: [in-person | telehealth-video | telehealth-audio-only]
CPT: [code]    ICD-10: [codes]
Treatment-plan goals addressed: [Goal #X label, Goal #Y label]

DATA

Client report:
- [Stated agenda; symptom report since last session; sleep / appetite / substance use / medication adherence; stressors; one direct quote if illustrative.]
- [Self-reported risk: SI/HI/NSSI status in client's words.]

Clinician observation / MSE / measures:
- [MSE paragraph: appearance, behavior, speech, mood (quoted), affect (observed), TP, TC, cognition, insight, judgment.]
- [Outcome measures: PHQ-9 = X (prior X on YYYY-MM-DD); GAD-7 = X; PCL-5 = X.]
- [Behavioral observations: engagement, affect shifts, in-session skill use.]

Interventions delivered:
- [Named technique #1 — what was done — tied to Goal #X.]
- [Named technique #2 — what was done — tied to Goal #Y.]
- [Risk-related actions if any: safety-plan review, means restriction conversation, warm handoff, etc.]

Client response:
- [Observable response to each intervention: engagement, insight statements, skill rehearsal performance, distress reduction, homework receptivity.]

ASSESSMENT
Active diagnoses: [F##.#; F##.#].
[Progress vs goals: Goal #X — improving/stable/worsening; evidence: ...].
[Diagnostic impression update if any.]
[Response-to-treatment: which interventions were absorbed vs which need revision.]
Risk formulation: [SI/HI/NSSI status, severity, plan/intent/means, protective factors, risk level this session: low/moderate/high; rationale].
Trajectory: [improving / stable / worsening / acute change].

PLAN
- Next session: [date / frequency].
- Continue: [modality, modules].
- Homework: [specific, measurable, review point].
- Coordination: [referrals, collateral contacts, dates].
- Medication: [coordination notes].
- Safety: [safety plan status, means restriction follow-up].
- Clinician follow-up: [tasks owned by clinician].

BILLING
CPT [#####] x 1, [N] min face-to-face. [+90785 if applicable, reason: ...]
Medical necessity: [one-sentence rationale tied to active diagnosis and goal].

Clinician: [name, credentials, license #, signature, date/time]
```

## Verification

- [ ] Three sections present (Data / Assessment / Plan), correctly ordered.
- [ ] Data sub-blocks all labeled; client-report vs clinician-observation distinction preserved.
- [ ] Interventions named with evidence-based labels and tied to numbered goals.
- [ ] Client response documented for each intervention.
- [ ] Risk reassessed in Data and formulated in Assessment.
- [ ] Outcome measures include prior comparator where available.
- [ ] Plan items are concrete (no "continue therapy as needed" without specifics).
- [ ] CPT code consistent with duration and medical-necessity sentence.
- [ ] All gaps flagged with bracketed prompts; nothing fabricated.
