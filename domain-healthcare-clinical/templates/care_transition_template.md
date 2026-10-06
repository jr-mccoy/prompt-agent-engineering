---
title: "Care Transition Template"
category: healthcare-clinical/templates
description: "Copy-ready template for structured care transition plans covering hospital discharge, facility transfers, and post-acute transitions — medication reconciliation, discharge services, follow-up, pending results, teach-back and readmission risk."
techniques:
  - NE-03
  - ST-05
  - OC-03
  - DS-40
  - QA-01
difficulty: intermediate
tags:
  - care-transitions
  - discharge-planning
  - medication-reconciliation
  - readmission-prevention
  - patient-family-education
updated: "2026-10-06"
---

# Care Transition Template

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

> Copy this template for creating structured care transition plans.
> Covers hospital discharge, facility transfers, and post-acute transitions.

---

```markdown
# Care Transition Plan: [Patient Identifier]

**Transition Type:**
- [ ] Hospital → Home
- [ ] Hospital → Skilled Nursing Facility (SNF)
- [ ] Hospital → Acute Rehabilitation
- [ ] Hospital → Long-Term Acute Care (LTAC)
- [ ] Hospital → Hospice
- [ ] SNF → Home
- [ ] ED → Home (discharge)
- [ ] ICU → Floor (intra-hospital)

**Prepared By:** [Name, Role]
**Date:** [Date]
**Expected Transition Date:** [Date]

---

## Patient Information

- **Name:** [Patient Name]
- **MRN:** [Medical Record Number]
- **DOB:** [Date of Birth]
- **Admission Date:** [Date]
- **Primary Diagnosis:** [Diagnosis]
- **Code Status:** [Full code / DNR / DNI / Comfort measures]
- **Allergies:** [List all — drug, food, latex]
- **Insurance:** [Type]

---

## Clinical Summary

**Admission Reason:** [Why admitted]

**Hospital Course Summary:**
[Key events, procedures, complications — 3-5 sentences]

**Discharge Diagnoses:**
1. [Diagnosis]
2. [Diagnosis]
3. [Diagnosis]

**Procedures Performed:**
- [Procedure 1]: [Date]
- [Procedure 2]: [Date]

**Functional Status at Discharge:**
- Mobility: [ ] Independent [ ] With assistive device [ ] With assistance [ ] Non-ambulatory
- ADLs: [ ] Independent [ ] Needs some assistance [ ] Dependent
- Cognitive: [ ] Baseline [ ] Impaired — specify: ___
- Baseline comparison: [ ] At baseline [ ] Below baseline — expected recovery: ___

---

## Medication Reconciliation

### Pre-Admission Medications
| Medication | Dose | Frequency | Continue at Discharge? |
|-----------|------|-----------|----------------------|
| [Drug] | [Dose] | [Freq] | [ ] Yes [ ] No — reason: ___ |

### New Medications Started During Admission
| Medication | Dose | Frequency | Duration | Reason Started |
|-----------|------|-----------|----------|----------------|
| [Drug] | [Dose] | [Freq] | [Duration or ongoing] | [Indication] |

### Medications Changed During Admission
| Medication | Old Dose | New Dose | Reason for Change |
|-----------|----------|----------|-------------------|
| [Drug] | [Old] | [New] | [Why] |

### Medications Stopped During Admission
| Medication | Reason Stopped | Restart? |
|-----------|----------------|----------|
| [Drug] | [Reason] | [ ] No [ ] Yes — when: ___ |

### Discharge Medication List (Complete)
| Medication | Dose | Frequency | Route | Special Instructions |
|-----------|------|-----------|-------|---------------------|
| [Drug 1] | [Dose] | [Freq] | [PO/SQ/etc.] | [With food, at bedtime, etc.] |

### High-Risk Medication Alerts
- [ ] Anticoagulant: [Drug, dose, monitoring plan (INR schedule, etc.)]
- [ ] Insulin: [Regimen, glucose monitoring schedule, hypoglycemia plan]
- [ ] Opioid: [Dose, expected duration, taper plan, naloxone prescribed]
- [ ] Other: [Drug, specific monitoring or precaution]

### Medication Reconciliation Verification
- [ ] Pre-admission list compared to discharge list
- [ ] All changes intentional and documented
- [ ] No inadvertent omissions
- [ ] No therapeutic duplications
- [ ] Patient/caregiver understands all changes
- [ ] Prescriptions sent to pharmacy
- [ ] Patient can afford medications / assistance arranged

---

## Discharge Services

### Home Health (if applicable)
| Service | Frequency | Purpose |
|---------|-----------|---------|
| Skilled nursing | [X visits/week] | [Wound care, IV meds, assessment] |
| Physical therapy | [X visits/week] | [Mobility, strengthening, balance] |
| Occupational therapy | [X visits/week] | [ADL training, home safety] |
| Speech therapy | [X visits/week] | [Swallowing, cognition, communication] |
| Home health aide | [X visits/week] | [Personal care, bathing] |
| Social work | [As needed] | [Resources, support] |

**Agency:** [Name] | **Start Date:** [Date] | **Authorization #:** [If applicable]

### Durable Medical Equipment
| Equipment | Ordered | Delivery Date | Verified |
|-----------|---------|---------------|----------|
| [Hospital bed] | [ ] Y | [Date] | [ ] |
| [Oxygen: ___ L/min via ___] | [ ] Y | [Date] | [ ] |
| [Walker/wheelchair] | [ ] Y | [Date] | [ ] |
| [Commode/shower chair] | [ ] Y | [Date] | [ ] |
| [Wound care supplies] | [ ] Y | [Date] | [ ] |
| [Glucose monitor/supplies] | [ ] Y | [Date] | [ ] |
| [Other: ___] | [ ] Y | [Date] | [ ] |

### Other Services
- [ ] Cardiac rehabilitation — Referral sent: [Date]
- [ ] Pulmonary rehabilitation — Referral sent: [Date]
- [ ] Diabetes self-management education — Referral sent: [Date]
- [ ] Meals on Wheels / nutrition services
- [ ] Medical transportation for follow-up
- [ ] Pharmacy delivery service
- [ ] Telehealth monitoring enrollment
- [ ] Other: ___

---

## Follow-Up Appointments

| Provider | Specialty | Purpose | Timeframe | Scheduled? | Date/Time |
|----------|-----------|---------|-----------|-----------|-----------|
| [PCP name] | Primary care | Post-discharge check | Within 7 days | [ ] Y [ ] N | [Date] |
| [Specialist] | [Specialty] | [Reason] | [Timeframe] | [ ] Y [ ] N | [Date] |
| [Surgeon] | Surgery | Wound/surgical check | [Timeframe] | [ ] Y [ ] N | [Date] |
| Lab work | — | [Specific tests] | [When] | Order given | [Date] |

### Critical Follow-Up (Must Not Be Missed)
- [ ] [Item 1]: [Why critical] — by [date]
- [ ] [Item 2]: [Why critical] — by [date]

### Pending Results
| Test | Expected Date | Responsible Provider | Action if Abnormal |
|------|--------------|---------------------|-------------------|
| [Test] | [Date] | [Who will follow up] | [Plan] |

---

## Patient/Family Education

### Education Completed (Teach-Back Confirmed)
- [ ] Diagnosis explained in plain language
- [ ] All medication changes reviewed — patient can state what changed and why
- [ ] New medication instructions — patient can demonstrate proper use
- [ ] Activity restrictions and timeline for resuming activities
- [ ] Diet modifications (if any)
- [ ] Wound care instructions (if applicable) — return demonstration done
- [ ] Equipment use (oxygen, glucose monitor, etc.) — return demonstration done
- [ ] Follow-up appointment dates and locations
- [ ] Who to call with questions: [Name, Phone]

### Warning Signs Reviewed
**Call the office if:**
- [Symptom 1]
- [Symptom 2]
- [Symptom 3]

**Go to the Emergency Department if:**
- [Emergency symptom 1]
- [Emergency symptom 2]
- [Emergency symptom 3]

### Materials Provided
- [ ] Written discharge instructions (in patient's language: ___)
- [ ] Updated medication list
- [ ] Follow-up appointment card
- [ ] Condition-specific education materials
- [ ] Emergency contact numbers
- [ ] After-visit summary

### Caregiver Training (if applicable)
- Caregiver: [Name, relationship]
- [ ] Present for education
- [ ] Can demonstrate: [Specific skills taught]
- [ ] Understands warning signs
- [ ] Has caregiver support resources

---

## Communication to Receiving Providers

### Discharge Summary
- [ ] Completed
- [ ] Sent to PCP: [Name] via [Method: fax/EHR/portal/mail]
- [ ] Sent to specialists: [Names] via [Method]
- [ ] Sent to receiving facility: [If transfer]

### Verbal Handoff (if applicable)
- [ ] PCP notified of discharge: [Date, time, who spoke with]
- [ ] Receiving facility nurse-to-nurse handoff: [Completed]
- [ ] Key pending issues communicated verbally (not just written)

### Transfer Documentation (if to facility)
- [ ] Transfer orders with complete medication list
- [ ] Relevant imaging and lab results
- [ ] Therapy recommendations and goals
- [ ] Wound care protocol
- [ ] Diet orders
- [ ] Code status documented
- [ ] Insurance authorization

---

## Post-Discharge Follow-Up Plan

### 48-72 Hour Post-Discharge Call
**Call scheduled:** [Date] by [Who]

**Checklist for call:**
- [ ] Patient arrived safely
- [ ] Medications obtained from pharmacy
- [ ] Understands medication regimen
- [ ] No new or worsening symptoms
- [ ] Knows follow-up appointment dates
- [ ] Equipment delivered and working
- [ ] Home health services started
- [ ] Has questions or concerns

### Readmission Risk Assessment
**Risk level:** [ ] Low [ ] Moderate [ ] High

**Risk factors present:**
- [ ] Prior admission within 30 days
- [ ] ≥ 5 medications
- [ ] Heart failure / COPD
- [ ] Lives alone / limited support
- [ ] Low health literacy
- [ ] Other: ___

**High-risk interventions activated:**
- [ ] Transitional care nurse visit within 48 hours
- [ ] Pharmacist medication reconciliation call
- [ ] PCP appointment within 3 days (not 7)
- [ ] Disease management program enrollment
- [ ] Social work follow-up for SDOH barriers
- [ ] Telehealth check-in schedule

---

## Transition Risk Summary

| Risk | Mitigation Plan | Responsible |
|------|----------------|-------------|
| [Risk 1] | [How addressed] | [Who] |
| [Risk 2] | [How addressed] | [Who] |
| [Risk 3] | [How addressed] | [Who] |

---

**Transition Plan Prepared By:** [Name, Role]
**Date:** [Date]
**Reviewed With Patient/Family:** [ ] Yes — Date: [Date]
```

