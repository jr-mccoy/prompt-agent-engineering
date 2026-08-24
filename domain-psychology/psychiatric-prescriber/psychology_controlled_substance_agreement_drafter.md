---
title: "Controlled-Substance Treatment Agreement Drafter"
category: psychology/psychiatric-prescriber
description: "Draft a controlled-substance treatment agreement for the chart (stimulant or benzodiazepine): single-prescriber/single-pharmacy terms, PDMP checks, lost/early-refill policy, UDS, safe storage, diversion consequences, and signatures."
techniques:
  - ST-04
  - DS-02
  - QA-04
  - CM-02
  - DT-01
difficulty: intermediate
intended_use: model-testing
tags:
  - controlled-substance-agreement
  - stimulant
  - benzodiazepine
  - PDMP
  - diversion-mitigation
  - safe-storage
updated: "2026-06-08"
related_prompts:
  - domain-psychology/psychiatric-prescriber/psychology_adhd_med_algorithm_reasoner.md
  - domain-psychology/psychiatric-prescriber/psychology_anxiety_med_algorithm_reasoner.md
  - domain-psychology/psychiatric-prescriber/psychology_med_management_progress_note.md
  - domain-psychology/documentation/psychology_initial_treatment_plan.md
---

# Controlled-Substance Treatment Agreement Drafter

## Objective

Generate a controlled-substance treatment agreement suitable for the clinical record when prescribing a Schedule II stimulant or a benzodiazepine (or other controlled psychotropic). The agreement documents the shared expectations that support safe prescribing: a single-prescriber/single-pharmacy arrangement, PDMP monitoring, refill and lost/stolen-medication policy, urine drug screening, safe storage, and the consequences of diversion or misuse. The output is chart-ready, signable, and frames terms as a clinical safety framework — not as a legal threat or a barrier to legitimate care.

## When to Use

- Initiating a stimulant for ADHD or a benzodiazepine where ongoing controlled prescribing is anticipated.
- Continuing controlled prescribing for a patient who lacks an agreement on file.
- Elevated diversion/misuse risk (history, household risk, prior early refills) requiring documented expectations.
- Practice or payor policy requiring a signed controlled-substance agreement.

## Inputs / Context Required

- **Medication(s) and schedule**: agent, formulation, schedule (e.g., II stimulant, IV benzodiazepine).
- **Indication** and treating prescriber/practice information.
- **PDMP review result** and frequency of planned checks per jurisdiction.
- **Pharmacy** the patient designates (single pharmacy).
- **UDS policy**: baseline and random schedule, expected/unexpected results handling.
- **Refill cadence** and whether early refills are permitted.
- **Risk factors**: SUD history, household members at risk, prior agreement violations.
- `[clinician input required: jurisdiction-specific PDMP check frequency and any state-mandated agreement language]`
- `[clinician input required: patient's designated single pharmacy and prescriber of record]`

## Constraints

### Must

- Output labeled sections: **Header / Parties**, **Medication & Indication**, **Single Prescriber / Single Pharmacy**, **PDMP Monitoring**, **Refills & Quantity**, **Lost / Stolen / Early-Refill Policy**, **Urine Drug Screening**, **Safe Storage & Disposal**, **Diversion & Misuse Consequences**, **Patient Responsibilities**, **Prescriber Responsibilities**, **Acknowledgment & Signatures**.
- Specify the **single-prescriber/single-pharmacy** term explicitly (controlled prescriptions for this condition come from one prescriber and are filled at one pharmacy).
- State **PDMP** monitoring expectations and the planned check cadence (`[clinician input required: jurisdiction frequency]`).
- Define the **lost/stolen/early-refill policy**: generally no early replacement of lost/stolen controlled medication; report-to-prescriber requirements; how exceptions are handled.
- Define **UDS** expectations: baseline + random, and how expected/unexpected results are addressed clinically (not punitively framed, but with consequences for diversion).
- Address **safe storage** (locked/secured, away from minors and household members at risk) and **disposal** of unused medication.
- State **diversion/misuse consequences**: clinical actions (re-evaluation, change of plan, taper, discontinuation of controlled prescribing, referral) framed as safety responses.
- Include **patient and prescriber responsibilities** and an **acknowledgment with signature lines** (patient, prescriber, and guardian when a minor).
- Frame the agreement as a **safety and continuity-of-care framework**; keep language respectful and non-stigmatizing.

### Must Not

