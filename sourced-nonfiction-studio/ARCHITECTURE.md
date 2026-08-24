# ARCHITECTURE — Sourced Nonfiction Studio

Why this system is built the way it is: the Gate-0 justification, blast-radius analysis, topology
choice, gate-enforcement model, and the reuse discipline.

---

## 1. Gate 0 — Why an agent (not a prompt or a fixed workflow)

Walking the repo's complexity ladder (`authoring/system-patterns/`, Step 0):

1. Deterministic function? No — the work is judgment-heavy over natural language.
2. Single model call? No — one call can't do extract → live-search → verify → dispose → screen → assemble.
3. Fixed code-controlled workflow? Close, but insufficient — the **number of claims is unknown**, the
   **number and shape of searches per claim is data-dependent**, and claims **loop** (a claim found
   UNVERIFIED routes back through disposition; a source found non-supporting triggers another search).
4. **Model must decide the next step at runtime → an agent is justified.**

> **An agent is required because** the pipeline must decide, per claim at runtime, how many sources
> to seek, whether a fetched source actually supports the claim, and which disposition path each claim
> takes — **and a deterministic workflow cannot** because the claim count, search depth, and
> per-claim branching are all input-dependent and discovered only while running.

The fan-out per claim + data-dependent branching is the classic **orchestrator-workers (TP-06)**
topology — the same as the repo's gold-standard research-fleet example.

## 2. Blast radius → gate-enforcement model

**Worst thing this system can do:** publish a **fabricated citation**, an **unsupported factual claim
dressed as established fact**, plagiarized prose, or an **unsupported defamatory statement about a
real person**. The blast radius is *content integrity and legal exposure* — reputational and legal
harm to the author, not money movement or data loss.

That blast radius dictates **critique-enforced gates, not code-enforced gates** — the same reasoning
`childrens-book-studio` documents. The load-bearing gate criteria ("does this source *actually
support* the claim," "is this harmful factual assertion about a named person supported," "is this
genuinely re-expressed or synonym-swapped") are **semantic judgments a lexical script can only
approximate.** So enforcement lives in the orchestrator's critique against each stage's Verification
checklist, and integrity gates are non-negotiable (no override).

**The one mechanical exception:** citation *shape* is lexically checkable, so `scripts/check_citations.py`
provides a cheap Gate-A floor — it catches orphan KEEP claims and unresolvable `[S#]` tokens before
the (more expensive) semantic critique runs. It verifies **shape, not truth**: a passing matrix can
still fail the semantic check if a real-looking source doesn't actually support its claim. Two-layer
model: mechanical floor + semantic ceiling.

*(If this system ever grew a real-money or irreversible-action surface, it would need code-not-trust
gates like `ai-investment-research-toolkit`. It does not, by design — it produces documents.)*

## 3. Topology & primitives

- **TP-06 Orchestrator-Workers.** `sourcing-orchestrator` drives; `source-discovery-worker` fans out
  (one per claim/cluster) for Stage 2; `claim-verifier` handles hard support calls in Stage 3;
  `risk-reviewer` runs Stage 5.
- **Why workers are isolated:** each source-discovery worker sees only its claim(s) — this bounds
  context and, critically, **contains prompt-injection blast radius** from untrusted fetched pages
  (a poisoned page can't reach the whole pipeline through one worker).

## 4. Security (SAFE-01/02 — untrusted content)

Fetched web pages are **untrusted data**. Workers are instructed to treat page content as information
about a possibly-manipulative source, never as commands — the studio's explicit data/control
separation. A page saying "cite this site" or "ignore previous instructions" is reported neutrally,
never obeyed. This is the primary security surface (the system takes no destructive actions, so the
threat model is manipulation-of-output, not manipulation-of-action).

## 5. Gates (0/A/B/C)

| Gate | Enforces | How |
|------|----------|-----|
| **0** Justify | agent is warranted | this document (§1) |
| **A** Sourcing integrity | no fabricated/orphan/unverified-as-fact citations | `check_citations.py` (floor) + orchestrator critique (ceiling); **blocks Stage 6** |
| **B** Legal safety | fair-use, defamation/publicity, plagiarism screened & routed | `risk-reviewer` + Stage 5 prompts; flags to counsel, never "clears" |
| **C** Publish-readiness | 3 deliverables, calibrated certainty, disclosure + residue | Stage 6 verification |

Integrity gates (A) cannot be overridden. Legal flags (B) are routed to a human, not decided by the
system. Style/voice preferences are adjustable with the author.

## 6. Reuse discipline (reference, don't rebuild)

The pipeline is ~70% assembly of existing repo prompts (see `referenced-prompts/README.md`). Only the
7 stage prompts, the orchestrator, 4 agents, config, and the gate script are net-new to the bundle,
plus **3 net-new reusable Tier-1 prompts** given proper domain homes (indexed, not bundle-local):
- `domain-professional-writing/writing/writing_unsourced_claim_disposition.md`
- `domain-research-academic/research_manuscript_fact_check_reconciler.md`
- `domain-legal/ip/legal_defamation_publicity_risk_screen.md`

## 7. Key decisions
- **D1 — Live-fetch, not plan-only.** Real citations are the product; a plan-only variant is documented
  in `PROMPT_PACK_PLAN.md` for offline/portable use.
- **D2 — Reframe, don't delete.** Unsourceable expertise is valuable; the honest move is to label it as
  the author's judgment, not to strip it. `writing_unsourced_claim_disposition` is the heart of this.
- **D3 — Field-pluggable.** `source-standards-profiles.yaml` adapts the credibility bar per field
  rather than hard-coding one.
- **D4 — Not legal advice.** The legal pass flags and routes; it never clears. Jurisdiction is a
  required input, US-common-law default.
