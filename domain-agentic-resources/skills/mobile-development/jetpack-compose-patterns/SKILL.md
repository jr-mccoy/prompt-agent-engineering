---
name: jetpack-compose-patterns
description: Master Jetpack Compose UI development with modern patterns including state management, navigation, theming, and Material 3 implementation. Use this skill when building Android UIs with Compose, implementing state hoisting, creating custom components, setting up navigation, or when users mention "Compose UI", "Compose state", "remember", "LaunchedEffect", "Material 3", or "Compose navigation".
metadata:
  tags:
    - android
    - compose
    - jetpack
    - jetpack-compose
    - kotlin
    - mobile
  updated: "2026-04-11"
---
# Jetpack Compose Patterns

Comprehensive guidance for building modern Android UIs with Jetpack Compose, covering state management, navigation, theming, and Material 3 implementation.

## Purpose

This skill provides patterns and best practices for Jetpack Compose development, helping developers:
- Build declarative, reactive UIs following Compose best practices
- Implement proper state management with state hoisting
- Create reusable, composable UI components
- Set up type-safe navigation with Navigation Compose
- Implement Material 3 theming with dynamic colors

## When to Use This Skill

Use this skill when you need to:
- Build new UI screens with Jetpack Compose
- Implement state management in Compose (remember, rememberSaveable, ViewModel)
- Create custom composable components
- Set up navigation between Compose screens
- Implement Material 3 theming and dynamic colors
- Handle side effects (LaunchedEffect, SideEffect, DisposableEffect)
- Optimize Compose performance (stability, recomposition)
- Migrate from View-based UI to Compose

## When NOT to Use This Skill

Do NOT use this skill when:
- Working with traditional View-based Android UI (use Android View patterns)
- Building iOS apps (use SwiftUI or UIKit skills)
- Working with React Native or Flutter (use cross-platform skills)
- Working exclusively with non-UI Android code

## Core Patterns

### State Management

#### State Hoisting Pattern

**When to use:** Always hoist state to the appropriate level for reusability and testability.

```kotlin
// Stateless composable (preferred)
@Composable
fun UserInput(
    text: String,
    onTextChange: (String) -> Unit,
    modifier: Modifier = Modifier
) {
    TextField(
        value = text,
        onValueChange = onTextChange,
        modifier = modifier
    )
}

// Stateful wrapper (when needed)
@Composable
fun UserInputScreen() {
    var text by remember { mutableStateOf("") }
    UserInput(
        text = text,
        onTextChange = { text = it }
    )
}
```

#### ViewModel State Pattern

**When to use:** For screen-level state that survives configuration changes.

```kotlin
@HiltViewModel
class ProfileViewModel @Inject constructor(
    private val userRepository: UserRepository
) : ViewModel() {

    private val _uiState = MutableStateFlow(ProfileUiState())
    val uiState: StateFlow<ProfileUiState> = _uiState.asStateFlow()

    fun updateName(name: String) {
        _uiState.update { it.copy(name = name) }
    }
}

data class ProfileUiState(
    val name: String = "",
    val email: String = "",
    val isLoading: Boolean = false,
    val error: String? = null
)

@Composable
fun ProfileScreen(
    viewModel: ProfileViewModel = hiltViewModel()
) {
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()

    ProfileContent(
        uiState = uiState,
        onNameChange = viewModel::updateName
    )
}
```

#### Remember Variants

**`remember`:** Survives recomposition
```kotlin
val count = remember { mutableStateOf(0) }
```

**`rememberSaveable`:** Survives configuration changes and process death
```kotlin
val text = rememberSaveable { mutableStateOf("") }
```

**`derivedStateOf`:** Computed state that only updates when dependencies change
```kotlin
val sortedList = remember(list) {
    derivedStateOf { list.sortedBy { it.name } }
}
```

### Side Effects

#### LaunchedEffect

**When to use:** One-time events or coroutine-based side effects.

```kotlin
@Composable
fun SnackbarHandler(
    message: String?,
    snackbarHostState: SnackbarHostState
) {
    LaunchedEffect(message) {
        message?.let {
            snackbarHostState.showSnackbar(it)
        }
    }
}
```

#### DisposableEffect

**When to use:** Cleanup required when composable leaves composition.

```kotlin
@Composable
fun LifecycleObserver(
    onStart: () -> Unit,
    onStop: () -> Unit
) {
    val lifecycleOwner = LocalLifecycleOwner.current

    DisposableEffect(lifecycleOwner) {
        val observer = LifecycleEventObserver { _, event ->
            when (event) {
                Lifecycle.Event.ON_START -> onStart()
                Lifecycle.Event.ON_STOP -> onStop()
                else -> {}
            }
        }
        lifecycleOwner.lifecycle.addObserver(observer)
        onDispose {
            lifecycleOwner.lifecycle.removeObserver(observer)
        }
    }
}
```

#### SideEffect

**When to use:** Non-suspend effects on every successful recomposition.

```kotlin
@Composable
fun AnalyticsTracker(screenName: String) {
    val analytics = LocalAnalytics.current
    SideEffect {
        analytics.trackScreen(screenName)
    }
}
```

### Navigation

