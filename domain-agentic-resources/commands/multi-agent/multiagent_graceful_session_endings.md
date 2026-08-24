---
name: multiagent_graceful_session_endings
description: "Design a session-end protocol: what to checkpoint, what to discard, what the next session needs to restart productively. Prevents lost context and wasted restart time."
version: "1.0.0"
category: multi-agent
tags: [endings, graceful, multi-agent, multiagent, session]
agents_used: []
title: "Graceful Session Endings: Checkpoint and Restart Design"
techniques:
  - ST-01
  - ST-02
  - CM-02
  - RT-11
  - DD-04
  - QA-08
difficulty: intermediate
updated: "2026-04-20"
related_prompts:
  - domain-agentic-resources/commands/multi-agent/multiagent_worker_isolation_boundaries.md
  - domain-agentic-resources/commands/multi-agent/multiagent_good_enough_gate_design.md
  - domain-engineering-workflows/ai-patterns/ai_pattern_agent_work_loop_design.md
---
# Graceful Session Endings: Checkpoint and Restart Design

**Purpose:** Long-running agent sessions eventually end — context window fills, the day ends, the process crashes, the task hits a convergence gate. How the session ends determines whether the next session picks up in seconds or wastes its first hour reconstructing state. This prompt produces a checkpoint-and-restart protocol specific to the agent's task, naming what to save, what to discard, and what the restart prompt must include.

**When to use:**
- An agent regularly runs long enough that context window, credit budget, or time forces a stop
- Restarts currently require re-reading large swaths of a repo or re-explaining the task
- A multi-agent system needs to persist coordination state across sessions
- An agent keeps "forgetting" decisions made in prior sessions
- You want to design session boundaries deliberately instead of letting them happen abruptly

**What you'll get:** A checkpoint spec (what to save, in what format, where), a discard list (what not to save, and why), a restart prompt template, and a "first 5 minutes after restart" checklist.

---

```
## ROLE
You design the session-end and session-start protocol for an agent (or multi-agent system). You do not design the task itself. You define what gets persisted between sessions, in what format, and what the agent reads first when it resumes.

## CONTEXT
Sessions end for one of four reasons:

1. **Convergence** — the task is done; the session ends on success
2. **Hard limit** — context window / credit / time cap hit; the task is unfinished
3. **Soft pause** — human stops the session to review or to context-switch
4. **Failure** — a tool error, an escalation, a crash

The checkpoint strategy is different for each:

- Convergence should leave only a short final note and the artifacts
- Hard limits need enough state for the next session to pick up *without re-discovering context*
- Soft pauses need the same, plus whatever the human wants to review
- Failures need the partial state plus the failure reason and the proposed resolution

Bad checkpoints take two forms:
- **Too little:** next session starts from scratch; loses expensive exploration
- **Too much:** next session re-reads 20k tokens of stale transcript before it can do useful work

A good checkpoint answers: "what can't be reconstructed from the code, the plan, and the task description?" Everything else is redundant.

## INPUTS
Ask the user:

1. **Task type** — what the agent does across a session (coding task, research task, multi-step workflow, ongoing maintenance).
2. **Typical session lifespan** — minutes / hours / days.
3. **What ends sessions currently** — context window? deliberate stop? crash? all of the above?
4. **What restarts currently look like** — how much reconstruction happens, what gets lost, how long until the agent is productive.
5. **Persistence mechanism available** — file in repo, external store, database, scratchpad, memory MCP, git notes, etc.
6. **Who reads the checkpoint** — same agent, different agent (multi-agent), human, all three.

## INSTRUCTIONS

1. **Enumerate the four end states** (Convergence / Hard limit / Soft pause / Failure) and, for this task, note which happen in practice. Skip end states that don't occur.

2. **For each occurring end state, define the checkpoint.** Each checkpoint contains:
   - **What to save** — a specific, named list (plan / progress / decisions / open questions / artifacts / last-known-good commit / tool state / whatever is task-specific)
   - **What to discard** — transcript chatter, reasoning that didn't pan out, tool output that's recoverable, duplicated data
   - **Format** — structured (JSON/YAML/markdown table) over prose; prose only where nuance matters
   - **Location** — where in the repo or external store, with naming convention
   - **Author** — which agent writes it (the working agent itself, or a summarizer agent)

3. **Design the restart prompt.** What does the next session read first? Order matters:
   - Task description (from the task file, not reconstructed)
   - Plan (from the planner's last output)
   - Checkpoint (compressed: what's been done, what's open, key decisions)
   - Pointer to full history if needed — but do not auto-load it
   
   The restart prompt should fit under a fixed size (e.g., 3–5k tokens) so the next session has headroom.

4. **Specify the "first 5 minutes" checklist** — what the resuming agent does before it touches anything:
   - Verify checkpoint is current (timestamp, hash of plan file, pointer to HEAD commit)
   - Confirm task is still valid (task file exists, not obsoleted by a newer task)
   - Sanity check: are there open file locks / running processes / pending approvals from the prior session?
   - Produce a one-sentence resume report for the human

5. **Handle staleness.** Checkpoints rot. Define:
   - How long a checkpoint is considered fresh (minutes / hours / days)
   - What happens when a stale checkpoint resumes (revalidate, replan, or escalate)
   - How partial work is reconciled if the underlying code changed between sessions

6. **Specify checkpoint invariants.** E.g., "every checkpoint names the next action," "every checkpoint includes a pointer to a git commit or a file-hash set," "no checkpoint exceeds 2k tokens."

7. **List what is never checkpointed.** Tool output that's recoverable, secrets, full transcripts, old plans superseded by newer ones. The discard list prevents checkpoint bloat.

## FALSE-POSITIVE PREVENTION (MUST follow)
- Do NOT design a checkpoint that requires the next session to parse an unbounded transcript. If the transcript is the checkpoint, there is no checkpoint.
- Do NOT omit the "what to discard" list. Without it, checkpoints grow until they cost more than the work they preserve.
- Do NOT save raw tool output that can be regenerated. Save the decision, not the evidence.
- Do NOT save secrets (API keys, tokens, PII) in a checkpoint that will be committed or shared.
- Do NOT let the working agent write its own checkpoint without a format constraint. Structured fields only; free-form prose is where drift hides.
- Do NOT assume the restarting agent is the same model as the writing agent. Checkpoints must be readable by any agent in the system and, ideally, by a human.
- Do NOT omit the staleness handling. A 3-day-old checkpoint resuming on a changed codebase without revalidation is a footgun.
- DO include "next action" in every checkpoint. Without it, the resuming agent spends the first minutes deciding, not doing.
- DO include a pointer to the task file / plan file rather than copying them. Copies go stale.

## OUTPUT FORMAT

### End States in Scope
- [ ] Convergence
- [ ] Hard limit
- [ ] Soft pause
- [ ] Failure

### Checkpoint Specification (per end state)
For each end state in scope:

**End state: [name]**
- **What to save:** [named list]
- **What to discard:** [named list]
- **Format:** [JSON / YAML / markdown table / mixed]
- **Location:** [path + naming convention]
- **Author:** [which agent writes it]
- **Size cap:** [tokens]

### Checkpoint Template (generic)
```
task_id:
plan_ref: (path or commit)
completed:
  - [done item]
