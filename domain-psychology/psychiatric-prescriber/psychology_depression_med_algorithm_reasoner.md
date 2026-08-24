---
title: "Depression Pharmacologic Algorithm Reasoner (MDD)"
category: psychology/psychiatric-prescriber
description: "Reason through pharmacologic management of major depressive disorder: first-line agent selection, adequate-trial definition, partial- vs non-response branching, switch/augmentation strategies, treatment-resistant options, and measurement-based anchoring."
techniques:
  - RT-02
  - DT-01
  - DS-02
  - QA-04
  - CM-02
difficulty: advanced
intended_use: model-testing
tags:
  - MDD
  - antidepressant
  - augmentation
  - treatment-resistant-depression
  - measurement-based-care
  - psychopharmacology
updated: "2026-06-08"
related_prompts:
  - domain-psychology/psychiatric-prescriber/psychology_med_management_progress_note.md
  - domain-psychology/psychiatric-prescriber/psychology_bipolar_med_algorithm_reasoner.md
  - domain-psychology/treatment-planning/psychology_measurement_based_care_plan.md
  - domain-psychology/treatment-planning/psychology_stepped_care_decision_aid.md
---

# Depression Pharmacologic Algorithm Reasoner (MDD)

## Objective

Produce a structured pharmacologic reasoning pathway for an adult with unipolar major depressive disorder, identifying where the patient sits in a sequenced algorithm (first-line selection → adequate trial → response branching → switch/augment → treatment-resistant options) and recommending the next evidence-based step with explicit rationale. The reasoning must be anchored to measurement-based care and to recognized frameworks (APA Practice Guideline for MDD, VA/DoD, CANMAT) by name, name the drug class AND a representative generic agent with dosing, and include monitoring, warnings, and a bipolarity screen before antidepressant escalation.

## When to Use

- Selecting an initial antidepressant for a new MDD diagnosis.
- A patient has completed a trial and the prescriber must decide continue / optimize / switch / augment.
- Evaluating apparent treatment resistance and considering next-tier strategies.
- Reconciling a complex prior-trial history into a clear next move.

## Inputs / Context Required

- **Diagnosis & specifiers**: MDD single vs recurrent, severity, with anxious distress / melancholic / atypical / psychotic / peripartum / seasonal features.
- **Bipolarity screen result** (MDQ/clinical) — required before antidepressant escalation.
- **Prior antidepressant trials**: agent, max dose, duration at that dose, response, tolerability, reason discontinued.
- **Current measure scores**: PHQ-9 (or QIDS/MADRS) now vs baseline; remission threshold and MCID.
- **Comorbidities**: anxiety, pain, insomnia, OCD, substance use, cardiac/QTc, hepatic/renal, seizure risk, weight/metabolic concerns, sexual side-effect sensitivity.
- **Concomitant medications** for interaction screening (CYP, serotonergic load, MAOI washout constraints).
- **Suicide risk** status and age (< 25 black-box relevance).
- `[clinician input required: pregnancy/lactation status and reproductive plans]`
- `[clinician input required: patient preference re: side-effect tradeoffs and prior family medication response]`

## Constraints

### Must

- Begin with a **bipolarity / mixed-features screen**; if positive or suggestive, halt the unipolar algorithm and route to the bipolar reasoner before antidepressant escalation.
- Define an **adequate trial** explicitly: therapeutic dose maintained ≥ 4–6 weeks (8 weeks for full assessment) with documented adherence.
- Classify current status as: no trial yet / inadequate trial (dose or duration) / adequate trial with non-response (< 25%) / partial response (25–49%) / response (≥ 50%) / remission.
- Map status to the correct branch: optimize (push dose / extend) vs switch (within-class, cross-class) vs augment/combine vs treatment-resistant tier.
- For every recommended agent: name class + representative generic, starting dose, target range, and onset expectation.
- Name augmentation options with evidence support: **lithium** (target 0.6–0.8 mEq/L for augmentation; check renal/thyroid), **atypical antipsychotic** (e.g., aripiprazole 2–10 mg, quetiapine XR, brexpiprazole — with metabolic/AIMS monitoring), **T3/liothyronine** (~25–50 mcg; check TSH), and **bupropion combination** (with an SSRI/SNRI; note seizure threshold and eating-disorder contraindication).
- Address **treatment-resistant depression (TRD)** options after ≥ 2 adequate failed trials: **esketamine** (REMS, BP/dissociation monitoring), **MAOIs** (tyramine diet, washout, hypertensive crisis), and **ECT referral** (especially for psychotic/catatonic/acutely suicidal/pregnancy-appropriate cases).
- State monitoring and the **antidepressant black-box suicidality warning** for patients < 25, plus serotonin-syndrome and discontinuation-syndrome cautions.
- Anchor the recommendation to a named framework without fabricating page citations.

### Must Not

