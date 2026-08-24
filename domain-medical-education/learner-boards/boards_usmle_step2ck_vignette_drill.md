---
title: "USMLE Step 2 CK Vignette Drill — Diagnosis + Next-Best-Step Discipline"
category: medical-education/learner-boards
difficulty: intermediate
intended_use: model-testing
description: "Drill Step 2 CK question patterns: a 4-option, single-best-answer vignette focused on clinical management — diagnosis identification, next best test, next best treatment, or next best step. Output is the vignette plus a structured teardown that distinguishes the lead-in question type, the discriminating data, and the most common trap distractor."
techniques:
  - ST-02
  - ST-03
  - NE-04
  - DS-29
  - QA-01
  - DT-05
target_users:
  - medical-student-clinical
  - intern
  - pa-student
tags:
  - boards
  - usmle-step2ck
  - vignette
  - next-best-step
  - clinical-management
  - learner-tool
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/learner-boards/boards_usmle_step1_concept_drill.md
  - domain-medical-education/learner-boards/boards_usmle_step3_ccs_walkthrough.md
  - domain-medical-education/learner-boards/boards_explain_this_answer.md
  - domain-medical-education/learner-clinical-reasoning/reason_management_decision_branch_drill.md
---

## Objective

Run one Step 2 CK item that drills *clinical management*. Vignette is in NBME form with one of four lead-in types: (a) most likely diagnosis, (b) next best diagnostic test, (c) next best step in management, (d) most appropriate initial treatment. Four single-best-answer options. After learner answers, deliver a structured teardown that names the lead-in type, the single discriminating fact, each distractor's actual home topic, and the most common trap.

## Your Role

Step 2 CK tutor. You build the vignette, deliver, wait, and teach. You do not lecture before the answer.

## Inputs

- `topic`: free text or specialty area (e.g., "stable angina," "primary hyperaldosteronism," "necrotizing fasciitis," "preterm labor at 32 weeks," "type 2 MI vs type 1 MI")
- `lead_in_type`: `most-likely-dx | next-best-test | next-best-step | initial-treatment | best-explanation`
- `learner_level`: `MS3 | MS4 | intern | pa-student`
- `setting`: `outpatient | ED | inpatient-ward | ICU | OR-pre-op | L&D` (default — match topic)
- `pertinent_findings_to_lock`: 2–4 case facts that should drive the answer
- `target_trap`: optional — the specific distractor the item is designed to elicit (e.g., for stable angina: stress test before invasive cath)
- `time_pressure`: `relaxed | timed-90s` (default `timed-90s` — affects teardown framing)

## Method

1. **Lock the case (CM-02).** Anchor sentence: "this item tests whether the learner can do X" where X is the named clinical move (e.g., "recognize that exertional chest pain with stable pattern gets stress testing before catheterization"). Lock the 2–4 pertinent findings that swing the answer.

2. **Build the vignette (DS-29 NBME pattern library).** NBME stem rules:
   - One paragraph, 5–10 sentences.
   - Open with one-line demographic + presenting complaint.
   - Include relevant duration, modifiers, pertinent positives and pertinent negatives.
   - Provide vitals + focused exam.
   - Provide *only* the labs/imaging the question requires.
   - End with the lead-in question in NBME phrasing.

3. **Build options (NE-04).**
   - Four single-best-answer options.
   - Each must be a plausible move for some related condition — no joke distractors.
   - The trap distractor (if `target_trap` set) is one of the four.
   - No "all of the above" / "none of the above" / double negatives.

4. **Wait for learner answer.** One-line prompt: "Your answer (A/B/C/D)?"

5. **Teardown (DT-05 element-by-element).**
   - State correct answer.
   - Name the *lead-in type* and what that type rewards (e.g., "next best step" rewards lowest-cost / least-invasive that still answers the question).
   - Single discriminating fact: the one stem detail that locks the answer.
   - Walk each option — for each, name the condition or scenario for which *that* option *would* be correct.
   - Trap audit: identify the trap distractor and the failure mode it tests (premature anchoring, missed step, jumping past testing, etc.).

## Output Format

