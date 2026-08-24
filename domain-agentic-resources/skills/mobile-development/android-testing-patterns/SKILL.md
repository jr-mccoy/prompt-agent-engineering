---
name: android-testing-patterns
description: Comprehensive Android testing patterns for unit, integration, UI, and E2E testing. Use when writing tests for Android apps, setting up test infrastructure, or implementing test-driven development.
metadata:
  tags:
    - android
    - compose
    - espresso
    - kotlin
    - mobile-development
    - robolectric
    - testing
  updated: "2026-04-11"
---
# Android Testing Patterns

Comprehensive testing strategies for Android applications covering unit tests, integration tests, Compose UI tests, and Espresso tests.

## Purpose

- Write effective unit tests with MockK and coroutines
- Test Compose UI components
- Write Espresso tests for View-based UI
- Use Robolectric for fast local tests
- Organize test code for maintainability

## When to Use This Skill

- Setting up Android test infrastructure
- Writing unit tests for ViewModels and repositories
- Testing Jetpack Compose UI components
- Writing integration tests with Hilt
- Implementing test-driven development (TDD)
- Debugging flaky or failing tests
- Improving test coverage

## When NOT to Use

- For backend/server-side testing (use JUnit directly)
- For web application testing (use different frameworks)
- For cross-platform testing (use framework-specific tools)
- When tests need real device hardware features (use manual testing)

## Test Types Overview

| Type | Location | Speed | Scope | Framework |
|------|----------|-------|-------|-----------|
| Unit | Local JVM | Fast | Single class/function | JUnit4, MockK |
| Integration | Local/Device | Medium | Multiple components | JUnit4, Hilt |
| Compose UI | Local JVM | Medium | UI components | Compose Test |
| Espresso | Device/Emulator | Slow | Full screen/flow | Espresso |
| E2E | Device/Emulator | Slowest | Full app flow | Espresso, UIAutomator |

## Unit Testing

### ViewModel Testing

```kotlin
@ExtendWith(MockKExtension::class)
class UserViewModelTest {

    @get:Rule
    val mainDispatcherRule = MainDispatcherRule()

    @MockK
    private lateinit var userRepository: UserRepository

    private lateinit var viewModel: UserViewModel

    @BeforeEach
    fun setup() {
        viewModel = UserViewModel(userRepository)
    }

    @Test
    fun `loadUsers updates state with user list`() = runTest {
        // Given
        val users = listOf(User(1, "Alice"), User(2, "Bob"))
        coEvery { userRepository.getUsers() } returns flowOf(users)

        // When
        viewModel.loadUsers()

        // Then
        assertEquals(users, viewModel.uiState.value.users)
        assertFalse(viewModel.uiState.value.isLoading)
    }

    @Test
    fun `loadUsers sets error state on failure`() = runTest {
        // Given
        coEvery { userRepository.getUsers() } throws IOException("Network error")

        // When
        viewModel.loadUsers()

        // Then
        assertNotNull(viewModel.uiState.value.error)
        assertFalse(viewModel.uiState.value.isLoading)
    }
}

class MainDispatcherRule(
    private val dispatcher: TestDispatcher = UnconfinedTestDispatcher()
) : TestWatcher() {
    override fun starting(description: Description) {
        Dispatchers.setMain(dispatcher)
    }

    override fun finished(description: Description) {
        Dispatchers.resetMain()
    }
}
```

### Repository Testing

```kotlin
class UserRepositoryTest {

    private lateinit var repository: UserRepositoryImpl
    private val apiService: ApiService = mockk()
    private val userDao: UserDao = mockk()
    private val testDispatcher = StandardTestDispatcher()

    @Before
    fun setup() {
        repository = UserRepositoryImpl(apiService, userDao, testDispatcher)
    }

    @Test
    fun `getUsers returns cached data from database`() = runTest {
        // Given
        val cachedUsers = listOf(User(1, "Cached"))
        every { userDao.observeAll() } returns flowOf(cachedUsers)

        // When
        val result = repository.getUsers().first()

        // Then
        assertEquals(cachedUsers, result)
        coVerify(exactly = 0) { apiService.getUsers() }
    }

    @Test
    fun `refreshUsers fetches from API and saves to database`() = runTest {
        // Given
        val apiUsers = listOf(User(1, "From API"))
        coEvery { apiService.getUsers() } returns apiUsers
        coEvery { userDao.insertAll(any()) } returns Unit

        // When
        repository.refreshUsers()

        // Then
        coVerify { apiService.getUsers() }
        coVerify { userDao.insertAll(apiUsers) }
    }
}
```

