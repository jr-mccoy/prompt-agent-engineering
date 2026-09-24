---
title: "Microbiology Culture and Susceptibility Interpretation"
category: domain-healthcare-clinical/interpretation
description: "Read a patient's culture, Gram stain, rapid molecular, and susceptibility report — pathogen vs contaminant, resistance phenotype, site-appropriate agent — and commit to the definitive antimicrobial, dose, duration, and mandatory bundle actions."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: advanced
tags:
  - infectious-disease
  - microbiology
  - antimicrobial-resistance
  - bacteremia
  - interpretation
  - bacteria-in-blood
  - which-antibiotic
  - drug-resistant-infection
updated: "2026-09-24"
related_prompts:
  - domain-healthcare-clinical/prompts/interpretation/interp_urinalysis_microscopy.md
  - domain-healthcare-clinical/prompts/pharmacology/medicine_antibiotic_stewardship_advisor.md
  - domain-medical-education/learner-foundational-sciences/study_microbiology_bug_drug_grid.md
---

## Objective

Interpret a specific patient's microbiology result — specimen, Gram stain, rapid molecular panel, organism ID, and susceptibility report — and commit to whether it is real, what resistance phenotype it represents, which agent reaches the site, and the definitive regimen with dose, route, duration, and bundle actions.

Decision support for a licensed clinician: confirm antimicrobial doses, renal/hepatic adjustment and breakpoints against the current guideline, the lab's reporting standard, and local formulary. A patient in septic shock is resuscitated and escalated now, not after this output.

## When to Use

- A culture, Gram stain, or rapid molecular result for one patient needs a real-vs-contaminant call.
- Susceptibilities are back and empirical therapy must be narrowed, switched, or stopped.
- A resistance phenotype (MRSA, ESBL, AmpC, CRE, VRE) needs an agent that reaches the site.
- A bacteremia or candidemia needs its mandatory bundle and a duration anchor.

**Not this prompt if:**

- The question is program-level empiric selection, de-escalation, or duration policy → `domain-healthcare-clinical/prompts/pharmacology/medicine_antibiotic_stewardship_advisor.md`; this prompt reads one report for one patient.
- A learner is studying organism–drug patterns → `domain-medical-education/learner-foundational-sciences/study_microbiology_bug_drug_grid.md`.
- The vancomycin dose itself is being calculated → `domain-healthcare-clinical/prompts/pharmacology/pharm_vancomycin_auc_dosing.md`.

## Inputs

- Specimen type and collection (peripheral vs line blood cultures, number of sets positive, time to positivity; clean-catch vs catheter urine; expectorated sputum vs BAL; swab vs tissue/bone; sterile fluid)
- Gram stain, rapid ID/resistance markers (e.g., mecA/MREJ, vanA/B, CTX-M, KPC, NDM, VIM, IMP, OXA-48)
- Organism ID and colony count where relevant
- Susceptibility report: agents, MIC, interpretation (S / SDD / I / R), breakpoint standard (CLSI or EUCAST), cascade/suppressed agents
- Clinical context: syndrome and source, severity, current antimicrobials and start time, allergies (reaction type), renal function, weight, devices/prosthetics, immune status, prior cultures and colonization

## Role

Senior infectious diseases attending supporting the treating clinician; reviews micro results on rounds.

## Reasoning Steps

1. **Stop and escalate first if:** septic shock or hypotension, bacteremia in a deteriorating patient, S. aureus bacteremia or candidemia, a carbapenemase result, or suspected meningitis, endocarditis, or necrotizing infection — make therapy active now, pursue source control, and involve ID. Then **specimen quality and source.** Sputum with >25 PMNs and <10 squamous epithelial cells per low-power field is a quality sample. Swabs of chronic wounds grow colonizers; tissue or bone biopsy defines osteomyelitis pathogens. Catheter urine grows biofilm organisms. Cultures drawn after antibiotics can be falsely negative.

2. **Pathogen or contaminant/colonizer.**
   - **Blood:** S. aureus, S. lugdunensis, S. pneumoniae, beta-hemolytic streptococci, Enterobacterales, Pseudomonas, and Candida are never contaminants. Coagulase-negative staphylococci, Cutibacterium, Corynebacterium, Bacillus (non-anthracis), and Micrococcus in 1 of ≥2 sets are usually contaminants — unless a prosthetic valve, device, or line with the same organism in multiple sets.
   - **Urine:** bacteriuria without symptoms is asymptomatic bacteriuria — do not treat except pregnancy and before urologic procedures with mucosal trauma. Candiduria is usually colonization.
   - **Respiratory:** Candida, enterococci, CoNS in sputum are colonizers.

