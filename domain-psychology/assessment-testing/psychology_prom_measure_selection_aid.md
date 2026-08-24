---
title: "Patient-Reported Outcome Measure (PROM) Selection Aid"
category: psychology/assessment-testing
description: "Select patient-reported outcome measures matched to presentation and setting — mapping construct, population, setting, administration burden, cadence, sensitivity to change, and licensing into a measurement-based-care recommendation."
techniques:
  - ST-04
  - DT-02
  - QA-04
  - CM-02
  - DS-04
difficulty: intermediate
intended_use: model-testing
tags:
  - PROM
  - measurement-based-care
  - PHQ-9
  - GAD-7
  - PCL-5
  - OQ-45
  - ORS-SRS
  - WHODAS
  - outcome-monitoring
updated: "2026-06-08"
related_prompts:
  - domain-psychology/treatment-planning/psychology_measurement_based_care_plan.md
  - domain-psychology/intake-assessment/psychology_screening_battery_interpreter.md
  - domain-psychology/measurement-based-care/psychology_mbc_implementation_plan_for_practice.md
---

# Patient-Reported Outcome Measure (PROM) Selection Aid

## Objective

Given a clinical presentation and a practice setting, recommend a fit-for-purpose set of patient-reported outcome measures (PROMs) for measurement-based care (MBC). The aid maps the **target construct(s)** to be tracked against candidate instruments and weighs them across: population/age validity, setting fit (primary care vs. specialty mental health vs. telehealth), administration burden (item count, time, reading level), monitoring cadence, **sensitivity to change** (responsiveness over time vs. trait stability), and **licensing/cost** (public-domain vs. proprietary). The output is a recommended baseline-plus-monitoring battery with a cadence schedule and a fallback if the first-line measure is unavailable or unsuitable. This aid selects and structures measures; it does not interpret scores or assign diagnoses.

## When to Use

- Standing up measurement-based care for a caseload, program, or practice and needing a default battery.
- Onboarding a new client whose presentation does not fit the practice's existing standard panel.
- Choosing a progress/process monitor (session-by-session) distinct from a baseline severity measure.
- Switching from a proprietary instrument to a public-domain alternative for cost or licensing reasons.
- Adapting a battery for telehealth, low-literacy, or brief-visit primary-care contexts.

This aid assumes a clinician will administer, score, and interpret the selected measures within their scope. It is a selection tool, not a substitute for clinical evaluation or for the publisher's manual.

## Inputs / Context Required

Provide what is known; flag the rest so the output recommends defaults rather than fabricating fit.

- **Primary clinical target(s) to track:** e.g., depression severity, anxiety, PTSD symptoms, global distress, functioning/disability, alliance, substance-use risk `[clinician input required]`
- **Population:** age band (child/adolescent/adult/older adult), and any language/literacy considerations.
- **Setting:** primary care / integrated behavioral health / specialty outpatient / intensive outpatient / inpatient / telehealth-only / hybrid.
- **Purpose of measurement:** baseline severity, repeated outcome monitoring, session-by-session process feedback, treatment-response tracking, or program-level aggregate reporting.
- **Cadence constraint:** how often the measure can realistically be administered (every session / biweekly / monthly / intake-and-discharge only).
- **Burden ceiling:** acceptable item count and completion time per administration.
- **Licensing/budget constraints:** must be public-domain/free, or proprietary acceptable with budget `[clinician input required]`
- **Existing measures already in use** (to avoid redundant constructs).
- **Reporting/interop requirements:** registry submission, EHR-embedded scoring, value-based-care metric alignment.

## Constraints

### Must

- Map each recommended measure to the **specific construct** it tracks; do not recommend a depression scale to monitor functioning, or a severity scale where a process/alliance monitor is needed.
- State each measure's **public-domain vs. proprietary** status and the practical licensing implication (free use vs. permission/fee). Where status is uncertain, label it `[verify licensing — publisher-dependent]` rather than asserting it is free.
- Distinguish **baseline/severity measures** (e.g., PHQ-9, GAD-7, PCL-5, WHODAS) from **session-by-session process/feedback measures** (e.g., ORS/SRS, OQ-45 with its alliance companion) and recommend at least one of each when the purpose calls for ongoing monitoring.
- Note **sensitivity to change**: flag whether a candidate is designed to detect short-interval change or is a more stable trait/screening instrument better suited to intake-and-discharge.
- Match **burden to setting**: prefer ultra-brief measures (e.g., PHQ-2/GAD-2, ORS/SRS) where visit time or reading load is constrained; reserve longer batteries (e.g., OQ-45, PCL-5 full) for settings that can sustain them.
- Provide a **cadence recommendation** per measure (e.g., baseline + every visit; baseline + monthly; intake/discharge only).
- Provide a **fallback measure** for each primary target if the first choice is unavailable, unaffordable, or population-inappropriate.
- State explicitly what the recommended battery **cannot** answer (e.g., PROMs do not establish diagnosis, do not assess capacity, do not replace risk assessment).

### Must Not

