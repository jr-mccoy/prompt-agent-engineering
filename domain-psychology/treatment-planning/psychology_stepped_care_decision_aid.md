---
title: "Stepped Care Decision Aid"
category: psychology/treatment-planning
description: "Determine the appropriate level of care — outpatient to inpatient — and decide when to step up, step down, or hold using LOCUS criteria and clinical indicators."
techniques:
  - RT-02
  - DT-01
  - QA-04
  - DS-02
  - CM-02
difficulty: advanced
intended_use: model-testing
tags:
  - level-of-care
  - stepped-care
  - IOP
  - PHP
  - residential
  - inpatient
  - LOCUS
  - ASAM
  - treatment-planning
updated: "2026-06-08"
related_prompts:
  - domain-psychology/treatment-planning/psychology_modality_selection_decision_aid.md
  - domain-psychology/treatment-planning/psychology_treatment_resistance_reformulation.md
  - domain-psychology/documentation/psychology_initial_treatment_plan.md
  - domain-psychology/risk-crisis/psychology_columbia_suicide_risk_assessment.md
---

# Stepped Care Decision Aid

## Objective

Determine the clinically appropriate level of care for a client at a decision point — initial placement, step-up, or step-down — using structured criteria drawn from the Level of Care Utilization System (LOCUS) for mental health and the American Society of Addiction Medicine (ASAM) criteria for substance use disorders. Output a level-of-care recommendation with explicit clinical justification, documentation language suitable for managed-care authorization, and a trigger-condition plan for re-evaluation.

## When to Use

- At intake, when the referring clinician or payor requires a level-of-care determination.
- When a client's clinical status has deteriorated and a step-up from outpatient to IOP, PHP, residential, or inpatient is being considered.
- When a client has stabilized in a higher level of care and step-down criteria need to be evaluated.
- When an insurer or managed-care organization has denied or is questioning medical necessity at the current level.
- When the treatment team is split on whether to step up versus intensify within the current level.

## Inputs / Context Required

- **Current diagnosis(es)** (DSM-5-TR / ICD-10-CM with specifiers): primary psychiatric and any active SUD diagnoses.
- **Risk assessment summary**: suicidal ideation (frequency, intensity, plan, access to means), self-harm, homicidal ideation, recent attempts or self-injurious behavior.
- **Symptom severity scores**: PHQ-9, GAD-7, PCL-5, Columbia C-SSRS severity rating, AUDIT/DAST-10, or other applicable.
- **Current level of care** (if established): outpatient / IOP / PHP / residential / inpatient / crisis stabilization.
- **Response to current level**: improving, plateauing, or deteriorating — and over what timeframe.
- **Functional status**: ability to maintain safety between sessions, attend work/school, care for self/dependents.
- **Support system**: social support availability, stability of living environment, access to transportation.
- **Medical / co-occurring factors**: active medical conditions requiring medical monitoring; substance withdrawal risk; medication complexity.
- **Engagement history**: attendance, medication adherence, therapy participation, prior authorizations.
- `[clinician input required: collateral information from family, treatment team, prior records]`
- `[clinician input required: insurance plan's specific LOC definitions and medical necessity criteria if payor-specific language is needed]`

## Constraints

### Must

- Map the clinical presentation to the LOCUS six dimensions: Risk of Harm, Functional Status, Medical / Psychiatric Co-occurring Complexity, Recovery Environment, Treatment and Recovery History, and Engagement.
- For SUD presentations, also apply ASAM six dimensions: Acute Intoxication/Withdrawal, Biomedical Conditions, Emotional/Behavioral/Cognitive Conditions, Readiness to Change, Relapse/Continued Use Potential, Recovery Environment.
- Produce a level-of-care recommendation from the defined continuum with explicit dimensional scores or ratings.
- Provide step-up criteria: the specific observable conditions that would indicate the current level is no longer sufficient.
- Provide step-down criteria: the specific observable conditions that must be met before reducing intensity.
- Write a medical-necessity justification paragraph suitable for submission to a managed-care organization.
- Include a re-evaluation trigger plan: when and under what conditions the LOC assessment should be repeated.
- Flag any safety concern that requires immediate action independent of LOC determination (e.g., an acutely suicidal client needing emergency evaluation before LOC discussion proceeds).

### Must Not

