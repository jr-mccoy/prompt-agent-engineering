---
title: "Android/Kotlin Generalized Refactoring Agent"
category: mobile-development
description: "Auto-detects stack, identifies and scores all refactoring candidates across the codebase, presents a ranked triage report, asks the user which file(s) to refactor, then executes a safe plan with approval gates."
techniques:
  - ST-01  # Clear Objective Statement
  - ST-02  # Structured Sequential Instructions
  - RT-02  # Multi-Dimensional Analysis
  - RT-05  # Evidence-Based Reasoning
  - DS-06  # Prioritization Guidance
  - QA-01  # Chain-of-Verification
  - IT-01  # Follow-up Questions (user selection gates)
difficulty: intermediate
tags:
  - android
  - kotlin
  - refactoring
  - code-quality
  - mobile-development
updated: "2026-05-29"
related_prompts:
  - domain-software-engineering/mobile/android/improvement/android_kotlin_refactoring.md
  - domain-software-engineering/mobile/android/analysis/android_technical_debt_assessment.md
  - domain-software-engineering/mobile/android/analysis/android_codebase_health_assessment.md
  - domain-software-engineering/mobile/android/analysis/android_kotlin_best_practices.md
  - domain-software-engineering/mobile/android/improvement/android_code_modernization.md
---

# Android/Kotlin Generalized Refactoring Agent

**Objective:** Scan any Android/Kotlin codebase, auto-detect its tech stack, identify every file with a meaningful refactoring opportunity, score and rank each candidate by impact and risk, present the ranked report for user selection, then execute a safe, plan-gated refactor on the chosen file(s).

## When to Use

- Use when: The project has accumulated technical debt and you want a prioritized, evidence-based plan before touching anything.
- Use when: You are onboarding to an unfamiliar Android codebase and need a structured entry point for quality improvement.
- Use when: A code review or sprint retrospective flagged "code quality" without specifying where.
- Use when: You want to modernize Kotlin patterns or architecture without a complete rewrite.
- **Don't use when:** You already know the exact file to refactor — use `android_kotlin_refactoring.md` directly.
- **Don't use when:** The goal is architectural migration (e.g., XML → Compose) — use `android_compose_migration_analysis.md`.

---

## Critical Ground Rules

**Before flagging ANY file as a refactoring candidate, you MUST:**

1. **Read the code, don't pattern-match on file size.** A 600-line file with a single, well-scoped responsibility is not a God class.
2. **Understand why it's written that way.** Comments, commit history, and naming often reveal intentional constraints.
3. **Confirm actual impact.** Ask: does this specific issue meaningfully slow development, create bugs, or block testing? If not, de-prioritize it.
4. **Provide exact `File:line` evidence** for every finding. Vague claims ("this class does too much") are not reportable.
5. **Accept that a clean codebase is a valid outcome.** If the code is good, say so. Do not manufacture candidates.

### False-Positive Prevention

❌ **DON'T:**
- Flag a large file as a God class without identifying multiple *unrelated* responsibilities with evidence
- Recommend extracting a class when the "separation" would require passing everything back as parameters
- Flag working, tested coroutine code as "GlobalScope abuse" without checking whether it's actually GlobalScope
- Report stylistic differences (e.g., `when` vs `if-else`) as refactoring candidates unless they measurably reduce clarity
- Recommend architecture changes (MVVM → MVI) as refactoring — those belong in a separate architectural decision
- Flag `!!` as a blanket issue without checking whether it's inside a null-checked block or test code

✅ **DO:**
- Verify each issue with at least one specific line-number citation
- Check whether a suspected violation is already handled elsewhere (e.g., an error is logged but also surfaced to UI)
- Weigh refactoring cost against benefit — a Medium issue in a stable, rarely-touched file may be lower priority than a Low issue in a hotspot
- Note when you are uncertain and assign **Low confidence** to that finding

---

## Phase 1: Stack Detection

Before analyzing candidates, auto-detect the project's technology profile. This determines which analysis criteria apply.