- Do not reproduce, paraphrase, or embed any copyrighted instrument's items, exact wording, full normative tables, or proprietary scoring keys. Reference instruments **by name only**, and describe structure/score range/score bands at a level that does not reconstruct the instrument.
- Do not assign cutoffs as diagnostic thresholds; PROM bands indicate probable severity ranges, not diagnoses.
- Do not recommend a measure validated only in one population (e.g., a military-sample PTSD cutoff) for an unvalidated population without flagging the mismatch.
- Do not fabricate licensing terms, validation status, or psychometric properties; flag uncertainty with `[verify in publisher manual]`.
- Do not omit a risk/safety note when the tracked construct (e.g., depression) includes a suicidality item that requires its own monitoring and response pathway.

## Instructions

1. **Identify the constructs to track.** Convert the clinical target(s) into measurable constructs (e.g., "is he getting less depressed?" → depression severity; "is therapy working overall?" → global distress + functioning). Separate severity constructs from process constructs (alliance, session feedback).

2. **Generate candidate measures per construct.** For each construct, list 2–4 named candidates with: typical item count, approximate completion time, score range, number of severity bands (named, not reproduced), public-domain vs. proprietary status, validated population(s), and whether it is responsive to short-interval change.

3. **Score candidates against the setting.** Apply the decision factors — population validity, setting fit, burden ceiling, cadence feasibility, sensitivity to change, licensing/cost. Eliminate poor fits and note why.

4. **Assemble the recommended battery.** Choose: (a) one baseline/severity measure per primary construct, (b) at least one process/feedback measure if ongoing monitoring is the purpose, and (c) a functioning/disability measure (e.g., WHODAS) when functional outcome matters beyond symptoms.

5. **Set the cadence schedule.** Specify administration timing per measure (intake, every session, biweekly, monthly, discharge), balancing signal value against burden and against minimum-interval-for-reliable-change considerations.

6. **Define the fallback set.** For each primary measure, name a substitute and the trigger for using it (unavailable, cost, population mismatch, reading level).

7. **State scope and safety.** Note what the battery cannot answer and identify any item-level safety flag (e.g., a depression measure's suicidality item) that requires a separate response pathway.

8. **Run verification.**

## Output Format

### Selection Context

```
CONSTRUCT(S) TO TRACK: [list]
POPULATION / AGE BAND: [ ... ]
SETTING: [primary care / specialty / IOP / telehealth / ...]
PURPOSE: [baseline / repeated monitoring / session feedback / program reporting]
CADENCE CONSTRAINT: [ ... ]    BURDEN CEILING: [ ~N items / ~N min ]
LICENSING CONSTRAINT: [public-domain required / proprietary OK]
OUTPUT STATUS: Measure-selection scaffold — administration, scoring, and interpretation remain the clinician's
```

### Candidate Comparison (per construct)

| Measure (name only) | Construct | Items / ~Time | Score Range | Bands | License | Validated Population | Sensitive to Change? | Setting Fit |
|---------------------|-----------|---------------|-------------|-------|---------|----------------------|----------------------|-------------|
| [Name] | [construct] | [N / ~min] | [low–high] | [N named bands] | [public-domain / proprietary / verify] | [pop] | [Yes / Limited / Trait] | [Good / Marginal / Poor — why] |

### Recommended Battery

| Role | Measure | Cadence | Rationale | Fallback (+ trigger) |
|------|---------|---------|-----------|----------------------|
| Baseline severity | [Name] | [intake + ...] | [ ... ] | [Name — when X] |
| Process / feedback | [Name, e.g., ORS/SRS] | [every session] | [ ... ] | [Name — when X] |
| Functioning / disability | [Name, e.g., WHODAS] | [intake + monthly] | [ ... ] | [Name — when X] |

### Scope and Safety Note

```
THIS BATTERY CAN ANSWER: [e.g., change in depression severity over time; alliance trend]
THIS BATTERY CANNOT ANSWER: [diagnosis; capacity; standalone risk determination]
ITEM-LEVEL SAFETY FLAG: [e.g., depression-measure suicidality item — route to risk-assessment + response pathway]
LICENSING ACTIONS NEEDED: [obtain permission / confirm free use / budget line]
```

## Verification

- [ ] Each recommended measure is mapped to the specific construct it tracks.
- [ ] Baseline/severity measures are distinguished from process/feedback measures; both are present when ongoing monitoring is the purpose.
- [ ] Each measure's public-domain vs. proprietary status is stated, with uncertainty flagged rather than asserted.
- [ ] Sensitivity to change vs. trait stability is noted for each candidate.
- [ ] Burden and cadence are matched to the stated setting and constraints.
- [ ] A fallback measure and its trigger are given for each primary target.
- [ ] The scope note states what the battery cannot answer (diagnosis/capacity/standalone risk).
- [ ] Any embedded suicidality/safety item is flagged with a separate response pathway.
- [ ] No copyrighted item content, exact item wording, full normative tables, or proprietary scoring keys are reproduced — instruments referenced by name and band/structure only.
- [ ] No psychometric or licensing properties are fabricated; uncertainty carries `[verify in publisher manual]`.
