---
title: "Pediatric Weight-Based Dosing"
category: domain-healthcare-clinical/pharmacology
description: "Compute pediatric drug doses with weight-based or BSA-based dosing, age- and developmental-stage adjustments, neonatal pharmacokinetic considerations, max-dose caps, and double-check for high-risk medications; output a verified order with monitoring."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
  - QA-01
difficulty: advanced
tags:
  - pediatrics
  - dosing
  - neonatology
  - pharmacology
  - safety
updated: "2026-05-12"
---

## Objective

Compute a pediatric medication dose accurately and safely: select correct weight (actual body weight; use age-based estimation in resuscitation; BSA-based dosing for chemotherapy and some specialty drugs), apply age- and stage-specific pharmacokinetic adjustments (neonatal vs infant vs child vs adolescent), respect maximum dose caps to avoid exceeding adult doses, double-check high-alert medications, and specify volume, concentration, and route. Output the prescription with explicit calculation trail.

## Inputs

- Age (specify in days for neonates <30 days, months for infants, years for children)
- Gestational age and post-menstrual age (PMA) for premature / neonatal patients
- Actual body weight (use most current measured weight, not stated weight)
- Length / height for BSA calculation
- Indication and severity
- Renal and hepatic function (eGFR by Schwartz equation in children: eGFR = 0.413 × height (cm) / SCr (mg/dL))
- Drug name, formulation availability (liquid suspension concentration, tablet strengths, IV)
- Route preference (PO if tolerating, IV if NPO or critical, IM, IN, IO)
- Allergy and prior medication history
- Currently weight-band protocols if institution uses them

## Role

Senior pediatrician / pediatric pharmacist / pediatric hospitalist / neonatologist writing the prescription with verified calculation.

## Reasoning Steps

1. **Confirm patient identification and current weight.**
   - Always use the most recently measured weight (within 24 h for inpatient, current visit for outpatient).
   - Never use parent-reported weight for high-alert medications without verifying.
   - For resuscitation in unknown weight: use Broselow tape (length-based) or APLS formula (age-based: 8 + 2×age in years, or 2 × age + 8 = weight in kg, ages 1–10).

2. **Choose dosing strategy.**
   - **Weight-based (mg/kg or units/kg):** most common in pediatrics; uses actual body weight.
   - **Body surface area (BSA, m²):** chemotherapy, some immunosuppressants, some monoclonal antibodies. Mosteller formula: BSA = √[(height_cm × weight_kg) / 3600].
   - **Age-based:** for some emergency drugs (epinephrine 0.01 mg/kg IM/IV; never to exceed 0.3 mg in pediatrics, 0.5 mg in adolescents/adults).
   - **Fixed-dose by age or weight band:** vaccines, some antibiotics, syrup formulations dispensed by mL based on age.

3. **Apply age- and developmental-stage pharmacokinetic principles.**
   - **Absorption:** gastric pH higher in neonates (achlorhydric) — affects oral β-lactam and PPI absorption; slower gastric emptying in infants; intramuscular absorption variable.
   - **Distribution:** higher total body water (especially preterm) increases Vd of hydrophilic drugs (aminoglycosides, beta-lactams) → may need higher mg/kg dose; lower body fat; lower protein binding (especially in neonates, more free drug).
   - **Metabolism:** CYP450 activity matures over months to years; neonates often have reduced CYP3A4, CYP2D6, glucuronidation (UGT). Phase II conjugation immature → bilirubin (jaundice), morphine (lower clearance), chloramphenicol (gray baby syndrome).
   - **Excretion:** renal clearance immature in neonates; matures by ~12 months. GFR < adult normal until ~12 months.
   - **Practical implication:** dosing intervals often longer in neonates; doses per kg may be higher or lower depending on PK.

4. **Apply max-dose caps.**
   - **Never exceed adult dose** even if calculated weight-based dose suggests higher.
   - Common caps:
     - Acetaminophen: 75 mg/kg/day pediatric, max 4 g/day adult.
     - Ibuprofen: 40 mg/kg/day, max 2400 mg/day.
     - Amoxicillin: 80–90 mg/kg/day for high-dose, max 3 g/day.
     - Azithromycin: 10 mg/kg day 1, then 5 mg/kg days 2–5; max 500 mg day 1 then 250 mg.
     - Ceftriaxone: 50–80 mg/kg/day (meningitis 100 mg/kg/day, max 4 g/day).
     - Vancomycin: 10–15 mg/kg/dose, max 1000 mg/dose initially.
     - Furosemide: 1–2 mg/kg/dose IV, max 6 mg/kg/dose.
     - Epinephrine IM/SC for anaphylaxis: 0.01 mg/kg, max 0.3 mg (pediatric autoinjector 0.15 mg for 15–30 kg; 0.3 mg for ≥30 kg).
     - Diphenhydramine: 1 mg/kg/dose, max 50 mg.

