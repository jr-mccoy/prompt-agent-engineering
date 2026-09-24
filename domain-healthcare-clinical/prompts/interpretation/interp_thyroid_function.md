---
title: "Thyroid Function Test Interpretation"
category: domain-healthcare-clinical/interpretation
description: "Read TSH, free T4, T3, and thyroid antibodies as a pattern — primary vs central, overt vs subclinical, thyroiditis vs Graves, assay interference, non-thyroidal illness — and commit to diagnosis, dosing, and recheck timing."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: intermediate
tags:
  - endocrinology
  - thyroid
  - hypothyroidism
  - hyperthyroidism
  - interpretation
  - racing-heart
  - tired-and-cold
  - after-giving-birth
updated: "2026-09-24"
related_prompts:
  - domain-healthcare-clinical/prompts/specialty/specialty_thyroid_nodule_workup.md
  - domain-healthcare-clinical/prompts/pathophysiology/patho_endocrine_axis_dysfunction.md
  - domain-healthcare-clinical/prompts/pharmacology/pharm_pregnancy_lactation_drug_safety.md
---

## Objective

Interpret a set of thyroid function tests as a pattern, identify the category (primary, central, subclinical, destructive vs overproduction, interference, non-thyroidal illness), and commit to the confirmatory test, treatment with dose, and recheck interval.

Decision support for a licensed clinician: confirm levothyroxine, antithyroid-drug, and beta-blocker doses, pregnancy-specific ranges, and treatment thresholds against the current guideline and local formulary. A patient with suspected thyroid storm or myxedema coma is escalated now, not after this output.

## When to Use

- A TSH/free T4/T3 result (± antibodies) needs to be read as a pattern and turned into a diagnosis, dose, and recheck interval.
- Results that do not fit the clinical picture — possible assay interference, central disease, non-thyroidal illness, or drug effect.
- Thyroid tests in pregnancy or postpartum, where ranges and treatment choices differ.

**Not this prompt if:**
- The question is a palpable or incidental thyroid nodule — use `domain-healthcare-clinical/prompts/specialty/specialty_thyroid_nodule_workup.md`.
- The task is explaining the hypothalamic–pituitary–thyroid axis mechanism rather than acting on a result — use `domain-healthcare-clinical/prompts/pathophysiology/patho_endocrine_axis_dysfunction.md`.

## Inputs

