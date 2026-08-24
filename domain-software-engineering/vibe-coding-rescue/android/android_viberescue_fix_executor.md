---
title: "Safely Execute a Single Prioritized Fix on a Vibe-Coded Android App"
category: software-engineering/vibe-coding-rescue/android
description: "Apply one fix from the queue produced by android_viberescue_fix_prioritization.md with discipline: write or extend a failing test first, make the smallest possible change, one issue per commit, no unrelated edits, document a rollback plan, and abort if the change cascades beyond expected files. Designed to run in a loop over the fix queue; refuses to proceed if preconditions are unmet."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - CM-03
  - RT-05
  - QA-01
  - QA-02
  - QA-05
difficulty: advanced
tags:
  - vibe-coding
  - android
  - fix-execution
  - test-first
  - safe-refactor
  - rollback
updated: "2026-05-17"
related_prompts:
  - domain-software-engineering/vibe-coding-rescue/android/android_viberescue_fix_prioritization.md
  - domain-software-engineering/vibe-coding-rescue/android/android_viberescue_codebase_audit.md
  - domain-software-engineering/vibe-coding-rescue/android/android_viberescue_security_privacy_audit.md
  - domain-software-engineering/vibe-coding-rescue/viberescue_decompose_stuck_task.md
---

# Safely Execute a Single Prioritized Fix on a Vibe-Coded Android App

**Purpose:** This is the executor side of the rescue. It takes one fix from `android_viberescue_fix_prioritization.md`'s queue and applies it with discipline that vibe-coding does not enforce: test first, smallest change, one issue per commit, abort on cascade. The goal is to make the codebase strictly better with this one commit and to leave a clear rollback path. Designed for an AI coding agent (Claude Code, Codex, Cursor) operating with file-edit and shell-execution tools; equally usable by a careful human.

**When to use:**
- Looping through the queue from `android_viberescue_fix_prioritization.md`. One invocation per fix.
- After the queue exists. Do not run this without a queue — pre-execution prioritization is what prevents random fixes from making things worse.

**Don't use when:**
- The fix is `human_required: true` in the queue. A human must own it.
- Tier 0 dependencies are unsatisfied. Run those first.
- The project's working tree has uncommitted changes unrelated to this fix. Commit or stash first; this prompt requires a clean slate.

**Audience:** AI coding agent or engineer applying one fix at a time.

**Agent portability note:** Written for any coding agent with file-edit and shell capabilities. Substitute your agent's specific tool names for the generic verbs ("read", "search", "write", "run").

---

## Inputs Required

Refuse to execute without 1, 2, 3, and 4.

1. **Single fix item.** One entry from `android_viberescue_fix_prioritization.md`'s queue, with all fields populated.
2. **Project root path** (absolute path).
3. **Current branch** the agent is working on. The agent will NOT switch branches.
4. **Build / test commands.**
   - How to build: e.g., `./gradlew :app:assembleDebug`
   - How to run unit tests: e.g., `./gradlew :app:testDebugUnitTest`
   - How to run instrumentation tests: e.g., `./gradlew :app:connectedDebugAndroidTest` (or "device not available" — record explicitly)
   - How to run lint / static analysis: e.g., `./gradlew :app:lintDebug` or `./gradlew detekt`
5. **Optional: project rules file** (`CLAUDE.md` / `.cursorrules`). If present, the fix must not violate it.
6. **Optional: blast-radius cap.** Max files the fix should touch (default: 5 for ISOLATE, 15 for BATCH). Cascade beyond this triggers abort.

---

## Instructions

### Step 0 — Precondition checks (abort early if violated)

Before reading any project file:

- [ ] Fix item is fully specified (all queue fields present).
- [ ] `human_required` is `false`.
- [ ] All `depends_on` fix IDs are marked complete (verify via git log or by asking the user).
- [ ] Working tree is clean (`git status` reports nothing).
- [ ] Current branch matches input 3.
- [ ] Project rules file (if provided) does not forbid this fix.

If any check fails, ABORT. Report which check failed and what the user must do to unblock.

### Step 1 — Read the fix's target file(s)

Read the file at the fix's specified file:line range. Read surrounding context — at minimum the full function, class, or Composable containing the fix site, and the file's imports.

If the fix touches an Android-specific file (AndroidManifest.xml, build.gradle.kts, network_security_config.xml, proguard-rules.pro), read the full file regardless of size.

### Step 2 — Verify the finding is still real

Before fixing, confirm the finding still applies:

- The code at file:line still exhibits the pattern the audit described.
- The framework protection check from the audit still holds (no library upgrade has fixed it).
- The fix direction from the audit still makes sense given current code.

If the finding is no longer real, ABORT with "stale finding — re-run audit." If the finding is real but the fix direction is wrong, ABORT with "fix direction needs revision."

