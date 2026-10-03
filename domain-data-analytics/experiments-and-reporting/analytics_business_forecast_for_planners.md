---
title: "Operational Volume Forecast for Planners — Baseline, Seasonality, Known Events, a Range, and Forecast-Error Tracking"
category: data-analytics/experiments-and-reporting
description: "Build an explainable forecast of an operational volume — orders, tickets, calls, shipments, appointments — that a planner can staff or stock against: a clean history, a baseline level and trend, weekly and annual seasonality as indices, known events added as separate owned lines, a range from measured past error, and a tracking table of bias and WMAPE that tells you when the method needs changing."
techniques:
  - NE-11
  - QA-04
  - RT-23
  - QA-02
difficulty: intermediate
tags:
  - volume-forecast
  - demand-forecast
  - seasonality
  - forecast-accuracy
  - workforce-planning
  - business-planning
  - how-many-orders-next-month
  - how-many-staff-do-we-need
  - plan-for-peak-season
updated: "2026-10-02"
related_prompts:
  - domain-finance/corporate-finance-fpa/finance_rolling_forecast_designer.md
  - domain-AI-ML/specialized-ml/time-series/ts_forecasting_model_selection.md
  - domain-data-analytics/analysis-and-sql/analytics_metric_movement_investigation.md
---

# Operational Volume Forecast for Planners

**Objective:** Produce a volume forecast a planner can act on — weekly or daily, with
a range — built from components each stakeholder can inspect and challenge, and a
tracking loop that measures whether it is any good.

**When to Use:**
- A support, operations, or fulfilment lead needs next quarter's volume to set
  staffing, shifts, or stock, and the current method is "last year plus 10%".
- Peak season is coming and the plan needs a defensible number and a high case.
- Forecasts keep missing and nobody knows whether it is the method or one-off events.
- You need something a spreadsheet can hold and a manager can explain, not a model
  only a data scientist can run.

**When NOT to use:**
- The forecast is of **revenue, costs, or the P&L**, or you are designing the
  finance team's re-forecast cadence —
  `domain-finance/corporate-finance-fpa/finance_rolling_forecast_designer.md`. This
  prompt forecasts operational volumes (orders, tickets, calls, units) that drive
  staffing and capacity; finance may convert them to money afterwards.
- You are forecasting hundreds or thousands of series, intermittent demand, or need
  an ML or probabilistic model chosen and back-tested — start at
  `domain-AI-ML/specialized-ml/time-series/ts_forecasting_model_selection.md`.
- Volume already moved and the question is why —
  `domain-data-analytics/analysis-and-sql/analytics_metric_movement_investigation.md`.
- Monthly family-level demand/supply reconciliation across sales, ops, and finance is
  `domain-operations/supply-chain-procurement/ops_sales_and_operations_planning_cycle.md`;
  this prompt can supply its baseline.

## Inputs / Context

1. **History**: at least 2 years of daily or weekly volume for the series, so annual
   seasonality is seen twice. Tag `queried` with the source table and definition.
2. **The planning decision**: what will be set from the forecast (agents per interval,
   shifts per week, stock), its lead time, and the cost of under vs. over.
3. **Calendar**: holidays, promotions, price changes, launches, outages, policy
   changes — past (to clean history) and future (to add as events).
4. **Structural changes**: new channels, product launches, a self-service deflection
   tool, market entry — with dates.
5. **Past forecasts**, if any, to measure the method being replaced.

## Method

1. **Clean the history.** Mark weeks distorted by one-off events (outage, data
   loss, a one-time recall). Replace them with the seasonal expectation for modelling,
   and keep the original. Check the volume definition did not change.
2. **Baseline level and trend (NE-11).** De-seasonalise and fit level and trend on
   the most recent 26–52 weeks: e.g. `trend = (avg last 13 wk − avg same 13 wk last
   year) / 52` per week, or a linear fit. Prefer a damped or flat trend beyond the
   first quarter; extrapolated growth is the most common forecast error.
3. **Seasonality as indices.** Annual: `index_week = avg(volume_week / centred
   52-week average)` across years. Weekly: day-of-week share. Intraday if staffing by
   interval. Indices should average 1.0; check.
4. **Forecast = baseline × annual index × day share + event lines.** Each known
   future event is a separate line with owner, assumption, and the evidence for its
   size ("+18% for 3 days, based on last two Black Fridays"), not folded into the
   baseline.
5. **Tag every input (RT-23).** `[data]` queried history; `[estimate]` derived
   indices and trend; `[guess]` event sizes without precedent. Count guesses per
   period; periods dominated by guesses get a wider range.
6. **Range from measured error (QA-04).** Back-test the method on the last 26–52
   weeks (forecast each week from data available at the time); take the 80% band of
   percentage errors and apply it to the forecast. Planning cost asymmetry decides
   which point to plan to: if being short is worse than being over (missed SLAs), plan
   at the P70–P80, and say so.
7. **Stress-test (QA-02).** Compare against two naive benchmarks — same week last year,
   and last 4 weeks' average — on the back-test. If the method does not beat both,
   use the simpler one.
8. **Tracking loop.** Weekly: actual vs. forecast, bias (`Σ(F − A)/ΣA`) and WMAPE
   (`Σ|F − A|/ΣA`) on a rolling 8 weeks. Rules: bias beyond ±5% for 4 weeks →
   re-level the baseline; WMAPE worse than the naive benchmark for 8 weeks → change
   method; miss explained by an event → log it for next year's event line.

