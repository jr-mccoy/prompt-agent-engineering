---
title: "iOS Core Animation Hitch Review"
category: mobile-development
description: "Review animation hitches caused by off-screen rendering, shadows, masks, corner radius, layer compositing, and Instruments analysis in iOS applications."
techniques:
  - ST-01
  - RT-02
  - AG-02
  - AG-12
difficulty: advanced
tags:
  - ios
  - swift
  - code-review
  - performance
  - core-animation
  - rendering
updated: "2026-03-19"
---

# iOS Core Animation Hitch Review

**Objective:** Audit rendering pipeline for animation hitches by identifying off-screen rendering triggers, expensive shadow/mask/corner radius combinations, layer compositing bottlenecks, and providing Instruments-based analysis guidance to achieve consistent 60/120fps rendering.

**When to Use:** Apply when users report scroll jank, animations dropping frames, or when Instruments shows commit/render hitch ratios above threshold. Particularly important for views with rounded corners, shadows, blurs, or complex layer hierarchies.

**Prompt Type:** Modular (80-150 lines)

## Context Gathering

1. What device targets must be supported (older A-series chips vs modern)?
2. Are there views combining shadows + corner radius + masks?
3. Is the app using UIKit layers directly or SwiftUI with overlay/clipShape?
4. Are there custom CALayer subclasses or Core Graphics drawing?

## Instructions

### CRITICAL: Verification Requirements

- No off-screen rendering for cells in scrollable lists (check with Instruments Color Offscreen-Rendered)
- Shadow paths must be set explicitly — never rely on auto-calculated shadow paths
- Corner radius + clipsToBounds + shadow must not be on the same layer
- Blur effects in scrollable content must use rasterization or pre-rendered assets

### False-Positive Prevention

- ❌ Do NOT flag cornerRadius without clipsToBounds — this does not trigger off-screen rendering
- ✅ DO flag cornerRadius + clipsToBounds + shadow on the same layer
- ❌ Do NOT flag shadows on static, non-scrolling views — impact is negligible
- ✅ DO flag shadows without explicit shadowPath on any view in a scrollable container
- ❌ Do NOT flag `.compositingGroup()` in SwiftUI — this is often the fix, not the problem
- ✅ DO flag nested `.shadow()` modifiers that compound into multiple render passes

1. **Off-Screen Rendering Triggers**

```swift
// BAD: cornerRadius + masksToBounds forces off-screen render
let imageView = UIImageView()
imageView.layer.cornerRadius = 12
imageView.layer.masksToBounds = true // triggers off-screen rendering
imageView.layer.shadowColor = UIColor.black.cgColor
imageView.layer.shadowOffset = CGSize(width: 0, height: 2)
imageView.layer.shadowOpacity = 0.3
// shadow + clip = two off-screen passes per frame

// GOOD: Separate shadow and clipping layers
let containerView = UIView()
containerView.layer.shadowColor = UIColor.black.cgColor
containerView.layer.shadowOffset = CGSize(width: 0, height: 2)
containerView.layer.shadowOpacity = 0.3
containerView.layer.shadowPath = UIBezierPath(
    roundedRect: containerView.bounds, cornerRadius: 12
).cgPath // explicit path avoids recalculation

let imageView = UIImageView()
imageView.layer.cornerRadius = 12
imageView.layer.masksToBounds = true
containerView.addSubview(imageView)
```

2. **Shadow Path Optimization**

```swift
// BAD: Auto-calculated shadow path — recalculated every frame
view.layer.shadowColor = UIColor.black.cgColor
view.layer.shadowOpacity = 0.2
view.layer.shadowRadius = 4
// no shadowPath set — Core Animation traces view outline each frame

// GOOD: Explicit shadow path
view.layer.shadowPath = UIBezierPath(
    roundedRect: view.bounds, cornerRadius: view.layer.cornerRadius
).cgPath

// Update in layoutSubviews
override func layoutSubviews() {
    super.layoutSubviews()
    layer.shadowPath = UIBezierPath(roundedRect: bounds, cornerRadius: layer.cornerRadius).cgPath
}
```

