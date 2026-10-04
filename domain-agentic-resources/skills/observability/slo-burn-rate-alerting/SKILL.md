---
name: slo-burn-rate-alerting
description: Designs, generates and tests multi-window, multi-burn-rate alerts for an SLO that already exists. Derives each threshold from the share of error budget it represents, emits every recording rule the alerts reference, guards low-traffic services, unit-tests rules with promtool and backtests them against past incidents. Use when asked to "set up burn rate alerts", "our SLO alerts are noisy or missed an incident", "page on error budget", or "test our alerting rules".
metadata:
  tags:
    - observability
    - slo
    - error-budget
    - burn-rate
    - alerting
    - prometheus
  updated: "2026-10-04"
---
# SLO Burn-Rate Alerting

Builds the alerting layer on top of a defined SLO: alerts that page when the error budget
is being spent fast enough to matter, stay quiet otherwise, and are proven by unit tests
and a backtest before anyone is woken up by them.

## Purpose

Threshold alerts on raw error rate either page for every blip or miss slow degradations.
Burn-rate alerts tie paging to the error budget, but they are easy to get subtly wrong:
thresholds copied for a 30-day window applied to a 28-day SLO, alert expressions that
reference recording rules nobody defined, one error in a quiet hour paging someone, and
rules never tested before production. This skill derives the numbers, generates complete
rules, and tests them.

## When to Use This Skill

- An SLO exists (SLI, target, window) and needs alerts
- SLO alerts page too often, page too late, or missed an incident
- Reviewing or migrating burn-rate rules (for example after changing the SLO window or target)
- Adding unit tests for alerting rules to CI
- A service has low or bursty traffic and burn-rate alerts are noisy

## When NOT to Use This Skill

- **Choosing SLIs, setting SLO targets, error-budget policy and SLO reviews.** Use
  `slo-implementation` first; this skill assumes its output. The `/slo_implement` command
  covers the broader SLO programme.
- **ML model quality SLOs** (prediction quality, drift). See the prompt
  `domain-AI-ML/production-monitoring/mlmonitor_slo_design_for_ml.md`.
- **Installing or scaling Prometheus, or scrape configuration.** Use `prometheus-configuration`.
- **Dashboards for SLOs.** Use `grafana-dashboards`.
- **Alerting a solo developer's side project.** The prompt
  `domain-software-engineering/devops/monitoring_solo_dev_alerting.md` fits better than a
  multi-window scheme.

## Prerequisites

- SLO definition: the SLI as a ratio of bad events to all events, the target (for example
  99.9%), and the window (for example 30 days)
- The metrics behind the SLI, with enough history to backtest (ideally the full SLO window)
- `promtool` (ships with Prometheus) for rule checks and unit tests. The math is
  vendor-neutral; for other backends, translate the expressions and use their own test
  tooling (verify against current docs).

## Key Definitions

- **Error budget** = 1 − SLO target. At 99.9%, the budget is 0.001 (0.1% of events).
- **Burn rate** = observed error ratio ÷ error budget. A burn rate of 1 spends exactly the
  whole budget over the SLO window; 10 spends it in a tenth of the window.
- **Budget consumed** by burning at rate *b* for duration *w*, in an SLO period *T*:
  `consumed = b × w / T`.

## Workflow

### Step 1: Decide what each alert tier means in budget terms

