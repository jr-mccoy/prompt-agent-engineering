---
title: "Immunosuppression Regimen Design"
category: domain-healthcare-clinical/pharmacology
description: "Design and monitor an immunosuppression regimen for solid-organ transplant, autoimmune disease, or hematologic indications by induction agent, maintenance triple therapy (CNI + antimetabolite + steroid), drug levels, infection prophylaxis, malignancy surveillance, and dose-adjustment rules."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
  - QA-01
difficulty: advanced
tags:
  - transplant
  - rheumatology
  - immunosuppression
  - prophylaxis
  - drug-monitoring
updated: "2026-05-12"
---

## Objective

Design and manage an immunosuppression regimen tailored to a specific indication: select induction agent (basiliximab, ATG, alemtuzumab) for transplant, choose triple-therapy maintenance (calcineurin inhibitor + antimetabolite + steroid) or alternative (belatacept, mTOR-inhibitor), set drug-level targets, mandate infection and malignancy surveillance, and specify dose-modification rules for rejection, infection, toxicity, and drug-drug interactions.

## Inputs

- Indication (kidney, liver, heart, lung, pancreas, intestinal transplant; HSCT; autoimmune disease — SLE, vasculitis, MS, RA, IBD)
- Patient: age, weight, comorbidities (DM, CKD, hypertension, hepatitis B/C, HIV, malignancy history), pregnancy status
- HLA matching, panel-reactive antibodies (PRA), donor specific antibodies (DSA) for transplant
- CMV serostatus of donor and recipient (D/R: D+/R−, D+/R+, D−/R+, D−/R−)
- Hepatitis B/C, HIV, EBV, VZV, syphilis, latent TB status
- Current medications (CYP3A4 / P-gp interactions)
- Vaccination history
- Prior immunosuppression and rejection events

## Role

Senior transplant nephrologist / hepatologist / cardiologist / pulmonologist / rheumatologist writing the regimen with explicit reasoning, drug-level targets, and surveillance schedule.

## Reasoning Steps

1. **Define rejection-risk stratification (transplant context).**
   - **High immunologic risk:** prior transplant, high PRA, DSA present, retransplant, ABO-incompatible, HLA-mismatched, African-American kidney recipient.
   - **Standard risk:** primary transplant, low PRA, well-matched.
   - Higher risk drives stronger induction (ATG vs basiliximab) and tighter maintenance levels early.

2. **Choose induction therapy (transplant).**
   - **Basiliximab** (anti-CD25 mAb): 20 mg IV day 0 and day 4. Low-risk induction; well tolerated; common in liver and standard-risk kidney.
   - **Anti-thymocyte globulin (ATG, rabbit — Thymoglobulin)**: 1.5 mg/kg/day IV ×3–7 days; deeper T-cell depletion; reserved for high-risk, sensitized, retransplant; or for treating acute rejection (5–7 days at 1.5 mg/kg).
     - Premedicate: methylprednisolone, diphenhydramine, acetaminophen.
     - Toxicities: cytokine release first dose, leukopenia, thrombocytopenia, serum sickness, PTLD long-term, infection.
   - **Alemtuzumab (anti-CD52 mAb)**: 30 mg SC × 1; profound and durable T- and B-cell depletion; used in selected transplant contexts and MS.

