---
title: "iOS App Thinning Optimization"
category: mobile-development
description: "Modular guide for optimizing iOS app size through App Thinning techniques including slicing, bitcode, on-demand resources, asset catalog optimization, and binary size analysis."
techniques:
  - ST-01 (Structured Task Decomposition)
  - RT-02 (Checklist Verification)
  - DS-02 (Domain-Specific Terminology)
  - AN-01 (Analysis Framework)
difficulty: intermediate
tags:
  - ios
  - swift
  - app-store
  - app-thinning
  - slicing
  - on-demand-resources
  - binary-size
  - asset-catalog
  - optimization
updated: "2026-03-19"
---

# iOS App Thinning Optimization

**Objective:** Reduce iOS app download and install size through Apple's App Thinning technologies (slicing, on-demand resources), asset catalog optimization, and systematic binary size analysis. A smaller app increases conversion rates (apps over 200MB cannot be downloaded over cellular), reduces user churn, and improves update adoption.

**When to Use:** When app size exceeds 100MB, when adding new asset-heavy features, when targeting markets with limited bandwidth, during quarterly size audits, or when App Store Connect shows high "did not download" rates.

**Prompt Type:** Modular (approximately 280 lines)

## Context Gathering

1. What is the current app download size and install size (from App Store Connect)?
2. Does the app include large assets (images, 3D models, audio, video, ML models)?
3. Are assets organized in Xcode Asset Catalogs or stored as loose files?
4. Does the app use any on-demand resources currently?
5. What is the minimum deployment target?
6. Does the app include multiple architectures or frameworks with unused slices?
7. Are there any embedded frameworks or dynamic libraries?

## Instructions

### CRITICAL: Verification Requirements

- [ ] App Thinning report generated from App Store Connect shows size reduction
- [ ] All asset catalogs use appropriate compression and scale factors
- [ ] On-demand resources download correctly and handle unavailability gracefully
- [ ] Binary size analysis identifies and addresses the largest contributors
- [ ] App functions correctly on all supported devices after thinning

### False-Positive Prevention

- ❌ DO NOT assume Xcode automatically optimizes all assets; loose files bypass App Thinning
- ❌ DO NOT remove @1x assets if you still support non-Retina devices
- ❌ DO NOT set on-demand resources as "initial install" tags which defeats the purpose
- ❌ DO NOT ignore third-party framework sizes; they often contribute the most to binary bloat
- ❌ DO NOT use PNG for photographic content; HEIC or JPEG in asset catalogs is dramatically smaller
- ✅ DO use Asset Catalogs for ALL image assets to enable slicing
- ✅ DO test on-demand resource downloads on slow network connections
- ✅ DO profile the app size report in Xcode Organizer after every release
- ✅ DO set appropriate asset catalog compression for each image type

## Module 1: App Slicing

App slicing delivers only the resources needed for a specific device:

```
SLICING OPTIMIZATION CHECKLIST:
[ ] All images are in Asset Catalogs (not loose in bundle)
[ ] Asset Catalogs include only needed scale factors:
    - @1x: Only if supporting non-Retina (rare)
    - @2x: iPhone SE, iPad (non-Pro)
    - @3x: iPhone (6s and later Pro/Plus models)
[ ] Device-specific assets use trait variations in Asset Catalogs:
    - Memory: 1GB, 2GB, 3GB, 4GB+ variants
    - Graphics: GPU family variants
    - Device: iPhone vs iPad specific assets
[ ] Metal shaders compiled for target GPU families only
[ ] Architecture slicing confirmed (arm64 only for modern deployment targets)
```

Verify slicing in App Store Connect:

```
App Store Connect → App → Activity → Build → App Thinning Size Report
- Check "Compressed File Size" for each device variant
- Verify iPhone variant is smaller than universal build
- Confirm iPad variant excludes iPhone-only assets
```

## Module 2: On-Demand Resources (ODR)

