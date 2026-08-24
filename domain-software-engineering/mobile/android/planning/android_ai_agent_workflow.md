---
title: "AI Agent Android Workflow"
category: mobile-development
description: "Design a workflow for effectively using AI coding agents with Android projects — task delegation, prompt structuring for Android-specific work, common AI mistakes to watch for, and verification strategies"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-01
  - ED-05
difficulty: intermediate
tags:
  - android
  - ai-assisted-development
  - claude-code
  - workflow
  - mobile-development
  - solo-developer
updated: "2026-02-12"
---

# AI Agent Android Workflow

**Objective:** Design an effective workflow for using AI coding agents (Claude Code, Cursor, GitHub Copilot) with Android projects — identifying which tasks to delegate to AI agents, how to structure prompts for Android-specific work (Gradle, Compose, lifecycle), common mistakes AI agents make with Android code, and verification strategies to catch those mistakes — producing a playbook that maximizes AI effectiveness while minimizing debugging AI-generated bugs.

**When to Use:** Use this prompt when starting to integrate AI coding agents into your Android development workflow, when AI-generated code is causing more problems than it solves, when you want to increase development velocity with AI assistance, or when establishing AI coding practices for your project.

**Sequence Map:** Use after project scaffold exists; use before sustained AI-assisted implementation cycles.

**Important context:** AI coding agents are powerful for Android development but have specific blind spots. They excel at: boilerplate generation, test writing, documentation, refactoring, and implementing well-documented patterns. They struggle with: Gradle configuration (complex and version-sensitive), Android lifecycle nuances, Compose recomposition correctness, Firebase security rules, and project-specific conventions. The key to effectiveness is knowing what to delegate and how to verify the output.

---

## Instructions

### Step 1: Task Delegation Matrix

Classify Android development tasks by AI suitability:

**High Confidence (Delegate freely):**
| Task | Why AI Excels | Verification |
|------|-------------|--------------|
| Writing data class models | Mechanical, pattern-based | Quick review |
| Generating Room entities + DAOs | Well-documented patterns | Compile + basic test |
| Writing unit tests for ViewModels | Pattern-based, deterministic | Run tests |
| Converting XML layouts to Compose | Documented equivalencies | Visual inspection |
| Writing repository implementations | Standard patterns | Compile + test |
| Generating extension functions | Small, focused, testable | Review + test |
| Writing documentation/comments | Natural language generation | Review for accuracy |
| Creating Compose Previews | Low risk, visual verification | Visual check |

**Medium Confidence (Delegate with guidance):**
| Task | AI Limitation | Mitigation |
|------|-------------|-----------|
| Compose state management | May use `collectAsState` vs `collectAsStateWithLifecycle` | Specify in CLAUDE.md |
| Navigation setup | May use outdated API patterns | Specify type-safe routes |
| Hilt module configuration | May create wrong scope | Review scope annotations |
| WorkManager implementation | May miss constraints or retry logic | Review constraints |
| Firebase integration | May use deprecated SDK patterns | Specify SDK version |
| Coroutine error handling | May not handle cancellation correctly | Review CancellationException handling |

**Low Confidence (AI-assisted, human-led):**
| Task | Why AI Struggles | Approach |
|------|-----------------|---------|
| Gradle configuration changes | Version-sensitive, complex resolution | Human writes, AI reviews |
| ProGuard/R8 rules | Highly project-specific, subtle | Human writes with AI suggestions |
| Manifest configuration | Platform-specific behavior changes by API level | Human decides, AI implements |
| Firebase security rules | Security-critical, Firebase-specific DSL | Human designs, AI generates draft |
| Architecture decisions | Requires project context, trade-off analysis | Human decides, AI documents |
| Performance optimization | Requires profiling data, not just patterns | Human identifies, AI assists fix |

### Step 2: CLAUDE.md Configuration

Create a project-specific CLAUDE.md that prevents common AI mistakes:

