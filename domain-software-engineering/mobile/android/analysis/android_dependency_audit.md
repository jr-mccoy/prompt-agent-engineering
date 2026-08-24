---
title: "Android Dependency Audit"
category: mobile-development
description: "Audits project dependencies for version freshness, security vulnerabilities, and provides safe update recommendations"
techniques:
  - ST-01
  - ST-02
  - RT-05
  - DS-06
difficulty: intermediate
tags:
  - android
  - mobile-development
updated: "2026-03-19"
related_prompts:
  - domain-software-engineering/mobile/android/analysis/android_open_source_license_audit.md
  - domain-software-engineering/mobile/android/analysis/android_build_gradle_health_analysis.md
  - domain-software-engineering/mobile/android/maintenance/android_dependency_update.md
---


# Android Dependency Audit

**Objective:** Audit all project dependencies for version freshness, security vulnerabilities, optimization opportunities, and provide safe update recommendations.

**When to Use:** Use this prompt before major releases to ensure dependencies are current and secure, during quarterly maintenance windows, when planning dependency update sprints, or when security advisories affect Android libraries. Best used as a focused follow-up to a codebase health assessment.

**Prompt Type:** Modular (100-150 lines)

> **Scope — quick audit.** This is the fast, read-only freshness/CVE pass. For a deeper CVE + abandonment-risk audit with a prioritized multi-sprint paydown plan, use [`../maintenance/android_dependency_audit.md`](../maintenance/android_dependency_audit.md). To *apply* a specific set of updates safely, use [`../maintenance/android_dependency_update.md`](../maintenance/android_dependency_update.md).

---

## Context Gathering

1. **Update Appetite:**
   - "Are you looking for safe incremental updates or willing to tackle major version upgrades?"
   - "Are there dependencies that must stay at specific versions due to compatibility?"

2. **Risk Tolerance:**
   - "How robust is your test coverage for catching regressions?"
   - "Is there a staging/beta testing phase before production?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Trace actual usage** - Don't flag based on version numbers alone. Verify that the suspected issue actually affects the application.
2. **Check for existing mitigations** - Search for patches, ProGuard rules, or workarounds that may already address vulnerabilities.
3. **Understand the context** - Consider WHY specific versions are used. Compatibility constraints and testing requirements are valid factors.
4. **Confirm actual impact** - Is the vulnerability reachable in the app's usage pattern? Is the "outdated" library stable and working?
5. **Provide specific locations** - Every finding MUST include exact dependency coordinates (e.g., `androidx.room:room-runtime:2.5.0` in `libs.versions.toml`).

**Finding NO critical issues is an acceptable outcome.** If dependencies are reasonably current and secure, say so with confidence. Don't manufacture urgency.

### False-Positive Prevention

- ❌ Do NOT flag all outdated libraries as critical (stability matters)
- ❌ Do NOT flag CVEs without checking if they're reachable in the app
- ❌ Do NOT assume update safety without checking breaking changes
- ❌ Do NOT report version differences as issues without actual impact
- ✅ DO differentiate between security updates and feature updates
- ✅ DO check if CVEs apply to the specific usage pattern
- ✅ DO consider test coverage when assessing update risk
- ✅ DO understand that "latest" isn't always "best"

---

### Phase 1: Dependency Inventory

#### 1.1 Extract All Dependencies

**Analyze build files:**

```kotlin
// Check these files:
- build.gradle.kts / build.gradle (root and module level)
- gradle/libs.versions.toml (version catalog)
- buildSrc (if convention plugins exist)

// Categorize dependencies:
- Core Android (AndroidX, Jetpack)
- Kotlin (stdlib, coroutines, serialization)
- Networking (Retrofit, OkHttp, Ktor)
- Database (Room, SQLDelight)
- DI (Hilt, Dagger, Koin)
- UI (Compose, Material, Glide/Coil)
- Testing (JUnit, MockK, Espresso)
- Third-party services (Firebase, Analytics)
```

#### 1.2 Version Analysis

**Check current vs latest versions:**

