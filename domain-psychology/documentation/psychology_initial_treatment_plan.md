---
title: "Initial Treatment Plan Drafter (Golden-Thread)"
category: psychology/documentation
description: "Build a goal-driven initial treatment plan with explicit golden thread linking problem → goal → measurable objective → intervention → frequency → reviewer."
techniques:
  - ST-04
  - DT-01
  - DS-02
  - QA-04
  - CM-02
difficulty: advanced
tags:
  - treatment-plan
  - golden-thread
  - smart-goals
  - measurable-objectives
  - care-planning
intended_use: model-testing
updated: "2026-05-08"
related_prompts:
  - domain-psychology/documentation/psychology_intake_assessment_note.md
  - domain-psychology/documentation/psychology_treatment_plan_update.md
  - domain-psychology/diagnostic-formulation/psychology_case_conceptualization_framework.md
  - domain-psychology/documentation/psychology_girp_progress_note.md
---

# Initial Treatment Plan Drafter (Golden-Thread)

## Objective

Generate an initial outpatient or program treatment plan that withstands a Joint Commission, CARF, or Medicaid utilization-review audit. The plan must:

1. Derive directly from the intake biopsychosocial and case formulation.
2. Express the **golden thread**: each *problem* yields one or more *goals*, each goal yields one or more *measurable objectives* with target dates, each objective yields specific *interventions* (modality + technique + frequency + responsible clinician).
3. Use SMART criteria for every objective (Specific, Measurable, Achievable, Relevant, Time-bound).
4. Be written so subsequent progress notes can quote the goals and objectives verbatim.

## When to Use

- After the intake assessment, typically within 1–3 sessions.
- When transitioning a client between programs (e.g., outpatient → IOP) and a new plan is required.
- When reauthorizing an episode of care after a long lapse.

## Inputs / Context

- Completed intake with provisional diagnoses, formulation, risk stratification.
- Outcome-measure baselines (PHQ-9, GAD-7, PCL-5, etc.).
- Client-stated goals in their own words.
- Modality decision: individual psychotherapy / family / group / med management / IOP / PHP combination.
- Frequency: weekly / biweekly / 2x weekly / step-down schedule.
- Treatment-plan completion deadline imposed by program (e.g., within 30 days of admission).
- Reviewer / supervisor name and review interval (typically 90 days).
- Client's literacy / language / accessibility considerations.
- Parent / guardian involvement if minor.

## Constraints

### Must

- Output the following labeled sections in order: **Demographics**, **Diagnoses**, **Strengths**, **Problem List**, **Goals & Objectives** (the core), **Interventions**, **Discharge Criteria**, **Coordination of Care**, **Crisis / Safety Plan Reference**, **Plan Review**, **Signatures**.
- The **Problem List** uses verbatim or near-verbatim language; problem statements are functional (e.g., "depression symptoms interfering with work attendance and parenting") not just diagnostic labels.
- For each problem, generate at least one **Goal** (long-term, narrative, client-meaningful) and one or more **Measurable Objectives** that meet SMART criteria.
- Each objective specifies a measurement method and a target threshold (e.g., "PHQ-9 score ≤ 9 sustained over 4 weeks," "Attend work ≥ 4 days per week for 3 consecutive weeks," "Complete 5 of 7 daily mood logs per week for 4 weeks").
- For each objective, specify one or more **Interventions** with modality, evidence-based technique name, frequency, duration, responsible clinician, and target start date.
- Include client's own words for at least one goal per problem.
- Specify **Discharge Criteria** in observable, measurable terms.
- Reference the existing safety plan by date or attach a placeholder for one to be completed.
- Include client signature line and date; co-occurring guardian / collateral signature when applicable.

### Must Not

- Do not write goals as restated diagnoses ("Resolve major depressive disorder"). Goals are functional / experiential.
- Do not use immeasurable objective language ("client will feel better," "client will manage anxiety").
- Do not list interventions without naming the technique (no "supportive therapy as needed").
- Do not omit responsible clinician or frequency from any intervention.
- Do not exceed the program's max review interval before scheduling a review.
- Do not fabricate; flag missing items as `[clinician input required: ...]`.

## Instructions

1. Read the intake/formulation; identify 1–4 functional problems. More than 4 dilutes focus.
2. For each problem, draft 1–2 long-term goals; include client's voice in at least one per problem.
3. For each goal, draft 1–3 SMART objectives, each with a measurement method and a target date. Keep total objectives across the plan to ≤ 8 for outpatient (more for IOP/PHP).
4. For each objective, attach 1–3 interventions: modality, technique (evidence-based name), frequency, duration, responsible clinician.
5. Write Discharge Criteria as observable thresholds per problem.
6. Cross-reference safety plan and any active referrals.
7. Schedule plan review with reviewer name and date.
8. Run verification.

