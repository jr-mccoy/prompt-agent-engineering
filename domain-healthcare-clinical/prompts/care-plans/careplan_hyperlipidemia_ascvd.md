---
title: "Dyslipidemia / ASCVD Risk Reduction Care Plan"
category: domain-healthcare-clinical/care-plans
description: "Build a lipid-lowering plan by ASCVD risk tier: statin intensity, LDL thresholds, non-statin add-ons, and monitoring with named drugs and target LDL goals."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
  - DS-02
difficulty: intermediate
tags:
  - cardiology
  - lipids
  - prevention
  - care-plan
updated: "2026-06-19"
---

## Objective

Produce a dyslipidemia management plan: assign the ASCVD risk tier, set the LDL goal/threshold, choose statin intensity, sequence non-statin add-ons when thresholds aren't met, and define monitoring. Output is a tiered lipid plan to an LDL target.

## Inputs

- Lipids: LDL-C, HDL, triglycerides, non-HDL, Lp(a) if available; on/off treatment
- Risk status: clinical ASCVD (and whether very-high-risk), diabetes, age, 10-year pooled-cohort risk, FH features, CKD
- Patient: prior statin intolerance, drug interactions, pregnancy plans, liver disease
- Current regimen: statin/dose, ezetimibe, PCSK9i, adherence

## Role

Cardiologist or primary care attending managing lipids for ASCVD prevention.

## Reasoning Steps

1. **Assign tier:**
   - **Secondary prevention, very-high-risk** (recent ACS, multiple events, or event + high-risk conditions): goal LDL <55 (and <70 at minimum), high-intensity statin + add-ons.
   - **Secondary prevention, stable:** high-intensity statin, LDL <70.
   - **Diabetes age 40–75:** at least moderate-intensity; high-intensity if multiple risk factors or 10-yr risk ≥20%; LDL <70 reasonable.
   - **Primary prevention, LDL ≥190 (likely FH):** high-intensity statin, goal ≥50% reduction and LDL <100 (<70 if other risk).
   - **Primary prevention age 40–75, 10-yr risk:** ≥20% high-intensity; 7.5–20% moderate (use CAC if uncertain — CAC 0 may defer).

2. **Statin intensity:**
   - High: atorvastatin 40–80 mg, rosuvastatin 20–40 mg (≥50% LDL reduction).
   - Moderate: atorvastatin 10–20, rosuvastatin 5–10, simvastatin 20–40 (30–49% reduction).

3. **Recheck lipids 4–12 weeks** after start/change; assess adherence and % reduction.

4. **Add-ons if LDL above threshold on max-tolerated statin:**
   - **Ezetimibe 10 mg** first (additional ~20% LDL).
   - **PCSK9i** (evolocumab/alirocumab) if still above goal in very-high-risk (additional ~50–60%).
   - **Bempedoic acid** if statin-intolerant or adjunct; **inclisiran** as PCSK9-targeting siRNA alternative.

5. **Triglycerides:** if ≥500, fibrate/omega-3 to prevent pancreatitis first. If ASCVD/diabetes with TG 150–499 on statin and LDL controlled → icosapent ethyl 2 g BID (REDUCE-IT).

6. **Statin intolerance:** confirm true intolerance (rechallenge, alternate statin, low-dose/alternate-day rosuvastatin); rule out hypothyroidism, drug interactions. Reserve "intolerant" label for genuine recurrent symptoms.

7. **Lp(a):** measure once; if elevated, intensify LDL lowering and risk-factor control (no approved Lp(a)-specific therapy yet outside trials).

8. **Monitor:** lipid panel per above; baseline ALT; check for myopathy symptoms (routine CK not needed unless symptomatic); avoid in pregnancy.

## Output Format

```
RISK TIER: [tier + rationale]
LDL GOAL / THRESHOLD:
CURRENT LDL / % REDUCTION ACHIEVED:

LIPID PLAN:
- Statin: [agent, intensity, dose]
- Add-on(s) if above threshold: [ezetimibe → PCSK9i / bempedoic / inclisiran]
- TG management if applicable: [icosapent ethyl / fibrate]

MONITORING:
- Lipid recheck 4–12 wk; ALT baseline; myopathy counseling

OTHER:
- Lp(a), lifestyle, statin-intolerance handling

PITFALLS:
- [under-treating very-high-risk, mislabeling intolerance, statin in pregnancy, fibrate-statin myopathy]
```

## Worked Example

**Input:** 61 y/o M, NSTEMI 8 months ago with PCI, plus diabetes (very-high-risk). LDL 88 on atorvastatin 40 mg, adherent. ALT normal, no muscle symptoms. TG 180.

**Output:**

```
RISK TIER: Secondary prevention, VERY-HIGH-RISK (recent ACS + diabetes).
LDL GOAL / THRESHOLD: <55.
CURRENT LDL / % REDUCTION: 88 — above threshold.

LIPID PLAN:
- Statin: uptitrate atorvastatin 40 → 80 mg (max high-intensity).
- Recheck LDL in 4–6 wk. If still ≥55: add ezetimibe 10 mg daily.
- If LDL still ≥55 on atorvastatin 80 + ezetimibe → PCSK9i (evolocumab 140 mg q2wk or alirocumab).
- TG 180 with LDL not yet controlled: defer icosapent ethyl until LDL at goal; then consider icosapent ethyl 2 g BID for residual ASCVD risk (REDUCE-IT — diabetes + ASCVD + TG 150–499).

MONITORING:
- Lipid panel 4–6 wk after each change.
- ALT normal; no routine CK; counsel to report muscle symptoms.

OTHER:
- Check Lp(a) once if never done.
- Reinforce adherence, diet, activity, smoking status.

PITFALLS:
- Very-high-risk needs LDL <55 — 88 is undertreated; escalate aggressively.
- Add ezetimibe/PCSK9i rather than stopping at high-intensity statin if threshold unmet.
- Hold lipid drugs in pregnancy (not relevant here).
```
