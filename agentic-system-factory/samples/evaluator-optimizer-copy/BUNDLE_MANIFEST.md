# BUNDLE MANIFEST — marketing-copy-evaluator-optimizer

> Worked sample bundle exercising topology TP-07 (evaluator-optimizer) AND the SAFE-04 "na" (not-applicable, tool-free) gate branch. Passes `validate_bundle.py`, all four gates in `check_gate.py`, and `score_rubric.py` (87/100).

**System:** marketing-copy-evaluator-optimizer · **Bundle version:** 1.0 · **Date:** 2026-06-20 · **Stack committed (Stage 7):** none

---

## 1. Artifacts in this bundle

| # | Artifact | File | Present |
|---|----------|------|---------|
| — | Bundle index | `BUNDLE_MANIFEST.md` | ✅ |
| 1 | System design doc | `ARCHITECTURE.md` | ✅ |
| 2 | Per-agent specs | `agents/generator.md`, `agents/critic.md` | ✅ |
| 3 | Tool specs | `tools/no_external_tools.md` (deliberate-absence statement) | ✅ |
| 4 | Gate / policy spec | `GATE_DESIGN.md` | ✅ |
| 5 | Eval harness | `EVAL_HARNESS.md` | ✅ |
| 6 | Observability plan | `OBSERVABILITY.md` | ✅ |
| 7 | Disclosure manifest | `DISCLOSURE_MANIFEST.md` | ✅ |
| 8 | Runbook | `RUNBOOK.md` | ✅ |
| 9 | Rules file | (n/a — no coding-agent build committed) | — |
| — | Rubric score | `RUBRIC_SCORE.md` | ✅ |

## 2. What this sample exercises
- **Topology TP-07 (evaluator-optimizer):** an iterative generate→critique→revise loop with a BOUNDED round count (MAX_ROUNDS) and a cap-fallback (return best-scoring draft + `did_not_converge`); two roles (generator + critic).
- **SAFE-04 na-branch:** because there are no external tools, least-privilege-tools is *not applicable* — the bundle uses `<!-- SAFE-04: na: ... -->` with a real reason, and documents the deliberate tool absence in `tools/no_external_tools.md` as the least-privilege design statement.

## 3. Gate status

| Gate | Pass condition | Status |
|------|----------------|--------|
| 0 Justification | justified (runtime-decided round count) | PASS |
| A Security | SAFE-01/02 enforced + SAFE-04 na + kill switch + defense-in-depth | PASS |
| B Evaluation | capability **and** content-risk safety | PASS |
| C Disclosure | 6 dims + rollback + observability | PASS |
