---
name: multiagent_tool_set_minimization
description: "Audit an agent's tool set, classify each tool as always-on / on-demand / remove, and produce the minimal always-on set. Smaller tool sets reduce drift, context bloat, and failure surface."
version: "1.0.0"
category: multi-agent
tags: [minimization, multi-agent, multiagent, set, tool]
agents_used: []
title: "Agent Tool Set Minimization (Always-On vs On-Demand)"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-02
  - DS-06
  - QA-01
difficulty: beginner
updated: "2026-04-20"
related_prompts:
  - domain-agentic-resources/commands/multi-agent/multiagent_worker_isolation_boundaries.md
  - domain-agentic-resources/commands/multi-agent/multiagent_two_tier_architecture_template.md
---
# Agent Tool Set Minimization (Always-On vs On-Demand)

**Purpose:** Every tool in an agent's always-on set costs tokens (schemas in the system prompt), cognitive surface (the model considers it at every step), and failure surface (wrong-tool selection, unexpected side effects). This prompt audits a tool set, classifies each tool as **always-on**, **on-demand**, or **remove**, and produces the minimal always-on configuration for the agent's actual job.

**When to use:**
- An agent has accumulated tools over time and the tool list is suspiciously long
- An agent keeps picking the wrong tool (calls `grep` when `read` would do, or vice versa)
- System-prompt token cost is climbing and you don't know which tools are pulling their weight
- You're launching a new worker agent and want to start with the minimum viable tool set
- Related agents have overlapping tool sets and no clear specialization

**What you'll get:** A classified tool table (Always-On / On-Demand / Remove), the always-on tool set as a shipped list with per-tool justifications, a load-on-demand plan for the rest, and a "test it's still enough" check.

---

