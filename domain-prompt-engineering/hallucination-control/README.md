# hallucination-control/

Per-claim guards against fabrication. Each prompt installs either (a) a system-prompt rule the model must follow, or (b) a post-hoc validator that runs against the model's output. Pair design-time pre-mortem with runtime validators — neither alone is sufficient.

## When to use this subdirectory

Any factual or reasoning task where unsupported claims are bugs. Use alongside `rag-prompts/` when retrieval is the evidence source; use standalone for tool-use and code-execution tasks where the "evidence" is structured output.

## Files

| File | Description |
|------|-------------|
| `hallucination_grounding_only_pattern.md` | System-prompt block restricting claims to evidence container; literal refusal string when asked beyond. |
| `hallucination_calibrated_uncertainty_prompt.md` | Per-claim confidence value tied to evidence type; ECE check on a calibration set. |
| `hallucination_known_unknown_separator.md` | Two physically separate output blocks: known (cited) vs. inferred-or-guessed. |
| `hallucination_citation_required_pattern.md` | Per-claim source-token contract plus deterministic validator that rejects unattributed or invented IDs. |
| `hallucination_invented_entity_audit.md` | Post-hoc scan tagging entities as grounded / paraphrased_match / invented / unverifiable. |
| `hallucination_temporal_anchoring.md` | Preamble + per-claim `(as of date, source)` tags; staleness action by class. |
| `hallucination_self_consistency_check.md` | N-sample run, claim clustering, agreement-rate-based keep/flag/drop. |
| `hallucination_premortem_for_factual_task.md` | Design-time walk of the fabrication-class taxonomy; selects guards within budget. |

## Stack ordering

Typical pipeline (top = earliest):

1. `hallucination_premortem_for_factual_task.md` — picks guards.
2. `hallucination_grounding_only_pattern.md` or `rag_grounding_contract.md` — system-prompt contract.
3. `hallucination_temporal_anchoring.md`, `hallucination_known_unknown_separator.md`, `hallucination_calibrated_uncertainty_prompt.md` — output-shape constraints.
4. `hallucination_citation_required_pattern.md` — runtime validator.
5. `hallucination_invented_entity_audit.md`, `hallucination_self_consistency_check.md` — post-hoc audits / sampling.

## Companion subdirectories

- `rag-prompts/` — retrieval-side contracts and refusals.
- `evaluation/` — correctness eval and pre-mortem prompts at the system level.
