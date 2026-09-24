---
title: "Pulmonary Nodule Management (Fleischner 2017)"
category: domain-healthcare-clinical/specialty
description: "Manage an incidental pulmonary nodule: confirm Fleischner applicability, measure and classify (solid, ground-glass, part-solid; single vs multiple), estimate malignancy risk, and commit to surveillance CT, PET-CT, biopsy, or resection with intervals."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: advanced
tags:
  - pulmonology
  - radiology
  - pulmonary-nodule
  - lung-cancer
  - specialty-assessment
  - spot-on-lung
  - chance-scan-finding
  - when-to-rescan
updated: "2026-09-24"
related_prompts:
  - domain-healthcare-clinical/prompts/reasoning/medicine_incidental_findings_management.md
  - domain-healthcare-clinical/prompts/interpretation/interp_ct_chest.md
  - domain-healthcare-clinical/prompts/specialty/medicine_oncology_case_framer.md
---

## Objective

Produce a pulmonology nodule-clinic recommendation for an incidentally detected pulmonary nodule: decide whether the Fleischner Society 2017 guidelines apply, classify the nodule precisely, estimate malignancy probability, and give a committed next step with CT intervals or a tissue/PET pathway. Decision support for a licensed clinician: confirm doses, renal/hepatic adjustment and thresholds against the current guideline and local formulary. A patient with hemoptysis or signs of advanced disease is escalated now, not placed on a surveillance schedule.

## When to Use

- An incidental pulmonary nodule on any CT (chest, CT angiogram, abdomen) in an adult — deciding whether Fleischner 2017 applies.
- Assigning surveillance intervals, or choosing PET-CT, biopsy, or resection for a solid nodule ≥8 mm.
- Checking a radiology recommendation for a wrong-row or wrong-measurement error.

**Not this prompt if:**

- Several incidental findings across organs, or how to communicate them — `reasoning/medicine_incidental_findings_management.md`; this prompt is the nodule-specific decision at full depth.
- You need the whole chest CT read systematically — `interpretation/interp_ct_chest.md`.
- Lung cancer is already confirmed and being staged for treatment — `specialty/medicine_oncology_case_framer.md`.

## Inputs

- CT details: indication, slice thickness, contrast, date; prior imaging for comparison
- Nodule(s): size (long and short axis, or volume), density (solid, pure ground-glass, part-solid with solid-component size), margin (smooth, lobulated, spiculated), location (lobe, perifissural, subpleural), calcification pattern, fat, cavitation, number and distribution
- Patient: age, smoking history (pack-years, quit date), prior cancer (type, date), family history of lung cancer, occupational/radon exposure, emphysema or fibrosis on CT, immune status
- Context that removes the nodule from Fleischner: lung cancer screening CT, known active malignancy, immunosuppression, age <35
- Fitness for biopsy or surgery; patient preference

## Role

Senior attending pulmonologist running a nodule clinic, supporting the referring clinician with a written recommendation for their review.

## Reasoning Steps

1. **Check that Fleischner applies.** It is for incidental nodules in adults ≥35. It does not apply to lung cancer screening CT (use Lung-RADS), patients with known primary cancer at risk of metastasis, immunocompromised patients (infection risk), or patients <35. Say which pathway you are using.
   - **Stop and escalate first if:** hemoptysis, a cavitating lesion with fever or weight loss (infection or TB — consider isolation), or signs of advanced disease (SVC obstruction, cord compression, hypercalcemia, airway obstruction) → urgent pathway, not nodule surveillance.

2. **Exclude benign features first.** Benign calcification patterns (diffuse, central, laminated, popcorn) or intranodular fat (hamartoma) need no follow-up. A perifissural or subpleural nodule with typical intrapulmonary lymph node morphology (smooth, triangular/lentiform, attached to a fissure) generally needs no follow-up even near 6–8 mm.

