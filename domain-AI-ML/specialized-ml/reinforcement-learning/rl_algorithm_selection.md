---
title: "RL Algorithm Family Selection"
category: AI-ML/specialized-ml/reinforcement-learning
description: "Choose an RL algorithm family — value-based, policy-gradient, actor-critic, offline, or model-based — by matching it to the action space, data/interaction regime, sample budget, and safety needs of the problem."
techniques:
  - RT-02
  - ST-02
  - CM-02
  - DS-06
  - QA-12
difficulty: advanced
tags:
  - reinforcement-learning
  - algorithm-selection
  - offline-rl
  - model-based-rl
  - actor-critic
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/specialized-ml/reinforcement-learning/rl_problem_framing.md
  - domain-AI-ML/specialized-ml/reinforcement-learning/rl_environment_design.md
  - domain-AI-ML/specialized-ml/reinforcement-learning/rl_evaluation_safety.md
---

# RL Algorithm Family Selection

**Objective:** Recommend an RL algorithm *family* (not a tuned hyperparameter set) — value-based, policy-gradient, actor-critic, offline/batch RL, or model-based RL — that fits the problem's action space, interaction/data regime, sample budget, stability needs, and safety constraints, with the deciding tradeoffs made explicit and the cheaper baselines named first.

**When to Use:**
- The MDP is framed and the environment is roughly known, and you must pick an approach to implement.
- A current algorithm is unstable, sample-inefficient, or unsafe and you want to re-evaluate the family choice.
- You have only logged data and need to know whether online RL is even viable.

**When NOT to Use:**
- The problem isn't confirmed as RL (use `rl_problem_framing.md`).
- You need hyperparameter tuning of an already-chosen algorithm (out of scope — this picks the family, not the config).
- You need to evaluate a trained agent (use `rl_evaluation_safety.md`).

## Inputs / Context

Provide what you can; selection degrades gracefully if some are missing:
- **Action space** — discrete (size) vs continuous (dimensionality); structured/hierarchical.
- **Interaction regime** — unlimited online interaction, expensive/limited online, simulator-only, or offline logged data only.
- **Sample budget** — how many environment steps/episodes are affordable (and their cost/risk).
- **Reward structure** — sparse vs dense; horizon length.
- **Stability & reproducibility needs** — production reliability, variance tolerance.
- **Safety constraints** — must-never conditions; whether exploration is dangerous.

## Constraints

**Must:**
- Map the decisive problem features (action space, data regime, sample budget, safety) to the recommended family explicitly.
- Name a baseline to beat first (random / heuristic / behavior-cloning) before any deep-RL family.
- State the failure mode the recommended family is most prone to and how it will be detected.

**Must Not:**
- Recommend online algorithms (PPO, SAC, DQN) when only logged data exists — that requires offline RL or a simulator.
- Cite specific benchmark scores or "X beats Y on Atari/MuJoCo" numbers from memory as if measured; reason from the user's regime and mark external claims as unverified.
- Present a single family as universally best; surface the tradeoff that could flip the choice.

**Instructions:**

1. **Anchor on the interaction/data regime first.** This is the hardest constraint: offline-only data → offline RL (e.g., conservative value methods, behavior-regularized) or imitation; simulator with cheap steps → online methods are open; expensive/risky real interaction → sample-efficient (model-based / off-policy) or offline-then-finetune.

2. **Branch on the action space.** Discrete + moderate size → value-based (DQN-family) viable; large/continuous → policy-gradient or actor-critic (off-policy actor-critic for sample efficiency, on-policy for stability); combinatorial → consider structured/hierarchical or action factorization.

3. **Weigh sample efficiency vs. stability.** On-policy methods are more stable but sample-hungry; off-policy and model-based are sample-efficient but trickier to stabilize. Match to the sample budget.

4. **Consider model-based RL when steps are precious.** If a dynamics model is learnable and steps are expensive, model-based planning can slash sample cost — but flag model-bias risk.

5. **Establish the baseline ladder.** Specify the baselines to clear in order (random → heuristic/PID/rules → behavior cloning on logs → the chosen RL family). Skipping this is how teams ship RL that a heuristic would beat.

6. **Factor in safety and exploration risk.** If exploration is dangerous, prefer offline RL, constrained RL, or sim-train-then-deploy; avoid algorithms whose exploration could trigger must-never states live.

