---
title: "Superbill Generator (Out-of-Network Claim)"
category: psychology/practice-operations
description: "Generate a compliant superbill for a client's out-of-network reimbursement claim — provider NPI/tax-ID, rendering vs billing provider, dates of service, CPT + modifiers + units, ICD-10 diagnosis codes, charges, payments, and the required statement language."
techniques:
  - ST-02
  - OC-01
  - DS-02
  - CM-02
  - QA-04
difficulty: beginner
intended_use: model-testing
tags:
  - superbill
  - out-of-network
  - CPT
  - ICD-10
  - NPI
  - reimbursement
  - billing
updated: "2026-06-08"
related_prompts:
  - domain-psychology/practice-operations/psychology_insurance_verification_intake_protocol.md
  - domain-psychology/practice-operations/psychology_missed_appointment_policy_letter.md
  - domain-psychology/practice-operations/psychology_informed_consent_template_builder.md
  - domain-psychology/documentation/psychology_telehealth_session_note.md
---

# Superbill Generator (Out-of-Network Claim)

## Objective

Produce a complete, itemized superbill (an enhanced receipt) that an out-of-network client can submit to their insurer for reimbursement. A superbill must carry everything a payer needs to adjudicate the claim: provider identifiers (NPI, tax ID), the distinction between the rendering and billing provider, the client/subscriber information, each date of service with its CPT code(s), modifiers and units, the ICD-10 diagnosis code(s) linked to each line, the charge per line, payments received, and the standard statement language clarifying that this is a receipt for services already paid and not a request for payment to the practice.

## When to Use

- A client sees the provider out-of-network (or fully private-pay) and wants to seek partial reimbursement from their plan's OON benefits.
- Monthly or per-session superbill generation for an established OON caseload.
- A client's insurer requests an itemized statement to process a previously submitted claim.
- Transitioning a client flagged as OON during insurance verification into a reimbursement workflow.

## Inputs / Context Required

