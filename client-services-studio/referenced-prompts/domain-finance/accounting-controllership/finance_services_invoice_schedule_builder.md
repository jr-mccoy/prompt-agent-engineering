---
title: "Services Invoice Schedule Builder"
category: accounting-controllership/order-to-cash
description: "Turn a signed statement of work into an invoice schedule that survives the client's accounts-payable review — milestone triggers tied to acceptance rather than activity, the evidence pack each invoice needs, purchase-order and approval routing, and the terms that decide when cash actually arrives"
techniques:
  - CM-02
  - ST-02
  - OC-03
  - QA-08
  - NE-03
difficulty: intermediate
tags:
  - services-practice
  - invoicing
  - order-to-cash
  - milestone-billing
  - accounts-payable
  - consulting
  - solo-operator
updated: "2026-09-21"
---

# Services Invoice Schedule Builder

**Objective:** Convert a signed scope of work into an **invoice schedule**: what is
billed, on what trigger, with what supporting evidence, routed to whom, under what
terms. The output is designed against the client's accounts-payable process rather
than against your own convenience, because that process is what determines when cash
arrives.

**When to Use:** Use immediately after signature and before the first invoice. Also
use when an existing client pays reliably late — the cause is frequently an invoice
that does not match what their AP function needs, not unwillingness to pay.

This is **distinct from** `domain-agentic-resources/skills/payments/billing-automation/`
and `stripe-integration/`, which are engineering skills for implementing subscription
billing in software. This is a services practice raising invoices against a statement
of work. It is also the inverse of
`../../domain-legal/in-house-legalops/legal_legal_spend_anomaly_analyzer.md`, which
scrutinises *received* professional-services invoices — read that one to understand
what a client's reviewer will look for, then build invoices that survive it.

**Scope note.** Following `../tax-planning/solo_dev_tax_strategy.md` and
`../personal-finance-planning/solo_dev_financial_planning.md`, this is the
small-practice exception to this domain's institution-grade framing.

---

## Context Gathering

1. **The scope**
   - "Deliverables, milestones and acceptance criteria as written in the SOW."
   - "Total fee and structure — fixed, milestone, day rate, retainer?"
   - "Expenses: reimbursable, capped, or included?"

2. **The client's machinery** — the decisive section:
   - "Is there a purchase order? What number, what value, what period?"
   - "Who approves the invoice — the sponsor, or a separate budget holder?"
   - "Is there a portal, or does it go by email? To whom exactly?"
   - "Payment run frequency — weekly, fortnightly, monthly, and on which day?"
   - "Is there a cut-off for inclusion in the next run?"
   - "What must appear on the invoice: PO number, cost centre, project code, contact?"

3. **The terms**
   - "Contractual payment terms, and what they actually pay in practice."
   - "Late-payment interest or fees agreed?"
   - "Anything conditioning payment on acceptance, and who signs acceptance?"

The payment-run question is the one that converts theory into a date. Net-30 terms
with a monthly payment run on the 25th and a 10-day cut-off means an invoice issued
on the 16th is paid roughly 40 days later, not 30. Building the schedule around the
run is the difference between a forecast and a guess.

---

## Method

### Step 1 — Tie every trigger to acceptance, not activity

Each invoice line needs a trigger that is observable by both parties and not
arguable. Ranked by collection reliability:

| Trigger | Reliability | Note |
|---|---|---|
| Deposit on signature | Highest | No delivery risk at all |
| Milestone acceptance against written criteria | High | Requires the criteria to exist |
| Milestone delivery | Medium | Client may dispute completeness |
| Calendar date | Medium | Clean, but invites "what did we get?" |
| Time elapsed / hours worked | Lower | Invites line-by-line review |
| Project completion | Lowest | All risk carried to the end |

Where acceptance criteria are vague, fix that before building the schedule — use
`../../domain-engineering-workflows/workflows/workflow_definition_of_done_builder.md`
to convert fuzzy deliverables into testable conditions. A milestone that cannot be
objectively judged complete is a payment that can be deferred indefinitely.

### Step 2 — Front-load deliberately

Structure so that cash collected stays ahead of cost incurred. Conventional and
defensible for a small practice:

- Deposit of 25–50% on signature, before work begins
- Progress payments at real milestones
- A final payment of no more than 15–25% on completion

The final tranche is the one at risk: it is due exactly when your leverage is lowest,
because the work is delivered. Keeping it small is worth more than an extra clause.

For retainers, invoice **in advance** of the period, not in arrears. For day-rate
work, invoice at a stated cadence with a stated cut-off rather than at the end.

### Step 3 — Build the evidence pack per line

