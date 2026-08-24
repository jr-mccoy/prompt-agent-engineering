---
title: "iOS App Size Optimization"
category: mobile-development
description: "Reduce IPA size and optimize assets through asset catalog optimization, unused code elimination, framework thinning, on-demand resources, image format selection, and binary size analysis."
techniques:
  - ST-01
  - RT-02
difficulty: intermediate
tags:
  - ios
  - swift
  - app-size
  - optimization
  - assets
  - mobile-development
updated: "2026-03-20"
---

# iOS App Size Optimization

**Objective:** Systematically reduce the iOS app's IPA download and install size through asset catalog optimization, unused code and resource elimination, framework thinning, on-demand resources, optimal image format selection (HEIF, SVG, WebP), and binary size analysis using Xcode tooling and third-party utilities.

**When to Use:** Use this prompt when the app binary exceeds acceptable thresholds (200MB App Store limit, or team-defined limits), when download conversion rates drop due to size, when cellular download limits are a concern (200MB over cellular), or during periodic optimization reviews. Best used before major releases.

**Prompt Type:** Modular (150-400 lines)

---

## Context Gathering

Before optimizing, gather essential context:

1. **Current Size:**
   - "What is the current App Store download size and install size?"
   - "What is the thinned size for the most common device (check App Store Connect)?"
   - "Have you run the App Thinning Size Report from Xcode?"

2. **Size Budget:**
   - "What is the target size reduction (e.g., under 100MB download)?"
   - "Is the 200MB cellular download limit a concern for your users?"
   - "Are there stakeholder requirements for maximum app size?"

3. **Asset Inventory:**
   - "How many images/assets are in the asset catalog?"
   - "Are there bundled videos, ML models, or large data files?"
   - "Are all assets actively used in the current codebase?"

4. **Architecture:**
   - "How many frameworks (static/dynamic) does the app link?"
   - "Are there third-party SDKs contributing significant size?"
   - "Is the app modularized (SPM packages, frameworks)?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before making ANY optimization changes, you MUST:**

1. **Measure baseline** - Generate an App Thinning Size Report to establish the starting point for each device variant.
2. **Identify top contributors** - Use the size report and binary analysis to rank contributors by size before optimizing.
3. **Test after each change** - Verify app functionality is preserved after removing or converting assets.
4. **Track size impact** - Measure the delta after each optimization to confirm it had the expected effect.
5. **Document findings** - Record what was changed and the size impact for future reference.

### False-Positive Prevention

- Do NOT remove assets without verifying they are unused (string-based asset references may not appear in code search)
- Do NOT convert all images to a single format; choose format per use case (vector vs raster, transparency needs)
- Do NOT strip bitcode or debug symbols in debug builds; only in release
- Do NOT remove frameworks without checking all code paths (including dynamically loaded features)
- Do NOT assume On-Demand Resources work offline; test the download flow
- DO use Xcode's App Thinning Size Report as the source of truth, not raw IPA size
- DO test on physical devices after optimization to catch missing resources
- DO keep a size budget CI check to prevent regression
- DO consider the tradeoff between download size and runtime performance

---

### Phase 1: Size Analysis & Measurement

#### 1.1 Generate App Thinning Size Report

```bash
# Step 1: Archive the app
# Xcode > Product > Archive

# Step 2: Export with thinning report
# Organizer > Distribute App > Ad Hoc > Export
# Check "Include App Thinning Report"

# Step 3: Review the App Thinning Size Report.txt
# Shows compressed and uncompressed size per device variant

# Alternatively, use command line:
xcodebuild -exportArchive \
  -archivePath build/YourApp.xcarchive \
  -exportPath build/export \
  -exportOptionsPlist ExportOptions.plist

# ExportOptions.plist should include:
# <key>thinning</key>
# <string>&lt;thin-for-all-variants&gt;</string>
```

#### 1.2 Binary Size Breakdown

