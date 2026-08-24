---
title: "Audit a Vibe-Coded Android Codebase for Fragile / Sprawling AI Patterns"
category: software-engineering/vibe-coding-rescue/android
description: "Systematic audit of an AI-generated Android codebase for the specific fragility and sprawl patterns AI tends to introduce — duplicated screens and repositories, dead components, mixed state-management approaches, deprecated APIs (AsyncTask, startActivityForResult, legacy permissions), lifecycle violations, leaked Contexts, force-unwraps, unhandled coroutine exceptions, Compose recomposition smells, Hilt scope errors. Produces a severity-tiered findings report with file:line evidence, AI-pattern category, and concrete fix direction. Refuses keyword-match findings."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - DS-01
  - RT-05
  - RT-07
  - QA-01
  - QA-04
difficulty: advanced
tags:
  - vibe-coding
  - android
  - code-audit
  - kotlin
  - compose
  - hilt
  - coroutines
  - lifecycle
  - fragility
updated: "2026-05-17"
related_prompts:
  - domain-software-engineering/vibe-coding-rescue/android/android_viberescue_wall_diagnosis.md
  - domain-software-engineering/vibe-coding-rescue/android/android_viberescue_security_privacy_audit.md
  - domain-software-engineering/vibe-coding-rescue/android/android_viberescue_fix_prioritization.md
  - domain-software-engineering/vibe-coding-rescue/viberescue_security_audit.md
  - domain-software-engineering/mobile/android/analysis/android_codebase_health_assessment.md
  - domain-software-engineering/mobile/android/analysis/ai_code_review_android.md
---

# Audit a Vibe-Coded Android Codebase for Fragile / Sprawling AI Patterns

**Purpose:** AI-generated Android code accumulates a specific class of fragility that conventional code review misses: duplicated screens introduced because the AI didn't search for existing ones, mixed state-management (LiveData + StateFlow + RxJava + plain callbacks), deprecated APIs the AI knows about but uses inconsistently, lifecycle / coroutine scope violations that don't crash but leak, Compose state that lives in the wrong place, and Hilt bindings that overlap or conflict. This audit runs against those patterns, produces findings with file + line evidence and an AI-pattern category, and refuses to report findings without tracing actual code paths.

**When to use:**
- After running `android_viberescue_wall_diagnosis.md` and the primary mode is A1–A6, A9, A10, or A11.
- Before running `android_viberescue_fix_prioritization.md` (which depends on this output).
- When you want a complete fragility picture before deciding what to fix and what to delete.