Choose, per tier, the share of budget that must be at risk before someone acts. The
following is a common starting point (from the Google SRE Workbook's alerting chapter);
adjust it to your on-call policy.

| Tier | Budget consumed | Long window | Short window | Action |
|---|---|---|---|---|
| Page (fast) | 2% | 1h | 5m | Page |
| Page (medium) | 5% | 6h | 30m | Page |
| Ticket (slow) | 10% | 1d | 2h | Ticket |
| Ticket (slowest) | 10% | 3d | 6h | Ticket |

The short window is about 1/12 of the long window. Its job is to make the alert stop
firing soon after the problem stops; without it, a long window keeps the alert firing for
hours after recovery.

### Step 2: Derive the thresholds for *your* SLO period

Rearranging the consumption formula, the threshold for each tier is:

```
burn_rate_threshold = budget_fraction × T / long_window
```

| Tier | 30-day period (T = 720h) | 28-day period (T = 672h) |
|---|---|---|
| 2% in 1h | 0.02 × 720 / 1 = **14.4** | 0.02 × 672 / 1 = **13.44** |
| 5% in 6h | 0.05 × 720 / 6 = **6** | 0.05 × 672 / 6 = **5.6** |
| 10% in 1d | 0.10 × 720 / 24 = **3** | 0.10 × 672 / 24 = **2.8** |
| 10% in 3d | 0.10 × 720 / 72 = **1** | 0.10 × 672 / 72 ≈ **0.93** |

The widely quoted 14.4 and 6 assume a 30-day period. Using them on a 28-day SLO is a
small error, but recompute rather than copy. The alert compares the **error ratio**
against `threshold × error_budget`, for example `14.4 × 0.001 = 0.0144` for 99.9%.

**Detection time check:** with a full outage (error ratio 1.0), the fast-page tier fires
after about `threshold × budget × long_window` = 14.4 × 0.001 × 60 min ≈ 52 seconds of
outage, plus any `for:` duration. Calculate this for your numbers and confirm it matches
expectations.

### Step 3: Generate every recording rule the alerts use

Each window in Step 1 needs an error-ratio recording rule: typically 5m, 30m, 1h, 2h, 6h,
1d and 3d. Write a generator (script, Jsonnet or template) rather than hand-copying seven
near-identical rules. Open-source generators such as Sloth and Pyrra produce these rules
from an SLO spec (verify against current docs).

```yaml
- record: slo:sli_error:ratio_rate1h
  expr: |
    sum(rate(http_requests_total{job="checkout",code=~"5.."}[1h]))
    /
    sum(rate(http_requests_total{job="checkout"}[1h]))
  labels:
    slo: checkout-availability
```

For a **latency SLI**, the bad events are requests slower than the threshold:
`1 - (sum(rate(<histogram>_bucket{le="0.3"}[w])) / sum(rate(<histogram>_count[w])))`.
The `le` value must exactly match an existing bucket boundary. Native histograms use a
different query form; verify against current docs.

**Long windows are expensive.** If `[3d]` range queries are too heavy, record the error
and total rates at 5m and derive long windows with `avg_over_time` over both, which keeps
the ratio correctly weighted. Both forms are in the reference file.

### Step 4: Write the alert rules

```yaml
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
```

The ticket tier is the same shape with the 1d/2h and 3d/6h pairs and `severity: ticket`.
The complete, tested rule file is in
[references/burn-rate-rules-and-tests.md](references/burn-rate-rules-and-tests.md).

Routing: send `severity: page` to the pager and `severity: ticket` to the ticket queue.
Use an inhibition rule so the ticket alert is suppressed while the page alert for the
same `slo` fires (Alertmanager supports this with `inhibit_rules`; verify field names
against your version's docs).

### Step 5: Guard low-traffic services

With little traffic, one failed request can exceed every threshold. Options, in order of
preference:

1. **Require a minimum event count** in the long window before paging:
   `... and on(slo) (slo:sli_requests:rate1h{slo="..."} * 3600 > 100)`.
2. **Add synthetic traffic** (probes) so the SLI has a steady denominator; label it so it
   can be separated in analysis.
3. **Group services** that share an on-call team and user journey into one SLO.
4. **Page only on the longer tiers**, and send the fast tier to a ticket.

Write the chosen minimum into the SLO document; it is part of the alert's contract.

### Step 6: Unit-test the rules with promtool

```bash
promtool check rules slo-checkout.rules.yml
promtool test rules slo-checkout.test.yml
```

Write at least these cases per alert:

- **No errors:** no alert at any time
- **Fast burn** (for example 9% errors starting at a known time): alert absent before the
  expected detection time and present after it
- **Short spike that recovers:** the short window clears the alert promptly
- **Low traffic** (if Step 5 applies): a single error does not page

The reference file contains a passing test for the fast-burn case and the low-traffic case.
Run `promtool test rules` in CI on every change to rule files.

### Step 7: Backtest against real history

Before enabling paging, evaluate the alert expression over past data:

1. Run the alert expression as a range query (Prometheus HTTP API `/api/v1/query_range`,
   or the expression browser's graph view) across at least one SLO window. If the
   recording rules did not exist historically, substitute their raw expressions.
2. List the intervals where the expression returned results.
3. Compare them with the incident log:

| Measure | Question | Target |
|---|---|---|
| Recall | Which real incidents would have fired the page tier? | Every incident that consumed meaningful budget |
| Precision | Which firings matched no real incident? | Few; each one explained |
| Detection time | How long after impact began did it fire? | Within what the on-call policy promises |
| Reset time | How long after recovery did it stop? | Minutes for page tiers |

Adjust tiers or the low-traffic guard and backtest again. Record the results next to the
rules.

## Verification

- [ ] Thresholds recomputed for the actual SLO period and target
- [ ] Every recording rule referenced by an alert exists, with the same labels the alert selects on
- [ ] `promtool check rules` and `promtool test rules` pass, and run in CI
- [ ] A test proves the page fires for a fast burn and stays silent for no errors
- [ ] Backtest results recorded: recall, precision, detection time, reset time
- [ ] Every page-tier alert has a `runbook_url` that resolves
- [ ] Low-traffic behaviour decided and documented

## Common Failure Modes

| Symptom | Cause | Fix |
|---|---|---|
| Alert never fires | Expression references a recording rule that does not exist, or label mismatch (`and` matches on all labels) | Generate rules from one source; unit-test each alert |
| Pages for single errors at night | Low traffic | Step 5 guard |
| Alert keeps firing long after recovery | No short window, or short window too long | Pair each long window with ~1/12 short window |
| Fires slightly too early or late | 30-day thresholds used on a 28-day SLO | Recompute (Step 2) |
| Rule evaluation slow or expensive | `[3d]` range over raw high-cardinality counters | Pre-aggregate at 5m; derive long windows with `avg_over_time` |
| SLI ratio is NaN | No traffic in the window (0/0) | Treat as no alert; consider synthetic probes for a steady denominator |
| Unit test passes but production differs | Test series do not match real label sets | Copy label sets from real series when writing tests |

## Safety & Constraints

**NEVER:**
- Enable paging on new burn-rate rules before they pass unit tests and a backtest
- Silence a noisy page tier indefinitely; fix the threshold, guard or SLI, or demote it to a ticket
- Change an SLO target or window without regenerating the thresholds

**ALWAYS:**
- Keep the SLO spec, the generated rules and their tests in the same repository change
- Link every page to a runbook (see `executable-runbook-authoring`)

## Reference Files

| Resource | Purpose |
|---|---|
| [references/burn-rate-rules-and-tests.md](references/burn-rate-rules-and-tests.md) | Complete recording rules, page and ticket alerts, low-traffic guard, cheaper long-window rules, and promtool unit tests (validated with promtool 3.5) |

## Related Skills

- `slo-implementation`: SLI selection, targets, error-budget policy and review cadence (prerequisite)
- `prometheus-configuration`: rule file loading and Alertmanager wiring
- `grafana-dashboards`: burn-rate and remaining-budget panels
- `executable-runbook-authoring` (devops): the runbook each page links to
