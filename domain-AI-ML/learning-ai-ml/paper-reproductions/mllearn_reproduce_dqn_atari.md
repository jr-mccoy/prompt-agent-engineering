---
title: "Reproduce DQN on a Control/Atari Task"
category: AI-ML/learning-ai-ml/paper-reproductions
description: "A scoped guide to reproducing Deep Q-Networks on a tractable environment — extract the replay, target-network, and epsilon-schedule specs from the actual paper, name the omitted details (frame preprocessing, reward clipping) as risks, and evaluate over seeds against a random/heuristic baseline given RL's high variance."
techniques:
  - ST-02
  - CM-02
  - DS-02
  - RT-05
  - QA-01
difficulty: advanced
tags:
  - reproduction
  - dqn
  - reinforcement-learning
  - deep-rl
  - rigor
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/learning-ai-ml/mllearn_reproduce_paper_plan.md
  - domain-AI-ML/specialized-ml/reinforcement-learning/rl_offline_rl_design.md
  - domain-AI-ML/learning-ai-ml/study-tracks/mllearn_study_track_reinforcement_learning.md
---

# Reproduce DQN on a Control/Atari Task

**Objective:** Guide a learner through reproducing the Deep Q-Network claim — that a single value-based deep-RL agent with experience replay and a target network can learn control directly from high-dimensional input — scoped to a tractable environment and compute, by extracting the algorithmic specifics *from the actual paper*, cataloguing the under-specified details that dominate deep-RL results, and judging success over multiple seeds against a random/heuristic baseline because RL variance makes single runs meaningless.

**When to Use:**
- A learner wants to understand deep RL by rebuilding DQN, not just running a library agent.
- Practicing reproduction rigor where variance and unstated details are the central challenge.
- Building an RL portfolio piece or a trustworthy baseline before extending it.

**When NOT to Use:**
- The learner just wants the paper summarized (use `mllearn_paper_digest_generator.md`).
- They want the general reproduction method (use `domain-AI-ML/learning-ai-ml/mllearn_reproduce_paper_plan.md`).
- They can't yet implement a tabular value method (do the RL study track first).

## Inputs / Context

- **The paper** — the DQN paper itself, open (this guide supplies none of its numbers).
- **Compute budget** — full Atari is expensive; most learners should start on a simpler control env or a single, cheap Atari game with frame-skipping. Compute sets the target.
- **Learner level** — to scope ambition and scaffolding.
- **Purpose** — understanding deep RL, an RL baseline, or a launchpad for new work.

## Constraints

**Must:**
- Extract the algorithmic specifics **from the paper the learner is holding** — this guide names *which* (replay buffer size, target-network update frequency, epsilon schedule, discount, optimizer/LR, minibatch size, network architecture), never their values.
- Define "reproduced" by **mean return over multiple seeds** clearly beating a random/heuristic baseline and showing the learning trend — never a single run.
- Treat frame/observation preprocessing and reward clipping as load-bearing, under-specified details.

**Must Not:**
- State the paper's scores, buffer sizes, or schedule constants from memory — mark all as `[extract from paper]`.
- Let one lucky seed, or performance measured on the training conditions only, count as success.
- Assume the paper's full-Atari scale; reproduce the *behavior* on a tractable env if compute is limited.

**Instructions:**

1. **Pin the reproduction target.** State the claim: on a chosen tractable environment, a DQN agent learns a policy whose mean return over seeds beats a random/heuristic baseline (and, where feasible, approaches a reported level). Record paper numbers as `[extract from paper, Table X]`.

2. **Define "reproduced."** Set the metric (mean episodic return), the number of seeds (RL needs several), a tolerance/threshold, and the evaluation protocol (greedy eval episodes separate from training).

3. **Extract the algorithm spec.** From the paper: replay buffer size, target-network update frequency, epsilon-greedy schedule, discount factor, optimizer/LR, minibatch size, and the network architecture. Mark each Given/Partial/Missing.

4. **Pin preprocessing and reward handling.** Document frame preprocessing (resizing, grayscale, frame stacking, frame skip) and reward clipping — flagging these as load-bearing and often under-specified.