7. **Name the dominant failure mode + detection.** For the recommended family, state its characteristic failure (value overestimation, policy collapse, distributional shift in offline RL, model exploitation) and the signal that reveals it.

8. **Deliver a ranked recommendation.** Primary family + one fallback, each with the regime fit, expected risks, and the baseline it must beat.

**Output Format:**

A markdown report:
- **Decisive Constraints** — table: Feature | Value | Implication for choice.
- **Family Fit Matrix** — table: Family | Fit (High/Med/Low) | Why | Main risk.
- **Baseline Ladder** — ordered baselines to clear before trusting RL.
- **Recommendation** — primary + fallback, with the tradeoff that would flip it.
- **Dominant Failure Mode & Detection** — for the recommended family.

## Verification

- [ ] The interaction/data regime is identified and used as the first filter.
- [ ] Offline-only data is never paired with an online-only algorithm recommendation.
- [ ] A baseline ladder (incl. a non-RL baseline) is specified before the RL family.
- [ ] The recommendation names its dominant failure mode and how it'll be detected.
- [ ] No fabricated benchmark numbers; external claims marked unverified.
- [ ] A fallback family and the tradeoff that would flip the choice are given.

## False-Positive Prevention

❌ **DON'T:**
- Recommend PPO/SAC/DQN when the user only has logged data and no simulator — that is an offline-RL or imitation problem.
- Assume deep RL is needed before checking a heuristic or bandit beats it.
- Pick value-based methods for high-dimensional continuous control where they struggle.
- Quote "algorithm X is SOTA" from memory as if it were a measured result for this problem.

✅ **DO:**
- Filter on data regime first; it eliminates whole families immediately.
- Require the chosen family to beat a behavior-cloning / heuristic baseline before celebrating.
- Match action-space type to the family's natural domain (discrete→value, continuous→actor-critic/PG).
- State the family's known failure mode and its monitoring signal up front.

## Example Output

```markdown
## Algorithm Selection: HVAC Energy Control (commercial building)

### Decisive Constraints
| Feature | Value | Implication |
|---|---|---|
| Interaction regime | 2 years logged BMS data; live exploration risky (comfort) | Offline RL or sim-first |
| Action space | Continuous setpoints (4 dims) | Actor-critic / PG family |
| Sample budget | Cannot freely experiment on live building | Sample efficiency critical |
| Safety | Must-never: temp outside 19–25°C occupied | Constrained / offline |

### Family Fit Matrix
| Family | Fit | Why | Main risk |
|---|---|---|---|
| Offline RL (behavior-regularized) | High | Uses logs, no risky exploration | Distributional shift / OOD actions |
| Model-based (learn building dynamics) | High | Cheap planning, few real steps | Model bias exploited by planner |
| On-policy PG (PPO) | Low | Needs lots of live interaction | Unsafe exploration on real building |
| Value-based (DQN) | Low | Continuous actions | Discretization loss |

### Baseline Ladder
1. Current rule-based BMS schedule (incumbent).
2. Behavior cloning of best historical operators.
3. Offline RL must beat BC and the rule-based controller on logged-counterfactual energy + comfort.

### Recommendation
**Primary:** Offline RL with conservative/behavior-regularized value estimation, validated via off-policy evaluation. **Fallback:** model-based RL trained on a calibrated building sim. Tradeoff that flips it: if a high-fidelity sim becomes available and trustworthy, model-based + sim training overtakes pure offline.

### Dominant Failure Mode & Detection
Offline RL over-values out-of-distribution actions (distributional shift). Detect via OPE confidence intervals and flagging actions far from the logged behavior policy; reject the policy if it relies on unsupported actions.
```

**Techniques Used:**
- **RT-02 (Multi-Dimensional Analysis Framework):** the family-fit matrix across regime/action/sample/safety axes.
- **ST-02 (Structured Sequential Instructions):** regime-first → action space → efficiency → baselines → recommendation.
- **CM-02 (Constraint Specification):** data regime and safety limits as the governing filters.
- **DS-06 (Prioritization & Severity Guidance):** ranked recommendation + baseline ladder.
- **QA-12 (False Positives Identification):** prevents online-algorithm-on-offline-data and SOTA-from-memory errors.

**Related Prompts:**
- `rl_problem_framing.md` — confirm the problem is RL and the regime before selecting.
- `rl_environment_design.md` — a simulator's availability changes the family choice.
- `rl_evaluation_safety.md` — evaluate the chosen algorithm with variance- and safety-aware protocols.
