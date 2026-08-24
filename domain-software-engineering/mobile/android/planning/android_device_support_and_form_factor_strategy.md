---
title: "Android Device Support & Form-Factor Strategy"
category: mobile-development
description: "Decide, at the start of a greenfield Android project, which API levels, devices, and form factors the app will support — producing a minSdk/targetSdk policy, a justified form-factor support matrix, an adaptive layout strategy, and the resulting test device/API matrix."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-06
  - CM-01
  - MP-09
difficulty: intermediate
tags:
  - android
  - form-factors
  - min-sdk
  - adaptive-layout
  - window-size-classes
  - foldables
  - mobile-development
updated: "2026-06-06"
related_prompts:
  - android_app_concept_validation.md
  - ../maintenance/android_min_sdk_raise_planner.md
  - ../improvement/android_adaptive_large_screen_improvement.md
  - ../testing/android_device_api_test_matrix_design.md
---

# Android Device Support & Form-Factor Strategy

**Objective:** At the start of a greenfield Android project, decide and document the device-support boundary — the minSdk/targetSdk/compileSdk policy, which form factors (phone, tablet, foldable, ChromeOS/large screen, Wear OS, Android TV, Android Auto/Automotive, XR) are in or out of scope and why, the adaptive/large-screen strategy expressed in window size classes and canonical layouts, the supported input modes, and the test device/API matrix these choices imply — so that architecture and navigation are built once for the right surface area instead of being retrofitted.

**When to Use:** Use this prompt immediately after the app concept is validated and before architecture and scaffolding. Form-factor scope is one of the cheapest decisions to make on paper and one of the most expensive to retrofit: an app that locks orientation and hardcodes single-pane navigation cannot be made adaptive without a navigation rewrite. Use it to set an explicit, defensible boundary instead of an accidental one (the default "phone-only portrait" that emerges from never deciding).

**Sequence Map:**
- **Before this:** [`android_app_concept_validation.md`](android_app_concept_validation.md) (validate the concept and audience)
- **This prompt:** Decide device + form-factor scope
- **After this:** [`android_architecture_selection.md`](android_architecture_selection.md) and [`android_project_scaffold.md`](android_project_scaffold.md) (build architecture/navigation for the chosen surface)
- **Later (raise the floor):** [`../maintenance/android_min_sdk_raise_planner.md`](../maintenance/android_min_sdk_raise_planner.md)
- **Later (adapt UI):** [`../improvement/android_adaptive_large_screen_improvement.md`](../improvement/android_adaptive_large_screen_improvement.md)
- **Feeds:** [`../testing/android_device_api_test_matrix_design.md`](../testing/android_device_api_test_matrix_design.md)

**Important context:** Two distinct decisions get confused here. **minSdk** is a *reach vs. cost* tradeoff — lower reaches more users but forces you to support older APIs and carry compatibility code; it changes which platform features you can use unconditionally. **Form factor** is a *product surface* decision — supporting tablets/foldables/large screens is mostly a UI/navigation cost, while Wear/TV/Auto/XR are effectively separate apps with their own UX, modules, and store tracks. The expensive mistake is treating "supports large screens" as a checkbox; it is an architecture commitment (window size classes + canonical layouts + no orientation lock) that must be made before navigation is built. The opposite mistake is over-scoping: greenlighting Wear + TV + Auto for a v1 that should ship phone + large screen first. This prompt forces both boundaries to be explicit and justified, sized to the actual audience.

---

## Context Gathering

1. **Audience and reach:**
   - "Who are the target users and where (geography, consumer vs. enterprise, BYOD vs. managed fleet)?"
   - "Is there an existing user base whose device/OS distribution you can pull (Play Console → Statistics, or analytics)?"
   - "Is there a hard institutional floor (e.g. an enterprise standardized on a specific OS version or device)?"

2. **Product surface and context of use:**
   - "Where is the app actually used — in hand, on a desk, on a couch, in a car, on a wrist?"
   - "Is large-screen / multitasking use a real workflow (side-by-side, drag-and-drop) or incidental?"
   - "Does the product have a credible Wear / TV / Auto / XR use case, or is that aspiration?"

3. **Feature and capability constraints:**
   - "Are there features that require a recent API (e.g. specific media, security, or system APIs) that would pull minSdk up?"
   - "Do you depend on libraries with their own minSdk floors (some Jetpack/Compose/third-party SDKs)?"

4. **Team capacity and maintenance:**
   - "How many engineers, and can they realistically test + maintain extra form factors and old API levels?"
   - "What is the release cadence, and can it absorb extra store tracks (Wear/TV/Auto are separate)?"