- TSH, free T4, total or free T3 (with the lab's reference ranges — ranges are assay- and lab-dependent)
- Antibodies if available: TPO Ab, TRAb/TSI, thyroglobulin Ab; thyroglobulin
- Radioactive iodine uptake/scan, thyroid ultrasound if done
- Context: symptoms, goiter/nodules, eye signs, pregnancy or postpartum status (weeks), breastfeeding, acute illness/ICU, age, cardiac disease, osteoporosis
- Medications: levothyroxine dose and timing, amiodarone, lithium, glucocorticoids, dopamine/dobutamine, immune checkpoint inhibitors, tyrosine kinase inhibitors, biotin, iodinated contrast, estrogen
- Prior TFTs

## Role

Senior endocrinology attending supporting the treating clinician; reads the thyroid tests as a pattern and commits to a plan they can verify.

## Reasoning Steps

1. **Check whether TSH can be trusted.** TSH is the best single screen only when the hypothalamic–pituitary axis is intact and the patient is in steady state. It misleads in: central hypothyroidism (TSH low/normal with low FT4), recent treatment of hyperthyroidism (TSH suppressed for weeks to months), non-thyroidal illness, glucocorticoids/dopamine (suppress TSH), first-trimester pregnancy (hCG suppresses TSH; use trimester-specific ranges), and biotin supplements (streptavidin–biotin immunoassays → falsely low TSH and falsely high FT4/T3; hold biotin ≥48 hours and redraw).

   **Stop and escalate now if** features of thyroid storm or myxedema coma are present (step 5) — treat before completing the pattern read.

2. **Pattern table.**
   - **High TSH, low FT4:** overt primary hypothyroidism — Hashimoto (TPO Ab), post-ablation/thyroidectomy, drugs (lithium, amiodarone, checkpoint inhibitors, TKIs), recovery phase of thyroiditis.
   - **High TSH, normal FT4:** subclinical hypothyroidism — repeat in 6–12 weeks before labeling (transient elevations are common). Treat if TSH ≥10, pregnancy or planning pregnancy, or selected symptomatic patients with TSH 4.5–10 (individualize; less benefit in older adults).
   - **Low TSH, high FT4 and/or T3:** overt hyperthyroidism — Graves (TRAb, diffuse increased uptake, orbitopathy), toxic multinodular goiter or toxic adenoma (nodular uptake), thyroiditis (low uptake: painless, postpartum, subacute with tender gland and high ESR, drug-induced), exogenous (low thyroglobulin), iodine-induced, hCG-mediated (hyperemesis, molar pregnancy).
   - **Low TSH, normal FT4 and T3:** subclinical hyperthyroidism — repeat; treat if TSH <0.1 and age ≥65, cardiac disease, AF, or osteoporosis.
   - **Low/normal TSH, low FT4:** central hypothyroidism (pituitary/hypothalamic — check other pituitary axes, morning cortisol before replacing thyroid hormone) vs non-thyroidal illness.
   - **Normal/high TSH with high FT4:** assay interference (biotin, heterophile antibodies), amiodarone, recent levothyroxine loading before the draw, TSH-secreting adenoma, thyroid hormone resistance.
   - **Low T3, normal/low TSH in critical illness:** non-thyroidal illness (euthyroid sick) — do not treat.

3. **Hyperthyroid next step.** TRAb first (positive → Graves, no scan needed). TRAb negative → RAIU/scan (contraindicated in pregnancy; breastfeeding must be interrupted) or Doppler ultrasound. A high T3-to-T4 ratio favors Graves/toxic nodules over destructive thyroiditis.

4. **Treatment anchors.**
   - **Hypothyroidism:** levothyroxine full replacement ~1.6 mcg/kg/day in healthy younger adults; 25–50 mcg/day start in older adults or coronary disease, titrate by 12.5–25 mcg. Recheck TSH 6–8 weeks after any change. Take fasting, separate from calcium, iron, PPIs, bile acid sequestrants. Pregnancy: increase dose ~25–30% at confirmation (e.g., two extra doses per week).
   - **Hyperthyroidism:** beta-blocker for symptoms (propranolol 10–40 mg TID–QID or atenolol 25–50 mg daily). Graves/toxic nodular: methimazole 10–30 mg daily scaled to severity (baseline CBC and LFTs; counsel on agranulocytosis — fever/sore throat → stop and check CBC); PTU in first trimester and thyroid storm. Thyroiditis: beta-blocker only — antithyroid drugs do nothing for destructive release.

5. **Emergencies.** Thyroid storm (fever, tachyarrhythmia, CNS dysfunction, GI/hepatic dysfunction — Burch-Wartofsky score) and myxedema coma (hypothermia, altered mental status, hyponatremia, hypoventilation) are clinical diagnoses — treat without waiting for repeat labs.

6. **Pitfalls before signing.** Single abnormal TSH acted on without repeat; TSH used to titrate in central hypothyroidism (use FT4); thyroid tests sent in ICU patients; biotin; starting levothyroxine in untreated adrenal insufficiency (precipitates crisis); checking T3 to manage hypothyroidism.

## Output Format

```
VALUES: [TSH, FT4, T3 vs lab ranges]
TRUST CHECK: [interference / illness / drugs / pregnancy — present or excluded]
PATTERN: [category from table]
ETIOLOGY (most likely → next): [1., 2.]

ACTION:
- [confirmatory test]
- [treatment with drug and dose]
- [recheck test and interval]
- [long-term monitoring]
```

## Verification

- [ ] Thyroid storm and myxedema coma considered before routine pattern interpretation.
- [ ] Each value compared with the reporting lab's own reference range (trimester-specific in pregnancy), not a remembered range.
- [ ] TSH trustworthiness checked (biotin, illness, drugs, recent treatment, pituitary disease) before the pattern is named.
- [ ] Treatment thresholds and doses attributed to a named guideline and year, and checked against age, cardiac disease, weight, pregnancy, and breastfeeding.
- [ ] Adrenal insufficiency excluded before levothyroxine in suspected central disease.
- [ ] States what would change the diagnosis (repeat TFTs, TRAb, uptake scan, trend over 4–6 weeks).

## False-Positive Prevention

- **Single abnormal TSH labeled as disease:** subclinical results are repeated before diagnosis or treatment.
- **Non-thyroidal illness called hypothyroidism** in hospitalized or ICU patients with low T3 and low/normal TSH.
- **Assay interference read as hyperthyroidism:** biotin or heterophile antibodies giving discordant TSH and FT4.
- **Destructive thyroiditis treated as Graves** with antithyroid drugs because TSH is suppressed.

## Worked Example

**Input:** 31 y/o F, 9 weeks postpartum, exclusively breastfeeding. Three weeks of palpitations, heat intolerance, 3 kg weight loss. Small non-tender goiter, no eye signs, HR 108. TSH <0.01 mIU/L, FT4 3.1 ng/dL (lab reference 0.8–1.8), total T3 175 ng/dL (lab reference 80–200). TRAb negative. ESR 12. TPO Ab strongly positive. No biotin, no iodine exposure, no levothyroxine.

**Output:**

```
VALUES: TSH suppressed, FT4 ~1.7× ULN, T3 within range (T4-predominant).
TRUST CHECK: No biotin, no interfering drugs, not in the hCG-suppression window; clinical picture concordant.
PATTERN: Overt hyperthyroidism, T4-predominant.
ETIOLOGY:
1. Painless postpartum thyroiditis — onset within the first postpartum year, TPO Ab positive, TRAb negative, non-tender gland, normal ESR, T4-predominant (destructive release).
2. Postpartum Graves — less likely with negative TRAb and no orbitopathy; revisit if hyperthyroidism persists beyond ~3 months or worsens.

ACTION:
- No RAIU scan (breastfeeding); Doppler thyroid ultrasound if confirmation needed — low flow supports thyroiditis.
- Propranolol 10–20 mg PO TID–QID titrated to HR <90 (compatible with breastfeeding; watch infant for bradycardia/lethargy).
- No methimazole or PTU — antithyroid drugs do not treat destructive thyroiditis.
- TSH and FT4 every 4–6 weeks: expect a hypothyroid phase at ~3–6 months postpartum. Start levothyroxine (e.g., 50 mcg daily, titrate) if TSH >10, if hypothyroid symptoms are present, or if she is planning another pregnancy.
- Taper propranolol as FT4 normalizes.
- Long term: TSH annually — TPO-positive women carry substantial risk of permanent hypothyroidism; check TSH before and early in any future pregnancy.
```
