---
title: "Thyroid Nodule Workup"
category: domain-healthcare-clinical/specialty
description: "Work up a thyroid nodule from TSH through ultrasound risk stratification (ACR TI-RADS or ATA pattern), FNA size thresholds, Bethesda cytology category, and molecular testing to a committed surveillance, repeat-FNA, or surgical plan."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: advanced
tags:
  - endocrinology
  - thyroid
  - ultrasound
  - specialty-assessment
updated: "2026-09-24"
---

## Objective

Take a palpable or incidentally discovered thyroid nodule to a committed plan: functional status by TSH, sonographic risk category with the exact point or pattern assignment, FNA decision by size threshold, interpretation of Bethesda cytology and molecular results, and the next step — no follow-up, ultrasound surveillance at a stated interval, repeat FNA, molecular testing, active surveillance, lobectomy, or total thyroidectomy.

Distinct from [`medicine_incidental_findings_management.md`](../reasoning/medicine_incidental_findings_management.md), which triages many incidental findings across organ systems at a framework level; this prompt goes to point-level TI-RADS scoring, cytology, and surgical decision-making for the thyroid alone.

## Inputs

- How found: palpation, incidental CT/MRI/carotid US, incidental focal FDG-PET uptake
- Symptoms: compressive (dysphagia, dyspnea, positional), hoarseness, rapid growth, hyper/hypothyroid symptoms
- Risk history: childhood head/neck or total-body radiation, family history of thyroid cancer or MEN2/familial syndromes (FAP, PTEN hamartoma, Carney complex, DICER1), prior thyroid cancer
- Exam: nodule size, fixation, cervical lymphadenopathy, vocal cord function if hoarse
- Labs: TSH (± free T4), calcitonin if obtained
- Ultrasound: size in 3 dimensions, composition, echogenicity, shape (taller-than-wide on transverse), margin, echogenic foci, number of nodules, suspicious cervical nodes
- Cytology: Bethesda category, molecular test result (gene expression classifier or mutation/fusion panel) if performed
- Patient factors: age, comorbidities, pregnancy, preference toward surveillance vs surgery

## Role

Senior attending endocrinologist running a thyroid nodule clinic. Committed to one plan per nodule and explicit about which risk system and threshold is being used.

## Reasoning Steps

1. **TSH first.**
   - **Low TSH** → radionuclide scintigraphy (I-123 or Tc-99m pertechnetate). A hyperfunctioning ("hot") nodule has very low malignancy risk → no FNA; manage the hyperthyroidism (radioactive iodine, lobectomy, or antithyroid drug). Iso- or hypofunctioning nodules in a low-TSH patient proceed to US-based assessment.
   - **Normal or high TSH** → no scintigraphy; proceed to ultrasound. A higher TSH, even within range, is associated with modestly higher malignancy risk.
   - Scintigraphy is contraindicated in pregnancy.

2. **Ultrasound risk stratification — name the system.**
   **ACR TI-RADS (points summed across five features):**
   - Composition: cystic or almost completely cystic 0; spongiform 0; mixed cystic and solid 1; solid or almost completely solid 2
   - Echogenicity: anechoic 0; hyper- or isoechoic 1; hypoechoic 2; very hypoechoic (darker than strap muscles) 3
   - Shape: wider-than-tall 0; taller-than-wide 3
   - Margin: smooth 0; ill-defined 0; lobulated or irregular 2; extrathyroidal extension 3
   - Echogenic foci (sum all that apply): none or large comet-tail artifact 0; macrocalcifications 1; peripheral (rim) calcifications 2; punctate echogenic foci 3
   - Levels: TR1 (0 points) benign; TR2 (2) not suspicious; TR3 (3) mildly suspicious; TR4 (4–6) moderately suspicious; TR5 (≥7) highly suspicious
   - FNA thresholds: TR3 ≥2.5 cm (follow if ≥1.5 cm); TR4 ≥1.5 cm (follow if ≥1.0 cm); TR5 ≥1.0 cm (follow if ≥0.5 cm); TR1–TR2 no FNA
   **ATA 2015 sonographic pattern (alternative):** high suspicion (solid hypoechoic with irregular margin, microcalcifications, taller-than-wide, rim calcification with extrusive soft tissue, or ETE) → FNA ≥1 cm; intermediate (solid hypoechoic, smooth margins) → FNA ≥1 cm; low (iso/hyperechoic solid, or partially cystic with eccentric solid area) → FNA ≥1.5 cm; very low (spongiform, partially cystic without suspicious features) → FNA ≥2 cm or observe; purely cystic → no FNA.
   The two systems' thresholds differ (TI-RADS was designed to reduce FNAs of small nodules). Use one consistently and say which.

