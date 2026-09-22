---
title: "Retainer Design and Scope Ceiling"
category: client-services/pricing
description: "Design a services retainer that does not decay into unpaid employment — what is being bought, the scope ceiling and what happens above it, the rollover rule, the review cadence, and the exit terms, with the four failure modes that kill retainers named and guarded"
techniques:
  - CM-02
  - CM-03
  - QA-08
  - OC-03
  - DD-06
difficulty: intermediate
tags:
  - consulting
  - freelance
  - retainer
  - recurring-revenue
  - scope-ceiling
  - solo-operator
updated: "2026-09-21"
---

# Retainer Design and Scope Ceiling

**Objective:** Design a retainer with a stated unit of purchase, an explicit scope
ceiling, a rule for what happens above the ceiling, a rollover policy, a review
cadence, and exit terms. The output is a retainer that survives four quarters without
becoming unpaid employment.

**When to Use:** Use when a client relationship is recurring and you are about to
propose ongoing work, or when an existing retainer has started to feel like a job.
`retainer` returns no results anywhere else in this repository — nothing here covers
it, and the adjacent subscription-design prompts are app billing, not services.

This is **distinct from** `../startup/monetization_subscription_design.md`, which
designs consumer subscription tiers and Play Store billing. The problem there is
conversion and churn; the problem here is that the buyer's demand is elastic and
yours is not, so an uncapped commitment is consumed until it is unprofitable.

---

## Context Gathering

1. **The need**
   - "What does the client actually need continuously, as opposed to periodically?"
   - "What happens today when they need you and there is no retainer?"
   - "Is the demand steady, or bursty with quiet months?"

2. **The history**
   - "Over the last six months, how many hours did this client consume? How variable?"
   - "What fraction was reactive versus planned?"
   - "What did you do for them that you did not bill?"

3. **What they are buying**
   - "Would they rather guarantee your availability, or guarantee a volume of output?"
   - "Who else could do this if you were unavailable for two weeks?"

4. **Your side**
   - "What share of your capacity would this hold?"
   - "If this ended with 30 days' notice, what would you do?"

The variability answer decides the design. A steady need supports an output retainer;
a bursty need supports an access retainer; neither supports the vague "some hours
each month" that most retainers default to and that fails first.

---

## Method

### Step 1 — Name the unit of purchase

A retainer sells exactly one of these. Mixing them is the root cause of most retainer
disputes, because the client bills against one definition and you deliver against
another.

| Unit | The client is buying | Priced on | Unused time |
|---|---|---|---|
| **Access** | Right to your attention within an SLA | Reserved capacity | Not refunded — they bought the reservation |
| **Output** | A recurring deliverable | The deliverable | Not applicable |
| **Capacity** | A block of hours or days | The block | Governed by the rollover rule |
| **Outcome** | A maintained state (uptime, compliance, cadence) | The standard | Not applicable |

The access retainer is the most profitable and the hardest to sell, because the
client is paying for availability they may not consume. Sell it by naming the
response time — that is the product.

### Step 2 — Set the ceiling in the unit you sell

The ceiling must be expressed in the same unit as the purchase. An access retainer
capped in hours is not an access retainer.

- Access → number of requests, or hours of response, per month
- Output → number of deliverables per period
- Capacity → hours or days, stated
- Outcome → the scope of systems or processes covered, enumerated

### Step 3 — Decide what happens above the ceiling, in advance

This is the clause that makes or breaks the retainer. Pick one and write it down:

- **Hard stop** — work pauses until the next period. Cleanest; needs a client who
  plans.
- **Overage at a stated rate** — commonly the standard rate or a premium to it.
  Never at a discount: a discounted overage rate teaches the client that the ceiling
  is decorative.
- **Pull forward** — next period's allocation is consumed early, with a floor on how
  far.
- **Renegotiate at a trigger** — two consecutive overages force a retainer resize.

The failure to avoid is the unwritten fourth option: you absorb it, twice, and the
ceiling stops existing.

