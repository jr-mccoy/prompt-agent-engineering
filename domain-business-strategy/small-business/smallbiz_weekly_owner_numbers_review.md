---
title: "Weekly Owner Numbers Review — Bank, Tax Set-Asides, Owner Draw, 8-Week Cash Look-Ahead"
category: business-strategy/small-business
description: "A 20-minute weekly routine for the owner of a local shop, trades business or freelance practice — true available cash after tax set-asides and committed bills, sales against last year, money owed in and out, an owner-draw decision rule, and a plain 8-week cash look-ahead against a stated floor; distinct from finance_cash_flow_forecasting_model (a finance team's driver-based treasury forecast) and solo_dev_metrics_dashboard (MRR and product metrics for a software business)."
techniques:
  - NE-11
  - DS-02
  - DP-28
  - OC-03
  - QA-01
difficulty: beginner
tags:
  - small-business
  - cash-flow
  - owner-draw
  - tax-set-aside
  - weekly-review
  - local-business
updated: "2026-09-24"
related_prompts:
  - domain-finance/treasury-capital-markets/finance_cash_flow_forecasting_model.md
  - domain-business-strategy/startup/solo_dev_metrics_dashboard.md
  - domain-business-strategy/small-business/smallbiz_bookkeeping_routine.md
---

# Weekly Owner Numbers Review

**Objective:** Give a small-business owner one short weekly session that answers four
questions — how much cash is really mine to use, am I selling more or less than last
year, who owes whom, and will I have enough cash in eight weeks — and ends in one
decision about this week's owner draw.

**When to Use:**
- You run a shop, café, trades business, salon, studio or freelance practice and
  check the bank app instead of the numbers.
- You have been surprised by a tax bill, a slow month or a payroll you nearly missed.
- Your accountant sees your numbers once a year and you want to see them weekly.

**Not this prompt if:**
- You need a driver-based treasury forecast for a finance team, with scenarios and a
  revolver — `domain-finance/treasury-capital-markets/finance_cash_flow_forecasting_model.md`.
- You run a software or subscription product and need MRR, churn and activation —
  `domain-business-strategy/startup/solo_dev_metrics_dashboard.md`.
- You need to get the books themselves in order — `smallbiz_bookkeeping_routine.md`
  comes first; this review reads its output.

## Inputs

1. Balances today: operating account, tax savings account, any other account.
2. This week's sales, and the same week last year if you have it.
3. Money owed to you (unpaid invoices) with how many days old.
4. Bills due in the next eight weeks: payroll, rent, loan, utilities, suppliers,
   tax payments — with dates.
5. Your tax set-aside rule as your accountant gave it (for example, a percentage of
   profit, plus any sales tax collected). If you have no rule, that is the first flag.
6. Your cash floor: the lowest operating balance you are willing to see — a common
   starting point is one payroll plus one rent.

## Method

1. **Truly available cash (NE-11).**
   `available = operating balance − bills due in the next 14 days`
   Money in the tax account is not yours; it is excluded from "available" and
   tracked separately.

2. **Tax set-asides.** Move this week's sales tax collected and your income-tax
   set-aside into the tax account. Confirm the tax account covers the next payment
   due. The percentage is your accountant's, not the prompt's.

3. **Sales pulse (DS-02).** This week vs same week last year, and vs your 4-week
   average. One number each, one sentence on why.

4. **Owed in and out.** Unpaid invoices by age; supplier bills by due date. Anything
   owed to you over 30 days gets a follow-up today.

