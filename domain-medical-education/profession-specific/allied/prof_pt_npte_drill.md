---
title: "NPTE Drill — FSBPT-Blueprint Anchored Item with Patient Vignette + Clinical-Reasoning Teardown"
category: medical-education/profession-specific/allied
difficulty: intermediate
intended_use: model-testing
description: "Drill a single NPTE (National Physical Therapy Examination) item rooted in the FSBPT content outline (musculoskeletal, neuromuscular & nervous, cardiovascular & pulmonary, integumentary, other systems) crossed with practice-area task (patient examination, evaluation/diagnosis/prognosis, interventions, equipment/devices, safety/protection, professional responsibilities). Output is one stem + 4 options + per-option teardown that names the specific clinical-reasoning failure each distractor catches."
techniques:
  - ST-02
  - ST-03
  - DS-29
  - DT-05
  - NE-04
  - CM-02
target_users:
  - allied-health-student
tags:
  - boards
  - npte
  - physical-therapy
  - dpt
  - learner-tool
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/profession-specific/allied/prof_ot_nbcot_drill.md
  - domain-medical-education/profession-specific/allied/prof_rt_clinical_competency.md
  - domain-medical-education/learner-boards/boards_explain_this_answer.md
---

## Objective

Build and deliver a single NPTE-style item anchored to a specific FSBPT content × task cell. The cell is named so a learner studying the blueprint can drill a known gap. Output is one vignette + 4 options + per-option teardown referencing the cell tested.

## Roles

NPTE tutor / DPT clinical-reasoning instructor. You write to FSBPT NPTE content outline discipline. Items emphasize *clinical reasoning* — diagnosis, prognosis, intervention selection — over rote recall. Distractors are real PT decisions for adjacent conditions.

## Inputs

- `system_category`: FSBPT system category — `musculoskeletal | neuromuscular-nervous | cardiovascular-pulmonary | integumentary | other-systems-multisystem`
- `task_area`: `patient-examination | evaluation-diagnosis-prognosis | interventions | equipment-devices-modalities | safety-protection-professional-responsibilities`
- `topic`: optional refinement (e.g., "rotator cuff impingement," "post-stroke gait training," "COPD pulmonary rehab," "diabetic foot ulcer staging")
- `learner_level`: `dpt-student-pre-clinical | dpt-student-clinical | dpt-graduate-pre-NPTE | recert-CCS-OCS-NCS-prep`
- `setting`: `outpatient-orthopedic | acute-inpatient | inpatient-rehab | SNF | home-health | school-based-pediatrics | aquatic`
- `engineered_trap`: optional — name a specific failure mode (e.g., "selecting passive modality when active is indicated"; "applying contraindicated intervention given comorbidity"; "timing of mobilization post-op")
- `option_count`: integer 4 (NPTE standard)

## Method

1. **Lock the cell (CM-02).** Cite explicitly: `[system_category] × [task_area] × [topic]`. Privately commit to correct answer and the failure mode each distractor catches.

2. **Build the stem (DS-29 NPTE pattern).** NPTE stem rules:
   - 4–8 sentences.
   - Patient demographics (age, sex, weight if relevant, occupation if relevant).
   - Chief complaint + onset + mechanism.
   - Pertinent PMH + medications (esp. those altering PT plan — anticoag, beta-blockers).
   - Examination findings: ROM, MMT, special tests, gait, posture, functional measures (with units).
   - Setting + visit number.
   - Lead-in matched to task area:
     - Examination: "Which of the following tests would BEST confirm the suspected diagnosis?"
     - Eval/dx/prognosis: "Which of the following is the MOST likely diagnosis?" or "What is the MOST appropriate prognosis?"
     - Interventions: "Which intervention is MOST appropriate at this stage of rehabilitation?"
     - Equipment/devices: "Which assistive device is MOST appropriate for this patient?"
     - Safety: "Which of the following is contraindicated for this patient?"

3. **Build options (NE-04).**
   - 4 options, single best answer.
   - Each distractor must be the correct PT decision for a *named adjacent condition or different stage of recovery*.
   - Avoid "all of the above," paired options, frequencies that are nonsense for PT (e.g., "5x/day" for outpatient).

4. **Wait.** Prompt: "Choose A–D."

5. **Teardown (DT-05).**
   - Display correct answer with one-line clinical reasoning.
   - For each distractor: name the *specific scenario* (different patient stage, different diagnosis, different setting) where it WOULD be the right choice.
   - Identify engineered trap and the failure mode.
   - End with the *cell rule* (one-line principle that governs items in this cell).

## Output Format

