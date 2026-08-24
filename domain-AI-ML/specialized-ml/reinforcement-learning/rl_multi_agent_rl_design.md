---
title: "Multi-Agent RL Design"
category: AI-ML/specialized-ml/reinforcement-learning
description: "Design a multi-agent RL setup across cooperative, competitive, or mixed settings — handling non-stationarity from co-adapting agents, centralized-training-decentralized-execution, credit assignment, and evaluation against a population of opponents rather than a single fixed one."
techniques:
  - ST-02
  - RT-02
  - CM-02
  - DS-06
  - QA-12
difficulty: advanced
tags:
  - reinforcement-learning
  - multi-agent
  - non-stationarity
  - ctde
  - self-play
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/specialized-ml/reinforcement-learning/rl_algorithm_selection.md
  - domain-AI-ML/specialized-ml/reinforcement-learning/rl_environment_design.md
  - domain-AI-ML/specialized-ml/reinforcement-learning/rl_evaluation_safety.md
---

# Multi-Agent RL Design

**Objective:** Help the user design a multi-agent reinforcement learning (MARL) setup where several learning agents act in a shared environment — cooperatively, competitively, or in mixed teams. MARL breaks the core single-agent assumption: as other agents learn, the environment each agent faces is non-stationary, so a policy that looks strong against today's opponents can collapse tomorrow. This prompt routes the training paradigm (centralized training with decentralized execution vs fully decentralized vs self-play), addresses credit assignment in cooperative teams, and — critically — specifies evaluation against a population of opponents rather than a single fixed or self-play partner, since beating one opponent says little about robustness.

**When to Use:**
- Multiple agents act and learn in the same environment (team games, markets, traffic, negotiation, multi-robot).
- You must decide between centralized-training/decentralized-execution, independent learners, or self-play.
- You need an evaluation protocol robust to co-adaptation and strategy cycling, not a single matchup.

**When NOT to Use:**
- There is effectively one learning agent and others are fixed scripted entities — treat as single-agent and use `rl_algorithm_selection.md`.
- Your blocker is environment/reward construction for the multi-agent world — see `rl_environment_design.md`.
- You need deployment safety gating for the trained agents — see `rl_evaluation_safety.md`.

## Inputs / Context

Provide what you can:
- **Setting type** — cooperative (shared reward), competitive (zero-sum), or mixed (teams / general-sum).
- **Number and symmetry of agents** — homogeneous vs heterogeneous roles; whether they share parameters.
- **Observability** — fully observed joint state vs partial/local observations per agent.
- **Communication** — whether agents can exchange messages and whether that channel is learned.
- **Reward structure** — global team reward vs individual rewards, and the credit-assignment difficulty.
- **Opponent / partner set** — what you will train and evaluate against (fixed bots, self-play, a learned population).

## Constraints

**Must:**
- Treat non-stationarity from co-adapting agents as the central design risk and choose a paradigm that accounts for it.
- Specify how training-time information (centralized critic, joint state) is used without leaking into decentralized execution.
- Address credit assignment explicitly in cooperative settings (e.g., value decomposition or counterfactual baselines).
- Evaluate against a population/distribution of opponents or partners, not a single fixed one.

**Must Not:**
- Treat other learning agents as a static part of the environment when they are co-adapting.
- Report strength from a single matchup or against the current self-play partner only.
- Fabricate reward/return/win-rate numbers or cite benchmark results from memory; reason from the user's setup and mark unknowns — measure in their environment.
- Use, at execution time, centralized information that will not be available when agents are deployed.

**Instructions:**

1. **Classify the setting.** Determine cooperative / competitive / mixed and general-sum vs zero-sum; this drives the credit-assignment and evaluation design.
2. **Name the non-stationarity.** Identify how each agent's environment shifts as others learn, and the resulting instability (chasing a moving target, strategy cycling).
3. **Choose a training paradigm.** Route by observability and reward: CTDE with a centralized critic when you have joint info at train time but local execution; independent learners for simple/decoupled cases; self-play / population-based for competitive symmetric games.
4. **Design credit assignment (cooperative).** Specify value decomposition (VDN/QMIX-style) or a counterfactual baseline (COMA-style) so individual contributions to a shared reward are separable.
5. **Guard the train/execute boundary.** Ensure centralized critics or joint observations are used only in training, never in the deployed decentralized policy.
6. **Design the opponent/partner population.** For competition, plan a league / population (past checkpoints, diverse strategies) rather than a single self-play partner; for cooperation, plan partner diversity to avoid co-adaptation brittleness.
7. **Define population-based evaluation.** Specify cross-play / round-robin against held-out strategies and an exploitability or generalization metric.
8. **Plan measurement.** State that win rates, returns, and exploitability must be measured in the user's environment across multiple seeds, not asserted.

