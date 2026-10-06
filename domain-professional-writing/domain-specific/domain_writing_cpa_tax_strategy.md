---
title: "CPA Year-End Tax Strategy Letter — Eligible Strategies, Save-vs-Defer, Dated Actions"
category: professional-writing/domain-specific
description: "Draft a CPA's year-end tax strategy letter to a business client: each recommendation tied to the client facts that make it eligible, its effect labelled as permanent saving or deferral, the cash it costs, a dated owner-assigned action list, and every threshold or deadline either from the CPA's inputs or marked [VERIFY]. Writes the letter from analysis already done — distinct from building the projection (finance_multi_year_tax_projection) or researching an uncertain position (legal_tax_research_memo)."
techniques:
  - NE-13
  - NE-11
  - DS-40
  - QA-04
  - QA-20
difficulty: advanced
tags:
  - cpa
  - tax-strategy-letter
  - year-end-tax-planning
  - client-advisory-letter
  - small-business-tax
  - explain-tax-strategy-to-client
updated: "2026-10-06"
related_prompts:
  - domain-finance/tax-planning/finance_multi_year_tax_projection.md
  - domain-finance/tax-planning/finance_entity_structure_tax_comparison.md
  - domain-legal/tax/legal_tax_research_memo.md
  - client-services-studio/verticals/cpa/README.md
---

# CPA Year-End Tax Strategy Letter

**Objective:** Turn a CPA's completed year-end analysis into a letter a business owner can act on — what to do, why it applies to *them*, what it saves or merely defers, what it costs in cash, and who does what by when.

**When to Use:**
- Q4 planning is done and the client needs the recommendations in writing before year-end deadlines.
- Several strategies are in play and the client must choose, fund, or supply facts for each.
- The client asked about a strategy (a vehicle, a bonus, a retirement plan) and the answer — yes or no — needs a written rationale.
- `client-services-studio/verticals/cpa/` Stage 5 needs the strategy document that sits inside the engagement proposal; this prompt writes that section.
- **Not this prompt if** you still need the numbers — build them with `domain-finance/tax-planning/finance_multi_year_tax_projection.md` (or `finance_entity_structure_tax_comparison.md` for an entity change) and bring the output here. If a position is uncertain enough to need authority and a confidence level, that is `domain-legal/tax/legal_tax_research_memo.md`; this letter summarises its conclusion, it does not replace it.

**Audience:** A business owner who is financially literate but not a tax specialist. They need the decision, the cash consequence, and the deadline — and enough of the "why" to trust it and explain it to a partner or spouse. The CPA signs and owns the letter; this prompt drafts it for the CPA's review.

## Inputs / Context

Paste source material inside the named tags and refer to it by tag name.

1. **Client and entity** — legal name, entity type and tax classification, industry, owners and ownership %, state(s) of filing, number of employees (full- and part-time) — in `<client_profile>`.
2. **Current-year position** — the CPA's projection: taxable income, federal and state marginal rates, estimated payments made, changes from last year — in `<projection>`. Rates come from here, never from a bracket table recalled by the model.
3. **Strategies identified** — for each: what it is, the client facts that make it eligible, the estimated effect, the cash required, the deadline, and the risk — in `<strategies>`. Include strategies considered and rejected.
4. **Thresholds, limits, and deadlines** the CPA has confirmed for this year — in `<confirmed_rules>`. Anything not here is marked `[VERIFY]`.
5. **Action items** — what the client, the CPA's firm, and any third party (payroll provider, plan administrator, bank) must do, and by when.
6. **Scope note** — what this letter does not cover (e.g. personal return, other entities), and that client-provided figures were not audited.

## Method

1. **Lead with the bottom line (NE-13).** One paragraph: the number of actions, the estimated combined effect, how much of it is permanent vs. deferred, the cash required, and the first deadline.
2. **Gate each strategy on eligibility.** For every recommendation, list the client facts it depends on (entity classification, employee count, business-use %, placed-in-service date, state availability of an election). If a fact is missing from `<client_profile>`, the strategy becomes a question for the client, not a recommendation.
3. **Compute and label every effect (NE-11).**
   - `Estimated effect = deduction or income shift × marginal rate from <projection>` — federal and state separately; state only if the state conforms.
   - Label each **Permanent** (tax not owed later) or **Deferral** (tax moved to a later year — retirement contributions, accelerated depreciation).
   - Strategies interact: a combined figure must come from re-running the projection with all strategies applied, not from summing separate estimates. If the rerun is not available, present the sum as an upper bound.
