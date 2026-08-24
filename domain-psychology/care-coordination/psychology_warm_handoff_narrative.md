---
title: "Warm-Handoff / Transfer-of-Care Narrative"
category: psychology/care-coordination
description: "Produce a warm-handoff narrative for transferring a client between clinicians or levels of care: reason for transfer, treatment summary, what's working vs. not, active risk, open loops, and recommended next steps."
techniques:
  - ST-04
  - DT-01
  - CM-02
  - DS-02
  - QA-04
difficulty: intermediate
intended_use: model-testing
tags:
  - warm-handoff
  - transfer-of-care
  - continuity-of-care
  - care-coordination
  - level-of-care-transition
  - release-of-information
updated: "2026-06-08"
related_prompts:
  - domain-psychology/care-coordination/psychology_referral_letter_generator.md
  - domain-psychology/care-coordination/psychology_integrated_care_huddle_brief.md
  - domain-psychology/documentation/psychology_initial_treatment_plan.md
  - domain-psychology/documentation/psychology_collateral_contact_note.md
---

# Warm-Handoff / Transfer-of-Care Narrative

## Objective

Produce a transfer-of-care narrative that lets a receiving clinician or program pick up a client without losing continuity: it states **why** the transfer is happening, summarizes the treatment to date, distinguishes **what is working from what is not**, foregrounds **active risk and the current safety plan**, lists **open loops** (pending labs, referrals, prior auths, unaddressed goals), and recommends concrete **next steps**. The narrative is scoped to the signed ROI, applies minimum-necessary, handles SUD content under 42 CFR Part 2, and ensures risk information is never lost in the handoff.

## When to Use

- A client is transferring from one clinician to another (clinician leaving, caseload change, client relocating).
- A client is stepping up or down a level of care (outpatient ↔ IOP/PHP/residential/inpatient) and the receiving program needs a clinical bridge.
- A trainee's caseload is being reassigned at the end of a rotation.
- A client is returning to outpatient after an inpatient or crisis-stabilization stay.
- A practice is closing or a clinician is going on extended leave.

## Inputs / Context Required

- **Transfer direction**: clinician→clinician, step-up, step-down, post-discharge return, rotation handoff.
- **Reason for transfer**: clinical (LOC change) vs. administrative (clinician departure, relocation).
- **Receiving clinician/program**: name, setting, and (if known) modality/intensity.
- **ROI status**: signed ROI to the receiving party? Scope? Expiration? `[clinician input required: ROI specifics if not provided]`.
- **Treatment summary**: diagnoses, presenting concern, course, modalities used, duration, outcome-measure trajectory.
- **What's working / what's not**: interventions with traction; interventions that stalled; alliance notes.
- **Active risk**: current SI/HI/self-harm, recent attempts, current safety-plan status, lethal-means status.
- **Open loops**: pending referrals, labs, prior authorizations, unmet treatment-plan objectives, prescriptions due.
- **Medications**: current list with prescriber.
- **SUD involvement**: any Part 2–governed content?
- `[clinician input required: client's own stated goals and preferences for the next phase of care]`

## Constraints

### Must

- State the reason for transfer and the transfer direction in the first lines.
- Provide a treatment summary that includes diagnoses, modalities tried, duration, and the outcome-measure trajectory (baseline → most recent) where available.
- Separate **what is working** from **what is not** — name specific interventions, not global impressions.
- Carry **active risk forward explicitly**: current risk level, most recent risk assessment date, current safety-plan status, and lethal-means status. Risk content must appear even when the rest of the summary is trimmed for minimum-necessary.
- Enumerate **open loops** with owner and status (pending labs, referrals, prior auths, prescriptions, unmet objectives).
- Provide **recommended next steps** the receiving clinician can act on in the first session.
- Restrict content to the ROI scope and minimum-necessary; gate any 42 CFR Part 2 SUD content behind a Part 2–compliant authorization.
- Include the client's own goals/preferences for the next phase where available.
- Note relevant care-management / transitional-care billing where it applies (e.g., transitional care management when transferring from inpatient back to outpatient, or care-management time).
- Flag missing items as `[clinician input required: ...]`; do not fabricate course, scores, or medications.

### Must Not

