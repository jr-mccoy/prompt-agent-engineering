---
title: "Contextual Bandits & Exploration Design"
category: AI-ML/specialized-ml/recommender-systems
description: "Decide when and how to use bandits for recommendation — epsilon-greedy / UCB / Thompson sampling, contextual vs non-contextual, off-policy evaluation (IPS / doubly-robust), exploration budget and safety guardrails, and propensity logging that makes future evaluation possible."
techniques:
  - ST-02
  - RT-02
  - CM-02
  - DS-01
  - QA-12
difficulty: advanced
tags:
  - recommender-systems
  - contextual-bandits
  - exploration
  - off-policy-evaluation
  - propensity-logging
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/specialized-ml/recommender-systems/recsys_cold_start_strategy.md
  - domain-AI-ML/specialized-ml/recommender-systems/recsys_feedback_loop_bias_audit.md
  - domain-AI-ML/specialized-ml/recommender-systems/recsys_offline_evaluation.md
---

# Contextual Bandits & Exploration Design

**Objective:** Help the user decide whether a bandit / exploration approach is the right tool for a recommendation problem and, if so, design it safely. The aim is to determine when bandits beat a static ranker (non-stationary catalog, cold items, need to learn from sparse feedback), choose an algorithm family (epsilon-greedy, UCB, Thompson sampling) and whether to make it contextual, set an exploration budget with safety guardrails so exploration never harms users unacceptably, and — critically — design propensity logging and off-policy evaluation (IPS / doubly-robust) so that a new policy can be evaluated honestly from logged data rather than judged by a naive comparison that ignores how the logging policy chose what to show.

**When to Use:**
- The catalog or user interests are non-stationary and a periodically-retrained static ranker reacts too slowly.
- You need to learn which new/cold items are good while still serving good experiences — see also `recsys_cold_start_strategy.md`.
- Feedback is bandit feedback (you only observe outcomes for what you showed) and you want principled exploration plus off-policy evaluation.

**When NOT to Use:**
- You can collect rich, unbiased labeled data and a supervised ranker suffices — start with `recsys_offline_evaluation.md`.
- The core problem is diagnosing how the current recommender biases your logs — see `recsys_feedback_loop_bias_audit.md`.
- The system cannot tolerate any exploration risk and you have no propensity logging in place.

## Inputs / Context

Provide what you can:
- **Action space** — number and churn rate of items/arms; whether arms appear/disappear.
- **Context availability** — user/session/item features available at decision time.
- **Reward definition** — the immediate outcome (click, dwell, conversion) and its delay.
- **Logging infrastructure** — whether the serving policy's action probabilities (propensities) are or can be logged.
- **Exploration tolerance** — acceptable degradation budget and any hard safety constraints.
- **Traffic volume** — requests/day, to judge whether exploration converges in useful time.
- **Existing policy** — what serves today and whether its propensities are known.

## Constraints

**Must:**
- Justify bandits over a static ranker via non-stationarity, cold-item learning, or bandit-feedback structure — not novelty.
- Log the serving policy's action propensities at decision time so off-policy evaluation is possible later.
- Choose the algorithm (epsilon-greedy / UCB / Thompson) and contextual-vs-not based on context availability and reward structure.
- Bound exploration with an explicit budget and safety guardrails.

**Must Not:**
- Evaluate a new policy on logged data by naively replaying it without propensity correction (IPS / doubly-robust).
- Deploy unbounded or unguarded exploration that can degrade the user experience without limit.
- Serve without logging propensities, which makes any future off-policy evaluation impossible.
- Fabricate offline/online reward or regret numbers from memory; reason from the user's data and mark unknowns.

**Instructions:**

1. **Justify the bandit framing.** Confirm the problem has bandit feedback and benefits from active exploration (non-stationary, cold arms, sparse feedback). If a supervised ranker on unbiased data would do, route back to `recsys_offline_evaluation.md`.
2. **Define reward and delay.** Pin the immediate reward signal and its observability delay; note whether delayed/credit-assignment issues complicate the bandit loop.
3. **Decide contextual vs non-contextual.** If useful context is available at decision time and rewards vary with it, use a contextual bandit; otherwise a simpler multi-armed bandit may suffice. Justify.
4. **Choose the exploration algorithm.** Map to epsilon-greedy (simple, tunable budget), UCB (optimism, needs reward bounds), or Thompson sampling (Bayesian, strong in practice). State assumptions each makes.
5. **Set the exploration budget and safety guardrails.** Define how much exploration is allowed (e.g. epsilon schedule, capped exploration share) and hard limits that protect users (no exploration on high-stakes surfaces, fallback to safe arm).
6. **Design propensity logging.** Specify that the serving policy logs the probability with which each shown action was chosen, per request — this is the prerequisite for honest off-policy evaluation.
7. **Design off-policy evaluation.** Plan IPS and/or doubly-robust estimators to evaluate candidate policies from logs, including variance controls (clipping/weight capping) and the online A/B that confirms the OPE estimate.
8. **Plan monitoring and rollback.** Track regret/reward, exploration share, and guardrail breaches; define rollback triggers.

