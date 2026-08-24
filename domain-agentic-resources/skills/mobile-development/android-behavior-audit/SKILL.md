---
name: android-behavior-audit
description: "Behavioral scrutiny methodology for evaluating whether Android app code behavior matches developer intent, with structured finding classification (Likely Bug, Suspicious Pattern, Design Question, Confirmed Correct) and calibrated confidence scoring. Use this skill when auditing app behavior against intent, identifying behavioral discrepancies, classifying code issues by confidence, or when users mention 'behavior audit', 'does this code make sense', 'behavioral scrutiny', or 'intent vs actual behavior'."
metadata:
  tags:
    - android
    - audit
    - behavior
    - scrutiny
    - intent-analysis
  updated: "2026-02-17"
---

# Android Behavior Audit

Methodology for scrutinizing an Android app's behavior catalog to identify discrepancies between what the code actually does and what a reasonable developer would intend. This is not code review (quality), security audit (vulnerabilities), or architecture review (structure) — this is behavioral scrutiny: "Does this behavior make sense?"

## Purpose

Given a factual behavior catalog (produced by the trace phase), this skill provides the framework for:
1. Systematically evaluating each behavior for sensibility
2. Classifying findings by confidence level
3. Asking the right questions to the developer
4. Presenting findings in a format that enables productive clarification

The goal is to surface issues that traditional reviews miss — not bugs that crash the app, but behaviors that are subtly wrong, confusing, or incomplete.

## When to Use This Skill

- Evaluating a behavior catalog from the trace phase of a behavior audit
- Reviewing code behavior to identify "something feels off" issues
- Pre-release behavioral verification (does the app do what we think it does?)
- When a developer says "the app works but something doesn't seem right"

## When NOT to Use This Skill

- You don't have a behavior catalog yet (use `android-behavior-trace` first)
- You need to find security vulnerabilities (use security audit prompts)
- You need to evaluate code quality or style (use code review prompts)
- You need to assess performance (use performance audit prompts)
- You need to plan or implement fixes (use `android-behavior-fix-planning` after audit)

## Prerequisites

- Completed behavior catalog from the trace phase
- Each behavior entry must include: user action, code behavior, code location, edge cases
- The catalog must be factual (no judgments — that's this skill's job)

## Finding Classification Guide

### Category 1: Likely Bug (Confidence >80%)

**Definition:** Behavior that is almost certainly unintended. The code does something that would produce a negative user experience or data integrity issue, and there is no reasonable interpretation where this behavior is correct.

