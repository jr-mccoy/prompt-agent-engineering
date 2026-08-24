---
title: "Set Up Long-Running Project Memory That Survives Sessions"
category: engineering-workflows/ai-native-rollouts
description: "Design persistent project memory for AI-assisted work that survives across sessions, agents, and tools — so context doesn't have to be rebuilt every time. Produces a concrete file layout, update protocol, read order, and decay checks, not a vague 'use CLAUDE.md' recommendation."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DS-01
  - RT-11
  - QA-01
difficulty: intermediate
tags:
  - ai-native-rollouts
  - memory
  - claude-md
  - persistence
  - context-management
updated: "2026-04-21"
related_prompts:
  - domain-business-strategy/chief-of-staff/cos_memory_scaffold_claude_md.md
  - domain-engineering-workflows/ai-native-rollouts/airollout_delegate_like_parallel_coworker.md
  - domain-engineering-workflows/ai-native-rollouts/airollout_ship_without_writing_code.md
  - domain-prompt-engineering/skill-development/promptcraft_personal_context_document.md
  - domain-prompt-engineering/escape-median/escapemedian_correction_compounder.md
---

# Set Up Long-Running Project Memory That Survives Sessions

**Purpose:** AI sessions are amnesiac. Projects are not. Without persistent memory, every session starts from zero — the user reconstructs context, reminds the AI of decisions, and re-teaches preferences. This prompt produces a concrete memory layout for a specific project: what files exist, what each stores, the update protocol, the read order on a new session, and the decay checks that prevent stale memory from actively misleading future work.

**When to use:**
- A project will run weeks to months across many sessions with AI.
- Multiple AI tools or agents need to share context (IDE copilot, CLI tool, review bot, internal agent).
- The user keeps re-explaining the same decisions, preferences, or domain facts to the AI.
- A team is standardizing project memory practice and needs a template project can adopt.

**Don't use when:** The project is a one-off session. Memory setup cost exceeds value for < ~5 sessions of expected work.

**Audience:** Engineer, PM, or team lead standing up memory for a real project. Output is a file-tree + protocols, ready to commit.

---

## Inputs Required

1. **Project shape.** Code / writing / research / strategy / mixed. Is there a repo? Is it shared across people?
2. **Expected duration and session count.** Weeks, months, or indefinite.
3. **Who accesses the memory.** Solo / team of N / some humans + some AI agents.
4. **AI tools in use.** Claude Code / Cursor / Copilot / API scripts / custom agents. Which tools read which files.
5. **Where files live.** Repo root / shared drive / private scratch. Confidentiality posture matters for what goes where.
6. **What's been lost across sessions so far.** 2–3 specific things the user had to re-explain or reconstruct. This shapes what needs memory.

---

## Instructions

### Step 1 — Separate memory by decay rate

Not all context decays at the same speed. Force the layout to reflect four decay classes:

| Class | Changes | Examples | Typical file |
|-------|---------|----------|-------------|
| **Constitutional** | Rarely — quarterly at most | Project purpose, success definition, non-negotiables | `CLAUDE.md` or `PROJECT.md` root section |
| **Architectural / Structural** | Monthly | Stack, key components, interface contracts, directory map, key glossary | Dedicated section in root memory file, or `ARCHITECTURE.md` |
| **Active state** | Weekly or faster | Current work, open questions, recent decisions, blockers, what's in flight | `STATE.md` or a dated log (e.g., `state/2026-04-WK17.md`) |
| **Session-local** | Per session | Scratch, transient reasoning, in-progress drafts | Not committed; session-local |

Each class goes in its own file (or clearly-delimited section), read in a defined order. Mixing decay classes in one file is the #1 failure mode.

### Step 2 — Define the file layout

Produce a concrete file tree. Minimum viable layout:

```
<project root>
├── CLAUDE.md              # Constitutional + pointers to other files. Read first.
├── ARCHITECTURE.md        # Structural (or as section of CLAUDE.md for small projects)
├── STATE.md               # Active state, updated by whoever ends a session
├── decisions/
│   ├── 2026-04-10-auth-provider.md
│   └── 2026-04-14-rename-user-type.md
└── state/                 # Optional. Dated state snapshots for history.
    └── 2026-04-WK17.md
```

Customize based on input 1 (non-code projects may have `BRIEF.md` instead of `ARCHITECTURE.md`). Non-code projects still need all four decay classes.

### Step 3 — Specify contents per file

