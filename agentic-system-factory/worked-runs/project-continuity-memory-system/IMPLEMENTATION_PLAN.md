# Project Continuity Memory System — Implementation Plan

> **Purpose:** This is the standalone build plan for a portable project continuity memory system. It is written so an AI coding agent or human developer can build the system without knowing the conversation that produced it.
>
> **Important distinction:** This plan is for a standalone, repo-agnostic tool that can be installed into any project. It is **not** a plan to store this repository's own project memory inside `Prompting-guides`. The `Prompting-guides` repository is the prompt/workflow library and design forge for the tool.

---

## 1. Product Definition

Build a portable, repo-local continuity system for human-agent software work.

The system stores durable project state as typed, human-readable records inside a target project's `.project-memory/` directory. It helps humans and agents resume work across sessions, tools, devices, branches, and time without re-discovering decisions, repeating failed attempts, or trusting stale context.

### North-star statement

**Project Continuity Memory is a repo-local, human-readable ledger of durable project state: what was decided, what failed, what is active, what is risky, what is unresolved, and what the next agent or human must know before acting. It is not a transcript archive, not a vector database, and not a replacement for source code, tests, current human instruction, or authoritative docs.**

### Working product name

Use one of these names consistently in the implementation repo:

- `continuity-kit` — recommended package/repo name.
- `continuity` — recommended CLI binary name.
- `Project Continuity Memory` — formal capability name.

---

## 2. Non-Goals

Do **not** build these first:

1. **Do not build a vector database as the source of truth.** Vectors can be added later as a disposable search accelerator.
2. **Do not store full chat transcripts as memory.** Extract durable decisions, attempts, handoffs, questions, traps, and evidence.
3. **Do not rely on one vendor's memory feature.** Codex, Claude, Cursor, Gemini, and future agents must all read the same project records.
4. **Do not require MCP, hooks, or a daemon for baseline functionality.** Plain files and CLI must work first.
5. **Do not use `AGENTS.md`, `CLAUDE.md`, or Cursor/Gemini rules as the memory database.** These files should be signposts only.
6. **Do not store secrets, credentials, customer PII, or sensitive local notes in committed project memory.**
7. **Do not make the capture workflow so heavy that humans stop using it.** Routine session capture should take under 90 seconds.

---

## 3. System Principles

1. **Plain files first.** Any agent or human should be able to read `.project-memory/` without a special runtime.
2. **Typed records over transcript sludge.** Memory should be structured enough to validate, search, audit, and guard against.
3. **Generated projections are not source of truth.** Resume packets, indexes, stale reports, FTS databases, and vector stores are rebuildable artifacts.
4. **Memory is advisory.** Current user instruction, code, tests, build output, and authoritative docs outrank memory.
5. **Status beats silent edits.** Use `active`, `superseded`, `stale`, `disputed`, `rejected`, and `quarantined` status instead of quietly rewriting history.
6. **Failed attempts are first-class.** They prevent repeated expensive mistakes.
7. **Branch and commit context matter.** Memory written on another branch may be stale or misleading.
8. **Interop is layered.** Plain files → CLI → agent signposts → MCP → hooks → optional indexes/vectors.
9. **Security is part of memory design.** Memory can be stale, poisoned, private, or executable-adapter-adjacent.
10. **The system must degrade gracefully.** Read-only cloud agents should still benefit from memory files even if CLI/MCP/hooks are unavailable.

---

## 4. Target User Stories

### Solo builder resumes after context switch

As a solo developer juggling multiple projects, I can run:

```bash
continuity resume
```

and see what I was doing, what was decided, what failed, what is unresolved, and what to do next.

### Agent avoids repeating a failed attempt

Before a coding agent rewrites a fragile subsystem, it can run:

```bash
continuity guard "rewrite auth middleware"
```

and receive a warning if a prior failed attempt or active decision says not to repeat that path.

### Claude Code hands work to Codex

At the end of a Claude Code session, memory capture writes a session record and handoff. The next day, Codex reads `.project-memory/handoff.md`, active decisions, and relevant failed attempts before editing.

### Cloud agent with no CLI still works

A cloud agent that cannot run local binaries can still read:

```text
.project-memory/current.md
.project-memory/handoff.md
.project-memory/decisions/
.project-memory/attempts/
.project-memory/known-traps.md
.project-memory/open-questions.md
```

and resume manually.

### Team reviews memory changes in PRs

A team can review changes to `.project-memory/decisions/` and `.project-memory/attempts/` like any other project artifact. High-impact memory changes require human review.

---

## 5. Repository Layout Installed Into Target Projects

The CLI should initialize this directory in any target project:

