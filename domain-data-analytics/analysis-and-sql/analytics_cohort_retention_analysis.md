---
title: "Cohort Retention Analysis — Define the Cohort, the Return Event, and the Clock; Then Read the Triangle"
category: data-analytics/analysis-and-sql
description: "Run a cohort retention analysis a decision can rest on: choose the cohort key, the return event and the period clock on purpose, build the retention triangle with censoring handled, separate logo from revenue retention, read it along cohorts, periods and calendar diagonals, and flag the small-cohort and mix effects that make a curve look better or worse than it is."
techniques:
  - DS-02
  - NE-11
  - RT-06
  - QA-04
  - DS-05
difficulty: intermediate
tags:
  - cohort-analysis
  - retention-curve
  - churn-analysis
  - business-analytics
  - survival-curve
  - revenue-retention
  - customers-leaving
  - users-come-back
  - after-pricing-change
updated: "2026-09-24"
related_prompts:
  - domain-data-analytics/framing-and-metrics/analytics_metric_definition_spec.md
  - domain-data-analytics/analysis-and-sql/analytics_sql_query_correctness_review.md
  - domain-presentations/board-decks/boarddeck_cohort_retention_heatmap.md
---

# Cohort Retention Analysis

**Objective:** Build and interpret a retention triangle whose cohort key, return
event, and clock are chosen deliberately, so a claim like "newer cohorts retain
better" survives a check for censoring, cohort size, and mix.

**When to Use:**
- You need to know whether retention is improving, and a single churn rate is hiding it.
- A product or pricing change shipped and you want to see if later cohorts behave differently.
- Finance or leadership asked for logo and revenue retention, and you need both built the same way.
- A retention chart exists but nobody can say what "Month 3" means.

**When NOT to use:**
- You need the board-deck heatmap *visual* rendered — `domain-presentations/board-decks/boarddeck_cohort_retention_heatmap.md`
  renders it; this prompt produces the numbers and the reading.
- You need LTV/CAC and payback — `domain-finance/corporate-finance-fpa/finance_unit_economics_model.md`.
- You need a formal time-to-event model with covariates for research —
  `domain-science/statistics/science_survival_analysis_design.md`.
- A solo app developer's revenue dashboard — `domain-business-strategy/startup/monetization_revenue_analytics.md`.

## Inputs / Context

1. **Entity** — user, account, or subscription — and the table it comes from.
2. **Candidate cohort keys** — signup date, first purchase date, first-value event, acquisition channel.
3. **Candidate return events** — login, core action, paid renewal, revenue.
4. **Data window** and the current date, so censoring can be computed.
5. **Changes during the window** — pricing, onboarding, tracking.
6. **The question** — "is retention improving?", "did the onboarding change help?", "what is NRR?"

## Method

1. **Fix three definitions (DS-02).** Write each as a sentence:
   - **Cohort key** — which date puts an entity in a cohort. Signup cohorts include
     people who never activated; first-value cohorts exclude them. Pick for the question.
   - **Return event** — what counts as retained. Logins retain better than core actions;
     choose the event that matches the value the business cares about.
   - **Clock** — period since cohort start (Day 7, Week 4, Month 3), and whether retention
     is **bounded** ("active in period N") or **unbounded** ("active in N or later").
     Bounded curves can rise; unbounded curves cannot. State which.

2. **Build the triangle (NE-11).**
   - `retention(c, n) = entities in cohort c active in period n / entities in cohort c`
   - Revenue retention: `revenue in period n from cohort c / revenue in period 0 from cohort c`
     (can exceed 100% with expansion).
   - Leave cells that have not fully elapsed **empty**, never zero. The newest cohort's
     Month 3 does not exist yet.

3. **Handle size and weighting.** Show cohort size on every row. Mark cohorts below a
   floor (e.g. n < 200) and never compute the blended curve as a simple average of
   cohort percentages; weight by cohort size.

4. **Read it three ways (RT-06).**
   - **Down a column** (same age, different cohorts): is retention at Month 3 improving over time?
   - **Along a row** (one cohort ageing): where does the curve flatten, and at what level?
   - **Along a diagonal** (same calendar month, different ages): a drop on one diagonal
     is a calendar event (outage, price change) hitting every cohort at once — not a
     cohort-quality change.

5. **Check mix before crediting improvement.** If newer cohorts came from a different
   channel, plan, or region, split by that dimension and compare like with like.

6. **State uncertainty (QA-04).** For the column comparison you rely on, give an interval
   (for proportions, a Wilson or normal-approximation interval is enough) and say whether
   the difference exceeds it.

7. **Specify the visual (DS-05).** Heatmap for the triangle (sequential colour, one
   hue, empty cells visibly blank); line chart of selected cohorts for curve shape.
   Hand the rendering to the board-deck prompt if one is needed.

## Output Format