```swift
// Tag configuration in Xcode:
// 1. Select asset in Asset Catalog or resource file
// 2. In Attributes Inspector, set "On Demand Resource Tags"
// 3. Assign to logical groups: "level-1", "tutorial", "premium-content"

// Requesting on-demand resources
final class ODRManager {
    private var resourceRequest: NSBundledResourceRequest?

    func loadResources(withTag tag: String) async throws {
        let request = NSBundledResourceRequest(tags: [tag])
        self.resourceRequest = request

        // Check if already available
        let isAvailable = request.conditionallyBeginAccessingResources { available in
            if available {
                // Resources already downloaded and available
                self.useResources(tag: tag)
            }
        }

        if !isAvailable {
            // Download resources
            request.loadingPriority = NSBundledResourceRequestLoadingPriorityUrgent
            try await request.beginAccessingResources()
            useResources(tag: tag)
        }
    }

    func releaseResources(withTag tag: String) {
        resourceRequest?.endAccessingResources()
        resourceRequest = nil
    }

    private func useResources(tag: String) {
        // Access resources from the main bundle as normal
        // They are temporarily available after download
    }
}
```

```
ON-DEMAND RESOURCES CHECKLIST:
[ ] Resources categorized into logical tag groups
[ ] Tag categories defined in Xcode:
    - Initial Install Tags: Resources needed at first launch
    - Prefetch Tag Order: Resources likely needed soon
    - Download On Demand: Resources loaded when needed
[ ] Error handling for network unavailability
[ ] Progress UI shown during resource download
[ ] Resources released (endAccessingResources) when no longer needed
[ ] Low disk space handling implemented
[ ] Purge priority set correctly for resource groups
[ ] Total on-demand resource hosting under 20GB limit
[ ] Individual resource tag under 512MB
[ ] Tested resource loading on slow/no network conditions
```

## Module 3: Asset Catalog Optimization

```
ASSET CATALOG AUDIT:

Image Compression Settings (per asset in Asset Catalog):
┌─────────────────────┬──────────────────┬──────────────────────────────┐
│ Image Type          │ Recommended      │ Compression                  │
│                     │ Format           │ Setting                      │
├─────────────────────┼──────────────────┼──────────────────────────────┤
│ App Icons           │ PNG              │ Automatic                    │
│ UI Elements (flat)  │ PDF (vector)     │ Automatic + Preserve Vector  │
│ Photos              │ HEIC             │ Lossy (GPU Best Quality)     │
│ Illustrations       │ PNG              │ Lossless                     │
│ Gradients/Patterns  │ PDF (vector)     │ Preserve Vector Data         │
│ Large backgrounds   │ HEIC or JPEG     │ Lossy (GPU Balanced)         │
│ Thumbnails          │ HEIC             │ Lossy (GPU Smaller Size)     │
└─────────────────────┴──────────────────┴──────────────────────────────┘

Asset Catalog Checklist:
[ ] Remove unused image assets (search project for references)
[ ] Use PDF vectors with "Preserve Vector Data" for scalable UI elements
[ ] Enable "Compress" option for photographic content
[ ] Use "Individual Scales" and provide only needed scale factors
[ ] Consolidate duplicate assets across targets
[ ] Use symbol images (SF Symbols) instead of custom icons where possible
[ ] Sprite atlases configured for game assets
[ ] Color assets use named colors in Asset Catalog (not hardcoded)
```

Find unused assets:

```bash
# List all assets in the Asset Catalog
find YourProject -name "*.imageset" -exec basename {} .imageset \; | sort > catalog_assets.txt

# Search for references in code
grep -rn --include="*.swift" --include="*.xib" --include="*.storyboard" -f catalog_assets.txt YourProject/ | awk -F: '{print $3}' | sort -u > used_assets.txt

# Find unreferenced assets
comm -23 catalog_assets.txt used_assets.txt > unused_assets.txt
```

## Module 4: Binary Size Analysis

```bash
# Generate app size report from archive
xcodebuild -exportArchive \
  -archivePath YourApp.xcarchive \
  -exportPath export/ \
  -exportOptionsPlist ExportOptions.plist \
  -allowProvisioningUpdates

# Analyze binary segments
xcrun size -m export/YourApp.app/YourApp

# Detailed segment breakdown
xcrun otool -l export/YourApp.app/YourApp | grep -A4 "LC_SEGMENT"

# Find largest object files in the binary
xcrun nm -print-size -size-sort export/YourApp.app/YourApp | tail -20

# List all embedded frameworks and their sizes
du -sh export/YourApp.app/Frameworks/* | sort -rh

# Generate link map for detailed analysis (add to Other Linker Flags: -Xlinker -map -Xlinker /tmp/linkmap.txt)
# Then analyze:
# Sort sections by size from link map
awk '/^# Sections:/{found=1; next} /^# Symbols:/{found=0} found{print}' /tmp/linkmap.txt | sort -t$'\t' -k3 -rn
```

