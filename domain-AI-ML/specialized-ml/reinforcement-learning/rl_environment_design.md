---
title: "RL Environment & Simulator Design"
category: AI-ML/specialized-ml/reinforcement-learning
description: "Design or wrap an RL environment/simulator — observation and action spaces, reset/termination semantics, determinism, and the sim-to-real gap — so the thing the agent learns in matches the thing it must act in."
techniques:
  - ST-02
  - RT-05
  - CM-02
  - QA-12
  - RT-10
difficulty: advanced
tags:
  - reinforcement-learning
  - environment-design
  - simulator
  - sim-to-real
  - observation-space
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/specialized-ml/reinforcement-learning/rl_problem_framing.md
  - domain-AI-ML/specialized-ml/reinforcement-learning/rl_reward_function_design.md
  - domain-AI-ML/specialized-ml/reinforcement-learning/rl_evaluation_safety.md
---

# RL Environment & Simulator Design

**Objective:** Specify or wrap the environment an RL agent will train in — observation space, action space, reset and termination semantics, stochasticity, time-step semantics, and the sim-to-real gap — so that a policy that succeeds in the environment is likely to succeed in the real target, and so the environment cannot be gamed by artifacts of its own design.

**When to Use:**
- The MDP is framed and you must build or adapt a simulator / Gym-style environment.
- You are wrapping a real system (logged data, a physics sim, a digital twin) for RL training.
- An agent learns well in sim but fails in deployment, and you suspect environment mismatch.

**When NOT to Use:**
- The problem isn't yet confirmed as RL or the MDP is undefined (use `rl_problem_framing.md`).
- You only need the reward signal (use `rl_reward_function_design.md`).
- You are evaluating an already-trained agent (use `rl_evaluation_safety.md`).

## Inputs / Context

Provide what you can; the design degrades gracefully if some are missing:
- **MDP spec** — state/action/reward/horizon from framing.
- **Target deployment** — the real system the agent must eventually act in, and how it differs from any simulator.
- **Available sim/data** — existing simulator, physics engine, digital twin, or only logged transitions (offline).
- **Fidelity & cost** — how accurate the sim is, and the cost/latency of one environment step.
- **Safety & reset constraints** — what a "reset" means in the real world; whether arbitrary resets are even possible.

## Constraints

**Must:**
- Define observation and action spaces concretely (types, bounds, units) and confirm they match what the agent can sense/do at deployment.
- Specify reset distribution, termination/truncation conditions, and time-step semantics (what one step physically means).
- Enumerate the sim-to-real gaps that matter and how each is mitigated (domain randomization, system ID, calibration, or accepted risk).

**Must Not:**
- Invent simulator fidelity, noise levels, or dynamics the user did not provide — mark them as measurements to obtain.
- Let the observation expose information unavailable at deployment (a form of train/serve skew that inflates sim performance).
- Treat episode truncation (time-limit) as true termination in the bootstrapping logic without flagging it.

**Instructions:**

1. **Define the observation space against deployment sensing.** List each observation, its type/bounds/units, and confirm the same signal is available, with the same timing and noise, at deployment. Flag any observation that is privileged (sim-only) — it must be removed or replaced with an estimator.

2. **Define the action space and its real-world realizability.** Discrete/continuous, bounds, rate limits, and safety masks. Verify the agent's actions map cleanly to actuators/decisions in the target and respect physical limits.

3. **Specify reset and initial-state distribution.** What states an episode can start in, how diverse they are, and whether the real system can actually be reset. Insufficient start diversity causes narrow, brittle policies.

4. **Specify termination vs. truncation.** Separate genuine episode end (goal/failure) from time-limit truncation, and note that the two must be handled differently in value bootstrapping. Define all termination conditions.

5. **Characterize stochasticity and determinism.** Note where randomness enters (dynamics, observation noise, opponent), whether seeds are controlled for reproducibility, and whether the sim is too deterministic (over-fit-able) relative to reality.

6. **Map the sim-to-real gap.** Enumerate concrete discrepancies (dynamics, latency, sensor noise, unmodeled effects) and assign a mitigation: domain randomization, system identification, calibration, real-data fine-tuning, or accepted-and-monitored risk.

7. **Audit for environment-gaming artifacts.** Identify loopholes the agent could exploit that exist only because of the env implementation (clipping bugs, infinite-energy glitches, reward leaking through observations, boundary teleports).

8. **Deliver the environment spec + validation plan.** Provide the full spec and a short plan to validate the env (sanity policies, random-agent baseline behavior, real-vs-sim trajectory comparison).

**Output Format:**

