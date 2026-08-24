---
title: "Android Release Preparation"
category: mobile-development
description: "./gradlew bundleRelease"
tags:
  - android
  - mobile-development
updated: "2026-03-19"
---

# Android Release Preparation

> Part of the end-to-end flow: see [`android_release_governance_runbook.md`](android_release_governance_runbook.md).

**Objective:** Prepare an Android application for production release by conducting a comprehensive pre-release audit covering signing, versioning, build configuration, security hardening, and Play Store compliance requirements.

**When to Use:** Use this prompt when you're ready to prepare an Android app for release to the Google Play Store or other distribution channels. Ideal before your first release, when moving from beta to production, or before major version releases. Prerequisites include a working app that passes basic testing. This prompt ensures nothing critical is missed in the release process.

**Prompt Type:** Comprehensive (400-500 lines)

---

## Context Gathering

Before beginning the release preparation, gather essential context:

1. **Release Context:**
   - "Is this the initial release or an update to an existing app?"
   - "What version number will this release be?"

2. **Distribution Channel:**
   - "Will this be released on Google Play Store, enterprise distribution, or other channels?"
   - "Are you planning a full rollout or staged/beta release?"

3. **Release Timeline:**
   - "Do you have a target release date?"
   - "Are there any blocking issues you're already aware of?"

4. **Previous Issues:**
   - "Have there been any previous release rejections or issues from Google Play?"
   - "Are there any known compliance concerns (data privacy, target audience, etc.)?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before flagging ANY release issue, you MUST:**

1. **Trace actual configuration** - Don't flag issues without checking actual build.gradle and manifest settings.
2. **Check for existing setup** - Search for signing configurations, ProGuard rules, or release build types that may already be configured.
3. **Understand the context** - Consider if this is a first release or update, and what distribution channel is targeted.
4. **Confirm actual impact** - Will this issue actually prevent or cause problems with release?
5. **Provide specific file:line locations** - Every finding must reference exact configurations.

**Finding the app is RELEASE-READY is an acceptable outcome.** If configuration is correct, say so with confidence.

### False-Positive Prevention

- ❌ Do NOT flag development settings in debug builds as release issues
- ❌ Do NOT assume missing optional configurations are problems
- ❌ Do NOT ignore build variants when checking configurations
- ❌ Do NOT report Play Store requirements that don't apply to the distribution channel
- ✅ DO check release build type specifically, not debug
- ✅ DO verify signing configuration exists and is correct
- ✅ DO confirm version codes are properly incremented
- ✅ DO check for debuggable=false in release builds

---

### Phase 1: Build Configuration Audit

Examine the app's build configuration for release readiness.

#### 1.1 Version Configuration

**Verify versioning in build files:**

```kotlin
// Locations to check:
// - app/build.gradle.kts or app/build.gradle
// - Version catalog (libs.versions.toml) if used
// - BuildConfig references

// Required configuration:
android {
    defaultConfig {
        versionCode = [incrementing integer]
        versionName = "[semantic version]"
    }
}
```

**Evaluate:**
- [ ] `versionCode` is higher than any previously published version
- [ ] `versionName` follows semantic versioning (X.Y.Z)
- [ ] Version is not hardcoded in multiple places (single source of truth)
- [ ] Version is accessible in app for display (About screen, support)

#### 1.2 SDK Targets

**Verify SDK configuration:**

```kotlin
android {
    compileSdk = 34  // Should be latest stable
    defaultConfig {
        minSdk = [appropriate for target audience]
        targetSdk = 34  // Must meet Play Store requirements
    }
}
```

**Evaluate:**
- [ ] `targetSdk` meets current Play Store requirements
- [ ] `minSdk` is appropriate for target market
- [ ] No deprecated API usage that will break on target SDK
- [ ] CompileSdk is up to date

#### 1.3 Build Types Configuration

**Verify release build type:**

```kotlin
buildTypes {
    release {
        isMinifyEnabled = true
        isShrinkResources = true
        proguardFiles(
            getDefaultProguardFile("proguard-android-optimize.txt"),
            "proguard-rules.pro"
        )
        signingConfig = signingConfigs.getByName("release")
    }
}
```

**Evaluate:**
- [ ] ProGuard/R8 is enabled for release builds
- [ ] Resource shrinking is enabled
- [ ] Release signing config is properly configured
- [ ] Debug information is stripped
- [ ] Debuggable is false for release

#### 1.4 ProGuard/R8 Rules

**Check ProGuard configuration:**

```
Files to examine:
├── proguard-rules.pro
├── consumer-rules.pro (if library)
└── Any feature-specific ProGuard files
```

**Evaluate:**
- [ ] Rules exist for all third-party libraries
- [ ] Data classes used for serialization are kept
- [ ] Reflection-based code is properly excluded
- [ ] No overly broad keep rules that defeat optimization
- [ ] Test build with minification to verify no runtime crashes

