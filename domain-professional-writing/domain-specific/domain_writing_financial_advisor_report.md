---
title: "Financial Advisor Quarterly Portfolio Report — Net Returns, Fair Benchmark, Goal Progress"
category: professional-writing/domain-specific
description: "Draft a financial advisor's quarterly portfolio letter to a client: net- and gross-of-fee returns over fixed standard periods against the benchmark in the client's IPS, dollar change split into contributions and investment result, plain explanation of what drove the gap, progress against the client's own goal, and outlook written as conditions-to-watch with every forward-looking line flagged for the firm's compliance review. Distinct from reviewing the portfolio's construction (finance_portfolio_construction_review) or checking a recommendation process (finance_reg_bi_fiduciary_check)."
techniques:
  - NE-15
  - NE-11
  - DD-05
  - QA-04
  - QA-20
difficulty: intermediate
tags:
  - financial-advisor
  - quarterly-portfolio-report
  - client-review-letter
  - performance-vs-benchmark
  - wealth-management
  - explain-portfolio-performance
updated: "2026-10-06"
related_prompts:
  - domain-finance/investing-research/finance_portfolio_construction_review.md
  - domain-finance/regulatory-compliance/finance_reg_bi_fiduciary_check.md
  - domain-finance/personal-finance-planning/finance_retirement_projection_model.md
  - domain-finance/personal-finance-planning/finance_asset_allocation_glidepath.md
---

# Financial Advisor Quarterly Portfolio Report

**Objective:** Produce a quarterly letter that tells a client, honestly and in plain language, how their portfolio did against a fair yardstick, why, whether they are still on track for their goal, and what the advisor is doing next — with nothing that reads as a promise.

**When to Use:**
- Quarter-end client reporting, where the performance system's numbers need a human explanation.
- A quarter where the portfolio lagged its benchmark and the client will notice.
- A drawdown quarter where the client needs context without minimisation.
- A quarter with a change (rebalance, new contribution plan, cash reserve refill) the client should understand.
- **Not this prompt if** you are deciding whether the portfolio itself is well built — that is `domain-finance/investing-research/finance_portfolio_construction_review.md`. Checking whether a recommendation meets best-interest or fiduciary obligations is `domain-finance/regulatory-compliance/finance_reg_bi_fiduciary_check.md`. Re-running goal probability is `domain-finance/personal-finance-planning/finance_retirement_projection_model.md`; this letter reports its result.

**Audience:** An individual client or couple who reads the letter once, cares about their goal more than the index, and will remember any sentence that sounded like a promise. A second reader is the firm's compliance reviewer. The advisor signs and owns the letter; firm compliance approves it before it is sent.

## Inputs / Context

Paste source material inside the named tags and refer to it by tag name.

1. **Client profile** — ages, goal and target date, risk tolerance, time horizon, IPS target allocation and stated benchmark — in `<client_profile>`.
2. **Performance report** — beginning and ending values, contributions, withdrawals, fees charged, time-weighted returns net and gross of fees for QTD, YTD, 1-year, 3-year, and since inception, with benchmark returns for the same periods — in `<performance_report>`.
3. **Market context** — the advisor's own notes on what happened this quarter — in `<market_notes>`. The model adds no market events of its own.
4. **Positioning and actions** — why the portfolio did what it did (allocation, tilts, cash reserve), trades made or planned — in `<positioning>`.
5. **Goal status** — latest planning-software output (projected funding, probability, assumptions date) — in `<plan_report>`.
6. **Outlook notes** — the advisor's views and any planned adjustments — in `<outlook_notes>`.

## Method

1. **Fix the periods before writing (NE-15).** Always report the same standard set — QTD, YTD, 1-year, 3-year annualised, since inception annualised — whether flattering or not. Name the benchmark exactly as the IPS defines it.
2. **Reconcile the dollars (NE-11).**
   - `Investment result = ending value − beginning value − contributions + withdrawals` (after fees).
   - State fees in dollars and the net-vs-gross return gap; confirm the net return is consistent with investment result ÷ beginning value (approximately, as flows are timed).
