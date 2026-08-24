# EVAL HARNESS — deep-research-fleet (INTENTIONALLY INCOMPLETE SAMPLE)

> This sample deliberately ships a capability suite but **no real-tool safety eval**, to prove that `check_gate.py --gate B` and `score_rubric.py` FAIL when safety is skipped. Capability ≠ safety.

## Gate B-capability — ABC-valid acceptance suite

<!-- GATE-B-CAPABILITY: present -->

- Task validity: 20 held-out research questions; agent isolated from the answer key; oracle answers; versions pinned.
- Outcome validity: citation-coverage + source-reality graders; LLM-judge validated on a pilot.
- Reporting: trivial-agent baseline scores ~0; dual process+outcome metrics; cost reported.

## Gate B-safety — real-tool safety eval (OpenAgentSafety)

**NOT YET DESIGNED.** No real-tool safety suite exists for this bundle. The `GATE-B-SAFETY` marker is intentionally absent, so Gate B fails and the rubric tier is capped at "Needs work" regardless of total — exactly the failure mode the factory is meant to catch.

## Sign-off
- Capability gate: PASS.
- Safety gate: MISSING → Gate B FAIL → not production-ready.
