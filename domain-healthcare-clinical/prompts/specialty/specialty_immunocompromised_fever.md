---
title: "Fever in the Immunocompromised Host"
category: domain-healthcare-clinical/specialty
description: "Evaluate fever by type of immune defect — neutropenia (MASCC risk, empiric antipseudomonal therapy within 60 minutes), solid-organ transplant (post-transplant timeline), biologic/steroid therapy, asplenia — and write the cultures, empiric regimen, escalation, and de-escalation plan."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: advanced
tags:
  - infectious-disease
  - oncology
  - transplant
  - febrile-neutropenia
  - specialty-assessment
  - sick-after-chemo
  - low-white-count
  - transplant-infection
updated: "2026-09-24"
related_prompts:
  - domain-healthcare-clinical/prompts/reasoning/workup_fever_unknown_origin.md
  - domain-healthcare-clinical/prompts/acute-care/medicine_sepsis_recognition_framework.md
  - domain-healthcare-clinical/prompts/pharmacology/medicine_antibiotic_stewardship_advisor.md
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

Produce an infectious-disease plan for a febrile immunocompromised patient: identify the immune defect, predict the likely pathogens from that defect, risk-stratify, start the right empiric therapy on time, and set escalation (antifungal, broader gram-positive cover) and de-escalation rules. Decision support for a licensed clinician: confirm doses, renal/hepatic adjustment and thresholds against the current guideline and local formulary. A hypotensive or deteriorating patient gets antibiotics and escalation now, not after this output.

## When to Use

- Fever in a patient on chemotherapy, after HSCT or solid-organ transplant, on biologics or chronic glucocorticoids, or with asplenia — the first hours and days.
- Choosing the empiric regimen, whether to add vancomycin or an antifungal, and when to stop.
- Checking an admission ID plan for a defect–pathogen mismatch or an azole–immunosuppressant interaction.

**Not this prompt if:**

- The fever is ≥3 weeks old and undiagnosed — `reasoning/workup_fever_unknown_origin.md` stages it and mentions neutropenic fever only as a category; this prompt is the acute, defect-specific plan.
- Suspected sepsis in an immunocompetent host — `acute-care/medicine_sepsis_recognition_framework.md`.
- Starting antiretroviral therapy at an HIV intake visit — `specialty/specialty_hiv_initial_visit_art.md`.

## Inputs

- Immune defect: chemotherapy (regimen, day of cycle, expected nadir), hematologic malignancy, HSCT (auto/allo, day post-transplant, GVHD), solid-organ transplant (organ, date, induction, current immunosuppression, CMV D/R serostatus), biologics (anti-TNF, rituximab, JAK inhibitor, others), chronic glucocorticoids (dose, duration), asplenia, HIV with CD4
- Fever: maximum temperature, duration, rigors
- Vitals and perfusion: HR, BP, RR, SpO₂, mental status, lactate
- Focal clues: central line site, mucositis, perianal pain, skin lesions, cough/infiltrate, diarrhea, sinus pain, headache, abdominal pain
- Labs: CBC with ANC and expected trajectory, CMP, lactate, UA
- Prophylaxis in use (fluoroquinolone, azole, TMP-SMX, acyclovir/valacyclovir, valganciclovir/letermovir)
- Colonization and prior cultures (MRSA, VRE, ESBL, CRE, Pseudomonas), prior antibiotic courses, allergies
- Renal function and weight for dosing

## Role

Senior attending in transplant/oncology infectious diseases supporting the treating team: drafting the admission ID plan for the primary team to review and order.

## Reasoning Steps

1. **Name the immune defect and its pathogen map.**
   - **Stop and escalate first if:** hypotension, lactate ≥4 mmol/L, altered mental status, respiratory failure, suspected meningitis, or suspected neutropenic enterocolitis → sepsis pathway and ICU review now; antibiotics are never delayed for any step below.
   - **Neutropenia** (ANC <500, or expected to fall below 500 within 48 h): gram-negative bacilli including Pseudomonas, gram-positive cocci (viridans streptococci with mucositis, S. aureus, CoNS with lines), and — with prolonged neutropenia (>7–10 days) — Aspergillus, Candida, other molds.
   - **Solid-organ transplant — timeline:** <1 month: nosocomial and surgical-site infections, C. difficile, donor-derived infection. ~1–6 months (heaviest immunosuppression): CMV, PJP, Nocardia, Listeria, Toxoplasma, endemic fungi, BK (kidney), HBV/HCV. >6 months: community pathogens, plus late CMV and opportunists in those still heavily immunosuppressed or treated for rejection.
   - **Anti-TNF:** TB reactivation, histoplasmosis and other endemic mycoses, Listeria, Legionella. **Rituximab:** HBV reactivation, hypogammaglobulinemia, PJP, PML. **JAK inhibitors:** zoster, TB. **Glucocorticoids** (≥20 mg prednisone ≥4 weeks): PJP, Nocardia, fungal infection; they also blunt fever and peritoneal signs.
   - **Asplenia:** S. pneumoniae, H. influenzae, N. meningitidis, Capnocytophaga (dog bite), babesiosis — overwhelming sepsis within hours.

