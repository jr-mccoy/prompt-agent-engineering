---
title: "Android Navigation & Screen Map"
category: mobile-development
description: "Produce an Android app's information architecture before any screen is built — a full screen inventory, a top-level navigation pattern decision, an adaptive (large-screen/foldable) plan, a Navigation Compose type-safe route map, a back-stack/predictive-back plan, and a deep-link/App-Links strategy."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-03
  - DS-06
  - NE-02
difficulty: intermediate
tags:
  - android
  - mobile-development
  - navigation
  - jetpack-compose
  - information-architecture
  - deep-linking
updated: "2026-06-06"
related_prompts:
  - android_architecture_selection.md
  - android_feature_specification.md
  - ../implementation/android_navigation_implementation.md
  - ../analysis/android_navigation_deeplink_analysis.md
---

# Android Navigation & Screen Map

**Objective:** Plan the complete information architecture of an Android app before a single screen is implemented — enumerate every destination, choose the top-level navigation pattern with explicit selection criteria, design adaptive navigation for tablets and foldables, define a type-safe Navigation Compose route map (serializable route objects), plan the back stack / predictive back / up-vs-back behavior, and lock a deep-link & App Links strategy — producing a navigation graph that implementation can build against without redesign.

**When to Use:** Use this prompt right after you know your screens and your architecture but before you wire any `NavHost`. Ideal when an app has grown past 3–4 screens, when you're adding a second top-level area (e.g., adding a "Profile" tab to a single-flow app), when you need deep links / App Links, or when you're targeting tablets and foldables and the phone-only nav no longer fits. Retrofitting navigation after screens are built is one of the most expensive Android refactors — plan it once, here.

**Sequence Map:** Use after [android_architecture_selection.md](android_architecture_selection.md) (you need the layering decided so routes map cleanly to ViewModels); use before [../implementation/android_navigation_implementation.md](../implementation/android_navigation_implementation.md) (which builds the `NavHost` and typed routes from this map). Feeds and is fed by [android_feature_specification.md](android_feature_specification.md).

**Important context:** Navigation is the skeleton the whole UI hangs on, and it is the single hardest thing to change late because every screen, every deep link, every test, and every analytics event references routes. The most common failure mode is *emergent* navigation — screens get bolted on one at a time, a `String`-keyed `NavHost` accumulates `"detail/{id}?tab={tab}"` routes with hand-parsed arguments, and six months later nobody can answer "what are all the screens and how do you reach each one?" The second failure mode is the opposite: over-architecting a 5-screen utility app with nested graphs, an adaptive `NavigationSuiteScaffold`, and deep links nobody will ever fire. The goal is a navigation graph that is *complete on paper*, *type-safe in code*, and *no more complex than the app's actual surface area*.

---

## Context Gathering

Ask these before drawing anything. Do not assume a pattern.

1. **App surface area:**
   - "List every screen you can think of, even roughly. Don't filter — we'll structure them."
   - "Of those, which are 'top-level' (a user could reasonably start their session there) vs. 'detail/sub' screens reached from somewhere else?"
   - "Are there modal surfaces (bottom sheets, dialogs, full-screen takeovers like onboarding/paywall) as opposed to normal back-stack destinations?"

2. **Entry & gating:**
   - "Does the app require sign-in? Is it auth-required, auth-optional (browse then sign in to act), or fully public?"
   - "Which screens are reachable while signed out, and which require auth?"
   - "Is there a first-run flow (onboarding, permission priming, account setup) that runs once?"

3. **Form factor & reach:**
   - "Phone only, or do you support tablets / foldables / ChromeOS / large screens?"
   - "Is there a list→detail relationship that would benefit from a side-by-side (list-detail) layout on wide screens?"

4. **Deep linking & external entry:**
   - "Do you need to open specific screens from notifications, widgets, other apps, the web (App Links), or marketing links?"
   - "Which destinations carry parameters (an item id, a tab, a filter)?"
   - "Do you own a web domain you can verify for Android App Links (verified `https://` links that open the app directly)?"

5. **Constraints & scale:**
   - "Single-module or multi-module? (Feature modules change how routes are declared and shared.)"
   - "Roughly how many destinations total — under 10, 10–25, or more? (Drives whether nested graphs earn their keep.)"

