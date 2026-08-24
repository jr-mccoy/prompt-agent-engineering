---
title: "ICD-10-CM to DSM-5-TR Crosswalk Assistant"
category: psychology/diagnostic-formulation
description: "Produce accurate DSM-5-TR to ICD-10-CM code crosswalk tables for billing and clinical documentation"
techniques:
  - ST-04
  - QA-04
  - CM-01
  - DT-02
difficulty: beginner
intended_use: model-testing
tags:
  - ICD-10-CM
  - DSM-5-TR
  - billing-codes
  - crosswalk
  - diagnostic-coding
  - documentation
updated: "2026-06-08"
related_prompts:
  - domain-psychology/diagnostic-formulation/psychology_dsm5_differential_generator.md
  - domain-psychology/diagnostic-formulation/psychology_case_conceptualization_framework.md
  - domain-psychology/diagnostic-formulation/psychology_provisional_vs_rule_out_decision_aid.md
  - domain-psychology/documentation/psychology_initial_treatment_plan.md
---

# ICD-10-CM to DSM-5-TR Crosswalk Assistant

## Objective

Produce a structured crosswalk table that maps DSM-5-TR diagnostic labels to their corresponding ICD-10-CM codes, specifiers, and code-selection decision rules. Output supports accurate billing documentation, treatment plan coding, and clinical record alignment. The crosswalk covers code families, specifier-driven sub-codes, and common coding pitfalls for each diagnostic category requested. All final code selection requires clinician confirmation and payer-specific verification.

## When to Use

- Preparing or auditing treatment plan diagnostic sections for correct ICD-10-CM code entry
- Translating a differential or working diagnosis list into billable codes before claim submission
- Training clinicians or billing staff on specifier-to-code mapping logic
- Identifying which specifiers must be documented to support a specific code (e.g., severity, episode type)
- Resolving discrepancies between DSM-5-TR clinical terminology and ICD-10-CM billing requirements
- Model-testing contexts requiring accurate code-family knowledge

Do not substitute this output for a real-time ICD-10-CM code lookup against the current CMS General Equivalence Mapping (GEM) tables. Codes are updated annually; verify against the current fiscal year's ICD-10-CM tabular list before billing.

## Inputs / Context Required

- **DSM-5-TR diagnosis name(s):** Provide the exact DSM-5-TR diagnostic term (e.g., "Major Depressive Disorder, recurrent episode, severe, without psychotic features")
- **Applicable specifiers already documented:** Episode type, severity, with/without psychotic features, remission status, course specifiers, or any other specifiers noted in the clinical record
- **Setting:** Outpatient, inpatient, partial hospital — some codes and modifiers differ by setting
- **Payer context (if known):** Medicare, Medicaid, commercial — payer-specific guidance may override standard crosswalk
- **Purpose:** Billing only, treatment plan documentation, audit review, or training

If specifiers are not yet determined, the prompt will output the full specifier decision tree so the clinician can select the appropriate sub-code.

## Constraints

### Must
- Map each DSM-5-TR diagnosis to its correct ICD-10-CM code family using the DSM-5-TR coding note appendix structure
- Provide the full specifier decision tree when multiple sub-codes exist under a single diagnosis (e.g., F32.0 vs. F32.1 vs. F32.2 vs. F32.3 vs. F32.4 vs. F32.5 vs. F32.89 vs. F32.9)
- Flag diagnoses that require documentation of specific specifiers before the code can be applied (e.g., psychotic features must be documented to use F32.3/F33.3)
- Include a **Common Coding Pitfalls** row for each diagnosis category covering frequent errors (e.g., using F41.1 when GAD criteria are not fully met, or failing to specify episode type for MDD)
- Note when a DSM-5-TR specifier does not change the ICD-10-CM code (documentation-only specifiers)
- Flag diagnoses without a unique ICD-10-CM code that must use an "Other specified" (e.g., F41.8) or "Unspecified" code (e.g., F41.9)
- Include the NOS/unspecified code option for each category as a fallback row
- Tag each code as `[Clinician confirmation required]` — final code selection is a clinical and billing responsibility