5. **Common pediatric drugs with calculated doses.**
   - **Acetaminophen:** 10–15 mg/kg PO/PR q4–6h; max 75 mg/kg/day or 4 g/day.
   - **Ibuprofen:** 5–10 mg/kg PO q6–8h; ≥6 months only.
   - **Albuterol nebulizer:** 2.5 mg in 3 mL NS for ages <2; 2.5 or 5 mg for ages ≥2.
   - **Dexamethasone for croup:** 0.6 mg/kg PO/IM/IV once, max 16 mg.
   - **Ondansetron:** 0.15 mg/kg IV/PO; max 4 mg pediatric (8 mg adolescent).
   - **Ceftriaxone for meningitis:** 100 mg/kg/day IV divided q12h or once daily (max 4 g/day).
   - **Vancomycin:** 15 mg/kg q6h IV (neonates per PNA / GA tables).
   - **Amoxicillin for AOM:** 80–90 mg/kg/day PO divided BID; high-dose for pneumococcal resistance.
   - **Amoxicillin-clavulanate:** 80–90 mg/kg/day amoxicillin component; use ES-600 formulation to avoid excess clavulanate.
   - **Epinephrine 1:1000 IM for anaphylaxis:** 0.01 mg/kg = 0.01 mL/kg; max 0.3 mL (=0.3 mg).
   - **Atropine for bradycardia:** 0.02 mg/kg IV, min 0.1 mg, max 0.5 mg.
   - **Glucose 10% for hypoglycemia:** 5 mL/kg IV bolus (=0.5 g/kg).
   - **Mannitol for ICP:** 0.5–1 g/kg IV over 20–30 min.
   - **3% hypertonic saline:** 3–5 mL/kg IV bolus.
   - **Phenobarbital load (status):** 20 mg/kg IV; second dose 10 mg/kg if needed.
   - **Levetiracetam load:** 60 mg/kg IV (max 4500 mg).
   - **Fosphenytoin load:** 20 PE/kg IV.
   - **Sucrose 24% for procedural pain in neonates:** 0.1–0.5 mL on pacifier or buccally.

6. **Neonatal special considerations.**
   - Use **post-menstrual age (PMA)** for dosing tables (PMA = GA at birth + chronological age in weeks).
   - Aminoglycoside dosing in neonates uses PMA-stratified tables (e.g., gentamicin 4–5 mg/kg q24–48h depending on PMA).
   - Vancomycin neonatal dosing: 10–15 mg/kg/dose q8–24h depending on PMA / SCr.
   - Bilirubin-displacing drugs (ceftriaxone in neonates — avoid in first 30 days, especially with concurrent calcium; sulfonamides — kernicterus).
   - Chloramphenicol — gray baby syndrome from glucuronidation deficiency.
   - Codeine — never in pediatrics post-2017 FDA warning (CYP2D6 polymorphism); avoid in lactating mothers.

7. **Liquid formulation considerations.**
   - State concentration: e.g., amoxicillin 250 mg/5 mL → 10 kg child needs 80 mg/kg/day = 800 mg/day = 400 mg BID = 8 mL BID.
   - Always specify dose in **both mg and mL** to reduce error.
   - Specify **mL** with milliliter syringe (not teaspoon).
   - Round to deliverable volume (0.1 or 0.5 mL increments).

8. **Double-check verification (high-alert drugs).**
   - High-alert pediatric drugs: insulin, opioids, anticoagulants, chemotherapy, sedatives, vasopressors, electrolytes (KCl, NaCl 3%), digoxin.
   - Independent double-check by second nurse or pharmacist for high-alert IV medications.
   - Smart-pump dose limits; alert on extreme deviations.
   - Use mg/kg/dose written, not mg/kg/day, when stating PRN doses.
   - State weight used in calculation in the order.

9. **Renal / hepatic adjustments.**
   - Use Schwartz equation for pediatric eGFR.
   - Adjust dose or interval per drug PK; consult pediatric reference (Lexicomp, Micromedex, Harriet Lane).

10. **Verify before signing.**
    - Patient ID, weight, allergy.
    - Drug, dose, route, frequency, duration.
    - Indication.
    - Max-dose check.
    - Concentration / mL conversion.
    - Monitoring plan.

## Output Format

```
PATIENT SNAPSHOT:
- Age (days/months/years), GA / PMA if neonate
- Current measured weight (kg)
- Height (cm) if BSA-based
- Renal / hepatic function
- Allergies

INDICATION:
[Disease, severity]

DRUG SELECTED:
- Drug name
- Class / mechanism / indication match

DOSING CALCULATION:
- mg/kg or BSA-based: [target dose mg/kg]
- Calculation: [weight × mg/kg] = [mg/dose]
- Max-dose check: [adult max not exceeded]
- Frequency: [q__h or daily / divided]
- Route: [PO / IV / IM / PR / IN / IO]

CONCENTRATION / VOLUME:
- Available formulation: [e.g., suspension 250 mg/5 mL]
- mL per dose: [computed]
- Round to: [deliverable volume]

DURATION:
- [Days; reassessment trigger]

RENAL / HEPATIC / NEONATAL ADJUSTMENT:
- [Applied; cite Schwartz eGFR or PMA-stratified table]

MONITORING:
- Clinical response (vitals, fever, dyspnea, etc.)
- Labs (CBC, CMP, drug levels, INR as relevant)
- Toxicity surveillance specific to drug

CALCULATION SELF-CHECK:
- Weight: [kg, source]
- Dose mg/kg: [within recommended range]
- Daily total: [does not exceed adult max]
- Concentration and mL: [correct]
- Frequency: [appropriate for age and PK]
- High-alert verification: [independent double-check if applicable]

WHEN TO ESCALATE:
- Inadequate response → reassess diagnosis, escalate or switch
- Toxicity or adverse reaction → hold, evaluate
- Renal / hepatic worsening: redose or switch

PATIENT/FAMILY COUNSELING:
- Liquid concentration and mL by syringe (not teaspoon)
- Schedule, food interactions, completion of course
- Adverse-effect monitoring
- Storage (refrigeration for some suspensions)
```

