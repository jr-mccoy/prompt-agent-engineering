---
title: "Kidney Replacement Therapy Modality Decision"
category: domain-healthcare-clinical/specialty
description: "Plan kidney replacement for advancing CKD: time preparation by KFRE risk, decide when to start (symptoms, not an eGFR number), and match the patient to preemptive transplant, peritoneal dialysis, home or in-center hemodialysis, or conservative kidney management, with access planning."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: advanced
tags:
  - nephrology
  - dialysis
  - ckd
  - shared-decision-making
  - specialty-assessment
  - kidneys-failing
  - fistula-planning
updated: "2026-09-24"
related_prompts:
  - domain-healthcare-clinical/prompts/care-plans/careplan_ckd_staged.md
  - domain-healthcare-clinical/prompts/communication/medicine_goals_of_care_conversation_guide.md
  - domain-healthcare-clinical/prompts/acute-care/acute_severe_hyperkalemia.md
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
> **Review status:** clinical content and doses reviewed by AI only (2026-09-24);
> **not yet reviewed by a licensed clinician.**

## Objective

Produce a nephrologist's kidney-failure life plan for a patient with advancing CKD: when preparation must begin, when dialysis should actually start, which modality (or no dialysis) fits this person's medical profile, home situation, and goals, and the matching access and transplant steps.

Decision support for a licensed clinician: confirm doses, renal adjustment and thresholds against the current guideline and local formulary. A patient with an urgent dialysis indication (step 1) is escalated now, not after this output.

## When to Use

- Advancing CKD (eGFR falling toward 15–20, or a high KFRE risk) where preparation for kidney failure has to start.
- Choosing between transplant, peritoneal dialysis, home or in-center hemodialysis, and conservative (no-dialysis) care with the patient and family.
- Deciding when dialysis should actually begin, and matching vascular or PD access to the chosen modality.

**Not this prompt if:**
- The task is managing CKD progression and complications by stage, or deciding when to refer → [`careplan_ckd_staged.md`](../care-plans/careplan_ckd_staged.md); this prompt makes the modality and timing decision itself.
- The main task is the goals-of-care conversation rather than the modality decision → [`medicine_goals_of_care_conversation_guide.md`](../communication/medicine_goals_of_care_conversation_guide.md).

## Inputs

- Kidney trajectory: eGFR series, UACR, cause of CKD, rate of decline; KFRE inputs (age, sex, eGFR, UACR)
- Uremic and volume status: appetite, nausea, pruritus, cognition, weight loss, edema, dyspnea, pericardial rub, bleeding; potassium, bicarbonate, phosphate, albumin
- Comorbidities: heart failure (EF), CAD, diabetes, peripheral vascular disease, cirrhosis, frailty, cognitive impairment, life expectancy
- Abdominal history: prior surgery, adhesions, hernias, stomas, polycystic kidneys, diverticular disease, obesity
- Vascular access factors: arm vein quality/prior cannulation, PICCs, central venous stenosis, dominant arm, vein mapping
- Function and home: independence, dexterity, vision, caregiver, home space and storage, water and electricity, distance and travel time to dialysis unit
- Work, schooling, travel, and personal goals; values about burden vs longevity
- Transplant candidacy: potential living donors, contraindications (active cancer, uncontrolled infection, severe cardiopulmonary disease, adherence)

## Role

Senior attending nephrologist in a CKD clinic supporting the treating clinician, writing the kidney-failure plan after a modality-education visit.

## Reasoning Steps

1. **Quantify risk and set the preparation clock.** Use the kidney failure risk equation (KFRE) with eGFR and UACR to estimate 2- and 5-year kidney-failure risk. Higher 2-year risk (a common threshold is >40%) or eGFR approaching 15–20 is the signal to complete modality education, transplant referral, and access planning now — preparation takes months.
   - **Stop and escalate now if:** hyperkalemia with ECG changes or persisting despite treatment, pulmonary edema not responding to diuretics, pericardial rub or effusion (uremic pericarditis, tamponade risk), uremic encephalopathy or seizure, uremic bleeding, or severe metabolic acidosis — these are urgent-start indications for same-day nephrology and emergency care, not a planning visit.

