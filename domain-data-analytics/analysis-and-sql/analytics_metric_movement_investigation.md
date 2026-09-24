---
title: "Metric Movement Investigation — Why Did the Number Move? Data Quality First, Then Mix, Segments, and Calendar"
category: data-analytics/analysis-and-sql
description: "Investigate a business metric that moved unexpectedly in a fixed order — confirm the move is real, rule out data and definition changes, check calendar effects, separate mix shift from rate change, decompose by segment, then match to known events — and report the explanation with its share of the move, its confidence, and what remains unexplained."
techniques:
  - DD-03
  - RT-10
  - DT-04
  - RT-23
  - QA-04
difficulty: advanced
tags:
  - metric-investigation
  - root-cause-analysis
  - mix-shift
  - segment-decomposition
  - business-analytics
  - anomaly-explanation
updated: "2026-09-24"
related_prompts:
  - domain-data-analytics/framing-and-metrics/analytics_kpi_tree_decomposition.md
  - domain-data-analytics/analysis-and-sql/analytics_sql_query_correctness_review.md
  - domain-engineering-workflows/workflows/engineering_debugging_root_cause.md
---

# Metric Movement Investigation

**Objective:** Answer "why did X drop?" with an explanation that accounts for a stated
share of the move, has been checked against cheaper explanations first, and says
plainly how much is still unexplained.

**When to Use:**
- A metric on a dashboard or in a weekly review moved and someone is asking why.
- An alert fired on a business metric and you need to decide whether it is real.
- A stakeholder has already offered a cause and you need to test it before it spreads.

**When NOT to use:**
- The software is broken and you are debugging code —
  `domain-engineering-workflows/workflows/engineering_debugging_root_cause.md`.
- You are explaining a budget-vs-actual variance for finance close —
  `domain-finance/corporate-finance-fpa/finance_budget_variance_investigator.md`.
- A model's accuracy or drift moved — `domain-AI-ML/production-monitoring/`.
- The metric is undefined or disputed — settle it with `analytics_metric_definition_spec.md` first.

## Inputs / Context

1. **The metric, its spec, and the move** — values for the current and comparison
   periods, and how the move was noticed.
2. **The metric's normal variation** — at least 8 comparable periods of history.
3. **Available dimensions** for slicing (platform, region, plan, channel, cohort).
4. **Change log** — releases, pricing changes, marketing launches, tracking changes,
   pipeline incidents in the window.
5. **Any cause already proposed**, and by whom.

## Method

Run the checks in order, cheapest and most common first (DD-03). Each is a branch in a
decision tree (RT-10): if it explains the move, stop, quantify it, and check whether any
residual remains.

1. **Is the move real?** Compare it with the metric's normal variation. A move inside
   the historical range of period-to-period changes is noise until shown otherwise.
   Check that the comparison periods are complete (no partial week).

2. **Is it the data?** Before any business explanation:
   - row counts and freshness of every source table for the period;
   - duplicate or missing loads (a day with zero or double events);
   - tracking changes: SDK release, event renamed, consent banner, bot filter;
   - definition or code changes to the metric's query.
   If the numerator and the denominator both come from one broken pipeline, a flat
   rate can hide a big volume drop. Check both separately.

3. **Is it the calendar?** Day-of-week composition, holidays, month length, payday
   timing, daylight-saving, a promotion last year that is missing this year. Compare
   against the same period last year, and like-for-like days.

4. **Is it mix or rate? (DT-04)** For a rate metric, split the change into:
   - **rate effect** — rates changed within segments at constant mix;
   - **mix effect** — the population shifted toward segments with different rates.
   Formula for two periods, segment i with share w and rate r:
   `rate_effect = Σ w_i,t0 × (r_i,t1 − r_i,t0)`,
   `mix_effect = Σ (w_i,t1 − w_i,t0) × r_i,t1`.
   The two sum to the total change.

5. **Where is it concentrated?** Decompose by one dimension at a time and rank segments
   by contribution to the total change (not by their own percentage change — a small
   segment can drop 50% and matter little). Avoid slicing until something turns up;
   limit to the dimensions listed in Inputs.

6. **What happened then?** Only now match the concentrated segment and the start date
   to the change log. A cause must match *where* and *when*.

7. **Tag the evidence (RT-23).** Each claim in the explanation is `[data]` (queried),
   `[estimate]` (reasoned from queried facts), or `[guess]` (a hypothesis). No
   `[guess]` goes into the headline.

8. **Report confidence and residual (QA-04).** State how much of the move is
   explained, how confident you are, and the next check that would raise confidence.

## Output Format

```
# Why did [metric] move? — [period] vs [comparison]

## Headline
[metric] moved [a → b] ([Δ]). [Explanation] accounts for ~[x]% of the move. Confidence: [H/M/L].

## Decision tree
| Step | Check | Result | Explains? |
|---|---|---|---|
| 1 | Real vs noise | | |
| 2 | Data / tracking / definition | | |
| 3 | Calendar | | |
| 4 | Mix vs rate | | |
| 5 | Segment concentration | | |
| 6 | Event match | | |

## Decomposition
| Segment | Share t0→t1 | Rate t0→t1 | Rate effect | Mix effect | Contribution |
|---|---|---|---|---|---|

## Explanation with evidence tags
## Unexplained residual
## Proposed causes ruled out
## Next check
```

