---
title: "Hepatitis C Treatment Care Plan"
category: domain-healthcare-clinical/care-plans
description: "Build a hepatitis C direct-acting antiviral treatment plan: pretreatment assessment, pangenotypic regimen selection, cirrhosis and HBV considerations, and SVR confirmation with named regimens."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
  - DS-02
difficulty: advanced
tags:
  - infectious-disease
  - hepatitis-c
  - antiviral
  - care-plan
updated: "2026-10-06"
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
> **Review status:** AI-assisted content, reviewed by AI only (2026-10-06);
> **not yet reviewed by a licensed clinician.**

## Objective

Produce a hepatitis C treatment plan with direct-acting antivirals: complete pretreatment assessment, stage fibrosis, select a pangenotypic regimen and duration, manage cirrhosis/HBV/drug-interaction considerations, and confirm cure (SVR12). Output is a treatment + monitoring plan.

## Inputs

- Virology: HCV RNA (confirm viremia), genotype (often unnecessary with pangenotypic regimens)
- Fibrosis stage: APRI/FIB-4, elastography, or clinical cirrhosis; compensated (Child-Pugh A) vs decompensated (B/C)
- Co-infections: HBV (HBsAg, anti-HBc), HIV, prior HCV treatment (treatment-naive vs experienced)
- Labs: CBC, CMP (renal/hepatic), pregnancy; concomitant meds (interactions)
- Substance use, reinfection risk, adherence

## Role

Hepatologist or infectious-disease attending treating hepatitis C.

## Reasoning Steps

1. **Confirm active infection** (HCV RNA positive). Nearly all patients should be treated regardless of fibrosis stage.

2. **Pretreatment assessment:**
   - Stage fibrosis (FIB-4/APRI + elastography) — determines duration and whether cirrhosis precautions apply.
   - **Screen HBV (HBsAg + anti-HBc): HBV reactivation can occur during DAA therapy** — manage/monitor or treat HBV concurrently.
   - HIV co-infection, prior treatment history, pregnancy, drug interactions (PPIs, statins, anticonvulsants, amiodarone with sofosbuvir).
   - Assess decompensation — protease-inhibitor-containing regimens (glecaprevir, voxilaprevir) are **contraindicated in decompensated cirrhosis (Child-Pugh B/C)**.

3. **Select a pangenotypic regimen:**
   - **Glecaprevir/pibrentasvir** 8 weeks (treatment-naive without cirrhosis or compensated cirrhosis) — avoid in decompensated cirrhosis.
   - **Sofosbuvir/velpatasvir** 12 weeks (naive, with or without compensated cirrhosis; for decompensated cirrhosis use sofosbuvir/velpatasvir + ribavirin, no protease inhibitor).
   - Treatment-experienced/NS5A failures: sofosbuvir/velpatasvir/voxilaprevir (compensated only).
   - Simplified treatment algorithms apply for treatment-naive without cirrhosis.

4. **Cirrhosis:** even after cure, **continue HCC surveillance (US ± AFP q6 months)** in cirrhotics — SVR reduces but does not eliminate HCC risk. Continue variceal surveillance.

5. **Drug interactions:** review carefully (acid suppression affects some regimens, statins, anticonvulsants, amiodarone + sofosbuvir bradycardia risk).

6. **Adherence & reinfection:** counsel completion; harm reduction and reinfection prevention for ongoing risk (PWID — treatment still indicated; offer syringe services, repeat RNA for reinfection).

7. **Confirm cure:** HCV RNA at 12 weeks after treatment completion = **SVR12 (cure)**. Check RNA for reinfection if ongoing risk.

8. **Monitor:** on-treatment clinical check; HBV reactivation monitoring; SVR12; post-cure cirrhosis surveillance.

## False-Positive Prevention

