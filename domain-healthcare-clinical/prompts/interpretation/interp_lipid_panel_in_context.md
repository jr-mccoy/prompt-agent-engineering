---
title: "Lipid Panel Interpretation in Clinical Context"
category: domain-healthcare-clinical/interpretation
description: "Read a lipid panel for what the numbers actually mean — LDL calculation validity, non-HDL/apoB, familial phenotypes, triglyceride severity, Lp(a), secondary causes, on-treatment response — before any lipid-lowering plan is built."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: intermediate
tags:
  - cardiology
  - lipids
  - preventive-medicine
  - familial-hypercholesterolemia
  - interpretation
  - high-cholesterol
  - family-heart-disease
  - very-high-triglycerides
updated: "2026-09-24"
related_prompts:
  - domain-healthcare-clinical/prompts/care-plans/careplan_hyperlipidemia_ascvd.md
  - domain-healthcare-clinical/prompts/interpretation/interp_thyroid_function.md
  - domain-healthcare-clinical/prompts/specialty/specialty_pancreatitis_severity_management.md
---

> **Medical disclaimer — read before use.** This prompt is a decision-support and
> teaching aid for **licensed clinicians**. It is **not medical advice** and is not for
> patients to diagnose or treat themselves. Drug doses, thresholds and guideline
> references in it and in its worked example may be incomplete, outdated or wrong:
> verify each one against the current guideline, the product label and your local
> formulary, and follow your institution's protocols. It does not replace examination
> or clinical judgment. **Medical emergency: call your local emergency number (911 in
> the US).**
>
> **Review status:** clinical content and doses reviewed by AI only (2026-09-24);
> **not yet reviewed by a licensed clinician.**

## Objective

Interpret a lipid panel in clinical context: decide whether the reported LDL is trustworthy, identify the phenotype (polygenic, familial hypercholesterolemia, hypertriglyceridemia, mixed, secondary), screen for secondary causes, read on-treatment response, and hand a clean phenotype and risk frame to the treatment plan.

Decision support for a licensed clinician: confirm drug doses, renal/hepatic adjustment and treatment thresholds against the current guideline and local formulary. Very high triglycerides with abdominal pain, or a child with xanthomas or suspected homozygous FH, is escalated now, not after this output.

## When to Use

- A lipid panel is back and the question is whether the LDL is trustworthy and which phenotype it shows.
- Very high LDL, xanthomas, or premature family ASCVD raise familial hypercholesterolemia.
- High triglycerides need a severity grade and a secondary-cause screen.
- On-treatment response must be judged before therapy is intensified.

**Not this prompt if:**

- The phenotype is settled and the lipid-lowering regimen is being built by ASCVD risk tier → `domain-healthcare-clinical/prompts/care-plans/careplan_hyperlipidemia_ascvd.md`, which builds the regimen; this prompt reads the panel that plan depends on.
- Secondary prevention after MI is being planned as a whole → `domain-healthcare-clinical/prompts/care-plans/careplan_post_mi_secondary_prevention.md`.

## Inputs

- Total cholesterol, HDL-C, triglycerides, LDL-C (and method: Friedewald, Martin-Hopkins, Sampson/NIH, direct), non-HDL-C
- ApoB, Lp(a) (with units: mg/dL vs nmol/L) if available
- Fasting status; acute illness at time of draw
- Current lipid therapy, dose, adherence, baseline pre-treatment values
- Context: age, sex, ASCVD history, diabetes, CKD, family history (premature ASCVD, known FH), xanthomas/xanthelasma/corneal arcus <45, BMI, alcohol, medications (steroids, antiretrovirals, antipsychotics, retinoids, estrogen, cyclosporine, thiazides)
- TSH, A1c/glucose, creatinine, urine protein, ALP/bilirubin

## Role

Senior preventive cardiology or lipid clinic attending supporting the treating clinician.

## Reasoning Steps

