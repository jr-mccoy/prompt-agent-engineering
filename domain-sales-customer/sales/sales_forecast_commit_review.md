---
title: "Forecast Commit Review — Evidence per Deal for Commit, Best Case and Pipeline, and a Number You Can Defend"
category: sales-customer/sales
description: "Prepare a rep's or manager's forecast call: place each deal closing this period in Commit, Best Case or Pipeline by a stated evidence test rather than by stage or feel, show the one fact that would move each deal between categories, and roll the categories into a committed number with a range and the history-based haircut — distinct from pipeline risk assessment, which triages the whole pipeline for action rather than calling this period's number."
techniques:
  - RT-05
  - AG-02
  - NE-10
  - QA-04
difficulty: advanced
tags:
  - sales
  - forecasting
  - commit
  - pipeline-review
  - sales-management
  - revenue
  - hit-quota
  - deals-slipping
  - boss-wants-number
updated: "2026-09-24"
related_prompts:
  - domain-sales-customer/sales/sales_deal_qualification_scorecard.md
  - domain-sales-customer/sales/sales_mutual_close_plan.md
  - domain-sales-customer/sales/sales_pipeline_risk_assessment.md
---

# Forecast Commit Review

**Objective:** Walk into the forecast call with a number, a range, and — for every
deal in it — the evidence that put it in its category and the event that would
take it out.

**When to Use:**
- Weekly or monthly forecast call, as the rep preparing or the manager rolling up.
- Your commit has missed in either direction in two of the last four periods.
- A leader asks "what's your number?" and you want to answer with deals, not a
  percentage of pipeline.
- End of quarter, when pressure to pull deals forward is highest.
- **Not this prompt if** you need to decide where to spend effort across the
  whole pipeline — stalled deals, single-threading, stage hygiene — use
  `domain-sales-customer/sales/sales_pipeline_risk_assessment.md`.
  To grade whether one deal is qualified at all, use
  `sales_deal_qualification_scorecard.md`. For forecasting as a general
  calibration skill, see `domain-reasoning-craft/forecasting/forecasting_calibration_self_audit.md`.

## Inputs / Context

1. **Deals with a close date in the period:** account, amount, stage, close date,
   times the close date has moved.
2. **Per-deal evidence:** latest buyer contact and what they said, mutual plan
   status, paper-process status, economic-buyer status.
3. **Category definitions your org uses.** If none, the defaults below apply and
   are labelled.
4. **History:** last 4–6 periods' commit versus actual, and win rate by category
   if known.
5. **Target or quota** for the period — used only for the gap line, never to
   place a deal.

## Method

1. **Set the category tests before looking at the deals.**
   - **Commit:** buyer has confirmed the signature date *and* the paper process
     is known and under way *and* the economic buyer has approved. Missing any
     one → not Commit.
   - **Best Case:** qualified, buyer-confirmed timing, one named gate still open.
   - **Pipeline:** close date in period but timing or approval unconfirmed.
   - **Out:** close date moved 3+ times with no new buyer-dated event, or no
     buyer contact in 14 days.

2. **Place each deal on evidence (RT-05).** For each deal, cite the fact that
   meets the test — who said it, when. Stage alone never qualifies a deal for a
   category.

3. **Challenge every Commit (AG-02).** For each deal in Commit, ask: what would
   the buyer have to say this week for this to slip? If you cannot name it, you
   have not looked. Default Commit deals to Best Case until the test is met.

4. **Name the swing fact.** For each deal, the single upcoming event that moves
   it up or down a category, with its date ("security sign-off due 10-24").

5. **Roll up with scenarios (NE-10).**
   - **Commit number** = sum of Commit.
   - **Expected** = Commit × historical Commit conversion + Best Case × its rate.
   - **Range:** low = Commit × conversion; high = Commit + Best Case.
   Show the arithmetic.

6. **Apply the history haircut and state confidence (QA-04).** If commit has
   historically converted at, say, 85%, the call should say so. Confidence in the
   number is stated separately: High / Medium / Low, with the reason.

7. **State the gap honestly.** Target minus expected. List what would close it —
   specific Best Case deals and their swing facts — and do **not** move a deal
   up a category to close it.

8. **Write the call script.** Three lines: the number, what it depends on, and
   what you need (an exec meeting, a legal resource) to protect it.

## Output Format

```
# Forecast — [rep/team] — period [..] — as of [date]
Category tests: [org | default]

## Deals
| Deal | Amount | Category | Evidence meeting the test (who, date) | Swing fact (date) | Close-date moves |

## Roll-up
Commit: $[..]   Best Case: $[..]   Pipeline: $[..]
Historical conversion — Commit [n%] ([source]) · Best Case [n%]
Expected: [arithmetic] = $[..]
Range: $[low] – $[high]
Confidence: [H/M/L] — [reason]

## Gap to target
Target $[..] − Expected $[..] = $[..]; closable by: [deal → swing fact]

## Deals removed or downgraded this week (and why)

## Call script (3 lines)
```