4. **Show the cash.** For each strategy, the cash out the door and when. A deduction that spends $1 to save $0.40 is a business decision first.
5. **Close the rejected options.** Anything the client raised or the CPA considered and set aside gets one line on why — it prevents the question returning in December.
6. **Extract dated actions (DS-40).** Each action: owner, task, deadline, what happens if missed.
7. **Verify before drafting (QA-04).** Every dollar amount traces to `<projection>` or `<strategies>`; every limit, threshold, phase-out, election, or deadline is in `<confirmed_rules>` or carries `[VERIFY: <rule>, <tax year>, IRS/state source]`. Produce a CPA review sheet listing every `[VERIFY]` — it is not sent to the client.

## Output Format

```
[Firm letterhead]                                         [Date]
[Client name, address]
Re: [Tax year] year-end tax strategy — [Entity]

## The short version
[Actions count · combined estimated effect · permanent vs deferred · cash required · first deadline]

## Where you stand for [year]
[Projected taxable income, marginal rates, payments made, what changed — from <projection>]

## Recommendations
### [n]. [Strategy in plain words]
- Why it fits you: [the eligibility facts]
- Estimated effect: [$ federal / $ state] — [Permanent | Deferral]
- Cash required: [$, when]
- Deadline: [date or VERIFY]
- What could change it: [risk, dependency]

## Combined effect
[Rerun figure vs. sum of separate estimates]

## Considered and not recommended
[Item — one-line reason]

## Action items
| # | Who | What | By | If missed |

## What this letter relies on
[Client-provided figures not audited; scope exclusions; conditions]

[Closing; CPA signature, credential]

--- CPA REVIEW SHEET (do not send) ---
[Every VERIFY item; every figure and its source tag]
```

## Verification

- [ ] Every rate used appears in `<projection>`; no bracket or rate is supplied by the model.
- [ ] Every recommendation lists the client facts that make it eligible, and each fact is in `<client_profile>`.
- [ ] Every effect is labelled Permanent or Deferral; state benefit is omitted or `[VERIFY]` where conformity is unconfirmed.
- [ ] Each effect recomputes from its deduction × rate as stated.
- [ ] The combined figure comes from a projection rerun, or is labelled an upper bound.
- [ ] Every action has an owner and a date; every limit and deadline is confirmed or `[VERIFY]`.
- [ ] Rejected options the client raised are answered.

## False-Positive Prevention

1. **A limit or deadline recalled rather than confirmed.** Contribution limits, depreciation caps, election due dates, and phase-outs change by year and by statute. A plausible number in a signed letter is worse than a visible `[VERIFY: 2026 limit, IRS source]`.
2. **Recommending what the client is not eligible for.** A solo-style retirement plan for an entity with part-time employees, a vehicle deduction with no business-use log, a state election the state does not offer — each reads well and fails on one missing fact. No eligibility fact, no recommendation.
3. **Deferral sold as savings.** Accelerated depreciation and pre-tax retirement contributions move tax to a later year. Calling them "savings" sets an expectation the next return will break.
4. **Summed estimates presented as the total.** Deductions lower the rate the next deduction saves at and can shrink other deductions tied to income. The sum of separate estimates overstates the combined effect.
5. **State benefit assumed to follow federal.** Many states decouple from federal depreciation or treat elections differently; count state benefit only where `<confirmed_rules>` says the state conforms.
6. **Tax saved with cash the client does not have.** A December purchase that cuts tax by $21,000 also spends $60,000. Leave the cash line out and the letter recommends a liquidity problem.
7. **An action with no owner.** "Establish the plan by year-end" without naming whether the client, the firm, or the plan administrator does it is how deadlines are missed by everyone.

## Dual-Failure Prevention (QA-20)

- **Harmful:** confident recommendations resting on an unverified limit or an unconfirmed eligibility fact — the client acts, the position fails on review, and the letter is the evidence.
- **Unhelpful:** a letter so hedged ("you may wish to consider discussing whether…") that the client cannot tell what to do, or a page of Code citations the owner cannot use.
- **Bar:** the owner can say, after one read, what to do this month, what it costs in cash, how much is a real saving versus a postponement — and every number in the letter has a source tag on the review sheet.

## Example Output

