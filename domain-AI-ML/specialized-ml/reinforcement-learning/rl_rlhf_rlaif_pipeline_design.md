---
title: "RLHF / RLAIF Pipeline Design"
category: AI-ML/specialized-ml/reinforcement-learning
description: "Design a preference-optimization pipeline that aligns an LLM or policy from human or AI feedback — preference data collection, reward-model training, the optimization step (PPO vs DPO vs others), and KL/regularization to prevent reward over-optimization."
techniques:
  - ST-02
  - RT-02
  - CM-02
  - DS-01
  - QA-12
difficulty: advanced
tags:
  - reinforcement-learning
  - rlhf
  - rlaif
  - preference-optimization
  - reward-model
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/specialized-ml/reinforcement-learning/rl_reward_function_design.md
  - domain-AI-ML/specialized-ml/reinforcement-learning/rl_evaluation_safety.md
  - domain-AI-ML/genai-llm-engineering/genai_fine_tuning_workflow.md
---

# RLHF / RLAIF Pipeline Design

**Objective:** Help the user design a preference-based alignment pipeline that shapes an LLM or policy from human (RLHF) or AI (RLAIF) feedback. A complete pipeline has four coupled stages: collecting comparison/preference data, training a reward model that scores outputs, running the optimization step that pushes the policy toward higher reward, and constraining that optimization (typically a KL penalty against a reference model) so the policy does not over-optimize a reward model that is only a noisy proxy for true preferences. The defining failure mode is Goodhart's law — the policy games the reward model and climbs the reward number while real quality falls. This prompt routes the optimization-algorithm choice (PPO vs DPO vs others), specifies the regularization, and defines evaluation that does not trust the reward model alone.

**When to Use:**
- You have (or can collect) pairwise preference comparisons over model outputs and want to align behavior to them.
- You are choosing between an explicit reward-model + PPO loop and a direct-preference method (DPO/IPO/KTO-style).
- You need to prevent reward over-optimization and quantify alignment with held-out, non-reward-model evaluation.

**When NOT to Use:**
- You only need supervised fine-tuning on demonstrations — see `genai_fine_tuning_workflow.md`; preference optimization usually comes after SFT.
- Your task is shaping a non-preference scalar reward in a control/game setting — see `rl_reward_function_design.md`.
- Your primary concern is deployment safety gating and red-teaming — see `rl_evaluation_safety.md`.

## Inputs / Context

Provide what you can:
- **Base / reference model** — the SFT checkpoint the policy starts from and that KL is measured against.
- **Feedback source** — human raters, an AI judge (RLAIF), or a hybrid; and the rating protocol (pairwise, rankings, ratings).
- **Preference data volume and quality** — count, inter-annotator agreement, and known biases (length, sycophancy, formatting).
- **Objective** — what "good" means (helpfulness, harmlessness, format adherence) and any explicit constraints.
- **Compute / serving budget** — whether a separate online RL loop (PPO) is feasible or a single-stage method (DPO) is preferred.
- **Evaluation assets** — held-out prompts, human eval capacity, and any task metrics independent of the reward model.

## Constraints

