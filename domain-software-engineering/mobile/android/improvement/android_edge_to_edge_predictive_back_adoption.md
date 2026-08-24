---
title: "Android Edge-to-Edge & Predictive Back Adoption"
category: mobile-development
description: "Migrate an existing app to enforced edge-to-edge (Android 15 / SDK 35), correct window-inset handling, and predictive back gestures — including the deprecated status/navigation-bar APIs and Compose/View back handling."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - CM-01
  - QA-01
difficulty: intermediate
tags:
  - android
  - mobile-development
  - edge-to-edge
  - window-insets
  - predictive-back
updated: "2026-06-06"
related_prompts:
  - domain-software-engineering/mobile/android/improvement/android_adaptive_large_screen_improvement.md
  - domain-software-engineering/mobile/android/improvement/android_code_modernization.md
  - domain-software-engineering/mobile/android/maintenance/android_target_sdk_migration.md
  - domain-software-engineering/mobile/android/improvement/android_compose_ui_polish.md
---

# Android Edge-to-Edge & Predictive Back Adoption

**Objective:** Migrate an existing Android app to **enforced edge-to-edge** display and **predictive back** gestures — drawing behind the system bars with correct `WindowInsets` handling, replacing deprecated status/navigation-bar color APIs, and adopting the back-invoked callback model in both Compose and Views — without clipping content, double-padding, or breaking back navigation.

## When to Use

- Use when: The app targets (or is moving to) SDK 35+ (Android 15), where edge-to-edge is enforced for apps targeting 35 and the legacy status/nav-bar color APIs are deprecated.
- Use when: Content is hidden behind the status bar, gesture nav pill, or IME after enabling edge-to-edge; or back gestures show no predictive animation.
- Use when: The app still uses `Activity.onBackPressed()` or `setOnKeyListener` for back handling.
- **Don't use when:** The task is broad SDK migration — use `../maintenance/android_target_sdk_migration.md` (run this prompt as the UI-facing part of it).
- **Don't use when:** The task is tablet/foldable adaptation — use `android_adaptive_large_screen_improvement.md`.

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Confirm the target SDK and current state.** Edge-to-edge behavior differs by `targetSdk`. Check `targetSdk`, whether `enableEdgeToEdge()` is already called, and whether `decorFitsSystemWindows` is set.
2. **Distinguish "not yet edge-to-edge" from "edge-to-edge but mis-padded."** The fixes differ: the first needs `enableEdgeToEdge()`; the second needs correct inset consumption (and removal of double padding).
3. **Trace each inset consumer.** A `Scaffold` already applies insets to its content lambda — adding `systemBarsPadding()` on top double-pads. Identify exactly where insets are (or should be) consumed.
4. **Verify back handling per surface.** Predictive back needs the manifest opt-in AND back logic expressed through `OnBackPressedCallback` / `PredictiveBackHandler` / the `OnBackInvokedDispatcher` — not `onBackPressed()`.
5. **Provide `File:line` evidence** for every finding.

**Finding the app is ALREADY correctly edge-to-edge with predictive back is an acceptable outcome.** Say so if true; do not invent inset bugs.

### False-Positive Prevention

- ❌ Do NOT add `systemBarsPadding()`/`safeDrawingPadding()` to content already inside a `Scaffold` that handles insets — that double-pads.
- ❌ Do NOT set a hardcoded status-bar color via the deprecated APIs to "fix" edge-to-edge — that fights the platform.
- ❌ Do NOT apply `imePadding()` globally; apply it only to the surface that must move with the keyboard.
- ❌ Do NOT enable predictive back in the manifest without migrating `onBackPressed()` — the gesture will look broken.
- ✅ DO consume insets once, at the right level (`Scaffold` content padding, or explicit `windowInsetsPadding`).
- ✅ DO test with both 3-button and gesture navigation, and in light/dark.
- ✅ DO verify the IME and rotation cases.

---

### Phase 1: Audit Current State

| Check | Where | Finding |
|-------|-------|---------|
| `targetSdk` value | `build.gradle.kts` | [n] |
| `enableEdgeToEdge()` called | Activity `onCreate` | [yes/no] |
| `setDecorFitsSystemWindows` usage | Activity / theme | [yes/no] |
| Deprecated `window.statusBarColor` / `navigationBarColor` | Activity / theme | [locations] |
| Inset handling | Scaffolds, custom layouts | [consumed where] |
| Hardcoded top/bottom padding compensating for bars | Composables / XML | [locations] |
| Back handling | `onBackPressed()`, callbacks | [locations] |
| Predictive back opt-in | `AndroidManifest.xml` | [present?] |

---

### Phase 2: Edge-to-Edge