## Output Format

```
# Volume forecast — [series]   Grain: [daily/weekly]   Horizon: [..]   Made: [date]
Decision served: [..]   Plan to: [P50 | P70 | P80] because [cost asymmetry]

## History and cleaning
Source: [table, definition]  Period: [..]  Weeks adjusted: [list, reason]

## Components
Baseline level: [..]  Trend: [..]/wk (damped after [..])
Annual index (excerpt): | Week | Index |   Day-of-week share: | Mon … Sun |
Event lines: | Event | Dates | Effect | Evidence | Owner | Tag |

## Forecast
| Period | Baseline × index | Events | Forecast P50 | P10–P90 | Plan value | Guess count |

## Back-test
Method WMAPE [..]  Bias [..]   Naive LY WMAPE [..]   Naive 4-wk WMAPE [..]

## Tracking rules
| Trigger | Action |
```

## Verification

- [ ] At least two years of history, or the annual index is labelled weak.
- [ ] Cleaned weeks are listed with reasons; originals kept.
- [ ] Seasonal indices average 1.0.
- [ ] Events are separate lines with owner and evidence, not hidden in the baseline.
- [ ] The range comes from back-tested error, not a guessed ±%.
- [ ] The method beats both naive benchmarks, or the simpler benchmark is used.
- [ ] Bias and WMAPE tracking rules are stated with thresholds.

## False-Positive Prevention

1. **Growth extrapolated.** A trend fitted on a growth spurt compounds into an
   impossible peak. Damp it and show the flat-trend alternative.
2. **Last year's one-offs as seasonality.** An outage week in last year's history
   becomes a dip in this year's forecast unless cleaned.
3. **Events double counted.** If last year's promotion is in the index and also added
   as an event line, the peak is counted twice. Clean the event out of the index.
4. **A point forecast for staffing.** Staffing to P50 means being short half the
   time. Choose the plan point from the cost of being short.
5. **WMAPE without a benchmark.** 12% sounds good until "same week last year" scores 10%.
6. **Accuracy measured on the fit.** In-sample error flatters. Use the back-test.
7. **Volume definition drift.** A new ticket category or channel changes the series;
   check the definition before blaming the forecast.

## Example Output

```
# Volume forecast — Inbound support contacts (all channels)   Grain: weekly   Horizon: 13 wk
Made: 2026-10-02   Decision: agent hiring for Nov–Dec (6-wk lead time)
Plan to: P75 — a missed SLA week costs more than ~3 idle agent-weeks.

## History and cleaning
Source: fct_contacts, definition v3 (excludes spam). Period: Oct 2023 – Sep 2026 [data].
Adjusted: wk 2025-31 (outage spike +62%), replaced with seasonal expectation.

## Components
Baseline (de-seasonalised, last 13 wk): 9,400/wk [estimate]
Trend: +40/wk, damped to 0 after wk 6 [estimate]
Annual index (2 yr avg): wk 46 0.98 | wk 47 1.08 | wk 48 1.31 | wk 49 1.12 | wk 52 0.74 [estimate]
Event lines:
| Help-centre chatbot launch | from wk 45 | −6% | vendor pilot: −5 to −8% | Support ops | [guess] |
| Black Friday promo          | wk 48     | already in index (2 yrs) — not added | — | — | — |

## Forecast (excerpt)
| Wk | Baseline × index         | Events | P50    | P10–P90        | Plan (P75) | Guesses |
| 46 | (9,400+240) × 0.98 = 9,447  | −567   | 8,880  | 7,990–9,770    | 9,350  | 1 |
| 47 | (9,400+240) × 1.08 = 10,411 | −625   | 9,790  | 8,810–10,770   | 10,310 | 1 |
| 48 | (9,400+240) × 1.31 = 12,628 | −758   | 11,870 | 10,680–13,060  | 12,500 | 1 |
Range: back-test 80% band of errors −10% / +10% (≈ normal, σ ≈ 7.8%);
P75 ≈ +0.674σ ≈ +5.3%.

## Back-test (52 weeks, as-of forecasts)
Method WMAPE 6.8%, bias +1.2%.  Naive LY WMAPE 11.4%.  Naive 4-wk WMAPE 14.9%. → method kept.

## Tracking rules
| Bias beyond ±5% for 4 wk          | re-level baseline |
| WMAPE > 11.4% for 8 wk             | revert to naive LY and review method |
| Chatbot effect outside −3% to −10% by wk 48 | re-estimate event line; tell hiring |
```

## Techniques Used

- **NE-11 Embedded Calculation Formulas** — baseline, trend, seasonal indices, the forecast product, bias and WMAPE.
- **QA-04 Uncertainty Acknowledgment** — the range from back-tested error and an explicit plan percentile.
- **RT-23 Input Provenance Tagging** — data, estimate, and guess tags with a guess count per period.
- **QA-02 Adversarial Stress-Test** — the method must beat two naive benchmarks or be replaced by them.

## Related Prompts

- `domain-finance/corporate-finance-fpa/finance_rolling_forecast_designer.md` — the P&L re-forecast process that consumes volume drivers.
- `domain-AI-ML/specialized-ml/time-series/ts_forecasting_model_selection.md` — choosing statistical or ML models for many or harder series.
- `domain-data-analytics/analysis-and-sql/analytics_metric_movement_investigation.md` — explaining a volume that already moved.
