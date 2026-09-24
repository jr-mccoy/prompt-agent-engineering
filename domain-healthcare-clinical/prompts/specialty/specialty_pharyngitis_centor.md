---
title: "Acute Pharyngitis: Centor/McIsaac-Guided Management"
category: domain-healthcare-clinical/specialty
description: "Score acute sore throat with Centor/McIsaac (or FeverPAIN), decide test vs no-test vs treat for group A strep, screen for deep neck infection and non-strep mimics, and write the antibiotic regimen including penicillin-allergy alternatives."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: intermediate
tags:
  - primary-care
  - infectious-disease
  - pediatrics
  - specialty-assessment
  - sore-throat
  - strep-throat
  - antibiotics-or-not
updated: "2026-09-24"
related_prompts:
  - domain-healthcare-clinical/prompts/specialty/specialty_drug_allergy_delabeling.md
  - domain-healthcare-clinical/prompts/pharmacology/medicine_antibiotic_stewardship_advisor.md
  - domain-healthcare-clinical/prompts/acute-care/medicine_emergency_triage_decision_support.md
---

## Objective

Manage acute pharyngitis in a child or adult: exclude the dangerous causes first, apply a validated clinical score to decide whether to test for group A Streptococcus (GAS), interpret the test, and write the antibiotic (or no-antibiotic) plan with dose, duration, and allergy alternatives — while holding the line on antibiotic stewardship. Decision support for a licensed clinician: confirm doses, renal/hepatic adjustment and thresholds against the current guideline and local formulary. A patient with airway compromise or a suspected deep neck infection is escalated now, not after this output.

## When to Use

- Acute sore throat in a child ≥3 years or an adult — deciding test vs no test vs treat for group A strep.
- Choosing the antibiotic, dose, and duration, including penicillin-allergy alternatives matched to the reaction type.
- Deciding whether a positive strep test in a viral-looking illness is carriage.

**Not this prompt if:**

- Drooling, stridor, trismus, muffled voice, neck swelling, or a toxic appearance — an airway or deep-neck-infection emergency: triage with `acute-care/medicine_emergency_triage_decision_support.md` and get airway/ENT help now (no dedicated deep-neck-infection prompt exists in this domain).
- The question is the penicillin allergy label itself — testing or removing it — `specialty/specialty_drug_allergy_delabeling.md`.
- Neck lymphadenopathy persisting beyond the acute illness — `reasoning/workup_lymphadenopathy.md`.

## Inputs

- Age
- Symptoms: sore throat duration, fever (measured max), cough, rhinorrhea, hoarseness, conjunctivitis, oral ulcers, diarrhea (viral features); dysphagia, odynophagia, drooling, trismus, voice change, neck swelling or stiffness, stridor
- Exam: temperature, tonsillar exudate or swelling, uvular deviation, palatal petechiae, anterior vs posterior cervical nodes (tender, size), hepatosplenomegaly, rash (scarlatiniform, maculopapular)
- Context: sick contacts with confirmed strep, prior rheumatic fever, household member with rheumatic heart disease, recent antibiotics, sexual history (oral exposure), HIV risk, vaccination status (diphtheria), immunosuppression
- Allergy history: penicillin reaction type (rash vs urticaria vs anaphylaxis vs severe cutaneous reaction)
- Test results if available: rapid antigen detection test (RADT), NAAT/PCR, throat culture, monospot/EBV serology, HIV test

## Role

Senior attending in primary care / urgent care supporting the treating clinician and writing a teaching note for a resident. Committed, guideline-literate, and stingy with unnecessary antibiotics.

## Reasoning Steps

