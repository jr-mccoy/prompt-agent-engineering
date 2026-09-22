# Stage 8 — Invoice and Collect

**Gate: none.** The escalation ladder enforces its own rules in code.

**Input:** the signed engagement · **Output:** an invoice schedule, and collection
actions

---

## Purpose

Getting paid is a process. Most services practices treat it as an afterthought, which
is why the median services invoice is paid late and the median response is the same
polite reminder, monthly, forever.

## Set up the schedule

### 1. Project cash dates from the payment run

```bash
python3 skills/receivables-tracker/scripts/receivables.py --schedule <engagement.json>
```

Net-30 is a ceiling on the client's obligation, not a prediction. The date that
matters is the first payment run after the approval window closes. With a monthly run
on the 25th and a 10-day cut-off, a net-30 invoice issued on the 16th arrives around
day 40.

The `payment_machinery` block comes from the discovery call (Stage 2). If it is
empty, ask now — before the first invoice, when the question is administrative rather
than loaded.

### 2. Act on the warnings

| Warning | Fix |
|---|---|
| Final payment above 25% of total | Restructure. It falls due when your leverage is lowest |
| No deposit | Add one, or accept the delivery risk deliberately |
| PO required but not recorded | Get it. A missing PO number is the most common cause of an invoice rejected silently at intake |

### 3. Pre-agree the mechanics in writing

Confirm with the client before the first invoice: approver, submission route, PO
position and remaining value, evidence format, payment-run calendar. Ten minutes
here removes the most common causes of a 60-day delay.

### 4. Build the evidence pack

Attach at issue, not on request — every round-trip for documentation costs a payment
run. What each invoice type needs is in
`domain-finance/accounting-controllership/finance_services_invoice_schedule_builder.md`.

Read `domain-legal/in-house-legalops/legal_legal_spend_anomaly_analyzer.md` as the
inverse model: it is what a client's reviewer looks for in a received
professional-services invoice. Build invoices that survive it.

## When an invoice goes overdue

### 5. Age the ledger and diagnose the cause

```bash
python3 skills/receivables-tracker/scripts/receivables.py --age <ledger.json>
```

Four causes, identical on an aging report, opposite remedies:

| Cause | Remedy | Wrong response |
|---|---|---|
| **Administrative** | Fix the document or route. Usually one call to AP | Escalating to the sponsor |
| **Dispute** | Resolve the substance; collect the undisputed portion separately | Chasing payment |
| **Distress** | Move fast, rank early, get a written payment plan | Waiting politely |
| **Refusal** | Legal path. Stop work; preserve evidence | More reminders |

Roughly half are administrative and resolve at rung 1. Invoices the tool lists as
`undiagnosed` are not ready to escalate — one direct call to AP resolves most of
them and reveals the rest.

Full method:
`domain-finance/accounting-controllership/finance_receivables_aging_triage.md`.

### 6. Name the next rung

```bash
python3 skills/receivables-tracker/scripts/receivables.py --rung <invoice.json>
```

The ladder enforces in code what practices fail to enforce by intention: a dispute is
never escalated, a rung fires only when its trigger is met, **a rung is never
repeated**, suspension is not proposed without a contractual right or ongoing work,
and distress compresses every trigger by half.

Staying on rung 2 indefinitely is the single most common reason invoices reach 120
days. It feels like action. It is not.

The ladder, with triggers and relationship costs:
`skills/receivables-tracker/references/ladder.md`. The method:
`domain-finance/accounting-controllership/finance_collections_escalation_ladder.md`.

### 7. Decide about ongoing work

Continuing to deliver into an unpaid account is a financing decision. Make it
deliberately with a stated ceiling. Check your suspension right first —
`domain-legal/contracts-transactional/legal_payment_terms_and_late_fee_review.md` —
and never announce a suspension you will not execute.

## Verification

- [ ] Cash dates projected from the payment run, not contractual terms
- [ ] Every schedule warning addressed
- [ ] Mechanics pre-agreed in writing before the first invoice
- [ ] Evidence attached at issue
- [ ] Every overdue invoice has a diagnosed cause before any escalation
- [ ] No rung repeated
- [ ] No suspension threatened without the right and the intention
- [ ] Ongoing-work decisions are explicit, with an exposure ceiling

## Boundaries

Not legal, tax or accounting advice. Rungs 6 and 7 involve formal notice and legal
process — take advice first. Interest entitlement, suspension rights and limitation
periods are jurisdiction-specific.
