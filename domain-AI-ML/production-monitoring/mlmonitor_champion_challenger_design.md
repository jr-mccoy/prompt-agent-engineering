---
title: "Champion-Challenger Design"
category: AI-ML/production-monitoring
description: "Run challenger models against a production champion continuously — deciding what challengers see and whether they act, defining promotion criteria before results arrive, and preventing the multiple-comparisons problem that continuous challenging creates."
techniques:
  - ST-02
  - DS-02
  - CM-02
  - QA-12
  - DS-06
difficulty: advanced
tags:
  - champion-challenger
  - shadow-deployment
  - model-promotion
  - continuous-evaluation
  - multiple-comparisons
updated: "2026-08-22"
related_prompts:
  - domain-AI-ML/production-monitoring/mlmonitor_canary_shadow_deployment.md
  - domain-AI-ML/model-evaluation-validation/mleval_ab_test_design_for_models.md
  - domain-AI-ML/production-monitoring/mlmonitor_model_portfolio_health_review.md
  - domain-AI-ML/mlops-infrastructure/mlops_model_registry_design.md
---

# Champion-Challenger Design

**Objective:** Run candidate models continuously against the production champion so replacement decisions rest on production evidence — choosing whether challengers observe or act, fixing promotion criteria before any results are seen, and controlling the multiple-comparisons problem that continuous challenging creates by construction.

**When to Use:**
- Models are replaced often enough that per-release A/B tests are too slow or too costly.
- Offline metrics have previously disagreed with production outcomes and you want continuous production evidence.
- Several candidate approaches are in flight and you need a fair, standing comparison.

**When NOT to Use:**
- A single planned replacement with a defined hypothesis — run a proper experiment via `../model-evaluation-validation/mleval_ab_test_design_for_models.md`.
- You want to validate one new model before rollout — use `mlmonitor_canary_shadow_deployment.md`.
- Labels never arrive in production; challengers cannot be scored and the framework has nothing to measure.

## Inputs / Context

- **Champion** — current production model, its metrics, and how long it has held the position.
- **Challenger pipeline** — how candidates are produced and how many are in flight at once.
- **Label availability and latency** — when production outcomes become known, which sets the evaluation clock.
- **Traffic volume** — total, and what fraction can be allocated to acting challengers.
- **Cost of running challengers** — inference cost for shadow mode, opportunity cost for live traffic.
- **Business metric** — the outcome that actually matters, alongside any model metric.

## Constraints

**Must:**
- Decide explicitly whether challengers are **shadow** (observe, do not act) or **live** (serve a traffic slice). Shadow is cheap and safe but cannot measure outcomes that depend on the model having acted; live measures the real thing at real risk.
- Fix promotion criteria — metric, margin, minimum duration, and minimum sample — **before** any challenger runs. Criteria set after seeing results are not criteria.
- Control multiple comparisons: with many challengers evaluated continuously, some will beat the champion by chance. State the correction or the pre-registration discipline used.
- Require a minimum evaluation duration covering the natural cycle — weekly seasonality at minimum — so a challenger cannot win on a favourable Tuesday.
- Define challenger retirement, so the framework does not accumulate stale candidates indefinitely.

**Must Not:**
- Assert significance thresholds, minimum sample sizes, or evaluation durations from memory; derive them from your own metric variance and mark them `[compute for your metrics]`.
- Promote on a model metric alone when a business metric exists and can be measured; they diverge, and the business metric is the one that matters.
- Compare a shadow challenger's outcome metric against the champion's when the outcome depends on having acted — the comparison is invalid and will systematically favour whichever model did not act.
- Let challengers see different data, features, or time windows than the champion; then you are comparing pipelines, not models.
- Stop an evaluation early because a challenger looks good — early stopping without a designed rule inflates false positives.

**Instructions:**

1. **Characterize the champion.** Current metrics with their variance, tenure, and known weaknesses. Variance matters: it determines the margin a challenger must clear to be distinguishable from noise.

2. **Choose shadow or live per challenger.** Shadow when the metric can be computed from predictions alone. Live when the outcome depends on the model having acted — a recommendation nobody saw generates no engagement, and shadow-scoring it is measuring a different thing. State the choice and its consequence for what can be concluded.