5. **Input and accessibility expectations:**
   - "Will users have keyboards/mice (ChromeOS, desktop mode), styluses, or d-pad/remote input?"
   - "Are there accessibility or regulatory requirements that imply specific input or layout support?"

---

## Instructions

### Phase 1: minSdk Decision (Reach vs. API vs. Maintenance)

Do not hardcode a number from memory. Frame the decision against *current* Play distribution data and the project's constraints.

1. **Pull live distribution data:** Use Android Studio's "Help me choose" dialog on the `minSdk` field (it shows current cumulative device reach per API level) or Play Console statistics for an existing app. Treat percentages as fetched-at-decision-time, not as constants in this document.
2. **Score the tradeoff** for two or three candidate floors:

| Candidate minSdk | Cumulative device reach* | API features unlocked unconditionally | Compatibility cost (code you must carry) |
|------------------|--------------------------|----------------------------------------|------------------------------------------|
| Lower floor | Higher reach | Fewer modern APIs without `if (SDK_INT >= …)` guards | More back-compat branches, more test devices, more bugs |
| Middle floor | Moderate reach | Most current Jetpack/Compose APIs available | Moderate; aligns with common library floors |
| Higher floor | Lower reach | Newest platform APIs unconditionally | Least back-compat code; smallest test matrix |

*Fill from the live "Help me choose" / Play data at decision time — do not copy a stale percentage.

3. **Decide and justify in one sentence**, e.g. "minSdk = the floor that retains ≥X% of our target-region devices while letting us use [required API] without guards, set via the version catalog."

**CHECKPOINT 1:** The minSdk justification must reference *actual current* reach data and at least one concrete API or library constraint — not "everyone uses a recent version."

### Phase 2: targetSdk / compileSdk Policy

| Setting | Policy | Rationale |
|---------|--------|-----------|
| **compileSdk** | Always the latest stable SDK (via the version catalog) | Lets you compile against and adopt the newest APIs and lint checks |
| **targetSdk** | Latest stable, raised promptly each year | Opting into the latest behavior changes is required; Google Play enforces a recent target API level for new apps and updates, so staying current avoids being blocked |
| **AGP / Kotlin / Compose** | Latest stable via the version catalog (Kotlin 2.1+, current Compose BOM, AGP 8.7+) | Keep a single source of truth in `libs.versions.toml`; no version pins scattered in module build files |

State the standing rule: "compileSdk and targetSdk track the latest stable release; raising targetSdk is a planned annual task" — and link the target-SDK migration work to [`../maintenance/android_target_sdk_migration.md`](../maintenance/android_target_sdk_migration.md) when the time comes.

### Phase 3: Form-Factor Support Matrix

Decide each form factor explicitly: in scope, out of scope (this version), or future. Record *why* and the incremental cost — costs differ by an order of magnitude across these.

| Form factor | Decision | Why | Incremental cost |
|-------------|----------|-----|------------------|
| **Phone (portrait + landscape)** | In | Baseline | Baseline |
| **Tablet / large screen** | In / Future | Real desk/multitask use? | Adaptive layouts + test devices (same codebase) |
| **Foldable (folded + unfolded, posture)** | In / Future | Subset of large-screen; resize + fold posture | Continuity across fold, hinge-aware layout |
| **ChromeOS / desktop windowing** | In / Future | Keyboard+mouse, free-form resizable windows | Free-form resize, pointer/keyboard support, no orientation lock |
| **Wear OS** | Out / Future | Glanceable wrist use case? | **Separate app** (Compose for Wear, own UX, own store track) |
| **Android TV** | Out / Future | Lean-back, 10-ft UI? | **Separate app** (Leanback/TV Compose, d-pad nav, own track) |
| **Android Auto / Automotive OS** | Out / Future | Driving/in-car use? | **Separate app** + strict driver-distraction templates |
| **Android XR** | Out / Future | Spatial/immersive use? | Emerging surface; spatial UI; treat as separate target |

**Decision rules:**
- Phone + large-screen family (tablet, foldable, ChromeOS) **share one codebase** — the cost is adaptive layout discipline, not a second app.
- Wear / TV / Auto / XR are **effectively separate apps** (distinct UX paradigms, modules, and Play tracks) — only greenlight one with a validated use case and team capacity.
- Default a typical v1 to **phone + large screen**; defer Wear/TV/Auto/XR unless the concept centers on them.

**CHECKPOINT 2:** Every form factor has an explicit In/Out/Future decision with a one-line reason. "Phone-only portrait" must be a *chosen* default, never an accidental one.

### Phase 4: Large-Screen / Adaptive Strategy (for every in-scope large screen)

If anything beyond phone-portrait is in scope, commit to the adaptive primitives now — they are architectural.