**Criteria — classify as Likely Bug when:**
- Data is silently lost, corrupted, or orphaned
- An error occurs but the user is never informed
- A state transition is impossible to recover from
- The code explicitly contradicts its own documentation or naming
- A feature is partially implemented (some paths work, others don't)
- The behavior creates a security vulnerability

**Example signals:**
- `catch(e: Exception) { /* empty */ }` in a data-saving operation
- Insert with `OnConflictStrategy.REPLACE` silently overwriting user edits
- Navigation to a screen that has no back navigation path
- A listener that is attached but never detached
- A WorkManager task with `Result.success()` even when the operation fails

### Category 2: Suspicious Pattern (Confidence 40-80%)

**Definition:** Behavior that could be intentional but has characteristics that suggest it's likely wrong. There is a plausible interpretation where this behavior is correct, but the more probable interpretation is that it's a mistake.

**Criteria — classify as Suspicious when:**
- Error handling exists but seems insufficient for the failure mode
- A fallback behavior exists but might confuse users
- Timing or ordering assumptions that might not always hold
- Data handling that works in common cases but fails in edge cases
- Retry logic that could mask underlying issues

**Example signals:**
- `catch(e: Exception) { Log.e(TAG, "Error", e) }` without user notification for important operations
- Hardcoded timeout values with no explanation
- `delay(1000)` used as synchronization (timing-dependent behavior)
- Saving state in ViewModel but not in SavedStateHandle (lost on process death)
- Using `GlobalScope` instead of a lifecycle-aware scope

### Category 3: Design Question (Confidence <40%)

**Definition:** Behavior that works as coded but whose intent is ambiguous. The behavior might be exactly what the developer intended, or it might be an oversight. Only the developer can clarify.

**Criteria — classify as Design Question when:**
- A choice was made but the reasoning isn't obvious from the code
- Multiple valid approaches exist and the chosen one has tradeoffs
- Default values or thresholds that seem arbitrary
- UX flows that could go either way
- Missing features that might be intentionally deferred

**Example signals:**
- Pagination limit of 50 — was this chosen deliberately or is it a placeholder?
- Error messages that show technical details to users — intentional for debugging or oversight?
- Auto-save frequency of 30 seconds — based on research or arbitrary?
- Offline data available for 7 days — business decision or arbitrary?
- No confirmation dialog before delete — intentional simplicity or missing feature?

### Category 4: Confirmed Correct

**Definition:** Behavior that was scrutinized and appears to be working as a reasonable developer would intend. Document why it appears correct to provide audit trail.

**When to classify as Confirmed Correct:**
- The behavior matches its naming, documentation, and context
- Error handling is proportionate to the failure mode
- Edge cases are handled appropriately
- The behavior produces the expected user experience

## Scrutiny Checklist: By Android Subsystem

### Compose UI Scrutiny
- [ ] **Recomposition side effects:** Are side effects in `LaunchedEffect` / `SideEffect` or improperly in the composable body?
- [ ] **State loss on configuration change:** Is state hoisted to ViewModel or only in composable local state?
- [ ] **Loading state completeness:** Does every async operation have a loading indicator?
- [ ] **Error state completeness:** Does every error path show the user a meaningful message?
- [ ] **Empty state handling:** What does the user see when there's no data?
- [ ] **Back button behavior:** Does the back button do what the user expects from every screen?
- [ ] **Input validation feedback:** Is validation feedback immediate or only on submit?

### ViewModel State Scrutiny
- [ ] **Unreachable states:** Can the state machine reach a state it can never exit?
- [ ] **Missing state transitions:** Are there user actions that don't update the state?
- [ ] **State restoration after process death:** Is critical state in SavedStateHandle?
- [ ] **Concurrent state updates:** Can two operations update state simultaneously?
- [ ] **Initial state correctness:** Is the initial state before data loads appropriate?
- [ ] **Error state recovery:** Can the user recover from error states (retry, dismiss)?

### Room Database Scrutiny
- [ ] **Silent write failures:** Are insert/update failures caught and surfaced?
- [ ] **Orphaned records:** When a parent entity is deleted, are children handled?
- [ ] **Migration data loss:** Do migrations preserve all user data?
- [ ] **Transaction completeness:** Are related write operations in a single transaction?
- [ ] **Query correctness:** Do queries return what the calling code expects?
- [ ] **Type converter accuracy:** Do type converters round-trip correctly (serialize → deserialize)?

### Firebase Scrutiny
- [ ] **Conflict resolution:** What happens when local and remote data disagree?
- [ ] **Offline queue behavior:** Are offline writes queued and applied on reconnect?
- [ ] **Partial sync states:** What happens if sync is interrupted midway?
- [ ] **Auth token expiry:** What happens when the auth token expires mid-operation?
- [ ] **Security rules alignment:** Does the code assume operations that rules might deny?
- [ ] **Listener leaks:** Are all Firebase listeners properly detached on lifecycle events?

### Navigation Scrutiny
- [ ] **Dead-end screens:** Can the user reach a screen they can't navigate away from?
- [ ] **Back stack consistency:** Is the back stack what the user would expect after deep navigation?
- [ ] **Deep link handling:** Do deep links work from all entry points (notification, widget, external)?
- [ ] **Auth gate completeness:** Are all screens that require auth properly gated?
- [ ] **Navigation during async operations:** What happens if navigation occurs while an operation is pending?

### Error Handling Scrutiny
- [ ] **Swallowed exceptions:** Are any exceptions caught and silently ignored?
- [ ] **Generic error messages:** Are error messages useful to the user or just "Something went wrong"?
- [ ] **Retry mechanism:** For retryable errors, can the user retry?
- [ ] **Network error distinction:** Does the app distinguish between no-network and server-error?
- [ ] **Crash prevention vs. correctness:** Does the code prevent crashes at the cost of incorrect behavior?

### Background Work Scrutiny
- [ ] **WorkManager constraints:** Are constraints appropriate for the work type?
- [ ] **Interrupted work handling:** What happens if a worker is interrupted by the system?
- [ ] **Result delivery:** Is the work result delivered to the UI or just logged?
- [ ] **Periodic work overlap:** Can periodic work instances overlap?
- [ ] **Notification accuracy:** Do notifications reflect the actual state (not stale data)?

## Presentation Format

Present findings in this structure:

```markdown
# Behavior Audit Findings: [Feature Area]

## Summary
- **Total behaviors reviewed:** [count]
- **Likely Bugs:** [count]
- **Suspicious Patterns:** [count]
- **Design Questions:** [count]
- **Confirmed Correct:** [count]

---

## Likely Bugs

### BUG-001: [Short descriptive title]
- **Behavior:** [What the code actually does]
- **Why it seems wrong:** [Specific reasoning]
- **User impact:** [What the user would experience]
- **Code location:** `file.kt:line`
- **Scenario:** [Step-by-step user scenario that triggers this]

### BUG-002: ...

---

## Suspicious Patterns

### SUS-001: [Short descriptive title]
- **Behavior:** [What the code actually does]
- **Why it's suspicious:** [Specific reasoning]
- **Possible intent:** [How this might be intentional]
- **Code location:** `file.kt:line`
- **Question for developer:** [Specific question to clarify intent]

### SUS-002: ...

---

## Design Questions

### DQ-001: [Short descriptive title]
- **Behavior:** [What the code actually does]
- **Ambiguity:** [Why the intent is unclear]
- **Option A:** [One interpretation]
- **Option B:** [Alternative interpretation]
- **Code location:** `file.kt:line`
- **Question for developer:** [Specific question to resolve ambiguity]

---

## Confirmed Correct
[Brief list of behaviors that were scrutinized and appear correct, with one-line rationale for each]
```

## Calibration Principles

### Avoiding False Positives
- **Assume intentionality:** Code exists because someone wrote it deliberately. Assume the behavior is intentional until you have concrete evidence otherwise.
- **Consider the context:** A `catch` block that logs and continues might be correct in a non-critical code path.
- **Don't flag style:** If the code works correctly but you'd write it differently, that's not a finding.
- **Don't flag architecture:** If the architecture is unconventional but the behavior is correct, that's not a finding.

### Ensuring Real Issues Are Caught
- **Follow the data:** If data can be lost, corrupted, or orphaned, that's always worth flagging.
- **Follow the user:** If the user would be confused, stuck, or misled, that's always worth flagging.
- **Follow the errors:** If errors are swallowed silently, that's always suspicious.
- **Follow the edge cases:** If edge cases aren't handled, check whether they're realistic.

### Confidence Calibration
- **>80% (Likely Bug):** You would bet money this is a bug. The evidence is strong.
- **40-80% (Suspicious):** You think it's probably wrong but you can see how it might be intentional.
- **<40% (Design Question):** You genuinely don't know if this is right or wrong. Only the developer can say.

## Related Skills

- `android-behavior-trace` — Produces the behavior catalog that this skill evaluates
- `android-behavior-fix-planning` — Plans fixes for confirmed issues found by this skill
- `android-app-survey` — Survey phase that precedes both tracing and auditing