### MockK Patterns

```kotlin
// Basic mocking
val repository: UserRepository = mockk()
every { repository.getUser(1) } returns User(1, "Test")

// Suspend function mocking
coEvery { repository.fetchUser(1) } returns User(1, "Test")

// Flow mocking
every { repository.observeUsers() } returns flowOf(listOf(User(1, "Test")))

// Verification
verify { repository.getUser(1) }
coVerify { repository.fetchUser(1) }
verify(exactly = 2) { repository.getUser(any()) }
verify(exactly = 0) { repository.deleteUser(any()) }

// Argument capture
val slot = slot<User>()
coEvery { repository.saveUser(capture(slot)) } returns Unit
repository.saveUser(User(1, "Test"))
assertEquals("Test", slot.captured.name)

// Relaxed mock (returns default values)
val relaxedMock: UserRepository = mockk(relaxed = true)

// Spy (partial mock)
val realRepository = UserRepositoryImpl()
val spy = spyk(realRepository)
every { spy.getUser(1) } returns User(1, "Mocked")
// Other methods call real implementation
```

### Testing Coroutines and Flow

```kotlin
class FlowTest {

    @Test
    fun `flow emits expected values`() = runTest {
        val flow = flow {
            emit(1)
            delay(100)
            emit(2)
            delay(100)
            emit(3)
        }

        val values = flow.toList()
        assertEquals(listOf(1, 2, 3), values)
    }

    @Test
    fun `stateFlow updates correctly`() = runTest {
        val viewModel = TestViewModel()

        // Collect in background
        val values = mutableListOf<State>()
        val job = launch(UnconfinedTestDispatcher()) {
            viewModel.state.toCollection(values)
        }

        viewModel.action1()
        viewModel.action2()

        assertEquals(3, values.size)
        assertEquals(State.Initial, values[0])
        assertEquals(State.Loading, values[1])
        assertEquals(State.Success, values[2])

        job.cancel()
    }

    @Test
    fun `turbine for flow testing`() = runTest {
        val viewModel = TestViewModel()

        viewModel.state.test {
            assertEquals(State.Initial, awaitItem())

            viewModel.loadData()

            assertEquals(State.Loading, awaitItem())
            assertEquals(State.Success, awaitItem())

            cancelAndIgnoreRemainingEvents()
        }
    }
}
```

## Compose UI Testing

### Basic Compose Test

```kotlin
class UserListScreenTest {

    @get:Rule
    val composeTestRule = createComposeRule()

    @Test
    fun `displays user list`() {
        // Given
        val users = listOf(
            User(1, "Alice"),
            User(2, "Bob")
        )

        // When
        composeTestRule.setContent {
            UserListScreen(users = users)
        }

        // Then
        composeTestRule.onNodeWithText("Alice").assertIsDisplayed()
        composeTestRule.onNodeWithText("Bob").assertIsDisplayed()
    }

    @Test
    fun `shows loading indicator when loading`() {
        composeTestRule.setContent {
            UserListScreen(
                users = emptyList(),
                isLoading = true
            )
        }

        composeTestRule
            .onNodeWithTag("loading_indicator")
            .assertIsDisplayed()
    }

    @Test
    fun `clicking user triggers callback`() {
        var clickedUser: User? = null
        val users = listOf(User(1, "Alice"))

        composeTestRule.setContent {
            UserListScreen(
                users = users,
                onUserClick = { clickedUser = it }
            )
        }

        composeTestRule.onNodeWithText("Alice").performClick()

        assertEquals(users.first(), clickedUser)
    }
}
```

