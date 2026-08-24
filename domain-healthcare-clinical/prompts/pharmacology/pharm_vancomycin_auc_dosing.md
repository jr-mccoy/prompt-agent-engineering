---
title: "Vancomycin AUC-Guided Dosing"
category: domain-healthcare-clinical/pharmacology
description: "Initiate and adjust vancomycin using AUC24:MIC-guided dosing per IDSA 2020 consensus: select loading and maintenance doses from population PK, target AUC24/MIC 400–600 mg·h/L, perform two-level Bayesian or first-order kinetic calculations, and adjust for renal function, hemodialysis, augmented renal clearance, and obesity."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
  - QA-01
difficulty: advanced
tags:
  - infectious-disease
  - antibiotics
  - pharmacokinetics
  - dosing
  - critical-care
updated: "2026-05-12"
---

## Objective

Initiate and adjust intravenous vancomycin using AUC24:MIC-guided dosing (IDSA / ASHP / SIDP / PIDS 2020 consensus). Compute loading and maintenance doses from population pharmacokinetics, target AUC24/MIC 400–600 mg·h/L for serious MRSA infections, derive AUC from either two-level kinetics or Bayesian software, and adjust for renal function, hemodialysis, CRRT, obesity, augmented renal clearance, and pregnancy. Output is a written order with rationale, monitoring plan, and explicit re-dose math.

## Inputs

- Patient age, sex, height, actual body weight, BMI, ideal body weight
- Renal function: SCr trend, urine output, eGFR (Cockcroft-Gault commonly used for dosing in adults — actual body weight, adjusted if obese)
- Indication: empiric vs targeted, suspected/proven MRSA bacteremia, endocarditis, pneumonia, meningitis, prosthetic-device infection, osteomyelitis, severe SSTI
- MIC (if known) — vancomycin MIC ≤1 mg/L (most CLSI MRSA isolates) assumed if unknown
- Concomitant nephrotoxins (aminoglycosides, contrast, piperacillin-tazobactam concurrent — known additive nephrotoxicity)
- Hemodialysis status, dialysis access, dialyzer (high-flux vs low-flux), CRRT modality (CVVHD, CVVHDF) and effluent flow rate
- Hospital protocol: Bayesian software (e.g., InsightRx, DoseMeRx) available vs first-order kinetic two-level approach

## Role

Senior infectious disease pharmacist / physician writing the vancomycin order with computed loading, maintenance, monitoring plan, and dose-adjustment rules.

## Reasoning Steps

1. **Determine appropriateness.**
   - Confirm indication: vancomycin for serious gram-positive infection (MRSA suspected/confirmed), penicillin allergy with severe strep coverage, C. difficile (oral, not relevant to AUC dosing), or empiric gram-positive coverage.
   - For empiric coverage with low MRSA risk, consider whether cefazolin or alternative narrower agent is sufficient.
   - For pneumonia: vancomycin reaches lung concentrations slowly; consider linezolid or ceftaroline if rapid tissue penetration matters; lack of intracellular activity vs Legionella.

2. **Loading dose.**
   - **25–35 mg/kg actual body weight (ABW) IV × 1**, capped at 3000 mg, for serious infection (bacteremia, endocarditis, meningitis, sepsis, severe SSTI).
   - Use **actual body weight** for loading. For BMI ≥40, some institutions cap loading at 3000 mg or use adjusted body weight to avoid overshooting.
   - Infusion duration: ≥1 h per 1000 mg (e.g., 2000 mg over 2 h) to avoid red man / vancomycin infusion reaction (histamine release; not true allergy). Pre-treat with diphenhydramine 25–50 mg if reaction prior.

3. **Maintenance dose (initial population PK estimate).**
   - **CrCl-based starting dose:**
     - CrCl >130: 15–20 mg/kg ABW q8h (augmented renal clearance, e.g., young trauma / sepsis patients).
     - CrCl 80–130: 15–20 mg/kg ABW q8h or q12h.
     - CrCl 50–80: 15–20 mg/kg q12h.
     - CrCl 30–50: 15 mg/kg q24h (some q12h with closer monitoring).
     - CrCl 15–30: 15 mg/kg q24–48h (level-driven).
     - CrCl <15 / dialysis: see step 6.
   - **Maximum single dose**: typically 3000 mg per dose (some 2000 mg) per institution; if calculated >3000, split frequency.
   - **Round** to nearest 250 mg.

