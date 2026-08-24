---
name: android-release-pipeline
description: "End-to-end Android release workflow covering version bumping, changelog generation, signing config verification, ProGuard/R8 rules validation, bundle generation, and Play Console upload preparation. Use this skill when preparing a release build, when automating the release process, when verifying release readiness, or when a developer mentions 'release build', 'version bump', 'Play Console upload', 'signing config', or 'changelog generation'."
metadata:
  tags:
    - android
    - release
    - ci-cd
    - play-store
    - solo-developer
  updated: "2026-02-12"
---

# Android Release Pipeline

End-to-end release workflow for Android applications. Guides a developer through a structured release process covering version management, changelog generation, build configuration verification, signing, optimization validation, and Play Console upload preparation — ensuring every release is consistent, complete, and policy-compliant.

## Purpose

This skill eliminates the "did I forget something?" anxiety of releasing an Android app. Solo developers especially benefit because there is no team to catch missed steps. The workflow is designed to be run before every production release, producing a release checklist artifact that documents what was verified.

## When to Use This Skill

Use this skill when you need to:
- Prepare a production release build for Google Play
- Set up or verify a release automation pipeline (CI/CD)
- Create a consistent, repeatable release process
- Verify that signing, ProGuard, and build configs are correct before upload
- Generate changelogs from git history or commit messages
- Prepare a release candidate for internal/beta testing before promotion to production

## When NOT to Use This Skill

Do NOT use this skill when:
- You are doing a debug build for local testing (no release process needed)
- You need to fix a production crash (use incident response or crash triage skills)
- You are setting up CI/CD from scratch (use the CI/CD pipeline design prompt first)
- You are planning what features go into the release (use roadmap planning instead)

## Prerequisites

- Android project with a working debug build
- Release signing keystore configured (or ready to create one)
- Google Play Developer account with app already created
- Git repository with commit history for changelog generation

## Step 1: Version Management

### 1.1 Determine Version Numbers

```kotlin
// app/build.gradle.kts
android {
    defaultConfig {
        // versionCode: Monotonically increasing integer. Play Store rejects lower values.
        // Strategy: MAJOR*10000 + MINOR*100 + PATCH (e.g., 2.3.1 = 20301)
        versionCode = 20301

        // versionName: User-visible version string
        versionName = "2.3.1"
    }
}
```

### 1.2 Version Bump Checklist

- [ ] `versionCode` is incremented from the last published version
- [ ] `versionName` follows semantic versioning (MAJOR.MINOR.PATCH)
- [ ] Version is consistent across all modules (if multi-module)
- [ ] Version is tagged in git: `git tag v2.3.1`

### 1.3 Automated Version from Git Tags

```kotlin
// build.gradle.kts
val gitVersionCode: Int by lazy {
    val process = Runtime.getRuntime().exec("git rev-list --count HEAD")
    process.inputStream.bufferedReader().readText().trim().toInt()
}

val gitVersionName: String by lazy {
    val process = Runtime.getRuntime().exec("git describe --tags --abbrev=0")
    process.inputStream.bufferedReader().readText().trim().removePrefix("v")
}
```

## Step 2: Changelog Generation

### 2.1 From Git Commits

```bash
# Generate changelog since last release tag
git log v2.2.0..HEAD --pretty=format:"- %s" --no-merges > CHANGELOG_DRAFT.md

# Group by conventional commit type
git log v2.2.0..HEAD --pretty=format:"%s" --no-merges | \
  awk '/^feat/ {print "### New Features"; print "- " $0} /^fix/ {print "### Bug Fixes"; print "- " $0} /^perf/ {print "### Performance"; print "- " $0}'
```

### 2.2 Changelog Template

```markdown
## Version 2.3.1 (2026-02-12)

### New Features
- Added dark mode support for all screens
- New widget for home screen quick actions

### Bug Fixes
- Fixed crash when rotating device on settings screen
- Resolved sync issue with Firebase when offline

### Performance
- Reduced cold start time by 200ms via Baseline Profile update
- Optimized image loading cache strategy

### Internal
- Updated Compose BOM to 2024.12.01
- Migrated from KAPT to KSP for Hilt processing
```

## Step 3: Build Configuration Verification

### 3.1 Signing Configuration

```bash
# Verify keystore exists and is readable
ls -la release-keystore.jks

# Verify signing config in build.gradle.kts
grep -A 10 "signingConfigs" app/build.gradle.kts
```

Checklist:
- [ ] Release keystore file exists and is NOT checked into git
- [ ] Keystore password, key alias, and key password are stored securely (not in build files)
- [ ] Signing config is assigned to the release build type
- [ ] Keystore backup exists in a secure location (losing it = can never update the app)

### 3.2 Build Type Configuration

```bash
# Verify release build type settings
grep -A 20 "release {" app/build.gradle.kts
```

Checklist:
- [ ] `isMinifyEnabled = true` (R8 shrinking enabled)
- [ ] `isShrinkResources = true` (unused resource removal)
- [ ] `isDebuggable = false` (never deploy a debuggable release)
- [ ] ProGuard/R8 rules file is referenced
- [ ] No debug-only dependencies in release configuration
- [ ] No `debuggable true` override anywhere in the build

