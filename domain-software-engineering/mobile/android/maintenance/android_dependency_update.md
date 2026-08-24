---
title: "Android Dependency Update"
category: mobile-development
description: "Safely updates Android project dependencies by analyzing compatibility, identifying breaking changes, planning migration paths, and verifying stability"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-02
  - QA-01
difficulty: intermediate
tags:
  - android
  - mobile-development
  - dependencies
  - maintenance
updated: "2026-06-06"
related_prompts:
  - domain-software-engineering/mobile/android/maintenance/android_dependency_audit.md
  - domain-software-engineering/mobile/android/maintenance/android_third_party_sdk_upgrade_review.md
  - domain-software-engineering/mobile/android/maintenance/android_build_toolchain_upgrade.md
  - domain-software-engineering/mobile/android/improvement/android_version_catalog_migration.md
---

# Android Dependency Update

**Objective:** Safely update project dependencies by analyzing compatibility, identifying breaking changes, planning migration paths, and implementing updates with proper testing to maintain app stability and security.

**When to Use:** Use this prompt when you need to update outdated dependencies, address security vulnerabilities, adopt new library features, or perform routine maintenance updates. Ideal before major releases, when security advisories are published, or during scheduled maintenance windows. Prerequisites include a working build and understanding of your current dependency versions.

**Prompt Type:** Comprehensive (400-500 lines)

---

## Context Gathering

Before beginning dependency updates, gather essential context:

1. **Update Scope:**
   - "Are you updating all dependencies, specific libraries, or addressing a security issue?"
   - "Is this routine maintenance or triggered by a specific need?"

2. **Risk Tolerance:**
   - "Is this a critical production app or a project that can tolerate some instability?"
   - "Do you have comprehensive tests to catch regressions?"

3. **Constraints:**
   - "Are there any dependencies you cannot update? (locked versions, company policies)"
   - "What's your minimum SDK version? (affects library compatibility)"

4. **Timeline:**
   - "Is there a deadline for these updates? (e.g., Play Store targetSdk requirement)"
   - "Can updates be staged across multiple releases?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before recommending ANY update, you MUST:**

1. **Trace actual compatibility** - Don't recommend updates without checking compatibility with other dependencies.
2. **Check for breaking changes** - Search release notes and changelogs for breaking changes before suggesting version bumps.
3. **Understand the context** - Consider WHY specific versions are pinned. There may be compatibility reasons.
4. **Confirm actual impact** - Will this update provide real benefit, or just churn for version's sake?
5. **Provide specific locations** - Every update recommendation must reference exact files (e.g., `libs.versions.toml:23`).

**Finding NO urgent updates is an acceptable outcome.** If dependencies are reasonably current and stable, say so with confidence.

### False-Positive Prevention

- ❌ Do NOT recommend major version bumps without checking breaking changes
- ❌ Do NOT assume latest is always best (stability matters)
- ❌ Do NOT recommend updates that would break minSdk compatibility
- ❌ Do NOT ignore existing version constraints
- ✅ DO check release notes for breaking changes
- ✅ DO consider test coverage before recommending risky updates
- ✅ DO prioritize security updates over feature updates
- ✅ DO recommend staged rollout for major updates

---

### Phase 1: Dependency Inventory & Analysis

Create a comprehensive inventory of current dependencies and their update status.

#### 1.1 Current Dependency Audit

**Analyze build configuration:**

```kotlin
// Files to examine:
// - build.gradle.kts / build.gradle (app and all modules)
// - libs.versions.toml (version catalog)
// - buildSrc/src/main/kotlin/Dependencies.kt (if used)
// - settings.gradle.kts (plugin versions)

// Extract all dependencies and versions:
dependencies {
    implementation("androidx.core:core-ktx:1.12.0")
    implementation("androidx.lifecycle:lifecycle-runtime-ktx:2.7.0")
    implementation("com.squareup.retrofit2:retrofit:2.9.0")
    // ... catalog all dependencies
}
```

**Create dependency inventory:**

