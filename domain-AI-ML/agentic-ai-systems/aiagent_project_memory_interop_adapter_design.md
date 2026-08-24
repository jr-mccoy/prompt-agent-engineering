---
title: "Project Memory Interop Adapter Design"
category: AI-ML/agentic-ai-systems
description: "Design portable adapter surfaces for project continuity memory across plain files, CLI, MCP resources/prompts/tools, hooks, and agent-specific signpost files without making any one agent vendor the source of truth."
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
  - mcp
  - agent-interop
  - cli
  - hooks
  - portability
updated: "2026-06-25"
related_prompts:
  - domain-AI-ML/agentic-ai-systems/aiagent_project_continuity_memory_design.md
  - domain-AI-ML/agentic-ai-systems/aiagent_project_memory_capture_protocol.md
  - domain-AI-ML/agentic-ai-systems/aiagent_project_memory_guard_before_action.md
  - domain-AI-ML/agentic-ai-systems/aiagent_tool_design.md
  - domain-AI-ML/agentic-ai-systems/aiagent_runtime_guardrails_policy.md
---

# Project Memory Interop Adapter Design

**Objective:** Design the adapter layer that lets a portable `.project-memory/` system work across humans, plain shells, Claude Code, Codex, Cursor, Gemini CLI, OpenCode, MCP clients, cloud agents, and local devices without vendor lock-in.

**When to Use:**
- A project continuity memory system already has or will have a repo-local file layout.
- Multiple agents or work surfaces need to read the same project memory.
- You need `AGENTS.md`, `CLAUDE.md`, Cursor/Gemini rules, CLI commands, MCP resources/prompts/tools, or hooks that point to the same memory substrate.
- You are designing a standalone continuity tool that should be installable into any project.

**When NOT to Use:**
- The project has no persistent memory layout yet. Use `aiagent_project_continuity_memory_design.md` first.
- You only need one-off instructions for a single agent. Write a small signpost file instead.
- You plan to make MCP, hooks, vectors, or a daemon mandatory. This prompt assumes plain files remain the baseline.

## Inputs / Context

Provide what you can; the design degrades gracefully if some are missing:
- **Memory substrate:** proposed `.project-memory/` layout, record schemas, generated projections, and local indexes.
- **Target agents:** Claude Code, Codex, Cursor, Gemini CLI, OpenCode, custom MCP clients, browser/cloud agents, humans, or other tools.
- **Runtime permissions:** whether the agent can read files, run shell commands, use MCP, install packages, or write repo files.
- **Adapter targets:** `AGENTS.md`, `CLAUDE.md`, `.mcp.json`, `.codex/config.toml`, Cursor rules, Gemini files, slash commands, hooks, CLI, or MCP server.
- **Trust model:** what configuration requires explicit human approval, what can be checked in, and what must remain local.
- **Portability requirement:** local-only, cloud-capable, team-shared, or public/open-source.

## Constraints

**Must:**
- Make plain files the baseline interface. Every richer adapter must degrade to reading and writing `.project-memory/` directly.
- Keep agent-specific instruction files as signposts, not duplicated memory databases.
- Separate MCP **resources** for readable memory, MCP **prompts** for reusable workflows, and MCP **tools** for search, validation, guard, and mutation.
- Include a CLI-first interface that works in any shell-capable agent environment.
- Define trust, approval, and configuration review rules for checked-in MCP configs, hooks, and commands.
- Specify local/cloud differences and what functionality remains available when tools cannot run.

**Must Not:**
- Make one agent's native memory feature the source of truth for the project.
- Copy the whole project memory into `AGENTS.md`, `CLAUDE.md`, or Cursor/Gemini rules.
- Require network access, a vector database, a local daemon, or MCP for basic resume and capture.
- Treat checked-in hooks or MCP startup commands as harmless; they are executable configuration and need review.
- Let adapters write conflicting memory formats for different agents.

**Instructions:**

1. **Define the adapter philosophy.** State the baseline and enhancement layers: plain files, CLI, signpost files, MCP, hooks, local index/vector acceleration. Specify that all layers read/write the same canonical records.

2. **Design the plain-file contract.** Define the minimal files any agent or human can read to resume: `current.md`, `handoff.md`, active decisions, attempts, open questions, traps, and generated resume packet if present.

3. **Design the CLI surface.** Specify commands such as `init`, `resume`, `capture session`, `remember decision`, `remember attempt`, `guard`, `audit`, `build-resume-packet`, and `scan-secrets`. For each, define input, output, and file writes.

4. **Design agent signpost files.** Specify minimal `AGENTS.md`, `CLAUDE.md`, Cursor/Gemini/OpenCode guidance, and root README snippets. They should point to `.project-memory/` and commands, not duplicate memory.

5. **Design MCP resources.** Expose read-only memory views such as `memory://current`, `memory://handoff`, `memory://resume-packet`, `memory://decisions`, `memory://decisions/{id}`, `memory://attempts/{id}`, `memory://open-questions`, and `memory://known-traps`.

6. **Design MCP prompts.** Define user-invoked workflows such as `resume_project`, `capture_session`, `remember_decision`, `remember_attempt`, `guard_before_action`, and `audit_project_memory`.

