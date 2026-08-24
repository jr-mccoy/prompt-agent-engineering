---
title: "DSM-5-TR Differential Diagnosis Generator"
category: psychology/diagnostic-formulation
description: "Generate a ranked ICD-10-CM / DSM-5-TR differential with confirm and refute criteria per candidate diagnosis"
techniques:
  - RT-02
  - DS-04
  - QA-04
  - ST-04
  - RT-05
difficulty: advanced
intended_use: model-testing
tags:
  - differential-diagnosis
  - DSM-5-TR
  - ICD-10-CM
  - diagnostic-reasoning
  - clinical-formulation
updated: "2026-06-08"
related_prompts:
  - domain-psychology/diagnostic-formulation/psychology_case_conceptualization_framework.md
  - domain-psychology/diagnostic-formulation/psychology_provisional_vs_rule_out_decision_aid.md
  - domain-psychology/diagnostic-formulation/psychology_comorbidity_mapping.md
  - domain-psychology/diagnostic-formulation/psychology_icd10_crosswalk_assistant.md
---

# DSM-5-TR Differential Diagnosis Generator

## Objective

Generate a structured, ranked differential diagnosis list from a clinical presentation using DSM-5-TR nosology and ICD-10-CM code families. For each candidate diagnosis, produce a confirm/refute reasoning column that maps available symptom data to specific DSM-5-TR criterion sets — without reproducing copyrighted criterion text verbatim. The output functions as a working clinical scaffold; all diagnostic conclusions require clinician review and confirmation.

## When to Use

- Initial or re-evaluation sessions where diagnostic clarity is needed before treatment planning
- Complex or ambiguous presentations with symptom overlap across multiple disorder categories
- Supervision or peer consultation preparation to organize clinical evidence systematically
- Transitional moments (e.g., treatment non-response) prompting diagnostic reconsideration
- Training and model-testing contexts requiring structured differential reasoning

Do not use as a standalone diagnostic instrument. Every candidate diagnosis listed is a hypothesis for clinician evaluation, not an AI-assigned diagnosis.

## Inputs / Context Required

Provide all available data. The richer the input, the more targeted the differential.

- **Chief complaint and symptom description:** duration, onset pattern (acute vs. gradual), course (episodic, chronic, progressive)
- **Symptom domains observed or reported:** mood, cognition, perception, behavior, somatic, sleep, appetite, social/occupational functioning
- **Functional impairment:** severity across work, relationships, self-care, safety
- **Timeline:** longitudinal symptom history, age of first onset, prior episodes
- **Rule-out medical and substance context:** known medical conditions, medications, recent labs if available, substance use history
- **Prior diagnoses:** confirmed, suspected, or documented in record
- **Relevant developmental, trauma, and psychosocial history:** [clinician input required]
- **Mental status findings:** from current or most recent MSE [clinician input required]
- **Setting and evaluation purpose:** outpatient, inpatient, forensic, medication management, therapy intake

## Constraints

### Must
- Rank candidates by clinical fit from highest to lowest based on symptom correspondence to DSM-5-TR criterion sets
- For each candidate, provide a **Confirm** column (evidence supporting inclusion) and a **Refute** column (evidence against or missing criteria)
- Reference DSM-5-TR criterion set labels (e.g., Criterion A, B, C, D) without reproducing full copyrighted criterion text; paraphrase the threshold being evaluated
- Pair each diagnosis with its primary ICD-10-CM code family (e.g., F32.x, F41.1, F20.x)
- Flag when a medical or substance etiology must be ruled out before a primary mental disorder code is appropriate (DSM-5-TR exclusion hierarchy)
- Include a **Specifiers Applicable** field for diagnoses where specifiers materially change ICD-10-CM coding (e.g., severity, episode type, psychotic features)
- End with a **Diagnostic Gaps** section listing information the clinician still needs to confirm or rule out candidates
- Frame all output as hypotheses requiring clinician confirmation; include a `[Clinician confirmation required]` tag at each candidate diagnosis

### Must Not
- Assign a final diagnosis — the output is a differential scaffold only
- Reproduce DSM-5-TR criterion text verbatim or in full (copyright)
- Include ICD-10-CM codes that do not correspond to the DSM-5-TR diagnosis named
- Apply organic / medical / substance-induced diagnoses without flagging the need for medical workup
- Omit the Refute column — confirming only without falsification pressure produces anchoring bias
- Assume symptom endorsement from unmarked fields; flag missing data explicitly

## Instructions

1. **Parse the clinical presentation** by organizing supplied information into symptom domains: mood/affect, thought/cognition, perception, behavior, somatic/neurovegetative, interpersonal/relational, temporal course, and functional impairment. Note any domain where data are absent or ambiguous.

2. **Identify the primary diagnostic zone** using DSM-5-TR chapter organization as the organizing heuristic:
   - Neurodevelopmental (F80–F89, F90–F98)
   - Schizophrenia spectrum and other psychotic disorders (F20–F29)
   - Bipolar and related disorders (F30–F31)
   - Depressive disorders (F32–F33, F34, F41.2)
   - Anxiety disorders (F40–F41)
   - Obsessive-compulsive and related (F42–F45)
   - Trauma- and stressor-related (F43)
   - Dissociative (F44)
   - Somatic symptom and related (F45)
   - Feeding and eating (F50)
   - Substance-related and addictive (F10–F19, F63)
   - Neurocognitive (F01–F09)
   - Personality disorders (F60–F69)
   - Other specified / unspecified categories
   Start in the zone most consistent with the presenting concern but cast the net across zones when overlap symptoms are present.

