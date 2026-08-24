---
title: "Android CI/CD Pipeline Design"
category: devops
description: "Design a CI/CD pipeline for a solo Android developer — GitHub Actions for build, test, lint, and deploy with Firebase App Distribution and Play Console automation"
techniques:
  - ST-01
  - ST-02
  - DT-01
  - CM-01
  - CM-02
  - RT-03
  - DS-06
difficulty: intermediate
tags:
  - android
  - ci-cd
  - github-actions
  - devops
  - automation
  - firebase
  - solo-developer
updated: "2026-02-11"
---

# Android CI/CD Pipeline Design

**Objective:** Design a CI/CD pipeline for a solo Android developer — covering GitHub Actions workflows for build, test, lint, and deploy, Firebase App Distribution for testing builds, Play Console upload automation, cost optimization for free-tier GitHub Actions, and signing key management — producing a pipeline configuration that automates repetitive tasks and catches issues before they reach users.

**When to Use:** Use this prompt when setting up a new Android project, when you're tired of manually building and uploading APKs/AABs, when you want to catch bugs before they ship, or when your manual release process has caused errors. CI/CD is the #1 automation force multiplier for a solo developer — it replaces 30-60 minutes of manual work per release with a single button push.

**Important context:** For a solo developer, CI/CD is not about the "enterprise best practices" you read about. You don't need 50 parallel test jobs, a staging environment, canary deployments, or Kubernetes orchestration. You need: (1) automated builds that catch errors, (2) automated tests that catch regressions, (3) automated distribution to testers, and (4) automated upload to the Play Store. This prompt gives you exactly that — no more, no less.

---

## Context Gathering

Before designing the pipeline, gather essential context:

1. **Current Setup:**
   - "Where is your code hosted (GitHub, GitLab, Bitbucket)?"
   - "How do you currently build and release your app?"
   - "Do you have any existing CI/CD configuration?"
   - "How often do you release (weekly, biweekly, monthly)?"

2. **Project Details:**
   - "What build tools do you use (Gradle, Gradle with KTS)?"
   - "Do you have unit tests? UI tests? How many?"
   - "Do you use lint, detekt, or other static analysis?"
   - "Do you have build flavors or variants (free/paid, dev/prod)?"

3. **Distribution:**
   - "Do you use Firebase App Distribution for beta testing?"
   - "Do you upload to Play Console manually or via API?"
   - "Do you have separate signing keys for debug and release?"
   - "Do you use Play App Signing?"

4. **Constraints:**
   - "Are you on GitHub's free tier (2,000 minutes/month)?"
   - "Do you need to keep builds fast (< 15 minutes)?"
   - "Do you have secrets to manage (signing keys, API keys)?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before designing ANY pipeline, you MUST:**

1. **Start simple** — A complex pipeline that breaks constantly is worse than a simple one that works every time. Begin with build + lint, add more stages later.
2. **Respect free tier limits** — GitHub Actions free tier gives 2,000 minutes/month. Android builds take 5-15 minutes. Plan accordingly.
3. **Secure signing keys** — Never commit signing keys or passwords to the repository. Use GitHub Secrets or equivalent.
4. **Test the pipeline itself** — A CI/CD pipeline that fails on every push because of misconfiguration wastes more time than it saves.
5. **Make failures actionable** — If a build fails, the developer must understand why quickly. Clear error messages, not 500 lines of logs.

### False-Positive Prevention

- ❌ Do NOT design a 45-minute pipeline with 10 parallel jobs — this burns free tier minutes and is overkill for a solo developer
- ❌ Do NOT require all tests to pass on every push to feature branches — flaky UI tests will block all development
- ❌ Do NOT store signing keys in the repository, even encrypted
- ❌ Do NOT automate Play Store production deployment without manual approval
- ❌ Do NOT skip the build cache — uncached Android builds are 3-5x slower
- ✅ DO keep the pipeline under 15 minutes for the fast-feedback loop
- ✅ DO use build caching aggressively (Gradle build cache, dependency cache)
- ✅ DO separate PR checks (fast) from release builds (thorough)
- ✅ DO include a manual approval step before production deployment
- ✅ DO monitor GitHub Actions minutes usage to stay within free tier

---

### Phase 1: Pipeline Architecture

#### 1.1 Recommended Pipeline Structure

