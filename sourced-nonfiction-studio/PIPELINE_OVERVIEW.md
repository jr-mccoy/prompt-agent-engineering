# PIPELINE_OVERVIEW — Sourced Nonfiction Studio

The flow, stage I/O, and gate table. Walk this to run the studio manually.

---

## Flow

```
                       ┌─────────────────────────────────────────────┐
 material ───────────► │ [0] Intake & Scope                          │
 (uncited braindump)   │   → Scope Record (profile, style, names,     │
                       │     jurisdiction, stakes, deliverables)      │
                       └───────────────┬─────────────────────────────┘
                                       ▼
                       ┌─────────────────────────────────────────────┐
                       │ [1] Claim Extraction & Typing                │
                       │   → Claim Ledger (atomic, typed, queued)     │
                       └───────────────┬─────────────────────────────┘
                                       ▼   (load-bearing facts)
                       ┌─────────────────────────────────────────────┐
                       │ [2] Source Discovery  (LIVE, fan-out)        │◄─ workers, one per claim
                       │   → real candidates + passages  |  NO SOURCE │   (untrusted content)
                       └───────────────┬─────────────────────────────┘
                                       ▼
                       ┌─────────────────────────────────────────────┐
                       │ [3] Match & Weight                           │
                       │   → verdicts: SUPPORTED/PARTIAL/CONTESTED/   │
                       │     UNVERIFIED + licensed certainty          │
                       └───────────────┬─────────────────────────────┘
                                       ▼
                       ┌─────────────────────────────────────────────┐
                       │ [4] Disposition                              │
                       │   KEEP / SOFTEN / REFRAME / QUOTE / CUT      │
                       │   (tacit knowledge → labeled judgment)       │
                       └───────────────┬─────────────────────────────┘
                                       ▼
                       ┌─────────────────────────────────────────────┐
                       │ [5] Risk & Integrity   ══ GATE A + GATE B ══ │
                       │   copyright · defamation/publicity ·         │
                       │   plagiarism · no-fabrication                │
                       └───────────────┬─────────────────────────────┘
                              GATE A PASS? ──no──► back to [4] for offending claims
                                       │ yes
                                       ▼
                       ┌─────────────────────────────────────────────┐
                       │ [6] Assembly   ══ GATE C ══                  │
                       │   → matrix + cited manuscript + risk report  │
                       └─────────────────────────────────────────────┘
```

## Stage I/O

| Stage | Prompt | In | Out |
|-------|--------|----|-----|
| 0 | `prompts/stage-0-intake-scope.md` | material | Scope Record |
| 1 | `prompts/stage-1-claim-extraction-typing.md` | material + scope | Claim Ledger + queues |
| 2 | `prompts/stage-2-source-discovery.md` | fact queue | candidate sources / NO SOURCE FOUND |
| 3 | `prompts/stage-3-claim-source-matching.md` | candidates | verdicts + certainty |
| 4 | `prompts/stage-4-claim-disposition.md` | verdicts + ledger | dispositions + rewrites + residue |
| 5 | `prompts/stage-5-legal-risk-integrity.md` | dispositions + draft | risk report + Gate A/B status |
| 6 | `prompts/stage-6-assembly.md` | everything (Gate A PASS) | matrix + manuscript + risk report |

## Gate table

| Gate | Where | Pass condition | On fail |
|------|-------|----------------|---------|
| 0 | ARCHITECTURE §1 | agent justified | n/a (one-time) |
| **A** | Stage 5 | 0 orphan KEEP, 0 fabricated/unresolvable cites, 0 UNVERIFIED-as-fact | return to Stage 4 |
| **B** | Stage 5 | all quotes/named-parties/paraphrase screened & routed | surface blockers to author + counsel |
| **C** | Stage 6 | 3 deliverables + calibrated certainty + disclosure/residue | complete before delivering |

## Command → stage mapping

| Command | Stages |
|---------|--------|
| `/source-my-draft` | 0–6 (full) |
| `/extract-claims` | 1 |
| `/find-sources` | 2–3 |
| `/fact-check-manuscript` | reconciler (finished-draft variant) |
| `/risk-pass` | 5 |

## Cadence
One pass per manuscript (or per chapter/section for long works — reconcile per section, roll up the
matrix). Re-run Stages 2–5 when new claims are added.