4. **Target AUC24/MIC 400–600 mg·h/L.**
   - For serious MRSA (bacteremia, endocarditis, pneumonia, osteomyelitis): target AUC24:MIC of 400–600, assuming MIC ≤1 mg/L (broth microdilution); if MIC = 2, target AUC may not be achievable safely; consider alternative agent (daptomycin, ceftaroline).
   - Avoid trough-only monitoring as primary target in most cases per 2020 guidelines; troughs ≥15–20 mg/L correlate with higher AUC but also higher AKI risk. Bayesian or two-level kinetics more accurate.

5. **Compute AUC from two levels (first-order, no Bayesian software).**
   - Draw **peak** (1–2 h after end of infusion, at distribution-equilibrated time) and **trough** (≤30 min before next dose) at presumed steady state (third or fourth dose).
   - Compute elimination rate constant: **ke = ln(peak / trough) / Δt** (Δt = time between peak and trough samples).
   - Half-life: **t½ = 0.693 / ke**.
   - Extrapolate peak and trough back to true Cmax (just after distribution complete) and forward to Cmin (immediately before dose):
     - **Cmax (true)** = peak / e^(−ke × Δt_peak), where Δt_peak is time from end of infusion to peak draw (usually 1 h).
     - **Cmin (true)** = trough × e^(−ke × Δt_trough), where Δt_trough is time from trough draw to next dose.
   - Compute AUC for one dosing interval:
     - **AUC_infusion** = (Cmax + Cprior-end-of-infusion) × infusion duration / 2
     - **AUC_elimination** = (Cmax − Cmin) / ke
     - **AUC_τ** = AUC_infusion + AUC_elimination
     - **AUC24** = AUC_τ × (24 / τ), where τ is dosing interval.
   - Compare with target 400–600 mg·h/L. Adjust dose / interval to bring AUC within range.

6. **Hemodialysis dosing.**
   - **Intermittent HD (3–4×/wk, high-flux dialyzer):** vancomycin clearance ~30–50% per session.
     - Loading: 25 mg/kg ABW IV during last hour of HD (or post-HD).
     - Maintenance: 7.5–10 mg/kg ABW IV post-HD on dialysis days.
     - Pre-HD level on next session — target pre-HD level ~15–20 mg/L. Adjust maintenance dose up or down by 25% based on pre-HD trough.
   - **Low-flux dialyzer:** vancomycin clearance minimal; treat as if not dialyzed for most of the interval; q72h dosing common.
   - **CRRT (CVVH, CVVHD, CVVHDF):** effective vancomycin clearance similar to CrCl ~30–50 mL/min depending on effluent flow.
     - Loading: 25 mg/kg ABW IV × 1.
     - Maintenance: 10–15 mg/kg ABW IV q24h (or q12h if effluent flow rate high).
     - Check level at 24 h; adjust by Bayesian if available.
   - **PIRRT/SLED:** between intermittent and continuous; institution-specific dosing.

7. **Special populations.**
   - **Augmented renal clearance** (young trauma, burn, sepsis with hyperdynamic state, pregnancy): CrCl >130; consider continuous infusion to maintain target AUC (loading 25–35 mg/kg, then 30–40 mg/kg/day continuous infusion; check level at 24 h, target serum 20–25 mg/L); reassess q8–12h.
   - **Obesity (BMI ≥30):** use ABW for loading; ABW for maintenance with closer level monitoring; volumes of distribution larger.
   - **Pediatrics:** weight-based with separate population PK parameters; AUC target same; Bayesian software preferred.
   - **Burn:** increased clearance, larger Vd; higher per-dose mg/kg and more frequent intervals; serial monitoring.
   - **Pregnancy:** higher CrCl in 2nd–3rd trimester → may need q8h; monitor levels closely.

8. **Toxicity monitoring.**
   - AKI risk: AUC >600 mg·h/L (and especially >800), prolonged duration >7 days, concurrent piperacillin-tazobactam (additive nephrotoxicity by some data; controversial — some studies show no causal effect), concurrent aminoglycoside, contrast, NSAIDs, ACEi, ARB.
   - Baseline SCr and daily SCr while on therapy.
   - Ototoxicity: rare at typical doses; higher risk with sustained troughs >30 mg/L or aminoglycoside coadministration.
   - Red man / vancomycin infusion reaction: histamine release from rapid infusion → flushing, pruritus, hypotension. Treat by slowing infusion and antihistamine; not a true allergy; can re-challenge.
   - DRESS, SJS, ANC: rare immune reactions; discontinue.

