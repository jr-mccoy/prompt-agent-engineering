# Burn-Rate Rules and Tests: Complete Example

A complete, internally consistent example for one SLO: **checkout availability, 99.9%
over 30 days** (error budget 0.001). Every file below passed `promtool check rules` and
`promtool test rules` with promtool 3.5.0. A negative control (the same test with no
errors injected) failed as expected. Re-run both commands against your Prometheus version
before relying on them.

Replace `job="checkout"`, the metric names, the `code` label convention and the runbook
URL with your own. If your SLO period is not 30 days, recompute the thresholds (SKILL.md
Step 2) before using these files.

## Contents

1. `slo-checkout.rules.yml`: recording rules for seven windows, page and ticket alerts
2. `slo-checkout-guard.rules.yml`: low-traffic guard variant of the fast page
3. `slo-checkout.test.yml`: unit tests (fast burn, low traffic)
4. Cheaper long-window recording rules
5. Adapting the tests

## 1. `slo-checkout.rules.yml`

Thresholds: page at 14.4× (1h/5m) or 6× (6h/30m); ticket at 3× (1d/2h) or 1× (3d/6h).
Each threshold is multiplied by the error budget (0.001) because the recorded series are
error *ratios*, not burn rates.

```yaml
groups:
  - name: slo-checkout-availability-recording
    rules:
      - record: slo:sli_error:ratio_rate5m
        expr: |
          sum(rate(http_requests_total{job="checkout",code=~"5.."}[5m]))
          /
          sum(rate(http_requests_total{job="checkout"}[5m]))
        labels:
          slo: checkout-availability
      - record: slo:sli_error:ratio_rate30m
        expr: |
          sum(rate(http_requests_total{job="checkout",code=~"5.."}[30m]))
          /
          sum(rate(http_requests_total{job="checkout"}[30m]))
        labels:
          slo: checkout-availability
      - record: slo:sli_error:ratio_rate1h
        expr: |
          sum(rate(http_requests_total{job="checkout",code=~"5.."}[1h]))
          /
          sum(rate(http_requests_total{job="checkout"}[1h]))
        labels:
          slo: checkout-availability
      - record: slo:sli_error:ratio_rate2h
        expr: |
          sum(rate(http_requests_total{job="checkout",code=~"5.."}[2h]))
          /
          sum(rate(http_requests_total{job="checkout"}[2h]))
        labels:
          slo: checkout-availability
      - record: slo:sli_error:ratio_rate6h
        expr: |
          sum(rate(http_requests_total{job="checkout",code=~"5.."}[6h]))
          /
          sum(rate(http_requests_total{job="checkout"}[6h]))
        labels:
          slo: checkout-availability
      - record: slo:sli_error:ratio_rate1d
        expr: |
          sum(rate(http_requests_total{job="checkout",code=~"5.."}[1d]))
          /
          sum(rate(http_requests_total{job="checkout"}[1d]))
        labels:
          slo: checkout-availability
      - record: slo:sli_error:ratio_rate3d
        expr: |
          sum(rate(http_requests_total{job="checkout",code=~"5.."}[3d]))
          /
          sum(rate(http_requests_total{job="checkout"}[3d]))
        labels:
          slo: checkout-availability
  - name: slo-checkout-availability-alerts
    rules:
      # 99.9% SLO over 30 days -> error budget = 0.001
      - alert: CheckoutErrorBudgetBurn
        expr: |
          (
            slo:sli_error:ratio_rate1h{slo="checkout-availability"} > (14.4 * 0.001)
            and
            slo:sli_error:ratio_rate5m{slo="checkout-availability"} > (14.4 * 0.001)
          )
          or
          (
            slo:sli_error:ratio_rate6h{slo="checkout-availability"} > (6 * 0.001)
            and
            slo:sli_error:ratio_rate30m{slo="checkout-availability"} > (6 * 0.001)
          )
        for: 2m
        labels:
          severity: page
        annotations:
          summary: "checkout is burning its 30-day error budget fast"
          runbook_url: "https://runbooks.example.internal/checkout/error-budget-burn"
      - alert: CheckoutErrorBudgetBurnSlow
        expr: |
          (
            slo:sli_error:ratio_rate1d{slo="checkout-availability"} > (3 * 0.001)
            and
            slo:sli_error:ratio_rate2h{slo="checkout-availability"} > (3 * 0.001)
          )
          or
          (
            slo:sli_error:ratio_rate3d{slo="checkout-availability"} > (1 * 0.001)
            and
            slo:sli_error:ratio_rate6h{slo="checkout-availability"} > (1 * 0.001)
          )
        for: 1h
        labels:
          severity: ticket
        annotations:
          summary: "checkout is steadily consuming its error budget"
          runbook_url: "https://runbooks.example.internal/checkout/error-budget-burn"
```

## 2. `slo-checkout-guard.rules.yml`

Pages only if the last hour had more than 100 requests. `and on(slo)` matches the two
sides on the `slo` label alone. Pick the minimum count from your traffic profile and
record it in the SLO document.