### 3.3 BuildConfig Verification

```bash
# Check for debug URLs or test keys in release config
grep -r "localhost\|10.0.2.2\|debug\|test.*key\|staging" app/src/release/
grep "buildConfigField" app/build.gradle.kts
```

Checklist:
- [ ] No localhost URLs in release buildConfigField
- [ ] No test/debug API keys in release configuration
- [ ] Feature flags set to production values

## Step 4: ProGuard/R8 Validation

### 4.1 Rules Verification

```bash
# Check ProGuard files exist
ls app/proguard-rules.pro
ls app/proguard-rules-*.pro 2>/dev/null

# Build release and check for warnings
./gradlew assembleRelease 2>&1 | grep -i "warning\|error"
```

Checklist:
- [ ] Keep rules exist for: Firebase, Room entities, Retrofit/Ktor models, Hilt, serialization classes
- [ ] No missing class warnings in R8 output
- [ ] Enums used in serialization have keep rules
- [ ] Parcelable/Serializable classes are kept
- [ ] Reflection-accessed classes are kept

### 4.2 Shrinking Effectiveness

```bash
# Compare debug vs release APK size
ls -la app/build/outputs/apk/debug/app-debug.apk
ls -la app/build/outputs/bundle/release/app-release.aab
```

- Target: Release AAB should be 30-60% smaller than debug APK
- If not, R8 rules may be over-keeping

## Step 5: Build and Bundle Generation

```bash
# Clean build to ensure no stale artifacts
./gradlew clean

# Build release AAB (required for Play Store since 2021)
./gradlew bundleRelease

# Verify the bundle was created
ls -la app/build/outputs/bundle/release/app-release.aab

# (Optional) Also build APK for direct distribution
./gradlew assembleRelease
```

### 5.1 Bundle Validation

```bash
# Install bundletool if not already
# Validate the bundle
java -jar bundletool.jar validate --bundle=app/build/outputs/bundle/release/app-release.aab

# Check bundle size
java -jar bundletool.jar get-size total --bundle=app/build/outputs/bundle/release/app-release.aab
```

Checklist:
- [ ] AAB is generated successfully (no build errors)
- [ ] Bundle size is within Play Store limits (150MB for AAB)
- [ ] Bundle validation passes with no errors
- [ ] Baseline Profiles are included in the bundle

## Step 6: Pre-Upload Testing

### 6.1 Install from Bundle on Test Device

```bash
# Generate APKs from bundle
java -jar bundletool.jar build-apks --bundle=app/build/outputs/bundle/release/app-release.aab --output=release.apks --ks=release-keystore.jks --ks-key-alias=key-alias

# Install on connected device
java -jar bundletool.jar install-apks --apks=release.apks
```

### 6.2 Smoke Test Checklist

- [ ] App launches without crash
- [ ] Login/auth flow works
- [ ] Core feature works end-to-end
- [ ] Firebase services connect (Analytics, Crashlytics, Auth)
- [ ] In-app purchases/subscriptions are accessible (if applicable)
- [ ] Deep links resolve correctly
- [ ] Push notifications are received
- [ ] No ProGuard-related crashes (check Crashlytics for obfuscation issues)

## Step 7: Play Console Upload Preparation

### 7.1 Store Listing Updates

- [ ] What's New text updated (matches changelog, under 500 characters)
- [ ] Screenshots updated if UI changed
- [ ] Feature graphic current
- [ ] App description reflects new features

### 7.2 Release Track Selection

| Track | Use Case | Rollout |
|-------|----------|---------|
| Internal testing | Team/stakeholder review | Immediate, up to 100 testers |
| Closed testing | Beta testers | Immediate to selected group |
| Open testing | Public beta | Immediate to anyone who opts in |
| Production | Public release | Staged: 1% → 5% → 20% → 50% → 100% |

### 7.3 Upload Checklist

- [ ] AAB uploaded to the correct track
- [ ] Release name set (e.g., "2.3.1 (20301)")
- [ ] Release notes added for each supported language
- [ ] Staged rollout percentage set (start at 1-5% for production)
- [ ] Managed publishing enabled (review before going live)
- [ ] Deobfuscation mapping file uploaded (for Crashlytics/Play Console crash reporting)

```bash
# Upload mapping file location
ls app/build/outputs/mapping/release/mapping.txt
```

## Step 8: Post-Release Monitoring

After the release is live:

- [ ] Monitor Crashlytics for new crash clusters (first 1-2 hours critical)
- [ ] Check Play Console for ANR rate and crash rate vs. previous version
- [ ] Monitor user reviews for new complaints
- [ ] Verify Firebase Analytics events are flowing
- [ ] If staged rollout: check metrics at each percentage before expanding
- [ ] Tag the release in git: `git tag -a v2.3.1 -m "Release 2.3.1"`

## Related Skills

- `android-quarterly-maintenance` - Quarterly review that may trigger a maintenance release
- `android-crash-triage` - If post-release monitoring reveals crashes
- `android-testing-patterns` - Testing strategy to improve pre-release confidence