| Category | Dependency | Current | Latest Stable | Gap | Notes |
|----------|------------|---------|---------------|-----|-------|
| AndroidX | core-ktx | 1.12.0 | 1.13.1 | Minor | Safe update |
| AndroidX | lifecycle-* | 2.7.0 | 2.8.0 | Minor | Check migration guide |
| Network | retrofit | 2.9.0 | 2.11.0 | Minor | Review changelog |
| DI | hilt | 2.48 | 2.51.1 | Minor | AGP compatibility |

#### 1.2 Outdated Dependency Detection

**Use Gradle to find outdated dependencies:**

```bash
# Add versions plugin to check for updates
# settings.gradle.kts
plugins {
    id("com.github.ben-manes.versions") version "0.51.0"
}

# Run dependency update check
./gradlew dependencyUpdates -Drevision=release

# Or use Android Studio's built-in inspection
# Analyze > Run Inspection by Name > "Newer Library Versions Available"
```

**Categorize updates by risk:**

```markdown
## Update Risk Assessment

### Safe Updates (Patch Versions - X.Y.Z)
- Typically bug fixes only
- Low risk of breaking changes
- Example: 2.9.0 → 2.9.1

### Moderate Updates (Minor Versions - X.Y.0)
- New features, deprecations
- May require code adjustments
- Example: 2.9.0 → 2.10.0

### High Risk Updates (Major Versions - X.0.0)
- Breaking changes expected
- Require migration effort
- Example: 2.9.0 → 3.0.0
```

#### 1.3 Security Vulnerability Scan

**Check for known vulnerabilities:**

```kotlin
// Add dependency verification
// build.gradle.kts
dependencyCheck {
    analyzers {
        assemblyEnabled = false
    }
    format = "HTML"
    outputDirectory = "$buildDir/reports/dependency-check"
}

// Or use GitHub Dependabot / Snyk integration
```

**Review security advisories:**
- [ ] Check NIST NVD for CVEs in dependencies
- [ ] Review GitHub Security Advisories
- [ ] Check library-specific security announcements
- [ ] Verify transitive dependency vulnerabilities

#### 1.4 Compatibility Matrix

**Verify compatibility relationships:**

```markdown
## Critical Compatibility Chains

### Kotlin + AGP + Gradle
| Kotlin | AGP | Gradle | Status |
|--------|-----|--------|--------|
| 1.9.22 | 8.2.x | 8.4+ | ✅ Stable |
| 2.0.0 | 8.4.x | 8.6+ | ✅ Stable |

### Compose + Kotlin + Compose Compiler
| Compose BOM | Kotlin | Compiler | Status |
|-------------|--------|----------|--------|
| 2024.02.00 | 1.9.22 | 1.5.10 | ✅ Stable |
| 2024.06.00 | 2.0.0 | Included | ✅ Stable |

### Hilt + AGP + KSP
| Hilt | AGP | KSP | Status |
|------|-----|-----|--------|
| 2.51 | 8.2+ | 1.9.22-1.0.18 | ✅ Stable |
```

---

### Phase 2: Update Planning

Develop a safe update strategy.

#### 2.1 Update Grouping Strategy

**Group related dependencies:**

```kotlin
// Group 1: AndroidX Foundation (update together)
val androidxCore = "1.13.1"
val androidxAppcompat = "1.7.0"
val androidxActivity = "1.9.0"
val androidxFragment = "1.8.0"

// Group 2: Lifecycle Components (update together)
val lifecycleVersion = "2.8.0"
// lifecycle-runtime-ktx, lifecycle-viewmodel-ktx, lifecycle-livedata-ktx

// Group 3: Compose Suite (use BOM)
val composeBom = "2024.06.00"
// All Compose dependencies versioned through BOM

// Group 4: Network Stack (update together)
val retrofitVersion = "2.11.0"
val okhttpVersion = "4.12.0"

// Group 5: Testing Suite (update together)
val junitVersion = "4.13.2"
val mockitoVersion = "5.11.0"
val truthVersion = "1.4.2"
```

**Rationale for grouping:**
- Related libraries often have interdependencies
- Reduces chance of version conflicts
- Simplifies troubleshooting if issues arise

#### 2.2 Update Order Strategy

**Recommended update order:**