3. **Generate candidate diagnoses**, typically 3–6, ranked by fit. Include:
   - At minimum one "closest fit" diagnosis
   - At minimum one commonly confused differential (highest diagnostic neighbor)
   - At minimum one rule-out requiring explicit medical/substance exclusion
   - At minimum one "don't miss" diagnosis (high clinical consequence if missed — e.g., bipolar I when the presentation is primarily depressive)

4. **For each candidate, complete the confirm/refute table** (see Output Format). Map available clinical data to:
   - Criterion A (primary symptom threshold) — met, partially met, insufficient data
   - Duration criterion — met, not yet assessable, uncertain
   - Impairment/distress criterion — met, partially met, absent
   - Exclusion criteria — cleared, pending, not cleared
   Note the **strength of evidence** for each column entry: strong, moderate, weak, or absent.

5. **Identify applicable specifiers** for diagnoses that reach the confirm threshold. Note how specifiers affect ICD-10-CM code selection (e.g., single vs. recurrent episode, mild/moderate/severe, with anxious distress, with psychotic features, in partial/full remission).

6. **Run the DSM-5-TR exclusion hierarchy check**:
   - Has a medical etiology been ruled out (DSM-5-TR: "not attributable to physiological effects of substance or medical condition")?
   - Has substance/medication etiology been ruled out?
   - Are hierarchical exclusions between diagnoses respected (e.g., major depressive episode not occurring exclusively during schizophrenia)?
   Flag each pending exclusion clearly.

7. **Compile the Diagnostic Gaps section**: list specific information that, if obtained, would most change the differential. Prioritize: (a) information that would rule in or rule out the highest-ranked candidate, (b) safety-relevant diagnostic questions.

8. **Apply uncertainty calibration** throughout. Use explicit confidence language: "strong correspondence," "moderate correspondence," "insufficient data to assess," "symptom pattern argues against." Do not suppress low-confidence candidates — include them with explicit uncertainty flags.

## Output Format

### Differential Summary Header

```
PRESENTING CONCERN: [clinician input required]
EVALUATION DATE / CONTEXT: [clinician input required]
PRIMARY DIAGNOSTIC ZONE(S): [list DSM-5-TR chapter zones flagged]
EXCLUSIONS PENDING: [medical / substance rule-out items]
OUTPUT STATUS: Working hypothesis — clinician confirmation required
```

---

### Differential Diagnosis Table

| Rank | Candidate Diagnosis | ICD-10-CM Code Family | Confirm (evidence supporting) | Refute (evidence against / gaps) | Specifiers Applicable | Confidence |
|------|--------------------|-----------------------|-------------------------------|-----------------------------------|-----------------------|------------|
| 1 | [Diagnosis name — DSM-5-TR term] | [F__.x] | [Criterion A: symptom X, Y, Z meets threshold per clinician report; Duration: meets __ criterion; Impairment: documented in work and relationships] | [Criterion B: symptom Z not clearly endorsed; Exclusion pending: medical workup needed] | [e.g., Severe; with anxious distress; current episode] | Strong / Moderate / Weak |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 (Don't Miss) | | | | | | |

`[Clinician confirmation required]` at each row before diagnosis is applied.

---

### Exclusion Hierarchy Checklist

- [ ] Medical etiology ruled out (relevant workup ordered or documented): [specify]
- [ ] Substance / medication etiology ruled out: [specify substances / medications]
- [ ] Hierarchical DSM-5-TR exclusions between candidates addressed: [specify pairs]
- [ ] Bereavement / normal grief exclusion considered where applicable
- [ ] Culture-bound or culturally normative presentation considered

---

### Diagnostic Gaps (Information Needed)

| Priority | Gap Description | Would Most Affect |
|----------|-----------------|-------------------|
| High | [e.g., Longitudinal mood history to distinguish MDD from bipolar II] | Rank 1 vs. Rank 5 (Don't Miss) |
| High | [e.g., Labs: TSH, CBC to rule out thyroid or anemia as mood etiology] | Exclusion hierarchy |
| Medium | [e.g., Collateral from family regarding hypomanic episodes] | Rank 5 |
| Medium | [e.g., Full trauma history to assess PTSD Criterion A event] | Rank 3 |
| Low | [e.g., Clarify onset age for developmental history] | Rank 4 |

---

### Working Diagnostic Impression (Clinician to Complete)

```
Primary Diagnosis:  _________________________________ [ICD-10-CM: _____]
Secondary Diagnoses (if comorbid):
  1. _________________________________ [ICD-10-CM: _____]
  2. _________________________________ [ICD-10-CM: _____]
Rule Out:          _________________________________ [ICD-10-CM: _____]
Deferred:          _________________________________
Clinician Signature / Attestation: _________________________________ Date: _____
```

## Verification

Self-check before delivering output:

- [ ] Each candidate diagnosis uses DSM-5-TR terminology and is paired with a valid ICD-10-CM code family
- [ ] Every candidate has both a Confirm and a Refute column — no diagnosis is confirmed without falsification pressure
- [ ] Criterion-set references (Criterion A, B, C, duration, impairment) are present for each candidate without reproducing copyrighted text verbatim
- [ ] The DSM-5-TR exclusion hierarchy (medical, substance, hierarchical) is addressed at least as a checklist
- [ ] A "Don't Miss" high-consequence differential is included
- [ ] Specifiers are noted for all diagnoses where they change ICD-10-CM coding
- [ ] Confidence language is calibrated — no diagnosis is stated with certainty
- [ ] All diagnostic conclusions are tagged `[Clinician confirmation required]`
- [ ] Diagnostic Gaps section is populated with prioritized, actionable items
- [ ] No diagnostic label appears without corresponding ICD-10-CM code family reference
