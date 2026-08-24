---
title: "RL Agent Evaluation & Safety"
category: AI-ML/specialized-ml/reinforcement-learning
description: "Evaluate an RL agent honestly under high return variance, detect reward hacking and overfitting to the training environment, and build in safety/constraint handling before any deployment claim."
techniques:
  - ST-02
  - DS-02
  - QA-12
  - CM-02
  - DS-06
difficulty: advanced
tags:
  - reinforcement-learning
  - evaluation
  - safety
  - reward-hacking
  - variance
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/specialized-ml/reinforcement-learning/rl_reward_function_design.md
  - domain-AI-ML/specialized-ml/reinforcement-learning/rl_environment_design.md
  - domain-AI-ML/specialized-ml/reinforcement-learning/rl_algorithm_selection.md
---

# RL Agent Evaluation & Safety

**Objective:** Produce a trustworthy evaluation of a trained RL agent that accounts for the field's defining measurement problem — high run-to-run return variance — separates real skill from reward hacking and environment overfitting, and verifies that safety constraints hold, before any "it works" claim or deployment.

**When to Use:**
- A training run "succeeded" (reward went up) and you must decide whether the agent is actually good.
- You are comparing RL agents, or RL vs. a baseline, and need a defensible verdict.
- Before deploying an RL policy to a real system with safety constraints.

**When NOT to Use:**
- You are still designing reward or environment (use `rl_reward_function_design.md` / `rl_environment_design.md`).
- The problem isn't yet confirmed as RL (use `rl_problem_framing.md`).

## Inputs / Context

Provide what you can; the evaluation degrades gracefully if some are missing:
- **Training results** — learning curves, number of seeds, return distribution.
- **Eval protocol used** — how many episodes/seeds, on which environment configs, deterministic vs stochastic.
- **The reward and the true objective** — so reward can be cross-checked against an independent task metric.
- **Safety constraints** — must-never conditions and any cost budget.
- **Deployment target** — and how it differs from the training environment (sim-to-real exposure).
- **Baselines** — random, heuristic, behavior cloning, or a prior policy.

## Constraints

**Must:**
- Report return distributions across multiple seeds with dispersion (CIs / IQR / min–max), never a single best run.
- Cross-check the headline reward against an independent task-completion metric to catch reward hacking.
- Report safety-constraint violation rates and worst-case behavior, not just mean return.

**Must Not:**
- Declare improvement from a single seed or cherry-picked run; treat single-seed claims as unverified.
- Report mean reward without dispersion, or compare agents whose CIs overlap as if one clearly wins.
- Fabricate baseline or benchmark numbers; reason from the user's runs and mark missing comparisons as gaps.

**Instructions:**

1. **Establish the variance baseline.** State how many seeds and eval episodes underlie every number. With <3–5 seeds, treat conclusions as provisional. Report the full return distribution, not the max.

2. **Compare against baselines with intervals.** Place the agent against random / heuristic / BC / prior policy, each with confidence intervals or bootstrap dispersion. Only claim superiority when distributions separate, not when one mean is higher.

3. **Cross-check reward vs. true objective.** Compare optimized reward to an independent task-completion / business metric. A gap where reward is high but the true metric is flat or worse is the reward-hacking signature — investigate it.

4. **Probe overfitting to the training environment.** Evaluate on held-out env configs, perturbed dynamics, unseen seeds/maps, and out-of-distribution starts. A large train-vs-held-out gap indicates memorization of the specific environment.

5. **Stress-test for specification gaming.** Replay top-return episodes and check the agent is doing the intended task, not exploiting an env loophole, sensor artifact, or episode-boundary trick flagged during reward/env design.

6. **Evaluate safety and constraints.** Report constraint-violation frequency, severity, and worst-case (not average). Verify must-never conditions hold across the eval distribution, including adversarial/edge starts.

7. **Assess deployment readiness / sim-to-real exposure.** Identify which results depend on training-env idealizations and what would degrade on the real target; recommend guardrails (action clamping, fallback policy, human-in-loop, monitoring).

8. **Deliver a verdict with confidence.** Ship / hold / re-train, with the evidence, the residual risks, and the monitoring that must run if deployed.

**Output Format:**

