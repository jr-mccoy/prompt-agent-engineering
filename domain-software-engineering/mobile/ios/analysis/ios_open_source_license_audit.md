---
title: "iOS Open Source License Audit"
category: mobile-development
description: "Audit open source license compliance across all iOS dependencies covering license identification, compatibility analysis, attribution requirements, copyleft risk, and App Store compliance"
techniques:
  - ST-01
  - RT-02
difficulty: intermediate
tags:
  - ios
  - swift
  - licensing
  - compliance
  - open-source
updated: "2026-03-20"
---

# iOS Open Source License Audit

**Objective:** Audit all open source dependencies in an iOS project for license compliance, covering license identification for every dependency (direct and transitive), compatibility between licenses, attribution requirements, copyleft risk assessment, and Apple App Store distribution compatibility to produce a compliance report with required actions.

**When to Use:** Use this prompt before App Store submission, during legal reviews, when adding new dependencies, when an enterprise customer requests a Software Bill of Materials (SBOM), or when preparing for acquisition due diligence.

**Prompt Type:** Modular (200-350 lines)

---

## Context Gathering

Before beginning the audit, gather context:

1. **Distribution Model:**
   - "Is this app distributed via the App Store, enterprise distribution, or open source?"
   - "Is the app itself open source? If so, under what license?"

2. **Corporate Policy:**
   - "Are there corporate-approved or banned licenses?"
   - "Does your legal team have existing guidance on open source usage?"

3. **Current State:**
   - "Has a license audit been done before?"
   - "Is there an existing acknowledgements/attribution screen in the app?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Verify the actual license** - Check the LICENSE file in the dependency source, not assumptions based on the repository host or language.
2. **Check all transitive dependencies** - A permissively-licensed library may pull in a copyleft transitive dependency.
3. **Understand the linking model** - Static linking and dynamic linking have different implications for copyleft licenses.
4. **Confirm App Store relevance** - Some license concerns apply only to source distribution, not binary distribution.
5. **Reference specific files** - Every finding must reference the dependency name, version, and license file location.

**Most popular iOS libraries use permissive licenses (MIT, Apache, BSD).** An audit finding zero issues is a normal, positive outcome. Don't create problems where none exist.

### False-Positive Prevention

- ❌ Do NOT flag MIT, Apache 2.0, or BSD licenses as problematic without specific reason
- ❌ Do NOT assume a library without a LICENSE file is unlicensed (check podspec, Package.swift, README)
- ❌ Do NOT flag LGPL as incompatible without checking the linking model
- ❌ Do NOT flag test-only dependencies as production license risks
- ✅ DO check transitive dependencies, not just direct ones
- ✅ DO verify the license text matches the claimed license type
- ✅ DO distinguish between production and development dependencies
- ✅ DO check for dual-licensing options that may resolve conflicts

---

### Phase 1: License Identification

#### 1.1 Dependency License Catalog

**For each dependency, identify the license:**

```
// License identification sources (check in order):
1. LICENSE or LICENSE.md file in repository root
2. COPYING file
3. Package.swift license field
4. .podspec license field
5. README.md license section
6. Repository "About" section (GitHub/GitLab)
7. Source file header comments
```

**Complete License Inventory:**

| Dependency | Version | License | License File Found | Production/Dev | Transitive Of |
|-----------|---------|---------|-------------------|---------------|---------------|
| [Library] | [Version] | [License] | [Yes — path / No] | [Prod/Dev/Test] | [Direct / Parent] |

#### 1.2 License Classification

**Classify each license by category:**