2. **Separate "when to start" from "how."** Start dialysis for clinical indications, not an eGFR number: uremic symptoms (serositis, encephalopathy, bleeding, refractory nausea/pruritus), volume overload refractory to diuretics, refractory hyperkalemia or metabolic acidosis, or declining nutritional status attributable to uremia. This usually occurs around eGFR 5–10. Planned early starts at a higher eGFR did not improve outcomes (IDEAL).

3. **Transplant first.** Kidney transplantation offers the best survival and quality of life for eligible patients. Refer early; in the US, waitlist time can accrue once eGFR ≤20 mL/min/1.73m². Preemptive living-donor transplant avoids dialysis entirely — identify potential donors and start their evaluation in parallel.

4. **Offer conservative kidney management (CKM) explicitly** to older patients with high comorbidity, frailty, or limited life expectancy. In such patients, dialysis may add little survival while adding treatment burden and hospital time. CKM includes symptom control, anemia and fluid management, advance care planning, and hospice when appropriate. Present it as an active treatment, not a withdrawal of care.

5. **Screen for peritoneal dialysis suitability.**
   - Favoring PD: residual kidney function, desire for independence/work/travel, long distance to a unit, poor vascular access options, heart failure with need for gentle continuous ultrafiltration, younger age.
   - Absolute barriers: documented loss of peritoneal function or extensive adhesions, uncorrectable mechanical defects (hernia that cannot be repaired, abdominal wall defect, diaphragmatic leak), no ability to perform and no helper.
   - Relative barriers: recent major abdominal surgery, large polycystic kidneys, severe obesity, ostomies, active inflammatory or ischemic bowel disease, severe malnutrition.
   - Options: CAPD (manual exchanges through the day) vs APD (overnight cycler). Assisted PD extends access to patients needing help.
   - Catheter placement ideally ≥2 weeks before planned start; urgent-start PD is possible with low-volume supine exchanges.

6. **Screen for home hemodialysis** — needs a trained partner or independent patient, space, and utilities; more frequent sessions improve volume and phosphate control.

7. **In-center hemodialysis** when home therapies are declined or not feasible, or when medical or social complexity requires supervised treatment.

8. **Plan vascular access to match the life plan.**
   - Protect veins now: from about CKD G3b onward avoid PICCs in either arm and protect the nondominant arm from venipuncture and IVs [VERIFY local vascular-access policy].
   - Arteriovenous fistula needs months to mature; refer to access surgery with vein mapping when HD is the likely modality and kidney failure is expected within about 6–12 months. AV graft if veins are inadequate (usable in weeks; some early-cannulation grafts sooner).
   - Avoid starting HD with a tunneled catheter when a fistula or graft could have been placed; catheters carry the highest infection and mortality risk.
   - A patient choosing PD does not routinely need a backup fistula.

9. **Integrate comorbidity.** Heart failure: PD offers continuous gentle ultrafiltration; in-center HD can cause intradialytic hypotension. Diabetes: PD dextrose load adds glycemic and weight effects — icodextrin for the long dwell. Cirrhosis with ascites: PD is feasible in selected patients. Cognitive impairment: needs a caregiver-supported plan or in-center HD.

10. **Document the decision with the patient's goals** and a contingency: what happens if the chosen modality fails (PD peritonitis/ultrafiltration failure → HD access plan), and the trigger for revisiting CKM.

11. **Verify.** Confirm the start is symptom-driven, transplant referral and donor search are underway if eligible, CKM was offered where relevant, access timing matches the chosen modality, and vein protection orders are in place.

## Output Format

```
RISK AND TIMELINE: [eGFR trend, KFRE 2-/5-year, expected time to kidney failure]

START CRITERIA: [present / not yet — what will trigger initiation]

TRANSPLANT: [eligibility, referral status, living donor steps, waitlist timing]

MODALITY ASSESSMENT:
- CKM: [appropriate to offer? patient view]
- PD: [favoring factors / barriers]
- Home HD: [feasibility]
- In-center HD: [role]

RECOMMENDATION: [modality + rationale tied to goals and medical factors]

ACCESS PLAN: [catheter or fistula/graft, timing, vein protection]

CONTINGENCY: [backup plan; when to revisit]

PITFALLS:
- [starting by eGFR number, late access, catheter starts, CKM not offered, PICC in a future access arm]
```

