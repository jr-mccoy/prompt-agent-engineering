---
title: "Experiment Design — Hypothesis, Metric, MDE Handoff, Guardrails, and the Decision Rule Before Launch"
category: product-management/prompts
description: "Write the pre-launch record for a product experiment from the PM's seat: a gate asking whether any result would change the decision, a falsifiable hypothesis, one primary metric whose unit matches the randomisation unit, guardrails with stated margins, a minimum detectable effect justified in business terms and handed to an analyst for sample size and duration, and an outcome-to-action decision rule that includes the inconclusive case — distinct from analytics_ab_test_readout (reading results after), product_pricing_experiment_matrix (pricing grids) and the ab-test-setup skill (test mechanics and implementation)."
techniques:
  - DP-11
  - DS-02
  - DP-13
  - QA-08
  - NE-20
difficulty: intermediate
tags:
  - experimentation
  - ab-testing
  - hypothesis
  - minimum-detectable-effect
  - guardrail-metrics
  - decision-rule
  - pre-registration
updated: "2026-09-24"
related_prompts:
  - domain-data-analytics/experiments-and-reporting/analytics_ab_test_readout.md
  - domain-product-management/prompts/product_pricing_experiment_matrix.md
  - domain-agentic-resources/skills/marketing/ab-test-setup/SKILL.md
---

# Experiment Design

**Objective:** Before an experiment launches, write down what it is for and what each
result will cause. That means a falsifiable hypothesis, one primary metric, guardrails
with margins, and the smallest effect worth acting on, with the reason. The effect size
goes to an analyst, who returns sample size and duration. Finally, record a decision
rule mapping every outcome, including "inconclusive", to an action. An experiment whose
result would not change the decision is refused. So is a design with no decision rule,
because a rule written after the data is seen is a rationalisation.

**When to Use:**
- A feature change is about to go to an A/B test and nobody has written down what "win" means.
- The last three experiments ended in debate about what the result meant.
- Someone wants to "just test it" and you are not sure a test can detect anything at your traffic.

**Distinct from:**
- `../../domain-data-analytics/experiments-and-reporting/analytics_ab_test_readout.md` —
  reads the finished test. This writes the record that readout checks against.
- `product_pricing_experiment_matrix.md` — a grid of pricing experiments with revenue
  blast-radius limits. Use it when the variable is price.
- `../../domain-agentic-resources/skills/marketing/ab-test-setup/SKILL.md` — test
  mechanics for conversion tests: variants, traffic allocation, client- or server-side
  implementation, sample-size tables. Use it, or an analyst, for the calculation this
  prompt hands off.

---

## Inputs

1. **The change** and the population it applies to.
2. **The decision** the result informs, and who makes it.
3. **Baseline** for the candidate primary metric, with its source and period.
4. **Traffic**: eligible units per week.
5. **Cost** to build, maintain or roll back the change.
6. **The longest the team can wait** for a result.

---

## Method

1. **Gate: would any result change the decision? (QA-08)** Write what you will do if the
   change wins, loses and shows nothing. If all three answers are "ship it", do not run
   an experiment. Ship with rollback criteria via `product_launch_readiness_gate.md`, and
   say so.

2. **Write a falsifiable hypothesis.** "Because [evidence], we believe [change] for
   [population] will [increase/decrease] [primary metric] by at least [MDE]." The
   evidence clause is required. A hypothesis with no evidence is a guess and should be
   labelled as one.

3. **Choose metrics (DS-02).**
   - **One primary metric.** Its unit of analysis must match the unit of randomisation.
     If accounts are randomised, measure per account, not per session.
   - **Secondary metrics** are explanatory only. They cannot rescue a flat primary.
   - **Guardrails**, each with a margin: "support tickets per new account may not rise by
     more than 10%".

4. **Set the MDE in business terms and hand off (NE-20).** State the smallest effect for
   which the change is worth its build and maintenance cost, and why. Then give the
   analyst a handoff package: baseline rate or mean and variance, MDE (absolute and
   relative), one- or two-sided test, significance level, power, traffic per week and the
   maximum duration. The analyst returns sample size per arm and duration in full weeks.
   Do not compute significance thresholds by guesswork.

5. **Check feasibility.** If the duration exceeds the maximum wait, change the design:
   a bigger change, a more sensitive metric closer to the change, a population with more
   traffic. Or don't test. A test that cannot detect the MDE in time produces a
   confident-looking null that means nothing.

6. **Write the decision rule (DP-13).** A table mapping each outcome to an action,
   covering: primary meets the MDE with guardrails intact; primary positive but
   inconclusive; primary flat; primary negative; any guardrail breached. State the default
   action for inconclusive. That is the row teams most often leave blank and then argue about.

7. **Fix stopping and safety (DP-11).** Run for the full planned duration in whole weeks.
   Stop early only for guardrail harm, unless the analyst has chosen a sequential method.
   Name who can stop the test, and how quickly the change can be reverted.

8. **Record and hand forward.** Date the record before launch. The readout
   (`analytics_ab_test_readout.md`) checks the results against it.

---

## Output Format

