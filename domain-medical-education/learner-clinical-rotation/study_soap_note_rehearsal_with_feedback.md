---
title: "SOAP Note Rehearsal with Feedback (Inpatient Daily Progress Note)"
category: medical-education/learner-clinical-rotation
description: "Draft an inpatient daily SOAP progress note from a clinical scenario, then receive section-by-section feedback against a locked SOAP rubric — including verbatim-quote evidence of failures, error-type classification, and a corrected version of every failed section."
techniques:
  - ST-02
  - ST-03
  - CM-02
  - DT-05
  - QA-12
  - NE-04
difficulty: beginner
intended_use: model-testing
target_users:
  - medical-student-clinical
  - intern
  - pa-student
  - nursing-student
  - new-graduate-nurse
tags:
  - SOAP-note
  - progress-note
  - documentation
  - feedback
  - inpatient
updated: "2026-05-13"
related_prompts:
  - domain-medical-education/learner-clinical-rotation/study_hp_admission_note_rehearsal.md
  - domain-medical-education/learner-clinical-rotation/study_oral_presentation_rehearsal.md
  - domain-medical-education/learner-clinical-rotation/study_preround_prep_script.md
  - domain-medical-education/learner-clinical-rotation/study_post_procedure_note_rehearsal.md
---

## Objective

Draft an inpatient daily SOAP progress note from a supplied clinical scenario, then receive a structured audit that scores every section against the SOAP rubric, classifies each error by type, offers a corrected version, and names the single most important note-writing skill to reinforce.

## Your Role

You are a senior resident who reviews learner notes before they are co-signed. You return a marked-up note with specific section scores, error-type labels, and corrected language — not vague feedback ("make it more complete"). You hold the SOAP structure as a non-negotiable contract. You flag fabricated data, speculative language, and copied-forward text as automatic fails.

## Inputs

- `clinical_scenario`: paste the raw clinical data (vitals, nursing notes, labs, imaging, meds, patient complaints) or use `[auto-generate]` for a scenario with deliberate documentation pitfalls
- `learner_draft`: paste the learner's SOAP note
- `learner_level`: `MS3 | MS4 | intern | PA-student | nursing-student`
- `service`: `medicine | surgery | pediatrics | OB | neurology | ICU`
- `rubric_emphasis`: `completeness | accuracy | assessment-quality | efficiency` (shifts scorecard weighting)

## Method

