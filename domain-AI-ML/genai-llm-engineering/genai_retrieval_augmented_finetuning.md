---
title: "Retrieval-Augmented Fine-Tuning (RAFT)"
category: AI-ML/genai-llm-engineering
description: "Decide among fine-tuning, RAG, and RAFT (both together), and if RAFT, design training data with gold plus distractor documents so the model learns to ground answers in retrieved context, cite, and reject irrelevant retrievals — instead of memorizing facts that go stale."
techniques:
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-12
difficulty: advanced
tags:
  - raft
  - fine-tuning
  - rag
  - distractor-documents
  - grounding
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/genai-llm-engineering/genai_finetune_vs_rag_vs_prompt_decision.md
  - domain-AI-ML/genai-llm-engineering/genai_rag_system_design.md
  - domain-AI-ML/genai-llm-engineering/genai_fine_tuning_workflow.md
---

# Retrieval-Augmented Fine-Tuning (RAFT)

**Objective:** Produce a defensible decision about whether a workload needs fine-tuning, RAG, or RAFT (fine-tuning a model specifically to use retrieved context well), and if RAFT, design the training data — gold documents plus deliberate distractors — and the evaluation so the model learns to ground answers in retrieval, cite sources, and ignore irrelevant retrievals. The output keeps volatile facts in the retrieval layer where they can be updated, and reserves fine-tuning for the skill of *using* that retrieval, not for memorizing the facts themselves.

**When to Use:**
- You have a closed-domain QA or assistant task where answers must come from a known corpus and stay current.
- Plain RAG works but the model ignores, misreads, or fails to cite retrieved context, or gets distracted by near-miss passages.
- You are weighing fine-tuning against RAG and suspect the answer is a combination.

**When NOT to Use:**
- You have not yet made the fine-tune/RAG/prompt decision at all — start with `genai_finetune_vs_rag_vs_prompt_decision.md`.
- You only need to design or debug the retrieval pipeline — use `genai_rag_system_design.md`.
- You need the general supervised fine-tuning mechanics — use `genai_fine_tuning_workflow.md`.

## Inputs / Context

Provide what you can:
- **Task** — the question/answer or assistant behavior, and what a correct, grounded answer looks like.
- **Corpus** — the source documents, their volatility (how often facts change), and size.
- **Current failure mode** — what plain RAG gets wrong (ignores context, hallucinates, no citations, distracted by similar passages).
- **Retriever** — the existing or planned retriever and its typical top-k quality.
- **Training data availability** — questions with gold answers and known source passages you can build from.
- **Citation requirement** — whether outputs must cite specific sources, and in what format.
- **Compute / latency budget** — constraints on fine-tuning effort and on serving the RAFT model.

## Constraints

**Must:**
- First confirm whether the problem is retrieval, generation, or staleness — RAFT only fixes how the model *uses* retrieval.
- Keep volatile, frequently-changing facts in the retrieval layer; do not bake them into weights.
- Build RAFT training examples that include distractor documents alongside gold documents.
- Train and evaluate the model to cite and to explicitly ignore irrelevant retrieved passages.

**Must Not:**
- Recommend fine-tuning to memorize facts that change — those belong in retrieval, not weights.
- Construct training data with only gold documents (no distractors) — the model then never learns to reject irrelevant retrievals.
- Invent benchmark/eval numbers from memory — measure grounding, citation, and distractor-rejection on your data and mark unknowns.
- Assert version-specific fine-tuning API behavior or limits from memory — verify against current docs.

**Instructions:**

1. **Diagnose the real failure.** Determine whether the problem is bad retrieval, weak generation/grounding, or fact staleness. If retrieval is broken, fix it before RAFT. If facts go stale, that is a retrieval-layer job, not weights.
2. **Confirm the fit for RAFT.** RAFT is indicated when retrieval returns relevant context but the model ignores it, fails to cite, or is thrown off by near-miss distractor passages. State the evidence.
3. **Design the training schema.** Each example pairs a question with a context set: the gold document(s) plus deliberately chosen distractor documents, and a target answer that grounds in and cites the gold while ignoring the distractors.
4. **Choose distractors deliberately.** Sample distractors from the retriever's realistic top-k near-misses, not random unrelated text — the model must learn to reject the passages it will actually retrieve.
5. **Mix gold-only and distractor-heavy examples.** Include some examples where no gold document is present so the model learns to abstain or say it cannot answer rather than confabulate.
6. **Specify grounding and citation targets.** Define the required output form: answer grounded in retrieved context with explicit citations, and an abstention path when the context does not support an answer.
7. **Design the evaluation.** Measure grounding (answer supported by cited source), citation accuracy, distractor-rejection rate, and abstention correctness on a held-out set from the user's corpus.
8. **Recommend and stage.** Propose RAFT (or plain RAG / plain fine-tune if RAFT is not warranted), the data-build plan, and a rollout gated on grounding and distractor-rejection metrics.

