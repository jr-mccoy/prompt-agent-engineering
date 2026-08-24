---
title: "HFrEF Guideline-Directed Medical Therapy Plan"
category: domain-healthcare-clinical/care-plans
description: "Build and titrate four-pillar GDMT for heart failure with reduced ejection fraction with named target doses, sequencing, monitoring, and device referral triggers."
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
  - heart-failure
  - gdmt
  - care-plan
updated: "2026-06-19"
---

## Objective

Produce a HFrEF (LVEF ≤40%) care plan that initiates and titrates the four GDMT pillars to target doses, sequences them safely, sets monitoring cadence, and identifies device and advanced-therapy referral triggers. Output is a titration roadmap to target doses over weeks.

## Inputs

- Cardiac: LVEF, etiology (ischemic vs non-ischemic), NYHA class, NT-proBNP, recent decompensation
- Vitals/labs: BP, HR, K, eGFR/creatinine, volume status
- Current regimen: each pillar, dose, tolerability
- Comorbidities: AF, CKD, diabetes, COPD/asthma, gout, hyperkalemia history
- Device status: QRS width/morphology, prior ICD/CRT, time since diagnosis

## Role

Cardiologist or HF specialist managing GDMT, writing the titration plan for the team.

## Reasoning Steps

1. **Four pillars — start all early, even at low doses, then up-titrate.** Survival benefit is from the combination; do not max one before starting the next.
   - **ARNI** (sacubitril/valsartan) preferred over ACEi/ARB: start 49/51 mg BID (24/26 mg if low BP, prior low-dose ACEi, or ARNI-naive), target 97/103 mg BID. 36-hour washout from ACEi.
   - **Beta-blocker** proven in HF: carvedilol 3.125 mg BID (target 25 mg BID, 50 mg BID if >85 kg), metoprolol succinate 12.5–25 mg daily (target 200 mg), or bisoprolol (target 10 mg). Start when euvolemic; do not start during acute decompensation.
   - **MRA** spironolactone 12.5–25 mg daily (target 25–50) or eplerenone; only if K <5.0 and eGFR >30.
   - **SGLT2i** dapagliflozin or empagliflozin 10 mg daily — no titration, benefit regardless of diabetes.

2. **Sequence by phenotype.** If BP/HR permit, start ARNI + beta-blocker + SGLT2i early; add MRA. In low BP, prioritize ARNI/beta-blocker at low dose + SGLT2i (minimal BP effect). In bradycardia, start ARNI/MRA/SGLT2i first.

3. **Up-titrate every 2 weeks** as BP, HR, K, renal function allow. Double doses toward target.

4. **Monitor:** BMP 1–2 weeks after ARNI/MRA start or change (K, creatinine); BP and HR each visit; weight/symptoms. Tolerate eGFR dip up to ~30% and K up to 5.5 with management.

5. **Diuretics** (furosemide/torsemide/bumetanide) for congestion — symptom control, not survival; use lowest dose maintaining euvolemia.

6. **Device referral:**
   - **ICD** for primary prevention if LVEF ≤35% after ≥3 months optimal GDMT (and ≥40 days post-MI), life expectancy >1 year.
   - **CRT** if LVEF ≤35%, sinus rhythm, LBBB with QRS ≥150 ms (consider 120–149).
   - Reassess LVEF after 3 months GDMT before committing to device.

7. **Advanced therapy referral** (LVAD/transplant eval) for persistent NYHA III–IV, recurrent hospitalizations, inotrope dependence, escalating diuretics — INTERMACS thinking.

8. **Comorbidity coordination:** treat iron deficiency (IV ferric carboxymaltose if ferritin <100 or 100–300 with TSAT <20%), manage AF rate/rhythm and anticoagulation, avoid NSAIDs/most CCBs/thiazolidinediones.

## Output Format

```
LVEF / NYHA / ETIOLOGY:
GDMT TARGET: four pillars to target dose

PILLAR PLAN (each: current → next step → target):
- ARNI: [dose → titration → target] (or ACEi/ARB + reason)
- Beta-blocker: [agent, dose → target]
- MRA: [agent, dose → target] (K/eGFR gate)
- SGLT2i: [agent, dose]

DIURETIC: [agent, dose for euvolemia]

TITRATION SCHEDULE: [q2 week up-titration plan]

MONITORING:
- BMP timing after ARNI/MRA
- BP/HR/weight cadence
- eGFR/K tolerance thresholds

DEVICE / ADVANCED THERAPY:
- ICD/CRT criteria + reassessment timing
- Advanced referral triggers

COMORBIDITY:
- Iron, AF, avoid-list

PITFALLS:
- [washout, decompensation BB timing, hyperK, drugs to avoid]
```

## Worked Example

**Input:** 64 y/o M, non-ischemic cardiomyopathy, LVEF 28%, NYHA II, QRS 110 narrow, NT-proBNP 1800. BP 118/72, HR 78, K 4.4, eGFR 58. Current: lisinopril 10 mg, furosemide 40 mg. No ICD. Euvolemic.

**Output:**

```
LVEF / NYHA / ETIOLOGY: 28%, NYHA II, non-ischemic.
GDMT TARGET: all four pillars to target dose over ~8–12 weeks.

PILLAR PLAN:
- ARNI: stop lisinopril, wait 36 h, start sacubitril/valsartan 49/51 mg BID (BP 118 supports standard start) → target 97/103 BID.
- Beta-blocker: euvolemic now — start carvedilol 3.125 mg BID → target 25 mg BID (HR 78, BP 118 allow).
- MRA: K 4.4, eGFR 58 → start spironolactone 25 mg daily → target 25–50.
- SGLT2i: dapagliflozin 10 mg daily (no titration).

DIURETIC: continue furosemide 40 mg; reduce as congestion resolves to maintain euvolemia.

TITRATION SCHEDULE:
- Wk 0: ARNI 49/51 BID, carvedilol 3.125 BID, spironolactone 25, dapagliflozin 10.
- Wk 2: BMP; double ARNI to 97/103 and carvedilol to 6.25 BID if BP/HR/K OK.
- Wk 4–8: continue doubling carvedilol q2 wk to 25 BID; hold ARNI target if BP <100.

MONITORING:
- BMP at 1–2 wk after ARNI + spironolactone, then with each up-titration.
- BP/HR each visit; daily weights at home; tolerate eGFR dip ≤30%, K ≤5.5.

DEVICE / ADVANCED THERAPY:
- ICD: reassess LVEF after ≥3 months optimal GDMT; if still ≤35%, primary-prevention ICD.
- CRT: QRS 110 narrow → not a candidate now.
- No advanced-therapy triggers (NYHA II, euvolemic).

COMORBIDITY:
- Check iron studies (NT-proBNP elevated, symptomatic) — IV iron if ferritin <100 or TSAT <20%.
- Avoid NSAIDs, non-dihydropyridine CCBs, TZDs.

PITFALLS:
- 36-hour washout lisinopril → ARNI (angioedema risk).
- Started carvedilol only because euvolemic — never during active decompensation.
- Recheck K after spironolactone; hold MRA if K >5.5 or eGFR <30.
```
