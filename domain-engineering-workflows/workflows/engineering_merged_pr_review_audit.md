---
title: "Merged PR Review Audit"
category: engineering-workflows/workflows
description: "Critically review the last 5 merged pull requests for correctness, oversights, edge cases, and regressions — then report findings with suggested fixes"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
  - DT-04
  - QA-01
difficulty: advanced
tags:
  - pull-request
  - code-review
  - audit
  - post-merge
  - regression
  - edge-cases
updated: "2026-03-25"
related_prompts:
  - domain-agentic-resources/skills/developer-tools/code-review-excellence/SKILL.md
  - domain-agentic-resources/agents/code-quality/solo_dev_reviewer.md
  - domain-software-engineering/analysis/security/security_vulnerability_analysis.md
---

# Merged PR Review Audit — Last 5 Pull Requests

**Objective:** Perform a critical, post-merge code review of the 5 most recently merged pull requests in this repository. Identify correctness issues, missed edge cases, potential regressions to existing functionality, and security or performance concerns — then report findings with severity ratings and suggested fixes.

> **Important:** This is a READ-ONLY audit. All PRs have already been merged into `main`. Do NOT create branches, open PRs, or modify any code. Your job is to analyze and report.

---

## Instructions

### Phase 1 — Gather the PRs

1. **Fetch the 5 most recently merged pull requests** for this repository.
   - Use `mcp__github__search_pull_requests` with query `is:merged sort:updated-desc` scoped to this repo, `perPage: 5`.
   - For each PR, record: PR number, title, author, merge date, and description.

2. **For each PR, retrieve the diff and changed files.**
   - Use `mcp__github__pull_request_read` with method `get_diff` to get the full diff.
   - Use `mcp__github__pull_request_read` with method `get_files` to get the file list with additions/deletions counts.
   - Also read the PR description and any linked issues for intent context.

### Phase 2 — Analyze Each PR

3. **For each PR, read the actual merged code on `main`** for every file that was changed. Do not rely solely on the diff — read the full file to understand surrounding context, imports, callers, and downstream consumers.

4. **Analyze each PR across these dimensions:**

   **a. Correctness**
   - Logic errors, off-by-one mistakes, wrong comparison operators, missing return statements
   - Incorrect type handling, implicit coercions, narrowing failures
   - Broken control flow (unreachable code, infinite loops, swallowed exceptions)
   - Contract violations (function signatures changed but callers not updated)

   **b. Edge Cases**
   - Null, undefined, empty string, empty array, zero, negative values
   - Boundary values (max int, empty collections, single-element arrays)
   - Concurrent access / race conditions
   - Error paths — what happens when the happy path fails?
   - Malformed or unexpected input (extra fields, wrong types, missing required fields)

   **c. Regressions**
   - Existing functionality broken by the change
   - Removed safety checks, validation, or error handling that previously existed
   - Changed function signatures, return types, or API contracts that other code depends on
   - Modified shared utilities, constants, or configuration that affect other features
   - Deleted or altered tests that previously caught bugs

   **d. Security**
   - New user input paths without validation or sanitization
   - Authentication or authorization changes that widen access
   - Secrets, tokens, or credentials exposed in code or config
   - SQL injection, XSS, CSRF, or path traversal introduced
   - Dependency additions with known vulnerabilities

   **e. Performance**
   - N+1 query patterns, unbounded loops, missing pagination
   - Large allocations in hot paths, memory leaks, unclosed resources
   - Missing caching where repeated expensive operations occur
   - Blocking I/O on main thread or in async contexts

### Phase 3 — Verify Before Reporting

5. **CRITICAL: Verify each potential finding before including it in the report.**
   - **Read the actual code on `main`** — confirm the issue exists in the merged state, not just in the diff context.
   - **Check for mitigations elsewhere** — search the codebase for validation, error handling, or guards that may exist in callers or middleware.
   - **Understand intent** — read the PR description and any comments. Was this a deliberate tradeoff? Is there a follow-up PR planned?
   - **Confirm impact** — can this actually cause a bug, crash, data corruption, or security breach in practice?
   - **Assign confidence** — only report findings you are Medium or High confidence about.
     - **High:** You traced the code path end-to-end and confirmed the issue exists with no mitigations.
     - **Medium:** The issue is likely based on the code you read, but you could not fully confirm all callers or downstream effects.
     - **Low:** Do NOT include Low confidence findings. Mention them only in a brief "areas to watch" note if relevant.

