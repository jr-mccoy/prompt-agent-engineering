---
title: "Receivables Aging Triage"
category: accounting-controllership/order-to-cash
description: "Triage an overdue receivables ledger for a services practice — separating administrative blockage from dispute from distress from refusal, because each has a different remedy — and convert the ledger into a prioritized action list with an exposure figure and a provisioning decision"
techniques:
  - RT-10
  - RT-05
  - OC-03
  - QA-08
  - CM-02
difficulty: intermediate
tags:
  - services-practice
  - receivables
  - aging
  - dso
  - cash-collection
  - consulting
  - solo-operator
updated: "2026-09-21"
---

# Receivables Aging Triage

**Objective:** Turn a list of overdue invoices into a **diagnosis and an action
list**. Each overdue invoice has one of four causes, and the remedy differs
completely; treating them all as "chasing" wastes the recoverable ones and delays the
distressed ones. Output: cause per invoice, prioritised actions, total exposure, and
a provisioning decision.

**When to Use:** Use monthly, and immediately whenever a single receivable becomes
material relative to your reserves. Run it before escalating anything — the
escalation ladder in `finance_collections_escalation_ladder.md` assumes you already
know which of the four causes you are dealing with.

This is **distinct from** `../financial-statement-analysis/finance_working_capital_analysis.md`,
which analyses DSO and the cash conversion cycle for an institution as a balance-sheet
efficiency question. This is operational triage for a practice where two unpaid
invoices can be an existential cash event rather than a metric. It is also distinct
from `domain-agentic-resources/skills/marketing/churn-prevention/references/dunning-playbook.md`,
which handles failed-card dunning in subscription software.

**Scope note.** The small-practice exception to this domain's institution-grade
framing, following `../tax-planning/solo_dev_tax_strategy.md`.

---

## Context Gathering

1. **The ledger** — per overdue invoice:
   - "Client, amount, issue date, due date, days overdue."
   - "What it was for, and whether the work was accepted."
   - "Every contact made about it: date, channel, who, what they said."

2. **The relationship**
   - "Is work ongoing with this client, or is the engagement finished?"
   - "Is there more work in the pipeline with them?"
   - "Is the invoice approver the same person as your sponsor?"

3. **Your position**
   - "Cash on hand, and committed outgoings in the next 60 days."
   - "Is anything you owe — subcontractors especially — waiting on this?"
   - "What are the contractual terms: interest, suspension rights, notice?"

4. **Signals**
   - "Have they gone quiet, or are they responsive but not paying?"
   - "Any news — funding, layoffs, restructuring, leadership change?"
   - "Are other suppliers being paid?"

The responsive-but-not-paying versus gone-quiet distinction is the most diagnostic
single signal available, and it costs nothing to observe.

---

## Method

### Step 1 — Classify each invoice into one of four causes

This is the core of the prompt. The four causes look identical on an aging report and
require opposite responses.

| Cause | Signals | Remedy | Wrong response |
|---|---|---|---|
| **Administrative** | Responsive; "it's in the system"; PO missing, approver away, wrong format, missed cut-off | Fix the document or route it. One phone call to AP usually resolves it | Escalating to the sponsor — annoys the person who will pay you |
| **Dispute** | Responsive; questions the work, the amount, or the scope | Resolve the substance. Separate the disputed portion and collect the rest | Chasing payment — hardens the position and stalls the undisputed amount |
| **Distress** | Slow, evasive, partial payments, other suppliers unpaid, adverse news | Move fast and rank early. Payment plan in writing; secure a position now | Waiting politely — the queue forms in front of you |
| **Refusal** | Clear, deliberate, sometimes silent after a decision | Legal path. Stop work; preserve evidence | More reminders — signals the deadline is soft |

Do not assign a cause without evidence. Where evidence is absent, the first action is
diagnostic: one direct call to the AP contact, which resolves the administrative
majority immediately and reveals the others.

### Step 2 — Age it, but do not trust age alone

Bucket at 1–30, 31–60, 61–90, and 90+ days overdue, measured from the due date. Age
correlates with recoverability but does not determine it: a 75-day administrative
blockage is more recoverable than a 20-day dispute. Use age to prioritise within a
cause, not across causes.

