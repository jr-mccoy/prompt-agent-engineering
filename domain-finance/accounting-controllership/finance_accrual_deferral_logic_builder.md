---
title: "Accrual & Deferral Logic Builder — Entries, Support, and Reversal Logic"
category: finance/accounting-controllership
description: "Build month-end accrual and deferral journal entries with calculation support, period-matching rationale, reversal logic, and a true-up plan — distinguishing accruals, deferrals, prepaids, and unearned revenue, and avoiding double-count when actuals post."
techniques:
  - NE-11
  - DT-02
  - DS-06
  - QA-01
  - RT-05
difficulty: intermediate
tags:
  - accruals
  - deferrals
  - journal-entries
  - matching-principle
  - reversing-entries
  - period-cutoff
updated: "2026-06-08"
related_prompts:
  - domain-finance/accounting-controllership/finance_journal_entry_review_protocol.md
  - domain-finance/accounting-controllership/finance_account_reconciliation_protocol.md
  - domain-finance/accounting-controllership/finance_revenue_recognition_asc606_memo.md
  - domain-finance/field_guide.md
---

**Informational only — not accounting, audit, or tax advice. Verify all standard references against current authoritative guidance (FASB ASC / IASB IFRS).**

## Objective

Build correct, well-supported accrual and deferral journal entries for a period close — each with an explicit calculation, the period-matching rationale (accrual basis under both US GAAP and IFRS), the correct debit/credit direction, and a reversal-or-true-up plan that prevents double-counting when the actual transaction posts. The output is a set of audit-ready entries plus the logic that governs their reversal.

---

## When to Use

- Booking month-end accruals (expenses incurred but not yet invoiced/paid) and deferrals (cash received/paid not yet earned/consumed).
- Designing reversing-entry vs true-up logic so accruals don't double-count when the invoice arrives.
- Cleaning up a prepaid or unearned-revenue schedule that has drifted.
- Standardizing how a team books recurring accruals each period.
- **Do not use** to recognize revenue — for customer-contract revenue timing use the ASC 606 / IFRS 15 memo; this prompt handles the mechanics of accrual/deferral entries, not the revenue-recognition policy decision.

---

## Inputs / Context Required

```
<accrual_context>
Entity / framework: US GAAP | IFRS
Period end:
Item type: accrued expense | deferred (prepaid) expense | accrued revenue | deferred (unearned) revenue

ITEM FACTS:
- Description (what economic event):
- Amount basis (invoice estimate, contract rate × period, run-rate, headcount × rate, etc.):
- Period the cost/benefit relates to (matching):
- Expected actual-settlement date (when invoice/payment/recognition occurs):
- Supporting evidence available (contract, prior invoice, schedule):

POLICY:
- Materiality threshold for accruing:
- Reversal convention: auto-reverse next period | true-up against actual | amortize on schedule:
- Account coding (expense/revenue account; accrual/deferral balance-sheet account):
</accrual_context>
```

---

## Constraints

### Must
- Classify the item correctly using the four-way matrix and the cash-vs-recognition timing:
```
                    Cash AFTER recognition         Cash BEFORE recognition
Expense side    →   ACCRUED EXPENSE (liability)     PREPAID / DEFERRED EXP (asset)
Revenue side    →   ACCRUED REVENUE (asset)         UNEARNED / DEFERRED REV (liability)
```
- Show the **calculation** behind every accrued/deferred amount (NE-11 auditability) — no round-number plug without basis.
- State the **matching rationale**: which period the cost/benefit belongs to and why the entry moves it there.
- Give the correct **debit/credit** direction and account coding.
- Define the **reversal/true-up logic** explicitly:
  - **Auto-reversing accrual:** entry reverses on day 1 of next period; when actual posts, it hits the expense account directly (net effect correct). Use when an invoice/payment will post next period.
  - **True-up (non-reversing):** accrual stays on the balance sheet; when actual arrives, the difference is trued up against the accrual liability/asset (variance to expense). Use when the timing/amount is uncertain or settled over multiple periods.
  - **Amortization (deferral):** systematic recognition over the benefit period (prepaid expense amortized; unearned revenue recognized).
- Include a **double-count guardrail**: state exactly how the actual transaction is prevented from hitting the P&L twice.
- Apply the **materiality threshold** — note when an item is below threshold and need not be accrued.
- Note any **GAAP-vs-IFRS** treatment difference relevant to the item (generally minimal for routine accruals; flag if the item touches an area that diverges, e.g., development-cost capitalization, provisions/IAS 37 vs ASC 450).