```
PERMISSIVE (Low Risk):
├── MIT License                    — Attribution required, no copyleft
├── Apache License 2.0             — Attribution + patent grant, no copyleft
├── BSD 2-Clause (Simplified)      — Attribution required
├── BSD 3-Clause (New)             — Attribution + no-endorsement clause
├── ISC License                    — Functionally equivalent to MIT
├── zlib License                   — Attribution in source only
├── Boost Software License 1.0     — Very permissive
└── The Unlicense / CC0            — Public domain dedication

WEAK COPYLEFT (Medium Risk):
├── LGPL 2.1                       — Dynamic linking usually OK
├── LGPL 3.0                       — Dynamic linking OK, must allow re-linking
├── MPL 2.0 (Mozilla)              — File-level copyleft only
└── EPL 2.0 (Eclipse)              — Module-level copyleft

STRONG COPYLEFT (High Risk for App Store):
├── GPL 2.0                        — Entire binary must be GPL
├── GPL 3.0                        — GPL + anti-tivoization
├── AGPL 3.0                       — Network use triggers copyleft
└── SSPL                           — Server-side copyleft (not OSI-approved)

PROPRIETARY / CUSTOM:
├── Commercial license              — Check terms individually
├── Custom license                  — Legal review required
├── No license found                — All rights reserved by default — HIGH RISK
└── Dual license                    — Choose the permissive option if available
```

**License Distribution Summary:**

| Category | Count | Dependencies |
|----------|-------|-------------|
| Permissive | [N] | [List] |
| Weak Copyleft | [N] | [List] |
| Strong Copyleft | [N] | [List] |
| Proprietary | [N] | [List] |
| Unknown/Missing | [N] | [List] |

---

### Phase 2: Compatibility Analysis

#### 2.1 License Compatibility Matrix

**Check that all dependency licenses are compatible with each other and with the app's distribution model:**

```
App Store Binary Distribution Compatibility:

MIT          ✅ Compatible — include attribution
Apache 2.0   ✅ Compatible — include attribution + NOTICE file
BSD 2/3      ✅ Compatible — include attribution
ISC          ✅ Compatible — include attribution
zlib         ✅ Compatible — attribution in source only
LGPL 2.1     ⚠️ Conditionally — must use dynamic linking (framework)
LGPL 3.0     ⚠️ Conditionally — must allow user re-linking
MPL 2.0      ⚠️ Conditionally — modified MPL files must be shared
GPL 2.0      ❌ Incompatible with App Store (DRM/code signing clause conflict)
GPL 3.0      ❌ Incompatible with App Store (anti-tivoization + DRM)
AGPL 3.0     ❌ Incompatible with App Store
No License   ❌ Cannot use — all rights reserved by copyright holder
```

#### 2.2 Inter-License Compatibility

**Check for conflicts between dependency licenses:**

```
// Common compatibility issues:

// Apache 2.0 + GPL 2.0 only = INCOMPATIBLE
// Apache 2.0 has patent retaliation clause that GPL 2.0 doesn't allow
// Apache 2.0 + GPL 3.0 = Compatible (GPL 3.0 accommodates Apache)

// MIT + anything = Compatible (MIT imposes minimal requirements)

// LGPL + static linking in iOS:
// iOS apps typically use static linking (SPM default, CocoaPods default)
// LGPL requires dynamic linking OR providing object files for re-linking
// If using LGPL with static linking: must provide object files or switch to dynamic
```

| License Pair | Compatible | Notes |
|-------------|-----------|-------|
| [License A] + [License B] | [Yes/No/Conditional] | [Details] |

---

### Phase 3: Attribution Requirements

#### 3.1 Required Attributions

**Catalog what each license requires in the distributed app:**

```swift
// Attribution requirements by license:

// MIT: Include copyright notice + license text
// "Copyright (c) 2024 Author Name"
// + full MIT license text

// Apache 2.0: Include copyright + license + NOTICE file (if exists)
// Must reproduce NOTICE file contents
// Must state changes if modified

// BSD 3-Clause: Include copyright + license
// Must NOT use contributor names for endorsement

// LGPL: Include copyright + license + link to source
// Must allow re-linking (provide object files or use dynamic linking)
```

**Attribution Checklist:**

