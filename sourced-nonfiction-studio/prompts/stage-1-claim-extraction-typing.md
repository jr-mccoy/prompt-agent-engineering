# Stage 1 — Claim Extraction & Typing

**Role in pipeline:** Turns the author's undifferentiated braindump into an atomic, typed claim list — the spine everything downstream operates on.

**Objective:** Decompose the source material into atomic claims and tag each by type and load-bearing status, so the pipeline knows what needs sourcing, what needs labeling, and what needs nothing.

**Orchestrates:** `domain-reasoning-craft/epistemic/epistemic_claim_inference_separator.md` (the primary engine), optionally `domain-research-academic/research_question_formulation.md` to turn load-bearing claims into searchable questions.

---

## Inputs
- Scope Record (from Stage 0).
- The author's material, wrapped in `<material>...</material>`.

## Instructions
1. **Atomize.** Split the material into single-assertion claims. One claim = one checkable statement. Break compound sentences apart.
2. **Type each claim** into exactly one:
   - `verifiable-fact` — a statement about the world that could, in principle, be sourced.
   - `professional-judgment` — the author's earned opinion/recommendation.
   - `original-analysis` — the author's own synthesis/model/framework.
   - `common-knowledge` — uncontroversial, needs no citation.
   - `experiential-opinion` — "in my experience" claims.
   - `claim-about-named-person` — asserts something about an identifiable living party (also feeds Stage 5).
3. **Flag load-bearing.** Mark claims the argument depends on, or that a reader would act on. Load-bearing `verifiable-fact` claims are the priority queue for Stage 2 source discovery.
4. **Watch for inference-dressed-as-fact.** A sentence that sounds factual but is really the author's inference gets typed `original-analysis` or `professional-judgment`, not `verifiable-fact`. This split is the whole point — surface it.
5. **Turn load-bearing facts into search questions** (optional, aids Stage 2): phrase each as an answerable question.

## Output Format
```
## Claim Ledger
| # | Claim (atomic) | Type | Load-bearing? | Search question (if fact) |
|---|----------------|------|---------------|---------------------------|
| 1 | ... | verifiable-fact | yes | "What is the average ___?" |
| 2 | ... | professional-judgment | yes | — |
| 3 | ... | experiential-opinion | no | — |

## Queues
- To source (load-bearing verifiable-facts): [#s]
- To label/dispose (judgment/opinion/analysis): [#s]
- Named-party claims (also → Stage 5): [#s]
- Common knowledge (no action): [#s]
```

## Verification
- [ ] Claims are atomic (one assertion each).
- [ ] Every claim has exactly one type.
- [ ] Inference-dressed-as-fact is caught and retyped (not left as verifiable-fact).
- [ ] Load-bearing verifiable-facts are queued for Stage 2.
- [ ] Named-party claims are cross-listed for Stage 5.
