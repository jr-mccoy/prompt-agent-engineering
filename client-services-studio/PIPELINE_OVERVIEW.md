# Pipeline Overview

*Not legal, tax, or accounting advice.*

Ten stages, four gates. Each stage names its input, its output, and whether a gate
stands in front of it.

```
 Stage 0  Practice config          config/practice.json
    │
 Stage 1  Qualify            ── Gate 0 ──►  decline / probe / book discovery
    │
 Stage 2  Discovery call                    discovery record
    │
 Stage 3  Scope & estimate                  scope block  (no price yet)
    │
 Stage 4  Price & package    ── Gate A ──►  commercial block
    │
 Stage 5  Proposal & SOW                    proposal, SOW input
    │
 Stage 6  Contract risk      ── Gate B ──►  negotiating position, counsel questions
    │
 Stage 7  Deliver & report       (drift)    change orders, status reports
    │
 Stage 8  Invoice & collect      (ladder)   invoice schedule, collection actions
    │
 Stage 9  Close out          ── Gate C ──►  realised margin, case study, asks
    │
    └────► feeds Stage 0: rate floor, disqualifiers, fixed-price eligibility
```

## Stage table

| Stage | Prompt | Gate | Output |
|---|---|---|---|
| 0 | [`stage-0-practice-config.md`](prompts/stage-0-practice-config.md) | — | `config/practice.json` |
| 1 | [`stage-1-qualify-lead.md`](prompts/stage-1-qualify-lead.md) | **Gate 0** | decline, probe, or booking |
| 2 | [`stage-2-discovery-call.md`](prompts/stage-2-discovery-call.md) | — | discovery record |
| 3 | [`stage-3-scope-and-estimate.md`](prompts/stage-3-scope-and-estimate.md) | — | `scope` block |
| 4 | [`stage-4-price-and-package.md`](prompts/stage-4-price-and-package.md) | **Gate A** | `commercial` block |
| 5 | [`stage-5-proposal-and-sow.md`](prompts/stage-5-proposal-and-sow.md) | — | proposal, SOW input |
| 6 | [`stage-6-contract-risk-review.md`](prompts/stage-6-contract-risk-review.md) | **Gate B** | position, counsel questions |
| 7 | [`stage-7-deliver-scope-control-and-status.md`](prompts/stage-7-deliver-scope-control-and-status.md) | drift | change orders, status |
| 8 | [`stage-8-invoice-and-collections.md`](prompts/stage-8-invoice-and-collections.md) | ladder | schedule, collections |
| 9 | [`stage-9-closeout-case-study-and-referral.md`](prompts/stage-9-closeout-case-study-and-referral.md) | **Gate C** | margin, case study, asks |

## What each gate checks

### Gate 0 — qualify (Stage 1)

Five structural checks plus the practice's declared disqualifiers.

| Check | Blocks when |
|---|---|
| `decision_maker` | No name given |
| `budget_authority` | Not confirmed |
| `outcome_defined` | Outcome is an activity, not a changed state |
| `rate_floor` | A *stated* budget implies a rate below walk-away. Unknown budget is a discovery question, not a failure |
| `concentration` | Current + added share exceeds the limit |
| declared disqualifiers | Any `decline`-tier signal observed. `probe` and `proceed_with_protection` warn |

### Gate A — priceable scope (Stage 4)

`scope.deliverables`, `scope.assumptions`, `scope.exclusions` and
`scope.client_inputs` must all be non-empty. Every deliverable needs `name`, `format`
and `acceptance`. Every client input needs `owner`, `due` and `if_late`. A
decision-maker must be named.

### Gate B — signature risk (Stage 6)

Ten flags at three severities over a contract summary you extracted. Critical and
high block unless accepted with a **recorded rationale**; medium warns. Missing
counsel review is itself a high finding. Full list:
[`skills/proposal-assembler/references/red-flags.md`](skills/proposal-assembler/references/red-flags.md).

### Gate C — close-out (Stage 9)

Blocks while an invoice is outstanding and not written off, while unbilled effort or
the original estimate is unrecorded, or while case-study consent and the
repeat/decline verdict are missing.

## The two continuous mechanisms

**Drift detection (Stage 7)** runs at every delivery checkpoint, not at the end. High
severity means delivered work is on the exclusion list; medium means it is not an
agreed deliverable, or effort has exceeded agreed by more than 15%.

**The escalation ladder (Stage 8)** enforces in code what intention fails to enforce:
a dispute is never escalated, an undiagnosed invoice goes back to triage, a rung
fires only on its trigger, a rung is never repeated, suspension is not proposed
without a contractual right and ongoing work, and distress halves every trigger.

## The feedback loop

Stage 9 is not the end. Three things flow back:

| From close-out | To |
|---|---|
| Typical overrun | The rate floor's risk loading (Stage 0) |
| Estimate-error series and its CV | Fixed-price eligibility (Stage 4) |
| Client verdict | The disqualifier list (Stage 0, Gate 0) |

A practice that runs Stage 9 on every engagement gets better at quoting. One that
runs it only after bad engagements learns only about bad engagements.

## Live status

All ten stages, four gates, four skills, four commands and three agents are built.
`DRY_RUN.md` proves each gate on the `samples/` fixtures, including the negatives.
37 tests pass. No stage is stubbed.