```bash
# Analyze the binary with bloaty or nm
# Install bloaty: brew install bloaty

# Analyze Mach-O binary
bloaty -d compileunits YourApp.app/YourApp

# List all symbols by size
nm -print-size -size-sort YourApp.app/YourApp | tail -50

# Framework sizes
du -sh YourApp.app/Frameworks/* | sort -rh

# Asset catalog size
du -sh YourApp.app/Assets.car

# Total app bundle breakdown
find YourApp.app -type f -exec du -sh {} \; | sort -rh | head -30
```

#### 1.3 Size Breakdown Categories

```markdown
## Size Analysis Template

| Category | Size (MB) | % of Total | Action |
|----------|----------|------------|--------|
| Binary code (Mach-O) | — | — | Dead code elimination |
| Asset catalog (.car) | — | — | Image optimization |
| Bundled resources | — | — | ODR, compression |
| Frameworks (dynamic) | — | — | Static linking, removal |
| ML models (.mlmodel) | — | — | Quantization, ODR |
| Localization (.lproj) | — | — | Review unused strings |
| Storyboards/XIBs | — | — | SwiftUI migration |
| Other | — | — | Investigation |
| **TOTAL** | — | 100% | |
```

---

### Phase 2: Asset Optimization

**CHECKPOINT 1:** Complete size analysis before optimizing assets.

```markdown
## Size Analysis Results

| Component | Compressed | Uncompressed | Priority |
|-----------|-----------|--------------|----------|
| [Fill from analysis] | — | — | High/Med/Low |

**Top 3 size contributors identified. Proceed with optimization?**
```

#### 2.1 Image Format Selection Guide

```markdown
| Format | Best For | Transparency | Animation | Compression |
|--------|----------|-------------|-----------|-------------|
| SVG (via PDF vector) | Icons, simple graphics | Yes | No | Scales to any size, tiny file |
| HEIF (.heic) | Photos, complex images | Yes | No | 50% smaller than JPEG |
| WebP | Web-origin images | Yes | Yes | 30% smaller than PNG |
| PNG | UI elements needing transparency | Yes | No | Lossless, larger |
| JPEG | Photos without transparency | No | No | Good compression |
| SF Symbols | System icons | Yes | No | Zero bundle cost |
```

```swift
// Prefer SF Symbols over bundled icons (zero size cost)
// BEFORE: Custom icon in asset catalog (~2-10KB each)
Image("custom_settings_icon")

// AFTER: SF Symbol (0KB added to bundle)
Image(systemName: "gearshape.fill")

// For custom icons, use PDF vectors in asset catalog:
// Asset catalog > Image Set > Scales: Single Scale
// Render As: Template Image
// Preserves Vector Data: YES (checkbox in Xcode)
```

#### 2.2 Asset Catalog Optimization

```bash
# Find unused images in the asset catalog
# Method 1: Search for references in code
find . -name "*.swift" -o -name "*.storyboard" -o -name "*.xib" | \
  xargs grep -l "image_name" # per asset

# Method 2: Use a dedicated tool
# Install: brew install peripheryapp/periphery/periphery
periphery scan --format csv | grep "unused"

# Method 3: Xcode Build Setting
# ASSETCATALOG_COMPILER_OPTIMIZATION = space  (optimize for size)
# Set in Build Settings > Asset Catalog Compiler - Options
```

```swift
// Asset catalog optimization settings in Build Settings:
// ASSETCATALOG_COMPILER_OPTIMIZATION = space
// ENABLE_ON_DEMAND_RESOURCES = YES (if using ODR)
// COMPRESS_PNG_FILES = YES
// STRIP_PNG_TEXT = YES
```

#### 2.3 Image Compression Script

```bash
#!/bin/bash
# compress_assets.sh - Lossless PNG compression for asset catalogs

# Install: brew install pngquant optipng

find . -path "*/Assets.xcassets/*.imageset/*.png" | while read file; do
    original_size=$(stat -f%z "$file")

    # Lossy compression (visually lossless at quality 80-100)
    pngquant --quality=80-100 --skip-if-larger --force --output "$file" "$file"

    # Lossless optimization pass
    optipng -o5 -quiet "$file"

    new_size=$(stat -f%z "$file")
    saved=$((original_size - new_size))
    if [ $saved -gt 0 ]; then
        echo "Saved $(($saved / 1024))KB: $file"
    fi
done
```