**Output Format:**

A markdown decision + design brief:
- **Failure Diagnosis** — retrieval vs generation vs staleness, with evidence.
- **Approach Decision** — fine-tune / RAG / RAFT, and why.
- **Training Schema** — example structure: question, gold docs, distractor docs, grounded/cited target.
- **Distractor Strategy** — how distractors are sampled from realistic retriever output.
- **Abstention Cases** — gold-absent examples that teach "I can't answer from this."
- **Grounding & Citation Spec** — required output form and citation format.
- **Evaluation Plan** — grounding, citation accuracy, distractor-rejection, abstention metrics on the user's data.
- **Recommendation & Rollout** — staged plan with metric gates.

## Verification

- [ ] The real failure (retrieval / generation / staleness) is diagnosed before RAFT is recommended.
- [ ] Volatile facts stay in the retrieval layer; fine-tuning targets *using* retrieval, not memorizing facts.
- [ ] Training examples include realistic distractor documents, plus some gold-absent abstention cases.
- [ ] Evaluation measures grounding, citation accuracy, and distractor-rejection — not just answer correctness.
- [ ] Distractors are sampled from the retriever's actual near-misses, not random text.
- [ ] No benchmark/eval numbers are stated from memory; unknowns are marked and measured on the user's corpus.

## False-Positive Prevention

❌ **DON'T:**
- Fine-tune the model to memorize domain facts when retrieval was the real fix — those facts go stale and the weights lie.
- Build RAFT data from gold documents only; with no distractors the model never learns to reject irrelevant retrievals.
- Judge RAFT success by answer accuracy alone while ignoring whether the answer was actually grounded in the cited source.
- Use random unrelated passages as distractors — the model must learn to reject the realistic near-misses it will retrieve.

✅ **DO:**
- Keep changeable facts in retrieval; reserve fine-tuning for the *behavior* of grounding, citing, and rejecting distractors.
- Mix gold + distractor and gold-absent examples so the model learns both grounding and honest abstention.
- Evaluate grounding and distractor-rejection rate explicitly, on a held-out slice of the user's corpus.
- Sample distractors from the retriever's real top-k near-misses for the questions in training.

## Example Output

```markdown
## Failure Diagnosis
Retriever returns the right passage in top-3 ~88% of the time, but the model
often answers from a similar-looking distractor or omits citations.
=> Retrieval is adequate; the gap is in *using* retrieval. RAFT indicated.

### Training Schema (per example)
Q: "What is the refund window for Plan B?"
Context: [gold: policy.md §4] + [distractor: policy.md §4 for Plan A] + [distractor: FAQ]
Target: "30 days [policy.md §4]." (grounded in gold, cites it, ignores Plan A passage)

### Abstention Cases
~15% of examples omit the gold doc; target = "The provided context does not
state this." (teaches refusal over confabulation)

### Evaluation Plan
Held-out (our corpus): grounding rate, citation accuracy, distractor-rejection
rate, abstention correctness. (All UNMEASURED pre-train — gates before rollout.)
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** Sequences diagnose → decide → schema → distractors → eval so RAFT is only recommended after the failure is understood.
- **RT-02 (Multi-Dimensional Analysis Framework):** Frames the model as an ML engineer accountable for grounding and freshness, not just answer accuracy.
- **DS-01 (Framework Application):** Separates the retrieval, grounding, and staleness concerns so each is solved in the right layer.
- **CM-02 (Constraint Specification):** Forces distractor inclusion and keeps volatile facts out of weights.
- **QA-12 (False Positives Identification):** Ensures evaluation covers grounding, citation, distractor-rejection, and abstention rather than a single accuracy number.

**Related Prompts:**
- `genai_finetune_vs_rag_vs_prompt_decision.md` — the upstream choice this prompt refines into RAFT when both are needed.
- `genai_rag_system_design.md` — designing the retrieval layer RAFT depends on.
- `genai_fine_tuning_workflow.md` — general supervised fine-tuning mechanics for the training run.