1. **Window size classes** — drive layout off `WindowSizeClass` (Compact / Medium / Expanded width and height), never off a hardcoded "is tablet" boolean or screen-size resource buckets alone:

```kotlin
val windowSizeClass = currentWindowAdaptiveInfo().windowSizeClass
when (windowSizeClass.windowWidthSizeClass) {
    WindowWidthSizeClass.COMPACT  -> SinglePaneLayout()   // phone
    WindowWidthSizeClass.MEDIUM   -> /* list-detail or rail */ ListDetailLayout()
    WindowWidthSizeClass.EXPANDED -> ListDetailLayout(showBoth = true) // tablet/unfolded
}
```

2. **Canonical layouts** — pick the right adaptive pattern per screen and prefer the Material adaptive components (`NavigableListDetailPaneScaffold`, `SupportingPaneScaffold`):

| Canonical layout | Use for | Compact behavior | Expanded behavior |
|------------------|---------|------------------|-------------------|
| **List-Detail** | Browsable collection + item view | List, then navigate to detail | List + detail side by side |
| **Feed** | Card/grid content | 1 column | Multi-column responsive grid |
| **Supporting Pane** | Primary content + secondary info | Stacked / sheet | Side supporting pane |

3. **Adaptive navigation** — bottom bar (Compact) → navigation rail (Medium) → navigation drawer (Expanded), via `NavigationSuiteScaffold`. Navigation must not assume a single pane.

4. **Resizability & orientation — hard rules:**
   - **No orientation lock** (`screenOrientation` stays unspecified/`fullSensor`); locking breaks foldables, tablets, and desktop windows.
   - **No `resizeableActivity="false"`**; the app must survive free-form resize and multi-window.
   - **Preserve state across configuration changes and resize** (hoist state / `rememberSaveable` / ViewModel; never rely on the activity not being recreated).

**CHECKPOINT 3:** If any large screen is in scope, the design must use window size classes + a named canonical layout per screen + no orientation lock. A "supports tablets" claim with a portrait-locked, single-pane, non-resizable app is a false positive.

### Phase 5: Input Modes

Map supported input to in-scope form factors; each implies concrete work.

| Input mode | Implied by | What it requires |
|------------|-----------|------------------|
| **Touch** | All | Baseline; adequate touch targets |
| **Keyboard** | ChromeOS, foldables w/ keyboard, accessibility | Tab order, keyboard shortcuts, focus traversal |
| **Mouse / trackpad (pointer)** | ChromeOS, desktop mode | Hover states, right-click/context, pointer icons |
| **Stylus** | Tablets, some foldables | Pressure/precision where relevant (notes/draw apps) |
| **D-pad / remote** | Android TV | Focus-based navigation, visible focus, no touch-only flows |
| **Rotary / crown** | Wear OS | Rotary scrolling support |

Record which modes are in scope and the resulting requirements (e.g. "ChromeOS in scope → keyboard focus traversal + pointer hover states required").

### Phase 6: Resulting Test Device / API Matrix

The decisions above determine what must be tested. Produce the matrix; it feeds [`../testing/android_device_api_test_matrix_design.md`](../testing/android_device_api_test_matrix_design.md).

| Dimension | In-scope values (from above) | Tested via |
|-----------|------------------------------|-----------|
| **API level** | minSdk, a mid level, latest | Emulators + a couple of physical devices |
| **Width size class** | Compact, Medium, Expanded (if large screen in scope) | Resizable emulator / foldable emulator / physical tablet |
| **Fold posture** | Folded, unfolded, half-open (if foldable in scope) | Foldable emulator |
| **Orientation** | Portrait + landscape (since no lock) | Rotation + resize tests |
| **Input** | Touch (+ keyboard/pointer/d-pad as scoped) | Instrumented + manual |
| **Separate-app targets** | Wear/TV/Auto/XR only if in scope | Their own device profiles |

### Phase 7: How the Decision Feeds Architecture & Navigation

State the downstream commitments so [`android_architecture_selection.md`](android_architecture_selection.md) and [`android_project_scaffold.md`](android_project_scaffold.md) inherit them:

- **Navigation** must be adaptive (single source of truth for routes; pane-aware) — not hardcoded single-pane.
- **State** must survive configuration changes and resize (ViewModel + saved state).
- **Modularization** must account for separate-app targets if Wear/TV/Auto/XR are Future (e.g. a shared `:core` reused by a future `:wear` app).
- **Theming/resources** must provide large-screen and orientation resources, not just defaults.

---

## Expected Output