3. **Maintenance regimen — triple therapy (standard) or alternatives.**
   - **Calcineurin inhibitor (CNI):**
     - **Tacrolimus (Prograf, Astagraf, Envarsus)** — most common; binds FKBP12 → inhibits calcineurin → blocks NFAT → blocks IL-2 transcription → T-cell activation suppressed.
       - Trough target (whole blood, immediately pre-dose):
         - Months 0–3 post-transplant: 8–12 ng/mL.
         - Months 3–12: 6–10 ng/mL.
         - >12 months: 4–8 ng/mL.
         - Higher targets if rejection / sensitized; lower if BK / CMV / nephrotoxicity.
       - Side effects: nephrotoxicity, neurotoxicity (tremor, headache), new-onset diabetes after transplant (NODAT), hypertension, hyperkalemia, hypomagnesemia, alopecia.
       - Many drug interactions (CYP3A4): azoles, macrolides, diltiazem, verapamil, grapefruit increase levels; rifampin, phenytoin, carbamazepine, St. John's wort decrease levels.
     - **Cyclosporine (Neoral, Sandimmune):** alternative; less neurotox but more gingival hyperplasia, hirsutism, hypertension; CYP3A4 metabolism similar.
   - **Antimetabolite:**
     - **Mycophenolate (mycophenolate mofetil / MMF — CellCept; mycophenolate sodium — Myfortic)**: 1000 mg PO BID (or 720 mg EC BID). Inhibits IMPDH → blocks de novo guanine synthesis → suppresses lymphocyte proliferation.
       - Side effects: GI (diarrhea, nausea), leukopenia, anemia, increased infection.
       - Teratogenic — pregnancy contraindicated; counsel contraception.
     - **Azathioprine** (older alternative; 1–2 mg/kg PO daily). Check TPMT before starting; severe myelosuppression in TPMT-deficient. Use in pregnancy if mycophenolate not feasible.
   - **Corticosteroid:**
     - **Prednisone** maintenance after transplant taper: 5 mg PO daily long-term in many centers; some practice steroid-free maintenance after induction with ATG.
     - **Methylprednisolone** for rejection treatment (500–1000 mg IV daily ×3 doses).
   - **Alternatives / additions:**
     - **Belatacept (Nulojix)**: CTLA-4-Ig fusion blocking CD28 co-stimulation. IV monthly. EBV-seronegative recipients excluded (PTLD risk). Less nephrotoxic than CNI; first-line in selected kidney transplant.
     - **mTOR inhibitors (sirolimus, everolimus)**: less nephrotoxic, antitumor, anti-CMV, anti-vasculopathy. Side effects: hyperlipidemia, mouth ulcers, pneumonitis, impaired wound healing (avoid in first 3 months post-op), proteinuria, edema.
     - **Rituximab (anti-CD20)**: for ABO-incompatible transplant, antibody-mediated rejection, autoimmune disease (vasculitis, lupus nephritis), PTLD.
     - **Plasmapheresis + IVIG**: desensitization protocols, antibody-mediated rejection.

4. **Autoimmune-disease regimens (specific patterns).**
   - **SLE — lupus nephritis induction:** mycophenolate 2–3 g/day or cyclophosphamide (Euro-Lupus 500 mg q2wk ×6; NIH high-dose monthly); add glucocorticoid; consider belimumab + voclosporin (NEPTUNE / AURORA).
   - **ANCA vasculitis induction:** rituximab 375 mg/m² weekly ×4 or 1 g ×2 (RAVE, RITUXVAS); + steroid (avacopan can replace high-dose steroid in select cases).
   - **MS:** ocrelizumab (anti-CD20), natalizumab, fingolimod, dimethyl fumarate, glatiramer, IFN-β, alemtuzumab, cladribine.
   - **RA:** methotrexate first-line + folic acid; TNF inhibitor or other biologic as add-on; JAKi.
   - **IBD:** azathioprine, methotrexate, anti-TNF (infliximab, adalimumab), anti-IL-12/23 (ustekinumab), anti-integrin (vedolizumab), JAKi (upadacitinib), S1P modulator (ozanimod).

