# BUNDLE MANIFEST — deep-research-fleet (INTENTIONALLY INCOMPLETE SAMPLE)

> Worked sample bundle (the gold-standard `deep-research-fleet` use case). Passes `validate_bundle.py`, all four gates in `check_gate.py`, and `score_rubric.py` (93/100). Used by every script's `--self-check`.

**System:** deep-research-fleet · **Bundle version:** 1.0 · **Date:** 2026-06-20 · **Stack committed (Stage 7):** none

---

## 1. Artifacts in this bundle

| # | Artifact | File | Present |
|---|----------|------|---------|
| — | Bundle index | `BUNDLE_MANIFEST.md` | ✅ |
| 1 | System design doc | `ARCHITECTURE.md` | ✅ |
| 2 | Per-agent specs | `agents/orchestrator.md`, `agents/worker.md`, `agents/synthesizer.md` | ✅ |
| 3 | Tool specs | `tools/research_sources_search.md`, `tools/research_page_fetch.md` | ✅ |
| 4 | Gate / policy spec | `GATE_DESIGN.md` | ✅ |
| 5 | Eval harness | `EVAL_HARNESS.md` | ✅ |
| 6 | Observability plan | `OBSERVABILITY.md` | ✅ |
| 7 | Disclosure manifest | `DISCLOSURE_MANIFEST.md` | ✅ |
| 8 | Runbook | `RUNBOOK.md` | ✅ |
| 9 | Rules file | (n/a — no coding-agent build committed) | — |
| — | Rubric score | `RUBRIC_SCORE.md` | ✅ |

## 3. Gate status

| Gate | Pass condition | Status |
|------|----------------|--------|
| 0 Justification | justified | PASS |
| A Security | SAFE-01/02 enforced + kill switch | PASS |
| B Evaluation | capability **and** safety | FAIL (safety eval missing) |
| C Disclosure | 6 dims + rollback + observability | PASS |