```
┌─────────────────────────────────────────────────────┐
│ PR / Push to feature branch                          │
│ ├── Build (debug) .............. 3-5 min            │
│ ├── Lint ...................... 1-2 min              │
│ └── Unit Tests ............... 2-4 min              │
│     Total: ~8-10 min                                │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│ Merge to main                                        │
│ ├── Build (release) ........... 5-8 min             │
│ ├── Lint ...................... 1-2 min              │
│ ├── Unit Tests ............... 2-4 min              │
│ ├── Build AAB ................ 2-3 min              │
│ └── Deploy to Firebase App Distribution .. 1 min    │
│     Total: ~12-15 min                               │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│ Tag / Manual trigger (Release)                       │
│ ├── Build (release) ........... 5-8 min             │
│ ├── Full test suite ........... 5-10 min            │
│ ├── Build signed AAB ......... 2-3 min              │
│ ├── Generate changelog ........ 1 min               │
│ └── Upload to Play Console .... 1 min               │
│     Total: ~15-20 min                               │
│ ⚠️ Manual approval before production rollout         │
└─────────────────────────────────────────────────────┘
```

#### 1.2 GitHub Actions Minutes Budget

On the free tier (2,000 minutes/month):

| Trigger | Frequency | Duration | Monthly Minutes |
|---------|-----------|----------|----------------|
| PR checks | ~20 PRs/month | 10 min | 200 min |
| Main branch builds | ~20 merges/month | 15 min | 300 min |
| Release builds | ~4/month | 20 min | 80 min |
| **Total** | | | **580 min** |
| **Headroom** | | | **1,420 min** |

**Optimization tips to stay within free tier:**
- Use `paths` filters to skip CI on docs-only changes
- Cancel in-progress runs when new commits push to the same PR
- Cache Gradle dependencies and build outputs aggressively
- Use `ubuntu-latest` (Linux) runners — macOS runners cost 10x more minutes

---

### Phase 2: GitHub Actions Workflow Files

#### 2.1 PR Check Workflow (Fast Feedback)

```yaml
# .github/workflows/pr-check.yml
name: PR Check

on:
  pull_request:
    branches: [main]
    paths-ignore:
      - '**.md'
      - 'docs/**'

concurrency:
  group: pr-${{ github.event.pull_request.number }}
  cancel-in-progress: true

jobs:
  check:
    runs-on: ubuntu-latest
    timeout-minutes: 15

    steps:
      - uses: actions/checkout@v4

      - name: Set up JDK
        uses: actions/setup-java@v4
        with:
          distribution: 'temurin'
          java-version: '17'

      - name: Setup Gradle
        uses: gradle/actions/setup-gradle@v3
        with:
          cache-read-only: ${{ github.ref != 'refs/heads/main' }}

      - name: Lint
        run: ./gradlew lintDebug

      - name: Unit Tests
        run: ./gradlew testDebugUnitTest

      - name: Build Debug
        run: ./gradlew assembleDebug

      - name: Upload lint results
        if: failure()
        uses: actions/upload-artifact@v4
        with:
          name: lint-results
          path: app/build/reports/lint-results-debug.html

      - name: Upload test results
        if: failure()
        uses: actions/upload-artifact@v4
        with:
          name: test-results
          path: app/build/reports/tests/testDebugUnitTest/
```

#### 2.2 Main Branch Build + Firebase Distribution

```yaml
# .github/workflows/build-distribute.yml
name: Build and Distribute

on:
  push:
    branches: [main]
    paths-ignore:
      - '**.md'
      - 'docs/**'

jobs:
  build:
    runs-on: ubuntu-latest
    timeout-minutes: 20

    steps:
      - uses: actions/checkout@v4

      - name: Set up JDK
        uses: actions/setup-java@v4
        with:
          distribution: 'temurin'
          java-version: '17'

      - name: Setup Gradle
        uses: gradle/actions/setup-gradle@v3

      - name: Lint
        run: ./gradlew lintRelease

      - name: Unit Tests
        run: ./gradlew testReleaseUnitTest

      - name: Build Release APK
        run: ./gradlew assembleRelease
        env:
          KEYSTORE_PASSWORD: ${{ secrets.KEYSTORE_PASSWORD }}
          KEY_ALIAS: ${{ secrets.KEY_ALIAS }}
          KEY_PASSWORD: ${{ secrets.KEY_PASSWORD }}

      - name: Distribute to Firebase App Distribution
        uses: wzieba/Firebase-Distribution-Github-Action@v1
        with:
          appId: ${{ secrets.FIREBASE_APP_ID }}
          serviceCredentialsFileContent: ${{ secrets.FIREBASE_SERVICE_ACCOUNT }}
          groups: internal-testers
          file: app/build/outputs/apk/release/app-release.apk
          releaseNotes: |
            Build: ${{ github.run_number }}
            Commit: ${{ github.sha }}
```

