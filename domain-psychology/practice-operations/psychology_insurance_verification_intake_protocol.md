---
title: "Insurance Verification (Benefits Check) Intake Protocol"
category: psychology/practice-operations
description: "Run a structured benefits-verification at intake — eligibility, in/out-of-network, copay/coinsurance/deductible, telehealth coverage, prior-auth and session limits, CPT-code coverage — and document plus read back the result to the client."
techniques:
  - ST-02
  - DS-02
  - OC-01
  - CM-02
difficulty: beginner
intended_use: model-testing
tags:
  - insurance-verification
  - benefits-check
  - intake
  - eligibility
  - prior-authorization
  - telehealth-coverage
updated: "2026-06-08"
related_prompts:
  - domain-psychology/practice-operations/psychology_superbill_generator.md
  - domain-psychology/practice-operations/psychology_missed_appointment_policy_letter.md
  - domain-psychology/practice-operations/psychology_informed_consent_template_builder.md
---

# Insurance Verification (Benefits Check) Intake Protocol

## Objective

Produce a structured, repeatable benefits-verification worksheet a front-desk or intake clinician can complete before the first session — capturing eligibility, network status, cost-share (copay/coinsurance/deductible), telehealth coverage, prior-authorization and session-limit requirements, and CPT-code-specific coverage — and ending with a client read-back script so the client understands their out-of-pocket responsibility before care begins.

## When to Use

- Before a new client's first billed session, once you have their plan information.
- When a returning client changes plans, employers, or has a new plan year (deductibles reset).
- When verifying whether a planned service (e.g., 90837, family therapy, telehealth) is covered before scheduling.
- When a claim was denied and you need to re-verify what the plan actually covers.

## Inputs / Context Required

- Client name, date of birth, and member ID exactly as on the insurance card.
- Insurer name, plan type (HMO/PPO/EPO/POS), and group number.
- Subscriber name and relationship to client (self / spouse / parent), if client is a dependent.
- Provider's network status with this plan (in-network / out-of-network / unknown).
- The CPT code(s) you expect to bill (e.g., 90791 intake; 90834/90837 individual; 90847 family; 90853 group).
- Place of service: office (POS 11) vs telehealth (POS 02 home-of-provider rules / POS 10 client-home), and whether telehealth is the intended delivery method.
- Verification channel: payer portal / provider phone line / clearinghouse eligibility (270/271).
- `[practice input required: the reference/call ID and representative name from the verification call, for documentation]`
- `[practice input required: any carve-out behavioral-health vendor (e.g., the medical plan vs a separate managed behavioral-health organization) handling these benefits]`

## Constraints

### Must

- Verify and record eligibility status and effective dates first (an active member ID is not proof of active coverage).
- Capture network status explicitly; if out-of-network, record OON benefit details and route the client toward a superbill workflow.
- Record the full cost-share picture: copay, coinsurance %, individual and family deductible amounts, and **how much of the deductible has been met**.
- Verify telehealth coverage as a distinct line item — coverage, any audio-only (modifier 93) limitation, and parity with in-person.
- Check prior-authorization requirements and any annual session/visit limit for outpatient psychotherapy.
- Confirm coverage of the specific CPT code(s) intended, including the intake code and the routine session code.
- Capture the verification reference: date, channel, representative name, and call/reference ID for the record.
- End with a client read-back script stating estimated per-session out-of-pocket cost and that the quote is not a guarantee of payment.

### Must Not

- Do not treat "member is active" as a complete verification; benefits, network, and limits must each be confirmed.
- Do not quote a copay without noting whether the deductible must be met first (cost-share often changes once the deductible is satisfied).
- Do not present any benefits quote as a guarantee of payment; payers describe quotes as estimates.
- Do not assume telehealth or family therapy is covered because individual in-person therapy is.
- Do not fabricate a reference ID, representative name, or coverage figure; flag unknowns with `[practice input required]`.

## Instructions

