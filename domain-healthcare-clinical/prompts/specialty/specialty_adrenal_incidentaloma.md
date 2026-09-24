---
title: "Adrenal Incidentaloma Evaluation"
category: domain-healthcare-clinical/specialty
description: "Evaluate an incidentally found adrenal mass on two axes — malignant potential (unenhanced HU, washout, size, heterogeneity) and hormonal function (dexamethasone suppression, metanephrines, aldosterone-renin ratio) — and commit to discharge, follow-up, or adrenalectomy."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: advanced
tags:
  - endocrinology
  - adrenal
  - radiology
  - specialty-assessment
  - found-on-scan
  - lump-near-kidney
  - resistant-blood-pressure
updated: "2026-09-24"
related_prompts:
  - domain-healthcare-clinical/prompts/specialty/specialty_hypercortisolism_workup.md
  - domain-healthcare-clinical/prompts/reasoning/medicine_incidental_findings_management.md
  - domain-healthcare-clinical/prompts/interpretation/interp_ct_abdomen_pelvis.md
---

## Objective

Take an adrenal mass ≥1 cm discovered on imaging done for another reason and answer the two questions that decide management: **Is it malignant (or at risk)?** and **Is it hormonally active?** Produce the imaging interpretation with numbers, the biochemical screening panel with interfering-drug review, the interpretation of results, and a committed plan: discharge from follow-up, surveillance with stated interval, further imaging, or referral for adrenalectomy.

Decision support for a licensed clinician: confirm doses, renal/hepatic adjustment and thresholds against the current guideline and local formulary. A suspected catecholamine crisis, adrenal hemorrhage or adrenal crisis is escalated now, not after this output.

## When to Use

- An adrenal mass ≥1 cm reported on CT or MRI done for another reason.
- A known adrenal nodule where the referring clinician asks whether hormones need checking, imaging needs repeating, or surgery is warranted.
- Bilateral adrenal masses, or an adrenal mass in someone with a history of cancer, where the imaging phenotype and the biopsy question must be settled.

**Not this prompt if:**
- The report lists several incidental findings across organs and needs triage as a whole → [`medicine_incidental_findings_management.md`](../reasoning/medicine_incidental_findings_management.md).
- The starting point is clinical suspicion of overt Cushing syndrome rather than an adrenal image → [`specialty_hypercortisolism_workup.md`](specialty_hypercortisolism_workup.md).

## Inputs

- Imaging: modality, size (cm), unilateral vs bilateral, unenhanced CT attenuation (HU), homogeneity, margins, calcification/necrosis, contrast washout (enhanced and 15-min delayed HU), chemical-shift MRI signal loss, prior imaging for growth comparison, FDG-PET if done
- Clinical: age, known extra-adrenal malignancy, hypertension (number of drugs, resistant?), hypokalemia, diabetes, osteoporosis/fragility fracture, obesity, paroxysmal headache/palpitations/sweating, virilization or feminization, Cushingoid features
- Medications: glucocorticoids (any route), estrogens, CYP3A4 inducers/inhibitors, antihypertensives (MRAs, diuretics, ACEi/ARB, beta-blockers, dihydropyridine CCBs), tricyclics, SNRIs, MAOIs, levodopa, sympathomimetics
- Labs available: 1 mg DST cortisol (with dexamethasone level if measured), ACTH, DHEAS, plasma free metanephrines or 24-h urine fractionated metanephrines, aldosterone, renin (activity or concentration), potassium

## Role

Senior attending endocrinologist in an adrenal clinic supporting and writing to the referring (treating) clinician. Numbers first, interfering factors named, one plan.

## Reasoning Steps

1. **Confirm it is a true incidentaloma.** ≥1 cm, discovered on imaging not performed for suspected adrenal disease. In a patient with known extra-adrenal cancer, the pretest probability of metastasis is much higher — imaging interpretation and biopsy thresholds change.
   - **Stop and escalate now if:** paroxysmal severe hypertension, tachyarrhythmia or chest pain suggesting catecholamine crisis; acute flank or abdominal pain with hypotension (adrenal hemorrhage or rupture); hypotension, vomiting, hyponatremia or hyperkalemia suggesting adrenal crisis (hydrocortisone first, tests later). Give no beta-blocker, biopsy or surgery before pheochromocytoma is excluded.