```markdown
## Dependency Update Order

### Phase A: Build Tools (Foundation)
1. Gradle wrapper
2. Android Gradle Plugin (AGP)
3. Kotlin plugin and stdlib
4. KSP/KAPT plugins

### Phase B: Core Platform
5. AndroidX core libraries
6. AndroidX lifecycle components
7. AndroidX navigation

### Phase C: UI Layer
8. Compose BOM and components
9. Material Design
10. Coil/Glide (image loading)

### Phase D: Data Layer
11. Room database
12. DataStore
13. Retrofit/OkHttp

### Phase E: DI & Architecture
14. Hilt/Dagger
15. Coroutines
16. Kotlin serialization

### Phase F: Testing
17. JUnit, Espresso, Robolectric
18. MockK/Mockito
19. Compose testing
```

#### 2.3 Breaking Change Analysis

**Identify and plan for breaking changes:**

```kotlin
// Check release notes and migration guides for each update

// Example: Lifecycle 2.7.0 → 2.8.0 Breaking Changes
/*
1. Minimum Kotlin version increased to 1.9.22
2. New: repeatOnLifecycle extensions changed
3. Deprecated: LiveData.observe() with lambda
4. Removed: LifecycleRegistry.setCurrentState() (use handleLifecycleEvent)
*/

// Document migration requirements:
data class MigrationTask(
    val dependency: String,
    val fromVersion: String,
    val toVersion: String,
    val breakingChanges: List<String>,
    val migrationSteps: List<String>,
    val estimatedEffort: String
)
```

---

### Phase 3: Findings Presentation

**CHECKPOINT 1:** Present the dependency analysis and proposed update plan.

```markdown
## Dependency Update Analysis

### Current State
- **Total Dependencies:** [X]
- **Outdated:** [Y] ([Y/X]%)
- **Security Issues:** [Z]
- **Major Updates Available:** [N]

### Recommended Updates

#### Priority 1: Security Fixes (Immediate)
| Dependency | Current | Target | CVE/Issue |
|------------|---------|--------|-----------|
| [lib] | [v1] | [v2] | [CVE-XXXX-XXXX] |

#### Priority 2: Breaking Changes (Plan Required)
| Dependency | Current | Target | Migration Effort |
|------------|---------|--------|------------------|
| [lib] | [v1] | [v2] | [High/Med/Low] |

#### Priority 3: Safe Updates (Low Risk)
| Dependency | Current | Target | Notes |
|------------|---------|--------|-------|
| [lib] | [v1] | [v2] | Patch update |

### Compatibility Concerns
- [Any identified compatibility issues]

### Recommended Approach
1. [First batch of updates]
2. [Second batch of updates]
3. [Updates requiring migration]

**Would you like me to proceed with the updates in this order?**
```

---

### Phase 4: Update Implementation

Execute the dependency updates systematically.

#### 4.1 Pre-Update Preparation

**Ensure a clean starting point:**

```bash
# 1. Ensure clean git state
git status  # Should be clean
git checkout -b feature/dependency-updates

# 2. Verify current build passes
./gradlew clean build

# 3. Run full test suite
./gradlew test connectedAndroidTest

# 4. Note current build metrics
./gradlew app:dependencies > deps-before.txt
```

#### 4.2 Version Catalog Updates

**Update version catalog (libs.versions.toml):**

```toml
[versions]
# Build tools
agp = "8.4.0"
kotlin = "2.0.0"
ksp = "2.0.0-1.0.21"

# AndroidX
androidxCore = "1.13.1"
androidxLifecycle = "2.8.0"
androidxActivity = "1.9.0"
androidxNavigation = "2.7.7"

# Compose
composeBom = "2024.06.00"
composeCompiler = "1.5.14"  # Or use Kotlin 2.0 built-in

# Network
retrofit = "2.11.0"
okhttp = "4.12.0"

# DI
hilt = "2.51.1"

# Testing
junit = "4.13.2"
androidxTestCore = "1.5.0"
espresso = "3.5.1"

[libraries]
# AndroidX
androidx-core-ktx = { module = "androidx.core:core-ktx", version.ref = "androidxCore" }
androidx-lifecycle-runtime = { module = "androidx.lifecycle:lifecycle-runtime-ktx", version.ref = "androidxLifecycle" }
# ... continue for all dependencies

[plugins]
android-application = { id = "com.android.application", version.ref = "agp" }
kotlin-android = { id = "org.jetbrains.kotlin.android", version.ref = "kotlin" }
```