**Must:**
- Treat the reward model as a noisy, potentially biased proxy — never as ground truth.
- Include an explicit regularizer (KL penalty to the reference model, or DPO's implicit constraint) and state what it controls.
- Evaluate the final policy with held-out signals that are independent of the reward model (human eval or task metrics), not just reward score.
- Separate preference data used to train the reward model from data used to evaluate it.

**Must Not:**
- Optimize reward without a KL/regularization term — that invites reward hacking.
- Treat a rising reward-model score as evidence of improved quality on its own.
- Fabricate reward/return numbers, win rates, or cite benchmark results from memory; reason from the user's setup and mark unknowns — measure in their environment.
- Tune the KL coefficient on the same prompts used for the final human/task evaluation.

**Instructions:**

1. **Confirm the starting point.** Verify an SFT checkpoint exists; preference optimization assumes a competent base and a reference model for KL.
2. **Design preference collection.** Specify pairwise vs ranking protocol, source (human/AI), volume, and audit for biases (length, position, sycophancy) — defer the underlying reward semantics to `rl_reward_function_design.md`.
3. **Decide reward model vs direct preference.** Route via conditions: explicit reward model + PPO when you want an online loop and reusable scorer; DPO/IPO/KTO when you want a simpler, stabler single stage and have clean pairwise data.
4. **Train and validate the reward model (if used).** Hold out comparisons; report agreement with held-out preferences and probe for exploitable biases.
5. **Specify the optimization step.** For PPO: rollout, reward scoring, advantage, KL-penalized update. For DPO: the contrastive loss with its implicit reference-model constraint and the β temperature.
6. **Set the regularization.** Explain the KL coefficient (or DPO β) as the over-optimization brake and that its value is empirical, swept on a validation set.
7. **Design over-optimization detection.** Plot a held-out true-quality metric vs reward; watch for the point where reward keeps rising but quality falls (Goodhart turn).
8. **Plan measurement.** State that win rates, reward curves, and KL must be measured in the user's environment across multiple seeds, not asserted.

**Output Format:**

A markdown pipeline brief:
- **Starting Point** — base/SFT checkpoint and reference model for KL.
- **Preference Data Plan** — protocol, source, volume, bias audit.
- **Reward Model vs Direct Preference** — chosen route with rationale.
- **Optimization Step** — PPO or DPO/variant details, including the regularizer.
- **Over-Optimization Guardrails** — KL/β setting plan and the Goodhart detection metric.
- **Evaluation Plan** — held-out, reward-model-independent signals; data separation.
- **Open Questions / Unknowns** — items to measure, marked explicitly.

## Verification

- [ ] An SFT/base checkpoint and a KL reference model are confirmed.
- [ ] The reward-model-vs-DPO decision is justified by data quality and compute.
- [ ] An explicit regularizer (KL coefficient or DPO β) is specified with its role stated.
- [ ] Final evaluation uses signals independent of the reward model, on separated data.
- [ ] An over-optimization (Goodhart) detection metric is defined.
- [ ] No reward/win-rate/benchmark numbers are fabricated; all are flagged to be measured in the user's environment across multiple seeds.

## False-Positive Prevention

❌ **DON'T:**
- Push reward up without a KL penalty and call it improvement — that is reward over-optimization / reward hacking, and the policy will Goodhart the reward model.
- Treat the reward model as the source of truth; it is a noisy, biased proxy for real preferences (often biased toward length or formatting).
- Skip the KL/β regularizer "to converge faster" — the brake is the point.
- Tune the KL coefficient on the evaluation prompts and then report those win rates.

✅ **DO:**
- Regularize toward the reference model and sweep the KL coefficient on a validation split.
- Audit the reward model for exploitable biases and hold out comparisons to measure its agreement.
- Track a held-out true-quality metric against reward to catch the Goodhart turn early.
- Confirm final gains with human or task evaluation independent of the reward model.

## Example Output

```markdown
## Starting Point
SFT checkpoint v3 as both policy init and KL reference.

### Preference Data Plan
~40k pairwise comparisons (helpfulness). Source: hybrid human + AI judge.
Bias audit: check length bias (longer-wins rate) and position bias.

### Reward Model vs Direct Preference
DPO chosen: clean pairwise data, single GPU budget, no need for a reusable
online scorer; β as the implicit KL brake.

### Optimization Step
DPO contrastive loss over (prompt, chosen, rejected); reference = SFT v3.
β controls deviation from reference.

### Over-Optimization Guardrails
Sweep β on validation. Plot held-out human-eval win rate vs DPO loss to find
the Goodhart turn. Reduce aggressiveness past the turn.

### Evaluation Plan
Held-out prompt set scored by human raters (not the AI judge used in training);
report win rate vs SFT v3 with CIs. Numbers TBD — measure across 3 seeds.

### Open Questions
- Is the AI-judge feedback correlated with the human held-out set? (mark UNKNOWN until measured)
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** stages flow data → reward model → optimization → regularization → eval in order.
- **RT-02 (Multi-Dimensional Analysis Framework):** Must / Must Not blocks fence the no-KL-free-optimization and no-fabrication boundaries.
- **CM-02 (Constraint Specification):** the PPO-vs-DPO choice is routed by data quality and compute conditions.
- **DS-01 (Framework Application):** the reward-model-vs-direct-preference tradeoff is made explicit.
- **QA-12 (False Positives Identification):** reward-model-independent evaluation gates any quality claim.

**Related Prompts:**
- `rl_reward_function_design.md` — define what the preference/reward actually encodes before optimizing it.
- `rl_evaluation_safety.md` — safety gating, red-teaming, and deployment checks for the aligned model.
- `genai_fine_tuning_workflow.md` — the SFT stage that precedes preference optimization.
