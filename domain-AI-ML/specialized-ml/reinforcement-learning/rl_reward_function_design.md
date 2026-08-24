---
title: "RL Reward Function Design & Hacking Stress-Test"
category: AI-ML/specialized-ml/reinforcement-learning
description: "Design a reward function that encodes the true objective, then adversarially stress-test it for reward hacking, unintended optima, and shaping artifacts before training."
techniques:
  - ST-02
  - RT-05
  - CM-02
  - QA-12
  - DS-06
difficulty: advanced
tags:
  - reinforcement-learning
  - reward-design
  - reward-hacking
  - specification-gaming
  - reward-shaping
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/specialized-ml/reinforcement-learning/rl_problem_framing.md
  - domain-AI-ML/specialized-ml/reinforcement-learning/rl_evaluation_safety.md
  - domain-AI-ML/specialized-ml/reinforcement-learning/rl_environment_design.md
---

# RL Reward Function Design & Hacking Stress-Test

**Objective:** Translate a real-world objective into a reward function for an RL agent, then adversarially probe it for the failure that defines RL — the agent maximizing reward while defeating the intent (reward hacking / specification gaming) — and produce a hardened reward plus a watchlist of exploit signatures to monitor during training.

**When to Use:**
- The MDP is framed and you must now write the reward signal.
- An agent is achieving high reward but doing something obviously wrong (classic specification gaming).
- You are adding reward shaping to speed learning and want to confirm it doesn't change the optimal policy.

**When NOT to Use:**
- The problem isn't yet confirmed as RL or the MDP isn't defined (use `rl_problem_framing.md` first).
- You only need to evaluate a trained agent's performance/safety (use `rl_evaluation_safety.md`).

## Inputs / Context

Provide what you can:
- **True objective** — what success means to the stakeholder, in plain language, including what must never happen.
- **MDP elements** — state/action/horizon, decision cadence, episodic vs continuing (from framing).
- **Candidate reward** — any existing reward terms, weights, and shaping signals.
- **Constraints & safety limits** — hard limits (must-never) vs soft preferences.
- **Known exploit surface** — degenerate actions, loopholes, or "do nothing" strategies the environment allows.

## Constraints

**Must:**
- Tie every reward term to a specific clause of the stated objective or constraint — no orphan terms.
- For each term, name at least one way an optimizer could satisfy it while violating intent.
- Distinguish the *objective* reward (defines the optimal policy) from *shaping* (speeds learning but must be potential-based or otherwise policy-invariant).

**Must Not:**
- Invent stakeholder priorities, magnitudes, or trade-off weights the user did not state; mark them as decisions to confirm.
- Encode the evaluation metric directly into reward such that the agent self-grades.
- Recommend dense shaping that changes which policy is optimal without flagging the risk.

**Instructions:**

1. **Restate the true objective and the must-nevers.** Separate what we want maximized from hard constraints that must never be violated regardless of reward. The latter are candidates for constrained-RL or termination, not soft penalties alone.

2. **Decompose into reward terms.** Propose terms for primary objective, costs, and constraints, each traced to a clause of the objective. Note units and the sign of each term.

3. **Adversarially attack each term.** For every term, role-play a pure reward-maximizer: how could it inflate this term without doing the real task? Catalog degenerate strategies (stalling, oscillating, exploiting episode boundaries, sensor gaming, "kill-the-task-to-stop-the-penalty").

4. **Check term interactions and balance.** Examine how terms trade off; identify weights where one term dominates or cancels another. Flag where the implied optimum diverges from intent and where weights are unknown decisions.

5. **Classify and validate shaping.** For any dense/shaping signal, confirm it is potential-based or argue why it won't shift the optimal policy. Replace risky shaping with curriculum, better state features, or sparse-but-correct reward where possible.

6. **Decide on hard-constraint handling.** For must-nevers, recommend constrained RL (cost budget / Lagrangian), action masking, or terminal penalties with episode end — not a tunable soft penalty that exploration may "pay through."

7. **Define exploit watchpoints.** Produce the monitoring signatures (e.g., "reward rising while task-completion flat", "agent ends episodes early") that indicate hacking during training.

8. **Deliver the hardened reward.** Present final terms, weights (or decisions needed), constraint mechanism, and the residual risks that remain.

**Output Format:**