7. **Design MCP tools.** Define tool calls for `memory_search`, `memory_record`, `memory_guard_before_action`, `memory_build_resume_packet`, `memory_validate`, `memory_mark_status`, and `memory_scan_secrets`. Include schemas, permissions, and write behavior.

8. **Design hooks as optional enhancements.** Define session-start, pre-action, failed-command, and session-end hooks where supported. Include fallback manual commands for environments without hooks.

9. **Design trust and review rules.** State which configs can be checked in, which should be local-only, how startup commands are reviewed, and how branch/PR changes to adapters are audited.

10. **Design cloud/local fallback.** For each feature, specify what works in a read-only cloud environment, a shell-capable cloud environment, a local IDE, and a local terminal with MCP.

11. **Design versioning and compatibility.** Specify adapter version, manifest version, schema migration, and backward-compatible behavior when a project has an older memory layout.

12. **Produce verification cases.** Include test scenarios for plain-file-only, CLI-only, MCP-enabled, hook-enabled, read-only cloud, untrusted config, and conflicting adapter behavior.

**Output Format:**

Produce a markdown interop design:

- **Adapter Philosophy** - baseline/enhancement layers and source-of-truth rule.
- **Capability Matrix** - environment | can read files | can run CLI | can use MCP | can use hooks | expected behavior.
- **Plain-File Contract** - required files and read order.
- **CLI Surface** - command | purpose | reads | writes | output.
- **Agent Signpost Files** - minimal `AGENTS.md`, `CLAUDE.md`, Cursor/Gemini/OpenCode snippets.
- **MCP Resources** - URI | contents | read policy.
- **MCP Prompts** - prompt | inputs | workflow | output.
- **MCP Tools** - tool | schema | permissions | side effects.
- **Hook Templates** - event | command | fallback | safety notes.
- **Trust & Review Rules** - executable config review, local-only config, PR changes.
- **Cloud/Local Fallbacks** - what degrades and how.
- **Versioning & Migration** - manifest versions and compatibility behavior.
- **Verification Cases** - scenarios and expected pass/fail outcomes.

## Verification

- [ ] Plain files remain sufficient for basic resume and capture.
- [ ] CLI commands cover resume, capture, decision, attempt, guard, audit, and validation.
- [ ] Signpost files are short and do not duplicate memory contents.
- [ ] MCP resources, prompts, and tools are separated by purpose.
- [ ] Hooks are optional and have manual fallbacks.
- [ ] Trust and review rules cover executable configs and checked-in adapter changes.
- [ ] Cloud/local fallback behavior is explicit.
- [ ] All adapters read and write the same canonical memory records.

## False-Positive Prevention

❌ **DON'T:**
- Call the system portable if it only works when an MCP server is running locally.
- Put the whole memory bundle into `AGENTS.md` because one agent auto-reads it.
- Let Claude, Codex, Cursor, and Gemini each invent their own memory format.
- Treat hooks as free magic; they are executable automation and need review.
- Build the adapter layer before the plain-file and CLI flows are useful.

✅ **DO:**
- Keep agent files as signposts to the canonical memory files.
- Make CLI the lowest common denominator for shell-capable agents.
- Use MCP resources for read access, prompts for workflows, and tools for mutation/search/guarding.
- Make every adapter optional and replaceable.
- Test the read-only cloud path separately from the full local path.

## Example Output

```markdown
## Capability Matrix
| Environment | Files | CLI | MCP | Hooks | Behavior |
|---|---|---|---|---|---|
| Browser/cloud agent, read-only | yes | no | no | no | Read `current.md`, `handoff.md`, and active decisions manually. |
| Codex CLI local | yes | yes | optional | optional | Run `continuity resume` and `continuity guard`. |
| Claude Code local | yes | yes | optional | optional | Read signpost, optionally use MCP resources/tools. |
| Cursor | yes | maybe | maybe | no | Rules file points to `.project-memory/`; CLI if shell available. |

### MCP Resources
- `memory://current` → `.project-memory/current.md`
- `memory://handoff` → `.project-memory/handoff.md`
- `memory://resume-packet` → generated bounded resume packet
- `memory://decisions/{id}` → one typed decision record

### CLI Surface
- `continuity resume` → builds/prints bounded resume packet
- `continuity guard "<action>"` → checks decisions, attempts, traps, questions
- `continuity capture session` → writes session record and updates handoff
```

**Techniques Used:**
- **ST-01 (Clear Objective Statement):** defines adapter design as the target artifact.
- **ST-02 (Structured Sequential Instructions):** plain files → CLI → signposts → MCP → hooks → trust → fallback.
- **ST-03 (Output Format Specification):** produces a full interop plan with matrices and schemas.
- **CM-02 (Constraint Specification):** prevents vendor lock-in and adapter-first overbuild.
- **RT-02 (Multi-Dimensional Analysis):** weighs portability, capability, trust, cloud/local limits, and friction.
- **QA-12 (False Positives Identification):** catches fake portability and duplicated-memory traps.

**Related Prompts:**
- `aiagent_project_continuity_memory_design.md` — canonical memory architecture this adapter exposes.
- `aiagent_tool_design.md` — tool-schema discipline for MCP and CLI surfaces.
- `aiagent_runtime_guardrails_policy.md` — enforcement approach for guard and mutation tools.
