---
title: "AI Test Generation for Android"
category: mobile-development
description: "Use AI to generate comprehensive Android tests — unit tests for ViewModels and Repositories, Compose UI tests, integration tests with Firebase emulators, and edge case discovery"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-01
  - ED-05
difficulty: intermediate
tags:
  - android
  - testing
  - ai-assisted
  - unit-testing
  - compose-testing
  - mobile-development
updated: "2026-02-12"
---

# AI Test Generation for Android

**Objective:** Use AI coding agents to generate comprehensive Android tests — including unit tests for ViewModels and Repositories, Compose UI tests with interaction verification, integration tests with Firebase Emulator Suite, edge case discovery that a solo developer might miss, and test infrastructure setup — producing a test suite that catches regressions, validates behavior, and improves confidence in shipping.

**When to Use:** Use this prompt when you have untested ViewModels or Repositories, when adding tests to an existing codebase that lacks coverage, when you need to quickly add regression tests after fixing a bug, when preparing for a release and want to improve test confidence, or when setting up test infrastructure for a new project.

**Important context:** AI coding agents are excellent at generating tests because test code follows predictable patterns: Arrange (set up state), Act (execute the function), Assert (verify the result). For Android specifically, AI can generate ViewModel tests with Turbine for Flow testing, Repository tests with MockK for dependency mocking, and Compose UI tests with testing APIs. The key insight is that AI should generate the test structure and you should verify that the tests actually test meaningful behavior (not just that the code runs).

---

## Instructions

### Phase 1: ViewModel Unit Tests

**Provide the AI with:**
1. The ViewModel source code
2. The UiState sealed interface/class
3. The repository interface it depends on

**Prompt template:**
```
Generate comprehensive unit tests for [ViewModel].

Test framework: JUnit 5 + MockK + Turbine + kotlinx-coroutines-test
Test all UI states: Loading, Success, Error, Empty
Test all user actions: [list the public functions]
Test edge cases: null inputs, empty lists, network errors

Follow this test structure:
```kotlin
@OptIn(ExperimentalCoroutinesApi::class)
class MyViewModelTest {
    @get:Rule
    val mainDispatcherRule = MainDispatcherRule()

    private val repository = mockk<MyRepository>()
    private lateinit var viewModel: MyViewModel

    @BeforeEach
    fun setup() {
        viewModel = MyViewModel(repository)
    }

    @Test
    fun `initial state is Loading`() = runTest {
        viewModel.uiState.test {
            assertThat(awaitItem()).isEqualTo(MyUiState.Loading)
        }
    }
}
```

**Expected test categories:**

| Category | Tests | Priority |
|----------|-------|----------|
| Initial state | ViewModel emits correct initial UI state | HIGH |
| Success path | Happy path for each operation | HIGH |
| Error handling | Network error, server error, timeout | HIGH |
| Empty state | Empty list, no data | MEDIUM |
| Loading state | Loading indicator shown during operations | MEDIUM |
| State transitions | Correct sequence of state changes | MEDIUM |
| Edge cases | Rapid repeated calls, null responses, large datasets | LOW |
| Refresh/retry | Pull-to-refresh, retry after error | MEDIUM |

### Phase 2: Repository Unit Tests

**Prompt template:**
```
Generate unit tests for [Repository].

Dependencies to mock: [DAO], [API client], [DataStore]
Test: successful data retrieval, caching behavior, error mapping,
      offline fallback, data transformation from DTO to domain model.

Use MockK for mocking. Verify interactions (coVerify).
```

**Key patterns to test:**

```kotlin
@Test
fun `getItems returns cached data when available`() = runTest {
    val cachedItems = listOf(ItemEntity(id = "1", title = "Cached"))
    coEvery { dao.observeItems() } returns flowOf(cachedItems)

    repository.observeItems().test {
        val result = awaitItem()
        assertThat(result).hasSize(1)
        assertThat(result[0].title).isEqualTo("Cached")
        cancelAndIgnoreRemainingEvents()
    }

    // API should NOT be called if cache is fresh
    coVerify(exactly = 0) { api.fetchItems() }
}

@Test
fun `getItems falls back to network when cache is empty`() = runTest {
    coEvery { dao.observeItems() } returns flowOf(emptyList())
    coEvery { api.fetchItems() } returns ApiResponse.Success(listOf(ItemDto("1", "Remote")))
    coEvery { dao.upsertAll(any()) } just Runs

    // Trigger network fetch
    repository.refreshItems()

    coVerify { api.fetchItems() }
    coVerify { dao.upsertAll(any()) }
}
```

### Phase 3: Compose UI Tests

**Prompt template:**
```
Generate Compose UI tests for [Screen].

