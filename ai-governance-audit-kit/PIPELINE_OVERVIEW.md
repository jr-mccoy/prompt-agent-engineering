# Pipeline Overview

Eight stages, four gates. Each stage names what it produces and what stops it.

| # | Stage | Prompt | Gate | Produces |
|---|---|---|---|---|
| 0 | Engagement config | `prompts/stage-0-engagement-config.md` | — | `config/audit.json` + a scope note |
| 1 | Inventory | `prompts/stage-1-inventory-the-corpus.md` | **Gate 0** | `audit/inventory.json` |
| 2 | Duplication clusters | `prompts/stage-2-duplication-clusters.md` | — | `audit/clusters.json` |
| 3 | Observed scoring | `prompts/stage-3-observed-scoring.md` | **Gate A** | one score record per artifact |
| 4 | Governance findings | `prompts/stage-4-governance-findings.md` | — | `audit/findings.md` |
| 5 | Report | `prompts/stage-5-report-and-claim-safety.md` | **Gate B** | the report |
| 6 | Registry handback | `prompts/stage-6-registry-handback.md` | **Gate C** | `<corpus>/meta/registry/` |
| 7 | Close-out | `prompts/stage-7-closeout-and-remediation-plan.md` | — | `audit/remediation.md` |

## The gates, in one line each

- **Gate 0 — inventoriable.** A corpus with no discoverable artifacts, or a
  config that matches nothing, cannot be audited. It blocks rather than
  reporting an empty clean bill of health.
- **Gate A — scoreable.** A score with no named rubric version and no stated
  observed-versus-self-reported provenance is not a finding.
- **Gate B — claim-safe.** The report may not contain a directional claim
  without a number requiring it, an ROI figure, an asserted tier, an unstamped
  fixture number, or quantities with no limitations.
- **Gate C — handback complete.** Not complete until the Engine opens the tree
  and `validate_registry` returns clean with checksums verified.

## Commands

| Command | Stage |
|---|---|
| `/inventory` | 1 |
| `/cluster` | 2 |
| `/score-observed` | 3 |
| `/handback` | 6 |

Stages 0, 4, 5 and 7 are deliberately conversational: they are where the
engagement happens, and a command would suggest otherwise.

## Agents

| Agent | Owns |
|---|---|
| `audit-orchestrator` | the sequence, and refusing to advance past a block |
| `duplication-analyst` | the candidate list, and the three ways it misleads |
| `claim-safety-reviewer` | everything that will be written down |

## What flows between stages

Stage 1 writes `audit/inventory.json` and every later stage reads it. Nothing
re-walks the tree. A membership correction therefore propagates through the
whole pipeline; a correction made anywhere else does not, which is why Stage 1
is the one to get right before moving on.
