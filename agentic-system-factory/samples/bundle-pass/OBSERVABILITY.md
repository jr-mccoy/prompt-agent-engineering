# OBSERVABILITY PLAN — deep-research-fleet

- **Spans:** one per agent (orchestrator, each worker, synthesizer) + a whole-run trajectory span.
- **Event schema:** `{run_id, agent_id, tool, args_hash, url, allowed:bool, tokens, latency_ms}` per tool call.
- **Key metrics:** citation-coverage (outcome), sources-fetched & subtopics-covered (process), tokens/run (cost), allowlist-deny count (safety signal).
- **Dashboards:** per-run coverage + cost; rolling allowlist-deny rate; worker fan-out distribution.
- **Alerts:** allowlist-deny spike (possible injection campaign); coverage below floor; tokens/run above budget; any non-allowlisted action attempt (should be zero).
- **Trace retention:** full trajectory for adversarial review; every fetch attributable to a worker identity.