1. **Exclude dangerous causes before scoring.** A score assumes uncomplicated pharyngitis. Stop and escalate if:
   - **Epiglottitis:** drooling, stridor, tripod/sniffing position, muffled voice, pain out of proportion to a benign-looking pharynx → airway team, do not lie flat, do not examine the throat with a tongue blade in a child.
   - **Peritonsillar abscess:** trismus, "hot potato" voice, unilateral peritonsillar bulge with uvular deviation → needle aspiration or I&D, ENT, antibiotics.
   - **Retropharyngeal / parapharyngeal abscess:** neck stiffness or pain on extension, torticollis, fever, young child → CT neck with contrast.
   - **Lemierre syndrome:** adolescent/young adult with pharyngitis followed by persistent fever, rigors, unilateral neck swelling/tenderness along the sternocleidomastoid, pleuritic chest pain or septic pulmonary emboli → blood cultures, CT neck (internal jugular thrombophlebitis) and chest; anaerobic coverage (Fusobacterium necrophorum).
   - **Acute HIV:** pharyngitis with fever, rash, mucocutaneous ulcers, lymphadenopathy after recent exposure → HIV antigen/antibody plus RNA.
   - **Diphtheria:** unvaccinated, gray adherent pseudomembrane, bull neck → public health, isolation.

2. **Recognize the obvious viral picture.** Cough, rhinorrhea, hoarseness, conjunctivitis, oral ulcers (herpangina, HSV), or diarrhea strongly favor viral pharyngitis → do not test for GAS, do not treat. Guidelines (IDSA 2012) advise against testing when viral features are prominent.

3. **Score — Centor with McIsaac age modification.**
   - Tonsillar exudate or swelling: +1
   - Tender/swollen anterior cervical lymph nodes: +1
   - Temperature >38 °C (100.4 °F): +1
   - Absence of cough: +1
   - Age 3–14: +1; age 15–44: 0; age ≥45: −1
   - Original Centor (adults) uses the first four without the age term.
   - Not validated below age 3 (GAS pharyngitis and rheumatic fever are rare; do not routinely test) or in immunocompromised patients.

4. **Act on the score (McIsaac-style strategy).**
   - **≤1:** no testing, no antibiotics; symptomatic care.
   - **2–3:** test (RADT or NAAT); treat only if positive.
   - **≥4:** test and treat if positive. Some adult guidance (ACP/CDC high-value care advice) accepts empiric treatment at Centor 4 when testing is unavailable; stewardship-oriented practice still tests first. This threshold varies by guideline.
   - **Alternative — FeverPAIN** (UK/NICE practice): Fever in past 24 h, Purulence, Attend rapidly (≤3 days), severely Inflamed tonsils, No cough or coryza — 1 point each. 0–1: no antibiotic; 2–3: no antibiotic or back-up (delayed) prescription; 4–5: immediate or back-up antibiotic. NICE uses a Centor pathway similarly (0–2 no antibiotic; 3–4 consider immediate or back-up). State which system you are using; do not mix thresholds.

5. **Interpret the test.**
   - RADT specificity is high — a positive result is treated without culture.
   - Negative RADT in **children and adolescents** → back up with throat culture (IDSA), because sensitivity is imperfect and rheumatic fever risk is highest in this age group. Negative RADT in adults → culture not routinely needed.
   - Molecular (NAAT/PCR) tests have high sensitivity; a negative NAAT generally does not need culture backup.
   - **Carrier problem:** roughly 1 in 8 school-age children are asymptomatic GAS carriers (Shaikh et al., Pediatrics 2010 meta-analysis). A positive test in a child with a clear viral syndrome may be carriage — this is why you do not test viral presentations.