```text
.project-memory/
  README.md
  manifest.yml

  current.md
  handoff.md
  open-questions.md
  known-traps.md

  decisions/
    .gitkeep

  attempts/
    .gitkeep

  sessions/
    .gitkeep

  ideas/
    .gitkeep

  evidence/
    refs.yml

  generated/
    README.md
    resume-packet.md
    stale-report.md
    memory-index.md

  private/
    README.md

  index/
    README.md
```

### Git tracking policy

Recommended committed paths:

```text
.project-memory/README.md
.project-memory/manifest.yml
.project-memory/current.md
.project-memory/handoff.md
.project-memory/open-questions.md
.project-memory/known-traps.md
.project-memory/decisions/
.project-memory/attempts/
.project-memory/sessions/
.project-memory/ideas/
.project-memory/evidence/refs.yml
.project-memory/generated/README.md
.project-memory/index/README.md
```

Recommended gitignored paths:

```gitignore
.project-memory/private/**
.project-memory/index/**
!.project-memory/index/README.md
.project-memory/generated/*.local.md
.project-memory/generated/*.tmp
```

### Tracking policy chosen at `init`

Two tracking decisions are set when `continuity init` runs and recorded in `manifest.yml` (§7) so every later command stays consistent:

1. **Generated Markdown projections** (`generated/resume-packet.md`, `generated/stale-report.md`, `generated/memory-index.md`) are **committed by default** (`commit_generated_projections: true`). This directly serves the "cloud agent with no CLI" user story (§4): a read-only agent gets a pre-built catch-up file. Each projection carries a source commit/hash header so staleness is visible (§15). A project that prefers a clean history can flip this to ignore them. **SQLite and vector indexes (`index/**`) are always ignored**, regardless of policy.

2. **Session records** (`sessions/`) follow a **user-chosen policy** captured at `init`:
   - `session_tracking: full` — commit dated session records, so handoffs and history travel across people and devices.
   - `session_tracking: distillate` — `sessions/` stays local (gitignored); only promoted `decisions/` and `attempts/` are committed, keeping the shared repo lean.

   `init` prompts for this (or accepts `--session-tracking <full|distillate>`) and writes the matching `.gitignore` rules. There is no universal right answer — solo multi-device work favors `full`; large team repos often favor `distillate`.

---

## 6. Memory Record Taxonomy

| Type | Purpose | Path | Lifespan | Source of truth? |
|---|---|---|---|---|
| Current state | What matters right now | `.project-memory/current.md` | days to 2 weeks | yes |
| Handoff | What the next session should do first | `.project-memory/handoff.md` | until resumed or superseded | yes |
| Decision | What was decided, rejected, and why | `.project-memory/decisions/YYYY-MM-DD-slug.md` | long-lived | yes |
| Attempt | What was tried, outcome, and do-not-retry condition | `.project-memory/attempts/YYYY-MM-DD-slug.md` | long-lived if instructive | yes |
| Trap | Reusable warning about fragile areas | `.project-memory/known-traps.md` or future `traps/` | long-lived, reviewed | yes |
| Open question | Unresolved ambiguity or blocker | `.project-memory/open-questions.md` | until resolved | yes |
| Idea | Potential future direction | `.project-memory/ideas/YYYY-MM-DD-slug.md` | reviewed periodically | yes |
| Session | What happened in one work session | `.project-memory/sessions/YYYY-MM-DD-tool-topic.md` | historical | yes, but lower priority |
| Evidence | Pointers to commits, tests, docs, issues, PRs | `.project-memory/evidence/refs.yml` | as long as referenced | yes |
| Private note | Local-only personal/sensitive context | `.project-memory/private/` | local policy | local-only |
| Resume packet | Bounded generated boot summary | `.project-memory/generated/resume-packet.md` | regenerated | no |
| Search index | FTS/vector/cache | `.project-memory/index/` | regenerated | no |

---

## 7. Canonical Metadata Schema

Every durable record should use Markdown with YAML frontmatter.

Required frontmatter for durable records:

Concrete values below are illustrative. Tokens in `<angle brackets>` are placeholders an implementation fills — never literals to copy (e.g. do not emit `abc1234` as a default commit).

