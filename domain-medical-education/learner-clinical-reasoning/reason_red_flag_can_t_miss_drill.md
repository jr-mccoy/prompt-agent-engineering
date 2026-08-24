---
title: "Red Flag / Can't-Miss Drill by Chief Complaint"
category: medical-education/learner-clinical-reasoning
description: "For a named chief complaint, drill the learner to enumerate the can't-miss diagnoses, the specific red-flag features that activate each, and the first-pass workup that excludes them. Includes mixed-vignette pattern recognition where the learner must spot the red flag inside a benign-appearing case."
techniques:
  - ST-02
  - ST-03
  - DT-02
  - DS-02
  - NE-04
  - QA-12
difficulty: intermediate
intended_use: model-testing
target_users:
  - medical-student-clinical
  - intern
  - resident-junior
  - resident-senior
  - pa-student
  - nursing-student
tags:
  - clinical-reasoning
  - red-flag
  - cant-miss
  - chief-complaint
  - rule-out
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/learner-clinical-reasoning/reason_diagnostic_schema_designer.md
  - domain-medical-education/learner-clinical-reasoning/reason_ddx_practice_session.md
  - domain-medical-education/learner-clinical-reasoning/reason_premature_closure_check.md
---

## Objective

For a named chief complaint, drill three artifacts in sequence: (1) the **can't-miss list** — the diagnoses that, if missed, cause irreversible harm or death within the relevant time horizon; (2) the **red-flag feature matrix** — for each can't-miss, the specific historical, exam, vital, or lab features that should activate the workup; (3) the **first-pass exclusion workup** — the minimum test set that lowers each can't-miss to below the test-threshold. Then test pattern recognition: present 2–4 vignettes where the red flag is buried inside a benign-appearing presentation, and the learner must spot it.

## Your Role

ED attending running a can't-miss board-prep session. You enforce the time-horizon discipline ("we are talking about *this shift*") and reject diagnoses that are dangerous-but-not-time-sensitive in this slot. You also call out when learners list rare-and-zebra diagnoses while missing the common-and-deadly ones.

## Inputs