---

### Phase 2: App Signing Verification

Ensure proper app signing configuration for release.

#### 2.1 Signing Configuration

**Verify signing setup:**

```kotlin
// DO NOT commit these values to version control
signingConfigs {
    create("release") {
        storeFile = file(keystorePath)
        storePassword = keystorePassword
        keyAlias = keyAlias
        keyPassword = keyPassword
    }
}
```

**Evaluate:**
- [ ] Release signing config exists and is separate from debug
- [ ] Keystore file exists and is accessible
- [ ] Credentials are NOT hardcoded in build files
- [ ] Credentials are loaded from environment variables or local.properties
- [ ] Keystore is properly backed up and secured

#### 2.2 Play App Signing

**Verify Play App Signing enrollment:**

- [ ] App is enrolled in Play App Signing (recommended)
- [ ] Upload key is properly configured
- [ ] Understand key rotation procedures if needed

#### 2.3 Signing Security Checklist

- [ ] Keystore password is strong and unique
- [ ] Key password is strong and unique
- [ ] Keystore is stored securely (not in version control)
- [ ] Backup of keystore exists in secure location
- [ ] Team members with access are documented

---

### Phase 3: Security Hardening

Verify security measures for production release.

#### 3.1 Debug/Development Artifacts

**Search for and remove:**

```kotlin
// Items to remove or guard:
- Log.d(), Log.v() statements (use BuildConfig checks)
- StrictMode configurations
- Development-only features
- Test credentials or endpoints
- Mock data or responses
```

**Evaluate:**
- [ ] Verbose logging is disabled in release
- [ ] No test credentials in code
- [ ] Development API endpoints are replaced with production
- [ ] Debug features are behind BuildConfig.DEBUG checks

#### 3.2 Network Security

**Verify network security configuration:**

```xml
<!-- res/xml/network_security_config.xml -->
<?xml version="1.0" encoding="utf-8"?>
<network-security-config>
    <base-config cleartextTrafficPermitted="false">
        <trust-anchors>
            <certificates src="system" />
        </trust-anchors>
    </base-config>
</network-security-config>
```

**Evaluate:**
- [ ] Network security config exists
- [ ] Cleartext traffic is disabled (or explicitly justified)
- [ ] Certificate pinning is implemented for sensitive APIs (if required)
- [ ] No debug certificate trust in release

#### 3.3 Data Security

**Verify data protection:**

- [ ] Sensitive data is encrypted at rest
- [ ] No sensitive data in SharedPreferences without encryption
- [ ] Proper use of Android Keystore for cryptographic keys
- [ ] Backup rules exclude sensitive data (`android:allowBackup` configuration)

#### 3.4 Code Security

**Check for security issues:**

```kotlin
// Issues to find and fix:
- Hardcoded secrets or API keys
- SQL injection vulnerabilities
- Intent injection vulnerabilities
- Exported components without permission protection
- WebView JavaScript enabled without proper safeguards
```

---

### Phase 4: Manifest Review

Comprehensive AndroidManifest.xml audit.

#### 4.1 Application Configuration

**Verify application attributes:**

```xml
<application
    android:name=".MyApplication"
    android:icon="@mipmap/ic_launcher"
    android:label="@string/app_name"
    android:roundIcon="@mipmap/ic_launcher_round"
    android:theme="@style/Theme.MyApp"
    android:allowBackup="false"
    android:fullBackupContent="@xml/backup_rules"
    android:dataExtractionRules="@xml/data_extraction_rules"
    android:networkSecurityConfig="@xml/network_security_config">
```

**Evaluate:**
- [ ] Proper icon and round icon are set
- [ ] App label is not hardcoded (uses string resource)
- [ ] Backup is properly configured or disabled
- [ ] Network security config is referenced
- [ ] Theme is properly set

#### 4.2 Permissions Audit

**Review all declared permissions:**

```xml
<!-- List all permissions and justify each -->
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

**Evaluate:**
- [ ] Only necessary permissions are declared
- [ ] No unused permissions from copied code
- [ ] Dangerous permissions have proper runtime handling
- [ ] Permission rationale is implemented for user-facing permissions

#### 4.3 Components Review

**Audit all components:**

```xml
<!-- Activities, Services, Receivers, Providers -->
<activity android:exported="false" ... />
<service android:exported="false" ... />
<receiver android:exported="false" ... />
<provider android:exported="false" ... />
```

**Evaluate:**
- [ ] Components are not exported unless necessary
- [ ] Exported components have proper permission protection
- [ ] Deep links are properly configured
- [ ] Intent filters are appropriate

#### 4.4 Feature Declarations

**Verify feature requirements:**

```xml
<uses-feature
    android:name="android.hardware.camera"
    android:required="false" />
