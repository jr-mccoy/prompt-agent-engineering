---
title: "Android Jetpack Compose Debugging & Root Cause Fix"
category: engineering-workflows/workflows
description: "Diagnose, fix, and verify a bug in an Android Jetpack Compose + Firebase + Room app — from a non-technical bug report through evidence-based root-cause analysis, blast-radius assessment, an implemented fix, regression testing, and an atomic commit."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-02
  - QA-01
difficulty: advanced
tags:
  - debugging
  - android
  - jetpack-compose
  - root-cause-analysis
  - firebase
updated: "2026-06-07"
related_prompts:
  - domain-engineering-workflows/workflows/engineering_debugging_root_cause.md
  - domain-engineering-workflows/workflows/engineering_prompt_for_debugging_code.md
  - domain-software-engineering/analysis/feature-design/task_sorting_kotlin_implementation_verifier.md
---

# Android Jetpack Compose Debugging & Root Cause Fix

**Objective:** Systematically diagnose, fix, and verify a bug in an Android Jetpack Compose application (Firebase RTDB/Firestore/Cloud Functions, encrypted Room, complex state) — starting from a non-technical bug description and ending with an evidence-backed root cause, a blast-radius-assessed fix, regression testing, and a clean atomic commit.

**When to use:**
- Triaging an Android/Compose bug reported by a non-technical user.
- A data/sync/UI/auth bug that needs root-cause analysis, not a quick patch.
- Bugs spanning Compose state, ViewModel, Repository, Room, and Firebase layers.
- When you need a disciplined, test-and-commit workflow for the fix.

