---
title: "Android Compose Screen Builder"
category: mobile-development
description: ""
tags:
  - android
  - mobile-development
updated: "2026-03-19"
---

# Android Compose Screen Builder

**Objective:** Build production-ready Jetpack Compose screens with proper architecture, state management, accessibility, and Material 3 design implementation following modern Android UI patterns.

**When to Use:** Use this prompt when implementing new screens in a Compose-based Android app. Ideal for converting designs to code, building feature screens, or creating reusable UI components. Best used after state design and navigation are defined.

**Prompt Type:** Comprehensive (350-450 lines)

---

## Context Gathering

Before building the screen, gather essential context:

1. **Design Specification:**
   - "Do you have design mockups or wireframes?"
   - "What Material 3 components does the screen use?"
   - "Are there specific animations or transitions required?"

2. **Screen Requirements:**
   - "What states does the screen need (loading, content, error, empty)?"
   - "What user interactions are supported?"
   - "Does the screen need pull-to-refresh, pagination, or real-time updates?"

3. **Existing Patterns:**
   - "Are there existing Compose components to reuse?"
   - "What theme/design system is in place?"
   - "Are there established patterns for common UI elements?"

4. **Data:**
   - "What data does this screen display?"
   - "Is there a ViewModel already defined?"
   - "How is navigation handled to/from this screen?"

---

## Instructions

### CRITICAL: Implementation Requirements

**Before implementing ANY code, you MUST:**

1. **Understand existing Compose patterns** - Check for existing composables, theme setup, and state management patterns in the codebase.
2. **Verify design specifications** - Confirm UI requirements, interaction patterns, and accessibility needs before building.
3. **Follow project conventions** - Match existing composable organization, naming, and theming patterns.
4. **Provide specific, working code** - All code samples MUST include file paths (e.g., `ui/screens/HomeScreen.kt`) and be copy-paste ready.
5. **Include preview annotations** - Provide @Preview composables for visual verification.

**Adapting to existing Compose patterns is preferred over introducing new approaches.** Match the project's existing style.

### Quality Requirements