---

## Usage Notes

- Complete all sections relevant to the transition type
- Medication reconciliation is the MOST CRITICAL section — errors here cause readmissions
- Teach-back should be documented for every educational topic
- Post-discharge call is strongly recommended for ALL patients, required for high-risk
- This template complements `medicine_care_coordination_transitions.md`
- For shift-to-shift handoffs, use `handoff_communication_template.md` instead

---

## False-Positive Prevention

When filling this template:

❌ **DON'T:**
- Fill Pre-Admission Medications from the previous discharge or the outpatient list without checking it against the patient, caregiver or pharmacy fill history — a copied-forward list carries drugs the patient already stopped.
- Tick every Medication Reconciliation Verification box while the Changed and Stopped tables are empty; a ticked "All changes intentional and documented" next to empty tables usually means the comparison was never made.
- Leave the template's pre-printed defaults standing as if they were orders — "Within 7 days" in Follow-Up Appointments, an oxygen flow rate, "[X visits/week]" home-health frequencies.
- Leave Pending Results blank when admission cultures, pathology or send-out labs exist, or carry "NKDA" into Allergies from triage without the current allergy record.

✅ **DO:**
- Recount the medication tables: each pre-admission drug appears in the Discharge Medication List or in Stopped with a reason, and each new or changed drug appears in the discharge list at the same dose and frequency.
- Check that the ticked Readmission Risk level agrees with the risk factors ticked beneath it, and that the high-risk interventions block is completed whenever the level is High.
- Date the Functional Status entries and compare them with a documented pre-admission baseline, not with the patient's state on admission.