---

## Instructions

### Phase 1: Screen / Destination Inventory

Build the master inventory. Classify every destination so the navigation pattern almost chooses itself. Modal surfaces (sheets/dialogs) are tracked but are **not** back-stack destinations unless they own a route.

| Screen / Destination | Type | Reached From | Auth | Params | Form-Factor Note |
|---|---|---|---|---|---|
| Home / Feed | Top-level | Launch, bottom nav | Public | — | List on wide screens |
| Search | Top-level | Bottom nav | Public | `query?` | — |
| Item Detail | Detail | Home, Search, deep link | Public | `itemId` | Detail pane on wide screens |
| Profile | Top-level | Bottom nav | Required | — | — |
| Settings | Sub | Profile → gear | Required | — | — |
| Sign In | Modal/flow | Gated action, Profile | Public | `returnTo?` | Full-screen |
| Onboarding | One-time flow | First launch | Public | — | Full-screen, no nav bar |
| Paywall | Modal | Gated feature | Required | `source` | Bottom sheet or full-screen |

**Type legend:** *Top-level* = appears in the primary nav surface; *Detail* = pushed onto the back stack; *Sub* = nested under a top-level area; *Modal/flow* = sheet, dialog, or full-screen takeover that does not belong in the tab bar.

**CHECKPOINT 1 — Inventory review (discuss before designing):** Present the filled inventory and confirm with the user: *How many true top-level destinations are there?* That count is the primary input to the next decision. If there are 0–1 top-level destinations, there may be no top-level nav pattern at all (single flow). Do **not** proceed to pattern selection until the top-level count is agreed.

---

### Phase 2: Top-Level Navigation Pattern

Choose the primary navigation surface from the top-level count and the app's nature. Pick **one** primary pattern; combine only deliberately.

| Pattern | Best when | Top-level dests | Wide-screen role | Avoid when |
|---|---|---|---|---|
| **No top-level nav (single flow)** | Linear or single-purpose app | 0–1 | N/A | App has multiple peer areas |
| **Bottom navigation bar** | Few peer areas, frequent switching | 3–5 | Becomes navigation rail | >5 areas; rarely-switched areas |
| **Navigation rail** | Tablet/foldable primary, or >5 phone areas | 3–7 | Native fit | Compact phone (use bottom bar) |
| **Navigation drawer** | Many areas, infrequent switching, or secondary destinations | 5+ | Permanent/dismissible drawer | Areas switched constantly (slow to reach) |
| **Nested graphs (per-area sub-flows)** | Each top-level area has its own multi-screen flow | Any | Composes with above | Flat app with no sub-flows |

**Selection rules:**
- **3–5 frequently-switched peer areas → bottom navigation.** This is the default for most consumer apps and the one Material expects on compact width.
- **>5 areas, or areas users rarely jump between → navigation drawer** (or a drawer for secondary areas + bottom bar for the top 3–5).
- **Tablet/foldable as a first-class target → plan the rail now**, even if phones use a bottom bar; an adaptive scaffold (Phase 3) swaps between them automatically.
- **Each tab is itself a multi-screen flow → nested graphs**, so each area keeps its own back stack and start destination.

Document the choice and *why the alternatives lost*:

```
DECISION: Bottom navigation, 4 destinations (Home, Search, Library, Profile)
Rationale: 4 peer areas, switched many times per session; compact-width primary device.
Rejected: Drawer (areas switched too often to bury behind a hamburger);
          Rail-only (poor ergonomics on compact phones — reserved for wide screens via adaptive scaffold).
Each tab owns a nested graph so its detail screens don't lose their back stack on tab switch.
```

**CHECKPOINT 2 — Pattern lock (discuss before adaptive/route work):** Confirm the primary pattern and the exact top-level destination list and order. Tab order and count are surprisingly load-bearing (analytics, muscle memory, default start). Get explicit sign-off before continuing.

---

### Phase 3: Adaptive Navigation (Large Screens & Foldables)

If the app targets only phones, state that explicitly and skip the adaptive scaffold — do not add complexity the app won't use. Otherwise, plan navigation against **window size classes** (Compact / Medium / Expanded), not device types.

