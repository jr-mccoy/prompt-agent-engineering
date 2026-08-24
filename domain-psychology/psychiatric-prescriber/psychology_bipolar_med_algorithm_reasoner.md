---
title: "Bipolar Pharmacologic Algorithm Reasoner (Mania / Bipolar Depression / Maintenance)"
category: psychology/psychiatric-prescriber
description: "Reason through mood-stabilizer, antipsychotic, and antidepressant decisions across bipolar phases — acute mania, bipolar depression, and maintenance — including lithium, valproate, lamotrigine, atypicals, antidepressant-switch caution, level/lab monitoring, and pregnancy considerations."
techniques:
  - RT-02
  - DT-01
  - DS-02
  - QA-04
  - CM-02
difficulty: advanced
intended_use: model-testing
tags:
  - bipolar-disorder
  - mood-stabilizer
  - lithium
  - lamotrigine
  - atypical-antipsychotic
  - psychopharmacology
updated: "2026-06-08"
related_prompts:
  - domain-psychology/psychiatric-prescriber/psychology_depression_med_algorithm_reasoner.md
  - domain-psychology/psychiatric-prescriber/psychology_med_management_progress_note.md
  - domain-psychology/psychiatric-prescriber/psychology_psychotropic_taper_plan.md
  - domain-psychology/treatment-planning/psychology_measurement_based_care_plan.md
---

# Bipolar Pharmacologic Algorithm Reasoner (Mania / Bipolar Depression / Maintenance)

## Objective

Produce a structured pharmacologic reasoning pathway for an adult with bipolar I or II disorder, identifying the current illness phase (acute mania/hypomania, acute bipolar depression, or maintenance) and recommending an evidence-based regimen with explicit rationale. The reasoning must name the drug class AND a representative generic agent with dosing and target levels, specify monitoring, address the antidepressant-induced switch risk, and incorporate pregnancy considerations. Anchor to recognized frameworks (CANMAT/ISBD, APA, NICE) by name.

## When to Use

- Acute mania or mixed/hypomanic presentation requiring stabilization.
- Acute bipolar depression where antidepressant monotherapy must be avoided.
- Building or revising a maintenance regimen to prevent recurrence.
- A patient with bipolar disorder of childbearing potential where teratogenic-risk planning is needed.

## Inputs / Context Required

- **Bipolar subtype** (I vs II) and **current phase** (mania/hypomania, mixed features, depression, euthymic maintenance).
- **Episode severity / safety**: psychosis, agitation, suicidality, sleep loss, insight, ability to maintain safety.
- **Prior medication response**: which mood stabilizers/antipsychotics worked, levels achieved, tolerability.
- **Current regimen** and adherence; any current antidepressant on board.
- **Labs/levels**: lithium level, valproate level, renal (eGFR), thyroid (TSH), CBC, LFTs, metabolic panel, EKG/QTc, weight/BMI.
- **Rapid-cycling** status; substance use; comorbid conditions.
- `[clinician input required: pregnancy/lactation status and reproductive plans]`
- `[clinician input required: most recent therapeutic drug levels and dates]`

## Constraints

### Must

- Identify the **phase first**; phase determines the algorithm branch.
- **Acute mania**: recommend an evidence-based mood stabilizer and/or atypical antipsychotic — **lithium** (target ~0.8–1.2 mEq/L acutely), **valproate/divalproex** (level ~50–125 µg/mL), or an **atypical antipsychotic** (e.g., risperidone, olanzapine, quetiapine, aripiprazole, cariprazine, asenapine); combination (lithium/valproate + atypical) for severe mania. Discontinue/taper any antidepressant.
- **Acute bipolar depression**: prioritize agents with bipolar-depression evidence — **quetiapine**, **lurasidone** (take with ≥ 350 kcal food; metabolic-favorable), **cariprazine**, **lamotrigine** (maintenance/depression; requires slow titration for SJS risk), or **lithium**; **olanzapine-fluoxetine combination** as an option. Avoid antidepressant monotherapy; if an antidepressant is used, it must be with a mood stabilizer/antipsychotic and with switch-risk monitoring.
- **Maintenance**: lithium (strong anti-suicide/relapse evidence), lamotrigine (better for depressive-pole prevention), valproate, or maintenance atypicals; select by predominant polarity and prior response.
- State the **antidepressant-induced manic/hypomanic switch risk** and rapid-cycling worsening; require a mood stabilizer "umbrella" and close monitoring whenever an antidepressant is present.
- Specify **monitoring**: lithium (level + renal + thyroid + calcium; check level 5 days after change and periodically; toxicity signs), valproate (level + LFTs + CBC; pancreatitis/hepatotoxicity; PCOS/weight), lamotrigine (slow titration; rash/SJS counseling; interaction with valproate doubling levels and OCPs lowering levels), atypicals (metabolic panel, lipids, HbA1c, weight, AIMS, prolactin, QTc).
- Address **pregnancy/teratogenicity**: valproate and carbamazepine carry high teratogenic risk (neural tube defects, neurodevelopmental); lithium (Ebstein anomaly risk, generally lower than valproate); lamotrigine and some atypicals relatively preferred — frame as risk-benefit with maternal-fetal/OB coordination.
- Anchor to a named framework without fabricating page citations.

