---
title: "DOAC Selection by Patient Profile"
category: domain-healthcare-clinical/pharmacology
description: "Choose between apixaban, rivaroxaban, dabigatran, and edoxaban for AFib stroke prevention, VTE treatment/prevention, or other indications based on renal function, bleeding risk, drug interactions, GI tolerance, dosing complexity, and weight; specify drug, dose, and monitoring."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: intermediate
tags:
  - cardiology
  - hematology
  - anticoagulation
  - doac
  - drug-selection
updated: "2026-05-12"
---

## Objective

Select the right direct oral anticoagulant (DOAC) for a specific patient and indication: match the agent to renal function, age, weight, bleeding risk, drug interactions, indication-specific evidence, GI tolerance, dose-adjustment rules, and reversibility. Output a written prescription with rationale, monitoring, and patient counseling.

## Inputs

- Indication (AFib stroke prevention with CHA₂DS₂-VASc; acute VTE treatment; extended VTE prophylaxis; post-PCI / triple therapy; LVAD; cancer-associated thrombosis; mechanical valve — DOAC contraindicated; antiphospholipid syndrome — DOAC contraindicated for triple-positive)
- Age, weight (esp. extremes: <60 kg, >120 kg), sex
- Renal function (CrCl by Cockcroft-Gault using ABW)
- Hepatic function (Child-Pugh)
- Bleeding risk factors (HAS-BLED for AFib; prior GI bleed, intracranial hemorrhage)
- Concomitant medications (P-gp and CYP3A4 inhibitors / inducers; NSAIDs; antiplatelets; SSRIs)
- GI tolerance and history of dyspepsia
- Adherence likelihood (BID vs daily dosing)
- Reversibility need (procedural risk)
- Insurance / cost considerations

## Role

Senior internist / cardiologist / hematologist writing the DOAC prescription with explicit reasoning for selection.

## Reasoning Steps

1. **Confirm DOAC is appropriate for the indication.**
   - **DOAC appropriate:** non-valvular AFib (no mechanical valve, no moderate-severe mitral stenosis), VTE (DVT/PE), extended VTE prophylaxis, post-hip/knee replacement VTE prophylaxis, recent ACS (limited indications), cancer-associated thrombosis (apixaban, edoxaban, rivaroxaban with caveats).
   - **DOAC not appropriate / use warfarin:** mechanical heart valve (RE-ALIGN dabigatran failed), moderate-to-severe mitral stenosis (rheumatic), triple-positive antiphospholipid syndrome (TRAPS — rivaroxaban inferior), advanced CKD with CrCl <15 / dialysis (some apixaban data, generally warfarin).
   - **Pregnancy:** all DOACs contraindicated; use LMWH.

2. **Map renal function to dose adjustments.**
   - **Apixaban (AFib dose):** 5 mg PO BID standard; reduce to 2.5 mg PO BID if any 2 of: age ≥80, weight ≤60 kg, SCr ≥1.5 mg/dL.
     - Acute VTE: 10 mg BID × 7 days, then 5 mg BID for 6 months, then 2.5 mg BID extended prophylaxis if indicated.
     - CrCl <15 / HD: not officially FDA-recommended for AFib but used off-label with caution (ARISTOTLE excluded; some renal-replacement data).
   - **Rivaroxaban (AFib):** 20 mg PO daily with food; 15 mg daily if CrCl 15–50; avoid if CrCl <15.
     - Acute VTE: 15 mg BID × 21 days → 20 mg daily × 6 months → 10 mg daily extended.
     - Post-orthopedic VTE prophylaxis: 10 mg daily.
   - **Dabigatran (AFib):** 150 mg PO BID; 75 mg BID if CrCl 15–30. Avoid if CrCl <15.
     - 80% renal elimination — least suitable for renal impairment of the four.
   - **Edoxaban (AFib):** 60 mg PO daily; 30 mg daily if CrCl 15–50, weight ≤60 kg, or strong P-gp inhibitor.
     - **Do NOT use edoxaban for AFib if CrCl >95** (ENGAGE AF post-hoc showed reduced efficacy at supratherapeutic clearance).
     - VTE: 60 mg daily (or 30 mg with adjustment criteria).

3. **Account for weight extremes.**
   - **Low body weight (<60 kg):** apixaban dose reduction trigger; edoxaban dose reduction; rivaroxaban no specific reduction but bleeding risk higher.
   - **High body weight (>120 kg or BMI >40):** ISTH 2021 guidance accepted DOACs for VTE in obese; preferred apixaban or rivaroxaban given more obesity data. For AFib in extreme obesity, ongoing debate; trough levels can be checked at specialty centers. Warfarin remains an option in patients >150 kg with extra-large body habitus.

