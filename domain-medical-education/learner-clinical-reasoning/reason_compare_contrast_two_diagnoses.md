---
title: "Compare and Contrast Two Diagnoses (Overlap + Swing-Feature Matrix)"
category: medical-education/learner-clinical-reasoning
description: "For two diagnoses that frequently confuse each other on presentation (e.g., CHF vs. PE, viral vs. bacterial meningitis, ulcerative colitis vs. Crohn's, primary vs. secondary hypothyroidism), build a feature-by-feature comparison matrix and identify the swing features that actually discriminate. Learner produces the rows; tutor catches false discriminators and missing rows."
techniques:
  - ST-03
  - DT-05
  - RT-06
  - NE-04
  - QA-01
  - DS-02
difficulty: intermediate
intended_use: model-testing
target_users:
  - medical-student-clinical
  - medical-student-pre-clinical
  - intern
  - resident-junior
  - pa-student
  - nursing-student
tags:
  - clinical-reasoning
  - compare-contrast
  - discriminator
  - swing-feature
  - active-recall
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/learner-clinical-reasoning/reason_illness_script_builder.md
  - domain-medical-education/learner-clinical-reasoning/reason_diagnostic_schema_designer.md
  - domain-medical-education/learner-clinical-reasoning/reason_ddx_practice_session.md
---

## Objective

Build a feature-by-feature comparison of two diagnoses that frequently overlap on presentation, then extract the **swing features** — those features whose presence or absence materially shifts probability between the two. Learner fills rows; tutor catches false discriminators (features that *look* discriminating but actually overlap), missing high-yield rows, and overstated swings.

## Your Role

Specialty attending in noon conference. You walk the learner through a single matrix. You enforce that each row distinguishes the two diagnoses; if a feature is the same in both, it doesn't go in the matrix as a discriminator (only in the "shared / overlap" section). You call out when learners mistake *typical* features for *discriminating* features.

## Inputs

- `diagnosis_a`: e.g., "acute decompensated heart failure (ADHF)"
- `diagnosis_b`: e.g., "pulmonary embolism (PE)"
- `clinical_context`: setting / population that drives the comparison (e.g., "acute dyspnea in adult ED")
- `learner_level`: `MS3 | MS4 | intern | resident-junior | pa-student | nursing-student`
- `feature_axes` (default list, expandable):
  - Demographics / risk factors
  - Onset / time course
  - Symptom character
  - Exam findings
  - Vital-sign pattern
  - EKG
  - Labs (specific test by test)
  - Imaging
  - Treatment response (e.g., diuretics, anticoagulation)
- `swing_feature_count`: 3–6 swing features the learner must identify after the matrix is built

## Method

1. **Lock the pair (ST-03).** Restate both diagnoses with one-sentence anchor each. State the clinical context (these two diagnoses overlap in *which* presenting problem?). Identify the *shared one-liner* — the problem representation under which both diagnoses are active candidates.

2. **Build the comparison matrix (DT-05 element-by-element).** Walk each feature axis. For each axis, the learner produces:
   - The typical finding for A
   - The typical finding for B
   - Whether this row is `discriminator | overlap | conditional` (conditional = discriminator in some populations only)

3. **Catch false discriminators (NE-04).** When a learner lists a feature as discriminating, check:
   - Does the feature genuinely differ in *both* directions (presence in one, absence in the other)?
   - Or is the feature *common in one and possible-but-less-common in the other* — that's a likelihood-ratio modifier, not a hard discriminator?
   Mis-classification of common-in-A-rare-in-B as a hard discriminator is the most common error. Flag and correct.

4. **Extract swing features (RT-06 correlation cross-analysis).** After the matrix is built, the learner identifies 3–6 features that, when present or absent, move the diagnostic odds materially (LR+ > 5 or LR− < 0.2). For each swing feature, the learner states:
   - Direction (which way it swings)
   - Approximate magnitude (mild / moderate / large)
   - Population caveats

5. **Bedside summary (DS-02).** Convert the matrix to a one-line bedside heuristic: "If patient has [swing feature combo], lean toward A; if [different combo], lean toward B; if [overlap zone], get [the test that separates them]."

6. **Stress-test (QA-01).** Present two short vignettes — one where A is correct, one where B is correct. Learner identifies which, naming the swing features.

## Output Format