1. **minSdk Decision** — chosen floor, the live reach data it was based on, and the API/library constraint that justifies it.
2. **targetSdk / compileSdk Policy** — the always-latest standing rule and version-catalog convention.
3. **Form-Factor Support Matrix** — In/Out/Future per form factor with reason and incremental cost.
4. **Adaptive Strategy** — window-size-class plan, canonical layout per screen, adaptive navigation, and the no-lock/resizable rules (for in-scope large screens).
5. **Input Mode Plan** — supported inputs and their requirements.
6. **Test Device / API Matrix** — the concrete matrix implied by the above.
7. **Downstream Commitments** — how the decision constrains architecture, navigation, state, modularization, and resources.

---

## CRITICAL: Verification Requirements

- [ ] minSdk is justified against current Play/Studio distribution data (not a remembered percentage) plus a concrete API/library constraint
- [ ] compileSdk and targetSdk are set to latest stable with a stated annual-raise policy
- [ ] All versions are governed by the version catalog (`libs.versions.toml`), not scattered pins
- [ ] Every form factor has an explicit In/Out/Future decision with a reason
- [ ] Phone + large-screen family are treated as one codebase; Wear/TV/Auto/XR are treated as separate apps
- [ ] If any large screen is in scope: window size classes are used (not an "isTablet" boolean), a canonical layout is named per screen, navigation is adaptive
- [ ] No orientation lock and no `resizeableActivity="false"`; state survives configuration change and resize
- [ ] Input modes are mapped to in-scope form factors with their requirements
- [ ] A test device/API matrix is produced and matches the scope decisions
- [ ] Scope is sized to audience and team capacity (no aspirational Wear/TV/Auto/XR without a validated use case)

---

## False-Positive Prevention

- ❌ "Set minSdk to a recent version — almost everyone is up to date." → ✅ Pull live distribution data at decision time and weigh reach against the specific APIs/libraries you need; the right floor depends on your target region and feature set, not a vibe.
- ❌ "We support tablets" (while the app is portrait-locked, single-pane, non-resizable). → ✅ Large-screen support means window size classes + a canonical adaptive layout + no orientation lock + resizable; a checkbox without these is a false claim.
- ❌ "Let's also do Wear, TV, and Auto in v1." → ✅ Those are separate apps with separate UX, modules, and store tracks; greenlight one only with a validated use case and capacity. Default v1 to phone + large screen.
- ❌ "Use screen-size resource buckets / an isTablet boolean to branch layouts." → ✅ Drive layout off `WindowSizeClass`, which also handles foldables, multi-window, and free-form desktop resizing that static buckets miss.
- ❌ "Lock orientation to portrait to simplify layout." → ✅ Never lock orientation; it breaks foldables, tablets, and ChromeOS windows and signals a non-adaptive architecture. Solve layout with adaptive composables instead.
- ❌ "Pin AGP/Kotlin/Compose versions in each module's build file." → ✅ Centralize in the version catalog and track latest stable; scattered pins drift and break the build matrix.
- ❌ "Phone-only portrait is fine" (never actually decided). → ✅ Make phone-only an explicit, justified choice tied to audience and capacity — not an accidental default from skipping the decision.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Opens with an explicit objective bounding the device/form-factor decision and its deliverables.
- **ST-02 (Structured Sequential Instructions):** Seven ordered phases from minSdk through downstream architecture commitments.
- **RT-02 (Multi-Dimensional Analysis Framework):** minSdk and each form factor are scored across multiple axes (reach, API availability, maintenance cost, product fit, capacity) rather than a single criterion.
- **DS-06 (Prioritization and Severity Guidance):** CHECKPOINT gates force the load-bearing decisions (minSdk justification, explicit per-form-factor scope, adaptive primitives) before downstream work proceeds.
- **CM-01 (Explicit Context Framing):** The "Important context" section disentangles the minSdk (reach/cost) decision from the form-factor (product surface) decision before any choices are made.
- **MP-09 (Human Clarity Before AI):** Context Gathering forces the team to clarify audience, usage context, and capacity up front, so scope is set deliberately rather than defaulting.

## Related Prompts

- [`android_app_concept_validation.md`](android_app_concept_validation.md) — validate the concept/audience that this scope decision depends on (run first)
- [`android_architecture_selection.md`](android_architecture_selection.md) — choose architecture for the surface area decided here (run next)
- [`android_project_scaffold.md`](android_project_scaffold.md) — scaffold the project with the chosen minSdk/targetSdk and adaptive setup
- [`../maintenance/android_min_sdk_raise_planner.md`](../maintenance/android_min_sdk_raise_planner.md) — later, plan raising the minSdk floor
- [`../improvement/android_adaptive_large_screen_improvement.md`](../improvement/android_adaptive_large_screen_improvement.md) — later, retrofit/improve adaptive large-screen support
- [`../testing/android_device_api_test_matrix_design.md`](../testing/android_device_api_test_matrix_design.md) — turn the resulting matrix into a concrete test plan