3. **Fix the promotion criteria now.** Primary metric, minimum margin, minimum duration, minimum sample, and the guardrail metrics that block promotion regardless of the primary. Write them down before any challenger runs — this is the discipline that makes the framework trustworthy rather than a machine for finding favourable comparisons.

4. **Design the comparison fairly.** Identical inputs, identical feature computation, identical time windows, identical population. Any difference makes the result a pipeline comparison. Where a challenger requires a new feature, that difference must be stated as part of the challenge.

5. **Handle multiple comparisons.** With N challengers evaluated continuously, some will appear better by chance alone. Options: correct the significance threshold for the number of comparisons, pre-register a small number of challengers per period, or require replication in an independent window before promotion. Choose one and state it — the alternative is a framework that reliably promotes noise.

6. **Set the minimum duration from the natural cycle.** At least one full weekly cycle, longer where monthly effects exist. State it, and enforce it even when a challenger leads early.

7. **Define the promotion procedure.** What happens on promotion: the challenger becomes champion, the previous champion is retained as a challenger for a defined period (which catches regressions the criteria missed), and the registry records the decision with its evidence.

8. **Define retirement.** A challenger that fails to beat the champion within a stated window is retired, with its result recorded. Without this, the pool grows, cost grows, and the multiple-comparisons problem worsens quietly.

9. **Monitor the framework itself.** Promotion rate, average challenger lifetime, and whether promoted challengers subsequently hold their advantage. A promotion whose gain evaporates is evidence the criteria are too loose.

**Output Format:**

A markdown design:
- **Champion Profile** — metrics, variance, tenure, known weaknesses.
- **Challenger Mode** — table: Challenger | Shadow or live | Why | What it can and cannot measure.
- **Promotion Criteria** — primary metric, margin, duration, sample, guardrails. Fixed in advance.
- **Comparison Fairness** — inputs, features, windows, population; any stated differences.
- **Multiple-Comparisons Control** — the chosen approach.
- **Minimum Duration** — derived from the natural cycle.
- **Promotion Procedure** — steps, retention of the previous champion, registry record.
- **Retirement Rule** — window and recording.
- **Framework Monitoring** — promotion rate, post-promotion holding.

## Verification

- [ ] Champion variance is characterized, and the required margin refers to it.
- [ ] Shadow or live is chosen per challenger with the consequence stated.
- [ ] Promotion criteria are written before any challenger runs.
- [ ] Comparison fairness is specified, with any input differences declared.
- [ ] A multiple-comparisons control is chosen and stated.
- [ ] Minimum duration covers at least one full natural cycle.
- [ ] The previous champion is retained as a challenger after promotion.
- [ ] A retirement rule exists with a stated window.
- [ ] Post-promotion holding is monitored.
- [ ] No thresholds or durations are asserted from memory.

## False-Positive Prevention

❌ **DON'T:**
- Run ten challengers continuously and promote whichever wins this week — with enough comparisons something always wins, and the framework becomes a noise amplifier.
- Set promotion criteria after seeing the results; the criteria then encode the result rather than testing it.
- Shadow-score an engagement metric — a recommendation the user never saw cannot generate a click, and the comparison systematically favours the model that did not act.
- Promote on a model metric when the business metric is available; they diverge, and the divergence is usually the interesting finding.
- Stop early because a challenger looks strong on day three; early stopping without a designed rule is how noise gets promoted.
- Let a challenger use a feature the champion lacks and report the difference as a model improvement.

✅ **DO:**
- Characterize champion variance so the required margin is grounded rather than chosen.
- Match the mode to what the metric requires: live when the outcome depends on acting.
- Write the criteria down first, including guardrails that block promotion regardless of the primary metric.
- Choose and state a multiple-comparisons control before running many challengers.
- Enforce the minimum duration even when a challenger leads early.
- Retain the demoted champion as a challenger, and watch whether promoted models hold their gains.

## Example Output

