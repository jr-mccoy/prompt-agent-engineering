---
title: "BMP and CMP Interpretation"
category: domain-healthcare-clinical/interpretation
description: "Interpret a basic or comprehensive metabolic panel: identify electrolyte, renal, glucose, and hepatic abnormalities and direct workup."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: intermediate
tags:
  - chemistry
  - electrolytes
  - renal
  - liver
  - interpretation
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

Read a BMP or CMP and produce a structured interpretation: identify each abnormality, name the pattern (e.g., volume contraction, AKI prerenal vs intrinsic vs postrenal, transaminitis hepatocellular vs cholestatic), and commit to next steps.

## Inputs

- BMP: Na, K, Cl, HCO3 (CO2), BUN, Cr, glucose
- CMP adds: Ca, total protein, albumin, AST, ALT, ALP, total bilirubin (some panels add direct bili, GGT, Mg, Phos)
- Patient context: age, sex, weight, presenting problem, vitals (especially BP, HR), urine output, medications (diuretics, ACE/ARB, NSAIDs, contrast exposure, nephrotoxins), comorbidities (CKD baseline Cr, DM, cirrhosis, CHF), recent imaging
- Prior values for trending (especially Cr baseline)

## Role

Senior internist or hospitalist reading the panel with the chart open.

## Reasoning Steps

1. **Glucose.**
   - <70: hypoglycemia — confirm with repeat fingerstick, treat (15 g PO carbs if alert; 25 g D50 IV if obtunded; 1 mg glucagon IM/SC if no IV access). Always look for cause: insulin/sulfonylurea, sepsis, adrenal insufficiency, liver failure, malnutrition.
   - >250: hyperglycemia — check ketones, anion gap, osmolality. DKA vs HHS vs uncontrolled T2DM.

2. **Sodium.** Always interpret with volume status.
   - **Hyponatremia (Na <135):**
     - Step 1: serum osmolality. Hypotonic (<275) is true hyponatremia. Isotonic (pseudo, hyperproteinemia/hyperlipidemia) and hypertonic (hyperglycemia, mannitol) need different management. Correct Na for glucose: add 2.4 mEq Na for every 100 glucose >100.
     - Step 2: volume status. Hypovolemic (orthostatic, dry mucous membranes, BUN/Cr >20:1), euvolemic, hypervolemic (CHF, cirrhosis, nephrotic).
     - Step 3: urine Na and urine osm.
       - Hypovolemic + UNa <20 → extrarenal loss (GI, third-spacing, skin)
       - Hypovolemic + UNa >20 → renal loss (diuretics, salt wasting, adrenal insufficiency)
       - Euvolemic + Uosm >100 + UNa >20 → SIADH (after ruling out hypothyroidism, adrenal insufficiency, low solute intake)
       - Hypervolemic → CHF, cirrhosis, nephrotic, AKI/CKD
     - Correction rate: <8 mEq/L per 24h to avoid osmotic demyelination (especially if chronic, alcoholic, malnourished, hypokalemic). Severe symptomatic (seizures, coma) → 3% saline 100 mL bolus, repeat up to 3 doses, then reassess.
   - **Hypernatremia (Na >145):** always represents a free water deficit (or rapid Na load). Calculate water deficit: 0.6 × weight × (Na/140 − 1). Replace half over 24h. Identify cause: poor access to water (elderly, neuro), DI (UOP high, Uosm low — central vs nephrogenic), osmotic diuresis (glucose, urea), insensible loss (fever, burns).

3. **Potassium.**
   - **Hypokalemia (K <3.5):** GI loss (diarrhea, vomiting), renal loss (diuretics, hyperaldo, Bartter/Gitelman, RTA 1/2, hypomag), shift (insulin, beta-agonist, alkalosis, refeeding), poor intake. Severe (<2.5) or symptomatic (weakness, ECG changes — flattened T, U waves, ST depression) → IV replacement 10 mEq/hr peripheral or up to 20 mEq/hr central with telemetry. Replace Mg in parallel — can't fix K without Mg.
   - **Hyperkalemia (K >5.0):** rule out hemolyzed sample first. True hyperkalemia: AKI/CKD, ACE/ARB/spironolactone/trimethoprim, RTA 4 (hyporeninemic hypoaldo, common in DM), tissue breakdown (rhabdo, tumor lysis), acidosis. ECG changes (peaked T, wide QRS, sine wave) → calcium gluconate 1g IV stat for cardiac membrane stabilization, then shift (insulin 10 units + D50, albuterol, bicarbonate if acidotic), then remove (loop diuretic if making urine, patiromer/SZC, dialysis if severe).

4. **Chloride / HCO3 (the metabolic side).** Use anion gap = Na − (Cl + HCO3); normal 8–12. Triggers acid-base workup — see ABG interpretation prompt for full pathway.

