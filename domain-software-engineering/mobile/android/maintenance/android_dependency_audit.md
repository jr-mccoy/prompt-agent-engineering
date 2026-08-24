---
title: "Android Dependency Audit"
category: mobile-development
description: "Systematic dependency audit for Android projects — identify outdated libraries, check for known CVEs, assess abandonment risk, find alternatives for risky dependencies, and produce a prioritized update plan."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-01
  - DS-06
difficulty: intermediate
tags:
  - android
  - maintenance
  - dependencies
  - security
  - gradle
  - version-catalog
  - solo-developer
updated: "2026-02-11"
---

# Android Dependency Audit

**Objective:** Perform a systematic audit of every dependency in an Android project — cataloging current versions, checking for known security vulnerabilities (CVEs), assessing each library's health and abandonment risk, identifying safer alternatives where needed, and producing a prioritized update plan that a solo developer can execute incrementally over one or two sprints.

**When to Use:** Run this audit quarterly as part of routine maintenance, immediately after receiving a security advisory affecting any dependency, before a major release, or when you notice build warnings about deprecated APIs. This audit is also valuable when onboarding to an inherited codebase or when Play Store policy changes require minimum SDK or library version bumps.

**Important context:** Dependencies are the hidden attack surface and maintenance burden of any Android app. A single abandoned library with a known CVE can get your app flagged by Play Protect. But blindly updating everything at once is a recipe for regression. This audit gives you a risk-scored, prioritized approach.

> **Which dependency prompt do I want?** Three prompts share this space, by depth and intent:
> - **This file (comprehensive audit + paydown):** full CVE + abandonment-risk scan with a prioritized, multi-sprint update plan — best for quarterly maintenance or an inherited codebase.
> - [`../analysis/android_dependency_audit.md`](../analysis/android_dependency_audit.md) **(quick modular audit):** a fast freshness/CVE read with safe-update recommendations — best as a focused follow-up to a health assessment.
> - [`android_dependency_update.md`](android_dependency_update.md) **(executor):** safely *applies* a specific set of updates with breaking-change analysis and verification.
> For data-collecting SDKs (Firebase, ads, analytics), use [`android_third_party_sdk_upgrade_review.md`](android_third_party_sdk_upgrade_review.md) instead — those upgrades change privacy/consent behavior.

---

## Context Gathering

Before starting the audit, gather:

1. **Project Configuration:**
   - "Where are your dependencies declared? (libs.versions.toml, build.gradle.kts, buildSrc, or a mix?)"
   - "How many modules does your project have?"
   - "What is your minimum SDK version and target SDK version?"

2. **Build Environment:**
   - "What version of AGP (Android Gradle Plugin) are you using?"
   - "What Kotlin version are you on?"
   - "Are you using any Gradle plugins for dependency management (e.g., Dependabot, Renovate, versions plugin)?"

3. **History & Constraints:**
   - "When was the last dependency update pass?"
   - "Are any versions intentionally pinned? Why?"
   - "Have you experienced breakage from a dependency update before? Which library?"

4. **Risk Tolerance:**
   - "Is this a production app with users, or a pre-launch project?"
   - "Do you have CI with automated tests?"
   - "What is your test coverage situation (rough estimate is fine)?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before flagging ANY dependency as a risk, you MUST:**

1. **Check the actual vulnerability** — A CVE in a transitive dependency may not be reachable from your code path. Verify exploitability before raising alarms.
2. **Verify abandonment signals** — A library with no commits in 12 months might be "done" (stable, feature-complete) rather than abandoned. Check issue tracker activity, not just commit frequency.
3. **Confirm version compatibility** — Before recommending an update, verify it works with your Kotlin version, AGP version, and other dependencies.
4. **Assess real impact** — A library used in one utility function has different risk than one wired into your entire data layer.
5. **Check transitive conflicts** — Updating one library may force updates to others. Map the dependency graph before recommending changes.