1. **Opt in once per Activity:**
   ```kotlin
   override fun onCreate(savedInstanceState: Bundle?) {
       enableEdgeToEdge()   // androidx.activity; sets transparent bars + decorFitsSystemWindows=false
       super.onCreate(savedInstanceState)
       setContent { AppTheme { /* ... */ } }
   }
   ```

2. **Consume insets correctly (Compose):**
   ```kotlin
   // Scaffold already provides insets via its content padding — use it, don't re-pad.
   Scaffold { innerPadding ->
       Content(Modifier.padding(innerPadding))
   }

   // Full-bleed surface that still keeps interactive content clear of bars:
   Box(Modifier.fillMaxSize()) {
       BackgroundImage(Modifier.fillMaxSize())                 // draws edge to edge
       Column(Modifier.safeDrawingPadding()) { /* controls */ } // padded off bars + IME
   }

   // Keyboard-aware input row only:
   TextField(..., modifier = Modifier.imePadding())
   ```
   Use the specific inset that matches intent: `statusBars`, `navigationBars`, `systemBars`, `safeDrawing` (bars + IME + cutout), `ime`.

3. **Replace deprecated bar-color APIs.** Remove `window.statusBarColor` / `navigationBarColor` (deprecated in SDK 35). Control bar-icon contrast via `enableEdgeToEdge(statusBarStyle = ...)` or `WindowInsetsControllerCompat.isAppearanceLightStatusBars`. Let content show through the bars.

4. **Views/XML surfaces:** apply `ViewCompat.setOnApplyWindowInsetsListener` and pad with `getInsets(WindowInsetsCompat.Type.systemBars())`; remove `fitsSystemWindows="true"` workarounds that conflict.

---

### Phase 3: Predictive Back

1. **Opt in (manifest):**
   ```xml
   <application android:enableOnBackInvokedCallback="true" ... >
   ```

2. **Migrate back logic off `onBackPressed()`:**
   ```kotlin
   // View / Activity:
   onBackPressedDispatcher.addCallback(this, object : OnBackPressedCallback(enabled = true) {
       override fun handleOnBackPressed() { /* handle */ }
   })
   ```
   ```kotlin
   // Compose — non-predictive:
   BackHandler(enabled = canHandle) { onBack() }

   // Compose — predictive (animate with gesture progress):
   PredictiveBackHandler(enabled = canHandle) { progress ->
       try {
           progress.collect { backEvent -> animateTo(backEvent.progress) }
           onBack()                 // committed
       } catch (e: CancellationException) {
           animateBackToRest()      // cancelled
       }
   }
   ```

3. **Compose Navigation:** confirm a Navigation version with predictive-back support so screen transitions animate during the gesture; verify nested nav graphs and bottom sheets respond.

---

### Phase 4: Verify on Device

Test matrix — each must be free of clipped content and broken back:

| Case | Gesture nav | 3-button nav |
|------|-------------|--------------|
| Top content clear of status bar | [ ] | [ ] |
| Bottom content clear of nav pill/bar | [ ] | [ ] |
| IME pushes the right surface only | [ ] | [ ] |
| Landscape / cutout (notch) | [ ] | [ ] |
| Light & dark bar-icon contrast | [ ] | [ ] |
| Predictive back animates from a screen | [ ] | n/a |
| Back exits/navigates correctly | [ ] | [ ] |

---

## Expected Output

1. **Current-state audit** — target SDK, edge-to-edge status, inset consumers, back handling.
2. **Edge-to-edge plan + diffs** — `enableEdgeToEdge()`, inset fixes, deprecated-API removals.
3. **Predictive back plan + diffs** — manifest opt-in and callback/`PredictiveBackHandler` migration.
4. **Double-padding removals** — hardcoded bar compensation deleted.
5. **Device verification matrix** — completed across nav modes and orientations.

---

## CRITICAL: Verification Checklist (self-audit before reporting)

- [ ] Distinguished "not edge-to-edge" from "edge-to-edge but mis-padded"
- [ ] No double-padding introduced over Scaffold-provided insets
- [ ] Deprecated `statusBarColor`/`navigationBarColor` usages removed, not re-added
- [ ] Predictive back manifest flag is paired with `onBackPressed()` migration
- [ ] Verified with both gesture and 3-button navigation
- [ ] IME, rotation, and display-cutout cases checked

---

## Related Prompts

- [android_adaptive_large_screen_improvement.md](android_adaptive_large_screen_improvement.md) - Tablet/foldable adaptive layouts
- [android_target_sdk_migration.md](../maintenance/android_target_sdk_migration.md) - Full target-SDK migration (this is its UI part)
- [android_code_modernization.md](android_code_modernization.md) - Replace other deprecated APIs
- [android_compose_ui_polish.md](android_compose_ui_polish.md) - Visual polish after the layout is correct