Per file, define what goes in and — critically — what does NOT.

- **CLAUDE.md (Constitutional, ≤ 1 page):**
  - Project purpose in 2 sentences.
  - Definition of success (observable).
  - Non-negotiables (coding conventions, tone, compliance).
  - Pointers: "For architecture see ARCHITECTURE.md. For current state see STATE.md."
  - Does NOT contain: current work, specific task detail, meeting notes.

- **ARCHITECTURE.md (Structural):**
  - System or content map.
  - Key contracts (APIs, schemas, terminology, audience definitions).
  - Known constraints.
  - Does NOT contain: rationale for every past decision (that goes in `decisions/`), current sprint.

- **STATE.md (Active):**
  - What's in flight, by whom (human or agent).
  - Open questions blocking progress.
  - Recent decisions (last ~2 weeks, with pointer to full record in `decisions/`).
  - Next 3 things.
  - Does NOT contain: architecture, philosophy, completed work older than ~2 weeks.

- **decisions/YYYY-MM-DD-short-slug.md:**
  - One file per decision, small (< 1 page).
  - Context, options considered, decision, who decided, date.
  - Never edited after write — new decisions supersede old ones (new file + cross-link).

### Step 4 — Define the update protocol

Memory rots if updates are ad hoc. Specify:

- **End-of-session update:** Whoever ends a session (human or agent) updates `STATE.md` with a short "What changed this session" block. Forced protocol; not optional.
- **Decision capture:** Any decision the AI or user makes that will affect future sessions goes in a dated file in `decisions/`. Format is fixed (step 3).
- **Constitutional edits:** Rare; require a comment at the top of `CLAUDE.md` with the date and reason.
- **Architectural edits:** Monthly review or on any change that invalidates a section. Date the section edit at the bottom of the section.

Name the owner (human) for each update type. If solo, the user is the owner.

### Step 5 — Define the read order on a new session

When a new AI session starts, the order of reads matters. Prescribe it:

1. `CLAUDE.md` (always).
2. `STATE.md` (always).
3. Relevant `decisions/` files as pointed to from STATE.md.
4. `ARCHITECTURE.md` sections relevant to the task.

Do NOT default to "read everything." Large memory becomes expensive and noisy. The read order is task-adaptive but always starts with CLAUDE + STATE.

For tools that auto-load CLAUDE.md (Claude Code), ensure its pointers are accurate. For tools that don't auto-load, the first user message should reference the relevant files explicitly.

### Step 6 — Define decay checks

Stale memory is worse than no memory — it actively misleads. Name:

- **Weekly STATE.md audit:** On a scheduled day, the owner re-reads STATE.md. Flag any in-flight item > 2 weeks old as stale; either reactivate or archive.
- **Monthly ARCHITECTURE.md audit:** Check the sections still match reality. Annotate or edit any section that drifted.
- **Decision deprecation check:** A superseded decision stays in `decisions/` but gets a `Superseded by YYYY-MM-DD-other.md` header added at the top when replaced.
- **CLAUDE.md quarterly check:** Does it still describe the project? If not, edit.

If audits aren't named on a schedule, they don't happen. Pick a day or a trigger.

### Step 7 — Handle multi-agent / multi-tool access

If multiple tools or agents read the memory (input 4), specify:

- Which tool reads which files by default.
- Whether writes go to the same files (yes, preferably) or tool-scoped scratch.
- Conflict resolution: if two agents edit STATE.md concurrently, one wins and the other re-reads.
- What's NOT in shared memory (secrets, personal preferences that don't belong in the project's memory).

For solo use, this step is a short note.

### Step 8 — Handle the "memory is leaking PII or secrets" risk

If the project has any sensitive data (input 5), explicitly state what does NOT go in memory:

- Credentials (secrets manager, not memory).
- Customer PII unless the project is explicitly sanctioned to hold it.
- Internal discussions that shouldn't be in a shared or committed file.
- Information that must be fresh at every use (e.g., live account balances).

Add a pre-commit check or a written protocol.

### Step 9 — Verify and output

Run the verification checklist.

---

## Constraints

### Must
- Separate memory into four decay classes (Constitutional, Structural, Active, Session-local).
- Produce an explicit file layout with naming conventions.
- Define what goes in each file AND what does NOT.
- Define an end-of-session update protocol.
- Name the read order on a new session.
- Schedule decay audits with specific owners.