### Must Not
- Present a single code as definitively correct without specifier context
- Omit the annual update caveat — ICD-10-CM codes change each October 1; codes here reflect structure, not a real-time verified lookup
- Conflate ICD-10-CM codes with CPT procedure codes — these serve different functions
- Assign codes to diagnoses that are rule-out or provisional without flagging appropriate coding conventions for unconfirmed diagnoses
- Omit the distinction between "Other Specified" and "Unspecified" categories

## Instructions

1. **Identify each DSM-5-TR diagnosis** provided in the input. If more than five diagnoses are listed, batch output by diagnostic category chapter (e.g., depressive disorders, anxiety disorders) for readability.

2. **For each diagnosis, retrieve the ICD-10-CM code family** anchored to the DSM-5-TR coding note. Organize by the following code family chapters most common in outpatient mental health:

   | DSM-5-TR Chapter | ICD-10-CM Block |
   |-----------------|-----------------|
   | Neurodevelopmental Disorders | F70–F79 (intellectual), F80–F89 (developmental), F90–F98 (childhood-onset behavioral) |
   | Schizophrenia Spectrum / Psychotic | F20–F29 |
   | Bipolar and Related | F30–F31 |
   | Depressive Disorders | F32–F33, F34, F41.2 (persistent depressive), F32.A (PMDD) |
   | Anxiety Disorders | F40–F41 |
   | OCD and Related | F42, F45.22, F45.21, L98.1 |
   | Trauma- and Stressor-Related | F43.0 (acute stress), F43.1x (PTSD), F43.2x (adjustment), F94.x |
   | Dissociative Disorders | F44 |
   | Somatic Symptom and Related | F45, F68.10 |
   | Feeding and Eating Disorders | F50.x |
   | Elimination | F98.0, F98.1 |
   | Sleep–Wake Disorders | F51.x, G47.x |
   | Disruptive, Impulse-Control, Conduct | F63.x, F91.x |
   | Substance-Related and Addictive | F10–F19 (substance-specific), F63.0 (gambling) |
   | Neurocognitive Disorders | F01–F09, G30.x |
   | Personality Disorders | F60.x, F61, F68.x |
   | Paraphilic Disorders | F65.x |

3. **Build the specifier decision tree** for each diagnosis. For diagnoses with multiple sub-codes:
   - Present the branching logic as a decision table (specifier present → code)
   - Identify which specifiers are **code-determining** (change the ICD-10-CM number) vs. **documentation-only** (recorded in the chart but do not change the code)
   - Highlight mandatory specifiers: when a specifier must be present to use a specific code

4. **Identify unspecified and other-specified code options** for each category. Clarify when "Other Specified" requires a clinician-entered reason in the medical record.

5. **Add common coding pitfalls** for each diagnostic category. Common categories of error:
   - Using an episode code (F32.x) when a recurrent episode code (F33.x) is indicated
   - Applying a full-syndrome code when only partial criteria are met (should use Other Specified)
   - Omitting severity specifier, resulting in default to unspecified code when severity documentation exists
   - Using personality disorder "unspecified" (F60.9) when a named PD is documented
   - Coding substance use disorder severity incorrectly (mild F1x.10 vs. moderate F1x.20 vs. severe F1x.20 with different 5th digits)

6. **Address provisional and rule-out coding**. ICD-10-CM outpatient guidelines instruct:
   - Outpatient: code the highest degree of certainty — code signs/symptoms, not unconfirmed diagnoses
   - Inpatient: may code probable/suspected diagnoses as if confirmed for the principal diagnosis
   - Present the appropriate coding convention for each setting and flag when clinical documentation must support the code chosen

7. **Output the crosswalk table** for each diagnosis requested, followed by a coding pitfalls summary and a verification checklist.