1. **Stop and escalate first if:** TG ≥1,000 mg/dL (≈11.3 mmol/L) — pancreatitis risk: TG lowering becomes urgent, and abdominal pain at this level needs assessment for acute pancreatitis now; or a child with xanthomas or suspected homozygous FH → specialist lipid referral now (suspected heterozygous FH in a child → routine specialist referral). Then **is the LDL real?** Friedewald (LDL = TC − HDL − TG/5, mg/dL) is invalid when TG ≥400 and underestimates LDL when LDL is low (<70) and TG 150–400. Prefer Martin-Hopkins or Sampson/NIH calculation or direct LDL in those settings. Non-fasting samples are acceptable for most screening; repeat fasting if TG ≥400.

2. **Non-HDL-C and apoB.** Non-HDL-C = TC − HDL-C, captures all atherogenic lipoproteins and is valid non-fasting. ApoB is the better particle-number marker when TG is high, in diabetes/metabolic syndrome, or when LDL and non-HDL disagree; apoB ≥130 mg/dL is a risk enhancer.

3. **Severe hypercholesterolemia.** LDL ≥190 mg/dL → treat as primary severe hypercholesterolemia and evaluate for FH: Dutch Lipid Clinic Network score (LDL level, tendon xanthoma, arcus <45, personal/family premature ASCVD, family LDL), genetic testing (LDLR, APOB, PCSK9), cascade screening of first-degree relatives including children.

4. **Triglycerides.** 175–499 mg/dL moderate (AHA/ACC 2018 definition) — lifestyle, secondary causes, ASCVD risk. ≥500 severe; ≥1,000 substantially raises pancreatitis risk → TG lowering becomes the priority (fibrate, omega-3 prescription, strict alcohol and simple-carbohydrate restriction, glycemic control). Persistent ≥1,000 from childhood or refractory → familial chylomicronemia syndrome.

5. **HDL.** Low HDL (<40 men, <50 women) is a metabolic-syndrome marker, not a treatment target. Very high HDL (>100) is not reliably protective.

6. **Lp(a).** Measure once in adulthood. ≥50 mg/dL (≈≥125 nmol/L) is a risk enhancer; mg/dL and nmol/L are not interconvertible by a fixed factor — report the unit. Not lowered meaningfully by statins.

7. **Secondary causes — rule out before labeling primary.** Hypothyroidism (TSH — also raises statin myopathy risk), nephrotic syndrome (urine protein), cholestasis (ALP/bilirubin — lipoprotein X produces very high cholesterol that statins do not lower), uncontrolled diabetes, alcohol, obesity, anorexia, pregnancy, drugs listed above.

8. **On-treatment reading.** Percent LDL reduction from baseline: high-intensity statin ≈ ≥50%, moderate ≈ 30–49%. Less than expected → adherence, dose timing, secondary cause, or true hypo-response. Add-on thresholds differ by guideline (e.g., US, 2018 AHA/ACC cholesterol guideline: LDL ≥70 mg/dL in very high-risk ASCVD — verify whether a newer ACC/AHA dyslipidemia guideline supersedes 2018; European, 2019 ESC/EAS: goal <55 mg/dL) — name the one being applied.

9. **Pitfalls before signing.** Lipids drawn during acute MI or acute illness fall — recheck 4–12 weeks later. Friedewald LDL in hypertriglyceridemia. Lp(a) unit confusion. Treating an isolated low HDL. Missing FH because the patient is "young and healthy."

## Output Format

```
LDL VALIDITY: [method, valid Y/N, recalculated value if needed]
NON-HDL-C / APOB: [values, discordance]
PHENOTYPE: [polygenic / probable-definite FH (DLCN score) / hypertriglyceridemia (severity) / mixed / secondary]
LP(A): [value + unit, risk enhancer Y/N, or "not measured — order"]
SECONDARY CAUSES: [screened / found]
ON-TREATMENT RESPONSE: [% reduction, adequate Y/N] (if applicable)

INTERPRETATION: [one line]

ACTION:
- [secondary-cause tests]
- [therapy start/adjust with drug and dose]
- [family screening / genetic testing]
- [recheck interval]
- Hand-off: [risk tier for care plan]
```