#### 2.3 Release Workflow (Play Store Upload)

```yaml
# .github/workflows/release.yml
name: Release to Play Store

on:
  push:
    tags:
      - 'v*'

jobs:
  release:
    runs-on: ubuntu-latest
    timeout-minutes: 25

    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0  # Full history for changelog

      - name: Set up JDK
        uses: actions/setup-java@v4
        with:
          distribution: 'temurin'
          java-version: '17'

      - name: Setup Gradle
        uses: gradle/actions/setup-gradle@v3

      - name: Run full test suite
        run: ./gradlew testReleaseUnitTest lintRelease

      - name: Decode keystore
        run: echo "${{ secrets.KEYSTORE_BASE64 }}" | base64 --decode > app/release.keystore

      - name: Build Release AAB
        run: ./gradlew bundleRelease
        env:
          KEYSTORE_PASSWORD: ${{ secrets.KEYSTORE_PASSWORD }}
          KEY_ALIAS: ${{ secrets.KEY_ALIAS }}
          KEY_PASSWORD: ${{ secrets.KEY_PASSWORD }}

      - name: Upload mapping file
        uses: actions/upload-artifact@v4
        with:
          name: mapping
          path: app/build/outputs/mapping/release/mapping.txt

      - name: Upload AAB to Play Console
        uses: r0adkll/upload-google-play@v1
        with:
          serviceAccountJsonPlainText: ${{ secrets.PLAY_SERVICE_ACCOUNT }}
          packageName: com.your.package
          releaseFiles: app/build/outputs/bundle/release/app-release.aab
          track: internal  # Start with internal, promote manually
          mappingFile: app/build/outputs/mapping/release/mapping.txt
          status: completed

      - name: Create GitHub Release
        uses: softprops/action-gh-release@v1
        with:
          generate_release_notes: true
          files: |
            app/build/outputs/bundle/release/app-release.aab
```

---

### Phase 3: Secrets Management

#### 3.1 Required Secrets

Set these in GitHub Repository Settings → Secrets:

| Secret | What It Is | How to Get It |
|--------|-----------|---------------|
| `KEYSTORE_BASE64` | Base64-encoded keystore file | `base64 -i release.keystore` |
| `KEYSTORE_PASSWORD` | Keystore password | Your keystore password |
| `KEY_ALIAS` | Key alias | Your key alias |
| `KEY_PASSWORD` | Key password | Your key password |
| `FIREBASE_APP_ID` | Firebase app ID | Firebase Console → Project Settings |
| `FIREBASE_SERVICE_ACCOUNT` | Firebase service account JSON | GCP Console → IAM → Service Accounts |
| `PLAY_SERVICE_ACCOUNT` | Play Console service account JSON | Play Console → Setup → API access |

#### 3.2 Service Account Setup for Play Console

```bash
# 1. Create a service account in GCP Console
# 2. Grant the role "Service Account User"
# 3. Create a JSON key and save it
# 4. In Play Console → Setup → API access → Link the service account
# 5. Grant "Release to production" permission (or "Release to testing" for safer setup)
# 6. Add the JSON key contents as a GitHub Secret
```

#### 3.3 Gradle Signing Configuration

```kotlin
// app/build.gradle.kts
android {
    signingConfigs {
        create("release") {
            storeFile = file("release.keystore")
            storePassword = System.getenv("KEYSTORE_PASSWORD") ?: ""
            keyAlias = System.getenv("KEY_ALIAS") ?: ""
            keyPassword = System.getenv("KEY_PASSWORD") ?: ""
        }
    }
    buildTypes {
        release {
            signingConfig = signingConfigs.getByName("release")
            isMinifyEnabled = true
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
        }
    }
}
```

---

### Phase 4: Build Optimization

#### 4.1 Caching Strategy

The Gradle Actions plugin handles most caching automatically. Additional optimizations:

```properties
# gradle.properties
org.gradle.caching=true
org.gradle.parallel=true
org.gradle.daemon=true
org.gradle.jvmargs=-Xmx2048m -XX:MaxMetaspaceSize=512m
```

#### 4.2 Build Time Targets

