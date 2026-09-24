---
title: "Dashboard Critique — Does Each Tile Answer a Question Someone Acts On, Correctly and Legibly?"
category: data-analytics/experiments-and-reporting
description: "Critique an existing business dashboard tile by tile: the question and owner each tile serves, whether its metric is defined and its number trustworthy, whether the chart form fits the question, whether comparisons and targets give it meaning, and what should be cut — ending in a ranked change list rather than a redesign."
techniques:
  - DT-05
  - DS-25
  - DS-05
  - DS-06
  - QA-21
difficulty: intermediate
tags:
  - dashboard-review
  - business-dashboard
  - data-visualization
  - reporting-quality
  - business-analytics
  - bi-reporting
  - too-many-charts
  - unused-reports
  - confusing-charts
updated: "2026-09-24"
related_prompts:
  - domain-data-analytics/framing-and-metrics/analytics_kpi_tree_decomposition.md
  - domain-AI-ML/production-monitoring/mlmonitor_monitoring_dashboard_design.md
  - domain-business-strategy/startup/solo_dev_metrics_dashboard.md
---

# Dashboard Critique

**Objective:** Review an existing business dashboard and produce a ranked list of
changes — cut, fix, redefine, or re-chart — so that every remaining tile answers a
question someone acts on, with a number they can trust.

**When to Use:**
- A dashboard exists, is opened rarely, and nobody can say what decision it supports.
- Stakeholders argue about what a tile means, or quote different numbers from it.
- A dashboard has grown past twenty tiles and needs pruning before a redesign.
- Before promoting a team dashboard to an exec or board audience.

**When NOT to use:**
- You are designing a new dashboard from scratch — `domain-agentic-resources/skills/data-engineering/kpi-dashboard-design/`
  covers metric selection, layout hierarchy, and implementation patterns.
- It is an ML model-monitoring dashboard — `domain-AI-ML/production-monitoring/mlmonitor_monitoring_dashboard_design.md`.
- You need a solo developer's 5–7 metric dashboard set up — `domain-business-strategy/startup/solo_dev_metrics_dashboard.md`.
- Infrastructure observability panels — `domain-agentic-resources/skills/observability/grafana-dashboards/`.
- You need the findings turned into a presentation narrative — `domain-agentic-resources/skills/data-engineering/data-storytelling/`.

## Inputs / Context

1. **The dashboard** — screenshot, export, or tile list with titles, charts, and filters.
2. **Intended audience and cadence** — who opens it, how often, in which meeting.
3. **Usage data** if available — views per tile or per dashboard, last opened.
4. **Metric definitions** behind each tile, or a note that none exist.
5. **Decisions the dashboard is supposed to support.**

## Method

1. **Name the dashboard's job.** One sentence: who uses it, when, to decide what.
   If there is no answer, the first finding is "no stated job" and every tile is judged
   against the job the owner confirms.

2. **Assess each tile on five checks (DT-05).**
   | Check | Question |
   |---|---|
   | Question | What question does this tile answer, and who acts on the answer? |
   | Definition | Is the metric specified (grain, filters, window, time zone)? |
   | Trust | Does the number reconcile with its source or with other tiles showing the same metric? |
   | Form | Does the chart type fit the question? |
   | Context | Is there a comparison — target, prior period, benchmark — that tells the viewer whether this is good? |

3. **Check chart form against question type (DS-25).**
   - Trend over time → line; not a bar per day over 90 days, not a pie.
   - Part of whole at one point → stacked bar or a short sorted bar; pie only for ≤ 3 parts.
   - Ranking → sorted horizontal bar.
   - Single current value → number with comparison and sparkline; a gauge adds nothing.
   - Distribution → histogram or box plot, not an average alone.
   - Dual-axis charts: flag unless both axes are labelled and the scales are defensible.

4. **Check legibility (DS-05).** Axis starts at zero for bars; consistent colours for
   the same series across tiles; units and time window in the tile title; no more than
   about six series per chart; red/green not the only encoding.

5. **Check what the dashboard rewards (QA-21).** Which tiles show a metric that could
   rise without the outcome improving? Is there a counter-metric beside it? Vanity
   totals (cumulative sign-ups, all-time revenue) only ever go up; flag them.

6. **Decide per tile:** Keep, Fix (definition / trust / form / context), Merge, or Cut.
   A tile with no question and no views is cut, not fixed.

7. **Rank the changes (DS-06)** by harm: wrong numbers first, then tiles that mislead,
   then missing context, then form and style.

## Output Format