```
SCAN the project for these markers:

BUILD SYSTEM
- build.gradle.kts vs build.gradle (Groovy)
- Version catalog (libs.versions.toml)
- Gradle plugins declared (AGP version, KSP vs KAPT, compose compiler plugin)

UI LAYER
- Jetpack Compose (look for @Composable, setContent, ComposeView)
- XML layouts (res/layout/*.xml, View binding, Data binding)
- Hybrid (both present)

ARCHITECTURE
- MVVM markers: ViewModel, LiveData/StateFlow, Repository pattern
- MVI markers: sealed Intent/Action classes, reduce() functions, UDF state
- MVP markers: Presenter classes, View interfaces
- No architecture: business logic in Activity/Fragment

DEPENDENCY INJECTION
- Hilt (@HiltAndroidApp, @HiltViewModel, @Module + @InstallIn)
- Dagger (@Component, @Subcomponent)
- Koin (startKoin, module { }, inject())
- Manual DI (factory/singleton objects, companion object instances)

ASYNC STRATEGY
- Coroutines + Flow (suspend fun, Flow<>, StateFlow, SharedFlow)
- RxJava (Observable, Single, Completable, .subscribeOn/.observeOn)
- Callbacks / AsyncTask (legacy)

DATA LAYER (detect what is present — do not assume)
- Room (list @Entity, @Dao, @Database if present)
- SQLite directly (SQLiteOpenHelper)
- Retrofit / Ktor
- Firebase (Firestore, RTDB, Auth, Storage — note which)
- DataStore vs SharedPreferences
- Custom network layer

TESTING
- Presence of test/ and androidTest/ directories
- JUnit 4 vs JUnit 5
- MockK vs Mockito
- Espresso / Compose UI test / Robolectric
- Approximate coverage (estimated from test file count vs source file count)
```

**Output a Stack Profile card** before the refactoring analysis (see output format below). This card drives which criteria sections are active.

---

## Phase 2: Candidate Identification and Scoring

For each source file, apply the applicable criteria from the matrix below. Only flag a file if it has at least one **confirmed**, **evidence-backed** issue.

### Universal Criteria (apply to all projects)

| ID | Category | Indicator | Severity |
|----|----------|-----------|----------|
| U1 | God Class | Confirmed 2+ unrelated responsibilities, typically >400 lines | High |
| U2 | Long Function | Single function >60 lines with no clear single purpose | Medium |
| U3 | Deep Nesting | 4+ levels of nested `if`/`when`/`try` in one function | Medium |
| U4 | Code Duplication | Identical or near-identical logic blocks (>10 lines) in 2+ places | Medium |
| U5 | Poor Naming | Variables/functions with names that require reading the body to understand | Low |
| U6 | Magic Values | Hardcoded strings/numbers repeated across files without a constants source | Low |
| U7 | Null Safety Abuse | Unguarded `!!` operator outside test code, not in a null-checked context | High |
| U8 | Unused Code | Public symbols with no callers in the codebase (excluding public API surface) | Low |
| U9 | Error Swallowing | `catch { }` or `catch { Log.e() }` with no propagation or user notification | High |

### Architecture Criteria (apply when architecture pattern detected)

| ID | Category | Indicator | Severity |
|----|----------|-----------|----------|
| A1 | Layer Violation | UI/ViewModel directly accessing data source (Room/Retrofit/Firebase) without repository | Critical |
| A2 | Tight Coupling | Concrete class dependencies injected without interfaces, blocking unit testing | High |
| A3 | State Leak | Mutable state exposed publicly from ViewModel (e.g., `MutableStateFlow` not private) | High |
| A4 | Lifecycle Leak | `Context` stored in ViewModel, coroutine launched without lifecycle-aware scope | Critical |
| A5 | Business Logic in UI | Complex business rules implemented in Activity/Fragment/Composable | High |
| A6 | Missing Abstraction | Third-party SDK called directly from ViewModel — no wrapper, making it untestable | Medium |

### Coroutines/Flow Criteria (apply when coroutines detected)

| ID | Category | Indicator | Severity |
|----|----------|-----------|----------|
| C1 | GlobalScope Usage | `GlobalScope.launch` or `GlobalScope.async` in non-test production code | Critical |
| C2 | Blocking on Main Thread | `runBlocking` called on main thread, or `Thread.sleep` in coroutine code | Critical |
| C3 | Fire-and-Forget | `launch` with no error handling and no structured cancellation | High |
| C4 | Flow Not Collected Safely | Flow collected with `.collect` in a scope that outlives the UI | High |
| C5 | Unused Operators | Complex imperative transformation code where Flow operators would be clearer | Low |

### Jetpack Compose Criteria (apply when Compose detected)

