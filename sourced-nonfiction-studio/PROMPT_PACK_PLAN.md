# PROMPT_PACK_PLAN — the flat-prompt-pack variant

The studio is a full agentic system (live search, fan-out, gates). Some users want the same capability
as a **flat set of standalone prompts** they run by hand — no orchestrator, no live-search dependency,
portable to any environment (including ones where the model can't browse). This document specifies that
variant. It is a **plan**, not a built artifact; build it if/when the portable form is wanted.

## When the pack beats the system
- The environment has **no live search** (the pack produces a *sourcing plan* the human executes).
- The user wants to run one step at a time, manually, with full control.
- Portability matters more than automation (drop the `.md` files anywhere).

## Key difference: plan-only sourcing
Without live fetch, Stage 2 changes from "find real sources" to "**produce a per-claim search
strategy + a citation slot the human fills** after searching themselves." Everything else (typing,
disposition, risk, assembly) is identical. The no-fabrication rule is actually easier to honor: the
pack never emits a citation at all — it emits empty slots the human populates with real sources.

## Proposed pack (7 standalone Tier-1 prompts)

| # | Prompt (proposed path) | Mirrors stage | Notes |
|---|------------------------|---------------|-------|
| 1 | `domain-research-academic/sourcingpack_claim_extraction_typing.md` | 1 | atomic + typed claim ledger |
| 2 | `domain-research-academic/sourcingpack_source_search_plan.md` | 2 | per-claim search strategy + empty citation slots (NO live fetch) |
| 3 | `domain-research-academic/sourcingpack_claim_source_match.md` | 3 | human pastes found sources; prompt rules on support + quality |
| 4 | `domain-professional-writing/writing/writing_unsourced_claim_disposition.md` | 4 | **already built** — reuse as-is |
| 5 | `domain-legal/ip/legal_defamation_publicity_risk_screen.md` | 5a | **already built** — reuse |
| 6 | `domain-research-academic/research_manuscript_fact_check_reconciler.md` | 5b/back-end | **already built** — reuse |
| 7 | `domain-research-academic/sourcingpack_matrix_and_cited_draft_assembler.md` | 6 | matrix + cited manuscript from human-filled slots |

Three of the seven already exist (built with this studio). The pack would add **4 net-new prompts**
(1, 2, 3, 7), each a self-contained Tier-1 prompt runnable without any orchestrator.

## What the pack gives up
- **Automation:** the human runs each prompt and does the actual searching.
- **Gate enforcement:** no `check_citations.py` auto-run, no orchestrator refusing to advance — the
  user must self-enforce "no KEEP without a real source." (Prompt 7 includes a manual citation-shape
  checklist as a stand-in.)
- **Fan-out:** claims are handled one batch at a time, by hand.

## What it keeps
- The full honest-disposition logic (KEEP/SOFTEN/REFRAME/QUOTE/CUT).
- The legal/defamation and fact-check reconciliation prompts (identical).
- The matrix + cited manuscript deliverables.
- The cardinal rule: no fabricated citations (trivially, since the pack emits slots, not sources).

## Build estimate
4 net-new Tier-1 prompts (~150 lines each) + register in `PROMPT_INDEX`. No config, scripts, agents,
or orchestrator needed. ~1–2 hours of authoring. Recommend building only if a concrete portable/offline
use case appears — otherwise the studio + its `data/` degradation note already covers most needs.
