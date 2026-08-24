---
title: "Aminoglycoside Dosing (Extended Interval and Traditional)"
category: domain-healthcare-clinical/pharmacology
description: "Initiate and adjust gentamicin, tobramycin, or amikacin using either extended-interval (once-daily) or traditional multiple-daily dosing strategies; select strategy by indication, compute weight-based dose, schedule level monitoring, and adjust for renal function, obesity, and synergy use in endocarditis."
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
  - aminoglycoside
  - nephrotoxicity
  - dosing
updated: "2026-05-12"
---

## Objective

Initiate and monitor aminoglycoside therapy: choose extended-interval (once-daily, "Hartford nomogram" or 7 mg/kg approach) vs traditional multiple-daily dosing based on indication, compute weight-based dose using ideal/adjusted body weight, schedule and interpret levels, adjust for renal function and obesity, and protect against nephro- and ototoxicity. Output a complete order with rationale.

## Inputs

- Patient: age, sex, height, actual body weight (ABW), ideal body weight (IBW), adjusted body weight (AdjBW), SCr, eGFR / CrCl, urine output
- Indication: empiric gram-negative coverage, complicated UTI, intra-abdominal sepsis, pyelonephritis, gram-negative endocarditis adjunct, enterococcal endocarditis synergy, pulmonary cystic fibrosis exacerbation
- Organism / MIC if known; cultures pending vs results
- Concomitant nephrotoxins (vancomycin, contrast, NSAIDs, loop diuretics, amphotericin B)
- Baseline auditory and vestibular function, hearing loss, balance, family history of mitochondrial mutations (m.1555A>G)
- Pregnancy status

## Role

Senior infectious disease pharmacist / physician writing the aminoglycoside order, choosing strategy, and specifying level monitoring and AUC-or-Cmax targets.

## Reasoning Steps

1. **Choose strategy.**
   - **Extended-interval (once-daily) dosing — first-line for most gram-negative indications:**
     - Leverages concentration-dependent killing (high Cmax/MIC = better efficacy) and post-antibiotic effect.
     - Lower trough means renal cortex recovery time, reducing nephrotoxicity vs traditional.
     - Indications: complicated UTI/pyelonephritis, intra-abdominal sepsis, hospital-acquired pneumonia (adjunct), pseudomonas coverage in CF exacerbation, empiric gram-negative bacteremia (adjunct).
   - **Traditional multiple-daily dosing (q8h) — preferred for:**
     - Enterococcal endocarditis synergy (low-dose, e.g., gentamicin 3 mg/kg/day divided q8h).
     - Gram-negative or HACEK endocarditis adjunct (controversial; current AHA guidance often shifts to ceftriaxone monotherapy for HACEK).
     - Pediatrics (some institutions).
     - Pregnancy (vary by institution).
     - Severe burns, ascites, third-spacing (highly variable Vd).
     - CrCl <20 (extended-interval less validated).

2. **Compute dosing weight.**
   - **IBW** males: 50 + 2.3 × (height_in − 60) kg. Females: 45.5 + 2.3 × (height_in − 60) kg.
   - **AdjBW** = IBW + 0.4 × (ABW − IBW). Use for obese patients (ABW > 1.2 × IBW).
   - For extended-interval: use **AdjBW** if obese, otherwise ABW or IBW (institution-specific; AdjBW reasonable).
   - For traditional: typically AdjBW or IBW.

3. **Compute initial dose.**
   - **Extended-interval gentamicin / tobramycin:**
     - Normal renal function (CrCl ≥60): **7 mg/kg AdjBW IV q24h** (Hartford); alternative 5 mg/kg q24h conservative.
     - CrCl 40–59: 7 mg/kg q36h.
     - CrCl 20–39: 7 mg/kg q48h.
     - CrCl <20: traditional dosing preferred, or load 2 mg/kg then levels-based.
   - **Extended-interval amikacin:** 15–20 mg/kg AdjBW IV q24h (higher than gent/tob because amikacin MICs are higher).
   - **Traditional gentamicin / tobramycin:**
     - 1.5–2 mg/kg IV q8h with normal renal function. Adjust interval q12h (CrCl 40–60), q24h (CrCl <40).
   - **Enterococcal endocarditis synergy gentamicin:** 1 mg/kg AdjBW IV q8h × 2 weeks (per AHA). Aim peak ~3–5 mg/L, trough <1 mg/L.