- Do not omit or soften active risk to make the handoff "cleaner."
- Do not include content outside the ROI scope or beyond minimum-necessary.
- Do not disclose Part 2 SUD treatment detail under a general HIPAA authorization.
- Do not collapse "what's working" and "what's not" into a single vague paragraph.
- Do not leave open loops without an owner and status.
- Do not fabricate trajectory data, medication details, or prior-clinician opinions.

## Instructions

1. State transfer direction and reason (clinical vs. administrative) first.
2. Verify ROI scope/expiration and Part 2 status; scope all content accordingly.
3. Write the treatment summary: diagnoses, modalities, duration, outcome-measure trajectory.
4. Build the two-column reality check — what's working / what's not — with named interventions and alliance notes.
5. Complete the risk block: current risk, last assessment date, safety-plan status, lethal-means status. Confirm it is present even if the rest is trimmed.
6. Enumerate open loops with owner and status; list current medications with prescriber.
7. Write recommended next steps for the first receiving session, incorporating the client's stated goals.
8. Note transitional-care / care-management billing where applicable.
9. Run verification.

## Output Format

```
=== WARM-HANDOFF / TRANSFER-OF-CARE NARRATIVE ===

DATE: [YYYY-MM-DD]
CLIENT: [Initials / MRN]  DOB: [YYYY-MM-DD]
FROM: [Sending clinician/program, credentials, contact]
TO: [Receiving clinician/program, setting]
TRANSFER DIRECTION: [Clinician→clinician / Step-up / Step-down / Post-discharge return / Rotation handoff]
REASON FOR TRANSFER: [Clinical (LOC change) / Administrative — 1–2 sentences]

TREATMENT SUMMARY (ROI-scoped, minimum-necessary)
Diagnoses: [F##.## Descriptor; ...]
Presenting concern & course: [Brief.]
Modalities & duration: [e.g., Individual CBT, 14 sessions over 4 months; DBT skills group ×8.]
Outcome trajectory: [Instrument: baseline [X] → most recent [Y] (date).]

WHAT'S WORKING
- [Specific intervention with traction + evidence.]
WHAT'S NOT WORKING / STALLED
- [Specific intervention that stalled + hypothesis.]
Alliance note: [Strength, ruptures/repairs, engagement pattern.]

ACTIVE RISK / SAFETY  (carry forward — do not omit)
Current risk: [None active / Passive ideation / Active SI/HI — describe frequency, plan, intent, means]
Most recent risk assessment: [Tool, date, result]
Safety plan: [On file dated [YYYY-MM-DD] / Updated / Needs update]
Lethal-means status: [Firearms/medications secured | N/A]

CURRENT MEDICATIONS (list date: [YYYY-MM-DD])
- [Medication, dose, frequency] — Prescriber: [Name]

OPEN LOOPS
| Item | Type | Owner | Status |
|------|------|-------|--------|
| [Pending lab / referral / prior auth / Rx / unmet objective] | [...] | [Sending/Receiving/PCP] | [Pending/Due [date]] |

RECOMMENDED NEXT STEPS (for first receiving session)
1. [Concrete, actionable]
2. [...]
Client's stated goals/preferences for next phase: [...]

RELEASE OF INFORMATION
Signed ROI to receiving party: [Yes/No]  Scope: [...]  Expires: [YYYY-MM-DD]
42 CFR Part 2 (SUD) content: [None | Present — Part 2 authorization required]

Billing note: [Transitional care management / care-management time if applicable]

Signature: ____________________  [Clinician, credentials]  Date: __________
```

## Verification

- [ ] Transfer direction and reason stated up front.
- [ ] Treatment summary includes diagnoses, modalities, duration, and outcome trajectory.
- [ ] "What's working" and "what's not" are separated, with named interventions.
- [ ] Active-risk block present with current risk, last assessment date, safety-plan status, lethal-means status — not omitted.
- [ ] Open loops enumerated with owner and status.
- [ ] Recommended next steps are concrete and first-session-actionable.
- [ ] Content limited to ROI scope and minimum-necessary; Part 2 SUD content gated separately.
- [ ] Current medications listed with prescriber and list date.
- [ ] Client's stated goals/preferences included.
- [ ] Transitional-care / care-management billing noted where applicable.
- [ ] Nothing fabricated; missing inputs flagged with `[clinician input required]`.
