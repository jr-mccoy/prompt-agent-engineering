---
title: "PCP Communication Note (Psychiatric / Medication Coordination)"
category: psychology/care-coordination
description: "Write a minimum-necessary note to the primary care physician conveying relevant psychiatric and medication information: diagnoses, current psychotropics and monitoring needs, labs requested, and specific coordination asks."
techniques:
  - ST-04
  - DT-01
  - CM-02
  - DS-02
  - QA-04
difficulty: intermediate
intended_use: model-testing
tags:
  - pcp-communication
  - care-coordination
  - medication-monitoring
  - psychotropic-labs
  - minimum-necessary
  - release-of-information
updated: "2026-06-08"
related_prompts:
  - domain-psychology/care-coordination/psychology_referral_letter_generator.md
  - domain-psychology/care-coordination/psychology_integrated_care_huddle_brief.md
  - domain-psychology/psychiatric-prescriber/psychology_med_management_progress_note.md
  - domain-psychology/documentation/psychology_collateral_contact_note.md
---

# PCP Communication Note (Psychiatric / Medication Coordination)

## Objective

Generate a concise note from a behavioral-health clinician or prescriber to the client's **primary care physician** that conveys only the psychiatric and medication information the PCP needs to coordinate safely: active diagnoses, current psychotropics with **monitoring requirements**, any **labs or vitals being requested**, drug-interaction or metabolic concerns, and a short list of **coordination asks**. The note respects the signed ROI, applies HIPAA minimum-necessary, handles SUD content under 42 CFR Part 2, and carries forward any active risk the PCP should know about.

## When to Use

- A psychiatric prescriber starts, changes, or stops a psychotropic and the PCP must be informed for monitoring (e.g., lithium, valproate, antipsychotics, stimulants, SSRIs with QTc considerations).
- A psychotropic requires baseline or interval labs/vitals the PCP can draw (CBC, CMP, lipids, HbA1c, TSH, lithium level, valproate level, ECG/QTc, weight/BMI, blood pressure).
- A medical condition or medication may be contributing to psychiatric symptoms and a work-up is requested (thyroid, B12, anemia, sleep apnea).
- Coordinating shared management of a client both providers see.
- After a psychiatric hospitalization, updating the PCP on medication changes.

## Inputs / Context Required

- **PCP** name, practice, and secure contact route.
- **Sending clinician** identity, credentials, license, role (therapist vs. prescriber), callback.
- **ROI status**: signed release to the PCP? Scope? Expiration? `[clinician input required: ROI specifics if not provided]`.
- **Active psychiatric diagnoses** (DSM-5-TR / ICD-10-CM) relevant to coordination.
- **Current psychotropic regimen**: agent, dose, frequency, start/change date, prescriber.
- **Monitoring requirements** tied to each agent (labs, vitals, ECG, weight/metabolic).
- **Labs/vitals requested** from the PCP and the rationale.
- **Interaction / metabolic concerns** with the client's medical medications.
- **Risk status**: any active SI/HI/self-harm the PCP should be aware of.
- **SUD involvement**: any Part 2–governed content?
- `[clinician input required: which provider owns ongoing monitoring (prescriber vs. PCP) for each lab]`

## Constraints

### Must

- Limit content to **minimum-necessary** for medical coordination — diagnoses, meds, monitoring, labs, and asks. No full psychotherapy narrative.
- For each current psychotropic, state agent, dose, frequency, prescriber, and the **specific monitoring requirement** (e.g., "lithium — check level, BUN/Cr, TSH q6 months; level 12 h post-dose").
- State any **labs/vitals requested** from the PCP with rationale and the requested timeframe, and identify **who owns** acting on the result.
- Note relevant **drug-interaction or metabolic** concerns with the client's medical regimen.
- Restrict disclosure to the **ROI scope**; gate 42 CFR Part 2 SUD content behind a Part 2–compliant authorization.
- Carry forward **active risk** in a clearly labeled block if present; do not bury it.
- End with a short, explicit list of **coordination asks** (each actionable).
- Note relevant care-coordination / interprofessional-consult billing where applicable (e.g., 99446–99449 / 99451 / 99452, or care-management time).
- Flag missing data as `[clinician input required: ...]`; do not fabricate doses, labs, or monitoring intervals.

