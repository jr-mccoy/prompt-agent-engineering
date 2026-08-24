---
title: "iOS Dependency Audit"
category: mobile-development
description: "Audit third-party dependencies across SPM, CocoaPods, and Carthage for version currency, license compliance, security vulnerabilities, maintenance health, and binary size impact"
techniques:
  - ST-01
  - RT-02
difficulty: intermediate
tags:
  - ios
  - swift
  - dependencies
  - spm
  - cocoapods
updated: "2026-03-20"
---

# iOS Dependency Audit

**Objective:** Audit all third-party dependencies in an iOS project across package managers (Swift Package Manager, CocoaPods, Carthage) evaluating version currency, dependency graph complexity, license compliance, security vulnerabilities, maintenance status, and binary size impact to produce an actionable risk report.

**When to Use:** Use this prompt before major releases, during quarterly security reviews, when evaluating whether to adopt or replace a dependency, or when binary size has grown unexpectedly. Also useful when preparing for Swift version upgrades or Xcode major updates.

**Prompt Type:** Modular (200-350 lines)

---

## Context Gathering

Before beginning the audit, gather context:

1. **Package Manager Setup:**
   - "Which package managers are in use (SPM, CocoaPods, Carthage, or a mix)?"
   - "Are any dependencies vendored or checked into the repository directly?"

2. **Constraints:**
   - "What is the minimum deployment target (e.g., iOS 16)?"
   - "Are there corporate policies on approved licenses or banned libraries?"

3. **Known Concerns:**
   - "Are there specific dependencies you suspect are problematic?"
   - "Has binary size growth been flagged as an issue?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Verify actual usage** - Confirm the dependency is actively imported and used in source code, not just declared in the manifest.
2. **Check version context** - A dependency one minor version behind is not the same as one three majors behind. Be proportional.
3. **Confirm vulnerability applicability** - CVEs may apply only to specific features or platforms not used by this project.
4. **Provide specific evidence** - Every finding must reference the manifest file, lockfile entry, or import statement.

**A project with well-chosen, maintained dependencies at reasonable versions is healthy.** Don't flag every minor version bump as urgent.

### False-Positive Prevention

- ❌ Do NOT flag dependencies one patch version behind as "outdated"
- ❌ Do NOT flag MIT/Apache licenses as problematic without corporate policy requiring it
- ❌ Do NOT report CVEs that don't apply to the features actually used
- ❌ Do NOT flag test-only dependencies with the same severity as production dependencies
- ✅ DO distinguish between production and development/test dependencies
- ✅ DO verify that "abandoned" projects aren't simply feature-complete and stable
- ✅ DO check if a dependency is widely adopted (community backing reduces risk)
- ✅ DO consider whether direct source inclusion might be better than a dependency

---

### Phase 1: Dependency Graph Analysis

#### 1.1 Manifest Discovery

**Locate all dependency declarations:**

```
// Swift Package Manager
Package.swift                        // Root package definition
*.xcodeproj (SPM tab)              // Xcode-managed SPM dependencies
Package.resolved                     // Resolved versions lockfile

// CocoaPods
Podfile                             // Pod declarations
Podfile.lock                        // Locked versions
Pods/ directory                     // Installed pods

// Carthage
Cartfile                            // Dependency declarations
Cartfile.resolved                   // Locked versions
Carthage/Build/                     // Built frameworks

// Vendored / Manual
Vendor/ or ThirdParty/ directory    // Checked-in source code
*.xcframework bundles               // Pre-built frameworks
```

#### 1.2 Dependency Tree Mapping

**Build the complete dependency graph:**

```
App
├── DirectDependency-A (v2.1.0)
│   ├── TransitiveDep-X (v1.3.0)
│   └── TransitiveDep-Y (v4.0.0)
├── DirectDependency-B (v5.2.1)
│   └── TransitiveDep-Y (v4.0.0)  // Shared with A
└── DirectDependency-C (v1.0.0)
    └── TransitiveDep-Z (v2.0.0)
```

**Graph Metrics:**

| Metric | Value | Assessment |
|--------|-------|------------|
| Total direct dependencies | [N] | [Lean/Moderate/Heavy] |
| Total transitive dependencies | [N] | [Manageable/Concerning] |
| Maximum dependency depth | [N] | [Shallow/Deep] |
| Shared transitive deps | [N] | [Version conflicts?] |
| Multiple package managers | [Yes/No] | [Adds complexity?] |

#### 1.3 Usage Verification

**For each direct dependency, confirm active usage:**