| Window width | Class | Top-level nav surface | List-detail behavior |
|---|---|---|---|
| < 600dp | Compact | Bottom navigation bar | Single pane (list → push detail) |
| 600–839dp | Medium | Navigation rail | Optional two-pane |
| ≥ 840dp | Expanded | Navigation rail or permanent drawer | Two-pane list-detail |

Use the adaptive navigation scaffold so the pattern morphs automatically instead of hand-branching on width:

```kotlin
// NavigationSuiteScaffold picks bottom bar / rail / drawer from the current
// window size class. Add the latest stable androidx.compose.material3.adaptive
// navigation-suite artifact via the version catalog.
NavigationSuiteScaffold(
    navigationSuiteItems = {
        TopLevelDestination.entries.forEach { dest ->
            item(
                selected = currentDestination == dest,
                onClick = { navController.navigateToTopLevel(dest) },
                icon = { Icon(dest.icon, contentDescription = null) },
                label = { Text(stringResource(dest.labelRes)) },
            )
        }
    }
) {
    AppNavHost(navController = navController)
}
```

For list→detail screens, plan a list-detail pane scaffold (`ListDetailPaneScaffold`) so wide screens show both panes and compact screens fall back to push navigation. Decide **now** which list→detail pairs are adaptive — mark them in the Phase 1 inventory's "Form-Factor Note" column. Also note: support drag-resize/free-form windows and table-top/book foldable postures only if the app's content genuinely benefits; otherwise the standard size-class behavior is sufficient.

---

### Phase 4: Type-Safe Route Map (Navigation Compose)

Define every route as a **serializable type**, not a `String`. Type-safe routes catch wrong/missing arguments at compile time and remove hand-rolled URL parsing. List the full route map first, then the graph wiring.

| Route object | Args (types) | Top-level? | Nested graph | Deep-linkable |
|---|---|---|---|---|
| `Home` | — | Yes | `HomeGraph` | No |
| `Search(query: String?)` | query: String? | Yes | `SearchGraph` | Yes |
| `ItemDetail(itemId: String)` | itemId: String | No | `HomeGraph` | Yes (App Link) |
| `Profile` | — | Yes | `ProfileGraph` | No |
| `Settings` | — | No | `ProfileGraph` | No |
| `SignIn(returnTo: String?)` | returnTo: String? | No (flow) | root | No |

```kotlin
// Routes as @Serializable types — no string templates, no manual arg parsing.
@Serializable data object Home
@Serializable data class Search(val query: String? = null)
@Serializable data class ItemDetail(val itemId: String)
@Serializable data object Profile

NavHost(navController, startDestination = Home) {
    composable<Home> { HomeScreen(onItem = { navController.navigate(ItemDetail(it)) }) }
    composable<Search> { entry ->
        val args = entry.toRoute<Search>()      // typed args, no bundle keys
        SearchScreen(initialQuery = args.query)
    }
    composable<ItemDetail> { entry ->
        val args = entry.toRoute<ItemDetail>()
        ItemDetailScreen(itemId = args.itemId)
    }
}
```

**Multi-module note:** when features live in separate modules, declare each route type in a shared API/navigation module so features can navigate to each other's routes without depending on each other's implementation. Keep navigation glue in the `:app` (or a navigation) module; features expose only their route types and `NavGraphBuilder` extensions.

---

### Phase 5: Back Stack, Predictive Back & Up vs. Back

Decide explicit behavior for each navigation edge. Ambiguity here produces the classic "back button does something weird" bug class.