## Verification

- [ ] The move is compared against at least 8 periods of history.
- [ ] Data freshness, row counts, tracking, and definition changes were checked before any business cause.
- [ ] The calendar check uses like-for-like days.
- [ ] Rate and mix effects sum to the total change.
- [ ] Segments are ranked by contribution to total, not by their own % change.
- [ ] The cause matches both the segment and the start date.
- [ ] The residual is stated as a number.
- [ ] No `[guess]` appears in the headline.

## False-Positive Prevention

1. **Business story before data check.** The most common cause of a sudden move is a
   pipeline or tracking change. Rule it out in writing first.
2. **Mix shift called a rate change.** Conversion "fell" because paid-social traffic
   doubled, and paid social always converts lower. Every segment's rate can be flat.
3. **Simpson's paradox.** Every segment can improve while the total falls. Always
   show the segment rates alongside the total.
4. **Ranking by segment % change.** A segment that is 2% of volume and fell 40% is
   not the story. Rank by contribution.
5. **Slicing until something turns up.** With twenty dimensions, one will show a big
   move by chance. Stick to the pre-listed dimensions, and treat surprises as hypotheses.
6. **Coincident events are not causes.** A release on the same day must also match
   the segment where the drop is concentrated.
7. **Presenting an inferred share as measured.** If the contribution comes from an
   assumption (e.g. a traffic estimate), tag it `[estimate]`.
8. **Explaining 100% by default.** Most real investigations leave a residual. Report it.

## Example Output

```
# Why did checkout conversion move? — week of 2026-09-14 vs prior 4-week average

## Headline
Checkout conversion moved 3.40% → 2.95% (−0.45 pts). A shift in traffic mix toward
paid social accounts for ~92% of the move (−0.41 pts). The remaining −0.04 pts is a
within-segment rate drop in organic traffic, concentrated in the Android app after
release 8.4. Confidence: High on mix, Low on the Android cause.

## Decision tree
| Step | Check | Result | Explains? |
|---|---|---|---|
| 1 | Real vs noise | 8-wk range of weekly changes ±0.15 pts; −0.45 is outside | Real |
| 2 | Data / tracking | Row counts and freshness normal; no SDK change; spec unchanged | No |
| 3 | Calendar | No holiday; same weekday mix; same week last year flat | No |
| 4 | Mix vs rate | Mix −0.41 pts, rate −0.04 pts | Mostly mix |
| 5 | Concentration | Rate effect entirely in organic; within organic, Android only | Partly |
| 6 | Event match | Paid social budget ×2 from 09-12 [data]; Android 8.4 shipped 09-15 [data] | Yes |

## Decomposition (by channel)
| Segment | Share t0→t1 | Rate t0→t1 | Rate effect | Mix effect | Contribution |
|---|---|---|---|---|---|
| Organic/direct | 60% → 50% | 4.20% → 4.14% | −0.036 | −0.414 | −0.450 |
| Paid social | 20% → 35% | 1.10% → 1.10% | 0.000 | +0.165 | +0.165 |
| Email | 20% → 15% | 3.30% → 3.30% | 0.000 | −0.165 | −0.165 |
| **Total** | | 3.40% → 2.95% | −0.036 | −0.414 | −0.450 |

Rate and mix effects sum to the total change. Organic ranks first by contribution
because its *share* fell, not because its rate did — the table shows both.

## Explanation with evidence tags
- Paid social sessions doubled after the 09-12 budget change [data]; that channel
  converts at about a quarter of the organic rate, and did so before the change too [data].
- Within organic, Android app conversion fell 4.3% → 3.9% from 09-15 while iOS and
  web were flat [data]; 8.4 changed the address form [data]; the form is the cause
  [guess — not yet tested against funnel-step data, so it stays out of the headline].

## Unexplained residual
~0.01 pts of the rate effect is not accounted for by Android [estimate]. That is
inside the noise band.

## Proposed causes ruled out
- "The new pricing page" (proposed by Growth): launched 09-02, before the drop, and
  web conversion is flat.

## Next check
Android funnel step by step from 09-15 onward: address-form completion rate against
build 8.3. Separately, tell Growth that the drop is mostly mix: paid-social volume
went up, and its conversion rate did not fall.
```

## Techniques Used

- **DD-03 Fail-Fast Ordering** — cheap, common explanations (noise, data, calendar) are ruled out before expensive ones.
- **RT-10 Troubleshooting Decision Tree** — each check is a branch with a stated result.
- **DT-04 Multi-Layer Analysis** — total → mix vs rate → segment → event.
- **RT-23 Input Provenance Tagging** — every claim is tagged data, estimate, or guess.
- **QA-04 Uncertainty Acknowledgment** — confidence, residual, and the next check are required.

## Related Prompts

- `domain-data-analytics/framing-and-metrics/analytics_kpi_tree_decomposition.md` — find which driver moved before asking why.
- `domain-data-analytics/analysis-and-sql/analytics_sql_query_correctness_review.md` — when the query itself is a suspect.
- `domain-engineering-workflows/workflows/engineering_debugging_root_cause.md` — root cause in software rather than in a metric.