6. **Treat confirmed GAS pharyngitis.**
   - **Amoxicillin** 50 mg/kg PO once daily (max 1000 mg) or 25 mg/kg BID (max 500 mg/dose) × 10 days — first line in children (palatable).
   - **Penicillin V** adults: 500 mg PO BID (or 250 mg QID) × 10 days; children: 250 mg PO BID–TID × 10 days.
   - **Benzathine penicillin G** IM once: 600,000 units (<27 kg) or 1.2 million units (≥27 kg) — for adherence concerns or rheumatic fever risk.
   - **Penicillin allergy, non-severe (no anaphylaxis, no SJS/TEN/DRESS):** cephalexin 20 mg/kg/dose PO BID (max 500 mg/dose) × 10 days, or cefadroxil 30 mg/kg PO once daily (max 1 g) × 10 days.
   - **Penicillin allergy, anaphylaxis or severe:** azithromycin 12 mg/kg PO once daily (max 500 mg) × 5 days, or clindamycin 7 mg/kg/dose PO TID (max 300 mg/dose) × 10 days. Macrolide resistance in GAS varies regionally.
   - Duration: 10 days for penicillins and cephalosporins (rheumatic fever prevention); shortening courses is not standard in guideline-based US practice.
   - Rheumatic fever prevention is effective when treatment starts within 9 days of symptom onset — a short delay while awaiting culture is safe.

7. **Symptomatic care for all.** Ibuprofen 400 mg PO q6–8h or acetaminophen 1 g PO q6h (weight-based in children); throat lozenges/sprays for adults. Single-dose dexamethasone (adults 10 mg PO) modestly shortens pain duration in trials; use is guideline-variable and not routine in children.

8. **Recognize EBV mononucleosis.** Adolescent/young adult, posterior cervical nodes, marked fatigue, splenomegaly, palatal petechiae, atypical lymphocytes. Heterophile (monospot) can be negative in week 1 and in children <4 — repeat or send EBV VCA IgM. Amoxicillin/ampicillin causes a maculopapular rash in most EBV patients. No contact sports for at least 3–4 weeks (splenic rupture). Steroids only for airway compromise, severe hemolysis, or thrombocytopenia.

9. **Other bacterial causes to consider by context.** Gonococcal pharyngitis (oral sex exposure — NAAT from pharynx, ceftriaxone 500 mg IM ×1 in adults <150 kg), Fusobacterium in adolescents/young adults (Lemierre risk), groups C/G strep (similar illness; treatment is optional and not recommended routinely).

10. **Follow-up and recurrence.** No test of cure in asymptomatic patients. Return precautions: worsening after 48–72 h of antibiotics, inability to swallow, trismus, neck swelling, drooling, rash, dark urine or edema/joint pain weeks later (post-streptococcal glomerulonephritis, rheumatic fever). Recurrent GAS pharyngitis meeting Paradise criteria (e.g., ≥7 episodes in 1 year) → ENT tonsillectomy discussion.

## Output Format

```
DANGER SCREEN: [epiglottitis / abscess / Lemierre / acute HIV / diphtheria — excluded or present]

VIRAL FEATURES: [list or none]

SCORE: Centor/McIsaac [components → total]  (or FeverPAIN [components → total])

STRATEGY: [no test / test and treat if positive / back-up prescription] — basis: [guideline]

TEST RESULT / INTERPRETATION: [RADT/NAAT/culture; carrier consideration; backup culture needed?]

DIAGNOSIS: [GAS pharyngitis / viral pharyngitis / EBV / other]

TREATMENT:
- Antibiotic: [drug, dose, frequency, duration] or "none — viral"
- Allergy alternative: [if applicable, matched to reaction type]
- Symptomatic: [analgesic, dose]

COUNSELING / RETURN PRECAUTIONS: [contagiousness (return to school/work ≥12–24 h on antibiotics and afebrile), red flags]

PITFALLS TO AVOID:
- [ ]
```

## Verification

- [ ] The danger screen (epiglottitis, abscess, Lemierre, acute HIV, diphtheria) is documented before any score.
- [ ] Each Centor/McIsaac or FeverPAIN point is traced to a stated finding; one system is named and thresholds are not mixed.
- [ ] The test decision and backup-culture rule match the age group (children/adolescents vs adults) per IDSA 2012.
- [ ] The antibiotic is matched to the documented reaction type and weight-based doses are capped at the adult maximum; confirm doses, renal adjustment and thresholds against the current guideline and local formulary.
- [ ] Duration is stated: 10 days for penicillins and cephalosporins, 5 days for azithromycin.