- **Billing / rendering provider details**: provider name and credentials, individual NPI (Type 1), organization NPI (Type 2) if billing under a group, tax ID / EIN or SSN, license number, and practice address. `[practice input required: NPI(s), tax ID, license #]`
- **Rendering vs billing provider**: is the clinician who provided care the same entity that bills, or is care billed under a group/supervising entity? Both may need to appear.
- **Client (patient) info**: name, date of birth, address.
- **Subscriber info** (if client is a dependent): subscriber name, DOB, member ID, relationship.
- **Insurer**: name and member/group ID (for the client's own submission).
- **Dates of service**: each session date to include.
- **CPT code(s) per session**: e.g., 90791 (intake), 90832/90834/90837 (individual 30/45/60 min), add-on 90833/90836/90838 (psychotherapy with E/M), 90846/90847 (family without/with patient), 90853 (group).
- **Modifiers**: e.g., telehealth modifier 95 (audio-video) or 93 (audio-only), and place of service (POS 11 office, POS 02 telehealth provider site, POS 10 telehealth in patient's home).
- **Units** per line (typically 1 for psychotherapy codes).
- **ICD-10 diagnosis code(s)**: e.g., F41.1, F33.1 — linked to each service line via a diagnosis pointer.
- **Charge per line and total**; **payments received** from the client.
- `[practice input required: confirm the diagnosis on the superbill matches the medical record; superbills must reflect the documented diagnosis, not a code chosen for reimbursement]`

## Constraints

### Must

- Include provider identifiers: individual NPI, and group/organization NPI if billing under a group; tax ID/EIN; license number; full practice address.
- Distinguish the **rendering provider** (who delivered the service) from the **billing provider/entity** when they differ.
- List each **date of service** as its own line with: CPT code, any modifier(s), units, charge, and a diagnosis pointer linking it to an ICD-10 code.
- Place **ICD-10 diagnosis code(s)** in a dedicated diagnosis section and reference them by pointer on each service line.
- Apply the correct **telehealth modifier (95/93)** and **place-of-service** when the session was delivered virtually.
- Show **charges, payments received, and balance** so it is clear the client already paid (or what remains).
- Include the **standard superbill statement language**: that this is an itemized receipt for services rendered and paid, provided to assist the client in seeking out-of-network reimbursement, and that it is not a bill to the client or a claim submitted by the practice.
- Include a provider signature line and date.

### Must Not

- Do not select or alter a diagnosis code to improve the odds of reimbursement; the ICD-10 must match the documented record.
- Do not omit the NPI or tax ID — payers cannot adjudicate without them.
- Do not place an in-person place-of-service code on a telehealth session, or omit the telehealth modifier.
- Do not merge multiple dates of service into one line; each session is its own line.
- Do not fabricate identifiers, codes, charges, or dates; flag missing values with `[practice input required: ...]`.

## Instructions

1. Gather billing/rendering provider identifiers; mark any missing as `[practice input required]`.
2. Enter client and subscriber info (subscriber only if the client is a dependent).
3. List ICD-10 diagnosis code(s) in the diagnosis section; assign each a pointer letter (A, B, C…).
4. For each date of service, create a service line: CPT code → modifier(s) → POS → units → charge → diagnosis pointer.
5. Apply telehealth modifier (95/93) and the correct telehealth POS for any virtual session.
6. Total the charges; record payments received and any balance.
7. Add the standard superbill statement language.
8. Add a provider signature line and date.
9. Run verification.

## Output Format

```
=== SUPERBILL — ITEMIZED STATEMENT FOR INSURANCE REIMBURSEMENT ===
Statement date: [YYYY-MM-DD]

BILLING / RENDERING PROVIDER
Rendering provider: [Name, credentials]   Individual NPI (Type 1): [practice input required]
Billing entity (if different): [Group name]   Group NPI (Type 2): [practice input required]
Tax ID / EIN: [practice input required]   License #: [practice input required]
Address: [Practice address]   Phone: [...]

PATIENT
Name: [Client]   DOB: [YYYY-MM-DD]   Address: [...]
Subscriber (if dependent): [Name, DOB, relationship]
Insurer: [Name]   Member ID: [...]   Group #: [...]

DIAGNOSIS (ICD-10)
A: [F##.##] [Descriptor]
B: [F##.##] [Descriptor]

SERVICES
| Date of Service | CPT  | Modifier | POS | Units | Dx Ptr | Charge |
|-----------------|------|----------|-----|-------|--------|--------|
| [YYYY-MM-DD]    | 90791| —        | 11  | 1     | A      | $[__]  |
| [YYYY-MM-DD]    | 90837| 95       | 10  | 1     | A      | $[__]  |
| [YYYY-MM-DD]    | 90847| 95       | 10  | 1     | A,B    | $[__]  |

TOTALS
Total charges: $[__]
Payments received from client: $[__]
Balance: $[__]

STATEMENT
This is an itemized receipt for psychotherapy services rendered and paid in full
[or as noted above]. It is provided to assist the client in seeking reimbursement
from out-of-network benefits. It is not a bill to the client and is not a claim
submitted by this practice to the insurer.

Provider signature: ____________________________  Date: ___________
```

## Verification

- [ ] Individual NPI present; group NPI present when billing under a group; tax ID/EIN and license # present or flagged.
- [ ] Rendering vs billing provider distinguished when they differ.
- [ ] Client and (if applicable) subscriber info complete.
- [ ] ICD-10 diagnosis code(s) in a dedicated section with pointer letters.
- [ ] Each date of service is its own line with CPT, modifier(s), POS, units, charge, and diagnosis pointer.
- [ ] Telehealth modifier (95/93) and telehealth POS (02/10) applied to virtual sessions; in-person POS (11) only for office sessions.
- [ ] Charges, payments received, and balance shown.
- [ ] Standard superbill statement language present (receipt, OON reimbursement aid, not a bill/claim).
- [ ] Provider signature line and date present.
- [ ] Diagnosis matches the documented record; no reimbursement-driven code selection.
- [ ] No fabricated identifiers, codes, charges, or dates; missing values flagged `[practice input required]`.
```