## Verification

- [ ] Category tests stated before any deal is placed.
- [ ] Every Commit deal cites buyer-confirmed date, paper-process status and
      economic-buyer approval.
- [ ] Every deal has one dated swing fact.
- [ ] Expected and range recomputed from the category sums.
- [ ] No deal was moved up to close the gap.
- [ ] Confidence is stated separately from the number.

## False-Positive Prevention

1. **Stage is not a category.** "Negotiation stage" deals are not Commit by
   default; they are Commit when the test is met.
2. **The rep's confidence is not evidence.** "I'm 90% on this one" is a feeling
   to be tested, not a fact to be forecast.
3. **A verbal from the champion is not a signature date.** The date must come
   from someone who can sign, or from the paper process itself.
4. **A close date that has moved three times is telling you something.** It
   stays in the forecast only with a new buyer-dated event.
5. **Quota does not place deals.** Filling the gap by promotion produces a
   number that is right until the last week and wrong at the end.
6. **Sandbagging is also a miss.** Deals that meet the Commit test belong in
   Commit even if the rep would rather under-promise; persistent over-delivery
   is miscalibration, not safety.
7. **One big deal can be the whole forecast.** If one deal is more than 40% of
   Commit, say so and give the number with and without it.
8. **Do not hedge the number into a range only.** The call gives a single
   committed figure *and* a range; a range alone is not a forecast.

## Example Output

```
# Forecast — T. Marsh (Mid-market West) — Q4 — as of 2026-09-24
Category tests: default

## Deals
| Deal | Amount | Cat. | Evidence | Swing fact | Moves |
| Sound Line Logistics | $52,000 | Commit | COO confirmed sign 10-15 (email 09-22); MSA redlines back 09-20; COO = EB, approved 09-18 | PO issued by 10-10 | 0 |
| Pinecrest Foods | $38,000 | Commit | CFO approved (call 09-19); procurement onboarding done 09-23; sign date 10-31 per CFO | DPA signed by 10-17 | 1 |
| Halvorsen Freight | $84,000 | Best Case | Qualified CONDITIONAL; CFO not met; security owner unnamed | Security owner named by 10-08 | 1 |
| Summit Produce | $29,000 | Pipeline | Eval ongoing; no buyer date | Shortlist decision 10-20 | 0 |
| Orca Marine | $41,000 | Out | Close date moved 3×; last contact 09-02 | New buyer-dated event | 3 |

## Roll-up
Commit: $90,000  Best Case: $84,000  Pipeline: $29,000
Historical conversion — Commit 85% (last 4 quarters) · Best Case 40%
Expected: 90,000 × 0.85 + 84,000 × 0.40 = 76,500 + 33,600 = $110,100
Range: $76,500 – $174,000
Concentration: Sound Line is 58% of Commit; without it Expected = 38,000 × 0.85
+ 33,600 = $65,900.
Confidence: Medium — Commit evidence is complete, but one deal carries most of it
and Halvorsen is all of Best Case.

## Gap to target
Target $130,000 − Expected $110,100 = $19,900; closable only by Halvorsen moving
to Commit (swing fact: security owner by 10-08, CFO meeting by 10-10).

## Deals removed or downgraded this week
Orca Marine → Out (3 moves, 22 days without contact). Halvorsen held at Best
Case despite rep asking for Commit: economic buyer not met.

## Call script
"My number is $110k against $130k, range $77k to $174k. It depends on Sound Line's
PO by 10-10 and Pinecrest's DPA by 10-17. To get to target I need Halvorsen's
CFO meeting — I'd like you on that call the week of 10-06."
```

## Techniques Used

- **RT-05 Evidence-Based Reasoning** — each placement cites a dated buyer fact.
- **AG-02 Skeptical Default Stance** — Commit is earned, and challenged every call.
- **NE-10 Probability-Weighted Scenarios** — expected value and range from category rates.
- **QA-04 Uncertainty Acknowledgment** — confidence reported apart from the number.

## Related Prompts

- `domain-sales-customer/sales/sales_deal_qualification_scorecard.md` — the
  qualification verdict behind each Best Case deal.
- `domain-sales-customer/sales/sales_mutual_close_plan.md` — gate status is the
  swing fact for most deals.
- `domain-sales-customer/sales/sales_pipeline_risk_assessment.md`
  — whole-pipeline triage and effort allocation.