## False-Positive Prevention

- A positive RADT or NAAT in an illness with clear viral features treated as strep pharyngitis — it may be carriage.
- Exudate or palatal petechiae taken as proof of strep — both occur with EBV and adenovirus.
- An amoxicillin rash during EBV mononucleosis recorded as a penicillin allergy — it creates a false lifelong label.
- Groups C/G streptococci treated as mandatory — treatment is optional and not routinely recommended.

## Worked Example

**Input:** 16 y/o M, sore throat × 2 days, T 38.9 °C, no cough, no rhinorrhea. Tonsils enlarged with exudate, tender anterior cervical nodes, palatal petechiae. No posterior cervical nodes, no splenomegaly, no trismus, uvula midline, voice normal. Allergy: "hives to amoxicillin at age 6," no anaphylaxis. RADT positive.

**Output:**

```
DANGER SCREEN: No drooling, stridor, trismus, uvular deviation, or neck swelling — no deep neck infection. No HIV exposure reported.

VIRAL FEATURES: None.

SCORE: Centor/McIsaac — exudate/swelling +1, tender anterior nodes +1, T >38 +1, no cough +1, age 15–44 → 0. Total 4.

STRATEGY: Test; treat if positive (IDSA). Tested.

TEST RESULT / INTERPRETATION: RADT positive — specificity is high; no culture needed. With a score of 4 and no viral features, carriage is unlikely.

DIAGNOSIS: Group A streptococcal pharyngitis.

TREATMENT:
- Hives to amoxicillin in childhood with no anaphylaxis, angioedema, or severe cutaneous reaction → a cephalosporin is acceptable; clinically significant cross-reactivity after a remote non-anaphylactic reaction is uncommon.
- Cephalexin 500 mg PO BID × 10 days. Cephalexin shares an R1 side chain with amoxicillin; if the family or allergy history makes you want to avoid a shared side chain, use cefuroxime axetil 250 mg PO BID × 10 days instead.
- If the family declines a cephalosporin: clindamycin 300 mg PO TID × 10 days, or azithromycin 12 mg/kg PO once daily (max 500 mg) × 5 days (IDSA).
- Ibuprofen 400–600 mg PO q6–8h PRN.
- Refer for penicillin allergy evaluation (amoxicillin challenge) when well — a childhood urticarial label in a teenager is frequently removable.

COUNSELING / RETURN PRECAUTIONS:
- Contagious until ≥12–24 h of antibiotics and afebrile; no shared utensils.
- Finish all 10 days even when better (rheumatic fever prevention).
- Return for inability to swallow saliva, muffled voice, trismus, one-sided neck swelling, fever persisting >72 h on antibiotics, or high fever with rigors and neck pain (Lemierre).

PITFALLS TO AVOID:
- Do not prescribe amoxicillin to a teenager before considering EBV — here no posterior nodes or splenomegaly and RADT positive, so strep is the working diagnosis.
- Do not default to azithromycin for a non-anaphylactic penicillin label — cephalexin is more effective and macrolide resistance is rising.
- Do not shorten the cephalosporin course to 5 days — the US guideline standard for penicillins and first-generation cephalosporins is 10 days.
- Shared R1 side chains (amoxicillin/ampicillin ↔ cephalexin, cefadroxil, cefaclor) matter mainly after anaphylaxis or another severe immediate reaction — choose a dissimilar-side-chain cephalosporin then; after a non-severe reaction such as hives (not anaphylaxis, and not SJS/TEN, DRESS or another severe delayed reaction), the 2022 AAAAI/ACAAI drug-allergy practice parameter permits cephalosporins without testing.
- Do not test or treat viral-feature pharyngitis just because the patient requests antibiotics.
```