3. **SwiftUI Shadow Patterns**

```swift
// BAD: Nested shadows multiply render passes
Text("Hello")
    .padding()
    .background(Color.white)
    .shadow(radius: 4) // shadow pass 1
    .padding()
    .background(Color.gray)
    .shadow(radius: 8) // shadow pass 2 — compounds

// GOOD: Single shadow on outermost container
Text("Hello")
    .padding()
    .background(Color.white)
    .cornerRadius(8)
    .padding()
    .background(
        RoundedRectangle(cornerRadius: 12)
            .fill(Color.gray)
            .shadow(radius: 8)
    )
```

4. **Rasterization for Complex Layers**

```swift
// BAD: Complex layer redrawn every frame during scroll
cell.layer.cornerRadius = 12
cell.layer.masksToBounds = true
cell.layer.borderWidth = 1
cell.layer.borderColor = UIColor.separator.cgColor
// All recomposited on each scroll frame

// GOOD: Rasterize static complex layers
cell.layer.shouldRasterize = true
cell.layer.rasterizationScale = UIScreen.main.scale
// Cached bitmap reused during scroll — update only on content change

// CAUTION: Only rasterize layers that don't change frequently
// Rasterizing animated layers is WORSE — forces re-rasterization each frame
```

## Expected Output

```
## Core Animation Hitch Review Report

### Summary
- **Layers/views reviewed:** N
- **Off-screen rendering triggers:** N
- **Missing shadow paths:** N
- **Compound shadow issues:** N
- **Rasterization candidates:** N
- **Estimated hitch severity:** Low/Medium/High

### Findings
#### [Severity] Issue — File:Line
- **Issue:** ...
- **Hitch type:** Commit hitch / Render hitch
- **Recommendation:** ...
```

## Example Output

```
## Core Animation Hitch Review Report

### Summary
- **Layers/views reviewed:** 12
- **Off-screen rendering triggers:** 3
- **Missing shadow paths:** 4
- **Compound shadow issues:** 1
- **Rasterization candidates:** 2
- **Estimated hitch severity:** High (in scroll contexts)

### Findings

#### [Critical] Off-Screen Render in List Cell — ProductCell.swift:L35
- **Issue:** `cornerRadius(12)` + `masksToBounds = true` + `shadow` on product image layer inside `UICollectionViewCell`.
- **Hitch type:** Render hitch — off-screen pass per visible cell per frame.
- **Recommendation:** Move shadow to container view with explicit shadowPath. Keep cornerRadius + clip on inner image view only.

#### [Warning] Missing Shadow Path — CardView.swift:L22
- **Issue:** Shadow applied without explicit `shadowPath`. 8 CardViews visible simultaneously in grid.
- **Recommendation:** Set `shadowPath` in `layoutSubviews()` using `UIBezierPath(roundedRect:cornerRadius:)`.
```

## Techniques Used

- **ST-01 (Structured Task Decomposition):** Separates off-screen, shadows, compositing, rasterization
- **RT-02 (Role-Based Task Framing):** Reviewer acts as Core Animation rendering expert
- **AG-02 (Automated Guardrails):** Prevents false flags on non-scrolling views and intentional compositing
- **AG-12 (Performance-Aware Review):** Focuses on per-frame rendering budget impact

## Related Prompts

- `ios_swiftui_view_update_review.md` — View body evaluation performance
- `ios_swiftui_list_performance_review.md` — List scrolling performance
- `ios_swiftui_uikit_interop_review.md` — Interop layer rendering issues

## Customization Guide

- **SwiftUI-only apps:** Focus on `.shadow()`, `.blur()`, `.clipShape()` modifier combinations
- **Games/media apps:** Add Metal/CAMetalLayer checks and display link synchronization
- **Accessibility:** Ensure rasterization respects Dynamic Type and does not cache at wrong text size
