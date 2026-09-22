# Management Consulting

*Not legal, tax, accounting or insurance advice. **Every number in `practice.json` is
invented** — a worked example so the gates have something to run against, not a benchmark.
Run [Stage 0](../../prompts/stage-0-practice-config.md) and replace all of them.*

## Shape of the practice

The vertical closest to the pipeline's default assumptions, and the one it was designed
around. Project-based advisory, sold on outcomes, delivered by the principal. Highest
positioning premium of the five (0.20) and highest rate floor, against the lowest
billable fraction (0.58) — because business development is the job when you are the
product.

**Where the money leaks:** pricing undiagnosed work as though it were diagnosed, scope
absorbed a request at a time, and a sponsor who leaves mid-engagement.

## Deliverable writer

`domain-professional-writing/domain-specific/domain_writing_consultant_executive_summary.md`
— the executive summary, which for this trade is frequently the deliverable that decides
whether the recommendation is acted on.

## Trade-specific disqualifiers

| Signal | Tier | Why |
|---|---|---|
| `outcome_shifts` | proceed with protection | The desired outcome moving between conversations is the strongest available predictor of overrun. Require a **paid discovery phase** and price the delivery after it — the highest-leverage structure available to this trade |
| `no_sponsor_above_contact` | probe | Work commissioned by a day-to-day contact with no executive sponsor dies when priorities move, and the recommendation is never implemented. Ask who will present this internally |

## Gate A — what must be in scope

This trade fails Gate A more than any other in the set, because the work is inherently
less tangible and clients ask for "help with" things. The acceptance criteria are where
the discipline lands:

- **Deliverables as artifacts**, not activities. "Strategic review" fails the stranger
  test; "a written assessment of the seven named processes against the six criteria in
  Appendix A" passes
- Interview and workshop counts, capped
- Number of review rounds on each deliverable before further work is a variation
- Whether implementation is in scope, or only the recommendation. **The most common
  disputed boundary in the trade**, and it belongs in the exclusion list explicitly
- Who provides data, by when, and what happens to conclusions if it does not arrive —
  findings marked unverified is a real and usable consequence
- Whether you present to a board or committee, and how many times

## Gate B — clauses that bite here

| Clause | Why it matters in this trade | Review with |
|---|---|---|
| **Unlimited liability** | Advisory exposure is uncapped by default and can exceed the fee by orders of magnitude. Gate B flags this as critical for good reason | `legal_contract_clause_redline_targeted.md` |
| **IP in methods and tools** | A clause assigning all work product can capture the frameworks and templates you bring to every engagement. Licence the deliverable; retain the method | `legal_contract_clause_redline_targeted.md` |
| **Non-solicitation of client staff** | Reasonable in principle, frequently drafted so broadly it prevents you working in the sector | `legal_contract_review_full_redline.md` |
| **Exclusivity or non-compete by sector** | Sometimes worth accepting for a premium. Usually worth less than the market it closes | `legal_contract_review_full_redline.md` |
| **Termination for convenience with no compensation** | Common in corporate paper and expensive when your capacity was reserved. Per-work-performed plus committed costs is a low-resistance ask | `legal_termination_economics_provider_side.md` |
| **Transition assistance, unpriced** | Frequently the largest unpriced liability in a long engagement, and nobody resists capping it | `legal_termination_economics_provider_side.md` |

## Pricing notes

The pipeline's pricing prompts were written with this trade in view:

- `services_pricing_model_selector.md` — the four hard rules, especially never
  fixed-pricing undiagnosed work
- `services_client_value_quantification.md` — the client-side economic case, where one
  exists and can be attributed
- `services_productized_offer_designer.md` — once the same engagement has run five times,
  the coefficient of variation decides whether it can be fixed-price

## Invoicing notes

- Deposit on signature, milestone payments on **deliverable acceptance** rather than on
  calendar dates, final tranche no more than 25%
- Where a paid discovery phase precedes delivery, invoice it separately and in full. It
  is the engagement that proves you can be paid before the larger one is at risk
- Watch the client's procurement machinery: corporate AP with a PO requirement is where
  Stage 8's silent-rejection failure mode lives