Note also that collection probability falls sharply with age, and steeply past 90
days. This is why the distress classification matters most — it is the one where
delay is expensive.

### Step 3 — Compute exposure and concentration

```
Total overdue
Overdue as % of the last three months' revenue
Largest single overdue amount
Overdue concentrated in one client?  [yes/no]
Days of your own runway covered by the overdue total
Anything you owe that is waiting on this?  [amount]
```

The last two lines convert an accounting exercise into a decision about your own
solvency. If overdue receivables exceed a month of your costs, this stops being an
admin task and becomes the priority.

### Step 4 — Decide about ongoing work

For each client with overdue invoices where work continues, answer explicitly:

- Does the contract give a **right to suspend** for non-payment, and on what notice?
  Check `../../domain-legal/contracts-transactional/legal_payment_terms_and_late_fee_review.md`.
- Does continuing increase exposure? By how much per week?
- Would suspension damage a relationship worth more than the exposure?

Continuing to deliver into an unpaid account is a financing decision. Make it
deliberately, with a stated ceiling, rather than by default.

### Step 5 — Prioritise into an action list

Rank by `amount × recoverability × urgency`, then write the specific next action for
each — not "chase," but the named person, channel, message and date. Where a cause
warrants escalation, hand off to the ladder.

### Step 6 — Provision honestly

For each invoice give a recoverability estimate, and state which you would write down
now. Practices systematically carry bad receivables at full value, which flatters
both cash forecasts and the sense of how the year is going. An honest provision makes
the pipeline decision clearer.

---

## Output Format

```markdown
## Receivables triage — [date]

### Ledger
| Invoice | Client | Amount | Days overdue | Bucket | Cause | Evidence | Recoverability |
|---|---|---|---|---|---|---|---|

### Exposure
| | |
|---|---|
| Total overdue | |
| As % of last 3 months' revenue | |
| Largest single | |
| Concentrated in one client? | |
| Days of runway covered | |
| Owed onward, waiting on this | |

### By cause
| Cause | Count | Amount | Typical remedy |
|---|---|---|---|

### Actions, prioritised
| # | Invoice | Action (who, channel, message) | By when | Then |
|---|---|---|---|---|

### Ongoing work decisions
| Client | Overdue | Work continuing? | Right to suspend | Exposure per week | Decision |
|---|---|---|---|---|---|

### Provision
| Invoice | Carried at | Recommended provision | Rationale |
|---|---|---|---|
```

---

## Verification

- [ ] Every invoice has a cause, and each cause is supported by named evidence.
- [ ] No invoice is classified as refusal without something explicit; silence alone
      is usually distress or administrative.
- [ ] Disputed invoices have the undisputed portion separated for collection.
- [ ] Exposure is expressed against your own runway, not only in absolute terms.
- [ ] Ongoing-work decisions are explicit, with a stated exposure ceiling.
- [ ] Actions name a person and a date; none says only "follow up."

**False-positive prevention.** The dominant failure is classifying everything as
administrative because that is the comfortable interpretation and the one that avoids
a difficult conversation. Test it: if two direct contacts with the AP function have
not resolved it, it is not administrative. Reclassify.

The opposite failure is reading ordinary slowness as distress and escalating hard
into a client who was simply between payment runs. Distress requires corroborating
signals beyond slowness — partial payments, other suppliers unpaid, adverse news,
evasiveness. One late invoice is not a signal.

The third is triaging the ledger without checking what you owe against it. A
receivable that is funding a subcontractor payment due next week has a different
urgency from one that is not, and the aging report does not show that.

**This is not legal or accounting advice.** Provisioning treatment, interest
entitlement and suspension rights are jurisdiction- and contract-specific. Confirm
with an accountant and, before any legal step, a lawyer.

---

## Related

- `finance_collections_escalation_ladder.md` — the escalation path once a cause is established
- `finance_services_invoice_schedule_builder.md` — preventing administrative causes at source
- `../../domain-legal/contracts-transactional/legal_payment_terms_and_late_fee_review.md` — suspension and interest rights
- `../../domain-business-strategy/client-services/services_client_concentration_risk_check.md` — where overdue amounts concentrate in one client
- `../financial-statement-analysis/finance_working_capital_analysis.md` — the institutional DSO view