- Do not recommend a higher level of care based on diagnosis alone, without functional and risk indicators.
- Do not recommend step-down based on symptom reduction alone, without functional stability and safety verification.
- Do not omit the recovery environment dimension; it is one of the strongest predictors of LOC appropriateness.
- Do not conflate level-of-care selection with modality selection (see `psychology_modality_selection_decision_aid.md`).
- Do not document step-down without recording the criteria that were met.
- Do not fabricate LOCUS or ASAM dimensional scores; mark as `[clinician input required: score after LOCUS/ASAM structured administration]` if not formally administered.

## Instructions

1. **Safety screen first**: Before any LOC analysis, identify whether the client meets criteria for emergent or urgent psychiatric evaluation (active suicidal plan with intent and means, active homicidal ideation, grave disability, acute intoxication with risk of harm). If yes, document that emergent evaluation precedes LOC planning and halt the analysis pending outcome.

2. **Apply LOCUS dimensional ratings** (1–5 scale per dimension; total composite score maps to LOC):

   | LOCUS Dimension | Rating (1–5) | Key indicators for this client |
   |-----------------|-------------|-------------------------------|
   | D1: Risk of Harm | [score] | [Suicidality, self-harm, violence, impulsivity] |
   | D2: Functional Status | [score] | [ADLs, work/school, self-care, parenting] |
   | D3: Medical / Psychiatric Complexity | [score] | [Co-occurring medical, psychiatric severity, withdrawal] |
   | D4: Recovery / Treatment History | [score] | [Chronicity, prior LOC, treatment response] |
   | D5: Recovery Environment | [score] | [Support, stability, access, stressors] |
   | D6: Engagement | [score] | [Motivation, compliance, insight] |
   | **Composite Score** | [total] | [LOC grid mapping] |

   LOCUS composite to LOC grid (approximate; local norms may vary):
   - 6–9: Basic outpatient (weekly or biweekly)
   - 10–14: Low-intensity outpatient (weekly, may include group)
   - 15–19: High-intensity outpatient / IOP (9–12 hours/week)
   - 20–24: PHP (20–30 hours/week; structured day program)
   - 25–29: Residential / medically monitored
   - 30+: Medically managed inpatient

3. **Apply ASAM dimensions** (if SUD diagnosis is active or primary). Rate each of six ASAM dimensions and use the resulting profile to determine which of the four ASAM levels of care (0.5 Early Intervention through Level 4 Medically Managed Intensive Inpatient) is indicated.

4. **Determine LOC recommendation**: State the recommended LOC from the defined continuum below, with the dimensional justification:
   - **Standard outpatient**: 1–4 sessions/month
   - **Outpatient** (routine): 1 session/week individual ± weekly group
   - **Intensive Outpatient Program (IOP)**: typically 3 days/week × 3 hours/day; 9 hours minimum/week
   - **Partial Hospitalization Program (PHP)**: typically 5 days/week × 5–6 hours/day; 20–30 hours/week
   - **Residential treatment**: 24-hour non-hospital structured living; medically monitored or managed
   - **Inpatient psychiatric**: 24-hour medically managed; locked or unlocked; crisis stabilization unit vs. acute inpatient vs. long-term
   - **Crisis stabilization unit (CSU)**: short-stay (1–7 days) bridge; less restrictive than acute inpatient

5. **Document step-up criteria**: List 3–5 specific observable indicators that, if met, would require reassessment for a higher LOC. Examples: re-emergence of suicidal plan with intent; inability to maintain safety between sessions; deterioration in PHQ-9 by ≥ 5 points over 2 weeks without explanation; decompensation in ADLs (unable to feed/dress self); substance use relapse with loss of control.

6. **Document step-down criteria**: List 3–5 specific observable indicators that must all be present before reducing LOC. Examples: PHQ-9 ≤ [threshold] for ≥ 2 consecutive assessments; C-SSRS passive ideation only (no plan/intent); stable housing confirmed; at least one support person identified and engaged; demonstrates 2 specific coping skills; attended ≥ [N]% of current LOC sessions.

7. **Write medical-necessity justification paragraph**: One paragraph (4–6 sentences) in managed-care authorization language describing: diagnosis, functional impairment, symptom severity, why the recommended LOC is the least restrictive level that can safely and effectively treat the presentation. Avoid vague language; quote scores.

8. **Set re-evaluation trigger plan**: Specify (a) routine re-evaluation interval (e.g., every 30 days in IOP/PHP, every 90 days in outpatient), (b) immediate trigger conditions for unscheduled re-evaluation.

9. **Run verification.**

## Output Format

