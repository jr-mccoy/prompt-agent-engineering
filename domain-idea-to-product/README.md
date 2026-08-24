# `domain-idea-to-product/` — Idea-to-Shippable-Software Pipeline

A complete, self-contained prompt pipeline for taking a software/platform idea from raw brainstorm to a working product, with the build phase optimized for handoff to an AI coding agent (Claude Code, Cursor, or similar).

This domain is **self-contained**: every prompt you need is here. Most are copies of prompts that live elsewhere in the repo, gathered into 11 stage subdirectories so you can `cd` into this directory and have the entire pipeline in one place. 8 prompts are net-new, authored specifically to fill gaps in the chain (concept-legs test, customer-discovery interview protocol, unit-economics designer, orchestrated GTM plan, PRD-to-epic decomposer, tech-stack selector, PRD-to-agent-brief bridge, and per-task acceptance-test writer).

---

## How to use this domain

There are three modes. Pick one.

### Mode 1: Guided (recommended for first-time users)
Start with **`orchestrator_idea_to_product.md`**. Paste it into a fresh Claude session, then answer the intake interview. The orchestrator classifies where you are, recommends the next 1-3 prompts to run, critiques your output at each stage, and enforces hard gates before you advance to building.

### Mode 2: Manual (you know the pipeline and want control)
Walk the stages yourself using **`PIPELINE_OVERVIEW.md`**. Each stage has inputs, outputs, and recommended prompts. Skip stages only if you have the equivalent artifact already.

### Mode 3: Surgical (you have most of the pipeline done and need one piece)
Jump straight into a stage subdirectory and grab the prompt. Each prompt is standalone (full frontmatter + objective + inputs + constraints + instructions + verification + false-positive prevention).

---

## "What stage am I at?" diagnostic

| Your current state | Start at |
|--------------------|----------|
| Just an idea, no validation | Stage 1 |
| Had 1-2 customer chats, nothing structured | Stage 1 then Stage 2 |
| ≥3 customer conversations, hypothesis forming | Stage 2 |
| Validated problem, need to understand market | Stage 3 |
| Need to design business model and pricing | Stage 4 |
| Need GTM, positioning, brand | Stage 5 |
| Need a sanity check before committing | Stage 6 |
| Need to author the PRD | Stage 7 |
| Have PRD, need architecture & stack | Stage 8 |
| Have stack, need phased build plan | Stage 9 |
| Ready to hand off to AI coding agent | Stage 10 (pre-gated by Stage 11) |
| Want to pre-mortem the build plan | Stage 11 |

---

## Stages

| # | Stage | Purpose | Subdirectory |
|---|-------|---------|--------------|
| 1 | **Ideation** | Generate / stress-test the raw idea | `stage-1-ideation/` |
| 2 | **Problem Validation** | Customer discovery, JTBD | `stage-2-problem-validation/` |
| 3 | **Market Research** | Competitive landscape, TAM/SAM/SOM, unit economics | `stage-3-market-research/` |
| 4 | **Business Model** | Canvas, pricing, monetization | `stage-4-business-model/` |
| 5 | **Strategy & Positioning** | SWOT, brand, GTM plan | `stage-5-strategy-positioning/` |
| 6 | **Decision Validation** | Pre-mortem, blind spots, "am I being nuts?" | `stage-6-decision-validation/` |
| 7 | **PRD Authoring** | Build the PRD, decompose into epics/features | `stage-7-prd-authoring/` |
| 8 | **Architecture Design** | Deep design, stack selection, API/schema | `stage-8-architecture-design/` |
| 9 | **Phased Build Plan** | Sprint plans, milestone sequencing | `stage-9-phased-build-plan/` |
| 10 | **AI-Agent Handoff** | CLAUDE.md, task specs, acceptance tests, work loop | `stage-10-ai-agent-handoff/` |
| 11 | **Build-Risk Pre-Mortem** | Failure-mode pre-mortem before kickoff | `stage-11-build-risk-premortem/` |

---

## The 8 new prompts (authored for this domain)

These were authored to fill gaps the upstream prompts didn't cover:

| Stage | New prompt | What it produces |
|-------|------------|-----------------|
| 1 | `ideation_concept_legs_test.md` | GO / KILL / RESHAPE verdict on a raw idea (founder fit, contrarian truth, distribution, why-now, 10x claim) |
| 2 | `validation_customer_discovery_interview_protocol.md` | 45-60 min JTBD + Mom Test interview guide with scoring rubric |
| 3 | `market_unit_economics_designer.md` | LTV/CAC/payback/cohort model with sensitivity bands and GREEN/YELLOW/RED verdict |
| 5 | `strategy_gtm_orchestrated_plan.md` | 90-day GTM plan: ICP, 3 ranked channels, launch sequence, first-100 playbook, weekly calendar with kill conditions |
| 7 | `prd_to_epic_feature_decomposer.md` | Epic → feature → story tree with dependency graph and MVP/V1/V2 cut lines |
| 8 | `architecture_tech_stack_selector.md` | Per-component decision matrix with AI-agent friendliness scoring + ADRs |
| 10 | `prd_to_agent_brief_bridge.md` | Day-1 file bundle the agent expects (CLAUDE.md skeleton, task list, work-loop spec, project-memory spec) |
| 10 | `agent_task_acceptance_test_writer.md` | Per-task acceptance block: commands, expected outputs, false-success traps |

Plus three framework documents at the root:
- `orchestrator_idea_to_product.md` — the master orchestrator
- `README.md` — this file
- `PIPELINE_OVERVIEW.md` — visual flow, branching logic, terminal artifacts

---

## Hard gates (enforced by the orchestrator)

The orchestrator will not let you skip these:

- **Before Stage 4:** Stage 2 must have produced ≥5 rubric-scored interviews.
- **Before Stage 7:** Stage 6 must have a completed pre-mortem and either a passed `am-i-being-nuts` check or an explicit declined-with-justification.
- **Before Stage 10:** Stage 7 (PRD passing quality gate), Stage 8 (stack decisions), Stage 9 (phased plan), and Stage 11 (build-risk pre-mortem) must all be complete.

If you skip a gate manually (without the orchestrator), the corresponding stage prompts will still ask for the upstream artifacts as inputs. You'll either provide them or stall.

---

## Terminal artifacts (what you end up with)

After running the full pipeline, you have:

**Business artifacts:**
- Validated problem hypothesis with interview evidence
- Market sizing (TAM/SAM/SOM) and unit-economics model
- Business model canvas
- 90-day GTM plan
- Decision validation / pre-mortem log

**Product artifacts:**
- Complete PRD
- Epic → feature → story tree with MVP/V1/V2 cut lines
- Open-questions register

**Engineering artifacts (handoff to AI agent):**
- `CLAUDE.md` rules file (project-canonical conventions, forbidden patterns)
- Architecture-decision-records per component
- Stack decisions doc
- Day-1 file bundle (repo skeleton + docs/ + .project-memory/)
- Sequenced task list (first 10 tasks with dependencies)
- Per-task acceptance specs
- Work-loop spec (when to stop, when to ask, when to advance)
- Project-memory file layout (cross-session continuity)
- Build-risk pre-mortem with verification attached to each failure mode

These artifacts let you start a Claude Code (or Cursor) session, paste the day-1 brief, and have the agent begin coding with the structural guardrails needed to avoid the common AI-coding-wall failure modes.

---

## Notes on copies vs. originals

To make this directory self-contained, ~40 existing prompts have been **copied** here from other domains (not moved). The originals remain in their domains. If you find improvements while using these copies, update the original first; this domain's copies should be refreshed periodically to stay in sync.

Each copied prompt keeps the frontmatter of its original, so the source domain is
identifiable from the prompt's own `category` field; `PROMPT_INDEX.json` lists both
the copy and the original.

---

## Related root-level resources

- `CLAUDE.md` — repo-wide agent guide
- `AI_AGENT_QUICK_START.md` — patterns for coding prompts
- `NON_CODING_QUICK_START.md` — patterns for non-coding prompts (used to author the business-side gap prompts)
- `PROMPT_QUALITY_STANDARDS.md` — Tier-1 quality bar all prompts in this domain meet
- `techniques/MASTER_TECHNIQUE_INDEX.md` — technique IDs referenced in frontmatter