```yaml
# id and slug are DERIVED from the filename, not authored by hand. See "Record identity" below.
id: dec_20260625_repo-local-memory-source-of-truth   # computed: <type-prefix>_<YYYYMMDD>_<slug>
type: decision
slug: repo-local-memory-source-of-truth              # the human segment of the filename
title: Use repo-local Markdown as source of truth
status: active              # active | superseded | stale | disputed | rejected | quarantined
created_at: 2026-06-25T14:30:00-05:00
updated_at: 2026-06-25T14:30:00-05:00
created_by: <username>      # human username or agent label, auto-derived
agent: human                # human | claude-code | codex | cursor | gemini | opencode | other
project: <project-name>     # auto-derived from repo/dir name
scope: project              # project | feature | branch | local | private
branch: <current-branch>    # auto-derived from git HEAD
commit: <short-sha>         # auto-derived from git HEAD
dirty_files: []             # auto-derived from git status
confidence: medium          # low | medium | high   (default: medium)
privacy: repo-safe          # repo-safe | local-private | secret-prohibited   (default: repo-safe)
review_status: unreviewed   # unreviewed | reviewed | needs-review   (default: unreviewed)
reviewed_by: null
supersedes: []
superseded_by: null
expires_at: null
tags:
  - memory
  - architecture
evidence:
  - type: commit
    ref: <short-sha>
  - type: command
    ref: npm test
```

### Record identity

Identity is **filename-canonical**. The file's path is the single source of truth; `id` and `slug` are computed from it and never stored as an independent authority.

- Filename pattern for directory records: `<YYYY-MM-DD>-<slug>.md` (e.g. `decisions/2026-06-25-repo-local-memory-source-of-truth.md`).
- `slug` = the human segment of the filename (everything after the date).
- `id` = `<type-prefix>_<YYYYMMDD>_<slug>`, where the type-prefix is `dec` / `att` / `idea` / `ses` / `trap` / `q`.

Why filename-canonical: the filesystem physically cannot hold two files with the same name in one directory, so ID uniqueness (§16.4) is enforced for free and the three-way drift between id, slug, and filename cannot occur. `validate` recomputes `id`/`slug` from the filename and flags any frontmatter that disagrees rather than trusting the stored value.

### Field population — keeping capture under 90 seconds

The capture budget (§2.7, §23) is a design constraint, not a hope. Most fields are machine-filled so a human is asked for almost nothing.

| Population | Fields | Source |
|---|---|---|
| **Auto-derived** | `id`, `slug`, `created_at`, `updated_at`, `created_by`, `agent`, `project`, `branch`, `commit`, `dirty_files` | filename, system clock, git, environment |
| **Defaulted** (overridable) | `status: active`, `confidence: medium`, `privacy: repo-safe`, `review_status: unreviewed`, `scope: project`, `tags: []`, `supersedes/superseded_by/expires_at: null` | constants |
| **Prompted** (human/agent supplies) | `title`, the record body sections, optionally `tags` and `evidence` | interactive input |

A routine `remember`/`capture` should require only a title and a few body lines; everything else is derived or defaulted.

### Manifest

`.project-memory/manifest.yml` is the per-project control file. It carries the schema version (so `validate` can check forward-compat, §16.1) and the tracking policies chosen at `init` time, so every later command behaves consistently with how the project was set up.

```yaml
schema_version: 1
created_at: 2026-06-25T14:30:00-05:00
project: <project-name>
# Tracking policy chosen during `continuity init` (see §5):
session_tracking: full        # full | distillate
#   full       = commit dated session records under sessions/
#   distillate = sessions/ stays local; commit only promoted decisions/attempts
commit_generated_projections: true   # commit generated/*.md summaries (indexes always ignored)
```

`init` writes `.gitignore` rules to match these values, and `audit`/`validate` read them rather than guessing.

### Status meanings

| Status | Meaning |
|---|---|
| `active` | Current and safe to consider. |
| `superseded` | Replaced by a newer record. Must include `superseded_by`. |
| `stale` | Possibly outdated; must be revalidated. |
| `disputed` | Conflicts with another record, code, tests, docs, or user instruction. |
| `rejected` | Considered and intentionally not used. |
| `quarantined` | Suspected unsafe/private/poisoned; do not use for agent guidance. |

### Privacy meanings

| Privacy | Meaning |
|---|---|
| `repo-safe` | May be committed. |
| `local-private` | Must live under `.project-memory/private/` or external private store. |
| `secret-prohibited` | Must not be stored in project memory at all. |

---

## 8. Record Body Templates

### Decision record

```markdown
---
# frontmatter
---

## Context
Why this decision came up.

## Options Considered
- Option A: ...
- Option B: ...

## Decision
What was chosen or rejected.

## Rationale
Why this is the current best choice.

## Consequences
What future work must respect.

## What Not To Retry
Paths that are closed unless conditions change.

## Evidence
Commits, tests, docs, user statements, PRs, issues.

## Stale / Review Conditions
When this decision should be revisited.
```

### Attempt record