- Do not write the agreement as a punitive contract or use threatening, shaming language.
- Do not omit the safe-storage and diversion-consequence sections.
- Do not promise early refills for lost/stolen controlled medication as routine.
- Do not invent jurisdiction-specific PDMP or legal language; flag with `[clinician input required: ...]`.
- Do not include a UDS policy without describing how unexpected results are clinically handled.
- Do not fabricate the designated pharmacy/prescriber; flag for completion.

## Instructions

1. Build the **Header/Parties** and **Medication & Indication** block.
2. State the **single-prescriber/single-pharmacy** term and the designated pharmacy/prescriber (`[clinician input required]`).
3. Document **PDMP** monitoring and cadence (`[clinician input required: jurisdiction frequency]`).
4. Define **refills/quantity**, then the **lost/stolen/early-refill policy**.
5. Define the **UDS policy** (baseline + random; handling of expected/unexpected results).
6. Add **safe storage & disposal** expectations.
7. State **diversion/misuse consequences** as clinical safety responses.
8. List **patient** and **prescriber responsibilities**.
9. Add **acknowledgment and signature lines** (patient/guardian/prescriber).
10. Run verification.

## Output Format

```
=== CONTROLLED-SUBSTANCE TREATMENT AGREEMENT ===

HEADER / PARTIES
Patient: [Name/Initials/MRN]   DOB: [YYYY-MM-DD]   Date: [YYYY-MM-DD]
Prescriber of record: [Name, credentials]   Practice: [..]

MEDICATION & INDICATION
Medication(s): [agent, formulation]   Schedule: [II stimulant / IV benzodiazepine / other]
Indication: [..]

SINGLE PRESCRIBER / SINGLE PHARMACY
- Controlled medication for this condition will be prescribed by one prescriber: [clinician input required].
- Filled at one designated pharmacy: [clinician input required].
- I will not obtain controlled medications for this condition from other prescribers/EDs without informing my prescriber.

PDMP MONITORING
- My prescriber will review the Prescription Drug Monitoring Program at the start of care and [clinician input required: jurisdiction-specified frequency].

REFILLS & QUANTITY
- Refills are provided on a [cadence] schedule; quantities are limited per visit.
- Refill requests are made during business hours / at scheduled visits.

LOST / STOLEN / EARLY-REFILL POLICY
- Lost or stolen controlled medication is generally NOT replaced early.
- I will report loss/theft to my prescriber [and file a report where applicable].
- Early refills are not routine; exceptions are at prescriber discretion and documented.

URINE DRUG SCREENING (UDS)
- Baseline and random UDS may be requested.
- Expected and unexpected results are reviewed clinically; unexpected results prompt a discussion and may change the plan.

SAFE STORAGE & DISPOSAL
- I will store medication securely (locked/secured), away from minors and household members at risk.
- I will dispose of unused medication appropriately (take-back/disposal).

DIVERSION & MISUSE CONSEQUENCES
- Diversion, sharing, selling, or misuse leads to clinical safety responses: re-evaluation, taper, discontinuation of controlled prescribing, and/or referral.
- These are safety measures, not punishment, and do not end my access to non-controlled care.

PATIENT RESPONSIBILITIES
- Take medication only as prescribed; attend follow-up; allow PDMP/UDS monitoring; keep medication secure.

PRESCRIBER RESPONSIBILITIES
- Monitor response and safety; review PDMP; provide clear instructions; support continuity and taper if discontinuation is indicated.

ACKNOWLEDGMENT & SIGNATURES
I have read, understand, and agree to this safety framework.
Patient: __________________  Date: ________
Guardian (if minor): ______________  Date: ________
Prescriber: __________________  Date: ________
```

## Verification

- [ ] All required sections present in order.
- [ ] Single-prescriber/single-pharmacy term explicit, with designated pharmacy/prescriber flagged for completion.
- [ ] PDMP monitoring and cadence stated (jurisdiction frequency flagged).
- [ ] Lost/stolen/early-refill policy: no routine early replacement; reporting expectation.
- [ ] UDS policy describes baseline + random AND how unexpected results are clinically handled.
- [ ] Safe storage and disposal addressed.
- [ ] Diversion/misuse consequences framed as clinical safety responses, not threats.
- [ ] Patient and prescriber responsibilities listed.
- [ ] Acknowledgment + signature lines (patient/guardian/prescriber) present.
- [ ] Tone respectful and non-stigmatizing; framed as continuity-of-care safety framework.
- [ ] No fabricated jurisdiction/legal language or designated-party details; gaps flagged `[clinician input required]`.
```
