# Sourced Nonfiction Studio

Turn a domain expert's **uncited knowledge** — the stuff learned over years in the field, with no
sources — into a **sourced, legally-screened, publishable nonfiction product**: a fact→source
matrix (audit trail) plus a publish-ready manuscript with real citations, plus a risk report.

> **Cardinal rule:** a citation is real or it does not exist. This studio never invents, guesses,
> or "recalls" a source. Claims that can't be backed by a real source found via live search are
> **softened, reframed as the author's labeled judgment, or cut** — never asserted as established fact.

This is a self-contained toolkit at the repo root. It **orchestrates existing repo prompts**
(research, epistemic, legal, writing) rather than rebuilding them — see `referenced-prompts/`.

---

## What it does (and won't)

**Does:**
- Separates *verifiable facts* from *professional judgment* from *folklore* in your material.
- Runs **live** web/PubMed/Consensus searches to find real, credible sources per factual claim.
- Maps every claim to a reference; honestly reframes what can't be sourced.
- Screens for copyright, defamation/right-of-publicity, plagiarism, and fabrication.
- Emits a fact→source matrix + a cited manuscript + a risk report.

**Won't:**
- Fabricate a citation to make a claim look supported.
- Publish your experience or opinion dressed as established fact.
- Tell you something is "legally safe" — it flags and routes legal exposure to counsel; it is **not legal advice**.
- Handle creative works (fiction/poetry/lyrics) — this is for **nonfiction**.

---

## Modes

| Mode | How | When |
|------|-----|------|
| **Guided** (default) | `orchestrator_sourced_nonfiction.md` (or `agents/sourcing-orchestrator`) | Run the whole thing; it interviews, routes, critiques, gates. |
| **Commands** | `/source-my-draft`, `/extract-claims`, `/find-sources`, `/fact-check-manuscript`, `/risk-pass` | You want one slice. |
| **Manual** | Walk `PIPELINE_OVERVIEW.md`, run `prompts/stage-*.md` yourself | Full control. |
| **Surgical** | Jump to one stage prompt | You need just that piece. Rule: jump *between* gates, never *through* Gate A. |

Also see **`PROMPT_PACK_PLAN.md`** — a documented flat-prompt-pack variant for environments without live search or orchestration.

---

## Pipeline

```
material (uncited braindump/draft)
   │
 [0] Intake & scope ........ field profile, citation style, named-party flag, jurisdiction
 [1] Claim extraction ...... atomic claims, typed (fact / judgment / analysis / opinion / named-person)
 [2] Source discovery ...... LIVE search per factual claim  → real sources or NO SOURCE FOUND   (fan-out)
 [3] Match & weight ........ does the source ACTUALLY support the claim? verdict + quality
 [4] Disposition ........... KEEP / SOFTEN / REFRAME / QUOTE / CUT   ← tacit knowledge reframed here
 [5] Risk & integrity ...... copyright · defamation/publicity · plagiarism · no-fabrication   ══ GATE A + B
 [6] Assembly .............. matrix + cited manuscript + risk report   (only if GATE A = PASS)
```

## Gates
- **Gate A — Sourcing integrity (cardinal, blocks assembly):** no orphan KEEP claims; no fabricated/unresolvable citations; no UNVERIFIED claim kept as fact. Mechanical floor = `scripts/check_citations.py`; semantic ceiling = orchestrator critique (does the source actually support the claim).
- **Gate B — Legal safety:** quotes fair-use-assessed; named-party claims screened; plagiarism audited. Exposure routed to counsel; nothing declared "cleared."
- **Gate C — Publish-readiness:** all three deliverables present; certainty calibrated; disclosure + residue surfaced to the author.

---

## Directory map

```
sourced-nonfiction-studio/
├── README.md · ARCHITECTURE.md · PIPELINE_OVERVIEW.md · AGENTS.md · DRY_RUN.md
├── orchestrator_sourced_nonfiction.md
├── prompts/stage-0…6.md
├── commands/ (source-my-draft, extract-claims, find-sources, fact-check-manuscript, risk-pass)
├── agents/ (sourcing-orchestrator, source-discovery-worker, claim-verifier, risk-reviewer)
├── referenced-prompts/README.md        # the ~15 upstream prompts it orchestrates
├── config/ (source-standards-profiles.yaml, citation-styles.yaml)
├── scripts/check_citations.py          # stdlib Gate-A citation-shape check (--self-check)
├── samples/ (braindump-sample, matrix-pass, matrix-fail)
├── data/{input,output}/                # git-ignored working tree
├── PROMPT_PACK_PLAN.md
├── .gitignore · requirements.txt
```

## Quick start
1. `python3 scripts/check_citations.py --self-check` (sanity-check the gate).
2. Guided: open `orchestrator_sourced_nonfiction.md`, paste your material, answer the Stage-0 questions.
3. Or run `/source-my-draft` and paste your braindump.
4. See `DRY_RUN.md` for a full worked example (with a real live-fetched citation).

## Requirements
Prompts need no dependencies. Live search uses WebSearch/WebFetch + optional PubMed/Consensus MCP.
`scripts/check_citations.py` is stdlib-only. Degrades to `PROMPT_PACK_PLAN.md` (plan-only) where live
search is unavailable.

**Not legal advice.** The risk pass organizes and routes exposure; publication decisions and legal
clearance require a qualified attorney.
