---
title: "Adverse Drug Reaction Assessment (Naranjo Algorithm + Clinical Reasoning)"
category: domain-healthcare-clinical/pharmacology
description: "Evaluate a suspected adverse drug reaction (ADR) using the Naranjo probability scale, distinguish allergic from non-allergic mechanisms, classify by Type A–F, decide on rechallenge/de-challenge, document for safety reporting (FDA MedWatch), and choose alternative therapy with cross-reactivity considerations."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: intermediate
tags:
  - pharmacology
  - adverse-drug-reaction
  - allergy
  - safety
  - naranjo
updated: "2026-05-12"
---

## Objective

Assess a suspected adverse drug reaction systematically: compute Naranjo probability score, distinguish allergic (Gell-Coombs Type I–IV) from non-allergic mechanisms, classify ADR by Rawlins-Thompson type (A–F), decide whether to de-challenge or rechallenge, recommend alternative therapy with cross-reactivity considerations, and document for pharmacovigilance. Output a structured assessment.

## Inputs

- Patient: age, weight, sex, comorbidities
- Suspect drug(s): name, dose, route, start date, prior exposures
- Reaction: timing relative to dose start, character (rash, urticaria, anaphylaxis, organ toxicity, lab abnormality), severity, duration
- Concomitant medications, alternative explanations (infection, autoimmune disease, comorbidity flare)
- Lab data (CBC, CMP, LFTs, tryptase if anaphylaxis, eosinophils, drug level)
- Prior history of reactions
- De-challenge / rechallenge data if available

## Role

Senior clinical pharmacist / allergist / internist evaluating the ADR and writing recommendations.

## Reasoning Steps

1. **Compute Naranjo Adverse Drug Reaction Probability Scale** (10 questions, each +1, 0, or −1, total range −4 to +13):

   1. Are there previous conclusive reports on this reaction? Yes (+1), No (0), Unknown (0).
   2. Did the adverse event appear after the suspected drug was administered? Yes (+2), No (−1), Unknown (0).
   3. Did the adverse reaction improve when the drug was discontinued OR a specific antagonist was administered? Yes (+1), No (0), Unknown (0).
   4. Did the adverse reaction reappear when the drug was readministered? Yes (+2), No (−1), Unknown (0).
   5. Are there alternative causes (other than the drug) that could have on their own caused the reaction? Yes (−1), No (+2), Unknown (0).
   6. Did the reaction reappear when a placebo was given? Yes (−1), No (+1), Unknown (0).
   7. Was the drug detected in the blood (or other fluids) in concentrations known to be toxic? Yes (+1), No (0), Unknown (0).
   8. Was the reaction more severe when the dose was increased, or less severe when the dose was decreased? Yes (+1), No (0), Unknown (0).
   9. Did the patient have a similar reaction to the same or similar drugs in any previous exposure? Yes (+1), No (0), Unknown (0).
   10. Was the adverse event confirmed by any objective evidence? Yes (+1), No (0), Unknown (0).

   **Score interpretation:**
   - **≥9:** Definite ADR.
   - **5–8:** Probable.
   - **1–4:** Possible.
   - **≤0:** Doubtful.

2. **Classify by Rawlins-Thompson mechanism.**
   - **Type A (Augmented):** dose-related, predictable from pharmacology, common (e.g., bleeding on warfarin, hypoglycemia on insulin, opioid sedation, β-blocker bradycardia).
   - **Type B (Bizarre):** not dose-related, unpredictable, idiosyncratic, often immune-mediated or genetic (e.g., anaphylaxis, SJS/TEN, hepatotoxicity from idiosyncratic hepatitis, agranulocytosis).
   - **Type C (Chronic):** related to cumulative dose / duration (e.g., osteoporosis on long-term steroid, lung fibrosis on amiodarone, tardive dyskinesia on antipsychotic).
   - **Type D (Delayed):** carcinogenesis, teratogenesis (e.g., DES daughters, valproate cognitive effect, secondary leukemia from alkylator).
   - **Type E (End-of-use):** withdrawal effects (e.g., rebound hypertension on clonidine cessation, opioid withdrawal, benzo seizure).
   - **Type F (Failure):** unexpected treatment failure (e.g., OCP failure with rifampin, drug-resistant infection).

