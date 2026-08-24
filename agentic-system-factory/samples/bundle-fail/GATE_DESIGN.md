# GATE DESIGN — deep-research-fleet

**Blast radius:** read-only web access, but untrusted content.

## Gate 0 — Justification
See `ARCHITECTURE.md §2` (input-dependent runtime decomposition).

## Gate A — Security (OWASP ASI)

| SAFE pattern | Requirement | Status & enforcement point |
|--------------|-------------|----------------------------|
| SAFE-01 data/control separation | Untrusted data never drives control flow | Fetched page text passed as a `<document>` data block; tool selection driven only by the trusted question + run-state, never page text |
| SAFE-02 deterministic policy | Tool allowlist + schema validation | Allowlist = {search, fetch}; https-only scheme; arg schema validated pre-call; no other tool can be invoked even if the model emits one |
| SAFE-04 least-privilege tools | Minimal tool set | Workers have read-only fetch; no write/exec tools exist in the system |
| SAFE-05 injection defense | Sanitize external content | Input spotlighting on fetched content; objective-drift check |
| SAFE-07 circuit breakers | Caps + isolation | MAX_WORKERS, MAX_FETCHES, token budget; tripping any cap halts spawning |
| SAFE-08 governed identity | Attributable actions | Each worker runs under a distinct traced identity |
| SAFE-10 inter-agent trust | No peer poisoning | Star topology only; workers can't message each other |

<!-- SAFE-01: enforced -->
<!-- SAFE-02: enforced -->
<!-- SAFE-04: enforced -->
<!-- DEFENSE-IN-DEPTH: 3-layers -->

**Defense-in-depth on the web-content path:** input spotlighting + instruction-hierarchy prompts + deterministic tool allowlist (the hard limit — even a hijacked worker can only search/fetch).

## HITL approval gates
None at runtime (read-only). A human consumes the output.

## Loop bounds & cap-fallbacks
| Loop | Bound | Cap-fallback |
|------|-------|--------------|
| Decomposition rounds | 3 | synthesize from what's gathered + flag "coverage capped" |
| Workers spawned | MAX_WORKERS=8 | proceed with 8; note un-explored subtopics |
| Fetches/worker | MAX_FETCHES=10 | summarize from fetched set |

## Kill switch
<!-- KILL-SWITCH: present -->
`config.halt: true` is checked before any search/fetch; when set, the system stops spawning/fetching and returns whatever is gathered. Tested by setting the flag and asserting no tool calls occur.

## Gate C — Production-readiness handoff
- [x] Disclosure manifest complete (6 dimensions) — see DISCLOSURE_MANIFEST.md
- [x] Observability/traces present — see OBSERVABILITY.md
- [x] Rollback path — see RUNBOOK.md
- [x] Inter-agent trust model documented (star topology)
