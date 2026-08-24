# BUNDLE MANIFEST — support-ticket-triage

> Worked sample bundle validating the factory on a **single-agent (TP-02)** topology. Passes `validate_bundle.py`, all four gates in `check_gate.py`, and `score_rubric.py` (91/100). Distinctive surface exercised: one agent, a WRITE/messaging tool (`send_reply`), a mandatory HITL approval gate before sending on sensitive categories, and idempotency on send.

**System:** support-ticket-triage · **Bundle version:** 1.0 · **Date:** 2026-06-20 · **Stack committed (Stage 7):** none

---

## 1. Artifacts in this bundle

| # | Artifact | File | Present |
|---|----------|------|---------|
| — | Bundle index | `BUNDLE_MANIFEST.md` | ✅ |
| 1 | System design doc | `ARCHITECTURE.md` | ✅ |
| 2 | Per-agent spec | `agents/triage_agent.md` | ✅ |
| 3 | Tool specs | `tools/crm_order_lookup.md`, `tools/send_reply.md` | ✅ |
| 4 | Gate / policy spec | `GATE_DESIGN.md` | ✅ |
| 5 | Eval harness | `EVAL_HARNESS.md` | ✅ |
| 6 | Observability plan | `OBSERVABILITY.md` | ✅ |
| 7 | Disclosure manifest | `DISCLOSURE_MANIFEST.md` | ✅ |
| 8 | Runbook | `RUNBOOK.md` | ✅ |
| 9 | Rules file | (n/a — no coding-agent build committed) | — |
| — | Rubric score | `RUBRIC_SCORE.md` | ✅ |

## 2. Topology note
TP-02 single agent — deliberately NOT multi-agent. One ticket at a time, no parallel breadth (see `ARCHITECTURE.md §2`, rejected higher rung). The interesting risk is the write tool (`send_reply`) and the sensitive-category branch, not coordination.

## 3. Gate status

| Gate | Pass condition | Status |
|------|----------------|--------|
| 0 Justification | justified | PASS |
| A Security | SAFE-01/02/04 enforced + 3-layer defense + kill switch | PASS |
| B Evaluation | capability **and** safety | PASS |
| C Disclosure | 6 dims + rollback + observability | PASS |
