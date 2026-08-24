---
name: android-behavior-fix-planning
description: "Fix planning and implementation methodology for resolving behavioral discrepancies in Android apps, including blast radius estimation, dependency ordering, minimal-change implementation, and post-fix verification. Use this skill when planning fixes for behavior audit findings, estimating fix complexity, ordering fix dependencies, or when users mention 'plan the fix', 'fix behavioral issues', 'implement audit fixes', or 'verify fix correctness'."
metadata:
  tags:
    - android
    - fix-planning
    - implementation
    - verification
    - behavior-audit
  updated: "2026-02-17"
---

# Android Behavior Fix Planning

Methodology for planning, implementing, and verifying fixes that align Android app behavior with developer intent. Works on confirmed findings from the behavior audit phase. Emphasizes minimal-change fixes, blast radius awareness, dependency ordering, and post-fix verification.

## Purpose

After the behavior audit identifies discrepancies and the developer confirms which findings are real issues, this skill provides the methodology to:
1. Integrate developer clarifications to build a confirmed fix list
2. Plan each fix with blast radius estimation
3. Order fixes by dependency and risk
4. Implement fixes one at a time with verification
5. Re-audit modified areas to confirm resolution

## When to Use This Skill

- Planning fixes for confirmed behavior audit findings
- Developer has reviewed audit findings and clarified intended behavior
- Need to estimate complexity and blast radius of behavioral fixes
- Implementing fixes and verifying they resolve the identified issues

## When NOT to Use This Skill

- You haven't completed the behavior audit yet (use `android-behavior-audit` first)
- The developer hasn't reviewed and confirmed findings yet (wait for clarification)
- The issues are performance-related (use performance optimization skills)
- The issues are security-related (use security remediation skills)
- You need to add new features (this is for fixing existing behavioral issues)

## Prerequisites

- Completed behavior audit with classified findings (Likely Bug, Suspicious, Design Question)
- Developer clarifications on each finding (confirmed bug, intentional, or needs more info)
- Access to the full source code with ability to make changes
- Test infrastructure available (or ability to create tests)

## Step 1: Clarification Integration

### Processing Developer Responses

For each finding from the audit, the developer will have provided one of:

| Developer Response | Action |
|---|---|
| "That's definitely a bug" | Move to confirmed fix list |
| "That's intentional" | Close finding, document the intent as a code comment |
| "I'm not sure" | Ask follow-up question with specific scenarios |
| "It should do X instead" | Document intended behavior, move to fix list |
| "Let's defer this" | Move to backlog, don't fix now |

### Building the Confirmed Fix List

For each confirmed fix, document:

```markdown
## FIX-[number]: [Title from audit finding]

**Finding ID:** [BUG-001 / SUS-003 / DQ-007]
**Current behavior:** [What the code actually does]
**Intended behavior:** [What the developer confirmed it should do]
**Code location:** `file.kt:line`
**Developer note:** [Any specific guidance from the developer]
```

## Step 2: Fix Planning

### For Each Confirmed Fix

#### 2a. Define the Change

Describe the specific code change needed. Be precise:
- Which file(s) need to change
- Which function(s) need to change
- What the function should do differently
- What new code needs to be added (if any)

**Template:**
```markdown
### Change Description
- **File:** `path/to/file.kt`
- **Function:** `functionName()`
- **Current behavior:** [what it does now]
- **New behavior:** [what it should do after the fix]
- **Change type:** [modify existing / add new / remove incorrect]
```

#### 2b. Estimate Blast Radius

Identify everything that could be affected by this change:

**Direct impact:**
- What code directly calls or is called by the changed function?
- What UI elements observe the state that this function modifies?
- What tests cover this function?

**Indirect impact:**
- Does this function's output flow to other operations?
- Does changing this function's behavior affect the timing or ordering of other operations?
- Are there shared resources (database tables, Firebase paths, shared state) that other code also accesses?

**Blast radius classification:**

