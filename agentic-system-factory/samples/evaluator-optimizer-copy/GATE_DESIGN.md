# GATE DESIGN — marketing-copy-evaluator-optimizer

**Blast radius:** read-only by construction — no external tools exist. The only risk surface is the *content itself* (unsubstantiated product claims, off-brand/unsafe text) and any untrusted user-supplied source text the copy may draw on.

## Gate 0 — Justification
See `ARCHITECTURE.md §2` (runtime-decided revision-round count; rubric verdict, not a fixed pass count, drives the stop).

## Gate A — Security (OWASP ASI)

| SAFE pattern | Requirement | Status & enforcement point |
|--------------|-------------|----------------------------|
| SAFE-01 data/control separation | Untrusted data never drives control flow | The product brief + brand rules are trusted configuration; any user-supplied source text the copy draws on is wrapped in a `<document>` data block and treated as data only — it can never change the rubric, end the loop, or instruct the generator |
| SAFE-02 deterministic policy | Loop control is a deterministic rule, not free-form | The critic emits a structured per-dimension verdict `{voice, claims, format} ∈ {pass, fail}`; the loop driver continues iff any dimension == fail AND round < MAX_ROUNDS — a fixed code rule, not the model's prose |
| SAFE-04 least-privilege tools | Minimal tool set | Not applicable: there are no external tools to scope. Both agents read only in-context content; see `tools/no_external_tools.md` for the deliberate-absence statement |
| SAFE-05 injection defense | Sanitize external content | Source text is spotlighted; an objective-drift check verifies the draft still serves the brief, not any embedded instruction |
| SAFE-07 circuit breakers | Caps + isolation | MAX_ROUNDS cap; per-round token budget; tripping the cap halts the loop and returns the best draft |
| SAFE-08 governed identity | Attributable actions | Generator and critic run under distinct traced identities per round |
| SAFE-10 inter-agent trust | No peer poisoning | Generator and critic never message each other directly; they communicate only through the loop driver's validated state |

<!-- SAFE-01: enforced -->
<!-- SAFE-02: enforced -->
<!-- SAFE-04: na: no external tools exist — generator/critic operate only on in-context content, so there is no tool privilege to minimize -->
<!-- DEFENSE-IN-DEPTH: 3-layers -->
<!-- KILL-SWITCH: present -->

**Defense-in-depth on the claims path (the real risk surface — 3 layers):**
1. **Generator self-check:** before submitting a draft, the generator verifies each product claim against the brief and removes any it cannot ground.
2. **Independent critic:** the critic re-checks claims-substantiation as a hard rubric dimension and fails the draft if any claim is unsupported by the brief — catching what the generator missed (including injected false claims).
3. **Final claims-substantiation guardrail:** a deterministic pre-ship check refuses to emit copy containing any claim not traceable to the brief, even if both agents passed it.

## HITL approval gates
None at runtime (read-only, no external action). A human consumes and ships the final copy.

## Loop bounds & cap-fallbacks
| Loop | Bound | Cap-fallback |
|------|-------|--------------|
| Generate→critique→revise rounds | MAX_ROUNDS = 4 | return the best-scoring draft seen so far + set flag `did_not_converge: true` |
| Tokens per round | per-round budget | truncate over-budget draft, count the round, continue |

## Kill switch
<!-- KILL-SWITCH: present -->
`config.halt: true` is checked at the top of every round; when set, the loop stops immediately and returns the best-scoring draft gathered so far with a `halted: true` flag. Tested by setting the flag and asserting no further generator/critic invocations occur.

## Gate C — Production-readiness handoff
- [x] Disclosure manifest complete (6 dimensions) — see DISCLOSURE_MANIFEST.md
- [x] Observability/traces present — see OBSERVABILITY.md
- [x] Rollback path — see RUNBOOK.md
- [x] Inter-agent trust model documented (loop driver mediates; no peer channel)