9. **Verify the calculation and the order.**
   - Show the loading dose calculation: weight × mg/kg = mg, rounded to nearest 250 mg.
   - Show the maintenance dose and interval with CrCl basis.
   - Specify level timing (peak, trough, or both) and assay turnaround expectation.
   - Specify SCr and BUN monitoring frequency.
   - Specify red flags for stopping or adjusting (AKI defined per KDIGO: SCr increase ≥0.3 mg/dL or 1.5× baseline within 48 h).

## Output Format

```
PATIENT SNAPSHOT:
[Age, sex, weight (ABW, IBW, BMI), SCr, eGFR / CrCl, indication, MIC if known, concomitant nephrotoxins]

INDICATION & TARGET:
- Indication: [serious MRSA infection — bacteremia / endocarditis / pneumonia / meningitis / osteomyelitis / SSTI]
- Target AUC24:MIC = 400–600 mg·h/L (assume MIC ≤1 mg/L unless otherwise specified)

LOADING DOSE:
- [25–35 mg/kg ABW × ABW] = [mg], rounded to [mg], cap at 3000 mg
- Infuse over [≥1 h per 1000 mg]

MAINTENANCE DOSE (initial population estimate):
- CrCl = [computed value] mL/min
- Dose = [15–20 mg/kg ABW] q[interval] = [mg q __ h]
- Rationale for interval: [CrCl-band match]

LEVEL MONITORING PLAN:
- Two-level approach: draw peak 1 h post end-of-infusion AND trough ≤30 min before next dose, at [3rd or 4th dose timing — steady state]
- OR Bayesian: draw level(s) at [specified times], software [X]
- SCr daily

EXPECTED AUC AT THIS DOSE:
- [Estimated AUC24 from population PK or two-level extrapolation, with calculation shown]

DOSE-ADJUSTMENT RULES (after first level):
- If AUC <400: increase dose by 25% OR shorten interval (e.g., q12 → q8h); re-check after 24–48 h
- If AUC 400–600: continue current regimen
- If AUC >600: decrease dose by 25% OR lengthen interval (e.g., q8h → q12h); re-check after 24–48 h
- If AUC >800: hold dose, recheck level, reduce dose by 30–50%
- If SCr increases ≥0.3 mg/dL or 1.5× baseline: hold dose, evaluate for AKI, dose-adjust per new CrCl

SPECIAL POPULATION ADJUSTMENT:
- [Obesity / pregnancy / augmented renal clearance / HD / CRRT specific notes applied]

CONCURRENT NEPHROTOXIN MANAGEMENT:
- [Avoid concurrent piperacillin-tazobactam if alternative gram-negative coverage available; review aminoglycoside, contrast, NSAIDs, RAAS inhibitors]

DURATION:
- [Days planned per indication; reassess source control, follow-up cultures, clinical response]

WHEN TO STOP OR SWITCH:
- Cultures negative for MRSA → de-escalate.
- MRSA MIC ≥2 → consider switching to daptomycin or ceftaroline (vancomycin AUC ≥600 typically requires nephrotoxic doses).
- Persistent bacteremia at day 5–7 → infectious disease consultation; consider alternative agent (daptomycin) and source-control review.

CALCULATION SELF-CHECK:
- Loading: weight × mg/kg = [show math]
- Maintenance: weight × mg/kg / interval = [show math]
- Two-level AUC math: ke = ln(peak/trough)/Δt; Cmax true; Cmin true; AUC_τ; AUC24 = AUC_τ × (24/τ)
- Cross-check daily mg/day = AUC24 × CL_vanco; reasonable?
```

## Worked Example

**Input:** 64-year-old man, 88 kg, height 178 cm, BMI 28, admitted with MRSA bacteremia (blood cultures growing MRSA, MIC 1 mg/L), TTE pending. SCr 1.1 mg/dL (baseline). Concurrent piperacillin-tazobactam being held now that MRSA is identified. No other nephrotoxins. Write the vancomycin order.

**Output:**

