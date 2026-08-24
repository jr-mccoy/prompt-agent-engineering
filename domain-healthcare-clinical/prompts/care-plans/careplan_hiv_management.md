---
title: "HIV Longitudinal Management Care Plan"
category: domain-healthcare-clinical/care-plans
description: "Build an HIV care plan: ART initiation and regimen selection, viral-load/CD4 monitoring, OI prophylaxis, comorbidity and prevention bundle with named regimens and doses."
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
  - hiv
  - antiretroviral
  - care-plan
updated: "2026-06-19"
---

## Objective

Produce a longitudinal HIV care plan: initiate antiretroviral therapy promptly, select a regimen by baseline data and comorbidity, set viral-load/CD4 monitoring, provide opportunistic-infection prophylaxis when indicated, and install the comorbidity/prevention/vaccination bundle. Output is a regimen + monitoring + prevention plan.

## Inputs

- Diagnosis/staging: confirmatory testing, baseline CD4 count, HIV RNA (viral load), HIV genotype/resistance, HLA-B*5701 status
- Co-infections: hepatitis B/C, latent/active TB, STIs, baseline opportunistic infections
- Labs: CMP/renal, lipids, A1c, urinalysis, pregnancy status, bone risk
- Comorbidities, concomitant meds (interactions), prior ART, adherence barriers
- Prevention context (partners, PrEP for contacts)

## Role

HIV/infectious-disease specialist managing longitudinal HIV care.

## Reasoning Steps

1. **Start ART promptly — for everyone, regardless of CD4** (rapid/same-day start is supported once baseline labs drawn; don't wait for results to begin a robust regimen). Treatment is prevention (U=U: undetectable = untransmittable).

2. **Baseline before/at start:** CD4, viral load, genotype resistance, HBV/HCV serologies, HLA-B*5701 (if considering abacavir), renal function, pregnancy test, TB screen, STI screen.

3. **First-line regimen — INSTI-based** (high barrier, well-tolerated):
   - Bictegravir/tenofovir alafenamide/emtricitabine (single tablet), or
   - Dolutegravir + (tenofovir/emtricitabine or abacavir/lamivudine if HLA-B*5701 negative), or dolutegravir/lamivudine 2-drug (if no resistance, HBV-negative, VL <500k).
   - **Coordinate with HBV:** if HBV co-infected, include tenofovir + emtricitabine/lamivudine (treats both); don't use HIV regimens that leave HBV untreated or risk HBV flare on withdrawal.
   - **Pregnancy:** preferred regimens per current guidance (e.g., dolutegravir-based now supported).

4. **Adherence support** — the determinant of success; address barriers, consider long-acting injectable cabotegravir/rilpivirine for suppressed patients with adherence challenges.

5. **OI prophylaxis by CD4:**
   - CD4 <200: TMP-SMX for PCP (also covers toxo at <100).
   - CD4 <50: consider azithromycin for MAC (less emphasized with prompt ART); evaluate.
   - Screen/treat latent TB; screen CMV/cryptococcal per CD4 and symptoms.
   - Discontinue prophylaxis after immune reconstitution (sustained CD4 recovery).

6. **Monitoring:**
   - Viral load at baseline, ~4–8 weeks after start, then until suppressed (<50); every 3–6 months, q6 months when stable.
   - CD4 periodically until reconstituted, then can space out.
   - Renal (tenofovir), lipids/weight/glucose (INSTI/TAF weight gain), bone, repeat resistance if virologic failure.

7. **Comorbidity & prevention bundle:** vaccinations (hepatitis A/B, pneumococcal, influenza, HPV, COVID, others per CD4), cervical/anal cancer screening, cardiovascular risk (statin), STI screening, contraception/reproductive planning, mental health/substance use, PrEP for partners.

8. **Manage drug interactions** (INSTI + polyvalent cations, rifamycins, acid suppression with rilpivirine, etc.).

## Output Format

```
BASELINE: CD4 / viral load / genotype / HBV-HCV-TB / HLA-B*5701 / pregnancy

ART REGIMEN:
- Regimen: [INSTI-based single tablet + rationale]
- HBV coordination / pregnancy adjustments
- Adherence support / LAI consideration

OI PROPHYLAXIS (by CD4):
- PCP/toxo/MAC/TB as indicated + discontinuation criteria

MONITORING:
- VL/CD4 schedule; renal/metabolic/bone; resistance if failure

PREVENTION / COMORBIDITY BUNDLE:
- Vaccines, cancer screening, CV risk, STI, reproductive, mental health, partner PrEP

PITFALLS:
- [HBV flare risk, drug interactions, delaying ART, stopping prophylaxis prematurely, missing resistance]
```

## Worked Example

**Input:** 32 y/o M, new HIV diagnosis. CD4 180, viral load 240,000. HBsAg positive (HBV co-infected), HCV negative, latent TB negative, HLA-B*5701 not yet back. Renal normal, not on other meds.

**Output:**

```
BASELINE: CD4 180 (PCP prophylaxis threshold), VL 240k, HBV co-infected, TB negative, HLA-B*5701 pending. Genotype sent.

ART REGIMEN:
- Start promptly: bictegravir/tenofovir alafenamide/emtricitabine single tablet daily.
  - Rationale: INSTI single-tablet, high barrier; TAF/FTC treats HBV co-infection simultaneously — essential here.
  - Avoid a 2-drug DTG/3TC regimen here: HBV-positive and VL >500k both make it inappropriate.
- Do not interrupt the tenofovir/emtricitabine backbone without HBV plan (withdrawal → HBV flare).
- Adherence counseling at start; same-day/rapid start appropriate.

OI PROPHYLAXIS:
- CD4 180 <200 → start TMP-SMX for PCP prophylaxis. Discontinue once CD4 >200 sustained ≥3 months on ART.
- Not <50, so no MAC prophylaxis; latent TB negative.

MONITORING:
- Viral load at 4–8 weeks, then until <50; CD4 periodically.
- Renal function (tenofovir), weight/lipids/glucose (INSTI/TAF), HBV DNA.
- Resistance testing if virologic failure.

PREVENTION / COMORBIDITY BUNDLE:
- Vaccines: hepatitis A (HBV already infected), pneumococcal, influenza, HPV, COVID; per CD4 timing.
- STI screening, reproductive/contraception discussion, CV risk/statin assessment, mental health/substance screen.
- Partner services + PrEP for HIV-negative partners; counsel U=U once suppressed.

PITFALLS:
- HBV co-infection mandates a tenofovir-containing regimen — and don't stop it abruptly (flare).
- Confirm HLA-B*5701 before any abacavir option (not used here).
- Start PCP prophylaxis now (CD4 180).
```
