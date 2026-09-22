---
title: "Collections Escalation Ladder"
category: accounting-controllership/order-to-cash
description: "A staged escalation path for an unpaid services invoice — from AP confirmation through sponsor escalation, work suspension, formal notice and handoff to a demand letter — with the trigger, message and relationship cost of each rung, and the rule that no rung is skipped or repeated"
techniques:
  - ST-02
  - QA-08
  - CM-09
  - OC-03
  - DD-06
difficulty: intermediate
tags:
  - services-practice
  - collections
  - escalation
  - unpaid-invoice
  - cash-collection
  - consulting
  - solo-operator
updated: "2026-09-21"
---

# Collections Escalation Ladder

**Objective:** Execute a staged escalation on an unpaid invoice, one rung at a time,
where each rung has a **trigger**, a **message**, a **relationship cost**, and a
**next-rung condition**. The discipline is that rungs are neither skipped nor
repeated: repeating a rung teaches the client the deadline is soft, and skipping one
burns relationship capital that was not yet necessary to spend.

**When to Use:** Use once `finance_receivables_aging_triage.md` has established the
cause. The ladder assumes an administrative or distress cause and a client who is
not disputing the work. **If the cause is dispute, do not start this ladder** —
resolve the substance first; escalating a disputed invoice hardens the dispute and
stalls the undisputed portion.

Nothing comparable exists in this repository. The nearest,
`domain-agentic-resources/skills/marketing/churn-prevention/references/dunning-playbook.md`,
is automated card-failure dunning for subscription software: no human relationship,
no contract, no suspension rights.

**Scope note.** The small-practice exception to this domain's institution-grade
framing, following `../tax-planning/solo_dev_tax_strategy.md`.

---

## Context Gathering

1. **The invoice** — amount, issue and due dates, days overdue, what it covers,
   whether the work was accepted.
2. **The contact record** — every approach made, with dates, channels, people and
   what was said. The ladder's position depends on this; guessing restarts it.
3. **The contract** — payment terms, late-payment interest, suspension rights,
   dispute-resolution clause, governing law, any personal guarantee.
4. **The relationship** — is work ongoing, is there pipeline, who is the sponsor as
   distinct from the approver, would you want this client again.
5. **The stakes** — the amount against your runway, and whether anything you owe is
   waiting on it.

---

## Method

### The ladder

Work down. Each rung states the trigger, the action, the tone and the cost.

**Rung 1 — AP confirmation.** *Trigger: due date + 3 days.*
Direct contact with the accounts-payable function, not the sponsor. Confirm the
invoice was received, is approved, is against a valid PO, and which payment run it is
in. Tone: administrative and neutral — you are checking your own records.
*Relationship cost: none.* This resolves the majority of overdue services invoices.

**Rung 2 — Written follow-up with the evidence.** *Trigger: no resolution at +14 days.*
Email to AP, sponsor copied, re-attaching the invoice and its evidence pack. State
the amount, the due date, the days overdue, and a specific requested payment date.
Ask one direct question: is there anything preventing payment? Tone: helpful, clear.
*Cost: negligible.*

**Rung 3 — Sponsor escalation.** *Trigger: no substantive response at +30 days.*
Direct to the sponsor — the person who wanted the work — not to AP. Frame it as
needing their help to unblock an internal process, not as an accusation. This is the
first rung with a real relationship cost, because you are asking them to spend
internal capital. Name the specific help required: approve it, or tell you who can.
*Cost: low, but it is now a favour asked.*

**Rung 4 — Notice of suspension.** *Trigger: no payment at +45 days, and work is
ongoing.*
Written notice that work will pause on a stated date unless payment is received,
citing the contractual right if one exists. Only issue this if you have checked the
right and will actually do it — see
`../../domain-legal/contracts-transactional/legal_payment_terms_and_late_fee_review.md`.
*Cost: material. It changes the relationship.* But continuing to deliver into an
unpaid account converts a collection problem into a larger one.

**Rung 5 — Suspension, executed.** *Trigger: the stated date passes.*
Stop. Confirm in writing, neutrally, with what is required to resume. An announced
suspension not carried out destroys every subsequent deadline you set.
*Cost: high. Proceed only if rung 4's notice was issued and the date has passed.*

**Rung 6 — Formal notice before action.** *Trigger: no payment at +60 to +75 days.*
A formal letter stating the debt, the contractual basis, any interest claimed, a
final deadline, and the intended next step. In several jurisdictions a pre-action
protocol governs the form and timing; this is the point to take advice.
*Cost: the commercial relationship is over.*

