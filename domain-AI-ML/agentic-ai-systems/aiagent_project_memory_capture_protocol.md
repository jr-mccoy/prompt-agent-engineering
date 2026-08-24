---
title: "Project Memory Capture Protocol"
category: AI-ML/agentic-ai-systems
description: "Design the low-friction write protocol for portable project continuity memory: session summaries, decisions, failed attempts, traps, ideas, open questions, and handoffs."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - QA-01
  - QA-12
difficulty: advanced
tags:
  - project-memory
  - capture-protocol
  - session-handoff
  - decisions
  - failed-attempts
  - continuity
updated: "2026-06-25"
related_prompts:
  - domain-AI-ML/agentic-ai-systems/aiagent_project_continuity_memory_design.md
  - domain-AI-ML/agentic-ai-systems/aiagent_project_memory_guard_before_action.md
  - domain-AI-ML/agentic-ai-systems/aiagent_failure_recovery_rescope.md
  - domain-prompt-engineering/agent-workflows/agent_state_summary_for_compaction.md
  - domain-agentic-resources/commands/multi-agent/multiagent_graceful_session_endings.md
---

# Project Memory Capture Protocol

**Objective:** Design a low-friction protocol for writing durable project memory records so important project state survives sessions without turning memory capture into a second job.

**When to Use:**
- You have already decided the project needs repo-local continuity memory.
- Agents or humans need to record what changed, what was decided, what failed, what remains unresolved, and what the next session should do.
- Existing memory files are stale, inconsistent, too verbose, or missing failed-attempt records.
- A project uses multiple coding agents or work surfaces and needs a common write contract.

**When NOT to Use:**
- You only need to design the overall memory architecture. Use `aiagent_project_continuity_memory_design.md` first.
- The project has no repeated sessions or durable decisions.
- The user wants to archive raw transcripts. This protocol extracts durable state; it does not preserve conversation chatter.

## Inputs / Context

Provide what you can; the protocol degrades gracefully if some are missing:
- **Memory layout:** existing or proposed `.project-memory/` tree.
- **Record types in scope:** sessions, decisions, attempts, traps, ideas, open questions, evidence, handoffs.
- **Who writes memory:** human, working agent, summarizer agent, CLI, hook, MCP server, or mixed.
- **Session boundaries:** when sessions usually end: done, pause, context limit, failure, tool crash, branch switch, or handoff.
- **Friction budget:** maximum time or token budget tolerated for session-end capture.
- **Review policy:** which memory writes can be agent-authored and which require human review.
- **Privacy posture:** what may be committed, what stays local, and what must never be recorded.

## Constraints

**Must:**
- Define capture triggers for session, decision, failed attempt, trap, idea, open question, recovery, and handoff records.
- Keep capture friction low: the protocol must include a minimal path that takes under 90 seconds for routine session end.
- Require typed records with status, timestamp, source, agent/human author, branch/commit when applicable, confidence, privacy, and evidence.
- Distinguish durable records from generated projections such as resume packets or indexes.
- Define promotion rules: when a session note becomes a decision, attempt, trap, or open question.
- Define review rules for high-impact memory writes that could steer future agents.

**Must Not:**
- Let the working agent write unbounded free-form prose as the only checkpoint.
- Record recoverable tool output, full transcripts, secrets, credentials, or PII into committed memory.
- Mix every memory type into one append-only log as the only source of truth.
- Treat a session summary as a decision record unless it contains the decision, rationale, status, and evidence.
- Require perfect curation before capture; rough typed records beat forgotten context.

**Instructions:**

1. **Map capture events.** List the events that should trigger memory writes: session end, material decision, failed attempt, recurring trap, unresolved question, useful idea, failure recovery, branch handoff, and completed milestone.

2. **Define record ownership.** For each record type, decide who can write it, who reviews it, and what status is assigned by default. Flag high-impact records that require human review before future agents rely on them.

3. **Design the minimal capture path.** Specify the fastest acceptable session-end flow: what changed, next action, blockers, files touched, tests/commands run, and whether any decision/attempt/question/trap should be promoted.

4. **Design typed record templates.** For each durable record type, define required frontmatter and body sections. Include one-file-per-record naming conventions for decisions, attempts, sessions, and ideas.

5. **Define promotion rules.** Specify when information moves from a session note into a durable record: decision, failed attempt, trap, open question, or idea. Prevent important facts from being buried only in session history.

6. **Define update rules.** State which files may be edited in place (`current.md`, `handoff.md`, indexes) and which should be immutable or superseded (`decisions/`, `attempts/`), with status changes rather than silent rewrites.

7. **Define evidence rules.** Require durable records to point to commits, files, tests, logs, PRs, issues, docs, or explicit human statements. If evidence is missing, mark confidence low or status unreviewed.