```markdown
## Champion-Challenger: Fraud-Scoring Model

### Champion Profile
| Attribute | Value |
|---|---|
| Primary metric | precision at the review-capacity threshold `[measure]` |
| Metric variance (weekly) | `[measure]` — **sets the detectable margin** |
| Business metric | fraud loss prevented per review-hour `[measure]` |
| Tenure | `[record]` |
| Known weaknesses | new-merchant cohort; card-not-present edge cases |

The weekly variance is the number that matters most here: a challenger cannot be credited with
an improvement smaller than the champion's own week-to-week movement.

### Challenger Mode
| Challenger | Mode | Why | Can / cannot measure |
|---|---|---|---|
| A: new features | **Shadow** | precision computable from predictions + eventual chargeback labels | ✅ precision · ❌ effect on reviewer behaviour |
| B: different architecture | **Shadow** | same | ✅ precision · ❌ reviewer effects |
| C: new score presentation | **Live (small slice)** | outcome depends on how reviewers act on the score | ✅ realized loss prevented · ❌ nothing — but carries real risk |

Challenger C **must** be live: its whole hypothesis concerns reviewer behaviour, and a shadow
comparison would measure a quantity that does not exist for it.

### Promotion Criteria — fixed before any challenger runs
| Criterion | Value |
|---|---|
| Primary | precision at threshold |
| Minimum margin | `[compute from champion variance — must exceed weekly noise]` |
| Minimum duration | **4 full weeks** (covers weekly cycle + month-end effects) |
| Minimum sample | `[compute from base rate and required margin]` |
| Guardrail 1 | false-positive rate on the legitimate-customer cohort must not rise |
| Guardrail 2 | new-merchant cohort must not regress |
| Guardrail 3 | review volume must stay inside capacity |

Any guardrail breach blocks promotion **regardless of the primary metric**. Fraud models that
improve precision by rejecting more legitimate customers are a well-known way to win the metric
and lose the business.

### Comparison Fairness
Identical transaction stream, identical feature computation path, identical time windows,
identical population. **Declared difference:** Challenger A consumes three features the champion
does not. That is part of the challenge and is stated in the promotion record, so a promotion is
never later mistaken for a pure modelling gain.

### Multiple-Comparisons Control
Three challengers evaluated continuously. **Control: replication in an independent window.** A
challenger meeting the criteria enters a second, non-overlapping 4-week window and must meet them
again before promotion. This is preferred to a corrected threshold because it also catches
challengers that won on a period-specific fraud pattern — which is the realistic failure here,
not merely statistical luck.

### Minimum Duration
4 weeks, enforced even if a challenger leads from week one. Fraud patterns are bursty; a
challenger can lead for a fortnight because one attack pattern happened to suit it.

### Promotion Procedure
1. Challenger meets criteria in window 1 → enters replication window 2.
2. Meets criteria again → promotion approved.
3. Promoted to champion; **previous champion retained as a challenger for 8 weeks** — this is
   what catches regressions the criteria did not cover.
4. Registry records: challenger ID, both windows' results, declared feature differences,
   guardrail values, approver.

### Retirement Rule
A challenger that fails to meet the criteria within 12 weeks is retired and its result recorded.
Without this the pool grows, inference cost grows, and the multiple-comparisons problem worsens
every time someone adds "just one more" candidate.

### Framework Monitoring
- Promotion rate — a high rate suggests the margin is set below real noise.
- Average challenger lifetime.
- **Post-promotion holding:** does a promoted challenger retain its advantage over the following
  8 weeks? Gains that evaporate are the clearest evidence the criteria are too loose, and this is
  the single most informative signal about the framework's health.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** criteria are fixed before challengers run, which is the ordering that makes the framework trustworthy.
- **DS-02 (Metric Specification):** the promotion margin is defined relative to measured champion variance rather than chosen.
- **CM-02 (Constraint Specification):** the fairness and criteria-in-advance rules bound what may be promoted.
- **QA-12 (False Positives Identification):** the multiple-comparisons control and post-promotion holding check target the framework's characteristic failure.
- **DS-06 (Prioritization and Severity Guidance):** guardrails outrank the primary metric in the promotion decision.

**Related Prompts:**
- `mlmonitor_canary_shadow_deployment.md` — validating a single model before rollout.
- `../model-evaluation-validation/mleval_ab_test_design_for_models.md` — the single-hypothesis experiment.
- `mlmonitor_model_portfolio_health_review.md` — reviewing the whole fleet this framework feeds.
- `../mlops-infrastructure/mlops_model_registry_design.md` — where promotion records live.