**Finding all dependencies current and healthy is an acceptable outcome.** If your dependency stack is solid, this audit should confirm that with evidence.

### False-Positive Prevention

- ❌ Do NOT flag a library as "abandoned" just because it has no recent commits — stable libraries (like OkHttp, Moshi) may simply be mature
- ❌ Do NOT recommend replacing a working library just because a newer alternative exists
- ❌ Do NOT treat every CVE as critical — check CVSS score, exploitability, and whether your usage is affected
- ❌ Do NOT recommend major version jumps without migration guides and breaking change analysis
- ❌ Do NOT ignore version catalog consistency — partial updates create more problems than they solve
- ✅ DO distinguish between direct and transitive dependency vulnerabilities
- ✅ DO check if a CVE has already been patched in a newer minor version (not just major)
- ✅ DO assess libraries by how deeply they are integrated (surface area of usage)
- ✅ DO provide specific file paths and line numbers for every recommendation
- ✅ DO group related updates that must happen together (e.g., all Compose libraries)

---

### Phase 1: Dependency Inventory

Build a complete inventory of every dependency in the project.

#### 1.1 Extract All Dependencies

**Using Gradle dependency task:**

```bash
# List all dependencies for the app module
./gradlew app:dependencies --configuration releaseRuntimeClasspath > deps_report.txt

# If using version catalog, also examine the catalog directly
cat gradle/libs.versions.toml

# List all Gradle plugin dependencies
./gradlew buildEnvironment
```

**Using the Gradle Versions Plugin (recommended for ongoing use):**

```kotlin
// In root build.gradle.kts — add temporarily for audit
plugins {
    id("com.github.ben-manes.versions") version "0.51.0"
}

// Then run:
// ./gradlew dependencyUpdates -Drevision=release
```

#### 1.2 Dependency Inventory Table

Catalog every direct dependency into this format:

| # | Group:Artifact | Current | Latest Stable | Latest Any | Category | Source File | Line |
|---|---------------|---------|---------------|------------|----------|-------------|------|
| 1 | androidx.core:core-ktx | 1.12.0 | 1.15.0 | 1.15.0 | AndroidX | libs.versions.toml | 12 |
| 2 | com.squareup.retrofit2:retrofit | 2.9.0 | 2.11.0 | 2.11.0 | Network | libs.versions.toml | 28 |
| 3 | com.google.firebase:firebase-bom | 32.7.0 | 33.8.0 | 33.8.0 | Firebase | libs.versions.toml | 35 |
| 4 | io.coil-kt:coil-compose | 2.5.0 | 2.7.0 | 3.0.4 | Image | libs.versions.toml | 42 |

**Categories to use:** AndroidX, Compose, Firebase, Network, Database, DI, Image, Testing, Security, Serialization, Utility, Build Plugin, Other

#### 1.3 Version Gap Analysis

For each dependency, calculate the version gap:

```
Gap Classification:
  CURRENT    = on latest stable (no action needed)
  MINOR      = 1-2 minor versions behind (low risk update)
  MODERATE   = 3+ minor versions behind (medium risk, schedule soon)
  MAJOR      = major version behind (requires migration planning)
  CRITICAL   = known CVE or approaching end-of-support
  DEPRECATED = library is deprecated, replacement needed
```

---

### Phase 2: Security Vulnerability Scan

#### 2.1 CVE Database Check

For each dependency, check against known vulnerability databases:

**Automated scanning:**

```bash
# Using OWASP Dependency Check (Gradle plugin)
# Add to build.gradle.kts:
# plugins { id("org.owasp.dependencycheck") version "10.0.3" }
./gradlew dependencyCheckAnalyze

# Output location:
# build/reports/dependency-check-report.html
```