## Output Format

### Crosswalk Table Header

```
DIAGNOSES REQUESTED: [list from clinician input]
SPECIFIERS AVAILABLE: [list from clinician input]
SETTING: [outpatient / inpatient / PHP]
OUTPUT STATUS: Reference crosswalk — verify against current CMS ICD-10-CM tabular list
ANNUAL UPDATE CAVEAT: Codes current as of ICD-10-CM FY2026; verify for current fiscal year
```

---

### Crosswalk Table (one block per diagnosis)

**Diagnosis: [DSM-5-TR Name]**

| Specifier Combination | ICD-10-CM Code | Code Type | Documentation Required |
|-----------------------|---------------|-----------|------------------------|
| [e.g., Single episode, mild] | [e.g., F32.0] | Specific | Document "mild" severity with functional descriptor |
| [e.g., Single episode, moderate] | [e.g., F32.1] | Specific | Document "moderate" severity |
| [e.g., Single episode, severe without psychotic features] | [e.g., F32.2] | Specific | Document "severe" with no psychotic features noted |
| [e.g., Single episode, severe with psychotic features] | [e.g., F32.3] | Specific | Document psychotic features explicitly in MSE or narrative |
| [e.g., Single episode, in partial remission] | [e.g., F32.4] | Specific | Document partial remission criteria met |
| [e.g., Single episode, in full remission] | [e.g., F32.5] | Specific | Document full remission criteria met |
| [e.g., Other specified] | [e.g., F32.89] | Other Specified | Document specifying reason in medical record |
| [e.g., Unspecified episode, unspecified severity] | [e.g., F32.9] | Unspecified | Use only when severity/episode genuinely unknown |

`[Clinician confirmation required before applying any code]`

**Documentation-Only Specifiers (do not change code):**
- [e.g., With anxious distress — document but F32.x code unchanged]
- [e.g., With mixed features — document but does not change depressive disorder code; assess for bipolar]

**Common Coding Pitfalls:**
- [Pitfall 1: Using F32.x for a recurrent episode — use F33.x when two or more episodes are documented]
- [Pitfall 2: Defaulting to F32.9 when severity is clearly documented in the chart]
- [Pitfall 3: Failing to document psychotic features explicitly, losing ability to use F32.3]

---

### Outpatient vs. Inpatient Coding Convention Note

| Setting | Convention for Uncertain/Rule-Out Diagnoses |
|---------|---------------------------------------------|
| Outpatient | Code signs/symptoms or the highest-certainty confirmed diagnosis; do not code rule-out as if confirmed |
| Inpatient | May code probable/suspected as principal diagnosis if it represents the condition chiefly responsible for admission |
| PHP/IOP | Follow outpatient convention unless operating under inpatient coding rules per facility |

---

### Provisional Diagnosis Coding Note

When a DSM-5-TR diagnosis is assigned with a "Provisional" specifier:
- The ICD-10-CM code used is the same as the confirmed diagnosis
- The provisional status must be noted in the clinical record
- Provisional coding is appropriate when criteria appear likely to be met but information is still being gathered
- Document timeline for when provisional status will be re-evaluated `[clinician input required]`

---

### Verification Checklist

- [ ] Each DSM-5-TR diagnosis name matches ICD-10-CM code family per DSM-5-TR coding notes
- [ ] Specifier-driven sub-codes are populated where specifiers are documented
- [ ] Documentation requirements for each code are listed (what must appear in the chart)
- [ ] Unspecified codes used only when genuinely unspecified — not as default when specificity exists
- [ ] Common coding pitfalls reviewed for each category
- [ ] Outpatient vs. inpatient convention noted for any uncertain or rule-out diagnoses
- [ ] Annual update caveat present — clinician will verify against current CMS ICD-10-CM tabular list
- [ ] No CPT procedure codes conflated with ICD-10-CM diagnosis codes
- [ ] All final code selections tagged `[Clinician confirmation required]`
