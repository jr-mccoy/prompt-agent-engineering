---
title: "Reinforcement Learning Specialization Study Track"
category: AI-ML/learning-ai-ml/study-tracks
description: "An instantiated, phased RL curriculum — MDPs/tabular methods → value/policy methods → deep RL → evaluation/safety — with prerequisite gates, an environment/build per phase, and checkpoints, with RL's distinctive evaluation pitfalls made explicit."
techniques:
  - ED-01
  - ST-02
  - DS-06
  - RP-01
  - CM-02
difficulty: intermediate
tags:
  - reinforcement-learning
  - study-track
  - curriculum
  - specialization
  - evaluation
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/learning-ai-ml/mllearn_study_path_designer.md
  - domain-AI-ML/specialized-ml/reinforcement-learning/rl_offline_rl_design.md
  - domain-AI-ML/learning-ai-ml/mllearn_portfolio_project_designer.md
---

# Reinforcement Learning Specialization Study Track

**Objective:** Give a learner a concrete, phased reinforcement-learning curriculum — sequenced by prerequisite, anchored to an environment/build and a demonstrable checkpoint per phase, and tuned to their honest starting level and weekly hours — so they reach working RL competence (implement and *honestly evaluate* an agent across seeds) instead of copying a deep-RL repo they can't debug or trust.

**When to Use:**
- A learner with solid ML/math basics wants to specialize in RL and needs the order and the eval discipline.
- An existing plan jumps to deep RL without tabular/value-method foundations.
- The learner can run deep-RL code but can't tell whether results are real (variance, no baseline).

**When NOT to Use:**
- The learner needs a generic, any-goal study path generator (use `mllearn_study_path_designer.md`).
- They want a specific offline-RL system designed (use `rl_offline_rl_design.md`).
- They lack probability/linear-algebra/ML foundations — fix that via a general study path first.

## Inputs / Context

- **Current level** — honest math (probability, linear algebra), ML, and any prior RL exposure.
- **Goal** — be specific (e.g., "understand and implement deep RL," "apply RL to a control problem," "research-readiness").
- **Time budget** — hours/week and target horizon.
- **Compute access** — RL is sample-hungry and high-variance; compute constrains which environments are realistic.
- **Theory vs applied bias** — how much derivation (Bellman, policy gradients) vs implementation.

## Constraints

**Must:**
- Sequence phases by prerequisite — MDPs and tabular methods before value/policy approximation before deep RL.
- Pair every phase with an implementation on a tractable environment and a checkpoint, and make **multi-seed evaluation against a baseline** an explicit, recurring deliverable.
- Surface RL's distinctive failure modes early: high variance across seeds, reward hacking/Goodhart, evaluation on the training environment, brittle hyperparameters.

**Must Not:**
- Invent specific course names, book titles, paper score numbers, or "best algorithm" claims from memory — describe the resource *type* and direct the learner to verify the current one.
- Schedule deep RL before the learner can implement and reason about a tabular value method.
- Let a single lucky run or training-environment performance count as "it works."

**Instructions:**

1. **Pin the goal and "done."** Restate the concrete RL goal and what reaching it looks like. Reverse-engineer the track from this.

2. **Assess the entry point.** Map math/ML/RL strengths and gaps; name the prerequisite gaps that set the start.

3. **Lay out the phase dependency order.** Present the sequence — MDPs + dynamic programming → tabular value/policy methods → function approximation → deep RL (value-based, policy-gradient/actor-critic) → evaluation + safety/offline RL — marking skippables.

4. **Phase to the time budget and compute.** Size phases in weeks; pick environments that fit the learner's compute (start with simple control, not pixel-based Atari unless compute allows).

5. **Make multi-seed evaluation a deliverable each phase.** Require runs across multiple seeds, a random/heuristic baseline, and held-out or distinct evaluation conditions — RL's variance makes single runs meaningless.

6. **Insert checkpoints and adjust-points.** Define how each phase is proven (can implement X, agent beats baseline across seeds) and where to re-plan.

7. **Right-size resources.** Recommend a small number of resource *types* per phase (one structured course/book + one implementation tutorial + one canonical paper), not a long list.

**Output Format:**