4. **Drug–drug interactions.**
   - **Strong P-gp and CYP3A4 inhibitors** (raise DOAC levels → bleeding):
     - Azoles (itraconazole, ketoconazole, voriconazole, posaconazole) — avoid combination, or reduce DOAC dose if no alternative.
     - Macrolides (clarithromycin, erythromycin) — short-course concern less than chronic.
     - HIV protease inhibitors (ritonavir-boosted regimens).
     - Cyclosporine, tacrolimus (moderate inhibition).
   - **Strong P-gp and CYP3A4 inducers** (lower DOAC levels → thrombosis):
     - Rifampin, phenytoin, carbamazepine, phenobarbital, St. John's wort — generally avoid concomitant; consider warfarin instead.
   - **Apixaban**: strong dual P-gp + CYP3A4 inhibitor (azole) → reduce to 2.5 mg BID for AFib; avoid with strong inducer.
   - **Rivaroxaban**: same — avoid with strong CYP3A4 inhibitors / inducers.
   - **Dabigatran**: P-gp interactions only (no CYP); P-gp inhibitor (dronedarone, ketoconazole, verapamil) → reduce dose to 75 mg BID if CrCl 30–50; avoid combination if CrCl <30.
   - **Edoxaban**: strong P-gp inhibitor → reduce dose to 30 mg daily.
   - **NSAIDs, aspirin, P2Y12:** additive bleeding risk; minimize concomitant use; if dual or triple therapy needed (post-PCI), limit duration per AUGUSTUS/PIONEER AF-PCI data.

5. **Indication-specific selection.**
   - **AFib, no comorbidity-defining factor:** apixaban often first-choice (lowest bleeding rate in ARISTOTLE, including ICH and GI; BID dosing).
   - **AFib with prior GI bleed:** apixaban preferred (less GI bleeding than rivaroxaban, dabigatran).
   - **AFib with adherence concern:** rivaroxaban once-daily; edoxaban once-daily.
   - **AFib with dyspepsia:** apixaban (dabigatran has highest dyspepsia rate, ~10%).
   - **VTE acute:** apixaban (10 BID → 5 BID) or rivaroxaban (15 BID → 20 daily). Both have lead-in dosing.
   - **VTE in cancer:** apixaban (Caravaggio), edoxaban (Hokusai-VTE Cancer); both non-inferior to LMWH with possibly less major bleeding. LMWH (enoxaparin, dalteparin) still first-line in some GI / GU cancers due to bleeding signal with rivaroxaban (SELECT-D).
   - **Post-PCI AFib (dual therapy):** apixaban + P2Y12 inhibitor (AUGUSTUS); duration of triple therapy minimized (1 week or none in some).
   - **Cardioversion:** any DOAC ≥3 weeks before cardioversion, or TEE-guided immediately.
   - **LVAD:** mostly warfarin; DOACs investigational.

6. **Reversibility considerations.**
   - **Idarucizumab** for dabigatran (5 g IV, restores thrombin time within minutes).
   - **Andexanet alfa** for apixaban / rivaroxaban (high or low dose by recent intake; expensive, limited availability).
   - **4-factor PCC** as alternative for any DOAC (50 units/kg) when reversal agent unavailable.
   - For elective procedures, see periprocedural anticoagulation prompt.

7. **Patient counseling.**
   - Adherence is critical (no level monitoring; short half-life means missed doses → quick loss of anticoagulation).
   - Take with food (rivaroxaban absorption depends on food at higher doses).
   - Watch for bleeding signs; report immediately.
   - Avoid NSAIDs.
   - Tell every provider you're on a blood thinner; bring updated list.
   - Cost: brand-name DOACs expensive; generic dabigatran available; insurance / 90-day supply / manufacturer assistance.

8. **Document the plan.**

## Output Format

```
PATIENT SNAPSHOT:
- Indication, demographics, weight, CrCl, comorbidities, bleeding history, current medications

DOAC SELECTION:
- Drug: [name]
- Dose: [mg] PO [frequency]
- Dose adjustment criteria triggered: [list any that applied]

RATIONALE:
- Indication match (with evidence base)
- Renal function fit
- Weight considerations
- Drug interaction profile
- Bleeding-risk fit (e.g., apixaban for low GI bleed risk)
- Convenience (BID vs daily)

CONTRAINDICATIONS REASSESSED:
- Mechanical valve: no
- Rheumatic mitral stenosis: no
- Triple-positive antiphospholipid: no
- Pregnancy: no
- CrCl <15 / HD: assessed

DRUG–DRUG INTERACTIONS:
- [Specific medications and rationale for any dose change or avoidance]

MONITORING:
- Renal function: CrCl every 6 months at minimum; more often if CrCl <50 or unstable
- Hepatic function: yearly LFTs
- CBC: yearly hemoglobin (occult bleeding)
- Clinical: bleeding signs, adherence review

PATIENT COUNSELING:
- Adherence (no level monitoring), take with food (if rivaroxaban), avoid NSAIDs, report bleeding, share medication list
- Bridging for procedures: see periprocedural plan
- Reversal agent availability if needed

WHEN TO CHANGE OR DISCONTINUE:
- Major bleed → hold, reverse if needed
- Recurrent thrombosis on therapeutic DOAC → reassess (level testing at specialty center; consider warfarin or LMWH)
- Renal deterioration: dose adjust per CrCl table
- New mechanical valve / pregnancy: switch to warfarin / LMWH

FOLLOW-UP:
- 1 month, 3 months, then every 6 months
- Anticoagulation clinic referral if available
```