2. **Imaging phenotype — malignant potential.**
   - **Unenhanced CT ≤10 HU, homogeneous:** lipid-rich adenoma. Benign phenotype; no further imaging needed for the mass itself.
   - **>10 HU or no unenhanced phase:** further characterization.
     - **Washout CT** (unenhanced, 60–75 s portal venous, 15-min delayed): absolute percentage washout = (enhanced − delayed) / (enhanced − unenhanced) × 100 ≥60%, or relative washout = (enhanced − delayed) / enhanced × 100 ≥40% → consistent with lipid-poor adenoma. Washout performance is less reliable than unenhanced HU and some pheochromocytomas and metastases wash out; interpret with the rest of the phenotype.
     - **Chemical-shift MRI:** signal drop on opposed-phase → intracellular lipid (adenoma).
     - **FDG-PET/CT** for indeterminate masses, especially with prior malignancy.
   - **Suspicious features:** size >4 cm, heterogeneity, irregular margins, necrosis, calcification, HU >20, growth on serial imaging, invasion. Adrenocortical carcinoma (ACC) is rare but most often presents as a large (>4 cm), heterogeneous, high-HU mass, sometimes with steroid/androgen excess.
   - **Homogeneous masses with HU 11–20 and <4 cm:** management (additional imaging now vs a single follow-up study) differs between guideline versions — state the guideline you follow.
   - **Myelolipoma** (macroscopic fat, markedly negative HU), **cyst**, and **hemorrhage** have diagnostic imaging appearances and need no hormonal workup beyond clinical judgment.