open:
  - [pending item]
next_action:
decisions:
  - [decision + rationale]
open_questions:
  - [question]
artifacts:
  - [path / commit / URL]
pointer_to_history: (optional)
written_at:
written_by:
```

### Restart Prompt Template
```
# Resume protocol

1. Read: {task_file}
2. Read: {plan_file}
3. Read: {checkpoint_file}
4. Confirm freshness: {checkpoint.written_at} within {freshness_window}
5. First 5 minutes checklist:
   - [ ] Task still valid
   - [ ] No stale locks / processes
   - [ ] Open questions surfaced to human (if any)
   - [ ] Emit one-sentence resume report

Only after the checklist passes, proceed with `next_action`.
```

### Staleness Handling
- Freshness window: 
- Stale behavior: revalidate / replan / escalate — choose one per end-state
- Revalidation steps (if applicable): 

### Invariants
- Every checkpoint names a next_action
- Every checkpoint ≤ [size cap] tokens
- Every checkpoint references the plan/task by path or commit, not by copy
- [task-specific invariants]

### Never-Checkpoint List
- 
- 

### Sanity Checklist
- [ ] Every end state has a defined checkpoint
- [ ] Discard list is present
- [ ] Next action is mandatory in the template
- [ ] Staleness handling is specified
- [ ] Secrets / PII explicitly excluded
- [ ] Restart prompt fits under the target token budget

## IMPORTANT
- A checkpoint is a contract with the next session. Keep it small, structured, and current.
- "Resume from last message" is not a checkpoint strategy — it's the absence of one.
- If the checkpoint can't fit the content, split the task, not the checkpoint.
```

**Techniques Used:**
- ST-01 (Clear Objective Statement) — output is a session-end protocol, not a general discussion of context management
- ST-02 (Structured Sequential Instructions) — 7 steps force enumeration of end states before checkpoint design
- CM-02 (Constraint Specification) — Must / Must Not blocks the "save the whole transcript" default
- RT-11 (Error Recovery / Rollback) — failure end-state and staleness handling define how the system recovers
- DD-04 (MVP Gates) — the first-5-minutes checklist gates productive work behind verification
- QA-08 (Gate-Based Verification) — invariants section becomes the pass/fail check on any future checkpoint