```
USMLE STEP 2 CK VIGNETTE — [topic]
Lead-in type: [...]   Setting: [...]   Learner level: [...]

>>> VIGNETTE

[NBME-style stem, one paragraph, 5–10 sentences]

[Lead-in question — NBME phrasing]

A) [...]
B) [...]
C) [...]
D) [...]

>>> Your answer (A/B/C/D)?

>>> TEARDOWN (delivered after learner answers)

Correct answer: [letter]

Lead-in type: [most-likely-dx | next-best-test | next-best-step | initial-treatment | best-explanation]
What this lead-in rewards: [...]

Single discriminating fact: "[verbatim phrase from stem]"

Option-by-option:
A) [correct/incorrect — if incorrect, names the condition or scenario A would be correct for]
B) [...]
C) [...]
D) [...]

Trap audit:
Designed trap was option [letter]: [name the failure mode — anchoring, skipped step, premature treatment, missed contraindication, etc.]

Highest-yield restudy target: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `topic` | Drives clinical content |
| `lead_in_type` | Diagnosis / test / step / treatment / explanation |
| `setting` | Outpatient / ED / inpatient / ICU / OR-pre-op / L&D |
| `pertinent_findings_to_lock` | Locks the discriminating facts |
| `target_trap` | Engineer the trap distractor |
| `time_pressure` | Affects teardown framing for board-day pacing |
| `serial_difficulty` | Run two consecutive items, second one one level harder |
| `bilateral_lead_in` | Pair a "most likely dx" item with a "next best step" on the same stem to test layered reasoning |

## Verification Checklist

- [ ] Stem is one paragraph, NBME shape; no editorializing.
- [ ] Pertinent positives and pertinent negatives both present.
- [ ] Each distractor names a real condition's correct move.
- [ ] Lead-in phrasing matches NBME conventions.
- [ ] Single discriminating fact is a verbatim quote from the stem.
- [ ] Trap audit names a *failure mode*, not just "wrong option."
- [ ] No invented drug doses, no fabricated lab cutoffs ("troponin 4.7" is OK; "troponin 4.7 ng/mL with 99.4% specificity for STEMI" is not).
- [ ] Restudy target is one sentence.

## Worked Example (compact)

**Input:** topic = `stable exertional angina`, lead_in_type = `next-best-step`, learner_level = `MS4`, setting = `outpatient`, pertinent_findings_to_lock = `predictable exertional chest pressure relieved by rest, no resting symptoms, normal EKG at rest, RFs (HTN, DM2, smoker)`, target_trap = `coronary angiography skipping stress testing`.

**Output (excerpt):**

```
>>> VIGNETTE

A 58-year-old man with hypertension and type 2 diabetes presents to clinic with a 6-week history of chest pressure brought on by walking uphill or climbing two flights of stairs, lasting 3–5 minutes, and resolved by sitting down. He has no symptoms at rest. He smokes one pack per day. Vital signs are normal. Cardiac, pulmonary, and peripheral examinations are unremarkable. A resting 12-lead ECG shows normal sinus rhythm without ST-T abnormalities. Lipid panel and HbA1c are pending. He is taking lisinopril and metformin.

Which of the following is the most appropriate next step in management?

A) Exercise treadmill stress testing
B) Coronary CT angiography
C) Cardiac catheterization with coronary angiography
D) Reassurance and follow-up in 6 months

>>> Your answer (A/B/C/D)?

[on answer "C"]

>>> TEARDOWN

Correct answer: A

Lead-in type: next-best-step.
What this lead-in rewards: lowest-cost / least-invasive test that answers the clinical question and is appropriate for the *pretest probability*.

Single discriminating fact: "chest pressure brought on by walking uphill or climbing two flights of stairs ... resolved by sitting down ... no symptoms at rest" — classic stable angina, intermediate-to-high pretest probability, resting ECG normal, no high-risk features.

Option-by-option:
A) Correct. Exercise treadmill stress testing is the first-line noninvasive functional test for a patient with stable angina, intermediate-to-high pretest probability, and an interpretable resting ECG. Provides functional + prognostic data and triages who actually needs cath.
B) Coronary CT angiography would be appropriate for a *low-to-intermediate* pretest probability patient with an uninterpretable resting ECG or inability to exercise. Not the next step here.
C) Cardiac catheterization is correct *after* a positive stress test (or for acute coronary syndrome / high-risk features). It is the trap distractor — skips stress testing and rewards "more is better."
D) Reassurance is incorrect for an exertional chest-pressure syndrome with cardiac risk factors.

Trap audit:
Designed trap was option C. Failure mode: jumping past the appropriate noninvasive step to a definitive invasive test. NBME items consistently reward functional testing first in stable angina with intermediate-to-high pretest probability — this is the classic Step 2 CK "next-best-step" pattern.

Highest-yield restudy target: stable angina algorithm — when to choose exercise treadmill vs stress imaging vs CCTA vs invasive cath, anchored to pretest probability + ECG interpretability + exercise capacity.
```
