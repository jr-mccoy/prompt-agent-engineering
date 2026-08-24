---
title: "Psychotropic Taper Plan Builder"
category: psychology/psychiatric-prescriber
description: "Build a class-specific taper plan for SSRI/SNRI, benzodiazepine, antipsychotic, or mood stabilizer discontinuation — with per-class taper rates, crossover/bridging logic, monitoring, and abort/hold criteria."
techniques:
  - DT-01
  - RT-02
  - DS-02
  - QA-04
  - CM-02
difficulty: advanced
intended_use: model-testing
tags:
  - taper
  - discontinuation-syndrome
  - benzodiazepine-taper
  - deprescribing
  - withdrawal
  - psychopharmacology
updated: "2026-06-08"
related_prompts:
  - domain-psychology/psychiatric-prescriber/psychology_med_management_progress_note.md
  - domain-psychology/psychiatric-prescriber/psychology_anxiety_med_algorithm_reasoner.md
  - domain-psychology/psychiatric-prescriber/psychology_bipolar_med_algorithm_reasoner.md
  - domain-psychology/treatment-planning/psychology_measurement_based_care_plan.md
---

# Psychotropic Taper Plan Builder

## Objective

Generate a class-specific, step-by-step deprescribing/taper plan for a psychotropic medication — SSRI/SNRI, benzodiazepine, antipsychotic, or mood stabilizer — that specifies the taper rate, crossover/bridging logic where applicable, the monitoring schedule, and explicit abort/hold criteria. The plan must distinguish discontinuation syndrome from relapse, name the agent (generic) with concrete dose decrements, and incorporate withdrawal-risk safeguards (e.g., seizure risk in benzodiazepine withdrawal). Anchor to recognized deprescribing guidance (Maudsley Deprescribing Guidelines, Ashton Manual for benzodiazepines) by name.

## When to Use

- Discontinuing an antidepressant after remission/maintenance, or switching with a cross-taper.
- Tapering a benzodiazepine for dependence, sedation, falls, or substance-use concern.
- Reducing or stopping an antipsychotic where rebound/supersensitivity is a concern.
- Discontinuing a mood stabilizer where relapse risk must be managed.

## Inputs / Context Required

- **Agent, current dose, formulation, and duration of use** (longer use → slower taper).
- **Reason for taper** (remission, side effects, switch, deprescribing, pregnancy, patient preference).
- **Class** (SSRI/SNRI, benzodiazepine, antipsychotic, mood stabilizer) and half-life of the specific agent.
- **Relapse risk**: number/severity of prior episodes, current stability, supports.
- **Withdrawal history**: prior failed tapers, seizures, severe discontinuation symptoms.
- **Comorbidities** and concurrent medications (interactions, additive sedation).
- **Setting**: outpatient vs higher level of care for high-risk tapers.
- `[clinician input required: prior taper attempts and what happened]`
- `[clinician input required: substance-use history relevant to sedative tapers]`

## Constraints

### Must

- Identify the **class and the specific agent's half-life**; pacing follows from these.
- **SSRI/SNRI**: taper gradually to avoid **discontinuation syndrome** (FINISH: Flu-like, Insomnia, Nausea, Imbalance, Sensory disturbances/"brain zaps," Hyperarousal); short-half-life agents (paroxetine, venlafaxine) need slower, smaller decrements; consider **hyperbolic/proportional tapering** (smaller percentage steps as dose lowers); fluoxetine's long half-life can self-taper or serve as a bridge. Distinguish discontinuation symptoms (onset within days, resolve on dose reinstatement) from **relapse** (later onset, original-episode symptoms).
- **Benzodiazepine**: use a **slow, percentage-based taper** (e.g., ~5–10% of current dose every 1–2 weeks, slowing near the end), consider **crossover to a long-half-life agent (diazepam) equivalent** for short-acting/high-potency agents (e.g., alprazolam), and explicitly flag **withdrawal-seizure risk and the danger of abrupt discontinuation**; reference the Ashton approach.
- **Antipsychotic**: taper gradually to mitigate **rebound psychosis, withdrawal dyskinesia, and dopamine supersensitivity**; slower for long-duration/high-dose use and for clozapine (cholinergic rebound risk); monitor for symptom re-emergence.
- **Mood stabilizer**: taper gradually (especially **lithium** — abrupt discontinuation raises relapse/rebound-mania risk; lamotrigine and valproate also tapered) with relapse monitoring and level checks where relevant.
- Provide a **concrete decrement schedule** (dose, interval) — not just "taper slowly."
- Define **monitoring** (symptom re-emergence, withdrawal symptoms, vitals/levels as relevant) and **abort/hold criteria** (e.g., intolerable withdrawal, symptom relapse, safety concern → hold at current dose or reinstate; for benzodiazepines, never accelerate, and treat withdrawal seriously).
- Include a **risk-reassessment hook** and a co-sign line for high-risk tapers (benzodiazepine with seizure history, high-dose antipsychotic, lithium in a high-relapse patient).
- Anchor to a named deprescribing framework without fabricating page citations.