3. **Early signals.** Gram stain and rapid markers justify changes before final susceptibilities: gram-positive cocci in clusters + mecA → MRSA coverage; CTX-M → carbapenem; carbapenemase gene → carbapenemase-directed agent and ID consult.

4. **Read the susceptibility report correctly.** MICs are not comparable across drugs — never pick "the lowest MIC." Know intrinsic resistance: Enterococcus to cephalosporins; Klebsiella to ampicillin; Pseudomonas to ceftriaxone and ertapenem; Stenotrophomonas to carbapenems; Listeria to cephalosporins; anaerobes to aminoglycosides. Cascade reporting may hide broad agents — ask the lab if needed.

5. **Resistance phenotypes that change the drug.**
   - **MRSA** (oxacillin R/mecA): vancomycin (AUC-guided 400–600 mg·h/L) or daptomycin (bacteremia; not pneumonia).
   - **ESBL phenotype** (ceftriaxone R in E. coli/Klebsiella): carbapenem for serious infection — piperacillin-tazobactam was inferior to meropenem for ceftriaxone-resistant bloodstream infection in a randomized trial (MERINO) even when reported susceptible. Oral step-down with an active agent once stable (TMP-SMX, fluoroquinolone).
   - **Inducible chromosomal AmpC** (Enterobacter cloacae, Klebsiella aerogenes, Citrobacter freundii): ceftriaxone may fail on therapy despite "S" in serious infection — use cefepime.
   - **Carbapenem-resistant Enterobacterales:** mechanism drives the agent — KPC/OXA-48 → ceftazidime-avibactam or meropenem-vaborbactam (KPC); metallo-β-lactamase (NDM/VIM/IMP) → ceftazidime-avibactam + aztreonam, or cefiderocol. ID consult.
   - **VRE:** linezolid or high-dose daptomycin.
   - **Inducible clindamycin resistance** (erythromycin R, clindamycin S, D-test positive): do not use clindamycin.

6. **Site pharmacology.** Nitrofurantoin and fosfomycin: cystitis only (no blood/renal levels). Daptomycin: inactivated by surfactant (no pneumonia). Moxifloxacin: poor urinary levels. Aminoglycosides: poor in abscess/acidic environments. CNS infection: meningitic breakpoints and high doses. Oral step-down favors high-bioavailability agents (fluoroquinolones, TMP-SMX, linezolid, metronidazole).

7. **Mandatory bundles.**
   - **S. aureus bacteremia (and S. lugdunensis):** ID consult; repeat blood cultures q24–48h until negative; echocardiography (TEE for most); remove infected lines; MSSA → cefazolin 2 g IV q8h (or nafcillin/oxacillin 2 g IV q4h); ≥14 days IV from first negative culture if uncomplicated, 4–6 weeks if complicated.
   - **Candidemia:** remove central lines; echinocandin (e.g., micafungin 100 mg IV daily); ophthalmology exam; repeat cultures; 14 days after first negative culture and symptom resolution.
   - **Streptococcus gallolyticus (bovis) bacteremia:** echo + colonoscopy.
   - **Enterococcus faecalis bacteremia:** assess for endocarditis.

8. **Duration.** Uncomplicated gram-negative bacteremia with source control and prompt response: 7 days total is non-inferior to 14 in randomized trials. Count from first effective therapy.

9. **Pitfalls before signing.** Treating contaminants or colonizers; trusting "S" to piperacillin-tazobactam in ESBL bacteremia; ceftriaxone for AmpC organisms in serious infection; a drug reported "S" that cannot reach the site; forgetting renal dose adjustment; leaving double coverage in place after susceptibilities return.

## Output Format