```
PATIENT SNAPSHOT:
- 64-year-old man, ABW 88 kg, IBW 50 + 2.3(70 − 60) = 73 kg, BMI 28 (not obese; use ABW).
- SCr 1.1, CrCl (Cockcroft-Gault, male) = ((140 − 64) × 88) / (72 × 1.1) = (76 × 88) / 79.2 = 6688 / 79.2 ≈ **84 mL/min**.
- Indication: MRSA bacteremia, source pending (TTE pending; suspect IE per clinical context if TEE planned). Serious deep-seated infection.
- No active nephrotoxins (piperacillin-tazobactam stopped, no AG, no contrast, no NSAIDs).

INDICATION & TARGET:
- MRSA bacteremia, MIC 1 mg/L; target AUC24:MIC 400–600 mg·h/L → target AUC24 400–600 mg·h/L.

LOADING DOSE:
- 25 mg/kg × 88 kg = 2200 mg → round to **2250 mg IV ×1**, infuse over 2.5 h (about 1 h per 1000 mg, conservative for infusion-reaction prevention).

MAINTENANCE DOSE (initial):
- CrCl 84 → 15–20 mg/kg ABW q12h.
- 17.5 mg/kg × 88 = 1540 mg → round to **1500 mg IV q12h** starting 12 h after loading dose end.
- Total daily 3000 mg/day.

LEVEL MONITORING PLAN:
- Two-level kinetic monitoring (Bayesian preferred if institutional software available, e.g., InsightRx; otherwise two-level first-order):
  - Peak: 1 h after end of 3rd dose infusion.
  - Trough: 30 min before 4th dose (or just before scheduled next dose at steady state).
- SCr daily; BUN, magnesium, phosphate every other day.
- Repeat blood cultures q24–48 h until negative.

EXPECTED AUC AT THIS DOSE (population estimate):
- Vd ≈ 0.7 L/kg × 88 = 62 L.
- CL_vanco ≈ CrCl × 0.79 (population estimate) = 84 × 0.79 = 66 mL/min = 3.96 L/h.
- Steady-state AUC24 = Total daily dose / CL = 3000 mg / 3.96 L/h = ~758 mg·h/L → above target; reduce maintenance dose at the time of first level if confirmed.
- Note: at CrCl 84 with q12h dosing, 15 mg/kg might be a better initial choice; will recalibrate after first level.

DOSE-ADJUSTMENT RULES AFTER FIRST AUC:
- AUC 400–600: continue 1500 mg IV q12h.
- AUC <400: increase to 1750 mg IV q12h.
- AUC 600–800: reduce to 1250 mg IV q12h.
- AUC >800: hold next dose, recheck level, restart at 1000 mg IV q12h.
- Recheck after dose change at 48–72 h.

CONCURRENT NEPHROTOXIN MANAGEMENT:
- Piperacillin-tazobactam already discontinued (good); avoid restarting if alternative gram-negative coverage needed (cefepime / meropenem alternatives if dual coverage required).
- Hold NSAIDs, ACEi/ARB if started.
- Use isotonic IV fluids to support renal perfusion.

DURATION:
- MRSA bacteremia minimum 14 days IV from first negative blood culture; longer (4–6 weeks) for endocarditis, complicated osteomyelitis, persistent bacteremia.
- ID consultation strongly recommended; obtain TEE to evaluate for IE if any concern; assess for metastatic foci (urine cultures, spine pain, fever curve).

WHEN TO STOP OR SWITCH:
- Blood cultures clearing within 72 h: continue vancomycin per duration plan.
- Bacteremia persistent >5–7 d: ID consult, switch to daptomycin 8–10 mg/kg IV q24h (assuming not pneumonia), reassess source control.
- MIC ≥2: consider daptomycin or ceftaroline early (AUC target may not be safely achievable).
- AKI: hold dose, adjust per new CrCl; consider alternative agent if AKI worsens.

CALCULATION SELF-CHECK:
- Loading dose 2250 mg = 25.6 mg/kg ABW. Within 25–35 range. Below 3 g cap. ✓
- Maintenance 1500 mg q12h = 17 mg/kg q12h. Within 15–20 range. ✓
- Daily total 3000 mg = 34 mg/kg/day. Above the conservative 30 mg/kg/day mark; expected AUC ~750 by population estimate — will adjust after first level. Acceptable starting point given indication severity and ABW; plan to reduce based on level.
- CrCl 84, CrCl-band q12h. ✓
- No active nephrotoxins. ✓
- Bayesian or two-level monitoring scheduled. ✓
- Source-control and ID consult plan in place. ✓
```