```markdown
---
# frontmatter
---

## Problem
What problem the attempt tried to solve.

## Tried
What was attempted.

## Result
What happened.

## Why It Failed / Succeeded
Mechanism, not vibes.

## Do Not Retry Unless
Conditions that would make retry reasonable.

## Evidence
Commands, errors, test output, files, commits.

## Related Records
Decisions, traps, sessions, questions.
```

### Session record

```markdown
---
# frontmatter
---

## Starting Context
What the session began with.

## Work Completed
Observable changes.

## Decisions Made
Links to decision records or `none`.

## Attempts / Failures
Links to attempt records or candidate promotions.

## Open Questions
Links or new questions.

## Files Touched
Paths and purpose.

## Commands / Verification
Commands run and results.

## Next Action
Exactly what the next session should do first.
```

The "Work Completed", "Files Touched", and "Commands / Verification" sections are pre-filled from git (`log`, `status`, `diff --stat` since the last session record) and edited by the human, not authored from scratch. A `--fast` capture writes a minimal session record (git snapshot + "Next Action" only) and defers the narrative sections.

### Handoff file

```markdown
# Project Handoff

_Last updated: YYYY-MM-DDTHH:mm:ssZ_
_Branch: main_
_Commit: abc1234_

## Current Focus

## Next Action

## Blockers / Open Questions

## Active Decisions To Respect

## Failed Attempts To Avoid

## Known Traps

## Likely Relevant Files

## Verification Commands

## Stale If
```

---

## 9. Source-of-Truth Rules

1. Canonical typed records are source of truth.
2. Generated projections are convenience only.
3. SQLite/FTS/vector indexes are disposable.
4. Agent-specific files are signposts only.
5. Memory cannot override:
   - current user instruction,
   - source code,
   - tests,
   - build output,
   - current authoritative docs,
   - security policy.
6. If memory conflicts with reality, mark it `disputed` or `stale` and link evidence.
7. If a decision changes, create a new decision and set the old one to `superseded`.
8. If a failed attempt becomes newly viable, update status or create a new attempt/decision record explaining why conditions changed.

---

## 10. CLI Design

The MVP should provide a CLI named `continuity`.

### MVP commands

```bash
continuity init
continuity resume
continuity capture session
continuity remember decision
continuity remember attempt
continuity guard "<proposed action>"
continuity audit
continuity validate
```

### Later commands

```bash
continuity remember idea
continuity remember question
continuity mark-status <id> <status>
continuity supersede <old-id> <new-id>
continuity build-index
continuity scan-secrets
continuity dashboard
continuity register
continuity where-was-i
```

### Command behavior

| Command | Reads | Writes | Purpose |
|---|---|---|---|
| `init` | project root | `.project-memory/`, `manifest.yml`, optional signposts, `.gitignore` edits | Install memory layout. Prompts for (or accepts `--session-tracking <full\|distillate>`) the session policy and records it + the generated-projection policy in `manifest.yml`. |
| `resume` | current, handoff, records, git state | generated resume packet | Print bounded resume packet. |
| `capture session` | git state (log, status, diff --stat) | session record, handoff, current | Record session end. Auto-fills "Work Completed", "Files Touched", and "Commands" from git (commits + files since the last session record) so the human edits rather than authors from scratch. `--fast` skips prompts and any LLM narrative and writes a git-only snapshot plus a one-line next action (a ~15-second path for a tired human). |
| `remember decision` | git state, user input | decision record | Capture durable choice. |
| `remember attempt` | git state, user input | attempt record | Capture tried path and outcome. |
| `guard` | decisions, attempts, traps, questions, handoff | optional session note | Warn before repeated mistake. |
| `audit` | all memory and adapters | stale report | Find stale/unsafe/bloated memory. |
| `validate` | all canonical files | validation output | Enforce schema and invariants. |

### CLI output style

All commands should support:

```bash
--json
--plain
--verbose
--project <path>
--fast            # capture/resume: git-only, no prompts or LLM narrative (fast path)
```

Default output should be human-readable Markdown/plain text.

---

## 11. MVP Guard-Before-Action Algorithm

The first implementation should not require embeddings.

Inputs:

```text
proposed_action: string
optional files: list[path]
current branch/commit
current task/issue/PR if available
```

Steps:

1. Tokenize action into normalized keywords.
2. Detect action class:
   - routine edit,
   - broad refactor,
   - architecture decision,
   - dependency/tool change,
   - migration,
   - deletion,
   - external side effect,
   - security/permission change.
3. Search exact metadata and text across:
   - active decisions,
   - failed attempts,
   - known traps,
   - open questions,
   - current handoff,
   - stale report.
