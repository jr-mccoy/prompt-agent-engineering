# Architecture Studio

*Not legal, tax, accounting or insurance advice. **Every number in `practice.json` is
invented** — a worked example so the gates have something to run against, not a benchmark.
Run [Stage 0](../../prompts/stage-0-practice-config.md) and replace all of them.*

## Shape of the practice

Staged design work, typically fee-per-stage against a recognised work-stage framework,
with a long tail of contract-administration. Billable fraction is low (0.58 in the
example) because business development, competitions and unpaid feasibility consume real
time. Typical overrun is the highest of the five verticals (0.25) because design iterates
and briefs move.

**Where the money leaks:** unpaid feasibility, brief creep between stages, and consent
risk priced as though it were controllable.

## Deliverable writer

`domain-professional-writing/domain-specific/domain_writing_architect_proposal.md` — the
proposal and RFP response. Stage 5 assembles; that prompt writes.

## Trade-specific disqualifiers

| Signal | Tier | Why |
|---|---|---|
| `planning_consent_assumed` | proceed with protection | A client treating consent as a formality will treat refusal as your failure. Stage the engagement so the consent gate is a commercial decision point, not a surprise |
| `brief_changes_between_conversations` | proceed with protection | A moving brief is the single best predictor of overrun here. Require a paid feasibility stage before committing to a fee for the whole job |

## Gate A — what must be in scope

The stage framework does most of the work, but Gate A still needs:

- **Which work stages are in this appointment**, and which are a separate future
  appointment. Naming stage boundaries is the scope
- Number of design iterations per stage before further work becomes a variation
- Who is responsible for surveys, and what is assumed in their absence
- Whether consent risk is yours or the client's — stated, not implied
- What happens to the fee if consent is refused
- Whether contract administration and site inspections are in, and how many visits
- Which consultants the client appoints directly versus through you

The consent question is the one that must be explicit. A fee structure that pays only on
approval transfers a risk substantially outside your control, and
`services_pricing_model_selector.md`'s hard rule against value-pricing without
attribution applies directly.

## Gate B — clauses that bite here

| Clause | Why it matters in this trade | Review with |
|---|---|---|
| **Fitness for purpose** | Higher than reasonable skill and care and commonly outside professional indemnity cover. Accepting it can leave the practice's largest exposure uninsured | `legal_contract_clause_redline_targeted.md` |
| **Copyright and licence to use designs** | Whether the client gets a licence or the copyright, and whether the licence survives non-payment. A licence conditional on payment is real leverage | `legal_contract_clause_redline_targeted.md` |
| **Novation** | Being novated to a contractor mid-project changes who you owe duties to, on terms you did not negotiate. Check the pre-agreed form | `legal_contract_review_full_redline.md` |
| **Net-contribution and liability cap** | Without a net-contribution clause you can carry the full loss where another consultant is partly responsible | `legal_contract_clause_redline_targeted.md` |
| **Professional indemnity run-off** | Claims-made cover responds only while live. Closing or selling the practice without run-off leaves historic work bare | `domain-finance/risk-management/finance_business_insurance_coverage_review.md` |

The insurance seam matters more here than in any other vertical in this set: several of
these clauses interact directly with what professional indemnity will and will not
respond to.

## Invoicing notes

- **Fee per stage, invoiced on stage completion**, with a written stage sign-off as the
  trigger — Stage 8's acceptance-based triggers rather than calendar dates
- Abortive-work provision: what is payable if the project pauses between stages. Pauses
  are common and indefinite
- Additional services logged and charged as they arise, not accumulated and presented at
  the end, which is how they get written off
