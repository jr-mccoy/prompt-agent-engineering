---
title: "Business-Logic Flaw Hunting"
category: bug-bounty/hunting
description: "Structured ideation and test plan for business-logic vulnerabilities on in-scope targets: abuse of intended functionality that scanners miss, with low duplicate rates and high payouts"
techniques:
  - ST-01
  - RT-02
  - QA-02
  - DS-01
  - DD-07
difficulty: advanced
tags:
  - bug-bounty
  - business-logic
  - abuse-case
  - workflow
  - race-condition
updated: "2026-06-18"
related_prompts:
  - domain-software-engineering/bug-bounty/bugbounty_access_control_idor_hunt.md
  - domain-software-engineering/bug-bounty/bugbounty_finding_triage_validation.md
  - domain-software-engineering/bug-bounty/bugbounty_severity_cvss_impact.md
---

# Business-Logic Flaw Hunting

**Objective:** Find ways to abuse the *intended* functionality of an in-scope target — the logic flaws automated scanners can't see — by reasoning about what the workflow assumes and where those assumptions break.

## When to Use
- The target has multi-step workflows: checkout, refunds, subscriptions, transfers, coupons, quotas, approvals.
- You want high-value, low-duplicate findings that require human reasoning, not payloads.
- A workflow "feels" abusable and you want to structure the attack on its assumptions.

## Inputs / Context
- **The workflow(s)** to analyze (steps, roles, money/quota/state involved).
- **Your own test accounts** and any test payment instruments the program provides.
- **RoE limits** — especially around payments, real money, and quotas.

## Instructions

1. **Authorization gate.** Confirm the workflow is in scope. Use only test accounts/instruments the program permits; never exploit a payment/refund flaw to obtain real goods, money, or services — prove the logic flaw and stop. Respect RoE on financial testing.

2. **Document the intended workflow** as the developer imagined it: the happy path, the state transitions, and the *implicit assumptions* (e.g., "price is recalculated server-side," "you can't refund more than you paid," "a coupon applies once").

3. **Enumerate the assumptions and attack each one:**
   - **Sequence:** skip a step, repeat a step, do steps out of order, resume an abandoned flow.
   - **Quantity/sign:** negative values, zero, huge values, fractional/decimal, currency mismatches.
   - **State:** modify server-trusted state from the client (price, role, status, discount) via parameter tampering / mass assignment.
   - **Time/concurrency:** race conditions on limited resources (apply a coupon, redeem credit, or withdraw twice in parallel).
   - **Identity/ownership:** perform an action on an object/step that belongs to another stage or account.
   - **Limits:** bypass quotas, rate limits, trial limits, or approval gates.

4. **Prioritize by impact-if-true:** money, free access, data exposure, or trust-boundary breaks rank above cosmetic logic quirks.

5. **Design a minimal abuse case** for each top hypothesis: the exact sequence of requests that would prove the assumption is unenforced, using your own accounts.

6. **CRITICAL — verify it's a real, impactful logic flaw, not intended behavior:**
   - Reproduce the abuse case with your own account(s) and confirm the system accepted the invalid state (e.g., order placed at the tampered price, coupon applied twice).
   - Confirm there's genuine impact (financial/access/data), not a harmless inconsistency the system later corrects.
   - Rule out that the behavior is intended or compensated elsewhere (e.g., reconciled at fulfillment).
   - For anything financial, stop at proof — do not complete a transaction that transfers real value to you.
   - Assign confidence (High/Med/Low) and note what would change it.

## False-Positive Prevention (MUST follow)
- ❌ Do NOT report a logic quirk that the system reconciles/corrects before any real effect (e.g., price fixed at payment capture).
- ❌ Do NOT actually obtain free goods/money/services — prove the flaw and halt.
- ❌ Do NOT assume a race condition exists without demonstrating a concrete double-effect (two redemptions, two withdrawals).
- ❌ Do NOT confuse a UI-only restriction with a server-enforced rule — test the API directly.
- ✅ DO confirm the server accepted the invalid state and it had real impact.
- ✅ DO check whether downstream reconciliation neutralizes the flaw.
- ✅ DO keep financial proofs at the minimum and never extract real value.

## Output Format
```
## Authorization & Safety Note
[In-scope workflow; test accounts/instruments; financial RoE]

## Intended Workflow & Assumptions
1. [step] — assumes: ...

## Abuse Hypotheses (ranked by impact-if-true)
| Rank | Assumption attacked | Technique | Impact if true |

## Abuse-Case Tests & Results
| # | Sequence | Server accepted invalid state? | Real impact? | Verdict |

## Verified Finding
### [Flaw] — confidence: High/Med/Low
- Assumption broken: ...
- Proof (own accounts, minimal): ...
- Impact: ...
- Reconciliation check: [does anything downstream correct it?]
- What would change confidence: ...

## Self-Audit
[Server accepted invalid state; real impact; no real value extracted]
```

## Example Output
```
## Authorization & Safety Note
In-scope: api.acme.com checkout + coupon flow. Test account bbtest+a, program-provided test card. RoE
allows checkout testing with the test card only; no real settlement.

## Intended Workflow & Assumptions
1. Add items → assumes price comes from server catalog.
2. Apply coupon → assumes one use per order, server-validated.
3. Pay → assumes total recomputed server-side.

## Abuse Hypotheses (ranked)
| Rank | Assumption attacked | Technique | Impact if true |
|------|--------------------|-----------|----------------|
| 1 | coupon once-per-order | concurrency (parallel apply) | stacked discounts → underpayment |
| 2 | price from server | tamper line-item price in body | arbitrary price |
| 3 | total recomputed | tamper total at pay step | underpayment |

## Abuse-Case Tests & Results
| # | Sequence | Invalid state accepted? | Real impact? | Verdict |
|---|----------|------------------------|--------------|---------|
| 1 | apply SAVE10 x5 in parallel | yes — 50% applied | discount stacked | VULN |
| 2 | PATCH line price to 0.01 | rejected (server price) | none | secure |
| 3 | tamper total field at pay | rejected (recomputed) | none | secure |

## Verified Finding
### Coupon stacking via race condition — confidence: High
- Assumption broken: "one coupon use per order" is not concurrency-safe.
- Proof: firing 5 parallel "apply SAVE10" requests on my own cart resulted in 5 stacked applications
  (50% off) before validation caught up. Reproduced twice. I did NOT complete settlement.
- Impact: arbitrary discount stacking → systematic underpayment; financial loss to the merchant.
- Reconciliation check: the discount persisted into the pre-payment total; no downstream correction
  observed before the pay step (stopped here).
- What would change confidence: if fulfillment recomputed discounts — could not verify post-pay without
  settling; reported with this caveat.

## Self-Audit
Server accepted the stacked-discount state on my own cart; concrete double+ effect shown; no real
purchase completed and no real value obtained.
```

## Techniques Used
- **ST-01 (Clear Objective Statement)** — targets abuse of intended functionality, not payloads.
- **RT-02 (Multi-Dimensional Analysis)** — attacks sequence, quantity, state, time, identity, and limits.
- **QA-02 (Adversarial Thinking)** — systematically inverts each workflow assumption.
- **DS-01 (Framework Application)** — applies an assumption-enumeration framework to any workflow.
- **DD-07 (Self-Audit Table)** — verification distinguishes real impact from reconciled quirks.
