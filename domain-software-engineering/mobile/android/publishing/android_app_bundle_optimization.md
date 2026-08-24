---
title: "Android App Bundle Optimization"
category: mobile-development
description: "bundletool build-apks --bundle=app.aab --output=app.apks --mode=universal"
tags:
  - android
  - mobile-development
  - optimization
updated: "2026-03-19"
---

# Android App Bundle Optimization

**Objective:** Reduce Android app download and install size by analyzing and optimizing the App Bundle, identifying bloat sources, and implementing size reduction strategies to improve conversion rates and user retention.

**When to Use:** Use this prompt when your app size exceeds category averages, when you receive Play Store warnings about size, when targeting emerging markets with limited bandwidth, or when optimizing conversion rates (smaller apps convert better). Essential before major releases to ensure competitive app size.

**Prompt Type:** Modular (120-150 lines)

---

## Context Gathering

Before beginning optimization, gather context:

1. **Current State:**
   - "What is your current app download size and installed size?"
   - "Have you already enabled App Bundles and R8?"

2. **Size Targets:**
   - "Do you have a target size in mind?"
   - "Are you targeting any specific markets (emerging markets have stricter size concerns)?"

3. **Constraints:**
   - "Are there any resources or dependencies you cannot remove?"
   - "Do you need to support specific screen densities or ABIs?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before recommending ANY optimization, you MUST:**

1. **Trace actual size contributors** - Don't recommend optimizations without analyzing what actually contributes to app size.
2. **Check for existing optimizations** - Search for R8 configuration, resource shrinking, and existing optimization efforts.
3. **Understand the context** - Consider WHY resources exist. Some "large" assets may be essential.
4. **Confirm actual impact** - Will this optimization provide meaningful size reduction?
5. **Provide specific locations** - Every recommendation must reference exact files or resources.

**Finding the app is ALREADY OPTIMIZED is an acceptable outcome.** If size is reasonable for the app's features, say so with confidence.

### False-Positive Prevention

- ❌ Do NOT recommend removing resources without understanding their purpose
- ❌ Do NOT assume all images need compression without checking quality requirements
- ❌ Do NOT recommend aggressive shrinking without checking for reflection usage
- ❌ Do NOT ignore feature requirements when recommending removals
- ✅ DO use APK Analyzer to identify actual size contributors
- ✅ DO consider trade-offs between size and app functionality
- ✅ DO check if Play Store's dynamic delivery already handles optimization
- ✅ DO prioritize optimizations with highest size impact

---

### Phase 1: Size Analysis

Analyze current app bundle composition.

#### 1.1 Generate Size Report

**Use Android Studio APK Analyzer or bundletool:**

```bash
# Generate size breakdown using bundletool
bundletool build-apks --bundle=app.aab --output=app.apks --mode=universal
bundletool get-size total --apks=app.apks

# Or analyze specific configuration
bundletool get-size total --apks=app.apks --device-spec=device-spec.json

# Detailed breakdown
unzip -l app.apks
```

**Size breakdown to document:**

| Component | Size | % of Total |
|-----------|------|------------|
| DEX files | XX MB | XX% |
| Resources | XX MB | XX% |
| Native libraries | XX MB | XX% |
| Assets | XX MB | XX% |
| Other | XX MB | XX% |
| **Total** | XX MB | 100% |

#### 1.2 Identify Bloat Sources

**Check each category:**

```
DEX Files:
- Large dependencies (ML libraries, SDKs)
- Dead code not removed by R8
- Reflection-heavy code

Resources:
- Unused resources
- Uncompressed images
- Multiple density assets
- Large raw files

Native Libraries:
- Multiple ABI support (arm64-v8a, armeabi-v7a, x86, x86_64)
- Debug symbols included
- Unused native code

Assets:
- Large media files
- Embedded databases
- Fonts
```

---

### Phase 2: Optimization Implementation

Apply size reduction techniques.

#### 2.1 Build Configuration Optimization

**Enable App Bundle and optimizations:**

```kotlin
// app/build.gradle.kts
android {
    bundle {
        language {
            // Split by language
            enableSplit = true
        }
        density {
            // Split by screen density
            enableSplit = true
        }
        abi {
            // Split by CPU architecture
            enableSplit = true
        }
    }

    buildTypes {
        release {
            isMinifyEnabled = true
            isShrinkResources = true
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
        }
    }
}
```

#### 2.2 Resource Optimization

**Image optimization:**

```kotlin
// Use WebP format for images
// In Android Studio: Right-click drawable → Convert to WebP

// Use vector drawables where possible
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="24dp"
    android:height="24dp"
    android:viewportWidth="24"
    android:viewportHeight="24">
    <path android:fillColor="#000" android:pathData="..."/>
</vector>

// Remove unused resources
android {
    buildTypes {
        release {
            isShrinkResources = true  // Removes unused resources
        }
    }
}
```

**Resource configuration:**

```kotlin
// Limit supported densities if appropriate
android {
    defaultConfig {
        resourceConfigurations += listOf("en", "es", "de")  // Limit languages
    }
}

// Or limit densities
android {
    splits {
        density {
            isEnabled = true
            include("mdpi", "hdpi", "xhdpi", "xxhdpi")
            exclude("ldpi", "xxxhdpi")
        }
    }
}
```

#### 2.3 Native Library Optimization

**Optimize ABI support:**

```kotlin
// Only include necessary ABIs
android {
    defaultConfig {
        ndk {
            // Modern devices only
            abiFilters += listOf("arm64-v8a", "armeabi-v7a")
            // Exclude x86 if not needed for emulators
        }
    }
}

// Or use App Bundle splits (recommended)
android {
    bundle {
        abi {
            enableSplit = true  // Each user downloads only their architecture
        }
    }
}
```