### Must Not

- Do not recommend antidepressant monotherapy for bipolar depression.
- Do not leave an antidepressant running during acute mania without a taper plan.
- Do not start lamotrigine at a high dose or fast titration (SJS risk); always specify the slow titration and the valproate-interaction adjustment.
- Do not default to valproate or carbamazepine in a patient of childbearing potential without explicit teratogenic-risk discussion and alternatives.
- Do not omit level/lab monitoring for lithium, valproate, or lamotrigine.
- Do not fabricate levels or prior response; flag with `[clinician input required: ...]`.

## Instructions

1. **Determine phase and subtype** (I/II; mania/hypomania, mixed, depression, maintenance) and assess safety/psychosis.
2. **Review prior response and current levels/labs**; note adherence and any antidepressant on board.
3. **Select the phase-appropriate branch**:
   - Mania → mood stabilizer and/or atypical (± combination for severe); taper antidepressant.
   - Bipolar depression → quetiapine/lurasidone/cariprazine/lamotrigine/lithium (± OFC); avoid AD monotherapy.
   - Maintenance → lithium/lamotrigine/valproate/atypical by predominant polarity and prior response.
4. **Name the agent(s)** with class, generic, dose, and target level/range.
5. **Specify monitoring** for each agent and the antidepressant switch-risk plan.
6. **Apply pregnancy/teratogenicity reasoning** where childbearing potential is present.
7. **Set re-measurement** (mood charting, relevant scales) and a **risk-reassessment hook**; include a co-sign line for acute high-acuity changes.
8. Run verification.

## Output Format

```
=== BIPOLAR PHARMACOLOGIC ALGORITHM REASONING ===

FRAMEWORK REFERENCED: [CANMAT/ISBD / APA / NICE]
SUBTYPE: [Bipolar I / II]   PHASE: [Mania/Hypomania | Mixed | Bipolar depression | Maintenance]
Safety: [psychosis/agitation/suicidality/sleep — describe]   Antidepressant on board: [Yes/No]

PRIOR RESPONSE & CURRENT LEVELS/LABS
| Agent | Best level/dose | Response | Tolerability |
|-------|-----------------|----------|--------------|
| [...] | [...] | [...] | [...] |
Current levels: Lithium [.. mEq/L] | Valproate [.. µg/mL] | Renal/TSH/LFTs/Metabolic: [..]
[clinician input required: most recent levels + dates]

BRANCH SELECTED (phase-appropriate)
[Acute mania | Bipolar depression | Maintenance]
Recommended regimen:
- Mood stabilizer: [lithium 0.8–1.2 acute | valproate 50–125 µg/mL | lamotrigine (slow titration)]
- Atypical antipsychotic: [quetiapine | lurasidone (w/ food) | cariprazine | aripiprazole | risperidone | olanzapine]
- Combination: [if severe mania — stabilizer + atypical]
Antidepressant plan: [taper if manic | only with stabilizer umbrella + switch monitoring]

MONITORING
Lithium: [level + renal + thyroid + calcium; recheck 5 days post-change; toxicity signs]
Valproate: [level + LFTs + CBC; pancreatitis/hepatotoxicity; weight/PCOS]
Lamotrigine: [slow titration; SJS/rash counseling; valproate doubles level; OCP lowers level]
Atypicals: [metabolic panel, lipids, HbA1c, weight, AIMS, prolactin, QTc]

ANTIDEPRESSANT SWITCH-RISK NOTE
[Manic/hypomanic switch + rapid-cycling risk; require mood-stabilizer coverage + close monitoring.]

PREGNANCY / TERATOGENICITY (if childbearing potential)
[Valproate/carbamazepine high risk (NTD/neurodevelopment); lithium (Ebstein); lamotrigine/select atypicals
relatively preferred. Risk-benefit + OB/maternal-fetal coordination. clinician input required: status.]

RE-MEASUREMENT & RISK PLAN
Mood charting / scales: [...]   Level recheck schedule: [...]
Risk-reassessment hook: [re-screen SI/C-SSRS; reassess on dose/level change]

CO-SIGN (acute high-acuity changes)
Prescriber: __________  Supervising/collaborating prescriber: __________  Date: ______
```

## Verification

- [ ] Illness phase and subtype identified before agent selection.
- [ ] Acute mania branch uses mood stabilizer and/or atypical (± combination) with target levels; antidepressant tapered.
- [ ] Bipolar depression branch uses evidence-based agents; antidepressant monotherapy avoided.
- [ ] Maintenance branch selected by predominant polarity and prior response.
- [ ] Each agent named with class + generic + dose + target level/range.
- [ ] Lamotrigine slow-titration and valproate/OCP interactions specified.
- [ ] Monitoring specified for lithium, valproate, lamotrigine, and atypicals (metabolic/AIMS/QTc/prolactin).
- [ ] Antidepressant-induced switch risk and mood-stabilizer-umbrella requirement stated.
- [ ] Pregnancy/teratogenicity reasoning applied where relevant.
- [ ] Re-measurement plan and risk-reassessment hook present; co-sign line included.
- [ ] Framework named without fabricated citations.
- [ ] Nothing fabricated; gaps flagged `[clinician input required]`.
```
