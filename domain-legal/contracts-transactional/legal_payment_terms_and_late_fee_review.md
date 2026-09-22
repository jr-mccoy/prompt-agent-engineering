---
title: "Payment Terms and Late Fee Review — Supplier Side"
category: legal/contracts-transactional
description: "Review the payment architecture of a services agreement from the supplier's side: net terms and when the clock starts, invoice-approval and acceptance gates, milestone triggers, late-payment interest and its enforceability, suspension-of-work rights, retainage, set-off and disputed-amount handling."
techniques:
  - ST-02
  - ST-03
  - CM-02
  - QA-01
  - OC-03
difficulty: intermediate
tags:
  - legal
  - contracts
  - payment-terms
  - late-payment
  - suspension-of-work
  - retainage
  - supplier-side
updated: "2026-09-21"
related_prompts:
  - domain-legal/contracts-transactional/legal_contract_clause_redline_targeted.md
  - domain-legal/contracts-transactional/legal_contract_risk_heatmap.md
  - domain-legal/contracts-transactional/legal_sow_drafter.md
  - domain-legal/client-intake-communications/legal_demand_letter_drafter.md
---

**Purpose:** Review the **payment architecture** of a services agreement from the
supplier's side and produce clause-by-clause positions: when the payment clock
starts, what gates sit before it, whether late-payment interest is claimable and
enforceable, whether work may be suspended for non-payment, and how disputed amounts
and set-off are handled.

**When to use:** Before signing any services agreement or SOW where you are the
supplier, and when an existing client pays persistently late and you need to know
what rights you actually hold. Also use when drafting your own terms.

**Why this exists as a separate prompt.** `legal_contract_clause_redline_targeted.md`
covers the five highest-risk clause families — indemnity, limitation of liability, IP
ownership, warranties and termination — calibrated to buyer or supplier posture. It
does not cover payment mechanics, and `legal_contract_risk_heatmap.md` scores risk
without reaching the clause detail here. Payment terms are where a services supplier
most often loses money without ever losing an argument: the clauses are unglamorous,
rarely negotiated, and decisive for cash.

**This is not legal advice.** Statutory late-payment entitlements, the enforceability
of interest and penalty provisions, prompt-payment legislation and construction-style
retainage rules are all jurisdiction-specific and change. This produces positions and
questions for a lawyer, not conclusions. Have counsel review before signature.

---

## Inputs required

- The draft agreement and any SOW or order form
- Governing law and jurisdiction clauses
- Your standard terms, if you have any
- The client's actual payment behaviour, if this is an existing relationship
- Whether you subcontract any of the delivery, and on what payment terms

---

## Review sequence

Work through the eight areas in order. Each produces a **position ladder**: primary
ask, acceptable fallback, and walkaway.

### 1. When the clock starts

The single most consequential and least-read provision. Net-30 means nothing until
you know net-30 from *what*.

| Trigger | Supplier position |
|---|---|
| Invoice date | Best. Ask for this |
| Invoice receipt | Acceptable if receipt is deemed on sending |
| Invoice approval | Poor — approval is unbounded unless a deadline is attached |
| Acceptance of deliverable | Poor unless acceptance is deemed after N days of silence |
| Month-end following invoice | Common and quietly adds up to 30 days |

Flag any trigger that depends on a client action with no deadline attached. Where
approval or acceptance gates the clock, the fix is a **deemed** provision: approval
is deemed given if no written objection within N days.

### 2. The net period and the payment run

Record the contractual period, then ask whether the client's payment run makes it
achievable. A net-30 term with a monthly run and a cut-off can be a 45-day term in
practice. This is commercial rather than legal, but it belongs in the same review.

### 3. Invoice-approval and acceptance gates

Identify every gate between delivery and payability:

- Who approves, and is that person named?
- Is there a deadline for approval or objection?
- Is objection required to be in writing and reasoned?
- Is there a deemed-acceptance backstop?
- Does a PO requirement sit in front of everything, and who maintains the PO?

A PO requirement with no obligation on the client to keep the PO funded is a common
and severe defect: work continues, the PO is exhausted, and invoices are rejected at
intake with no breach by anyone.

### 4. Milestone and instalment triggers

Where payment is milestone-based, check each trigger is objectively determinable.
Triggers tied to "satisfactory completion" without criteria hand the client an
unreviewable discretion. Cross-reference the acceptance criteria in
`legal_sow_drafter.md`.

Check also whether any payment is contingent on something outside your control — a
third-party sign-off, a client's internal launch, another supplier's delivery. Those
are not milestones; they are conditions, and they belong in the risk register.

### 5. Late-payment interest

Determine, and flag for counsel:

- Is there a contractual interest rate? At what rate, simple or compound, from when?
- Does the agreement **exclude** a statutory entitlement that would otherwise apply?
  Many jurisdictions provide a statutory rate plus fixed recovery costs for
  commercial debts, and a contract term can sometimes displace or limit it — whether
  it validly does so is a question for counsel.
- Is the rate at risk of being construed as a penalty rather than a genuine
  pre-estimate or a permitted contractual rate?
- Are recovery costs — collection costs, legal fees — recoverable?

The practical point: an interest clause is rarely enforced, and it is still worth
having, because it changes the conversation at the collections stage. Its absence, or
an express waiver of statutory interest, is worth objecting to.

### 6. Suspension of work for non-payment

This is the supplier's most effective remedy and is frequently absent. Check:

- Is there an express right to suspend for non-payment?
- What notice is required, and in what form?
- Does suspension extend deadlines and relieve you of liability for delay? Without
  this, suspending exposes you to a delay claim
- Is there a right to **terminate** for persistent non-payment, and at what threshold?
- Are demobilisation and remobilisation costs recoverable?

A right to suspend without a corresponding extension of time is a trap. Flag it as a
primary ask.

### 7. Retainage, set-off and disputed amounts

- **Retainage / holdback** — is a percentage withheld pending final acceptance? How
  much, released when, on what trigger? An unbounded holdback is an interest-free
  loan of your margin.
- **Set-off** — can the client deduct amounts it claims are owed? A unilateral
  set-off right allows the client to be the judge of its own claim. Primary ask: set-
  off only for sums admitted or finally determined.
- **Disputed amounts** — is there an express obligation to pay the undisputed portion
  while a dispute is resolved? Without it, a small dispute can hold a whole invoice.
  This is a high-value, low-resistance ask.

### 8. Flow-down where you subcontract

If you subcontract, compare your inbound and outbound payment terms. A net-60 inbound
term against net-14 outbound funds the client from your working capital. Check
whether a pay-when-paid or pay-if-paid clause exists in your subcontracts, and flag
that its enforceability varies by jurisdiction and is restricted or void in several.
Model the exposure in
`domain-finance/corporate-finance-fpa/finance_subcontractor_margin_model.md` on the
assumption you must pay regardless.

---

## Output format

```markdown
# Payment terms review — [agreement], supplier side
**Governing law:** [x] · **Reviewed:** [date] · **Counsel review:** [required before signature]

## Summary
| Area | Position | Risk | Priority |
|---|---|---|---|
| Clock trigger | | | |
| Net period | | | |
| Approval gates | | | |
| Milestone triggers | | | |
| Late-payment interest | | | |
| Suspension right | | | |
| Retainage / set-off | | | |
| Disputed amounts | | | |

## Clause-by-clause
### [Clause ref] — [area]
**As drafted:** > [quoted text]
**Effect:** [what it means for cash]
**Primary:** [ask, with proposed wording]
**Fallback:** [acceptable variant]
**Walkaway:** [the version that should not be signed]

## Questions for counsel
1. [jurisdiction-specific question — statutory interest, penalty construction, pay-when-paid validity]

## Commercial effect
| | |
|---|---|
| Contractual days to cash | |
| Realistic days to cash | |
| Working-capital exposure if subcontracting | |
| Worst case if every gate is used | |
```

---

## Verification

- [ ] The clock trigger is identified precisely and every gating client action has a
      deadline or a deemed provision.
- [ ] Every milestone trigger is objectively determinable.
- [ ] Any payment contingent on a third party is flagged as a condition, not a milestone.
- [ ] The statutory-interest position is raised as a question for counsel, not asserted.
- [ ] Suspension rights are checked together with extension-of-time relief.
- [ ] Set-off is limited to admitted or determined sums, or flagged.
- [ ] An undisputed-portion obligation is present or requested.
- [ ] Worst-case days-to-cash is computed with every gate exercised.

**False-positive prevention.** The most common error is reading the net period and
stopping. Net-30 from approval, with no approval deadline, a PO requirement and a 10%
holdback is not a 30-day term; it is an indefinite one. Always trace the full path
from delivery to cash and compute the worst case.

The second is treating an interest clause as protection. It is a negotiating
instrument, not a remedy — the remedy is suspension and, ultimately, termination.
A review that secures interest but leaves no suspension right has secured the weaker
of the two.

The third is asserting statutory entitlements. These vary by jurisdiction, by
contract type and by the parties' status, and some can be displaced by agreement.
Raise them as questions for counsel.

---

## Related

- `legal_contract_clause_redline_targeted.md` — the five other high-risk clause families
- `legal_contract_risk_heatmap.md` — scoring these findings alongside the rest
- `legal_sow_drafter.md` — the acceptance criteria milestone triggers depend on
- `legal_subcontractor_flow_down_check.md` — outbound payment terms
- `../client-intake-communications/legal_demand_letter_drafter.md` — when these rights are exercised