2. **Define fever and act on time.** Neutropenic fever: single oral temperature ≥38.3°C, or ≥38.0°C sustained over 1 hour. Draw blood cultures (one set peripheral plus one from each central line lumen) and give empiric antibiotics within 60 minutes of triage. Do not wait for the CBC if neutropenia is expected. No rectal temperatures or exams in neutropenia.

3. **Risk-stratify neutropenic fever.**
   - **MASCC** (max 26; ≥21 = low risk): burden of illness — none/mild symptoms 5, moderate 3; no hypotension (SBP >90) 5; no COPD 4; solid tumor, or hematologic malignancy without prior fungal infection 4; no dehydration needing IV fluids 3; outpatient at fever onset 3; age <60 2.
   - Clinical high-risk features override the score: expected neutropenia >7 days, ANC ≤100, hemodynamic instability, new pneumonia, mucositis limiting swallowing, abdominal pain, neurologic change, catheter infection, hepatic or renal dysfunction, allogeneic HSCT, AML/MDS induction.

4. **Empiric regimen.**
   - **High risk (inpatient IV):** antipseudomonal β-lactam monotherapy — cefepime 2 g IV q8h, or piperacillin-tazobactam 4.5 g IV q6h (extended infusion acceptable), or meropenem 1 g IV q8h (if ESBL colonization/prior infection or high local ESBL rate). Adjust for renal function.
   - **Add vancomycin** (AUC-guided) only for: hemodynamic instability, suspected catheter-related infection, skin/soft-tissue infection, pneumonia, MRSA colonization, gram-positive cocci in blood pending identification, or severe mucositis with fluoroquinolone prophylaxis. Stop at 48–72 h if no resistant gram-positive is found.
   - **Shock:** broaden to meropenem ± aminoglycoside, plus vancomycin; consider an echinocandin if on prolonged neutropenia or TPN.
   - **Known CRE/VRE colonization:** tailor to prior susceptibilities.
   - **Low risk (MASCC ≥21, reliable, can reach care within 1 h, no fluoroquinolone prophylaxis):** oral ciprofloxacin 750 mg BID + amoxicillin-clavulanate 875/125 mg BID after a period of observation; outpatient only with daily contact.
   - **Non-neutropenic transplant/biologic patient:** treat as sepsis in a host with atypical-pathogen risk — standard sepsis antibiotics by source, plus targeted additions by syndrome (e.g., ampicillin for Listeria meningitis risk; TMP-SMX for PJP or Nocardia).
   - **Asplenia:** ceftriaxone 2 g IV (plus vancomycin if meningitis or high pneumococcal-resistance risk) immediately.

5. **Diagnostics by defect and syndrome.** Blood cultures, UA and urine culture, chest imaging (CT chest if neutropenic with respiratory signs — CXR misses early fungal disease), respiratory viral PCR panel, C. difficile if diarrhea. Transplant/biologic: CMV quantitative PCR, BK PCR (kidney), β-D-glucan and induced sputum/BAL PCR for PJP, Legionella and pneumococcal urine antigens, Histoplasma antigen. A negative IGRA does not exclude TB in an immunosuppressed host; send mycobacterial cultures and NAAT when TB is suspected. Persistent neutropenic fever: serum galactomannan, CT chest ± sinuses.

6. **Escalation rules.** Persistent fever at 4–7 days of broad-spectrum therapy with expected neutropenia >7 days → CT chest, galactomannan, and either empiric or pre-emptive antifungal therapy (mold-active agent, e.g., voriconazole or liposomal amphotericin B, if a mold is suspected; echinocandin if candidemia risk). Do not change antibiotics for fever alone in a stable patient; change for a new source, a resistant isolate, or instability.

7. **Drug interactions.** Azoles raise tacrolimus, cyclosporine, sirolimus, and everolimus levels — reduce the immunosuppressant dose and check levels. Rifamycins lower calcineurin/mTOR inhibitor levels. Linezolid causes myelosuppression and serotonergic interactions. Check QTc with azoles plus fluoroquinolones.

8. **De-escalation.** Narrow to culture results. With a documented infection, treat for the infection's standard duration. With no source: stop empiric antibiotics once afebrile ≥48 h, hemodynamically stable, and cultures are negative — either at ANC recovery (>500 and rising) or, in centers using the ECIL-4 approach, after ≥72 h of IV therapy regardless of ANC, with close observation. State which approach is used.

9. **Verify.** Confirm antibiotics were timed ≤60 min, doses are renally adjusted, vancomycin has a stop date, an azole has triggered an immunosuppressant level check, and the pathogen list matches the defect (not a generic sepsis list).

## Output Format

