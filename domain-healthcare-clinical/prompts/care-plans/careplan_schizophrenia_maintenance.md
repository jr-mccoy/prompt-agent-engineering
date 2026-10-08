---
title: "Schizophrenia Maintenance Care Plan"
category: domain-healthcare-clinical/care-plans
description: "Build a schizophrenia maintenance plan: antipsychotic selection, long-acting injectable use, clozapine for treatment resistance, metabolic monitoring, and psychosocial care with named drugs and doses."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
  - DS-02
difficulty: advanced
tags:
  - psychiatry
  - schizophrenia
  - antipsychotic
  - care-plan
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

Produce a schizophrenia maintenance care plan: antipsychotic selection and dosing, long-acting injectable consideration, treatment-resistance pathway to clozapine, metabolic and movement-disorder monitoring, and psychosocial supports. Output is a maintenance regimen with monitoring schedule.

## Inputs

- Course: episode number, time since onset, current symptoms (positive/negative/cognitive), relapse history, adherence pattern
- Prior antipsychotics: agents, doses, response, side effects (EPS, akathisia, metabolic, prolactin), number of adequate trials
- Safety: suicide/violence risk, substance use, comorbid mood/anxiety
- Labs/metabolic: weight/BMI, glucose/A1c, lipids, prolactin, ECG/QTc, CBC (for clozapine)
- Psychosocial: housing, support, functional status, insight

## Role

Psychiatrist managing schizophrenia maintenance.

## Reasoning Steps

1. **Maintain antipsychotic — relapse risk is high off medication.** Continue an effective agent at the lowest effective dose; do not routinely discontinue after a first episode without careful risk discussion.

2. **Antipsychotic selection** (efficacy similar except clozapine; choose by side-effect profile):
   - Lower metabolic risk: aripiprazole, ziprasidone, lurasidone.
   - Higher metabolic risk: olanzapine, quetiapine (effective but weight/glucose/lipids).
   - Prolactin elevation: risperidone, paliperidone.
   - Match to the patient's prior response and tolerability.

3. **Long-acting injectable (LAI):** strongly consider for nonadherence, relapse history, or patient preference — reduces relapse/rehospitalization. Options: paliperidone palmitate (monthly, q3-month, q6-month), aripiprazole monthly, risperidone. Overlap oral as labeled when starting.

4. **Adequate trial:** therapeutic dose × 6 weeks. After **two adequate antipsychotic trials** without adequate response → **treatment-resistant schizophrenia → clozapine** (the only agent with superior efficacy here; underused).
   - Clozapine requires ANC monitoring per the current label (agranulocytosis) — US REMS requirements changed in 2025 `[VERIFY: current clozapine label / FDA REMS status]` — and monitoring for myocarditis, seizures, constipation/ileus, metabolic effects, sedation, hypersalivation. Titrate slowly.

5. **Metabolic monitoring** (atypicals): weight/BMI/waist, blood pressure each visit; fasting glucose/A1c and lipids at baseline, 12 weeks, then annually; intervene early (metformin, agent switch, lifestyle).

6. **Movement disorders:** monitor for EPS/akathisia and tardive dyskinesia (AIMS periodically); treat akathisia (propranolol), TD (VMAT2 inhibitors — valbenazine/deutetrabenazine).

7. **Comorbidity:** treat depression/suicidality (clozapine reduces suicidality), substance use, smoking (affects clozapine levels), cardiovascular risk.

8. **Psychosocial:** assertive community treatment / case management, supported employment, family psychoeducation, CBT for psychosis, cognitive remediation, social-skills training — improve function and reduce relapse.

9. **Monitor:** symptoms/relapse signs, adherence, metabolic, movement, prolactin if symptomatic, QTc as indicated, clozapine ANC per protocol.

## False-Positive Prevention

