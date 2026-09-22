---
name: collect
description: Build the invoice schedule, age the overdue ledger, and name the next collections escalation rung. Use this command when setting up billing on a signed engagement, when reviewing receivables monthly, or when an invoice is overdue and you need to know what to do next. Projects cash dates from the client's payment run rather than contractual terms, and refuses to escalate a disputed or undiagnosed invoice.
version: "1.0.0"
category: orchestration
tags: [client-services, invoicing, receivables, collections, cash-flow, consulting]
agents_used: [engagement-orchestrator]
---

# /collect — Stage 8

*Not legal, tax, or accounting advice. Rungs 6 and 7 involve formal notice and legal
process — take advice first.*

Runs [`prompts/stage-8-invoice-and-collections.md`](../prompts/stage-8-invoice-and-collections.md).

## What it does

**Setting up:**
```bash
python3 skills/receivables-tracker/scripts/receivables.py --schedule <engagement.json>
```
Projects each payment's cash date from the payment run and approval window, and warns
on a final tranche above 25%, a missing deposit, and a required-but-unrecorded PO.

**Reviewing:**
```bash
python3 skills/receivables-tracker/scripts/receivables.py --age <ledger.json>
```
Buckets overdue invoices, expresses exposure against your own monthly cost, and lists
anything undiagnosed.

**Escalating:**
```bash
python3 skills/receivables-tracker/scripts/receivables.py --rung <invoice.json>
```
Names the next rung — or refuses. A dispute is never escalated. An undiagnosed
invoice goes back to triage. A rung is never repeated. Suspension is not proposed
without a contractual right and ongoing work. Distress compresses every trigger by
half.

## Notes

Roughly half of overdue services invoices are administrative and resolve at rung 1,
with one call to accounts payable. Escalating one of those to the sponsor costs
goodwill over a missing PO number.

Staying on rung 2 indefinitely is the most common reason invoices reach 120 days.
