---
title: "Discharge Summary Template"
category: healthcare-clinical/templates
description: "Standardized fill-in template for inpatient discharge documentation to support safe transitions of care: problem-oriented hospital course, discharge medications, pending tests, return precautions and owned follow-up."
techniques:
  - NE-03
  - ST-42
  - OC-03
  - DS-40
  - QA-01
difficulty: intermediate
tags:
  - discharge-summary
  - care-transitions
  - clinical-documentation
  - medication-reconciliation
updated: "2026-10-06"
---

# Discharge Summary Template

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

> Standardized template for inpatient discharge documentation to support safe transitions of care.

---

```markdown
# Discharge Summary: [Patient Name / MRN]

## Mandatory Data Fields
- **Patient Name:** [Required]
- **MRN:** [Required]
- **DOB:** [Required]
- **Admission Date:** [Required]
- **Discharge Date:** [Required]
- **Discharge Disposition:** [Home/SNF/Rehab/Hospice/Other]
- **Discharging Clinician:** [Name, Role, Contact]
- **Primary Care Clinician:** [Name, Contact]
- **Follow-up Clinician(s):** [Name, Specialty, Contact]

---

## Hospital Course (Problem-Oriented)
1. **Primary Admission Diagnosis:** [Required]
2. **Secondary Diagnoses:** [Required]
3. **Major Interventions/Procedures:** [Include date, indication, findings]
4. **Clinical Course by Problem:**
   - **[Problem 1]:** [Assessment, treatment, response]
   - **[Problem 2]:** [Assessment, treatment, response]
5. **Complications/Adverse Events:** [None or describe]

---

## Discharge Condition and Exam
- **Condition at Discharge:** [Stable/Improved/Guarded]
- **Focused Discharge Exam:** [Required]
- **Latest Key Vitals/Labs:** [Required values and trends]

---

## Medications at Discharge
| Medication | Dose | Route | Frequency | Indication | New/Changed/Stopped | Patient Instructions |
|------------|------|-------|-----------|------------|---------------------|----------------------|
| [Required] |      |       |           |            |                     |                      |

- **Medication Reconciliation Completed:** [Yes/No]
- **High-Risk Med Changes Explained to Patient/Caregiver:** [Yes/No]

---

## Red-Flag / Safety Section
- **Return Precautions (Symptoms requiring urgent evaluation):**
  - [Required symptom/action pair 1]
  - [Required symptom/action pair 2]
- **Pending Tests at Discharge:** [Test, expected date, responsible clinician]
- **Critical Incidental Findings Requiring Follow-up:** [Required if present]
- **Allergies and Serious Reactions:** [Required]
- **Code Status at Discharge:** [Required]

---

## Follow-up Accountability
| Follow-up Task | Owner (Name/Role) | Due Date | Escalation Path if Missed |
|----------------|-------------------|----------|----------------------------|
| [Appointment scheduling] | [Required] | [Required] | [Required] |
| [Pending lab/result review] | [Required] | [Required] | [Required] |
| [Medication monitoring] | [Required] | [Required] | [Required] |

- **Warm handoff completed to next clinician/team:** [Yes/No, date/time]
- **Patient/caregiver contact method confirmed:** [Phone/Portal/Other]

---

## Communication Clarity Checks
- [ ] Diagnoses are written in plain language + clinical terms.
- [ ] Medication changes explicitly state *what changed* and *why*.
- [ ] Follow-up dates include exact dates/times and location/contact.
- [ ] Return precautions use action-oriented language (e.g., “call 911,” “go to ED now”).
- [ ] Pending items identify a specific accountable clinician.
- [ ] Teach-back documented: patient/caregiver repeated key plan elements.

**Teach-Back Notes:** [Required]

---

## Patient Instructions Summary
- **Diet:** [Required]
- **Activity:** [Required]
- **Wound/Device care:** [If applicable]
- **When to seek care:** [Required]
- **Interpreter used:** [Yes/No, language]

**Discharge Summary Signed:** [Date/Time]
```

---

## False-Positive Prevention

When filling this template:

❌ **DON'T:**
- Build Clinical Course by Problem from the admission H&P or a copied-forward progress note, so the course reads as day 2 rather than the day of discharge.
- Fill Focused Discharge Exam with a normal template exam that was not performed on the discharge day, or Latest Key Vitals/Labs with undated values or the word "stable".
- Write "None" in Pending Tests at Discharge by default; leave it unanswered until the outstanding orders have been checked.
- Answer Medication Reconciliation Completed "Yes" while home medications that were discontinued have no "Stopped" row in the medications table.

✅ **DO:**
- Reconcile the dates: every procedure and lab date falls between Admission Date and Discharge Date, the length of stay recomputes from them, and every follow-up date is after discharge.
- Account for each home medication in the Medications at Discharge table as continued, changed or stopped, with the reason in the Indication or Patient Instructions column.
- Take Allergies and Serious Reactions from the current allergy record with reaction types, and check every drug started during the stay against it.