3. **Lead with the honest headline.** One sentence: return net of fees vs. benchmark for the quarter, and one for progress toward the goal.
4. **Explain the gap, not the market.** Attribute over- or under-performance to the positioning in `<positioning>` (allocation, tilt, reserve). Market context is supporting, from `<market_notes>` only.
5. **Connect to the goal.** Report the `<plan_report>` figure with its date and what moved it; if not updated this quarter, say so.
6. **Write the outlook as conditions and actions.** "If X, we will do Y" and "what we are watching" — not forecasts of rates, prices, or returns.
7. **Verify and flag before drafting (QA-04, DD-05).** Every return and benchmark figure traces to `<performance_report>`; every period has a benchmark beside it; every forward-looking sentence, every comparative claim, and any wording near "guarantee", "safe", "will", "expect" is listed in a compliance flag block for the firm's review. Do not cite a specific rule — flag the sentence.

## Output Format

```
[Firm letterhead]   Quarterly review — [quarter, year]   [Client names]

## The quarter in one paragraph
[Net return vs benchmark · goal status · the one thing to know]

## Your account this quarter
[Beginning → contributions/withdrawals → investment result after fees → ending]
Fees this quarter: $[..] ([..]% net vs [..]% gross)

## Returns vs your benchmark ([IPS benchmark name])
| Period | Your portfolio (net) | Before fees | Benchmark | Difference (net) |
| QTD | YTD | 1 yr | 3 yr ann. | Since [date] ann. |

## Why the portfolio did what it did
[Positioning-driven explanation; market context from notes]

## Progress toward [goal]
[Plan figure, date, what moved it]

## What we're doing and watching
[Actions taken/planned · conditions we're watching and our response]

## Next steps for you
[Specific items, dates]

[Advisor signature; required firm disclosures inserted by compliance]

--- COMPLIANCE FLAGS (internal) ---
[Each forward-looking or sensitive sentence, quoted, with the reason flagged]
```

## Verification

- [ ] All five standard periods are shown, each with a benchmark figure for the same dates.
- [ ] Net and gross returns are both shown; fees appear in dollars.
- [ ] The dollar reconciliation balances: beginning + contributions − withdrawals + investment result = ending.
- [ ] The benchmark named matches `<client_profile>` IPS wording.
- [ ] No market event appears that is not in `<market_notes>`.
- [ ] Goal status quotes `<plan_report>` with its date.
- [ ] Every forward-looking sentence appears in the compliance flag block.

## False-Positive Prevention

1. **Account growth reported as return.** "Your account grew $49,500" when $15,000 of it was the client's own deposit. Split contributions from investment result every time.
2. **Gross return in the headline.** The client lives on the net figure. Leading with the before-fee number overstates results by the fee, every quarter, permanently.
3. **Periods chosen after seeing the numbers.** Dropping the 1-year line in a bad year, or adding "since the March low", is cherry-picking even when each figure is accurate. The period set is fixed in advance.
4. **A benchmark that is not the client's.** Comparing a 60/40 portfolio to a bond index in a strong-equity quarter, or to an all-equity index in a weak one, makes any result look like skill or misfortune. Use the IPS benchmark.
5. **Market narrative written by the model.** Plausible quarter-summaries ("investors cheered…") invent events. Market context comes only from the advisor's notes.
6. **Reassurance that reads as a promise.** "Markets always recover", "your income is secure", "we expect rates to fall" — each is a prediction or guarantee in a client's memory. Rewrite as condition-and-response and flag for compliance.
7. **Underperformance explained by the market alone.** If the benchmark rose more, the gap is the portfolio's positioning. Name the decision that caused it and whether it is still intended.

## Dual-Failure Prevention (QA-20)

- **Harmful:** a warm letter that buries a lag behind the benchmark, shows gross returns, or reassures with language that later reads as a guarantee.
- **Unhelpful:** a letter of disclaimers and index commentary in which the client cannot find their own return or whether they are on track.
- **Bar:** the client can answer three questions from the first screen — what did my money earn after fees, how did that compare with the yardstick we agreed, and am I still on track — and compliance finds every forward-looking sentence already flagged.

