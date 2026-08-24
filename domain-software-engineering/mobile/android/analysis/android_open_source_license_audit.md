---
title: "Open Source License Audit"
category: mobile-development
description: "Audit open source license compliance for an Android app — inventory all dependencies and their licenses, identify copyleft obligations, check license compatibility, and generate attribution notices"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: intermediate
tags:
  - android
  - open-source
  - licensing
  - compliance
  - legal
  - mobile-development
updated: "2026-02-12"
related_prompts:
  - domain-software-engineering/mobile/android/analysis/android_dependency_audit.md
  - domain-software-engineering/mobile/android/publishing/android_privacy_compliance.md
  - domain-software-engineering/mobile/android/publishing/play_store_policy_compliance_check.md
---


# Open Source License Audit

**Objective:** Conduct a comprehensive open source license compliance audit of an Android application — inventorying all direct and transitive dependencies with their licenses, identifying copyleft obligations (GPL, LGPL, MPL), checking license compatibility between dependencies, generating attribution notices required by permissive licenses (Apache 2.0, MIT, BSD), and producing a compliance report with remediation steps for any issues found.

**When to Use:** Use this prompt before launching an app, before a major release, when adding a significant new dependency, when your app is acquired or receives investment (legal due diligence), when you receive a license compliance inquiry, or during quarterly maintenance reviews.

**Important context:** Every open source library your app uses comes with license obligations. Most Android dependencies use permissive licenses (Apache 2.0, MIT) that require attribution but not source code sharing. However, some libraries use copyleft licenses (GPL, LGPL) that may require you to share your source code. Ignoring license obligations exposes you to legal claims. For solo developers, the most common issue is missing attribution notices — which is easy to fix.

---

## Context Gathering

1. **Project Setup:**
   - "How many modules does your project have?"
   - "Do you use any native libraries (NDK, C/C++)?"
   - "Do you bundle any third-party assets (fonts, icons, images)?"
   - "Is your app open source or proprietary?"

---

## Instructions

### Step 1: Generate Dependency Inventory

```bash
# Generate full dependency tree (direct + transitive)
./gradlew app:dependencies --configuration releaseRuntimeClasspath > dependency_tree.txt

# Count unique dependencies
./gradlew app:dependencies --configuration releaseRuntimeClasspath | grep "--- " | sort -u | wc -l

# If using a license plugin, generate license report
# com.jaredsburrows.license plugin:
./gradlew licenseReleaseReport
# Output: app/build/reports/licenses/licenseReleaseReport.json
```

### Step 2: Classify Licenses

For each dependency, classify the license type:

| License | Type | Obligations | Risk Level |
|---------|------|------------|------------|
| **Apache 2.0** | Permissive | Attribution, include license text, state changes | LOW |
| **MIT** | Permissive | Attribution, include license text | LOW |
| **BSD 2-Clause** | Permissive | Attribution | LOW |
| **BSD 3-Clause** | Permissive | Attribution, no endorsement | LOW |
| **ISC** | Permissive | Attribution | LOW |
| **MPL 2.0** | Weak Copyleft | Modified files must be MPL, but can combine with proprietary | MEDIUM |
| **LGPL 2.1/3.0** | Weak Copyleft | Must allow relinking, provide LGPL source, attribution | MEDIUM |
| **GPL 2.0/3.0** | Strong Copyleft | Entire work must be GPL — may require open-sourcing your app | **HIGH** |
| **AGPL 3.0** | Network Copyleft | Like GPL + network use triggers obligations | **CRITICAL** |
| **No License / Proprietary** | Varies | Cannot use without explicit permission | **HIGH** |
| **Creative Commons (for code)** | Varies | CC licenses are not recommended for code | MEDIUM |

### Step 3: Compatibility Check

Verify all dependency licenses are compatible with each other and with your app's license:

**Common Android dependency licenses:**
- AndroidX: Apache 2.0 ✅
- Kotlin stdlib: Apache 2.0 ✅
- Jetpack Compose: Apache 2.0 ✅
- Firebase SDKs: Apache 2.0 ✅ (SDK), Google Terms (service)
- OkHttp / Retrofit: Apache 2.0 ✅
- Ktor: Apache 2.0 ✅
- Coil: Apache 2.0 ✅
- Moshi: Apache 2.0 ✅
- Room / SQLDelight: Apache 2.0 ✅
- Hilt / Dagger: Apache 2.0 ✅
- Material Components: Apache 2.0 ✅