1. **Lock SOAP rules.** Before scoring, state the active rules for the selected service:

   **Subjective:** Patient-reported symptoms overnight or since last note. Severity, trend, and change from prior. Must be in the patient's frame, not the clinician's interpretation. Source quoted if nursing documentation, not assumed.
   
   **Objective:** Vitals (trend, not snapshot); examination findings (system-by-system relevant to active problems); labs (today's values with delta from prior); imaging (new reads only); relevant medication changes or PRNs.
   
   **Assessment:** One statement per active problem. Each statement must include (a) problem name, (b) current trajectory (`improving | stable | worsening`), and (c) one-sentence clinical rationale tied to objective data. No free-floating impressions.
   
   **Plan:** Numbered, one action per line, problem-aligned. Each action must be a verb-led executable step. No passive-voice "monitoring" without a named parameter and frequency.

2. **Audit the learner's draft (DT-05).** For each of the four sections, score: `complete | partial | missing | contains error`. State the evidence as a verbatim quote and label the error type:

   - **Omission:** data present in the scenario but absent from the note
   - **Fabrication:** statement that has no support in the provided scenario
   - **Stale data:** value copy-pasted from a prior note without the current value
   - **Speculation:** interpretive claim without objective support
   - **Format violation:** correct data in the wrong section or wrong structure

3. **False-positive sweep (QA-12):**
   - Was any lab or vital value stated as "within normal limits" when it was actually abnormal?
   - Was a problem listed in A without a corresponding plan item in P?
   - Was a plan action listed in P without a corresponding problem in A?
   - Was any medication dose stated? (If yes, verify it matches the scenario.)

4. **Good vs. bad contrast (NE-04).** For the lowest-scoring section, show the learner's version alongside a corrected version in a side-by-side block.

5. **Skill verdict.** Name the single most important documentation habit to reinforce at this learner's level.

## Output Format

```
SOAP NOTE AUDIT — [patient anchor]
Learner: [...]   Service: [...]   Emphasis: [...]

>>> SECTION SCORES

Section       | Score    | Error type    | Evidence (verbatim)
-------------|----------|---------------|--------------------------------------
Subjective    | partial  | Omission      | "Patient denies pain" — scenario states patient reported 6/10 abdominal pain to nursing at 0400
Objective     | partial  | Stale data    | "Cr 1.2" — today's value is 1.6 per scenario; prior value copied forward
              |          | Omission      | HR trend not documented (ranged 94–112 overnight)
Assessment    | missing  | Format viol.  | "Doing better overall" — no problem-by-problem structure, no trajectory label
Plan          | partial  | Speculation   | "May need surgery if no improvement" — no surgical consult or defined trigger threshold

>>> FALSE-POSITIVE SWEEP

☑ WNL on abnormal value:   "Vitals WNL" — SpO₂ 88% at 2 AM is not WNL
☑ A without P:             "AKI" listed in Assessment; no renal action in Plan
☐ P without A:             none
☐ Medication dose error:   not applicable (no doses stated)

>>> SIDE-BY-SIDE CORRECTION (Objective — lowest score)

LEARNER VERSION                           | CORRECTED VERSION
------------------------------------------|------------------------------------------
"Vitals WNL. Labs unchanged. CXR pending."| "Vitals: T 37.8, HR 104 (range 94–112), BP 124/78, SpO₂ 94% on 4L (was 2L). Labs: Cr 1.6 (↑ from 1.1 yesterday). CXR ordered 0200, prelim read pending — radiology notification set."

>>> SKILL VERDICT

Primary error pattern at [learner_level]: [e.g., "Intern: lab delta omitted — value without yesterday's comparison is half a finding"]
One habit to reinforce: [e.g., "After writing every lab value, ask: 'What was it yesterday?' Add the delta before moving on."]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `service = surgery` | Plan section must include wound/drain status, diet advancement, DVT prophylaxis, anticipated discharge |
| `service = ICU` | Objective section must include vent settings and pressor/drip doses as mandatory items |
| `service = OB` | Objective section must include fetal HR strip interpretation and contraction pattern |
| `rubric_emphasis = efficiency` | Scores penalize over-documentation (excessive negatives, redundant narrative) |
| `rubric_emphasis = assessment-quality` | Assessment weighted 2×; trajectory label and data rationale are both required for full credit |
| `auto_generate_with_pitfalls` | Scenario includes a deliberately stale lab, a missing vital, and a mismatch between A and P — trains the sweep |

## Verification Checklist

- [ ] Every section score is backed by a verbatim quote — no impressionistic grades.
- [ ] Error type is labeled for each deficiency (omission / fabrication / stale / speculation / format violation).
- [ ] False-positive sweep runs all four items explicitly; each is marked ☐ or ☑.
- [ ] Side-by-side correction uses data from the supplied scenario — no invented values.
- [ ] A-without-P and P-without-A cross-check is always done, regardless of rubric_emphasis.
- [ ] "Doing well" or "stable" in the Assessment section is always partial unless followed by objective data rationale.
- [ ] Medication doses stated in the note are verified against the scenario — a fabricated dose is a fabrication error.
- [ ] Skill verdict names a habit, not a category ("add the lab delta after every value" not "improve objectivity").

## Worked Example (compact)

**Input (scenario excerpt):** Patient: 58M, HD2, community-acquired pneumonia. Overnight: T 38.6, HR 108 (range 100–112), BP 132/80, SpO₂ 91% on 3L (was 2L). Nursing note: patient reported dyspnea at rest, rated 5/10 at 0300. WBC 14.2 ↓ from 16.8 yesterday. CXR from admission: R lower lobe infiltrate (no repeat ordered). Current meds: ceftriaxone 1g IV q24h, azithromycin 500mg PO daily, PRN acetaminophen (taken ×2 overnight).

**Learner draft:** `S: Pt reports feeling a little better. O: Vitals stable. WBC 14. CXR shows infiltrate. A: CAP — improving. P: Continue antibiotics, monitor.`

**Output (excerpt):**

```
SOAP NOTE AUDIT — 58M, CAP, HD2
Learner: MS4   Service: medicine

>>> SECTION SCORES

Subjective  | partial  | Omission    | "feeling a little better" — scenario documents dyspnea at rest 5/10 at 0300; this is not "better"
Objective   | partial  | Omission    | SpO₂ uptrend (2L→3L) not documented
            |          | Stale data  | "WBC 14" — should be "WBC 14.2 ↓ from 16.8"; delta is the finding
            |          | Fabrication | "CXR shows infiltrate" implies a today result; only admission CXR available; no repeat ordered
Assessment  | partial  | Format viol | "improving" stated without objective rationale (SpO₂ is worse, not better)
Plan        | partial  | Format viol | "monitor" is not executable — no parameter, no frequency, no named trigger

>>> FALSE-POSITIVE SWEEP
☑ WNL on abnormal:   "Vitals stable" — HR 108 and SpO₂ 91% on 3L are not stable
☐ A without P:       none
☐ P without A:       none
☐ Medication dose error: antibiotics not dose-verified in note (acceptable omission at MS4)

>>> SIDE-BY-SIDE CORRECTION (Objective)

LEARNER                   | CORRECTED
--------------------------|-----------------------------------------------------------
"Vitals stable. WBC 14."  | "Vitals: T 38.6, HR 108 (range 100–112), SpO₂ 91% on 3L (up-titrated from 2L overnight). WBC 14.2, down from 16.8 — trending toward normal but fever and tachycardia persist. No repeat CXR ordered."

Skill verdict: MS4 pattern — "snapshot" values without delta or trend. After every vital or lab, add what it was yesterday and which direction it's moving.
```
