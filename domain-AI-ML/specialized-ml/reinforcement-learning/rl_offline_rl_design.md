---
title: "Offline RL Design"
category: AI-ML/specialized-ml/reinforcement-learning
description: "Design an offline (batch) RL setup that learns a policy from a fixed logged dataset with no environment interaction — handling distributional shift, out-of-distribution actions, conservative learning methods, and off-policy evaluation before any deployment."
techniques:
  - ST-02
  - RT-02
  - CM-02
  - DS-06
  - QA-12
difficulty: advanced
tags:
  - reinforcement-learning
  - offline-rl
  - batch-rl
  - distributional-shift
  - off-policy-evaluation
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/specialized-ml/reinforcement-learning/rl_algorithm_selection.md
  - domain-AI-ML/specialized-ml/reinforcement-learning/rl_evaluation_safety.md
  - domain-AI-ML/specialized-ml/reinforcement-learning/rl_problem_framing.md
---

# Offline RL Design

**Objective:** Help the user design an offline (batch) reinforcement learning pipeline that learns a policy entirely from a fixed, previously-collected dataset of transitions — with no ability to interact with the environment during training. The central failure mode of offline RL is distributional shift: a learned policy that proposes out-of-distribution (OOD) actions the dataset never covered, where value estimates are unconstrained and wildly optimistic. This prompt walks through dataset characterization, the choice of a conservative learning family (policy-constraint, value-pessimism, or one-step methods), and — critically — how to evaluate a policy off-policy before trusting it, since you cannot simply "run it and see."

**When to Use:**
- You have logged interaction data (clicks, trajectories, sensor logs, historical decisions) and cannot or must not collect new data online.
- Online exploration is expensive, slow, or unsafe (healthcare, robotics on real hardware, recommender systems in production).
- You need a deployment-ready policy but can only validate it against historical data plus limited off-policy estimates.

**When NOT to Use:**
- You can interact with a cheap simulator or live environment freely — use `rl_algorithm_selection.md` for online algorithm choice instead.
- The problem is a one-step contextual bandit; off-policy bandit evaluation is simpler and the full offline-RL machinery is overkill.
- Your real need is environment fidelity / safety gating before any rollout — see `rl_evaluation_safety.md`.

## Inputs / Context

Provide what you can:
- **Dataset provenance** — what behavior policy collected it (expert, random, mixed, a deployed heuristic), and how it was logged.
- **Coverage** — which state-action regions are dense vs sparse; whether logged action propensities were recorded.
- **State / action spaces** — dimensionality, discrete vs continuous, and whether the reward is logged or must be reconstructed.
- **Horizon and reward sparsity** — episodic vs continuing, dense vs terminal-only reward.
- **Deployment constraint** — whether the eventual policy will face a true online test, a shadow/canary phase, or only offline metrics.
- **Safety / regret tolerance** — cost of a bad action at deployment, and whether constraints must be hard.

## Constraints

**Must:**
- Treat distributional shift as the primary design risk and choose a method whose conservatism matches dataset coverage.
- Use an off-policy / offline policy evaluation (OPE) estimator (e.g., fitted-Q evaluation, importance sampling with clipping, doubly-robust) before claiming any performance number.
- Hold out trajectories for OPE that the policy/value learning never touched.
- State explicitly which state-action regions are unsupported and how the policy is constrained there.

**Must Not:**
- Assume more coverage than the logged behavior policy actually provided.
- Evaluate the learned policy with standard online-style rollouts you cannot actually run, or report a value estimate as if it were a measured return.
- Fabricate reward/return numbers or cite benchmark results from memory; reason from the user's setup and mark unknowns — measure in their environment.
- Tune the conservatism coefficient on the same trajectories used for final evaluation.

**Instructions:**

1. **Characterize the dataset.** Determine the behavior policy, coverage density across the state-action space, whether propensities were logged, and reward availability. This dictates everything downstream.
2. **Frame the shift risk.** Identify where a greedy policy would propose OOD actions and why value estimates there are untrustworthy (overestimation on unseen actions).
3. **Pick a conservatism family.** Map coverage and action type to a method class: value-pessimism (CQL-style penalize OOD-action values), implicit/expectile methods (IQL-style, avoid querying OOD actions), policy-constraint (BCQ/BEAR-style, stay near the behavior policy), or one-step/behavior-regularized approaches for narrow data.
4. **Set the conservatism knob.** Explain how the penalty/constraint strength trades off staying-in-distribution vs improving over the behavior policy, and that its value is empirical.
5. **Design OPE.** Choose an estimator suited to coverage: importance sampling (with clipping) when propensities exist and overlap is good; fitted-Q evaluation / model-based OPE when overlap is poor; doubly-robust to combine. State the bias/variance tradeoff.
6. **Split data honestly.** Reserve held-out trajectories for OPE; never reuse them for learning or coefficient tuning.
7. **Define a deployment gate.** Specify the OPE confidence threshold, a shadow/canary phase, and abort conditions before any live use — defer hard safety gating to `rl_evaluation_safety.md`.
8. **Plan the measurement.** State which numbers must be measured in the user's environment across multiple seeds rather than asserted.