#### Type-Safe Navigation (Navigation 2.8+)

**Setup:**
```kotlin
@Serializable
data class ProfileRoute(val userId: String)

@Serializable
object HomeRoute

@Serializable
data class SettingsRoute(val section: String? = null)
```

**NavHost Setup:**
```kotlin
@Composable
fun AppNavHost(
    navController: NavHostController = rememberNavController()
) {
    NavHost(
        navController = navController,
        startDestination = HomeRoute
    ) {
        composable<HomeRoute> {
            HomeScreen(
                onNavigateToProfile = { userId ->
                    navController.navigate(ProfileRoute(userId))
                }
            )
        }

        composable<ProfileRoute> { backStackEntry ->
            val route = backStackEntry.toRoute<ProfileRoute>()
            ProfileScreen(userId = route.userId)
        }

        composable<SettingsRoute> { backStackEntry ->
            val route = backStackEntry.toRoute<SettingsRoute>()
            SettingsScreen(initialSection = route.section)
        }
    }
}
```

#### Navigation Patterns

**Single top navigation:**
```kotlin
navController.navigate(route) {
    launchSingleTop = true
}
```

**Pop up to destination:**
```kotlin
navController.navigate(HomeRoute) {
    popUpTo<HomeRoute> { inclusive = true }
}
```

**Navigate with result:**
```kotlin
// In source screen
val result = navController.currentBackStackEntry
    ?.savedStateHandle
    ?.getStateFlow<String>("result", "")
    ?.collectAsStateWithLifecycle()

// In destination screen
navController.previousBackStackEntry
    ?.savedStateHandle
    ?.set("result", selectedValue)
navController.popBackStack()
```

---

The Material 3 Theming section (Dynamic Color Theme, Custom Color Scheme, Typography) and Common Issues (Unnecessary Recompositions, State Lost on Configuration Change, Infinite Recomposition Loop, Navigation Memory Leak) are in the reference file.

See [references/material3-theming-and-issues.md](references/material3-theming-and-issues.md)

---

### Reusable Components

#### Component Template

```kotlin
@Composable
fun CustomCard(
    title: String,
    subtitle: String?,
    onClick: () -> Unit,
    modifier: Modifier = Modifier,
    leadingIcon: @Composable (() -> Unit)? = null,
    trailingContent: @Composable (() -> Unit)? = null
) {
    Card(
        onClick = onClick,
        modifier = modifier.fillMaxWidth()
    ) {
        Row(
            modifier = Modifier.padding(16.dp),
            verticalAlignment = Alignment.CenterVertically
        ) {
            leadingIcon?.let {
                it()
                Spacer(modifier = Modifier.width(16.dp))
            }

            Column(modifier = Modifier.weight(1f)) {
                Text(
                    text = title,
                    style = MaterialTheme.typography.titleMedium
                )
                subtitle?.let {
                    Text(
                        text = it,
                        style = MaterialTheme.typography.bodyMedium,
                        color = MaterialTheme.colorScheme.onSurfaceVariant
                    )
                }
            }

            trailingContent?.invoke()
        }
    }
}
```

### Performance Optimization

#### Stability Annotations

```kotlin
// Mark class as stable for Compose compiler
@Stable
data class UserState(
    val name: String,
    val email: String,
    val isVerified: Boolean
)

// For classes that can't be data classes
@Immutable
class ConfigState(
    val settings: Map<String, String>
)
```

#### Key for LazyColumn

```kotlin
LazyColumn {
    items(
        items = users,
        key = { user -> user.id }  // Always provide key!
    ) { user ->
        UserItem(user = user)
    }
}
```

#### remember with Keys

```kotlin
// Recompute only when userId changes
val userDetails = remember(userId) {
    expensiveComputation(userId)
}
```

#### derivedStateOf for Expensive Computations

```kotlin
val filteredList by remember(searchQuery, allItems) {
    derivedStateOf {
        allItems.filter { it.name.contains(searchQuery, ignoreCase = true) }
    }
}
```

## Best Practices Summary

1. **State Hoisting:** Hoist state to the lowest common ancestor
2. **Unidirectional Data Flow:** State flows down, events flow up
3. **Stateless Composables:** Prefer stateless composables for reusability
4. **Key Parameter:** Always provide keys for LazyColumn/LazyRow items
5. **Stability:** Mark custom classes as @Stable or @Immutable
6. **Side Effects:** Use appropriate effect handlers (LaunchedEffect, DisposableEffect)
7. **ViewModel:** Use ViewModel for screen-level state
8. **Preview:** Create @Preview functions for all composables
9. **Modifiers:** Accept Modifier as the first optional parameter
10. **Testing:** Extract business logic for unit testing

## Related Skills

- `android-hilt-di` - Dependency injection with Hilt
- `android-testing-patterns` - Testing Compose UIs
- `android-room-database` - Data persistence with Room

## Reference Files

| Resource | Purpose |
|----------|---------|
| `references/material3-theming-and-issues.md` | Material 3 Theming (Dynamic Color Theme, Custom Color Scheme, Typography) and Common Issues (Unnecessary Recompositions, State Lost on Configuration Change, Infinite Recomposition Loop, Navigation Memory Leak) |