3. **Always examine the neck nodes.** A suspicious cervical lymph node (loss of fatty hilum, round shape, cystic change, microcalcifications, peripheral vascularity) gets FNA of the node (with thyroglobulin washout) regardless of the thyroid nodule's size.

4. **Special situations.**
   - Focal FDG-avid thyroid incidentaloma on PET carries a substantially higher malignancy risk than diffuse uptake → US and FNA if ≥1 cm and sonographically indicated.
   - Multinodular goiter: assess each nodule independently; the dominant nodule is not necessarily the suspicious one.
   - High-risk history (childhood radiation, familial syndrome): lower the FNA threshold.
   - Pregnancy: FNA can proceed if clinically indicated; surgery for cytologically malignant differentiated thyroid cancer is often deferred to postpartum unless growth or advanced disease.

5. **Interpret cytology — Bethesda System for Reporting Thyroid Cytopathology.**
   - **I Nondiagnostic:** repeat US-guided FNA (with on-site adequacy if available); persistently nondiagnostic solid nodules → close follow-up or diagnostic lobectomy depending on US suspicion. Purely cystic nondiagnostic in a low-suspicion nodule → surveillance.
   - **II Benign:** no immediate surgery. Follow-up US interval by suspicion (e.g., high-suspicion pattern repeat US and FNA within 12 months; low suspicion 12–24 months; very low may not need follow-up). Surgery for compressive symptoms or growth.
   - **III Atypia of undetermined significance (AUS):** repeat FNA and/or molecular testing; diagnostic lobectomy or surveillance by molecular result, US pattern, and preference.
   - **IV Follicular neoplasm:** molecular testing or diagnostic lobectomy.
   - **V Suspicious for malignancy:** surgery (molecular testing may guide extent).
   - **VI Malignant:** surgery, or active surveillance for select low-risk papillary microcarcinoma.
   - Implied malignancy risk per category is published with each Bethesda edition and differs between editions — quote ranges from the edition your cytopathology lab uses rather than a fixed number.

6. **Molecular testing (Bethesda III/IV).** Gene expression classifiers and mutation/fusion panels are used to rule out (high negative predictive value → surveillance) or rule in (e.g., BRAF V600E, TERT promoter, high-risk fusions → surgery, possibly more extensive). A "suspicious" classifier result without a specific high-risk alteration still carries substantial benign rate — diagnostic lobectomy, not total thyroidectomy by default.

7. **Surgery and extent.**
   - Diagnostic surgery for indeterminate cytology: lobectomy.
   - Differentiated thyroid cancer 1–4 cm without ETE or nodal disease: lobectomy or total thyroidectomy (lobectomy acceptable per ATA 2015 for low-risk disease).
   - >4 cm, gross ETE, clinically apparent nodal or distant metastases, or bilateral disease → total thyroidectomy ± neck dissection.
   - Papillary microcarcinoma <1 cm without high-risk features, away from the trachea and recurrent laryngeal nerve: active surveillance is an evidence-based alternative to lobectomy.
   - Suspected medullary carcinoma: calcitonin, CEA, RET germline testing, and exclude pheochromocytoma before surgery.