3. **Distinguish allergic from non-allergic (Gell-Coombs for hypersensitivity).**
   - **Type I (IgE-mediated, immediate hypersensitivity):** anaphylaxis, urticaria, angioedema, bronchospasm. Onset minutes to <1 h. Mediators: histamine, tryptase. Penicillins, cephalosporins, NMBAs, latex, contrast (latter usually non-IgE/anaphylactoid). Diagnosis: skin testing, specific IgE, tryptase.
   - **Type II (cytotoxic, IgG/IgM + complement):** drug-induced hemolytic anemia, thrombocytopenia (e.g., heparin-induced thrombocytopenia by anti-PF4/heparin antibodies), neutropenia. Onset days.
   - **Type III (immune complex):** serum sickness (1–3 weeks post drug), drug-induced vasculitis, glomerulonephritis. Antibiotics, anticonvulsants, biologics.
   - **Type IV (T-cell mediated, delayed hypersensitivity):** contact dermatitis, maculopapular drug eruption, DRESS, SJS/TEN, AGEP. Onset days to weeks (DRESS 2–8 weeks).
   - **Non-allergic ADRs that mimic allergy:** vancomycin infusion reaction (red man — direct mast cell), opioid-induced histamine, ACEi cough, ACEi angioedema (bradykinin not histamine).

4. **Severity and management.**
   - **Mild ADR (e.g., transient mild rash, GI upset):** consider continued use with monitoring or switch.
   - **Moderate (rash with systemic symptoms, transaminitis 3–5× ULN):** stop drug, alternative therapy, monitor.
   - **Severe (anaphylaxis, SJS/TEN, DRESS, agranulocytosis, fulminant hepatitis):** stop drug immediately, supportive care, never rechallenge, avoid cross-reactive agents, allergist consultation.

5. **Decide on de-challenge and rechallenge.**
   - **De-challenge:** stop suspect drug; observe for resolution. Resolution within expected washout period supports ADR causality.
   - **Rechallenge:**
     - **Never** for severe reactions (anaphylaxis, SJS, TEN, DRESS, AGEP, AIHA, severe hepatotoxicity, agranulocytosis).
     - Acceptable for low-grade Type A reactions where the drug is essential and no alternative.
     - Desensitization protocols for IgE-mediated allergy to essential drugs (e.g., penicillin desensitization for syphilis in pregnancy, aspirin desensitization for cardioprotection in AERD).

6. **Cross-reactivity considerations.**
   - **β-lactams:** historic cross-reactivity penicillin → cephalosporin overstated (~1–2%). For mild/moderate reactions to penicillin, most cephalosporins (especially 3rd–5th generation) are acceptable. For severe IgE reactions, allergy testing or use of structurally distinct β-lactam (aztreonam — not cross-reactive with most penicillins except ceftazidime). Carbapenems have <1% cross-reactivity even in true penicillin allergy.
   - **Sulfa:** sulfonamide antibiotics (sulfamethoxazole) and sulfonamide non-antibiotics (sulfonylureas, thiazides, furosemide, celecoxib, sumatriptan) — cross-reactivity is rare clinically (different molecular structure beyond sulfa group). True allergy to sulfa antibiotic does not preclude use of non-antibiotic sulfas in most cases.
   - **NSAIDs:** AERD (aspirin-exacerbated respiratory disease) cross-reacts among COX-1 NSAIDs; COX-2 selective (celecoxib) usually tolerated.
   - **Iodinated contrast:** no cross-reactivity with shellfish iodine ("iodine allergy" misconception); some cross-reactivity among contrast agents — choose non-ionic low-osmolar agent and premedicate (steroid + diphenhydramine) if prior moderate reaction.
   - **Local anesthetics:** ester-type (procaine) vs amide-type (lidocaine, bupivacaine) — cross-reactivity within ester group, not between ester and amide.
   - **Heparin (HIT):** cannot use any unfractionated or LMWH; use direct thrombin inhibitor (argatroban, bivalirudin) or fondaparinux.

7. **Pharmacovigilance reporting.**
   - **FDA MedWatch** (www.fda.gov/medwatch) for any serious ADR — death, life-threatening event, hospitalization, persistent or significant disability, congenital anomaly, intervention to prevent permanent impairment, or any new safety signal.
   - **VAERS** for vaccines.
   - Internal hospital event reporting.
   - Update problem list, allergy list with reaction description (not just "allergy"); be specific.