```
# Cohort retention — [entity], [cohort key], [return event], [clock: bounded|unbounded]

## Definitions
## Triangle
| Cohort | Size | P0 | P1 | P2 | ... |
|---|---|---|---|---|---|
(blank = not yet elapsed; † = cohort below size floor)

## Revenue retention (if applicable)
## Reading
- Down the columns: [...]
- Along the rows: [...]   Flattens at: [period, level]
- Diagonals: [...]
## Mix check
## Uncertainty
## Conclusion — Confidence: [H/M/L]
## Visual spec
```

## Verification

- [ ] Cohort key, return event, and clock are each stated in a sentence.
- [ ] Bounded vs unbounded is stated.
- [ ] Unelapsed cells are blank, not zero.
- [ ] Every row shows cohort size; small cohorts are marked.
- [ ] The blended curve is size-weighted.
- [ ] Diagonals were checked for calendar events.
- [ ] Any "improving" claim has an interval and a mix check.

## False-Positive Prevention

1. **Zeros in unelapsed cells.** They drag the blended curve down and make the newest
   cohorts look like they churned. Leave them blank.
2. **Unweighted average of cohort percentages.** A 40-user cohort at 80% is not equal
   to a 4,000-user cohort at 30%.
3. **Mistaking a diagonal for a trend.** An April outage lowers April's cell for every
   cohort. That is one calendar event, not five worse cohorts.
4. **Signup cohorts after an onboarding change.** If the change moved activation, signup
   cohorts will show "better retention" that is really better activation. Say which you mean.
5. **Revenue retention above 100% read as "no churn".** NRR can exceed 100% while half
   the logos leave. Always show logo retention beside it.
6. **Bounded curves that rise.** In bounded retention, Month 6 can exceed Month 5
   (seasonal returners). That is not an error, but it is not "reactivation" either unless you checked.
7. **Crediting a product change for a mix shift.** Newer cohorts from a better channel
   retain better regardless of the product.

## Example Output

```
# Cohort retention — accounts, first-paid month, ≥1 core action in month, clock: bounded

## Definitions
Cohort key: calendar month of first successful payment.
Return event: ≥1 doc_create or doc_edit by any seat in the month.
Clock: months since first payment; bounded (active in that month).

## Triangle (as of 2026-09-24; Sep not complete)
| Cohort | Size | M0 | M1 | M2 | M3 | M4 | M5 |
|---|---|---|---|---|---|---|---|
| 2026-03 | 820 | 100% | 71% | 62% | 58% | 50% | 55% |
| 2026-04 | 910 | 100% | 72% | 63% | 52% | 56% | |
| 2026-05 | 880 | 100% | 74% | 58% | 61% | | |
| 2026-06 | 1,040 | 100% | 76% | 66% | | | |
| 2026-07 | 1,210 | 100% | 79% | | | | |
| 2026-08 | 160† | 100% | | | | | |
† below 200-account floor (billing migration paused sign-ups mid-August).

## Reading
- Down M1: 71% → 79% over five cohorts.
- Along rows: curves flatten near M3–M4 at ~55–60%.
- Diagonal: the July calendar month is low for every cohort (Mar M4 50%,
  Apr M3 52%, May M2 58%) — matches the 07-08 outage [data]. Not a cohort effect.

## Mix check
Jun–Jul cohorts are 38% annual-plan vs 22% for Mar–Apr [data]. Split by plan:
monthly-plan M1 went 69% → 73%; annual-plan flat at ~84%.

## Uncertainty
Monthly-plan M1, Mar (n=640) vs Jul (n=750): 69% [65–73] vs 73% [70–76] (95% Wilson).
Intervals overlap; the difference is suggestive, not established.

## Conclusion — Confidence: Medium
Most of the M1 improvement is plan mix. A smaller within-plan gain may exist; confirm
with the Aug–Sep cohorts once they pass M1.

## Visual spec
Heatmap, single-hue sequential, blank cells for unelapsed, July diagonal annotated.
Render via boarddeck_cohort_retention_heatmap if it goes to the board.
```

## Techniques Used

- **DS-02 Metric Specification** — cohort key, return event, and clock defined before any number.
- **NE-11 Embedded Calculation Formulas** — the retention formulas are written out, logo and revenue.
- **RT-06 Correlation and Cross-Analysis** — the triangle is read down columns, along rows, and along diagonals.
- **QA-04 Uncertainty Acknowledgment** — intervals and confidence on any "improving" claim.
- **DS-05 Visualization and Communication Guidance** — a specified heatmap and curve chart.

## Related Prompts

- `domain-data-analytics/framing-and-metrics/analytics_metric_definition_spec.md` — specify the return event as a metric.
- `domain-data-analytics/analysis-and-sql/analytics_sql_query_correctness_review.md` — check the triangle query for fan-out and censoring errors.
- `domain-presentations/board-decks/boarddeck_cohort_retention_heatmap.md` — render the heatmap for a board deck.
