---
title: "Anxiety Pharmacologic Algorithm Reasoner (GAD / Panic / SAD)"
category: psychology/psychiatric-prescriber
description: "Reason through pharmacologic management of generalized anxiety, panic disorder, and social anxiety disorder: SSRI/SNRI first-line, activation-aware titration, benzodiazepine role and risks, buspirone, and pregabalin/hydroxyzine/propranolol adjuncts, with CBT/exposure integration."
techniques:
  - RT-02
  - DT-01
  - DS-02
  - QA-04
  - CM-02
difficulty: advanced
intended_use: model-testing
tags:
  - GAD
  - panic-disorder
  - social-anxiety
  - SSRI
  - benzodiazepine
  - buspirone
  - psychopharmacology
updated: "2026-06-08"
related_prompts:
  - domain-psychology/psychiatric-prescriber/psychology_depression_med_algorithm_reasoner.md
  - domain-psychology/psychiatric-prescriber/psychology_controlled_substance_agreement_drafter.md
  - domain-psychology/psychiatric-prescriber/psychology_psychotropic_taper_plan.md
  - domain-psychology/treatment-planning/psychology_measurement_based_care_plan.md
---

# Anxiety Pharmacologic Algorithm Reasoner (GAD / Panic / SAD)

## Objective

Produce a structured pharmacologic reasoning pathway for an adult with a primary anxiety disorder — generalized anxiety disorder (GAD), panic disorder, or social anxiety disorder (SAD) — that selects a first-line agent, paces titration to minimize activation, defines the role and risks of benzodiazepines and adjuncts, and integrates psychotherapy. The reasoning must name the drug class AND a representative generic agent with dosing, anchor to recognized frameworks (APA, NICE, CANMAT) by name, and respect substance-use and dependence risk.

## When to Use

- Initiating pharmacotherapy for GAD, panic disorder, or SAD.
- Deciding whether/when to add or remove a benzodiazepine.
- Managing early-treatment activation/jitteriness on an SSRI/SNRI.
- Selecting an adjunct for partial response or specific contexts (performance anxiety, insomnia).

## Inputs / Context Required

- **Primary anxiety diagnosis** and any comorbid depression, PTSD, OCD, substance use, or bipolarity.
- **Symptom severity**: GAD-7 (and PDSS-SR for panic, LSAS-SR for SAD) now vs baseline.
- **Prior trials**: agent, dose, duration, response, tolerability.
- **Substance-use history** (alcohol, sedatives, opioids) — bears directly on benzodiazepine risk.
- **Comorbid medical** factors: respiratory disease, fall risk/age, hepatic impairment, QTc, pregnancy/lactation.
- **Concurrent medications** for interaction screening (sedative load, CYP).
- **Access to/engagement with CBT/exposure**.
- `[clinician input required: history of sedative or alcohol use disorder]`
- `[clinician input required: occupation/safety-sensitive duties affecting sedation tolerance]`

## Constraints

### Must

- Establish SSRIs and SNRIs as **first-line** maintenance therapy across GAD, panic, and SAD (e.g., escitalopram, sertraline, paroxetine, venlafaxine XR, duloxetine).
- **Start low and titrate slowly** in panic disorder and activation-prone patients (e.g., half the usual starting dose for 1–2 weeks) to reduce early jitteriness/activation that can mimic worsening anxiety; counsel that full anxiolytic onset takes 4–6+ weeks.
- Define the **benzodiazepine role** as time-limited and adjunctive (e.g., bridging during SSRI onset or for severe acute distress), with explicit cautions: tolerance, physiologic dependence, withdrawal (including seizure risk on abrupt discontinuation), cognitive/psychomotor impairment, fall risk in elderly, and **contraindication/high-caution with comorbid SUD, opioids, and respiratory compromise**. Reference a controlled-substance agreement when chronic use is contemplated.
- Name **buspirone** (GAD; 15–60 mg/day divided; no dependence; delayed onset; not effective for panic).
- Name context-appropriate **adjuncts**: **pregabalin** (GAD evidence; sedation, misuse potential, renal dosing), **hydroxyzine** (short-term GAD; sedation, anticholinergic, QTc), **propranolol** (performance/situational anxiety; check asthma/bradycardia/BP) — clarify it does not treat generalized chronic anxiety.
- Integrate **CBT/exposure** as first-line or co-first-line; specify combining medication with exposure for panic and SAD.
- State the antidepressant **black-box suicidality warning** (< 25), discontinuation-syndrome caution (especially paroxetine/venlafaxine), and serotonergic interaction cautions.
- Anchor to a named framework without fabricating page citations.

### Must Not