```yaml
groups:
  - name: slo-checkout-availability-traffic
    rules:
      - record: slo:sli_requests:rate1h
        expr: sum(rate(http_requests_total{job="checkout"}[1h]))
        labels:
          slo: checkout-availability
      - alert: CheckoutErrorBudgetBurnFastGuarded
        expr: |
          (
            slo:sli_error:ratio_rate1h{slo="checkout-availability"} > (14.4 * 0.001)
            and
            slo:sli_error:ratio_rate5m{slo="checkout-availability"} > (14.4 * 0.001)
          )
          and on(slo)
          (slo:sli_requests:rate1h{slo="checkout-availability"} * 3600 > 100)
        labels:
          severity: page
```

## 3. `slo-checkout.test.yml`

Input series use promtool's expanding notation: `a+bxn` produces `n+1` samples starting
at `a` and increasing by `b`; `axn` repeats `a`. The error counter stays flat at 0 for
the first 60 samples and then rises without a reset.

Expected labels must list every label on the alert: the labels kept by the expression
(`slo`) plus the rule's labels (`severity`). When a rule has annotations, list them under
`exp_annotations`.

```yaml
rule_files:
  - slo-checkout.rules.yml
  - slo-checkout-guard.rules.yml
evaluation_interval: 1m
tests:
  # Fast burn: 600 good req/min throughout; 60 errors/min from minute 60 (~9% errors).
  - interval: 1m
    input_series:
      - series: 'http_requests_total{job="checkout",code="200"}'
        values: '0+600x180'
      - series: 'http_requests_total{job="checkout",code="500"}'
        values: '0x59 0+60x120'
    alert_rule_test:
      - eval_time: 55m
        alertname: CheckoutErrorBudgetBurn
        exp_alerts: []
      - eval_time: 75m
        alertname: CheckoutErrorBudgetBurn
        exp_alerts:
          - exp_labels:
              severity: page
              slo: checkout-availability
            exp_annotations:
              summary: "checkout is burning its 30-day error budget fast"
              runbook_url: "https://runbooks.example.internal/checkout/error-budget-burn"
      - eval_time: 75m
        alertname: CheckoutErrorBudgetBurnFastGuarded
        exp_alerts:
          - exp_labels:
              severity: page
              slo: checkout-availability
  # Low traffic: 1 good and (from minute 60) 1 failed request per minute.
  # Error ratio is ~50%, but fewer than 100 requests/hour, so the guarded alert stays silent.
  - interval: 1m
    input_series:
      - series: 'http_requests_total{job="checkout",code="200"}'
        values: '0+1x180'
      - series: 'http_requests_total{job="checkout",code="500"}'
        values: '0x59 0+1x120'
    alert_rule_test:
      - eval_time: 75m
        alertname: CheckoutErrorBudgetBurnFastGuarded
        exp_alerts: []
```

Run:

```bash
promtool check rules slo-checkout.rules.yml slo-checkout-guard.rules.yml
promtool test rules slo-checkout.test.yml
```

Why the timings work: errors start at minute 60. The 1h error ratio passes 0.0144 after
about 9 minutes of ~9% errors. With `for: 2m` the alert fires at about minute 71, so the
test checks minute 75 and expects silence at minute 55.

## 4. Cheaper long-window recording rules

`[3d]` range selectors over raw counters can be expensive. Record error and total rates
at 5m, then average both over the long window. The ratio of the two averages weights each
5-minute slice by its traffic, which a plain average of ratios would not.

```yaml
groups:
  - name: slo-checkout-availability-recording-5m-base
    rules:
      - record: slo:sli_errors:rate5m
        expr: sum(rate(http_requests_total{job="checkout",code=~"5.."}[5m]))
        labels:
          slo: checkout-availability
      - record: slo:sli_requests:rate5m
        expr: sum(rate(http_requests_total{job="checkout"}[5m]))
        labels:
          slo: checkout-availability
      # Replaces the [3d] raw-counter rule in slo-checkout.rules.yml (do not load both).
      - record: slo:sli_error:ratio_rate3d
        expr: |
          avg_over_time(slo:sli_errors:rate5m{slo="checkout-availability"}[3d])
          /
          avg_over_time(slo:sli_requests:rate5m{slo="checkout-availability"}[3d])
```

Load this group *instead of* the raw `[3d]` rule, not alongside it. Loading both produces
two series with the same name and labels, and evaluation fails with duplicate samples.
Note that `avg_over_time` only covers history that the 5m rules have actually recorded:
for the first three days after deployment, the long window is shorter than its name says.

## 5. Adapting the tests

Add one case per behaviour you rely on:

| Case | Input | Expect |
|---|---|---|
| Healthy | errors flat at 0 | no alerts at any `eval_time` |
| Fast burn | high error rate from a known minute | silent before, firing after the computed detection time |
| Spike then recovery | errors for 5 minutes only | page clears within about one short window after recovery |
| Slow burn | small error rate over many hours (use `interval: 5m` and long series) | ticket fires, page does not |
| Low traffic | a handful of requests per hour with errors | guarded page silent |

Keep label sets in test series identical to production series. Most "passes in test, fails
in production" problems are label mismatches.
