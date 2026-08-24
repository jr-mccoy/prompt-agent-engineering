---
title: "Android CLAUDE.md Generator"
category: mobile-development
description: "Generate a comprehensive CLAUDE.md file for an Android project — project context, architecture decisions, coding conventions, testing requirements, Firebase configuration, build system specifics, and common pitfalls"
techniques:
  - ST-01
  - ST-02
  - CM-01
  - RT-02
  - DS-06
  - ED-05
difficulty: intermediate
tags:
  - android
  - claude-code
  - ai-assisted-development
  - project-documentation
  - coding-conventions
  - mobile-development
  - solo-developer
updated: "2026-02-11"
---

# Android CLAUDE.md Generator

**Objective:** Generate a comprehensive CLAUDE.md file for an Android project — covering project context, architecture decisions, coding conventions (Kotlin style, Compose patterns), testing requirements, Firebase configuration, build system specifics, dependency management, and common pitfalls specific to the project — producing a file that makes AI coding agents (Claude Code, Cursor, Copilot) dramatically more effective when working on the codebase.

**When to Use:** Use this prompt when starting a new Android project with AI coding agents, when onboarding an AI agent to an existing project, when your AI agent keeps making the same mistakes (wrong patterns, outdated APIs, incorrect Gradle syntax), or when you want to significantly improve AI-generated code quality for your specific project. The CLAUDE.md file is a force multiplier — it turns generic AI assistance into project-specific assistance.

**Sequence Map:** Use after architecture/stack conventions are decided; use before extensive AI-agent coding sessions.

**Important context:** AI coding agents work significantly better when they understand your project's conventions, architecture, and constraints. Without a CLAUDE.md, agents will use generic patterns that may not match your project. With a good CLAUDE.md, agents will follow your naming conventions, use your preferred architecture patterns, and avoid known pitfalls. The investment (1-2 hours to create) pays off on every AI-assisted task for the life of the project.

---

## Context Gathering

Before generating the CLAUDE.md, gather information about the project:

1. **Project Basics:**
   - "What is the app's name, package name, and purpose?"
   - "What is the minimum SDK version and target SDK version?"
   - "What programming language(s) (Kotlin only, Java + Kotlin, Compose + XML)?"
   - "Is this a single-module or multi-module project?"

2. **Architecture:**
   - "What architecture pattern do you follow (MVVM, MVI, Clean Architecture)?"
   - "What UI framework (Jetpack Compose, XML Views, both)?"
   - "What DI framework (Hilt, Koin, manual)?"
   - "What navigation approach (Navigation Component, Compose Navigation, custom)?"

3. **Backend/Data:**
   - "What backend services do you use (Firebase, custom API, both)?"
   - "What local storage (Room, DataStore, SharedPreferences)?"
   - "How do you handle networking (Retrofit, Ktor, Firebase SDK)?"
   - "What serialization (Gson, Moshi, Kotlin Serialization)?"

4. **Development Practices:**
   - "What testing frameworks and approach (JUnit, Turbine, Compose testing)?"
   - "What coding conventions do you follow?"
   - "What build flavors or variants do you use?"
   - "Are there specific patterns you enforce or avoid?"

5. **Known Issues:**
   - "What mistakes do AI agents commonly make on your project?"
   - "Are there deprecated patterns in the codebase that shouldn't be replicated?"
   - "Are there any files or directories that should never be modified?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before generating ANY CLAUDE.md content, you MUST:**

1. **Examine the actual codebase** — Don't guess at conventions. Look at existing files to determine the actual patterns, naming conventions, and architecture used.
2. **Check the actual build files** — Read build.gradle.kts (or .gradle) to determine real dependencies, SDK versions, and build configuration.
3. **Verify the actual project structure** — Look at the module structure, package organization, and directory layout.
4. **Identify actual pain points** — Ask about recurring issues with AI-generated code rather than listing generic Android pitfalls.
5. **Keep it concise** — CLAUDE.md is read by AI agents with context windows. Every unnecessary line reduces the space available for actual task context. Target 200-400 lines, not 1,000.

### False-Positive Prevention

