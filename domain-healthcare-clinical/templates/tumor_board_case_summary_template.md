---
title: "Tumor Board Case Summary Template"
category: healthcare-clinical/templates
description: "Fill-in multidisciplinary cancer case summary template for tumor board review, covering diagnostic summary, staging, prior treatment, red-flag safety constraints, and follow-up accountability for coordinated diagnostic and treatment planning."
techniques:
  - ST-03
  - OC-03
  - RT-02
  - QA-01
difficulty: advanced
tags:
  - tumor-board
  - oncology
  - multidisciplinary
  - cancer-staging
  - clinical-documentation
updated: "2026-10-06"
---

# Tumor Board Case Summary Template

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

> Multidisciplinary cancer case summary template for coordinated diagnostic and treatment planning.

---

```markdown
# Tumor Board Case Summary: [Patient Name / MRN]

## Mandatory Data Fields
- **Patient Identifiers:** [Name, MRN, DOB]
- **Tumor Board Date:** [Required]
- **Presenting Clinician:** [Name, specialty]
- **Primary Oncologist/Surgeon:** [Required]
- **Cancer Type / Site:** [Required]
- **Stage (with system used):** [Required]
- **Performance Status (ECOG/KPS):** [Required]

---

## Diagnostic Summary
- **Histology/Pathology:** [Required]
- **Biomarkers/Molecular Findings:** [Required; include test source/date]
- **Imaging Summary:** [Key findings + dates]
- **TNM details:** [Required if applicable]
- **Comorbidities impacting treatment:** [Required]

---

## Prior and Current Treatment
| Modality | Dates | Regimen/Procedure | Response | Toxicities/Complications |
|----------|-------|-------------------|----------|--------------------------|
| Surgery  |       |                   |          |                          |
| Systemic Therapy | |                 |          |                          |
| Radiation |      |                   |          |                          |

---

## Key Clinical Question for Tumor Board
- [Required specific decision question]
- [Alternative options under consideration]

---

## Red-Flag / Safety Section
- **Urgent oncologic issues:** [Spinal cord compression, SVC syndrome, neutropenic fever, etc.]
- **Safety constraints:**
  - Organ function limitations: [Renal/hepatic/cardiac]
  - Contraindicated therapies: [Required]
  - Drug interaction concerns: [Required]
- **Clinical trial eligibility risks/exclusions:** [Required]
- **Time-sensitive deadlines (e.g., surgery window):** [Required]

---

## Follow-up Accountability
| Board Recommendation | Responsible Clinician/Team | Deadline | Required Patient Discussion Date | Status |
|----------------------|----------------------------|----------|----------------------------------|--------|
| [Required] | [Required] | [Required] | [Required] | [Open/Closed] |

- **Who places orders:** [Required]
- **Who communicates final recommendations to patient/family:** [Required]
- **Who tracks completion of staging/workup items:** [Required]

---

## Communication Clarity Checks
- [ ] Recommendation includes goal (curative/palliative/symptom-control).
- [ ] Benefits/risks documented in language understandable by patient/family.
- [ ] Uncertainties and rationale for chosen plan documented.
- [ ] Next action has owner + date + contingency if delayed.
- [ ] Patient preferences/goals and equity/access barriers explicitly addressed.

**Board Consensus Level:** [Unanimous/Majority/No consensus]
**Documentation Finalized By:** [Name, date/time]
```

---

## False-Positive Prevention

When filling this template:

❌ **DON'T:**
- Fill "Stage (with system used)" from the imaging impression alone, or omit the staging-system edition and whether the stage is clinical (c) or pathologic (p); a bare "Stage III" passes as complete and may be wrong.
- List biomarker or molecular results that are merely expected for the histology; a marker that was never sent is "not tested", and one in process is "pending" with the send date.
- Write "None" in "Contraindicated therapies" or "Drug interaction concerns" when no one checked; the only acceptable negative is "none identified on review of [source] by [name, date]".
- Carry the ECOG/KPS forward from the initial consult when function has changed since then.
- Describe Response in the treatment table as "responding" or "stable" unless the dated imaging report says so (with the response criteria named, if the report uses them).

✅ **DO:**
- Trace each TNM element, biomarker result and imaging finding to the dated report it came from, and flag any result that predates the last treatment change.
- Re-derive the stage group from the T, N and M you entered using the named staging system, and confirm it matches the "Stage" field.
- Check the organ-function limitations against current, dated labs and studies (creatinine clearance, bilirubin, LVEF) rather than the values at diagnosis.
- Before "Documentation Finalized By", confirm each Follow-up Accountability row names a person, not only a team, plus a deadline.
