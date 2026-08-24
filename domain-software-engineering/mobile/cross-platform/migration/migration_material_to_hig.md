---
title: "Material Design to Human Interface Guidelines Migration"
category: mobile-development
description: "Map Material Design 3 components and patterns to Apple Human Interface Guidelines including navigation, actions, feedback, typography, and color systems"
techniques:
  - ST-01
  - RT-02
  - DS-02
difficulty: intermediate
tags:
  - ios
  - android
  - migration
  - material-design
  - hig
  - design-system
  - ui-patterns
updated: "2026-03-19"
---

# Material Design to Human Interface Guidelines Migration

**Objective:** Systematically translate Material Design 3 UI patterns, components, and design tokens to their Apple Human Interface Guidelines (HIG) equivalents. This ensures the iOS app feels native rather than a ported Android app, while preserving the app's brand identity and information architecture.

**When to Use:** During the design and UI implementation phase of an Android-to-iOS migration. Use this prompt when making decisions about how Android UI components should appear and behave on iOS.

**Prompt Type:** Modular (~280 lines)

## Context Gathering

1. Does the app follow Material Design 3 strictly or have a custom design system?
2. What Material components are used most heavily? (navigation, dialogs, sheets, cards)
3. Is there a shared brand identity that must be preserved across platforms?
4. What navigation pattern does the Android app use? (bottom nav, drawer, tabs)
5. Are there any custom Material components that deviate from standard patterns?

## Instructions

### CRITICAL: Verification Requirements

- Every design mapping MUST reference specific HIG component names and guidelines
- Navigation patterns MUST follow iOS conventions (users expect platform-standard behavior)
- Typography mappings MUST account for SF Pro font metrics vs. Roboto
- Color adaptations MUST support both light and dark mode on iOS

### False-Positive Prevention

- ❌ DO NOT port a navigation drawer as the primary navigation on iOS
- ✅ DO use TabView (tab bar) for primary navigation, which is the iOS standard
- ❌ DO NOT use a Floating Action Button (FAB) on iOS
- ✅ DO use navigation bar buttons, contextual menus, or prominent inline buttons
- ❌ DO NOT use Snackbars for feedback on iOS
- ✅ DO use inline banners, alerts, or toast-style notifications appropriate to iOS
- ❌ DO NOT replicate Material bottom sheets with drag handles for settings
- ✅ DO use `.sheet` or `.inspector` for secondary content on iOS

### Step 1: Navigation Pattern Mapping

| Material Design | HIG Equivalent | Implementation |
|----------------|----------------|----------------|
| Bottom Navigation Bar | Tab Bar (`TabView`) | Primary navigation — identical concept |
| Navigation Drawer | Tab Bar or sidebar (iPad) | Drawer is not standard on iOS |
| Top App Bar (small) | Navigation Bar (`.navigationTitle`) | Title + actions |
| Top App Bar (large) | Large Title (`.navigationBarTitleDisplayMode(.large)`) | Collapsible title |
| Navigation Rail (tablet) | Sidebar (`NavigationSplitView`) | iPad multi-column |
| Back arrow | System back (chevron) | Automatic with NavigationStack |

**Kotlin (Material bottom navigation):**
```kotlin
@Composable
fun MainScreen() {
    val navController = rememberNavController()
    Scaffold(
        bottomBar = {
            NavigationBar {
                NavigationBarItem(
                    icon = { Icon(Icons.Default.Home, "Home") },
                    label = { Text("Home") },
                    selected = currentRoute == "home",
                    onClick = { navController.navigate("home") }
                )
                NavigationBarItem(
                    icon = { Icon(Icons.Default.Search, "Search") },
                    label = { Text("Search") },
                    selected = currentRoute == "search",
                    onClick = { navController.navigate("search") }
                )
                NavigationBarItem(
                    icon = { Icon(Icons.Default.Person, "Profile") },
                    label = { Text("Profile") },
                    selected = currentRoute == "profile",
                    onClick = { navController.navigate("profile") }
                )
            }
        }
    ) { /* content */ }
}
```

**Swift (iOS tab bar):**
```swift
struct MainScreen: View {
    @State private var selectedTab = Tab.home

    var body: some View {
        TabView(selection: $selectedTab) {
            HomeScreen()
                .tabItem {
                    Label("Home", systemImage: "house")
                }
                .tag(Tab.home)

            SearchScreen()
                .tabItem {
                    Label("Search", systemImage: "magnifyingglass")
                }
                .tag(Tab.search)

            ProfileScreen()
                .tabItem {
                    Label("Profile", systemImage: "person")
                }
                .tag(Tab.profile)
        }
    }
}
```

### Step 2: Action Patterns

| Material Pattern | iOS Pattern | Notes |
|-----------------|-------------|-------|
| FAB (Floating Action Button) | Navigation bar button / inline CTA | iOS has no FAB convention |
| Extended FAB | Prominent button at top/bottom of list | Use `.borderedProminent` style |
| Icon button in top bar | `.toolbar` button | Identical placement |
| Speed dial (FAB expansion) | Context menu or action sheet | `.contextMenu` or `.confirmationDialog` |
| Long press menu | Context menu (`.contextMenu`) | Direct equivalent |
| Swipe actions on list | `.swipeActions` | Native SwiftUI support |

**Kotlin (Material FAB):**
```kotlin
Scaffold(
    floatingActionButton = {
        ExtendedFloatingActionButton(
            onClick = { createNewItem() },
            icon = { Icon(Icons.Default.Add, "Add") },
            text = { Text("New Item") }
        )
    }
) { /* content */ }
```