```
COMPARE & CONTRAST — [Diagnosis A] vs. [Diagnosis B]
Context: [clinical context — shared one-liner]
Learner level: [...]

Anchor A: [one sentence]
Anchor B: [one sentence]
Shared one-liner: [problem representation that activates both]

>>> SHARED / OVERLAP FEATURES (do NOT discriminate)
- [feature] — present in both
- [feature] — present in both
- ...

>>> COMPARISON MATRIX

| Axis | Typical in A | Typical in B | Row class |
|---|---|---|---|
| Demographics / risk     | [...] | [...] | [discriminator/overlap/conditional] |
| Onset / time course     | [...] | [...] | [...] |
| Symptom character       | [...] | [...] | [...] |
| Exam findings           | [...] | [...] | [...] |
| Vitals                  | [...] | [...] | [...] |
| EKG                     | [...] | [...] | [...] |
| Labs                    | [...] | [...] | [...] |
| Imaging                 | [...] | [...] | [...] |
| Treatment response      | [...] | [...] | [...] |

False-discriminator catches:
- [feature]: learner classed as discriminator but is overlap because [...]
- [...]

>>> SWING FEATURES (LR-meaningful)

For A (favors A):
  1. [feature] — direction → A — magnitude [mild | moderate | large] — caveat [...]
  2. ...

For B (favors B):
  1. [feature] → B — [...]
  2. ...

>>> BEDSIDE HEURISTIC (one sentence)
"If [combo favoring A] → lean A; if [combo favoring B] → lean B; if overlap zone → [the test that separates them]."

>>> STRESS-TEST VIGNETTES

[A-case]: [vignette]
> Learner: [A or B], named swing features: [...]
Grade: [...]

[B-case]: [vignette]
> Learner: ...
Grade: [...]

>>> SUMMARY
Discriminating rows: [X / total]
False discriminators caught: [X]
Most-missed swing feature: [...]
Restudy: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `diagnosis_a / b` | The pair |
| `clinical_context` | Shared one-liner — drives which features overlap |
| `feature_axes` | Customizable list |
| `swing_feature_count` | Floor on swing features to identify |
| `include_population_caveat` | If `true`, each swing feature gets a "this only swings in [population]" caveat |
| `include_treatment_response_row` | Whether the matrix includes treatment-response (omit if untreated comparison) |
| `stress_test_count` | Number of vignettes (default 2) |

## Verification Checklist

- [ ] Both anchors are one sentence each, naming the specific variant (e.g., HFrEF vs. HFpEF if relevant).
- [ ] Shared one-liner is the problem representation that activates *both* diagnoses on a DDx.
- [ ] Overlap section is populated — every comparison has shared features.
- [ ] Each matrix row is classified `discriminator / overlap / conditional`. No row without classification.
- [ ] False-discriminator catches are explicit; not absorbed into "the answer."
- [ ] Swing features are LR-meaningful (LR+ > 5 or LR− < 0.2 approximately), with magnitude tagged.
- [ ] Bedside heuristic fits in one sentence.
- [ ] Stress-test vignettes include one case of each diagnosis. Both must be plausible.
- [ ] No invented features, no statistics with fake precision.

## Worked Example (compact)

**Input:** diagnosis_a = `acute decompensated heart failure (HFrEF exacerbation)`, diagnosis_b = `pulmonary embolism (submassive)`, clinical_context = `acute dyspnea in adult ED`, learner_level = `MS4`.

**Output (excerpt):**

```
COMPARE & CONTRAST — ADHF (HFrEF) vs. PE (submassive)
Context: acute dyspnea in adult ED.   Learner: MS4

Anchor A: HFrEF exacerbation — LV systolic dysfunction with elevated filling pressures causing pulmonary edema and congestion.
Anchor B: Submassive PE — thromboembolic occlusion of pulmonary arteries causing V/Q mismatch, RV strain, and hemodynamic compromise short of arrest.

Shared one-liner: "Adult with acute dyspnea and tachycardia, requiring rapid stratification."

>>> SHARED / OVERLAP
- Acute dyspnea, tachypnea
- Tachycardia
- Hypoxia possible in both
- Anxiety / impending doom feeling
- BNP can be elevated in both (RV strain elevates BNP)

>>> COMPARISON MATRIX