| Dependency | License | Attribution Needed | NOTICE File | Currently Attributed | Action |
|-----------|---------|-------------------|-------------|---------------------|--------|
| [Library] | [License] | [Yes/No] | [Yes/No] | [Yes/No] | [Add/Update/OK] |

#### 3.2 Attribution Implementation

**Check current attribution implementation:**

```swift
// Common iOS attribution patterns:

// 1. Settings.bundle → Acknowledgements
// Settings.bundle/Acknowledgements.plist
// Auto-generated by CocoaPods (Pods-acknowledgements.plist)

// 2. In-app Licenses screen
// Settings → Open Source Licenses → List of libraries + license text

// 3. Generated by tools
// - CocoaPods: auto-generates acknowledgements plist
// - LicensePlist: SPM + CocoaPods + manual license aggregation
// - swift-package-licenses: SPM license extraction
// - AcknowList: SwiftUI/UIKit license display

// CHECK: Are ALL dependencies covered?
// SPM dependencies often missing from CocoaPods-only acknowledgements
// Vendored / manually included code often missing entirely
```

| Attribution Method | Covers SPM | Covers Pods | Covers Vendored | Complete |
|-------------------|-----------|-------------|----------------|----------|
| [Method] | [Yes/No] | [Yes/No] | [Yes/No] | [Yes/No] |

---

### Phase 4: Copyleft Risk Assessment

#### 4.1 LGPL Dependencies

**For each LGPL dependency, assess linking model:**

```swift
// LGPL compliance options for iOS:

// Option 1: Dynamic Framework (preferred)
// Build LGPL library as .framework or .xcframework
// User can theoretically swap the framework to re-link
// SPM: Use .dynamic library product type
// CocoaPods: use_frameworks! (dynamic)

// Option 2: Provide Object Files
// Distribute .o files so users can re-link
// Impractical for App Store distribution

// Option 3: Replace the Dependency
// Find an MIT/Apache alternative
// Or implement the functionality directly

// CHECK: How is the LGPL library linked?
// SPM default = static linking (LGPL non-compliant)
// CocoaPods with use_frameworks! = dynamic linking (compliant)
// Carthage = dynamic frameworks (compliant)
```

| LGPL Dependency | Linking | Compliant | Action |
|----------------|---------|-----------|--------|
| [Library] | [Static/Dynamic] | [Yes/No] | [Switch to dynamic / Replace / OK] |

#### 4.2 GPL Dependencies

**For each GPL dependency, assess risk:**

```
// GPL in an iOS app is almost always incompatible because:
// 1. App Store DRM (FairPlay) conflicts with GPL freedom requirements
// 2. Apple's terms restrict redistribution (conflicts with GPL)
// 3. Code signing prevents user modification (conflicts with GPL 3.0)

// Options:
// 1. Remove the GPL dependency
// 2. Find a permissively-licensed alternative
// 3. Contact the author for a commercial/alternative license
// 4. If the author offers dual licensing, use the permissive option
// 5. If your app is also GPL — still App Store incompatible
```

| GPL Dependency | Version | Alternative Available | Dual License | Action |
|---------------|---------|----------------------|-------------|--------|
| [Library] | [Version] | [Yes — name / No] | [Yes — license / No] | [Replace/Relicense/Remove] |

---

### Phase 5: App Store Compliance

#### 5.1 App Store Distribution Check

**Verify all licenses are compatible with App Store distribution:**

```
// Apple App Store requirements that interact with licensing:
// 1. FairPlay DRM applied to all App Store apps
// 2. Users cannot modify or redistribute the binary
// 3. Code signing prevents binary modification
// 4. Apple's developer agreement governs distribution terms

// These conflict with:
// - GPL (requires freedom to modify and redistribute)
// - AGPL (requires source disclosure for network use)
// - Some custom licenses with anti-DRM clauses
```

#### 5.2 SBOM (Software Bill of Materials)

**Generate a compliance-ready dependency list:**