- Do not escalate antidepressants before screening for bipolarity/mixed features.
- Do not call a trial a "failure" if it was sub-therapeutic in dose or duration; label it inadequate and optimize first.
- Do not combine an MAOI with serotonergic agents or recommend without washout (≥ 2 weeks; 5 weeks for fluoxetine).
- Do not recommend bupropion in patients with seizure disorder or active eating disorder.
- Do not omit lithium/thyroid monitoring when lithium or T3 augmentation is proposed.
- Do not fabricate prior-trial details or scores; flag with `[clinician input required: ...]`.

## Instructions

1. **Screen for bipolarity/mixed features**; if suggestive, stop and route to the bipolar reasoner.
2. **Catalog prior trials** in a table and classify each as adequate or inadequate (dose × duration × adherence).
3. **Quantify current response** using PHQ-9/QIDS/MADRS vs baseline; assign status (non/partial/response/remission).
4. **Select the branch**:
   - No/inadequate trial → start or optimize a first-line SSRI/SNRI (e.g., sertraline, escitalopram, duloxetine, venlafaxine XR), matched to comorbidity (e.g., SNRI for comorbid pain, bupropion for fatigue/sexual-SE concern, mirtazapine for insomnia/appetite).
   - Adequate non-response → switch (cross-class often preferred after non-response).
   - Adequate partial response → augment/combine (optimize dose first if room remains).
   - ≥ 2 adequate failures → TRD tier.
5. **Specify the recommended next step** with agent, dose, titration, onset, and monitoring.
6. **List warnings/interactions** for the recommended agent.
7. **Set the re-measurement plan** (PHQ-9 cadence; reassessment at 4–6 weeks at therapeutic dose).
8. Include a **risk-reassessment hook** and, for high-acuity changes, a prescriber/supervisor co-sign line.
9. Run verification.

## Output Format

```
=== MDD PHARMACOLOGIC ALGORITHM REASONING ===

FRAMEWORK REFERENCED: [APA MDD Guideline / VA-DoD / CANMAT]

STEP 0 — BIPOLARITY / MIXED-FEATURES SCREEN
Result: [negative / suggestive — if suggestive, HALT and route to bipolar reasoner]

PRIOR-TRIAL CATALOG
| Agent (generic) | Max dose | Duration at dose | Adherence | Response | Adequate? |
|-----------------|----------|------------------|-----------|----------|-----------|
| [...] | [...] | [...] | [...] | [non/partial/resp] | [Yes/No — why] |

CURRENT RESPONSE STATUS
Measure: [PHQ-9 / QIDS / MADRS]  Now: [..]  Baseline: [..]  % change: [..]
Status: [no trial / inadequate / non-response / partial / response / remission]
Remission threshold: [e.g., PHQ-9 ≤ 4]   MCID: [≥ 5]

BRANCH SELECTED
[Optimize / Switch (within-class | cross-class) / Augment-Combine / TRD tier]
Rationale: [tie to status + comorbidity + tolerability + prior trials]

RECOMMENDED NEXT STEP
Agent: [Class] — [representative generic]
Start dose → target range: [...]
Expected onset / reassessment: [4–6 wks at therapeutic dose]
If augmentation: [lithium 0.6–0.8 mEq/L | aripiprazole 2–10 mg | liothyronine 25–50 mcg | bupropion combo]
Monitoring: [labs/levels/metabolic/AIMS/EKG as applicable]

TRD CONSIDERATIONS (if ≥ 2 adequate failures)
[Esketamine (REMS, BP/dissociation) | MAOI (washout, tyramine, hypertensive crisis) | ECT referral]

WARNINGS / INTERACTIONS
Black-box: [antidepressant suicidality, age <25]
Serotonin syndrome / discontinuation syndrome: [...]
Interaction cautions: [CYP / serotonergic load / MAOI washout]

RE-MEASUREMENT & RISK PLAN
PHQ-9 cadence: [...]   Next decision point: [date/criteria]
Risk-reassessment hook: [re-screen SI/C-SSRS at next visit and on dose change]

CO-SIGN (high-acuity changes)
Prescriber: __________  Supervising/collaborating prescriber: __________  Date: ______
```

## Verification

- [ ] Bipolarity/mixed-features screen performed before any antidepressant escalation.
- [ ] Prior trials cataloged and classified adequate vs inadequate by dose × duration × adherence.
- [ ] Current response quantified against a validated measure with status assigned.
- [ ] Branch (optimize/switch/augment/TRD) follows logically from status and comorbidity.
- [ ] Recommended agent names class + generic + dose/range + onset.
- [ ] Augmentation options (lithium, atypical, T3, bupropion combo) named with monitoring where proposed.
- [ ] TRD tier addressed after ≥ 2 adequate failures (esketamine/MAOI/ECT).
- [ ] Black-box suicidality (<25), serotonin-syndrome, and discontinuation cautions stated.
- [ ] MAOI washout and bupropion contraindications respected.
- [ ] Re-measurement cadence and risk-reassessment hook present.
- [ ] Framework named without fabricated citations.
- [ ] Nothing fabricated; gaps flagged `[clinician input required]`.
```