### Step 3 — Write or extend a failing test FIRST

For the test gap identified in the queue entry:

1. Determine test type: unit / instrumentation / Compose UI / lint custom rule.
2. Find the appropriate test source set (`src/test/...`, `src/androidTest/...`).
3. Write the smallest test that asserts the desired post-fix behavior.
4. Run the test and confirm it FAILS for the expected reason.
   - If the test passes already, the fix may not be needed. ABORT with "test passes — finding may be stale; investigate."
   - If the test fails for an unrelated reason, fix the test and re-run.

If no realistic test can be written (the queue should have flagged this), you should have ABORTED at Step 0. If somehow you got here without a test, ABORT and require human review.

Exception: for AndroidManifest.xml-only fixes (e.g., adding `android:exported`), the "test" may be:
- A lint custom rule, OR
- A unit test asserting manifest contents via `PackageManager`, OR
- A build-time check via `manifestProcessor`.

Pick the lightest viable option and write it.

### Step 4 — Apply the smallest possible fix

Edit only the file(s) needed to make the failing test pass. Do not:
- Refactor adjacent code that "looks bad" but wasn't in the finding.
- Reformat unrelated files.
- Update unrelated dependencies.
- Reorganize imports beyond what the change requires.
- Add helpful comments throughout the file ("while you're here" creep).

The diff should be the minimum that:
1. Makes the failing test pass.
2. Resolves the audit finding.
3. Does not break any other test.

### Step 5 — Run the full test + build pipeline

Run, in order:

1. The new/updated test from step 3 — must PASS.
2. Unit tests (`testDebugUnitTest`) — must PASS.
3. Lint / static analysis (`lintDebug` / `detekt`) — must not introduce new violations.
4. Build (`assembleDebug`) — must SUCCEED.
5. Instrumentation tests if device available AND fix is in code paths an instrumentation test exercises — must PASS.

If any step fails, do NOT keep editing. Either:
- The failure is directly caused by the fix — revert your change and ABORT with diagnosis.
- The failure is a pre-existing broken test — note it, do NOT attempt to fix it in this commit. ABORT and surface the broken test.

### Step 6 — Cascade check

Before committing:

- Count files changed (`git diff --name-only | wc -l`). Compare to the blast-radius cap (input 6).
- If files changed exceeds the cap, ABORT. Either the fix was bigger than the queue estimated (revise the queue and run `viberescue_decompose_stuck_task.md`) or the executor over-edited.
- Read the diff once end-to-end. Confirm every line of change traces to: the fix, the new test, or a strictly required adjacent change.
- Confirm no unrelated comments, no debugging println / Log calls, no commented-out code added.

### Step 7 — Stage and commit (one issue per commit)

Stage only the files needed. Commit with the message from the queue's `suggested commit message`, expanded to include:

```
[tier-tag] short description

Fix ID: SEC-001 (from android_viberescue_fix_prioritization.md queue)
Audit source: android_viberescue_security_privacy_audit.md
Category: 2.1 manifest / exported components
Files: AndroidManifest.xml, ManifestExportedFlagsTest.kt

Pre-fix evidence: <one-line quote of the audit's evidence>
Fix applied: <one-line description>
Test added: <test name + what it asserts>
Rollback: revert this commit and the test will fail, restoring the prior (vulnerable) state.
```

Do NOT include co-author or AI-tool attribution unless the project's rules file requires it. Do not include the model identifier.

### Step 8 — Document the rollback path

In the commit body (last line) OR in a separate `FIX_LOG.md` in the project root:

- This commit's SHA.
- One sentence: "If this fix causes regression, revert this commit (`git revert <sha>`) and the project returns to its prior state because [reason]."
- If the fix included a migration (Room schema, manifest permission, signing config), the rollback path is more complex — document each step.

### Step 9 — Update the fix queue

If the fix completed cleanly:
- Mark fix ID as `complete` in the queue (output a one-line status update the user can paste back).
- If this fix's `depends_on` enables a downstream fix, list which fixes are now unblocked.

If the fix aborted:
- Mark fix ID as `aborted` with the abort reason.
- Recommend whether to: re-run the audit, re-run the prioritization, decompose with `viberescue_decompose_stuck_task.md`, or escalate to human.

### Step 10 — Verify and report

Run the verification checklist. Emit the final report.

---

## Constraints

### Must
- Run all precondition checks before reading any file.
- Write the failing test BEFORE the fix.
- Apply the smallest possible change.
- Run the full pipeline (test → lint → build → instrumentation if applicable).
- Check cascade before committing.
- Commit one fix per commit with the prescribed message template.
- Document rollback path.
- Update the fix queue with the result.

