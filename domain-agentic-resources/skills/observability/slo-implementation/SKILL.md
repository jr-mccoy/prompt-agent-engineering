---
name: slo-implementation
description: Define and implement Service Level Indicators (SLIs) and Service Level Objectives (SLOs) with error budgets and alerting. Use when establishing reliability targets, implementing SRE practices, or measuring service performance.
metadata:
  tags:
    - monitoring
    - observability
    - performance
    - slo
  updated: "2026-10-05"
---
# SLO Implementation

Framework for defining and implementing Service Level Indicators (SLIs), Service Level Objectives (SLOs), and error budgets.

## Purpose

Implement measurable reliability targets using SLIs, SLOs, and error budgets to balance reliability with innovation velocity.

## When to Use

- Define service reliability targets
- Measure user-perceived reliability
- Implement error budgets
- Create SLO-based alerts
- Track reliability goals

## SLI/SLO/SLA Hierarchy

```
SLA (Service Level Agreement)
  ↓ Contract with customers
SLO (Service Level Objective)
  ↓ Internal reliability target
SLI (Service Level Indicator)
  ↓ Actual measurement
```

## Defining SLIs

### Common SLI Types

#### 1. Availability SLI
```promql
# Successful requests / Total requests
sum(rate(http_requests_total{status!~"5.."}[28d]))
/
sum(rate(http_requests_total[28d]))
```

#### 2. Latency SLI
```promql
# Requests below latency threshold / Total requests
sum(rate(http_request_duration_seconds_bucket{le="0.5"}[28d]))
/
sum(rate(http_request_duration_seconds_count[28d]))
```

#### 3. Durability SLI
```
# Successful writes / Total writes
sum(storage_writes_successful_total)
/
sum(storage_writes_total)
```

**Reference:** See `references/slo-definitions.md`

## Setting SLO Targets

### Availability SLO Examples

The examples in this skill use a 28-day rolling window. A 30-day month is shown for
comparison; use the column that matches your SLO window.

| SLO % | Budget / 28 days | Budget / 30 days | Budget / year |
|-------|------------------|------------------|---------------|
| 99%   | 6.72 hours       | 7.2 hours        | 3.65 days     |
| 99.9% | 40.32 minutes    | 43.2 minutes     | 8.76 hours    |
| 99.95%| 20.16 minutes    | 21.6 minutes     | 4.38 hours    |
| 99.99%| 4.03 minutes     | 4.32 minutes     | 52.56 minutes |

### Choose Appropriate SLOs

**Consider:**
- User expectations
- Business requirements
- Current performance
- Cost of reliability
- Competitor benchmarks

**Example SLOs:**
```yaml
slos:
  - name: api_availability
    target: 99.9
    window: 28d
    sli: |
      sum(rate(http_requests_total{status!~"5.."}[28d]))
      /
      sum(rate(http_requests_total[28d]))

  - name: api_latency_p95
    target: 99
    window: 28d
    sli: |
      sum(rate(http_request_duration_seconds_bucket{le="0.5"}[28d]))
      /
      sum(rate(http_request_duration_seconds_count[28d]))
```

## Error Budget Calculation

### Error Budget Formula

```
Error Budget = 1 - SLO Target
```

**Example:**
- SLO: 99.9% availability over 28 days
- Error Budget: 0.1% = 40.32 minutes per 28 days
- Current Error: 0.05% = 20.16 minutes
- Remaining Budget: 50%

### Error Budget Policy

```yaml
error_budget_policy:
  - remaining_budget: 100%
    action: Normal development velocity
  - remaining_budget: 50%
    action: Consider postponing risky changes
  - remaining_budget: 10%
    action: Freeze non-critical changes
  - remaining_budget: 0%
    action: Feature freeze, focus on reliability
```

**Reference:** See `references/error-budget.md`

## SLO Implementation

### Prometheus Recording Rules

```yaml
# SLI Recording Rules
groups:
  - name: sli_rules
    interval: 30s
    rules:
      # Availability SLI
      - record: sli:http_availability:ratio
        expr: |
          sum(rate(http_requests_total{status!~"5.."}[28d]))
          /
          sum(rate(http_requests_total[28d]))

      # Latency SLI (requests < 500ms)
      - record: sli:http_latency:ratio
        expr: |
          sum(rate(http_request_duration_seconds_bucket{le="0.5"}[28d]))
          /
          sum(rate(http_request_duration_seconds_count[28d]))

  - name: slo_rules
    interval: 5m
    rules:
      # SLO compliance (1 = meeting SLO, 0 = violating)
      - record: slo:http_availability:compliance
        expr: sli:http_availability:ratio >= bool 0.999

      - record: slo:http_latency:compliance
        expr: sli:http_latency:ratio >= bool 0.99

      # Error budget remaining (percentage)
      - record: slo:http_availability:error_budget_remaining
        expr: |
          (sli:http_availability:ratio - 0.999) / (1 - 0.999) * 100

  # Burn rate = error ratio over a window / error budget (1 - 0.999).
  # 1x spends exactly the whole budget over the 28-day window.
  # One rule per window the alerts below use. Evaluated every minute so the
  # short windows stay fresh.
  - name: slo_burn_rate_rules
    interval: 1m
    rules:
      - record: slo:http_availability:burn_rate_5m
        expr: |
          (1 - (
            sum(rate(http_requests_total{status!~"5.."}[5m]))
            /
            sum(rate(http_requests_total[5m]))
          )) / (1 - 0.999)

      - record: slo:http_availability:burn_rate_30m
        expr: |
          (1 - (
            sum(rate(http_requests_total{status!~"5.."}[30m]))
            /
            sum(rate(http_requests_total[30m]))
          )) / (1 - 0.999)

      - record: slo:http_availability:burn_rate_1h
        expr: |
          (1 - (
            sum(rate(http_requests_total{status!~"5.."}[1h]))
            /
            sum(rate(http_requests_total[1h]))
          )) / (1 - 0.999)

      - record: slo:http_availability:burn_rate_6h
        expr: |
          (1 - (
            sum(rate(http_requests_total{status!~"5.."}[6h]))
            /
            sum(rate(http_requests_total[6h]))
          )) / (1 - 0.999)
```