5. **BUN/Cr → renal evaluation.**
   - Calculate eGFR (CKD-EPI 2021).
   - Compare to baseline. AKI definitions (KDIGO): Cr increase ≥0.3 mg/dL within 48h, or ≥1.5× baseline within 7 days, or UOP <0.5 mL/kg/hr for ≥6h.
   - Stage AKI: 1 (1.5–1.9× baseline), 2 (2–2.9×), 3 (≥3× or Cr ≥4.0 or initiation of RRT).
   - Categorize:
     - **Prerenal:** BUN/Cr >20, FENa <1% (off diuretics), FEUrea <35% (on diuretics), bland sediment. Causes: volume depletion, decreased effective circulating volume (CHF, cirrhosis), hypotension, ACE/ARB/NSAID-induced.
     - **Intrinsic:** FENa >2%, abnormal sediment.
       - ATN: muddy brown granular casts; ischemic or nephrotoxic (vanc, gent, contrast, cisplatin)
       - AIN: WBCs, WBC casts, eosinophiluria; drug-induced (PPI, NSAID, antibiotics)
       - GN: RBC casts, dysmorphic RBCs, proteinuria
       - Vascular: thrombotic microangiopathy, atheroembolic
     - **Postrenal:** obstruction — bladder scan + renal US; BPH, stones, retroperitoneal mass.

6. **Calcium.** Correct for albumin: corrected Ca = measured Ca + 0.8 × (4 − albumin). Or order ionized Ca.
   - **Hypercalcemia:** PTH-mediated (primary or tertiary hyperparathyroidism) vs PTH-independent (malignancy via PTHrP or bone mets, granulomatous disease, vitamin D toxicity, milk-alkali, immobilization, thiazides, lithium). Severe (>14 or symptomatic) → IV fluids 200–300 mL/hr NS, calcitonin 4 units/kg q12h for 24–48h, IV bisphosphonate (zoledronic acid 4 mg) for malignancy, denosumab if AKI present.
   - **Hypocalcemia:** check Mg first (low Mg causes functional hypoparathyroidism). Causes: hypoparathyroidism (post-surgical), vitamin D deficiency, CKD, pancreatitis, sepsis, citrate from massive transfusion, tumor lysis. Symptomatic (Chvostek, Trousseau, tetany, seizures, prolonged QT) → IV calcium gluconate 1–2 g IV over 10–20 min.

7. **Liver enzymes (CMP).**
   - **Hepatocellular pattern:** AST/ALT predominantly elevated, ALP/bili relatively spared. AST:ALT >2 with both elevated <300 → alcoholic. ALT >>AST with ALT >1000 → viral hepatitis, drug (acetaminophen), ischemic, autoimmune. ALT 1.5–5× ULN → NAFLD, chronic viral hepatitis, hemochromatosis, Wilson, A1AT.
   - **Cholestatic pattern:** ALP and direct bili predominantly elevated. Confirm hepatic ALP (not bone) with GGT. Imaging (RUQ ultrasound) to distinguish intrahepatic (PBC, PSC, drug) vs extrahepatic (stone, stricture, mass — MRCP, ERCP).
   - **Mixed pattern:** drug-induced liver injury, sepsis, congestion (right heart failure).
   - **R factor** = (ALT/ULN) / (ALP/ULN): >5 hepatocellular, <2 cholestatic, 2–5 mixed.
   - Synthetic function: albumin (chronic), INR (acute), bili. Acute liver failure = INR >1.5 + encephalopathy + no prior liver disease. Transfer to transplant center.

8. **Albumin / total protein.** Low albumin: malnutrition, liver synthetic failure, nephrotic syndrome, inflammation (negative acute phase), protein-losing enteropathy. Globulin gap (TP − albumin) elevated → consider monoclonal gammopathy (SPEP).

## Output Format

```
GLUCOSE: [value, action]
SODIUM: [value, volume status, expected etiology]
POTASSIUM: [value, action]
ACID-BASE: [HCO3, anion gap if calculable]
RENAL: [BUN, Cr, eGFR, baseline comparison, AKI stage if applicable, prerenal/intrinsic/postrenal]
CALCIUM: [corrected Ca, action]
LIVER (if CMP): [pattern: hepatocellular / cholestatic / mixed; synthetic function]
ALBUMIN: [value, interpretation]

PATTERN: [most clinically significant story]
ACTION:
1. [most urgent intervention]
2. [next labs / imaging]
3. [follow-up timing]
```

## False-Positive Prevention

