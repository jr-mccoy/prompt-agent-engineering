# RUNBOOK — marketing-copy-evaluator-optimizer

## Rollout
- Shadow on a sample of briefs; compare final rubric scores + cost vs the current single-shot-plus-manual-edit baseline before ramping.
- Canary one brand/cohort; watch the `did_not_converge` rate, the claims-guardrail block count, and tokens/run.

## Rollback
<!-- ROLLBACK: present -->
Rollback = disable the loop via `config.halt: true` (kill switch) and fall back to single-shot generation with a manual editor pass. The system is read-only by construction with no external side effects, so rollback is a routing change only; an in-flight run simply returns its best-scoring draft so far with a `halted: true` flag.

## Failure-mode catalog (seed)
| Failure | Mitigation | Detected by |
|---------|-----------|-------------|
| Unsubstantiated claim slips through | 3-layer claims defense (generator self-check + critic dimension + final guardrail) | claims-guardrail block count > 0 |
| Injected false claim in source text | spotlighting + objective-drift check; critic claims dimension | injected-claim survival check in safety eval |
| Loop never converges on a hard brief | MAX_ROUNDS cap-fallback returns best draft + `did_not_converge` flag | `did_not_converge` rate alert |
| Critic too lenient / too strict (rubric drift) | pinned rubric + LLM-judge calibration on a pilot set | convergence-rate or round-1-vs-final-delta drift |
| Cost runaway | MAX_ROUNDS + per-round token budget | tokens/run alert |