### SLO Alerting Rules

A burn-rate threshold depends on the SLO window. For each alert:

```
threshold = budget fraction consumed × SLO window ÷ alert window
```

For this skill's 28-day window (672 hours):

| Page when… | Long / short window | Threshold (28 days) | Same rule on a 30-day window |
|---|---|---|---|
| 2% of the budget is spent in 1 hour | 1h / 5m | 0.02 × 672 ÷ 1 = **13.44** | 0.02 × 720 ÷ 1 = 14.4 |
| 5% of the budget is spent in 6 hours | 6h / 30m | 0.05 × 672 ÷ 6 = **5.6** | 0.05 × 720 ÷ 6 = 6 |

The widely quoted 14.4 and 6 are the 30-day values. Recompute them whenever the
window changes.

```yaml
groups:
  - name: slo_alerts
    interval: 1m
    rules:
      # Page: 28-day window, thresholds from the table above.
      # Each long window is paired with a short window (1/12 of its length)
      # so the alert clears soon after the errors stop.
      - alert: SLOErrorBudgetBurn
        expr: |
          (
            slo:http_availability:burn_rate_1h > 13.44
            and
            slo:http_availability:burn_rate_5m > 13.44
          )
          or
          (
            slo:http_availability:burn_rate_6h > 5.6
            and
            slo:http_availability:burn_rate_30m > 5.6
          )
        for: 2m
        labels:
          severity: critical
        annotations:
          summary: "Error budget burning fast"
          description: "Burn rate {{ $value | humanize }}x (1x spends the 28-day budget in 28 days)"

      # Error budget exhausted
      - alert: SLOErrorBudgetExhausted
        expr: slo:http_availability:error_budget_remaining < 0
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "SLO error budget exhausted"
          description: "Error budget remaining: {{ $value }}%"
```

This is the paging tier only. For ticket-tier alerts, low-traffic guards, `promtool`
unit tests, backtesting and cheaper long-window rules, use the `slo-burn-rate-alerting`
skill. This skill does not repeat that material.

## SLO Dashboard

**Grafana Dashboard Structure:**

```
┌────────────────────────────────────┐
│ SLO Compliance (Current)           │
│ ✓ 99.95% (Target: 99.9%)          │
├────────────────────────────────────┤
│ Error Budget Remaining: 65%        │
│ ████████░░ 65%                     │
├────────────────────────────────────┤
│ SLI Trend (28 days)                │
│ [Time series graph]                │
├────────────────────────────────────┤
│ Burn Rate Analysis                 │
│ [Burn rate by time window]         │
└────────────────────────────────────┘
```

**Example Queries:**

```promql
# Current SLO compliance
sli:http_availability:ratio * 100

# Error budget remaining
slo:http_availability:error_budget_remaining

# Days until error budget exhausted (at current burn rate)
(slo:http_availability:error_budget_remaining / 100)
*
28
/
(1 - sli:http_availability:ratio) * (1 - 0.999)
```

## SLO Review Process

### Weekly Review
- Current SLO compliance
- Error budget status
- Trend analysis
- Incident impact

### Monthly Review
- SLO achievement
- Error budget usage
- Incident postmortems
- SLO adjustments

### Quarterly Review
- SLO relevance
- Target adjustments
- Process improvements
- Tooling enhancements

## Best Practices

1. **Start with user-facing services**
2. **Use multiple SLIs** (availability, latency, etc.)
3. **Set achievable SLOs** (don't aim for 100%)
4. **Implement multi-window alerts** to reduce noise, with thresholds computed for your SLO window
5. **Track error budget** consistently
6. **Review SLOs regularly**
7. **Document SLO decisions**
8. **Align with business goals**
9. **Automate SLO reporting**
10. **Use SLOs for prioritization**

## Reference Files

- `assets/slo-template.md` - SLO definition template
- `references/slo-definitions.md` - SLO definition patterns
- `references/error-budget.md` - Error budget calculations

## Related Skills

- `prometheus-configuration` - For metric collection
- `grafana-dashboards` - For SLO visualization
- `slo-burn-rate-alerting` - For the full multi-window, multi-burn-rate alert design and its tests
