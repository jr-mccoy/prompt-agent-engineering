---
title: "ADHD Pharmacologic Algorithm Reasoner (Stimulant / Non-Stimulant)"
category: psychology/psychiatric-prescriber
description: "Reason through stimulant (methylphenidate vs amphetamine class) and non-stimulant (atomoxetine, viloxazine, alpha-2 agonists) selection, titration, cardiac/BP/growth monitoring, diversion-and-misuse mitigation, and comorbidity sequencing for ADHD."
techniques:
  - RT-02
  - DT-01
  - DS-02
  - QA-04
  - CM-02
difficulty: advanced
intended_use: model-testing
tags:
  - ADHD
  - stimulant
  - methylphenidate
  - amphetamine
  - atomoxetine
  - diversion-mitigation
  - psychopharmacology
updated: "2026-06-08"
related_prompts:
  - domain-psychology/psychiatric-prescriber/psychology_controlled_substance_agreement_drafter.md
  - domain-psychology/psychiatric-prescriber/psychology_med_management_progress_note.md
  - domain-psychology/psychiatric-prescriber/psychology_anxiety_med_algorithm_reasoner.md
  - domain-psychology/treatment-planning/psychology_measurement_based_care_plan.md
---

# ADHD Pharmacologic Algorithm Reasoner (Stimulant / Non-Stimulant)

## Objective

Produce a structured pharmacologic reasoning pathway for ADHD across the lifespan that selects between stimulant classes (methylphenidate vs amphetamine) and non-stimulants (atomoxetine, viloxazine, alpha-2 agonists), specifies titration, defines cardiovascular/blood-pressure/growth monitoring, builds diversion-and-misuse mitigation, and sequences treatment around comorbidities (anxiety, substance use disorder, tics). The reasoning must name the class AND a representative generic agent with dosing, anchor to recognized frameworks (AAP, AACAP for youth; adult ADHD guidance) by name, and incorporate a controlled-substance agreement when a stimulant is prescribed.

## When to Use

- Initiating pharmacotherapy after a confirmed ADHD diagnosis.
- Choosing between stimulant and non-stimulant given comorbidity or misuse/diversion risk.
- A patient has failed or not tolerated one stimulant class and a switch is considered.
- Sequencing ADHD treatment alongside anxiety, SUD, or tic disorders.

## Inputs / Context Required

- **Confirmed ADHD diagnosis** and presentation (inattentive/hyperactive-impulsive/combined); age band (child/adolescent/adult).
- **Baseline rating scale**: Vanderbilt / Conners (youth) or ASRS / adult symptom scale.
- **Cardiovascular history**: personal/family history of sudden cardiac death, structural heart disease, arrhythmia; baseline HR/BP; need for cardiology clearance.
- **Growth data** (pediatrics): height/weight percentiles and trajectory.
- **Substance-use history** and diversion/misuse risk; household members at risk.
- **Comorbidities**: anxiety, depression, tics/Tourette, SUD, sleep, bipolarity.
- **Prior trials**: agent, class, dose, response, tolerability.
- `[clinician input required: cardiac red flags or family history requiring cardiology evaluation]`
- `[clinician input required: PDMP review result and diversion-risk assessment]`

## Constraints

### Must

- Confirm the diagnosis and obtain a **baseline rating scale**; treatment response is tracked against it.
- Establish **stimulants as first-line** for most patients without contraindication: **methylphenidate-class** (methylphenidate, dexmethylphenidate) and **amphetamine-class** (mixed amphetamine salts, lisdexamfetamine, dextroamphetamine). State that response to the two classes is individual; non-response/intolerance to one class warrants trying the other.
- Specify **titration**: start low, titrate at intervals (e.g., weekly) to effect/tolerability; describe long-acting vs immediate-release roles and duration coverage.
- Define **cardiovascular/BP monitoring**: baseline and on-treatment HR and BP at each titration and follow-up; screen cardiac history/family history; obtain EKG/cardiology only if red flags; counsel on the stimulant warning for serious cardiovascular events and on caution with structural cardiac disease.
- Define **growth monitoring** in pediatrics: plot height/weight at baseline and periodically; address appetite suppression and consider drug holidays if growth deceleration; monitor for sleep and mood effects.
- Build **diversion/misuse mitigation**: PDMP check, single-prescriber/single-pharmacy, quantity limits, safe storage, prefer lower-abuse-liability formulations (e.g., lisdexamfetamine prodrug, osmotic-release MPH) when misuse risk is elevated, and a **controlled-substance agreement**.
- Name **non-stimulants** with indications: **atomoxetine** (SNRI/NRI; non-controlled; delayed onset 4–6 wks; black-box suicidality in youth; hepatic caution), **viloxazine ER** (non-controlled; pediatric/adult), **alpha-2 agonists guanfacine ER / clonidine ER** (useful with tics, sleep, or as adjunct; monitor BP/HR, sedation, rebound on abrupt stop). Prefer non-stimulants when SUD/diversion risk is high or stimulants are not tolerated.
- **Sequence comorbidities**: in active SUD, prefer non-stimulant or lower-abuse-liability stimulant with safeguards; with prominent anxiety, treat/monitor anxiety (stimulants can worsen it); with tics, consider alpha-2 agonist or careful stimulant trial (stimulants are not absolutely contraindicated with tics).
- Anchor to a named framework without fabricating page citations.

