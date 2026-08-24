---
title: "Major Depressive Disorder Care Plan"
category: domain-healthcare-clinical/care-plans
description: "Build a measurement-based MDD treatment plan: antidepressant selection and titration, adequate-trial logic, augmentation/switch strategy, and safety monitoring with named drugs and doses."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
  - DS-02
difficulty: advanced
tags:
  - psychiatry
  - depression
  - care-plan
  - chronic-disease
updated: "2026-06-19"
---

## Objective

Produce a measurement-based MDD care plan: confirm diagnosis and severity, select an initial antidepressant by profile, define adequate-trial dose/duration, set a switch/augmentation pathway for partial or non-response, and install safety monitoring. Output is a sequenced pharmacologic + psychotherapy plan.

## Inputs

- Diagnosis/severity: PHQ-9 score, episode number, duration, functional impairment
- Safety: suicidal ideation (C-SSRS), prior attempts, access to means, substance use
- Subtype/features: anxious distress, atypical, melancholic, psychotic, seasonal, peripartum
- History: prior antidepressant trials (agent, dose, duration, response, tolerability), bipolar screen (rule out — antidepressant monotherapy can destabilize)
- Comorbidities, concurrent meds (interactions, QT, serotonergic burden), pregnancy/lactation

## Role

Psychiatrist or primary care attending managing depression with measurement-based care.

## Reasoning Steps

1. **Confirm unipolar MDD and screen for bipolarity** (past mania/hypomania) — a positive screen changes the whole plan (mood stabilizer, not antidepressant monotherapy). Assess safety with C-SSRS; address means restriction and crisis plan if SI present.

2. **Establish measurement-based care:** baseline PHQ-9, repeat at each visit; target ≥50% reduction (response) and PHQ-9 <5 (remission).

3. **Select initial antidepressant by profile** (efficacy broadly similar; choose by side effects/comorbidity):
   - First-line SSRI (sertraline, escitalopram) or SNRI (duloxetine, venlafaxine).
   - Insomnia/appetite loss → mirtazapine; comorbid pain → duloxetine; smoking cessation/low sexual side effects → bupropion (avoid in seizure/eating disorder); anxious → SSRI.
   - Start low, titrate to therapeutic dose over 1–2 weeks (e.g., sertraline 50 → 100–200; escitalopram 10 → 20).

4. **Adequate trial = therapeutic dose for 6–8 weeks.** Reassess at 2–4 weeks for partial response; do not abandon prematurely, but if zero response by 4 weeks at adequate dose, change.

5. **Partial/non-response pathway (STAR*D-informed):**
   - **No response:** switch (within class or to different class).
   - **Partial response:** augment — add bupropion, mirtazapine, or **atypical antipsychotic** (aripiprazole 2–5 mg, quetiapine, brexpiprazole) or lithium or T3; or add psychotherapy.
   - **Treatment-resistant** (≥2 adequate trials): consider esketamine, ECT (especially psychotic/catatonic/acutely suicidal), TMS.

6. **Psychotherapy:** CBT or interpersonal therapy — combine with medication for moderate-severe; can be monotherapy for mild.

7. **Special features:** psychotic depression → antidepressant + antipsychotic or ECT; peripartum → sertraline preferred, consider zuranolone/brexanolone; seasonal → light therapy.

8. **Duration & discontinuation:** continue 4–9 months after remission for a first episode; indefinite for recurrent (≥3 episodes) or chronic. Taper slowly to avoid discontinuation syndrome (especially paroxetine, venlafaxine).

9. **Monitor:** PHQ-9, emergent SI (especially early/under-25), activation/mania switch, metabolic (if antipsychotic augmentation), QT (citalopram >40 mg caution), serotonin syndrome with combinations, adherence.

## Output Format

```
DIAGNOSIS / SEVERITY (PHQ-9) / FEATURES:
SAFETY (C-SSRS, means, crisis plan):
BIPOLAR SCREEN:

PHARMACOLOGIC PLAN:
- Initial agent: [drug, dose, titration, rationale]
- Adequate trial definition (dose × 6–8 wk)
- Switch/augmentation pathway

PSYCHOTHERAPY: [modality]

SPECIAL FEATURES: [if applicable]

DURATION / DISCONTINUATION:

MONITORING:
- PHQ-9 cadence, emergent SI, activation, metabolic/QT

PITFALLS:
- [missed bipolarity, inadequate trial, abrupt discontinuation, serotonin burden, under-monitoring SI]
```

## Worked Example

**Input:** 34 y/o F, moderate-severe MDD, PHQ-9 18, first episode, passive SI without plan/intent, no prior attempts, no mania history. Comorbid generalized anxiety. No current meds. Not pregnant.

**Output:**

```
DIAGNOSIS / SEVERITY: MDD, moderate-severe (PHQ-9 18), first episode, anxious distress.
SAFETY: passive SI, no plan/intent/access concern → C-SSRS low-moderate; means-restriction counseling, crisis line, safety follow-up in 1–2 weeks.
BIPOLAR SCREEN: negative (no mania/hypomania).

PHARMACOLOGIC PLAN:
- Initial agent: sertraline 50 mg daily (SSRI covers comorbid GAD). Titrate to 100 mg after 1–2 weeks as tolerated; range to 200.
- Adequate trial: therapeutic dose × 6–8 weeks before judging efficacy; reassess at 2–4 weeks.
- If no response by 4–6 wk at adequate dose → switch (e.g., escitalopram or an SNRI like duloxetine).
- If partial response → augment (e.g., add bupropion, or aripiprazole 2–5 mg).

PSYCHOTHERAPY: refer for CBT — combine with medication for moderate-severe; addresses both depression and anxiety.

SPECIAL FEATURES: anxious distress — SSRI appropriate; warn about early transient anxiety/activation; start low.

DURATION / DISCONTINUATION: continue 4–9 months after remission (first episode); slow taper at the end.

MONITORING:
- PHQ-9 each visit; close SI monitoring early (age <25 boundary, first weeks) — follow up 1–2 weeks.
- Watch for activation/manic switch (would reopen bipolar question).
- Adherence and side-effect counseling (GI, sexual, sleep).

PITFALLS:
- Don't call it a failed trial before 6–8 weeks at therapeutic dose.
- Re-screen for bipolarity if activation/rapid mood elevation emerges.
- Taper slowly at discontinuation (sertraline less prone than paroxetine, but still).
```