5. **Infection prophylaxis.**
   - **CMV:**
     - High-risk (D+/R−): valganciclovir 900 mg PO daily (renal-adjust) for 200 days (kidney) or 6–12 months (heart/lung).
     - Moderate (R+): valganciclovir 100–200 days, or pre-emptive monitoring with PCR weekly and treat if rising.
     - Low (D−/R−): no antiviral prophylaxis.
   - **PJP (Pneumocystis jirovecii):** TMP-SMX 80/400 mg PO daily or 160/800 three times weekly for 6–12 months post-transplant; lifelong in some lung-transplant recipients. Pentamidine inhaled or atovaquone if sulfa allergy.
   - **Fungal:** fluconazole or itraconazole prophylaxis for select high-risk (liver transplant, neutropenia, induction with ATG).
   - **Hepatitis B reactivation:** entecavir or tenofovir prophylaxis in HBsAg+ or anti-HBc+ patients receiving immunosuppression (especially rituximab, anti-TNF, high-dose steroids).
   - **Latent TB:** screen with IGRA before initiating chronic immunosuppression; treat with INH ×6–9 months or rifapentine + INH (3HP) ×3 months.
   - **Strongyloides:** screen in endemic-area exposures; treat with ivermectin if positive — disseminated strongyloidiasis catastrophic on steroids.
   - **HSV / VZV:** acyclovir or valacyclovir prophylaxis in select transplant (e.g., HSCT).

6. **Vaccination strategy.**
   - **Before transplant:** complete all live vaccines (MMR, varicella, yellow fever) at least 4 weeks before transplant. Inactivated vaccines preferred timing — get pneumococcal, influenza, COVID, Hepatitis B, HPV, shingles (Shingrix — inactivated, safe post-transplant), Tdap.
   - **After transplant:** no live vaccines once on immunosuppression. Inactivated vaccines acceptable — annual flu, COVID updates, pneumococcal, etc.
   - Household contacts: live vaccines OK except oral polio; rotavirus precautions.

7. **Malignancy surveillance.**
   - Skin cancer screening yearly (squamous cell most common; melanoma higher risk); sun protection essential.
   - PTLD (EBV-driven) — high index of suspicion for lymphadenopathy, fever, unusual lymphocytosis; monitor EBV PCR in EBV-mismatched recipients.
   - Cervical cancer (HPV); colon (per usual screening); prostate; breast.
   - Latent HBV: HCC surveillance every 6 months.

8. **Drug-drug interactions.**
   - **CYP3A4 inhibitors increase CNI / mTOR levels:** azoles (fluconazole, itraconazole, voriconazole, posaconazole), macrolides (clarithromycin, erythromycin), diltiazem, verapamil, grapefruit, ritonavir / Paxlovid (nirmatrelvir-ritonavir contraindicated with tacrolimus / cyclosporine / sirolimus without expert management).
   - **CYP3A4 inducers decrease levels:** rifampin, phenytoin, carbamazepine, phenobarbital, St. John's wort.
   - **Allopurinol + azathioprine:** XO inhibition → azathioprine accumulation → severe myelosuppression. Reduce azathioprine to 25% if needed; better to switch to mycophenolate.
   - **TMP-SMX:** raises tacrolimus, additive nephrotoxicity, hyperkalemia.
   - **NSAIDs:** additive nephrotoxicity; avoid.

9. **Rejection management.**
   - Suspect: rising Cr, decreased graft function, donor-specific antibodies, fever.
   - Biopsy-confirmed: Banff classification.
   - Cell-mediated: methylprednisolone 500–1000 mg IV ×3; if steroid-resistant, ATG.
   - Antibody-mediated: plasmapheresis + IVIG + rituximab ± bortezomib + steroid.

## Output Format

