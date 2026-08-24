# VALIDATION — Phase 5 (run the factory on diverse use cases)

**Date:** 2026-06-20 · **Scope:** validate the factory across the topology spectrum it targets, harden the gate scripts from what the runs surface, and leave tracked regression fixtures.

This is the factory's final validation phase. The goal is not a demo — it is to prove the gates **bite the same way across very different systems**, and to convert each run into a permanent fixture the `scripts/` enforce forever.

---

## 1. Coverage matrix

Each row is a worked design bundle under `samples/`, scored by the three stdlib gate scripts (`validate_bundle.py`, `check_gate.py`, `score_rubric.py`). "Gates" = Gate 0 (justification) / A (OWASP-ASI security) / B (capability **and** real-tool safety) / C (disclosure + rollback + observability).

| Topology | Use case | Bundle dir | Blast radius exercised | validate | Gates 0/A/B/C | Rubric |
|----------|----------|------------|------------------------|----------|---------------|--------|
| **TP-02** single agent | support-ticket-triage | `samples/single-agent-triage/` | **messaging/write** (send-reply) + HITL + idempotency; cross-customer privacy | PASS | PASS / PASS / PASS / PASS | 91 — Exemplary |
| **TP-03** sequential pipeline | invoice-intake-pipeline | `samples/sequential-invoice-pipeline/` | **money/write** (post to accounting) + HITL approval threshold + idempotency + dry-run | PASS | PASS / PASS / PASS / PASS | 91 — Exemplary |
| **TP-06** orchestrator-workers | deep-research-fleet | `samples/bundle-pass/` | read-only web + untrusted content (injection) | PASS | PASS / PASS / PASS / PASS | 93 — Exemplary |
| **TP-07** evaluator-optimizer | marketing-copy-evaluator-optimizer | `samples/evaluator-optimizer-copy/` | **tool-free** (in-context only) + claims-substantiation safety | PASS | PASS / PASS / PASS / PASS | 87 — Production-ready |
| *(negative)* incomplete eval | (deep-research, safety eval omitted) | `samples/bundle-fail/` | — | PASS (structurally complete) | **FAIL at Gate B** (by design) | 84 — Needs work (load-bearing gate failed) |

Reproduce any row:
```bash
cd agentic-system-factory
python3 scripts/validate_bundle.py samples/<dir>
python3 scripts/check_gate.py     samples/<dir>
python3 scripts/score_rubric.py   samples/<dir>
```
Run the whole suite as a regression gate:
```bash
for s in validate_bundle check_gate score_rubric; do python3 scripts/$s.py --self-check; done
# each prints SELF-CHECK PASS
```

## 2. The WORKFLOW-STOP terminal (Gate 0 negative path)

The complexity-ladder gate can also **stop the factory** — the correct outcome when a use case does not earn an agent. When Gate 0 resolves to `WORKFLOW-STOP` (e.g., "email me a nightly CSV report" — deterministic, no content-dependent branching), the factory emits a **workflow recommendation and halts before Stage 1**; it does not produce agents/tools, so there is no full bundle to score. `check_gate.py gate_0` accepts the `WORKFLOW-STOP` marker so a stop is recorded as a pass-through, not a failure. This is the design working as intended: the default is *down the ladder*.

Originally validated only as a decision path; **since the 2026-07-02 hardening pass it is a tracked fixture** — `samples/workflow-stop/` carries the marker and `check_gate.py --self-check` pins Gate 0 = PASS on it permanently.

## 3. What the runs surfaced → refinements applied

Phase 5 is supposed to "refine patterns/rubric from what breaks." Findings and the fixes made:

1. **Fixture coverage was too narrow (2 → 5).** The scripts' `--self-check` previously pinned only `bundle-pass`/`bundle-fail` — both the *same* topology (orchestrator-workers) and the *same* blast radius (read-only web). Added three structurally-complete passing fixtures spanning **four distinct topologies** and wired them into all three scripts' `self_check()` so they are enforced permanently.
2. **The SAFE-04 `na` (tool-free least-privilege) branch was never exercised.** `check_gate.gate_a` supports `SAFE-04: na: <reason>` for systems with no external tools, but no fixture covered it. The evaluator-optimizer bundle is deliberately tool-free and uses the `na` marker, so the parser's `na`-branch is now under test.
3. **Write/irreversible blast radius was untested.** The original fixtures were read-only. The new triage (messaging) and invoice (money) bundles exercise the **HITL-approval + idempotency + dry-run** gate-design path that read-only systems never touch — the highest-stakes part of Gate A/C.
4. **No script/rubric defects required code changes.** The gates bit exactly as designed on every bundle: the negative fixture still trips Gate B (capability ≠ safety), and `score_rubric` still caps the tier on a load-bearing failure regardless of total. The only hardening needed was broader fixtures, not logic fixes.

## 4. Conclusion

The factory was validated across the topology spectrum its pattern index targets (single-agent, sequential, orchestrator-workers, evaluator-optimizer), across read-only / messaging / money / tool-free blast radii, plus the negative-path and workflow-stop terminals. All gates enforce as code-not-trust and are now protected by a 7-fixture regression suite (5 Phase-5 bundles + the two §5 fixtures below). **The system is ready for testing/use.**

### Follow-on (optional, not blocking)
- Add a **group-chat / Magentic** fixture (manager-coordinated dynamic subagents) — currently covered by proxy via TP-06 + the Microsoft Agent Framework Magentic mapping in `stacks/microsoft-agent-framework.md`.
- As real users run the factory, fold any new failure they hit into `samples/` as a fixture (the pattern this phase established).

## 5. Hardening pass — 2026-07-02 (adversarial script audit)

Phase 5's item 4 ("no script defects required code changes") did not survive an adversarial audit of the scripts themselves. The audit attacked the *marker contract*, not the bundles, and found the gates could be gamed; all findings are fixed and pinned as regressions:

1. **Template-copy gaming (critical).** The templates ship the passing marker values verbatim in fenced example blocks, and the old `_marker()` searched raw text — so a bundle made of verbatim, unfilled template copies passed Gates A, B, C and self-attested 100/100. **Fix:** the scripts now strip fenced code blocks and inline code spans before marker search; only live markers count. **Regression:** `samples/templates-verbatim/` (unfilled template copies) is pinned in `--self-check` as failing every gate.
2. **First-marker-wins masking.** A stale `<!-- SAFE-01: enforced -->` example above a real `<!-- SAFE-01: na -->` passed Gate A. **Fix:** two same-name markers with different values now fail closed with a `<<conflicting duplicate markers>>` verdict (identical duplicates remain fine).
3. **SAFE-04 `na` accepted garbage.** `SAFE-04: nachos` passed (`startswith("na")`). **Fix:** the `na` branch now requires the exact `na: <reason>` shape with a non-empty reason.
4. **`>` in a marker value broke parsing** and reported the marker as *missing*. **Fix:** the marker regex now permits `>` inside values (e.g., `na: privilege > read is never granted`).
5. **RUBRIC block shadowing.** An innocuous `<!-- RUBRIC block is below -->` prose comment made `score_rubric.py` parse the wrong "block" with misleading errors. **Fix:** the parser now takes the first RUBRIC comment that actually contains `catN_*` lines.
6. **No argparse.** `--help` was treated as a bundle path; unknown flags failed opaquely; exit codes disagreed with docstrings. **Fix:** all three scripts use argparse (loud unknown-flag errors, `--help`, consistent 0/1/2 exit codes).
7. **The `WORKFLOW-STOP` branch had zero regression coverage.** **Fix:** `samples/workflow-stop/` added and pinned (see §2).

Honesty boundary made explicit (in the script docstrings, the stage prompts' new False-Positive Prevention blocks, and `ARCHITECTURE.md` §4): the scripts verify marker **presence and shape, not truth**. A marker with no enforcement point / eval suite behind it — *marker-stuffing* — passes the script and must be caught by the orchestrator's critique loop.
