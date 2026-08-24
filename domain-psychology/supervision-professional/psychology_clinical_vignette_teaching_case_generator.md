---
title: "Clinical Vignette / Teaching Case Generator"
category: psychology/supervision-professional
description: "Generate a de-identified teaching case or vignette from a real case for didactics, supervision, or board prep — with learning objectives, discussion questions, and a HIPAA-grade de-identification checklist."
techniques:
  - ED-03
  - ST-04
  - DT-01
  - QA-04
  - QA-05
difficulty: intermediate
intended_use: model-testing
tags:
  - teaching-case
  - clinical-vignette
  - de-identification
  - didactics
  - case-based-learning
  - board-prep
updated: "2026-06-08"
related_prompts:
  - domain-psychology/supervision-professional/psychology_board_exam_vignette_study_tool.md
  - domain-psychology/supervision-professional/psychology_therapeutic_technique_explainer.md
  - domain-psychology/supervision-professional/psychology_ethics_consultation_walkthrough.md
  - domain-psychology/supervision-professional/psychology_supervision_agenda_builder.md
---

# Clinical Vignette / Teaching Case Generator

## Objective

Convert a real clinical case into a de-identified teaching vignette suitable for case conference, supervision group, didactic seminar, or board/licensing review. The product must:

1. Preserve the teaching value (the clinical reasoning, diagnostic ambiguity, or ethical tension) while removing all identifiers.
2. State explicit learning objectives the vignette is built to serve.
3. Include facilitator discussion questions graded from recall to synthesis.
4. Pass a structured de-identification checklist aligned to the HIPAA Safe Harbor 18-identifier standard and APA/ACA confidentiality expectations.

## When to Use

- Building a case for grand rounds, case conference, or a training seminar.
- Generating practice vignettes for supervisees or for licensing/board preparation.
- Writing up a case for a journal club or for a competency demonstration where the real case must be protected.
- Standardizing how a training program de-identifies cases before they circulate.

## Inputs / Context Required

- **Source case material**: the real presentation, course, and outcome `[clinician input required: the de-identified clinical facts to be taught from]`.
- **Teaching target**: what the case is meant to teach (a differential, a treatment decision, an ethical dilemma, a rupture-and-repair, a risk call).
- **Audience and level**: trainees / interns / licensed clinicians / interdisciplinary; novice vs. advanced.
- **Format**: written vignette, branching case, oral-exam style, OSCE-style standardized scenario.
- **Setting constraints**: small community where re-identification risk is higher (may require compositing).
- `[clinician input required: whether consent or program policy permits use of this case even de-identified]`

## Constraints

### Must

- Remove all 18 HIPAA Safe Harbor identifiers (names, geographic subdivisions smaller than state, all date elements except year, contact info, SSN/MRN/account/license/device/IP/URL, biometric and full-face identifiers, and any other unique identifying characteristic).
- Alter or generalize non-essential details that could re-identify in a small community (employer, rare diagnosis combinations, unique events) — using compositing or generalization when a single detail is identifying.
- Preserve the **clinically load-bearing** facts so the teaching point survives de-identification; note any alteration that changes clinical meaning.
- State 2–4 explicit learning objectives using observable verbs (identify, differentiate, justify, prioritize).
- Provide discussion questions across at least three cognitive levels (recall/comprehension → application/analysis → synthesis/evaluation).
- Include a teaching-point / debrief section with the intended takeaways.
- Include the de-identification checklist as a completed artifact, not just a reminder.

### Must Not

- Do not retain any direct identifier or any quasi-identifier combination that enables re-identification.
- Do not alter clinically essential facts silently; if a change affects the teaching point, disclose it.
- Do not fabricate clinical phenomena to make the case "cleaner"; teaching cases must remain clinically realistic and labeled if composited.
- Do not present a single-source identifiable case from a small population without compositing.
- Do not omit the consent/policy check.

## Instructions

1. **Confirm permission**: verify consent or program policy permits teaching use of this case (de-identified).
2. **Extract the teaching skeleton**: isolate the clinically load-bearing facts that carry the learning objective.
3. **Strip identifiers**: run the 18-identifier pass; replace ages >89 with "90+", dates with year-only or relative timing, locations with region/setting type.
4. **Mitigate re-identification**: generalize or composite rare/unique details; mark composited cases as such.
5. **Write the vignette**: present the case in the chosen format, preserving the diagnostic/ethical tension.
6. **Author learning objectives and tiered discussion questions.**
7. **Write the debrief / teaching points** and any branching outcomes.
8. **Complete the de-identification checklist** and run verification.

## Output Format

```
=== TEACHING VIGNETTE PACKAGE ===

METADATA
Title (non-identifying): [...]
Audience / level: [...]   Format: [Written / Branching / Oral / OSCE]
Composite case?: [Yes — fields combined / No]
Consent or policy basis for teaching use: [clinician input required]

LEARNING OBJECTIVES
By the end, learners will be able to:
1. [Observable verb + content]
2. [...]
3. [...]

────────────────────────────────────────────────────────
VIGNETTE (de-identified)
[Presentation: demographics generalized, setting type, presenting concern.]
[History and course: year-only / relative timing; load-bearing clinical facts preserved.]
[Decision point(s): the tension the case is built to teach.]
[Outcome, if disclosed for teaching.]

────────────────────────────────────────────────────────
DISCUSSION QUESTIONS (tiered)
Recall / comprehension:
1. [...]
Application / analysis:
2. [...]
Synthesis / evaluation:
3. [...]

────────────────────────────────────────────────────────
DEBRIEF / TEACHING POINTS
- [Intended takeaway tied to objective 1]
- [Takeaway tied to objective 2]
- Common learner pitfalls: [...]

────────────────────────────────────────────────────────
DE-IDENTIFICATION CHECKLIST (completed)
[ ] Names (patient, family, providers, facilities) removed
[ ] Geographic units smaller than state removed/generalized
[ ] All dates reduced to year or relative timing; ages 90+ collapsed
[ ] Contact info / SSN / MRN / account / license / device / IP / URL removed
[ ] Biometric and full-face identifiers removed
[ ] Rare/unique characteristics generalized or composited
[ ] Employer / school / unique events generalized
[ ] Residual re-identification risk assessed for small-community context
[ ] Clinically load-bearing facts preserved; any meaning-changing alteration disclosed
Altered-detail disclosure (if any): [...]
Prepared by: ____________________  Date: ________
Reviewer / supervisor co-sign: ____  Date: ________
```

## Verification

- [ ] Consent/policy basis for teaching use confirmed.
- [ ] All 18 HIPAA Safe Harbor identifiers removed or generalized.
- [ ] Quasi-identifier / small-community re-identification risk mitigated (compositing noted where used).
- [ ] Clinically load-bearing facts preserved; meaning-changing alterations disclosed.
- [ ] 2–4 learning objectives stated with observable verbs.
- [ ] Discussion questions span at least three cognitive levels.
- [ ] Debrief / teaching points tied back to objectives.
- [ ] De-identification checklist completed as an artifact, not a reminder.
- [ ] Composite cases labeled as composite.
- [ ] Supervisor co-sign field present; gaps flagged with `[clinician input required]`; nothing fabricated.