```
PATIENT SNAPSHOT:
- Indication, demographics, comorbidities, immunologic risk, donor/recipient serostatus

INDUCTION:
- [Agent + dose + days; rationale based on risk]

MAINTENANCE TRIPLE THERAPY:
- CNI: [drug + starting dose + trough target by post-transplant period]
- Antimetabolite: [drug + dose]
- Steroid: [prednisone taper plan to maintenance dose]
- Alternative: [belatacept / mTOR-inhibitor / rituximab if specific indication]

INFECTION PROPHYLAXIS:
- CMV: [agent + duration based on D/R serostatus]
- PJP: [agent + duration]
- Fungal, HBV, TB latent, Strongyloides as applicable
- HSV/VZV per protocol

VACCINATION STATUS:
- Pre-transplant updates (live vaccines complete)
- Post-transplant inactivated vaccines

MALIGNANCY SURVEILLANCE:
- Skin annually; PTLD vigilance; standard screenings

DRUG-DRUG INTERACTIONS:
- CYP3A4 inhibitor/inducer flags
- TMP-SMX / NSAID / allopurinol caveats

DOSE MODIFICATION / REJECTION ALGORITHM:
- Rejection management protocol
- Infection management (hold antimetabolite first)
- Toxicity (BK virus, CMV, NODAT, nephrotoxicity)

MONITORING SCHEDULE:
- CNI level: pre-dose trough; frequency by post-transplant time
- CBC, CMP, urinalysis, urine protein/Cr (proteinuria)
- BK virus PCR: monthly first 3 months, then trimonthly first year (kidney)
- CMV PCR: weekly if pre-emptive strategy, otherwise per protocol
- DSA monitoring at intervals
- Imaging / Doppler graft per protocol

PATIENT COUNSELING:
- Adherence (critical — nonadherence is leading cause of late graft loss)
- Lab follow-up cadence
- Infection signs and emergency contact
- No live vaccines, no NSAIDs, grapefruit avoidance
- Sun protection; skin self-exam
- Pregnancy planning (avoid mycophenolate; switch to azathioprine)

WHEN TO ESCALATE:
- Acute rejection: pulse steroid → ATG if refractory; transplant team
- Severe infection: hold antimetabolite first, then CNI dose-reduce if necessary
- Drug interaction (e.g., new azole, rifampin): adjust CNI dose, monitor level
```

## Worked Example

**Input:** 47-year-old man receives a deceased-donor kidney transplant. Standard immunologic risk (PRA 5%, no DSA, primary transplant). CMV D+/R−. EBV R+. Latent TB negative. No hepatitis. Outline initial regimen.

**Output:**