**Manual verification sources:**
- [NVD (National Vulnerability Database)](https://nvd.nist.gov/)
- [GitHub Security Advisories](https://github.com/advisories)
- [Google OSV](https://osv.dev/)
- [Snyk Vulnerability Database](https://security.snyk.io/)

#### 2.2 CVE Assessment Matrix

For each discovered vulnerability:

| CVE ID | Library | CVSS Score | Severity | Your Usage Affected? | Fix Available? | Priority |
|--------|---------|------------|----------|---------------------|----------------|----------|
| CVE-2024-XXXXX | okhttp 4.11.0 | 7.5 | High | Yes — used in API layer | Yes — 4.12.0 | P0 |
| CVE-2024-YYYYY | gson 2.10.1 | 4.3 | Medium | No — only used for logging | Yes — 2.11.0 | P2 |

**Priority classification:**
- **P0 (Immediate):** CVSS >= 7.0 AND your usage is in the affected code path AND fix available
- **P1 (This sprint):** CVSS >= 7.0 but usage may not be affected, OR CVSS 4.0-6.9 with affected usage
- **P2 (Next sprint):** CVSS < 4.0 OR usage not in affected path OR no fix yet available
- **P3 (Monitor):** CVE exists but does not apply to Android context or your usage

#### 2.3 Transitive Dependency Risks

```bash
# Find which of your direct dependencies pull in a vulnerable transitive dependency
./gradlew app:dependencyInsight --dependency com.example:vulnerable-lib --configuration releaseRuntimeClasspath
```

Document transitive chains:
```
Your dependency: com.squareup.retrofit2:retrofit:2.9.0
  └── pulls in: com.squareup.okhttp3:okhttp:3.14.9
      └── which has: CVE-2023-XXXXX (fixed in okhttp 4.x)

Resolution: Update retrofit to 2.11.0 (uses okhttp 4.12.0)
       OR: Force override okhttp version (riskier)
```

---

### Phase 3: Library Health Assessment

#### 3.1 Health Scoring Framework

For each dependency, assess health across these dimensions:

| Signal | Healthy (3) | Concerning (2) | Risky (1) | Critical (0) |
|--------|-------------|----------------|-----------|---------------|
| **Last release** | < 6 months ago | 6-12 months | 12-24 months | > 24 months |
| **Open issues** | Actively triaged | Growing backlog | Many stale issues | No responses |
| **Maintainer activity** | Multiple active | 1-2 active | Sporadic | No activity |
| **Stars/adoption** | > 5k or Google-backed | 1k-5k, growing | < 1k, flat | Declining |
| **Breaking changes** | Semver-compliant | Occasional breaks | Frequent breaks | Unpredictable |
| **Documentation** | Comprehensive | Adequate | Minimal | Outdated/none |
| **Android compatibility** | Explicitly supports | Generally works | Untested | Known issues |

**Health score interpretation:**
- **18-21:** Excellent — no action needed
- **14-17:** Good — monitor, no immediate concern
- **10-13:** Watch — plan contingency, evaluate alternatives
- **7-9:** Concerning — actively seek alternatives
- **0-6:** Critical — migrate away as soon as feasible

#### 3.2 Abandonment Risk Indicators

Check for these warning signs:

```
🔴 HIGH RISK:
  - Archived GitHub repository
  - Maintainer publicly announced end-of-life
  - No releases in 24+ months AND open security issues
  - Android-specific: doesn't support latest targetSdk

🟡 MEDIUM RISK:
  - Single maintainer with declining activity
  - No releases in 12-24 months (but no open CVEs)
  - Incomplete migration to Kotlin/Compose (for Android libs)
  - Repository transferred to unknown organization

🟢 LOW RISK:
  - Stable, "feature-complete" library (e.g., Moshi, Timber)
  - Backed by major company (Google, Square, JetBrains)
  - Active community fork exists
  - Part of official AndroidX ecosystem
```

#### 3.3 Alternative Identification

For any dependency scoring below 10, identify alternatives:

| Current Library | Score | Alternative | Migration Effort | Notes |
|----------------|-------|-------------|-----------------|-------|
| abandoned-image-lib | 4 | Coil 3.x | Medium (2-3 days) | Compose-native, active |
| custom-json-parser | 6 | Kotlinx Serialization | High (1 week) | Kotlin-native, no reflection |

---

### Phase 4: Prioritized Update Plan

#### 4.1 Update Priority Matrix

Combine security, health, and effort scores into a priority matrix:

```
                     LOW Effort          HIGH Effort
                 ┌─────────────────┬─────────────────┐
   HIGH Risk     │   DO FIRST      │   PLAN CAREFULLY │
   (CVE, dying)  │   Quick wins    │   Needs migration│
                 │   Sprint N      │   Sprint N+1     │
                 ├─────────────────┼─────────────────┤
   LOW Risk      │   BATCH UPDATE  │   DEFER          │
   (minor, okay) │   Maintenance   │   Revisit next   │
                 │   window        │   quarter        │
                 └─────────────────┴─────────────────┘
```

#### 4.2 Update Execution Plan

For each recommended update, provide:

```markdown
### Update #1: [library-name] v[current] → v[target]
- **Priority:** P0 / P1 / P2 / P3
- **Reason:** [CVE fix / major version currency / abandonment risk / feature need]
- **Breaking changes:** [None / List specific changes]
- **Files to modify:**
  - `gradle/libs.versions.toml` line XX: change version
  - `app/build.gradle.kts` line YY: update API usage (if breaking)
  - `app/src/.../SomeClass.kt` line ZZ: adapt to new API
- **Test plan:**
  - [ ] Build succeeds
  - [ ] Existing tests pass
  - [ ] Manual smoke test: [specific feature using this library]
- **Rollback:** Revert version in `libs.versions.toml`, no code changes needed
- **Estimated effort:** [30 min / 2 hours / 1 day / multi-day]
```

#### 4.3 Grouped Updates

Some updates must happen together. Group them:

```markdown
### Update Group: Compose BOM Update
All Compose libraries must update together via the BOM.

| Library | Current | Target |
|---------|---------|--------|
| compose-bom | 2024.02.00 | 2024.12.01 |
| compose-compiler | 1.5.8 | 1.5.14 |
| kotlin | 1.9.22 | 2.0.21 |

⚠️ Kotlin 2.0 requires Compose Compiler Gradle plugin migration.
See: https://developer.android.com/develop/ui/compose/compiler

Effort: 2-4 hours (mostly build config, limited code changes)
```

#### 4.4 Version Catalog Hygiene

If using `libs.versions.toml`:

```toml
# Check for these issues:

# 1. Unused entries (declared but not used in any build.gradle.kts)
# Run: grep -r "libs\." --include="*.kts" to find actual usage

# 2. Inconsistent version references
[versions]
compose-bom = "2024.12.01"      # ✅ Single source of truth
# composeMaterial = "1.7.0"     # ❌ Don't override BOM-managed versions

# 3. Missing bundle definitions for related libraries
[bundles]
compose = ["compose-ui", "compose-material3", "compose-ui-tooling-preview"]
testing = ["junit", "espresso-core", "compose-ui-test-junit4"]
```

---

### Phase 5: Ongoing Monitoring Setup

#### 5.1 Automated Dependency Monitoring

Set up ongoing monitoring so the next audit is easier:

**Option A: GitHub Dependabot (if using GitHub)**

```yaml
# .github/dependabot.yml
version: 2
updates:
  - package-ecosystem: "gradle"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 5
    labels:
      - "dependencies"
    ignore:
      # Don't auto-bump major versions
      - dependency-name: "*"
        update-types: ["version-update:semver-major"]
```

**Option B: Gradle Versions Plugin (for local checks)**

```kotlin
// root build.gradle.kts
plugins {
    id("com.github.ben-manes.versions") version "0.51.0"
}

// Run periodically: ./gradlew dependencyUpdates
```

#### 5.2 Quarterly Audit Reminder

```markdown
## Quarterly Dependency Audit Checklist
- [ ] Run `./gradlew dependencyUpdates` and review output
- [ ] Run `./gradlew dependencyCheckAnalyze` for CVE scan
- [ ] Check health of any library scoring < 14 in previous audit
- [ ] Review and merge any pending Dependabot PRs
- [ ] Update this audit document with new findings
- [ ] Verify Play Store targetSdk deadline compliance
```

---

## Expected Output

The audit should produce a report in this format:

```markdown
# Dependency Audit Report — [App Name]
**Date:** YYYY-MM-DD
**Auditor:** [Your name or "automated"]
**Previous audit:** YYYY-MM-DD (or "first audit")

## Executive Summary
- **Total dependencies:** XX direct, YY transitive
- **Up to date:** XX (XX%)
- **Minor updates available:** XX
- **Major updates available:** XX
- **Known CVEs:** XX (XX critical, XX medium, XX low)
- **Abandoned/at-risk libraries:** XX
- **Estimated total update effort:** X hours / X days

## Critical Items (P0 — act this week)
[List with CVE details and fix instructions]

## Scheduled Updates (P1 — this sprint)
[Prioritized list with grouped updates]

## Maintenance Updates (P2 — next sprint)
[Lower priority updates]

## Deferred (P3 — revisit next quarter)
[Items to monitor]

## Library Health Watchlist
[Libraries trending toward abandonment]

## Dependency Graph Changes
[Any new transitive dependencies introduced, any removed]

## Recommendations
[Structural recommendations: adopt version catalog, add Dependabot, etc.]
```

---

## Techniques Used

| Technique | How It's Applied |
|-----------|-----------------|
| **ST-01: Structured Taxonomy** | Dependencies categorized by type, risk level, and priority tier |
| **ST-02: Decision Matrices** | Multi-dimensional scoring (security, health, effort) drives prioritization |
| **RT-02: Verification Gates** | Each CVE and risk flag must be verified before reporting |
| **CM-01: Context Mapping** | Dependencies mapped to actual usage in codebase, not just version numbers |
| **DS-06: Output Templates** | Standardized audit report format for consistency across quarters |

---

## Related Prompts

- **[android_dependency_update.md](android_dependency_update.md)** — Companion prompt for actually executing dependency updates safely after this audit identifies what to update
- **[android_tech_debt_triage.md](android_tech_debt_triage.md)** — Dependencies are one category of tech debt; this audit feeds into the broader triage
- **[android_proguard_r8_optimization.md](android_proguard_r8_optimization.md)** — Dependency changes affect R8 shrinking rules; audit before R8 optimization
- **[../../analysis/security/security_vulnerability_analysis.md](../../../analysis/security/security_vulnerability_analysis.md)** — General security analysis that complements dependency-specific CVE checks
- **[../../devops/android_ci_cd_pipeline_design.md](../../../devops/android_ci_cd_pipeline_design.md)** — Integrate dependency checking into CI/CD pipeline

---

## Customization Guide

1. **Enterprise/Team variant:** Add columns for "approved alternatives list," "license compliance" (GPL/LGPL detection), and "internal library registry" checks. Replace Dependabot with enterprise tools like Snyk or Sonatype.

2. **Library author variant:** Flip the perspective — audit your library's own dependencies for downstream consumers. Add "minimum dependency principle" checks and API surface analysis.

3. **Compose-heavy app variant:** Add specific sections for Compose BOM alignment, compiler compatibility matrix, and Compose-specific performance libraries (Molecule, Circuit).

4. **Multi-module monorepo variant:** Add per-module dependency ownership, shared vs. module-specific dependency tracking, and version alignment enforcement across modules.

5. **Pre-launch security audit variant:** Increase severity of all findings by one tier, add Play Protect compatibility check, and include a "launch blocker" classification for any P0 or P1 items.
