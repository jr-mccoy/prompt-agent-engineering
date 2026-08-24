---
title: "Therapeutic Drug Monitoring (TDM) Interpretation"
category: domain-healthcare-clinical/pharmacology
description: "Interpret a drug level (vancomycin AUC, aminoglycoside trough, digoxin, lithium, phenytoin, valproate, theophylline, calcineurin inhibitors, mTOR inhibitors, antifungals) by assessing timing relative to dose, steady state, sampling technique, free vs total drug concentration, and patient-specific PK factors; output dose adjustment with rationale."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
  - QA-01
difficulty: advanced
tags:
  - pharmacology
  - tdm
  - drug-monitoring
  - dosing
  - pharmacokinetics
updated: "2026-05-12"
---

## Objective

Interpret a measured drug level in clinical context: verify timing relative to dose and steady state, confirm sampling technique was correct, account for free vs total concentration (high-protein-bound drugs), apply patient-specific PK (renal/hepatic function, age, body composition, drug interactions, ECMO/CRRT/dialysis), and propose dose or interval adjustment. Output a written interpretation with rationale and follow-up plan.

## Inputs

- Drug name, current dose, route, frequency, dosing start date and most recent dose time
- Level: value, units, sampling time relative to last dose, sampling method (peak vs trough, random)
- Target range for the indication
- Patient: age, weight, renal function (SCr, CrCl, eGFR), hepatic function, albumin, comorbidities
- Concomitant medications (interactions affecting PK)
- Special situations: dialysis, CRRT, ECMO, plasmapheresis
- Clinical response: efficacy markers, toxicity signs

## Role

Senior clinical pharmacist / physician interpreting the level and writing the dose adjustment.

## Reasoning Steps

1. **Verify sampling timing relative to dose.**
   - **Trough:** measured immediately before next dose (within 30 min); reflects minimum concentration in dosing interval.
   - **Peak:** measured after distribution complete; varies by drug:
     - Aminoglycosides traditional: 30 min post end of 30-min infusion.
     - Vancomycin: 1–2 h post end of infusion (extrapolation if Bayesian).
     - Lithium: 12 h post dose (12-h trough).
     - Phenytoin: trough preferred; or random for toxicity assessment.
     - Tacrolimus / cyclosporine: trough.
     - Digoxin: ≥6 h post dose (8 h preferred) — earlier samples are misleadingly high during distribution.
     - Theophylline: ~30 min before next dose (oral, sustained release).
   - If timing wrong, level may misrepresent clinical exposure. Re-draw if doubt.

2. **Confirm steady state has been reached.**
   - Steady state reached after ~4–5 half-lives.
   - Drug-specific:
     - Vancomycin t½ ~6 h normal renal → steady state ~24–30 h.
     - Phenytoin t½ ~22 h (nonlinear at higher doses) → SS ~3–5 days; longer at high concentrations.
     - Lithium t½ 18–36 h → SS 5–7 days.
     - Digoxin t½ 36–48 h → SS 5–10 days.
     - Tacrolimus t½ ~12–18 h → SS 2–3 days.
     - Warfarin: not a TDM by serum level — use INR, but full INR effect after 3–5 days of stable dose.
     - Levothyroxine: 6–8 weeks to reach steady-state TSH.
   - If level drawn before steady state, the level reflects ongoing accumulation, not the eventual plateau — adjust interpretation.

3. **Account for free vs total concentration.**
   - **Phenytoin** (90% protein-bound to albumin): hypoalbuminemia and renal failure shift the free-to-total ratio; total phenytoin appears low but free fraction may be therapeutic. Calculate corrected total phenytoin using **Sheiner-Tozer**:
     - Adjusted = measured total / (0.2 × albumin + 0.1) — if eGFR <20: use 0.1 × albumin + 0.1.
     - Better: measure **free phenytoin** directly (target 1–2 µg/mL).
   - **Valproate** (~90% protein-bound; saturable binding at higher concentrations): high-dose can have higher free fraction at the same total; consider free valproate measurement if uncertainty.
   - **Calcium** (50% protein-bound to albumin): correct or measure ionized.

4. **Apply patient-specific PK adjustments.**
   - **Renal function:**
     - Vancomycin, aminoglycosides, lithium — renal clearance dominant; CrCl drop raises levels.
     - Digoxin — 70% renal clearance; renal decline causes toxicity.
   - **Hepatic function:** affects CNI, valproate, theophylline, mTOR inhibitors; low albumin influences free fraction.
   - **Drug-drug interactions:**
     - CYP3A4 inhibitors (azoles, macrolides, diltiazem, grapefruit) raise tacrolimus, cyclosporine, sirolimus levels — dose reduce when starting.
     - CYP3A4 inducers (rifampin, phenytoin, carbamazepine) lower CNI levels — dose increase.
     - Quinidine, amiodarone, verapamil raise digoxin levels.
     - Thiazides, NSAIDs raise lithium.
   - **Dialysis / CRRT:** vancomycin removed during HD with high-flux dialyzer; aminoglycosides removed; lithium dialyzable; digoxin not appreciably dialyzed. Adjust around dialysis sessions.
   - **ECMO:** sequestration of lipophilic drugs (fentanyl, propofol, voriconazole, midazolam) — higher doses often needed.
   - **Pregnancy:** lamotrigine clearance increases; many levels rise / fall through pregnancy.
   - **Body weight extremes:** Vd changes affect peak concentrations.

