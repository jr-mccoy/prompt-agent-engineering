# Observability — Children's Book Studio (design bundle)

Because the system is prompt-orchestration with a human at every gate, observability is *trace-by-artifact*: each stage leaves a legible record the author (and orchestrator) can inspect. There is no telemetry backend; the "logs" are the stage outputs and the gate verdicts.

## What each stage records

| Stage | Recorded signal | Where it lives |
|-------|-----------------|----------------|
| 0 Setup | project spec + convention contract + form-conditioned route + Gate 0 verdict | the Stage 0 output block |
| 1 Concept | agency moment, theme statement, NF source plan | the Stage 1 output block |
| 2 Structure | beat map, projected length vs. band, agency-beat location | the Stage 2 output block |
| 3 Draft | actual word count vs. band, open `VERIFY` count | the draft header |
| 4 Revision | per-pass diagnosis, routed tools, fix queue, Gate A verdict (per item) | each revision pass block; manuscript versions `manuscript-v[N].md` |
| 5 Polish | VERIFY ledger (claim → resolution), artifacts produced, Gate B verdict (per item) | the Stage 5 output block |
| 6 Package | Gate C verdict (per item), deliverable manifest | the Stage 6 output block |

## Key traces

- **Gate verdicts** — every gate emits PASS/FAIL per checklist item. A FAIL names the failing item and the stage to return to. This is the primary trace.
- **Revision trajectory** — the sequence of `manuscript-v[N].md` versions plus per-pass change logs shows how the draft converged (and lets the author revert — the rollback path).
- **VERIFY ledger** — the running list of nonfiction claims and their resolution (sourced | cut) is the audit trail for Gate B.
- **Bracket ledger** — every `[AUTHOR TO VERIFY]` in the submission package is an open item the author must close before sending.

## Alerts (author-facing)

- Word count drifts out of band at Stage 3 → flagged in the draft header.
- Any open `VERIFY` at Stage 5 → Gate B blocks; surfaced in the VERIFY ledger.
- Any certification language in the audit → Gate B blocks; surfaced explicitly.
- Any un-bracketed market fact at Stage 6 → Gate C blocks.
