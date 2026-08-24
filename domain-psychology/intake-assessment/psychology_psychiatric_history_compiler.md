---
title: "Psychiatric History Compiler"
category: psychology/intake-assessment
description: "Compile a structured past psychiatric history covering prior diagnoses, providers, medications with response/side effects, hospitalizations, and longest period of stability for an adult intake."
techniques:
  - ST-04
  - DT-02
  - CM-02
  - QA-04
  - DS-04
difficulty: intermediate
intended_use: model-testing
tags:
  - psychiatric-history
  - medication-history
  - hospitalization
  - prior-treatment
  - intake
  - cpt-90791
  - cpt-90792
updated: "2026-06-08"
related_prompts:
  - domain-psychology/documentation/psychology_intake_assessment_note.md
  - domain-psychology/intake-assessment/psychology_medical_history_for_psych_intake.md
  - domain-psychology/intake-assessment/psychology_screening_battery_interpreter.md
  - domain-psychology/diagnostic-formulation/psychology_case_conceptualization_framework.md
---

# Psychiatric History Compiler

## Objective

Compile a complete, structured Past Psychiatric History (PPH) that:

1. Documents prior DSM diagnoses with approximated dates, treating providers, and treatment setting.
2. Creates a medication chronology: each psychotropic agent tried, approximate dates, reason for use, maximum dose, clinical response, side effects, and reason for discontinuation.
3. Documents psychiatric hospitalizations, ED psychiatric presentations, IOP/PHP, and residential/SUD treatment episodes.
4. Identifies the client's longest period of psychiatric stability and the factors associated with it.
5. Surfaces treatment history patterns clinically relevant to current planning: treatment-resistant episodes, prior medication intolerance, preferred modalities, and medication classes already exhausted.

## When to Use

- At every adult psychiatric intake; this is a required section for CPT 90791/90792.
- When records are unavailable and clinician must rely on client self-report with appropriate caveats.
- When transferring care and a synthesized PPH is needed to brief an incoming provider.
- When building a medication decision framework for a current treatment-resistant presentation.

## Inputs / Context Required

- **Prior psychiatric diagnoses:** What diagnoses the client reports receiving, approximate year first diagnosed, who made the diagnosis (psychiatrist, PCP, therapist, self-diagnosed, ED), and the client's acceptance of or disagreement with each diagnosis.
- **Prior outpatient providers:** Type (psychiatrist, psychologist, LCSW, LPC, LMFT, PCP providing psych meds, NP), approximate treatment duration, reason for ending.
- **Medication chronology:** For each psychotropic medication ever tried — medication name and class, starting dose and maximum dose, approximate start/end dates, indication, clinical response (improved / partially improved / no response), side effects experienced, reason for discontinuation (side effects, non-response, cost, patient preference, provider decision, pregnancy).
- **Psychiatric hospitalizations:** Number of total inpatient admissions; for each — approximate year, duration, admitting diagnosis or chief reason, voluntary or involuntary, discharge diagnosis, discharge medications, discharge disposition.
- **ED psychiatric visits:** Approximate number; reasons; dispositions.
- **IOP / PHP episodes:** Dates, primary treatment focus, completion status.
- **Residential / SUD treatment:** Dates, program type, completion status.
- **Psychotherapy history:** Modalities experienced (CBT, DBT, psychodynamic, supportive, EMDR, etc.); duration; perceived benefit; reason for ending.
- **Longest period of psychiatric stability:** Duration, what the client attributes it to (specific medication, sobriety, life circumstances, therapy), and what precipitated the end of that stable period.
- **Family psychiatric history:** First-degree relatives' diagnoses, medication responses (treatment response can be heritable — especially for lithium, SSRIs, stimulants), psychiatric hospitalizations, suicide history.

## Constraints

### Must

- Compile a complete medication chronology table; each row must capture class, response, side effects, and reason discontinued — not just name and date.
- Flag medication classes that have been fully exhausted for a given indication (e.g., "three SSRIs tried for MDD with inadequate response") as this is directly relevant to treatment-resistance determination and augmentation strategy.
- Document each hospitalization separately with voluntary/involuntary status; involuntary hospitalizations are clinically significant for alliance and trauma considerations.
- Identify longest stability period with client's attribution, as this informs treatment target.
- Note family medication response history where provided; heritable pharmacogenomic patterns (e.g., lithium response, SSRI non-response) are relevant to current prescribing.
- Note any pharmacogenomic testing (GeneSight, Genomind, or equivalent) if previously performed, with results if known.
- Distinguish client-reported diagnoses from confirmed diagnoses; record the client's certainty and any stated disagreements with prior diagnoses.
- Flag when records from prior treatment are unavailable and clinical data rely on client self-report.

