---
title: "Android Navigation Implementation"
category: mobile-development
description: ""
tags:
  - android
  - mobile-development
updated: "2026-03-19"
---

# Android Navigation Implementation

**Objective:** Implement type-safe navigation using Jetpack Compose Navigation with proper argument passing, deep linking, and nested navigation graphs following modern Android patterns.

**When to Use:** Use this prompt when setting up navigation for a Compose-based Android app or adding new navigation flows to an existing app. Ideal for new projects, migrating from Fragment navigation, or implementing deep links. Best used after screen designs are finalized.

**Prompt Type:** Modular (120-150 lines)

---

## Context Gathering

Before implementing navigation, gather essential context:

1. **Current Setup:**
   - "Is Navigation Compose already in the project?"
   - "Are there existing routes or navigation patterns?"
   - "Do you use a single Activity or multiple Activities?"

2. **Navigation Requirements:**
   - "What screens need to be connected?"
   - "Which screens need arguments (IDs, data)?"
   - "Do you need deep link support?"

3. **Structure:**
   - "Should navigation be organized into nested graphs (auth, main, settings)?"
   - "Do you need bottom navigation or drawer navigation?"

---

## Instructions

### CRITICAL: Implementation Requirements

**Before implementing ANY code, you MUST:**

1. **Understand existing navigation setup** - Check for existing Navigation Compose, Fragment navigation, or custom navigation in the codebase.
2. **Verify navigation requirements** - Confirm deep linking, argument passing, and back stack requirements before implementing.
3. **Follow project conventions** - Match existing route naming, argument patterns, and navigation graph organization.
4. **Provide specific, working code** - All code samples MUST include file paths (e.g., `navigation/AppNavGraph.kt`) and be copy-paste ready.
5. **Include proper type safety** - Use type-safe navigation arguments where supported.

**Adapting to existing navigation patterns is preferred over introducing new approaches.** Don't mix navigation libraries.

### Quality Requirements

- ❌ Do NOT mix Navigation Compose with Fragment navigation without clear interop strategy
- ❌ Do NOT generate routes without proper argument serialization
- ❌ Do NOT skip deep link configuration for user-facing screens
- ❌ Do NOT ignore back stack behavior and edge cases
- ✅ DO follow existing route definition patterns
- ✅ DO provide proper SavedStateHandle integration for arguments
- ✅ DO include navigation testing helpers where applicable
- ✅ DO specify exact file paths for all code changes

---

### Phase 1: Route Definition

#### 1.1 Type-Safe Routes with Kotlin Serialization

Define routes using sealed classes for type safety:

```kotlin
// Navigation destinations
@Serializable
sealed interface Route {
    @Serializable
    data object Home : Route

    @Serializable
    data object Profile : Route

    @Serializable
    data class ItemDetail(val itemId: String) : Route

    @Serializable
    data class EditItem(
        val itemId: String,
        val initialTitle: String? = null
    ) : Route

    @Serializable
    data object Settings : Route
}

// Nested graph routes
@Serializable
sealed interface AuthRoute {
    @Serializable
    data object Login : AuthRoute

    @Serializable
    data object Register : AuthRoute

    @Serializable
    data class ForgotPassword(val email: String? = null) : AuthRoute
}
```

#### 1.2 Dependencies Setup

```kotlin
// build.gradle.kts
dependencies {
    implementation("androidx.navigation:navigation-compose:2.8.0")
    implementation("org.jetbrains.kotlinx:kotlinx-serialization-json:1.6.0")
}

// Apply serialization plugin
plugins {
    kotlin("plugin.serialization") version "1.9.0"
}
```

---

### Phase 2: NavHost Configuration

#### 2.1 Main Navigation Setup

```kotlin
@Composable
fun AppNavigation(
    navController: NavHostController = rememberNavController(),
    startDestination: Route = Route.Home
) {
    NavHost(
        navController = navController,
        startDestination = startDestination
    ) {
        // Simple destination
        composable<Route.Home> {
            HomeScreen(
                onNavigateToProfile = { navController.navigate(Route.Profile) },
                onNavigateToItem = { id -> navController.navigate(Route.ItemDetail(id)) }
            )
        }

        // Destination with arguments
        composable<Route.ItemDetail> { backStackEntry ->
            val args = backStackEntry.toRoute<Route.ItemDetail>()
            ItemDetailScreen(
                itemId = args.itemId,
                onNavigateToEdit = { title ->
                    navController.navigate(Route.EditItem(args.itemId, title))
                },
                onNavigateBack = { navController.popBackStack() }
            )
        }

        composable<Route.EditItem> { backStackEntry ->
            val args = backStackEntry.toRoute<Route.EditItem>()
            EditItemScreen(
                itemId = args.itemId,
                initialTitle = args.initialTitle,
                onSaveComplete = {
                    navController.popBackStack(Route.ItemDetail(args.itemId), inclusive = false)
                }
            )
        }

        // Nested graph
        navigation<AuthGraph>(startDestination = AuthRoute.Login) {
            composable<AuthRoute.Login> {
                LoginScreen(
                    onLoginSuccess = {
                        navController.navigate(Route.Home) {
                            popUpTo<AuthGraph> { inclusive = true }
                        }
                    },
                    onNavigateToRegister = { navController.navigate(AuthRoute.Register) }
                )
            }

            composable<AuthRoute.Register> {
                RegisterScreen(
                    onRegisterSuccess = {
                        navController.navigate(Route.Home) {
                            popUpTo<AuthGraph> { inclusive = true }
                        }
                    }
                )
            }
        }
    }
}

// Graph marker for nested navigation
@Serializable
data object AuthGraph
```

