---
title: "Urinalysis and Microscopy Interpretation"
category: domain-healthcare-clinical/interpretation
description: "Interpret a urinalysis with dipstick and microscopy findings to identify infection, glomerular vs tubular vs post-renal pathology, and direct workup."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: intermediate
tags:
  - nephrology
  - urinalysis
  - infection
  - hematuria
  - interpretation
updated: "2026-05-08"
---

## Objective

Read a urinalysis with dipstick + microscopy and produce a clinical interpretation that names the likely pathology category (infection, glomerular, tubular, post-renal/structural, or contaminant) and the next workup step.

## Inputs

- Dipstick: pH, specific gravity, leukocyte esterase, nitrite, blood, protein, glucose, ketones, bilirubin, urobilinogen
- Microscopy: WBC, RBC, bacteria, casts (hyaline, granular, RBC, WBC, waxy, fatty), crystals, epithelial cells (squamous, renal tubular), yeast
- Collection: clean catch, catheter, suprapubic, indwelling
- Patient context: presenting symptom, age, sex, pregnancy, comorbidities (DM, CKD, HTN, lupus), recent meds (vanc, NSAID, ACE/ARB), recent imaging or instrumentation

## Role

Senior internist or nephrologist reading the UA with the chart open.

## Reasoning Steps

1. **Specimen quality.** >5 squamous epithelial cells/HPF or >10⁵ mixed flora suggests contamination; recommend clean recollection or catheter sample before committing to a pathology call.

2. **Concentration check.** Specific gravity (1.005–1.030) and pH (4.5–8.0). Fixed SG ~1.010 suggests inability to concentrate (CKD, ATN). Alkaline pH with WBC + nitrite-negative could mean *Proteus* or other urea-splitter; persistent alkaline pH with stones suggests RTA type 1 or struvite.

