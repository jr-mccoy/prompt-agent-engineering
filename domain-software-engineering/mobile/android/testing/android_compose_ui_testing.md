---
title: "Android Compose UI Testing"
category: mobile-development
description: "Implements effective UI tests for Jetpack Compose screens covering user interactions, state rendering, and accessibility using Compose Testing APIs"
tags:
  - android
  - mobile-development
  - testing
updated: "2026-03-19"
---

# Android Compose UI Testing

**Objective:** Implement effective UI tests for Jetpack Compose screens and components, covering user interactions, state rendering, accessibility, and navigation flows using Compose Testing APIs.

**When to Use:** Use this prompt when adding UI tests to Compose screens, when validating critical user flows end-to-end, when ensuring accessibility compliance through automated checks, or when protecting complex UI interactions from regressions.

**Prompt Type:** Modular (120-150 lines)

---

## Context Gathering

1. **Target Screens:**
   - "Which Compose screens need UI tests?"
   - "Are these standalone screens or part of a navigation flow?"

2. **Testing Scope:**
   - "Are you testing isolated components, full screens, or navigation flows?"
   - "Should tests include accessibility validation?"

3. **Dependencies:**
   - "Does the screen use a ViewModel? How is state provided?"
   - "Are there network calls or database operations to mock?"

---

## Instructions

### CRITICAL: Implementation Requirements

**Before generating ANY test, you MUST:**

1. **Understand the composable under test** - Read the actual implementation to understand state and interactions.
2. **Check for existing UI tests** - Search for existing Compose test patterns, rules, or utilities in the project.
3. **Follow project conventions** - Match existing test naming, semantic matchers, and assertion patterns.
4. **Provide specific, working tests** - All tests MUST include file paths and be immediately runnable.
5. **Include meaningful interactions** - Tests should verify real user scenarios, not just static rendering.

**Adapting to existing test patterns is required.** Match the project's testing style.

### Quality Requirements

- ❌ Do NOT generate tests that just assert composables exist without interaction
- ❌ Do NOT use hardcoded strings if test tags or content descriptions exist
- ❌ Do NOT generate flaky tests with arbitrary delays
- ❌ Do NOT skip accessibility assertions for user-facing UI
- ✅ DO use semantic matchers (testTag, contentDescription) consistently
- ✅ DO test state changes, not just initial state
- ✅ DO include navigation and flow tests for connected screens
- ✅ DO specify exact file paths for all test files

---

### Phase 1: Test Setup

#### 1.1 Dependencies

```kotlin
// build.gradle.kts
dependencies {
    // Compose Testing
    androidTestImplementation("androidx.compose.ui:ui-test-junit4:1.5.4")
    debugImplementation("androidx.compose.ui:ui-test-manifest:1.5.4")

    // Navigation Testing (if testing navigation)
    androidTestImplementation("androidx.navigation:navigation-testing:2.7.6")

    // Hilt Testing (if using Hilt)
    androidTestImplementation("com.google.dagger:hilt-android-testing:2.48.1")
    kspAndroidTest("com.google.dagger:hilt-compiler:2.48.1")
}
```

#### 1.2 Test Class Structure

```kotlin
@HiltAndroidTest // If using Hilt
class FeatureScreenTest {

    @get:Rule(order = 0)
    val hiltRule = HiltAndroidRule(this) // If using Hilt

    @get:Rule(order = 1)
    val composeTestRule = createAndroidComposeRule<ComponentActivity>()

    @Before
    fun setup() {
        hiltRule.inject() // If using Hilt
    }
}
```

---

### Phase 2: Component Testing Patterns

#### 2.1 Isolated Component Tests