| Level | Description | Example |
|---|---|---|
| **Contained** | Change is isolated to one function, no external effects | Adding null check, improving error message |
| **Local** | Change affects the immediate feature area (1-3 files) | Modifying state handling in a ViewModel |
| **Cross-cutting** | Change affects multiple features or shared infrastructure | Changing repository caching strategy, modifying database schema |
| **Architectural** | Change requires modifying the fundamental approach | Replacing sync mechanism, changing state management pattern |

#### 2c. Estimate Complexity

| Level | Time Estimate | Description |
|---|---|---|
| **Trivial** | <15 min | Single-line change, obvious fix, no side effects |
| **Simple** | 15-60 min | Small change in 1-2 files, straightforward logic |
| **Moderate** | 1-3 hours | Changes in 3-5 files, some edge cases to handle |
| **Complex** | 3-8 hours | Significant refactoring, new patterns, many edge cases |
| **Major** | 1+ day | Architectural change, requires careful migration |

## Step 3: Dependency Ordering

### Building the Fix Dependency Graph

Some fixes depend on others. Build the dependency graph:

```
FIX-001 (no dependencies)
FIX-002 → depends on FIX-001
FIX-003 (no dependencies)
FIX-004 → depends on FIX-002 and FIX-003
```

### Ordering Rules

1. **Dependencies first:** If FIX-B depends on FIX-A, do FIX-A first
2. **Data integrity first:** Fixes that prevent data loss before fixes that improve UX
3. **Lowest blast radius first:** Contained fixes before cross-cutting fixes
4. **Highest confidence first:** Certain bugs before ambiguous issues
5. **Independent fixes can be parallel:** If two fixes have no dependency, order doesn't matter

### Fix Plan Template

```markdown
# Fix Implementation Plan

## Execution Order

| Order | Fix ID | Title | Blast Radius | Complexity | Dependencies |
|-------|--------|-------|-------------|------------|--------------|
| 1 | FIX-003 | Silent data loss on save | Contained | Simple | None |
| 2 | FIX-001 | Firebase listener leak | Local | Simple | None |
| 3 | FIX-002 | State not restored after process death | Local | Moderate | None |
| 4 | FIX-005 | Navigation dead end on deep link | Local | Moderate | None |
| 5 | FIX-004 | Incomplete error handling in sync | Cross-cutting | Complex | FIX-003 |

## Risk Assessment
- **Low risk fixes (1-3):** Isolated changes, well-understood behavior
- **Medium risk fixes (4):** Broader impact, needs careful testing
- **High risk fixes (5):** Cross-cutting, should be tested extensively

## Estimated Total Effort
- Trivial/Simple fixes: [count] × ~30 min = [time]
- Moderate fixes: [count] × ~2 hrs = [time]
- Complex fixes: [count] × ~5 hrs = [time]
- **Total estimated: [sum]**
```

## Step 4: Implementation

### Implementation Protocol

For each fix, follow this protocol:

#### Before Coding
1. Re-read the current code at the fix location
2. Verify the behavior catalog entry is still accurate (code hasn't changed)
3. Understand the full context (what calls this, what this calls)

#### During Coding
4. Make the minimal change that resolves the finding
5. Do NOT refactor surrounding code (even if tempting)
6. Do NOT fix other issues you notice (log them for a future audit)
7. Do NOT change function signatures unless absolutely necessary
8. Preserve existing behavior for all non-affected code paths

#### After Coding
9. Run existing tests to check for regressions
10. Add or update tests for the fixed behavior
11. Verify the fix against the specific user scenario from the finding
12. Check edge cases identified in the behavior catalog

### Minimal Change Principle

The fix should be the **smallest possible change** that resolves the identified behavioral discrepancy. This is critical because:

- Larger changes have larger blast radius
- Each additional change could introduce new behavioral issues
- The behavior audit validated specific behaviors — changing more than necessary invalidates that validation
- Small, focused fixes are easier to review and verify

**Good fix example (Contained):**
```kotlin
// Before: Silent failure
catch (e: Exception) {
    Log.e(TAG, "Save failed", e)
}

// After: User notified
catch (e: Exception) {
    Log.e(TAG, "Save failed", e)
    _uiState.update { it.copy(error = "Failed to save. Please try again.") }
}
```

**Over-engineered fix (avoid):**
```kotlin
// Don't do this — refactoring the entire error handling pattern
// when the finding was about one specific silent failure
sealed class SaveResult {
    data class Success(val item: Item) : SaveResult()
    data class Error(val message: String, val cause: Throwable) : SaveResult()
}
// ... 50 lines of new abstraction
```

## Step 5: Post-Fix Verification

### Verification Checklist Per Fix

- [ ] **Finding resolved:** The specific behavior identified in the audit no longer occurs
- [ ] **Intended behavior confirmed:** The code now does what the developer specified
- [ ] **Edge cases handled:** The edge cases from the behavior catalog are still handled
- [ ] **No regressions:** Existing tests pass, no new test failures
- [ ] **New tests added:** At least one test covers the fixed behavior
- [ ] **Code compiles:** Build succeeds without new warnings

### Re-Audit Modified Areas

After all fixes are applied, run a targeted re-audit:

1. Trace the modified code paths again (same methodology as initial trace)
2. Compare new behavior against the intended behavior
3. Check for any new behavioral issues introduced by the fixes
4. Verify that "Confirmed Correct" findings from the original audit are still correct

### Verification Report Template

```markdown
# Fix Verification Report

## Fixes Applied
| Fix ID | Status | Verification |
|--------|--------|-------------|
| FIX-001 | Applied | Verified — listener now removed in onCleared() |
| FIX-002 | Applied | Verified — state restored after process death |
| FIX-003 | Applied | Verified — user sees error snackbar on save failure |

## Regression Check
- [ ] All existing tests pass
- [ ] No new warnings or errors in build
- [ ] Manual verification of related features

## New Issues Found During Verification
[List any new behavioral issues discovered during re-audit, if any]

## Remaining Items
[List any deferred fixes or items that need future attention]
```

## Common Fix Patterns

### Pattern: Add User Notification for Silent Failure
**Finding type:** Silent data loss, swallowed exception
**Fix:** Add error state emission or event emission in the catch block
**Blast radius:** Contained (single catch block)
**Test:** Verify error state is set when exception is thrown

### Pattern: Add Listener Cleanup
**Finding type:** Leaked Firebase/system listener
**Fix:** Remove listener in `onCleared()` (ViewModel) or `awaitClose` (callbackFlow)
**Blast radius:** Contained (single function)
**Test:** Verify listener is removed after ViewModel cleared

### Pattern: Add Process Death State Preservation
**Finding type:** State not restored after process death
**Fix:** Use `SavedStateHandle` for critical ViewModel state
**Blast radius:** Local (ViewModel + UI reading state)
**Test:** Save state, clear ViewModel, restore, verify state is correct

### Pattern: Fix Navigation Back Stack
**Finding type:** Dead-end screen, back stack corruption
**Fix:** Add `popUpTo` in navigation, handle empty back stack in deep links
**Blast radius:** Local (navigation graph changes)
**Test:** Navigate via deep link, press back, verify correct destination

### Pattern: Add CancellationException Rethrow
**Finding type:** Caught CancellationException in coroutine
**Fix:** Add `if (e is CancellationException) throw e` at the start of catch block
**Blast radius:** Contained (single catch block)
**Test:** Cancel the coroutine, verify it stops executing

### Pattern: Complete State Machine Transitions
**Finding type:** Missing state transition, unreachable state
**Fix:** Add the missing transition handler in the state machine
**Blast radius:** Local (state machine + UI observing state)
**Test:** Trigger the previously missing transition, verify correct state

## Related Skills

- `android-behavior-audit` — Produces the findings that this skill resolves
- `android-behavior-trace` — May need to re-trace after fixes to verify
- `android-testing-patterns` — For creating regression tests for fixes
- `android-app-survey` — If fixes require understanding of broader app structure