#### 4.3 Incremental Update Process

**Update in stages with verification:**

```kotlin
// Stage 1: Build Tools
// Update: AGP, Kotlin, Gradle wrapper

// Verify:
// ./gradlew clean build
// ./gradlew test

// Commit:
// git commit -m "build: update AGP to 8.4.0, Kotlin to 2.0.0"

// Stage 2: AndroidX Core
// Update: core-ktx, appcompat, activity, fragment

// Verify:
// ./gradlew clean build
// ./gradlew test
// Manual smoke test on device

// Commit:
// git commit -m "deps: update AndroidX core libraries"

// Continue for each stage...
```

#### 4.4 Migration Code Changes

**Handle breaking changes:**

```kotlin
// Example: Lifecycle 2.8.0 Migration

// Before: Old coroutine launch pattern
lifecycleScope.launchWhenStarted {
    viewModel.state.collect { state ->
        updateUI(state)
    }
}

// After: New repeatOnLifecycle pattern
lifecycleScope.launch {
    repeatOnLifecycle(Lifecycle.State.STARTED) {
        viewModel.state.collect { state ->
            updateUI(state)
        }
    }
}

// Example: Compose Navigation type-safe routes (2.8.0+)

// Before: String-based routes
composable("profile/{userId}") { backStackEntry ->
    val userId = backStackEntry.arguments?.getString("userId")
    ProfileScreen(userId)
}

// After: Type-safe routes
@Serializable
data class ProfileRoute(val userId: String)

composable<ProfileRoute> { backStackEntry ->
    val route = backStackEntry.toRoute<ProfileRoute>()
    ProfileScreen(route.userId)
}
```

#### 4.5 Deprecation Resolution

**Address deprecation warnings:**

```kotlin
// Find all deprecation warnings
// ./gradlew lint --warning-mode all 2>&1 | grep -i deprecat

// Common deprecation patterns:

// 1. LiveData observe with lifecycle owner
// Deprecated:
viewModel.data.observe(this) { data -> }
// Replacement:
viewModel.data.observe(viewLifecycleOwner) { data -> }

// 2. Fragment setRetainInstance
// Deprecated:
setRetainInstance(true)
// Replacement: Use ViewModel instead

// 3. Activity requestPermissions
// Deprecated:
requestPermissions(permissions, REQUEST_CODE)
// Replacement:
val launcher = registerForActivityResult(RequestPermission()) { }
launcher.launch(permission)

// 4. AsyncTask
// Deprecated: Entire class
// Replacement: Coroutines with viewModelScope
```

---

### Phase 5: Verification & Testing

Comprehensive verification of updates.

#### 5.1 Build Verification

**Verify successful build:**

```bash
# Clean build
./gradlew clean

# Full build
./gradlew build

# Check for warnings
./gradlew build --warning-mode all

# Verify lint passes
./gradlew lint

# Check dependency tree for conflicts
./gradlew app:dependencies
```

#### 5.2 Test Suite Execution

**Run comprehensive tests:**

```bash
# Unit tests
./gradlew test

# Instrumented tests
./gradlew connectedAndroidTest

# If using screenshot tests
./gradlew verifyPaparazziDebug

# Coverage report (if configured)
./gradlew jacocoTestReport
```

**Analyze test results:**
- [ ] All tests pass
- [ ] No new test failures
- [ ] Test execution time is comparable
- [ ] No flaky tests introduced

#### 5.3 Runtime Verification

**Manual testing checklist:**

```markdown
## Post-Update Testing Checklist

### Critical Paths
- [ ] App launches successfully
- [ ] Login/authentication flow
- [ ] Main feature workflows
- [ ] Data persistence (close and reopen)
- [ ] Network operations

### Regression Areas
- [ ] Areas using updated dependencies
- [ ] Screens with complex state
- [ ] Background processing
- [ ] Push notifications

### Configuration Changes
- [ ] Screen rotation
- [ ] Dark mode toggle
- [ ] Language change
- [ ] Back navigation

### Performance
- [ ] App startup time
- [ ] Screen transitions
- [ ] Memory usage (no new leaks)
```