A markdown report:
- **Objective & Must-Nevers** — maximized objective vs hard constraints.
- **Reward Terms** — table: Term | Clause it serves | Sign/Units | Hacking risk | Mitigation.
- **Reward-Hacking Attack Log** — degenerate strategies found, per term, with the fix.
- **Shaping Audit** — each shaping signal: policy-invariant? yes/no/decision.
- **Constraint Handling** — mechanism for each must-never.
- **Exploit Watchlist** — signals to monitor during training.
- **Hardened Reward Spec** — final terms + open weight decisions + residual risks.

## Verification

- [ ] Every reward term traces to a stated objective/constraint clause.
- [ ] Each term has at least one explicit reward-hacking attack and a mitigation.
- [ ] Objective reward and shaping are separated; shaping is shown policy-invariant or flagged.
- [ ] Hard constraints use a constraint mechanism, not only a soft penalty.
- [ ] An exploit watchlist is provided for use during training, not just at the end.

## False-Positive Prevention

❌ **DON'T:**
- Assume a reward is "fine" because it makes sense to a human — optimizers find the loophole, not the intent.
- Add dense shaping to "help learning" without checking it changes the optimal policy.
- Encode a must-never as a small negative reward the agent can profitably violate.
- Treat high training reward as evidence the objective is met — it may be the hack succeeding.

✅ **DO:**
- Adversarially simulate a pure maximizer for each term and look for the cheapest exploit.
- Prefer potential-based shaping, curriculum, or better features over reward hacks that bias the optimum.
- Use constrained RL / masking / termination for safety limits.
- Pair reward with an independent task-completion signal so hacking shows up as reward-up/task-flat divergence.

## Example Output

```markdown
## Reward Design: Robotic Cube-Stacking Agent

### Objective & Must-Nevers
- Maximize: number of cubes correctly stacked and held stable for ≥3s.
- Must-never: collide with the human workspace boundary; drop a cube off-table.

### Reward Terms
| Term | Clause | Sign/Units | Hacking risk | Mitigation |
|---|---|---|---|---|
| +1 per stable stack | primary | sparse, +1 | "flick & catch" pseudo-stacks | require 3s stability check in env |
| +0.01·height | shaping | dense | tip a tall single column (not stacking) | gate by base-contact check |
| −0.1 per boundary breach | safety | dense neg | pay penalty to take shortcut | move to hard termination + cost budget |
| −time | efficiency | dense neg | knock cubes off to end episode early | add −5 terminal for off-table drop |

### Reward-Hacking Attack Log
1. **Height-shaping exploit:** agent learns to balance one cube vertically to farm height reward without stacking. Fix: only credit height when a stack base is detected; demote height to a curriculum stage that is removed once stacking emerges.
2. **Early-termination exploit:** with −time pressure, agent sweeps cubes off-table to end the episode and stop accruing penalty. Fix: large terminal penalty for off-table drop + episode does not end on drop.

### Shaping Audit
- height bonus: NOT policy-invariant as written → gated + scheduled (decision: remove at stage 2).
- time penalty: invariant w.r.t. correct policy, but interacts with termination → kept after drop-penalty fix.

### Constraint Handling
- Boundary breach: terminate episode + cost-budget Lagrangian (constrained RL), not soft penalty.

### Exploit Watchlist
- Episode reward rising while `stacks_completed` flat → height farming.
- Mean episode length collapsing with off-table drops up → early-termination hack.

### Hardened Reward Spec
Sparse +1 stable-stack; gated/scheduled height shaping; cost-constrained boundary; terminal off-table penalty. Open decision: efficiency weight (−time) magnitude. Residual risk: stability sensor noise could be gamed — monitor.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** objective → terms → adversarial attack → constraints → watchlist.
- **RT-05 (Evidence-Based Reasoning):** every term anchored to an objective clause.
- **CM-02 (Constraint Specification):** must-nevers handled as hard constraints, not soft penalties.
- **QA-12 (False Positives Identification):** core to catching reward-hacking and policy-shifting shaping.
- **DS-06 (Prioritization & Severity Guidance):** exploits ranked; safety constraints prioritized over shaping.

**Related Prompts:**
- `rl_problem_framing.md` — define the MDP this reward serves.
- `rl_evaluation_safety.md` — verify at eval time that the reward wasn't hacked.
- `rl_environment_design.md` — the env must support the stability/boundary checks this reward needs.
