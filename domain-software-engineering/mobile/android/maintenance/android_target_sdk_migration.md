---
title: "Android Target SDK Version Migration Planner"
category: mobile-development
description: "Plan and execute targetSdkVersion upgrades (e.g., 34→35) by mapping behavior changes, required code modifications, testing plans, and Google Play deadline compliance"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DT-01
  - CM-01
  - QA-01
difficulty: intermediate
tags:
  - android
  - sdk-migration
  - targetSdk
  - maintenance
  - play-store
  - mobile-development
  - solo-developer
updated: "2026-02-11"
---

# Android Target SDK Version Migration Planner

**Objective:** Plan and execute a targetSdkVersion upgrade (e.g., API 34 → 35) by systematically mapping every behavior change introduced between the current and target API levels, identifying required code modifications, producing a test plan for affected features, estimating scope, and ensuring compliance with Google Play's annual target SDK deadline.

**When to Use:** Use this prompt annually when Google announces the new targetSdk requirement (typically at I/O in May, with an August 31 deadline for new apps and a November 1 deadline for existing app updates). Also use when proactively upgrading ahead of the deadline, or when upgrading compileSdk to access new APIs. This is a critical annual maintenance task — failure to comply means your app updates will be rejected from the Play Store.

**How this differs from `android_sdk_migration.md`:** The existing SDK migration prompt covers migration from deprecated APIs to modern replacements (e.g., AsyncTask → Coroutines). THIS prompt specifically covers the annual targetSdkVersion bump, which introduces mandatory behavior changes, new permission models, and platform restrictions that affect your existing code regardless of which APIs you use.

> **Role — Planner.** This prompt **plans** the targetSdk upgrade (behavior-change mapping, scope estimation, deadline tracking). To **execute** the plan — apply the code changes, run the test plan, and stage the rollout — hand the output to [`android_version_upgrade.md`](android_version_upgrade.md). The two chain: **planner (here) → executor**.

---

## Context Gathering

Before planning the migration, gather:

1. **Current State:**
   - "What is your current targetSdkVersion?"
   - "What is your current compileSdkVersion?"
   - "What is your minSdkVersion?"
   - "What Android Gradle Plugin version are you using?"

2. **Target State:**
   - "What targetSdkVersion are you migrating to?"
   - "Are you also updating compileSdk and/or minSdk?"
   - "What is the Google Play deadline for this target SDK?"

3. **App Characteristics:**
   - "Does your app use background services or work scheduling?"
   - "Does your app request runtime permissions?"
   - "Does your app use notifications?"
   - "Does your app access media files (photos, videos, audio)?"
   - "Does your app use foreground services? If so, what types?"
   - "Does your app use exact alarms?"
   - "Does your app use broadcast receivers declared in the manifest?"
   - "Does your app target large screens or foldables?"

4. **Dependencies:**
   - "Are there third-party libraries that may not be compatible with the new target SDK?"
   - "Do you use any native (NDK) code?"
   - "Are you using any deprecated APIs that the new target SDK enforces?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before flagging ANY required change, you MUST:**

1. **Verify the behavior change applies to your target API level** - Not all changes apply at every API level. Changes are cumulative from the API level they were introduced.
2. **Confirm the change affects targetSdk, not just compileSdk** - Some changes are compileSdk-only (new APIs available). Others are enforced when targeting that SDK level.
3. **Check if the app actually uses the affected feature** - Don't flag changes for features the app doesn't use.
4. **Distinguish between hard requirements and recommendations** - Some changes will break the app; others are best practices.
5. **Verify against official Android documentation** - Use the official "Behavior changes for apps targeting Android [X]" documentation.

**Finding that migration requires minimal changes is an acceptable outcome.** Well-architected apps following modern patterns may only need version number bumps and minor adjustments.

### False-Positive Prevention