**Output Format:**

A markdown design brief:
- **Dataset Profile** — provenance, coverage map, propensity availability, reward source.
- **Distributional-Shift Risk** — where OOD actions arise and the overestimation mechanism.
- **Recommended Method Family** — chosen conservatism approach with rationale tied to coverage.
- **Conservatism Tuning Plan** — what the knob controls and how to sweep it.
- **OPE Plan** — estimator(s), held-out split, bias/variance notes.
- **Deployment Gate** — thresholds, shadow phase, abort criteria.
- **Open Questions / Unknowns** — items requiring measurement, marked explicitly.

## Verification

- [ ] Dataset coverage and the behavior policy are characterized, not assumed.
- [ ] A specific conservatism family is recommended and justified by coverage.
- [ ] An OPE estimator is named with its bias/variance tradeoff stated.
- [ ] Held-out trajectories are reserved for evaluation and not reused for tuning.
- [ ] A deployment gate (threshold + shadow + abort) is defined before live use.
- [ ] No reward/return/benchmark numbers are fabricated; all performance claims are flagged to be measured in the user's environment across multiple seeds.

## False-Positive Prevention

❌ **DON'T:**
- Let the policy exploit out-of-distribution actions because the value function reports them as high — that's extrapolation error, not real value.
- Trust an online-style evaluation when you cannot actually run the environment; an unverified value estimate is not a measured return.
- Tune the conservatism coefficient on your evaluation trajectories and then report those same numbers.
- Assume importance-sampling OPE is reliable when behavior/target overlap is poor — variance explodes.

✅ **DO:**
- Constrain the policy to in-distribution actions or penalize OOD-action values explicitly, and name which regions are unsupported.
- Use OPE estimators matched to coverage (FQE/model-based when overlap is weak, IS+DR when propensities and overlap are good).
- Keep a strictly held-out trajectory set for final evaluation and report uncertainty.
- Defer the go/no-go deployment decision to a measured shadow/canary phase, not an offline point estimate.

## Example Output

```markdown
## Dataset Profile
- Behavior policy: deployed rules-based recommender (logged with action propensities).
- Coverage: dense on popular items; sparse on long-tail and on "show nothing" action.
- Reward: 7-day engagement, logged per session.

### Distributional-Shift Risk
A greedy policy will favor long-tail items whose Q-values are extrapolated from
almost no data → overestimation. "Show nothing" is nearly unsupported.

### Recommended Method Family
IQL-style (implicit Q-learning): avoids querying OOD actions during the value
update; well-suited to mixed-quality logs with uneven coverage.

### Conservatism Tuning Plan
Sweep the expectile/temperature; higher = closer to behavior policy, lower =
more aggressive improvement. Select on a held-out OPE split, not test.

### OPE Plan
Primary: Fitted-Q Evaluation (poor long-tail overlap). Secondary: clipped
weighted IS as a sanity check. Bias/variance both flagged.

### Deployment Gate
Promote to a 1% shadow cohort only if FQE estimate beats logged policy with a
non-overlapping CI; abort on engagement drop. Numbers TBD — measure live.

### Open Questions
- Are propensities reliable for the "show nothing" action? (likely sparse → mark UNKNOWN)
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** the design proceeds dataset → shift → method → OPE → gate in a fixed order.
- **RT-02 (Multi-Dimensional Analysis Framework):** Must / Must Not blocks fence the no-online-interaction and no-fabrication boundaries.
- **CM-02 (Constraint Specification):** the conservatism family is selected by coverage/action-type conditions.
- **DS-06 (Prioritization & Severity Guidance):** unsupported regions and unmeasured numbers are surfaced rather than hidden.
- **QA-12 (False Positives Identification):** an OPE-driven deployment gate must pass before any live claim.

**Related Prompts:**
- `rl_algorithm_selection.md` — choose an online algorithm when interaction is available.
- `rl_evaluation_safety.md` — hard safety gating and shadow/canary design before deployment.
- `rl_problem_framing.md` — decide whether the problem is RL-shaped at all before committing.