```markdown
## Experiment record — [name] · recorded [date, before launch] · Decider: [name]

### Gate
Win → [action] · Loss → [action] · Nothing → [action] · Test justified: [yes/no, why]

### Hypothesis
Because [evidence], we believe [change] for [population] will [direction] [metric] by ≥ [MDE].

### Metrics
| Role | Metric | Unit | Baseline (source) | Margin / MDE |
|---|---|---|---|---|
| Primary | | | | |
| Guardrail | | | | |

### Sizing handoff → analyst [name]
Baseline · MDE (abs/rel) · sides · α · power · traffic/week · max weeks
Returned: n per arm [ ] · duration [ ] weeks · feasible [y/n]

### Decision rule
| Outcome | Action |
|---|---|

### Stopping and safety
Duration: [whole weeks] · Early stop only if: [...] · Can stop: [name] · Revert time: [...]
```

---

## Verification

- [ ] The gate shows at least two outcomes lead to different actions
- [ ] The hypothesis has an evidence clause, a direction and a threshold
- [ ] Exactly one primary metric, measured at the randomisation unit
- [ ] Every guardrail has a numeric margin
- [ ] The MDE is justified in business terms, not chosen to fit the traffic
- [ ] Sample size and duration came from an analyst or a stated tool, not estimated by eye
- [ ] Duration is within the maximum wait, or the design was changed
- [ ] The decision rule covers inconclusive and guardrail breach, with a default
- [ ] The record is dated before launch

## False-Positive Prevention

1. **Do not choose the MDE to fit your traffic.** If the effect worth acting on is +3
   points and your traffic can only detect +8, the answer is a different design or no
   test, not an MDE of 8.
2. **A secondary metric cannot rescue a flat primary.** If the rule does not say it can,
   it cannot.
3. **Peeking is not monitoring.** Watching guardrails for harm is required. Stopping when
   the primary looks good inflates false positives unless a sequential method was chosen
   in advance.
4. **Unit mismatch manufactures significance.** Randomising accounts and analysing
   sessions treats correlated events as independent.
5. **"Inconclusive" needs a default before launch.** Without one, it becomes "ship"
   whenever the sponsor wants it.
6. **Some changes should not be tested.** Legal fixes, accessibility repairs and
   reversible low-risk changes are often better shipped with rollback criteria.
7. **Novelty is not effect.** For changes users notice, plan to check whether the effect
   holds after week one. The readout will test this.

---

## Example

**Context:** An onboarding checklist for new accounts in an invoicing app. Decision: build
it fully (6 engineer-weeks more) or drop it. Decider: Growth PM.

- **Gate:** win → build fully; loss → drop; nothing → drop, because maintaining it is not
  justified at an unknown effect. Outcomes differ, so the test is justified.
- **Hypothesis:** because 14 of 20 churned trial users never created an invoice, we
  believe a three-step checklist for new accounts will increase 7-day activation by at
  least 3 percentage points.
- **Metrics:** primary is 7-day activation (first invoice sent), per account, baseline
  30% (last 90 days). Guardrails: support tickets per new account +10% maximum; median
  time to first invoice no more than 1 day worse.
- **MDE:** +3 points absolute (10% relative). With 4,000 signups a month, +3 points = 120
  more activated accounts a month. Below that, the 6 engineer-weeks and ongoing
  maintenance are not justified.
- **Handoff:** 30%, +3 points, two-sided, α 0.05, power 0.8, about 1,000 accounts/week,
  maximum 10 weeks. **Analyst returned:** 3,760 per arm = 7,520 total; 7,520 / 1,000 = 7.5
  → **8 full weeks**. 8 ≤ 10, so feasible.

| Outcome | Action |
|---|---|
| ≥ +3 points, interval excludes 0, guardrails intact | Build fully |
| Positive, interval includes 0 | Inconclusive → **drop** (default) |
| Flat or negative | Drop |
| Any guardrail breached | Stop, revert, drop regardless of primary |

**Stopping:** 8 weeks; early stop only on a guardrail breach; the Growth PM can stop it;
revert by flag in under 5 minutes. Record dated 1 Oct, launch 6 Oct.

---

## Techniques Used

- **DP-11 Safe Experiment Design** — bounded, reversible, with a named stopper and revert time.
- **DS-02 Metric Specification** — one primary at the right unit; guardrails with margins.
- **DP-13 Kill Signal Definition** — guardrail breaches and the decision rule's stop rows.
- **QA-08 Gate-Based Verification** — the "would any result change the decision" gate and the feasibility check.
- **NE-20 Third-Party Handoff Package** — the sizing handoff an analyst can act on without a meeting.

## Related Prompts

- `../../domain-data-analytics/experiments-and-reporting/analytics_ab_test_readout.md` — reads the result against this record
- `product_pricing_experiment_matrix.md` — when the variable is price
- `../../domain-agentic-resources/skills/marketing/ab-test-setup/SKILL.md` — mechanics and sample-size references
- `product_north_star_metric_definition.md` — where the primary metric should connect
- `product_launch_readiness_gate.md` — the route when the gate says do not test
