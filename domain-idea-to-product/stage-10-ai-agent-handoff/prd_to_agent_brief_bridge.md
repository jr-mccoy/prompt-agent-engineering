---
title: "PRD-to-AI-Agent Brief Bridge (Convert Spec to Claude-Code-Ready Package)"
category: idea-to-product/ai-agent-handoff
description: "Take the full upstream artifact set — PRD, epic/feature tree, stack decisions — and restructure it into the exact bundle that a Claude Code / Cursor agent expects: CLAUDE.md skeleton, per-epic delegation briefs, per-feature task specs sized to agent capacity, work-loop templates, and pointers to the project-memory and acceptance-test prompts that complete the handoff."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DS-02
  - RT-02
  - RT-06  # Composition / Cross-referencing
  - QA-01
difficulty: advanced
tags:
  - ai-agent-handoff
  - claude-code
  - cursor
  - delegation
  - rules-file
  - prd-to-build
updated: "2026-05-19"
related_prompts:
  - domain-idea-to-product/stage-7-prd-authoring/prd_to_epic_feature_decomposer.md
  - domain-idea-to-product/stage-8-architecture-design/architecture_tech_stack_selector.md
  - domain-idea-to-product/stage-10-ai-agent-handoff/viberescue_rules_file_design.md
  - domain-idea-to-product/stage-10-ai-agent-handoff/ai_pattern_agent_task_first_delegation_spec.md
  - domain-idea-to-product/stage-10-ai-agent-handoff/ai_pattern_agent_task_code_distance_scorer.md
  - domain-idea-to-product/stage-10-ai-agent-handoff/ai_pattern_agent_work_loop_design.md
  - domain-idea-to-product/stage-10-ai-agent-handoff/airollout_long_running_project_memory.md
  - domain-idea-to-product/stage-10-ai-agent-handoff/agent_task_acceptance_test_writer.md
---

# PRD-to-AI-Agent Brief Bridge (Convert Spec to Claude-Code-Ready Package)

**Objective:** Take the upstream pipeline artifacts (PRD, epic/feature tree, stack decisions) and produce the *exact bundle of files* a Claude Code or Cursor agent expects to start building. This prompt is the structural bridge that turns "we have a spec" into "the agent has everything it needs for the first 2 weeks of work." It does not author the rules file or per-task acceptance specs itself — those are delegated to sibling prompts via cross-reference.

## When to Use

- Stages 7 (PRD + decomposition) and 8 (stack decisions) are complete.
- You're about to start the build with an AI coding agent (Claude Code, Cursor, Codex, or similar).
- You want a complete handoff package, not an ad-hoc collection of "here's the PRD, go build it."

## Inputs

The user must provide:
1. **PRD** (from stage 7).
2. **Epic/feature tree with MVP/V1/V2 tiers** (from stage 7 decomposer).
3. **Stack-decisions document with AI-agent canonical declarations** (from stage 8 tech-stack selector).
4. **Repo state:** new repo / existing repo with code / existing repo from a different stack. If existing, paste tree + key files.
5. **Agent context:** which agent (Claude Code / Cursor / other), expected session length, whether the user will review every task or only milestones.
6. **Build cadence target:** tasks per day, expected first-milestone date (typically MVP feature 1 working end-to-end).

If any input is missing, ask. Do not infer.

## Constraints

**Must:**
- Produce the **complete file bundle** the agent should see on day 1: CLAUDE.md outline, repo skeleton, per-epic brief, first-task spec, work-loop template, project-memory file, acceptance-test template — even if some are stubs that delegate to sibling prompts.
- Map every MVP feature to one or more **agent tasks** sized for the agent's capacity. Reference the code-distance scorer to flag tasks that are too large.
- Sequence the first 10 agent tasks in a build order that respects the dependency graph and front-loads the load-bearing risky pieces.
- For each task, name the **sibling prompt** that will author its acceptance spec (`agent_task_acceptance_test_writer.md`) and its delegation brief format (`ai_pattern_agent_task_first_delegation_spec.md`).
- Produce a **CLAUDE.md skeleton** with section headers and pointers to where each section's content comes from (e.g., "Stack section → from `architecture_tech_stack_selector.md` output," "Rules section → from `viberescue_rules_file_design.md`").
- Specify the **work-loop convergence criteria** (when does the agent stop? what tests must pass?) — delegate detailed design to `ai_pattern_agent_work_loop_design.md`.
- Specify the **project-memory file layout** for cross-session continuity — delegate detailed design to `airollout_long_running_project_memory.md`.

