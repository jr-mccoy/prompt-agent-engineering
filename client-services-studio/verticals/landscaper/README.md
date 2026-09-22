# Landscape & Grounds

*Not legal, tax, accounting or insurance advice. **Every number in `practice.json` is
invented** — a worked example so the gates have something to run against, not a benchmark.
Run [Stage 0](../../prompts/stage-0-practice-config.md) and replace all of them.*

## Shape of the practice

Project installation plus recurring maintenance, largely consumer and small-commercial.
Highest billable fraction of the five (0.70) because site time is billable and the
selling cycle is short — and the highest bad-debt rate (0.05), because consumer work
concentrates collection risk and the amounts are small enough that pursuit rarely pays.

**Where the money leaks:** ground conditions discovered on the day, weather absorbed
rather than priced, and plant establishment failures blamed on the installer when the
client did not water.

## Deliverable writer

`domain-professional-writing/domain-specific/domain_writing_landscaper_proposal.md` — the
proposal. Stage 5 assembles; that prompt writes.

## Trade-specific disqualifiers

| Signal | Tier | Why |
|---|---|---|
| `no_site_access_before_quote` | **decline** | Quoting a fixed price without walking the site is the trade's defining unforced error. What is under the surface is most of the cost variance |
| `weather_risk_not_accepted` | proceed with protection | A client who will not accept weather-related date movement is a client who will treat rain as your breach. Price the risk explicitly or decline |

## Gate A — what must be in scope

- The **site walk findings**, including access constraints for machinery and spoil removal
- **Ground conditions assumed** — and what happens if rock, made ground, services or
  contamination are found. A named variation route, priced, not goodwill
- Who is responsible for underground service location
- Spoil and green-waste removal: in or out, and volume assumed
- **Plant establishment and any replacement guarantee — conditional on stated aftercare.**
  The trade's most common dispute, and it is resolved entirely by writing the watering
  obligation down
- Weather: what movement is accepted, and how the date changes
- Whether maintenance follows, and whether that is this engagement or a separate one
- Making good of access routes and neighbouring surfaces

The ground-conditions and establishment items are where the exclusion list earns its
keep. Both are foreseeable and both are routinely left implicit.

## Gate B — clauses that bite here

Consumer contracts in particular carry statutory protections that override what the
contract says, and they vary by jurisdiction:

| Clause | Why it matters in this trade | Review with |
|---|---|---|
| **Cancellation rights** | Consumer contracts frequently carry a statutory cooling-off period, and starting work inside it without the right written acknowledgement can mean you cannot recover for work done. This is not negotiable by contract — check the rule | `legal_payment_terms_and_late_fee_review.md` and take advice |
| **Deposit and staged payments** | Some jurisdictions cap deposits or require protection for consumer prepayments | `legal_payment_terms_and_late_fee_review.md` |
| **Establishment guarantee** | A guarantee not conditioned on aftercare is an unbounded replacement obligation | `legal_contract_clause_redline_targeted.md` |
| **Adjacent property damage** | Access routes, neighbours' boundaries and shared drives. Check what public liability actually responds to | `finance_business_insurance_coverage_review.md` |
| **Suspension for non-payment** | Most valuable remedy in a trade with high bad debt — and consumer rules may limit it | `legal_payment_terms_and_late_fee_review.md` |

The cancellation-rights point is the one to get advice on rather than reason about: it is
statutory, it differs by jurisdiction, and the consequence of getting it wrong is losing
the fee for work already done.

## Invoicing notes

Bad debt is the structural risk, so the schedule matters more here than the rate:

- **Deposit before mobilisation**, staged payments against site milestones, small final
  tranche. Stage 8 warns when the final payment exceeds 25% — in this trade treat that
  warning as a hard rule
- Materials-heavy jobs: invoice materials at delivery to site, not at completion
- Maintenance contracts invoiced **in advance** of the period
- The collections ladder runs faster here. Small consumer debts frequently justify rung 7's
  write-off branch, and computing that honestly beats pursuing a £900 debt through a
  process costing more than the debt

Model the working-capital gap where subcontractors or plant hire are involved:
`domain-finance/corporate-finance-fpa/finance_subcontractor_margin_model.md`.
