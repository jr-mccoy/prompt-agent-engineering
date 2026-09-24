---
title: "Owner Bookkeeping Routine — Weekly, Monthly, Quarterly, and a Clean Accountant Handoff"
category: business-strategy/small-business
description: "Set up the bookkeeping cadence an owner of a local shop, trades business or freelance practice can keep without a bookkeeper — a 15-minute weekly pass, a monthly reconciliation that must tie to the statement, quarterly tax-date checks, and a year-end handoff package — with a written line between what the owner records and what the accountant decides; distinct from finance_month_end_close_checklist (a controller's multi-entity close) and financial-records-toolkit (organising personal statements for an attorney)."
techniques:
  - ST-02
  - NE-20
  - CM-09
  - DD-05
  - QA-01
difficulty: beginner
tags:
  - small-business
  - bookkeeping
  - reconciliation
  - accountant-handoff
  - receipts
  - owner-operator
updated: "2026-09-24"
related_prompts:
  - domain-finance/accounting-controllership/finance_month_end_close_checklist.md
  - financial-records-toolkit/README.md
  - domain-business-strategy/small-business/smallbiz_weekly_owner_numbers_review.md
---

# Owner Bookkeeping Routine

**Objective:** Give a small-business owner a bookkeeping routine short enough to keep
every week, strict enough that the books reconcile every month, and organised so the
year-end handoff to the accountant takes an afternoon rather than a fortnight.

**When to Use:**
- The books are "done" once a year in a panic before the tax deadline.
- You cannot say this week whether last month was profitable.
- Personal and business spending are mixed in the same account or card.
- Your accountant keeps asking for the same documents.

**Not this prompt if:**
- You run a finance function with a close calendar, accruals and multiple entities —
  `domain-finance/accounting-controllership/finance_month_end_close_checklist.md`.
- You are organising your own bank and card statements for an attorney or a legal
  matter — `financial-records-toolkit/`.
- You want the weekly decisions the books feed — `smallbiz_weekly_owner_numbers_review.md`.

## Inputs

1. Accounts: business bank, cards, payment processors, cash handling.
2. Tool in use: accounting software, spreadsheet, or none yet.
3. How you get paid (cards, invoices, cash) and how you pay (card, transfer, cash).
4. Whether you collect sales tax, have employees or pay contractors.
5. Your accountant's name and the documents they have asked for before.
6. Current state: months behind, uncategorised transactions, missing receipts.

## Method

1. **Separate first (CM-09).** One business account and one business card. Owner
   money moves in and out as recorded draws or contributions, never as expenses.
   Mixed accounts are the root of most small-business bookkeeping trouble.

2. **Write the authority line.** Owner records: every transaction categorised, every
   receipt attached, every invoice sent. Accountant decides: ambiguous categories,
   asset versus expense, depreciation, deductibility, tax filings. Ambiguous items go
   to a "question for accountant" category with a note, not a guess.

3. **Weekly — 15 minutes (ST-02).**
   1. Categorise new transactions; photograph and attach receipts.
   2. Record cash sales and cash paid out.
   3. Send invoices for work finished this week.
   4. Move tax set-asides as the accountant specified.

4. **Monthly — about one hour.**
   1. Reconcile each account and card to its statement: book balance plus or minus
      items not yet cleared must equal the statement ending balance, to the cent.
   2. Review unpaid invoices; follow up anything over 30 days.
   3. Confirm sales tax collected matches the sales tax report, if you collect it.
   4. Look at the month's profit and loss once; note anything that looks wrong.
   5. Clear the "question for accountant" list or send it.

5. **Quarterly.** Check tax payment dates and amounts with the accountant; file or
   confirm sales tax returns; review whether any contractor will need year-end
   reporting.

6. **Year-end handoff package (NE-20).** One folder: reconciled statements for all
   12 months, the profit and loss and balance sheet, list of equipment purchases with
   dates and receipts, loan statements, contractor payment totals with their details,
   inventory count if applicable, vehicle and home-office records if used, and the
   open questions list. Ask the accountant for their own checklist and merge it.

7. **Flag, don't decide (DD-05).** Anything touching deductibility, entity type,
   payroll, or what must be filed is a question for the accountant.

8. **Check (QA-01).** Each monthly reconciliation ties exactly; unexplained
   differences are investigated, not plugged.