---

### Phase 3: Code & Framework Optimization

#### 3.1 Dead Code Elimination

```swift
// Build Settings for dead code stripping:
// DEAD_CODE_STRIPPING = YES (default, ensure it's on)
// STRIP_SWIFT_SYMBOLS = YES (release builds)
// GCC_OPTIMIZATION_LEVEL = -Os (optimize for size in release)

// Link-Time Optimization (LTO) for maximum dead code removal:
// LLVM_LTO = YES (or YES_THIN for faster builds)
// This enables cross-module dead code elimination
```

```bash
# Find unused Swift code with periphery
periphery scan \
  --project YourApp.xcodeproj \
  --schemes YourApp \
  --targets YourApp \
  --format csv

# Output shows unused classes, methods, properties
# Review before removing -- some may be used via reflection or dynamic dispatch
```

#### 3.2 Framework Thinning

```markdown
## Framework Optimization Strategies

| Strategy | Size Impact | Effort |
|----------|------------|--------|
| Replace dynamic with static linking | 2-10% reduction | Medium |
| Remove unused SDK features | Variable | Low |
| Use lite/core SDK variants | 30-70% per SDK | Low |
| Replace SDK with native API | 100% of SDK size | High |
| Merge small frameworks into app binary | 1-5% reduction | Low |
```

```swift
// In Package.swift or Xcode Build Settings:

// Prefer static libraries to avoid dynamic framework overhead
// Each dynamic framework adds ~200KB+ for the Mach-O header
// Static linking merges code into the main binary

// SPM: Use .staticLibrary for internal packages
let package = Package(
    products: [
        .library(name: "SharedKit", type: .static, targets: ["SharedKit"])
    ]
)

// Xcode: Build Settings
// MACH_O_TYPE = staticlib (for framework targets)
```

#### 3.3 Common SDK Size Offenders

```markdown
| SDK | Typical Size | Lighter Alternative |
|-----|-------------|-------------------|
| Firebase (full) | 15-30MB | Firebase Lite / specific pods only |
| Google Maps | 15-20MB | MapKit (free, no SDK) |
| AWS Amplify (full) | 10-20MB | Individual AWS SDK modules |
| Facebook SDK | 5-10MB | Limited Login Kit only |
| Lottie | 2-5MB | Native SwiftUI animations |
| Realm | 5-8MB | SwiftData / Core Data (built-in) |
```

---

### Phase 4: On-Demand Resources & Advanced Techniques

**CHECKPOINT 2:** Review asset and code optimizations before advanced techniques.

```markdown
## Optimization Progress

| Optimization | Size Saved | Status |
|-------------|-----------|--------|
| Image compression | — MB | Done/Pending |
| Unused asset removal | — MB | Done/Pending |
| Dead code elimination | — MB | Done/Pending |
| Framework thinning | — MB | Done/Pending |
| **Total saved** | **— MB** | |

**Current size: — MB. Target: — MB. Proceed with advanced techniques?**
```

#### 4.1 On-Demand Resources (ODR)

```swift
// Tag resources in Xcode asset catalog with ODR tags
// Asset catalog > Select image set > On Demand Resource Tags: "level-2-assets"

// Request ODR at runtime:
final class ODRManager {
    private var resourceRequest: NSBundleResourceRequest?

    func loadResources(tag: String) async throws {
        let request = NSBundleResourceRequest(tags: [tag])
        self.resourceRequest = request // retain to keep resources loaded

        // Check if already available
        let available = await request.conditionallyBeginAccessingResources()
        if available { return }

        // Download
        try await request.beginAccessingResources()
    }

    func releaseResources() {
        resourceRequest?.endAccessingResources()
        resourceRequest = nil
    }
}

// Use cases for ODR:
// - Game levels/maps loaded progressively
// - Tutorial content loaded on first launch
// - Seasonal/promotional assets
// - Region-specific content
```

