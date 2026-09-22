---
name: receivables-tracker
description: Build the invoice schedule, age the overdue ledger, and name the next collections escalation rung for a services practice. Use this skill to "when will I actually get paid", "build the invoice schedule", "age my receivables", "which invoices should I chase", "what do I do about this unpaid invoice", or "should I escalate". Projects cash dates from the client's payment run rather than contractual terms, buckets overdue invoices with exposure expressed against your own runway, triages by cause, and walks a seven-rung escalation ladder that never repeats a rung and refuses to escalate a dispute.
license: MIT
compatibility: Standard library only, Python 3.9+. `scripts/receivables.py` implements schedule projection, aging with cause triage, and the escalation ladder; `--self-check` proves the payment run pushes cash later than contractual terms, that not-yet-due invoices are excluded from aging, that a dispute is refused escalation, that rungs are never repeated, that suspension is not proposed without a contractual right or ongoing work, and that distress compresses the triggers. No dependencies, no network, no writes.
metadata:
  tags: [client-services, invoicing, receivables, collections, escalation, cash-flow, consulting]
  updated: "2026-09-21"
---

# Receivables Tracker

## Purpose

Getting paid is a process, and services practices routinely treat it as an
afterthought — which is why the median services invoice is paid late and the
median response is the same polite reminder, monthly, forever.

**Schedule.** Projects each payment's cash date from the client's payment run and
approval window, not from the contractual terms. Net-30 is a ceiling on the
client's obligation, not a prediction: with a monthly run on the 25th and a 10-day
cut-off, a net-30 invoice issued on the 16th arrives around day 40. The schedule
also warns when the final payment exceeds 25% of the total, when there is no
deposit, and when a PO is required but not recorded — the last being the most
common cause of an invoice that is rejected silently at intake.

**Age.** Buckets overdue invoices at 1–30 / 31–60 / 61–90 / 90+, and expresses the
total against your own monthly cost, because a services practice's receivables
question is a solvency question rather than a metric. Invoices with no recorded
cause are listed as undiagnosed.

**Rung.** Given a cause and a contact history, names the next escalation rung. The
ladder enforces its own rules in code: a **dispute is never escalated** (resolve
the substance first — escalating hardens the position and stalls the undisputed
portion); an undiagnosed invoice is sent back for triage; a rung fires only when
its trigger is met; **a rung is never repeated**; suspension is not proposed where
there is no contractual right or the work has already finished; and a distress
cause compresses every trigger by half.

The four causes — administrative, dispute, distress, refusal — look identical on
an aging report and have opposite remedies. Roughly half of overdue services
invoices are administrative and resolve at rung 1.

## When to Use This Skill

- A SOW has been signed and the invoice schedule is being set up
- Monthly, to age the ledger
- An invoice is overdue and you are deciding what to do next

## Usage

```bash
python scripts/receivables.py --schedule engagement.json
python scripts/receivables.py --age ledger.json
python scripts/receivables.py --rung invoice.json
python scripts/receivables.py --self-check
```

## Boundaries

- **Not legal or accounting advice.** Rungs 6 and 7 involve formal notice and legal
  process; take advice before either. Interest entitlement, suspension rights and
  limitation periods are jurisdiction-specific.
- **Never threaten a rung you will not execute.** The script will not propose
  suspension without a recorded contractual right, and you should not either.
- See [`references/ladder.md`](references/ladder.md) for the full ladder with
  triggers and relationship costs.