**When NOT to use:**
- Non-Android or non-Compose codebases (the layer/tooling steps won't apply).
- A language-agnostic debugging flow — use `engineering_prompt_for_debugging_code.md`.
- Post-incident organizational analysis — use `engineering_post_mortem_root_cause_ladder.md`.

**Audience:** Android engineers debugging a Compose + Firebase + Room application.

---

## Inputs / Context

The user supplies:
1. **Bug report** — what they were doing, expected vs. actual behavior, reproduction steps, screenshots/recordings, when it started.
2. **Environment** — device/Android version, online/offline, account state.
3. **Logs and code** — wrap Logcat/crash output in a `<logs>` tag and suspect code in a `<code>` tag (note file paths).
4. **Constraints** — branch policy, Firebase emulator availability, areas off-limits.

If the bug can't be reproduced or evidence is missing, say so and request screenshots/steps/logs before asserting a cause.

---

## Constraints

### Must
- Drive root cause from evidence (Logcat, stack traces, traced data flow) — cite file:line and the failure mechanism.
- State the change **blast radius** before implementing.
- Present solution alternatives (minimal / root-cause / refactored) and wait for confirmation before coding.
- Add tracking/instrumentation and a regression test plan; verify the original bug no longer reproduces.
- Produce an atomic commit with a structured message.

### Must Not
- Guess a root cause without tracing evidence — if you can't reproduce or trace it, say so and request more data.
- Expand scope to unrelated bugs found along the way (note them separately).
- Claim the fix works without running the reproduction steps and regression checks.
- Fabricate log lines, stack traces, or test results.

---

## Phase 1: Bug Discovery & Context Gathering

### Step 1: Understand the User's Experience
Ask clarifying questions one at a time to understand the issue from a user perspective:

**Initial Questions:**
- What were you trying to do when this happened?
- What did you expect to happen?
- What actually happened instead?
- Can you consistently reproduce this? If yes, what exact steps?
- Did this work before? If yes, when did it stop working?

**Visual Context (CRITICAL):**
- If the user has a screenshot or screen recording, request it immediately
- If they can reproduce the issue, ask them to take a screenshot showing the problem
- Screenshots are often more valuable than lengthy text descriptions

**Environmental Context:**
- What device/Android version are you using?
- Are you online or offline when this happens?
- Does this happen right after app launch, or after using the app for a while?
- Have you recently logged in/out or switched accounts?

### Step 2: Translate Non-Technical Description to Technical Symptoms

Based on user description, identify likely technical categories:

**UI Issues:**
- Visual glitches → Compose recomposition, state management
- Wrong data displayed → Data flow, ViewModel, database query
- Crashes on interaction → Exception in event handler, null pointer
- Slow/frozen UI → Main thread blocking, heavy computation

**Data Issues:**
- Data not saving → Firebase write failure, Room transaction issue, permission problem
- Data not loading → Network issue, query problem, null handling
- Wrong data showing → Stale cache, sync conflict, query logic error
- Missing data → Deletion bug, filter/query issue, relationship problem

**Authentication/Authorization:**
- Can't log in → Firebase Auth issue, credential problem
- Wrong permissions → Security rules, authorization logic
- Session expired → Token refresh, timeout issue

**Sync/Offline Issues:**
- Changes not syncing → Network error, conflict resolution, listener not attached
- Offline mode broken → Room database issue, offline persistence config
- Conflicts on sync → Last-write-wins logic, merge strategy

---

## Phase 2: Evidence Collection & Root Cause Analysis

### Step 3: Locate the Bug with Evidence

**A. Check Logcat/Crash Logs:**
```bash
# Search for relevant errors
adb logcat | grep -i "error\|exception\|crash"
```

Look for:
- Stack traces with file paths and line numbers
- Firebase error codes
- Room database errors
- Compose recomposition warnings

**B. Search Codebase Strategically:**

Based on symptom category, search relevant areas:

**For UI Issues:**
```bash
# Find the screen/composable mentioned by user
find . -name "*.kt" -exec grep -l "ScreenName\|ComposableName" {} \;
```

**For Data Issues:**
```bash
# Find ViewModel, Repository, or DAO handling this data
find . -name "*ViewModel.kt" -o -name "*Repository.kt" -o -name "*Dao.kt"
```

**For Firebase Issues:**
```bash
# Find Firebase RTDB/Firestore references
grep -r "Firebase\|firestore\|database()" --include="*.kt"
```

**C. Trace Data Flow:**

Starting from the UI issue, trace backwards:
1. **Composable** → What state is it observing?
2. **ViewModel** → Where does this state come from?
3. **Repository** → What data sources are queried?
4. **Database/Firebase** → What's the actual query/listener?

Document each layer with file paths and line numbers.

### Step 4: Apply Five Whys Root Cause Analysis

For the identified issue, ask "Why?" five times:

**Example Flow:**
1. **Issue:** User sees stale data after sync
2. **Why?** → The UI isn't reacting to database changes
3. **Why?** → The Flow/LiveData isn't emitting new values
4. **Why?** → Room observer isn't triggering on update
5. **Why?** → Update is happening in a transaction that's not being observed
6. **Why (Root Cause)?** → We're using `.update()` instead of DAO method, bypassing Room's observer mechanism

**Document Your Analysis:**
```
Root Cause: [Clear statement of fundamental issue]

Evidence:
- File: [path/to/File.kt]
- Lines: [line numbers]
- Code: [relevant code snippet]

Why This Causes the Bug:
[Explanation of mechanism]

Related Issues This Might Cause:
[Other symptoms from same root cause]
```

---

## Phase 3: Solution Design & Blast Radius Assessment

### Step 5: Assess Change Blast Radius

**CRITICAL: Estimate how many files this fix will touch:**

- **1-3 files (Small blast radius):** 
  - Single bug fix in one component
  - Can implement directly
  
- **4-10 files (Medium blast radius):**
  - Touching multiple layers (UI → ViewModel → Repository)
  - Plan carefully, test thoroughly
  
- **10+ files (Large blast radius):**
  - Architectural change or cross-cutting concern
  - Break into smaller commits if possible
  - Consider if this should be a separate feature branch

**Before proceeding, state the blast radius explicitly.**

### Step 6: Design Solution with Alternatives

Generate 3 solution approaches:

**Solution 1: Minimal Fix**
- What: [Smallest possible change to fix immediate symptom]
- Pros: [Quick, low risk]
- Cons: [May not address root cause, technical debt]
- Files affected: [list]
- Estimated risk: Low/Medium/High

**Solution 2: Root Cause Fix**
- What: [Proper fix addressing underlying issue]
- Pros: [Fixes root cause, prevents future bugs]
- Cons: [More complex, needs more testing]
- Files affected: [list]
- Estimated risk: Low/Medium/High

**Solution 3: Refactored Solution (if applicable)**
- What: [Fix plus improvement to architecture]
- Pros: [Better long-term, improves code quality]
- Cons: [Most complex, highest blast radius]
- Files affected: [list]
- Estimated risk: Low/Medium/High

**Recommendation:** [Choose one with clear rationale]

**Wait for confirmation before implementing.**

---

## Phase 4: Implementation with Safety Checks

### Step 7: Implement Fix Incrementally

**A. Create Feature Branch (if large change):**
```bash
git checkout -b fix/[brief-description-of-bug]
```

**B. Implement fix following Android best practices:**

**For Compose UI fixes:**
- Ensure proper state hoisting
- Use `remember` and `derivedStateOf` appropriately
- Check for recomposition loops
- Verify LaunchedEffect keys are correct

**For ViewModel fixes:**
- Use viewModelScope for coroutines
- Handle errors properly with try-catch
- Update StateFlow/LiveData correctly
- Ensure no memory leaks

**For Repository/Database fixes:**
- Use Room transactions when needed
- Implement proper error handling
- Test both online and offline scenarios
- Verify Firebase security rules compliance

**For Cloud Functions:**
- Update function logic carefully
- Test locally with Firebase emulator if possible
- Consider backward compatibility

**C. Add Defensive Checks:**
```kotlin
// Example: Add null safety where bug occurred
val data = dataState.value ?: run {
    Log.e(TAG, "Unexpected null data in [location]")
    return // or handle gracefully
}
```

### Step 8: Add Instrumentation & Logging

Before completing the fix, add tracking to verify it works:

```kotlin
// Add temporary debugging logs
Log.d(TAG, "Bug fix checkpoint: [what you're checking]")

// Add crash reporting context
FirebaseCrashlytics.getInstance().log("Fixed bug: [brief description]")

// Add analytics event if user-facing
analytics.logEvent("bug_fix_triggered") {
    param("fix_type", "specific_bug_name")
}
```

---

## Phase 5: Testing & Verification

### Step 9: Multi-Level Testing

**A. Unit Tests (if applicable):**
- Test the specific function/method that was fixed
- Test edge cases that caused the bug
- Verify fix doesn't break existing tests

**B. Manual Testing - Bug Reproduction:**
1. Follow the exact steps the user reported
2. Verify the bug NO LONGER occurs
3. Try variations of those steps
4. Test in different states (online/offline, fresh install, with data)

**C. Regression Testing:**

Test areas that COULD be affected by your changes:

**If you changed database code:**
- Test all CRUD operations on that table
- Test queries that use modified fields
- Test offline sync and conflict resolution

**If you changed UI code:**
- Test different screen sizes/orientations
- Test with different data states (empty, loading, error, success)
- Test navigation to/from this screen

**If you changed ViewModel/Repository:**
- Test all features that use this data
- Test error scenarios
- Test state restoration (process death)

**D. Create Regression Test Checklist:**
```
Manual Test Results:
✓ Bug reproduction steps - FIXED
✓ Feature X still works
✓ Feature Y still works
✓ Offline mode works
✓ Data syncs correctly
✗ Issue found: [if any]
```

### Step 10: Verify No New Issues Introduced

**Check for common regression patterns:**

**Memory Leaks:**
- ViewModels properly cleared?
- Firebase listeners detached?
- Compose remember keys correct?

**Performance:**
- No new blocking on main thread?
- No excessive recompositions?
- Database queries still efficient?

**State Issues:**
- State survives configuration changes?
- No race conditions introduced?
- Proper error state handling?

**Use Android Studio tools:**
- Layout Inspector (for Compose issues)
- Profiler (for performance)
- Database Inspector (for Room issues)

---

## Phase 6: Commit & Documentation

### Step 11: Create Atomic Commit

**Commit Message Format:**
```
fix: [Brief description of bug fixed]

Problem:
[What the user experienced - non-technical description]

Root Cause:
[Technical root cause identified]

Solution:
[What was changed and why]

Testing:
- [Test scenario 1] ✓
- [Test scenario 2] ✓
- [Regression test 3] ✓

Files Changed:
- [file1]: [what changed]
- [file2]: [what changed]

Blast Radius: [Small/Medium/Large]
Risk Level: [Low/Medium/High]
```

**Example:**
```
fix: User profile not updating after edit

Problem:
Users reported that changes to their profile (name, bio) weren't 
saving. They could edit and click save, but on returning to the 
profile screen, old data was shown.

Root Cause:
ProfileRepository.updateProfile() was using direct Firestore update
instead of going through Room cache, causing local state to be stale.
Room observers weren't triggered, so UI kept showing old cached data.

Solution:
- Changed updateProfile to write to both Room and Firestore
- Updated Room first, then Firestore in background
- Added error handling for Firestore write failures
- Added offline support using Room as source of truth

Testing:
- Profile edit with network ✓
- Profile edit offline ✓
- Navigation away and back shows new data ✓
- Sync works after coming back online ✓
- Other profile features (image upload, etc) unaffected ✓

Files Changed:
- ProfileRepository.kt: Added dual-write logic
- ProfileDao.kt: Added update method with proper observer
- ProfileViewModel.kt: Updated error handling
- ProfileScreen.kt: Added offline indicator

Blast Radius: Medium (3 files in data layer, 1 in UI)
Risk Level: Low (well-tested, atomic change)
```

### Step 12: Commit and Push

```bash
# Stage only the relevant files
git add [specific files changed for this fix]

# Commit with detailed message
git commit -m "[commit message from above]"

# Push to remote
git push origin [branch-name]
```

**For multi-agent environments (if applicable):**
```bash
# Ensure you're committing only your changes
git status # Review what's staged
git diff --cached # Review actual changes

# Commit with clear message for other agents
git commit -m "fix: [bug] - Agent [name] - See message for details"
```

---

## Success Criteria Checklist

Before considering the bug fixed, verify ALL of these:

**Diagnosis:**
- [ ] Root cause identified with evidence (file, line, mechanism)
- [ ] Five Whys analysis completed and documented
- [ ] Blast radius assessed and acceptable

**Implementation:**
- [ ] Fix implements recommended solution
- [ ] Code follows Android/Compose best practices
- [ ] Error handling added
- [ ] Defensive checks in place
- [ ] Instrumentation/logging added for verification

**Testing:**
- [ ] Original bug no longer reproduces
- [ ] All regression tests pass
- [ ] No new issues introduced
- [ ] Performance not degraded
- [ ] Works online and offline

**Documentation:**
- [ ] Commit message comprehensive and clear
- [ ] Changes documented in code comments if complex
- [ ] User-facing changes noted (if applicable)

**Git Hygiene:**
- [ ] Only relevant files staged
- [ ] Commit is atomic (single logical change)
- [ ] Branch name descriptive (if using branches)

---

## Edge Case Handling

**If you can't reproduce the bug:**
- State this clearly
- Ask for more information (screenshot, video, steps)
- Check logs for historical errors matching description
- Implement defensive fixes based on most likely cause
- Add extensive logging to catch it next time

**If the fix requires Firebase changes:**
- Test with Firebase Emulator first
- Update Security Rules carefully
- Document rule changes in commit message
- Consider backward compatibility

**If the fix is too large (20+ files):**
- Explain why it's large
- Break into multiple smaller commits if possible
- Suggest creating a feature branch
- Request review of the plan before implementing

**If you find related bugs while fixing:**
- Note them separately
- Fix the original bug first
- Create new tasks for related bugs
- Don't expand scope without discussion

---

## Output Format

After completing all phases, provide a summary:

```
BUG FIX SUMMARY
===============

Original Issue:
[User's description]

Root Cause:
[Technical diagnosis]

Solution Implemented:
[What was changed]

Files Modified:
- [file 1]: [changes]
- [file 2]: [changes]

Testing Results:
✓ [Test 1]
✓ [Test 2]
✓ [Test 3]

Commit Details:
Branch: [branch name]
Commit: [commit hash]
Message: [first line of commit message]

Verification:
[How to verify the fix is working]

Next Steps:
[If any follow-up needed]
```

---

**Remember:**
- Screenshots are 50% of debugging - always request/provide them
- Blast radius guides risk - know how many files you'll touch before starting
- Root cause beats symptoms - use Five Whys to find the real issue
- Testing prevents regressions - test both the fix AND related functionality
- Commit messages are documentation - be thorough for future you

---

## False-Positive Prevention

❌ **DON'T:**
- Don't declare a root cause without a traced path (Logcat line, stack frame, or data-flow step) — if you can't reproduce it, say so.
- Don't start coding before stating blast radius and getting confirmation on the chosen solution.
- Don't claim "FIXED" without running the user's reproduction steps and the regression checks.
- Don't fabricate log output, stack traces, or test results to fill the template.

✅ **DO:**
- Cite file:line and the failure mechanism for the root cause.
- Trace UI → ViewModel → Repository → Room/Firebase to locate the real source.
- Verify online and offline behavior and check for memory leaks / extra recompositions.
- Note unrelated bugs separately instead of expanding scope.

---

## Verification

- [ ] Root cause identified with evidence (file, line, mechanism); Five Whys documented.
- [ ] Blast radius assessed before implementation.
- [ ] Solution alternatives presented; chosen one confirmed before coding.
- [ ] Instrumentation/tracking added; baseline captured.
- [ ] Original bug no longer reproduces; regression checks pass (online and offline).
- [ ] No new leaks, recomposition storms, or main-thread blocking introduced.
- [ ] Atomic commit with structured message; only relevant files staged.
- [ ] No fabricated logs, traces, or test results.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Frames the diagnose-fix-verify goal across the app's layers.
- **ST-02 (Structured Sequential Instructions):** Six gated phases from discovery to commit.
- **RT-02 (Multi-Dimensional Analysis):** Traces UI, state, data, sync, and auth layers in parallel.
- **QA-02 (Adversarial Self-Critique):** Regression sweep and "what could break" checks stress the fix.
- **QA-01 (Self-Verification):** Success-criteria checklist confirms the bug is truly resolved.

---

## Related Prompts

- `domain-engineering-workflows/workflows/engineering_debugging_root_cause.md` — Language-agnostic root-cause workflow.
- `domain-engineering-workflows/workflows/engineering_prompt_for_debugging_code.md` — Stuck-bug brainstorming with tracking metrics.
- `domain-software-engineering/analysis/feature-design/task_sorting_kotlin_implementation_verifier.md` — Verify Kotlin/Android implementation quality.