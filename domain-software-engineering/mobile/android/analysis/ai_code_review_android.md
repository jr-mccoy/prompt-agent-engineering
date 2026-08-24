---
title: "AI Code Review for Android"
category: mobile-development
description: "AI-assisted code review checklist for Android covering Kotlin idiom compliance, Compose best practices, lifecycle safety, memory leak patterns, security practices, accessibility, and performance anti-patterns"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: intermediate
tags:
  - android
  - code-review
  - ai-assisted
  - kotlin
  - jetpack-compose
  - mobile-development
updated: "2026-02-12"
related_prompts:
  - domain-software-engineering/mobile/android/analysis/android_kotlin_best_practices.md
  - domain-software-engineering/mobile/android/analysis/android_kotlin_compose_debugging_audit.md
  - domain-software-engineering/mobile/android/testing/ai_test_generation_android.md
---


# AI Code Review for Android

**Objective:** Conduct a comprehensive AI-assisted code review of Android code — checking Kotlin idiom compliance, Jetpack Compose best practices (recomposition, state, stability), lifecycle safety, memory leak patterns, security practices, accessibility, and performance anti-patterns — producing a review report with severity-rated findings, specific code locations, and fix suggestions.

**When to Use:** Use this prompt when reviewing pull requests or code changes, when doing periodic codebase quality checks, when onboarding to a new Android codebase, when AI-generated code needs human-equivalent review, or as a pre-merge quality gate in solo development (where there is no second pair of eyes).

**Important context:** Solo developers lack a code review partner, which means bugs, anti-patterns, and technical debt accumulate unchecked. An AI-assisted code review provides the "second pair of eyes" that catches issues a single developer misses — especially patterns that are technically correct but suboptimal (using `collectAsState` instead of `collectAsStateWithLifecycle`, or `remember` instead of `rememberSaveable` for form data).

---

## Instructions

Review the provided Android code against the following checklist. For each category, check every item and report findings with severity and fix suggestions.

### Category 1: Kotlin Idioms

| Check | Severity if Violated | What to Look For |
|-------|---------------------|-----------------|
| Null safety | MEDIUM | Avoid `!!` operator — use `?.`, `?:`, `let`, or require/check |
| Data classes | LOW | Use data classes for value types (models, DTOs, state) |
| Sealed classes/interfaces | LOW | Use for state hierarchies (UiState, Events, Results) |
| Scope functions | LOW | Appropriate use of `let`, `apply`, `also`, `run`, `with` |
| Collection operations | LOW | Use `map`, `filter`, `groupBy` over manual loops |
| Coroutine usage | HIGH | No `GlobalScope`, no `runBlocking` on main thread, proper `viewModelScope` |
| String templates | LOW | Use `"Hello, $name"` over `"Hello, " + name` |
| Extension functions | LOW | Appropriate use for readability (not over-engineering) |
| `lateinit` safety | MEDIUM | Every `lateinit` var must be initialized before access — check for `UninitializedPropertyAccessException` risk |

### Category 2: Jetpack Compose

| Check | Severity | What to Look For |
|-------|----------|-----------------|
| `collectAsStateWithLifecycle()` | HIGH | Must use instead of `collectAsState()` — prevents resource waste when backgrounded |
| State hoisting | MEDIUM | Composables should receive state as parameters, not own business state |
| `remember` vs `rememberSaveable` | HIGH | Form data and user input must use `rememberSaveable` to survive rotation |
| Stable types | MEDIUM | Classes used in Composable parameters should be `@Stable` or `@Immutable` |
| LazyColumn keys | MEDIUM | `items(list, key = { it.id })` — missing keys cause incorrect item reuse |
| `derivedStateOf` | LOW | Use for derived values to prevent unnecessary recomposition |
| Side effects | HIGH | `LaunchedEffect`, `DisposableEffect` must have correct keys — wrong keys cause stale closures or missing cleanup |
| ViewModel in nested Composables | HIGH | ViewModel should be obtained at screen level, not deep in the tree |
| `Modifier` ordering | MEDIUM | Modifier order matters — `padding` before `background` vs after produces different results |
| Recomposition scope | MEDIUM | Avoid passing lambdas that capture unstable references (breaks skipping) |

### Category 3: Lifecycle Safety

