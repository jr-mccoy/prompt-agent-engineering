# Reinforcement Learning

Framing a problem as RL, designing the reward and environment, choosing an algorithm, and evaluating safely — plus the three settings that matter most in practice: offline RL, RLHF/RLAIF, and multi-agent.

**8 prompts.** Part of [`domain-AI-ML/`](../README.md) — see the domain README for the lifecycle routing table and the [boundary with adjacent domains](../README.md#boundary-with-adjacent-domains).

## When to enter here

- A sequential decision problem where actions change future state.
- Reward design is producing behaviour nobody intended.
- Training from logged data rather than a live environment.

**Not here:**
- The problem is a one-shot prediction rather than a sequence of decisions — RL machinery is overhead.
- The multi-agent question is about LLM agents coordinating — [`../../agentic-ai-systems/aiagent_multi_agent_orchestration.md`](../../agentic-ai-systems/aiagent_multi_agent_orchestration.md).

## Prompts

| Prompt | Use it to |
|---|---|
| [`rl_problem_framing.md`](rl_problem_framing.md) | Decide whether a problem is genuinely reinforcement learning, and if so formulate it as a well-posed MDP — state, action, reward, transition, horizon — before any algorithm is chosen. |
| [`rl_reward_function_design.md`](rl_reward_function_design.md) | Design a reward function that encodes the true objective, then adversarially stress-test it for reward hacking, unintended optima, and shaping artifacts before training. |
| [`rl_environment_design.md`](rl_environment_design.md) | Design or wrap an RL environment/simulator — observation and action spaces, reset/termination semantics, determinism, and the sim-to-real gap — so the thing the agent learns in matches the thing it must act in. |
| [`rl_algorithm_selection.md`](rl_algorithm_selection.md) | Choose an RL algorithm family — value-based, policy-gradient, actor-critic, offline, or model-based — by matching it to the action space, data/interaction regime, sample budget, and safety needs of the problem. |
| [`rl_evaluation_safety.md`](rl_evaluation_safety.md) | Evaluate an RL agent honestly under high return variance, detect reward hacking and overfitting to the training environment, and build in safety/constraint handling before any deployment claim. |
| [`rl_offline_rl_design.md`](rl_offline_rl_design.md) | Design an offline (batch) RL setup that learns a policy from a fixed logged dataset with no environment interaction — handling distributional shift, out-of-distribution actions, conservative learning methods, and off-policy evaluation before any deployment. |
| [`rl_rlhf_rlaif_pipeline_design.md`](rl_rlhf_rlaif_pipeline_design.md) | Design a preference-optimization pipeline that aligns an LLM or policy from human or AI feedback — preference data collection, reward-model training, the optimization step (PPO vs DPO vs others), and KL/regularization to prevent reward over-optimization. |
| [`rl_multi_agent_rl_design.md`](rl_multi_agent_rl_design.md) | Design a multi-agent RL setup across cooperative, competitive, or mixed settings — handling non-stationarity from co-adapting agents, centralized-training-decentralized-execution, credit assignment, and evaluation against a population of opponents rather than a single fixed one. |

## Conventions

- **Prefix:** `rl_` — one prefix per subdirectory, so a filename identifies its home.
- **Frontmatter:** the domain's eight fields — `title`, `category` (`AI-ML/specialized-ml/reinforcement-learning`), `description`, `techniques` (validated against `techniques/MASTER_TECHNIQUE_INDEX.md`), `difficulty`, `tags`, `updated`, `related_prompts`.
- **Structure:** five H2 sections — `Inputs / Context`, `Constraints`, `Verification`, `False-Positive Prevention`, `Example Output` — with `Objective`, `When to Use`, `When NOT to Use`, `Instructions`, `Output Format`, `Techniques Used`, `Related Prompts` as bold labels inside them.
- **No fabrication:** no invented benchmark numbers, accuracy figures, SOTA claims, or dataset statistics. Quantities that would change a decision are marked for measurement or verification.
- **Framework-neutral:** the user names the stack; prompts avoid hardcoding APIs that drift.

## What lives elsewhere

- RLHF as part of an LLM fine-tuning workflow → [`../../genai-llm-engineering/genai_fine_tuning_workflow.md`](../../genai-llm-engineering/genai_fine_tuning_workflow.md).
- Bandits for exploration in recommendation → [`../recommender-systems/recsys_bandits_exploration.md`](../recommender-systems/recsys_bandits_exploration.md).