### Must Not

- Do not recommend abrupt discontinuation of benzodiazepines, lithium, or high-dose antipsychotics.
- Do not use fixed-percentage-of-original (linear) steps where hyperbolic tapering is indicated at low doses.
- Do not conflate discontinuation syndrome with relapse; the plan must include the differentiation logic.
- Do not omit seizure-risk warning in benzodiazepine tapers.
- Do not omit the option to hold/slow when withdrawal is intolerable.
- Do not fabricate dose-equivalence figures or prior taper history; flag with `[clinician input required: ...]`.

## Instructions

1. **Identify class, agent, half-life, dose, and duration of use**; assess relapse and withdrawal risk.
2. **Select the taper template** for the class and adjust speed for half-life, duration, and prior taper history.
3. **For short-half-life or high-potency agents**, specify crossover/bridging (e.g., diazepam crossover for short-acting benzodiazepines; fluoxetine bridge for difficult SSRI tapers).
4. **Write a concrete decrement schedule** (dose → dose, interval), slowing near the end (hyperbolic where indicated).
5. **Define monitoring** (symptoms, withdrawal, vitals/levels) and the **discontinuation-vs-relapse** differentiation.
6. **Set abort/hold criteria** and the response (hold, slow, reinstate, escalate care).
7. **Add a risk-reassessment hook** and co-sign line for high-risk tapers.
8. Run verification.

## Output Format

```
=== PSYCHOTROPIC TAPER PLAN ===

FRAMEWORK REFERENCED: [Maudsley Deprescribing Guidelines / Ashton Manual (benzodiazepines)]
AGENT (generic): [..]   Class: [SSRI/SNRI | Benzodiazepine | Antipsychotic | Mood stabilizer]
Current dose / formulation: [..]   Half-life: [..]   Duration of use: [..]
Reason for taper: [..]   Relapse risk: [low/moderate/high]   Prior taper history: [clinician input required]

TAPER STRATEGY
Pacing principle: [gradual; slower for short half-life/long duration; hyperbolic at low doses]
Crossover/bridge (if applicable): [diazepam crossover for short-acting benzo | fluoxetine bridge for SSRI]

DECREMENT SCHEDULE
| Step | Dose | Interval at this dose | Notes |
|------|------|-----------------------|-------|
| 1 | [..] | [1–2 wks] | [...] |
| 2 | [..] | [...] | [smaller % steps as dose lowers] |
| ... | ... | ... | [final steps slowest] |

CLASS-SPECIFIC CAUTIONS
[SSRI/SNRI: FINISH discontinuation syndrome; paroxetine/venlafaxine slower]
[Benzodiazepine: WITHDRAWAL-SEIZURE RISK; never abrupt; ~5–10% q1–2 wks]
[Antipsychotic: rebound psychosis/withdrawal dyskinesia/supersensitivity; clozapine cholinergic rebound]
[Mood stabilizer: lithium abrupt-stop relapse/rebound-mania risk; level checks]

MONITORING
Symptoms tracked: [withdrawal vs re-emergence]   Vitals/levels: [as relevant]
Discontinuation-vs-relapse logic: [discontinuation = onset within days, resolves on reinstatement;
relapse = later onset, original-episode symptoms]

ABORT / HOLD CRITERIA
- Intolerable withdrawal → [hold at current dose / lengthen interval / reinstate prior dose]
- Symptom relapse → [hold and reassess treatment; do not force taper]
- Safety concern (seizure risk, severe symptoms) → [escalate care / higher LOC]
Never accelerate a benzodiazepine taper; treat withdrawal seriously.

RE-ASSESSMENT
Follow-up cadence: [..]   Risk-reassessment hook: [re-screen SI/relapse at each step-down]

CO-SIGN (high-risk tapers)
Prescriber: __________  Supervising/collaborating prescriber: __________  Date: ______
```

## Verification

- [ ] Class, agent, half-life, dose, and duration of use identified.
- [ ] Taper pacing matched to half-life, duration, and prior taper history.
- [ ] Crossover/bridge specified where indicated (diazepam crossover; fluoxetine bridge).
- [ ] Concrete decrement schedule with doses and intervals, slowing near the end (hyperbolic where indicated).
- [ ] Class-specific cautions present (FINISH; benzo seizure risk; antipsychotic rebound/supersensitivity; lithium abrupt-stop risk).
- [ ] Discontinuation-syndrome vs relapse differentiation included.
- [ ] Abort/hold criteria with concrete responses; benzodiazepine taper never accelerated.
- [ ] Monitoring (symptoms, vitals/levels) specified.
- [ ] Risk-reassessment hook and co-sign line for high-risk tapers present.
- [ ] Framework named without fabricated citations.
- [ ] Nothing fabricated; gaps flagged `[clinician input required]`.
```
