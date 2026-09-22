# Stage 4 — Price and Package

**Gate A — priceable scope.** Code-enforced. No price is quoted until the scope
record is complete.

**Input:** the scope record · **Output:** the `commercial` block

---

## Purpose

Choose the charging structure and the number. Gate A stands in front of both,
because pricing an under-specified scope is the most expensive routine mistake in
services work — and the one that feels most like momentum at the time.

## Procedure

### 1. Run the gate first

```bash
python3 skills/scope-ledger/scripts/scope_ledger.py --gateA <engagement.json>
```

**BLOCKED** → go back to Stage 3. The gate names each missing element. Do not quote
a number "subject to scoping"; that number becomes the anchor and the scoping never
catches up.

If the client is pressing for a figure before scope is finished, the honest answer is
a range with its basis stated and an explicit note that it is not a quote — or better,
a proposal for a **paid discovery phase**, which is the highest-leverage structure
available to a services practice.

**PASS** → continue.

### 2. Establish the floor

```bash
python3 skills/engagement-economics/scripts/economics.py --floor config/practice.json
```

Three thresholds come back. Nothing below walk-away is quotable at any relationship
value: it consumes capacity and returns nothing.

### 3. Establish the ceiling

Run `domain-business-strategy/client-services/services_client_value_quantification.md`
where the engagement has a plausible economic case. It produces a conservative annual
value and a fee band derived from it.

Where the value case cannot be built — inputs unavailable, attribution contested —
say so and price from the floor plus positioning. That is a legitimate outcome, and
better than a value case built entirely from client-supplied optimism.

### 4. Choose the structure

Run `domain-business-strategy/client-services/services_pricing_model_selector.md`.
It reasons from scope stability, outcome measurability and who carries the estimation
risk, and enforces four hard rules:

1. Never fixed-fee undiagnosed work
2. Never value-price without attribution
3. Never quote fixed fee with unmeasured estimate error
4. Never leave a retainer uncapped

Rule 3 binds here. Check your estimate-error series:

```bash
python3 skills/engagement-economics/scripts/economics.py --self-check
```

— and see `skills/engagement-economics/references/method.md` for the eligibility
rule. Fewer than five data points, or a coefficient of variation above 0.40, means
day rate or milestone, not fixed fee.

If a retainer is selected, run
`domain-business-strategy/client-services/services_retainer_design_and_ceiling.md`
and carry its ceiling, overage rule, rollover policy and review cadence into the
record.

### 5. Set the number

- **Fixed price** → price from **75th-percentile effort**, not median. Half your
  engagements exceed the median by definition; a fixed price at median loses on
  roughly half of deliveries.
- **Day rate** → at or above the floor. Discounting toward walk-away is a decision
  about reserves and pipeline, not about the client.
- **Milestone** → each milestone priced from its own deliverable estimate.
- Check the result sits inside the value band. If the variance-loaded price exceeds
  what the work is worth, the scope is too large — narrow it rather than discounting.

### 6. Build two options

Offer two or three structures at comparable expected value, tiered by **scope**, not
by quality. A choice between shapes converts "is this too expensive" into "which
suits us," and the answer tells you what the client fears.

### 7. Set the payment schedule

Front-load deliberately. Deposit on signature, progress payments at real milestones,
and a final tranche no larger than 25%. Stage 8 projects the cash dates; Stage 5
carries the schedule into the proposal.

### 8. Assemble the record

```json
"commercial": {
  "structure": "fixed | day_rate | milestone | retainer | value_share",
  "fee": 0,
  "estimated_days": 0,
  "rate_basis": "75th percentile effort × floor rate",
  "options": [],
  "payment_schedule": [
    { "label": "Deposit", "amount": 0, "trigger": "signature", "issue_date": "" }
  ]
}
```

## Verification

- [ ] Gate A passed **before** any number was written
- [ ] The floor was computed, not remembered
- [ ] The quoted rate is at or above walk-away
- [ ] Fixed price, if used, is based on 75th-percentile effort and a measured
      estimate error with CV ≤ 0.40
- [ ] The four hard rules are explicitly checked
- [ ] A retainer, if used, has a ceiling and an above-ceiling rule
- [ ] Two options are offered, tiered by scope
- [ ] The final payment is no more than 25% of total

## Boundaries

Not tax or accounting advice. The rate floor's employment-burden treatment is
jurisdiction-specific — see `domain-finance/tax-planning/solo_dev_tax_strategy.md`.