## Output Format

```
=== INITIAL TREATMENT PLAN ===

DEMOGRAPHICS
Client: [Initials/MRN]    Date of Birth: [YYYY-MM-DD]    Pronouns: [...]
Plan effective date: [YYYY-MM-DD]    Plan review date: [YYYY-MM-DD]
Primary clinician: [name, credentials, license #]
Other team members: [name, role]

DIAGNOSES
Primary: [F##.##] [Descriptor]
Secondary: [F##.##] [Descriptor]
Rule-outs: [...]
Z-codes (psychosocial): [Z##.##] [Descriptor]

STRENGTHS
- [Specific strength tied to formulation]
- [...]

PROBLEM LIST
1. [Functional problem statement, in plain language. Optional client quote.]
2. [...]
3. [...]

GOALS & OBJECTIVES
─────────────────────────────────────────────────────────
Problem #1: [Statement]

Goal #1.A: [Long-term, client-meaningful, narrative goal.]
   Client's own words: "[...]"
   Target date: [YYYY-MM-DD]

  Objective #1.A.i: [SMART objective.]
     Measurement: [Instrument / behavioral count / observation method]
     Target threshold: [Specific number, frequency, or score]
     Start date: [YYYY-MM-DD]    Target date: [YYYY-MM-DD]
     Status: [Not started / In progress / Met / Modified]

  Objective #1.A.ii: [...]

Goal #1.B: [...]
─────────────────────────────────────────────────────────
Problem #2: [...]
[same structure]
─────────────────────────────────────────────────────────

INTERVENTIONS
| ID | Tied to | Modality | Technique (evidence-based name) | Frequency | Duration | Responsible | Start |
|----|---------|----------|----------------------------------|-----------|----------|-------------|-------|
| I1 | Obj #1.A.i | Individual psychotherapy | CBT — cognitive restructuring & behavioral activation | Weekly | 50 min | [Clinician] | [Date] |
| I2 | Obj #1.A.ii | Group | DBT skills group — Mindfulness module | Weekly | 90 min | [Group leader] | [Date] |
| I3 | Obj #2.A.i | Med management | Psychiatric prescriber visits | q4 weeks | 25 min | [Prescriber] | [Date] |
| I4 | All goals | Care coordination | Monthly PCP communication | Monthly | n/a | [Care manager] | [Date] |

DISCHARGE CRITERIA
- Problem #1: [Observable threshold, e.g., "PHQ-9 ≤ 9 sustained x 8 weeks AND return to baseline work attendance."]
- Problem #2: [...]
- Problem #3: [...]

COORDINATION OF CARE
- PCP: [Name, contact, ROI status, communication frequency]
- Prescriber: [Name, contact, ROI status, communication frequency]
- Other (school, case manager, family): [...]

CRISIS / SAFETY PLAN
Stanley-Brown safety plan dated: [YYYY-MM-DD] (attached / on file).
Lethal means status: [Firearms removed/secured | Medications secured | N/A].
Crisis line provided: [988 | local crisis number] — confirmed client knows how to access.
After-hours protocol explained: [Yes / No, with reason].

PLAN REVIEW
Reviewer: [Supervisor name, credentials]
Review interval: [90 days standard; sooner if level-of-care change]
Next review date: [YYYY-MM-DD]

SIGNATURES
Client: ____________________________  Date: ___________
Guardian (if applicable): __________  Date: ___________
Primary clinician: __________________  Date: ___________
Reviewer / Supervisor: ______________  Date: ___________
```

## Verification

- [ ] Demographics, Diagnoses, Strengths, Problem List, Goals & Objectives, Interventions, Discharge Criteria, Coordination, Crisis Plan, Plan Review, Signatures — all present.
- [ ] 1–4 functional problems (not 0, not 10+).
- [ ] Each problem has ≥ 1 goal; each goal has ≥ 1 SMART objective; each objective has ≥ 1 named intervention.
- [ ] Every objective has measurement method AND target threshold AND target date.
- [ ] Every intervention has modality, technique name, frequency, duration, responsible clinician, start date.
- [ ] At least one goal per problem includes client's own words.
- [ ] Discharge criteria are observable / measurable per problem.
- [ ] Safety plan referenced with date or marked for completion.
- [ ] Plan review scheduled within program max interval.
- [ ] Signatures placeholder present for client / guardian / clinician / reviewer.
- [ ] No diagnostic-label-as-goal, no immeasurable objective, no unnamed intervention.
- [ ] Gaps flagged; nothing fabricated.