#### 2.2 Bottom Navigation Integration

```kotlin
@Composable
fun MainScreenWithBottomNav() {
    val navController = rememberNavController()

    Scaffold(
        bottomBar = {
            NavigationBar {
                val navBackStackEntry by navController.currentBackStackEntryAsState()
                val currentDestination = navBackStackEntry?.destination

                bottomNavItems.forEach { item ->
                    NavigationBarItem(
                        icon = { Icon(item.icon, contentDescription = item.label) },
                        label = { Text(item.label) },
                        selected = currentDestination?.hasRoute(item.route::class) == true,
                        onClick = {
                            navController.navigate(item.route) {
                                popUpTo(navController.graph.findStartDestination().id) {
                                    saveState = true
                                }
                                launchSingleTop = true
                                restoreState = true
                            }
                        }
                    )
                }
            }
        }
    ) { padding ->
        NavHost(
            navController = navController,
            startDestination = Route.Home,
            modifier = Modifier.padding(padding)
        ) {
            // Destinations...
        }
    }
}

data class BottomNavItem<T : Route>(
    val route: T,
    val icon: ImageVector,
    val label: String
)

val bottomNavItems = listOf(
    BottomNavItem(Route.Home, Icons.Default.Home, "Home"),
    BottomNavItem(Route.Search, Icons.Default.Search, "Search"),
    BottomNavItem(Route.Profile, Icons.Default.Person, "Profile")
)
```

---

### Phase 3: Advanced Navigation

#### 3.1 Deep Link Support

```kotlin
composable<Route.ItemDetail>(
    deepLinks = listOf(
        navDeepLink<Route.ItemDetail>(basePath = "https://app.example.com/item")
    )
) { backStackEntry ->
    val args = backStackEntry.toRoute<Route.ItemDetail>()
    ItemDetailScreen(itemId = args.itemId)
}

// AndroidManifest.xml
<activity android:name=".MainActivity">
    <intent-filter>
        <action android:name="android.intent.action.VIEW" />
        <category android:name="android.intent.category.DEFAULT" />
        <category android:name="android.intent.category.BROWSABLE" />
        <data
            android:scheme="https"
            android:host="app.example.com"
            android:pathPrefix="/item" />
    </intent-filter>
</activity>
```

#### 3.2 Result Handling

Pass results back to previous screen:

```kotlin
// In EditItemScreen - save result
navController.previousBackStackEntry
    ?.savedStateHandle
    ?.set("edited_item", editedItem)
navController.popBackStack()

// In ItemDetailScreen - receive result
val savedStateHandle = navController.currentBackStackEntry?.savedStateHandle
val editedItem by savedStateHandle
    ?.getStateFlow<Item?>("edited_item", null)
    ?.collectAsStateWithLifecycle() ?: remember { mutableStateOf(null) }

LaunchedEffect(editedItem) {
    editedItem?.let { item ->
        // Handle updated item
        savedStateHandle?.remove<Item>("edited_item")
    }
}
```

#### 3.3 Conditional Navigation

```kotlin
@Composable
fun AppNavigation(isLoggedIn: Boolean) {
    val navController = rememberNavController()

    val startDestination = if (isLoggedIn) Route.Home else AuthGraph

    NavHost(
        navController = navController,
        startDestination = startDestination
    ) {
        // Destinations...
    }
}
```

---

## Expected Output

### File Structure

```
navigation/
├── Route.kt           # All route definitions
├── AppNavigation.kt   # Main NavHost setup
└── NavigationExt.kt   # Navigation extensions
```

### Implementation Checklist

- [ ] Route sealed class with all destinations
- [ ] NavHost with all composable destinations
- [ ] Argument passing with type safety
- [ ] Nested navigation graphs (if needed)
- [ ] Bottom/drawer navigation (if needed)
- [ ] Deep link configuration
- [ ] Result handling between screens
- [ ] Proper back stack management

---

## Techniques Used

- **ST-01** (Clear Objective): Single-sentence objective for navigation
- **ST-02** (Sequential Instructions): Phased approach from routes to advanced
- **RT-04** (Best Practice Review): Modern Navigation Compose patterns
- **ST-03** (Output Format Templates): Code templates for navigation

---

## Related Prompts

- [android_compose_screen_builder.md](android_compose_screen_builder.md) - Build screens for navigation
- [android_state_management.md](android_state_management.md) - Handle navigation events
- [android_feature_specification.md](../planning/android_feature_specification.md) - Design navigation flows
- [android_dependency_injection.md](android_dependency_injection.md) - Inject NavController

---

## Customization Guide

### For Fragment-Based Navigation

Use Navigation Component with Fragments:
- Define navigation graph in XML
- Use `findNavController()` for navigation
- Handle arguments with Safe Args plugin

### For Multi-Module Projects

Share navigation between modules:
- Define routes in shared `:core:navigation` module
- Each feature module registers its destinations
- Main app assembles the complete NavHost

### For Complex Transitions

Add custom animations:
```kotlin
composable<Route.Detail>(
    enterTransition = { slideInHorizontally { it } },
    exitTransition = { slideOutHorizontally { -it } }
) { ... }
```