| Concern | Decision to make | Typical answer |
|---|---|---|
| **Start destination** | Which destination is the back-stack root? | First top-level (e.g., `Home`) |
| **Tab re-selection** | Tap current tab again → ? | Pop that tab's graph to its start |
| **Tab switching back stack** | Switch A→B→back → returns to A? | `saveState`/`restoreState` per top-level |
| **Up vs. Back** | Up (toolbar arrow) vs system Back semantics | Up = parent in hierarchy; Back = previous in time |
| **Modal dismissal** | Back on a sheet/dialog | Dismiss modal, not pop underlying screen |
| **Exit** | Back from start destination | Exit app (don't loop tabs) |

Top-level navigation should preserve each tab's state and use a single-instance start:

```kotlin
fun NavController.navigateToTopLevel(route: Any) = navigate(route) {
    popUpTo(graph.findStartDestination().id) { saveState = true }
    launchSingleTop = true   // don't stack duplicates of a tab
    restoreState = true      // restore that tab's previous back stack
}
```

**Predictive back:** opt into predictive back (`android:enableOnBackInvokedCallback="true"` in the manifest; handle in-app back via `PredictiveBackHandler` where you intercept back, e.g., for custom dismiss animations or "unsaved changes" guards). Confirm Navigation Compose's built-in predictive-back transitions are acceptable, or list the screens that need custom handling. Plan **back-press guards** (e.g., a "discard draft?" confirm) per screen rather than discovering them ad hoc.

---

### Phase 6: Deep Link & App Links Strategy

Decide which destinations are externally reachable and how. Distinguish three mechanisms:

| Mechanism | Looks like | Verified? | Use for |
|---|---|---|---|
| **Custom scheme** | `myapp://item/123` | No | Internal links, notifications, widgets |
| **Web link (http)** | `https://app.example.com/item/123` (chooser may appear) | No | Fallback when domain unverified |
| **Android App Links** | `https://app.example.com/item/123` opens app directly | Yes (Digital Asset Links) | Marketing/web links you own a domain for |

Map each deep-linkable destination, its parameters, the auth requirement, and the unauthenticated fallback:

| URL pattern | Route | Params | Auth | If signed out |
|---|---|---|---|---|
| `https://app.example.com/item/{id}` | `ItemDetail(id)` | id | Public | Open directly |
| `https://app.example.com/search?q={q}` | `Search(q)` | q | Public | Open directly |
| `myapp://profile/orders` | `Orders` | — | Required | Route to `SignIn(returnTo="/orders")`, then continue |

Attach deep links to typed routes and declare verified App Links in the manifest:

```kotlin
composable<ItemDetail>(
    deepLinks = listOf(navDeepLink<ItemDetail>(basePath = "https://app.example.com/item"))
) { /* ... */ }
```

```xml
<!-- Verified Android App Link: autoVerify + a hosted assetlinks.json -->
<intent-filter android:autoVerify="true">
    <action android:name="android.intent.action.VIEW" />
    <category android:name="android.intent.category.DEFAULT" />
    <category android:name="android.intent.category.BROWSABLE" />
    <data android:scheme="https" android:host="app.example.com" />
</intent-filter>
```

**Auth-gated deep links:** never drop the user on a sign-in wall and lose their destination. Carry the intended route through sign-in (`returnTo`) and resume after auth. Plan this once, centrally, in the deep-link handler — not per screen.

---

### Phase 7: Navigation Graph Diagram

Render the whole graph so the architecture is visible at a glance. Top-level destinations, nested graphs, detail edges, and modal surfaces should all be distinguishable.

```mermaid
graph TD
    subgraph Root
        Onboarding -. first run .-> Home
        SignIn((SignIn modal))
    end
    subgraph BottomNav
        Home --> ItemDetail
        Search --> ItemDetail
        Library --> ItemDetail
        Profile --> Settings
        Profile -. gated .-> SignIn
    end
    ItemDetail -. paywall .-> Paywall((Paywall modal))
    AppLink[/https://app.example.com/item/{id}/] --> ItemDetail
```

---

## Expected Output

1. **Screen / Destination Inventory** — the full classified table (type, reached-from, auth, params, form-factor note).
2. **Top-Level Pattern Decision** — chosen pattern, ordered top-level list, and a recorded rationale with rejected alternatives.
3. **Adaptive Navigation Plan** — window-size-class behavior and which list→detail pairs become two-pane (or an explicit "phone-only, no adaptive scaffold" statement).
4. **Type-Safe Route Map** — every route as a serializable object/class with typed args, plus the `NavHost`/graph wiring and any multi-module route-sharing notes.
5. **Back-Stack & Predictive-Back Plan** — start destination, tab state save/restore, up-vs-back rules, modal dismissal, exit behavior, and per-screen back guards.
6. **Deep Link & App Links Strategy** — URL→route map with params, auth gating, signed-out fallbacks, and manifest/verification plan.
7. **Navigation Graph Diagram** — Mermaid (or text) graph showing all destinations, nesting, modals, and deep-link entry points.

---

## CRITICAL: Verification Requirements

- [ ] Every screen in the app appears exactly once in the inventory and is classified (top-level / detail / sub / modal).
- [ ] Exactly one primary top-level navigation pattern is chosen, with the top-level count and order explicitly justified.
- [ ] Every navigable parameter is typed (no `String`-template routes, no hand-parsed arguments).
- [ ] Each top-level destination's back-stack save/restore behavior is defined (switching tabs doesn't lose state or loop on back).
- [ ] The start destination and the "back from start = exit" behavior are stated.
- [ ] Predictive back is opted into, and every screen that needs a back guard (unsaved changes, confirm-dismiss) is listed.
- [ ] Each deep-linkable destination has a URL pattern, auth requirement, and a defined signed-out fallback.
- [ ] App Links destinations have a domain-verification plan (`autoVerify` + assetlinks.json), or are explicitly downgraded to unverified web/custom-scheme links.
- [ ] Adaptive behavior is either planned per window size class OR the app is explicitly declared phone-only.

