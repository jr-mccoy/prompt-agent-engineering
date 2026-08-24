---
title: "Android Adaptive & Large-Screen Improvement"
category: mobile-development
description: "Adapt a phone-only Android app for tablets and foldables — WindowSizeClass-driven layouts, Material 3 adaptive scaffolds (list-detail, supporting pane, navigation suite), foldable posture, and removal of orientation/resize restrictions — verified against Play large-screen quality guidelines."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
  - QA-01
difficulty: advanced
tags:
  - android
  - mobile-development
  - large-screen
  - foldable
  - adaptive-layout
  - compose
updated: "2026-06-06"
related_prompts:
  - domain-software-engineering/mobile/android/improvement/android_edge_to_edge_predictive_back_adoption.md
  - domain-software-engineering/mobile/android/improvement/android_compose_ui_improvement.md
  - domain-software-engineering/mobile/android/planning/android_offline_first_architecture.md
  - domain-software-engineering/mobile/android/testing/android_screenshot_testing.md
---

# Android Adaptive & Large-Screen Improvement

**Objective:** Adapt an existing phone-only Android app so it is genuinely usable on tablets, foldables, desktop windows, and split-screen — driving layout from `WindowSizeClass`, adopting Material 3 adaptive scaffolds (list-detail / supporting pane / navigation suite), handling foldable posture, and removing orientation/resizeability restrictions — measured against the Play Store large-screen quality tiers.

## When to Use

- Use when: The app "works" on a tablet but is a stretched phone UI — single column, bottom nav at 1000dp wide, wasted space.
- Use when: The app locks orientation or sets `resizeableActivity="false"` and is downgraded on large-screen devices (and ignored on Android 16+ large screens).
- Use when: You want list-detail / supporting-pane layouts that collapse gracefully to phones and foldables.
- **Don't use when:** The task is purely system-bar/back behavior — use `android_edge_to_edge_predictive_back_adoption.md`.
- **Don't use when:** You are doing a from-scratch visual redesign — use `android_compose_ui_improvement.md`.

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Test on actual large-screen configurations.** Use a foldable + tablet emulator (or resizable emulator) and split-screen — not just a phone. A finding must be reproduced at a real breakpoint.
2. **Read layout decisions, don't assume.** Confirm whether the app already keys off `WindowSizeClass`/`currentWindowAdaptiveInfo()` before flagging "no adaptivity."
3. **Separate three distinct problems:** (a) restrictions that block large screens (orientation/resize locks), (b) layouts that don't reflow, (c) interaction gaps (keyboard/mouse, drag-drop). Fixes differ.
4. **Check state survival across configuration changes** — resizing/unfolding triggers recreation; verify `rememberSaveable`/ViewModel retention so the detail pane and scroll position survive.
5. **Provide `File:line` evidence** for every finding.

**Finding the app is ALREADY adaptive is an acceptable outcome.** If it keys off size classes and reflows correctly, say so.

### False-Positive Prevention

- ❌ Do NOT recommend separate `layout-sw600dp` resource forks for a Compose app — drive it from `WindowSizeClass` in one tree.
- ❌ Do NOT hardcode "tablet = two panes" — base it on available width (`WindowWidthSizeClass`), not device type.
- ❌ Do NOT remove orientation locks for genuinely fixed-orientation experiences (e.g., a camera viewfinder) without flagging the tradeoff.
- ❌ Do NOT widen content to full bleed at 1200dp — cap content width / use margins for readable line length.
- ✅ DO collapse adaptive scaffolds back to single-pane on compact width and folded postures.
- ✅ DO preserve selection/scroll state across fold/resize.
- ✅ DO verify keyboard, mouse, and stylus input on large screens.

---

### Phase 1: Audit

| Check | Where | Finding |
|-------|-------|---------|
| `screenOrientation` locks | `AndroidManifest.xml` | [activities] |
| `resizeableActivity="false"` | `AndroidManifest.xml` | [present?] |
| Max-aspect-ratio / fixed sizing | manifest / theme | [present?] |
| Uses `WindowSizeClass` / `currentWindowAdaptiveInfo()` | Compose entry points | [yes/no] |
| Single-column screens that could be list-detail | feature screens | [list] |
| Navigation type fixed (bottom bar always) | scaffold | [yes/no] |
| Content width unbounded at large widths | screens | [list] |
| State survives config change | ViewModels / saveable | [gaps] |
| Foldable posture awareness | `WindowInfoTracker` usage | [yes/no] |
| Keyboard/mouse/drag-drop support | input handling | [gaps] |

Map each top screen to a **canonical layout** target: *list-detail*, *supporting pane*, *feed*, or *single* (no change).

---

### Phase 2: Remove Restrictions

