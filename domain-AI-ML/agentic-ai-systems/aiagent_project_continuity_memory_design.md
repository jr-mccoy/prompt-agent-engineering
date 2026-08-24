---
title: "Project Continuity Memory Design"
category: AI-ML/agentic-ai-systems
description: "Design a portable, repo-local project memory system that preserves decisions, failed attempts, handoffs, open questions, and durable project state across humans, sessions, agents, tools, and devices."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - RT-02
  - QA-12
difficulty: advanced
tags:
  - project-memory
  - continuity
  - agent-interop
  - repo-local-memory
  - handoff
  - second-brain
updated: "2026-06-25"
related_prompts:
  - domain-AI-ML/agentic-ai-systems/aiagent_memory_design.md
  - domain-AI-ML/agentic-ai-systems/aiagent_context_engineering_at_scale.md
  - domain-AI-ML/agentic-ai-systems/aiagent_durable_execution_state_persistence.md
  - domain-AI-ML/agentic-ai-systems/aiagent_memory_poisoning_defense.md
  - domain-engineering-workflows/ai-native-rollouts/airollout_long_running_project_memory.md
  - domain-agentic-resources/commands/multi-agent/multiagent_graceful_session_endings.md
---

# Project Continuity Memory Design

**Objective:** Design a portable, repo-local project continuity memory system that lets any future human or agent resume work without re-discovering decisions, repeating failed attempts, or trusting stale context.

**When to Use:**
- A project will span many sessions, tools, branches, devices, or agents.
- The user repeatedly re-explains prior decisions, current state, failed attempts, open questions, or next steps.
- Different coding agents may touch the same project, such as Claude Code, Codex, Cursor, Gemini CLI, OpenCode, or a custom MCP client.
- You are designing a project-local second brain that should be useful in any repo, not only in one model or one vendor's memory feature.

**When NOT to Use:**
- The work is a one-off task with no meaningful cross-session continuity need.
- You only need internal agent memory for one runtime loop. Use `aiagent_memory_design.md`.
- You only need active context-window compaction. Use `aiagent_context_engineering_at_scale.md`.
- The user wants a full transcript archive. This prompt designs curated durable state, not chat-history hoarding.

## Inputs / Context

Provide what you can; the design degrades gracefully if some are missing:
- **Project shape:** codebase, writing project, research project, business plan, mixed project, or non-repo workspace.
- **Continuity pain:** what keeps getting lost across sessions, such as decisions, failed fixes, ideas, blockers, branch state, or next actions.
- **Tool surface:** agents and environments expected to read or write memory, including local CLI, cloud agent, IDE, MCP client, or human-only use.
- **Sharing model:** solo, small team, public repo, private repo, client repo, or local-only workspace.
- **Privacy posture:** what can be committed, what must stay local, and what must never enter memory.
- **Existing artifacts:** `AGENTS.md`, `CLAUDE.md`, ADRs, PRDs, tasks, issues, docs, tests, or existing memory files.
- **Maintenance tolerance:** how much friction the user will realistically tolerate at session end.

## Constraints

**Must:**
- Treat repo-local, human-readable records as the source of truth; indexes, vectors, generated summaries, hooks, and MCP servers are acceleration layers.
- Separate durable project memory from active context, execution checkpoints, personal preferences, raw transcripts, and secrets.
- Define a memory taxonomy with record types, ownership, storage path, lifespan, stale conditions, and evidence requirements.
- Include a read/resume protocol and a write/capture protocol that work even when MCP, hooks, or local indexes are unavailable.
- Define status and supersession rules so old memory cannot silently masquerade as current truth.
- State that memory is advisory: current user instruction, source code, tests, build output, and authoritative docs outrank memory.

**Must Not:**
- Make a vector database, chat transcript, vendor memory feature, or MCP server the canonical source of truth.
- Dump all memory into `AGENTS.md`, `CLAUDE.md`, or another always-loaded instruction file.
- Store secrets, credentials, customer PII, or sensitive personal notes in committed project memory.
- Leave decisions, failed attempts, traps, and handoffs as untyped prose with no status, date, source, or evidence.
- Design a system so heavy that the user will stop updating it after three sessions.

**Instructions:**

1. **Decide whether project continuity memory is justified.** Estimate expected session count, number of tools/agents, context-loss pain, and cost of repeated mistakes. If the work is short-lived or low-friction, recommend a minimal handoff file and stop.

2. **Separate memory scopes.** Define what belongs in project-shared memory, local-private memory, external systems, and nowhere. Explicitly separate project facts from personal preferences and secrets.

3. **Define the memory taxonomy.** Specify record types such as current state, handoff, decision, attempt, trap, open question, idea, session, evidence pointer, and private note. For each, define purpose, storage path, expected lifespan, owner, and stale trigger.

4. **Design the repo-local layout.** Produce a portable `.project-memory/` layout that can live in any repo or project folder. Include which paths are committed, generated, or gitignored.

5. **Specify canonical record metadata.** Define required fields: `id`, `type`, `title`, `status`, `created_at`, `created_by`, `agent`, `scope`, `branch`, `commit`, `confidence`, `privacy`, `supersedes`, `superseded_by`, `expires_at`, `tags`, and `evidence`. Adjust for non-git projects if needed.

6. **Define source-of-truth and conflict rules.** State how memory relates to code, tests, docs, issue trackers, user instructions, and generated indexes. Include the rule for marking memory `stale`, `disputed`, or `superseded` when reality changes.

7. **Design the resume protocol.** Define what a future agent or human reads first, how a bounded resume packet is generated, and how branch/commit mismatch or stale handoff warnings are surfaced.