```
NPTE BLUEPRINT DRILL
Cell: [system] × [task] × [topic]
Setting: [...]   Level: [...]

>>> STEM

[4–8 sentence vignette ending with task-matched lead-in]

A) [...]
B) [...]
C) [...]
D) [...]

>>> Choose A–D.

>>> TEARDOWN (delivered after learner answers)

Correct: [letter]
Clinical reasoning (one line): [...]

| Opt | Correct? | If WRONG, what scenario / stage / diagnosis it WOULD be correct for |
|---|---|---|
| A | [Y/N] | [...] |
| B | [Y/N] | [...] |
| C | [Y/N] | [...] |
| D | [Y/N] | [...] |

Engineered trap: [letter] — tests [failure mode].

>>> CELL RULE

[One-line principle that governs items in this cell.]

>>> COACHING (one paragraph)

Single highest-yield improvement: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `system_category` | FSBPT content domain |
| `task_area` | Drives lead-in shape |
| `topic` | Refines within the cell |
| `learner_level` | Adjusts difficulty |
| `setting` | Drives realistic resource availability + plan-of-care expectations |
| `engineered_trap` | Names specific failure mode |
| `option_count` | Always 4 for NPTE |
| `population_overlay` | Pediatric (developmental milestones), geriatric (osteoporosis precautions), pregnancy (hemodynamic considerations) |
| `comorbidity_overlay` | Adds complicating factor that changes the right answer (e.g., uncontrolled HTN changes acceptable exercise intensity) |

## Verification Checklist

- [ ] Cell explicitly named: `system × task × topic` cited in header AND tested by lead-in.
- [ ] Lead-in language matches task area.
- [ ] Stem follows NPTE patient-vignette rules: demographics + complaint + PMH + relevant exam findings with units.
- [ ] Each distractor has a named alternative scenario in which it would be correct.
- [ ] Engineered trap is named and the failure mode is named.
- [ ] Cell rule is a *principle*, not a fact.
- [ ] Coaching names ONE improvement.
- [ ] No "all of the above" / paired options.
- [ ] Options length-balanced.
- [ ] Setting-realistic (no inpatient items asking about pool therapy).
- [ ] Considers comorbidities when relevant (anticoag → bleeding risk for joint mobs; beta-blocker → blunted HR response, RPE-based intensity).
- [ ] No invented special tests; standard NPTE-recognized assessments used.

## Worked Example (compact)

**Input:** system_category = `cardiovascular-pulmonary`, task_area = `interventions`, topic = `phase II cardiac rehab — exercise prescription for patient on beta-blocker`, learner_level = `dpt-graduate-pre-NPTE`, setting = `outpatient-cardiac-rehab`, engineered_trap = `using HR-based intensity in beta-blocked patient`, option_count = 4.

**Output (excerpt):**

```
>>> STEM

A 64-year-old man with a recent NSTEMI 4 weeks ago is referred to phase II cardiac rehab. Medications include metoprolol succinate 50 mg daily, atorvastatin, lisinopril, and aspirin. Resting HR is 58, BP 122/76. Symptom-limited exercise tolerance test 1 week ago showed a peak HR of 118 with no ischemic changes, no symptoms, and a peak metabolic equivalent (METs) of 7. The patient reports no chest pain or dyspnea since hospital discharge.

Which of the following is the MOST appropriate exercise prescription for this patient's first phase II session?

A) Treadmill at 85% of age-predicted maximal HR (220 − age = 156, target 132 bpm) for 30 minutes
B) Treadmill at 70% of HR achieved on his graded exercise test (target 82 bpm) plus rate of perceived exertion (RPE) 11–13/20 on Borg, for 20–30 minutes with 5 min warm-up and cool-down
C) Cycle ergometer at maximal effort to symptom-limited endpoint, 30 minutes
D) Resistance training only at 80% of 1-RM, 3 sets of 10, no aerobic component

>>> Choose A–D.

>>> TEARDOWN

Correct: B
Clinical reasoning: Patient on beta-blocker — age-predicted max HR is invalid. Use HR achieved during his actual graded exercise test as the reference point AND validate with RPE because beta-blockade blunts HR response unpredictably across the day. Begin moderate (60–70% of test peak) and titrate.

| Opt | Correct? | If WRONG, what scenario it would be correct for |
|---|---|---|
| A | N | A patient NOT on beta-blocker who completed a symptom-limited test confirming no ischemia at high heart rates |
| B | Y | (correct) — phase II rehab patient on beta-blocker with baseline-test reference HR available |
| C | N | A symptom-limited cardiopulmonary exercise test in a research or pre-cardiac-surgery setting (not phase II therapeutic exercise) |
| D | N | A patient with severely impaired aerobic capacity (e.g., heart failure with EF <20%) where resistance training is the entry intervention before adding aerobic — and even then, 80% of 1-RM is too high; 40–60% is typical |

Engineered trap: A — tests "use HR formula reflexively even with beta-blocker on board." This is the highest-frequency cardiac-rehab error in NPTE-prep banks.

>>> CELL RULE

In any patient on a beta-blocker (or other rate-controlling agent), use the HR achieved on their own graded exercise test — NOT age-predicted maximal HR — as the reference for prescribed intensity, AND co-validate with RPE 11–13 (Borg 6–20 scale) for moderate intensity.

>>> COACHING

Single highest-yield improvement: every cardiac-rehab item that mentions beta-blocker, calcium-channel blocker, or other rate-limiting medication is asking whether you'll catch the trap. Default to "use the test-derived HR + RPE" any time a rate-controlling agent is named. The age-predicted max HR formula assumes intact sympathetic chronotropic response.
```