| Stage | Target | If Exceeds |
|-------|--------|------------|
| PR check (total) | < 10 min | Review test count, add caching |
| Main build (total) | < 15 min | Reduce test scope, parallelize |
| Release build (total) | < 20 min | Acceptable — runs infrequently |
| Gradle dependency resolution | < 30 sec | Check for missing caches |
| Compilation | < 3 min | Check for unnecessary modules |

#### 4.3 Skipping Unnecessary Work

```yaml
# Skip CI on docs-only changes
paths-ignore:
  - '**.md'
  - 'docs/**'
  - '.gitignore'
  - 'LICENSE'

# Cancel previous runs on same PR
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```

---

### Phase 5: Release Process

#### 5.1 Recommended Release Flow

```
1. Develop on feature branches
2. PR to main → PR checks run (build + lint + test)
3. Merge to main → Build + distribute to Firebase App Distribution
4. Testers verify on Firebase App Distribution
5. Ready to release → Create git tag (v1.2.3)
6. Tag triggers release workflow → Build AAB + upload to Play Console internal track
7. In Play Console → Promote from internal to production (manual)
8. Monitor staged rollout in Play Console
```

#### 5.2 Version Management

```kotlin
// Version in build.gradle.kts
android {
    defaultConfig {
        versionCode = calculateVersionCode() // Auto-increment or CI build number
        versionName = "1.2.3" // Semantic versioning
    }
}

// Option: Use git tag for version
fun calculateVersionCode(): Int {
    val process = Runtime.getRuntime().exec("git rev-list --count HEAD")
    return process.inputStream.bufferedReader().readText().trim().toIntOrNull() ?: 1
}
```

---

## Expected Output

### CI/CD Pipeline Specification

```markdown
# CI/CD Pipeline: [App Name]

## Pipeline Overview
- **Platform:** GitHub Actions
- **Estimated monthly minutes:** [N] / 2,000 free
- **PR check duration:** ~[N] min
- **Release build duration:** ~[N] min

## Workflows

| Workflow | Trigger | Steps | Duration |
|----------|---------|-------|----------|
| PR Check | Pull request | Build, lint, test | ~10 min |
| Build & Distribute | Merge to main | Build, test, Firebase dist | ~15 min |
| Release | Git tag v* | Full test, AAB, Play Console | ~20 min |

## Secrets Configuration
[List of required secrets with setup instructions]

## Release Process
[Step-by-step release flow]

## Cost
- Monthly GitHub Actions: ~[N] minutes (free tier)
- Firebase App Distribution: Free
- Play Console service account: Free

## Setup Checklist
- [ ] GitHub Actions workflows created
- [ ] Secrets configured in GitHub
- [ ] Firebase App Distribution configured
- [ ] Play Console API access configured
- [ ] Signing key securely stored
- [ ] First PR check verified
- [ ] First release pipeline verified
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) - CI/CD pipeline focus
- **ST-02** (Structured Sequential Instructions) - Phased pipeline design
- **DT-01** (Hierarchical Task Breakdown) - Pipeline stages broken into steps
- **CM-01** (Explicit Context Framing) - Solo developer constraints and free tier limits
- **CM-02** (Constraint Specification) - Build time targets, minute budgets
- **RT-03** (Tree of Thoughts) - Pipeline options for different triggers
- **DS-06** (Prioritization Guidance) - Essential vs optional pipeline stages

---

## Related Prompts

- `play_store_pre_launch_checklist.md` - Pre-launch requirements (CI/CD helps automate many of these)
- `android_target_sdk_migration.md` - SDK migration that CI/CD validates
- `firebase_cloud_functions_design.md` - Cloud Functions deployment automation
- `solo_dev_weekly_operating_rhythm.md` - CI/CD frees time in the weekly schedule
- `devops_cicd_pipeline_analysis.md` - General CI/CD pipeline analysis

---

## Customization Guide

- **For GitLab:** Replace GitHub Actions with GitLab CI (.gitlab-ci.yml). The concepts are identical; the YAML syntax differs.
- **For apps with UI tests:** Add an emulator step for instrumented tests, but only on merge to main (not PR checks — too slow and flaky).
- **For multi-module projects:** Parallelize module builds with `./gradlew assembleDebug --parallel` and consider caching per module.
- **For apps with build flavors:** Add a matrix strategy for flavors, but be mindful of minutes — 3 flavors × 10 minutes = 30 minutes per run.
- **For teams (> 1 developer):** Add required status checks on the main branch, code owner review requirements, and deployment approval gates.