**Don't use when:** The app's primary issue is security (run `android_viberescue_security_privacy_audit.md` instead — it covers some of the same ground from a security angle, and you don't want to double-report). Both audits can run, but security comes first if A7 or A8 was diagnosed.

**Audience:** The engineer or a trusted reviewer. Output is a findings report ready to feed into the prioritization prompt.

**Agent portability note:** This prompt is written for any coding agent (Claude Code, Codex, Cursor, etc.). When you see "read the file at X" or "search the codebase for Y," use whatever file-reading and search capabilities your agent provides.

---

## Inputs Required

1. **Project root path** (absolute path to the repo).
2. **Build configuration.** Path to `build.gradle.kts` or `build.gradle` (app-level and project-level). `minSdk`, `targetSdk`, `compileSdk`, AGP version, Kotlin version, Compose Compiler version (if applicable).
3. **Tech stack declaration.** UI toolkit (Compose / XML / mixed), DI (Hilt / Koin / manual / none), async (coroutines / RxJava / mixed), persistence (Room / SQLite / DataStore / SharedPreferences / mixed), networking (Retrofit / OkHttp / Ktor / other).
4. **Modules.** Single-module or multi-module? If multi, the module list.
5. **Optional: wall-diagnosis output.** If `android_viberescue_wall_diagnosis.md` was run, paste its primary + secondary modes — the audit will prioritize categories accordingly.
6. **Optional: test posture.** Unit tests, instrumentation tests, Compose UI tests — present yes/no/coverage.

---

## Instructions

### Step 1 — Establish scope and evidence rule

Audit scope is the entire codebase under the project root, with these passes:

- Read `build.gradle(.kts)` files (app + project + module-level).
- Read `AndroidManifest.xml` for every module.
- Map the source tree: list packages, count files per package, identify entry points (Application class, Activities with LAUNCHER intent filter, exported components).
- Identify the DI graph entry points (Hilt `@HiltAndroidApp`, `@AndroidEntryPoint` annotations).

Every finding MUST cite a specific file path and line range. No findings without evidence. If a finding can't be traced to a specific file:line, it's a scope gap, not a finding.

### Step 2 — Run each fragility category

For each category below, scan the codebase and collect findings. Each finding gets: file, line range, evidence snippet, AI-pattern category, severity, confidence, fix direction.

#### 2.1 Duplication and sprawl
- Multiple Activities/Fragments/Composables that render very similar UIs (look for near-identical layout files, near-identical Composable bodies).
- Multiple ViewModels per screen (look for `*ViewModel.kt` files where two could be consolidated).
- Multiple repositories for the same data domain.
- Multiple Hilt modules providing the same dependency (will cause runtime errors or "lucky" wins).
- Dead components: Activities/Services/Receivers declared in manifest but never referenced from code; Composables defined but never called.
- Three or more navigation paths between the same pair of screens.

#### 2.2 Mixed and deprecated APIs
- `AsyncTask` usage anywhere (deprecated in API 30).
- `startActivityForResult` / `onActivityResult` usage (use Activity Result API).
- `requestPermissions` / `onRequestPermissionsResult` (use `ActivityResultContracts.RequestPermission`).
- `findViewById` mixed with ViewBinding mixed with Compose in the same module.
- `Handler()` / `Handler(Looper.getMainLooper())` mixed with coroutines for the same kind of work.
- Old `support` library imports (`android.support.*`) alongside AndroidX.
- `LocalBroadcastManager` (deprecated; use LiveData/Flow/an event bus).
- Old camera APIs (`android.hardware.Camera`) instead of CameraX.

#### 2.3 Lifecycle violations
- Listeners / observers registered in `onCreate` / `onResume` and never unregistered in matching teardown.
- `LiveData.observeForever` calls without a matching `removeObserver`.
- `Flow.collect` outside a `lifecycleScope` / `viewModelScope` / `repeatOnLifecycle` block.
- Static references to Activity, Fragment, View, or anything holding a Context.
- Storing Activity Context in singletons (vs Application Context).
- Inner classes (especially `Handler`, `AsyncTask`, `Runnable`) holding implicit Activity references.
- `onSaveInstanceState` / `onRestoreInstanceState` absent or incomplete for non-trivial state.

#### 2.4 Coroutine and threading
- `GlobalScope.launch` anywhere.
- `CoroutineScope(Dispatchers.*)` constructed ad-hoc (instead of `viewModelScope` / `lifecycleScope`).
- `runBlocking` in UI code.
- I/O on main thread (network, disk, database) — look for direct calls outside `Dispatchers.IO`.
- Missing `try/catch` or `CoroutineExceptionHandler` on top-level coroutines that can throw.
- `Job` references without cancellation paths.
- `Flow` operators (`shareIn`, `stateIn`) without scope or sharing strategy specified.

#### 2.5 Compose recomposition smells
- `remember { mutableStateOf(...) }` for state that should be hoisted to a ViewModel.
- ViewModels exposing both `LiveData<T>` and `StateFlow<T>` for the same data.
- `mutableStateListOf` / `mutableStateMapOf` rebuilt on every recomposition.
- Lambdas allocated in composable arguments without `remember` where stability matters.
- `derivedStateOf` missing where it would prevent recomposition cascades.
- Side effects (`LaunchedEffect`, `DisposableEffect`) keyed on `Unit` when they should re-trigger on input changes.
- Modifier chains rebuilt on every recomposition (no `remember`).

#### 2.6 Null safety and Kotlin idioms
- Force unwraps (`!!`) outside of test code — every one is a candidate finding (downgrade to Low if proven safe).
- `lateinit var` without a clear initialization path; `lateinit` on nullable types.
- Platform types (Java interop) used without null annotations.
- `Any?` or `Any` as type where a sealed class or enum would fit.
- `if (x != null) x.foo()` instead of `x?.foo()` (style sprawl across files).

#### 2.7 Hilt / DI errors
- Same dependency `@Provides` in multiple modules (will fail at compile or produce wrong binding).
- `@Singleton` on something with shorter intended lifecycle.
- `@ViewModelScoped` mixed with `@Singleton` injection of the same class in different places.
- `@Inject` on classes Hilt can't construct (no constructor injection path).
- Missing `@HiltAndroidApp` on Application class.
- Manual instantiation of classes that should be injected (defeats the graph).

#### 2.8 Build / Gradle health
- Version Catalog (`libs.versions.toml`) not used, or used inconsistently.
- Compose BOM / Firebase BOM not used while related libraries are pinned individually.
- `kapt` and `ksp` both present (consolidate).
- `compileSdk` ahead of `targetSdk` by more than one major (audit `targetSdk` decisions).
- Hard-coded dependency versions in `build.gradle` files when a version catalog exists.
- Conflicting dependency versions across modules.
- ProGuard / R8 rules missing for reflected classes, Gson/Moshi/Kotlinx-Serialization models, or Hilt-generated classes.

#### 2.9 Error handling discipline
- `try { ... } catch (e: Exception) { }` (empty catch).
- `catch (e: Exception) { Log.e(...) }` followed by happy-path continuation.
- `Result.success()` / `Result.failure()` mixed with throwing functions for the same kind of operation.
- Errors swallowed in coroutines (no `CoroutineExceptionHandler`, no `try/catch`).
- UI shows generic "Something went wrong" without distinguishing actionable vs non-actionable errors.

#### 2.10 Test sprawl and AI-shaped tests
- Tests that assert what the just-generated code produces (no contract).
- Tests with mocks of everything (testing the mocks, not the code).
- No rotation / process-death tests.
- Compose UI tests absent for screens with non-trivial state.
- Test files for deleted components (orphan tests).
- Multiple test approaches for the same kind of code (JUnit4 + JUnit5 + kotest mixed).

### Step 3 — Verify each finding before reporting

For each candidate finding:

- **Trace the path.** Where is the code called from? Does it actually execute under realistic conditions, or is it dead?
- **Check for framework / library protection.** Some patterns that look bad in isolation are mitigated by Hilt, Compose, or AndroidX defaults. Confirm before reporting.
- **Check test coverage.** Is there a test exercising this path? If yes, what does it actually assert?
- **Confidence label.** High / Medium / Low per how confident you are the finding is real and not a false positive.

### Step 4 — Tag AI-pattern signal per finding

For each finding, indicate whether it shows AI-generation signatures:
- Style mismatch with surrounding code.
- Over-elaborate naming for simple logic.
- Comments narrating what the code does without why.
- Near-identical duplicated blocks across files.
- "Almost-right" idiom — the correct function with subtly wrong arguments.
- Boilerplate that a framework primitive would replace.

This is a prior, not a rule. It raises confidence and suggests broader sweeps for similar patterns.

### Step 5 — Assign severity

Per finding:

- **Critical:** Will crash, leak memory in production, or actively corrupt state. Includes anything that breaks the app on rotation or process death.
- **High:** Will cause regressions or fragility under normal use. Includes most lifecycle and coroutine-scope violations.
- **Medium:** Maintenance burden; will compound. Includes duplication, mixed APIs, Hilt sloppiness.
- **Low:** Hygiene. Includes most null-safety idiom inconsistencies and style sprawl.
- **Informational:** Observation worth noting but not actionable on its own.

### Step 6 — Dual-failure-prevention pass

Before delivering:

- **Harmful direction:** Did every category get a real look? If a category was skipped because the codebase doesn't appear to use that tech (e.g., no Compose, no Hilt), say so explicitly so the reviewer knows the gap.
- **Unhelpful direction:** Cap Critical + High findings at 15 for the main body; move Medium / Low / Informational to an appendix. A 200-finding report is unactionable.

### Step 7 — Emit the "AI patterns repeating in this codebase" summary

Based on findings, list 3–8 patterns that recur. This feeds directly into `android_viberescue_rules_file.md` as hard don'ts. Do not list every instance; summarize.

### Step 8 — Verify and output

Run the verification checklist.

---

## Constraints

### Must
- Every finding cites a specific file and line range.
- Every finding has: category (from step 2), traced reachability, framework check, severity, confidence, AI-pattern tag.
- Categories not applicable to this codebase are noted as "N/A — codebase does not use [X]" rather than silently omitted.
- Critical + High findings are capped at 15 in the main report; others go to an appendix.
- AI patterns repeating section is present and feeds the rules file.

### Must Not
- Issue a finding on keyword match alone (e.g., flag every `GlobalScope` string) without confirming reachability.
- Report "this area should be reviewed" as a finding. Either it's a finding with file + line or it's a scope gap.
- Omit the verification step on findings that look obvious — many "obvious" patterns are mitigated by framework defaults.
- Flood the report with Low / Informational findings at the expense of Critical / High.
- Reference Claude-Code-specific tool names (`Read`, `Edit`, `Grep`, `Bash`) — keep the prompt portable across coding agents.

---

## False-Positive Prevention (MUST follow)

DON'T:
- Flag every `!!` as Critical. A `!!` after an explicit null check or in a `requireNotNull` context is Low or Informational.
- Flag every `LiveData.observeForever` — confirm the corresponding removal is absent.
- Flag `runBlocking` inside `main()` of a test file (it's correct there).
- Claim a Hilt module conflict without tracing the actual binding graph.
- Flag a "deprecated API" usage that is in fact still the recommended path for the project's `minSdk`.
- Report Compose state as "should be hoisted" without checking whether it's local-only by design.

DO:
- Trace each `Flow.collect` to its enclosing scope before flagging.
- Distinguish between Activity Context and Application Context when reporting Context leaks.
- Note when the codebase lacks tests that would catch a class of issue — that's a finding (Medium).
- Acknowledge when reachability can't be determined — "potential finding, needs runtime confirmation" is valid output.
- Call out the framework primitive when reporting hand-rolled reimplementations.

---

## Dual-Failure Prevention (QA-20)

HARMFUL failure: Confident finding that's framework-protected; team spends days "fixing" non-issues while real fragility remains. Or critical lifecycle leak missed because the file wasn't reviewed.

UNHELPFUL failure: 200-finding report dominated by style nits; reviewer can't see the 3 Critical findings.

Quality check: A senior Android engineer reads the Critical / High findings, can point to the file:line, agrees with the severity, and identifies the fix direction without further investigation.

---

## Output Format

```markdown
# Android Vibe-Code Fragility Audit — [App name]

## Summary
- Modules audited: [list]
- UI toolkit: [Compose / XML / mixed]
- DI: [Hilt / Koin / manual / none]
- Async: [coroutines / RxJava / mixed]
- Critical: [N] | High: [N] | Medium: [N] | Low: [N] | Informational: [N]
- Categories N/A: [list with reason]

## Findings (sorted by severity, Critical+High in main body)

### Finding 1: [Short title]
- **File / lines:** path/to/File.kt:42-58
- **Category:** [2.1–2.10 number + name]
- **Evidence:** [Code snippet or paraphrase, ≤5 lines]
- **Traced reachability:** [where this code is reached from]
- **Framework check:** [protection present / absent / N/A, brief reasoning]
- **Severity:** Critical | High | Medium | Low | Informational
- **Confidence:** High | Medium | Low
- **AI-pattern signal:** [yes + which signature(s) / neutral]
- **Fix direction:** [Specific, not generic. Reference a framework primitive if applicable.]

### Finding 2: …

[Continue for Critical + High findings, up to 15.]

## AI Patterns Repeating in This Codebase
- [Pattern + locations summary] → rules-file hard don't recommendation
- [...]

## Scope Gaps
- [Areas not reached by this audit, with one-line reason each.]

## Medium / Low / Informational Findings (appendix)
- [Abbreviated list — file:line, category, one-line description.]

## Recommended Next Step
Feed this report + `android_viberescue_security_privacy_audit.md` output (if run) into `android_viberescue_fix_prioritization.md`.
```

---

## Verification

- [ ] Every entry point / module was considered.
- [ ] Every finding has file + lines, category, traced reachability, framework check, severity, confidence, AI-pattern tag, fix direction.
- [ ] No finding rests on keyword match alone.
- [ ] Critical + High capped at 15 in main body.
- [ ] N/A categories explicitly noted.
- [ ] AI patterns repeating section present.
- [ ] Scope gaps acknowledged honestly.
- [ ] Recommended next step points to the prioritization prompt.

---

## Techniques Used

- **ST-01 (Clear Objective):** Produce a findings report with evidence and severity, not a generic "review your Android code" essay.
- **ST-02 (Structured Sequential Instructions):** Eight steps drive scope → ten categories → verify → AI tag → severity → dual-failure → patterns → verify.
- **ST-03 (Output Format Specification):** Fixed report format with per-finding fields enables downstream tooling (prioritization prompt consumes this directly).
- **CM-02 (Constraint Specification):** Must Not block forbids keyword findings and Low-finding flooding.
- **DS-01 (Framework Application):** Ten-category fragility framework specific to AI-generated Android.
- **RT-05 (Evidence-Based Reasoning):** Every finding traced to file:line; framework-check step prevents false positives.
- **RT-07 (Cascade Effect Analysis):** AI-pattern signal section traces individual findings to systemic prevention via rules file.
- **QA-01 (Self-Verification):** Verification checklist + dual-failure-prevention block prevents under- and over-reporting.
- **QA-04 (Confidence Calibration):** Per-finding confidence labels force explicit grounding.