### Must Not

- Do not confirm prior diagnoses without records; document as "client reports diagnosis of [X] made by [provider type] in approximately [year] — records not yet reviewed."
- Do not omit hospitalizations because the client minimizes them; document what was reported.
- Do not use trade names as the sole medication identifier — use generic name with trade name in parentheses for readability.
- Do not recommend specific medications in this history section; the PPH informs clinical decision-making but does not itself constitute a treatment recommendation.
- Do not fabricate; gaps are flagged.

## Instructions

1. **Compile prior diagnoses table.** For each diagnosis, record: diagnosis name, approximate year of first diagnosis, source/provider type, client's agreement/disagreement with the diagnosis, current status (active / in remission / questioned).

2. **Build medication chronology table.** Organize chronologically or by medication class. For each agent: generic name (trade name), medication class, approximate dates, indication, maximum dose, clinical response, side effects, reason for discontinuation.

3. **Flag medication patterns.** After the table, note:
   - Medication classes fully exhausted for current presentation.
   - Any medications with good past response (protective for current planning).
   - Side-effect patterns likely to recur (e.g., SSRI-emergent sexual dysfunction, weight gain with specific agents).
   - Prior adverse reactions or serious side effects.

4. **Document psychiatric hospitalizations.** Create a hospitalization log with: year, duration, voluntary/involuntary, reason, discharge diagnosis, discharge medications, disposition.

5. **Document IOP/PHP and residential episodes.**

6. **Document psychotherapy history.** Note each modality, duration, benefit, and ending reason.

7. **Identify and document longest stability period** with client's attribution.

8. **Document family psychiatric history** with particular attention to medication response and suicide history.

9. **Write the PPH Summary paragraph.** In three to five sentences, synthesize the most clinically salient elements: treatment history trajectory, medication response patterns, degree of treatment resistance, prior hospitalization burden, and the stable-period factors that may be replicable.

10. **Run verification.**

## Output Format

