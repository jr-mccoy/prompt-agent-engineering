---
title: "Prior Authorization Packet Builder"
category: medicine
description: "Build a payer-ready prior authorization packet by mapping captured clinical data to each payer decision criterion, separating objective facts from recommendation language, and surfacing documentation gaps."
tags:
  - medicine
  - prior-authorization
  - utilization-management
  - clinical-documentation
updated: "2026-05-05"
related_prompts:
  - domain-healthcare-clinical/prompts/medicine_prior_authorization_letter.md
  - domain-healthcare-clinical/prompts/medicine_clinical_documentation.md
  - domain-healthcare-clinical/prompts/medicine_em_coding_level_justification.md
---

# Prior Authorization Packet Builder

**Objective:** Assemble a complete prior-authorization packet that directly answers payer approval criteria and clearly distinguishes objective clinical facts from clinician recommendation statements.

**Important Disclaimer:** This prompt supports documentation quality and packet structure. It does not replace clinician judgment, payer policy review, legal review, or plan-specific authorization rules.

---

## Input Required

### 1) Request Metadata
- Payer and plan name
- Request type (initial, continuation, expedited)
- Service/therapy requested (include CPT/HCPCS/J-code/NDC when available)
- Diagnosis and ICD-10 codes
- Turnaround deadline / urgent status reason

### 2) Patient Clinical Facts (Objective)
- Relevant diagnoses, severity markers, staging/classification
- Symptom burden and functional impact
- Pertinent exam, labs, imaging, pathology, and dates
- Comorbidities and contraindications
- Prior treatments with dose/duration/outcome
- Adverse effects and discontinuation reasons

### 3) Policy + Evidence Inputs
- Payer medical policy criteria text
- Step therapy or prerequisite requirements
- Guideline/evidence references to support appropriateness
- Any denial history tied to same request

### 4) Recommendation Inputs (Assessment/Plan)
- Why the requested service is appropriate now
- Why alternatives are less appropriate for this patient
- Monitoring plan and reassessment timeline

---

## Processing Instructions

1. **Extract payer decision nodes** from policy language into a checklist of explicit approval criteria.
2. **Map each criterion to supporting chart evidence** with source location placeholders.
3. **Separate outputs into two sections:**
   - **Factual Summary (objective, chart-derived only)**
   - **Recommendation Language (clinical assessment and request framing)**
4. **Flag missing elements** required by payer criteria.
5. If required evidence is missing, generate the **Insufficient Documentation branch output**.
6. Include citation placeholders for clinician/staff completion before submission.

---

## Output Format

```markdown
# PRIOR AUTH PACKET BUILD

## A) Payer Decision Map
| Payer Criterion | Needed Data Element | Evidence Found? (Y/N/Partial) | Source Placeholder | Gap/Action |
|---|---|---|---|---|
| [Criterion 1 exact text] | [Required field] | [Y/N/Partial] | [EHR note date/author; lab ID; imaging report ID] | [If gap, what to obtain] |
| [Criterion 2...] | [...] | [...] | [...] | [...] |

## B) Factual Summary (Objective Only)
- Patient: [age/sex/relevant demographics]
- Diagnoses: [condition + ICD-10 + severity/stage]
- Clinical course: [timeline with key dates]
- Objective findings:
  - [Exam/lab/imaging/pathology result + date]
  - [Prior treatment trial: drug/procedure, dose, duration, outcome]
  - [Adverse events/contraindications with specifics]
- Functional impact: [validated measure/work/ADL impact]

### Evidence Citations To Complete
- [Source 1: guideline/policy/document + section/page]
- [Source 2: chart note/lab/imaging + date/accession]
- [Source 3: denial letter/payer communication + date]

## C) Recommendation Language (Assessment + Request Framing)
- Medical necessity statement: [why requested service is indicated now]
- Patient-specific rationale: [why this patient meets criteria]
- Alternative therapy rationale: [why preferred alternatives are not appropriate]
- Safety/monitoring plan: [follow-up interval, metrics, stop/change thresholds]
- Requested authorization details: [units, duration, site of care, urgency]

### Evidence Citations To Complete
- [Guideline citation placeholder]
- [Trial/compendia citation placeholder]
- [Payer policy citation placeholder]

## D) Insufficient Documentation Branch (if any critical criterion is unmet)
**Status:** INSUFFICIENT DOCUMENTATION FOR SUBMISSION

**Missing Critical Items:**
1. [Missing element tied to criterion]
2. [Missing element tied to criterion]

**Why This Blocks Approval:**
- [Criterion text] requires [specific data], currently unavailable.

**Required Next Steps Before Submission:**
- [Obtain record/test/result]
- [Complete trial/failure documentation details]
- [Add contraindication evidence with source]

**Provisional Language (Do Not Submit Until Complete):**
"Current documentation does not yet satisfy all payer criteria. Additional records are being gathered to support medical necessity and criterion-level compliance."
```

---

## Quality Checks Before Finalizing Packet

- Every payer criterion has a row in the decision map.
- Every "Yes"/"Partial" determination has a specific source placeholder.
- Objective facts and recommendation language remain separate.
- Failed/contraindicated alternatives are specific (dose, duration, outcome).
- Insufficient Documentation branch is present whenever a critical gap exists.