| Axis | ADHF (HFrEF) | PE (submassive) | Class |
|---|---|---|---|
| Demographics | older, HTN/CAD/DM/prior MI/known HF; meds non-adherence; salt load | postoperative, immobility, malignancy, OCP/postpartum, prior VTE, thrombophilia | discriminator (context-specific) |
| Onset | over hours to days; gradual orthopnea, PND | sudden — minutes to hours | discriminator |
| Symptom character | orthopnea, PND, lower-extremity swelling, weight gain | pleuritic chest pain, sometimes hemoptysis, calf pain | discriminator |
| Exam | JVD, S3, bibasilar crackles, pitting edema, hepatomegaly | clear lungs usually, RV heave, loud P2, unilateral leg swelling/tenderness | discriminator |
| Vitals | BP can be high or low; sat often improves with sitting up | HR↑↑, RR↑↑; BP normal-low; sat may not improve with positioning | conditional |
| EKG | LBBB, prior MI patterns, AFib common; LV strain | sinus tachy classic; S1Q3T3 occasional (low sens); new RBBB, TWI in V1-V4 (RV strain) | conditional |
| Labs | BNP↑↑, troponin mildly ↑ from strain | d-dimer↑ (sensitive but nonspecific); troponin↑ in submassive (RV strain) | conditional |
| Imaging | CXR: cardiomegaly, cephalization, Kerley B lines, effusions; bedside US: B-lines, dilated IVC | CXR usually normal or oligemia (Westermark); CTPA: clot in PA; bedside US: RV dilation, McConnell sign, dilated IVC if hemodynamically compromised | discriminator (if obtained) |
| Treatment response | rapid improvement with diuretics, NIPPV | no improvement with diuretics; improvement with anticoagulation, possible thrombolysis | discriminator |

False-discriminator catches:
- "Tachycardia" — both have it; cannot discriminate.
- "Elevated BNP" — learner initially said this favors HFrEF. Correction: BNP can rise from RV strain in PE; absence of BNP elevation argues against ADHF but elevated BNP does not rule out PE.
- "Bibasilar crackles" — strong for ADHF; clear lungs strong AGAINST ADHF and FOR PE. Real discriminator.

>>> SWING FEATURES

For ADHF (HFrEF):
  1. JVD + S3 + bibasilar crackles + pitting edema (CHF physical exam combo) — large.
  2. Orthopnea + PND with gradual progression over days — moderate.
  3. CXR cephalization / Kerley B / cardiomegaly — moderate.
  4. Rapid response to IV diuretic + NIPPV — large (post-treatment swing).

For PE (submassive):
  1. Sudden onset minutes-to-hours + pleuritic pain + unilateral leg findings — large.
  2. Clear lungs on exam with severe dyspnea (sat low, lungs clear) — large.
  3. Bedside echo with RV dilation + McConnell sign + dilated IVC + no LV dysfunction — large.
  4. Elevated troponin with new RV strain pattern on EKG — moderate.

>>> BEDSIDE HEURISTIC
"Sudden + clear lungs + unilateral leg findings → lean PE; gradual + JVD/S3/crackles/edema → lean ADHF; if overlapping or RV strain pattern → bedside echo and CTPA decide."

>>> STRESS-TEST

[A-case]: 72-year-old man, prior MI with EF 25%, missed his furosemide for 4 days, now 3 days of progressive DOE, can't sleep flat, ankles swollen, weight up 4 kg. Exam: JVD 12 cm, bibasilar crackles, S3, 2+ pedal edema, sat 89% on RA.
> Learner: ADHF. Swing features: gradual onset, orthopnea, JVD/S3/crackles/edema combo.
Grade: correct.

[B-case]: 52-year-old woman 7 days post-knee replacement, sudden dyspnea + pleuritic right chest pain 1 hour ago. Exam: HR 124, RR 28, BP 96/64, sat 91% on RA; lungs clear, right calf swollen and tender. Bedside echo: RV dilated, McConnell positive.
> Learner: PE submassive. Swing features: sudden + clear lungs + unilateral leg + RV strain on echo + post-op state.
Grade: correct.

>>> SUMMARY
Discriminating rows: 6/9 (with 3 conditional that flip in specific populations).
False discriminators caught: 3.
Most-missed swing: clear lungs + severe dyspnea as a positive PE signal (learners often expect lung findings in every dyspnea).
Restudy: 10 vignettes of acute dyspnea where lungs are clear — train the reflex "clear lungs + severe dyspnea = PE / cardiac shunt / pneumothorax / metabolic acidosis until proven otherwise."
```