**Red flags to check for:**
- Any GPL-licensed library (incompatible with proprietary apps unless using a GPL exception)
- Libraries with "no license" (cannot legally use — contact the maintainer)
- Libraries with AGPL (even server-side use requires source disclosure)
- Conflicting copyleft licenses (GPL 2.0-only vs GPL 3.0-only)
- Dependencies pulling in copyleft-licensed transitive dependencies

### Step 4: Generate Attribution Notices

Most Android licenses require attribution. Create an in-app "Open Source Licenses" screen:

```kotlin
// Using the OSS Licenses Plugin (Google)
// In app/build.gradle.kts:
plugins {
    id("com.google.android.gms.oss-licenses-plugin")
}

// In your settings screen:
@Composable
fun SettingsScreen() {
    TextButton(onClick = {
        val intent = Intent(context, OssLicensesMenuActivity::class.java)
        context.startActivity(intent)
    }) {
        Text("Open Source Licenses")
    }
}
```

**Manual attribution template (if not using plugin):**

```markdown
## Open Source Libraries

### Library Name
- **License:** Apache License 2.0
- **Copyright:** Copyright 2024 The Library Authors
- **URL:** https://github.com/org/library

[Full license text]

---

### [Next library...]
```

### Step 5: Non-Code Assets Audit

Check licenses for non-code assets:

| Asset Type | Common Licenses | Check |
|-----------|----------------|-------|
| **Fonts** | SIL Open Font License, Apache 2.0, Proprietary | Verify each font's license allows app embedding |
| **Icons** | Apache 2.0 (Material), Various (third-party) | Check icon pack license |
| **Images/Illustrations** | Various (Unsplash, CC, Proprietary) | Verify commercial use is permitted |
| **Sound effects** | Various | Verify distribution rights |
| **Animations (Lottie)** | Check per animation | Some Lottie files have restricted licenses |

### Step 6: Produce Compliance Report

```markdown
# Open Source License Compliance Report
**App:** [App Name]
**Date:** [Date]
**Total Dependencies:** [Count]

## License Distribution
- Apache 2.0: [Count] (XX%)
- MIT: [Count] (XX%)
- BSD: [Count] (XX%)
- Other Permissive: [Count] (XX%)
- Weak Copyleft (LGPL/MPL): [Count] (XX%)
- Strong Copyleft (GPL): [Count] (XX%)
- No License: [Count] (XX%)

## Issues Found
| # | Issue | Severity | Library | License | Remediation |
|---|-------|----------|---------|---------|-------------|
| 1 | GPL library in proprietary app | HIGH | libfoo | GPL 3.0 | Replace with Apache 2.0 alternative |
| 2 | Missing attribution | LOW | libbar | MIT | Add to license screen |

## Remediation Plan
1. [Ordered actions]

## Attestation
All obligations for permissive licenses (attribution) are met: [YES/NO]
No copyleft license violations exist: [YES/NO]
In-app license screen is implemented: [YES/NO]
```

---

## Expected Output

1. **Dependency Inventory** — complete list with license for each
2. **License Classification** — categorized by type and risk level
3. **Compatibility Assessment** — any license conflicts identified
4. **Attribution Implementation** — in-app license screen or notice file
5. **Non-Code Asset Audit** — license status for fonts, icons, images
6. **Compliance Report** — summary with issues, risk level, and remediation plan

---

## CRITICAL: Verification Requirements

- [ ] All direct dependencies have identified licenses
- [ ] Transitive dependencies are checked (not just direct dependencies)
- [ ] No GPL-licensed code in a proprietary app (unless GPL exception applies)
- [ ] Attribution notices are present in the app (in-app license screen or similar)
- [ ] Non-code assets (fonts, icons) have verified licenses allowing commercial use
- [ ] **Disclaimer:** This is a technical audit — consult a qualified IP attorney for complex license questions