## False-Positive Prevention

- ❌ Do NOT default to a bottom nav bar with 6+ tabs — past ~5 destinations it stops fitting; reconsider drawer or grouping.
- ❌ Do NOT add a `NavigationSuiteScaffold`, navigation rail, or two-pane list-detail to a phone-only app that will never run on tablets/foldables.
- ❌ Do NOT introduce nested graphs for a flat app where no top-level area has its own multi-screen flow.
- ❌ Do NOT design deep links / App Links the app has no external entry point for — notifications, widgets, and marketing links must actually exist.
- ❌ Do NOT keep `String`-based routes "for simplicity" — type-safe serializable routes are the current Navigation Compose default and prevent a whole bug class.
- ❌ Do NOT bury frequently-switched areas behind a hamburger drawer to "keep the bar clean."
- ✅ DO match navigation complexity to surface area — a 5-screen utility may need only a single flow plus one detail edge and zero deep links.
- ✅ DO plan the rail/adaptive swap up front *if* tablets/foldables are a real target, since retrofitting it is costly.
- ✅ DO route auth-gated deep links through sign-in while preserving the original destination.
- ✅ DO record *why* the chosen pattern beat the alternatives, so a later reviewer doesn't relitigate it.

## Techniques Used

- **ST-01** (Clear Objective Statement): Anchors the work to one deliverable — a complete, type-safe, appropriately-scoped navigation graph produced before implementation.
- **ST-02** (Structured Sequential Instructions): Drives the seven-phase flow from inventory → pattern → adaptive → routes → back stack → deep links → diagram.
- **RT-02** (Multi-Dimensional Analysis Framework): Pattern and adaptive decisions weigh destination count, switching frequency, form factor, and sub-flow structure as independent axes.
- **CM-03** (Scope Definition): The inventory and "phone-only / no deep links" off-ramps set explicit boundaries so the IA doesn't sprawl.
- **DS-06** (Prioritization and Severity Guidance): Top-level vs. detail vs. modal classification and the pattern selection rules force prioritized structure rather than a flat screen pile.
- **NE-02** (Phased Workflow Architecture): CHECKPOINT gates at inventory and pattern-lock prevent committing routes/graphs before the user shapes the IA.

## Related Prompts

- [android_architecture_selection.md](android_architecture_selection.md) — Decide layering/architecture first so routes map cleanly to ViewModels.
- [android_feature_specification.md](android_feature_specification.md) — The feature specs whose screens populate this inventory.
- [../implementation/android_navigation_implementation.md](../implementation/android_navigation_implementation.md) — Build the `NavHost`, typed routes, and deep links from this map.
- [../analysis/android_navigation_deeplink_analysis.md](../analysis/android_navigation_deeplink_analysis.md) — Audit an existing app's navigation and deep-link setup against this plan.
