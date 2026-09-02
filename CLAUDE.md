# Prompt & Agent Engineering — Agent Guide

**Purpose:** How AI agents should navigate and extend the Prompt & Agent Engineering
(PAE) repository — a governed registry of prompts, skills, agents, commands, and
personas.

This file is deliberately short. It carries only what an agent needs *every* session:
how to route, where things belong, how to author, and how not to waste context.
Everything exhaustive lives one hop away.

## Routing: use the Engine first

```bash
pae route  "<task>"     # which scope and kind should handle this, and why
pae search "<task>"     # ranked resources, with the matched terms shown
```

Generated from `meta/registry/`, so unlike a hand-maintained table it cannot drift.
It reports `ambiguous`, `weak`, or `no_route` rather than guessing; every status
exits 0. Details: [`pae-engine/docs/search-routing.md`](pae-engine/docs/search-routing.md).

An MCP client can call the same Engine directly instead of shelling out:
`pae mcp --repo <checkout>` serves four read-only tools over stdio behind the
optional `[mcp]` extra. See [`pae-engine/docs/mcp.md`](pae-engine/docs/mcp.md).

**Fallbacks, in order:**

| Need | Go to |
|---|---|
| Engine not installed, or you want the full per-domain tables | [`meta/ROUTING_REFERENCE.md`](meta/ROUTING_REFERENCE.md) — repository structure, category mapping, non-coding domain mapping, task→resource table |
| Find an existing prompt by keyword/technique/domain | `PROMPT_INDEX.json` (machine-readable) or `PROMPT_INDEX.md` |
| A domain's own conventions, guards, and boundaries | that domain's `README.md` / `EXPANSION_ROADMAP.md` |

The reference file is the *only* source for what the registry cannot represent:
negative boundaries ("X lives here, **not** there"), load-bearing domain conventions
and safety guards, and ordered workflows. A lexical router can rank resources; it
cannot tell you not to create a duplicate. Agreement measurements and the migration
plan: [ADR-0023](meta/adr/0023-executable-routing-migration.md).

---

## Repository Overview

This is a governed collection of AI prompts and agentic resources — the **PAE Registry** — designed for:
- **AI coding agents** (Claude Code, Cursor, GitHub Copilot)
- **Developers** building with AI
- **Teams** standardizing prompt quality
- **Learners** studying prompt engineering

**Total resources** (generated — do not hand-edit; run `python3 scripts/generate_repo_facts.py --write`):