4. **Level monitoring — extended-interval.**
   - **Hartford nomogram (7 mg/kg):** draw a single level 6–14 h after start of first infusion (the "Hartford nomogram zone" defines next dose interval).
   - **Random level interpretation:**
     - Level >3 mg/L in the 8–12 h window → next dose interval longer (q36 or q48).
     - Level <1 mg/L → re-dose typical q24h.
   - **Steady-state Cmax (peak)**: extrapolated end-of-infusion concentration; target 16–24 mg/L for gentamicin/tobramycin, 56–64 mg/L for amikacin (concentration-dependent killing target Cmax/MIC ≥10).
   - **Trough (right before next dose)**: target **<1 mg/L** (gent/tob), **<5 mg/L** (amikacin) — undetectable trough is the goal in extended-interval.
   - Daily SCr; redraw levels if SCr changes.

5. **Level monitoring — traditional.**
   - Peak 30 min after end of 30-min infusion. Trough just before next dose.
   - Target peak: 5–10 mg/L (gent/tob, gram-negative); 25–35 mg/L (amikacin).
   - Target trough: <2 mg/L (gent/tob); <8 mg/L (amikacin).
   - Endocarditis synergy: peak 3–4 mg/L, trough <1 mg/L (gent).
   - Adjust dose for peak, interval for trough.

6. **Duration.**
   - Empiric gram-negative coverage: discontinue at 48–72 h once cultures de-escalate to a single-class agent if not needed for synergy.
   - Pseudomonas pneumonia: typically 5–7 days adjunct; some use entire course depending on monotherapy considerations.
   - Endocarditis synergy: 2 weeks of gentamicin in viridans strep with high MIC, 2 weeks for enterococcal, longer for some streptococci or staph (newer AHA guidance reduced gent use due to nephrotoxicity).
   - Pyelonephritis: 5–7 days; UTI shorter.
   - Long courses (>7–10 days): increase nephro- and ototoxicity risk; reassess necessity, consider alternatives.

7. **Monitor for toxicity.**
   - **Nephrotoxicity:** ATN from accumulation in renal cortex; reversible if caught early. Daily SCr, urine output. Risk factors: extended duration (>7 d), other nephrotoxins, prior renal disease, hypovolemia, hypotension, advanced age.
   - **Ototoxicity:** cochlear (hearing loss, high frequency first) and vestibular (gait instability, oscillopsia); irreversible. Baseline and weekly audiometry on longer courses. Mitochondrial m.1555A>G mutation predisposes to severe deafness even with normal doses — family history; testing available where indicated.
   - **Neuromuscular blockade:** rare, with rapid IV bolus, concurrent NM blockers, myasthenia gravis. Slow infusion.
   - **Hypomagnesemia and hypocalcemia:** electrolyte monitoring.

8. **Special situations.**
   - **Cystic fibrosis:** higher Vd, faster clearance — use higher mg/kg (10 mg/kg/day tobramycin), adjust to levels.
   - **Pregnancy:** crosses placenta; ototoxicity in fetus reported; use only when no alternative.
   - **Renal replacement therapy:** dose 2–3 mg/kg post-HD; check pre- and post-HD levels; CRRT dosing institution-specific.
   - **Burns:** highly variable PK; level-driven dosing essential.
   - **Pediatrics:** weight-based; institution-specific extended-interval protocols (Nottingham 7 mg/kg, some 5 mg/kg).

9. **Verify and write.**
   - Show dose calculation, level draw times, target ranges, monitoring schedule, duration with reassessment trigger.

## Output Format