8. **Choose alternative therapy.**
   - Match the original indication.
   - Avoid same class if Type B / hypersensitivity.
   - Same class allowed for Type A / pharmacologic effect with dose adjustment if no better option.
   - Cross-reactivity check.
   - Patient counseling on documented allergy and reaction; carry MedicAlert.

## Output Format

```
PATIENT SNAPSHOT:
- Demographics, comorbidities, current medications

SUSPECT DRUG & REACTION:
- Drug: [name, dose, route, start date]
- Reaction: [character, timing relative to dose, severity, lab data]
- Alternative explanations: [infection, autoimmune, comorbidity flare]

NARANJO SCORE:
1. [+1/0/0]
2. [+2/-1/0]
3. [+1/0/0]
4. [+2/-1/0]
5. [-1/+2/0]
6. [-1/+1/0]
7. [+1/0/0]
8. [+1/0/0]
9. [+1/0/0]
10. [+1/0/0]
TOTAL: [X] → [Definite ≥9 / Probable 5–8 / Possible 1–4 / Doubtful ≤0]

MECHANISM CLASSIFICATION:
- Rawlins-Thompson type: [A/B/C/D/E/F]
- If allergic, Gell-Coombs type: [I/II/III/IV]
- Direct vs immune: [...]

DE-CHALLENGE / RECHALLENGE DECISION:
- De-challenge: [stop / hold / continue]
- Rechallenge: [acceptable / never / desensitization]

ALTERNATIVE THERAPY:
- [Drug, dose, monitoring]
- Cross-reactivity assessment

DOCUMENTATION & REPORTING:
- Update allergy list with specific reaction (not just drug name)
- FDA MedWatch / institutional reporting if serious
- Patient education and MedicAlert if severe

MONITORING:
- Resolution of reaction
- Function recovery (e.g., LFTs, CBC, renal)
- Lab normalization timing

WHEN TO ESCALATE:
- Anaphylaxis, SJS/TEN, DRESS, severe hepatotoxicity, agranulocytosis — supportive care, allergist / dermatology / hematology / hepatology consultation
- Persistent toxicity despite drug withdrawal — search for alternative cause
- Need for essential drug despite documented reaction → desensitization protocol with allergist

PATIENT COUNSELING:
- Specific reaction description
- Avoidance: drug, class, cross-reactive agents
- MedicAlert (severe reactions)
- Photographs of rash if cutaneous (for future ID)
```

## Worked Example

**Input:** 56-year-old woman, started TMP-SMX 10 days ago for UTI. Develops widespread maculopapular rash on day 8 + fever 38.3°C + lymphadenopathy + eosinophils 1500 + transaminitis (ALT 280, AST 220). No alternative explanation. Evaluate for ADR.

**Output:**