3. **Measure correctly.** Use thin-section (≤1.5 mm) images. Diameter = average of long and short axes, rounded to the nearest millimeter; volume where available. Part-solid nodules: record total size and solid-component size separately. Growth is a real change beyond measurement error (generally ≥2 mm).

4. **Estimate risk.** Low risk vs high risk per Fleischner combines patient factors (smoking, older age, prior cancer, family history, exposures, emphysema/fibrosis) with nodule factors (larger size, spiculation, upper lobe). For a quantitative estimate on solid nodules, use a validated model — the Mayo Clinic model (age, smoking, extrathoracic cancer >5 years ago, diameter, spiculation, upper lobe) for incidental nodules; the Brock (PanCan) model was derived in screening cohorts. For solid nodules ≥8 mm, ACCP thresholds are a common frame: <5% → surveillance; ~5–65% → PET-CT and/or non-surgical biopsy; >65% → proceed to tissue diagnosis or resection if fit.

5. **Apply Fleischner 2017 — solid nodules.**
   - **Single, <6 mm:** low risk — no routine follow-up; high risk — optional CT at 12 months.
   - **Single, 6–8 mm:** low risk — CT at 6–12 months, then consider CT at 18–24 months; high risk — CT at 6–12 months, then CT at 18–24 months.
   - **Single, >8 mm:** consider CT at 3 months, PET-CT, or tissue sampling (both risk groups).
   - **Multiple, <6 mm:** low risk — no routine follow-up; high risk — optional CT at 12 months.
   - **Multiple, 6–8 mm:** low risk — CT at 3–6 months, then consider CT at 18–24 months; high risk — CT at 3–6 months, then CT at 18–24 months.
   - **Multiple, >8 mm:** CT at 3–6 months, then consider CT at 18–24 months. Manage multiples by the most suspicious nodule.

6. **Apply Fleischner 2017 — subsolid nodules** (risk category does not change these).
   - **Single pure ground-glass, <6 mm:** no routine follow-up.
   - **Single pure ground-glass, ≥6 mm:** CT at 6–12 months to confirm persistence, then CT every 2 years until 5 years.
   - **Single part-solid, <6 mm:** no routine follow-up.
   - **Single part-solid, ≥6 mm:** CT at 3–6 months to confirm persistence. If unchanged and solid component remains <6 mm, annual CT for 5 years. A persistent part-solid nodule with a solid component ≥6 mm is highly suspicious.
   - **Multiple subsolid, <6 mm:** CT at 3–6 months; if stable, consider CT at 2 and 4 years.
   - **Multiple subsolid, ≥6 mm:** CT at 3–6 months; subsequent management by the most suspicious nodule.

7. **Choose PET-CT and biopsy correctly.** PET-CT is useful for solid nodules ≥8 mm with intermediate probability. It is unreliable for pure ground-glass and small solid nodules (false negatives from low metabolic activity; adenocarcinoma in situ/minimally invasive) and false-positive in infection/inflammation. Biopsy route: CT-guided transthoracic (peripheral; pneumothorax risk, higher with emphysema) vs navigational/robotic bronchoscopy with radial EBUS (central-to-mid, and when mediastinal staging is needed). A non-diagnostic biopsy does not exclude cancer.

8. **Stability rules.** A solid nodule stable for 2 years is generally benign. A subsolid nodule needs 5 years of stability because adenocarcinoma-spectrum lesions grow slowly. Increase in size or new/enlarging solid component → escalate.

9. **Link to screening.** After the nodule pathway, check lung cancer screening eligibility (USPSTF 2021: age 50–80, ≥20 pack-years, current smoker or quit within 15 years) and enroll if eligible. Offer smoking cessation to every current smoker.

10. **Verify.** Re-check that the size used is the average diameter (or volume) of the correct component, the table row matches density and multiplicity, the risk category is justified, and the plan does not use Fleischner in a screening, cancer, or immunocompromised patient.

## Output Format