```
# Dashboard critique — [name]   Audience: [..]   Cadence: [..]

## Job
[who, when, to decide what] — [stated | confirmed with owner | missing]

## Tile assessment
| # | Tile | Question / actor | Definition | Trust | Form | Context | Verdict |
|---|---|---|---|---|---|---|---|

## Ranked changes
| Rank | Tile | Change | Why | Effort |
|---|---|---|---|---|

## Incentive check
## What the dashboard is missing
## Confidence and limits of this review
```

## Verification

- [ ] The dashboard's job is stated, or its absence is the first finding.
- [ ] Every tile has all five checks answered.
- [ ] Every "Trust" pass is backed by a reconciliation, or marked `[not checked]`.
- [ ] Chart-form findings name the question type and the better form.
- [ ] Every tile has a verdict: Keep, Fix, Merge, or Cut.
- [ ] Changes are ranked with wrong numbers first.

## False-Positive Prevention

1. **Taste is not a finding.** "I'd use a different colour" is Style. Findings must
   name a question the tile fails to answer, a wrong number, or a misleading encoding.
2. **Redesigning instead of critiquing.** The output is a change list for this
   dashboard, not a new dashboard. Route a redesign to `kpi-dashboard-design`.
3. **Assuming a number is right because it is on a dashboard.** Reconcile at least the
   headline tiles against source.
4. **Cutting low-view tiles blindly.** A tile opened monthly before a board meeting may
   be the most important one. Check the cadence before cutting.
5. **Flagging every dual-axis or pie chart.** They are occasionally the right form. Flag
   only when the question type calls for something else.
6. **Missing the absent tile.** The most harmful gap is often a counter-metric that is
   not there. List what is missing.
7. **Presenting an inferred usage pattern as measured.** Without usage data, "nobody
   uses this" is a guess; mark it.

## Example Output

```
# Dashboard critique — Growth Weekly   Audience: Growth leads + VP Marketing   Cadence: Monday review

## Job
Decide where to shift next week's acquisition budget and which funnel step to work on — confirmed with owner.

## Tile assessment
| # | Tile | Question / actor | Definition | Trust | Form | Context | Verdict |
|---|---|---|---|---|---|---|---|
| 1 | Total sign-ups (all time) | none | ok | ok | big number | none | Cut — vanity |
| 2 | Weekly sign-ups by channel | budget shift / Growth leads | ok | ok | pie, 9 slices | no prior week | Fix form + context |
| 3 | Activation rate | funnel focus / PM | none — 3 versions in use | differs from product dash by 6 pts | line | no target | Fix definition first |
| 4 | CAC by channel | budget shift / VP | ok | paid social excludes agency fees [verify] | sorted bar | target line | Fix trust |
| 5 | Sessions and revenue (dual axis) | unclear | ok | ok | dual-axis line | none | Cut or split |
| 6 | Paid conversion, 12 weeks | funnel / Growth | ok | reconciled | line | prior year | Keep |

## Ranked changes
| Rank | Tile | Change | Why | Effort |
|---|---|---|---|---|
| 1 | 3 | Adopt one activation spec; show its version on the tile | Two teams quote different numbers | M |
| 2 | 4 | Include agency fees in paid-social CAC | Budget decisions made on understated CAC | S |
| 3 | 2 | Replace pie with sorted bar + week-over-week delta | 9-slice pie cannot be compared | S |
| 4 | 1, 5 | Cut | No question, no actor | S |

## Incentive check
Sign-ups (tile 2) with no quality counter-metric rewards cheap low-intent channels.
Add activation rate by channel beside it once tile 3's definition is fixed.

## What the dashboard is missing
Activation by channel; payback period by channel.

## Confidence and limits of this review
Medium. No tile-level usage data was available; cadence from owner interview.
Tile 4 trust issue is inferred from the finance export and needs confirmation.
```

## Techniques Used

- **DT-05 Element-by-Element Assessment Matrix** — every tile is scored on the same five checks.
- **DS-25 Chart Selection Dictionary** — question type maps to the chart form that fits it.
- **DS-05 Visualization and Communication Guidance** — legibility rules for axes, colours, units, and series count.
- **DS-06 Prioritization and Severity Guidance** — changes are ranked by harm, wrong numbers first.
- **QA-21 Metric Gaming Vector Enumeration** — the incentive check finds tiles that reward the wrong behaviour.

## Related Prompts

- `domain-data-analytics/framing-and-metrics/analytics_kpi_tree_decomposition.md` — decide which drivers deserve a tile.
- `domain-AI-ML/production-monitoring/mlmonitor_monitoring_dashboard_design.md` — the ML-monitoring counterpart.
- `domain-business-strategy/startup/solo_dev_metrics_dashboard.md` — a minimal dashboard for a solo developer.