### Must Not

- Do not initiate a stimulant without cardiovascular screening and baseline HR/BP.
- Do not omit growth monitoring in pediatric patients.
- Do not prescribe a controlled stimulant without PDMP review and a controlled-substance agreement when risk is present.
- Do not present atomoxetine/viloxazine as fast-onset; state the delayed onset.
- Do not stop an alpha-2 agonist abruptly (rebound hypertension); specify taper.
- Do not fabricate scales, growth data, or cardiac history; flag with `[clinician input required: ...]`.

## Instructions

1. **Confirm diagnosis and baseline scale**; record age band and presentation.
2. **Screen cardiovascular history** and obtain baseline HR/BP; flag any red flags for cardiology.
3. **Assess diversion/misuse and SUD risk**; review PDMP.
4. **Select the class/agent**:
   - Default → first-line stimulant (MPH-class or amphetamine-class); choose formulation by needed duration and misuse risk.
   - Elevated SUD/diversion risk or stimulant intolerance → non-stimulant (atomoxetine/viloxazine/alpha-2).
5. **Specify titration** and the long-acting/immediate-release coverage plan.
6. **Define monitoring**: cardiovascular/BP at each visit; growth in pediatrics; sleep/appetite/mood.
7. **Build diversion mitigation** and reference the controlled-substance agreement.
8. **Sequence comorbidities** (anxiety, SUD, tics) explicitly.
9. **Set re-measurement** against the baseline scale and a **risk-reassessment hook**; add a co-sign line where a trainee prescribes a controlled substance.
10. Run verification.

## Output Format

```
=== ADHD PHARMACOLOGIC ALGORITHM REASONING ===

FRAMEWORK REFERENCED: [AAP / AACAP (youth) / adult ADHD guidance]
DIAGNOSIS/PRESENTATION: [inattentive/HI/combined]   AGE BAND: [child/adolescent/adult]
BASELINE SCALE: [Vanderbilt/Conners/ASRS] score: [..]

CARDIOVASCULAR & RISK SCREEN
CV history (personal/family): [...]   Baseline HR/BP: [..]   Cardiology needed: [Yes/No]
PDMP review: [clinician input required]   Diversion/misuse risk: [low/elevated — basis]
SUD history: [...]

PRIOR TRIALS
| Agent (class/generic) | Dose | Response | Tolerability |
|-----------------------|------|----------|--------------|
| [...] | [...] | [...] | [...] |

CLASS / AGENT SELECTION
[First-line stimulant: MPH-class (methylphenidate/dexmethylphenidate) | amphetamine-class (MAS/lisdexamfetamine/dextroamphetamine)]
[or Non-stimulant: atomoxetine | viloxazine ER | guanfacine ER / clonidine ER]
Formulation/duration: [long-acting vs IR; misuse-liability consideration]
Start dose → titration: [start low; weekly titration to effect/tolerability]

MONITORING
Cardiovascular/BP: [HR/BP at each titration + follow-up; EKG/cardiology only if red flags]
Growth (pediatrics): [height/weight percentiles baseline + periodic; drug-holiday consideration]
Appetite / sleep / mood: [...]
Non-stimulant specifics: [atomoxetine onset 4–6 wks + youth suicidality warning + hepatic; alpha-2 BP/HR + taper]

DIVERSION / MISUSE MITIGATION
[PDMP check; single-prescriber/single-pharmacy; quantity limits; safe storage; prefer prodrug/osmotic formulations
when risk elevated; controlled-substance agreement — see psychology_controlled_substance_agreement_drafter.md]

COMORBIDITY SEQUENCING
Anxiety: [stimulants can worsen — monitor/treat]   SUD: [prefer non-stimulant or low-abuse-liability + safeguards]
Tics: [alpha-2 agonist or careful stimulant trial — not absolutely contraindicated]

RE-MEASUREMENT & RISK PLAN
Rating-scale cadence: [...]   Next decision point: [...]
Risk-reassessment hook: [re-screen mood/SI (esp. atomoxetine youth); reassess CV at dose changes]

CO-SIGN (trainee prescribing controlled substance)
Prescriber: __________  Supervising/collaborating prescriber: __________  Date: ______
```

## Verification

- [ ] Diagnosis confirmed and baseline rating scale recorded.
- [ ] Cardiovascular history screened; baseline HR/BP recorded; cardiology only if red flags.
- [ ] Stimulant classes (MPH vs amphetamine) presented as first-line with class + representative generics.
- [ ] Titration and long-acting/IR coverage specified.
- [ ] Growth monitoring specified for pediatric patients.
- [ ] Non-stimulants named with correct onset/warnings (atomoxetine delayed onset + youth suicidality; alpha-2 taper).
- [ ] Diversion/misuse mitigation incl. PDMP and controlled-substance agreement built in.
- [ ] Comorbidity sequencing (anxiety, SUD, tics) addressed.
- [ ] Re-measurement cadence and risk-reassessment hook present; co-sign line where applicable.
- [ ] Framework named without fabricated citations.
- [ ] Nothing fabricated; gaps flagged `[clinician input required]`.
```