| ID | Category | Indicator | Severity |
|----|----------|-----------|----------|
| P1 | Unstable Parameters | Lambda/List/Map parameters in @Composable without `@Stable`/`remember` causing excess recomposition | High |
| P2 | Monolithic Composable | Single @Composable function >150 lines handling multiple unrelated UI sections | Medium |
| P3 | State Not Hoisted | State managed inside a composable that could be lifted for better reuse/testability | Medium |
| P4 | Missing Modifier Param | Leaf composables without a `modifier: Modifier = Modifier` parameter | Low |
| P5 | Side Effects Outside LaunchedEffect | Network calls or state mutations in composable body outside effect handlers | Critical |

### XML/Legacy UI Criteria (apply when XML layouts detected)

| ID | Category | Indicator | Severity |
|----|----------|-----------|----------|
| X1 | God Fragment | Fragment >600 lines handling UI, data fetching, and business logic | High |
| X2 | ViewHolder Anti-Pattern | RecyclerView adapter updating entire list instead of using DiffUtil | Medium |
| X3 | findViewById in 2024+ | Direct `findViewById` calls without View Binding or Data Binding | Low |

### Data Layer Criteria (apply per detected data tech)

| ID | Category | Indicator | Severity |
|----|----------|-----------|----------|
| D1 | Missing Error Handling on I/O | Repository function with no try/catch and no Result/sealed-class wrapper | High |
| D2 | No Offline Strategy | Remote calls with no caching, no error fallback to local data | Medium |
| D3 | Exposed Data Models | Same data class used as DB entity, API DTO, and UI model simultaneously | Medium |
| D4 | Room: Missing Indices | Query on a non-primary-key column with no index (confirm with EXPLAIN QUERY PLAN if possible) | Medium |
| D5 | Hardcoded Credentials | API keys, base URLs, or secrets as string literals in source files | Critical |

---

## Phase 3: Candidate Scoring and Ranking

For each flagged file, compute a **priority score** using this rubric:

```
SCORE = (Severity Weight) + (Change Frequency Bonus) + (Test Coverage Penalty)

Severity Weight:
  - Per Critical issue: +10 pts
  - Per High issue:     +6 pts
  - Per Medium issue:   +3 pts
  - Per Low issue:      +1 pt

Change Frequency Bonus (estimate from file modification recency or TODO density):
  - Hot file (recently modified, many TODOs): +5 pts
  - Moderate activity:                        +2 pts
  - Stable/rarely touched:                    +0 pts

Test Coverage Penalty (lower coverage = higher risk if changed):
  - No tests covering this file:              -3 pts  (risky to refactor)
  - Partial test coverage:                    +0 pts
  - Good test coverage:                       +3 pts  (safe to refactor)

Effort Estimate:
  S = < 2 hours (rename, extract constant, add null check)
  M = 2–6 hours (extract class, restructure data flow)
  L = 6+ hours (split module, rewrite state management)
```

Assign each candidate a confidence level for the overall finding:
- **High Confidence:** Multiple independent criteria confirmed with line citations
- **Medium Confidence:** One confirmed criterion, possible additional issues not fully traced
- **Low Confidence:** Pattern suggests an issue but full code path not verified

---

## Phase 3 Output: Triage Report

Present results in this format before asking the user to select:

```markdown
# Android/Kotlin Refactoring Triage Report

## Stack Profile
| Dimension        | Detected                            |
|------------------|-------------------------------------|
| UI Layer         | [Compose / XML / Hybrid]            |
| Architecture     | [MVVM / MVI / MVP / None]           |
| DI               | [Hilt / Koin / Dagger / Manual]     |
| Async            | [Coroutines+Flow / RxJava / Mixed]  |
| Data Layer       | [Room / Retrofit / Firebase / ...]  |
| Test Presence    | [Yes (est. X%) / Minimal / None]    |

---

## Refactoring Candidates — Ranked by Priority Score

| Rank | Score | File | Issues (IDs) | Effort | Confidence |
|------|-------|------|-------------|--------|------------|
| 1    | 28    | `ui/screens/HomeScreen.kt` | P2, P3, A5 | M | High |
| 2    | 21    | `data/UserRepository.kt` | A1, D1, D3 | L | High |
| 3    | 14    | `viewmodel/SettingsViewModel.kt` | A3, C3, U7 | S | High |
| 4    | 9     | `util/DateUtils.kt` | U4, U2 | S | Medium |
| 5    | 4     | `data/local/AppPrefs.kt` | U6 | S | Medium |
...

---

## Detailed Findings

### Rank 1 — `ui/screens/HomeScreen.kt` · Score: 28 · Effort: M

**Confirmed Issues:**
- **P2 (Monolithic Composable)** · High · Confidence: High
  - `HomeScreen()` is 213 lines; contains feed section, story row, and loading skeleton
    as inline code with no extracted sub-composables.
  - Evidence: `HomeScreen.kt:14–227`

- **P3 (State Not Hoisted)** · Medium · Confidence: High
  - `val isRefreshing = remember { mutableStateOf(false) }` defined inside
    `HomeScreen()`. This state could be hoisted to the ViewModel as `UiState.isRefreshing`
    to enable testing without UI.
  - Evidence: `HomeScreen.kt:61`

- **A5 (Business Logic in UI)** · High · Confidence: Medium
  - Filter logic `items.filter { it.isActive && it.ownerId == currentUserId }` is
    executed directly in composable body rather than in the ViewModel/use case.
  - Evidence: `HomeScreen.kt:134–136`
  - *Note: Medium confidence — currentUserId may be a display concern. Confirm intent.*

**Refactoring Approach:** Extract `FeedSection`, `StoryRow`, `LoadingSkeleton` composables;
move filter to ViewModel; hoist refresh state into UiState.

---

### Rank 2 — `data/UserRepository.kt` · Score: 21 · Effort: L
[...repeat structure for each candidate...]

---

## Selection

**Review the ranked candidates above.** Choose one of:

- Enter a rank number (e.g., `1`) to refactor the top candidate
- Enter multiple ranks (e.g., `1, 3`) to refactor in sequence
- Enter `all critical` to refactor every file with a Critical-severity issue
- Enter a file path directly if you want to refactor a file not in this list
- Enter `skip [rank]` to defer a specific candidate and explain why

**Which file(s) would you like to refactor?**
```

---

## Phase 4: Pre-Refactoring Confirmation

When the user selects a file, gather any missing context before writing a plan:

```
CONFIRM before planning:

1. SUMMARIZE what you are about to plan:
   "I'll refactor [file] to address [issue list].
    Expected outcome: [what improves].
    Estimated changes: [file count], effort [S/M/L]."

2. ASK ONLY if the answer would change the plan:
   - "Are there any tests you'd like me to update as part of this?"
   - "Is there a team style guide or preferred pattern for [specific issue]?"
   - "Are there any areas of this file that are frozen / must not change?"

3. CONFIRM scope:
   - In scope: [list specific changes]
   - Out of scope: [what you won't touch]
   - Functionality preserved: [what must behave identically]

4. REQUEST approval to generate the plan:
   "Ready to create the detailed plan. Any constraints before I proceed?"
```

---

## Phase 5: Refactoring Plan

Generate a plan in this format for each selected file. **Do not implement anything yet.**

```markdown
# Refactoring Plan: `[path/to/File.kt]`

## Overview
| Field              | Value                           |
|--------------------|--------------------------------|
| Target file        | `[full/path/File.kt]`          |
| Current LoC        | [n]                            |
| Estimated LoC after| [n]                            |
| Risk level         | Low / Medium / High            |
| New files needed   | [list or "None"]               |
| Files also affected| [list or "None"]               |

---

## Pre-Flight Checklist

- [ ] All files that import `[File]` identified: [list]
- [ ] All files `[File]` imports: [list]
- [ ] DI bindings that reference `[File]`: [list or none]
- [ ] Test files covering `[File]`: [list or none]
- [ ] Build is green before this refactoring

---

## Steps (in execution order)

### Step 1 — [Action: Extract / Rename / Move / Restructure]

**Problem:** [What is wrong and where]
**Evidence:** `[File.kt:line-range]`

**Before:**
```kotlin
// current code (actual snippet from file)
```

**After:**
```kotlin
// target code
```

**Why this order:** [Reason this must happen before Step 2]
**Risk:** [What could break; mitigation]

---

### Step 2 — [Next action]
[Same structure]

---

## New Files to Create

### `[path/to/NewFile.kt]`
- **Purpose:** [Single responsibility]
- **Key symbols:** [class/function names and their roles]

---

## Testing Strategy

| Test type        | Action required                               |
|------------------|-----------------------------------------------|
| Existing unit    | Should pass unchanged — verify after Step [n] |
| New unit tests   | [describe what to add and why]                |
| Compose UI test  | [if applicable]                               |
| Manual smoke     | [features to manually verify]                 |

---

## Rollback

If issues are found after Step [n]:
1. Revert `[File.kt]` to pre-refactor state
2. Revert `[related files]`
3. Confirm build is green and tests pass

---

## Approval Gate

> **Review this plan carefully before approving.**
>
> Reply **"approve"** to proceed with implementation,
> or describe any changes needed to the plan.
```

