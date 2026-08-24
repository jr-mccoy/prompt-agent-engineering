---
title: "RL Problem Framing & MDP Formulation"
category: AI-ML/specialized-ml/reinforcement-learning
description: "Decide whether a problem is genuinely reinforcement learning, and if so formulate it as a well-posed MDP — state, action, reward, transition, horizon — before any algorithm is chosen."
techniques:
  - ST-02
  - RT-02
  - CM-02
  - QA-12
  - DS-06
difficulty: advanced
tags:
  - reinforcement-learning
  - mdp
  - problem-framing
  - reward
  - sequential-decision
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/specialized-ml/reinforcement-learning/rl_reward_function_design.md
  - domain-AI-ML/specialized-ml/reinforcement-learning/rl_algorithm_selection.md
  - domain-AI-ML/specialized-ml/reinforcement-learning/rl_environment_design.md
---

# RL Problem Framing & MDP Formulation

**Objective:** Determine whether a stated problem actually warrants reinforcement learning — as opposed to supervised learning, bandits, planning, or a hand-written policy — and, if it does, formulate it as a precise Markov Decision Process (state, action, reward, transition, horizon, discount) that downstream reward and algorithm choices can be built on.

**When to Use:**
- Someone proposes "use RL" for a control, recommendation, optimization, or sequencing problem and you need to pressure-test that framing.
- You have a sequential decision problem and need to write down its MDP cleanly before building anything.
- A prior RL effort is thrashing and you suspect the problem was never well-posed.