4. Score matches using:
   - same file path,
   - same tag/component,
   - active/high-confidence/reviewed status,
   - recency (record age and commit-distance since written — older/more-commits-behind weighs lower),
   - branch match,
   - explicit `Do Not Retry Unless`,
   - open blocker keywords.
5. Emit one of:
   - `PROCEED`,
   - `READ_FIRST`,
   - `PAUSE`,
   - `ASK_HUMAN`.
6. Include record IDs, reason, and next safest action.
7. Keep warnings bounded. Default max: 5.

Example output:

```text
PAUSE

Proposed action: Rewrite auth middleware around new session parser.

Relevant memory:
1. att_20260618_auth_middleware_rewrite — failed attempt, same files, high confidence.
2. dec_20260612_tenant_resolver_contract — active decision, same component.
3. trap_auth_legacy_cookie_path — known trap, verification command exists.

Recommended next action:
Read those records. Make a surgical patch and run `npm test -- auth.middleware.test.ts`.
```

---

## 12. Resume Packet Design

`continuity resume` should generate a bounded packet suitable for pasting into any agent.

Default max size: 3,000 to 5,000 tokens.

Contents:

```markdown
# Resume Packet

## Project
Name, path, branch, commit, dirty state.

## Current Focus
From current.md and handoff.md.

## Next Action
Exactly what to do first.

## Active Decisions
Top relevant active decisions with IDs and one-line rationale.

## Failed Attempts To Avoid
Relevant attempts with IDs and do-not-retry condition.

## Known Traps
Relevant traps.

## Open Questions / Blockers
Questions that may require human input.

## Likely Relevant Files
Paths and why.

## Verification Commands
Commands to run before/after work.

## Stale / Risk Warnings
Computed automatically, not just authored:
- Handoff/current age and commit-distance, e.g. "handoff is 6 days old, written 14 commits behind current HEAD." Age + commit-distance is the primary signal that a train of thought has gone cold.
- Aged-unresolved items: open questions and active decisions older than a staleness threshold with no resolution or update since — the "is this still true / did I ever fix this?" signal for plans and audits that have aged out (the long-horizon failure mode where you re-review month-old work without knowing if it was addressed).
- Branch mismatch (§15), expired decisions (`expires_at`), low-confidence records.
```

Do not include raw transcripts.

`continuity resume --fast` prints just the git snapshot, current focus, next action, and the computed staleness warnings — skipping the fuller record summaries — for a quick reorientation.

---

## 13. Agent Interop Design

### Baseline: plain files

Any agent can read `.project-memory/` manually.

### CLI

Any shell-capable agent can run `continuity` commands.

### Agent signpost files

Optional generated files:

```text
AGENTS.md
CLAUDE.md
.gemini/GEMINI.md
.cursor/rules/project-memory.mdc
```

These files must be short. They should point to `.project-memory/` and `continuity` commands.

Example `AGENTS.md` snippet:

```markdown
## Project memory protocol

This project uses `.project-memory/` for project continuity.

Before non-trivial work:
1. Read `.project-memory/current.md`.
2. Read `.project-memory/handoff.md`.
3. Review relevant records under `decisions/`, `attempts/`, `known-traps.md`, and `open-questions.md`.
4. If available, run `continuity guard "<proposed action>"`.

At session end:
1. Run or perform `continuity capture session`.
2. Record durable decisions and failed attempts as typed records.

Memory is advisory. Current user instructions, code, tests, build output, and authoritative docs outrank memory.
```

### MCP later

MCP resources:

```text
memory://current
memory://handoff
memory://resume-packet
memory://decisions
memory://decisions/{id}
memory://attempts/{id}
memory://open-questions
memory://known-traps
```

MCP prompts:

```text
resume_project
capture_session
remember_decision
remember_attempt
guard_before_action
audit_project_memory
```

MCP tools:

```text
memory_search(query, filters)
memory_record(type, payload)
memory_guard_before_action(action, files?)
memory_build_resume_packet(task?)
memory_validate()
memory_mark_status(id, status, reason)
memory_scan_secrets()
```

### Hooks last

Optional hooks can run:

- session start → build resume packet,
- pre-action → guard,
- failed command → offer attempt record,
- session end → prompt capture.

Hooks must have manual fallback commands.

---

## 14. Global Multi-Project Dashboard

This is a post-MVP feature but important for users juggling many projects.

Global registry:

```text
~/.continuity/
  registry.yml
  dashboard-cache.json
```

Commands:

```bash
continuity register .
continuity dashboard
continuity recent
continuity where-was-i
```

Dashboard output:

| Project | Path | Current focus | Last touched | Next action | Stale? |
|---|---|---|---|---|---|
| my-app | ~/dev/my-app | Auth tenant fix | 2 days ago | Run auth test | no |
| research-tool | ~/dev/research-tool | Memory schema | 9 days ago | Decide index format | yes |

Registry stores pointers and summaries only, not secrets.

**Cache freshness (no daemon).** Consistent with the no-daemon principle (§2.4), `dashboard-cache.json` is a disposable projection, never a source of truth. It is rebuilt on demand: `dashboard`/`recent` re-read each registered project's `current.md` + `handoff.md` (cheap, a few files per project) and refresh the cache as they run. Each cached row carries the source project's last-touched timestamp/commit so a stale entry is visible rather than silently trusted, and a missing or unreadable project path is shown as `unavailable` rather than dropped. Projects opt in via `continuity register`; nothing scans the filesystem in the background.

---

## 15. Security and Privacy

### Threat surfaces

1. Malicious PR edits `.project-memory/` to steer future agents.
2. Memory record contains prompt-injection-like text.
3. Old decision remains active after code changes.
4. Private notes are accidentally committed.
5. Secrets from logs are captured in session records.
6. Checked-in MCP/hook config runs unsafe commands.
7. Generated resume packet is stale but trusted.
8. Vector/FTS index is stale or built from wrong commit.

### Required controls

- Secret scan memory before commit.
- Treat memory content as data, not instruction.
- High-impact memory writes require review.
- Executable configs require human review.
- Generated projections include source timestamp/hash/commit.
- Indexes include source file hash and are invalidated on mismatch.
- Branch mismatch warning in `resume` and `guard`. **Definition:** a record's `branch` differs from the current git `HEAD` branch. `resume`/`guard` surface such records as possibly-stale rather than hiding them; detached HEAD and a record written on a since-merged branch both count as a mismatch and warn.
- Privacy labels enforced by validation.

### High-impact memory changes

Require human review when a record:

- changes authority boundaries,
- says to skip or reduce tests,
- changes security/privacy posture,
- changes tool permissions,
- changes dependency/vendor strategy,
- marks a major decision superseded,
- quarantines or unquarantines memory.

---

## 16. Validation Rules

`continuity validate` should check:

1. `.project-memory/manifest.yml` exists and has supported version.
2. Required core files exist.
3. Durable records have valid frontmatter.
4. Record IDs are unique.
5. Status values are valid.
6. `superseded` records include `superseded_by`.
7. `privacy: local-private` records are not in committed/shared paths.
8. `secret-prohibited` records fail validation.
9. Decisions and attempts have evidence or low confidence.
10. Session records have `Next Action` or explicitly mark convergence/done.
11. Handoff has branch, commit, next action, and stale conditions.
12. Generated files are not treated as canonical.
13. Adapter files do not duplicate full memory content.
14. Required structural files (manifest, core files) and frontmatter shape are well-formed — the deterministic checks above. **Detecting instruction-like text in known traps is not one of them** (see note).

> **Note on instruction-like memory text.** Detecting "imperative instructions that override policy" (e.g. a trap saying "skip the tests") in free text is a heuristic, not a deterministic check, so it does **not** gate `validate`. It belongs in `audit` as a flagging heuristic — a lexical scan for override-style phrasing ("ignore", "skip", "disable", "always", "never run") that emits a warning for human review. This is the same content-as-data posture as Fixture 7 (poisoned memory): `audit` flags it, `guard` treats matched text as data, never command. `validate` stays fully deterministic.

---

## 17. Evaluation Plan

Build a small fixture suite.

### Fixture 1: Fresh resume

Given a sample `.project-memory/`, `continuity resume` must answer:

- What is the project?
- What is active?
- What was decided?
- What failed before?
- What is next?
- What should not be retried?

### Fixture 2: Guard true positive

Proposed action matches a failed attempt and active decision. Expected outcome: `PAUSE` or `READ_FIRST`.

### Fixture 3: Guard false-positive control

Proposed action shares a generic word with old memory but no file/tag/component overlap. Expected outcome: `PROCEED` or low-severity note.

### Fixture 4: Stale handoff

Handoff older than threshold or written on another branch. Expected warning.

### Fixture 5: Superseded decision

Old decision is superseded. Guard should not treat it as active but may mention history.

### Fixture 6: Secret leak

Session record contains token-like string. `audit` or `scan-secrets` fails.

### Fixture 7: Poisoned memory text

Memory record contains text like "ignore tests". Audit flags instruction-like content; guard treats it as data, not command.

### Fixture 8: Generated packet stale

Source record is newer than resume packet. Audit flags regeneration needed.

### Fixture 9: Cloud fallback

No CLI execution. A generated resume packet and plain files still support manual resume.