5. **Compare to target range for the indication.**
   - **Vancomycin:** AUC24/MIC 400–600 (serious MRSA); trough 15–20 if no AUC monitoring (older standard).
   - **Aminoglycosides extended-interval:** peak >16 mg/L (gent/tob), >56 mg/L (amikacin); trough <1 (gent/tob), <5 (amikacin).
   - **Aminoglycosides traditional:** peak 5–10 mg/L (gent/tob), 25–35 (amikacin); trough <2 (gent/tob), <8 (amikacin).
   - **Digoxin:** 0.5–0.9 ng/mL for heart failure (lower toxicity than older 0.8–2.0); 1.5–2 ng/mL for rate control AFib if needed; toxicity >2.0.
   - **Lithium:** acute mania 0.8–1.2 mEq/L; maintenance 0.6–0.8; toxicity >1.5; severe >2.0.
   - **Phenytoin (total):** 10–20 µg/mL (free 1–2 µg/mL).
   - **Valproate:** 50–100 µg/mL (some up to 125).
   - **Carbamazepine:** 4–12 µg/mL.
   - **Theophylline:** 5–15 µg/mL (older 10–20 with more toxicity).
   - **Tacrolimus:** see immunosuppression prompt; varies by transplant and time post-op.
   - **Cyclosporine C0:** 100–400 ng/mL; C2 levels for cyclosporine reflect peak.
   - **Sirolimus / everolimus:** 5–15 ng/mL trough.
   - **Voriconazole:** 1.5–5.5 µg/mL trough (>5.5 risk of CNS toxicity).
   - **Posaconazole:** 0.7–3 µg/mL trough.
   - **Itraconazole:** 0.5–3 µg/mL.
   - **Caffeine in neonates:** 5–20 µg/mL.

6. **Adjust dose by linear or nonlinear PK.**
   - **Linear (most drugs):** double dose → double concentration. New dose = current dose × (target / measured).
   - **Nonlinear (phenytoin, theophylline, voriconazole — Michaelis-Menten):** small dose changes cause disproportionate concentration changes. Phenytoin Vmax saturation: dose increase of 25–50% may cause 100–200% concentration rise; use small increments.
   - **For interval changes:** double interval → halve trough roughly; useful when trough too high but peak therapeutic.
   - For elimination-rate-constant calculations (two-level kinetics), see vancomycin prompt.

7. **Recognize and manage toxicity.**
   - Symptomatic toxicity overrides specific number:
     - Digoxin: nausea, anorexia, visual disturbance (yellow halos), arrhythmia, hyperkalemia (toxicity sign); reversal with digoxin-immune Fab (DigiFab) for hemodynamic instability, refractory arrhythmia, K >5, ingestion >10 mg.
     - Lithium: tremor, ataxia, confusion, seizure, coma; reversal hemodialysis if level >4.0, or >2.5 with severe symptoms.
     - Phenytoin: nystagmus, ataxia (mild), coma (severe); hold dose, supportive care.
     - Aminoglycosides: oto- and nephrotoxicity (often delayed).
     - Vancomycin: AKI; ototoxicity rare.
     - Theophylline: nausea, tremor, seizure, arrhythmia; charcoal hemoperfusion in severe.
     - CNI: tremor, headache, seizure, AKI, hyperkalemia.

8. **Document level, interpretation, action.**
   - Level: value, time of draw relative to dose, steady-state status, target.
   - Interpretation: in target / sub / supra; clinical correlation; PK factors considered.
   - Action: continue, increase, decrease, hold, switch.
   - Re-check timing and method.

## Output Format

