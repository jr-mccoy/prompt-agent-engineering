# Client Services

Prompts for running a practice that **sells expertise** — consulting, freelance and
agency work — as opposed to selling a product.

The distinction is load-bearing. The rest of `domain-business-strategy/` and the
41 marketing skills under `domain-agentic-resources/skills/marketing/` address a
founder taking a *product* to market: positioning, funnels, CRO, subscription tiers.
This directory addresses the person whose inventory is their own time, where the
binding constraints are capacity, scope stability and getting paid.

**Prefix:** `services_`

## Contents

| Prompt | Job |
|---|---|
| `services_offer_definition_and_boundary.md` | Name the offer, close the deliverable list, write the exclusions |
| `services_ideal_client_and_disqualifiers.md` | Two-sided client profile; the disqualifier list is the point |
| `services_pricing_model_selector.md` | Hourly / day rate / fixed / milestone / retainer / value share |
| `services_client_value_quantification.md` | The client-side economic model that anchors a price |
| `services_retainer_design_and_ceiling.md` | A retainer that does not decay into unpaid employment |
| `services_capacity_and_utilization_planner.md` | Sellable days, the bench date, and whether pipeline covers it |
| `services_productized_offer_designer.md` | Whether an offer is repeatable enough to fix a price to |
| `services_client_concentration_risk_check.md` | Revenue and capacity dependence on one buyer |

## Where the rest of the workflow lives

These prompts are sequenced end to end by
[`client-services-studio/`](../../client-services-studio/) at the repository root,
which orchestrates them alongside existing resources rather than duplicating any:

| Step | Owned by |
|---|---|
| Discovery call | `../../domain-sales-customer/sales/sales_discovery_call_preparation.md` |
| Acceptance criteria | `../../domain-engineering-workflows/workflows/workflow_definition_of_done_builder.md` |
| SOW and contract clauses | `../../domain-legal/contracts-transactional/` |
| Rate conversation | `../../domain-negotiation/contexts/negotiation_freelance_rate_conversation.md` |
| Rate floor, margin, invoicing, AR | `../../domain-finance/` |
| Proposal, case study, testimonial | `../../domain-professional-writing/business-writing/` |

## Boundaries

- **Self scope, not here.** Your own confidence in a number is
  `../../domain-personal-development/prompts/solo-dev/solo_dev_pricing_value_confidence.md`.
  This directory handles the client's arithmetic and the practice's structure.
- **Money objects go to finance.** Rate floors, subcontractor margin and engagement
  profitability live in `../../domain-finance/`, following the precedent recorded in
  this domain's "What moved out, and why".
- **Not legal advice.** Contract prompts draft and flag; a lawyer reviews before
  signature.