#### 4.2 App Thinning Best Practices

```swift
// Ensure app thinning slices correctly:

// 1. Asset catalogs automatically thin per device
//    - 1x, 2x, 3x variants → only matching scale delivered
//    - Device-specific assets → only matching device delivered

// 2. Bitcode (deprecated in Xcode 14+, but for older projects):
//    ENABLE_BITCODE = NO (Xcode 14+)

// 3. Executable architecture:
//    EXCLUDED_ARCHS (Simulator) = arm64 (for Intel-based CI)
//    App Store automatically thins to device architecture

// 4. Build Settings for minimum size:
//    SWIFT_COMPILATION_MODE = wholemodule (better dead code elimination)
//    GCC_OPTIMIZATION_LEVEL = -Os (optimize for size)
//    SWIFT_OPTIMIZATION_LEVEL = -Osize
```

#### 4.3 CI Size Monitoring

```bash
#!/bin/bash
# ci_size_check.sh - Fail CI if app exceeds size budget

MAX_SIZE_MB=100
ARCHIVE_PATH="build/YourApp.xcarchive"

# Build and archive
xcodebuild archive \
  -project YourApp.xcodeproj \
  -scheme YourApp \
  -archivePath "$ARCHIVE_PATH" \
  -configuration Release

# Get size
APP_SIZE=$(du -sm "$ARCHIVE_PATH/Products/Applications/YourApp.app" | cut -f1)

echo "App size: ${APP_SIZE}MB (budget: ${MAX_SIZE_MB}MB)"

if [ "$APP_SIZE" -gt "$MAX_SIZE_MB" ]; then
    echo "ERROR: App exceeds size budget by $((APP_SIZE - MAX_SIZE_MB))MB"
    exit 1
fi
```

---

## Expected Output

### Size Optimization Report

```markdown
## App Size Optimization Report

### Before/After Summary
| Metric | Before | After | Saved |
|--------|--------|-------|-------|
| Download size (iPhone 15) | — MB | — MB | — MB (—%) |
| Install size (iPhone 15) | — MB | — MB | — MB (—%) |
| Asset catalog (.car) | — MB | — MB | — MB |
| Binary (Mach-O) | — MB | — MB | — MB |
| Frameworks | — MB | — MB | — MB |

### Changes Made
1. [Description of change] → [size impact]
2. [Description of change] → [size impact]
3. [Description of change] → [size impact]

### Recommendations for Future
- [Recommendation with estimated impact]
```

### Implementation Checklist

- [ ] Baseline App Thinning Size Report generated
- [ ] Binary size breakdown by category completed
- [ ] Unused assets identified and removed
- [ ] Images converted to optimal formats (SVG, HEIF, SF Symbols)
- [ ] PNG compression applied to remaining raster images
- [ ] Dead code elimination verified (build settings + tooling)
- [ ] Framework audit completed (static vs dynamic, unused SDKs)
- [ ] On-Demand Resources configured for non-essential content
- [ ] Build settings optimized (-Osize, DEAD_CODE_STRIPPING, LTO)
- [ ] CI size monitoring script added
- [ ] Post-optimization testing passed on physical device

---

## Techniques Used

- **ST-01** (Clear Objective): Focused on systematic IPA size reduction
- **RT-02** (Multi-Dimensional Analysis): Covers assets, code, frameworks, and build settings

---

## Related Prompts

- [ios_app_thinning_optimization.md](../publishing/ios_app_thinning_optimization.md) - App Store thinning configuration
- [ios_startup_optimization.md](../improvement/ios_startup_optimization.md) - Launch time optimization (related to binary size)
- [ios_code_modernization.md](../improvement/ios_code_modernization.md) - Dead code identification during modernization
- [ios_pre_submission_checklist.md](../publishing/ios_pre_submission_checklist.md) - Pre-submission size verification