Each invoice needs the evidence its reviewer requires, attached at issue rather than
supplied on request. Every round-trip for documentation costs a payment run.

| Invoice type | Evidence |
|---|---|
| Milestone | Acceptance confirmation, deliverable reference, SOW clause |
| Time-based | Timesheet at the agreed granularity, approver name |
| Expenses | Receipts, policy reference, prior approval where required |
| Retainer | Period covered, consumption against ceiling |

State granularity explicitly. A client who requires daily narrative entries and
receives a monthly total will not pay until it is re-cut.

### Step 4 — Route it correctly

Record, as a checklist the invoice must satisfy:

- PO number, and whether remaining PO value covers this invoice
- Cost centre or project code
- Named approver and their AP contact
- Submission channel — portal, email address, both
- The client's own reference format if they require one

A missing PO number is the single most common cause of a services invoice sitting
unpaid without anyone raising an objection: it is rejected silently at intake.

### Step 5 — Project the cash dates

For each line compute:

```
Trigger date → issue date → approval window → next payment run → expected receipt
```

Then compare against the practice's own commitments — subcontractor payments in
particular (see `../corporate-finance-fpa/finance_subcontractor_margin_model.md`).
A schedule that is profitable but pays out before it collects is a working-capital
problem wearing a margin's clothing.

### Step 6 — Pre-agree the mechanics

Before the first invoice, confirm in writing with the client: the approver, the
submission route, the PO position, the evidence format, and the payment-run calendar.
Ten minutes here removes the most common causes of a 60-day delay, and it is far
easier to ask before an invoice is overdue than after.

---

## Output Format

```markdown
## Invoice schedule — [client], [engagement]

**Total fee:** [x] · **Structure:** [x] · **Terms:** [net-x] · **PO:** [number / none]

### Schedule
| # | Amount | Trigger | Evidence required | Issue date | Expected receipt |
|---|---|---|---|---|---|

**Cash ahead of cost?** [yes / no — peak negative position of [x] in [period]]

### Routing checklist (every invoice)
- [ ] PO number [x] — remaining value [x], covers through invoice [#]
- [ ] Cost centre / project code: [x]
- [ ] Approver: [name, role] · AP contact: [name]
- [ ] Channel: [portal / email]
- [ ] Reference format: [x]

### Client payment machinery
| | |
|---|---|
| Payment run | [frequency, day] |
| Cut-off | [days before run] |
| Contractual terms | |
| Observed behaviour | |
| **Effective days to cash** | |

### Pre-agreed with client on [date] by [email / call]
- [ ] Approver confirmed
- [ ] Evidence format confirmed
- [ ] PO covers full engagement value
- [ ] Payment-run calendar confirmed

### Escalation
First follow-up at [x] days · Ladder: `finance_collections_escalation_ladder.md`
```

---

## Verification

- [ ] Every trigger is objectively observable by both parties.
- [ ] Milestone triggers reference written acceptance criteria that exist.
- [ ] A deposit or advance payment is present unless deliberately waived.
- [ ] Final payment is no more than 25% of total.
- [ ] Expected receipt dates use the payment-run calendar, not contractual terms.
- [ ] PO value is confirmed to cover the full engagement, not just the first invoice.
- [ ] Cash-ahead-of-cost is checked where subcontractors are involved.

**False-positive prevention.** The dominant failure is a schedule built on
contractual payment terms. Net-30 is a ceiling on the client's obligation, not a
prediction. Always derive the date from the payment run and the approval window, and
where observed behaviour differs from contract, forecast on behaviour.

The second failure is milestones invented for billing convenience — "50% at
mid-point" where no deliverable lands at the mid-point. These invite a dispute at
exactly the moment the client is deciding whether to continue. Bill against something
that arrives.

The third is assuming a PO covers the engagement because one exists. POs are raised
for a value and a period; work continuing past either stops being payable until a new
one is raised, and nobody will tell you.

**This is not accounting or tax advice.** Revenue recognition, VAT or sales-tax
treatment and invoice content requirements are jurisdiction-specific. Confirm with an
accountant. For revenue-recognition treatment of milestone billing see
`finance_revenue_recognition_asc606_memo.md`.

---

## Related

- `finance_receivables_aging_triage.md` — when invoices are not paid on schedule
- `finance_collections_escalation_ladder.md` — the escalation path
- `../../domain-legal/contracts-transactional/legal_payment_terms_and_late_fee_review.md` — the contractual terms behind this
- `../../domain-engineering-workflows/workflows/workflow_definition_of_done_builder.md` — making milestone triggers objective
- `../../domain-legal/in-house-legalops/legal_legal_spend_anomaly_analyzer.md` — what the client's reviewer looks for