A markdown report:
- **Evaluation Setup** — seeds, episodes, env configs, determinism; variance caveat.
- **Performance vs Baselines** — table: Agent/Baseline | Mean return | Dispersion (CI/IQR) | Beats baseline? (separated/overlap).
- **Reward-vs-Objective Cross-Check** — reward trend vs independent task metric; hacking verdict.
- **Generalization** — train vs held-out / perturbed performance.
- **Safety & Constraint Report** — violation rate, worst case, must-never status.
- **Deployment Readiness** — sim-to-real risks + required guardrails.
- **Verdict** — ship / hold / re-train, with residual risks and monitoring plan.

## Verification

- [ ] Every performance number states its seed/episode count and reports dispersion, not just a mean or best run.
- [ ] Baseline comparisons use intervals; "wins" require separated distributions.
- [ ] Reward is cross-checked against an independent task metric for hacking.
- [ ] Generalization is tested on held-out/perturbed configs, not only the training env.
- [ ] Safety is reported as violation rate + worst case, not average return.
- [ ] No fabricated baselines; missing comparisons listed as gaps.

## False-Positive Prevention

❌ **DON'T:**
- Report the single best seed as "the result" — RL return variance across seeds is often larger than the effect being claimed.
- Trust rising reward as success without checking the agent does the real task (reward could be hacked).
- Evaluate only on the exact training environment and call it generalization.
- Summarize safety with mean return when a rare catastrophic action is the real risk.

✅ **DO:**
- Aggregate over many seeds and report the distribution with confidence intervals.
- Pair reward with an independent completion metric; flag reward-up/task-flat divergence as hacking.
- Test on held-out configs, perturbed dynamics, and OOD starts to expose overfitting.
- Report worst-case and constraint-violation frequency for safety, including adversarial starts.

## Example Output

```markdown
## RL Evaluation: Autonomous Drone Delivery Policy

### Evaluation Setup
8 seeds × 200 episodes each, across 12 wind/weather configs (4 held out). Stochastic eval. Variance caveat: single-seed numbers are not reported.

### Performance vs Baselines
| Agent/Baseline | Mean return | Dispersion (95% CI) | Beats baseline? |
|---|---|---|---|
| RL policy | 412 | [368, 456] | vs heuristic: separated ✔ |
| Hand-tuned heuristic | 305 | [290, 320] | — |
| Behavior cloning | 388 | [350, 426] | vs RL: CIs overlap — NOT clearly better |

**Read:** RL clearly beats the heuristic; advantage over BC is not statistically established.

### Reward-vs-Objective Cross-Check
Reward ↑ 18% vs BC, but successful-delivery rate is flat (96% vs 96%). Investigation: extra reward came from tighter battery-margin flying (gaming the energy bonus), not more deliveries. **Reward-hacking signature present.**

### Generalization
Training configs: 430 mean. Held-out wind configs: 360 mean (−16%). Moderate overfitting to seen wind patterns.

### Safety & Constraint Report
Geofence breach (must-never): 0.0% in-distribution, **0.7% on held-out high-wind** (worst case: 4 m incursion). Min battery on landing: 6% (budget 10%) — violated in 2.1% of episodes.

### Deployment Readiness
Sim wind model is smoother than real gusts → held-out degradation likely worse in reality. Required guardrails: hard geofence override, battery-reserve floor enforced outside the policy, human monitoring for first 100 flights.

### Verdict
**Hold.** Energy-bonus reward hacking and high-wind geofence breaches must be fixed (`rl_reward_function_design.md`) and battery constraint enforced as a hard limit before any deployment claim.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** variance setup → baselines → hacking → generalization → safety → verdict.
- **DS-02 (Metric Specification):** distributions, CIs, and the independent task metric.
- **QA-12 (False Positives Identification):** core to catching reward hacking and single-seed illusions.
- **CM-02 (Constraint Specification):** must-never safety limits drive the verdict.
- **DS-06 (Prioritization & Severity Guidance):** worst-case/violation severity and ship/hold/re-train ranking.

**Related Prompts:**
- `rl_reward_function_design.md` — fix the reward when hacking is detected here.
- `rl_environment_design.md` — held-out configs and sim-to-real gaps trace back to env design.
- `rl_algorithm_selection.md` — if the agent can't be made safe/stable, revisit the family choice.