```
PATHWAY: [Fleischner 2017 applies / does not — use X instead, and why]

NODULE CLASSIFICATION:
- Size: [average diameter or volume; solid component if part-solid]
- Density / margin / location: [ ]
- Single vs multiple: [dominant nodule identified]
- Benign features: [present/absent]

RISK: [low / high per Fleischner — factors; model estimate if solid ≥8 mm]

RECOMMENDATION:
- Next step: [CT at X months / PET-CT / biopsy route / resection referral / no follow-up]
- Subsequent: [intervals to end of surveillance]
- Escalation triggers: [growth ≥2 mm, new solid component, etc.]

SCREENING / PREVENTION: [LDCT eligibility; smoking cessation]

PITFALLS:
- [wrong pathway, wrong measurement, PET on GGN, 2-year rule applied to subsolid, non-diagnostic biopsy treated as benign]
```

## Verification

- [ ] The pathway is named (Fleischner 2017, Lung-RADS, or oncology/immunocompromised management) with the reason.
- [ ] Size is the average of long and short axes (or volume) on ≤1.5 mm sections, with the solid component recorded separately for part-solid nodules.
- [ ] The table row matches density, multiplicity, and risk category, and the risk category is traced to named patient and nodule factors.
- [ ] Any probability model (Mayo, Brock) is named with its inputs and ACCP thresholds are attributed; confirm doses, renal adjustment and thresholds against the current guideline and local formulary (e.g., renal function before any contrast study).
- [ ] The end of surveillance is stated (2 years solid, 5 years subsolid) and screening eligibility is addressed.

## False-Positive Prevention

- A perifissural or subpleural intrapulmonary lymph node treated as a suspicious nodule.
- A change under 2 mm, or a difference between thick- and thin-section scans, called growth.
- A new ground-glass or part-solid opacity put on 5-year surveillance before persistence is confirmed — many resolve (infection, hemorrhage) by the 3–6-month scan.
- A PET-avid nodule assumed malignant — infection and granulomatous disease (TB, endemic fungi, sarcoidosis) cause false positives.

## Worked Example

**Input:** 63 y/o F, CT angiogram for suspected PE (negative for PE). Incidental 7 mm (8 × 6 mm) smooth solid nodule in the right upper lobe, no other nodules. No calcification or fat. Mild centrilobular emphysema. 35 pack-years, quit 8 years ago. No cancer history. No prior chest CT. Immunocompetent.

**Output:**

```
PATHWAY: Fleischner 2017 — incidental finding, age ≥35, no cancer, immunocompetent, not a screening CT.

NODULE CLASSIFICATION:
- Size: average 7 mm ((8 + 6)/2) on 1 mm sections.
- Density / margin / location: solid, smooth, right upper lobe, not perifissural.
- Single.
- Benign features: none.

RISK: High — 35 pack-years, age 63, emphysema, upper-lobe location.

RECOMMENDATION:
- Next step: high-risk single solid 6–8 mm → non-contrast thin-section chest CT at 6–12 months (schedule at 6 months given upper lobe and emphysema).
- Subsequent: CT at 18–24 months. Stable at 2 years → discharge from nodule follow-up.
- PET-CT not indicated at 7 mm.
- Escalation triggers: growth ≥2 mm or new spiculation → PET-CT and tissue sampling (navigational bronchoscopy preferred; emphysema raises pneumothorax risk with a transthoracic approach).

SCREENING / PREVENTION: She is LDCT-eligible (50–80, ≥20 pack-years, quit <15 years). Once nodule surveillance ends, move her to annual low-dose CT screening. Reinforce abstinence from smoking.

PITFALLS:
- Using the long axis (8 mm) instead of the average invites the >8 mm row and an unnecessary PET or 3-month scan.
- A CT angiogram reported with thick slices must be re-measured on thin sections.
- She is screening-eligible now: either finish Fleischner surveillance then start LDCT, or fold the nodule into the screening program under Lung-RADS per local practice — not two parallel schedules.
```