- ❌ Do NOT introduce conflicting state management (e.g., don't add Redux if using vanilla StateFlow)
- ❌ Do NOT hardcode colors/dimensions outside the theme system
- ❌ Do NOT generate composables without proper state hoisting
- ❌ Do NOT skip accessibility (contentDescription, semantics)
- ✅ DO follow Material 3 guidelines where applicable
- ✅ DO provide proper recomposition optimization (remember, keys)
- ✅ DO include error and loading states
- ✅ DO specify exact file paths for all code changes

---

### Phase 1: Screen Architecture

#### 1.1 Screen Structure Pattern

Follow this layered screen pattern:

```kotlin
// Layer 1: Route - Navigation entry point
@Composable
fun FeatureRoute(
    onNavigateToDetail: (String) -> Unit,
    onNavigateBack: () -> Unit,
    viewModel: FeatureViewModel = hiltViewModel()
) {
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()

    // Handle one-time events
    ObserveEvents(viewModel.events) { event ->
        when (event) {
            is FeatureUiEvent.NavigateToDetail -> onNavigateToDetail(event.id)
            is FeatureUiEvent.NavigateBack -> onNavigateBack()
        }
    }

    FeatureScreen(
        uiState = uiState,
        onEvent = viewModel::onEvent
    )
}

// Layer 2: Screen - Scaffold and state-based content switching
@Composable
internal fun FeatureScreen(
    uiState: FeatureUiState,
    onEvent: (FeatureEvent) -> Unit
) {
    val snackbarHostState = remember { SnackbarHostState() }

    Scaffold(
        topBar = {
            FeatureTopBar(
                title = uiState.title,
                onBackClick = { onEvent(FeatureEvent.OnBackClick) }
            )
        },
        snackbarHost = { SnackbarHost(snackbarHostState) }
    ) { padding ->
        FeatureContent(
            uiState = uiState,
            onEvent = onEvent,
            modifier = Modifier.padding(padding)
        )
    }
}

// Layer 3: Content - Main content with state handling
@Composable
private fun FeatureContent(
    uiState: FeatureUiState,
    onEvent: (FeatureEvent) -> Unit,
    modifier: Modifier = Modifier
) {
    Box(modifier = modifier.fillMaxSize()) {
        when {
            uiState.isLoading -> LoadingContent()
            uiState.error != null -> ErrorContent(
                error = uiState.error,
                onRetry = { onEvent(FeatureEvent.Retry) }
            )
            uiState.items.isEmpty() -> EmptyContent(
                onAction = { onEvent(FeatureEvent.OnEmptyAction) }
            )
            else -> SuccessContent(
                items = uiState.items,
                onItemClick = { onEvent(FeatureEvent.OnItemClick(it)) }
            )
        }
    }
}
```

#### 1.2 Event Observation Helper

```kotlin
@Composable
fun <T> ObserveEvents(
    flow: Flow<T>,
    onEvent: (T) -> Unit
) {
    val lifecycleOwner = LocalLifecycleOwner.current

    LaunchedEffect(flow, lifecycleOwner) {
        lifecycleOwner.lifecycle.repeatOnLifecycle(Lifecycle.State.STARTED) {
            flow.collect(onEvent)
        }
    }
}
```

---

### Phase 2: Common Screen Patterns

**CHECKPOINT 1:** Confirm screen architecture before implementing patterns.

```markdown
## Screen Architecture Summary

### Screen Layers
| Layer | Responsibility |
|-------|---------------|
| Route | Navigation, ViewModel injection, events |
| Screen | Scaffold, top bar, state orchestration |
| Content | State-based UI switching |

### State Handling
| State | UI |
|-------|-----|
| Loading | [Shimmer/Spinner] |
| Error | [Error message + retry] |
| Empty | [Empty illustration + CTA] |
| Success | [Main content] |

**Proceed with content implementation?**
```

#### 2.1 List Screen Pattern

```kotlin
@OptIn(ExperimentalMaterial3Api::class)
@Composable
private fun ListContent(
    items: List<ItemUiModel>,
    isRefreshing: Boolean,
    hasMoreItems: Boolean,
    onRefresh: () -> Unit,
    onLoadMore: () -> Unit,
    onItemClick: (ItemUiModel) -> Unit,
    modifier: Modifier = Modifier
) {
    val pullToRefreshState = rememberPullToRefreshState()

    PullToRefreshBox(
        isRefreshing = isRefreshing,
        onRefresh = onRefresh,
        state = pullToRefreshState,
        modifier = modifier
    ) {
        LazyColumn(
            contentPadding = PaddingValues(16.dp),
            verticalArrangement = Arrangement.spacedBy(12.dp)
        ) {
            items(
                items = items,
                key = { it.id }
            ) { item ->
                ItemCard(
                    item = item,
                    onClick = { onItemClick(item) },
                    modifier = Modifier.animateItem()
                )
            }

            // Load more trigger
            if (hasMoreItems) {
                item(key = "load_more") {
                    LoadMoreTrigger(onLoadMore = onLoadMore)
                }
            }
        }
    }
}

@Composable
private fun LoadMoreTrigger(onLoadMore: () -> Unit) {
    LaunchedEffect(Unit) {
        onLoadMore()
    }

    Box(
        modifier = Modifier
            .fillMaxWidth()
            .padding(16.dp),
        contentAlignment = Alignment.Center
    ) {
        CircularProgressIndicator(
            modifier = Modifier.size(24.dp),
            strokeWidth = 2.dp
        )
    }
}
```

#### 2.2 Detail Screen Pattern

```kotlin
@Composable
private fun DetailContent(
    item: ItemDetailUiModel,
    onActionClick: () -> Unit,
    modifier: Modifier = Modifier
) {
    Column(
        modifier = modifier
            .fillMaxSize()
            .verticalScroll(rememberScrollState())
    ) {
        // Hero image
        AsyncImage(
            model = item.imageUrl,
            contentDescription = item.title,
            contentScale = ContentScale.Crop,
            modifier = Modifier
                .fillMaxWidth()
                .height(250.dp)
        )

        Column(
            modifier = Modifier.padding(16.dp),
            verticalArrangement = Arrangement.spacedBy(16.dp)
        ) {
            // Title section
            Text(
                text = item.title,
                style = MaterialTheme.typography.headlineMedium
            )

            // Metadata row
            Row(
                horizontalArrangement = Arrangement.spacedBy(16.dp)
            ) {
                MetadataChip(
                    icon = Icons.Default.CalendarToday,
                    text = item.formattedDate
                )
                MetadataChip(
                    icon = Icons.Default.Person,
                    text = item.author
                )
            }

            // Description
            Text(
                text = item.description,
                style = MaterialTheme.typography.bodyLarge
            )

            // Action button
            Button(
                onClick = onActionClick,
                modifier = Modifier.fillMaxWidth()
            ) {
                Text("Take Action")
            }
        }
    }
}
```

#### 2.3 Form Screen Pattern

```kotlin
@Composable
private fun FormContent(
    formState: FormUiState,
    onFieldChange: (FormField, String) -> Unit,
    onSubmit: () -> Unit,
    modifier: Modifier = Modifier
) {
    val focusManager = LocalFocusManager.current
    val scrollState = rememberScrollState()

    Column(
        modifier = modifier
            .fillMaxSize()
            .verticalScroll(scrollState)
            .padding(16.dp)
            .imePadding(),
        verticalArrangement = Arrangement.spacedBy(16.dp)
    ) {
        // Email field
        OutlinedTextField(
            value = formState.email,
            onValueChange = { onFieldChange(FormField.EMAIL, it) },
            label = { Text("Email") },
            isError = formState.emailError != null,
            supportingText = formState.emailError?.let { { Text(it) } },
            keyboardOptions = KeyboardOptions(
                keyboardType = KeyboardType.Email,
                imeAction = ImeAction.Next
            ),
            keyboardActions = KeyboardActions(
                onNext = { focusManager.moveFocus(FocusDirection.Down) }
            ),
            singleLine = true,
            modifier = Modifier.fillMaxWidth()
        )

        // Password field
        var passwordVisible by remember { mutableStateOf(false) }

        OutlinedTextField(
            value = formState.password,
            onValueChange = { onFieldChange(FormField.PASSWORD, it) },
            label = { Text("Password") },
            isError = formState.passwordError != null,
            supportingText = formState.passwordError?.let { { Text(it) } },
            visualTransformation = if (passwordVisible) {
                VisualTransformation.None
            } else {
                PasswordVisualTransformation()
            },
            trailingIcon = {
                IconButton(onClick = { passwordVisible = !passwordVisible }) {
                    Icon(
                        imageVector = if (passwordVisible) {
                            Icons.Default.VisibilityOff
                        } else {
                            Icons.Default.Visibility
                        },
                        contentDescription = if (passwordVisible) {
                            "Hide password"
                        } else {
                            "Show password"
                        }
                    )
                }
            },
            keyboardOptions = KeyboardOptions(
                keyboardType = KeyboardType.Password,
                imeAction = ImeAction.Done
            ),
            keyboardActions = KeyboardActions(
                onDone = {
                    focusManager.clearFocus()
                    if (formState.canSubmit) onSubmit()
                }
            ),
            singleLine = true,
            modifier = Modifier.fillMaxWidth()
        )

        Spacer(modifier = Modifier.weight(1f))

        // Submit button
        Button(
            onClick = onSubmit,
            enabled = formState.canSubmit,
            modifier = Modifier.fillMaxWidth()
        ) {
            if (formState.isSubmitting) {
                CircularProgressIndicator(
                    modifier = Modifier.size(20.dp),
                    strokeWidth = 2.dp,
                    color = MaterialTheme.colorScheme.onPrimary
                )
            } else {
                Text("Submit")
            }
        }
    }
}
```

---

### Phase 3: Reusable Components

#### 3.1 State Components

```kotlin
@Composable
fun LoadingContent(
    modifier: Modifier = Modifier
) {
    Box(
        modifier = modifier.fillMaxSize(),
        contentAlignment = Alignment.Center
    ) {
        CircularProgressIndicator()
    }
}

@Composable
fun ErrorContent(
    error: ErrorState,
    onRetry: () -> Unit,
    modifier: Modifier = Modifier
) {
    Column(
        modifier = modifier
            .fillMaxSize()
            .padding(32.dp),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center
    ) {
        Icon(
            imageVector = Icons.Default.ErrorOutline,
            contentDescription = null,
            modifier = Modifier.size(64.dp),
            tint = MaterialTheme.colorScheme.error
        )

        Spacer(modifier = Modifier.height(16.dp))

        Text(
            text = error.title,
            style = MaterialTheme.typography.titleLarge,
            textAlign = TextAlign.Center
        )

        Spacer(modifier = Modifier.height(8.dp))

        Text(
            text = error.message,
            style = MaterialTheme.typography.bodyMedium,
            textAlign = TextAlign.Center,
            color = MaterialTheme.colorScheme.onSurfaceVariant
        )

        if (error.canRetry) {
            Spacer(modifier = Modifier.height(24.dp))

            Button(onClick = onRetry) {
                Text("Try Again")
            }
        }
    }
}

@Composable
fun EmptyContent(
    title: String = "No items found",
    message: String? = null,
    actionLabel: String? = null,
    onAction: (() -> Unit)? = null,
    modifier: Modifier = Modifier
) {
    Column(
        modifier = modifier
            .fillMaxSize()
            .padding(32.dp),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center
    ) {
        Icon(
            imageVector = Icons.Default.Inbox,
            contentDescription = null,
            modifier = Modifier.size(64.dp),
            tint = MaterialTheme.colorScheme.outline
        )

        Spacer(modifier = Modifier.height(16.dp))

        Text(
            text = title,
            style = MaterialTheme.typography.titleMedium,
            textAlign = TextAlign.Center
        )

        message?.let {
            Spacer(modifier = Modifier.height(8.dp))
            Text(
                text = it,
                style = MaterialTheme.typography.bodyMedium,
                textAlign = TextAlign.Center,
                color = MaterialTheme.colorScheme.onSurfaceVariant
            )
        }

        if (actionLabel != null && onAction != null) {
            Spacer(modifier = Modifier.height(24.dp))
            OutlinedButton(onClick = onAction) {
                Text(actionLabel)
            }
        }
    }
}
```

#### 3.2 Card Components

```kotlin
@Composable
fun ItemCard(
    item: ItemUiModel,
    onClick: () -> Unit,
    modifier: Modifier = Modifier
) {
    Card(
        onClick = onClick,
        modifier = modifier.fillMaxWidth()
    ) {
        Row(
            modifier = Modifier
                .padding(16.dp)
                .fillMaxWidth(),
            horizontalArrangement = Arrangement.spacedBy(16.dp)
        ) {
            // Thumbnail
            AsyncImage(
                model = item.imageUrl,
                contentDescription = null,
                contentScale = ContentScale.Crop,
                modifier = Modifier
                    .size(80.dp)
                    .clip(RoundedCornerShape(8.dp))
            )

            // Content
            Column(
                modifier = Modifier.weight(1f),
                verticalArrangement = Arrangement.spacedBy(4.dp)
            ) {
                Text(
                    text = item.title,
                    style = MaterialTheme.typography.titleMedium,
                    maxLines = 2,
                    overflow = TextOverflow.Ellipsis
                )

                Text(
                    text = item.subtitle,
                    style = MaterialTheme.typography.bodyMedium,
                    color = MaterialTheme.colorScheme.onSurfaceVariant,
                    maxLines = 1,
                    overflow = TextOverflow.Ellipsis
                )

                Text(
                    text = item.metadata,
                    style = MaterialTheme.typography.bodySmall,
                    color = MaterialTheme.colorScheme.outline
                )
            }

            // Action
            Icon(
                imageVector = Icons.AutoMirrored.Default.KeyboardArrowRight,
                contentDescription = "View details",
                tint = MaterialTheme.colorScheme.outline
            )
        }
    }
}
```

---

### Phase 4: Accessibility & Polish

**CHECKPOINT 2:** Review components before adding accessibility.

```markdown
## Components Created

### Screen Components
| Component | Purpose |
|-----------|---------|
| FeatureRoute | Navigation entry |
| FeatureScreen | Scaffold wrapper |
| FeatureContent | State switching |
| ListContent | List pattern |

### Reusable Components
| Component | Purpose |
|-----------|---------|
| LoadingContent | Loading state |
| ErrorContent | Error with retry |
| EmptyContent | Empty state |
| ItemCard | List item |

**Ready for accessibility and polish?**
```

#### 4.1 Accessibility Implementation

```kotlin
@Composable
fun AccessibleItemCard(
    item: ItemUiModel,
    onClick: () -> Unit,
    modifier: Modifier = Modifier
) {
    Card(
        onClick = onClick,
        modifier = modifier
            .fillMaxWidth()
            .semantics {
                // Combine all text for screen readers
                contentDescription = "${item.title}. ${item.subtitle}. ${item.metadata}"
                // Indicate it's clickable
                role = Role.Button
            }
    ) {
        Row(
            modifier = Modifier.padding(16.dp),
            horizontalArrangement = Arrangement.spacedBy(16.dp)
        ) {
            AsyncImage(
                model = item.imageUrl,
                contentDescription = null, // Decorative, described in card semantics
                modifier = Modifier
                    .size(80.dp)
                    .clip(RoundedCornerShape(8.dp))
            )

            Column(modifier = Modifier.weight(1f)) {
                Text(
                    text = item.title,
                    style = MaterialTheme.typography.titleMedium
                )
                Text(
                    text = item.subtitle,
                    style = MaterialTheme.typography.bodyMedium
                )
            }

            Icon(
                imageVector = Icons.AutoMirrored.Default.KeyboardArrowRight,
                contentDescription = null // Part of card action, not separate
            )
        }
    }
}

// Minimum touch target
@Composable
fun AccessibleIconButton(
    onClick: () -> Unit,
    contentDescription: String,
    icon: ImageVector,
    modifier: Modifier = Modifier
) {
    IconButton(
        onClick = onClick,
        modifier = modifier.sizeIn(minWidth = 48.dp, minHeight = 48.dp)
    ) {
        Icon(
            imageVector = icon,
            contentDescription = contentDescription
        )
    }
}
```

#### 4.2 Loading Shimmer

```kotlin
@Composable
fun ShimmerLoadingContent(
    modifier: Modifier = Modifier
) {
    val shimmerColors = listOf(
        MaterialTheme.colorScheme.surfaceVariant.copy(alpha = 0.3f),
        MaterialTheme.colorScheme.surfaceVariant.copy(alpha = 0.5f),
        MaterialTheme.colorScheme.surfaceVariant.copy(alpha = 0.3f)
    )

    val transition = rememberInfiniteTransition(label = "shimmer")
    val translateAnimation = transition.animateFloat(
        initialValue = 0f,
        targetValue = 1000f,
        animationSpec = infiniteRepeatable(
            animation = tween(1200, easing = LinearEasing),
            repeatMode = RepeatMode.Restart
        ),
        label = "shimmer_translate"
    )

    val brush = Brush.linearGradient(
        colors = shimmerColors,
        start = Offset(translateAnimation.value - 200f, 0f),
        end = Offset(translateAnimation.value, 0f)
    )

    LazyColumn(
        contentPadding = PaddingValues(16.dp),
        verticalArrangement = Arrangement.spacedBy(12.dp),
        modifier = modifier
    ) {
        items(5) {
            ShimmerItemCard(brush = brush)
        }
    }
}

@Composable
private fun ShimmerItemCard(brush: Brush) {
    Card(modifier = Modifier.fillMaxWidth()) {
        Row(
            modifier = Modifier.padding(16.dp),
            horizontalArrangement = Arrangement.spacedBy(16.dp)
        ) {
            Box(
                modifier = Modifier
                    .size(80.dp)
                    .clip(RoundedCornerShape(8.dp))
                    .background(brush)
            )
            Column(
                modifier = Modifier.weight(1f),
                verticalArrangement = Arrangement.spacedBy(8.dp)
            ) {
                Box(
                    modifier = Modifier
                        .fillMaxWidth(0.7f)
                        .height(20.dp)
                        .clip(RoundedCornerShape(4.dp))
                        .background(brush)
                )
                Box(
                    modifier = Modifier
                        .fillMaxWidth(0.5f)
                        .height(16.dp)
                        .clip(RoundedCornerShape(4.dp))
                        .background(brush)
                )
            }
        }
    }
}
```

---

## Expected Output

### File Structure

```
feature/
├── FeatureRoute.kt       # Navigation entry point
├── FeatureScreen.kt      # Screen implementation
├── FeatureContent.kt     # Content with state handling
└── components/
    ├── ItemCard.kt
    ├── LoadingContent.kt
    ├── ErrorContent.kt
    ├── EmptyContent.kt
    └── ShimmerLoading.kt
```

### Implementation Checklist

- [ ] Route/Screen/Content layer separation
- [ ] State-based content switching
- [ ] Loading state (shimmer or spinner)
- [ ] Error state with retry
- [ ] Empty state with CTA
- [ ] Pull-to-refresh (if list)
- [ ] Pagination (if applicable)
- [ ] Accessibility: content descriptions
- [ ] Accessibility: touch targets (48dp min)
- [ ] Accessibility: semantic grouping
- [ ] Preview functions for all states

---

## Techniques Used

- **ST-01** (Clear Objective): Single-sentence objective for screen building
- **ST-02** (Sequential Instructions): Phased approach from architecture to polish
- **RT-02** (Multi-Dimensional Analysis): Covers structure, patterns, components
- **RT-04** (Best Practice Review): Compose and Material 3 best practices
- **ST-03** (Output Format Templates): Code templates for patterns
- **NE-02** (Phased Workflow): Clear phases with checkpoints

---

## Related Prompts

- [android_state_management.md](android_state_management.md) - Define state for screens
- [android_navigation_implementation.md](android_navigation_implementation.md) - Connect screens
- [android_accessibility_improvement.md](../improvement/android_accessibility_improvement.md) - Enhance accessibility
- [android_compose_ui_testing.md](../testing/android_compose_ui_testing.md) - Test Compose screens
- [android_ui_polish_audit.md](../improvement/android_ui_polish_audit.md) - Polish UI

---

## Customization Guide

### For Adaptive Layouts

Add multi-window support:
```kotlin
@Composable
fun AdaptiveFeatureScreen(uiState: UiState) {
    val windowSizeClass = currentWindowAdaptiveInfo().windowSizeClass

    if (windowSizeClass.windowWidthSizeClass == WindowWidthSizeClass.EXPANDED) {
        ListDetailLayout(uiState)
    } else {
        SinglePaneLayout(uiState)
    }
}
```

### For Design System Integration

Use your design tokens:
```kotlin
// Replace MaterialTheme references
Text(
    style = AppTheme.typography.titleLarge,
    color = AppTheme.colors.textPrimary
)
```

### For Animation-Heavy Screens

Add transitions:
```kotlin
AnimatedContent(
    targetState = uiState,
    transitionSpec = { fadeIn() togetherWith fadeOut() }
) { state ->
    when (state) {
        is Loading -> LoadingContent()
        is Success -> SuccessContent(state.data)
    }
}
```
