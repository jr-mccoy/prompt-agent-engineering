---
title: "Collateral Contact Note Drafter"
category: psychology/documentation
description: "Document a collateral contact with PCP, school, family, probation, or other party — including ROI status, purpose, content shared and received, and clinical impact."
techniques:
  - ST-04
  - DT-02
  - QA-04
  - CM-02
difficulty: intermediate
tags:
  - collateral-contact
  - care-coordination
  - release-of-information
  - cpt-90887
  - hipaa
intended_use: model-testing
updated: "2026-05-08"
related_prompts:
  - domain-psychology/documentation/psychology_birp_progress_note.md
  - domain-psychology/care-coordination
---

# Collateral Contact Note Drafter

## Objective

Document a collateral contact involving the client's care — phone call, secure message, email, fax, written report, or in-person meeting — with a third party such as PCP, psychiatrist, school, parent/guardian, custodial parent, probation officer, case manager, or family member. The note must:

1. Confirm Release of Information (ROI) authority for the disclosure.
2. State the purpose of the contact.
3. Document **what was disclosed by the clinician** and **what was received from the collateral source**.
4. Document the clinical impact and any plan changes.
5. Be billable as **CPT 90887** (interpretation/explanation of results to family) when criteria met, or chartable as a non-billable coordination note otherwise.

## When to Use

- Phone call with PCP for medication coordination.
- School-team contact for IEP/504 input.
- Custodial parent / guardian update or coordination.
- Probation/parole or court coordination.
- Receiving a hospital discharge summary or treatment record.
- Collateral interview with family member with client's consent.

## Inputs / Context

- Date, time, duration, modality (phone / secure message / email / fax / in-person).
- Collateral party: name, role, agency, contact method.
- Client: identifiers, treatment-plan goals relevant to the contact.
- ROI status: signed ROI on file, scope of release, expiration date; or basis for disclosure without ROI (mandated reporting, duty to warn, emergency).
- Purpose: medication coordination / school accommodations / discharge handoff / risk concern / case management / forensic / family education.
- Content disclosed by clinician.
- Content received from collateral source.
- Clinical impact: what the clinician learned, what changes the contact triggers, what the client should know.
- Whether the client was informed of the contact in advance and/or after.

## Constraints

### Must

- Output the following labeled sections in order: **Contact Metadata**, **ROI / Authority for Disclosure**, **Purpose**, **Content Disclosed**, **Content Received**, **Clinical Impact**, **Client Informed Status**, **Plan**, **Billing**.
- Document ROI scope (what is permitted), signed-on date, and expiration. If contact is made under a non-ROI authority (mandated report, duty to warn, emergency, court order), document the legal basis.
- "Content Disclosed" and "Content Received" must be separated explicitly so an auditor sees both directions.
- Document whether the client was informed in advance, after, or not yet, with rationale.
- For 90887 billing, document that the activity meets criteria (interpreting/explaining results to a family member, time-based) and time spent.
- Coordination contacts that are not directly with/about the client's care (e.g., general staffing) are not documented in client chart.

### Must Not

- Do not disclose more than the ROI permits. If asked for more, the note documents what was declined and why.
- Do not document content from collateral that is hearsay about non-client third parties unless clinically necessary.
- Do not use client identifiers beyond ROI authorization.
- Do not retroactively justify a contact made without authority; document what occurred and consult supervisor.
- Do not fabricate; flag missing inputs.

## Instructions

1. Compile contact metadata.
2. Document ROI status and scope; if non-ROI authority, name the basis.
3. State purpose.
4. List content disclosed by clinician (with brevity — only what is relevant).
5. List content received from collateral source.
6. Summarize clinical impact in 2–4 sentences.
7. Document whether client was informed of the contact and when.
8. Document plan implications.
9. Apply CPT 90887 if billable; otherwise mark non-billable coordination.
10. Run verification.

## Output Format

```
=== COLLATERAL CONTACT NOTE ===

CONTACT METADATA
Client: [Initials/MRN]
Date: [YYYY-MM-DD]    Time: [HH:MM–HH:MM]    Duration: [N min]
Modality: [Phone / Secure message / Email / Fax / In-person]
Collateral party: [Name, role, agency, contact info]
Treatment-plan goals relevant: [Goal #X, Goal #Y]

ROI / AUTHORITY FOR DISCLOSURE
ROI signed: [YYYY-MM-DD]    Expiration: [YYYY-MM-DD]    Scope: [What may be disclosed]
[OR — non-ROI authority]: [Mandated report (CPS/APS) / Duty to warn (Tarasoff) / Medical emergency exception / Court order / Other — basis cited]

PURPOSE
[1–2 sentences. E.g., "Coordinate SSRI initiation with PCP given client's recent fluoxetine titration and persistent SI."]

CONTENT DISCLOSED (by clinician)
- [Specific items disclosed — limited to ROI scope.]
- [Items declined: "Asked about [X]; disclosure declined as outside ROI scope."]

CONTENT RECEIVED (from collateral source)
- [Specific items received.]

CLINICAL IMPACT
[2–4 sentences: what the clinician learned, how it changes case formulation or plan, what the client should know.]

CLIENT INFORMED STATUS
Informed in advance: [Yes / No, with rationale]
Will be informed after: [Yes — when / How]
[If contact was made over client objection or without consent (mandated report, emergency), document basis and supervisor consultation.]

PLAN
- [Specific changes to treatment plan or coordination triggered by this contact.]
- [Follow-up contact scheduled: party, date, purpose.]
- [Documentation to obtain: e.g., records to be sent, drug-screen result to receive.]
- [Discussion with client at next session.]

BILLING
CPT [90887 if billable family-involvement criteria met / "Non-billable coordination" otherwise]    Time: [N min]
Medical necessity: [If billed, one-sentence justification tied to active diagnosis.]

Clinician: [name, credentials, signature, date/time]
```

## Verification

- [ ] All labeled sections present.
- [ ] ROI scope and expiration documented, OR non-ROI legal basis cited.
- [ ] Content Disclosed and Content Received explicitly separated.
- [ ] Items declined or limited noted if applicable.
- [ ] Client-informed status explicit (advance / after / not yet, with rationale).
- [ ] Clinical impact stated in 2–4 sentences with case-formulation or plan implication.
- [ ] CPT 90887 used only when criteria met; otherwise marked non-billable.
- [ ] Time and duration consistent.
- [ ] Gaps flagged; nothing fabricated.