## Worked Example

**Input:** 78-year-old woman, ABW 54 kg, SCr 1.6 (CrCl 28), AFib with CHA₂DS₂-VASc 6 (prior stroke 2 years ago), on amiodarone, no major bleeding history, mild dyspepsia. No mechanical valve. Wants to start anticoagulation.

**Output:**

```
PATIENT SNAPSHOT:
- 78 y F, 54 kg, CrCl 28, AFib CHA₂DS₂-VASc 6 with prior CVA, on amiodarone (CYP3A4 + P-gp inhibitor), mild dyspepsia. No prior GI bleed.

DOAC SELECTION:
- **Apixaban 2.5 mg PO BID** (dose-reduction criteria met: age ≥80? close — age 78 + weight ≤60 kg + SCr ≥1.5 → 2 of 3 criteria triggered, **reduce to 2.5 mg BID**).

RATIONALE:
- Indication: AFib stroke prevention; high stroke risk (CHA₂DS₂-VASc 6 with prior CVA).
- Renal: CrCl 28 — apixaban appropriate (dabigatran less safe at CrCl <30, rivaroxaban acceptable but dose 15 mg daily).
- Weight: 54 kg → low body weight criterion met for apixaban dose reduction.
- Drug interactions: amiodarone is a mild-moderate P-gp inhibitor — apixaban package insert does not mandate further reduction beyond the criteria-based reduction; clinically often kept at 2.5 mg BID for caution.
- Bleeding profile: apixaban has lowest ICH and GI bleed rates of DOACs in ARISTOTLE.
- Dyspepsia: dabigatran has highest dyspepsia rate (~10%); apixaban tolerated better.

CONTRAINDICATIONS REASSESSED:
- No mechanical valve, no rheumatic MS, no APS, not pregnant, CrCl 28 (above HD threshold).

DRUG–DRUG INTERACTIONS:
- Amiodarone (CYP3A4 + P-gp mild inhibitor) — apixaban dose already at reduced 2.5 mg BID; no further adjustment required.
- NSAIDs: counsel to avoid.
- No SSRI, no rifampin, no azole, no protease inhibitor on current list.

MONITORING:
- CrCl at 1, 3, 6 months and then every 6 months (CrCl 28 — close to dose-reduction threshold; will not change apixaban dosing further as currently at min, but if CrCl <15 or HD, reassess).
- LFTs yearly.
- Hemoglobin yearly.
- Bleeding-screen and adherence at each visit.

PATIENT COUNSELING:
- Take with or without food, BID dosing — set phone reminders.
- Avoid NSAIDs, aspirin, naproxen, ibuprofen.
- Report any bruising, blood in stool/urine, headache, fall.
- Carry medication list with "on apixaban — blood thinner."
- Bridging for any procedure: discuss with prescriber.
- Reversal agent (andexanet) available at most hospitals; 4F-PCC alternative.

WHEN TO CHANGE OR DISCONTINUE:
- Major bleeding → hold, consider andexanet or PCC, evaluate source.
- New mechanical valve or pregnancy: switch to warfarin/LMWH.
- CrCl decline to dialysis: discuss with specialist (apixaban off-label in HD with limited data).
- Newly initiated rifampin, phenytoin: switch off DOAC.

WHY NOT [ALTERNATIVES]:
- Warfarin: still very reasonable in this patient; would be acceptable with INR target 2–3. DOAC chosen for predictable PK and reduced ICH rate.
- Dabigatran: 80% renal clearance; CrCl 28 close to threshold and dyspepsia history.
- Rivaroxaban: 15 mg daily at CrCl 28 acceptable; daily dosing favorable for adherence; bleeding rates higher than apixaban especially GI; reasonable alternative.
- Edoxaban: 30 mg daily for CrCl 15–50 and weight ≤60 kg; reasonable alternative.

FOLLOW-UP:
- 1 month: tolerability, dyspepsia, bleeding signs.
- 3 months: CrCl, hemoglobin.
- 6 months and every 6 months thereafter.
```
