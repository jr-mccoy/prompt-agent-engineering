# AGENTS.md — Children's Book Studio (coding-agent entry point)

This file orients a coding agent (Codex, Claude Code, or similar) that is asked to *run* or *extend* the Children's Book Studio. Humans should start at [`README.md`](README.md).

---

## What this toolkit is

A prompt-orchestration system that converts a children's-writing idea into a finished, publishable manuscript + submission package. It has **no executable code** — it is a pipeline of markdown prompts driven by an orchestrator, enforcing gates by critique. There is nothing to install, build, or compile.

## How to run it

1. Read [`orchestrator_childrens_book.md`](orchestrator_childrens_book.md). It is the conductor: it interviews the user, classifies the project's form and entry stage, routes to stage prompts, and critiques each output against that stage's Verification Checklist before advancing.
2. Each stage prompt in [`prompts/`](prompts/) names the [`domain-childrens-writing/`](../domain-childrens-writing/) prompt(s) it routes to. Run those against the user's manuscript.
3. At each gate, apply the stage's Verification Checklist mechanically (PASS/FAIL per item). **Do not advance on any FAIL** — return the user to fix or re-run.
4. The four agents in [`agents/`](agents/) define authority boundaries (Can-Do / Ask-First / Never). Respect them.

## The gates (enforce these)

| Gate | Stage | Blocks advancement unless |
|------|-------|---------------------------|
| 0 Age boundary | 0 | form + age band valid; mature-YA content → redirect to `domain-creative-writing/` |
| A Craft integrity | 4 | child drives climax; theme not preached; read-aloud rhythm where required; reading level on band |
| B Truth & representation | 5 | NF specifics sourced-or-`VERIFY`; back matter present; representation audit = flags only (never a certification); no age-inappropriate content |
| C Publishing honesty | 6 | no fabricated comps/agents/figures (bracketed `[AUTHOR TO VERIFY]`); deliverable manifest complete |

## Hard rules (do not violate)

- **Never fabricate nonfiction fact.** Bracket unknowns `VERIFY`; never supply dates/quotes/sources from memory.
- **Never certify representation.** The audit produces risk flags and questions for a human reader only.
- **Never invent publishing facts** (comps, agents, sales, submission rules). Bracket `[AUTHOR TO VERIFY]`.
- **Never write mature-content YA.** Redirect out at Gate 0.
- **Never silently overwrite the author's draft.** Save revisions as a new version; the author owns the files.

## Extending the toolkit

- New stage prompt → follow the Tier-1 structure (Objective, When to Use, Inputs, Constraints Must/Must-Not, Instructions, Output Format, Verification Checklist) and register it in [`PIPELINE_OVERVIEW.md`](PIPELINE_OVERVIEW.md) + the orchestrator's classification table.
- New routing to a domain prompt → add it to [`referenced-prompts/README.md`](referenced-prompts/README.md) and confirm the path resolves under `domain-childrens-writing/`.
- Changing a gate → update both the relevant stage prompt's checklist AND [`design-bundle/GATE_DESIGN.md`](design-bundle/GATE_DESIGN.md).

## Verification

There is no test suite (no code). The verification artifact is [`DRY_RUN.md`](DRY_RUN.md), a worked end-to-end run with deliberate failure injections showing each gate firing. After any change, re-walk the relevant DRY_RUN scenario to confirm the gate still bites.