Test framework: Compose testing APIs
Test: UI element visibility, user interactions, state-driven UI changes,
     navigation triggers, accessibility (content descriptions, touch targets).

Use createComposeRule() and hiltViewModel mocking.
```

**UI test patterns:**

```kotlin
@HiltAndroidTest
class ItemListScreenTest {
    @get:Rule(order = 0)
    val hiltRule = HiltAndroidRule(this)

    @get:Rule(order = 1)
    val composeTestRule = createAndroidComposeRule<TestActivity>()

    @Test
    fun loadingState_showsProgressIndicator() {
        composeTestRule.setContent {
            ItemListScreen(uiState = ItemListUiState.Loading)
        }
        composeTestRule
            .onNodeWithTag("loading_indicator")
            .assertIsDisplayed()
    }

    @Test
    fun successState_showsItemList() {
        val items = listOf(Item("1", "First"), Item("2", "Second"))
        composeTestRule.setContent {
            ItemListScreen(uiState = ItemListUiState.Success(items))
        }
        composeTestRule.onNodeWithText("First").assertIsDisplayed()
        composeTestRule.onNodeWithText("Second").assertIsDisplayed()
    }

    @Test
    fun emptyState_showsEmptyMessage() {
        composeTestRule.setContent {
            ItemListScreen(uiState = ItemListUiState.Success(emptyList()))
        }
        composeTestRule.onNodeWithText("No items yet").assertIsDisplayed()
    }

    @Test
    fun clickItem_triggersNavigation() {
        var navigatedToId: String? = null
        val items = listOf(Item("1", "First"))

        composeTestRule.setContent {
            ItemListScreen(
                uiState = ItemListUiState.Success(items),
                onItemClick = { navigatedToId = it }
            )
        }

        composeTestRule.onNodeWithText("First").performClick()
        assertThat(navigatedToId).isEqualTo("1")
    }

    @Test
    fun pullToRefresh_triggersRefresh() {
        var refreshCalled = false
        composeTestRule.setContent {
            ItemListScreen(
                uiState = ItemListUiState.Success(emptyList()),
                onRefresh = { refreshCalled = true }
            )
        }

        composeTestRule.onNodeWithTag("item_list").performTouchInput {
            swipeDown()
        }
        assertThat(refreshCalled).isTrue()
    }
}
```

### Phase 4: Edge Case Discovery

**Ask AI to identify edge cases:**
```
Analyze [ViewModel/Screen/Feature] and identify edge cases that a solo developer
might miss. Consider:
- Race conditions (rapid user input, double-tap submit)
- State recovery (process death, configuration change, low memory)
- Data boundaries (empty, null, maximum length, special characters)
- Network conditions (offline, slow, timeout, partial failure)
- Concurrent operations (background sync during user edit)
- Device-specific (small screen, large font, RTL language, dark mode)
```

### Phase 5: Test Infrastructure

**MainDispatcherRule for coroutine testing:**

```kotlin
class MainDispatcherRule(
    private val testDispatcher: TestDispatcher = UnconfinedTestDispatcher()
) : TestWatcher() {
    override fun starting(description: Description) {
        Dispatchers.setMain(testDispatcher)
    }
    override fun finished(description: Description) {
        Dispatchers.resetMain()
    }
}
```

**Test fakes for common Android dependencies:**

```kotlin
// Fake repository for UI tests
class FakeItemRepository : ItemRepository {
    var items = mutableListOf<Item>()
    var shouldThrow = false

    override fun observeItems(): Flow<List<Item>> =
        if (shouldThrow) flow { throw IOException("Network error") }
        else flowOf(items)
}
```

---

## Expected Output

1. **ViewModel test suite** — tests for all UI states, user actions, and error cases
2. **Repository test suite** — tests for data operations, caching, and error mapping
3. **Compose UI test suite** — tests for rendering, interaction, and accessibility
4. **Edge case report** — identified edge cases with test implementations
5. **Test infrastructure** — dispatcher rules, fakes, and test utilities
6. **Coverage assessment** — what percentage of critical paths are covered

---

## CRITICAL: Verification Requirements

- [ ] All generated tests actually pass (compile + run)
- [ ] Tests verify behavior, not implementation details (mock interactions are secondary to state assertions)
- [ ] Edge cases are tested (not just happy path)
- [ ] Compose tests use semantic assertions (`onNodeWithText`) not implementation details (`onNodeWithTag` only for disambiguation)
- [ ] Tests don't depend on timing (`Thread.sleep` is never used — use Turbine and TestDispatcher)
- [ ] Test names describe the scenario and expected behavior
