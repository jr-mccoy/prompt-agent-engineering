---
title: "Referral Quality Optimizer"
category: medicine
description: "Optimize referral packets by mapping referral data capture to specialist triage/decision needs, separating objective findings from referral recommendations, and identifying missing documentation before submission."
tags:
  - medicine
  - referrals
  - care-coordination
  - documentation-quality
updated: "2026-05-05"
related_prompts:
  - domain-healthcare-clinical/prompts/medicine_handoff_communication.md
  - domain-healthcare-clinical/prompts/medicine_care_coordination_transitions.md
  - domain-healthcare-clinical/prompts/medicine_clinical_documentation.md
---

# Referral Quality Optimizer

**Objective:** Produce high-signal referral packages that align with specialist acceptance/triage needs, improve first-pass scheduling readiness, and clearly separate factual chart summary from referral recommendation language.

**Important Disclaimer:** This prompt structures referral documentation but does not replace clinical judgment, specialty-specific intake policies, or emergency escalation pathways.

---

## Input Required

### 1) Referral Context
- Referring service/clinician
- Target specialty and subspecialty
- Referral priority (routine/urgent/stat)
- Primary referral question(s)
- Patient availability/logistics constraints

### 2) Objective Clinical Data
- Working diagnosis/problem list with ICD-10
- Onset/course timeline and key interventions
- Pertinent positives/negatives from history and exam
- Relevant labs/imaging/pathology/procedures with dates
- Current medication list, allergies, anticoagulation/implant status
- Red flag symptoms/signs and stability status

### 3) Decision-Critical Specialist Needs
- What the specialist must decide (diagnosis confirmation, procedure candidacy, treatment selection)
- Required pre-referral tests/forms per specialty policy
- Required exclusion data (e.g., ruled-out emergencies, contraindications)

### 4) Recommendation Context
- Why this specialty is needed now
- Interim management completed
- Requested consult scope (evaluate-and-treat, second opinion, procedure evaluation)

---

## Processing Instructions

1. Build a **specialist decision map** from the referral question and specialty intake criteria.
2. Link each decision need to specific available evidence and dates.
3. Separate output into:
   - **Factual Summary (objective data only)**
   - **Referral Recommendation Language (assessment/request framing)**
4. Flag missing required items that reduce triage quality or delay scheduling.
5. If critical intake elements are missing, generate the **Insufficient Documentation branch output**.
6. Add source/evidence placeholders for clinician completion.

---

## Output Format

```markdown
# REFERRAL QUALITY OPTIMIZATION OUTPUT

## A) Specialist Decision Map
| Specialist Decision Need | Minimum Data Needed | Present? (Y/N/Partial) | Source Placeholder | Gap/Action |
|---|---|---|---|---|
| [Decision 1: e.g., procedure candidacy] | [Required findings/tests] | [Y/N/Partial] | [Note date; report ID; lab date] | [Obtain test/document] |
| [Decision 2...] | [...] | [...] | [...] | [...] |

## B) Factual Summary (Objective Only)
- Referral reason: [single-sentence clinical question]
- Problem summary: [diagnosis + timeline + severity]
- Key objective findings:
  - [Exam finding + date]
  - [Lab/imaging/pathology result + date]
  - [Prior intervention + response]
- Current risk/safety status: [stable vs unstable; red flags present/absent]
- Current treatment context: [active meds, relevant contraindications, allergies]

### Evidence Citations To Complete
- [Primary care/ED/inpatient note + date]
- [Imaging/lab/pathology source + accession/date]
- [Specialty guideline/intake requirement source]

## C) Referral Recommendation Language (Assessment + Ask)
- Why specialist input is needed now: [clinical justification]
- What decision is being requested: [specific consult question]
- Urgency rationale: [routine/urgent/stat with rationale]
- Interim actions completed: [tests done, therapies tried, response]
- Requested next step: [consult only vs procedure evaluation vs co-management]

### Evidence Citations To Complete
- [Guideline/policy citation placeholder]
- [Chart evidence citation placeholder]
- [Referral protocol citation placeholder]

## D) Insufficient Documentation Branch (if critical intake data missing)
**Status:** INSUFFICIENT DOCUMENTATION FOR REFERRAL SUBMISSION

**Missing Critical Referral Elements:**
1. [Missing item tied to specialist decision need]
2. [Missing item tied to urgency/triage determination]

**Operational Impact:**
- Likely triage delay/decline because [specific missing requirement].

**Required Next Steps Before Referral Submission:**
- [Order/collect required test or report]
- [Document required history/exam component]
- [Clarify consult question and urgency with explicit rationale]

**Provisional Language (Do Not Submit Until Complete):**
"Referral packet is currently incomplete for specialist triage requirements. Additional objective documentation is being finalized to support timely and appropriate specialty review."
```

---

## Quality Checks

- Each specialist decision need is explicitly mapped to supporting data.
- Factual summary excludes recommendation language.
- Recommendation section avoids introducing uncited new facts.
- Source placeholders are present for all critical claims.
- Insufficient Documentation branch is emitted for any critical missing intake item.