```
PATIENT SNAPSHOT:
- 56 y F, day 10 of TMP-SMX (sulfa antibiotic) for UTI. New systemic illness: rash, fever, lymphadenopathy, eosinophilia, transaminitis.

SUSPECT DRUG & REACTION:
- TMP-SMX (sulfamethoxazole + trimethoprim).
- Reaction: maculopapular rash + fever + lymphadenopathy + eosinophilia + hepatitis at day 10 of therapy.
- Clinical picture strongly consistent with **DRESS (Drug Reaction with Eosinophilia and Systemic Symptoms)** = SCAR (severe cutaneous adverse reaction).
- Alternative explanations: viral infection (CMV, EBV, HHV-6 — HHV-6 reactivation common in DRESS), autoimmune flare. Send EBV/CMV/HHV-6 PCR for completeness; clinical pattern still favors DRESS.

NARANJO SCORE:
1. Previous conclusive reports of TMP-SMX causing DRESS? Yes (+1).
2. Adverse event appeared after drug administration? Yes (+2).
3. Improved when drug discontinued (still in progress; will assess)? Pending — given likely yes upon stopping → +1 if resolves.
4. Reappeared with rechallenge? Unknown (not done) (0).
5. Alternative causes? Workup pending, but pattern fits DRESS more than viral. Tentatively No (+2). Adjust if viral PCR positive.
6. Placebo control? Unknown (0).
7. Drug detected at toxic concentrations? Not assessed; therapeutic dosing (0).
8. Dose-response? Not applicable for hypersensitivity (0).
9. Similar prior reaction to sulfa? Unknown (0).
10. Objective confirmation? Yes — eosinophilia, transaminitis, rash documented (+1).
TOTAL: 7 (assuming de-challenge improves and viral causes negative) → **Probable ADR (5–8)**.

MECHANISM CLASSIFICATION:
- **Rawlins-Thompson Type B (idiosyncratic / immune-mediated).**
- **Gell-Coombs Type IV (T-cell-mediated delayed hypersensitivity)** — DRESS is a SCAR with T-cell-mediated mechanism, HLA-associated in some populations (HLA-A*31:01 with carbamazepine; less defined HLA for sulfa).
- DRESS diagnostic criteria (RegiSCAR): rash, fever, lymphadenopathy, eosinophilia or atypical lymphocytes, internal organ involvement (here: hepatitis), drug exposure 2–8 weeks before onset.

DE-CHALLENGE / RECHALLENGE DECISION:
- **STOP TMP-SMX immediately.**
- **NEVER rechallenge.** Future avoidance of all sulfonamide antibiotics (sulfamethoxazole, sulfadiazine, dapsone has some cross-reactivity; cautious avoidance of sulfasalazine).
- Cross-reactivity with non-antibiotic sulfa drugs (sulfonylureas, thiazides, furosemide, celecoxib): clinical cross-reactivity rare with isolated antibiotic-sulfa allergy. **Avoid in DRESS** out of abundance of caution due to severity.

ALTERNATIVE THERAPY:
- For ongoing UTI: alternative antibiotic based on culture/susceptibility — nitrofurantoin (if not pyelonephritis and CrCl adequate), fosfomycin 3 g PO ×1 dose, cephalexin, or fluoroquinolone (e.g., ciprofloxacin 250–500 mg BID ×3–7 days). Choose based on UTI severity and isolate susceptibility.

MANAGEMENT OF DRESS:
- **Hospitalize** for monitoring of organ involvement.
- **Stop offending drug.**
- **Supportive care:** fluid balance, electrolyte management, fever control.
- **Systemic corticosteroids:** prednisone 1 mg/kg/day for moderate-severe (organ involvement); IV methylprednisolone 1 mg/kg/day if severe; slow taper over 8–12 weeks (rapid taper provokes flare).
- **Dermatology consultation.**
- **Avoid additional drugs** during acute phase (every new drug a potential cross-reaction or further insult).
- Monitor: CBC, CMP, LFTs, glucose, BUN/Cr daily; serum tryptase / IL-5 not routine.
- Monitor for late autoimmune sequelae (thyroiditis, type 1 diabetes, autoimmune hepatitis) — surveillance for months after.

DOCUMENTATION & REPORTING:
- Allergy list updated: "TMP-SMX — DRESS syndrome (severe cutaneous adverse reaction with rash, fever, eosinophilia, hepatitis, day 10 of therapy 2026-05-12)" — specific.
- **FDA MedWatch report** for serious adverse event.
- Internal hospital safety reporting.
- Discharge education with written documentation.

MONITORING:
- Rash, fever, organ function (LFTs, BUN/Cr, CBC) — weekly until normalized (typically 4–8 weeks to clear).
- Glucose, thyroid function over 3–6 months (autoimmune sequelae).
- Dermatology and internist follow-up.

WHEN TO ESCALATE:
- Worsening transaminitis, jaundice → hepatology, consider transplant evaluation if fulminant.
- Respiratory involvement (pneumonitis) → pulmonology.
- Renal failure → nephrology.
- Cardiac involvement (myocarditis — sometimes in DRESS) → cardiology.

PATIENT COUNSELING:
- This is a severe drug reaction; lifelong avoidance of TMP-SMX and other sulfonamide antibiotics.
- MedicAlert bracelet: "Sulfa allergy — DRESS syndrome."
- Carry detailed allergy information for future medical encounters.
- Discuss with all future providers before any new medication.
- Watch for delayed autoimmune issues over coming months — report new fatigue, neck swelling, polyuria, jaundice.
- Photos of rash documented in chart for future reference.
- Avoid OTC products containing sulfonamides.
```