```markdown
## Software Bill of Materials

| Component | Version | License | Copyright | Source URL |
|-----------|---------|---------|-----------|-----------|
| [Library] | [Version] | [SPDX ID] | [Copyright holder] | [URL] |

Generated: [Date]
App Version: [Version]
```

---

## Expected Output

1. **License Inventory** - Complete catalog of all dependency licenses
2. **Compatibility Analysis** - Inter-license and App Store compatibility assessment
3. **Attribution Report** - Required attributions with implementation status
4. **Copyleft Risk Assessment** - LGPL/GPL dependencies with compliance options
5. **Compliance Action Items** - Prioritized list of required actions

---

## Example Interaction

**User:** We're preparing for our first App Store submission. Can you audit our open source licenses?

**Agent:** I'll audit all dependency licenses for App Store compliance. Let me scan your package manifests.

*[Agent scans Package.swift, Podfile, and vendored code]*

**Agent:**

## License Audit Summary

**Total Dependencies:** 31 (24 SPM, 5 CocoaPods, 2 vendored)

### License Distribution

| Category | Count | Action Needed |
|----------|-------|--------------|
| MIT | 22 | Attribution only |
| Apache 2.0 | 5 | Attribution + check NOTICE files |
| BSD 3-Clause | 1 | Attribution only |
| LGPL 3.0 | 1 | Linking model review |
| GPL 2.0 | 1 | **Must replace** |
| No license found | 1 | **Must resolve** |

### Blocking Issues for App Store

1. **`libxml2-swift` — GPL 2.0** — Incompatible with App Store distribution
   - **Alternative:** Use Foundation's `XMLParser` (built-in) or `SWXMLHash` (MIT)
   - **Action:** Replace before submission

2. **`CustomLogger` (vendored) — No license file**
   - Copied from a GitHub repo that has no LICENSE file
   - **Action:** Contact author for license clarification or replace with `swift-log` (Apache 2.0)

### Required Actions Before Submission

3. **`ffmpeg-kit` — LGPL 3.0, statically linked via SPM**
   - Must switch to dynamic framework linking or replace
   - **Action:** Build as .xcframework with dynamic linking

4. **Missing attributions** — 14 of 28 permissive libraries not in acknowledgements
   - **Action:** Add LicensePlist or equivalent to generate complete attribution screen

**Shall I provide the specific attribution text for each library?**

---

## Techniques Used

- **ST-01** (Clear Objective): Focused license compliance audit
- **RT-02** (Multi-Dimensional Analysis): License type, compatibility, attribution, copyleft, and App Store dimensions

---

## Related Prompts

- [ios_dependency_audit.md](ios_dependency_audit.md) - Broader dependency health audit including licenses
- [ios_technical_debt_assessment.md](ios_technical_debt_assessment.md) - Debt assessment including dependency risks
- [ios_codebase_health_assessment.md](ios_codebase_health_assessment.md) - Overall codebase evaluation

---

## Customization Guide

### For Enterprise Distribution
- Enterprise distribution has fewer DRM conflicts than App Store
- Still check attribution requirements (legal obligation remains)
- Corporate policy may ban certain licenses regardless of technical compatibility
- Check if enterprise agreement allows GPL usage (unlikely but possible)

### For Open Source iOS Apps
- If your app is MIT/Apache: check all dependencies are compatible
- If your app is GPL: still App Store incompatible, but GitHub/TestFlight OK
- Document contribution license agreement (CLA) if accepting external contributions
- Include SPDX license identifiers in all source files

### For Acquisition Due Diligence
- Generate complete SBOM with version pinning
- Document all license obligations and current compliance status
- Identify any dependencies with contributor license agreements
- Flag any dependencies from sanctioned entities or jurisdictions
- Check for patent grant implications (Apache 2.0 section 3)

### For Healthcare / Government Apps
- Check for FIPS 140-2 implications on cryptographic libraries
- Verify no dependencies phone home (some analytics SDKs have restrictive terms)
- Check export control classification for cryptographic libraries
- Verify supply chain integrity (signed packages, verified publishers)
