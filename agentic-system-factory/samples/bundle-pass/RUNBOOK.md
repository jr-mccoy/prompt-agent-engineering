# RUNBOOK — deep-research-fleet

## Rollout
- Shadow on 10% of questions; compare coverage + cost vs the single-agent baseline before ramping.
- Canary one region/cohort; watch the allowlist-deny rate and tokens/run.

## Rollback
<!-- ROLLBACK: present -->
Rollback = disable the fleet via `config.halt: true` (kill switch) and fall back to single-agent search. No state-modifying actions exist, so rollback is a routing change only; in-flight runs return partial gathered results.

## Failure-mode catalog (seed)
| Failure | Mitigation | Detected by |
|---------|-----------|-------------|
| Injection in a page | deterministic allowlist + spotlighting | allowlist-deny spike; injected-link check |
| Coverage too low | decomposition-round cap-fallback + flag | coverage metric below floor |
| Cost runaway | MAX_WORKERS / MAX_FETCHES / token budget | tokens/run alert |
| Worker stall | per-worker timeout + proceed with completed set | missing worker span |