- ❌ Do NOT flag behavior changes from API levels below the CURRENT target (those are already handled)
- ❌ Do NOT confuse compileSdk-only changes with targetSdk behavior changes
- ❌ Do NOT flag changes for features the app doesn't use
- ❌ Do NOT assume all deprecated APIs will stop working (most continue to work, just with warnings)
- ✅ DO only flag behavior changes for API levels BETWEEN current and target (exclusive of current, inclusive of target)
- ✅ DO verify each change against the official behavior changes documentation
- ✅ DO check if the app's libraries have published target SDK compatibility notes
- ✅ DO test on actual devices/emulators running the target API level

---

### Phase 1: Behavior Change Mapping

For each API level between current targetSdk (exclusive) and new targetSdk (inclusive), document every behavior change.

#### 1.1 Change Inventory Template

For each behavior change:

```markdown
### [Change ID]: [Short Description]

**API Level Introduced:** [API level]
**Category:** [Permissions / Privacy / Security / UI / Background / Storage / Networking / Other]
**Impact on Your App:** [High / Medium / Low / None]

**What Changed:**
[Description of the platform behavior change]

**Affects Your App If:**
[Conditions under which this change impacts the app]

**Does Your App Use This?** [Yes / No / Uncertain — needs investigation]

**Required Code Changes:**
```kotlin
// Before (current behavior)
[Old code pattern]

// After (required for new targetSdk)
[New code pattern]
```

**Testing Required:**
- [ ] [Specific test scenario]
- [ ] [Edge case to verify]

**Risk Level:** [Breaking / Degraded UX / Cosmetic / None]
```

#### 1.2 Common Behavior Change Categories

**Permissions changes (most common migration work):**
- New runtime permissions added
- Permission behavior changes (e.g., notification permission in API 33)
- Granular media permissions (API 33+)
- Permission auto-revocation for unused apps
- Background location restrictions

**Privacy and security changes:**
- Package visibility restrictions
- Clipboard access restrictions
- Non-resettable identifier restrictions
- PendingIntent mutability requirements
- Exported component requirements

**Background execution changes:**
- Foreground service type requirements
- Exact alarm restrictions
- Broadcast receiver restrictions
- Background activity launch restrictions
- JobScheduler and WorkManager changes

**Storage changes:**
- Scoped storage enforcement
- Media permission granularity
- Photo picker requirements

**UI and UX changes:**
- Edge-to-edge enforcement
- Predictive back gesture requirements
- Large screen and foldable requirements
- Dynamic color and Material You changes

---

### Phase 2: Impact Assessment

#### 2.1 Change-by-Change Impact Matrix

| Change | Category | App Uses Feature | Code Change Needed | Test Effort | Risk |
|--------|----------|-----------------|-------------------|-------------|------|
| [Change 1] | [Cat] | [Yes/No/TBD] | [None/Minor/Major] | [Low/Med/High] | [Breaking/Low/None] |
| [Change 2] | [Cat] | [Yes/No/TBD] | [None/Minor/Major] | [Low/Med/High] | [Breaking/Low/None] |

#### 2.2 Scope Summary

```markdown
**Migration Scope Summary:**
- Total behavior changes to review: [X]
- Changes affecting this app: [Y]
- Breaking changes requiring code modification: [Z]
- Non-breaking changes requiring testing only: [W]

**Estimated effort:**
- Code changes: [Count of files/components to modify]
- New tests needed: [Count]
- Manual testing scenarios: [Count]
```

#### 2.3 Dependency Compatibility Check

For each major dependency:

| Library | Current Version | Target SDK Compatible? | Update Required? | Notes |
|---------|----------------|----------------------|-----------------|-------|
| [Library] | [Version] | [Yes/No/Unknown] | [Yes/No] | [Notes] |

**Check these common libraries for compatibility:**
- AndroidX libraries (core, appcompat, fragment, activity, lifecycle)
- Firebase SDK
- Google Play Services
- Retrofit / OkHttp
- Room / SQLDelight
- Hilt / Dagger
- Compose (compiler and BOM)
- Navigation
- WorkManager
- Ad SDKs (AdMob, etc.)

