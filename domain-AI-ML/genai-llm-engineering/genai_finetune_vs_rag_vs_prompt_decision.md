---
title: "Prompt vs RAG vs Fine-Tuning Decision"
category: AI-ML/genai-llm-engineering
description: "Decide among prompt engineering, retrieval-augmented generation, and fine-tuning for an LLM task using a structured tradeoff across knowledge type, behavior change, cost, latency, and maintenance — escalating only when a cheaper option provably fails."
techniques:
  - RT-02
  - DS-06
  - CM-02
  - RT-05
  - ST-03
difficulty: intermediate
tags:
  - rag
  - fine-tuning
  - prompt-engineering
  - decision-framework
  - tradeoffs
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/genai-llm-engineering/genai_fine_tuning_workflow.md
  - domain-AI-ML/genai-llm-engineering/genai_rag_system_design.md
  - domain-AI-ML/genai-llm-engineering/genai_llm_cost_latency_optimization.md
---

# Prompt vs RAG vs Fine-Tuning Decision

**Objective:** Recommend whether an LLM task is best served by prompt engineering, retrieval-augmented generation, fine-tuning, or a combination — by separating *what kind of gap* exists (knowledge vs behavior vs format vs reasoning) and weighing each option against cost, latency, maintenance, and data availability, with a bias toward the cheapest approach that meets the bar.

**When to Use:**
- Starting a new LLM feature and choosing the adaptation approach.
- A prompt-only solution is hitting a quality ceiling and you're considering RAG or fine-tuning.
- Someone is pushing to fine-tune and you need a structured check that it's actually warranted.

**When NOT to Use:**
- The decision is already made and you need to execute (use `genai_fine_tuning_workflow.md` or `genai_rag_system_design.md`).
- This is a pure ops/cost-routing question across models (see `domain-software-engineering/devops/`).

## Inputs / Context

State the candidate model + provider + version. Provide what you can:
- **Task** — what the model must do, with examples of good and bad outputs.
- **Gap type** — is the model missing *knowledge*, the right *behavior/style/format*, *fresh/changing data*, or *reasoning capability*?
- **Data** — volume and quality of labeled examples; availability of a retrievable corpus.
- **Constraints** — latency SLA, cost ceiling, hosting (can you serve a custom model?), update frequency, privacy.
- **Current state** — what's been tried (prompt versions, RAG prototype) and where it fell short.

## Constraints

**Must:**
- Diagnose the *gap type* first; the right tool follows from it (knowledge gaps lean RAG, behavior/format gaps lean fine-tuning, reasoning gaps lean better model/prompt).
- Compare options on the same axes: quality fit, cost (build + run), latency, data needs, maintenance, and freshness.
- Recommend the cheapest sufficient option and define the evidence that would justify escalating.

**Must Not:**
- Recommend fine-tuning for knowledge that changes frequently — it bakes in a stale snapshot.
- Assume RAG fixes behavior/style problems (it supplies context, not new behavior) or that prompting alone holds complex format constraints at scale.
- Fabricate cost or accuracy figures; frame them as ranges to measure on the user's task.

**Instructions:**

1. **Classify the gap.** Decide whether the failure is missing knowledge (and is it static or changing?), wrong behavior/style/format, insufficient reasoning, or grounding/hallucination. Multiple gaps may coexist — name each.

2. **Map gaps to candidate tools.** Knowledge (changing) → RAG; knowledge (static, narrow) → prompt or fine-tune; behavior/style/format → prompt then fine-tune; reasoning → stronger model / better prompt / decomposition; grounding → RAG + prompt discipline. Note combinations (e.g., RAG + light fine-tune).

3. **Score each candidate on the decision axes.** Build a matrix: quality fit, build cost, run cost, latency, data required, maintenance burden, freshness handling. Use the user's constraints as the weights.

4. **Apply the escalation ladder.** Default to prompt engineering; escalate to RAG only if the gap is retrievable knowledge/grounding; escalate to fine-tuning only when prompt+RAG provably can't hold the behavior/format and you have quality labeled data and can serve a custom model.

5. **Define the proof for escalation.** State the experiment that would justify moving up a rung (e.g., "if a tuned prompt + RAG still scores < X on the held-out set, then fine-tune"). Tie to a metric and held-out set.