```markdown
# Project: [Your App Name]

## Build System
- Gradle 8.7, AGP 8.5.0, Kotlin 2.1.0
- Version catalog: gradle/libs.versions.toml (ALWAYS use catalog references, never hardcoded versions)
- KSP for annotation processing (NOT kapt)

## Architecture
- MVVM with Clean Architecture layers
- Jetpack Compose for ALL new UI (no XML)
- Hilt for dependency injection
- Compose Navigation with type-safe routes

## Coding Standards
- ALWAYS use `collectAsStateWithLifecycle()` (NEVER `collectAsState()`)
- ALWAYS use `rememberSaveable` for user input state
- ViewModels expose `StateFlow`, never `MutableStateFlow` publicly
- Use `sealed interface` for UI state, not `sealed class`
- Room entities in `data/local/entity/`, DTOs in `data/remote/dto/`
- One Composable per file for screen-level components

## Common Mistakes to Avoid
- Do NOT use `GlobalScope` or `runBlocking`
- Do NOT import `android.util.Log` — use Timber
- Do NOT use `java.util.Date` — use `kotlinx-datetime`
- Do NOT use `@Suppress("DEPRECATION")` — fix the deprecation
- Do NOT add dependencies without using the version catalog
- Do NOT create Activities — everything is in Compose via single Activity

## Testing
- Unit tests: JUnit 5 + MockK + Turbine
- UI tests: Compose testing with `createComposeRule()`
- Every ViewModel must have tests for all UI states
```

### Step 3: Prompt Patterns for Android

**Pattern 1: Implementation with constraints**
```
Implement [feature] in [file/module].
Use Jetpack Compose for the UI.
Follow the existing architecture pattern in [reference file].
State should be managed in the ViewModel with StateFlow.
Include Compose Preview annotations.
```

**Pattern 2: Test generation**
```
Write unit tests for [ViewModel/Repository].
Test all UI states: Loading, Success, Error, Empty.
Use MockK for mocking dependencies.
Use Turbine for testing Flow emissions.
Follow the testing patterns in [reference test file].
```

**Pattern 3: Code review request**
```
Review this code for:
1. Compose recomposition issues
2. Lifecycle safety problems
3. Memory leak risks
4. Missing null safety
5. Performance anti-patterns
Provide findings with severity and fix suggestions.
```

**Pattern 4: Refactoring with guardrails**
```
Refactor [class/function] to [target pattern].
Do NOT change the public API.
Do NOT modify test files.
Ensure all existing tests still pass.
Preserve the current behavior — this is a refactor, not a feature change.
```

### Step 4: Verification Strategies

**After AI generates code, verify:**

| Verification | Method | When |
|-------------|--------|------|
| Compilation | `./gradlew assembleDebug` | Every change |
| Existing tests | `./gradlew test` | Every change |
| Lint | `./gradlew lint` | Every change |
| Compose preview | Visual check in Android Studio | UI changes |
| Lifecycle behavior | Rotate device, toggle dark mode, background/foreground | UI + state changes |
| Process death | Developer options → Don't keep activities | State management changes |
| Memory leaks | LeakCanary in debug builds | Any lifecycle changes |
| Gradle sync | Android Studio sync after build changes | Build file changes |

### Step 5: Common AI Mistakes Checklist

After every AI-generated change, check for these known issues:

- [ ] **Gradle:** No hardcoded dependency versions (must use `libs.*` catalog references)
- [ ] **Compose:** Uses `collectAsStateWithLifecycle`, not `collectAsState`
- [ ] **Compose:** State hoisted correctly (stateless Composable pattern)
- [ ] **Compose:** Modifier parameter is last, with `Modifier` default
- [ ] **Hilt:** Correct scope annotations (`@Singleton`, `@ViewModelScoped`, `@ActivityRetainedScoped`)
- [ ] **Coroutines:** Error handling doesn't catch `CancellationException`
- [ ] **Navigation:** Uses type-safe route definitions, not hardcoded strings
- [ ] **Room:** Migration provided for schema changes
- [ ] **Manifest:** New components are correctly exported/not-exported
- [ ] **Imports:** No wildcard imports, no deprecated API usage

---

## Expected Output

1. **Task Delegation Matrix** — categorized by AI confidence level
2. **CLAUDE.md Template** — project-specific AI configuration
3. **Prompt Templates** — reusable prompts for common Android tasks
4. **Verification Checklist** — post-generation verification steps
5. **Common Mistakes Reference** — Android-specific AI error patterns
6. **Workflow Diagram** — when to use AI vs manual development

---

## CRITICAL: Verification Requirements

- [ ] AI-generated code compiles without errors
- [ ] All existing tests pass after AI changes
- [ ] No deprecated APIs introduced by AI
- [ ] Gradle version catalog is used consistently
- [ ] The CLAUDE.md file captures project-specific conventions