- Do not present chronic benzodiazepine monotherapy as a standard maintenance strategy for an anxiety disorder.
- Do not start a benzodiazepine in a patient with active SUD or on opioids without explicit risk documentation and justification.
- Do not use propranolol or hydroxyzine as if they treat generalized chronic anxiety long-term.
- Do not titrate an SSRI/SNRI at full standard speed in a panic-prone patient if activation risk is high.
- Do not fabricate trial history or scores; flag with `[clinician input required: ...]`.

## Instructions

1. **Confirm the primary anxiety diagnosis** and screen comorbidity (depression, PTSD, OCD, SUD, bipolarity).
2. **Quantify severity** with GAD-7 (± PDSS-SR / LSAS-SR) vs baseline.
3. **Select first-line SSRI/SNRI** matched to the disorder and comorbidity; specify a **slow-start titration** plan for panic/activation-prone patients.
4. **Decide the benzodiazepine question** explicitly: indicated as a short bridge? contraindicated? If used, define duration, dose ceiling, taper plan, and monitoring; reference the controlled-substance agreement.
5. **Select adjuncts** if warranted (buspirone for GAD augmentation; pregabalin/hydroxyzine/propranolol per context) with cautions.
6. **Integrate psychotherapy** (CBT/exposure) and specify the combination plan.
7. **State warnings/interactions** for chosen agents.
8. **Set the re-measurement plan**, a **risk-reassessment hook**, and a co-sign line for higher-risk regimens (e.g., benzodiazepine with comorbidity).
9. Run verification.

## Output Format

```
=== ANXIETY PHARMACOLOGIC ALGORITHM REASONING ===

FRAMEWORK REFERENCED: [APA / NICE / CANMAT]
PRIMARY DIAGNOSIS: [GAD / Panic / SAD]   COMORBIDITY: [...]

SEVERITY
GAD-7: now [..] / baseline [..]   PDSS-SR (panic): [..]   LSAS-SR (SAD): [..]

PRIOR TRIALS
| Agent (generic) | Dose | Duration | Response | Tolerability |
|-----------------|------|----------|----------|--------------|
| [...] | [...] | [...] | [...] | [...] |

FIRST-LINE SELECTION (SSRI / SNRI)
Agent: [Class — representative generic]   Start dose → target: [...]
Titration plan: [slow-start if panic/activation-prone — e.g., half-dose × 1–2 wks]
Onset counseling: [4–6+ wks for full anxiolysis; activation may precede benefit]

BENZODIAZEPINE DECISION
Indicated as bridge? [Yes — agent/dose/duration ceiling/taper | No — reason]
Risks documented: [tolerance, dependence, withdrawal/seizure, sedation, falls, SUD/opioid/respiratory caution]
Controlled-substance agreement: [see psychology_controlled_substance_agreement_drafter.md if chronic use considered]

ADJUNCTS (context-specific)
Buspirone (GAD): [15–60 mg/day divided; delayed onset; not for panic]
Pregabalin (GAD): [sedation, misuse, renal dosing]
Hydroxyzine (short-term): [sedation, anticholinergic, QTc]
Propranolol (situational/performance): [asthma/bradycardia/BP checks; not for chronic generalized anxiety]

PSYCHOTHERAPY INTEGRATION
CBT / exposure: [first-line or combined; plan to pair meds with exposure for panic/SAD]

WARNINGS / INTERACTIONS
Black-box suicidality (<25): [...]   Discontinuation syndrome: [paroxetine/venlafaxine]
Serotonergic / sedative interaction cautions: [...]

RE-MEASUREMENT & RISK PLAN
GAD-7 cadence: [...]   Next decision point: [...]
Risk-reassessment hook: [re-screen SI/C-SSRS at next visit and on dose change]

CO-SIGN (higher-risk regimens)
Prescriber: __________  Supervising/collaborating prescriber: __________  Date: ______
```

## Verification

- [ ] Primary anxiety diagnosis confirmed and comorbidity (incl. SUD, bipolarity) screened.
- [ ] Severity quantified with GAD-7 (± panic/SAD-specific measures).
- [ ] SSRI/SNRI established as first-line with class + representative generic + dose/range.
- [ ] Slow-start titration specified for panic/activation-prone patients with onset counseling.
- [ ] Benzodiazepine decision explicit: time-limited role, risks, taper, and SUD/opioid/respiratory cautions.
- [ ] Buspirone and adjuncts (pregabalin/hydroxyzine/propranolol) named with correct indications and cautions.
- [ ] CBT/exposure integration specified.
- [ ] Black-box (<25), discontinuation-syndrome, and serotonergic/sedative cautions stated.
- [ ] No chronic benzodiazepine monotherapy framed as standard maintenance.
- [ ] Re-measurement cadence, risk-reassessment hook, and co-sign present.
- [ ] Framework named without fabricated citations.
- [ ] Nothing fabricated; gaps flagged `[clinician input required]`.
```