**When NOT to Use:**
- The decision is single-shot with a labeled correct answer (use supervised learning) or independent one-step decisions with immediate feedback (use contextual bandits — note this, don't force a full MDP).
- The dynamics are known and cheap to simulate end-to-end (a planner/solver may dominate RL).
- For designing the reward once RL is confirmed (use `rl_reward_function_design.md`).

## Inputs / Context

Provide what you can; framing degrades gracefully if some are missing:
- **The decision** — who/what acts, how often, and what they are trying to achieve.
- **Feedback structure** — is reward immediate or delayed; do actions change future state; is there a credit-assignment-over-time problem at all.
- **Observability** — what the agent can actually see at decision time vs. hidden state.
- **Data/interaction regime** — can the agent interact (live or simulated), or only logged data (offline)? Cost/risk of a bad action.
- **Objective & horizon** — episodic or continuing; finite/infinite horizon; what "good" means over time.

## Constraints

**Must:**
- Explicitly answer "is this RL?" before formulating the MDP, with the deciding evidence.
- Define every MDP element concretely against the user's domain, not as abstract placeholders.
- Verify the Markov property holds for the proposed state — or document what must be added to the state to make it hold.

**Must Not:**
- Default to RL because it is fashionable; name the cheaper alternative if it fits.
- Fabricate dynamics, reward magnitudes, or environment behavior the user did not provide; mark unknowns as open questions.
- Conflate the reward (what we want) with shaping signals or with the metric used to evaluate the agent.

**Instructions:**

1. **Test the RL preconditions.** Confirm the three things RL needs: (a) sequential decisions where actions influence future states, (b) feedback that is evaluative (reward) rather than instructive (labels), and (c) a need to optimize long-run return, not one-step accuracy. If any is absent, name the better-fit method.

2. **Rule out cheaper alternatives explicitly.** Map the problem against supervised learning, contextual bandits (no state transitions), classical planning/optimization (known model), and a hand-coded heuristic. State why each does or does not fit.

3. **Define the action space.** Discrete vs continuous, dimensionality, any constraints/safety masks, and the action frequency (decision cadence). Flag combinatorial blowups early.

4. **Define the state/observation.** List what the agent observes; check the Markov property — does the current observation summarize enough history to predict the next state and reward? If not, specify what to add (stacked frames, memory, belief state) or declare it a POMDP.

5. **Define reward and horizon.** State what is rewarded (sketch only — full design is downstream), whether the task is episodic or continuing, the horizon, and a discount factor with a one-line justification tied to how far-sighted the agent should be.

6. **Characterize the transition/interaction regime.** Is the environment available for online interaction, only via simulator, or offline (logged data only)? Note stochasticity, partial observability, and the cost/risk of exploration.

7. **Surface framing risks.** Identify reward-hacking exposure, sparse-vs-dense reward, non-stationarity, and where the formulation could quietly become ill-posed.

8. **Deliver a go / reshape / no-go recommendation.** Conclude whether to proceed with RL, reshape the problem (e.g., to a bandit), or use a non-RL method — ranked by confidence.

**Output Format:**

A markdown report:
- **Is This an RL Problem?** — verdict + deciding evidence + the best alternative if not.
- **MDP Specification** — table: Element (State / Action / Reward / Transition / Horizon / Discount) | Definition | Markov-OK? | Open Questions.
- **Alternatives Considered** — supervised / bandit / planning / heuristic, with fit verdicts.
- **Framing Risks** — ranked (reward hacking, partial observability, exploration cost, non-stationarity).
- **Recommendation** — go / reshape / no-go, with next prompt to run.

## Verification

- [ ] The "is this RL?" question is answered before the MDP is written.
- [ ] At least two non-RL alternatives are explicitly evaluated and accepted/rejected with reasons.
- [ ] Every MDP element is defined against the user's domain, not generically.
- [ ] The Markov property is assessed for the proposed state, with a fix noted if it fails.
- [ ] The interaction regime (online / simulator / offline) is identified, since it constrains everything downstream.

## False-Positive Prevention

❌ **DON'T:**
- Call something RL just because it "makes decisions over time" — a sequence of independent labeled predictions is supervised learning.
- Treat a one-step decision with immediate reward and no state transition as full RL when it is a contextual bandit.
- Assume the Markov property holds because the observation "looks complete."
- Write an MDP whose reward silently encodes the evaluation metric, guaranteeing optimistic self-grading.

✅ **DO:**
- Require that actions demonstrably change future states before committing to RL.
- Downgrade to a bandit when transitions are absent — it is far cheaper and more stable.
- Probe the Markov assumption with a concrete counterexample ("could two states that look identical have different optimal actions?").
- Keep reward (the objective) separate from the evaluation protocol from the start.

## Example Output

```markdown
## RL Framing: Dynamic Warehouse Pick-Route Assignment

### Is This an RL Problem?
**Verdict: Yes (reshape lightly).** Actions (which order to assign next) change future congestion and pending-order state, feedback is evaluative (throughput, not a labeled "correct" route), and we care about long-run throughput over a shift. A pure supervised "predict best route" loses the downstream-congestion effect. **Best alternative considered:** combinatorial optimization per timestep — rejected because the model of future order arrivals is unknown and stochastic.

### MDP Specification
| Element | Definition | Markov-OK? | Open Questions |
|---|---|---|---|
| State | Pending-order queue, picker positions/loads, aisle congestion map | Partial — past arrival rate matters | Add 5-min arrival-rate window |
| Action | Assign next order to one of N pickers, or hold | Yes (masked to idle pickers) | Cap action set at top-k nearest |
| Reward | + orders completed; − total picker idle-time per step | Yes | Penalty weight unknown |
| Transition | Stochastic order arrivals + picker movement | Simulator only | Arrival model fidelity? |
| Horizon | Episodic = one 8-hr shift | Yes | — |
| Discount | γ=0.99 (far-sighted; congestion effects are delayed) | — | — |

### Alternatives Considered
- Supervised (imitate dispatcher logs): rejected — propagates current suboptimal policy, no counterfactual.
- Contextual bandit: rejected — assignments create lasting congestion state (transitions exist).
- MILP per step: partial fit — strong baseline, but no lookahead over stochastic arrivals.

### Framing Risks (ranked)
1. Reward hacking: agent could "hold" orders to avoid idle penalty — needs a completion-deadline term.
2. Partial observability: arrival burstiness hidden — mitigated by arrival-rate feature.
3. Exploration cost: cannot explore on the live floor — train in simulator, hence sim-to-real exposure.

### Recommendation
**Go**, with state augmented by arrival-rate window. Next: `rl_reward_function_design.md` to harden the throughput/idle/deadline tradeoff against hacking.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** preconditions → alternatives → element-by-element MDP build.
- **RT-02 (Multi-Dimensional Analysis Framework):** weighs RL against supervised/bandit/planning/heuristic.
- **CM-02 (Constraint Specification):** Markov property and interaction regime are governing constraints.
- **QA-12 (False Positives Identification):** guards against mislabeling supervised/bandit problems as RL.
- **DS-06 (Prioritization & Severity Guidance):** framing risks and the go/reshape/no-go verdict are ranked.

**Related Prompts:**
- `rl_reward_function_design.md` — once RL is confirmed, design and stress-test the reward.
- `rl_algorithm_selection.md` — pick an algorithm family for the formulated MDP and data regime.
- `rl_environment_design.md` — build the simulator/environment the MDP implies.