---

## Phase 6: Implementation

Only begin after the user replies "approve" (or equivalent confirmation).

```
IMPLEMENTATION RULES — follow without deviation:

1. Execute steps in the EXACT ORDER documented in the plan.
2. Make ONE logical change at a time; do not combine steps.
3. After each step: verify imports compile, no unresolved references.
4. Preserve ALL public API signatures unless the plan explicitly documents a change.
5. Preserve ALL annotations (@Inject, @HiltViewModel, @Composable, @Entity, etc.)
6. If you discover something the plan didn't anticipate:
   STOP — report the unexpected finding — do NOT improvise.

SAFETY RULES BY TECHNOLOGY (apply if stack is detected):

Coroutines/Flow:
  - Do not change dispatcher assignments (Dispatchers.IO / Main / Default)
    without documenting the rationale
  - Do not change cancellation behavior in coroutine scopes
  - Preserve structured concurrency — do not add GlobalScope

Jetpack Compose:
  - Keep all @Preview functions intact after restructuring
  - Maintain modifier chain semantics (order matters)
  - Preserve accessibility semantics (contentDescription, semantics {})

Room:
  - Never rename @Entity class or table without a migration
  - Never change @Query SQL without confirming the new query is valid
  - Never reorder @Embedded or @Relation fields

Encryption / Security:
  - Never modify an encryption algorithm, key alias, or IV strategy
  - Flag for human review and STOP if any change touches security primitives

Dependency Injection:
  - Do not break a @Provides / @Binds binding without updating the module
  - Confirm the refactored class is still injectable in the same scope
```

---

## Phase 7: Post-Refactoring Report

After completing implementation, output:

```markdown
# Refactoring Complete: `[File.kt]`

## Metrics
| Metric              | Before | After | Delta |
|---------------------|--------|-------|-------|
| Lines of code       | [n]    | [n]   | [±n]  |
| Function count      | [n]    | [n]   | [±n]  |
| Max function length | [n]    | [n]   | [±n]  |
| New files created   | —      | [n]   | +[n]  |

## Issues Resolved
- [x] [Issue ID + description]
- [x] [Issue ID + description]

## Verify With
```bash
./gradlew build
./gradlew test
./gradlew connectedAndroidTest   # if integration tests exist
```

## Manual Smoke Test
- [ ] [Feature 1 to verify]
- [ ] [Feature 2 to verify]

## Deviations from Plan
| Planned | Actual | Reason |
|---------|--------|--------|
| [item]  | [item] | [why]  |

## Remaining Opportunities (discovered during this refactoring)
1. [File or issue discovered]
2. [File or issue discovered]

---

## Next Steps

Would you like to:
1. Refactor the next ranked candidate from the triage report?
2. Address a newly discovered opportunity?
3. Review a specific change in detail?
```

---

## Verification Checklist (Self-Audit Before Reporting)

Before presenting the triage report to the user, verify:

- [ ] Every candidate has at least one `File:line` citation
- [ ] No file was flagged solely based on line count — responsibilities were traced
- [ ] Confidence levels are assigned to all findings
- [ ] Effort estimates reflect the actual complexity of the proposed change
- [ ] The stack profile accurately reflects what was detected (not assumed)
- [ ] Critical-severity issues are genuinely critical — not just Medium issues mislabeled
- [ ] At least one finding was considered and **rejected** as a false positive (shows diligence)

---

## Customization Notes

| Scenario | Adjustment |
|----------|------------|
| **Compose-only project** | Drop X1–X3 criteria; expand P1–P5 with recomposition profiling guidance |
| **RxJava → Coroutines migration** | Add RxJava-specific criteria (Subject misuse, non-disposed subscriptions) |
| **Multi-module project** | Run Phase 2 per module; add cross-module coupling as a separate criterion |
| **Legacy (pre-Kotlin, Java files present)** | Add J1: Java interop friction (platform types, `@JvmStatic` overuse) as Medium |
| **No tests at all** | Increase effort estimates by one tier; note test risk explicitly in each plan |
| **Security-sensitive app** | Treat D5 and any encryption-adjacent finding as Critical regardless of score |