- Remove `android:screenOrientation` locks and `resizeableActivity="false"` unless a hard product reason exists (flag the tradeoff). Note: Android 16 ignores orientation/resize restrictions on screens ≥ ~600dp for most apps — relying on them is a dead end.
- Ensure activities handle resize/unfold without losing state (prefer letting the system recreate + restore via `rememberSaveable`/ViewModel over broad `configChanges` overrides).

---

### Phase 3: Adaptive Layout

1. **Drive layout from window size:**
   ```kotlin
   val adaptiveInfo = currentWindowAdaptiveInfo()
   val widthClass = adaptiveInfo.windowSizeClass.windowWidthSizeClass
   // Compact → single pane; Medium/Expanded → two panes
   ```

2. **Adaptive navigation** (bottom bar → rail → drawer by width):
   ```kotlin
   NavigationSuiteScaffold(   // androidx.compose.material3.adaptive.navigationsuite
       navigationSuiteItems = { /* destinations */ }
   ) { CurrentDestination() }
   ```

3. **Canonical panes** that auto-collapse on compact/folded:
   ```kotlin
   val navigator = rememberListDetailPaneScaffoldNavigator<ItemId>()
   ListDetailPaneScaffold(                 // androidx.compose.material3.adaptive.layout
       directive = navigator.scaffoldDirective,
       value = navigator.scaffoldValue,
       listPane = { ItemList(onClick = { navigator.navigateTo(ListDetailPaneScaffoldRole.Detail, it) }) },
       detailPane = { navigator.currentDestination?.contentKey?.let { ItemDetail(it) } },
   )
   // Back integrates with the navigator so it pops the detail pane first.
   ```
   Use `SupportingPaneScaffold` for primary + supporting (e.g., editor + tools).

4. **Readable bounds:** cap content width (e.g., `widthIn(max = 840.dp)` centered) or use responsive margins so text lines don't span a 1200dp display.

5. **Foldables:** observe posture via `WindowInfoTracker.windowLayoutInfo` (or the adaptive info's `Posture`) and avoid placing interactive content across the hinge; in book/tabletop posture, route panes around the fold.

---

### Phase 4: Large-Screen Interaction

- Keyboard: support Tab focus traversal and common shortcuts.
- Pointer: hover states, right-click context where relevant, correct cursor.
- Drag-and-drop and external displays where the app's content warrants it.
- Camera/media: handle letterboxing and sensor orientation on tablets.

---

### Phase 5: Verify

Run against the Play large-screen quality expectations and a screenshot suite (see `../testing/android_screenshot_testing.md`):

| Configuration | Reflows correctly | State survives | No wasted space | Input OK |
|---------------|-------------------|----------------|-----------------|----------|
| Phone (compact) | [ ] | [ ] | [ ] | [ ] |
| Foldable folded | [ ] | [ ] | [ ] | [ ] |
| Foldable unfolded | [ ] | [ ] | [ ] | [ ] |
| Tablet portrait | [ ] | [ ] | [ ] | [ ] |
| Tablet landscape | [ ] | [ ] | [ ] | [ ] |
| Split-screen / freeform | [ ] | [ ] | [ ] | [ ] |

---

## Expected Output

1. **Audit** — restrictions, current adaptivity, per-screen canonical-layout targets.
2. **Restriction-removal plan + diffs** — orientation/resize locks, with tradeoffs flagged.
3. **Adaptive layout plan + diffs** — size-class routing, navigation suite, pane scaffolds, content bounds.
4. **Interaction gaps + fixes** — keyboard/mouse/drag-drop.
5. **Verification matrix** — across the configuration set, plus screenshot-test coverage.

---

## CRITICAL: Verification Checklist (self-audit before reporting)

- [ ] Findings reproduced at real large-screen breakpoints, not assumed
- [ ] Adaptivity keyed off available width, not device-type detection
- [ ] No resource-fork (`layout-sw600dp`) recommendation for a Compose tree
- [ ] State survival across fold/resize verified
- [ ] Orientation/resize-lock removals flag any genuine tradeoff
- [ ] Content width bounded for readability on the widest target
- [ ] Adaptive scaffolds collapse correctly to compact and folded postures

---

## Related Prompts

- [android_edge_to_edge_predictive_back_adoption.md](android_edge_to_edge_predictive_back_adoption.md) - System bars / insets / predictive back
- [android_compose_ui_improvement.md](android_compose_ui_improvement.md) - Broader UI redesign consultation
- [android_offline_first_architecture.md](../planning/android_offline_first_architecture.md) - State architecture that survives recreation
- [android_screenshot_testing.md](../testing/android_screenshot_testing.md) - Lock multi-size layouts with screenshot tests
