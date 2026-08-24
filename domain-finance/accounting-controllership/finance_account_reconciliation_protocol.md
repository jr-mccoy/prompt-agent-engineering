---
title: "Account Reconciliation Protocol — Structured Recs with Exception Handling"
category: finance/accounting-controllership
description: "Run a structured balance-sheet account reconciliation: tie GL to an independent supporting source, classify and age reconciling items, set materiality and aging thresholds, and route exceptions for resolution and sign-off."
techniques:
  - ST-02
  - DT-02
  - NE-11
  - DS-06
  - QA-01
difficulty: beginner
tags:
  - reconciliation
  - balance-sheet
  - exception-handling
  - controllership
  - aging
  - sign-off
updated: "2026-06-08"
related_prompts:
  - domain-finance/accounting-controllership/finance_month_end_close_checklist.md
  - domain-finance/accounting-controllership/finance_journal_entry_review_protocol.md
  - domain-finance/accounting-controllership/finance_audit_pbc_preparation.md
  - domain-finance/field_guide.md
---

**Informational only — not accounting, audit, or tax advice. Verify all standard references against current authoritative guidance (FASB ASC / IASB IFRS).**

## Objective

Produce a disciplined account-reconciliation for a given balance-sheet account that ties the general-ledger balance to an independent supporting source, itemizes and ages every reconciling item, applies defined materiality and aging thresholds, classifies items by cause, routes exceptions for resolution, and ends in a documented preparer/reviewer sign-off — so that each balance is substantiated and audit-ready rather than merely "looking reasonable."

---

## When to Use

- Monthly/quarterly reconciliation of any balance-sheet account (cash, AR, AP, accruals, prepaids, fixed assets, intercompany, suspense/clearing).
- Cleaning up a stale or never-reconciled account ahead of an audit.
- Standardizing rec quality across a team so every account uses the same threshold and exception logic.
- Investigating a suspense or clearing account that keeps accumulating unexplained items.
- **Do not use** to reconcile bank cash without the actual bank statement, or to "force" a balance — an unexplained difference must remain an open exception, never a plug.

---

## Inputs / Context Required

```
<rec_context>
Account name & GL number:
Account type: asset | liability | equity | clearing/suspense
Accounting framework: US GAAP | IFRS
Period end date:
Reporting / functional currency (note FX if multi-currency):

GL BALANCE:
- GL ending balance (per trial balance):

SUPPORTING SOURCE (the independent substantiation):
- Source type (sub-ledger detail, bank statement, amortization schedule, vendor statement, FA register, third-party confirmation):
- Supporting balance per that source:

THRESHOLDS (or leave blank for recommended defaults):
- Materiality threshold for investigating a reconciling item:
- Aging threshold beyond which an open item is escalated (e.g., >60 days):

KNOWN RECONCILING ITEMS (optional):
- Timing differences, in-transit items, disputed amounts, known errors:
</rec_context>
```

---

## Constraints

### Must
- State the basic reconciliation identity and prove it:
```
GL Balance  −  Supporting Source Balance  =  Total Reconciling Items
Reconciliation is COMPLETE only when every reconciling item is identified, classified, and explained (sum ties exactly).
```
- Use an **independent** supporting source (not another extract of the same GL).
- Itemize each reconciling item with: amount, age (origination date), cause classification, and resolution status.
- Classify each item by **cause**: timing/in-transit | unrecorded transaction | error | dispute | unsupported (requires investigation).
- Apply a **materiality threshold** (investigate items above it) and an **aging threshold** (escalate items older than it).
- Treat any **unexplained residual as an open exception**, never a balancing plug.
- Distinguish **reconciled and clean** from **reconciled with open items** — a rec with aged unresolved items is not "clean."
- End with a **preparer sign-off and an independent reviewer sign-off** (different people).
- Flag clearing/suspense accounts that should net to zero but do not.

### Must Not
- Plug a difference to make the rec tie; an unexplained difference stays open and routed.
- Use a second pull of the GL as the "supporting source" (no independent substantiation).
- Mark a rec "complete" while material or aged items remain unresolved.
- Invent supporting balances, statement figures, or item ages not supplied.
- Let the same person prepare and review the reconciliation.

---

## Instructions

1. **Capture both balances.** Record the GL ending balance and the independent supporting-source balance as of the same date.

2. **Compute the difference.** `Difference = GL − Source`. This is the total that the reconciling items must fully explain.

