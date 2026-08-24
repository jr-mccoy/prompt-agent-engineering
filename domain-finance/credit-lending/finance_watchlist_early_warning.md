---
title: "Watchlist & Early-Warning Indicators — Trigger Design and Escalation"
category: finance/credit-lending
description: "Design an early-warning indicator set and watchlist trigger framework for a credit portfolio: define financial, behavioral, and external signals, set escalation thresholds and actions, and rank exposures by deterioration risk — evidence-based, no invented data."
techniques:
  - DS-02
  - RT-05
  - NE-10
  - QA-02
  - OC-01
difficulty: intermediate
tags:
  - early-warning
  - watchlist
  - portfolio-monitoring
  - credit-deterioration
  - escalation
  - triggers
updated: "2026-06-08"
related_prompts:
  - domain-finance/credit-lending/finance_covenant_headroom_monitor.md
  - domain-finance/credit-lending/finance_workout_restructuring_options.md
  - domain-finance/credit-lending/finance_pd_lgd_ead_framing.md
  - domain-finance/field_guide.md
---

*For informational purposes only. Not financial, credit, or lending advice. Watchlist classification and remedial action require qualified credit-officer judgment.*

## Objective

Design an early-warning system for a credit or portfolio: define the financial, behavioral, structural, and external indicators that signal deterioration; set measurable trigger thresholds and the escalation action each trigger drives; and rank exposures by deterioration risk so attention goes where it matters. Triggers are computed from user-supplied data; thresholds are stated, not invented, and signals are evidence-based rather than impressionistic.

## When to Use

- Standing up a watchlist / early-warning framework for a loan portfolio
- Periodic portfolio review to identify deteriorating credits before default
- Defining the monitoring section of a credit memo (`finance_credit_memo_builder.md`)
- Triaging which exposures need a workout assessment (`finance_workout_restructuring_options.md`)
- Reviewing whether an existing trigger set catches the right signals

## Inputs / Context Required

Provide as much as available; missing items are flagged, not invented.

**Per-exposure data**
- Financial trend: revenue, EBITDA, leverage, DSCR, liquidity, working capital
- Covenant headroom and recent test results
- Behavioral signals: payment delays, overdraft/utilization spikes, late reporting
- Structure: maturity wall, refinancing dependence, collateral value trend

**External / sector**
- Industry stress indicators the user supplies (sector spreads, demand signals)
- Any rating actions, news, or counterparty events provided

**Framework**
- Watchlist categories / grades to use (e.g., Pass / Watch / Special Mention / Substandard) — state them; otherwise `[ASSUMED SCALE]`
- Escalation governance: who acts at each level, reporting cadence
- Reporting currency and period

## Constraints

### Must
- Define each indicator with a measurable trigger threshold computed from supplied data (DS-02).
- Map each trigger to a specific escalation action and owner (OC-01).
- Use forward-looking signals where possible (RT-05): leading indicators ahead of lagging defaults.
- Cross-check (QA-02) that triggers are not redundant or conflicting, and that a single benign fluctuation does not over-escalate.
- State the watchlist scale used; never map to an external agency rating.
- Flag assumed thresholds with `[ASSUMED]`; do not invent sector benchmarks.

### Must Not
- Invent financial data, sector benchmarks, or rating actions.
- Set a trigger so loose it never fires or so tight it fires on noise.
- Escalate on a single lagging indicator without corroboration.
- Map watchlist grades to agency ratings.
- Treat one bad data point as deterioration without trend context.

## Instructions

1. **Define the indicator taxonomy.** Group signals into financial, behavioral, structural, and external categories. For each candidate indicator, state what risk it leads.

