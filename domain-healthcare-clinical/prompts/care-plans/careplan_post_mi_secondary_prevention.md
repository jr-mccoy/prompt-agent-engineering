---
title: "Post-MI Secondary Prevention Care Plan"
category: domain-healthcare-clinical/care-plans
description: "Build the post-myocardial-infarction secondary prevention bundle: antiplatelet duration, statin, beta-blocker, ACEi/ARB, aldosterone antagonist, and risk-factor control with named doses."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
  - DS-02
difficulty: advanced
tags:
  - cardiology
  - secondary-prevention
  - post-mi
  - care-plan
updated: "2026-06-19"
---

## Objective

Produce a post-MI secondary prevention plan: dual antiplatelet therapy selection and duration, high-intensity statin to LDL target, beta-blocker, ACEi/ARB, aldosterone antagonist when indicated, SGLT2i/GLP-1 in diabetes, and structured risk-factor modification plus cardiac rehab. Output is the discharge-and-followup medication bundle with durations.

## Inputs

- Event: STEMI vs NSTEMI, revascularization (PCI with stent type / CABG / medical), LVEF, residual disease
- Bleeding/ischemic risk: prior bleeding, anticoagulation indication (AF, mechanical valve), age, weight, renal function
- Comorbidities: diabetes, CKD, HF, prior stroke, smoking, hypertension, dyslipidemia
- Current meds and allergies; lipid values

## Role

Cardiologist managing post-MI secondary prevention.

## Reasoning Steps

1. **Antiplatelet (DAPT):** aspirin 81 mg indefinitely + a P2Y12 inhibitor.
   - Ticagrelor 90 mg BID or prasugrel 10 mg (prasugrel avoided if prior stroke/TIA, age ≥75, weight <60 kg) preferred over clopidogrel for ACS.
   - **Duration:** 12 months default after ACS; shorten (3–6 months) if high bleeding risk; extend if high ischemic/low bleeding risk.
   - **Triple therapy (DAPT + anticoagulant)** if AF: minimize duration — typically drop aspirin early (1 week) and continue P2Y12 (clopidogrel) + DOAC; full triple only peri-PCI.

2. **High-intensity statin** (atorvastatin 80 / rosuvastatin 40) for all; goal LDL <55 (very-high-risk). Add ezetimibe → PCSK9i to reach goal.

3. **Beta-blocker** (metoprolol succinate, carvedilol, bisoprolol) — strongest benefit with reduced EF or HF; continue ≥1 year (indefinite if HFrEF).

4. **ACEi/ARB** (lisinopril, ramipril) — especially LVEF <40%, HTN, diabetes, CKD; reduces remodeling.

5. **Aldosterone antagonist** (eplerenone/spironolactone) if LVEF ≤40% AND (HF symptoms OR diabetes), K <5.0, eGFR adequate.

6. **SGLT2i / GLP-1 RA** in diabetes for CV benefit; SGLT2i also if HFrEF develops.

7. **Cardiac rehabilitation referral** — class I, mortality benefit.

8. **Risk-factor modification:** smoking cessation (pharmacotherapy), BP <130/80, diabetes control, influenza/COVID vaccination, Mediterranean diet, activity, weight, depression screen.

9. **Monitor:** lipids 4–12 wk, BMP after ACEi/MRA, bleeding on DAPT, LVEF reassessment, adherence (DAPT interruption is high-risk for stent thrombosis).

## Output Format

```
EVENT / REVASC / LVEF:
ISCHEMIC vs BLEEDING RISK:

MEDICATION BUNDLE:
- Aspirin: 81 mg indefinite
- P2Y12: [agent, dose, DURATION + rationale]
- Statin: [agent, dose, LDL goal, add-ons]
- Beta-blocker: [agent, dose]
- ACEi/ARB: [agent, dose]
- Aldosterone antagonist: [if LVEF ≤40 + criteria]
- SGLT2i/GLP-1 if diabetes/HF

ANTICOAGULATION OVERLAP (if AF/valve):
- [triple → dual de-escalation plan]

CARDIAC REHAB: referral

RISK-FACTOR MODIFICATION:
- Smoking, BP, diabetes, vaccines, diet, depression

MONITORING:
- Lipids, BMP, bleeding, LVEF, adherence

PITFALLS:
- [DAPT interruption/stent thrombosis, prasugrel contraindications, triple-therapy bleeding, under-dosed statin]
```

## Worked Example

**Input:** 66 y/o M, STEMI with drug-eluting stent to LAD 3 days ago, LVEF 38%, diabetes, no AF, no prior stroke, weight 82 kg, eGFR 65, K 4.2. LDL 102 (statin-naive). Active smoker.

**Output:**

```
EVENT / REVASC / LVEF: STEMI, DES to LAD, LVEF 38%, diabetic.
ISCHEMIC vs BLEEDING RISK: high ischemic (DES, diabetes, low EF), no major bleeding risk.

MEDICATION BUNDLE:
- Aspirin 81 mg indefinitely.
- P2Y12: ticagrelor 90 mg BID × 12 months (no stroke history, prefers over clopidogrel for STEMI). Reassess duration at 12 mo.
- Statin: atorvastatin 80 mg; LDL goal <55 (very-high-risk). Recheck in 4–6 wk; add ezetimibe → PCSK9i if above goal.
- Beta-blocker: carvedilol 6.25 mg BID, titrate toward 25 BID (LVEF 38 — indefinite).
- ACEi: lisinopril 5 mg, uptitrate (LVEF <40 + diabetes).
- Aldosterone antagonist: LVEF ≤40 + diabetes, K 4.2, eGFR 65 → eplerenone 25 mg daily; recheck K in 1 wk.
- SGLT2i: empagliflozin 10 mg (diabetes + LVEF 38 — dual benefit).

ANTICOAGULATION OVERLAP: none (no AF).

CARDIAC REHAB: refer.

RISK-FACTOR MODIFICATION:
- Smoking cessation: varenicline or NRT + counseling — highest-yield intervention.
- BP <130/80; diabetes optimization; influenza + COVID vaccines; Mediterranean diet; depression screen.

MONITORING:
- Lipids 4–6 wk; BMP after lisinopril + eplerenone; bleeding on ticagrelor (dyspnea is common, usually benign); reassess LVEF in ~40 days–3 mo for ICD candidacy if ≤35%.
- Stress DAPT adherence — interruption risks stent thrombosis.

PITFALLS:
- Do not interrupt DAPT prematurely.
- Recheck K after eplerenone.
- Statin-naive with LDL 102 and very-high-risk → needs aggressive lowering, likely add-on.
```