## Worked Example

**Input:** 18-month-old girl, 11 kg, presents with acute otitis media. No allergies. Otherwise healthy. Tympanic membrane bulging, fever 38.5°C. Compute and write the antibiotic order.

**Output:**

```
PATIENT SNAPSHOT:
- 18-month-old female, weight 11 kg (measured today), no allergies, no chronic medical conditions, no prior antibiotic in last 30 days.

INDICATION:
- Acute otitis media (AOM), moderate (TM bulging, fever 38.5°C); meets criteria for antibiotic treatment per AAP 2013 guidelines (age <2 with bilateral or moderate-severe symptoms; this patient has bulging TM + fever ≥38.5°C → treat).

DRUG SELECTED:
- **Amoxicillin** (first-line for AOM per AAP; covers Strep pneumoniae, non-typeable H. influenzae beta-lactamase-negative, M. catarrhalis).
- High-dose because of S. pneumoniae resistance patterns: **90 mg/kg/day** divided BID.

DOSING CALCULATION:
- Target: 90 mg/kg/day = 90 × 11 = 990 mg/day.
- Divided BID = 495 mg per dose, twice daily.
- Round to deliverable: **500 mg PO BID.**
- Max-dose check: adult max amoxicillin for AOM ~3 g/day; 990 mg/day is well below adult max.
- Frequency: BID for amoxicillin in AOM (some guidelines TID at 80 mg/kg/day; BID at 90 mg/kg/day is widely accepted and improves adherence).
- Route: PO.

CONCENTRATION / VOLUME:
- Available: amoxicillin suspension **400 mg/5 mL** (most common for high-dose).
- mL per dose: 500 mg / (400 mg / 5 mL) = 6.25 mL.
- Round to deliverable: **6.25 mL PO BID** (use oral syringe — 6 mL or 6.5 mL acceptable; specify 6.25 mL for precision).
- Alternative concentration: 250 mg/5 mL → 10 mL BID (larger volume).

DURATION:
- **10 days** for AOM in child <2 years per AAP. (5-day course OK for children ≥6 years without severe symptoms.)

RENAL / HEPATIC ADJUSTMENT:
- Normal renal function — no adjustment.

MONITORING:
- Fever curve, ear pain trend at 48–72 h.
- If not improving by 48–72 h, reassess in clinic; consider amoxicillin-clavulanate (treatment failure / beta-lactamase production).
- Diarrhea, rash, oral thrush monitoring.

CALCULATION SELF-CHECK:
- Weight: 11 kg (measured today). ✓
- Dose: 90 mg/kg/day = 990 mg/day; per dose 500 mg BID. ✓
- Daily total: 990 mg < adult max 3 g/day. ✓
- Concentration: 400 mg/5 mL → 6.25 mL per dose. ✓
- Frequency: BID appropriate. ✓
- High-alert: not applicable (oral amoxicillin not on high-alert list).

WHEN TO ESCALATE:
- No improvement in 48–72 h: switch to amoxicillin-clavulanate 90 mg/kg/day of amoxicillin component (use ES-600 = 600 mg amoxicillin + 42.9 mg clavulanate per 5 mL); 6.25 mL PO BID.
- Severe allergy or beta-lactam intolerance: cefdinir 14 mg/kg/day PO daily (max 600 mg) ×10 days; or ceftriaxone IM 50 mg/kg ×3 days if oral not tolerated.
- Recurrent AOM (≥3 in 6 months or ≥4 in 12 months): ENT referral for tympanostomy tubes consideration.

PATIENT/FAMILY COUNSELING:
- Suspension: shake well before each dose.
- Refrigerate (per manufacturer); discard after 14 days.
- Use oral syringe (not teaspoon).
- Give 6.25 mL twice daily for 10 days; complete entire course even if better.
- Symptoms of allergic reaction: rash, swelling, hives, breathing trouble → ED.
- GI upset, loose stools common; severe diarrhea / blood → call.
- Acetaminophen 10–15 mg/kg PO q4–6h prn for fever / pain.
- Follow-up in clinic if no improvement in 48–72 h or worsening at any time.
```
