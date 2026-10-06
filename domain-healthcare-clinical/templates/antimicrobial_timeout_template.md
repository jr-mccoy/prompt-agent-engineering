---
title: "Antimicrobial Timeout Template"
category: healthcare-clinical/templates
description: "Fill-in 48–72 hour antimicrobial timeout template to improve stewardship, safety, and treatment precision: reassess cultures, source control and clinical response, then continue, narrow, escalate, switch to PO or stop with a documented end date and owner."
techniques:
  - NE-03
  - ST-42
  - OC-03
  - DS-40
  - QA-01
difficulty: intermediate
tags:
  - antimicrobial-stewardship
  - antibiotics
  - infectious-disease
  - medication-safety
  - documentation
updated: "2026-10-06"
---

# Antimicrobial Timeout Template

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

> 48–72 hour antimicrobial timeout template to improve stewardship, safety, and treatment precision.

---

```markdown
# Antimicrobial Timeout: [Patient Name / MRN]

## Mandatory Data Fields
- **Timeout Date/Time:** [Required]
- **Hospital Day / Antibiotic Day #:** [Required]
- **Primary Team:** [Required]
- **Reviewer(s):** [ID/PharmD/Primary team]
- **Suspected/Confirmed Infection Source:** [Required]
- **Current Antimicrobials (drug/dose/route/frequency/start date):** [Required]

---

## Diagnostic Reassessment
- **Culture/Microbiology Data:** [Source, date, organism, susceptibilities]
- **Key Imaging/Source Control Findings:** [Required]
- **Clinical Response:** [Improving/No change/Worsening]
- **Alternative Diagnoses Considered:** [Required]

---

## Timeout Decision (Select and justify)
- [ ] Continue current regimen
- [ ] Narrow/de-escalate
- [ ] Escalate/broaden
- [ ] Switch IV to PO
- [ ] Stop antimicrobials

**Rationale:** [Required]

---

## Red-Flag / Safety Section
- **Sepsis/instability red flags present?** [Yes/No; details]
- **Drug safety checks:**
  - [ ] Renal dose adjusted
  - [ ] Hepatic dose adjusted
  - [ ] Allergy cross-reactivity reviewed
  - [ ] QT/proarrhythmia risk assessed
  - [ ] C. difficile risk reviewed
  - [ ] Major drug-drug interactions reviewed
- **Source control incomplete?** [Yes/No; action plan]

---

## Follow-up Accountability
| Next Action | Owner | Due Date/Time | Success Metric | Escalation Path |
|-------------|-------|---------------|----------------|-----------------|
| [Repeat culture / stop date / consult] | [Required] | [Required] | [Required] | [Required] |

- **Documented planned duration/end date:** [Required]
- **Automatic stop/review order placed:** [Yes/No]
- **ID consult needed or updated:** [Yes/No]

---

## Communication Clarity Checks
- [ ] Indication for each antimicrobial is explicitly linked to diagnosis.
- [ ] Stop date or review date specified for every agent.
- [ ] Dosing rationale is understandable to covering clinicians.
- [ ] Patient counseling completed for major adverse effects and adherence.
- [ ] Handoff note includes what to do if culture data changes.

**Patient/Caregiver Education Notes:** [Required if discharge therapy planned]
**Timeout Signed:** [Name, role, date/time]
```

---

## False-Positive Prevention

When filling this template:

❌ **DON'T:**
- Copy "Current Antimicrobials (drug/dose/route/frequency/start date)" from the original order when the dose was renally adjusted or the agent changed since; the timeout must match the current MAR.
- Tick "Renal dose adjusted" because the drug appears on a renal-adjustment list rather than after comparing the current dose with the latest CrCl; a ticked box records a check done, not a check that applies.
- Count "Antibiotic Day #" from the most recent regimen change instead of the first antimicrobial dose for this infection — the planned duration and end date then come out too long.
- Enter "no growth" under Culture/Microbiology Data while cultures are still preliminary, or "Improving" under Clinical Response without the temperature, WBC or source-control trend behind it.

✅ **DO:**
- Recompute the end date from the Day-1 date plus the intended duration, and confirm the same date appears in "Documented planned duration/end date" and in the automatic stop order.
- Match each continued agent to an organism and susceptibility listed in Culture/Microbiology Data; an agent with no match needs its empiric rationale stated in **Rationale**.
- Write `[not available at timeout]` in any field whose data are missing rather than a typical dose, duration or result.