### Must Not
- Recognize customer-contract revenue here — route revenue-timing policy to ASC 606 / IFRS 15.
- Book a round-number accrual with no stated basis ("plug").
- Leave reversal logic unspecified — every accrual must say whether it reverses, trues up, or amortizes.
- Allow the actual to double-count by omitting the reversal/true-up mechanism.
- Invent supporting amounts, contract rates, or invoice figures not supplied.
- Treat an IFRS provision (IAS 37) as identical in recognition timing to a US GAAP loss contingency (ASC 450) without noting the threshold difference ("probable" definitions differ).

---

## Instructions

1. **Classify the item** with the four-way matrix and confirm the balance-sheet account (liability vs asset) and P&L account.

2. **Build the calculation.** Document the basis (rate × days, headcount × rate, % of contract, prior-invoice estimate) and compute the amount. Show the arithmetic.

3. **Apply materiality.** If below threshold, recommend not accruing (and note the policy). Otherwise proceed.

4. **Write the entry.** Provide DR/CR with accounts and amount, plus a one-line matching rationale.

5. **Choose reversal logic** via this decision tree:
```
Will the actual invoice/payment post in a single later period?
  └─ Yes, amount fairly certain → AUTO-REVERSE next period (actual hits expense directly)
  └─ Uncertain amount / settled over time → TRUE-UP (keep on BS; variance to P&L on settlement)
Deferral with a benefit/earning period?
  └─ AMORTIZE on a schedule (straight-line unless usage pattern differs)
```

6. **State the double-count guardrail.** Describe how the period-2 actual nets correctly (reversal cancels prior accrual, or true-up absorbs the difference).

7. **Build the schedule** for deferrals/amortizing items (period, opening, recognized, closing).

8. **GAAP-vs-IFRS note** where relevant (provisions, capitalization).

9. **Verification (QA-01).** Re-check the entry balances (DR = CR); confirm the reversal/true-up prevents double-count; confirm every amount traces to a stated basis.

---

## Output Format

```
## Accrual / Deferral Entry — [Item]
Framework: [US GAAP / IFRS] | Period end: [date]
Type: [Accrued expense | Deferred expense | Accrued revenue | Deferred revenue]

### Classification & Matching
Matrix position: [e.g., Expense side, cash after recognition → Accrued expense]
Belongs to period: [period] because [matching rationale].

### Calculation (basis shown)
[e.g., Contracted service $60,000/yr × (20 of 30 days) = $40,000 ... or headcount 50 × $1,200 bonus accrual]
Accrued/deferred amount: [illustrative] 40,000
Materiality: [above / below threshold]

### Journal Entry
| Account | DR | CR |
|---------|----|----|
| [Expense account] | 40,000 | |
| [Accrued liability] | | 40,000 |
Memo: accrue [item] for [period]; reverses [convention].

### Reversal / True-Up Logic
Convention: [Auto-reverse next period | True-up against actual | Amortize over [n] periods]
Double-count guardrail: [exactly how period-2 actual nets to zero / correct expense]

### Deferral / Amortization Schedule (if applicable)
| Period | Opening | Recognized | Closing |
|--------|---------|------------|---------|
| 1 | 120,000 | 10,000 | 110,000 |
| … | | | |

### GAAP vs IFRS Note
[Only if item touches a divergence — e.g., IAS 37 provision threshold vs ASC 450; else "no divergence."]
```

---

## Verification

- [ ] Item classified correctly via the four-way matrix; correct BS and P&L accounts.
- [ ] Calculation basis shown; no unsupported round-number plug.
- [ ] Entry balances (total DR = total CR).
- [ ] Matching rationale stated (which period, why).
- [ ] Reversal/true-up/amortization convention explicitly chosen.
- [ ] Double-count guardrail describes how the actual nets correctly.
- [ ] Materiality threshold applied.
- [ ] Amortization schedule foots for deferrals.
- [ ] GAAP-vs-IFRS difference noted where relevant (or "none").

---

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Accrual double-counts when the actual invoice posts | Every accrual must specify reverse/true-up; state how period-2 actual nets correctly |
| Booking a round-number plug with no basis | Require a documented calculation (NE-11); reject unsupported amounts |
| Misclassifying a deferral as an accrual (wrong BS side) | Use the four-way matrix; confirm asset vs liability against cash-vs-recognition timing |
| Recognizing customer revenue under the guise of an "accrual" | Route revenue-timing decisions to ASC 606 / IFRS 15; this prompt is mechanics only |
| Treating an IFRS provision like a US GAAP contingency without checking thresholds | Note IAS 37 vs ASC 450 recognition-threshold differences before booking |
| Inventing contract rates or invoice amounts | Use only supplied figures; missing support means the item is an estimate flagged for confirmation |