---

### Phase 3: Migration Plan

#### 3.1 Pre-Migration Checklist

- [ ] Current app builds and all tests pass on current targetSdk
- [ ] All dependencies updated to latest stable versions
- [ ] Android Gradle Plugin updated to support new compileSdk
- [ ] Kotlin version is compatible with new AGP
- [ ] Compose compiler version matches Kotlin version (if using Compose)
- [ ] Baseline branch created for rollback if needed

#### 3.2 Migration Steps (Ordered)

**Step 1: Update build configuration**
```kotlin
// build.gradle.kts (app module)
android {
    compileSdk = [NEW_COMPILE_SDK]

    defaultConfig {
        targetSdk = [NEW_TARGET_SDK]
        // minSdk stays the same unless intentionally updating
    }
}
```

**Step 2: Fix compilation errors**
- Address any new compilation warnings or errors from the updated compileSdk
- Update deprecated API calls flagged by the compiler

**Step 3: Address breaking behavior changes (in priority order)**
For each breaking change identified in Phase 2:
1. [Change]: [Specific code modification]
2. [Change]: [Specific code modification]

**Step 4: Address non-breaking behavior changes**
For each non-breaking change:
1. [Change]: [Verification or minor adjustment]

**Step 5: Update AndroidManifest.xml**
- Add any newly required manifest declarations
- Update exported component declarations if needed
- Add foreground service types if needed
- Update permission declarations

**Step 6: Run full test suite**
- Unit tests
- Integration tests
- UI tests (Espresso / Compose)

**Step 7: Manual testing on target API emulator/device**
- Test all features affected by behavior changes
- Test on both minimum SDK and target SDK devices

#### 3.3 Rollback Plan

If migration causes critical issues:
1. Revert targetSdk in build.gradle.kts
2. Revert any behavior-change-specific code modifications
3. Keep dependency updates that aren't causing issues
4. Document what failed for the next attempt

---

### Phase 4: Testing Plan

#### 4.1 Automated Test Updates

For each behavior change that requires code modification:

```markdown
**Change:** [Description]
**Test Type:** [Unit / Integration / UI]
**Test Scenario:**
- Given: [Precondition]
- When: [Action]
- Then: [Expected behavior on new targetSdk]

**New Test:**
```kotlin
@Test
fun `feature works correctly on API [X]`() {
    // Test implementation
}
```
```

#### 4.2 Manual Testing Checklist

**Test on devices/emulators running the TARGET API level:**

- [ ] App launches successfully
- [ ] All permissions are requested and granted properly
- [ ] Notifications display correctly (if permission-gated)
- [ ] Background work executes as expected
- [ ] Foreground services start and display correctly
- [ ] File access works (scoped storage)
- [ ] Deep links resolve correctly
- [ ] Back navigation works as expected (predictive back if applicable)
- [ ] All third-party SDKs function correctly (analytics, crash reporting, ads)
- [ ] App works on large screens / foldables (if targeting)

**Test on devices/emulators running the MINIMUM SDK level:**
- [ ] Backward compatibility maintained
- [ ] No new crashes on older devices
- [ ] Permission flows work on older API levels

#### 4.3 Play Store Pre-Launch Report

Before submission:
- [ ] Run the Play Console pre-launch report
- [ ] Check for new accessibility issues
- [ ] Check for new security warnings
- [ ] Verify on all device form factors tested by Firebase Test Lab

---

### Phase 5: Google Play Compliance

#### 5.1 Deadline Tracking

```markdown
**Google Play Target SDK Requirements for [Year]:**

| Deadline | Requirement | Status |
|----------|-------------|--------|
| [Month Day] | New apps must target API [X] | [Met / Pending] |
| [Month Day] | Updated apps must target API [X] | [Met / Pending] |
| [Month Day] | Existing apps may be restricted if below API [X-1] | [Met / Pending] |
```