| Category | Library | Current | Latest Stable | Versions Behind |
|----------|---------|---------|---------------|-----------------|
| Core | Kotlin | | | |
| Core | AGP | | | |
| Jetpack | Core-ktx | | | |
| Jetpack | Lifecycle | | | |
| Compose | BOM | | | |

#### 1.3 Security Scan

**Check for known vulnerabilities:**

```kotlin
// Look for:
- CVEs in current versions
- Security advisories from Google
- Deprecated libraries with security implications
- Transitive dependencies with vulnerabilities
```

---

### Phase 2: Dependency Analysis Report

```markdown
## Dependency Audit Report

### Summary

| Metric | Count |
|--------|-------|
| Total Dependencies | [X] |
| Up to Date | [X] |
| Minor Updates Available | [X] |
| Major Updates Available | [X] |
| Security Issues | [X] |
| Deprecated | [X] |

### Update Recommendations

#### Safe Updates (Patch/Minor - Low Risk)
*Can update immediately with basic testing*

| Library | Current | Update To | Changes |
|---------|---------|-----------|---------|
| [lib] | X.X.X | X.X.Y | Bug fixes |

#### Moderate Updates (Minor - Medium Risk)
*Update with thorough testing*

| Library | Current | Update To | Breaking Changes |
|---------|---------|-----------|------------------|
| [lib] | X.X.X | X.Y.0 | [Changes] |

#### Major Updates (Requires Migration)
*Plan dedicated migration effort*

| Library | Current | Update To | Migration Guide |
|---------|---------|-----------|-----------------|
| [lib] | X.X.X | Y.0.0 | [Link/Notes] |

### Security Issues

| Library | Version | CVE/Issue | Severity | Fixed In |
|---------|---------|-----------|----------|----------|
| [lib] | X.X.X | [CVE-XXXX] | [Critical/High/Med] | X.X.Y |

### Deprecated Libraries

| Library | Status | Replacement | Migration Effort |
|---------|--------|-------------|------------------|
| [lib] | Deprecated | [alternative] | [Low/Med/High] |

### Optimization Opportunities

| Issue | Libraries | Recommendation | Savings |
|-------|-----------|----------------|---------|
| Duplicate functionality | [libs] | Consolidate | [KB] |
| Unused dependency | [lib] | Remove | [KB] |

### Compatibility Matrix

| Library | Min Kotlin | Min AGP | Min SDK |
|---------|------------|---------|---------|
| [lib latest] | X.X | X.X | XX |

### Recommended Update Order

1. **First:** Security fixes and patch updates
2. **Second:** Minor version updates (test thoroughly)
3. **Third:** Major version migrations (plan sprints)
```

---

## Expected Output

1. **Dependency Inventory** - All dependencies with current versions
2. **Version Gap Analysis** - How far behind each dependency is
3. **Security Report** - Known vulnerabilities
4. **Update Recommendations** - Prioritized by safety and importance
5. **Compatibility Information** - Version requirements for updates

---

## Techniques Used

- **ST-01** (Clear Objective): Focused dependency analysis
- **RT-04** (Best Practice Review): Latest version recommendations
- **ST-03** (Output Format Templates): Structured tables
- **OC-05** (Severity Classification): Risk-based prioritization
- **DS-06** (Prioritization Guidance): Update order recommendations

---

## Related Prompts

- [android_codebase_health_assessment.md](android_codebase_health_assessment.md) - Overall health check
- [android_technical_debt_assessment.md](android_technical_debt_assessment.md) - Includes dependency debt
- [android_code_modernization.md](../improvement/android_code_modernization.md) - Modernization including deps

---

## Customization Guide

### For Security-Focused Audit
- Prioritize CVE checking
- Include transitive dependency analysis
- Add OWASP dependency check results

### For Size Optimization
- Focus on large dependencies
- Identify unused dependencies
- Suggest lighter alternatives

### For Compose Migration
- Focus on Compose-related dependencies
- Check Compose compiler/Kotlin compatibility
- Identify blocking dependencies