3. **Identify reconciling items.** List every item bridging GL to source. For each, record amount, origination date (for aging), and a one-line description.

4. **Classify by cause** using this decision tree:

```
Is the item a known timing/in-transit difference expected to clear next period?
  └─ Yes → "Timing"  (monitor; no error)
  └─ No  → Is it a transaction that occurred but is not yet recorded in the GL or source?
           └─ Yes → "Unrecorded" (book a correcting JE)
           └─ No  → Is it a posting/keying/classification mistake?
                    └─ Yes → "Error" (correct and root-cause)
                    └─ No  → Is it disputed (vendor/customer disagreement)?
                             └─ Yes → "Dispute" (route to owner; track)
                             └─ No  → "Unsupported" → OPEN EXCEPTION (investigate)
```

5. **Apply thresholds.** Flag items above the materiality threshold for investigation; flag items older than the aging threshold for escalation regardless of size.

6. **Confirm the tie.** Sum of classified items must equal the Step-2 difference exactly. If a residual remains, it is an open "unsupported" exception — do not plug.

7. **Route exceptions.** Assign each open/aged item an owner and a target resolution date.

8. **Determine rec status:** `Clean` (ties, no material/aged open items) vs `Reconciled with exceptions` (ties, but open items remain) vs `Not reconciled` (does not tie / unexplained residual).

9. **Sign off.** Preparer signs; an independent reviewer reviews and signs. Different people.

10. **Verification (QA-01).** Re-add the item schedule; confirm it equals GL − Source; confirm preparer ≠ reviewer.

---

## Output Format

```
## Account Reconciliation — [Account name / GL #]
Period end: [date] | Framework: [US GAAP / IFRS] | Currency: [ccy]
Status: [Clean | Reconciled with exceptions | Not reconciled]

### Balance Tie
| Line | Amount |
|------|--------|
| GL ending balance | [illustrative] 1,250,400 |
| Supporting source balance | 1,243,900 |
| **Difference to explain** | **6,500** |
Source: [sub-ledger / bank stmt / amortization schedule / etc.]

### Reconciling Items
| # | Description | Amount | Origination date | Age (days) | Cause | Status | Owner | Target date |
|---|-------------|--------|------------------|------------|-------|--------|-------|-------------|
| 1 | Deposit in transit | 9,000 | [date] | 3 | Timing | Will clear | AR Acct | next period |
| 2 | Unposted vendor credit | (3,500) | [date] | 12 | Unrecorded | JE booked | AP Acct | resolved |
| 3 | Aged unidentified variance | 1,000 | [date] | 74 | Unsupported | OPEN ⚠ | Acct Mgr | [date] |
| | **Total reconciling items** | **6,500** | | | | (ties to difference) | | |

### Exceptions Requiring Action
| # | Item | Why open | Threshold breached | Escalation |
|---|------|----------|--------------------|------------|
| 3 | Unidentified variance $1,000 | No support found | Aging >60d | Controller |

### Sign-Off
| Role | Name | Date |
|------|------|------|
| Preparer | [name] | [date] |
| Reviewer (independent) | [name] | [date] |
```
*All amounts and dates are illustrative until populated from the entity's records.*

---

## Verification

- [ ] GL and supporting balances are as of the same period-end date.
- [ ] Supporting source is independent of the GL (not a re-extract of it).
- [ ] Sum of reconciling items equals exactly GL − Source (no plug).
- [ ] Every item has an age, a cause classification, and a status.
- [ ] Materiality and aging thresholds applied; breaches escalated.
- [ ] Any unexplained residual is shown as an OPEN exception, not absorbed.
- [ ] Rec status correctly reflects whether open items remain.
- [ ] Preparer and reviewer are different individuals and both signed.

---

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Plugging the difference so the rec "ties" | Forbidden; unexplained residual must remain an OPEN unsupported exception |
| Calling a rec "clean" with aged open items | Distinguish Clean vs Reconciled-with-exceptions; aged/material open items disqualify "clean" |
| Using a second GL extract as the "support" | Require an independent source (bank, sub-ledger, schedule, third-party confirmation) |
| Inventing supporting balances or item ages | Use only supplied figures; if support is missing, the item is an open exception, not an assumed value |
| Same person preparing and reviewing | Enforce preparer ≠ reviewer; reject self-review |
| Treating an FX or framework difference as an error | For multi-currency/IFRS-vs-GAAP accounts, separate genuine errors from translation/remeasurement and policy differences before classifying as "error" |