#### 5.4 Compatibility Testing

**Test across configurations:**

```markdown
## Device Testing Matrix

| Configuration | Status | Notes |
|---------------|--------|-------|
| Min SDK (API [X]) | [Pass/Fail] | |
| Target SDK (API [Y]) | [Pass/Fail] | |
| Latest SDK (API [Z]) | [Pass/Fail] | |
| Low memory device | [Pass/Fail] | |
| Tablet | [Pass/Fail] | |
```

---

### Phase 6: Documentation & Commit

Document and commit the changes.

#### 6.1 Update Documentation

**Document the updates:**

```markdown
# Dependency Update - [Date]

## Summary
Updated [X] dependencies to latest stable versions.

## Major Updates
- **Kotlin**: 1.9.22 → 2.0.0
  - Migration notes: [link]
  - Breaking changes addressed: [list]

- **Lifecycle**: 2.7.0 → 2.8.0
  - Migration: Updated coroutine patterns
  - Files changed: [list]

## Security Fixes
- [CVE-XXXX-XXXX]: Updated [library] from [v1] to [v2]

## Breaking Changes Addressed
1. [Change and how it was handled]
2. [Change and how it was handled]

## Testing Performed
- Unit tests: [X] passed
- Integration tests: [X] passed
- Manual testing: Completed
- Devices tested: [list]

## Known Issues
- [Any known issues or follow-up work needed]
```

#### 6.2 Commit Strategy

**Commit with clear messages:**

```bash
# Option 1: Atomic commits per dependency group
git commit -m "build: update Kotlin to 2.0.0 and AGP to 8.4.0

- Updated Kotlin from 1.9.22 to 2.0.0
- Updated AGP from 8.2.0 to 8.4.0
- Updated Gradle wrapper from 8.4 to 8.7
- Added compose compiler Gradle plugin for Kotlin 2.0"

# Option 2: Single commit for all updates
git commit -m "deps: update all dependencies to latest stable versions

Major updates:
- Kotlin 1.9.22 → 2.0.0
- Lifecycle 2.7.0 → 2.8.0
- Compose BOM 2024.02.00 → 2024.06.00

Security fixes:
- CVE-XXXX: updated okhttp

All tests passing."
```

---

## Expected Output

### Dependency Update Report

```markdown
# Dependency Update Report

## Update Summary
| Metric | Value |
|--------|-------|
| Total Updates | [X] |
| Security Fixes | [Y] |
| Breaking Changes | [Z] |
| Migration Effort | [Hours] |

## Updates Applied

### Build Tools
| Dependency | Before | After | Notes |
|------------|--------|-------|-------|
| Kotlin | 1.9.22 | 2.0.0 | Major |
| AGP | 8.2.0 | 8.4.0 | Minor |
| Gradle | 8.4 | 8.7 | Minor |

### Libraries
| Dependency | Before | After | Notes |
|------------|--------|-------|-------|
| lifecycle-* | 2.7.0 | 2.8.0 | Migration required |
| compose-bom | 2024.02 | 2024.06 | Safe update |
| retrofit | 2.9.0 | 2.11.0 | Safe update |

## Migration Changes
### File: [path/to/file.kt]
```kotlin
// Code changes made
```

## Verification Results
- Build: ✅ Passing
- Unit Tests: ✅ [X]/[X] passing
- Integration Tests: ✅ [Y]/[Y] passing
- Manual Testing: ✅ Complete

## Remaining Work
- [ ] [Any follow-up tasks]
```

---

## Example Interaction

**User:** Our app hasn't been updated in 6 months. We need to update dependencies before our next release. We're particularly concerned about security.

**Agent:** I'll conduct a comprehensive dependency audit focusing on security and stability. Let me analyze your current dependencies.

*[Agent examines build.gradle.kts and libs.versions.toml]*

## Dependency Analysis

### Current State Overview
- **Total Dependencies:** 47
- **Outdated:** 23 (49%)
- **Security Vulnerabilities:** 2
- **Major Version Updates Available:** 4