#### 2.4 Code Optimization

**Enable aggressive R8 optimization:**

```kotlin
// proguard-rules.pro
# Aggressive optimizations
-optimizationpasses 5
-allowaccessmodification
-repackageclasses ''

# Remove logging in release
-assumenosideeffects class android.util.Log {
    public static *** d(...);
    public static *** v(...);
    public static *** i(...);
}
```

**Remove unused dependencies:**

```kotlin
// Identify unused dependencies with Gradle
./gradlew app:dependencies --configuration releaseRuntimeClasspath

// Use implementation instead of api where possible
dependencies {
    implementation("...") // Preferred - not exposed to consumers
    api("...")           // Only when consumers need it
}
```

#### 2.5 Asset Optimization

**On-demand delivery with Play Feature Delivery:**

```kotlin
// For large features, use dynamic feature modules
// settings.gradle.kts
include(":app", ":dynamicfeature")

// dynamicfeature/build.gradle.kts
plugins {
    id("com.android.dynamic-feature")
}

android {
    // Feature module configuration
}
```

**External asset delivery:**

```kotlin
// For large assets (>150MB), use Play Asset Delivery
// build.gradle.kts
android {
    assetPacks += listOf(":assetpack")
}

// assetpack/build.gradle.kts
plugins {
    id("com.android.asset-pack")
}

assetPack {
    packName = "assetpack"
    dynamicDelivery {
        deliveryType = "install-time" // or "fast-follow" or "on-demand"
    }
}
```

---

### Phase 3: Verification

Verify size improvements.

#### 3.1 Measure Improvement

**Compare before and after:**

```bash
# Generate size report
bundletool get-size total --apks=app-before.apks
bundletool get-size total --apks=app-after.apks

# Device-specific size
bundletool get-size total --apks=app.apks \
  --device-spec=pixel6-spec.json
```

**Document results:**

| Metric | Before | After | Reduction |
|--------|--------|-------|-----------|
| Download size | XX MB | XX MB | XX% |
| Install size | XX MB | XX MB | XX% |

#### 3.2 Test Functionality

- [ ] App installs correctly
- [ ] All features work
- [ ] No crash on startup
- [ ] Resources load correctly
- [ ] Native libraries work on all target ABIs

---

## Expected Output

### Size Optimization Report

```markdown
# App Size Optimization Report

## Summary
- **Original Download Size:** XX MB
- **Optimized Download Size:** XX MB
- **Reduction:** XX MB (XX%)

## Optimizations Applied

| Optimization | Size Saved | Risk Level |
|-------------|------------|------------|
| R8/ProGuard optimization | X MB | Low |
| Resource shrinking | X MB | Low |
| WebP conversion | X MB | Low |
| ABI splits | X MB | Low |
| Unused dependency removal | X MB | Medium |

## Size Breakdown (After)

| Component | Size | Change |
|-----------|------|--------|
| DEX | X MB | -X MB |
| Resources | X MB | -X MB |
| Native libs | X MB | -X MB |
| Assets | X MB | -X MB |

## Additional Recommendations
1. [Recommendation with potential savings]
2. [Recommendation with potential savings]
```

---

## Example Interaction

**User:** My app is 85MB and I'd like to get it under 50MB for better emerging market performance.

**Agent:** I'll analyze your app bundle and identify optimization opportunities.

*[Agent analyzes APK/AAB]*

**Agent:**

## Size Analysis

**Current Breakdown:**
| Component | Size | % |
|-----------|------|---|
| DEX | 18 MB | 21% |
| Resources | 25 MB | 29% |
| Native libs | 38 MB | 45% |
| Assets | 4 MB | 5% |

**Key Findings:**

1. **Native libraries are 45% of size** - You're bundling 4 ABIs. With App Bundle splits, most users would download only ~10MB of native code.

2. **25MB resources** - Found 312 unused resources and 47 PNGs that could be WebP.

3. **ML Kit dependency** - Adding 12MB to DEX. Consider on-device ML only if essential.

**Recommended Actions:**

1. Enable ABI splits (immediate -28MB for most users)
2. Run resource shrinking + WebP conversion (-8MB estimated)
3. Remove unused dependencies (-4MB estimated)

**Projected result: 45MB download size for arm64 devices**

Want me to implement these optimizations?

---

## Techniques Used

- **ST-01** (Clear Objective): Focused size optimization objective
- **ST-02** (Sequential Instructions): Analysis → Optimization → Verification
- **RT-05** (Evidence-Based Reasoning): Size data with measurements
- **ST-03** (Output Format Templates): Structured size reports
- **AG-12** (Quantitative Metrics): MB savings and percentages
- **NE-07** (Discussion Before Action): Checkpoint for approval before changes

---

## Related Prompts

- [android_release_preparation.md](android_release_preparation.md) - Complete release checklist
- [android_performance_audit.md](../analysis/android_performance_audit.md) - Overall performance analysis
- [android_play_store_optimization.md](android_play_store_optimization.md) - Store listing (size affects conversion)

---

## Customization Guide

### For Different Size Targets

**Under 10MB (Instant Apps eligible):**
- Aggressive feature removal
- On-demand feature delivery
- Minimal assets bundled

**Under 150MB (No warnings):**
- Standard optimizations
- App Bundle splits
- Asset optimization

**Over 150MB (Games/Media):**
- Play Asset Delivery required
- Streaming assets consideration
- Feature delivery prioritization

### For Different App Types

**Games:**
- Asset packs for levels/content
- Texture compression (ETC2/ASTC)
- On-demand level downloads

**Media Apps:**
- Stream rather than bundle
- Adaptive quality assets
- Offline sync strategy

**Utility Apps:**
- Should target <30MB
- Minimize native dependencies
- Consider Kotlin-only (no NDK)
