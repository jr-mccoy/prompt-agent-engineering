---
title: "HIV Initial Visit and ART Start"
category: domain-healthcare-clinical/specialty
description: "Run the first HIV visit: confirm the diagnosis, draw the complete baseline panel, decide same-day vs deferred ART (cryptococcal/TB meningitis exceptions), apply regimen-selection logic against guideline-dependent choices, and start OI prophylaxis by CD4."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: advanced
tags:
  - infectious-disease
  - hiv
  - antiretroviral
  - specialty-assessment
  - newly-diagnosed
  - first-clinic-visit
  - same-day-treatment
updated: "2026-09-24"
related_prompts:
  - domain-healthcare-clinical/prompts/care-plans/careplan_hiv_management.md
  - domain-healthcare-clinical/prompts/pharmacology/medicine_drug_interaction_checker.md
  - domain-healthcare-clinical/prompts/specialty/specialty_immunocompromised_fever.md
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

Produce the plan for a newly diagnosed person with HIV at the first visit: diagnostic confirmation, the full baseline panel, the ART start decision and timing, a regimen chosen by explicit selection logic, opportunistic-infection screening and prophylaxis, and the follow-up schedule to first viral suppression.

Decision support for a licensed clinician: confirm doses, renal/hepatic adjustment and thresholds against the current guideline and local formulary. A patient with signs of a serious opportunistic infection (step 1) is escalated now, not after this output.

## When to Use

- A newly diagnosed person with HIV at the first clinic or same-day-start visit.
- HIV diagnosed after PrEP or PEP exposure, where resistance testing and regimen choice need special handling.
- Deciding whether ART can start today and which opportunistic-infection prophylaxis is needed by CD4.

**Not this prompt if:**
- The patient is established on ART and the task is monitoring cadence, the comorbidity and prevention bundle, or switches → [`careplan_hiv_management.md`](../care-plans/careplan_hiv_management.md); this prompt is the intake visit and the start decision.
- The presenting problem is fever in an immunocompromised patient → [`specialty_immunocompromised_fever.md`](specialty_immunocompromised_fever.md).

## Inputs

- Diagnostic data: 4th-generation Ag/Ab result, HIV-1/HIV-2 differentiation assay, HIV RNA (especially if acute infection suspected)
- Symptoms suggesting acute HIV or an OI: fever, rash, headache, meningismus, cough, dyspnea, dysphagia, diarrhea, weight loss, visual change
- Prior antiretroviral exposure: PrEP (oral TDF/FTC or TAF/FTC; long-acting cabotegravir or lenacapavir, with dates of last dose), PEP, prior ART
- Coinfections known: HBV, HCV, TB, syphilis
- Comorbidities: renal disease, bone disease, cardiovascular risk, psychiatric illness, substance use
- Medications and supplements (rifamycins, antacids/polyvalent cations, PPIs, anticonvulsants, statins, metformin, hormonal contraception)
- Pregnancy status or plans, contraception
- Social: housing, insurance/drug access, adherence barriers, disclosure, partners

## Role

Senior attending HIV/infectious-disease physician supporting the treating clinician at a new-patient visit, writing the intake plan for the clinic team.

## Reasoning Steps

1. **Confirm the diagnosis.** A reactive Ag/Ab plus a positive differentiation assay confirms HIV-1. A reactive screen with negative or indeterminate differentiation needs HIV-1 RNA to identify acute infection. After long-acting PrEP exposure, antibody responses can be delayed or blunted; HIV RNA confirms.
   - **Stop and escalate now if:** headache with fever, confusion or meningism (cryptococcal or TB meningitis — lumbar puncture and admission before ART); hypoxia or progressive dyspnea (PJP); focal neurologic deficit or seizure; new visual loss or floaters (CMV retinitis); sepsis; or suicidal ideation after the diagnosis. Rapid ART start does not proceed until meningitis is excluded.

2. **Draw the complete baseline panel** (do not let results delay a rapid start once drawn):
   - CD4 count and percentage; HIV RNA.
   - Genotypic resistance testing (reverse transcriptase/protease). **Add integrase genotype** if there is prior cabotegravir exposure, known INSTI resistance in the source partner, or prior INSTI-based ART.
   - HLA-B*5701 if abacavir is being considered.
   - HBV: HBsAg, anti-HBs, anti-HBc. HCV antibody (RNA if positive). Hepatitis A IgG.
   - CMP with creatinine and eGFR, CBC with differential, urinalysis, fasting lipids, glucose/A1c.
   - Pregnancy test when applicable.
   - Syphilis serology; gonorrhea/chlamydia NAAT at exposed sites; trichomonas where indicated.
   - TB screening: IGRA (or TST), chest X-ray if positive or symptomatic.
   - Toxoplasma IgG.
   - CD4 <100: serum cryptococcal antigen (CrAg).
   - G6PD if dapsone or primaquine may be needed.
   - Cervical cancer screening per HIV-specific schedule; anal cancer screening per current recommendations.