1. Confirm member identity fields against the card; note the subscriber if the client is a dependent.
2. Verify eligibility: active status, plan effective and term dates, and whether behavioral health is carved out to a separate vendor.
3. Determine network status for the rendering provider; if OON, capture OON benefits and flag for superbill.
4. Capture cost-share: copay, coinsurance %, deductible (individual/family) and amount met; note out-of-pocket maximum if provided.
5. Verify telehealth coverage separately, including audio-only limitations and any originating-site rules.
6. Check prior-authorization requirement and outpatient session/visit limits per plan year.
7. Confirm coverage of each intended CPT code (intake + routine session + any add-on or family/group code).
8. Record the verification reference (date, channel, rep, call ID).
9. Write the client read-back script with an estimated per-session cost and the not-a-guarantee statement.
10. Run verification.

## Output Format

```
=== INSURANCE BENEFITS VERIFICATION WORKSHEET ===

MEMBER & PLAN
Client: [Name]   DOB: [YYYY-MM-DD]   Member ID: [as on card]
Insurer: [Name]   Plan type: [HMO/PPO/EPO/POS]   Group #: [...]
Subscriber: [Name]   Relationship: [self/spouse/parent]
Behavioral health carved out to: [None / vendor name]

ELIGIBILITY
Active: [Yes/No]   Effective: [YYYY-MM-DD]   Term/renewal: [YYYY-MM-DD]
Plan year resets (deductible) on: [YYYY-MM-DD]

NETWORK STATUS
Rendering provider: [In-network / Out-of-network]
If OON: OON benefit %: [__]   → route to superbill workflow.

COST-SHARE
Copay (specialist/behavioral health): $[__]
Coinsurance: [__]% after deductible
Individual deductible: $[__]   Met so far: $[__]
Family deductible: $[__]   Met so far: $[__]
Out-of-pocket max: $[__]   Met so far: $[__]
Cost-share applies: [before deductible met / only after deductible met]

TELEHEALTH
Telehealth covered: [Yes/No]   Parity with in-person: [Yes/No]
Audio-only (modifier 93) covered: [Yes/No/Limited]
Originating-site / location notes: [...]

AUTHORIZATION & LIMITS
Prior authorization required: [Yes/No]   Auth #: [if obtained]
Outpatient session limit (plan year): [__]   Used: [__]

CPT-CODE COVERAGE CHECK
| CPT | Service | Covered? | Cost-share notes |
|-----|---------|----------|------------------|
| 90791 | Intake / diagnostic eval | [Y/N] | [...] |
| 90834 / 90837 | Individual 45 / 60 min | [Y/N] | [...] |
| 90847 | Family w/ patient | [Y/N] | [...] |
| 90853 | Group | [Y/N] | [...] |

VERIFICATION REFERENCE
Date verified: [YYYY-MM-DD]   Channel: [portal / phone / 270-271]
Representative: [name]   Call/Reference ID: [practice input required]

CLIENT READ-BACK SCRIPT
"Based on what your plan told us on [date], your estimated cost per session is
about $[__] [until your deductible of $[__] is met, then $[__]]. Telehealth
[is/is not] covered. This is an estimate, not a guarantee of payment — your plan
makes the final decision when the claim is processed. Do you have questions about
your out-of-pocket cost before we begin?"
```

## Verification

- [ ] Eligibility status and effective/term dates recorded (not just an active member ID).
- [ ] Network status captured; OON cases routed to superbill workflow.
- [ ] Copay, coinsurance, deductible (individual/family), and amount met all recorded.
- [ ] Whether cost-share applies before or after the deductible is stated.
- [ ] Telehealth verified as a separate line item, including audio-only and parity.
- [ ] Prior-authorization requirement and session limit checked.
- [ ] Each intended CPT code's coverage confirmed (intake + routine + family/group as relevant).
- [ ] Verification reference (date, channel, rep, call ID) captured or flagged.
- [ ] Client read-back script includes a per-session estimate and a not-a-guarantee statement.
- [ ] No coverage figure, rep name, or reference ID fabricated; unknowns flagged with `[practice input required]`.
