---
title: "Navigation Patterns Migration - Compose to SwiftUI"
category: mobile-development
description: "Migrate Compose Navigation to NavigationStack covering routes, type-safe arguments, deep linking, back stack management, and nested navigation graphs"
techniques:
  - ST-01
  - RT-02
  - DS-02
difficulty: intermediate
tags:
  - ios
  - android
  - migration
  - navigation
  - compose-navigation
  - navigationstack
  - deep-linking
updated: "2026-03-19"
---

# Navigation Patterns Migration - Compose to SwiftUI

**Objective:** Translate Compose Navigation patterns (NavHost, NavController, routes, arguments, deep links, nested graphs) to SwiftUI NavigationStack equivalents, producing a navigation architecture that feels native on iOS while preserving the same user flows.

**When to Use:** When migrating an Android app's navigation architecture to iOS. This prompt covers both simple linear flows and complex nested navigation with deep linking support.

**Prompt Type:** Modular (~280 lines)

## Context Gathering

1. How many navigation destinations does the app have?
2. What argument types are passed between screens? (primitives, complex objects, optional)
3. Is deep linking used? What URL patterns?
4. Are there nested navigation graphs? (e.g., auth flow, main flow, onboarding)
5. Is there any conditional navigation? (e.g., auth guard, onboarding completion check)
6. Are there modal presentations? (bottom sheets, full-screen dialogs)
7. Is there any back stack manipulation? (popUpTo, launchSingleTop)

## Instructions

### CRITICAL: Verification Requirements

- Navigation paths MUST reproduce the same user flows as the Android app
- Deep link handling MUST be tested with actual URL schemes on iOS
- Argument passing MUST use type-safe patterns (Codable for complex types)
- Back stack behavior MUST match expected UX (swipe-back, programmatic pop)

### False-Positive Prevention

- ❌ DO NOT create a string-based route system mimicking Compose Navigation on iOS
- ✅ DO use SwiftUI's type-safe NavigationPath with Hashable destinations
- ❌ DO NOT manage navigation state manually with arrays of screens
- ✅ DO use NavigationStack with NavigationPath for programmatic navigation
- ❌ DO NOT replicate `popUpTo(inclusive = true)` literally — SwiftUI handles this differently
- ✅ DO use NavigationPath manipulation or `.navigationDestination` conditionals
- ❌ DO NOT use `NavigationLink(isActive:)` — it is deprecated
- ✅ DO use `NavigationLink(value:)` with `navigationDestination(for:)`

### Step 1: Basic Route Mapping

**Kotlin (Compose Navigation routes):**
```kotlin
// Route definitions
sealed class Screen(val route: String) {
    data object Home : Screen("home")
    data object Profile : Screen("profile/{userId}") {
        fun createRoute(userId: String) = "profile/$userId"
    }
    data object Settings : Screen("settings")
    data object ItemDetail : Screen("item/{itemId}?source={source}") {
        fun createRoute(itemId: Int, source: String? = null) =
            "item/$itemId${source?.let { "?source=$it" } ?: ""}"
    }
}

// NavHost
NavHost(navController = navController, startDestination = "home") {
    composable("home") {
        HomeScreen(
            onNavigateToProfile = { userId ->
                navController.navigate(Screen.Profile.createRoute(userId))
            }
        )
    }
    composable(
        route = "profile/{userId}",
        arguments = listOf(navArgument("userId") { type = NavType.StringType })
    ) { backStackEntry ->
        val userId = backStackEntry.arguments?.getString("userId")!!
        ProfileScreen(userId = userId)
    }
    composable(
        route = "item/{itemId}?source={source}",
        arguments = listOf(
            navArgument("itemId") { type = NavType.IntType },
            navArgument("source") {
                type = NavType.StringType
                nullable = true
                defaultValue = null
            }
        )
    ) { backStackEntry ->
        val itemId = backStackEntry.arguments?.getInt("itemId")!!
        val source = backStackEntry.arguments?.getString("source")
        ItemDetailScreen(itemId = itemId, source = source)
    }
}
```

**Swift (SwiftUI NavigationStack):**
```swift
// Type-safe destination definitions
enum AppDestination: Hashable {
    case home
    case profile(userId: String)
    case settings
    case itemDetail(itemId: Int, source: String? = nil)
}

// Navigation container
struct AppNavigationStack: View {
    @State private var path = NavigationPath()

    var body: some View {
        NavigationStack(path: $path) {
            HomeScreen(onNavigateToProfile: { userId in
                path.append(AppDestination.profile(userId: userId))
            })
            .navigationDestination(for: AppDestination.self) { destination in
                switch destination {
                case .home:
                    HomeScreen(onNavigateToProfile: { userId in
                        path.append(AppDestination.profile(userId: userId))
                    })
                case .profile(let userId):
                    ProfileScreen(userId: userId)
                case .settings:
                    SettingsScreen()
                case .itemDetail(let itemId, let source):
                    ItemDetailScreen(itemId: itemId, source: source)
                }
            }
        }
    }
}
```

### Step 2: Deep Linking

**Kotlin (Compose deep links):**
```kotlin
composable(
    route = "item/{itemId}",
    deepLinks = listOf(
        navDeepLink {
            uriPattern = "myapp://item/{itemId}"
            action = Intent.ACTION_VIEW
        }
    )
) { backStackEntry ->
    ItemDetailScreen(itemId = backStackEntry.arguments?.getInt("itemId")!!)
}
```