### Semantics and Test Tags

```kotlin
// In production code
@Composable
fun UserCard(user: User, onClick: () -> Unit) {
    Card(
        onClick = onClick,
        modifier = Modifier
            .testTag("user_card_${user.id}")
            .semantics {
                contentDescription = "User ${user.name}"
            }
    ) {
        Text(
            text = user.name,
            modifier = Modifier.semantics { heading() }
        )
        Text(
            text = user.email,
            modifier = Modifier.testTag("user_email")
        )
    }
}

// In test code
@Test
fun `user card has correct semantics`() {
    val user = User(1, "Alice", "alice@email.com")

    composeTestRule.setContent {
        UserCard(user = user, onClick = {})
    }

    // By test tag
    composeTestRule
        .onNodeWithTag("user_card_1")
        .assertIsDisplayed()

    // By content description
    composeTestRule
        .onNodeWithContentDescription("User Alice")
        .assertIsDisplayed()

    // By text and semantic properties
    composeTestRule
        .onNode(hasText("Alice") and hasAnyAncestor(hasTestTag("user_card_1")))
        .assertIsDisplayed()
}
```

### Navigation Testing

```kotlin
class NavigationTest {

    @get:Rule
    val composeTestRule = createComposeRule()

    private lateinit var navController: TestNavHostController

    @Before
    fun setup() {
        composeTestRule.setContent {
            navController = TestNavHostController(LocalContext.current)
            navController.navigatorProvider.addNavigator(ComposeNavigator())

            AppNavHost(navController = navController)
        }
    }

    @Test
    fun `clicking profile navigates to profile screen`() {
        composeTestRule
            .onNodeWithText("Profile")
            .performClick()

        assertEquals("profile", navController.currentBackStackEntry?.destination?.route)
    }

    @Test
    fun `back press returns to previous screen`() {
        // Navigate to profile
        composeTestRule.onNodeWithText("Profile").performClick()

        // Press back
        composeTestRule.activityRule.scenario.onActivity {
            it.onBackPressedDispatcher.onBackPressed()
        }

        assertEquals("home", navController.currentBackStackEntry?.destination?.route)
    }
}
```

### Testing with Hilt

```kotlin
@HiltAndroidTest
class UserListScreenIntegrationTest {

    @get:Rule(order = 0)
    val hiltRule = HiltAndroidRule(this)

    @get:Rule(order = 1)
    val composeTestRule = createAndroidComposeRule<MainActivity>()

    @BindValue
    val fakeRepository: UserRepository = FakeUserRepository()

    @Before
    fun setup() {
        hiltRule.inject()
    }

    @Test
    fun `screen shows users from repository`() {
        (fakeRepository as FakeUserRepository).setUsers(
            listOf(User(1, "Test User"))
        )

        composeTestRule
            .onNodeWithText("Test User")
            .assertIsDisplayed()
    }
}
```

## Espresso, Robolectric & Test Organization

Espresso testing for view-based UI (LoginActivity, RecyclerView actions, IdlingResource for async operations), Robolectric for fast JVM-based Android testing with `ActivityScenario`, test naming conventions (`methodName_condition_expectedBehavior`), `TestFixtures` object for shared test data, fake repository implementations with `MutableStateFlow`, common issue resolutions (flaky Compose tests with `waitUntil`, test isolation with `clearAllMocks`, Espresso timeouts with `IdlingResource`), and best practices summary (test pyramid, AAA pattern, 80% coverage goal).

See [references/espresso-robolectric-and-test-organization.md](references/espresso-robolectric-and-test-organization.md)

---

## Reference Files

| Resource | Purpose |
|----------|---------|
| `references/espresso-robolectric-and-test-organization.md` | Espresso, Robolectric, test organization patterns, common issues, best practices |

## Related Skills

- `android-hilt-di` - DI testing with Hilt
- `jetpack-compose-patterns` - Compose UI development
- `android-room-database` - Database testing