```
=== STEPPED CARE DECISION AID ===

SAFETY SCREEN
[ ] No emergent/urgent indicators — proceed to LOC analysis.
[ ] EMERGENT — [describe] — halt LOC analysis; initiate emergency evaluation now.

────────────────────────────────────────────────────────
LOCUS DIMENSIONAL RATINGS

| Dimension | Score (1–5) | Key Clinical Indicators |
|-----------|-------------|------------------------|
| D1: Risk of Harm | [1–5] | [Describe SI/SH/HI severity, plan, intent, means access] |
| D2: Functional Status | [1–5] | [ADLs, work/school, self-care, parenting capacity] |
| D3: Med/Psych Complexity | [1–5] | [Comorbid conditions, withdrawal risk, medical complexity] |
| D4: Treatment History | [1–5] | [Chronicity, prior LOC responses, treatment-resistant features] |
| D5: Recovery Environment | [1–5] | [Support, housing stability, transportation, safety at home] |
| D6: Engagement | [1–5] | [Motivation, insight, attendance, medication adherence] |
| Composite | [6–30] | [LOC grid range] |

[clinician input required: LOCUS instrument formal administration for definitive scoring]

ASAM DIMENSIONAL SUMMARY [if SUD active]
| Dimension | Rating | Key Indicators |
|-----------|--------|----------------|
| D1: Withdrawal / Intoxication | [0–4] | [...] |
| D2: Biomedical Conditions | [0–4] | [...] |
| D3: Emotional/Behavioral/Cognitive | [0–4] | [...] |
| D4: Readiness to Change | [0–4] | [...] |
| D5: Relapse / Continued Use Risk | [0–4] | [...] |
| D6: Recovery Environment | [0–4] | [...] |
Indicated ASAM LOC: [0.5 / 1.0 / 2.1 / 2.5 / 3.1 / 3.3 / 3.5 / 3.7 / 4.0]

────────────────────────────────────────────────────────
LEVEL-OF-CARE RECOMMENDATION

Recommended LOC: [Standard outpatient / Outpatient routine / IOP / PHP / Residential / Inpatient / CSU]
Frequency / intensity: [Specific schedule — e.g., "3 days/week × 3 hours/day; 9 hours/week minimum"]
Decision rationale: [2–3 sentences linking dimensional scores to LOC recommendation]

Step-Up Criteria (if ANY of the following emerge, re-evaluate for higher LOC):
1. [Specific observable indicator]
2. [Specific observable indicator]
3. [Specific observable indicator]
4. [Specific observable indicator — optional]
5. [Specific observable indicator — optional]

Step-Down Criteria (ALL of the following must be present before reducing LOC):
1. [Specific observable indicator]
2. [Specific observable indicator]
3. [Specific observable indicator]
4. [Specific observable indicator]
5. [Specific observable indicator — optional]

────────────────────────────────────────────────────────
MEDICAL NECESSITY JUSTIFICATION (managed-care language)

[Paragraph — 4–6 sentences. Include: diagnosis (ICD-10 code), severity scores, functional impairment, why this
LOC is the least restrictive level that can safely and effectively treat the presentation. Quote numerical scores.
Avoid vague language.]

────────────────────────────────────────────────────────
RE-EVALUATION PLAN

Routine re-evaluation interval: [30 days in IOP/PHP | 90 days in outpatient | [other]]
Immediate re-evaluation triggers: [List specific clinical events that require unscheduled LOC review]
Reviewer / documenting clinician: [clinician input required]
```

## Verification

- [ ] Safety screen completed and documented before LOC analysis.
- [ ] All six LOCUS dimensions rated or flagged as requiring formal administration.
- [ ] ASAM dimensions completed if SUD diagnosis is active or primary.
- [ ] Composite LOCUS score mapped to specific LOC recommendation.
- [ ] Recommended LOC is from the defined continuum with explicit frequency/intensity specification.
- [ ] Dimensional justification present — not diagnosis-alone reasoning.
- [ ] Step-up criteria: ≥ 3 specific observable indicators.
- [ ] Step-down criteria: ≥ 3 specific observable indicators with "all must be present" framing.
- [ ] Medical-necessity paragraph written in MCO-appropriate language; numerical scores cited.
- [ ] Re-evaluation plan includes routine interval and immediate-trigger conditions.
- [ ] Recovery environment dimension not omitted.
- [ ] LOC recommendation does not conflate with modality selection.
- [ ] Nothing fabricated; missing inputs flagged with `[clinician input required]`.