5. **Implement the baseline and scale honestly.** Build a random/heuristic baseline on the same env. If you scaled the env/compute down, state the adjusted target.

6. **Train across seeds and evaluate.** Run several seeds; report mean and spread of returns from separate greedy-evaluation episodes, plus learning curves.

7. **Apply the divergence protocol.** If the agent doesn't learn, check preprocessing and the target-network/epsilon settings first (common culprits), confirm the replay buffer behaves, then the network — before concluding non-reproduction. Distinguish "didn't learn" (likely a bug/instability) from genuine non-reproduction.

**Output Format:**

A markdown reproduction plan + log:
- **Reproduction Target** — the over-baseline claim + `[extract from paper]` reference numbers.
- **Success Criterion** — metric, seed count, threshold, greedy-eval protocol.
- **Algorithm Spec** — extracted; Given/Partial/Missing.
- **Preprocessing & Reward Handling** — frame processing + clipping, flagged as assumptions.
- **Baseline & Scaling** — random/heuristic baseline; env/compute scale-down + adjusted target.
- **Results & Divergence Notes** — multi-seed mean/spread + curves; diagnosis order if it fails.

## Verification

- [ ] All paper-specific numbers appear as `[extract from paper]`, none from memory.
- [ ] Success is mean return over multiple seeds vs a baseline, with greedy evaluation — not one run.
- [ ] Frame preprocessing and reward clipping are documented and flagged as load-bearing.
- [ ] A random/heuristic baseline is implemented on the same env.
- [ ] A divergence protocol separates instability/bugs from genuine non-reproduction.

## False-Positive Prevention

❌ **DON'T:**
- Quote DQN's scores or hyperparameters from memory.
- Call one good seed "reproduced" — RL variance across seeds is large.
- Treat frame preprocessing, frame skip, and reward clipping as trivial.
- Evaluate only under training exploration; use greedy evaluation episodes.

✅ **DO:**
- Keep every paper value as `[extract from paper]` until read from the text/tables.
- Report mean and spread of returns over several seeds vs a baseline.
- Document preprocessing and reward handling as load-bearing assumptions.
- Diagnose failures in order (preprocessing → target/epsilon → replay → network).

## Example Output

```markdown
## Reproduce DQN — claim: learns a policy beating a baseline (tractable env)

### Reproduction Target
On [env], DQN's mean return over seeds beats random/heuristic and shows a learning trend.
Paper reports: [extract from paper, Table X] — do not assume.

### Success Criterion
Metric: mean episodic return (greedy eval). Seeds: 3–5. Reproduced = mean clearly beats baseline
with a learning trend; threshold [extract or set for scaled env]. Single seeds not sufficient.

### Algorithm Spec (extracted)
Replay size, target-update freq, epsilon schedule, discount, optimizer/LR, minibatch, architecture:
[extract from paper §X], each Given/Partial/Missing.

### Preprocessing & Reward Handling
Frame resize/grayscale/stack/skip: [document] — LOAD-BEARING. Reward clipping: [extract] —
LOAD-BEARING. Both flagged as assumptions.

### Baseline & Scaling
Random/heuristic baseline on the same env. Scaled to a simpler env / 1 GPU; adjusted target stated.

### Results & Divergence Notes
If it doesn't learn: check preprocessing + target-update/epsilon first, confirm replay behaves,
then the network, before reporting a specific-gap non-reproduction.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** target → criterion → spec → preprocessing → baseline → run.
- **CM-02 (Constraint Specification):** success as a multi-seed over-baseline result at reduced scale.
- **DS-02 (Metric Specification):** mean return, seed count, threshold, and greedy-eval protocol fixed up front.
- **RT-05 (Evidence-Based Reasoning):** algorithmic and preprocessing details extracted, not assumed.
- **QA-01 (Self-Verification):** the ordered divergence protocol is a built-in correctness check.

**Related Prompts:**
- `domain-AI-ML/learning-ai-ml/mllearn_reproduce_paper_plan.md` — the general reproduction method this guide instantiates.
- `rl_offline_rl_design.md` — deeper on RL evaluation and off-policy considerations.
- `study-tracks/mllearn_study_track_reinforcement_learning.md` — the curriculum this reproduction fits into.