## Output Format

```
# Bookkeeping routine — [business]

## Set-up gaps
| Gap | Fix | By when |

## Authority line
Owner records: … | Accountant decides: …

## Weekly (15 min) — [day]
## Monthly (60 min) — [date]
## Quarterly — [dates]
## Year-end handoff package
| Item | Where it lives | Status |

## This month's reconciliation
| Account | Statement end | Uncleared ± | Adjusted | Book | Difference |

## Questions for the accountant
```

## Verification

- [ ] Business and personal money are in separate accounts, or fixing it is item one.
- [ ] Every account reconciles to the cent, or the difference is explained.
- [ ] Owner draws are recorded as draws, not expenses.
- [ ] Ambiguous items sit in a question list, not a guessed category.
- [ ] The handoff package list matches the accountant's own checklist.

## False-Positive Prevention

1. **Syncing the bank feed is not bookkeeping.** Auto-imported transactions still
   need categories, receipts and reconciliation.
2. **"Close enough" is not reconciled.** A $40 difference can hide a duplicate or a
   missing sale. Find it or flag it; never post a plug entry.
3. **Owner draws are not wages or expenses** for a sole proprietor — how owner pay is
   treated depends on the business structure; ask the accountant.
4. **Do not categorise to reduce tax.** Categorise what the spend was; deductibility
   is the accountant's call.
5. **A receipt in the glovebox is not a record.** Photograph and attach it the same
   week.
6. **Catching up is its own project.** If you are months behind, do the backlog month
   by month, oldest first, before starting the weekly routine.
7. **Dual failure:** a routine designed for a controller will be abandoned in a month.
   Fifteen minutes weekly that happens beats two hours that doesn't.

## Example Output

```
# Bookkeeping routine — Ortiz Studio (freelance design), from Oct 2026

## Set-up gaps
| Gap | Fix | By when |
| Software subscriptions on personal card | Move to business card | 15 Oct |
| 7 uncategorised September transactions | Categorise or add to question list | This Friday |
| No receipt folder | Phone app attached to accounting software | This Friday |

## Authority line
Owner records: categories, receipts, invoices, draws, cash.
Accountant decides: new laptop as asset or expense; home-office share; quarterly
tax amounts; any year-end contractor reporting.

## Weekly — Friday 4:00–4:15
Categorise; attach receipts; invoice finished projects; move 25% of this week's
receipts to tax savings (accountant's instruction, Mar 2026).

## Monthly — first Monday, 60 min
Reconcile checking and card; chase invoices > 30 days; review P&L; send question list.

## Quarterly — Jan 15, Apr 15, Jun 15, Sep 15 [confirm dates with accountant]
Confirm estimated tax amount; check contractor totals.

## Year-end handoff package
| Item | Where | Status |
| 12 reconciled statements | Software → Reports | 9 of 12 |
| Equipment list (laptop, Sep) | Receipts folder | Receipt attached |
| Contractor totals (illustrator) | Vendor report | Details on file |
| Home-office measurements | Notes | Needed |

## This month's reconciliation — September
| Account | Statement end | Uncleared | Adjusted | Book | Diff |
| Checking | $12,480.55 | − $350.00 (printer, cleared 2 Oct) | $12,130.55 | $12,130.55 | $0.00 |
| Card | $1,212.40 owed | none | $1,212.40 | $1,212.40 | $0.00 |

## Questions for the accountant
1. Laptop ($1,850, Sep) — asset or expense?
2. Co-working day passes — how to categorise?
```

## Techniques Used

- **ST-02 Structured Sequential Instructions:** weekly, monthly and quarterly steps in order.
- **NE-20 Third-Party Handoff Package:** the year-end folder for the accountant.
- **CM-09 Authority Boundary Specification:** what the owner records vs what the accountant decides.
- **DD-05 Human Review Flags:** ambiguous items routed to the question list.
- **QA-01 Self-Verification:** reconciliation to the cent.

## Related Prompts

- `domain-finance/accounting-controllership/finance_month_end_close_checklist.md` — controller-level close
- `financial-records-toolkit/README.md` — organising statements for an attorney
- `domain-business-strategy/small-business/smallbiz_weekly_owner_numbers_review.md` — the weekly decisions these books feed