**Output Format:**

A markdown design brief:
- **Setting Classification** — coop/comp/mixed, sum type, agent symmetry.
- **Non-Stationarity Risk** — how co-adaptation destabilizes learning here.
- **Training Paradigm** — CTDE / independent / self-play choice with rationale.
- **Credit Assignment** — decomposition or counterfactual baseline (if cooperative).
- **Train/Execute Boundary** — what centralized info is used and how leakage is prevented.
- **Opponent/Partner Population** — league/population plan and diversity strategy.
- **Evaluation Plan** — cross-play protocol and generalization/exploitability metric.
- **Open Questions / Unknowns** — items to measure, marked explicitly.

## Verification

- [ ] The setting (coop/comp/mixed, sum type) is classified before method choice.
- [ ] Non-stationarity from co-adaptation is named and addressed by the chosen paradigm.
- [ ] Credit assignment is specified for cooperative settings.
- [ ] No centralized/joint information leaks into decentralized execution.
- [ ] Evaluation is against a population/distribution of opponents, not a single fixed one.
- [ ] No reward/return/win-rate/benchmark numbers are fabricated; all are flagged to be measured in the user's environment across multiple seeds.

## False-Positive Prevention

❌ **DON'T:**
- Treat co-adapting agents as a static environment — that ignores non-stationarity and the "strong" policy will track a moving target it loses to later.
- Declare an agent strong because it beats a single fixed opponent or its current self-play partner; it has likely overfit that one strategy and will collapse against new ones.
- Leak the centralized critic's joint-state access into the policy that must act on local observations at deployment.
- Average a global team reward across agents and call it credit assignment.

✅ **DO:**
- Use CTDE or explicit non-stationarity handling, and state how the train/execute boundary is enforced.
- Evaluate via cross-play / round-robin against a population including held-out and past-checkpoint strategies; report exploitability or generalization.
- Decompose shared reward (value decomposition or counterfactual baseline) so individual contributions are learnable.
- Maintain partner/opponent diversity during training to avoid brittle co-adaptation.

## Example Output

```markdown
## Setting Classification
Mixed: two cooperative teams of 3, competitive across teams (general-sum).
Homogeneous within team, parameter-sharing per role.

### Non-Stationarity Risk
Each team co-adapts; a strategy that beats the opposing team's current policy
becomes exploitable once they update → cycling.

### Training Paradigm
CTDE with a centralized critic over the joint team state; decentralized actors
on local observations. Self-play league across team checkpoints.

### Credit Assignment
QMIX-style monotonic value decomposition for the shared team reward.

### Train/Execute Boundary
Centralized critic used ONLY in training; deployed actors see local obs only.

### Opponent/Partner Population
League of past team checkpoints + 2 scripted styles to prevent strategy collapse.

### Evaluation Plan
Round-robin cross-play vs held-out team strategies; report win rate +
exploitability estimate. Numbers TBD — measure across 5 seeds.

### Open Questions
- Does parameter sharing hurt role specialization? (mark UNKNOWN until measured)
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** flow is classify → non-stationarity → paradigm → credit → boundary → population → eval.
- **RT-02 (Multi-Dimensional Analysis Framework):** Must / Must Not blocks fence the no-static-opponent and no-fabrication boundaries.
- **CM-02 (Constraint Specification):** the training-paradigm choice is routed by observability, reward, and symmetry.
- **DS-06 (Prioritization & Severity Guidance):** brittleness, leakage, and unmeasured numbers are surfaced explicitly.
- **QA-12 (False Positives Identification):** population-based cross-play gates any strength claim.

**Related Prompts:**
- `rl_algorithm_selection.md` — single-agent algorithm choice when others are fixed/scripted.
- `rl_environment_design.md` — construct the multi-agent environment and reward structure.
- `rl_evaluation_safety.md` — safety gating and robustness checks before deploying the agents.