❌ **DON'T:**
- Write "compensated cirrhosis" without recomputing Child-Pugh — protease-inhibitor eligibility turns on it, and a low albumin or a past ascites episode can move a patient to class B.
- Treat FIB-4 or APRI as staging outside their validated range — FIB-4 is unreliable at younger and older ages, and both need same-day AST, ALT and platelets.
- Read "pangenotypic" as "no genotype caveats" — genotype 3 with cirrhosis or prior treatment failure can still change resistance testing, duration or ribavirin use `[VERIFY: AASLD-IDSA HCV guidance]`.
- Conflate HBV states: HBsAg-positive patients may need HBV therapy alongside the DAA, while isolated anti-HBc needs ALT/HBV-DNA monitoring — the plan must say which applies.
- Limit the interaction review to drugs named in the prompt; run it on the full list, including OTC acid suppressants and supplements such as St John's wort.

✅ **DO:**
- Recompute FIB-4 as (age × AST) / (platelets × √ALT) and APRI from AST and the reporting lab's upper limit of normal, showing both.
- Check each concomitant drug in an HCV interaction resource and record the result drug by drug `[VERIFY: Liverpool HEP Drug Interactions or label]`.
- Date SVR12 from the end-of-treatment date, not the start date, and note the assay's lower limit of quantitation.
- Before sign-off, check pregnancy status, renal function and age (paediatric dosing is weight-banded) against the chosen regimen's label.

## Output Format

```
CONFIRMATION (HCV RNA) / GENOTYPE:
FIBROSIS STAGE (compensated vs decompensated):
HBV / HIV / PRIOR TREATMENT / INTERACTIONS:

REGIMEN:
- [pangenotypic DAA, duration + rationale]
- Cirrhosis/decompensation adjustment (no PI if Child-Pugh B/C)
- HBV co-management

DRUG-INTERACTION REVIEW:

CURE CONFIRMATION:
- SVR12 (RNA 12 wk post-treatment)

POST-CURE:
- HCC/variceal surveillance if cirrhotic; reinfection monitoring

MONITORING:
- On-treatment, HBV reactivation, SVR12

PITFALLS:
- [protease inhibitor in decompensated cirrhosis, missed HBV reactivation, stopping HCC surveillance after cure, drug interactions]
```

## Worked Example

**Input:** 48 y/o M, chronic HCV, HCV RNA positive, genotype 1a. FIB-4 and elastography → compensated cirrhosis (Child-Pugh A). HBsAg negative, anti-HBc positive (resolved/occult), HIV negative, treatment-naive. On a PPI for reflux. No amiodarone.

**Output:**

```
CONFIRMATION / GENOTYPE: HCV RNA positive, genotype 1a (pangenotypic regimen makes genotype largely moot).
FIBROSIS STAGE: compensated cirrhosis (Child-Pugh A).
HBV / HIV / PRIOR TX: HBsAg negative / anti-HBc positive (monitor for reactivation), HIV negative, treatment-naive. On PPI.

REGIMEN:
- Sofosbuvir/velpatasvir 12 weeks (naive, compensated cirrhosis) — clean choice.
  - Glecaprevir/pibrentasvir 8 weeks also acceptable for compensated cirrhosis (treatment-naive) — but note protease inhibitor; either works here since compensated.
- Both avoid the decompensated-cirrhosis contraindication (not applicable — Child-Pugh A).

DRUG-INTERACTION REVIEW:
- PPI: velpatasvir absorption is pH-dependent — separate/limit PPI and take with food per labeling, or manage acid suppression; review interaction explicitly.

HBV CO-MANAGEMENT:
- anti-HBc positive, HBsAg negative → risk of HBV reactivation during DAA; monitor ALT (and HBV DNA/HBsAg if ALT rises) during and after treatment.

CURE CONFIRMATION:
- HCV RNA at 12 weeks post-treatment = SVR12 (cure).

POST-CURE:
- Cirrhotic → CONTINUE HCC surveillance (ultrasound ± AFP q6 months) indefinitely despite cure, plus variceal surveillance per protocol.

MONITORING:
- On-treatment clinical/adherence check, HBV reactivation (ALT), SVR12 confirmation.

PITFALLS:
- Don't stop HCC surveillance after cure in a cirrhotic.
- Manage the PPI interaction with velpatasvir.
- Watch for HBV reactivation given anti-HBc positivity.
```
