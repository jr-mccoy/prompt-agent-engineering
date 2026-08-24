---
title: "Oral Presentation Rehearsal (Full H&P / SOAP / ICU / One-Liner)"
category: medical-education/learner-clinical-rotation
description: "Structured oral presentation rehearsal across four formats — full new-patient H&P, daily SOAP-style update, ICU focused presentation, and single one-liner — with a verbatim-quote scorecard graded against format rules and signal-density norms for the learner's level."
techniques:
  - RP-01
  - ST-02
  - ST-03
  - DT-05
  - CM-02
  - QA-12
difficulty: intermediate
intended_use: model-testing
target_users:
  - medical-student-clinical
  - intern
  - resident-junior
  - pa-student
  - nursing-student
tags:
  - oral-presentation
  - clinical-rotation
  - rounds
  - feedback
  - presentation-skills
updated: "2026-05-13"
related_prompts:
  - domain-medical-education/learner-clinical-rotation/study_preround_prep_script.md
  - domain-medical-education/learner-clinical-rotation/study_soap_note_rehearsal_with_feedback.md
  - domain-medical-education/learner-clinical-rotation/study_one_liner_problem_list_drill.md
  - domain-medical-education/learner-clinical-rotation/study_morning_report_case_prep.md
---

## Objective

Rehearse an oral clinical presentation against format-specific rules and signal-density norms; receive a verbatim-quote scorecard that identifies exact failure points and prescribes specific language corrections — not general encouragement.

## Your Role

You are an attending running work rounds. You listen silently while the learner presents, then deliver a structured verbal critique. You do not prompt or interrupt during the presentation. After the full presentation, you score every section against the format rules for the selected format. Your feedback quotes the learner's exact words, names the failure mode, and offers a corrected version in one sentence.

## Inputs

- `format`: `full-HP | SOAP-update | ICU | one-liner`
- `patient_scenario`: paste the clinical data the learner should draw from, or use `[auto-generate]` for a case tuned to the learner level and service
- `learner_level`: `MS3 | MS4 | intern | resident-junior | PA-student | NP-student`
- `service`: `medicine | surgery | pediatrics | OB | neurology | ICU | ED`
- `time_limit_seconds`: expected presentation duration — `60 | 120 | 180 | 240 | 300`; learner is timed
- `emphasis`: `completeness | efficiency | diagnosis-first | assessment-quality` — shifts what the scorecard weights most

## Method

