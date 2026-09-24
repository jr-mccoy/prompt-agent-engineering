---
title: "Hypercortisolism (Cushing Syndrome) Workup"
category: domain-healthcare-clinical/specialty
description: "Establish endogenous Cushing syndrome with the right first-line tests and their confounders, localize by ACTH (pituitary MRI, IPSS, ectopic imaging, adrenal CT), and commit to surgery, medical therapy, and complication prophylaxis."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: advanced
tags:
  - endocrinology
  - cushing-syndrome
  - pituitary
  - specialty-assessment
updated: "2026-09-24"
---

## Objective

Work up suspected hypercortisolism in three stages — **exclude exogenous glucocorticoid, confirm endogenous cortisol excess, then localize the source** — with each test chosen and interpreted against its specific confounders. Produce a committed diagnosis (Cushing disease, ectopic ACTH, adrenal Cushing, non-neoplastic physiologic hypercortisolism, or not Cushing) and the treatment and safety plan that follows.

Distinct from [`specialty_adrenal_incidentaloma.md`](specialty_adrenal_incidentaloma.md), which handles mild autonomous cortisol secretion discovered from an adrenal image; this prompt starts from the clinical suspicion of Cushing syndrome. Mechanism of the HPA axis lives in [`patho_endocrine_axis_dysfunction.md`](../pathophysiology/patho_endocrine_axis_dysfunction.md); tapering exogenous steroids lives in [`pharm_steroid_taper_design.md`](../pharmacology/pharm_steroid_taper_design.md).

## Inputs

- Clinical features: discriminating (easy bruising, facial plethora, proximal myopathy, wide violaceous striae >1 cm; in children, weight gain with falling height velocity) vs nonspecific (weight gain, hypertension, diabetes, depression, fatigue, acne, hirsutism, menstrual irregularity, osteoporosis, recurrent infections)
- Tempo: months-years vs rapid weeks (ectopic ACTH or carcinoma), hypokalemia, edema, hyperpigmentation
- All glucocorticoid exposure: oral, inhaled, intranasal, topical, intra-articular, epidural, injectable; megestrol; medroxyprogesterone; ritonavir or cobicistat with inhaled/nasal fluticasone or budesonide
- Confounders: pregnancy, oral estrogen, CYP3A4 inducers/inhibitors, alcohol use disorder, severe obesity, depression, uncontrolled diabetes, critical illness, night-shift work, renal impairment, smoking/licorice/chewing tobacco (salivary)
- Test results: 1 mg DST, late-night salivary cortisol (LNSC) ×2, 24-h urinary free cortisol (UFC) ×2 with creatinine and volume, morning ACTH, potassium, DHEAS, pituitary MRI, CRH/desmopressin stimulation, IPSS, CT/PET

## Role

Senior attending endocrinologist at a pituitary/adrenal center. Rigorous about test selection and confounders, decisive about localization, explicit about which consensus thresholds are being applied.

## Reasoning Steps

1. **Rule out exogenous glucocorticoid first.** Iatrogenic Cushing syndrome is the most common cause. Ask about every route. Exogenous steroids suppress ACTH and endogenous cortisol — biochemistry looks "low" while the patient looks Cushingoid (except with hydrocortisone/prednisolone, which cross-react in cortisol immunoassays). Ritonavir/cobicistat plus inhaled fluticasone is a classic hidden cause.

2. **Decide whether to test.** Test patients with multiple progressive features, especially the discriminating ones; unusual features for age (osteoporosis or hypertension in a young adult); children with weight gain and falling height percentile; and adrenal incidentalomas (handled separately). Do not screen unselected patients with obesity or diabetes.

3. **First-line tests (Endocrine Society 2008 Cushing diagnosis guideline) — use at least two.**
   - **1 mg overnight DST:** 1 mg at 23:00, cortisol at 08:00. Normal ≤1.8 µg/dL (50 nmol/L) — sensitive cut-off. False positives: CYP3A4 inducers (rifampin, phenytoin, carbamazepine, phenobarbital), oral estrogen/pregnancy (raised CBG), malabsorption, missed dose. Measure a dexamethasone level with the cortisol when confounding is possible.
   - **Late-night salivary cortisol (≥2 samples, 23:00–midnight):** above the assay-specific upper reference limit is abnormal. Best test for loss of circadian rhythm; preferred in estrogen users. Invalid in night-shift workers and disturbed sleep; contaminated by licorice, chewing tobacco, smoking, topical hydrocortisone on hands, gum bleeding.
   - **24-h UFC (≥2 collections):** above assay ULN is abnormal; much higher values (several-fold ULN) make Cushing very likely. Check creatinine to confirm adequate collection. False-low with eGFR <60; false-high with high fluid intake (>5 L/day), pregnancy, and some drugs with immunoassay cross-reactivity (carbamazepine, fenofibrate) — LC-MS/MS avoids most.
   - **Cyclical Cushing:** intermittent cortisol excess; normal tests during a trough do not exclude — repeat LNSC over time (patient collects during symptomatic periods).
   - **Discordant or borderline:** repeat, add the third test, or use dexamethasone-CRH or desmopressin testing to separate from physiologic (non-neoplastic) hypercortisolism.