```
PATIENT SNAPSHOT:
- 47 y M, primary deceased-donor kidney transplant (DDKT), standard immunologic risk, CMV D+/R− (high CMV risk), EBV R+, latent TB negative, hepatitis B/C negative.

INDUCTION:
- **Basiliximab (Simulect) 20 mg IV on day 0 (intra-op) and day 4.** Standard-risk DDKT.
- Alternative if higher risk emerged (e.g., PRA >50, DSA, retransplant): ATG 1.5 mg/kg/day ×3–5 days.

MAINTENANCE TRIPLE THERAPY:
- **Tacrolimus (Prograf) 0.05–0.1 mg/kg/day PO BID** (twice-daily formulation), titrate to trough:
  - Months 0–3: trough 8–12 ng/mL.
  - Months 3–12: 6–10 ng/mL.
  - >12 months: 4–8 ng/mL.
- **Mycophenolate mofetil (CellCept) 1000 mg PO BID.** Adjust for leukopenia or GI intolerance — reduce by 250 mg or switch to mycophenolate sodium (Myfortic) 720 mg BID.
- **Prednisone**: methylprednisolone 500 mg IV intra-op → 250 mg IV day 1 → oral taper:
  - Day 2: 100 mg PO.
  - Day 3: 50 mg PO.
  - Day 4: 30 mg PO.
  - Tapered weekly to 5 mg PO daily by week 4–6, then maintenance 5 mg PO daily long-term.
  - (Some centers practice rapid steroid taper or steroid-free maintenance after induction; per local protocol.)

INFECTION PROPHYLAXIS:
- **CMV (high risk, D+/R−):** **valganciclovir 900 mg PO daily × 200 days post-transplant** (renal-adjust: at typical post-transplant CrCl 40–60, dose ~450 mg daily). Monitor CMV PCR monthly during prophylaxis and every 1–2 weeks for 3 months after stopping (late-onset CMV risk).
- **PJP:** **TMP-SMX 80/400 mg PO daily × 6–12 months** post-transplant. Alternative if sulfa allergy: dapsone 100 mg daily (check G6PD) or atovaquone 1500 mg daily or pentamidine inhaled monthly.
- **HSV/VZV:** valacyclovir prophylaxis often combined with valganciclovir for CMV; no separate prophylaxis when on valgan.
- **Fungal:** not routine in kidney transplant unless additional risk.
- **HBV:** not applicable here.

VACCINATION STATUS:
- Confirm pre-transplant: pneumococcal (PCV20), influenza (annual), Hepatitis B series, HPV if age-eligible, Tdap, Shingrix (inactivated).
- Post-transplant: annual influenza, COVID updates, pneumococcal boosters; no live vaccines (no MMR, no oral polio, no rotavirus contact in household, no yellow fever).

MALIGNANCY SURVEILLANCE:
- Annual full-body skin exam by dermatologist; sunscreen, hat, sun-protective behavior.
- PTLD vigilance — fever, lymphadenopathy, splenomegaly; EBV PCR if symptoms in this R+ patient (PTLD less likely with EBV+ pre-transplant than EBV-mismatched).
- Standard cancer screenings (colon, prostate, etc.) per age.

DRUG-DRUG INTERACTIONS:
- **No CYP3A4 inhibitors / inducers currently on med list.**
- Warn patient about: grapefruit (avoid), St. John's wort (avoid), Paxlovid (consult transplant team if needed for COVID — significant tacrolimus interaction), azole antifungals (need tacrolimus dose adjustment), rifampin (avoid for TB if possible).
- TMP-SMX prophylaxis at low dose has minimal tacrolimus interaction; monitor.

DOSE MODIFICATION / REJECTION ALGORITHM:
- Rising Cr or new proteinuria → urgent transplant team contact; ultrasound + Doppler; biopsy for unexplained dysfunction.
- Acute cellular rejection: methylprednisolone 500 mg IV ×3 days; if steroid-resistant, ATG 1.5 mg/kg ×5–7 days; intensify maintenance.
- Antibody-mediated: plasmapheresis + IVIG + rituximab.
- BK viremia ≥10,000 copies/mL or BK nephropathy: reduce immunosuppression (lower tacrolimus, reduce/stop mycophenolate); consider mTOR inhibitor switch.
- CMV: switch to oral valganciclovir or IV ganciclovir at treatment doses; reduce mycophenolate.

MONITORING SCHEDULE:
- **Tacrolimus trough**: 2–3 times/week × first month, weekly × month 2, then biweekly to monthly.
- **CBC, CMP, urinalysis, urine protein/Cr ratio**: aligned with tacrolimus levels in first month, then monthly.
- **CMV PCR**: monthly × 6 months (on valgan); pre-emptive surveillance for 3 months post-prophylaxis.
- **BK virus PCR**: monthly months 1–3, every 3 months until 1 year.
- **DSA**: at 1, 3, 6, 12 months.
- **Doppler / ultrasound**: as clinically indicated.
- **Transplant clinic visits**: weekly month 1, biweekly month 2, monthly for 6 months, every 3 months thereafter.

PATIENT COUNSELING:
- Adherence to medications is the single most important factor preventing rejection.
- Same time daily for tacrolimus; if missed dose, take if within 4 hours; otherwise skip.
- Lab work cadence; bring lab results.
- Avoid grapefruit, NSAIDs, St. John's wort, live vaccines.
- Skin protection.
- Pregnancy planning: contraception while on mycophenolate; switch to azathioprine before conception (men also — mycophenolate package insert).
- Watch for: fever, decreased urine output, leg swelling, transplant site pain, BP elevation, new GI symptoms, persistent diarrhea, unusual fatigue or pallor.
- Carry transplant card and medication list.

WHEN TO ESCALATE:
- Rejection signs → transplant team same day.
- New infection symptoms → urgent labs; antimicrobial therapy with transplant input.
- Drug interaction emerges (e.g., new azole started for fungal infection): tacrolimus level needed and dose adjustment.
- Pregnancy planning: switch mycophenolate to azathioprine ≥6 weeks before conception.
```