5. **8-week look-ahead.** One row per week: expected money in (conservative — last
   year's same weeks, or your recent average, whichever is lower), known money out,
   ending balance. Mark any week below the floor.

6. **Rate each area (DP-28).** Green, amber or red for cash vs floor, tax account,
   receivables, and sales trend.

7. **Decide the owner draw.** Rule: take the planned draw if no week in the
   look-ahead falls below the floor; otherwise reduce it by enough to keep the lowest
   week above the floor, and say for how many weeks.

8. **Check (QA-01).** Each week's ending balance equals the previous ending plus in
   minus out; the tax account math matches.

## Output Format

```
# Owner numbers — [business], week of [date]

## Lights
| Area | Light | Why |

## Available cash
Operating [x] − next 14 days' bills [y] = available [z]
Tax account [a] — next payment [b] due [date]

## Sales pulse
This week [x] | Same week last year [y] ([±%]) | 4-week average [z]

## Owed
| To us | Days old | Action |   | We owe | Due |

## 8-week look-ahead (floor = [x])
| Week | In | Out (main items) | End | vs floor |

## Owner draw decision
[amount] this week — because [rule outcome]

## One thing to do this week
```

## Verification

- [ ] Tax account money is excluded from available cash.
- [ ] Look-ahead inflows are the conservative figure.
- [ ] Every ending balance reconciles to the previous week.
- [ ] The draw decision follows the stated rule.
- [ ] Any week below the floor is named with its cause.

## False-Positive Prevention

1. **The bank balance is not your money.** Sales tax collected and income-tax
   set-asides belong to the tax account; leaving them in operating makes every week
   look better than it is.
2. **Profit is not cash.** A profitable month with a big supplier prepayment can
   still miss payroll; this review is about cash timing.
3. **Do not forecast your hopes.** Use the lower of last year and recent average.
   The look-ahead exists to catch bad weeks, not to predict good ones.
4. **Do not count unpaid invoices as cash.** Show what happens if they arrive, but
   keep them out of the base look-ahead.
5. **No tax advice.** The set-aside percentage and payment dates come from your
   accountant; if you have none, the flag is "ask the accountant this week".
6. **Twenty minutes, not two hours.** If the review takes longer, the books behind it
   need `smallbiz_bookkeeping_routine.md` first.
7. **Dual failure:** cutting your own pay to zero every time a week dips amber is not
   prudence — it is how owners burn out. Cut by the amount the rule says.

## Example Output

```
# Owner numbers — Northside Bakery, week of 21 Sep 2026

## Lights
| Area | Light | Why |
| Cash vs floor | Amber | Week 7 falls to $5,710, below $7,200 floor |
| Tax account | Green | $9,200 covers the $2,480 sales tax due week 4 |
| Receivables | Amber | Catering invoice $1,800, 21 days old |
| Sales trend | Green | +4.9% vs same week last year |

## Available cash
Operating $18,400 − next 14 days (payroll $4,200, rent $3,000, ingredients $4,200,
tax transfers $2,640) = available $4,360
Tax account $9,200 — sales tax $2,480 due week 4; estimated tax $4,500 due week 6

## Sales pulse
This week $7,240 | Same week last year $6,900 (+4.9%) | 4-week average $7,050

## Owed
| To us | Days | Action |
| Office catering invoice $1,800 | 21 | Call Monday; resend invoice |
| We owe | Due |
| Flour supplier $2,100 | Weekly, Friday |

## 8-week look-ahead (floor = $7,200 = one payroll $4,200 + rent $3,000)
Weekly base out: ingredients $2,100 + draw $1,500 + tax transfers $1,320 = $4,920
| Wk | In | Out (main items) | End | vs floor |
| 1 | $7,000 | $9,120 (base + payroll) | $16,280 | ok |
| 2 | $7,000 | $7,920 (base + rent) | $15,360 | ok |
| 3 | $7,000 | $9,720 (base + payroll + utilities) | $12,640 | ok |
| 4 | $7,000 | $5,770 (base + loan) | $13,870 | ok |
| 5 | $5,800 | $9,120 (school holidays; payroll) | $10,550 | ok |
| 6 | $5,800 | $7,920 (rent) | $8,430 | ok |
| 7 | $7,000 | $9,720 (payroll + utilities) | $5,710 | below by $1,490 |
| 8 | $7,000 | $5,770 (loan) | $6,940 | below by $260 |
Tax account after week 8: $9,200 + 8 × $1,320 − 2 × $2,480 − $4,500 = $10,300

## Owner draw decision
Reduce draw by $500 in weeks 5, 6 and 7 ($1,500 total) → week 7 ends $7,210, week 8
$8,440 — both above floor. If the $1,800 catering invoice arrives, restore week 7.

## One thing to do this week
Collect the $1,800 catering invoice.
```

## Techniques Used

- **NE-11 Embedded Calculation Formulas:** available cash, look-ahead rows, tax account.
- **DS-02 Metric Specification:** a small fixed set of numbers, each defined.
- **DP-28 Traffic-Light Verdict System:** four lights the owner reads in seconds.
- **OC-03 Markdown Table Specification:** a table that is the same every week.
- **QA-01 Self-Verification:** week-to-week reconciliation of balances.

## Related Prompts

- `domain-finance/treasury-capital-markets/finance_cash_flow_forecasting_model.md` — full treasury forecast
- `domain-business-strategy/startup/solo_dev_metrics_dashboard.md` — metrics for a software business
- `domain-business-strategy/small-business/smallbiz_bookkeeping_routine.md` — the books this review reads