## Example Output

```
Ridgeline Wealth Partners   Quarterly review — Q3 2026   Marcus & Elena Reyes

## The quarter in one paragraph
Your portfolio earned 1.9% after fees this quarter, behind its benchmark's 2.6%.
Your retirement plan for 2033 remains on track at 82% in our latest projection.
The one thing to know: the shortfall came from the short-term bonds holding your
2027–28 spending money — a choice we made on purpose and are keeping.

## Your account this quarter
Value on 30 Jun:            $1,812,400
Your contribution:            +$15,000
Investment result after fees: +$34,500
Value on 30 Sep:            $1,861,900
(1,812,400 + 15,000 + 34,500 = 1,861,900. Of the $49,500 increase, $15,000 was
your own deposit.)
Fees this quarter: $4,530 — 1.9% net vs 2.2% before fees.

## Returns vs your benchmark (60% global equity / 40% US aggregate bond, per IPS)
| Period            | Net   | Before fees | Benchmark | Difference (net) |
| Q3 2026           | 1.9%  | 2.2%        | 2.6%      | −0.7 |
| Year to date      | 6.8%  | 7.6%        | 7.4%      | −0.6 |
| 1 year            | 9.1%  | 10.1%       | 9.8%      | −0.7 |
| 3 years, annual   | 6.2%  | 7.2%        | 6.0%      | +0.2 |
| Since Jan 2019, annual | 6.9% | 7.9%   | 7.1%      | −0.2 |

## Why the portfolio did what it did
About $180,000 sits in short-term bonds to fund your first two retirement years.
Per our notes, longer-term bonds rose more this quarter as interest rates fell;
your short-term holdings rose less. That explains most of the 0.7-point gap.
Over three years the same reserve helped (+0.2), when rising rates hurt longer bonds.

## Progress toward retiring in 2033
Our planning software, updated 28 Sep with this quarter's values and your
higher contribution, shows an 82% likelihood of funding your plan (79% in June).
That figure is a model estimate, not a promise.

## What we're doing and watching
- Done: rebalanced equities back to 60% on 12 Aug.
- Planned: top up the spending reserve in January from your bonus contribution.
- Watching: if equities fall more than 10% from here, we will rebalance into
  them rather than sell, as your IPS sets out.

## Next steps for you
- Confirm the January contribution amount by 15 Dec.
- Bring your CPA's 2026 estimate to our 4 Nov meeting for the Roth conversion
  discussion.

Jordan Pike, CFP®   [Firm disclosures inserted by compliance]

--- COMPLIANCE FLAGS (internal) ---
1. "remains on track at 82%" — projection result; check model-output disclosure.
2. "we will rebalance into them rather than sell" — forward-looking action.
3. Draft line removed: "we expect rates to keep falling, which should help bonds"
   — read as a forecast; replaced by the conditional above.
4. Market context ("longer-term bonds rose as rates fell") — from <market_notes>; confirm.
```

## Techniques Used

- **NE-15 Data Storytelling Framework** — headline, reconciliation, comparison, explanation, goal, in that order.
- **NE-11 Embedded Calculation Formulas** — dollar reconciliation and net-vs-gross gap recomputed in the letter.
- **DD-05 Human Review Flags** — every forward-looking or sensitive sentence routed to the firm's compliance review.
- **QA-04 Uncertainty Acknowledgment** — goal probability and outlook stated as model output and conditions, not forecasts.
- **QA-20 Dual-Failure Quality Test** — honest about lag without burying the client in disclaimers.

## Related Prompts

- `domain-finance/investing-research/finance_portfolio_construction_review.md` — whether the allocation and tilts the letter explains are sound.
- `domain-finance/regulatory-compliance/finance_reg_bi_fiduciary_check.md` — reviewing the recommendation process behind any change reported.
- `domain-finance/personal-finance-planning/finance_retirement_projection_model.md` — produces the goal figure the letter quotes.
- `domain-finance/personal-finance-planning/finance_asset_allocation_glidepath.md` — when the quarter's review leads to an allocation change.