**Output Format:**

A markdown bandit-design brief:
- **Bandit Justification** — why exploration beats a static ranker here.
- **Reward Definition** — signal, delay, credit-assignment notes.
- **Contextual Decision** — contextual vs. non-contextual and rationale.
- **Algorithm Choice** — epsilon-greedy / UCB / Thompson with assumptions.
- **Exploration Budget & Safety** — budget schedule and hard guardrails.
- **Propensity Logging Spec** — exactly what is logged per request.
- **Off-Policy Evaluation Plan** — IPS / doubly-robust, variance controls, online confirmation.
- **Monitoring & Rollback** — tracked metrics and triggers.
- **Open Questions / Unknowns** — values to measure on the user's data.

## Verification

- [ ] The bandit framing is justified by bandit-feedback / non-stationarity, not novelty.
- [ ] Action propensities are logged at serving time so off-policy evaluation is possible.
- [ ] The off-policy evaluation plan uses propensity correction (IPS / doubly-robust), not naive replay.
- [ ] Exploration is bounded by an explicit budget with safety guardrails and a safe fallback arm.
- [ ] Contextual-vs-non-contextual and the algorithm choice are justified against the inputs.
- [ ] No offline/online reward or regret numbers are invented — all are to be measured on the user's data.

## False-Positive Prevention

❌ **DON'T:**
- Evaluate a new policy by replaying it over logs and counting "wins" without propensity weighting — naive off-policy evaluation is biased toward whatever the logging policy already favored.
- Let exploration run unbounded so a fraction of users repeatedly get bad recommendations with no cap or safe fallback.
- Serve actions without logging the probability they were chosen, making any later IPS / doubly-robust evaluation impossible.
- Trust an OPE estimate with sky-high importance weights and no variance control.

✅ **DO:**
- Use IPS or doubly-robust estimators with weight clipping, and confirm the estimate with an online A/B before full rollout.
- Cap the exploration share, schedule epsilon down over time, and exclude high-stakes surfaces; keep a safe fallback arm.
- Log per-request action propensities from day one so off-policy evaluation is feasible later.
- Monitor regret, exploration share, and guardrail breaches with explicit rollback triggers.

## Example Output

```markdown
## Contextual Bandit Design — New-Item Promotion Slot

**Bandit Justification:** Catalog churns weekly; cold items need to be learned while still
serving good slots. Bandit feedback (only observe shown items). Static ranker too slow.

**Reward Definition:** Click within session (delay ~seconds). Conversion as secondary,
delayed — handled in OPE, not the live loop.

**Contextual Decision:** Contextual — device, category affinity, time-of-day shift reward;
use a contextual bandit.

**Algorithm Choice:** Thompson sampling (Bayesian, strong empirically, natural exploration).
Assumption: reward model is well-calibrated; revisit if miscalibrated.

**Exploration Budget & Safety:** Exploration capped at 10% of the promotion slot; no
exploration on checkout surface; safe fallback = popularity arm.

**Propensity Logging Spec:** Per request, log chosen action id + the probability it was
sampled + context vector.

**Off-Policy Evaluation Plan:** Doubly-robust estimator with weight clipping at 95th pct;
confirm with online A/B before scaling past 10%.

**Monitoring & Rollback:** Track reward, exploration share, guardrail breaches daily;
rollback if reward drops below safe-arm baseline.

**Open Questions:** Measure actual reward variance and weight distribution on the user's logs.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** Drives the design from justification through monitoring.
- **RT-02 (Multi-Dimensional Analysis Framework):** Forces the exploration-algorithm and contextual-vs-not choices to be compared explicitly.
- **CM-02 (Constraint Specification):** Encodes propensity-logging, bounded-exploration, and no-fabrication constraints.
- **DS-01 (Framework Application):** Maps reward/context/traffic inputs to algorithm and exploration choices.
- **QA-12 (False Positives Identification):** Enforces propensity-corrected off-policy evaluation over naive replay.

**Related Prompts:**
- `recsys_cold_start_strategy.md` — handling new users/items, a common driver for exploration.
- `recsys_feedback_loop_bias_audit.md` — diagnosing how the serving policy biases your logs.
- `recsys_offline_evaluation.md` — the offline metric harness and baselines exploration is measured against.
