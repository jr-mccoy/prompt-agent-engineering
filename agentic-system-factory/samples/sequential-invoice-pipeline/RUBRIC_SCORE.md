# RUBRIC SCORE — invoice-intake-pipeline

Scored against `authoring/system-patterns/SYSTEM_QUALITY_RUBRIC.md` (100 pts). Both load-bearing gates (security ≥14, Gate B capability+safety) pass.

| Category | Score | Notes |
|----------|-------|-------|
| 1. Agent justification & complexity-appropriateness | 14/15 | Honest Step-0: picked TP-03, the lowest rung above a single model call; rejected both lower (single call) and higher (autonomous agent) rungs because the flow is fixed and the post is code-gated |
| 2. Topology fit & primitive correctness | 14/15 | TP-03 sequential pipeline; fixed code-controlled order; seams S1–S5, loop bounds + cap-fallbacks defined |
| 3. Security gate vs OWASP ASI | 18/20 | Data/control separation + injection defense + deterministic post policy + idempotency + HITL + kill switch; money-write can't be triggered by the model |
| 4. Eval validity + real-tool safety | 18/20 | ABC-valid capability (cited extraction + decision accuracy + post-everything baseline) + separate real-tool safety eval targeting injection/approval-bypass/double-pay |
| 5. Durability / observability / cost | 9/10 | Resumable external state, idempotency key, per-stage isolation, right-sized models, post-control spans/metrics |
| 6. Documentation completeness | 9/10 | 3-layer docs + 6-dim disclosure manifest + staged fail-closed runbook |
| 7. Cross-link hygiene / no-fabrication | 9/10 | References existing `aiagent_*` prompts; no fabricated metrics (unknowns marked) |
| **Total** | **91/100** | **Exemplary.** Both load-bearing gates pass; money-write is code+HITL gated. |

<!-- RUBRIC
cat1_justification: 14
cat2_topology: 14
cat3_security: 18
cat4_eval: 18
cat5_durability: 9
cat6_documentation: 9
cat7_crosslink: 9
-->