### Must Not

- Do not transmit a full mental-health record or therapy process notes to the PCP — minimum-necessary only.
- Do not disclose content outside the ROI scope.
- Do not release Part 2 SUD treatment detail under a general HIPAA authorization.
- Do not list a psychotropic without its monitoring requirement when one exists.
- Do not request labs without naming the rationale and the owner of follow-up.
- Do not fabricate monitoring intervals, lab values, or doses.

## Instructions

1. Confirm the ROI to the PCP and its scope/expiration; restrict all content accordingly. Note Part 2 status if SUD content is present.
2. List active coordination-relevant diagnoses (omit unrelated history).
3. Build the medication table: each psychotropic with dose, frequency, prescriber, and its monitoring requirement.
4. Specify labs/vitals requested from the PCP, with rationale, timeframe, and follow-up owner.
5. Add interaction/metabolic concerns relative to the client's medical medications.
6. Add a risk/safety block if active risk exists.
7. Write the coordination asks as a short numbered list, each actionable.
8. Attach billing note where applicable; run verification.

## Output Format

```
=== PCP COMMUNICATION NOTE ===

DATE: [YYYY-MM-DD]
TO: [PCP name, practice]    Route: [secure fax / portal]
FROM: [Sending clinician, credentials, license #, role]    Callback: [phone]
RE: [Client initials / MRN]    DOB: [YYYY-MM-DD]

PURPOSE: [1 line — e.g., "Update on medication change and lab-monitoring request."]

────────────────────────────────────────────────────────
ACTIVE PSYCHIATRIC DIAGNOSES (coordination-relevant)
- [F##.## Descriptor]
- [...]

CURRENT PSYCHOTROPIC REGIMEN & MONITORING
| Agent | Dose | Freq | Start/Change | Prescriber | Monitoring requirement |
|-------|------|------|--------------|------------|------------------------|
| [..]  | [..] | [..] | [date]       | [..]       | [labs/vitals/ECG/weight + interval] |

LABS / VITALS REQUESTED FROM PCP
| Test | Rationale | Timeframe | Result follow-up owner |
|------|-----------|-----------|------------------------|
| [..] | [..]      | [..]      | [Prescriber / PCP]     |

INTERACTION / METABOLIC CONCERNS
- [Concern with the client's medical medications, if any — or "None identified."]

────────────────────────────────────────────────────────
RISK / SAFETY  [include only if active risk]
Current risk: [Passive/active SI/HI — describe]
Safety plan: [On file dated YYYY-MM-DD / N/A]
What the PCP should watch for: [...]

────────────────────────────────────────────────────────
COORDINATION ASKS
1. [Actionable ask — e.g., "Draw lithium level + BUN/Cr + TSH within 2 weeks; send results to prescriber."]
2. [...]

RELEASE OF INFORMATION
Signed ROI to PCP: [Yes/No]    Scope: [...]    Expires: [YYYY-MM-DD]
42 CFR Part 2 (SUD) content: [None | Present — Part 2 authorization required]

Billing note: [Interprofessional consult / care-management code if applicable]

Signature: ____________________  [Clinician, credentials]  Date: __________
```

## Verification

- [ ] Content limited to minimum-necessary for medical coordination (no full therapy narrative).
- [ ] Each psychotropic has dose, frequency, prescriber, and its monitoring requirement.
- [ ] Labs/vitals requested with rationale, timeframe, and follow-up owner.
- [ ] Interaction / metabolic concerns addressed (or explicitly "none identified").
- [ ] ROI scope and expiration stated; disclosure limited to that scope.
- [ ] 42 CFR Part 2 SUD content gated behind Part 2 authorization (not bundled under HIPAA ROI).
- [ ] Active risk, if present, carried forward in a labeled block.
- [ ] Coordination asks are a short, actionable numbered list.
- [ ] Billing note included where applicable.
- [ ] No fabricated doses, labs, or monitoring intervals; gaps flagged with `[clinician input required]`.
```