3. **Infection lane.**
   - **LE positive + nitrite positive + pyuria (>10 WBC/HPF) + bacteriuria** → UTI. Nitrite-positive specifically indicates Enterobacterales (E. coli, Klebsiella, Proteus). Nitrite-negative does not exclude UTI (Enterococcus, Staph saprophyticus, Pseudomonas don't reduce nitrate).
   - **Pyuria without bacteriuria (sterile pyuria):** TB, atypical organisms (Chlamydia, Mycoplasma), interstitial nephritis, nephrolithiasis, partially treated UTI, contamination.
   - **WBC casts** → pyelonephritis or interstitial nephritis (not lower tract).
   - Asymptomatic bacteriuria: do not treat outside pregnancy or pre-urologic procedure.

4. **Hematuria lane.**
   - **Dipstick blood + RBC on micro** → true hematuria.
   - **Dipstick blood + no RBC on micro** → myoglobinuria or hemoglobinuria (rhabdo, hemolysis).
   - **Dysmorphic RBCs / acanthocytes >5%, RBC casts, proteinuria >500 mg/day** → glomerular source. Workup: serum creatinine trend, complement (C3, C4), ANA, ANCA, anti-GBM, hepatitis serologies, consider renal biopsy.
   - **Isomorphic RBCs without casts/proteinuria** → urologic source. Workup: CT urogram, cystoscopy, especially if >40, smoker, exposure to aniline dyes/cyclophosphamide.

5. **Proteinuria lane.**
   - Trace–1+: orthostatic, fever, exercise, infection — repeat first morning.
   - 2+ or higher: quantify with UPCR or 24-hour. >3.5 g/day = nephrotic range.
   - **Glomerular proteinuria + edema + hyperlipidemia + hypoalbuminemia** → nephrotic syndrome (FSGS, MCD, MN, diabetic nephropathy, amyloid).
   - **Proteinuria + hematuria + RBC casts + HTN + AKI** → nephritic syndrome (IgA, lupus, ANCA, anti-GBM, post-infectious GN).
   - Dipstick detects albumin only — paraprotein (myeloma) requires SPEP/UPEP/free light chains.

6. **Cast lane.**
   - Hyaline: nonspecific (concentrated urine, exercise, fever)
   - Granular ("muddy brown"): ATN
   - RBC casts: glomerulonephritis (nearly pathognomonic)
   - WBC casts: pyelonephritis or interstitial nephritis
   - Waxy / broad: chronic kidney disease
   - Fatty / oval fat bodies / Maltese cross under polarized light: nephrotic syndrome

7. **Crystal lane.**
   - Calcium oxalate (envelope-shaped): common; ethylene glycol intoxication if abundant + AGMA + AKI
   - Uric acid (rhomboid, acid pH): gout, tumor lysis
   - Struvite (coffin lid, alkaline pH): urea-splitting infection (Proteus); staghorn stones
   - Cystine (hexagonal): cystinuria
   - Drug crystals: sulfa, indinavir, acyclovir, methotrexate

8. **Glucose / ketones / bilirubin.**
   - Glucose without hyperglycemia → SGLT2 inhibitor or proximal tubulopathy (Fanconi)
   - Ketones → DKA, starvation, alcoholic ketoacidosis (acetoacetate detected; beta-hydroxybutyrate not detected by dipstick)
   - Bilirubin → conjugated hyperbilirubinemia (hepatocellular or obstructive jaundice)

9. **Synthesis.** Name the syndrome (UTI, pyelonephritis, nephritic, nephrotic, AKI with ATN, contamination) and the action.

## Output Format

```
SPECIMEN: [collection method, quality]
DIPSTICK: [abnormal values, with interpretation]
MICROSCOPY: [WBC, RBC, bacteria, casts, crystals, epithelium, yeast]

PATTERN: [name the syndrome — UTI / pyelonephritis / nephritic / nephrotic / ATN / contamination / urologic hematuria / etc.]
LIKELY ETIOLOGY: [committed answer]

ACTION:
- [next test or treatment 1]
- [next test or treatment 2]
- [follow-up]
```

## Worked Example

**Input:** 32 y/o F, 1 week of facial swelling, frothy urine, BP 158/96. Clean catch UA: SG 1.020, pH 6.0, LE neg, nitrite neg, blood 3+, protein 4+, glucose neg, ketones neg. Micro: 25 RBC/HPF (dysmorphic), 2 WBC/HPF, 5 RBC casts/LPF, no bacteria, no squamous cells. UPCR pending.

**Output:**

```
SPECIMEN: Clean catch, good quality (no squamous, no bacteria)
DIPSTICK: 3+ blood, 4+ protein. LE/nitrite negative — not infection.
MICROSCOPY: Dysmorphic RBC 25/HPF, RBC casts 5/LPF. Pathognomonic of glomerular bleeding.

PATTERN: Nephritic syndrome (hematuria + dysmorphic RBC + RBC casts + significant proteinuria + hypertension).
LIKELY ETIOLOGY: Glomerulonephritis. Differential: IgA nephropathy (most common in young adults, often post-URI), lupus nephritis (ask about rash, arthralgia, oral ulcers, screen ANA/anti-dsDNA/complement), ANCA-associated vasculitis (ask about pulmonary or sinus symptoms; ANCA, anti-MPO/PR3), anti-GBM (Goodpasture if pulmonary involvement), post-streptococcal GN (recent strep throat or skin infection 1–4 weeks prior; low C3, normal C4).

ACTION:
- BMP now, repeat in 24h to track creatinine trajectory
- Quantify protein: UPCR or 24-hour urine protein
- Serologies: C3, C4, ANA, anti-dsDNA, ANCA (MPO, PR3), anti-GBM, ASO, hepatitis B and C
- BP control: ACE inhibitor (lisinopril 10 mg daily) if creatinine stable and K acceptable — also reduces proteinuria
- Nephrology consult today; biopsy likely indicated within days if creatinine rising or proteinuria nephrotic-range
- If rapidly progressive (creatinine rising over hours-to-days), this is a renal emergency — biopsy and empiric pulse steroids while results pending after consult agreement
```