- **Corrected calcium computed in mixed units.** Recompute it and show the arithmetic: Ca (mg/dL) + 0.8 × (4 − albumin g/dL), or in SI Ca (mmol/L) + 0.02 × (40 − albumin g/L). In critical illness, CKD, or very low albumin the correction is unreliable, so ask for ionized calcium before calling it normal.
- **Ratios and cut-offs applied to SI results without converting.** Convert creatinine µmol/L ÷ 88.4, urea mmol/L × 2.8 (to BUN mg/dL), and glucose mmol/L × 18 before using a BUN/Cr >20, a glucose-corrected sodium, or any mg/dL threshold in this prompt. Judge each analyte against the reporting lab's range, not the defaults written here.
- **eGFR and AKI stage given as if the creatinine were stable.** CKD-EPI assumes steady state and overestimates function while creatinine is rising, so label it. State the KDIGO criterion that was met with the ratio to a baseline actually supplied; with no baseline, say AKI vs CKD is undetermined rather than staging it.
- **Hyponatremia labelled "hypotonic" without a measured osmolality.** Compute the glucose-corrected Na (+2.4 per 100 mg/dL above 100) and ask for serum osmolality before ruling out pseudohyponatremia or a hypertonic cause.
- **Correction rate and potassium judged from a single draw.** Calculate the Na change per hour from the timestamps of successive results, not "per 24 h" by assumption. Before acting on a high K, check for a hemolyzed sample, extreme leukocytosis or thrombocytosis, or a whole-blood gas K being compared with serum.

## Worked Example

**Input:** 76 y/o F, 3 days vomiting and poor PO intake, history of HTN on lisinopril/HCTZ. BP 92/58 (baseline 142/82), HR 108, weight 60 kg. Today: Na 128, K 2.9, Cl 88, HCO3 30, BUN 48, Cr 1.8 (baseline 0.9), glucose 96, Ca 8.8, albumin 3.2, AST 24, ALT 22, ALP 88, total bili 0.6.

**Output:**

```
GLUCOSE: 96 — normal.
SODIUM: 128 — hyponatremia. Vitals (HR 108, BP drop from 142 → 92) and history (vomiting, poor PO) → hypovolemic hyponatremia with concurrent ADH-driven free water retention. Tonicity not established — serum osmolality not provided; glucose 96 needs no correction, so a hypertonic cause is unlikely, but send serum osm before excluding pseudohyponatremia. Will correct with isotonic resuscitation but watch rate.
POTASSIUM: 2.9 — hypokalemia. Cause is multifactorial: vomiting (gastric H+ loss with secondary HCO3 retention drives K into cells; renal K wasting from contraction alkalosis), HCTZ (chronic), poor intake. Replace K and Mg.
ACID-BASE: HCO3 30, no ABG provided. Anion gap = 128 − (88 + 30) = 10 → normal. Pattern: contraction alkalosis from vomiting + diuretic. Consistent with HCO3 30.
RENAL: Cr 1.8 from baseline 0.9 = 2× → AKI stage 2. BUN/Cr = 27 → consistent with prerenal. eGFR (CKD-EPI) ~30 mL/min/1.73m² acutely. ACE inhibitor + diuretic + volume depletion is the classic triple hit driving prerenal AKI.
CALCIUM: 8.8 measured, albumin 3.2 → corrected = 8.8 + 0.8 × (4 − 3.2) = 9.4. Normal.
LIVER: Within normal limits.
ALBUMIN: 3.2 — mildly low, consistent with acute illness / poor intake. No protein gap concern.

PATTERN: Volume-depleted elderly woman with hypovolemic hyponatremia (presumed hypotonic; serum osm pending), hypokalemic contraction alkalosis, and prerenal AKI driven by vomiting + ACE inhibitor + thiazide.

ACTION:
1. Hold lisinopril and HCTZ. Resume only after Cr returns to baseline and a different regimen is selected (ACE/diuretic combo is high-risk in this patient).
2. IV fluid resuscitation: NS 1 L bolus over 1 hour, reassess BP and HR. Then NS at 100–125 mL/hr. With volume repletion, ADH suppresses and Na will correct — watch the rate. Target Na correction <8 mEq/L per 24h to avoid osmotic demyelination. Recheck Na in 4 hours, then q4–6h.
3. Replace K: 40 mEq KCl PO once now (if tolerating PO) or 10 mEq/hr IV peripheral if NPO. Recheck K with next BMP. Replace Mg empirically with 2 g IV magnesium sulfate.
4. Workup vomiting cause: focused history (med changes, dietary, infection, abdominal pain). If persistent, consider AXR / CT abdomen for obstruction; lipase if epigastric pain.
5. Watch UOP. Foley if mental status declines or output unclear. Repeat BMP in 6 hours.
6. K may rise as volume repletion lowers aldosterone-driven renal K loss and the alkalosis corrects — recheck K before each further supplement rather than assuming the deficit persists.
```
