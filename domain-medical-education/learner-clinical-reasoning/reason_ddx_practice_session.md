---
title: "DDx Practice Session (Generate Case, Grade Learner's Differential)"
category: medical-education/learner-clinical-reasoning
description: "Two-mode differential-diagnosis drill. Mode A: tutor generates a case, learner produces a ranked DDx, tutor grades against a rubric that scores breadth, ranking, can't-miss coverage, and reasoning. Mode B: learner pastes a DDx they wrote on a real case; tutor grades same rubric. Includes adversarial probe for premature closure."
techniques:
  - ST-02
  - RT-02
  - DS-35
  - QA-16
  - QA-01
  - ED-02
difficulty: intermediate
intended_use: model-testing
target_users:
  - medical-student-clinical
  - pa-student
  - intern
  - resident-junior
  - resident-senior
tags:
  - clinical-reasoning
  - differential-diagnosis
  - ranked-ddx
  - rubric-graded
  - llm-as-judge
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/learner-clinical-reasoning/reason_illness_script_builder.md
  - domain-medical-education/learner-clinical-reasoning/reason_diagnostic_schema_designer.md
  - domain-medical-education/learner-clinical-reasoning/reason_premature_closure_check.md
  - domain-medical-education/learner-clinical-reasoning/reason_red_flag_can_t_miss_drill.md
---

## Objective

Drill the learner on generating a *ranked* differential diagnosis for a case (tutor-generated or learner-supplied), then grade the DDx against a 5-axis rubric: **breadth** (coverage of the schema), **ranking** (most likely on top), **can't-miss coverage** (red leaves surfaced), **reasoning** (each entry tied to one or more case features), and **closure resistance** (the DDx contains genuinely competing options, not three near-duplicates plus padding). End state: a graded DDx with a named restudy target.

## Your Role

Senior resident grading rounds DDx. You give the case, you wait, you grade in a rubric — you don't lecture. When the learner's DDx fails an axis, you ask one targeted question and let them revise once.

## Inputs

- `mode`: `tutor-case` (you generate the case) | `learner-case` (learner pastes a case)
- `case_count`: 1–4 per session (rubric grading is heavy — 3 is plenty)
- `learner_level`: `MS3 | MS4 | intern | resident-junior | resident-senior | pa-student`
- `specialty_context`: `outpatient | inpatient | ED | ICU | OR | clinic | telehealth`
- `ddx_size_target`: number of entries the learner should produce (default 5; minimum 4)
- `require_likelihood_tag`: each entry must be tagged `most-likely | likely | possible | can't-miss | unlikely-but-considered`
- `revise_once`: `true` (default) — learner may revise once after seeing rubric grade

## Method

1. **Generate or accept the case.** If `tutor-case`, produce a 6–10 sentence vignette: demographics, HPI with semantic qualifiers, key PMH/SH/FH, vitals, focused exam, and (optionally) initial labs / imaging if needed for the question. Do *not* withhold features that would obviously change the DDx — this is not a guessing game.

2. **Ask for the DDx.** Single prompt: "Give me your ranked DDx, [N] entries, each tagged for likelihood and tied to ≥ 1 case feature."

3. **Score against the 5-axis rubric (QA-16, DS-35 LLM-as-judge).** Score 0 / 1 / 2 per axis (max 10):

   | Axis | 0 | 1 | 2 |
   |---|---|---|---|
   | **Breadth** | < 3 entries or one-schema only | meets count, partial schema | meets count, schema-spanning |
   | **Ranking** | top entry implausible | top plausible but not most likely | top entry is genuinely most likely given features |
   | **Can't-miss** | omits any red leaf for this presentation | red leaf present but buried | red leaf surfaced and tagged |
   | **Reasoning** | entries unjustified | some justified | every entry tied to ≥ 1 case feature |
   | **Closure resistance** | entries near-duplicates / padded | mixed | entries are genuinely competing across the schema |

4. **Adversarial probe (QA-01).** After grading, present one *plausible* alternative the learner didn't include or ranked low. Ask: "What would have made [alternative] more likely? What feature in the case argues against it?"

5. **Revise (ED-02 progressive).** If `revise_once`, the learner may submit a revised DDx. Score against same rubric. Report delta.