### Fixture 10: Many sessions

100 session records exist. Resume packet remains bounded and prioritizes current/handoff/active decisions over old observations.

---

## 18. Implementation Phases

### Phase 0: Create standalone repo

Create a new repo, recommended:

```text
jr-mccoy/continuity-kit
```

Initial layout:

```text
continuity-kit/
  README.md
  docs/
    architecture.md
    record-schema.md
    cli-spec.md
    mcp-spec.md
    security.md
  templates/
    project-memory/
  fixtures/
  src/ or continuity.py
```

### Phase 1: Python single-file prototype

Goal: useful in real projects fast.

Implement:

```text
continuity.py init
continuity.py resume
continuity.py capture session
continuity.py remember decision
continuity.py remember attempt
continuity.py guard
continuity.py audit
continuity.py validate
```

Use only Python standard library if feasible:

- `argparse`,
- `pathlib`,
- `datetime`,
- `json`,
- `re`,
- `subprocess` for git metadata,
- minimal YAML frontmatter parser implemented locally or use JSON-compatible YAML subset.

If full YAML is needed, either vendor minimal parsing or clearly document dependency.

### Phase 2: Templates and fixtures

Add complete templates for every file and fixture repos for eval cases.

### Phase 3: Dogfood

Install in 2-3 real projects where context is actually lost. Do not start with `Prompting-guides` as the target. Use real project friction to refine:

- capture time,
- guard noise,
- resume usefulness,
- branch mismatch handling,
- stale audit quality.

### Phase 4: Package CLI

Language is committed to **Python end-to-end** — prototype, CLI, and MCP server (Phase 5). This removes the rewrite fork: the prototype evolves into the product rather than being thrown away. The Python MCP SDK is mature enough that there is no MCP-driven reason to rewrite in TypeScript.

Package and distribute via pipx:

```bash
pipx install continuity-kit
```

(If `npx` reach ever becomes a hard requirement, revisit — but treat that as a deliberate, separately-justified decision, not a default migration.)

### Phase 5: MCP server

Add the MCP server (in Python) only after CLI semantics stabilize.

Expose resources, prompts, and tools defined in this plan.

### Phase 6: Hooks and agent adapters

Generate optional:

- `AGENTS.md`,
- `CLAUDE.md`,
- Cursor rule,
- Gemini file,
- `.mcp.json`,
- `.codex/config.toml` snippets,
- hook templates.

Everything must be opt-in and reviewable.

### Phase 7: Search/index acceleration

Add SQLite FTS.

Later, add embeddings/vector index if exact search is insufficient.

Rules:

- index is ignored,
- index stores source file path + hash,
- invalidate on mismatch,
- never treat search result as source-of-truth without opening the canonical record.

### Phase 8: Global dashboard

Add `~/.continuity/registry.yml` and dashboard commands.

---

## 19. Suggested MVP Acceptance Criteria

The MVP ships in two stages so dogfooding (Phase 3) can start as soon as the value loop works, rather than waiting for the full trust toolchain. Build **19a first**, get it into a real project, then build **19b**.

### 19a. MVP-core (the capture → resume value loop)

Ship and dogfood when:

1. `continuity init` creates a valid `.project-memory/` layout and writes `manifest.yml` with the chosen tracking policies.
2. `continuity remember decision` creates a valid decision record.
3. `continuity remember attempt` creates a valid attempt record.
4. `continuity capture session` creates a session record and updates handoff — auto-filling work-completed/files-touched/commands from git — in under 90 seconds of human effort; `continuity capture session --fast` writes a git-only snapshot in under ~15 seconds (§7 field-population budget, §8).
5. `continuity resume` prints a bounded packet with current focus, next action, active decisions, failed attempts, questions, traps, branch/commit, verification commands, and computed staleness warnings (handoff age + commit-distance, aged-unresolved questions/decisions).
6. Fixture 1 (fresh resume) runs in CI.
7. Plain-file fallback works without the CLI.

This is the minimum that delivers value: a human or agent can capture state cheaply and resume cleanly. It is worth installing on its own.

### 19b. MVP-trust (makes the memory trustworthy)

Add after 19a is proven in a real project:

8. `continuity guard` identifies at least exact/tag/file matches against active decisions and failed attempts, with the false-positive control (Fixture 3) passing.
9. `continuity audit` flags stale handoff, missing evidence, invalid statuses, private-path violations, branch mismatch, and generated packet drift.
10. `continuity validate` fails on invalid frontmatter, duplicate IDs (and frontmatter that disagrees with the filename, §7), invalid statuses, or secret-prohibited committed records.
11. Fixtures 2–10 run in CI.