#### 5.2 Submission Checklist

- [ ] targetSdkVersion meets or exceeds requirement
- [ ] Data Safety section updated if behavior changes affect data collection
- [ ] Privacy policy updated if new permissions or data practices
- [ ] Content rating questionnaire reviewed
- [ ] Release notes mention compatibility improvements
- [ ] Staged rollout configured (don't go to 100% immediately)

---

## Expected Output

### Target SDK Migration Report

```markdown
# Target SDK Migration Plan: API [Current] → API [Target]

## Summary
- **Current targetSdk:** [Current]
- **New targetSdk:** [Target]
- **Google Play deadline:** [Date]
- **Behavior changes to address:** [X total, Y breaking, Z testing-only]
- **Estimated code changes:** [Scope description]
- **Dependencies to update:** [Count]

## Breaking Changes Requiring Code Modification

### 1. [Change Name]
**Impact:** [Description of what breaks]
**Fix:** [Specific code changes required]
**Files affected:** [List]
**Test plan:** [How to verify]

### 2. [Change Name]
[Same format]

## Non-Breaking Changes Requiring Testing

| Change | What to Test | Expected Behavior |
|--------|-------------|-------------------|
| [Change] | [Test] | [Expected] |

## Dependency Update Plan

| Library | Current | Update To | Breaking Changes |
|---------|---------|-----------|-----------------|
| [Lib] | [Ver] | [Ver] | [None / Description] |

## Migration Timeline

| Phase | Tasks | Status |
|-------|-------|--------|
| Pre-migration | Update deps, create branch | [ ] |
| Build config | Update compileSdk, targetSdk | [ ] |
| Code changes | [Count] breaking changes | [ ] |
| Testing | Unit + integration + manual | [ ] |
| Staged rollout | 1% → 5% → 20% → 100% | [ ] |
| Verify | Monitor crash rate and ANRs | [ ] |

## Rollback Plan
[Steps to revert if critical issues found]
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) - Migration objective defined
- **ST-02** (Structured Sequential Instructions) - Phased migration process
- **RT-02** (Multi-Dimensional Analysis) - Permissions, privacy, background, storage, UI dimensions
- **RT-05** (Evidence-Based Reasoning) - Official behavior change documentation citations
- **DT-01** (Hierarchical Task Breakdown) - Migration decomposed into phases and steps
- **CM-01** (Explicit Context Framing) - App-specific context for change applicability
- **QA-01** (Chain-of-Verification) - Pre-migration and post-migration verification

---

## Related Prompts

- `android_sdk_migration.md` - General deprecated API migration (AsyncTask → Coroutines, etc.)
- `android_version_upgrade.md` - Android version upgrade guidance
- `android_dependency_update.md` - Dependency update management
- `play_store_policy_compliance_check.md` - Policy compliance audit
- `android_dependency_audit.md` - Dependency security audit
- `android_build_toolchain_upgrade.md` - AGP/Gradle/Kotlin/JDK upgrades often paired with a targetSdk bump
- `android_min_sdk_raise_planner.md` - The complementary minSdk (drop-old-OS) decision

---

## Customization Guide

- **For minor version bumps (e.g., 34→35):** Focus on the single API level's behavior changes
- **For multi-level jumps (e.g., 31→35):** Expand Phase 1 to cover ALL intervening levels; prioritize breaking changes across all levels
- **For apps with extensive background work:** Expand the background execution changes section with WorkManager, foreground service, and alarm specifics
- **For apps with file access:** Expand the storage changes section with scoped storage migration details
- **For apps using camera/microphone:** Expand the permission changes section with detailed runtime permission flow updates
- **For Compose apps:** Focus on UI behavior changes, predictive back gesture, and edge-to-edge enforcement
- **For apps with legacy XML views:** Add View system-specific changes and window inset handling updates