**Must Not:**
- Author the CLAUDE.md content itself — that's `viberescue_rules_file_design.md`. This prompt produces the SKELETON and the ORDERING of inputs.
- Skip the dependency check. If task N depends on a feature not yet implemented, the agent will hallucinate the dependency. Build order must respect the graph.
- Generate full task specs in this prompt. Each task spec is its own artifact authored by `ai_pattern_agent_task_first_delegation_spec.md`. This prompt produces the **task list and ordering**.
- Pretend the agent can handle XL tasks. Decompose any XL task before delegating; reference `viberescue_decompose_stuck_task.md`.
- Combine multiple epics' tasks in one delegation. Each agent session should be scoped to one feature or smaller.

## Instructions

### Step 1: Inventory the upstream artifacts
List exactly what you received: PRD section count, epic count, feature count by tier, ADR count from stack decisions, AI-agent canonical declarations. If anything is missing, halt.

### Step 2: Produce the day-1 file bundle (the deliverable)

A complete starter package containing:

```
/project-root
├── CLAUDE.md                          # rules file skeleton — content from sibling prompt
├── README.md                          # user-facing overview
├── docs/
│   ├── prd.md                         # paste from stage 7
│   ├── architecture/
│   │   ├── stack-decisions.md         # paste from stage 8
│   │   └── adr/                       # one file per ADR
│   ├── feature-tree.md                # paste from stage 7 decomposer
│   └── build-plan/
│       ├── 00-overview.md             # this prompt's output
│       ├── 01-task-order.md           # this prompt's output: ordered task list
│       └── tasks/                     # one file per task, authored later
├── .project-memory/
│   ├── 00-state.md                    # project-memory current state
│   ├── decisions-log.md               # ADR append-only log
│   └── open-questions.md              # active questions for the user
```

For each file, indicate: (a) does this prompt author it now, (b) does a sibling prompt author it next, (c) is it a direct paste from an upstream artifact.

### Step 3: Build the day-1 CLAUDE.md skeleton
Provide section headers and source pointers, not content:

```markdown
# CLAUDE.md

## Project mission
[Source: stage 7 PRD § Vision]

## Stack canon
[Source: stage 8 architecture_tech_stack_selector AI-agent canonical declarations]

## Repo layout
[Source: this prompt § Step 2]

## Coding conventions
[Source: viberescue_rules_file_design — to be authored next]

## Forbidden patterns
[Source: viberescue_rules_file_design]

## Test policy
[Source: agent_task_acceptance_test_writer — defaults]

## Work loop
[Source: ai_pattern_agent_work_loop_design]

## Project memory
[Source: airollout_long_running_project_memory]

## Escalation rules
[when to stop and ask the user]
```

### Step 4: Generate the task list (first 10 tasks)
For each task:
- Task ID (T-001, T-002, ...)
- Title (one line, observable outcome)
- Maps to feature(s): [feature IDs from decomposer]
- Depends on: [other task IDs]
- Estimated complexity (from decomposer): S / M / L. (If L, flag for decomposition.)
- AI-agent code-distance score expected: low / medium / high — flag high for decomposition before delegation. Reference `ai_pattern_agent_task_code_distance_scorer.md`.
- Acceptance spec status: [TODO — authored by `agent_task_acceptance_test_writer.md`]
- Delegation brief status: [TODO — authored by `ai_pattern_agent_task_first_delegation_spec.md`]

Sequence tasks to respect the dependency graph and to front-load load-bearing/risky pieces (auth, data model, the first end-to-end "happy path").