`guard`, `audit`, and `validate` are what let a user *trust* the memory rather than just *use* it — important, but not on the critical path to first value.

---

## 20. Recommended First-Agent Task List

An agent implementing this should follow this sequence:

1. Create standalone repo and README with product definition and non-goals.
2. Add `.project-memory/` templates.
3. Add record schema documentation.
4. Implement `continuity.py init`.
5. Implement frontmatter parsing and record loading.
6. Implement `validate`.
7. Implement `remember decision` and `remember attempt`.
8. Implement `capture session` (with git pre-fill of body sections and a `--fast` git-only tier).
9. Implement `resume` packet generation (including computed age/commit-distance staleness and aged-unresolved flagging).
10. Implement simple exact/text/tag/path search.
11. Implement `guard` with deterministic ranking.
12. Implement `audit` checks.
13. Add fixtures and tests.
14. Dogfood on a real project.
15. Only then design package distribution.
16. Only then design MCP server.
17. Only then design hooks.
18. Only then add SQLite FTS/vector search.

---

## 21. Prompting-Guides Resources To Use

When implementing or refining this tool, use these prompts from `Prompting-guides`:

### Core project-memory design

- `domain-AI-ML/agentic-ai-systems/aiagent_project_continuity_memory_design.md`
- `domain-AI-ML/agentic-ai-systems/aiagent_project_memory_capture_protocol.md`
- `domain-AI-ML/agentic-ai-systems/aiagent_project_memory_guard_before_action.md`
- `domain-AI-ML/agentic-ai-systems/aiagent_project_memory_interop_adapter_design.md`
- `domain-AI-ML/agentic-ai-systems/aiagent_project_memory_security_decay_audit.md`

### Related agentic-system design prompts

- `domain-AI-ML/agentic-ai-systems/aiagent_memory_design.md`
- `domain-AI-ML/agentic-ai-systems/aiagent_context_engineering_at_scale.md`
- `domain-AI-ML/agentic-ai-systems/aiagent_durable_execution_state_persistence.md`
- `domain-AI-ML/agentic-ai-systems/aiagent_cross_agent_handoff_recovery.md`
- `domain-AI-ML/agentic-ai-systems/aiagent_memory_poisoning_defense.md`
- `domain-AI-ML/agentic-ai-systems/aiagent_agentic_threat_model.md`

### Session and compaction prompts

- `domain-prompt-engineering/agent-workflows/agent_state_summary_for_compaction.md`
- `domain-agentic-resources/commands/multi-agent/multiagent_graceful_session_endings.md`

### Existing lightweight project-memory seed

- `domain-engineering-workflows/ai-native-rollouts/airollout_long_running_project_memory.md`

### Factory integration

- `agentic-system-factory/README.md`
- `agentic-system-factory/referenced-prompts/README.md`

---

## 22. Open Design Questions

### Resolved (decided during planning)

- **Generated Markdown projections:** committed by default (`commit_generated_projections: true`); flippable per project. Indexes always ignored. See §5.
- **Session records:** project-chosen at `init` (`session_tracking: full | distillate`), recorded in `manifest.yml`. See §5, §7.
- **Implementation language:** Python end-to-end (prototype, CLI, MCP). See Phase 4.
- **Record identity:** filename-canonical; `id`/`slug` are computed and validated against the filename. See §7.

### Still open — resolve during dogfooding

1. Should schema be JSON Schema, Markdown convention, or both?
2. How aggressive should guard-before-action be before users ignore it?
3. Should `known-traps.md` remain one file or become `traps/` records?
4. How should local-private memory participate in global dashboard without leaking details?
5. How should the tool handle non-git project folders? (Several frontmatter fields — `branch`, `commit`, `dirty_files` — are git-derived; define their fallback when git is absent.)
6. Should high-impact memory review be enforced by CI, pre-commit, or only warnings?
7. What is the retention/rollup story for `sessions/` over months? (Fixture 10 keeps *resume* bounded, but the directory itself grows unbounded — decide on archival/rollup.)

---

## 23. Build Philosophy

Build the boring useful version first.

The correct order is:

```text
plain files
→ deterministic CLI
→ validation/audit
→ guard-before-action
→ fixtures/evals
→ dogfood
→ packaging
→ MCP
→ hooks
→ search/index acceleration
→ vectors if still needed
```

If the project-memory system cannot help a read-only cloud agent by exposing clear files, it is not portable enough.

If it cannot help a tired human capture a session in under 90 seconds, it is too heavy.

If it cannot warn before a repeated failed attempt, it is just a scrapbook.

The goal is a small continuity engine: a project cockpit with labeled switches, not a haunted attic of embeddings.