```
DRUG / INDICATION:
[Drug, indication, target range]

LEVEL:
- Value: [X units]
- Drawn at [time] post last dose; [trough / peak / random]
- Most recent dose: [time, mg]
- Days on therapy: [N] → [steady state reached: yes/no]

SAMPLING TECHNIQUE CHECK:
- Timing relative to dose appropriate? [yes/no]
- Steady state reached? [yes/no]
- Sampling technique appropriate? [yes/no]
- Free vs total adjustment (if applicable): [Sheiner-Tozer correction, free level]

PATIENT PK CONTEXT:
- Renal: [CrCl, eGFR]
- Hepatic: [albumin, LFTs]
- Drug interactions: [identified]
- Body weight / Vd considerations
- Dialysis / CRRT / ECMO

INTERPRETATION:
- [In target / below / above]
- Reasoning: [PK and clinical correlation]

DOSE ADJUSTMENT:
- New dose: [mg]
- New interval: [q__h]
- Linear or nonlinear adjustment rationale: [...]
- Show calculation: [current × target / measured]

NEXT LEVEL:
- Timing: [next trough or peak]
- Re-evaluation date

CLINICAL RESPONSE:
- Efficacy markers: [...]
- Toxicity surveillance: [drug-specific]

WHEN TO ESCALATE:
- Severe toxicity: [specific reversal — DigiFab, dialysis for lithium, etc.]
- Persistent supratherapeutic despite adjustment: alternative agent
- Inadequate efficacy at toxic levels: switch class

SELF-CHECK:
- Level interpretable (timing, SS, sampling)
- Dose adjustment reasonable
- Re-check timing scheduled
- Toxicity monitoring active
```

## Worked Example

**Input:** 67-year-old man, 78 kg, AFib + HFrEF, on digoxin 0.125 mg PO daily ×4 weeks for rate control. CrCl 35. Digoxin level 2.4 ng/mL drawn at 8 AM (last dose 8 PM previous day, ~12 h post-dose). Symptoms: nausea, fatigue, anorexia, no visual changes, K 5.1.

**Output:**

```
DRUG / INDICATION:
- Digoxin for AFib rate control / HFrEF; target 0.5–0.9 ng/mL (HFrEF), or ≤1.5 for AFib rate control.

LEVEL:
- 2.4 ng/mL, drawn 12 h post last dose.
- 4 weeks on therapy (steady state easily reached for digoxin t½ ~36 h in normal renal; longer with CrCl 35).

SAMPLING TECHNIQUE CHECK:
- Timing: ≥6 h post dose required (distribution to tissue complete); 12 h post is appropriate. ✓
- Steady state: reached. ✓
- Sampling technique: appropriate.

PATIENT PK CONTEXT:
- CrCl 35 → reduced digoxin clearance; longer half-life (~3–4 days in CKD); dose should typically be lower.
- Hyperkalemia (K 5.1) — sign of digoxin toxicity (digoxin inhibits Na/K ATPase → K accumulates extracellularly).
- No other interacting drugs reported. (Amiodarone, verapamil, quinidine would raise levels.)
- Hypokalemia, hypomagnesemia, hypercalcemia would worsen toxicity at same level — current K 5.1 paradoxically less arrhythmogenic but reflects toxicity.

INTERPRETATION:
- **Supratherapeutic / toxic.** 2.4 ng/mL exceeds both HFrEF target (0.5–0.9) and AFib target (≤1.5).
- Clinical signs consistent: nausea, anorexia, fatigue, hyperkalemia.
- Mechanism: dose appropriate for normal renal function is excessive with CrCl 35; accumulation over 4 weeks.

DOSE ADJUSTMENT:
- **Hold digoxin** for 48–72 h.
- **Restart at lower dose: 0.0625 mg PO every other day** (i.e., 0.0625 mg every 48 h, or alternatively 0.125 mg twice weekly with dose every 3–4 days), reflecting CrCl 35.
- Calculation: target trough ~1 ng/mL; current 2.4 → reduce by factor 2.4 = ~58%; new dose ≈ 0.5 × current daily dose = 0.0625 mg/day (or 0.125 mg every other day). Given CrCl 35, half-dose every 48 h is conservative and matches AHA/HFSA recommendation.

NEXT LEVEL:
- Recheck digoxin level **5–7 days after restart at new dose** (allows clearance of accumulated drug + reach new steady state).
- BMP at 48 h and at next office visit to confirm K and Cr trend.

CLINICAL RESPONSE & TOXICITY:
- Monitor symptoms: nausea, vision, fatigue, palpitations, syncope.
- EKG: look for digoxin-effect changes (scooping of ST, T abnormalities); arrhythmia surveillance (atrial tachycardia with AV block, frequent ventricular ectopy, bidirectional VT — pathognomonic).
- Correct hypokalemia / hypomagnesemia if present; in current case K 5.1 → no supplementation.

WHEN TO ESCALATE:
- Symptomatic bradycardia, hemodynamic instability, life-threatening arrhythmia, refractory hyperkalemia (K >5.5 with arrhythmia), or ingestion >10 mg → **digoxin-immune Fab (DigiFab)**: dose = (serum digoxin × weight × 0.0056) → number of vials; or empiric 10–20 vials for unknown ingestion. Watch for rebound after Fab clearance.
- Worsening AKI: hold digoxin entirely; reconsider need.

SELF-CHECK:
- Level: 2.4, clearly supratherapeutic. ✓
- Steady state: yes.
- Timing of draw: appropriate.
- Renal-adjusted dose calculated.
- Recheck level timing scheduled.
- Symptom surveillance and EKG plan in place.
- K + Mg monitoring active.
```