❌ **DON'T:**
- Count a trial as "adequate" because the drug name appears in the history — each needs a therapeutic dose, ≥6 weeks at that dose and evidence of adherence (LAI, pill count, level), as in the TRRIP consensus criteria; otherwise label it "adequacy unconfirmed".
- Reuse one LAI start regimen across products — aripiprazole monohydrate, aripiprazole lauroxil, paliperidone palmitate (deltoid loading) and olanzapine pamoate (post-injection observation) all start differently; take it from the clinician's order or `[VERIFY: product label]`.
- Write "metabolic monitoring in place" when the plan lists a schedule but no baseline weight, waist, BP, fasting glucose/A1c and lipids with dates.
- State the clozapine monitoring scheme from memory or apply one ANC cutoff to every patient — benign ethnic neutropenia/Duffy-null phenotype changes the thresholds, and US monitoring requirements changed in 2025 `[VERIFY: current clozapine label]`.
- Leave the dose unaddressed when smoking status changes (quitting, a smoke-free admission) — CYP1A2 induction falls and clozapine/olanzapine levels rise.

✅ **DO:**
- Build a trials table from the input — agent, maximum dose, weeks at dose, adherence evidence, response, adverse effect — and make the clozapine recommendation cite the rows that qualify.
- Check that every relapse the plan attributes to nonadherence has evidence in the input (missed fills, missed injections, patient report, level) rather than being inferred from the relapse itself.
- Before a QT-prolonging agent or combination, quote the QTc value and date, and check the list for clozapine-level interactions (fluvoxamine, ciprofloxacin) whenever clozapine is on the pathway.

## Output Format

```
COURSE / CURRENT SYMPTOMS / ADHERENCE PATTERN:

MAINTENANCE REGIMEN:
- Antipsychotic: [agent, dose, rationale]
- LAI consideration + product
- Lowest effective dose plan

TREATMENT-RESISTANCE PATHWAY:
- Two adequate trials → clozapine + monitoring protocol

METABOLIC MONITORING:
- Weight/glucose/lipids schedule + intervention

MOVEMENT MONITORING:
- EPS/akathisia/TD (AIMS), treatments

COMORBIDITY:
- Depression/suicide, substance, smoking, CV

PSYCHOSOCIAL:
- ACT/case mgmt, supported employment, family psychoed, CBTp

MONITORING:
- Symptoms, adherence, metabolic, movement, ANC if clozapine

PITFALLS:
- [discontinuation relapse, delaying clozapine, ignoring metabolic burden, missing TD, LAI underuse]
```

## Worked Example

**Input:** 26 y/o M, schizophrenia, 3 relapses in 2 years all following oral medication nonadherence. Adequate trials of risperidone and aripiprazole oral with partial response when adherent. Currently on aripiprazole 15 mg oral, residual paranoia, BMI 29, glucose normal, no TD. Smokes, cannabis use.

**Output:**

```
COURSE / SYMPTOMS / ADHERENCE: relapsing course driven by oral nonadherence; partial response to two agents when adherent; residual positive symptoms.

MAINTENANCE REGIMEN:
- The core problem is adherence → switch to an LAI: aripiprazole once-monthly LAI (he tolerates/partially responds to aripiprazole) with the labeled oral overlap (14 days). This directly targets the relapse driver.
- Optimize dose; lowest effective maintenance dose once stable.

TREATMENT-RESISTANCE PATHWAY:
- He has had two adequate trials but with adherence as the confound — relapses were nonadherence, not true resistance. Establish adherence via LAI first.
- If residual paranoia persists on a guaranteed-delivery LAI at adequate dose, that becomes a genuine adequate trial; after a second confirmed-adherent failure → clozapine (with ANC/myocarditis/metabolic monitoring).

METABOLIC MONITORING:
- BMI 29 — weight, BP each visit; fasting glucose/A1c + lipids baseline, 12 wk, annually. Aripiprazole is metabolically favorable; lifestyle counseling.

MOVEMENT MONITORING:
- No TD now; periodic AIMS; watch aripiprazole akathisia (propranolol if it emerges).

COMORBIDITY:
- Substance: cannabis worsens psychosis/relapse — motivational interviewing, SUD referral.
- Smoking: counsel cessation; note smoking induces CYP1A2 (relevant if clozapine later — levels change with smoking status).

PSYCHOSOCIAL:
- Case management/ACT given relapse pattern, family psychoeducation, supported employment, CBT for psychosis.

MONITORING: relapse early-warning signs, LAI adherence, metabolic, movement, substance use.

PITFALLS:
- Don't escalate to clozapine before securing adherence (the relapses were nonadherence) — but don't withhold clozapine either if a truly adherent trial fails.
- Don't ignore the modifiable cannabis/smoking contributors.
- LAI is the highest-yield change here.
```