```
=== PAST PSYCHIATRIC HISTORY ===

Client: [Initials/MRN]    Date of Service: [YYYY-MM-DD]
Records available: [Yes — sources / No — clinical data based on client self-report]
CPT Context: Section of 90791 biopsychosocial intake note.

─────────────────────────────────────────
PRIOR DIAGNOSES
─────────────────────────────────────────
| Diagnosis (DSM-5-TR label) | Year First Dx | Provider Type | Client Agreement | Current Status |
|----------------------------|---------------|---------------|-----------------|----------------|
| [Diagnosis 1]              | [Approx. year] | [Psychiatrist / PCP / etc.] | [Agrees / Disagrees / Uncertain] | [Active / Remission / Questioned] |
| [Diagnosis 2]              | [...]         | [...]         | [...]           | [...]          |

Note: Diagnoses listed are client-reported; confirmation pending records review where noted.

─────────────────────────────────────────
MEDICATION CHRONOLOGY
─────────────────────────────────────────
| Generic Name (Trade) | Class | Indication | Approx. Dates | Max Dose | Response | Side Effects | Reason D/C |
|----------------------|-------|------------|---------------|----------|----------|--------------|------------|
| [Sertraline (Zoloft)] | SSRI | MDD | [YYYY–YYYY] | [200 mg/day] | [Partial] | [Sexual dysfunction, nausea initial] | [Non-response] |
| [Lithium carbonate]   | Mood stabilizer | Bipolar I | [YYYY–YYYY] | [900 mg/day] | [Good — 18 mo stable] | [Tremor, polyuria] | [Non-adherence] |
| [...]                 | [...] | [...]      | [...]         | [...]    | [...]    | [...]        | [...]      |

─────────────────────────────────────────
MEDICATION PATTERN ANALYSIS
─────────────────────────────────────────
Classes exhausted for current indication:
  [e.g., "Three SSRIs tried for MDD (sertraline, escitalopram, fluoxetine) — all with inadequate
  antidepressant response; meets criteria for Treatment-Resistant Depression (TRD) consideration."]

Prior positive responses:
  [e.g., "Lithium associated with longest stability period (18 months); worth considering reinitiation
  if bipolar diagnosis confirmed."]

Side-effect patterns likely to recur:
  [e.g., "SSRI-emergent sexual dysfunction reported on sertraline and escitalopram — relevant to
  future SSRI selection."]

Serious adverse reactions / contraindications:
  [e.g., "Reported Stevens-Johnson rash on lamotrigine — do not rechallenge."]

Pharmacogenomic testing:
  [Not performed / Performed (GeneSight) on [date] — results: [...]  / Results not available]

─────────────────────────────────────────
PSYCHIATRIC HOSPITALIZATIONS
─────────────────────────────────────────
Total lifetime inpatient admissions: [X]

| # | Approx. Year | Duration | Voluntary / Involuntary | Admission Reason | Discharge Dx | Discharge Meds | Disposition |
|---|--------------|----------|------------------------|-----------------|--------------|----------------|-------------|
| 1 | [YYYY]       | [X days] | [Vol / Invol — 5150/302] | [SI with plan / Psychosis / Mania] | [F-code] | [...]  | [Outpatient / IOP / Residential] |
| 2 | [...]        | [...]    | [...]                   | [...]           | [...]        | [...]          | [...]       |

ED psychiatric visits: [X total — reasons: [list]; dispositions: [list]]
Note on involuntary holds: [If any, note client's reported experience and treatment alliance implications]

─────────────────────────────────────────
IOP / PHP / RESIDENTIAL EPISODES
─────────────────────────────────────────
| Program Type | Approx. Date | Duration | Primary Focus | Completion | Perceived Benefit |
|--------------|--------------|----------|---------------|------------|-------------------|
| [IOP — MH]   | [YYYY]       | [X weeks] | [Mood / Trauma / SUD] | [Yes / No / Partial] | [Helpful / Not helpful] |
| [PHP]        | [...]        | [...]    | [...]         | [...]      | [...]             |
| [Residential SUD] | [...]   | [...]    | [...]         | [...]      | [...]             |

─────────────────────────────────────────
PSYCHOTHERAPY HISTORY
─────────────────────────────────────────
| Modality | Approx. Dates | Duration | Perceived Benefit | Reason Ended |
|----------|---------------|----------|------------------|--------------|
| [CBT]    | [YYYY–YYYY]   | [X months] | [Helpful — thought records reduced anxiety] | [Completed / Moved / Cost] |
| [DBT]    | [...]         | [...]    | [...]            | [...]        |
| [Supportive] | [...]     | [...]    | [...]            | [...]        |

─────────────────────────────────────────
LONGEST PERIOD OF STABILITY
─────────────────────────────────────────
Duration: [X months / years]
Approximate dates: [YYYY–YYYY]
Attributed factors (client-reported): [Medication adherence / Sobriety / Stable housing /
Therapy / Work / Relationship / Other]
What ended the stable period: [...]
Clinical implication: [Identify replicable factors for current treatment planning]

─────────────────────────────────────────
FAMILY PSYCHIATRIC HISTORY
─────────────────────────────────────────
| Relative | Diagnosis (if known) | Medication Response Notes | Suicide History |
|----------|---------------------|--------------------------|----------------|
| [Mother] | [MDD]               | [Responded well to SSRIs] | [No]           |
| [Father] | [Alcohol Use Disorder] | [N/A]                 | [No]           |
| [Sibling] | [Bipolar I]        | [Lithium — good response] | [Attempt YYYY] |

Familial suicide history detail: [Relationship, year, method if known — clinical relevance for
risk assessment]

─────────────────────────────────────────
PAST PSYCHIATRIC HISTORY SUMMARY
─────────────────────────────────────────
[Three to five sentence synthesis: treatment trajectory, degree of treatment resistance,
medication response patterns, hospitalization burden, and the factors associated with the
client's longest stable period. Frame as relevant context for current treatment planning.]

─────────────────────────────────────────
BILLING NOTE
─────────────────────────────────────────
PPH documented as part of CPT [90791 | 90792].
Records reviewed: [List sources / Not yet available — requested from [provider/agency] on [date]].
```

## Verification

- [ ] Prior diagnoses table complete; client-reported vs. records-confirmed distinction maintained.
- [ ] Medication chronology table present with class, response, side effects, and discontinuation reason for each agent.
- [ ] Medication pattern analysis identifies: classes exhausted, prior positive responses, side-effect patterns, serious adverse reactions, pharmacogenomic testing if performed.
- [ ] Each hospitalization documented separately with voluntary/involuntary status.
- [ ] IOP/PHP/residential episodes documented.
- [ ] Psychotherapy history includes modality, duration, and perceived benefit.
- [ ] Longest stability period documented with client attribution.
- [ ] Family psychiatric history includes medication response and suicide history.
- [ ] PPH Summary is integrative synthesis, not a table restatement.
- [ ] Gaps flagged with `[clinician input required: ...]` and records request documented if applicable.
- [ ] No medication recommendations made within this history section.