| Check | Severity | What to Look For |
|-------|----------|-----------------|
| Fragment transactions after `onSaveInstanceState` | CRITICAL | Use `commitAllowingStateLoss()` or check lifecycle state |
| LiveData observation | HIGH | Observe with lifecycle owner (`viewLifecycleOwner` in Fragment, not `this`) |
| Coroutine scope | HIGH | Use `lifecycleScope` or `viewModelScope`, not custom unscoped coroutines |
| Configuration change survival | HIGH | Business state survives rotation (ViewModel or SavedStateHandle) |
| Process death survival | MEDIUM | Critical state survives process death (SavedStateHandle, persistent storage) |
| `onDestroy` cleanup | MEDIUM | Unregister listeners, cancel subscriptions, close connections |

### Category 4: Memory Leaks

| Check | Severity | What to Look For |
|-------|----------|-----------------|
| Activity/Context references in singletons | CRITICAL | Never store Activity context in companion objects, singletons, or static fields |
| Inner classes holding outer references | HIGH | Anonymous inner classes (listeners, callbacks) can leak the enclosing Activity |
| Unregistered BroadcastReceivers | HIGH | Register in `onResume`/`onStart`, unregister in `onPause`/`onStop` |
| Coroutine leaks | MEDIUM | Coroutines not scoped to lifecycle can leak the enclosing scope |
| Bitmap handling | MEDIUM | Large bitmaps not recycled, using full-resolution images for thumbnails |
| Handler leaks | HIGH | `Handler` holding Activity reference — use WeakReference or lifecycle-aware handler |

### Category 5: Security

| Check | Severity | What to Look For |
|-------|----------|-----------------|
| Hardcoded secrets | CRITICAL | API keys, passwords, tokens in source code |
| Logging sensitive data | HIGH | `Log.d(TAG, "Password: $password")` — remove before release |
| WebView JavaScript injection | HIGH | `setJavaScriptEnabled(true)` without input sanitization |
| Intent validation | MEDIUM | Exported components should validate incoming Intent data |
| SQL injection in Room | MEDIUM | Use parameterized queries, not string concatenation in `@RawQuery` |
| Insecure storage | HIGH | Sensitive data in SharedPreferences instead of EncryptedSharedPreferences |
| Network security config | MEDIUM | Cleartext traffic disabled, certificate pinning for sensitive endpoints |

### Category 6: Accessibility

| Check | Severity | What to Look For |
|-------|----------|-----------------|
| Content descriptions | MEDIUM | Images and icons have `contentDescription` (or `null` for decorative) |
| Touch target size | MEDIUM | Minimum 48dp × 48dp touch targets |
| Color contrast | MEDIUM | Text contrast ratio meets WCAG AA (4.5:1 for normal text) |
| Screen reader support | MEDIUM | Semantic properties set (`semantics { heading() }`, role descriptions) |
| Focus management | LOW | Logical focus order, focus indicators visible |

### Category 7: Performance

| Check | Severity | What to Look For |
|-------|----------|-----------------|
| Main thread operations | HIGH | Database queries, file I/O, network calls on main thread |
| Image loading | MEDIUM | Using Coil/Glide with proper caching, not loading full-resolution into small views |
| RecyclerView/LazyColumn | MEDIUM | Proper recycling, no nested scrolling without height constraints |
| StrictMode violations | MEDIUM | Enable StrictMode in debug to catch main-thread I/O |
| ProGuard/R8 keep rules | LOW | Over-kept classes bloating APK, missing rules causing crashes |
| Startup initialization | MEDIUM | Deferring non-essential initialization (analytics, ad SDKs) |

---

## Expected Output

For each finding:

```
[SEVERITY] Category: Description
File: path/to/File.kt:42
Issue: What's wrong and why it matters
Fix: Specific code change to resolve the issue
```

Summary:
1. **Critical findings** (fix before merge)
2. **High findings** (fix soon)
3. **Medium findings** (address in next sprint)
4. **Low findings** (address when convenient)
5. **Overall code quality score** (1-10)

---

## CRITICAL: Verification Requirements

- [ ] All 7 categories are checked (not just the reviewer's specialty)
- [ ] Findings include specific file and line references
- [ ] Fix suggestions are provided (not just "this is wrong")
- [ ] Severity is calibrated (CRITICAL = crash/security, HIGH = bug/leak, MEDIUM = quality, LOW = style)
- [ ] False positives are minimized (don't flag correct patterns as issues)