```

**Evaluate:**
- [ ] Required vs optional features are correctly marked
- [ ] Hardware features don't unnecessarily limit device compatibility
- [ ] Software features are properly declared

---

### Phase 5: Resource & Asset Verification

Verify all resources are production-ready.

#### 5.1 App Icons

**Verify icon assets:**

```
res/
├── mipmap-mdpi/ic_launcher.png (48x48)
├── mipmap-hdpi/ic_launcher.png (72x72)
├── mipmap-xhdpi/ic_launcher.png (96x96)
├── mipmap-xxhdpi/ic_launcher.png (144x144)
├── mipmap-xxxhdpi/ic_launcher.png (192x192)
└── mipmap-anydpi-v26/ic_launcher.xml (adaptive icon)
```

**Evaluate:**
- [ ] All density buckets have icons
- [ ] Adaptive icon is implemented (API 26+)
- [ ] Round icon variant exists
- [ ] Icons look correct at all sizes
- [ ] No placeholder or debug icons remain

#### 5.2 String Resources

**Verify string resources:**

- [ ] No hardcoded strings in layouts or code
- [ ] All user-facing strings are in strings.xml
- [ ] Strings are properly localized (if supporting multiple languages)
- [ ] No placeholder text remains (e.g., "Lorem ipsum")
- [ ] Version string is updated if displayed

#### 5.3 Asset Review

**Check all assets:**

- [ ] Images are optimized (WebP where appropriate)
- [ ] No unused resources (run `./gradlew lint`)
- [ ] Raw files are production-ready
- [ ] No development/test assets in release

---

### Phase 6: Third-Party SDK Compliance

Verify third-party SDK configurations.

#### 6.1 Analytics & Crash Reporting

**Verify configurations:**

```kotlin
// Firebase/Analytics example
FirebaseAnalytics.getInstance(context).apply {
    setAnalyticsCollectionEnabled(!BuildConfig.DEBUG)
}
```

**Evaluate:**
- [ ] Analytics is disabled for debug builds (or development data is filtered)
- [ ] Crash reporting is properly configured
- [ ] User consent is obtained before tracking (if required)
- [ ] Data collection complies with privacy policy

#### 6.2 Ad SDKs (if applicable)

**Verify ad configuration:**

- [ ] Test ads are replaced with production ads
- [ ] Ad unit IDs are production IDs
- [ ] GDPR consent is properly implemented
- [ ] App-ads.txt is configured (if using programmatic ads)

#### 6.3 Payment SDKs (if applicable)

**Verify payment configuration:**

- [ ] Production payment credentials are configured
- [ ] Sandbox/test mode is disabled
- [ ] Proper error handling for payment failures
- [ ] Receipts are properly validated

---

### Phase 7: Findings Presentation

**CHECKPOINT 1:** Present the release readiness assessment.

```markdown
## Release Preparation Assessment

### Release Readiness Score: [Ready/Needs Work/Not Ready]

### Configuration Summary
| Area | Status | Issues |
|------|--------|--------|
| Build Configuration | [Ready/Issues] | [Count] |
| App Signing | [Ready/Issues] | [Count] |
| Security | [Ready/Issues] | [Count] |
| Manifest | [Ready/Issues] | [Count] |
| Resources | [Ready/Issues] | [Count] |
| Third-Party SDKs | [Ready/Issues] | [Count] |

### Critical Issues (Must Fix)
1. [Issue with location and severity]
2. [Issue with location and severity]

### Warnings (Should Fix)
1. [Warning with recommendation]
2. [Warning with recommendation]

### Ready to Build?
[Yes/No with explanation]

**What would you like me to address first?**
```

---

### Phase 8: Release Build & Verification

After addressing issues, guide through the release build process.

#### 8.1 Build Release APK/Bundle

**Generate release build:**

```bash
# For App Bundle (recommended)
./gradlew bundleRelease

# For APK
./gradlew assembleRelease
```

**Verify output:**
- [ ] Build completes without errors
- [ ] Output file exists in expected location
- [ ] File size is reasonable (check for bloat)
- [ ] Signing is correct (use `apksigner verify`)

#### 8.2 Pre-Upload Testing

**Final verification:**

```bash
# Verify APK/Bundle
bundletool validate --bundle app-release.aab

# Check APK signature
apksigner verify --verbose app-release.apk

# Test on device
adb install app-release.apk
```

**Evaluate:**
- [ ] App installs correctly
- [ ] App launches without crashes
- [ ] Core user flows work correctly
- [ ] No debug artifacts visible
- [ ] Performance is acceptable

---

## Expected Output

### Pre-Release Checklist

```markdown
# Release Checklist: [App Name] v[X.Y.Z]