8. **Calcitonin screening** of all nodules is not uniformly recommended (practice differs between US and European guidance); obtain it when MTC is suspected (family history, MEN2 features, cytology suggestive).

## Output Format

```
FUNCTIONAL STATUS: TSH [value] → [scintigraphy needed? result]

ULTRASOUND:
- Size: [3 dimensions, max diameter]
- System: [ACR TI-RADS / ATA]
- Scoring: Composition [pts] | Echogenicity [pts] | Shape [pts] | Margin [pts] | Echogenic foci [pts] → Total [pts] = TR[n]  (or ATA pattern)
- Cervical nodes: [normal / suspicious — FNA node]

FNA DECISION: [FNA / surveillance / no follow-up] — threshold used: [ ]

CYTOLOGY: Bethesda [category] | Molecular: [result or not done]

PLAN:
- [surveillance US interval / repeat FNA / molecular test / lobectomy / total thyroidectomy / active surveillance]
- Pre-op if surgical: [vocal cord exam, calcium/PTH baseline, calcitonin/RET if MTC]

RISK MODIFIERS APPLIED: [radiation, family syndrome, PET avidity]

PITFALLS TO AVOID:
- [ ]
```

## Worked Example

**Input:** 44 y/o F, 1.8 cm right thyroid nodule found on carotid Doppler. Asymptomatic. No radiation history, no family history. TSH 1.9. Dedicated thyroid US: longitudinal 1.8 cm, transverse width 1.4 cm, AP height 1.6 cm (taller than wide on the transverse image); solid, hypoechoic, smooth margin, with multiple punctate echogenic foci. No suspicious cervical nodes. FNA: Bethesda III (AUS). Molecular panel: BRAF V600E detected.

**Output:**

```
FUNCTIONAL STATUS: TSH 1.9 — normal; no scintigraphy.

ULTRASOUND:
- Size: 1.8 (long) × 1.4 (transverse) × 1.6 (AP) cm; max 1.8 cm.
- System: ACR TI-RADS.
- Scoring: Composition solid 2 | Echogenicity hypoechoic 2 | Shape taller-than-wide 3 | Margin smooth 0 | Echogenic foci punctate 3 → Total 10 = TR5.
- Cervical nodes: none suspicious.

FNA DECISION: FNA indicated — TR5 ≥1.0 cm. (ATA pattern would also be high suspicion, FNA ≥1 cm.)

CYTOLOGY: Bethesda III (AUS) | Molecular: BRAF V600E detected.

PLAN:
- BRAF V600E in a TR5 nodule is highly specific for papillary thyroid carcinoma — manage as malignant despite indeterminate cytology.
- Surgery: 1.8 cm, no ETE, no nodal disease on US → right lobectomy is an appropriate initial operation for low-risk disease; total thyroidectomy is reasonable if the patient prefers to avoid possible completion surgery or if intraoperative/pathology findings upstage (ETE, nodal metastases, aggressive variant).
- Pre-op: laryngoscopy or vocal cord assessment baseline; dedicated neck nodal mapping US by an experienced sonographer; baseline calcium.
- Post-op: final pathology drives ATA risk-of-recurrence category, need for completion thyroidectomy, and whether RAI has any role; lobectomy patients often need no levothyroxine if TSH remains in target.

RISK MODIFIERS APPLIED: none; age 44 without adverse history.

PITFALLS TO AVOID:
- Do not stop at "AUS — repeat FNA in 3 months" when a high-risk molecular alteration is already in hand.
- Do not measure shape on the longitudinal view — taller-than-wide is assessed on the transverse image.
- Do not mix TI-RADS points with ATA size thresholds in the same report.
- Do not send a low-TSH patient straight to FNA — scintigraphy first; hot nodules are almost never malignant and cytology of a hot nodule is often misleading.
```