```
Ortiz & Wren CPAs                                         6 October 2026
Dana Ortiz, Harbor Lane Design LLC (S corporation), Portland
Re: 2026 year-end tax strategy — Harbor Lane Design LLC

## The short version
Three actions. Run together in our projection they reduce your 2026 tax by an
estimated $45,900. About $7,900 of that is a permanent saving; the rest is
deferral — tax you will pay in later years. Together they need about $106,000
of cash before 31 December. The first deadline is 15 November.

## Where you stand for 2026
Projected net business income passing to you: $412,000 (up from $338,000 in
2025, mainly the Lakeview contract). Our projection puts your federal marginal
rate at 35% and your state rate at 5.5%. Estimated payments to date: $96,000.

## Recommendations
### 1. Start a 401(k) profit-sharing plan and contribute $46,000 for you
- Why it fits you: S corporation with W-2 salary to you of $160,000; your two
  part-time employees each work under the plan's service threshold
  [VERIFY: eligibility rule in plan document with administrator].
- Estimated effect: $46,000 × 40.5% (35% + 5.5%) = $18,630 — Deferral.
- Cash required: $46,000, deposited by the plan deadline.
- Deadline: adopt the plan by 15 November (our target; legal deadline
  [VERIFY: 2026 adoption deadline]); contribution amount within
  [VERIFY: 2026 §415(c) and deduction limits].
- What could change it: if either employee crosses the service threshold, the
  plan must cover them — cost to be quoted by the administrator.
### 2. Buy and install the planned workstations and plotter in December, not February
- Why it fits you: purchase already budgeted for 2027; 100% business use.
- Estimated effect: $60,000 × 35% = $21,000 federal — Deferral (the same
  deduction would otherwise arrive in 2027). State: not counted
  [VERIFY: state conformity to 2026 federal expensing].
- Cash required: $60,000 in December.
- Deadline: delivered and set up for use by 31 December — ordered is not enough
  [VERIFY: placed-in-service rule].
### 3. Elect the state pass-through entity tax for 2026
- Why it fits you: your state tax on this income, about $22,700, would be paid by
  the company and deducted federally instead of by you personally.
- Estimated effect: $22,700 × 35% = $7,945 — Permanent.
- Cash required: none extra — replaces your personal state estimate.
- Deadline: [VERIFY: 2026 election and payment deadline, state revenue dept].

## Combined effect
Separate estimates sum to $47,575 (18,630 + 21,000 + 7,945). With all three run
together in our projection the figure is $45,900 — we quote the lower number.

## Considered and not recommended
Heavy SUV before year-end: no mileage log supports business use, and it would
spend about $70,000 to save tax on part of it.

## Action items
| # | Who      | What                                          | By     | If missed |
| 1 | Dana     | Confirm both employees' 2026 hours            | 20 Oct | Plan design stalls |
| 2 | Our firm | Engage plan administrator; send plan document | 1 Nov  | Item 1 lost for 2026 |
| 3 | Dana     | Sign plan document                            | 15 Nov | Item 1 lost for 2026 |
| 4 | Dana     | Place equipment order; confirm Dec install    | 30 Nov | Deduction moves to 2027 |
| 5 | Our firm | File PTET election; reset Q4 estimates        | [VERIFY] | Item 3 lost |

## What this letter relies on
Figures you supplied through 30 September, which we have not audited. Covers
Harbor Lane only — not your personal return beyond the pass-through effect.

Sincerely, Maya Wren, CPA

--- CPA REVIEW SHEET (do not send) ---
VERIFY: plan adoption deadline; §415(c)/deduction limits; part-time eligibility
rule; placed-in-service rule; state expensing conformity; PTET deadline.
Sources: $412,000, 35%, 5.5%, $22,700, $45,900 → <projection> v3 (rerun 5 Oct).
```

## Techniques Used

- **NE-13 Technical-to-Business Translation** — strategies stated as decision, cash, and deadline before mechanics.
- **NE-11 Embedded Calculation Formulas** — deduction × marginal rate, with the combined figure from a projection rerun.
- **DS-40 Follow-Up Action Extraction** — owner, task, date, and consequence for each action.
- **QA-04 Uncertainty Acknowledgment** — `[VERIFY]` on every unconfirmed limit and deadline, collected on the review sheet.
- **QA-20 Dual-Failure Quality Test** — neither unverified confidence nor disclaimer-heavy hedging.

## Related Prompts

- `domain-finance/tax-planning/finance_multi_year_tax_projection.md` — produces the projection and marginal rates this letter cites.
- `domain-finance/tax-planning/finance_entity_structure_tax_comparison.md` — when the strategy is an entity or election change.
- `domain-legal/tax/legal_tax_research_memo.md` — authority and confidence for a position the letter only summarises.
- `client-services-studio/verticals/cpa/README.md` — engagement pipeline that uses this prompt as its advisory deliverable writer.