3. **Hormonal evaluation — everyone gets cortisol screening.**
   - **1 mg overnight dexamethasone suppression test (DST):** 1 mg PO at 23:00, serum cortisol at 08:00–09:00.
     - ≤1.8 µg/dL (≤50 nmol/L): autonomous cortisol secretion excluded.
     - >1.8 µg/dL without overt Cushing features: autonomous cortisol secretion. The 2016 ESE guideline split this into "possible" (1.9–5.0 µg/dL, 51–138 nmol/L) and "autonomous" (>5.0 µg/dL); the 2023 ESE/ENSAT update groups these as mild autonomous cortisol secretion (MACS). Confirm the terminology and cut-offs of the guideline you are applying.
     - If DST abnormal: morning ACTH (suppressed supports ACTH-independent cortisol excess), DHEAS (low supports autonomous secretion), repeat DST ± dexamethasone level to confirm adequate exposure. 24-h UFC and late-night salivary cortisol are insensitive for MACS and are used for suspected overt Cushing.
     - False-positive DST: CYP3A4 inducers (rifampin, phenytoin, carbamazepine, St John's wort) accelerate dexamethasone clearance; oral estrogen raises cortisol-binding globulin (stop 6 weeks before or interpret with caution); malabsorption; nonadherence to the dose.
   - **Pheochromocytoma:** plasma free metanephrines (supine after 20–30 min rest, reference ranges for supine sampling) or 24-h urine fractionated metanephrines. The 2023 ESE/ENSAT update suggests omitting testing when unenhanced HU ≤10; older AACE/AAES guidance tests all incidentalomas. When in doubt, and always before any biopsy or surgery, test. Values ≥3–4× upper limit strongly suggest pheochromocytoma; mild elevations require exclusion of drug interference (tricyclics, SNRIs, MAOIs, levodopa, sympathomimetics, phenoxybenzamine) and repeat.
   - **Primary aldosteronism:** aldosterone-to-renin ratio (ARR) if hypertension or hypokalemia (spontaneous or diuretic-induced). Correct potassium first (hypokalemia suppresses aldosterone → false negative). MRAs and high-dose diuretics raise renin → false negatives; beta-blockers suppress renin → false positives; ACEi/ARB/dihydropyridine CCB raise renin → false negatives. Positive screen → confirmatory testing (saline infusion, oral salt loading, or captopril challenge) → adrenal vein sampling before surgery in most patients, because CT does not reliably lateralize.
   - **Sex steroids/androgens** (DHEAS, testosterone, 17-hydroxyprogesterone, 11-deoxycortisol, estradiol in men) only when ACC is suspected on imaging or clinical virilization/feminization.

4. **Bilateral adrenal masses.** Evaluate each mass separately for phenotype; add 17-OHP for congenital adrenal hyperplasia; consider bilateral metastases, lymphoma, infection (TB, histoplasmosis), hemorrhage, or bilateral macronodular hyperplasia. Test for adrenal insufficiency when infiltrative disease is suspected.

5. **Biopsy is rarely indicated.** Only when metastasis is suspected in a patient with known extra-adrenal cancer and the result will change management — and only after biochemical exclusion of pheochromocytoma (biopsy of a pheochromocytoma can trigger hypertensive crisis). Biopsy is not used to diagnose ACC.

6. **Decide.**
   - **Benign phenotype + non-functioning:** no further imaging or hormonal follow-up (ESE); advise the referring clinician explicitly so the patient is not surveilled indefinitely.
   - **Benign phenotype + MACS:** screen and treat comorbidities (hypertension, T2DM, dyslipidemia, osteoporosis); consider adrenalectomy individually in younger patients with progressive or cortisol-attributable comorbidities; annual reassessment of comorbidities.
   - **Pheochromocytoma:** alpha-blockade (phenoxybenzamine or doxazosin) for 7–14 days with liberal salt and fluid, then beta-blockade only after alpha-blockade if tachycardic; laparoscopic adrenalectomy by an experienced surgeon; germline genetic testing.
   - **Unilateral primary aldosteronism on AVS:** laparoscopic adrenalectomy; bilateral or non-surgical → MRA (spironolactone 12.5–25 mg daily titrated, or eplerenone).
   - **Overt Cushing syndrome:** adrenalectomy with perioperative glucocorticoid coverage (contralateral adrenal is suppressed).
   - **Indeterminate imaging, non-functioning:** repeat non-contrast CT or MRI in 6–12 months; growth >20% and ≥5 mm (or per chosen guideline) → surgery.
   - **Suspicious for ACC (>4 cm heterogeneous, high HU) or growing:** multidisciplinary adrenal tumor board; open or experienced laparoscopic adrenalectomy; full steroid panel preoperatively.

7. **Perioperative cortisol.** Any patient with MACS or overt cortisol excess undergoing unilateral adrenalectomy needs postoperative adrenal insufficiency testing or empiric glucocorticoid coverage — contralateral suppression can last months.

## Output Format

```
MASS: [side, size, discovery context]

IMAGING PHENOTYPE:
- Unenhanced HU: [ ] | Homogeneity: [ ] | Margins: [ ] | Washout APW/RPW: [ ] | MRI chemical shift: [ ]
- Interpretation: [lipid-rich adenoma / lipid-poor adenoma / indeterminate / suspicious for ACC or metastasis / myelolipoma]

HORMONAL SCREEN:
- 1 mg DST cortisol: [value, interpretation] — confounders: [ ]
- Metanephrines: [ordered / omitted (reason) / result]
- ARR: [indicated? result] — confounders: [ ]
- Androgens/steroids: [if indicated]

DIAGNOSIS: [non-functioning adenoma / MACS / pheochromocytoma / PA / Cushing / indeterminate / suspected ACC]

PLAN:
- [discharge from follow-up / surveillance imaging at X months / surgery referral / confirmatory testing]
- Comorbidity management: [ ]
- Perioperative glucocorticoid plan: [if surgical]

GUIDELINE / THRESHOLDS USED: [ ]

PITFALLS TO AVOID:
- [ ]
```

## Verification

- [ ] The imaging interpretation quotes the actual numbers (size, unenhanced HU, APW/RPW) and the phenotype call follows from them.
- [ ] Every patient has a 1 mg DST result or order, and each abnormal hormonal result lists the interfering drugs and conditions checked.
- [ ] Pheochromocytoma is excluded biochemically (or its omission justified by named guideline and HU) before any biopsy, surgery or beta-blocker.
- [ ] HU, washout, DST, ARR and growth thresholds are attributed to a named guideline and year; confirm doses, renal adjustment and thresholds against the current guideline and local formulary.
- [ ] The plan is one committed disposition, including an explicit "no further follow-up" statement when the mass is benign and non-functioning.

## False-Positive Prevention

- **Mildly raised metanephrines called pheochromocytoma.** Seated sampling, tricyclics/SNRIs, levodopa, sympathomimetics and acute illness cause false elevations; values below ~3× ULN need drug review and repeat supine sampling before imaging or surgery.
- **An unsuppressed DST called MACS without checking dexamethasone exposure.** CYP3A4 inducers, oral estrogen, malabsorption or a missed dose raise post-dexamethasone cortisol; repeat with a dexamethasone level when any apply.
- **A positive ARR taken as primary aldosteronism.** A high ratio driven by a very low renin with low-normal aldosterone, or measured on a beta-blocker, can be a false positive — confirm with a suppression test before lateralization.
- **The visible adenoma assumed to be the hormone source.** Non-functioning adenomas are common with age; in primary aldosteronism lateralize by AVS, not by the CT image.
- **A contrast-only scan read as "suspicious."** Without an unenhanced phase the mass is uncharacterized, not malignant — characterize it before escalating.

## Worked Example

**Input:** 61 y/o M, CT abdomen for renal colic shows a 2.8 cm homogeneous left adrenal mass, unenhanced 6 HU, smooth margins. No prior imaging. HTN on amlodipine 10 mg + hydrochlorothiazide 25 mg + losartan 100 mg; BP 146/88. K 3.4 on HCTZ. T2DM with A1c 7.9%. DEXA: osteopenia. No paroxysmal symptoms. No Cushingoid features. Not on glucocorticoids or estrogen. Labs: 1 mg DST cortisol 3.1 µg/dL (86 nmol/L). Plasma free metanephrines normal. Aldosterone 18 ng/dL, plasma renin activity 0.3 ng/mL/h (ARR 60).

**Output:**

```
MASS: Left adrenal, 2.8 cm, found on CT for renal colic.

IMAGING PHENOTYPE:
- Unenhanced HU 6 | homogeneous | smooth | washout not needed | MRI not needed
- Interpretation: lipid-rich adenoma. No further imaging for malignancy characterization.

HORMONAL SCREEN:
- 1 mg DST cortisol 3.1 µg/dL — not suppressed. No CYP3A4 inducers, no estrogen. Autonomous cortisol secretion without overt Cushing features = MACS (2023 ESE/ENSAT terminology; "possible autonomous cortisol secretion" under 2016 cut-offs). Next: morning ACTH, DHEAS, repeat DST with a dexamethasone level.
- Metanephrines: normal (HU ≤10 would have allowed omission under 2023 ESE, but the result is reassuring).
- ARR: 60 (ng/dL per ng/mL/h) with aldosterone 18 — positive screen. Confounders: losartan and HCTZ raise renin (tend to false negatives), and K 3.4 suppresses aldosterone — so a positive ARR despite these factors is meaningful.
- Androgens: not indicated.

DIAGNOSIS: Left adrenal adenoma with MACS and a positive screen for primary aldosteronism — possible co-secreting adenoma.

PLAN:
- Replete potassium to ≥4.0 (KCl 20–40 mEq daily); switch HCTZ to a non-interfering agent if BP allows (verapamil SR or hydralazine/doxazosin per local washout protocol) before confirmatory testing.
- Confirmatory PA test: saline infusion test (2 L NS over 4 h, seated protocol) or captopril challenge.
- If confirmed: adrenal vein sampling (cosyntropin-stimulated or unstimulated per center) to lateralize — a CT-visible left adenoma does not prove the left side is the aldosterone source, especially at age 61.
- If lateralizes left: laparoscopic left adrenalectomy — addresses both aldosterone and MACS; perioperative hydrocortisone coverage and post-op morning cortisol/ACTH stimulation to detect contralateral suppression.
- If bilateral PA: spironolactone 25 mg daily, titrate; MACS then managed medically with comorbidity control.
- Comorbidities: intensify T2DM therapy, DEXA-guided bone protection, statin per ASCVD risk — all plausibly worsened by MACS.

GUIDELINE / THRESHOLDS USED: ESE/ENSAT adrenal incidentaloma (2016, updated 2023) for imaging and DST; Endocrine Society primary aldosteronism guidance for ARR and AVS. ARR cut-offs are assay- and unit-dependent — interpret against the local lab.

PITFALLS TO AVOID:
- Do not stop at "benign adenoma, no follow-up" — the imaging is benign, but the hormones are not.
- Do not skip AVS because the CT shows a unilateral adenoma.
- Do not send a patient with MACS to adrenalectomy without a perioperative steroid plan.
- Do not interpret ARR with uncorrected hypokalemia.
```
