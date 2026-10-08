---
title: "Referral Quality Optimizer"
category: medicine
description: "Optimize referral packets by mapping referral data capture to specialist triage/decision needs, separating objective findings from referral recommendations, and identifying missing documentation before submission."
techniques:
  - ST-03
  - DT-05
  - RT-05
  - OC-04
  - QA-08
tags:
  - medicine
  - referrals
  - care-coordination
  - documentation-quality
updated: "2026-10-06"
related_prompts:
  - domain-healthcare-clinical/prompts/communication/medicine_handoff_communication.md
  - domain-healthcare-clinical/prompts/communication/medicine_care_coordination_transitions.md
  - domain-healthcare-clinical/prompts/workflow/medicine_clinical_documentation.md
---

# Referral Quality Optimizer

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

## False-Positive Prevention

❌ **DON'T:**
- Mark a Decision Map row `Y` because a test name appears in the chart when the result, its date, or the specialty's required timeframe (e.g., an echo "within 6 months" per the intake policy) is not actually there — that row is `Partial`.
- State the specialty's intake requirements or pre-referral tests from general knowledge; if the specialty policy was not supplied, write `[per receiving specialty intake policy]` instead of a list that looks authoritative.
- Fill the ICD-10 slot, an accession number, or a lab date with a plausible value — an invented code or date passes a skim and fails the specialist's triage.
- Raise the priority to urgent or stat in the Recommendation section with a rationale that relies on findings missing from the Factual Summary.
- Drop anticoagulation status, implant/device status, or an allergy from the Factual Summary because it seems unrelated to the referral question; procedural specialists triage on exactly these.

✅ **DO:**
- Before running the Quality Checks, count the Decision Map rows marked `Y` and confirm each cites a dated source in the input; re-mark any without one as `Partial` or `N`.
- Trace every sentence in Section C back to a fact in Section B; delete or move any fact that appears only in C.
- Emit the Insufficient Documentation branch whenever a decision-critical row is `N`, even if the rest of the packet is complete.
- Leave citation placeholders unfilled rather than completing them with a guessed guideline name or year.

---

## Quality Checks

- Each specialist decision need is explicitly mapped to supporting data.
- Factual summary excludes recommendation language.
- Recommendation section avoids introducing uncited new facts.
- Source placeholders are present for all critical claims.
- Insufficient Documentation branch is emitted for any critical missing intake item.
