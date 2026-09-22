# Accountancy Practice

*Not legal, tax, accounting or insurance advice — including about your own practice.
**Every number in `practice.json` is invented** — a worked example so the gates have
something to run against, not a benchmark. Run
[Stage 0](../../prompts/stage-0-practice-config.md) and replace all of them.*

## Shape of the practice

Recurring compliance work with an advisory layer on top. The most retainer-shaped of the
five verticals, and the one where `services_retainer_design_and_ceiling.md` does the most
work: compliance fees are fixed and predictable, while advisory questions arrive without
a ceiling and get absorbed.

Overrun is low (0.08) on compliance and misleadingly so — the variance lives in the
clean-up work that precedes a first year's filing. Concentration limit is the lowest of
the set (30%) because a small book concentrates quickly.

**Where the money leaks:** unbilled advisory inside a compliance retainer, first-year
clean-up quoted as though the records were in order, and deadline compression the client
caused and you absorb.

## Deliverable writer

`domain-professional-writing/domain-specific/domain_writing_cpa_tax_strategy.md` — the
advisory deliverable. Stage 5 assembles the engagement proposal; that prompt writes the
strategy document inside it.

## Trade-specific disqualifiers

| Signal | Tier | Why |
|---|---|---|
| `records_not_reconcilable` | **decline** | Taking on a client whose prior-year position cannot be reconciled, without funded clean-up, means owning someone else's problem at your own cost — and potentially attesting to something you cannot support |
| `deadline_inside_lead_time` | proceed with protection | Accept only with a written acknowledgement of late-filing risk and who bears any penalty. Absorbing a deadline the client caused sets the pattern for the whole relationship |

## Gate A — what must be in scope

- **Which filings and which periods**, named explicitly
- Whether bookkeeping is in scope or the client provides reconciled records
- **First-year clean-up: scoped and priced separately**, or explicitly excluded. This is
  the single most common scoping failure in the trade
- What advisory is included in a compliance retainer, and what is chargeable — with a
  ceiling, per `services_retainer_design_and_ceiling.md`
- Client-provided information: what, by when, and the consequence if late. Gate A already
  requires an `if_late` consequence; here it wants to be a real one, because late records
  are the norm rather than the exception
- Who is responsible for filing, and who signs
- Whether representation in an enquiry or audit is in scope

## Gate B — clauses that bite here

| Clause | Why it matters in this trade | Review with |
|---|---|---|
| **Reliance by third parties** | A bank or purchaser relying on work prepared for the client extends your exposure to someone you never contracted with. Disclaim it expressly | `legal_contract_clause_redline_targeted.md` |
| **Liability cap against fee** | A cap at a multiple of a modest compliance fee against a potential tax exposure is a large asymmetry. Check it is there and that it holds | `legal_contract_clause_redline_targeted.md` |
| **Scope of reliance on client information** | State that you have not audited what you were given, unless you have | `legal_contract_clause_redline_targeted.md` |
| **Payment terms and lien on records** | Whether you may retain records against unpaid fees is jurisdiction-specific and frequently constrained by professional rules — do not assume | `legal_payment_terms_and_late_fee_review.md` |
| **Disengagement** | How the engagement ends, what you hand over, and by when. The most-used clause in the trade | `legal_termination_economics_provider_side.md` |

The engagement letter is a regulated document in most jurisdictions with professional-body
requirements on content. `domain-legal/client-intake-communications/legal_engagement_letter_drafter.md`
drafts it; your professional body's requirements override anything here.

## Invoicing notes

- **Compliance fee invoiced in advance** of the period, per Stage 8's retainer guidance —
  advisory billed as consumed against the stated ceiling
- Advisory time captured **when it happens**. Absorbed advisory is the trade's largest
  unbilled category, and Stage 9's `unbilled_days` is where it becomes visible
- Deadline-driven work has a natural collection rhythm: invoice at filing, not after
- The collections ladder needs care. Professional-conduct rules may constrain what you
  may withhold, so check before relying on rung 4's suspension right