**Rung 7 — Handoff.** *Trigger: final deadline passes.*
Hand to `../../domain-legal/client-intake-communications/legal_demand_letter_drafter.md`
and take legal advice, or pass to a collections agency, or make a commercial decision
to write off. Writing off is a legitimate rung: a debt whose recovery cost exceeds
its value, or whose pursuit would consume capacity better spent on new work, is
sometimes correctly abandoned. Decide deliberately and record it.

### The rules

1. **One rung at a time.** Each requires its trigger to have been met.
2. **Never repeat a rung.** A second copy of the same email resets the clock and
   signals that nothing follows. If a rung produced no result, go to the next.
3. **Never threaten a step you will not take.** The most expensive error available:
   it converts every future deadline into a suggestion.
4. **Every rung in writing, or followed by written confirmation.** A call is fine;
   an unrecorded call is not.
5. **Stop the ladder if a dispute emerges.** Return to triage. The cause has changed.
6. **Accelerate on distress signals.** Where triage indicates distress, compress the
   triggers — the queue of creditors forms quickly and position matters.
7. **Payment plans are a branch, not a rung.** If offered a plan, get it in writing
   with dates and amounts, and restart the ladder at rung 2 from the first missed
   instalment.

### Tone, across every rung

Neutral, specific, factual. State the amount, the date, the ask. Do not apologise for
requesting payment for work delivered, and do not express anger. The practitioners
who collect best are consistently unembarrassed and consistently procedural — the
invoice is simply due.

---

## Output Format

```markdown
## Collections — [client], invoice [#]

**Amount:** [x] · **Due:** [date] · **Overdue:** [n] days
**Cause (from triage):** [administrative / distress] · **Work ongoing:** [y/n]
**Contractual rights:** interest [y/n] · suspension [y/n, notice period] · governing law [x]

### Contact history
| Date | Rung | Channel | Who | Outcome |
|---|---|---|---|---|

**Current rung: [n]** · **Next trigger: [date]**

### Next action
**Rung [n+1] — [name]**
- To: [person, role]
- Channel: [x]
- Trigger met: [evidence]
- Message:
  > [drafted text]
- Relationship cost: [x]
- If no response by [date] → rung [n+2]

### Stop conditions
- Dispute raised → return to `finance_receivables_aging_triage.md`
- Payment plan offered → document, restart at rung 2 on first miss
- Distress signals → compress triggers to [x]

### Write-off assessment
| | |
|---|---|
| Amount | |
| Estimated recovery cost | |
| Estimated probability | |
| Capacity cost of pursuit | |
| **Recommendation** | [pursue / plan / write off] |
```

---

## Verification

- [ ] The current rung is established from the recorded contact history, not assumed.
- [ ] The cause is administrative or distress — not dispute.
- [ ] Every trigger condition is met before the rung fires.
- [ ] No rung is repeated.
- [ ] Suspension is only threatened where the contractual right has been checked and
      you will execute it.
- [ ] Every rung is written or confirmed in writing.
- [ ] The drafted message states amount, date and a specific ask, with no apology and
      no anger.

**False-positive prevention.** The most common and most costly failure is staying on
rung 2 indefinitely — sending the same polite reminder monthly. It feels like action
and is the reason invoices reach 120 days. If a rung has fired and produced nothing
by its next trigger, escalate. The ladder only works as a ladder.

The second is skipping to rung 4 or 6 out of frustration on an invoice whose cause
was never diagnosed. Roughly half of overdue services invoices are administrative and
resolve at rung 1. Escalating one of those to a suspension notice costs a client
relationship over a missing PO number.

The third is treating write-off as failure. It is rung 7's legitimate branch. A
£2,000 debt pursued through a legal process that costs £1,500 and three weeks of
attention is a worse outcome than a recorded write-off and three weeks of business
development.

**This is not legal advice.** Pre-action protocols, statutory interest entitlement,
suspension rights and limitation periods vary by jurisdiction and contract. Take
advice before rung 6, and certainly before rung 7.

---

## Related

- `finance_receivables_aging_triage.md` — establishing the cause before starting
- `finance_services_invoice_schedule_builder.md` — preventing the administrative causes
- `../../domain-legal/contracts-transactional/legal_payment_terms_and_late_fee_review.md` — the rights this ladder relies on
- `../../domain-legal/client-intake-communications/legal_demand_letter_drafter.md` — rung 7
- `../../domain-negotiation/channels/negotiation_written_async_message.md` — tone on the harder rungs