8. **Design the capture protocol.** Define when and how sessions, decisions, failed attempts, traps, ideas, and open questions are written. Keep the capture path short enough to be used when the user is tired.

9. **Design guard-before-action behavior.** Specify how the system checks proposed work against active decisions, failed attempts, traps, stale warnings, and open questions before the agent acts.

10. **Design audit and decay.** Define scheduled and trigger-based audits for stale current state, superseded decisions, unreviewed high-impact records, missing evidence, possible secrets, branch mismatch, and memory bloat.

11. **Plan interop layers.** Define baseline plain-file behavior first, then CLI, optional MCP resources/prompts/tools, optional hooks, and optional local index/vector acceleration. Each enhancement must degrade to plain files.

12. **Produce the design and verification gates.** Name the minimal viable version, the later enhancements, and pass/fail gates for memory need, layout integrity, capture working, resume working, safety, and interop.

**Output Format:**

Produce a markdown design doc:

- **Continuity Need Assessment** - why memory is justified or why a minimal handoff is enough.
- **Scope & Privacy Model** - repo-shared, local-private, external, and never-store categories.
- **Memory Taxonomy** - table: Type | Answers | Path | Lifespan | Owner | Stale trigger.
- **Repo-Local Layout** - concrete `.project-memory/` tree with committed/generated/gitignored markers.
- **Record Schema** - required metadata fields plus body sections for each durable record type.
- **Source-of-Truth Rules** - memory priority, conflict handling, supersession, disputed status.
- **Resume Protocol** - read order, resume packet contents, stale/branch mismatch handling.
- **Capture Protocol** - session end, decision, attempt, trap, idea, and question triggers.
- **Guard-Before-Action Policy** - when to guard, inputs, lookup targets, output decisions.
- **Audit & Decay Plan** - cadence, checks, owners, and escalation.
- **Interop Plan** - plain files, CLI, MCP, hooks, generated index, vector layer if justified.
- **Validation Gates** - Gate 0/A/B/C/D/E pass criteria.

## Verification

- [ ] The design is portable across projects and not tied to this repository or one agent vendor.
- [ ] Human-readable repo files are the canonical source of truth.
- [ ] Memory types are separated by purpose and decay rate.
- [ ] Every durable record has status, source, timestamp, confidence, privacy, and evidence fields.
- [ ] Resume works without MCP, hooks, vectors, or a local daemon.
- [ ] Capture friction is low enough for repeated use.
- [ ] Stale, disputed, superseded, private, and secret-prohibited cases are handled.
- [ ] Guard-before-action checks prior decisions, attempts, traps, and open questions.
- [ ] Memory is advisory and cannot override code, tests, current user instructions, or authoritative docs.

## False-Positive Prevention

❌ **DON'T:**
- Design a beautiful memory cathedral whose capture ritual is so heavy no one uses it.
- Treat `AGENTS.md` or `CLAUDE.md` as the memory database; they should be signposts, not libraries.
- Preserve raw transcripts as memory. Extract durable decisions, attempts, open questions, and handoffs.
- Trust old memory because it is written down. Old wrong context is worse than no context.
- Add embeddings before exact lookup, metadata filters, stale checks, and source hashes exist.

✅ **DO:**
- Start with typed Markdown/YAML records and deterministic generated projections.
- Make failed attempts first-class records, since they prevent expensive repeated mistakes.
- Keep resume packets bounded and task-relevant.
- Use status and supersession instead of silently editing history.
- Design the plain-file path first, then layer CLI/MCP/hooks on top.

## Example Output

```markdown
## Continuity Need Assessment
Project expects months of work across Claude Code, Codex, and human weekend sessions. Prior decisions and failed migration attempts have already been rediscovered twice. Full continuity memory is justified.

### Repo-Local Layout
.project-memory/
  README.md                 # committed
  manifest.yml              # committed
  current.md                # committed
  handoff.md                # committed
  open-questions.md         # committed
  known-traps.md            # committed
  decisions/                # committed, one decision per file
  attempts/                 # committed, one attempt per file
  sessions/                 # committed or archived by policy
  ideas/                    # committed or local by policy
  evidence/refs.yml         # committed pointers only
  private/                  # gitignored
  generated/                # generated projections
  index/                    # gitignored local index

### Source-of-Truth Rules
Memory is advisory. Current user instruction, code, tests, build output, and authoritative docs outrank memory. If memory conflicts with present evidence, mark it `disputed` or `stale` and link the new evidence.

### Guard-Before-Action Policy
Before non-trivial work, guard the proposed action against active decisions, failed attempts, traps, and open questions. Output: PROCEED, PAUSE, ASK HUMAN, or READ FIRST.
```

**Techniques Used:**
- **ST-01 (Clear Objective Statement):** defines a concrete continuity-memory design outcome.
- **ST-02 (Structured Sequential Instructions):** need → scope → taxonomy → layout → schema → protocols → gates.
- **ST-03 (Output Format Specification):** forces a complete design artifact with named sections.
- **CM-02 (Constraint Specification):** prevents vector-first, transcript-first, or vendor-locked designs.
- **RT-02 (Multi-Dimensional Analysis):** balances portability, friction, security, stale risk, and interop.
- **QA-12 (False Positives Identification):** blocks memory theater that appears rigorous but fails in real use.

**Related Prompts:**
- `aiagent_project_memory_capture_protocol.md` - write/capture rules for sessions, decisions, attempts, and handoffs.
- `aiagent_project_memory_guard_before_action.md` - pre-action warning layer that checks prior memory before acting.
- `aiagent_project_memory_interop_adapter_design.md` - CLI/MCP/hooks/agent-signpost adapters.
- `aiagent_project_memory_security_decay_audit.md` - stale, poisoned, private, and unsafe memory controls.