2. **Set measurable triggers.** For each indicator, define the threshold and direction from supplied data:
```
Leverage trigger      = Net Debt / EBITDA  rises above [threshold]x or +X.Xx QoQ
DSCR trigger          = DSCR falls below [threshold]x
Covenant headroom     = Headroom % falls below [threshold]% (link to headroom monitor)
Liquidity runway      = (Cash + Revolver) / Monthly Burn < [threshold] months
Payment behavior      = Days past due > [threshold] or N late payments in M months
Utilization spike     = Revolver utilization > [threshold]% or +Xpp MoM
Reporting delinquency = Financials > [threshold] days late
```

2a. Use trend, not a single point: require a sustained move (e.g., two consecutive periods) before a hard escalation.

3. **Compute composite deterioration score.** Weight the fired triggers into a score per exposure:
```
Deterioration Score = Σ (Indicator Weight x Trigger Fired[0/1])
Rank exposures by score; map score bands to watchlist grades.
```

4. **Map triggers to escalation actions.** For each watchlist level, define the action, owner, and cadence (e.g., Watch -> increased reporting; Special Mention -> site visit + revised projections; Substandard -> workout referral).

5. **Cross-check the trigger set.** Confirm indicators are not double-counting the same risk and that thresholds avoid both noise (over-firing) and blind spots (under-firing). Note any indicator that requires data not supplied.

6. **Forward look.** Project which exposures are likely to cross a trigger next period under base / downside / severe, using internally consistent driver assumptions.

## Output Format

### Indicator Set & Triggers
| Category | Indicator | Trigger Threshold | Direction | Lead/Lag | Data Available? |
|---|---|---|---|---|---|
| Financial | Net Leverage | > [x]x | rising | leading | yes/no |
| Financial | DSCR | < [x]x | falling | leading | |
| Covenant | Headroom % | < [x]% | falling | leading | |
| Liquidity | Runway months | < [x] | falling | leading | |
| Behavioral | Days past due | > [x] | rising | lagging | |
| Behavioral | Utilization | > [x]% | rising | leading | |
| External | Sector signal | [supplied] | — | leading | |

### Per-Exposure Deterioration Ranking
| Exposure | Triggers Fired | Deterioration Score | Current Grade | Trend |
|---|---|---|---|---|
| ... | [list] | X | Watch/SM/Substandard | worsening/stable |

### Escalation Matrix
| Watchlist Level | Entry Trigger(s) | Action | Owner | Cadence |
|---|---|---|---|---|
| Watch | [composite] | enhanced monitoring | RM | monthly |
| Special Mention | [composite] | revised projections + site visit | Credit Officer | bi-weekly |
| Substandard | [composite] | workout referral | Workout team | weekly |

### Forward Trigger Projection (base / downside / severe)
| Exposure | Likely Next Trigger | Base | Downside | Severe |
|---|---|---|---|---|
| ... | DSCR < x | no | yes | yes |

### Cross-Check Notes
[Redundant/conflicting triggers, data gaps, noise-vs-signal calibration]

## Verification

- [ ] Each indicator has a measurable trigger computed from supplied data.
- [ ] Triggers require trend (sustained move), not a single data point, before hard escalation.
- [ ] Each trigger maps to a specific action, owner, and cadence.
- [ ] Leading indicators are distinguished from lagging ones.
- [ ] Deterioration score and ranking are shown with weights.
- [ ] Watchlist scale is stated; no agency-rating mapping.
- [ ] Assumed thresholds flagged `[ASSUMED]`; no invented sector benchmarks.
- [ ] Cross-check addresses redundancy, conflicts, and data gaps.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Escalating on one noisy data point | Triggers require sustained (multi-period) movement for hard escalation |
| Over-relying on lagging indicators (default already near) | Leading indicators prioritized and tagged |
| Inventing sector benchmarks to set thresholds | Thresholds supplied or flagged `[ASSUMED]`; not invented |
| Redundant triggers inflating the deterioration score | Cross-check removes double-counting of the same risk |
| Mapping watchlist grade to an agency rating | Internal scale only |
| Trigger set so loose it never fires | Forward projection tests whether triggers would catch a downside |
| Treating missing data as "no signal" | Data gaps flagged, not scored as benign |