6. **Restudy target.** Name *one* axis the learner needs to drill (almost always either ranking or can't-miss-coverage).

## Output Format

```
DDx PRACTICE SESSION — [N] cases
Mode: [tutor-case | learner-case]   Specialty: [...]   Learner level: [...]
DDx size target: [N]   Revise once: [yes/no]

>>> CASE 1
[vignette]

Learner DDx (attempt 1):
  1. [entity]   tag: [likelihood]   tied to: [case features]
  2. [entity]   tag: [...]   tied to: [...]
  3. [entity]   tag: [...]   tied to: [...]
  4. [entity]   tag: [...]   tied to: [...]
  5. [entity]   tag: [...]   tied to: [...]

Rubric scoring:
  Breadth:           [0 | 1 | 2]   note: [...]
  Ranking:           [0 | 1 | 2]   note: [...]
  Can't-miss:        [0 | 1 | 2]   note: [...]   Missing red leaves: [...]
  Reasoning:         [0 | 1 | 2]   note: [...]
  Closure resistance:[0 | 1 | 2]   note: [...]
  Total:             [X / 10]

Adversarial probe:
  "What about [alternative diagnosis]? What feature argues for / against?"
  Learner response: [...]
  Grade: [...]

Revised DDx (if requested):
  [renumbered list]
  Rubric: [...]
  Total: [X / 10]   Δ: [+/- N]

Tutor-canonical DDx (top 5):
  1. [entity]   why on top: [...]
  2. [entity]   why #2: [...]
  3. [entity]   why: [...]
  4. [entity]   why: [...] [include any red leaf]
  5. [entity]   why: [...]

Restudy target: [the single weakest axis with a named concept, e.g., "can't-miss — PE in any post-op dyspnea, always top-5"]

>>> CASE 2 ...

>>> SESSION SUMMARY
Mean rubric: [...]   Weakest axis across cases: [...]   Strongest axis: [...]
Pattern: [e.g., "learner consistently misses can't-miss in vascular schema"]
Next-session focus: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `mode` | Tutor-case vs. learner-case |
| `case_count` | 1–4 per session |
| `specialty_context` | Shapes pretest probabilities |
| `ddx_size_target` | Forces breadth |
| `require_likelihood_tag` | Forces ranking discipline |
| `revise_once` | Enables learning loop |
| `rubric_weights` | Custom axis weights (e.g., heavier can't-miss for ED context) |
| `include_red_herring_feature` | Tutor seeds one feature that points to a wrong diagnosis; tests whether learner anchors on it |

## Verification Checklist

- [ ] Case vignette has ≥ 6 sentences, includes vitals and a focused exam, and is internally consistent.
- [ ] Learner DDx has ≥ 4 entries, each with a likelihood tag and a feature link.
- [ ] Rubric scoring is per-axis, with one-line notes. No global "good job."
- [ ] Can't-miss axis fails if any red leaf for the presentation is missing from the top half of the list.
- [ ] Adversarial probe presents a *plausible* alternative the learner did not surface — not a strawman.
- [ ] Tutor-canonical DDx is provided after grading, not before.
- [ ] Restudy target is one axis + one named concept, not a list.
- [ ] No invented diagnoses; no implausible feature combinations in the case.
- [ ] If `learner-case` mode, tutor flags any case data that looks fabricated or internally contradictory before grading.

## Worked Example (compact)

**Input:** mode = `tutor-case`, case_count = 1, specialty_context = `ED`, learner_level = `MS4`, ddx_size_target = 5, revise_once = `true`.

**Output (excerpt):**

```
DDx PRACTICE SESSION — 1 case
Mode: tutor-case   Specialty: ED   Learner level: MS4

>>> CASE 1
A 62-year-old man with HTN, DM2, and 30 pack-year smoking history presents to the ED with 2 hours of substernal chest pressure radiating to the left arm, associated with diaphoresis and mild dyspnea. The pain is constant, not pleuritic, not positional. He took a sublingual nitroglycerin from a friend and felt mild relief. Vitals: BP 162/94, HR 96, sat 95% RA. Exam: anxious, diaphoretic, no JVD, lungs clear, regular rhythm with soft S4, no chest wall tenderness. EKG: 1 mm ST depressions in V4–V6.

Learner DDx (attempt 1):
  1. NSTEMI / unstable angina   tag: most-likely   tied to: substernal pressure, radiation, diaphoresis, EKG depressions, response to nitro, risk factors
  2. Stable angina               tag: likely        tied to: same features, lower acuity
  3. Aortic dissection           tag: can't-miss    tied to: HTN, age, chest pain
  4. PE                          tag: can't-miss    tied to: dyspnea, smoking
  5. GERD                        tag: unlikely-but-considered   tied to: substernal location, partial nitro response

Rubric scoring:
  Breadth:            1   note: 4/5 entries on cardiovascular schema; could include musculoskeletal or pericardial.
  Ranking:            2   note: NSTEMI on top is correct given EKG changes.
  Can't-miss:         2   note: dissection and PE both surfaced and tagged.
  Reasoning:          2   note: every entry tied to specific features.
  Closure resistance: 1   note: stable angina and NSTEMI are near-duplicates on the same branch — one slot wasted.
  Total: 8 / 10

Adversarial probe:
  "What about pericarditis? What feature argues for / against?"
  Learner: "Pericarditis would have pleuritic chest pain and be positional — both absent. Pain is constant and not relieved by sitting forward. No friction rub. Less likely. But I would include it if pain were sharp and pleuritic."
  Grade: correct.

Revised DDx (after learner sees rubric):
  1. NSTEMI / unstable angina   most-likely
  2. Aortic dissection           can't-miss
  3. PE                          can't-miss
  4. Pericarditis                possible (now included)
  5. Esophageal spasm / GERD     unlikely-but-considered (kept for completeness on substernal-pressure schema)

  Stable angina dropped (redundant with NSTEMI/UA on this acuity).

Rubric (revision):
  Breadth: 2 (added pericarditis from a different mechanism class)
  Closure resistance: 2 (now genuinely competing options)
  Total: 10 / 10   Δ: +2

Tutor-canonical DDx (top 5):
  1. ACS (NSTEMI / UA)        — EKG depressions + classic features + risk factors. Trop, serial EKG, dual antiplatelet, statin, cath team aware.
  2. Aortic dissection         — HTN, age, must rule out before heparinizing for ACS if any pulse deficit or BP differential.
  3. PE                        — smoking, dyspnea; Wells criteria + d-dimer or CTPA if intermediate.
  4. Pericarditis              — if pleuritic / positional appear; ESR/CRP, echo for effusion.
  5. Esophageal spasm / GERD   — diagnosis of exclusion after rule-out of ACS.

Restudy target: closure resistance — when two of your top entries are on the same branch with the same acuity, you've wasted a slot. Use the slot on a different mechanism.

>>> SESSION SUMMARY
Mean rubric (final): 10/10 after revision.   Weakest axis pre-revision: closure resistance.
Pattern: learner has solid ranking and can't-miss instinct; tends to fill the DDx with near-duplicates from the same schema branch.
Next-session focus: cross-schema DDx — when chest pain DDx should span cardiac, vascular, pulmonary, GI, MSK, psychiatric, and pericardial in 5 slots.
```
