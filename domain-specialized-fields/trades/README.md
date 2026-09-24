# Trades — Bidding, Estimating, and Change Orders

Three prompts for contractors and trade subcontractors, covering the commercial
decisions around the work: whether to bid, what the number is, and how to price
and communicate a change once the job is under way. They produce numbers and
decisions; the customer-facing estimate document and the contract come from
elsewhere (see boundaries).

## Contents

| File | Use |
|---|---|
| [`trades_bid_no_bid_decision.md`](trades_bid_no_bid_decision.md) | Hard gates (license, insurance, capacity in the work window, cash exposure on real days-to-pay, documents), anchored scores, expected value, kill signal, ready decline note |
| [`trades_bid_estimate_with_contingency.md`](trades_bid_estimate_with_contingency.md) | Quantity takeoff with sources, burdened labor, allowances, unknowns register (resolve / unit price / T&M / exclude / carry), contingency = Σ probability × impact |
| [`trades_change_order_pricing_notice.md`](trades_change_order_pricing_notice.md) | Classify the change, price it under the contract's pasted terms, credits and schedule days, plain-language owner notice with a dated decision |

Order of use: bid / no-bid → estimate → (mid-job) change order. The estimate and
change-order examples share one job, so the unit prices and allowances carry through.

## Guards (every prompt)

- **No legal or licensing determinations.** Contract clauses are quoted, never
  interpreted; enforceability questions go to an attorney.
- **Code, permit and safety items are flagged for the licensed trade or the local
  authority**, never asserted.
- **Every quantity and price has a source** (`[measured]`, `[sub quote]`,
  `[supplier quote]`, `[our-data]`, `[estimate]`); expired quotes are unknowns.

## Boundaries — not here

| If you need… | Go to |
|---|---|
| The customer-facing estimate or proposal document | [`domain-professional-writing/domain-specific/`](../../domain-professional-writing/domain-specific/) (`domain_writing_hvac_estimate.md`, `domain_writing_contractor_remodel.md`, …) |
| Engagement letters, client intake, or a standalone scope of work | [`legal_sow_drafter.md`](../../domain-legal/contracts-transactional/legal_sow_drafter.md), [`client-services-studio/`](../../client-services-studio/README.md) (stage 3 scoping, `scope-ledger` drift detection) |
| A trade's pre-configured services pipeline | [`client-services-studio/verticals/`](../../client-services-studio/verticals/README.md) |
| Project scheduling and supplier management for non-software projects | [`domain-operations/`](../../domain-operations/) |