```
SPECIMEN: [type, quality, sets positive, time to positivity]
ORGANISM: [ID, count] — REAL / CONTAMINANT / COLONIZER — [reason]
RESISTANCE PHENOTYPE: [MSSA/MRSA/ESBL/AmpC/CRE-mechanism/VRE/none]
AGENTS THAT REACH THE SITE AND ARE ACTIVE: [list]
AGENTS TO AVOID DESPITE "S": [list + reason]

DEFINITIVE REGIMEN:
- [drug, dose adjusted to renal function, route, frequency]
- [IV-to-PO step-down criteria and agent]
- [total duration and day 1 anchor]

BUNDLE / SOURCE ACTIONS:
- [repeat cultures, echo, imaging, line removal, consults]
```

## Verification

- [ ] Specimen type and collection method stated — or flagged as not stated — before an organism is called real.
- [ ] Real vs contaminant call traced to the organism, number of sets positive, time to positivity, and clinical syndrome.
- [ ] Breakpoint standard (CLSI or EUCAST) named, intrinsic resistance checked, and every "S" agent screened for site penetration.
- [ ] Doses adjusted to CrCl and weight and checked against the current guideline and local formulary; allergy reaction type considered.
- [ ] Mandatory bundle actions listed for the organism (S. aureus, Candida, S. gallolyticus, E. faecalis).
- [ ] Duration anchored to the first active dose or first negative culture, with what would extend it.

## False-Positive Prevention

- **Urine assumed to be the source of a bacteremia** because a urine culture is positive, without urinary symptoms or pyuria — look for another source.
- **A rapid resistance marker attributed to the wrong organism in a mixed culture** (e.g., mecA from a coagulase-negative staphylococcus assigned to S. aureus).
- **Carbapenem non-susceptibility assumed to be a carbapenemase** without a mechanism test; porin loss with ESBL/AmpC changes the agent choice.
- **A colonization screen treated as the pathogen.** A positive MRSA nares swab or rectal ESBL screen does not identify the organism causing this infection.

## Worked Example

**Input:** 72 y/o F, 60 kg, admitted with fever 38.9, right flank pain, rigors. Started ceftriaxone 1 g IV daily 36 hours ago; still febrile, BP 104/62. Cr 1.1 (CrCl ~40 mL/min). No allergies. Results: blood cultures 2 of 2 sets gram-negative rods, time to positivity 11 h; urine culture >100,000 CFU/mL E. coli. Susceptibilities (CLSI) for both isolates: ampicillin R, ampicillin-sulbactam R, cefazolin R, ceftriaxone R (MIC ≥4), cefepime SDD, piperacillin-tazobactam S (MIC 8), ertapenem S, meropenem S (MIC ≤0.25), ciprofloxacin R, TMP-SMX S, gentamicin S, nitrofurantoin S.

**Output:**

```
SPECIMEN: Two of two blood culture sets + concordant urine isolate — urine collection method not stated (clean-catch vs catheter); colony count significant, and concordance with blood confirms the source.
ORGANISM: E. coli — REAL (bacteremic pyelonephritis).
RESISTANCE PHENOTYPE: ESBL phenotype (ceftriaxone R, cefepime SDD). Explains persistent fever on ceftriaxone.
AGENTS THAT REACH THE SITE AND ARE ACTIVE: meropenem, ertapenem, TMP-SMX, gentamicin.
AGENTS TO AVOID DESPITE "S": piperacillin-tazobactam (inferior to carbapenem in ESBL bacteremia); nitrofurantoin (no renal-tissue or blood levels); cefepime (SDD — not reliable for ESBL bacteremia).

DEFINITIVE REGIMEN:
- Stop ceftriaxone. Meropenem 1 g IV q12h (CrCl 26–50 dose) now; once afebrile and stable may simplify to ertapenem 1 g IV daily.
- Oral step-down when afebrile ≥48 h, hemodynamically stable, tolerating PO, and obstruction excluded: TMP-SMX DS 1 tablet PO q12h (full dose at CrCl >30; halve if CrCl falls to 15–30).
- Total 7 days from the first dose of active therapy (meropenem day 1 = today), extend to 10–14 if slow response or unresolved source.

BUNDLE / SOURCE ACTIONS:
- Renal ultrasound (or CT) today — persistent fever at 36 h on inactive therapy still warrants excluding obstruction, abscess, or emphysematous pyelonephritis; obstruction → urology for decompression.
- Repeat blood cultures not routinely needed for gram-negative bacteremia; draw if fever persists 48–72 h on meropenem.
- Contact precautions per institutional ESBL policy; flag ESBL colonization in the chart for future empiric choices.
- BMP daily while on renally dosed therapy.
```