```
PATIENT SNAPSHOT:
- Age, sex, height, ABW, IBW, AdjBW (if obese), SCr, CrCl
- Indication, organism (if known), MIC
- Concomitant nephrotoxins
- Baseline auditory / vestibular status

STRATEGY:
- Extended-interval OR traditional, with rationale

DOSE:
- [Agent] [mg/kg using which weight] = [mg] IV q[hours]
- Infusion duration: 30–60 minutes

LEVEL MONITORING:
- Extended-interval: random level at 8–12 h or specific Hartford-nomogram time
- Traditional: peak 30 min post-infusion, trough pre-dose, at 3rd–4th dose
- Targets: [peak X–Y mg/L; trough <Z]
- SCr daily

DOSE-ADJUSTMENT RULES AFTER LEVELS:
- Peak below target: increase mg/kg; recheck
- Peak above target: decrease mg/kg; recheck
- Trough above target: lengthen interval; recheck
- SCr increase ≥0.3 or 1.5× baseline: hold, reassess

DURATION:
- Planned days, reassessment at 48–72 h, alternative if avoidable

NEPHRO/OTO/NM TOXICITY MONITORING:
- Daily SCr, weekly audiogram if course >7 d, watch for vertigo / hearing change
- Mg, Ca, K monitoring

ALTERNATIVES:
- If indication uncertain or short-course adequacy: ceftriaxone, ciprofloxacin, or carbapenem alternatives
- Endocarditis synergy: current guidance favors avoiding gentamicin in many staphylococcal IE

SELF-CHECK:
- Weight used: [ABW / AdjBW / IBW with rationale]
- Dose mg/kg/day: within strategy range
- Interval matches CrCl
- Level draw times specified
- Toxicity monitoring scheduled
```

## Worked Example

**Input:** 71-year-old man, ABW 102 kg, height 5'10" (70 in), IBW 73 kg, AdjBW 85 kg, SCr 1.4, CrCl 51, admitted with severe pyelonephritis and suspected gram-negative sepsis pending cultures. Concurrent vancomycin pending culture results.

**Output:**

```
PATIENT SNAPSHOT:
- 71 y M, ABW 102 kg, IBW 73 kg, AdjBW = 73 + 0.4(102 − 73) = 85 kg.
- SCr 1.4, CrCl 51 (Cockcroft-Gault).
- Indication: severe pyelonephritis, suspected gram-neg sepsis, empiric coverage.
- On vancomycin → additive nephrotoxicity risk; weigh need carefully.
- Baseline hearing intact per history.

STRATEGY:
- **Extended-interval gentamicin** — concentration-dependent killing, lower nephrotoxicity than traditional q8h despite same total daily exposure; appropriate for empiric coverage at moderate CrCl.

DOSE:
- **Gentamicin 7 mg/kg AdjBW IV q36h** = 7 × 85 = **595 mg → round to 600 mg IV q36h.** First dose now.
- Infuse over 30–60 minutes.

LEVEL MONITORING:
- Random level at 8 h after start of first infusion (Hartford nomogram zone).
  - If level falls in q24h band → shift to q24h.
  - If in q36h band → continue q36h.
  - If in q48h band → q48h.
- Trough just before next dose if any doubt — target undetectable (<1 mg/L).
- Daily SCr, BUN, K, Mg.

DOSE-ADJUSTMENT RULES:
- Trough >1 mg/L: lengthen interval (q36 → q48); recheck.
- SCr increase ≥0.3 mg/dL or 1.5× baseline (i.e., ≥1.7 or ≥2.1): hold next dose, reassess.
- After culture and de-escalation, consider stopping gentamicin if not needed for combined coverage.

DURATION:
- Empiric coverage 48–72 hours; reassess once cultures finalize.
- If organism susceptible to single agent (e.g., ceftriaxone for E. coli), de-escalate and stop gentamicin.
- Total course not typically needed for full pyelonephritis duration when β-lactam is effective.

NEPHRO/OTO/NM TOXICITY MONITORING:
- Daily SCr trend.
- Vancomycin AUC monitoring (both nephrotoxins together — risk additive).
- Watch for vertigo, gait instability, tinnitus, hearing change.
- Mg q3 days.
- If continuing >7 days: baseline + weekly audiogram.

ALTERNATIVES:
- Single-agent broad β-lactam (e.g., piperacillin-tazobactam 3.375 g IV q6h or cefepime 2 g IV q8h) often adequate for empiric coverage in pyelo without sepsis; aminoglycoside addition reserved for septic shock, recent multi-drug-resistant exposures, or known ESBL colonization.
- Reasonable to start cefepime + gentamicin loading dose, plan to discontinue gentamicin at 48–72 h after culture results.

SELF-CHECK:
- Weight: AdjBW 85 kg used (patient obese, ABW > 1.2 × IBW). ✓
- mg/kg: 7 mg/kg matches Hartford. ✓
- Interval q36h matches CrCl 51. ✓
- Level at 8 h scheduled. ✓
- Nephrotoxicity monitoring active. ✓
- Stop trigger at 48–72 h pending cultures. ✓
```