```swift
// Check: Is it imported anywhere in source?
import Alamofire    // Used in NetworkService.swift, APIClient.swift
import SnapKit      // Used in 47 UIKit view files
import SwiftyJSON   // Only imported in 1 legacy file — candidate for removal
```

| Dependency | Import Count | Files Using | Actually Needed |
|-----------|-------------|-------------|-----------------|
| [Library] | [N] | [File list] | [Yes/No/Partial] |

---

### Phase 2: Version Currency Assessment

#### 2.1 Version Comparison

**Compare current versions against latest available:**

| Dependency | Current | Latest | Gap | Breaking Changes | Update Risk |
|-----------|---------|--------|-----|-----------------|-------------|
| [Library] | [Version] | [Version] | [Patches/Minors/Majors] | [Yes/No] | [Low/Medium/High] |

#### 2.2 Swift / Xcode Compatibility

**Check compatibility with current and upcoming toolchain:**

```
Current toolchain: Xcode [X.X] / Swift [X.X]
Upcoming toolchain: Xcode [X.X] / Swift [X.X]

// Check each dependency for:
- Swift version support in Package.swift or podspec
- Xcode version requirements
- Platform version requirements
- Swift 6 strict concurrency readiness
```

| Dependency | Swift Version | Xcode Compat | Swift 6 Ready | Platform Min |
|-----------|--------------|--------------|---------------|-------------|
| [Library] | [Version] | [Yes/No] | [Yes/No/Partial] | [iOS version] |

---

### Phase 3: Security Vulnerability Scan

#### 3.1 Known Vulnerability Check

**Check dependencies against vulnerability databases:**

```
// Sources to check:
- GitHub Security Advisories (GHSA)
- National Vulnerability Database (NVD/CVE)
- Swift Package Index security notices
- CocoaPods security advisories
- Dependency's own SECURITY.md or CHANGELOG
```

| Dependency | CVE/GHSA | Severity | Affected Versions | Fixed In | Applicable |
|-----------|----------|----------|-------------------|----------|------------|
| [Library] | [ID] | [Critical/High/Medium/Low] | [Range] | [Version] | [Yes/No — why] |

#### 3.2 Supply Chain Risk

**Assess supply chain risk factors:**

| Risk Factor | Status | Notes |
|------------|--------|-------|
| Unsigned packages | [Count] | [Details] |
| Dependencies from unknown publishers | [Count] | [Details] |
| Binary dependencies (opaque) | [Count] | [Details] |
| Dependencies with broad permissions | [Count] | [Details] |

---

### Phase 4: License Compliance

#### 4.1 License Identification

**Catalog licenses for all dependencies:**

```
// Common iOS dependency licenses:
MIT          - Permissive, minimal restrictions
Apache 2.0   - Permissive, patent grant
BSD 2/3      - Permissive
ISC          - Permissive
LGPL 2.1/3.0 - Weak copyleft (dynamic linking usually OK)
GPL 2.0/3.0  - Strong copyleft (RISK for App Store)
SSPL         - Non-OSI, problematic for most uses
Proprietary  - Check terms carefully
```

| Dependency | License | Copyleft Risk | Attribution Required | App Store OK |
|-----------|---------|--------------|---------------------|-------------|
| [Library] | [License] | [None/Low/High] | [Yes/No] | [Yes/No/Check] |

#### 4.2 License Compatibility Matrix

**Check for license conflicts:**

- GPL dependencies statically linked into a proprietary app violate GPL terms
- LGPL requires dynamic linking or object file distribution
- Some licenses require prominent attribution in the app's About/Legal screen
- App Store distribution terms may conflict with certain licenses

**Action Items:**

| Issue | Dependency | Required Action |
|-------|-----------|----------------|
| Missing attribution | [Library] | Add to Settings > Acknowledgements |
| GPL static linking | [Library] | Replace or switch to dynamic linking |
| License file missing | [Library] | Locate and add to project |

---

### Phase 5: Maintenance Health

#### 5.1 Maintenance Status Assessment

**Evaluate each dependency's health:**

| Dependency | Last Release | Last Commit | Open Issues | Open PRs | Maintainers | Status |
|-----------|-------------|-------------|-------------|----------|-------------|--------|
| [Library] | [Date] | [Date] | [N] | [N] | [N] | [Active/Slow/Stale/Abandoned] |

**Status Definitions:**
- **Active:** Release within 6 months, responsive to issues
- **Slow:** Release within 12 months, occasional responses
- **Stale:** No release in 12+ months, issues piling up
- **Abandoned:** No activity in 18+ months, no response to issues
- **Feature-Complete:** Stable, minimal changes needed (not the same as abandoned)