## Build Configuration
- [x] Version code: [N] (higher than previous: [N-1])
- [x] Version name: [X.Y.Z]
- [x] Target SDK: [34] (meets Play requirements)
- [x] ProGuard enabled and tested
- [x] Shrink resources enabled

## App Signing
- [x] Release signing configured
- [x] Keystore secured and backed up
- [x] Enrolled in Play App Signing

## Security
- [x] Debug code removed/guarded
- [x] No hardcoded secrets
- [x] Network security configured
- [x] Cleartext traffic disabled

## Manifest
- [x] Permissions minimized
- [x] Components properly exported/protected
- [x] Backup rules configured

## Resources
- [x] App icons complete (all densities + adaptive)
- [x] No placeholder content
- [x] Strings localized

## Third-Party SDKs
- [x] Production credentials configured
- [x] Test/debug modes disabled
- [x] Privacy compliance verified

## Final Verification
- [x] Release build successful
- [x] APK/Bundle validated
- [x] Installation tested
- [x] Core flows verified

## Ready for Upload: [YES/NO]
```

---

## Example Interaction

**User:** I need to prepare my fitness tracking app for its first Play Store release. We've been in beta for 3 months.

**Agent:** I'll conduct a comprehensive release preparation audit. Let me start by examining your build configuration.

*[Agent examines build.gradle.kts, signing configuration, and manifest]*

**Agent:**

## Initial Release Preparation Scan

### Build Configuration
- **Version Code:** 15 (good - incrementing from beta)
- **Version Name:** 1.0.0 (appropriate for initial release)
- **Target SDK:** 34 (meets current requirements)
- **Min SDK:** 26 (supports 95%+ of devices)

### First Impressions
The build configuration is well-structured for release. I found a few items that need attention before uploading to the Play Store.

### Issues Found

**Critical (Must Fix):**
1. **Hardcoded API key** in `NetworkModule.kt:47` - Move to BuildConfig or secure storage
2. **Debug logging enabled** in release build - `LoggingInterceptor` still active in `NetworkModule.kt:62`

**Warnings (Should Fix):**
1. **Backup not configured** - `android:allowBackup="true"` without backup rules may expose user data
2. **Missing network security config** - Add explicit network security configuration

**Ready:**
- Signing configuration properly externalized
- ProGuard rules look comprehensive
- App icons are complete with adaptive icons

**Would you like me to help fix these issues, or should I continue with the security audit?**

---

## Techniques Used

- **ST-01** (Clear Objective): Single-sentence objective defining release preparation scope
- **ST-02** (Sequential Instructions): Phased audit from build config → signing → security → manifest → resources
- **RT-04** (Best Practice Review): Evaluation against Android release best practices
- **RT-05** (Evidence-Based Reasoning): All findings include file:line references
- **ST-03** (Output Format Templates): Structured checklist and assessment formats
- **OC-05** (Severity Classification): Critical/Warning categorization for issues
- **AG-02** (Skeptical Default Stance): Thorough security and compliance checking
- **NE-02** (Phased Workflow): Clear checkpoints between audit phases
- **NE-07** (Discussion Before Action): User approval before proceeding with fixes

---

## Related Prompts

- [android_privacy_compliance.md](android_privacy_compliance.md) - GDPR/CCPA and Play Store privacy compliance
- [android_app_bundle_optimization.md](android_app_bundle_optimization.md) - Reduce app size before release
- [android_play_store_optimization.md](android_play_store_optimization.md) - ASO and store listing optimization
- [android_staged_rollout.md](android_staged_rollout.md) - Plan beta and staged rollout strategy
- android_security_audit.md - Deep security analysis

---

## Customization Guide

### For Different Release Types

**Initial Release:**
- Extra emphasis on signing setup and backup
- Verify Play Console account setup
- Ensure all store listing assets are ready

**Major Version Update:**
- Focus on breaking changes and migration
- Verify version code increment
- Review changelog completeness

**Hotfix Release:**
- Streamlined checklist focusing on the fix
- Ensure no unintended changes included
- Fast-track testing on core flows

### For Different Distribution Channels

**Google Play Store:**
- Full compliance with Play policies
- App signing enrollment recommended
- All content rating questionnaires completed

**Enterprise/MDM Distribution:**
- Focus on security hardening
- Verify MDM compatibility
- Check certificate trust configuration

**Direct APK Distribution:**
- Ensure APK is self-signed properly
- Include update mechanism if needed
- Consider app bundle isn't applicable

### For Different App Categories

**Fintech/Banking Apps:**
- Enhanced security audit (certificate pinning, rooted device detection)
- Compliance verification (PCI-DSS if applicable)
- Fraud prevention measures

**Apps for Children:**
- COPPA compliance verification
- Families Policy requirements
- No behavioral advertising

**Health/Medical Apps:**
- HIPAA considerations if applicable
- Health data handling verification
- Appropriate disclaimers in place