8. **Define privacy and redaction rules.** Specify how the writer handles secrets, PII, local-only notes, proprietary client data, and private user preferences. Include where local-private notes live and how they are gitignored.

9. **Define branch/worktree handling.** Require branch, commit, dirty files, and related PR/issue when applicable. Define warning behavior when resuming from memory written on another branch.

10. **Define capture verification.** Produce checks that catch missing `next_action`, missing evidence, unreviewed high-impact records, stale handoff, oversize session summaries, and secret-like strings.

**Output Format:**

Produce a markdown capture protocol:

- **Capture Events** - table: Event | Trigger | Record type | Required write | Optional promotions.
- **Writer & Review Policy** - who may write, who reviews, default status, human-review triggers.
- **Minimal Session-End Capture** - under-90-second field list and template.
- **Record Templates** - frontmatter + body sections for session, decision, attempt, trap, idea, question, and handoff.
- **Promotion Rules** - when session facts become durable records.
- **Update & Supersession Rules** - edit-in-place vs immutable/superseded records.
- **Evidence Rules** - required and acceptable evidence by record type.
- **Privacy & Redaction Rules** - repo-safe, private, and never-store handling.
- **Branch/Worktree Rules** - branch, commit, dirty files, PR/issue, mismatch behavior.
- **Verification Checks** - pass/fail checks for the capture protocol.

## Verification

- [ ] Every important memory type has a trigger and a typed record template.
- [ ] Routine session-end capture can be completed quickly.
- [ ] Durable decisions and failed attempts cannot hide only inside session summaries.
- [ ] Each durable record has status, author/source, timestamp, confidence, privacy, and evidence.
- [ ] High-impact agent-authored memory requires review before being trusted.
- [ ] Secrets, PII, and local-only notes have explicit handling.
- [ ] Branch and commit context are captured for code projects.
- [ ] Supersession and stale marking are specified instead of silent history edits.

## False-Positive Prevention

❌ **DON'T:**
- Save the entire transcript and call it memory.
- Let session capture become so elaborate the user stops doing it.
- Bury a failed attempt in `sessions/` where no future guard check will find it.
- Let an agent create a project-wide rule from one shaky observation.
- Promote sensitive local notes into committed memory by default.

✅ **DO:**
- Capture now, refine later, but keep the record typed.
- Promote decisions, attempts, traps, and open questions out of session summaries.
- Make failed attempts easy to write and easy to retrieve.
- Use status, confidence, and evidence to prevent false authority.
- Keep generated projections separate from source records.

## Example Output

```markdown
## Minimal Session-End Capture
- Session title: Auth middleware tenant fix
- Branch/commit: feature/auth-tenancy @ abc1234
- Changed: patched tenant resolver lookup and added failing regression test
- Commands: npm test -- auth.middleware.test.ts (1 failing, expected)
- Decisions: none
- Attempts to promote: attempted full middleware rewrite, failed due to tenant context loss
- Open questions: whether legacy session cookie path still matters
- Next action: make tenant resolver test pass without changing cookie parser

### Attempt Template
---
id: att_20260625_auth_rewrite
type: attempt
title: Full auth middleware rewrite
status: failed
created_at: 2026-06-25T18:10:00-05:00
agent: claude-code
branch: feature/auth-tenancy
commit: abc1234
confidence: high
privacy: repo-safe
tags: [auth, tenancy]
evidence:
  - type: test
    ref: npm test -- auth.middleware.test.ts
---

### Problem
Tenant context was lost during middleware rewrite.

### Tried
Replaced resolver and cookie parser in one patch.

### Result
Regression test failed; tenant id became undefined on legacy cookie path.

### Do not retry unless
Parser behavior is isolated first and legacy cookie tests pass.
```

**Techniques Used:**
- **ST-01 (Clear Objective Statement):** narrows the prompt to memory writing, not overall architecture.
- **ST-02 (Structured Sequential Instructions):** event map → ownership → templates → promotion → verification.
- **ST-03 (Output Format Specification):** forces a concrete protocol and templates.
- **CM-02 (Constraint Specification):** blocks transcript archives and high-friction capture rituals.
- **QA-01 (Self-Verification):** verifies triggers, required fields, and safety handling.
- **QA-12 (False Positives Identification):** catches memory that looks useful but cannot be trusted or found later.

**Related Prompts:**
- `aiagent_project_continuity_memory_design.md` — overall portable project memory architecture.
- `aiagent_project_memory_guard_before_action.md` — uses captured decisions, attempts, and traps before future work.
- `multiagent_graceful_session_endings.md` — checkpoint/restart protocol that can feed this capture layer.