#### 5.2 Replacement Candidates

**For stale/abandoned dependencies, identify alternatives:**

| Current | Status | Recommended Replacement | Migration Effort |
|---------|--------|------------------------|-----------------|
| [Library] | [Stale] | [Alternative or native API] | [Hours/Days/Weeks] |

---

### Phase 6: Binary Size Impact

#### 6.1 Size Contribution Analysis

**Measure each dependency's contribution to app binary:**

```
// Methods to assess size impact:
// 1. Check .framework or .xcframework size in build output
// 2. Use Xcode's "Generate App Size Report"
// 3. Compare IPA size with/without dependency

// Size categories:
// Minimal:  < 100 KB
// Small:    100 KB - 500 KB
// Medium:   500 KB - 2 MB
// Large:    2 MB - 10 MB
// Heavy:    > 10 MB
```

| Dependency | Estimated Size | Category | Justified |
|-----------|---------------|----------|-----------|
| [Library] | [Size] | [Category] | [Yes — essential / No — could replace] |

#### 6.2 Size Optimization Opportunities

**Identify size reduction opportunities:**

- Dependencies used for only one or two functions (consider extracting just what's needed)
- Large image/asset bundles included in dependencies
- Debug symbols included in release builds
- Unused architectures in fat frameworks

---

## Expected Output

1. **Dependency Graph** - Complete map of direct and transitive dependencies
2. **Version Currency Report** - Current vs. latest with update risk assessment
3. **Security Report** - Known vulnerabilities with applicability analysis
4. **License Compliance Matrix** - All licenses identified with action items
5. **Maintenance Health Dashboard** - Status of each dependency's project health
6. **Binary Size Impact** - Size contribution per dependency

---

## Example Interaction

**User:** Audit the dependencies in our iOS app. We use SPM mostly but have a few CocoaPods left over.

**Agent:** I'll audit all dependencies across both package managers. Let me scan the manifests.

*[Agent scans Package.swift, Package.resolved, Podfile, Podfile.lock]*

**Agent:**

## Dependency Audit Summary

**Total Dependencies:** 23 direct (18 SPM, 5 CocoaPods), 41 transitive

### Critical Findings

| Finding | Dependency | Action |
|---------|-----------|--------|
| Known CVE (High) | `lottie-ios 3.4.x` — CVE-2024-XXXX DoS via malformed animation | Update to 4.4.0+ |
| Abandoned | `SwiftyJSON` — last release 2022, Swift 6 incompatible | Replace with native Codable |
| GPL License | `Charts` — GPL 3.0 static linking | Replace with DGCharts (Apache 2.0 fork) or use Swift Charts |
| Unused | `PromiseKit` — imported in 0 files | Remove from Podfile |

### Health Overview

| Status | Count |
|--------|-------|
| Active | 16 |
| Slow | 4 |
| Stale | 2 |
| Abandoned | 1 |

**Shall I proceed with detailed findings and replacement recommendations?**

---

## Techniques Used

- **ST-01** (Clear Objective): Focused multi-dimensional dependency audit
- **RT-02** (Multi-Dimensional Analysis): Six evaluation dimensions (version, security, license, maintenance, size, usage)

---

## Related Prompts

- [ios_technical_debt_assessment.md](ios_technical_debt_assessment.md) - Broader debt catalog including dependencies
- [ios_codebase_health_assessment.md](ios_codebase_health_assessment.md) - Overall codebase evaluation
- [ios_open_source_license_audit.md](ios_open_source_license_audit.md) - Deep license compliance analysis

---

## Customization Guide

### For Enterprise / Regulated Apps
- Add corporate approved-dependency whitelist check
- Verify all dependencies have matching entries in SBOM (Software Bill of Materials)
- Check for FIPS 140-2 compliance requirements on cryptographic libraries
- Verify no dependencies phone home or collect analytics

### For App Size Optimization
- Prioritize binary size analysis phase
- Check for tree-shaking opportunities with SPM
- Evaluate whether large dependencies can be replaced with lighter alternatives or native APIs
- Consider on-demand resources for heavy asset bundles

### For Swift 6 Migration
- Weight Swift 6 / strict concurrency readiness heavily
- Identify blocking dependencies that prevent Swift 6 adoption
- Check for `@preconcurrency import` needs
- Evaluate if forking stale dependencies is worthwhile for concurrency fixes