```
## ROLE
You are a tool-set auditor for an AI agent. You classify each tool as Always-On, On-Demand, or Remove, and produce the minimized always-on set for this specific agent's job. You err toward smaller sets. Bigger sets are the default — your job is to push back.

## CONTEXT
Tool choice failures show up in predictable ways:

- **Wrong tool:** the model picks `bash grep` when a dedicated `grep` tool exists, or `bash cat` when `read` exists, because both are always-on and their docs overlap
- **Tool-as-ritual:** a tool is called every turn without moving the task forward (e.g., re-listing directories)
- **Schema bloat:** multiple tools with similar signatures compete for the model's attention
- **Forgotten tools:** tools nobody's used in weeks but still in the prompt
- **Dangerous tools available by default:** `bash`, `curl`, `write` loaded for tasks that only need `read`

The minimal always-on set is the smallest set such that the agent's common tasks can be completed without loading additional tools. Everything else is loaded on demand when a specific task needs it.

## INPUTS
Ask the user for:

1. **Agent's job** — one sentence. What this agent is for.
2. **Current tool list** — every tool currently available, including builtin tools (Read, Edit, Write, Grep, Glob, Bash, etc.) and custom / MCP tools.
3. **Recent usage sample** — which tools were called in the last N sessions, how often. If they don't have this, ask them to grep recent traces or estimate.
4. **Common tasks** — 3–5 representative tasks this agent handles.
5. **Dangerous tools present** — shell, write, network, mutating API calls.
6. **On-demand loading capability** — can the environment add tools mid-session (Skill/MCP/lazy) or is the tool set fixed at session start?

## INSTRUCTIONS

1. **For each tool, record observed usage** from the sample: calls per session (median), tasks that used it, tasks that didn't need it. If the user can't produce data, mark NO-DATA and note the risk.

2. **Classify each tool** into one of:
   - **ALWAYS-ON:** used in ≥60% of sessions, or load-bearing for a common task, or only works if loaded at session start
   - **ON-DEMAND:** useful for a narrow subset of tasks; can be loaded when needed
   - **REMOVE:** unused in recent sessions; or its job is covered by another always-on tool; or it's a dangerous tool not needed for this agent's actual work

3. **Check for overlap.** When two tools have overlapping capabilities (e.g., `bash grep` vs dedicated `grep`, `bash cat` vs `read`), keep only one in Always-On. State which and why.

4. **Check for dangerous-by-default.** If `bash`, network access, or write-to-prod is Always-On, confirm every common task truly needs it. Move to On-Demand if not.

5. **Produce the minimized always-on set** as a shipped list. For each tool: one-sentence justification tied to a common task, any sub-restrictions, and the estimated token cost of its schema.

6. **Produce the on-demand plan.** For each On-Demand tool: which trigger loads it, from where, and when it's unloaded (if ever).

7. **Verify the minimized set is sufficient.** Walk each of the 3–5 common tasks and confirm the always-on set can complete it. If a task requires a tool not in Always-On and not loadable on demand, add it back with a note.

8. **List removals.** For each Remove tool: the reason, the last time it was useful (if ever), and what replaces it (or "nothing, task hasn't recurred").

## FALSE-POSITIVE PREVENTION (MUST follow)
- Do NOT keep a tool Always-On because "we might need it someday." Move it to On-Demand with a named trigger.
- Do NOT classify as ALWAYS-ON without citing at least one common task that needs it.
- Do NOT keep two tools that can replace each other both in Always-On. Overlap causes wrong-tool picks.
- Do NOT remove a tool without naming its replacement or the task that no longer needs to happen.
- Do NOT leave `bash` Always-On with no denylist. If it's Always-On, it must have a command denylist.
- Do NOT treat NO-DATA tools as safe. Flag them explicitly and recommend a short observation window before classification.
- Do NOT add tools during the audit. This prompt only classifies the tools already in scope. Adding tools is a separate design task.
- DO estimate per-tool schema token cost. If a tool adds >500 tokens to the system prompt, its frequency of use had better justify it.
- DO name what the agent cannot do anymore after removals. If that list includes anything the user cares about, revisit.

## OUTPUT FORMAT

### Usage Sample Summary
- Sessions audited: 
- Tasks covered: 
- Data quality: [observed / estimated / NO-DATA]

### Tool Classification
| Tool | Usage (sessions) | Common task coverage | Overlaps with | Classification | Reason |
|------|------------------|----------------------|---------------|----------------|--------|
| | | | | ALWAYS-ON / ON-DEMAND / REMOVE | |

### Minimized Always-On Set
1. **[Tool]** — justification (common task): — sub-restrictions: — schema token cost: 
2. ...
Total always-on schema cost: [tokens]

### On-Demand Plan
| Tool | Trigger to load | Source (Skill / MCP / plugin) | Unload condition |
|------|-----------------|-------------------------------|------------------|
| | | | |

### Removals
| Tool | Last used | Replacement | Capability lost (if any) |
|------|-----------|-------------|--------------------------|

### Sufficiency Check
For each common task, confirm always-on tools + on-demand triggers cover it:
| Task | Always-On tools used | On-demand needed | Covered? |
|------|---------------------|------------------|----------|
| 1 | | | Y/N |

If any row is N, revise.

### Sanity Checklist
- [ ] Every Always-On tool has a cited common task
- [ ] No two overlapping tools are both Always-On
- [ ] Dangerous tools in Always-On have a denylist
- [ ] Every common task is covered by Always-On + On-Demand
- [ ] No tool classified without usage data or explicit NO-DATA flag

## IMPORTANT
- Smaller is better. Default skepticism toward Always-On status.
- Overlap is a silent failure mode — it rarely causes a clear error; it just makes the agent slower and less consistent.
- Schema tokens are spent on every call. A tool used twice a week is not worth its ongoing tax.
```

**Techniques Used:**
- ST-01 (Clear Objective Statement) — output is a classified tool table and a shipped always-on set, not a philosophy of tools
- ST-02 (Structured Sequential Instructions) — 8 steps force usage sample → classification → overlap check → sufficiency proof
- RT-02 (Multi-Dimensional Analysis) — each tool evaluated against usage, overlap, danger, and schema cost
- CM-02 (Constraint Specification) — Must / Must Not blocks the "keep it in case we need it" bias
- DS-06 (Prioritization Guidance) — classification thresholds (≥60% of sessions) make the always-on cut explicit
- QA-01 (Chain-of-Verification) — sufficiency check walks common tasks against the minimized set before shipping