```kotlin
@Test
fun `item card displays title and subtitle correctly`() {
    val testItem = Item(
        title = "Test Title",
        subtitle = "Test Subtitle",
        imageUrl = "https://example.com/image.jpg"
    )

    composeTestRule.setContent {
        AppTheme {
            ItemCard(
                item = testItem,
                onClick = {}
            )
        }
    }

    composeTestRule
        .onNodeWithText("Test Title")
        .assertIsDisplayed()

    composeTestRule
        .onNodeWithText("Test Subtitle")
        .assertIsDisplayed()
}

@Test
fun `item card click triggers callback`() {
    var clicked = false

    composeTestRule.setContent {
        AppTheme {
            ItemCard(
                item = testItem,
                onClick = { clicked = true }
            )
        }
    }

    composeTestRule
        .onNodeWithText(testItem.title)
        .performClick()

    assertThat(clicked).isTrue()
}
```

#### 2.2 Screen State Testing

```kotlin
@Test
fun `screen shows loading state initially`() {
    composeTestRule.setContent {
        FeatureScreen(
            uiState = FeatureUiState(isLoading = true),
            onEvent = {}
        )
    }

    composeTestRule
        .onNodeWithTag("loading_indicator")
        .assertIsDisplayed()
}

@Test
fun `screen shows content when data loaded`() {
    val items = listOf(
        Item("1", "Item 1"),
        Item("2", "Item 2")
    )

    composeTestRule.setContent {
        FeatureScreen(
            uiState = FeatureUiState(
                isLoading = false,
                items = items
            ),
            onEvent = {}
        )
    }

    composeTestRule
        .onNodeWithTag("content_list")
        .assertIsDisplayed()

    composeTestRule
        .onNodeWithText("Item 1")
        .assertIsDisplayed()
}

@Test
fun `screen shows empty state when no items`() {
    composeTestRule.setContent {
        FeatureScreen(
            uiState = FeatureUiState(
                isLoading = false,
                items = emptyList()
            ),
            onEvent = {}
        )
    }

    composeTestRule
        .onNodeWithTag("empty_state")
        .assertIsDisplayed()

    composeTestRule
        .onNodeWithText("No items found")
        .assertIsDisplayed()
}

@Test
fun `screen shows error state with retry button`() {
    composeTestRule.setContent {
        FeatureScreen(
            uiState = FeatureUiState(
                isLoading = false,
                error = "Network error"
            ),
            onEvent = {}
        )
    }

    composeTestRule
        .onNodeWithText("Network error")
        .assertIsDisplayed()

    composeTestRule
        .onNodeWithText("Retry")
        .assertIsDisplayed()
        .assertHasClickAction()
}
```

#### 2.3 User Interaction Testing

```kotlin
@Test
fun `typing in search field filters results`() {
    val onEvent = mockk<(FeatureEvent) -> Unit>(relaxed = true)

    composeTestRule.setContent {
        FeatureScreen(
            uiState = testUiState,
            onEvent = onEvent
        )
    }

    composeTestRule
        .onNodeWithTag("search_field")
        .performTextInput("query")

    verify { onEvent(FeatureEvent.OnSearchQueryChange("query")) }
}

@Test
fun `pull to refresh triggers refresh event`() {
    val onEvent = mockk<(FeatureEvent) -> Unit>(relaxed = true)

    composeTestRule.setContent {
        FeatureScreen(
            uiState = testUiState,
            onEvent = onEvent
        )
    }

    composeTestRule
        .onNodeWithTag("pull_refresh")
        .performTouchInput {
            swipeDown()
        }

    verify { onEvent(FeatureEvent.OnRefresh) }
}

@Test
fun `scrolling list loads more items`() {
    val onEvent = mockk<(FeatureEvent) -> Unit>(relaxed = true)
    val manyItems = (1..50).map { Item("$it", "Item $it") }

    composeTestRule.setContent {
        FeatureScreen(
            uiState = FeatureUiState(items = manyItems),
            onEvent = onEvent
        )
    }

    composeTestRule
        .onNodeWithTag("content_list")
        .performScrollToIndex(49)

    verify { onEvent(FeatureEvent.OnLoadMore) }
}
```

---

### Phase 3: Accessibility Testing

#### 3.1 Semantic Validation