### Step 5: Work-loop spec (top-level only)
- Convergence criteria: tests pass + lint pass + type-check pass + acceptance spec satisfied + no open `TODO(human)` markers.
- Stop conditions: agent has tried >3 alternative approaches OR mid-task check fails OR scope clearly exceeded the task.
- Hand-back signal: agent writes a one-paragraph status to `.project-memory/00-state.md` and asks the user to confirm before proceeding to next task.
- Full design: delegate to `ai_pattern_agent_work_loop_design.md`.

### Step 6: Project-memory spec (top-level only)
- File layout (see Step 2).
- Update protocol: agent updates `00-state.md` after every task, appends to `decisions-log.md` on architectural choices, surfaces unresolved questions to `open-questions.md`.
- Read order: agent reads CLAUDE.md → `.project-memory/00-state.md` → relevant docs/ files at session start.
- Decay check: if a session-start read of `00-state.md` is older than 7 days, agent flags potential staleness.
- Full design: delegate to `airollout_long_running_project_memory.md`.

### Step 7: Escalation rules
List the situations in which the agent must stop and ask the user, e.g.:
- A new architectural decision not covered by ADRs.
- A required external service that wasn't decided in stack selection.
- A user story whose acceptance is ambiguous after re-reading the PRD.
- An estimate exceeding the task complexity by 2x.

### Step 8: Verification checklist for the user
Before kicking off the agent, the user verifies:
- [ ] CLAUDE.md is complete (rules file authored)
- [ ] First 10 task acceptance specs authored
- [ ] First task's delegation brief authored
- [ ] Project-memory file initialized
- [ ] Repo skeleton created (folders + stubs)
- [ ] At least 1 test command runs and reports something (even on empty project)

## Output Format

Produce a single Markdown document with the following top-level sections:

```
# Day-1 AI-Agent Handoff Package: [product name]

## 1. Upstream artifact inventory
## 2. Day-1 file bundle (table: path / who authors / status)
## 3. CLAUDE.md skeleton
## 4. First 10 tasks (table)
## 5. Work-loop spec (top-level)
## 6. Project-memory spec (top-level)
## 7. Escalation rules
## 8. User pre-kickoff verification checklist
## 9. Next-prompt queue
   - Run `viberescue_rules_file_design.md` to author CLAUDE.md
   - Run `agent_task_acceptance_test_writer.md` for T-001 through T-010
   - Run `ai_pattern_agent_task_first_delegation_spec.md` for T-001
   - Run `ai_pattern_agent_work_loop_design.md` for the project loop
   - Run `airollout_long_running_project_memory.md` for memory files
```

## Verification

- [ ] All upstream artifacts inventoried; halt if missing
- [ ] File bundle table covers every file in step 2 with authoring status
- [ ] CLAUDE.md skeleton has source pointers (not content)
- [ ] First 10 tasks respect dependency graph; L tasks flagged for decomposition
- [ ] High-code-distance tasks flagged
- [ ] Work-loop spec includes convergence + stop + hand-back
- [ ] Project-memory spec includes file layout + update protocol + read order
- [ ] Escalation rules enumerated
- [ ] Next-prompt queue tells the user exactly what to run next, in order

## False-Positive Prevention

- **"The agent can figure it out from the PRD."** No. The PRD is for humans. The agent needs CLAUDE.md + per-task acceptance specs + a constrained task. Skipping the handoff bundle is the #1 cause of vibe-coding wall failures.
- **Authoring everything in this prompt.** This prompt is a router and a structure-builder. Do not produce CLAUDE.md content here, or per-task acceptance specs, or detailed work-loop logic — those are sibling-prompt outputs. Keep this prompt cohesive.
- **Combining multiple features in one task.** Agent sessions degrade with scope. One feature per session minimum; large features split further.
- **Skipping the dependency-respecting order.** If T-005 depends on T-003 but is listed earlier, the agent will fabricate the dependency, creating drift the user will pay for in week 2.
- **Forgetting to initialize project memory.** Without it, every new session starts from zero context. Initialize the files even if empty.
- **Assuming the agent will surface ambiguity.** It won't — it will guess. Bake escalation rules into CLAUDE.md.
