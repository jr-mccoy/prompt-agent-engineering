# OBSERVABILITY PLAN — marketing-copy-evaluator-optimizer

- **Spans:** one generator span and one critic span per round, plus a whole-loop trajectory span (round count, terminal reason: passed / capped / halted).
- **Event schema:** `{run_id, round, role, draft_hash, verdict:{voice,claims,format}, unmapped_claims:int, tokens, latency_ms}` per round.
- **Key metrics:** rounds-to-pass (process), round-1-vs-final rubric delta (outcome quality), unsubstantiated-claims-shipped (safety — must be zero), `did_not_converge` rate, tokens/run (cost).
- **Dashboards:** per-run round trajectory with per-dimension verdicts; rolling convergence rate; round-1-vs-final score distribution; claims-guardrail block count.
- **Alerts:** any unsubstantiated claim reaching the final guardrail (should be zero — investigate the critic); convergence rate dropping below floor; `did_not_converge` rate spiking (brief or rubric drift); tokens/run above budget.
- **Trace retention:** full per-round trajectory (every draft hash + verdict) for adversarial review; each draft attributable to a generator/critic identity.