```kotlin
@Test
fun `all interactive elements have content descriptions`() {
    composeTestRule.setContent {
        FeatureScreen(uiState = testUiState, onEvent = {})
    }

    // Verify all clickable items have descriptions
    composeTestRule
        .onAllNodes(hasClickAction())
        .assertAll(hasContentDescription())
}

@Test
fun `touch targets meet minimum size`() {
    composeTestRule.setContent {
        FeatureScreen(uiState = testUiState, onEvent = {})
    }

    // 48dp minimum touch target
    composeTestRule
        .onAllNodes(hasClickAction())
        .assertAll(hasMinimumTouchTargetSize())
}

@Test
fun `screen reader can navigate through content`() {
    composeTestRule.setContent {
        FeatureScreen(uiState = testUiState, onEvent = {})
    }

    // Verify heading exists for screen readers
    composeTestRule
        .onNode(hasAnyChild(isHeading()))
        .assertExists()
}
```

---

### Phase 4: Navigation Testing

#### 4.1 Navigation Flow Tests

```kotlin
@Test
fun `clicking item navigates to detail screen`() {
    val navController = TestNavHostController(ApplicationProvider.getApplicationContext())

    composeTestRule.setContent {
        navController.navigatorProvider.addNavigator(ComposeNavigator())
        AppNavHost(navController = navController)
    }

    // Start at list screen
    composeTestRule
        .onNodeWithText("Item 1")
        .performClick()

    // Verify navigation to detail
    assertThat(navController.currentDestination?.route)
        .isEqualTo("detail/{itemId}")
}

@Test
fun `back button returns to previous screen`() {
    val navController = TestNavHostController(ApplicationProvider.getApplicationContext())

    composeTestRule.setContent {
        navController.navigatorProvider.addNavigator(ComposeNavigator())
        AppNavHost(navController = navController, startDestination = "detail/123")
    }

    composeTestRule
        .onNodeWithContentDescription("Navigate back")
        .performClick()

    assertThat(navController.currentDestination?.route)
        .isEqualTo("list")
}
```

---

## Test Utilities

### Custom Matchers

```kotlin
// Minimum touch target matcher (48dp)
fun hasMinimumTouchTargetSize(): SemanticsMatcher {
    return SemanticsMatcher("has minimum touch target size") { node ->
        val bounds = node.boundsInRoot
        val minSize = 48.dp.toPx()
        bounds.width >= minSize && bounds.height >= minSize
    }
}

// Has content description matcher
fun hasContentDescription(): SemanticsMatcher {
    return SemanticsMatcher.keyIsDefined(SemanticsProperties.ContentDescription)
}
```

### Test Tags Best Practices

```kotlin
// In your composables
@Composable
fun FeatureScreen(...) {
    Column(Modifier.testTag("feature_screen")) {
        CircularProgressIndicator(Modifier.testTag("loading_indicator"))
        LazyColumn(Modifier.testTag("content_list")) { ... }
        EmptyState(Modifier.testTag("empty_state"))
    }
}
```

---

## Expected Output

```markdown
## Compose UI Tests for [ScreenName]

### Test Categories
| Category | Count | Coverage |
|----------|-------|----------|
| State Rendering | [X] | Loading, Content, Empty, Error |
| User Interactions | [X] | Clicks, Scrolls, Input |
| Accessibility | [X] | Content descriptions, Touch targets |
| Navigation | [X] | Forward/back navigation |

### Generated Tests
[Complete test class]
```

---

## Techniques Used

- **ST-01** (Clear Objective): UI test implementation
- **RT-04** (Best Practice Review): Compose Testing best practices
- **ST-03** (Output Format Templates): Consistent test patterns

---

## Related Prompts

- [android_test_strategy_design.md](android_test_strategy_design.md) - Overall test strategy
- [android_unit_test_generation.md](android_unit_test_generation.md) - ViewModel unit tests
- [android_screenshot_testing.md](android_screenshot_testing.md) - Visual regression testing
- [android_accessibility_improvement.md](../improvement/android_accessibility_improvement.md) - Accessibility audit