### Critical Security Issues

| Library | Current | Fixed In | CVE | Severity |
|---------|---------|----------|-----|----------|
| okhttp | 4.9.0 | 4.12.0 | CVE-2023-0833 | High |
| json-kotlin | 1.2.0 | 1.4.1 | CVE-2023-2976 | Medium |

**Recommendation:** Update these immediately.

### Major Updates Requiring Migration

1. **Kotlin 1.8.22 → 2.0.0**
   - Compose compiler now integrated
   - K2 compiler (performance improvement)
   - Migration effort: Medium

2. **Lifecycle 2.5.1 → 2.8.0**
   - New coroutine patterns
   - Deprecations to address
   - Migration effort: Low

3. **Navigation 2.5.3 → 2.7.7**
   - Type-safe routes available
   - Migration effort: Low (optional new features)

### Safe Updates (23 dependencies)
All patch and minor updates with no breaking changes.

### Recommended Update Plan

**Phase 1 (Today): Security Fixes**
- okhttp 4.9.0 → 4.12.0
- json-kotlin 1.2.0 → 1.4.1

**Phase 2 (This Week): Core Platform**
- Kotlin 1.8.22 → 2.0.0
- AGP 7.4.0 → 8.4.0
- AndroidX core libraries

**Phase 3 (Next Week): Full Update**
- All remaining dependencies
- Migration of deprecated APIs

**Would you like me to start with Phase 1 security fixes?**

---

## Techniques Used

- **ST-01** (Clear Objective): Single-sentence objective for safe dependency updates
- **ST-02** (Sequential Instructions): Phased approach from analysis to implementation
- **RT-02** (Multi-Dimensional Analysis): Security, compatibility, and migration assessment
- **RT-04** (Best Practice Review): Follows dependency update best practices
- **RT-05** (Evidence-Based Reasoning): Version comparisons with changelog references
- **ST-03** (Output Format Templates): Structured inventory and update reports
- **OC-05** (Severity Classification): Risk categorization for updates
- **AG-02** (Skeptical Default Stance): Cautious approach to breaking changes
- **AG-12** (Quantitative Metrics): Version numbers, counts, compatibility matrices
- **NE-02** (Phased Workflow): Clear phases with checkpoints
- **NE-07** (Discussion Before Action): User approval before applying updates

---

## Related Prompts

- [android_dependency_audit.md](../analysis/android_dependency_audit.md) - Initial dependency analysis
- [android_version_upgrade.md](android_version_upgrade.md) - Target SDK upgrades
- [android_sdk_migration.md](android_sdk_migration.md) - Major SDK migrations
- [android_technical_debt_assessment.md](../analysis/android_technical_debt_assessment.md) - Broader technical debt
- [android_test_strategy_design.md](../testing/android_test_strategy_design.md) - Testing for regression prevention

---

## Customization Guide

### For Different Project Types

**New Projects:**
- Use latest stable versions from start
- Set up version catalog and BOMs
- Configure Dependabot/Renovate for automation

**Legacy Projects:**
- Prioritize security updates
- Stage major updates across releases
- Plan for deprecated API cleanup

**Library Projects:**
- Be conservative with minimum versions
- Test against multiple dependency versions
- Document supported version ranges

### For Different Risk Profiles

**High Stability (Production Critical):**
- Update only after thorough testing
- Use LTS/stable versions only
- Stage rollouts with monitoring

**Balanced Approach:**
- Update security issues immediately
- Minor updates in regular releases
- Major updates with dedicated testing

**Early Adopter:**
- Track RC/beta versions in dev
- Quick adoption of stable releases
- Active in issue reporting

### For CI/CD Integration

**Automated Checks:**
```yaml
# GitHub Actions example
- name: Check for dependency updates
  run: ./gradlew dependencyUpdates

- name: Security scan
  uses: dependency-check/Dependency-Check_Action@main

- name: Build verification
  run: ./gradlew build test
```

**Automated PRs:**
- Configure Dependabot for automatic PRs
- Set up merge requirements (tests, reviews)
- Use semantic PR titles for changelog
