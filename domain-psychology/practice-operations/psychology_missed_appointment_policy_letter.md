---
title: "Missed-Appointment / Late-Cancellation Policy Letter Drafter"
category: psychology/practice-operations
description: "Draft a no-show and late-cancellation policy letter or consent clause with fee, notice window, insurance-cannot-be-billed note, telehealth applicability, and a repeated-no-show discharge pathway."
techniques:
  - ST-02
  - OC-01
  - CM-02
  - QA-04
difficulty: beginner
intended_use: model-testing
tags:
  - missed-appointment
  - no-show
  - late-cancellation
  - practice-policy
  - billing
  - telehealth
updated: "2026-06-08"
related_prompts:
  - domain-psychology/practice-operations/psychology_informed_consent_template_builder.md
  - domain-psychology/practice-operations/psychology_insurance_verification_intake_protocol.md
  - domain-psychology/documentation/psychology_telehealth_session_note.md
---

# Missed-Appointment / Late-Cancellation Policy Letter Drafter

## Objective

Generate a clear, enforceable missed-appointment and late-cancellation policy — as either a standalone client letter or a consent-packet clause — that states the fee, the notice window, why the fee cannot be billed to insurance, how the policy applies to telehealth, and the pathway by which repeated no-shows lead to discharge. The output must be plain-language (6th–8th grade reading level), signable, and consistent with the practice's other intake documents.

## When to Use

- Building or refreshing the intake packet for a new client.
- Sending a standalone reminder letter to a client who has begun missing appointments.
- Standardizing a policy across a group practice so all clinicians apply the same fee and notice window.
- Converting a verbal "we charge for no-shows" practice into a written, signed policy.

## Inputs / Context Required

- Output type: standalone letter to client / consent-packet clause / both.
- No-show fee amount and late-cancellation fee amount (may be the same or different). `[practice input required: dollar amounts]`
- Cancellation notice window (e.g., 24 hours, 48 hours, "by close of business the prior day").
- Whether the first occurrence is waived (a one-time courtesy) or charged immediately.
- Telehealth applicability: does the same policy apply to video/phone sessions, and what counts as a "no-show" for telehealth (e.g., client not present in the virtual room within N minutes)?
- Repeated-no-show threshold that triggers a discharge conversation (e.g., 3 no-shows in a rolling 6 months).
- How the fee is collected (card on file, billed to client, due before next session).
- Practice identifying details: practice name, clinician name/credentials, contact line. `[practice input required: practice header details]`
- `[practice input required: any state or payer rule that restricts charging Medicaid/Medicare beneficiaries a missed-appointment fee]`

## Constraints

### Must

- State the fee amount(s) and the notice window in the first third of the document.
- Include an explicit note that **missed-appointment fees are the client's responsibility and cannot be billed to insurance** (insurers do not reimburse for services not rendered), so the client pays out of pocket.
- Specify telehealth applicability separately and define what constitutes a telehealth no-show.
- Describe the repeated-no-show discharge pathway as a sequence (warning → documented conversation → possible discharge with referral), not an abrupt termination.
- Keep language at a 6th–8th grade reading level; define any term that must be used.
- Include a signature/acknowledgment line with date when the output is a consent clause.
- Flag every missing dollar amount, window, or practice detail with `[practice input required: ...]`.

### Must Not

- Do not state or imply that the missed-appointment fee will be submitted to or paid by the client's insurance.
- Do not promise to waive the fee in cases not specified by the practice.
- Do not draft an immediate, no-warning termination as the standard pathway; abandonment risk requires notice and referral.
- Do not invent a specific dollar amount, notice window, or state rule; leave a flagged slot.
- Do not include legal-advice language about enforceability; this is a practice policy document, not a legal opinion.

## Instructions

1. Confirm the output type (letter, clause, or both) and the practice header details.
2. State the fee(s) and notice window plainly up front.
3. Add the insurance-cannot-be-billed note in client-facing language.
4. Add the telehealth section defining a telehealth no-show and confirming the same (or modified) fee applies.
5. Describe the repeated-no-show discharge pathway as a graduated sequence ending in referral, not abandonment.
6. Add a collection-mechanism sentence (how and when the fee is paid).
7. If a consent clause, append a signature/acknowledgment block.
8. Keep the tone respectful and non-punitive; frame the policy as protecting appointment availability for all clients.
9. Run verification.

## Output Format

```
=== MISSED-APPOINTMENT / LATE-CANCELLATION POLICY ===

[PRACTICE HEADER]
Practice: [Name]    Clinician: [Name, credentials]
Contact: [Phone | Email]    Effective date: [YYYY-MM-DD]

POLICY SUMMARY
- Late-cancellation fee: $[amount]   No-show fee: $[amount]
- Notice required to cancel without a fee: [e.g., 24 hours before the session]
- First occurrence: [waived as a courtesy / charged]

WHY YOU PAY THIS FEE DIRECTLY
Your insurance cannot be billed for a missed or late-cancelled session, because
no service was provided. That means this fee is your responsibility and is paid
out of pocket. [Collection method: e.g., charged to the card on file / due before
your next session.]

TELEHEALTH SESSIONS
This policy also applies to video and phone sessions. For telehealth, a "no-show"
means [you are not present in the virtual session within [N] minutes of the start
time]. The same notice window and fee apply [or describe any difference].

WHAT HAPPENS WITH REPEATED MISSED APPOINTMENTS
We want your appointment time to be available to you and to other clients. If
missed appointments continue:
1. After [N] no-shows, we will reach out to talk about what is getting in the way.
2. We will document that conversation and look for solutions (reminders, schedule changes).
3. If no-shows continue past [threshold, e.g., 3 in 6 months], we may end care and
   provide referrals so you can continue treatment elsewhere.

ACKNOWLEDGMENT  [include only for consent-clause output]
I have read and understand this policy.
Client: ____________________________  Date: ___________
Guardian (if applicable): __________  Date: ___________

[Flag any missing value as [practice input required: ...].]
```

## Verification

- [ ] Fee amount(s) and notice window stated in the first third of the document.
- [ ] Insurance-cannot-be-billed note present in client-facing language.
- [ ] Telehealth applicability addressed with a telehealth no-show definition.
- [ ] Repeated-no-show pathway is graduated (warning → conversation → discharge with referral), not abrupt.
- [ ] Collection mechanism stated.
- [ ] Signature/acknowledgment block present when output is a consent clause.
- [ ] Reading level plain (6th–8th grade); any technical term defined.
- [ ] No claim that the fee is billed to or paid by insurance.
- [ ] All missing dollar amounts, windows, and practice details flagged with `[practice input required]`.
- [ ] Nothing fabricated (no invented amounts, windows, or state rules).