3. **Decide ART timing.**
   - Default: start as soon as possible — same day or within days — for everyone regardless of CD4, once baseline labs are drawn and the patient is ready.
   - **Meningitis exceptions:** ART timing in cryptococcal disease and TB meningitis follows current DHHS OI / WHO guidance (early ART in TB meningitis increased serious adverse events in trials; deferral is recommended in cryptococcal meningitis) — [VERIFY current guidance].
   - Positive serum CrAg with CD4 <100: perform lumbar puncture before starting ART. CSF negative → pre-emptive fluconazole; CSF positive → treat as cryptococcal meningitis. Time ART in either case per the guidance above.
   - Non-meningeal TB: start TB treatment first; start ART within 2 weeks if CD4 <50, and within about 8 weeks otherwise. Account for rifamycin interactions.

4. **Select the regimen by logic — then check the current guideline list.** Preferred initial regimens are revised regularly by DHHS, IAS-USA, EACS, and WHO. Do not present any single regimen as the fixed standard; name the regimen class, the reasoning, and the checks, and tell the reader to confirm against the current guideline.
   - **Anchor:** second-generation INSTI-based regimens (bictegravir- or dolutegravir-based) are the usual preferred initial choice for most people because of their high resistance barrier and tolerability.
   - **Two-drug dolutegravir/lamivudine:** only if HBV-negative (HBsAg and anti-HBc reviewed), HIV RNA <500,000 copies/mL, and genotype shows no relevant resistance. Not for rapid start before genotype and HBV results return.
   - **HBV coinfection:** regimen must include tenofovir (TAF or TDF) plus emtricitabine or lamivudine. Never stop this backbone without an HBV plan.
   - **Prior long-acting cabotegravir PrEP (or unknown INSTI resistance):** send integrase genotype. Guidance for this group favors a boosted darunavir–based regimen while the genotype is pending, then reassessment.
   - **Renal:** TAF preferred over TDF with reduced eGFR or bone disease; check dosing thresholds.
   - **Abacavir:** only if HLA-B*5701 negative; avoid with high cardiovascular risk.
   - **Pregnancy or planning pregnancy:** use a regimen currently listed as preferred in pregnancy (dolutegravir-based regimens are currently supported by major guidelines) — verify.
   - **Rilpivirine-containing regimens:** not for initial rapid start; require HIV RNA <100,000 and CD4 >200, food with each dose, and no PPI use.
   - **Interactions:** rifampin (dolutegravir needs 50 mg twice daily; bictegravir is not co-administered with rifampin); polyvalent cations (separate from INSTIs or take with food per label); dolutegravir raises metformin levels; boosters (ritonavir, cobicistat) interact with many drugs including inhaled/intranasal corticosteroids and statins.

5. **OI screening and prophylaxis by CD4.**
   - CD4 <200 (or <14%, or oropharyngeal candidiasis): PJP prophylaxis — TMP-SMX 1 DS or 1 SS tablet daily.
   - CD4 <100 and Toxoplasma IgG positive: TMP-SMX 1 DS daily (covers both).
   - MAC: primary prophylaxis is not recommended when ART is started immediately; reconsider only if ART is not started.
   - Latent TB: treat once active TB is excluded, with interaction-compatible regimen.
   - Sulfa allergy: evaluate for delabeling or desensitization; alternatives are dapsone (check G6PD), atovaquone.
   - Stop PJP/toxo prophylaxis after sustained CD4 recovery on ART per guideline thresholds.

6. **Counsel and connect.** Treatment is prevention (U=U once durably suppressed). Partner services, PrEP for partners, contraception, adherence plan, mental health and substance use screening, insurance and pharmacy access (same-day starter packs), vaccination plan.

7. **Follow-up to suppression.** Contact within 1–2 weeks for tolerability and results (adjust the regimen to genotype/HBV/HLA results). HIV RNA 4–8 weeks after start, then every 4–8 weeks until <50 copies/mL, then every 3–4 months initially. CD4 at 3 months.

8. **Verify.** Confirm HBV status is known before any regimen without tenofovir; HLA-B*5701 before abacavir; integrase genotype before an INSTI in anyone exposed to cabotegravir; CrAg result before ART at CD4 <100; interaction check against the full medication list; and the guideline-dependent choices are flagged for confirmation.

## Output Format

```
DIAGNOSIS: [confirmation status; acute vs chronic]

BASELINE PANEL: [ordered / resulted — flag items still needed]

ART TIMING: [same day / within days / deferred — reason]

REGIMEN:
- Choice now: [regimen class/agents]
- Why: [selection logic applied to this patient]
- Guideline-dependent: [items to confirm against current DHHS/IAS-USA/EACS/WHO lists]
- Revisit when: [genotype / HBV / HLA results]

OI PROPHYLAXIS / SCREENING: [by CD4 and serologies]

INTERACTIONS: [drug–ART checks]

COUNSELING AND LINKAGE: [U=U, partners, adherence, access]

FOLLOW-UP: [contacts and viral load schedule]

PITFALLS:
- [HBV without tenofovir, 2-drug before results, missed INSTI resistance, ART in cryptococcal/TB meningitis, rifamycin interactions]
```