## Verification

- [ ] LDL method named and its validity checked against TG and LDL level before any threshold is applied.
- [ ] Red flags (TG ≥1,000 mg/dL, pediatric FH or xanthomas) addressed before routine interpretation.
- [ ] Every threshold attributed to a named guideline and year (e.g., AHA/ACC 2018 cholesterol guideline; ESC/EAS 2019), with a check for a newer version.
- [ ] Secondary causes screened, citing the actual TSH, urine protein, ALP/bilirubin, and A1c values from the input.
- [ ] FH scoring shows each Dutch Lipid Clinic Network component and its points traced to the input.
- [ ] Drug doses checked against renal and hepatic function and interacting medications.

## False-Positive Prevention

- **FH called on LDL alone before secondary causes are excluded.** Hypothyroidism, nephrotic syndrome, and cholestasis can produce LDL ≥190 mg/dL.
- **DLCN points over-counted.** Corneal arcus scores only before age 45, and a single relative's history should not be scored twice.
- **High Lp(a) mistaken for FH.** Reported LDL-C includes Lp(a) cholesterol, so a very high Lp(a) inflates LDL-C and can mimic an FH phenotype.
- **A single non-fasting triglyceride in the moderate range labeled as needing drug therapy.** Non-fasting TG runs modestly higher; repeat and address secondary causes and lifestyle first.

## Worked Example

**Input:** 44 y/o M, no known ASCVD, non-smoker, BP 128/80, BMI 26. Father had MI at 48; paternal aunt "high cholesterol." Exam: bilateral Achilles tendon thickening. Non-fasting panel: TC 342, HDL 42, TG 180, LDL (Friedewald) 264 mg/dL. TSH 1.8, A1c 5.4%, Cr 0.9, UA protein negative, ALP 78, bilirubin normal. No lipid therapy ever. Lp(a) not measured.

**Output:**

```
LDL VALIDITY: Friedewald valid (TG 180, LDL far above 70). LDL 264 mg/dL.
NON-HDL-C / APOB: Non-HDL 300 mg/dL; apoB not needed to classify — concordant.
PHENOTYPE: Definite FH by Dutch Lipid Clinic Network — LDL 250–329 (5) + tendon xanthoma (6) + first-degree relative with premature coronary disease (1) = 12 (>8 = definite).
LP(A): Not measured — order now (compounds FH risk).
SECONDARY CAUSES: Thyroid, renal, hepatic/cholestatic, glycemic screens negative.
ON-TREATMENT RESPONSE: N/A (untreated).

INTERPRETATION: Heterozygous familial hypercholesterolemia phenotype, untreated, LDL 264; primary severe hypercholesterolemia — risk calculators do not apply.

ACTION:
- Start high-intensity statin: rosuvastatin 20 mg daily, titrate to 40 mg at 6 weeks if tolerated.
- Recheck lipids 4–12 weeks after start; expect ≥50% LDL reduction. If LDL remains ≥100 mg/dL on maximally tolerated statin, add ezetimibe 10 mg daily; if still ≥100, PCSK9 monoclonal antibody (evolocumab 140 mg SC q2 weeks or alirocumab 75–150 mg SC q2 weeks).
- Baseline ALT; CK only if symptoms.
- Genetic testing (LDLR, APOB, PCSK9 panel) — confirms diagnosis and enables cascade testing.
- Cascade screening: lipid panels for all first-degree relatives, including his children (FH screening from age 2).
- Lp(a) once.
- Hand-off to careplan_hyperlipidemia_ascvd: risk tier = LDL ≥190 / FH, primary prevention; consider coronary calcium score only if it would change intensity (it should not here).
```
