# BUNDLE MANIFEST — invoice-intake-pipeline

> Worked sample bundle: a SEQUENTIAL-PIPELINE topology (TP-03) with a money/write blast radius. Demonstrates the factory on a fixed code-orchestrated flow whose stages are model-powered, where the money-moving post is gated by deterministic code + a mandatory human approval. Passes `validate_bundle.py`, all four gates in `check_gate.py`, and `score_rubric.py` (91/100).

**System:** invoice-intake-pipeline · **Bundle version:** 1.0 · **Date:** 2026-06-20 · **Stack committed (Stage 7):** none

---

## 1. Artifacts in this bundle

| # | Artifact | File | Present |
|---|----------|------|---------|
| — | Bundle index | `BUNDLE_MANIFEST.md` | ✅ |
| 1 | System design doc | `ARCHITECTURE.md` | ✅ |
| 2 | Per-stage agent specs | `agents/extractor.md`, `agents/validator.md`, `agents/poster.md` | ✅ |
| 3 | Tool specs | `tools/po_lookup.md`, `tools/accounting_post.md` | ✅ |
| 4 | Gate / policy spec | `GATE_DESIGN.md` | ✅ |
| 5 | Eval harness | `EVAL_HARNESS.md` | ✅ |
| 6 | Observability plan | `OBSERVABILITY.md` | ✅ |
| 7 | Disclosure manifest | `DISCLOSURE_MANIFEST.md` | ✅ |
| 8 | Runbook | `RUNBOOK.md` | ✅ |
| 9 | Rules file | (n/a — no coding-agent build committed) | — |
| — | Rubric score | `RUBRIC_SCORE.md` | ✅ |

## 2. Topology at a glance
TP-03 sequential pipeline: `extract → validate → [HITL gate] → post`. Stage order is fixed and owned by deterministic code. Models power extraction and discrepancy reasoning; the post is performed by code only after policy + a human approval token + an idempotency key.

## 3. Gate status

| Gate | Pass condition | Status |
|------|----------------|--------|
| 0 Justification | justified (lowest rung; fixed flow; code+HITL-gated post) | PASS |
| A Security | SAFE-01/02/04 enforced + 3-layer defense + kill switch | PASS |
| B Evaluation | capability **and** real-tool safety (injection / approval-bypass / double-pay) | PASS |
| C Disclosure | 6 dims + rollback + observability | PASS |