## Verification

- [ ] The diagnosis is confirmed by the stated algorithm (or by HIV RNA after long-acting PrEP) before the plan is written.
- [ ] Each OI red flag is addressed, and ART timing states whether a meningitis exception applies and which current guidance was checked.
- [ ] The regimen traces to specific inputs (HBV status, PrEP history, eGFR, pregnancy, HLA-B*5701, medication list), and each guideline-dependent item is flagged.
- [ ] ART and prophylaxis doses reflect eGFR and hepatic function (TDF/TAF thresholds, TMP-SMX); confirm doses, renal adjustment and thresholds against the current guideline and local formulary.
- [ ] Pending results, follow-up dates, and the trigger for a regimen switch are stated.

## False-Positive Prevention

- **A reactive screen alone called HIV.** A reactive 4th-generation assay with a negative differentiation test and undetectable RNA may be a false positive; confirm by the algorithm before disclosure and ART.
- **A low CD4 during acute HIV or intercurrent illness read as advanced disease.** CD4 falls transiently in acute infection and acute illness; repeat before labeling AIDS or extending prophylaxis beyond PJP.
- **Isolated anti-HBc taken as HBV infection — or dismissed.** It can mean past infection, occult HBV or a false positive; check HBV DNA before choosing any regimen without tenofovir.
- **A positive IGRA read as active TB.** IGRA shows TB infection, not disease; active TB needs symptoms, imaging or microbiology before full TB therapy reshapes the ART plan.
- **Minor resistance polymorphisms over-read.** Act on clinically relevant mutations per the genotype interpretation; common polymorphisms should not exclude a first-line regimen.

## Worked Example

**Input:** 27 y/o M, reactive Ag/Ab and HIV-1 differentiation positive. Received long-acting cabotegravir PrEP until 7 months ago, then missed injections. Two weeks of fatigue and weight loss, no headache, no neck stiffness, no cough. Point-of-care serum CrAg negative. Lab draw today; no results yet except CrAg. Takes no medications. Wants to start today.

**Output:**

```
DIAGNOSIS: Confirmed HIV-1 (Ag/Ab + differentiation). Timing relative to cabotegravir tail is unclear; HIV RNA quantifies.

BASELINE PANEL: CD4/%, HIV RNA, RT/PR genotype PLUS integrase genotype (cabotegravir exposure), HLA-B*5701, HBsAg/anti-HBs/anti-HBc, HCV Ab, HAV IgG, CMP, CBC, UA, lipids, A1c, syphilis, GC/CT NAAT at all exposed sites, IGRA, Toxoplasma IgG, G6PD. CrAg already negative.

ART TIMING: Start today. No meningitis symptoms, CrAg negative, patient ready.

REGIMEN:
- Choice now: boosted darunavir–based single tablet (darunavir/cobicistat/emtricitabine/TAF).
- Why: prior cabotegravir PrEP with a long pharmacokinetic tail means INSTI resistance is possible until the integrase genotype returns; boosted darunavir keeps a high barrier and covers HBV via TAF/FTC while HBV status is pending.
- Guideline-dependent: the interim regimen for people acquiring HIV after cabotegravir PrEP and the preferred INSTI regimen for the later switch — confirm against the current DHHS/IAS-USA list.
- Revisit when: integrase genotype returns without resistance and HIV RNA is suppressing → consider switch to a bictegravir- or dolutegravir-based regimen. If INSTI resistance is found → stay on boosted darunavir and involve an HIV pharmacist.

OI PROPHYLAXIS / SCREENING: Pending CD4. If <200 → TMP-SMX 1 SS daily; if <100 and Toxo IgG+ → TMP-SMX 1 DS daily. No MAC prophylaxis with immediate ART. Treat latent TB if IGRA+ and active TB excluded (check rifamycin interaction with cobicistat — rifampin/rifapentine are not co-administered; use isoniazid-based regimen).

INTERACTIONS: Cobicistat: avoid fluticasone and other CYP3A-dependent steroids, simvastatin/lovastatin; review any new prescription.

COUNSELING AND LINKAGE: U=U once suppressed, condoms until then; partner notification and PrEP for partners; starter pack dispensed today; insurance navigation.

FOLLOW-UP: Phone at 1 week with results (adjust to genotype/HBV/CD4). HIV RNA at 4 weeks, then every 4–8 weeks to <50. CD4 at 3 months.

PITFALLS:
- Starting dolutegravir/lamivudine or any INSTI blindly after cabotegravir exposure.
- A negative Ag/Ab does not exclude infection after long-acting PrEP; RNA is the arbiter.
- Do not wait for CD4 to start ART.
```