6. **Account for maintenance and drift.** Factor in re-tuning when base models update, corpus refresh for RAG, and prompt-rot — these change the long-run cost comparison.

7. **Recommend and sequence.** Give the recommended approach (or staged plan: prompt now, RAG next, fine-tune only if proven), the rationale, and the cross-link to the execution prompt.

**Output Format:**

A markdown decision brief:
- **Gap Diagnosis** — gap type(s) and whether knowledge is static or changing
- **Decision Matrix** — table: Option | Quality fit | Build cost | Run cost | Latency | Data need | Maintenance | Freshness
- **Escalation Ladder** — what justifies moving from prompt → RAG → fine-tune
- **Recommendation** — chosen approach (or staged plan) + rationale
- **Proof-to-Escalate** — the experiment + metric that would unlock the next rung
- **Next Step** — pointer to the execution prompt

## Verification

- [ ] The gap type is diagnosed before any tool is recommended.
- [ ] Changing knowledge is routed to RAG, not baked into a fine-tune.
- [ ] All options are scored on the same axes, weighted by the user's constraints.
- [ ] The recommendation favors the cheapest sufficient option with a defined escalation proof.
- [ ] Maintenance/drift cost is included in the comparison.
- [ ] Cost/accuracy figures are ranges-to-measure, not fabricated.

## False-Positive Prevention

❌ **DON'T:**
- Recommend fine-tuning to "teach the model our docs" when the docs change — that's a RAG job.
- Assume RAG will fix tone, format, or refusal behavior; retrieval changes *what* the model sees, not *how* it responds.
- Jump to fine-tuning before exhausting prompt engineering and RAG, especially without quality labeled data.
- Compare options only on build cost and ignore recurring run + maintenance + re-tune cost.

✅ **DO:**
- Diagnose knowledge-vs-behavior-vs-reasoning first; the gap dictates the tool.
- Default to the cheapest rung and require a measured failure before escalating.
- Consider combinations (RAG for knowledge + light fine-tune for format) when gaps coexist.
- Price in long-run maintenance: corpus refresh, prompt rot, and re-tuning on base-model updates.

## Example Output

```markdown
## Decision: Legal-Clause Explainer (model: <provider/model vX>)

### Gap Diagnosis
- Knowledge: needs current clause library — CHANGING (updated monthly) -> retrievable.
- Behavior: must answer in a fixed structured format with citations -> partly promptable.
- Reasoning: comparison/multi-hop across clauses -> model-capability dependent.

### Decision Matrix
| Option | Quality fit | Build | Run | Latency | Data need | Maint. | Freshness |
|---|---|---|---|---|---|---|---|
| Prompt only | partial (no fresh clauses) | low | low | low | none | prompt rot | poor |
| RAG | strong (fresh + cited) | med | med | med | corpus | corpus refresh | excellent |
| Fine-tune | wrong tool (stale knowledge) | high | med | low | many labels | re-tune | poor |

### Escalation Ladder
Prompt -> RAG (knowledge is changing + needs citation). Fine-tune NOT justified: knowledge churns.

### Recommendation
RAG with a strict citation prompt. If structured-format compliance < 95% after prompt tuning,
add a small LoRA *format* adapter — not a knowledge fine-tune.

### Proof-to-Escalate
Build held-out set of 80 clause questions. If RAG + tuned prompt format-compliance < 0.95,
then (and only then) train the format adapter per genai_fine_tuning_workflow.md.

### Next Step
-> genai_rag_system_design.md
```

**Techniques Used:**
- **RT-02 (Multi-Dimensional Analysis Framework):** options scored across quality/cost/latency/maintenance.
- **DS-06 (Prioritization & Severity Guidance):** the escalation ladder ranks cheapest-sufficient first.
- **CM-02 (Constraint Specification):** user constraints weight the matrix.
- **RT-05 (Evidence-Based Reasoning):** escalation requires a measured failure, not a hunch.
- **ST-03 (Output Format Specification):** decision matrix + laddered recommendation.

**Related Prompts:**
- `genai_fine_tuning_workflow.md` — execute if the ladder lands on fine-tuning.
- `genai_rag_system_design.md` — execute if the ladder lands on RAG.
- `genai_llm_cost_latency_optimization.md` — weigh the run-cost differences across the three approaches. (See also the LLM cost/routing one-offs under `domain-software-engineering/devops/`.)