- ❌ Do NOT include generic Android advice that any developer would know
- ❌ Do NOT document every file and class — only the important architectural decisions
- ❌ Do NOT include tutorial-level explanations — the AI agent doesn't need to learn Android
- ❌ Do NOT list every dependency — only the ones with non-obvious usage patterns
- ❌ Do NOT make the file so long that AI agents truncate it
- ✅ DO focus on project-specific conventions that differ from generic Android patterns
- ✅ DO include the "gotchas" specific to this project
- ✅ DO provide concrete examples of correct patterns (show, don't just tell)
- ✅ DO include build and test commands that the agent needs
- ✅ DO update the file when conventions change

---

### Phase 1: Project Context Section

This section orients the AI agent immediately.

```markdown
# [App Name]

## Project Overview
[1-2 sentences about what the app does and who it's for]

## Tech Stack
- **Language:** Kotlin [version]
- **UI:** Jetpack Compose (no XML layouts) / XML Views / Mixed
- **Min SDK:** [X] | **Target SDK:** [X] | **Compile SDK:** [X]
- **Architecture:** [MVVM / MVI / Clean Architecture]
- **DI:** [Hilt / Koin / Manual]
- **Navigation:** [Compose Navigation / Navigation Component]
- **Backend:** [Firebase / Custom API / Both]
- **Database:** [Room / DataStore / Both]
- **Networking:** [Retrofit + OkHttp / Ktor / Firebase SDK]
- **Serialization:** [Kotlin Serialization / Moshi / Gson]
- **Testing:** [JUnit5 / JUnit4] + [Turbine / MockK / Mockito]
- **Build:** Gradle [version] with [KTS / Groovy], Version Catalog
```

### Phase 2: Architecture and Patterns Section

Document the patterns the agent MUST follow.

```markdown
## Architecture

### Module Structure
```
app/              — Main application module
feature-home/     — Home feature module
feature-settings/ — Settings feature module
core-data/        — Data layer (repositories, data sources)
core-domain/      — Domain layer (use cases, models)
core-ui/          — Shared UI components and theme
core-network/     — Network configuration and API clients
```

### Layer Rules
- **UI Layer (feature modules):** Composables + ViewModels. ViewModels expose UI state via `StateFlow`. Never call repositories directly from Composables.
- **Domain Layer:** Use cases orchestrate data access. No Android framework dependencies.
- **Data Layer:** Repositories abstract data sources. Room entities map to domain models via mappers.

### Naming Conventions
- **Composables:** PascalCase, noun-based: `TaskListScreen`, `TaskCard`, `AddTaskDialog`
- **ViewModels:** `[Feature]ViewModel`: `TaskListViewModel`, `SettingsViewModel`
- **Use Cases:** `[Verb][Noun]UseCase`: `GetTasksUseCase`, `DeleteTaskUseCase`
- **Repositories:** `[Entity]Repository`: `TaskRepository`, `UserRepository`
- **Room DAOs:** `[Entity]Dao`: `TaskDao`, `UserDao`
- **Screens:** `[Feature]Screen` composable with a corresponding `[Feature]Route` for navigation
```

### Phase 3: Coding Conventions Section

This is the highest-impact section. AI agents default to generic patterns without this.

```markdown
## Coding Conventions

### Kotlin Style
- Use expression bodies for single-expression functions
- Prefer `when` over `if-else` chains for 3+ conditions
- Use `sealed interface` (not `sealed class`) for state and events
- Use `data class` for simple state containers
- Avoid `!!` — use `?.let`, `?:`, or explicit null checks
- Prefer `Flow` over `LiveData` for reactive streams

### Compose Patterns
- State hoisting: State lives in ViewModel, Composables are stateless
- Use `collectAsStateWithLifecycle()` (not `collectAsState()`) for ViewModel flows
- Preview functions use `@Preview` with `@Composable` and realistic sample data
- Theme: Use `MaterialTheme.colorScheme` and `MaterialTheme.typography`, never hardcode colors
- Modifiers: Always accept `modifier: Modifier = Modifier` as the first parameter of public Composables
- Navigation: Use type-safe navigation routes, not string routes

### Patterns to AVOID (common AI mistakes in this project)
- ❌ Do NOT use `remember { mutableStateOf() }` for ViewModel state — use `StateFlow` in ViewModel
- ❌ Do NOT use `GlobalScope` or `viewModelScope.launch` without a Dispatcher — use `Dispatchers.IO` for data operations
- ❌ Do NOT create new Retrofit/OkHttp instances — use the Hilt-provided singleton
- ❌ Do NOT add `@Composable` functions inside ViewModel classes
- ❌ Do NOT use string resource IDs in ViewModel — pass `StringResource` wrapper instead
- ❌ Do NOT use `LaunchedEffect(Unit)` for data loading — use `init` block in ViewModel
```

### Phase 4: Firebase-Specific Section (if applicable)

```markdown
## Firebase Configuration

### Services Used
- **Firestore:** Primary data store. Collections: `users`, `tasks`, `settings`
- **Auth:** Google Sign-In + email/password
- **Crashlytics:** Crash reporting
- **Analytics:** Core events only (see analytics strategy)
- **Cloud Functions:** [TypeScript / JavaScript], deployed from `/functions`
- **Remote Config:** Feature flags

### Firestore Rules
- Security rules are in `firestore.rules`
- All collections require authentication
- Users can only read/write their own documents
- Never test against production Firestore — use emulator

### Firebase Emulator
```bash
# Start emulator suite
firebase emulators:start

# Emulator ports:
# Auth: 9099
# Firestore: 8080
# Functions: 5001
# Storage: 9199
```

### Important Firebase Patterns
- Always use `Flow` for Firestore listeners (via `callbackFlow` or `snapshotFlow`)
- Handle offline state explicitly — `FirebaseFirestoreSettings.Builder().setPersistenceEnabled(true)`
- Cloud Functions: Check `functions/src/index.ts` for the trigger chain before adding new triggers
```

### Phase 5: Build and Test Commands

```markdown
## Commands

### Build
```bash
# Debug build
./gradlew assembleDebug

# Release build (requires signing config)
./gradlew bundleRelease

# Check for lint issues
./gradlew lintDebug

# Dependency updates check
./gradlew dependencyUpdates
```

### Test
```bash
# All unit tests
./gradlew testDebugUnitTest

# Specific module tests
./gradlew :feature-home:testDebugUnitTest

# With coverage report
./gradlew testDebugUnitTest jacocoTestReport
```

### Firebase
```bash
# Start emulators
firebase emulators:start

# Deploy Cloud Functions
firebase deploy --only functions

# Deploy security rules
firebase deploy --only firestore:rules
```

## Testing Conventions
- Unit tests next to source: `src/test/java/...`
- UI tests: `src/androidTest/java/...`
- Test naming: `fun \`given X when Y then Z\`()`
- Use MockK for mocking, Turbine for Flow testing
- ViewModels: Test state emissions, not implementation details
- Repositories: Test with fake data sources, not mocks
```

### Phase 6: Project-Specific Gotchas

```markdown
## Known Issues & Gotchas

### Build Issues
- If Gradle sync fails after dependency updates, try: `./gradlew --stop && ./gradlew clean`
- Version catalog is in `gradle/libs.versions.toml` — all dependencies must go through it
- KSP is used (not KAPT) for Room and Hilt — check processor configuration

### Common Mistakes
- [Specific to your project: "The UserRepository.getUser() returns cached data by default. Use getUser(forceRefresh = true) for fresh data."]
- [Specific to your project: "The theme colors in core-ui use dynamic colors on Android 12+. Always test on API 30 as well."]
- [Specific to your project: "The /functions directory has its own package.json. Run npm install in that directory separately."]

### Files That Should Not Be Modified
- `google-services.json` — Firebase config, managed via Firebase Console
- `release.keystore` — Signing key, do not regenerate
- `.github/workflows/` — CI/CD config, modify carefully
```

---

## Expected Output

A complete CLAUDE.md file that should be:
- **200-400 lines** — concise enough for AI agents to process fully
- **Project-specific** — not generic Android documentation
- **Actionable** — tells the agent what to DO and what NOT to do
- **Up-to-date** — reflects the current state of the project

### Quality Checklist

- [ ] Tech stack section accurately reflects all dependencies
- [ ] Architecture section matches actual project structure
- [ ] Naming conventions match actual file names in the project
- [ ] Build commands actually work when run
- [ ] "Patterns to avoid" includes real mistakes AI agents have made
- [ ] Firebase section matches actual firebase configuration
- [ ] No generic advice that applies to all Android projects
- [ ] File is under 400 lines

### Template Structure

```markdown
# [App Name]

## Project Overview
[2-3 sentences]

## Tech Stack
[Bullet list of key technologies]

## Architecture
[Module structure, layer rules, naming conventions]

## Coding Conventions
[Kotlin style, Compose patterns, patterns to AVOID]

## Firebase Configuration (if applicable)
[Services, rules, emulator setup]

## Commands
[Build, test, deploy commands]

## Testing Conventions
[Framework, naming, approach]

## Known Issues & Gotchas
[Project-specific pitfalls]

## Files That Should Not Be Modified
[Protected files and directories]
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) - CLAUDE.md generation focus
- **ST-02** (Structured Sequential Instructions) - Section-by-section generation
- **CM-01** (Explicit Context Framing) - Android project context
- **RT-02** (Multi-Dimensional Analysis) - Architecture, conventions, testing, build dimensions
- **DS-06** (Prioritization Guidance) - Focus on highest-impact sections
- **ED-05** (Reference Class Priming) - Example patterns and anti-patterns

---

## Related Prompts

- `android_architecture_selection.md` - Architecture decisions documented in CLAUDE.md
- `firebase_cloud_functions_design.md` - Firebase conventions referenced in CLAUDE.md
- `android_ci_cd_pipeline_design.md` - CI/CD commands documented in CLAUDE.md
- `ai_code_review_android.md` - AI code review using CLAUDE.md conventions (planned)
- `ai_agent_android_workflow.md` - Overall AI agent workflow for Android projects (planned)

---

## Customization Guide

- **For new projects:** Generate the CLAUDE.md as part of project scaffolding. Start with architecture and conventions; add gotchas section after the first week of development.
- **For existing projects with tech debt:** Include a "Legacy Patterns" section that lists old patterns still in the codebase that should NOT be replicated in new code.
- **For multi-module projects:** Emphasize module boundaries and dependency rules. AI agents frequently create circular dependencies between modules.
- **For projects with multiple developers:** Add a code review expectations section and PR conventions.
- **For projects transitioning from XML to Compose:** Add clear guidance on which screens are Compose vs XML, and the migration approach for new screens.
- **Maintenance:** Update CLAUDE.md whenever you change architecture patterns, add/remove dependencies, or discover a new common AI mistake. Review quarterly at minimum.