```
BINARY SIZE ANALYSIS TEMPLATE:

Size Breakdown:
┌─────────────────────────────┬──────────┬─────────────┐
│ Component                   │ Size     │ % of Total  │
├─────────────────────────────┼──────────┼─────────────┤
│ Main executable (__TEXT)     │          │             │
│ Main executable (__DATA)     │          │             │
│ Asset Catalog (Assets.car)  │          │             │
│ Embedded Frameworks         │          │             │
│   - Framework 1             │          │             │
│   - Framework 2             │          │             │
│ Storyboards/XIBs            │          │             │
│ Localization files          │          │             │
│ ML Models (.mlmodelc)       │          │             │
│ Other resources              │          │             │
├─────────────────────────────┼──────────┼─────────────┤
│ TOTAL                       │          │ 100%        │
└─────────────────────────────┴──────────┴─────────────┘

Top Optimization Opportunities:
1. _____________________________ (est. savings: ___MB)
2. _____________________________ (est. savings: ___MB)
3. _____________________________ (est. savings: ___MB)
```

## Module 5: Size Reduction Strategies

```
SIZE REDUCTION CHECKLIST:
[ ] Strip unused architectures from third-party frameworks
[ ] Enable Dead Code Stripping (DEAD_CODE_STRIPPING = YES)
[ ] Enable Link-Time Optimization (LTO) for Release builds
[ ] Remove unused frameworks and libraries from Link Binary phase
[ ] Convert large PNG images to HEIC or compressed JPEG
[ ] Use SF Symbols instead of custom icon assets
[ ] Move tutorial/onboarding assets to on-demand resources
[ ] Replace bundled ML models with Core ML on-device compilation or CloudKit
[ ] Audit localizable.strings for unused keys
[ ] Compress audio files (use AAC instead of WAV/AIFF)
[ ] Use vector PDFs instead of rasterized PNGs for UI elements
[ ] Review Info.plist for unnecessary embedded data
[ ] Enable ASSETCATALOG_COMPILER_OPTIMIZATION = space
```

## Expected Output

After completing this prompt, you will have:

1. App slicing verified with device-specific size variants
2. On-demand resources configured for large, non-essential assets
3. Asset catalog fully optimized with correct compression settings
4. Binary size analysis identifying top contributors
5. Actionable size reduction plan with estimated savings
6. Measurable reduction in app download and install size

## Example Interaction

**User:** My travel app is 245MB. It has lots of destination photos, offline maps, and an ML model for image recognition. Users complain they can't download over cellular.

**Assistant:** At 245MB you are above the 200MB cellular download limit. Here is the optimization plan:

**Immediate wins:**
- Destination photos: Convert from PNG to HEIC in Asset Catalogs (estimated 60-70% reduction)
- Offline maps: Move to on-demand resources, download per-region (maps are prime ODR candidates)
- ML model: Use Core ML model compression or move to on-device compilation

**Estimated size after optimization:**
- Photos: 80MB -> 24MB (HEIC compression)
- Maps: 100MB -> 0MB at install (on-demand)
- ML model: 40MB -> 15MB (quantization)
- Projected total: ~100MB (under cellular limit)

## Techniques Used

| Technique | Application |
|-----------|-------------|
| ST-01 (Structured Task Decomposition) | Five modular optimization areas |
| RT-02 (Checklist Verification) | Checklists for each optimization technique |
| DS-02 (Domain-Specific Terminology) | App Thinning, slicing, ODR, Asset Catalogs, link maps |
| AN-01 (Analysis Framework) | Binary size analysis with component breakdown |

## Related Prompts

- [ios_release_preparation.md](ios_release_preparation.md) - Build configuration for Release optimization
- [ios_pre_submission_checklist.md](ios_pre_submission_checklist.md) - Final validation including size verification
- [ios_testflight_rollout.md](ios_testflight_rollout.md) - Test thinned builds via TestFlight

## Customization Guide

- **For games:** Focus on sprite atlas optimization, texture compression (ASTC format), and on-demand resources for level packs
- **For media apps:** Emphasize streaming over bundling, use HLS for video, and compress audio to AAC
- **For apps with ML models:** Use Core ML model quantization (Float16 or Int8) and consider on-demand model downloads
- **For apps with many localizations:** Audit per-language asset duplication and use base localization where possible
- **For apps supporting older devices:** Keep @2x assets but remove @1x; analyze if @3x-only is viable for your deployment target