## Verification

- [ ] KFRE was calculated from the patient's actual age, sex, eGFR and UACR, and the preparation timeline follows from it.
- [ ] Each urgent-start indication is marked present or absent before any elective plan is written.
- [ ] PD barriers are classified as absolute or relative from the documented abdominal history, not assumed from age or BMI.
- [ ] The access plan names the dominant and nondominant arm and states the vein-protection order explicitly.
- [ ] Doses of potassium binders, diuretics and other renally cleared drugs reflect current eGFR; confirm doses, renal adjustment and thresholds against the current guideline and local formulary.

## False-Positive Prevention

- **An eGFR number read as a start indication.** An eGFR of 8–10 in an asymptomatic, well-nourished patient is not by itself a reason to start; IDEAL showed no benefit from planned early starts.
- **Fatigue or nausea attributed to uremia without other causes checked.** Anemia, depression, hypothyroidism, medication effects or heart failure can mimic uremic symptoms and trigger an unnecessary early start.
- **Creatinine-based eGFR mis-estimating function.** Low muscle mass (frailty, amputation) overestimates eGFR and large muscle mass underestimates it — consider cystatin C or measured clearance before timing decisions.
- **Age or one comorbidity taken as PD or transplant ineligibility.** Frailty, heart failure and obesity are relative factors; exclusion needs a specific contraindication or a transplant-center assessment.
- **KFRE applied outside its validated population.** It is validated for CKD G3–G5 not on dialysis; do not use it in AKI or after transplant.

## Worked Example

**Input:** 58 y/o F, diabetic kidney disease, eGFR 24 → 18 → 14 over 18 months, UACR 1,800 mg/g, KFRE 2-year risk ~60%. Mild fatigue, no nausea, pruritus, or edema; K 5.1, HCO₃ 20, albumin 3.8. HFrEF with EF 35%, NYHA II, on GDMT. Prior C-section only; BMI 31. Works full time as a school administrator; lives 70 minutes from the nearest unit. Independent, good dexterity, supportive husband. Right-hand dominant; left forearm veins good on exam, no prior PICC. Her brother has offered to be evaluated as a donor.

**Output:**

```
RISK AND TIMELINE: Steady decline ~7 mL/min/year, KFRE 2-year ~60% → kidney failure likely within ~12–18 months. Prepare now.

START CRITERIA: Not met — no uremic symptoms, volume controlled, K and HCO₃ manageable. Start when uremic symptoms, refractory volume overload, or refractory K/acidosis appear; do not start for an eGFR number.

TRANSPLANT: Eligible on current information (HF NYHA II needs cardiology clearance). Refer to the transplant center now. eGFR 14 — waitlist time can accrue. Brother to begin living-donor evaluation in parallel. Goal: preemptive living-donor transplant.

MODALITY ASSESSMENT:
- CKM: offered and discussed; she prefers dialysis if transplant is not completed in time.
- PD: strongly favored — full-time work, 70-minute distance, HFrEF (continuous gentle ultrafiltration, fewer intradialytic hypotension episodes), independent, supportive spouse, only a prior C-section. BMI 31 is a relative issue, not a barrier.
- Home HD: feasible backup.
- In-center HD: least compatible with her work and distance.

RECOMMENDATION: APD (overnight cycler) as the bridge to preemptive transplant, if transplant cannot be completed first. Icodextrin for the long day dwell to limit dextrose exposure and aid ultrafiltration.

ACCESS PLAN: Refer for PD catheter placement when eGFR ~10 or symptoms begin, at least 2 weeks before anticipated start. No backup fistula. Vein-preservation order: no PICCs in either arm; no venipuncture or IVs in the left (nondominant) arm.

CONTINGENCY: PD failure (recurrent peritonitis, ultrafiltration failure, mechanical problems) → home HD or in-center HD with fistula placement at that time. Revisit the plan every 3 months with eGFR, symptoms, and transplant progress.

PITFALLS:
- Do not start dialysis at eGFR 10 because of a number.
- Do not let a hospital PICC destroy future HD access.
- Heart failure is a reason to favor PD here, not to exclude it.
```