### Phase 4 — Classify and Report

6. **Classify each verified finding by severity:**
   - 🔴 **P0 — Critical:** Bugs that cause crashes, data corruption, security vulnerabilities, or broken core functionality. Fix immediately.
   - 🟡 **P1 — Important:** Missing error handling on critical paths, edge cases that will cause issues under real usage, performance problems at scale. Fix soon.
   - 🟢 **P2 — Minor:** Code quality improvements, missing edge case handling for unlikely scenarios, minor performance optimizations. Track for later.

7. **For each finding, provide a suggested fix:**
   - Include a code snippet showing the fix (or a clear description if the fix is architectural).
   - Estimate effort: "5-minute fix", "30-minute refactor", "needs design discussion".
   - If multiple approaches exist, briefly note the tradeoff.

8. **Produce the final report** using this structure:

---

## Output Format

```
# 🔍 Merged PR Review Audit

**Repository:** [owner/repo]
**Date:** [today]
**PRs Reviewed:** [count]
**Audit Summary:** [1-2 sentence overall assessment]

---

## Executive Summary

| Severity | Count | Description |
|----------|-------|-------------|
| 🔴 P0    | X     | [brief]     |
| 🟡 P1    | X     | [brief]     |
| 🟢 P2    | X     | [brief]     |

**Overall Verdict:** [CLEAN / NEEDS ATTENTION / ACTION REQUIRED]

---

## PR #[number]: [title]
**Author:** [author] | **Merged:** [date] | **Files Changed:** [count]
**Intent:** [1-sentence summary of what this PR does]

### Findings

#### 🔴 P0: [Finding Title]
- **File:** `path/to/file.ext` (lines X-Y)
- **Issue:** [Clear description of the problem]
- **Impact:** [What breaks, who is affected, under what conditions]
- **Evidence:** [Code snippet or trace showing the issue]
- **Confidence:** High | Medium
- **Suggested Fix:**
  ```[language]
  // Suggested code change
  ```
- **Effort:** [5-minute fix | 30-minute refactor | needs discussion]

#### 🟡 P1: [Finding Title]
[same structure]

#### 🟢 P2: [Finding Title]
[same structure]

### ✅ What This PR Did Well
- [Positive observation — good patterns, thorough handling, clean design]

---

[Repeat for each PR]

---

## Cross-PR Patterns

- [Any issues that appear across multiple PRs — systemic patterns]
- [Architectural trends — growing complexity, coupling, etc.]

## Areas to Watch (Low Confidence)

- [Brief notes on things that looked suspicious but could not be confirmed]

## Recommended Actions

1. [Highest priority action with PR reference]
2. [Next priority action]
3. [...]
```

---

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Do NOT flag issues based solely on the diff without reading the full file context on `main`
- Do NOT assume missing error handling in the diff means it is missing — check callers, middleware, and framework defaults
- Do NOT flag intentional tradeoffs documented in the PR description or comments
- Do NOT report style, formatting, or naming preferences — this audit is about correctness and safety
- Do NOT flag test code with the same rigor as production code (test helpers, fixtures, mocks are allowed to be simpler)
- Do NOT assume a missing test means a bug — flag missing tests only if you found an actual issue the test would have caught

✅ **DO:**
- DO read full files on `main`, not just diffs, before reporting
- DO check for guards, validation, and error handling in surrounding code and callers
- DO read the PR description to understand intent and deliberate tradeoffs
- DO verify that the issue is actually reachable in practice (trace the code path)
- DO include specific file paths, line numbers, and code snippets for every finding
- DO celebrate good patterns and well-structured changes — not every PR has issues

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Opens with a precise, unambiguous audit objective and scope (5 most recent merged PRs, read-only)
- **ST-02 (Structured Sequential Instructions):** 4-phase process (Gather → Analyze → Verify → Report) with numbered steps
- **RT-02 (Multi-Dimensional Analysis):** Each finding assessed across 5 dimensions (correctness, edge cases, regressions, security, performance)
- **RT-05 (Evidence-Based Reasoning):** Every finding requires file paths, line numbers, code snippets, and traced code paths
- **DS-06 (Prioritization Guidance):** P0/P1/P2 severity classification with clear definitions and effort estimates
- **DT-04 (Multi-Layer Analysis):** Reviews at function level (logic), module level (contracts), and system level (regressions)
- **QA-01 (Chain-of-Verification):** Mandatory verification phase before reporting — read actual code, check mitigations, confirm impact