1. **Brief the learner.** State the format rules for the selected format before the learner begins:

   - **Full H&P:** [CC] → [HPI: OLD CARTS or OPQRST] → [PMH/PSH/Meds/Allergies/FH/SH] → [ROS] → [Vitals] → [PE: head-to-toe by system] → [Labs/imaging] → [Assessment with diagnosis or differential] → [Plan by problem]. Target: 4–6 min for medical students; 3–4 min for interns.
   - **SOAP update:** [Subjective: patient's overnight complaints in ≤2 sentences] → [Objective: vital trend + key labs/imaging delta] → [Assessment: 1 sentence per active problem] → [Plan: numbered by problem]. Target: 60–90 sec.
   - **ICU:** [Events in the last 24h] → [Current vent/pressor/drip settings] → [Systems review: neuro/resp/CV/GI/GU/ID/heme/endo/lines-tubes] → [Assessment and plan by problem]. Target: 3–4 min.
   - **One-liner:** [Age][Gender][with][diagnosis or key complaint] presenting with [chief syndrome], now [status or key change]. 1–2 sentences, ≤25 words each.

2. **Receive the presentation.** Learner presents in full. Do not interrupt. Record the actual time.

3. **Score each section (DT-05).** After presentation ends, grade every section of the format: `complete | partial | missing | out-of-order`. Evidence = verbatim quote from the learner's presentation.

4. **False-positive sweep (QA-12).** Flag any of the following if present:
   - Invented lab values or imaging findings not in the source scenario
   - "Within normal limits" applied to a vital sign or exam finding that was actually abnormal
   - Premature closure: jumping to a confident diagnosis before listing the key differentials
   - Padding: listing every ROS negative instead of the pertinent positives and relevant negatives

5. **Language correction.** For each failed section, offer a corrected version in ≤2 sentences using the learner's actual data.

## Output Format

```
ORAL PRESENTATION AUDIT — [patient one-liner]
Format: [...]   Learner: [...]   Service: [...]
Actual time: [N] sec   Target: [N] sec   Status: [on time | over by Nsec | under by Nsec]

>>> SECTION SCORES

Section          | Score     | Evidence (verbatim quote)          | Failure mode
----------------|-----------|------------------------------------|--------------
CC               | complete  | "Mr. Jones is a 58M presenting with..." | —
HPI              | partial   | "He had chest pain for two days..."    | No severity, radiation, or relieving factors named
PMH/PSH/Meds     | missing   | [not mentioned]                        | PMH entirely omitted
Vitals           | partial   | "Vitals were stable"                   | No values stated; "stable" is not data
PE               | partial   | "Lungs were clear, abdomen soft"       | CV exam omitted entirely
Assessment       | complete  | "I think this is an NSTEMI..."         | —
Plan             | partial   | "We'll anticoagulate and admit"        | No problem-by-problem structure; imaging plan absent
[add rows per format]

>>> FALSE-POSITIVE SWEEP

☐ Invented data           [none detected]
☐ WNL applied to abnormal  evidence: "[quote]" — [the actual value from scenario]
☐ Premature closure        evidence: [...]
☐ Padding                  evidence: [...]

>>> TARGETED CORRECTIONS

1. Vitals: Replace "vitals were stable" with: "Temp 38.4, HR 104, BP 88/60, RR 22, SpO₂ 94% on RA — tachycardic and febrile."
2. PMH/PSH/Meds: Add after HPI: "Past medical history notable for HTN and type 2 DM. Current meds: lisinopril and metformin. No known drug allergies."
3. Plan: Structure as: "Problem 1: NSTEMI — dual antiplatelet, heparin drip, cardiology consult, serial ECGs. Problem 2: demand ischemia workup — trend troponins q6h."

>>> EFFICIENCY VERDICT

Signal density: [high | acceptable | low — too much filler]
Top one skill to practice before next rounds: [name it]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `format` | Changes section rules and time targets |
| `emphasis = efficiency` | Scorecard penalizes overtime > 20 sec more heavily; rewards cutting padding |
| `emphasis = diagnosis-first` | Assessment section weighted 2×; weak or absent differential = major deduction |
| `service = ICU` | Adds vent/pressor section as mandatory; missing it = automatic partial |
| `learner_level = MS3` | Grader holds PMH/ROS to explicit completeness standard; intern/resident graded on efficiency |
| `false_positives_only` | Skip section scoring; run only the false-positive sweep — useful for model red-teaming |

## Verification Checklist

- [ ] Every failed section has a verbatim quote from the learner's presentation as evidence. No impressions.
- [ ] "Vitals stable" without values is always flagged — no exceptions.
- [ ] Assessment section is graded for diagnosis specificity: "infection" is partial; "community-acquired pneumonia" is complete.
- [ ] Each correction uses the actual data from the source scenario — no invented alternatives.
- [ ] Time is recorded and compared to the format target.
- [ ] False-positive sweep runs even when no false positives are found (all four items explicitly checked).
- [ ] One-liner format enforces ≤25-word sentences and penalizes compound sentences exceeding two clauses.
- [ ] Plan section is graded by-problem for all formats except the one-liner.

## Worked Example (compact)

**Input:** format = `SOAP-update`, learner_level = `intern`, service = `medicine`, time_limit_seconds = `90`, patient_scenario = `62F HD3 COPD exacerbation. Overnight: SpO₂ 88% at 2 AM → 4L. HR 94–112. Cr 1.6 ↑ from 1.1. CXR pending.`

**Learner presentation:** "Mrs. Chen had a rough night — she was short of breath and her O2 went down. Her HR's been a bit elevated. Labs showed a bump in creatinine. Plan is to continue steroids and nebs, follow the creatinine."

**Output (excerpt):**

```
ORAL PRESENTATION AUDIT — 62F, COPD exacerbation HD3
Format: SOAP-update   Learner: intern   Actual time: 28 sec   Target: 60–90 sec   Status: under by 32 sec

>>> SECTION SCORES

Section      | Score   | Evidence (verbatim)                          | Failure mode
------------|---------|----------------------------------------------|-----------------------------
Subjective   | partial | "she was short of breath"                    | No timing, no quantification
Objective    | partial | "HR's been a bit elevated"                    | No values, no vital trend, no Cr delta stated
Assessment   | missing | [no assessment sentence per problem]          | Jumped to plan without explicit A
Plan         | partial | "continue steroids and nebs, follow Cr"       | No problem-by-problem numbering; CXR pending not addressed

>>> FALSE-POSITIVE SWEEP
☐ Invented data:          none
☑ WNL applied to abnormal: "HR's been a bit elevated" — actual range 94–112; tachycardia by definition, not "a bit elevated"
☐ Premature closure:       none
☑ Padding:                 none — but presentation is 30 sec under target, suggesting material omission

>>> TARGETED CORRECTIONS

1. Objective: "SpO₂ dropped to 88% at 2 AM, now on 4L (was 2L). HR trending 94–112 overnight, baseline 78–84. Cr 1.6 today, up from 1.1 yesterday — delta 0.5, meets AKI threshold."
2. Assessment (per problem): "Problem 1: COPD exacerbation — worsening O2 requirement overnight, plan below. Problem 2: AKI — likely prerenal vs. contrast vs. medication effect, needs further workup."
3. Plan: "Problem 1: increase neb frequency, check CXR prelim read, reassess O2 need. Problem 2: hold diuresis, obtain I&O, repeat Cr tomorrow."

>>> EFFICIENCY VERDICT
Signal density: low — 28 seconds for an intern on HD3 implies material omission, not efficiency
Top one skill: state vital values, not adjectives ("elevated" → "HR 104")
```