<!-- REPO_FACTS:BEGIN name=counts -->
<!-- REPO_FACTS_DECLARATION: {"active_techniques": 327, "agentic_resource_artifacts": 799, "agents": 143, "bundled_component_files": 667, "commands": 115, "domain_command_artifacts": 10, "domain_directories": 44, "domain_prompt_artifacts": 4121, "indexed_artifacts": 5597, "personas": 53, "skills": 330, "technique_categories": 18, "unindexed_domain_directories": 0} -->
- **4121 indexed domain prompt artifacts** across 44 `domain-*` directories. This is the index's structural classification, not a normalized resource-kind count.
- **330 skills, 143 agents, 115 commands, 53 personas** under `domain-agentic-resources/`.
- **327 active techniques** across 18 categories in `techniques/MASTER_TECHNIQUE_INDEX.md`.
- `PROMPT_INDEX.json` holds **5597 indexed artifacts**. That total is not a prompt count: it mixes the 4121 domain prompt artifacts with 10 domain slash commands, 799 agentic resources, and 667 bundled component files (a parent resource's `references/`, `assets/`, `cards/` and similar).
- All 44 `domain-*` directories are covered by the index allowlist (`DOMAIN_DIRS` in `scripts/generate_prompt_index.py`).
<!-- REPO_FACTS:END name=counts -->

Membership rules for each category live in [`meta/REPOSITORY_FACTS.json`](meta/REPOSITORY_FACTS.json).

### Top-level layout

| Path | What it holds |
|---|---|
| `domain-*/` (44) | The prompt corpus, one directory per domain |
| `domain-agentic-resources/` | **Implementation library** — skills, agents, commands, personas to *use* |
| `authoring/` | **Authoring system** — patterns, templates, rubrics for *creating* skills / agents / commands / agentic systems |
| `techniques/` | Technique index + use-case lookup |
| `meta/` | Registry, ADRs, routing reference, reorg map, vendored-copy ledger |
| `pae-engine/` | The `pae` CLI (routing, search, context bundles) and its optional MCP server |
| `scripts/` | Index generation, naming/link validation, drift checks |
| `tests/` | Repo invariants |
| Toolkits at root | `agentic-system-factory/`, `childrens-book-studio/`, `sourced-nonfiction-studio/`, `ai-investment-research-toolkit/`, `financial-records-toolkit/`, `continuity-kit/`, `portable-prompt-system/` — self-contained pipelines that *orchestrate* domain prompts rather than duplicating them |

The 44 domains: AI-ML, advertising, agentic-resources, biblical-studies,
business-strategy, childrens-writing, conversation-practice, creative-writing,
decision-making, deep-analysis, discipleship, education-teaching,
engineering-workflows, finance, frontend-development, game-development,
healthcare-clinical, hr-management, idea-to-product, ideation, image-generation,
learning, learning-coding, legal, medical-education, negotiation, parenting,
personal-development, policy, presentations, product-management, productivity,
professional-writing, prompt-engineering, psy-ops, psychology, reasoning-craft,
research-academic, risk, science, software-engineering, specialized-fields,
voice-conversational-ui, written-advocacy.

---

## Which domain does this belong in?

Most mis-filing here has come from one cause: several domains carving the same
territory on different axes. That is settled. **Subject decides first; audience
decides among the work domains.**

### 1. Does the prompt have a subject-matter home?

If the prompt's *input or object* belongs to a discipline, it goes there regardless
of who runs it:

| The prompt's object is… | Domain |
|---|---|
| A codebase, repo, API, or app build spec | `domain-software-engineering/` (business frameworks applied to code → `analysis/business/`) |
| Money, tax, valuation, markets | `domain-finance/` |
| A contract, entity, dispute, or filing | `domain-legal/` |
| A patient, or a clinician in training | `domain-healthcare-clinical/` / `domain-medical-education/` |
| A model, dataset, agent, or LLM system | `domain-AI-ML/` |
| A manuscript, letter, or piece of prose | `domain-professional-writing/` and the writing domains |

### 2. Otherwise: whose work is it, at what scope?

The five work domains sit on one axis. Pick by who holds the prompt:

| Scope | Domain | The question it answers |
|---|---|---|
| **Self** | `domain-personal-development/` | Who am I becoming? Identity, values, habits, goals, resilience, relationships, career |
| **Individual execution** | `domain-productivity/` | How do I get my own work done? Daily planning, deep work, reviews, cadence, automation |
| **Team delivery** | `domain-engineering-workflows/` | How does my team ship? Sprints, incidents, definition-of-done, AI adoption |
| **Product** | `domain-product-management/` | What should we build, and is the spec good enough? |
| **Org / company** | `domain-business-strategy/` | What should the company do? Strategy, positioning, go-to-market |

**Worked examples of the axis doing real work:**

- A weekly review exists in several domains and that is correct — they review
  different things. `domain-productivity/reviews/` reviews your *systems*;
  `domain-personal-development/prompts/agency/` reviews your *direction*;
  `domain-productivity/operating-cadence/` closes your *week's state*. When you add
  another, say in its description what it is distinct from.
- A prompt that takes a codebase and produces a SWOT is **software engineering**,
  not business strategy — the input decides.
- A "chief of staff" cadence for one person is **individual execution**, not org
  strategy — the scope decides.
- Sales, marketing, and customer-success workflows are **org**, not engineering,
  even when an engineering team wrote them.

### 3. Before adding anything, check it does not already exist

Run `pae search`, or search `PROMPT_INDEX.json` by keyword. If a near-neighbour
exists, either extend it or state in the new prompt's `## When to Use` what it is
**distinct from**. Two prompts doing the same job for the same reader in two domains
is the defect this structure exists to prevent.

---

## Handling a request

| The user is asking for… | Do this |
|---|---|
| **Help with a task** ("analyze my code", "review my…") | Find an existing resource. `pae search` → `domain-agentic-resources/skills/` → the domain directory. Execute it against their context; customize for their stack. Do **not** author something new when one exists. |
| **A new prompt — image generation** | Build from `domain-image-generation/IMAGE_GENERATION_GUIDE.md` (8 core techniques: terminology steering, grid forcing + enumerated slots, constraint redundancy, negative-space control, allowed-vs-forbidden, physical context anchoring, deliverables locking, validation checklist). Model-specific: `IMAGE_MODEL_SELECTION_GUIDE.md`, `GPT_IMAGE_2_GUIDE.md`, `NANO_BANANA_GUIDE.md`. |
| **A new prompt — coding/technical** | Build from `AI_AGENT_QUICK_START.md` (5-step process) + `techniques/USE_CASE_LOOKUP.md` + `techniques/MASTER_TECHNIQUE_INDEX.md`. |
| **A new prompt — non-coding** | Build from `NON_CODING_QUICK_START.md`. Classify task type (CREATE / LEARN / DECIDE / COMMUNICATE / IMPROVE / SIMULATE), identify domain, apply the pattern, use the 5 elements (intent clarity, audience, context, output spec, quality indicators), add verification + false-positive prevention. |
| **A new skill** | `authoring/skill-patterns/README.md` → classify type (WORKFLOW / TOOL / DOMAIN / CREATION / ANALYSIS / INTEGRATION / META) → `SKILL_USE_CASE_LOOKUP.md` → `SKILL_PATTERN_INDEX.md` (41 patterns) → validate with `SKILL_QUALITY_RUBRIC.md`. |
| **A new agent / command** | `authoring/agent-patterns/AGENT_QUICK_START.md` / `authoring/command-patterns/COMMAND_QUICK_START.md`. |
| **A whole agentic system** | Manual: `authoring/system-patterns/README.md`. Guided: `agentic-system-factory/`. Gate 0 first — `domain-AI-ML/agentic-ai-systems/aiagent_complexity_ladder_gate.md` asks whether it needs an agent at all. |
| **To learn about prompting** | `AI_AGENT_QUICK_START.md`, `techniques/MASTER_TECHNIQUE_INDEX.md`, `PROMPT_QUALITY_STANDARDS.md`. |

**Multi-faceted requests** (e.g. "security *and* performance"): execute each matching
prompt, then synthesize one report.

**Skill vs prompt.** Author a **skill** when the capability is reused across sessions,
needs bundled resources (scripts, templates, references), orchestrates a multi-step
workflow, integrates an external tool, or benefits from progressive disclosure.
Author a **prompt** when the task is one-off, self-contained, and instruction-only.

**`authoring/` vs `domain-agentic-resources/`** — complementary, not overlapping:
`authoring/` is *how to build* (patterns, templates, rubrics);
`domain-agentic-resources/` is *what is already built* (use it).

---

## Key reference files

| File | Use for |
|---|---|
| `PROMPT_INDEX.json` / `.md` / `PROMPT_INDEX_GUIDE.md` | Discovery by keyword, technique code (ST-01, RT-02…), domain, difficulty; `related_prompts` cross-refs |
| `AI_AGENT_QUICK_START.md` | Building coding/technical prompts |
| `NON_CODING_QUICK_START.md` | Building non-coding prompts (the 6 task-type patterns) |
| `domain-image-generation/IMAGE_GENERATION_GUIDE.md` | Building image-generation prompts |
| `techniques/USE_CASE_LOOKUP.md` | Technique selection by task type |
| `techniques/MASTER_TECHNIQUE_INDEX.md` | The 327-technique catalog |
| `PROMPT_QUALITY_STANDARDS.md` | Tier definitions; False-Positive Prevention is the #1 quality differentiator |
| `authoring/skill-patterns/templates/GOLD_STANDARD_SKILL.md` | Annotated exemplar skill |
| `meta/ROUTING_REFERENCE.md` | Full per-domain routing tables |
| `meta/REORG_MAP.tsv` / `meta/VENDORED.tsv` | Every move and deletion / canonical→copy pairs |

---

## Naming conventions

```
Prompts            {category}_{specific_function}.md    architecture_layer_identification.md
Non-engineering    {domain}_{specific_function}.md      decisioning_blind_spot_identifier.md
Personas           {domain}_{role_descriptor}.md        testing_reality_checker.md
```

One filename prefix per subdirectory, kept consistent within a domain. Validate with
the scripts in `scripts/` before committing.

---

## Guidelines

**Do:** use existing resources for task help; customize them to the user's stack;
combine several for multi-faceted requests; follow the authoring processes when
building new; keep prompts to 3–5 techniques and skills to one job.

**Don't:** author a new resource when one exists; skip the repository search;
over-complicate; create a skill where a prompt suffices; hand-edit generated blocks
(`REPO_FACTS`, `PROMPT_INDEX.json`) — run the generator scripts instead.

---

## Token efficiency rules

This repo is large enough that careless reading ends sessions early. Auto-compact
fires at 70% (`.claude/settings.json`); that budget only holds if you don't waste it.
Apply these always, unasked:

- **Never re-read a file** already read this session unless you edited it or need a
  different slice. An `Edit`/`Write` success response is authoritative — don't read
  back to "confirm."
- **Never re-verify established facts** — paths, frontmatter, technique IDs,
  directory structure, git state. Read `CLAUDE.md`, `PROMPT_INDEX.json`, and the
  technique index at most once per session.
- **Plan before reading.** State what you need from a file first; if you can answer
  without opening it, don't. Prefer `Grep` over `Read`; use `offset`/`limit` on large
  files.
- **Batch, don't iterate.** Independent reads/searches in one message; larger edits
  rather than many small ones to the same file.
- **Trust tool results.** No-result searches are real results — don't retry variants
  hoping otherwise.
- **Stop when done.** No "just in case" verification passes or summary re-reads.

---

**Last updated:** 2026-09-02 — CLAUDE.md reduced to the always-loaded essentials;
the exhaustive routing tables moved to [`meta/ROUTING_REFERENCE.md`](meta/ROUTING_REFERENCE.md).