### Step 4 — Write the rollover rule

Only capacity retainers need one, and the rule must be bounded:

- Does unused capacity roll? If yes, cap the accumulation (commonly one period) and
  set an expiry. Unbounded rollover creates a liability that surfaces exactly when
  you want to exit.
- State it explicitly for access and outcome retainers too — as "does not roll,
  because you are buying availability, not hours." Saying it prevents the argument.

### Step 5 — Set the review cadence and the exit

- **Review cadence** — a scheduled point (quarterly is standard) where consumption
  against ceiling is reviewed and the retainer is resized in either direction.
  Without this, resizing only ever happens in a crisis.
- **Notice period** — symmetric. A retainer you cannot exit on the same terms the
  client can is employment with extra steps.
- **Minimum term** — if any. Justify it by the ramp cost, or drop it.
- **Wind-down** — what the client gets on exit: handover, documentation, transition
  window. Pricing this in advance stops the final month becoming a hostage
  negotiation.

### Step 6 — Guard the four failure modes

Check the design against each and name the specific guard:

| Failure | Looks like | Guard |
|---|---|---|
| **Silent creep** | Consumption drifts up 10% a quarter, never enough to object to | Consumption tracked and reported monthly, not at renewal |
| **Reactive capture** | Retainer becomes on-call; planned work never happens | Reserve a stated fraction for planned work; protect it |
| **Value fade** | You solved the problem; the client now pays for less need | Review cadence; resize down honestly before they notice |
| **Single-client drift** | Retainer grows until it is most of your revenue | Concentration limit — see the concentration check |

Value fade deserves emphasis. A retainer that quietly stops being worth its price is
the most common way a good client relationship ends badly. Raising it yourself, at
the review, is both the honest move and the one that keeps the client.

---

## Output Format

```markdown
## Retainer — [client]

**Unit of purchase:** [access | output | capacity | outcome]
**What they are buying, in one sentence:** ...

### Terms
| Term | Value |
|---|---|
| Ceiling | [in the unit sold] |
| Above ceiling | [hard stop / overage at X / pull forward / renegotiate] |
| Rollover | [rule + cap + expiry, or "does not roll, because..."] |
| Review cadence | [period] — resize in either direction |
| Notice | [N days, symmetric] |
| Minimum term | [term + justification, or none] |
| Wind-down | [what they get, priced or included] |

### Reserved for planned work
[fraction] — protected from reactive requests by [mechanism]

### Consumption reporting
[what is reported, how often, to whom]

### Failure-mode guards
| Failure | Guard | Observable trigger |
|---|---|---|

### Resize triggers
- Up: [condition]
- Down: [condition] — including the honest fade case
```

---

## Verification

- [ ] Exactly one unit of purchase; the ceiling is stated in that same unit.
- [ ] The above-ceiling rule is written and is not "absorb it."
- [ ] Overage, if used, is not priced below the standard rate.
- [ ] Rollover is bounded and expires, or explicitly does not roll with a reason.
- [ ] Notice is symmetric.
- [ ] Consumption is reported monthly, not discovered at renewal.
- [ ] Each of the four failure modes has a guard with an observable trigger.

**False-positive prevention.** The retainer that looks healthiest on paper — generous
ceiling, flexible overage, warm relationship — is usually the one decaying fastest,
because none of its guards ever fire. Test the design by simulating four quarters at
15% consumption growth per quarter and ask at which point something in the document
objects. If nothing objects before the fourth quarter, the guards are decorative.

Second: a retainer priced on the hours you expect to work is a day rate with worse
cash flow and no upside. If the design ends up as hours × rate, either sell access
and price the reservation, or stop and sell days.

---

## Related

- `services_pricing_model_selector.md` — whether a retainer is the right structure at all
- `services_capacity_and_utilization_planner.md` — what this holds of your capacity
- `services_client_concentration_risk_check.md` — the single-client drift guard
- `../../domain-negotiation/after-the-deal/negotiation_renegotiate_existing_agreement.md` — resizing mid-term