4. **Distinguish physiologic hypercortisolism (formerly "pseudo-Cushing").** Alcohol use disorder, severe depression, severe obesity with PCOS, uncontrolled diabetes, critical illness, pregnancy, and extreme exercise activate the HPA axis. Features: mild elevations, LNSC often closer to normal, normalizes with treatment of the driver (e.g., after alcohol abstinence). Re-test after the driver is treated rather than proceeding to localization.

5. **Localize — morning plasma ACTH (on at least two occasions if borderline).**
   - **ACTH suppressed (commonly <5 pg/mL, <1.1 pmol/L; assay-dependent):** ACTH-independent → adrenal CT (adenoma, carcinoma, bilateral macronodular or micronodular disease such as PPNAD in Carney complex).
   - **ACTH normal or high (commonly >20 pg/mL, >4.4 pmol/L):** ACTH-dependent → pituitary (Cushing disease, ~70–80% in adults) vs ectopic ACTH.
   - **Intermediate (5–20 pg/mL):** repeat; CRH stimulation (ACTH rise supports pituitary) and DHEAS (low supports adrenal).

6. **ACTH-dependent: pituitary vs ectopic.**
   - **Pituitary MRI** with dynamic contrast (small corticotroph adenomas are frequently not seen; ~10% of healthy adults have incidental pituitary lesions).
   - Consensus (Pituitary Society 2021) supports proceeding to surgery without IPSS when MRI shows an adenoma ≥10 mm with concordant dynamic tests (CRH/desmopressin response, dexamethasone suppression on high-dose testing) — practice varies for 6–9 mm lesions; state the threshold used.
   - **Bilateral inferior petrosal sinus sampling (IPSS)** with CRH (or desmopressin) when MRI is negative, equivocal, or small: central-to-peripheral ACTH ratio ≥2 at baseline or ≥3 after stimulation → pituitary source. Must be done while hypercortisolemic (confirm cortisol excess on the day). Lateralization from IPSS is unreliable.
   - **Ectopic ACTH:** rapid onset, severe hypokalemia, edema, hypertension, hyperpigmentation, very high cortisol and ACTH, male predominance. Imaging: CT neck/chest/abdomen/pelvis, then somatostatin-receptor PET (Ga-68 DOTATATE) for neuroendocrine tumors (bronchial carcinoid, thymic, pancreatic NET, MTC, pheochromocytoma); small-cell lung cancer typically obvious on CT.

7. **Treat the source.**
   - **Cushing disease:** transsphenoidal adenomectomy by an experienced pituitary surgeon. Post-op remission = low morning cortisol (commonly <2–5 µg/dL) on day 1–3 → glucocorticoid replacement (hydrocortisone 10–12 mg/m²/day in divided doses) with slow wean over months as the axis recovers. Persistent/recurrent disease → repeat surgery, radiotherapy/radiosurgery, medical therapy, or bilateral adrenalectomy (lifelong replacement; monitor for corticotroph tumor progression — Nelson syndrome).
   - **Adrenal adenoma:** laparoscopic unilateral adrenalectomy with perioperative and postoperative glucocorticoid replacement.
   - **Adrenocortical carcinoma:** open adrenalectomy at a high-volume center; mitotane; oncology.
   - **Ectopic ACTH:** resect the source; if not resectable or not found, medical therapy or bilateral adrenalectomy.
   - **Medical therapy (bridge, inoperable, or persistent):** steroidogenesis inhibitors — osilodrostat, metyrapone, ketoconazole (hepatotoxicity, CYP3A4 interactions, QT), levoketoconazole; pituitary-directed — pasireotide (hyperglycemia), cabergoline; glucocorticoid receptor antagonist — mifepristone (cortisol levels cannot be used to monitor; watch hypokalemia and clinical adrenal insufficiency). Monitor for adrenal insufficiency on inhibitors (block-and-replace or titrate to normal UFC/LNSC).
   - **Severe hypercortisolism (emergency — psychosis, sepsis, severe hypokalemia, uncontrolled hyperglycemia/hypertension):** IV etomidate infusion in ICU, or rapid-onset oral osilodrostat/metyrapone ± ketoconazole combination; bilateral adrenalectomy if refractory.

8. **Treat the complications now, regardless of source.**
   - VTE: hypercortisolism is hypercoagulable — thromboprophylaxis perioperatively and around IPSS.
   - Infection: PJP prophylaxis (TMP-SMX) with severe hypercortisolism; screen and vaccinate.
   - Hypokalemia: spironolactone or eplerenone plus KCl.
   - Hypertension, diabetes, osteoporosis (bisphosphonate), myopathy (PT), psychiatric symptoms — treat actively; many improve slowly after cure.

## Output Format