**Swift (iOS — toolbar button replacement):**
```swift
NavigationStack {
    ItemListView()
        .navigationTitle("Items")
        .toolbar {
            ToolbarItem(placement: .primaryAction) {
                Button("New Item", systemImage: "plus") {
                    createNewItem()
                }
            }
        }
}
```

### Step 3: Feedback and Dialog Patterns

| Material Component | iOS Component | SwiftUI API |
|-------------------|---------------|-------------|
| Snackbar | Banner / inline message | Custom view or `.alert` |
| AlertDialog | Alert | `.alert()` |
| BottomSheetDialog | Sheet | `.sheet()` |
| DatePickerDialog | Inline date picker | `DatePicker` (inline style) |
| TimePicker | Wheel picker | `DatePicker` with `.datePickerStyle(.wheel)` |
| ProgressIndicator (linear) | ProgressView (linear) | `ProgressView(value:)` |
| ProgressIndicator (circular) | ProgressView (spinner) | `ProgressView()` |

**Kotlin (Material Snackbar):**
```kotlin
val snackbarHostState = remember { SnackbarHostState() }

LaunchedEffect(errorMessage) {
    errorMessage?.let {
        snackbarHostState.showSnackbar(
            message = it,
            actionLabel = "Retry",
            duration = SnackbarDuration.Short
        )
    }
}
```

**Swift (iOS — inline banner or alert):**
```swift
// Option 1: Alert (for actionable errors)
.alert("Error", isPresented: $showError) {
    Button("Retry") { retryAction() }
    Button("Dismiss", role: .cancel) { }
} message: {
    Text(errorMessage)
}

// Option 2: Inline banner (for non-blocking feedback)
if let errorMessage {
    HStack {
        Image(systemName: "exclamationmark.triangle")
        Text(errorMessage)
        Spacer()
        Button("Retry") { retryAction() }
    }
    .padding()
    .background(.yellow.opacity(0.2), in: RoundedRectangle(cornerRadius: 8))
    .padding(.horizontal)
}
```

### Step 4: Typography Mapping

| Material 3 Type Scale | iOS Equivalent | SwiftUI Font |
|-----------------------|----------------|-------------|
| Display Large | Large Title | `.largeTitle` |
| Display Medium | Title 1 | `.title` |
| Display Small | Title 2 | `.title2` |
| Headline Large | Title 3 | `.title3` |
| Headline Medium | Headline | `.headline` |
| Title Large | Headline | `.headline` |
| Title Medium | Subheadline | `.subheadline` |
| Body Large | Body | `.body` |
| Body Medium | Callout | `.callout` |
| Body Small | Footnote | `.footnote` |
| Label Large | Subheadline | `.subheadline` |
| Label Medium | Caption 1 | `.caption` |
| Label Small | Caption 2 | `.caption2` |

### Step 5: Color System Mapping

| Material 3 Color Role | iOS Equivalent | SwiftUI Color |
|-----------------------|----------------|---------------|
| `primary` | Tint color | `.tint` / `.accentColor` |
| `onPrimary` | White (on tint) | `.white` |
| `surface` | System background | `.background` |
| `onSurface` | Label | `.primary` |
| `surfaceVariant` | Secondary system background | `.secondarySystemBackground` |
| `onSurfaceVariant` | Secondary label | `.secondary` |
| `error` | Destructive / red | `.red` |
| `outline` | Separator | `.separator` |

## Expected Output

1. **Component mapping table** covering all Material components used in the app
2. **Navigation architecture** adapted to iOS conventions
3. **Design token translation** for typography, color, spacing, and elevation
4. **Before/after mockups or descriptions** for key screens

## Example Interaction

**User:** Our Android app uses bottom navigation (4 tabs), a FAB on the home screen, Material cards in a list, and snackbars for error feedback. How should the iOS version look?

**Assistant:**

| Android Pattern | iOS Adaptation |
|----------------|----------------|
| Bottom Navigation (4 tabs) | TabView with 4 tabs — direct equivalent |
| FAB "New Post" on Home | "+" button in navigation bar (`.toolbar`) |
| Material Card list | List rows with `.listRowBackground` or custom cards |
| Snackbar errors | `.alert` for actionable errors, inline banners for informational |

The iOS app should feel like it was built for iOS — using system navigation, system fonts, and standard interaction patterns.

## Techniques Used

| Technique | Application |
|-----------|-------------|
| **ST-01: Structured Task Decomposition** | Category-by-category design translation |
| **RT-02: Contextual Reference Integration** | Material Design 3 and Apple HIG documentation |
| **DS-02: Output Specification Framework** | Mapping tables, code examples, design tokens |

## Related Prompts

- `migration_compose_to_swiftui.md` — Code-level UI component translation
- `migration_navigation_patterns.md` — Navigation architecture deep dive
- `migration_android_to_ios_strategy.md` — Overall migration strategy

## Customization Guide

- **Brand Preservation:** When the app has strong brand colors/typography, keep those on iOS but use them within HIG patterns (e.g., brand color as `.accentColor`).
- **Hybrid Design System:** If maintaining a shared design system across platforms, create a theme abstraction that maps to Material on Android and HIG on iOS.
- **iPad Adaptation:** Material's responsive layout (rail + content) maps to `NavigationSplitView` on iPad.
- **Accessibility:** iOS has stronger built-in accessibility. Leverage Dynamic Type, VoiceOver labels, and reduce-motion preferences.