A markdown study track:
- **Goal & Definition of Done** — the concrete target.
- **Entry Point** — strengths, gaps, where the track starts.
- **Phase Dependency Order** — sequenced, skippables marked.
- **Phased Plan** — table per phase: Weeks | Topics | Environment/Build | Eval (seeds + baseline) | Checkpoint.
- **RL Evaluation Discipline** — multi-seed, baseline, distinct-eval, reward-hacking watch.
- **Resources** — a few resource *types* per phase (verify current canonical picks).
- **Adjust-Points** — where to re-plan if pace slips.

## Verification

- [ ] Phases ordered by prerequisite (MDPs/tabular → approximation → deep RL).
- [ ] Every phase has an implementation, multi-seed eval + baseline, and a checkpoint.
- [ ] Environments fit the stated compute; pace fits the hours/week.
- [ ] RL-specific pitfalls (variance, reward hacking, train-env eval) are addressed recurrently.
- [ ] No invented course/book/paper names or score figures — resource *types* only.

## False-Positive Prevention

❌ **DON'T:**
- Start at deep RL before the learner can implement a tabular value method.
- Let one good run or training-environment performance count as success.
- Cite specific algorithm score numbers or "the best algorithm is X" from memory.
- Pick pixel-based environments that the learner's compute can't train.
- Ignore reward hacking — agents optimize the reward you wrote, not the one you meant.

✅ **DO:**
- Build MDP/tabular intuition before function approximation and deep RL.
- Require multiple seeds, a baseline, and distinct evaluation conditions every phase.
- Describe resource *types*; tell the learner to verify the current canonical resource.
- Match environments to compute; start simple.
- Add a reward-hacking / Goodhart watch to every phase that designs a reward.

## Example Output

```markdown
## RL Study Track — Goal: "Understand and implement deep RL, honestly evaluated" (level: strong ML/math, no RL; 8 hrs/wk; single GPU; 5 mo)

### Goal & Definition of Done
Can implement a value-based and a policy-gradient agent, evaluate across seeds vs a baseline,
and explain RL's variance/reward-hacking pitfalls; has 1 RL portfolio project.

### Entry Point
Strong: ML, probability, linear algebra. Gaps: all RL. Start at Phase 1 (MDPs/tabular).

### Phase Dependency Order
MDPs + dynamic programming → tabular value/policy methods → function approximation → deep RL
(value-based, then actor-critic) → evaluation + safety/offline RL.

### Phased Plan
| Weeks | Topics | Environment/Build | Eval (seeds + baseline) | Checkpoint |
|---|---|---|---|---|
| 1–3 | MDPs, value/policy iteration | Tabular gridworld | Exact vs random policy | Derives + implements value iteration |
| 4–6 | Tabular Q-learning/SARSA | Simple control (tabular) | 5 seeds vs random | Agent beats random across seeds |
| 7–9 | Function approximation | Classic control (continuous state) | 5 seeds vs heuristic | Stable learning curve, multi-seed |
| 10–14 | Deep RL (value + actor-critic) | A tractable control env | 5+ seeds vs baseline | Reproduces expected behavior; project |
| 15–20 | Evaluation + offline/safety | Re-evaluate prior agents | Distinct eval conditions | Reports variance honestly; reward-hack check |

### RL Evaluation Discipline
Always: multiple seeds (RL variance is large), a random/heuristic baseline, and evaluation
conditions distinct from training. Watch for reward hacking on every reward you design.

### Resources
Per phase: one structured course/book (verify current canonical), one implementation tutorial,
one landmark paper to read critically.

### Adjust-Points
If function approximation is unstable, extend it before deep RL. Re-check pace at weeks 6 and 14.
```

**Techniques Used:**
- **ED-01 (Iterative Scaffolding):** phases build from MDP intuition up to deep RL.
- **ST-02 (Structured Sequential Instructions):** goal → entry point → dependency order → phases.
- **DS-06 (Prioritization & Severity Guidance):** dependency-driven sequencing; skippables marked.
- **RP-01 (Audience/Level Adaptation):** scope, pace, and environments tuned to level, time, and compute.
- **CM-02 (Constraint Specification):** time budget, compute, and prerequisites as hard constraints.

**Related Prompts:**
- `mllearn_study_path_designer.md` — the generic generator this track instantiates for RL.
- `rl_offline_rl_design.md` — deep reference for the offline-RL/safety phase.
- `mllearn_portfolio_project_designer.md` — design the RL project this track schedules.