```
EXOGENOUS STEROID EXCLUSION: [all routes reviewed — result]

PRETEST ASSESSMENT: [discriminating features present; indication to test]

FIRST-LINE TESTING:
- 1 mg DST: [value → interpretation; confounders]
- LNSC ×2: [values vs assay ULN]
- UFC ×2: [values vs ULN; creatinine; eGFR]
- Conclusion: [endogenous Cushing confirmed / excluded / physiologic hypercortisolism / indeterminate → next test]

LOCALIZATION:
- ACTH: [value → dependent / independent / intermediate]
- Imaging: [pituitary MRI / adrenal CT / ectopic search]
- Dynamic / IPSS: [results, ratios]
- Source: [pituitary / ectopic / adrenal]

TREATMENT:
- Definitive: [surgery type]
- Bridge / medical: [drug, starting dose, monitoring]
- Perioperative glucocorticoid plan: [ ]

COMPLICATION PROPHYLAXIS: [VTE, PJP, K, glucose, BP, bone]

THRESHOLDS / GUIDELINES APPLIED: [ ]

PITFALLS TO AVOID:
- [ ]
```

## Worked Example

**Input:** 34 y/o F, 18 months of 15 kg central weight gain, new hypertension (on lisinopril), prediabetes (A1c 6.3%), easy bruising, 1.5 cm purple abdominal striae, proximal weakness climbing stairs, oligomenorrhea. On combined oral contraceptive. No glucocorticoids by any route. Labs: 1 mg DST cortisol 6.4 µg/dL. LNSC 0.31 and 0.36 µg/dL (assay ULN 0.10). UFC 188 and 212 µg/24 h (ULN 50), creatinine appropriate, eGFR >90. K 3.8. Morning ACTH 58 pg/mL. Pituitary dynamic MRI: 5 mm hypoenhancing lesion in the left adenohypophysis.

**Output:**

```
EXOGENOUS STEROID EXCLUSION: None by oral, inhaled, nasal, topical, or injected route; no ritonavir/cobicistat.

PRETEST ASSESSMENT: High — bruising, wide violaceous striae, proximal myopathy (discriminating), plus hypertension, dysglycemia, oligomenorrhea at age 34.

FIRST-LINE TESTING:
- 1 mg DST 6.4 µg/dL: abnormal, but the combined OCP raises CBG and can falsely elevate total cortisol — do not rely on DST alone here.
- LNSC 0.31 and 0.36 (>3× ULN, unaffected by estrogen): abnormal.
- UFC 188 and 212 (~4× ULN, adequate collections): abnormal.
- Conclusion: Endogenous Cushing syndrome confirmed by two estrogen-independent tests. Severity and discriminating features argue against physiologic hypercortisolism.

LOCALIZATION:
- ACTH 58 pg/mL → ACTH-dependent.
- MRI: 5 mm lesion — below the ≥10 mm size at which consensus allows skipping IPSS, and within the range of incidental pituitary lesions.
- Next: IPSS with CRH (or desmopressin) while confirmed hypercortisolemic; LMWH prophylaxis around the procedure. If central:peripheral ratio ≥2 basal or ≥3 stimulated → Cushing disease.
- If IPSS shows no gradient → ectopic search: CT chest/abdomen, Ga-68 DOTATATE PET.
- Source (provisional): pituitary (female, 30s, gradual onset, K normal — typical of Cushing disease).

TREATMENT:
- Definitive (if IPSS confirms central): transsphenoidal adenomectomy targeting the left-sided lesion at a high-volume pituitary center.
- Bridge while awaiting IPSS/surgery (given myopathy and dysglycemia): metyrapone 250 mg PO TID-QID titrated to normal LNSC/UFC, or osilodrostat 2 mg PO BID titrated; watch for adrenal insufficiency, hypokalemia, and (metyrapone) hirsutism/hypertension from precursor accumulation.
- Post-op: morning cortisol day 1–3 without exogenous steroid until level drawn (per center protocol, or with stress coverage and dexamethasone if protocol requires); if low → hydrocortisone 15–20 mg/day divided and slow wean over 6–12 months with periodic ACTH stimulation testing.
- Stop combined OCP pre-op (VTE risk); use non-estrogen contraception.

COMPLICATION PROPHYLAXIS:
- VTE: LMWH around IPSS and surgery; mechanical prophylaxis.
- PJP: TMP-SMX DS three times weekly while UFC markedly elevated — discuss given severity.
- BP: switch or add as needed; target <130/80.
- Glucose: metformin 500 mg BID titrate.
- Bone: DEXA; vitamin D/calcium; bisphosphonate if osteoporotic.
- Contraception: progestin-only or IUD (also removes CBG confounding for repeat testing).

THRESHOLDS / GUIDELINES APPLIED: Endocrine Society 2008 diagnosis guideline for first-line tests; Pituitary Society consensus (2021) for MRI size and IPSS criteria; assay-specific ULNs for LNSC and UFC.

PITFALLS TO AVOID:
- Do not use DST as the deciding test in a woman on oral estrogen.
- Do not send a 5 mm MRI lesion to surgery without IPSS — an incidental pituitary lesion plus ectopic ACTH is a known trap.
- Do not perform IPSS when cortisol is not currently elevated (cyclical disease) — ratios become uninterpretable.
- Do not forget VTE prophylaxis — thrombosis is a leading cause of peri-procedural morbidity in Cushing syndrome.
```