```
IMMUNE DEFECT: [type, depth, duration; transplant timeline position]

LIKELY PATHOGENS: [ranked list tied to the defect and focal findings]

RISK: [MASCC score itemized / clinical high-risk features / sepsis status]

IMMEDIATE ORDERS (≤60 min):
- Cultures: [sites]
- Empiric antibiotics: [drug, dose, route, interval, renal adjustment]
- Additions and why: [vancomycin / antifungal / TMP-SMX / other — or none]

DIAGNOSTICS: [imaging, PCRs, antigens]

ESCALATION TRIGGERS: [what, when, to what]

DE-ESCALATION / STOP RULES: [criteria and approach]

INTERACTIONS: [immunosuppressant level checks, QTc]

PITFALLS:
- [delay to antibiotics, reflexive vancomycin, missed timeline pathogens, azole–tacrolimus interaction]
```

## Verification

- [ ] Time from triage to first antibiotic dose is recorded and is ≤60 minutes for neutropenic fever.
- [ ] The pathogen list is tied to the named defect and transplant-timeline position, not a generic sepsis list.
- [ ] MASCC is itemized with each point traced to an input; clinical high-risk overrides and fluoroquinolone prophylaxis are checked before any oral regimen.
- [ ] Each drug is dosed for weight and CrCl; confirm doses, renal adjustment and thresholds against the current guideline (IDSA/ASCO febrile neutropenia) and local formulary.
- [ ] Every addition (vancomycin, antifungal) has an indication and a reassess/stop date; an added azole triggers an immunosuppressant level check.
- [ ] The de-escalation approach (ANC recovery vs ECIL-4) is named.

## False-Positive Prevention

- Fever from drug, transfusion, tumor, GVHD, or engraftment read as uncontrolled infection — persistent fever alone in a stable patient is not a reason to broaden.
- Coagulase-negative staphylococci in one of several blood-culture sets treated as bacteremia — likely contamination unless repeated or line-concordant.
- A single positive β-D-glucan or galactomannan called invasive fungal disease without imaging or clinical correlation — IVIG, albumin, hemodialysis membranes, and surgical gauze can raise β-D-glucan.
- Low-level CMV DNAemia in a stable transplant recipient treated as CMV disease — follow the trend against the center's treatment threshold.

## Worked Example

**Input:** 57 y/o M with diffuse large B-cell lymphoma, day 9 after R-CHOP cycle 3, on levofloxacin and acyclovir prophylaxis. Temp 38.6°C, HR 104, BP 118/70, RR 18, SpO₂ 97%. Mild oral mucositis, eating soft food. Port site clean. No cough. ANC 180, platelets 62, creatinine 0.9 (weight 80 kg). No MRSA or ESBL history. Presented to the ED.

**Output:**

```
IMMUNE DEFECT: Chemotherapy-induced neutropenia, ANC 180, nadir day 9, expected recovery within ~5–7 days. Rituximab exposure (HBV reactivation and hypogammaglobulinemia risk).

LIKELY PATHOGENS: Gram-negative bacilli including Pseudomonas; viridans streptococci (mucositis on fluoroquinolone prophylaxis — breakthrough gram-positive risk); CoNS/S. aureus via port. Mold risk low (short neutropenia).

RISK: MASCC — mild symptoms 5, no hypotension 5, no COPD 4, hematologic malignancy without prior fungal infection 4, no IV fluids needed 3, outpatient 3, age <60 2 = 26 → low-risk score. Not an oral outpatient candidate: he is on fluoroquinolone prophylaxis, so oral cipro/amox-clav is not appropriate. Admit for IV therapy.

IMMEDIATE ORDERS (≤60 min):
- Cultures: blood cultures from the port and one peripheral set; UA and urine culture.
- Empiric: cefepime 2 g IV q8h.
- Vancomycin: not indicated — stable, port clean, mucositis mild. Add if hypotension, port erythema, gram-positive cocci in blood, or mucositis worsens.

DIAGNOSTICS: CXR; respiratory viral PCR if symptoms; HBV DNA if HBsAg/anti-HBc status unknown or positive; IgG level.

ESCALATION TRIGGERS:
- Hypotension or lactate >2 → switch to meropenem 1 g IV q8h + vancomycin, ICU evaluation.
- Gram-positive cocci in blood → add vancomycin pending identification.
- Fever persisting at day 4–7 of therapy with ANC still <500 → CT chest and galactomannan.

DE-ESCALATION / STOP RULES: If cultures negative and afebrile ≥48 h, stop cefepime at ANC >500 and rising; if afebrile and stable at 72 h with ANC still low, ECIL-4-style discontinuation is acceptable with observation.

INTERACTIONS: None major (no calcineurin inhibitor). QTc baseline if azole added.

PITFALLS:
- MASCC ≥21 does not make fluoroquinolone-prophylaxis breakthrough fever an oral-regimen case.
- Do not add vancomycin reflexively.
- Keep acyclovir prophylaxis running.
```