A markdown report:
- **Observation Space** — table: Signal | Type/Bounds/Units | Available at deploy? | Notes.
- **Action Space** — table: Action | Type/Bounds | Real-world realizable? | Safety mask.
- **Reset & Termination** — initial-state distribution; termination vs truncation conditions.
- **Stochasticity & Determinism** — sources of randomness; seeding; over-determinism risk.
- **Sim-to-Real Gap Register** — table: Discrepancy | Severity | Mitigation.
- **Environment-Gaming Watchlist** — implementation loopholes to test for.
- **Validation Plan** — how to confirm the env behaves and matches reality before training.

## Verification

- [ ] Every observation is confirmed available at deployment with matching timing/noise, or flagged as privileged.
- [ ] Action space maps to real actuators/decisions and respects physical/rate limits.
- [ ] Reset distribution and its real-world feasibility are stated.
- [ ] Termination is distinguished from time-limit truncation.
- [ ] At least the top sim-to-real gaps are enumerated with explicit mitigations.
- [ ] Assumed fidelity/noise numbers are flagged as measurements to obtain, not facts.

## False-Positive Prevention

❌ **DON'T:**
- Expose a privileged simulator state (true positions, future events) in the observation — it inflates sim scores and collapses on deployment.
- Treat a perfectly deterministic simulator as realistic; agents overfit its exact dynamics.
- Bootstrap value across a time-limit truncation as if it were a real terminal state.
- Assume a low sim-to-real gap because the sim "looks right" without comparing real vs sim trajectories.

✅ **DO:**
- Match the observation to exactly what the deployed agent can sense, with realistic noise/latency.
- Add domain randomization or system ID for the dynamics that differ from reality.
- Mark truncation explicitly so the learner bootstraps correctly at time limits.
- Validate the env with a random agent and a hand-coded policy before trusting any learning curve.

## Example Output

```markdown
## Environment Design: Quadruped Locomotion (sim → real robot)

### Observation Space
| Signal | Type/Bounds/Units | Available at deploy? | Notes |
|---|---|---|---|
| Joint angles (12) | float, rad, ±π | Yes | encoder noise ~0.5° → add |
| Joint velocities (12) | float, rad/s | Yes | finite-diff noisy on real |
| Base orientation (IMU) | quaternion | Yes | IMU drift to randomize |
| True base velocity | float m/s | NO (sim-only) | PRIVILEGED → estimate or drop |

### Action Space
| Action | Type/Bounds | Real-world realizable? | Safety mask |
|---|---|---|---|
| Target joint pos (12) | float, ±0.6 rad from default | Yes | clamp to torque limits |

### Reset & Termination
- Initial state: randomized base height, yaw, and joint perturbations (±0.1 rad). Real reset = manual replace; limited diversity → rely on randomization.
- Termination: base height < 0.2 m (fall) or roll/pitch > 50° → terminal. Truncation at 1000 steps (NOT terminal — bootstrap value).

### Stochasticity & Determinism
- Randomness: dynamics randomization (mass ±15%, friction 0.6–1.2), observation noise, action delay 0–2 steps. Seeded for eval. Sim otherwise deterministic → over-determinism mitigated by randomization.

### Sim-to-Real Gap Register
| Discrepancy | Severity | Mitigation |
|---|---|---|
| Motor latency/backlash | High | action-delay + actuator net (system ID) |
| Privileged base velocity | High | train a velocity estimator from history |
| Contact/friction model | Med | friction domain randomization |
| IMU drift | Med | randomize bias |

### Environment-Gaming Watchlist
- Agent exploiting integrator blow-up to "fly" — clamp velocities, test with random actions.
- Reward leaking via privileged obs — confirm obs vector at deploy == train.

### Validation Plan
1. Random agent: confirm falls terminate, no NaNs, episode lengths sane.
2. Hand-coded trot: should walk slowly → sanity of dynamics.
3. Compare 5 real vs sim trajectories under identical actions before any training.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** spaces → reset/termination → stochasticity → gap → validation.
- **RT-05 (Evidence-Based Reasoning):** each gap and observation grounded in deployment reality.
- **CM-02 (Constraint Specification):** deployment sensing/actuation limits as governing constraints.
- **QA-12 (False Positives Identification):** catches privileged-observation and env-gaming inflation.
- **RT-10 (Troubleshooting Decision Tree):** structures the sim-fails-on-real diagnosis path.

**Related Prompts:**
- `rl_problem_framing.md` — the MDP this environment must implement.
- `rl_reward_function_design.md` — the env must support the checks the reward relies on.
- `rl_evaluation_safety.md` — evaluate the trained agent accounting for the gaps logged here.