### Must Not
- Switch branches.
- Skip the failing-test step "because the fix is obvious."
- Refactor or clean up code outside the fix's scope.
- Bypass failing tests (`--no-verify`, ignore-lint).
- Amend an existing commit (always create new commits).
- Commit multiple fixes together unless the queue marked them BATCH AND they share a single test.
- Continue past an abort condition. ABORT is final for this invocation.
- Include AI-tool attribution or model identifiers in commit messages unless explicitly required.
- Reference Claude-Code-specific tool names in the prompt body.

---

## False-Positive Prevention (MUST follow)

DON'T:
- Conclude "the fix is too small to need a test" — Tier 0 and Tier 1 always need a test.
- Claim a test was written when you only added an assertion to an existing test that doesn't actually cover the fix path.
- Run only unit tests when the fix is in lifecycle / threading / UI behavior — those need instrumentation or Compose UI tests.
- Assume lint passing means correctness; lint catches a small slice.
- Treat "build succeeds" as sufficient validation for runtime behavior fixes.
- Squeeze in unrelated cleanups "while you have the file open."

DO:
- Treat the cascade check as a hard gate.
- Read the diff end-to-end before staging.
- ABORT loudly. Half-applied fixes are worse than the original problem.
- When the test infrastructure isn't ready for the fix (no instrumentation device, no Compose test harness), escalate rather than skip.
- Preserve the rollback path as a first-class output.

---

## Dual-Failure Prevention (QA-20)

HARMFUL failure: Fix lands, breaks an unrelated flow, no rollback documented, team learns from a user report.

UNHELPFUL failure: Agent aborts repeatedly on every fix because preconditions are over-strict; queue makes no progress.

Quality check: A senior engineer reads the commit, can revert it cleanly, the test demonstrates the issue, and the diff contains nothing extraneous.

---

## Output Format

```markdown
# Fix Execution Report — [Fix ID]

## Status
- Result: COMPLETE | ABORTED
- If aborted: [which step, which condition]

## Preconditions
- [x] Fix item fully specified
- [x] human_required = false
- [x] Dependencies complete
- [x] Working tree clean
- [x] Branch matches
- [x] Rules-file conflict: none

## Test
- Type: [unit / instrumentation / Compose UI / lint-rule / manifest assertion]
- Path: [path/to/Test.kt]
- Status pre-fix: FAILED (expected)
- Status post-fix: PASSED

## Change
- Files modified: [list with line counts]
- Lines added / removed: [N / N]
- Diff summary: [3-line description]

## Pipeline
- [x] New test: PASS
- [x] Unit tests: PASS ([N] tests)
- [x] Lint: PASS (no new violations)
- [x] Build: PASS
- [ ] Instrumentation: SKIPPED — no device available | PASS | FAIL

## Cascade Check
- Files changed: [N] / cap [N]
- Diff end-to-end review: clean

## Commit
- SHA: [sha]
- Message: [full message]

## Rollback Path
- [one-line revert instruction or migration-aware multi-step]

## Queue Update
- Fix [ID]: COMPLETE
- Unblocked: [other fix IDs] | none
- Next recommended fix: [fix ID from queue]

## If Aborted
- Abort step: [step N]
- Abort reason: [one sentence]
- Recommended action: [re-audit / re-prioritize / decompose / escalate]
```

---

## Verification

- [ ] All preconditions checked before file reads.
- [ ] Failing test written and verified failing BEFORE fix.
- [ ] Smallest possible diff applied.
- [ ] Full pipeline run (test → lint → build → instrumentation if applicable).
- [ ] Cascade check passed.
- [ ] Single commit with prescribed message template.
- [ ] Rollback path documented.
- [ ] Queue update emitted.
- [ ] If aborted: abort step and reason clear, recommended next action specified.

---

## Techniques Used

- **ST-01 (Clear Objective):** Apply exactly one fix safely; not "improve the codebase."
- **ST-02 (Structured Sequential Instructions):** Eleven steps (0–10) with strict ordering; later steps depend on earlier ones.
- **ST-03 (Output Format Specification):** Fixed report schema enables looping (queue → executor → queue update → next).
- **CM-02 (Constraint Specification):** Must Not block forbids branch switching, test skipping, scope creep.
- **CM-03 (Pre/Post-Conditions):** Step 0 preconditions + step 6 cascade check + step 8 rollback enforce contract before and after the fix.
- **RT-05 (Evidence-Based Reasoning):** Step 2 verifies the finding is still real; step 3 grounds the test in the audit's evidence.
- **QA-01 (Self-Verification):** Verification checklist at the end.
- **QA-02 (Self-Check Before Commit):** Cascade check (step 6) is an explicit self-check gate before staging.
- **QA-05 (Abort Triggers):** Explicit ABORT conditions at steps 0, 2, 3, 5, 6 — half-applied fixes are not allowed.
