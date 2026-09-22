# HVAC Contracting

*Not legal, tax, accounting or insurance advice. **Every number in `practice.json` is
invented** — a worked example so the gates have something to run against, not a benchmark.
Run [Stage 0](../../prompts/stage-0-practice-config.md) and replace all of them.*

## Shape of the practice

Installation and maintenance work, mostly fixed-price against a surveyed scope, with a
maintenance contract tail. Billable fraction runs high relative to advisory practices
(0.68 in the example) because travel and site time are billable — but the reserve is real,
because a plant room rarely matches its drawings.

**Where the money leaks:** quoting without surveying, discovering asbestos or
non-compliant existing work after starting, and retention held long after commissioning.

## Deliverable writer

`domain-professional-writing/domain-specific/domain_writing_hvac_estimate.md` — the
estimate itself. Stage 5 assembles the proposal; that prompt writes the estimate inside
it.

## Trade-specific disqualifiers

Beyond the three common ones, `practice.json` adds:

| Signal | Tier | Why |
|---|---|---|
| `no_site_access_before_quote` | **decline** | A fixed price on an unsurveyed site is an unbounded liability. This is the single most important gate in the trade |
| `landlord_tenant_payer_unclear` | proceed with protection | Get written confirmation of who pays before mobilising; the dispute surfaces at invoice, when the work is done and leverage is gone |

## Gate A — what must be in scope

Beyond the standard requirements, an HVAC scope is not priceable without:

- The **survey findings**, not the client's description of the system
- What happens if existing work is found non-compliant — a named variation route, not
  goodwill
- Who is responsible for asbestos survey and any removal
- Access windows, and whether out-of-hours working is priced
- Commissioning and handover: who witnesses, what document closes it
- Whether making-good of building fabric is in or out

## Gate B — clauses that bite here

Gate B's ten flags all apply. These three matter disproportionately, and the reviewing
prompts are in `domain-legal/contracts-transactional/`:

| Clause | Why it matters in this trade | Review with |
|---|---|---|
| **Retention** | A percentage held to a defect-liability date months after commissioning. Check the amount, the release trigger and who certifies it | `legal_payment_terms_and_late_fee_review.md` |
| **Liquidated damages for delay** | Frequently attached to a programme you do not control, where a main contractor's slippage becomes your exposure | `legal_contract_clause_redline_targeted.md` |
| **Fitness for purpose** | A materially higher standard than reasonable skill and care, and commonly excluded by professional indemnity cover — so accepting it can leave you uninsured | `legal_contract_clause_redline_targeted.md` |

The fitness-for-purpose point is the one to check with the broker rather than assume:
see `domain-finance/risk-management/finance_business_insurance_coverage_review.md`, which
covers the seam between contractual liability accepted and cover actually held.

## Invoicing notes

Stage 8 projects cash from the client's payment run. In this trade also check:

- **Application-for-payment cycles** on larger jobs, which are a different rhythm from
  invoicing and have their own cut-offs
- **Retention release** tracked as a dated receivable, or it is forgotten
- **Materials paid before mobilisation** — the working-capital gap that
  `domain-finance/corporate-finance-fpa/finance_subcontractor_margin_model.md` models