**Swift (iOS deep link handling):**
```swift
struct ContentView: View {
    @State private var path = NavigationPath()

    var body: some View {
        NavigationStack(path: $path) {
            HomeScreen()
                .navigationDestination(for: AppDestination.self) { dest in
                    destinationView(for: dest)
                }
        }
        .onOpenURL { url in
            handleDeepLink(url)
        }
    }

    private func handleDeepLink(_ url: URL) {
        // URL: myapp://item/42
        guard let components = URLComponents(url: url, resolvingAgainstBaseURL: false),
              let host = components.host else { return }

        switch host {
        case "item":
            if let itemIdString = components.path
                .trimmingCharacters(in: CharacterSet(charactersIn: "/")),
               let itemId = Int(itemIdString) {
                path.append(AppDestination.itemDetail(itemId: itemId))
            }
        case "profile":
            let userId = components.path
                .trimmingCharacters(in: CharacterSet(charactersIn: "/"))
            path.append(AppDestination.profile(userId: userId))
        default:
            break
        }
    }
}
```

### Step 3: Nested Navigation (Auth Flow)

**Kotlin (Compose nested nav graph):**
```kotlin
NavHost(navController, startDestination = "auth") {
    navigation(startDestination = "login", route = "auth") {
        composable("login") { LoginScreen() }
        composable("register") { RegisterScreen() }
        composable("forgot_password") { ForgotPasswordScreen() }
    }
    navigation(startDestination = "home", route = "main") {
        composable("home") { HomeScreen() }
        composable("profile/{userId}") { ProfileScreen() }
    }
}

// After login success:
navController.navigate("main") {
    popUpTo("auth") { inclusive = true }
}
```

**Swift (SwiftUI conditional root navigation):**
```swift
struct RootView: View {
    @State private var authManager: AuthManager

    var body: some View {
        Group {
            if authManager.isAuthenticated {
                MainTabView()
            } else {
                AuthNavigationStack()
            }
        }
        .animation(.default, value: authManager.isAuthenticated)
    }
}

struct AuthNavigationStack: View {
    @State private var path = NavigationPath()

    var body: some View {
        NavigationStack(path: $path) {
            LoginScreen(
                onRegister: { path.append(AuthDestination.register) },
                onForgotPassword: { path.append(AuthDestination.forgotPassword) }
            )
            .navigationDestination(for: AuthDestination.self) { dest in
                switch dest {
                case .register: RegisterScreen()
                case .forgotPassword: ForgotPasswordScreen()
                }
            }
        }
    }
}
```

> **Key Difference:** Compose uses `popUpTo(inclusive = true)` to clear the auth back stack. SwiftUI handles this structurally — when `isAuthenticated` changes, the auth stack is replaced entirely.

### Step 4: Back Stack Manipulation

| Compose Pattern | SwiftUI Equivalent |
|----------------|-------------------|
| `navController.popBackStack()` | System back button / `path.removeLast()` |
| `popUpTo("home") { inclusive = false }` | `path.removeLast(path.count - 1)` |
| `popUpTo("home") { inclusive = true }` | `path = NavigationPath()` (reset to root) |
| `launchSingleTop = true` | Check before appending to path |
| `restoreState = true` | No direct equivalent — use `@SceneStorage` |

## Expected Output

1. **Destination enum** with all navigation routes and arguments
2. **NavigationStack setup** with `navigationDestination` handlers
3. **Deep link handler** parsing URL schemes into navigation actions
4. **Auth flow** with conditional root navigation
5. **Modal presentation** patterns for sheets and full-screen covers

## Example Interaction

**User:** Our Android app has 12 screens across 3 nested nav graphs (auth, main, settings), uses deep links for product pages, and passes product IDs as arguments.

**Assistant:**

```swift
// Destination definitions
enum MainDestination: Hashable {
    case home
    case productDetail(productId: String)
    case category(categoryId: String)
    case cart
    case search(query: String?)
}

enum AuthDestination: Hashable {
    case login, register, forgotPassword
}

enum SettingsDestination: Hashable {
    case profile, notifications, privacy, about
}
```

The 3 nested nav graphs become: conditional auth root + TabView with separate NavigationStacks per tab + settings presented as `.sheet`.

## Techniques Used

| Technique | Application |
|-----------|-------------|
| **ST-01: Structured Task Decomposition** | Breaking navigation into routes, deep links, nesting, back stack |
| **RT-02: Contextual Reference Integration** | Compose Navigation and SwiftUI NavigationStack docs |
| **DS-02: Output Specification Framework** | Type-safe destination enums, handler code |

## Related Prompts

- `migration_compose_to_swiftui.md` — UI component translation
- `migration_material_to_hig.md` — Navigation UX design adaptation
- `migration_architecture_adaptation.md` — ViewModel and state management for navigation

## Customization Guide

- **Coordinator Pattern:** If the iOS team prefers Coordinator pattern, wrap NavigationPath in a Coordinator class that manages flow logic.
- **UIKit Navigation:** If targeting UIKit, map to UINavigationController with push/pop/present.
- **Tab-Scoped Stacks:** For apps with independent navigation per tab, use separate NavigationStack instances inside each TabView tab.
- **iOS 16 Compatibility:** NavigationStack is iOS 16+. For iOS 15, fall back to NavigationView (deprecated but functional).