### Must Not
- Mix decay classes in one file.
- Make memory a single growing log. Append-only monoliths become noise.
- Omit the "what does NOT go in" list per file. Without it, files rot.
- Leave audit cadence unscheduled.
- Let constitutional content depend on state that changes weekly.

---

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Dump meeting notes into CLAUDE.md — they have daily decay and belong in STATE.md or a note file.
- Replace ARCHITECTURE.md with a 50-page doc. If it's huge, the AI will skim or hallucinate. Break into sections.
- Leave decisions unrecorded because "the AI will remember." It won't.
- Let a single STATE.md grow unboundedly. Archive weekly to `state/YYYY-MM-WKNN.md` if useful, or trim.
- Confuse personal context with project context. Personal prompts preferences go elsewhere (see `promptcraft_personal_context_document.md`).

✅ **DO:**
- Test the layout on a second AI session: can the AI, reading only CLAUDE.md + STATE.md, restate the project purpose, current work, and next steps correctly? If not, the memory is broken.
- Force yourself to update STATE.md at session end even if tired. Missed updates compound.
- Make decisions/ files immutable once written. Supersede, don't edit.
- Include pointers (not content) from CLAUDE.md to specialized files. Keeps CLAUDE.md short.
- Log the "what changed this session" block even if the change is "nothing advanced." That's a signal in itself.

---

## Dual-Failure Prevention (QA-20)

❌ **HARMFUL failure:** Memory contains stale architecture that the AI reads and trusts; AI generates work against a model that no longer matches reality; bugs ensue.

❌ **UNHELPFUL failure:** Memory protocol is so heavy the user never updates it; three sessions in, memory is stale, user writes the memory off.

✅ **Quality check:** A new AI session, given only this layout and its contents, can produce a correct "here's where we are, here's what's next" summary within its first minute.

---

## Output Format

```markdown
# Project Memory Layout — [Project Name]

## File Tree
[Concrete tree with filenames]

## Per-File Contents
### CLAUDE.md
- Contains: [list]
- Does NOT contain: [list]
- Max size: [~1 page]

### ARCHITECTURE.md
- Contains: [list]
- Does NOT contain: [list]

### STATE.md
- Contains: [list]
- Does NOT contain: [list]
- Max size: [~1 page; archive weekly if longer]

### decisions/YYYY-MM-DD-short-slug.md
- Contains: [list]
- Immutable after write.

## Update Protocol
- End-of-session STATE.md update: [owner, format]
- Decision capture: [trigger, template]
- Constitutional edits: [who, comment required]
- Architectural edits: [cadence, dated annotations]

## Read Order (New Session)
1. CLAUDE.md
2. STATE.md
3. Relevant decisions/
4. Relevant ARCHITECTURE.md sections

## Decay Audits
| File | Cadence | Owner | Trigger |
|------|---------|-------|---------|
| STATE.md | Weekly | | |
| ARCHITECTURE.md | Monthly | | |
| decisions/ | On supersede | | |
| CLAUDE.md | Quarterly | | |

## Multi-Agent / Multi-Tool Access (if applicable)
- [Who reads what]
- [Write conflicts]
- [Not shared]

## Sensitive Data Rules
- Not in memory: [explicit list]
- Pre-commit check: [named tool / protocol]

## Two-Session Test
- [ ] New session can read CLAUDE.md + STATE.md and correctly state purpose, current work, next 3 items.
```

---

## Verification

- [ ] Four decay classes are represented in separate files or clearly-delimited sections.
- [ ] Each file has a "contains" AND a "does NOT contain" list.
- [ ] Update protocol names specific owners and triggers.
- [ ] Read order is explicit.
- [ ] Decay audits are scheduled with owners.
- [ ] Sensitive data exclusion list exists where relevant.
- [ ] Layout passes the two-session test mentally before shipping.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Output is a file tree + protocols, not a philosophy of memory.
- **ST-02 (Structured Sequential Instructions):** Nine steps from decay classification → layout → contents → update → read order → audits → multi-agent → secrets → verify.
- **CM-02 (Constraint Specification):** Must Not block forbids monolithic memory and unscheduled audits.
- **DS-01 (Framework Application):** Four-class decay-rate framework is the spine.
- **RT-11 (Error Recovery):** Decay audits are the recovery mechanism for stale memory; supersede-don't-edit for decisions prevents silent rewrites.
- **QA-01 (Self-Verification):** Two-session test validates the layout actually works before committing to it.