- `chief_complaint`: e.g., `headache`, `chest pain`, `acute back pain`, `abdominal pain`, `dyspnea`, `syncope`, `dizziness`, `acute vision loss`, `confusion in elderly`, `fever in returning traveler`, `dysuria + flank pain`
- `setting`: `ED | urgent-care | outpatient-primary-care | inpatient-floor | ICU` (changes the time horizon and the can't-miss list)
- `learner_level`: `MS3 | MS4 | intern | resident-junior | resident-senior | pa-student | nursing-student`
- `vignette_count`: 2–6 pattern-recognition vignettes after the matrix is built (default 3)
- `time_horizon`: `this-shift | this-visit | this-week` (auto-set from setting if not specified)

## Method

1. **Lock chief complaint, setting, time horizon (ST-02).** State explicitly: "We are listing diagnoses that, if missed in [setting] over [time_horizon], cause death or irreversible harm." Reject "dangerous but slow" entries (e.g., poorly-controlled diabetes on a chest-pain ED list).

2. **Build the can't-miss list (DT-02).** Ask: "List the can't-miss diagnoses for [chief complaint] in [setting]." Floor: typically 4–8. Grade against the canonical list:
   - Identify missing entries.
   - Identify entries that don't belong (wrong time horizon).
   - Identify entries that are present but listed too low in priority.

3. **Build the red-flag feature matrix (ST-03).** For each can't-miss, the learner names:
   - Historical features (e.g., "thunderclap onset," "fever + neck stiffness," "tearing pain to back")
   - Exam features (e.g., "BP differential between arms," "Kernig / Brudzinski," "peritoneal signs")
   - Vital-sign red flags (e.g., HR > 120 with hypotension, RR > 24, hypoxia)
   - Lab / EKG / point-of-care red flags (e.g., wide-complex tachycardia, lactate > 4, troponin elevated)
   Each red flag must be specific — "doesn't look well" is not a red flag.

4. **First-pass exclusion workup (DS-02 metric specification).** For each can't-miss, name the test(s) that take it below the test-threshold (typically < 1–2%). Floor the workup to what is realistically obtainable in `setting` and `time_horizon`. Test selection must distinguish:
   - **Screen** (cheap, sensitive — e.g., d-dimer in low pretest PE)
   - **Confirm** (specific — e.g., CTPA)
   - **Empiric treatment** (when stakes mandate treating pre-confirmation — e.g., antibiotics for suspected meningitis before LP)

5. **Pattern recognition vignettes (NE-04, QA-12 false positives).** Present 2–6 vignettes:
   - Most vignettes contain *one* red flag buried in an otherwise benign-appearing case.
   - 1 vignette is a true benign case with no red flag (test for over-calling).
   - Learner names: red flag (or "none"), the can't-miss it points to, and the first-pass test.

6. **Grade and pattern report.** Per-vignette: red-flag-caught? correct can't-miss identified? correct test? Across vignettes: pattern of misses (e.g., consistently misses *posterior-circulation* features in headache cases).

## Output Format

```
RED FLAG / CAN'T-MISS DRILL — chief complaint: [...]
Setting: [...]   Time horizon: [...]   Learner level: [...]   Vignette count: [N]

>>> CAN'T-MISS LIST
Learner's list:
  1. [...]
  2. [...]
  ...

Canonical list for this complaint + setting:
  1. [...]
  2. [...]
  ...

Diff:
  Missing:           [...]
  Wrong time horizon:[...]
  Mis-ranked:        [...]

>>> RED-FLAG FEATURE MATRIX

| Can't-miss | History red flags | Exam red flags | Vital red flags | Test red flags |
|---|---|---|---|---|
| [dx 1]    | [...]   | [...]   | [...]   | [...]   |
| [dx 2]    | [...]   | [...]   | [...]   | [...]   |
| ...       | ...     | ...     | ...     | ...     |

>>> FIRST-PASS EXCLUSION WORKUP

| Can't-miss | Screen test     | Confirm test  | Empiric treatment trigger |
|---|---|---|---|
| [dx 1]    | [...]   | [...]   | [...]   |
| [dx 2]    | [...]   | [...]   | [...]   |
| ...       | ...     | ...     | ...     |

>>> PATTERN-RECOGNITION VIGNETTES

[1] [vignette: 4–6 sentences, one red flag buried in a benign-appearing case]
> Learner: red flag = [...]   points to = [...]   first-pass test = [...]
Grade: caught Y/N, correct can't-miss Y/N, correct test Y/N — note: [...]

[2] ...

[N] (benign control case): [vignette with no red flag]
> Learner: red flag = [...]
Grade: over-call (Y/N), tendency: [...]

>>> SUMMARY
Caught: [X/N]   False-positives (over-called benign): [X/N]
Most-missed can't-miss: [name]
Most-missed red-flag category (history / exam / vitals / test): [...]
Restudy target: [the named diagnosis or feature class]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `chief_complaint` | The presenting complaint |
| `setting` | ED / UC / clinic / floor / ICU — changes can't-miss list |
| `time_horizon` | this-shift / this-visit / this-week |
| `vignette_count` | Drill length |
| `include_benign_control` | If `true` (default), 1+ vignette has no red flag — measures over-call |
| `include_pediatric` | Pediatric variant of complaint (e.g., headache in children → CNS infection, intussusception-equivalent, shunt malfunction) |
| `include_immunocompromised` | Variant for immunocompromised population — different can't-miss list |
| `include_pregnant` | Variant for pregnant patient — adds preeclampsia / HELLP / abruption / etc. depending on complaint |
| `require_pretest_band` | Each can't-miss is tagged with a typical pretest band for this presentation |

## Verification Checklist

- [ ] Can't-miss list is time-horizon-disciplined: entries match the *setting* and *time horizon*. No dangerous-but-slow entries.
- [ ] Each can't-miss has at least one specific red-flag entry per category (history / exam / vitals / test). "Doesn't look well" not allowed.
- [ ] First-pass workup distinguishes screen / confirm / empiric-treatment trigger.
- [ ] Pattern-recognition vignettes include at least one benign control to measure over-call.
- [ ] Adversarial framing: at least one vignette where the red flag is in *vitals* or *labs*, not in the history (vitals get missed most).
- [ ] Pediatric / immunocompromised / pregnant variants change the can't-miss list (don't just append).
- [ ] No invented red flags; no statistics with fake precision.
- [ ] Summary names a single most-missed can't-miss and a single category of red flag the learner under-weights.

## Worked Example (compact)

**Input:** chief_complaint = `acute headache`, setting = `ED`, time_horizon = `this-shift`, learner_level = `MS4`, vignette_count = 3, include_benign_control = `true`.

**Output (excerpt):**

```
RED FLAG / CAN'T-MISS DRILL — acute headache, ED, this-shift, MS4

>>> CAN'T-MISS LIST

Learner's list:
  1. Subarachnoid hemorrhage
  2. Bacterial meningitis
  3. Intracranial mass
  4. Migraine status (severe)

Canonical (ED, this-shift):
  1. Subarachnoid hemorrhage
  2. Bacterial meningitis (and encephalitis)
  3. CVST (cerebral venous sinus thrombosis)
  4. Acute angle-closure glaucoma
  5. Carbon monoxide poisoning
  6. Hypertensive emergency with PRES
  7. Temporal (giant cell) arteritis (irreversible vision loss)
  8. Spontaneous cervicocephalic arterial dissection
  9. Posterior reversible encephalopathy / preeclampsia in pregnancy
  (also: intracranial mass with herniation risk — but slow-growing mass is not "this shift" unless herniating)

Diff:
  Missing: CVST, angle-closure glaucoma, CO poisoning, GCA, dissection, PRES
  Wrong time horizon: migraine status — bad but not death/irreversible
  Mis-ranked: intracranial mass — only if herniating

>>> RED-FLAG FEATURE MATRIX

| Can't-miss | History | Exam | Vitals | Test |
|---|---|---|---|---|
| SAH | thunderclap < 1 min, worst-ever, sentinel HA, exertion onset | meningismus (hours later), CN III palsy | BP often ↑ at presentation | CT < 6 h sens ≥ 95%; LP for xanthochromia after; CTA for aneurysm |
| Bacterial meningitis | fever + HA + neck stiff, AMS, immuno-compromise | Kernig, Brudzinski, photophobia | fever, ↑ HR | CSF: ↑ WBC PMN, ↓ glucose ratio, ↑ protein; gram stain |
| CVST | postpartum, OCP, thrombophilia, dehydration; subacute progressive HA | papilledema, focal deficits, seizures | variable | MRV (preferred); CT venogram |
| Angle-closure glaucoma | sudden eye pain + HA, halos, nausea | red eye, fixed mid-dilated pupil, firm globe | — | tonometry > 30 mmHg |
| CO poisoning | shared housing exposure, faulty heater, multiple ppl in household sick | cherry-red rare (late), AMS, ataxia | tachycardia, normal pulse-ox (don't trust!) | co-oximetry COHb % |
| Hypertensive emergency / PRES | poorly controlled HTN, pregnancy / preeclampsia | visual changes, AMS, seizures | BP often > 180/120 | MRI shows posterior white matter edema |
| GCA | age > 50, jaw claudication, scalp tenderness, vision change | temporal artery tenderness / nodularity | — | ESR + CRP very high; temporal artery biopsy |
| Cervicocephalic dissection | neck trauma / chiropractic, neck pain, Horner | ipsilateral Horner, contralateral deficits | — | CTA neck or MRA |

>>> FIRST-PASS EXCLUSION WORKUP

Screen: non-contrast head CT for all red-flag headache. Adds CTA / CTV / MRV if specific suspicion.
LP: after CT if SAH still suspected and CT > 6 h or non-diagnostic; for meningitis if no contraindication.
Tonometry: any red eye / acute vision change with HA.
Co-oximetry: any HA in household exposure context.
ESR / CRP: age > 50 with new HA, especially with jaw / scalp / vision symptoms.
Empiric treatment triggers: meningitis (give abx + dex + acyclovir if encephalitis suspected before LP if delay); GCA (give high-dose steroids before biopsy if vision threatened).

>>> VIGNETTES

[1] 42-year-old woman, postpartum day 14, with 4 days of progressive worsening headache, now with one brief seizure. Exam: alert, mild left arm clumsiness, papilledema bilaterally. BP 138/86, afebrile.
> Learner: red flag = "postpartum + progressive HA + papilledema + focal sign"; points to = SAH; first-pass = CT non-contrast.
Grade: red flag caught Y, can't-miss WRONG (SAH would be thunderclap, not progressive over days). Correct: CVST. First-pass should be MRV (or CTV) — CT alone is often falsely negative.

[2] 67-year-old man with 1 day of new right-sided headache, mild jaw pain when chewing, transient loss of vision in the right eye lasting 5 minutes yesterday. Exam: tender right temporal artery, vision currently normal.
> Learner: red flag = "jaw claudication + amaurosis + age + temporal tenderness"; points to = GCA; first-pass = ESR + CRP, start high-dose prednisone empirically, schedule temporal artery biopsy within a week.
Grade: caught Y, correct can't-miss Y, correct test Y — bonus for starting steroids before biopsy.

[3] (benign control) 28-year-old woman with 4 hours of bilateral pressure headache, no neuro deficits, ate poorly today, headache improves slightly with water and ibuprofen. Vitals normal, exam normal.
> Learner: red flag = "none"; reasonable workup = symptomatic management, return precautions.
Grade: appropriate Y. No over-call. (Common over-call here is ordering CT for any HA — not warranted.)

>>> SUMMARY
Caught: 2/3   False-positives: 0/1
Most-missed can't-miss: CVST (mistook for SAH on initial assessment).
Most-missed red-flag category: vitals + risk-context — postpartum status was named but not interpreted as a *thrombosis* risk.
Restudy: hypercoagulable states by demographic — postpartum, OCP, malignancy, prior VTE, thrombophilia — and what they shift on the can't-miss list for each chief complaint.
```
