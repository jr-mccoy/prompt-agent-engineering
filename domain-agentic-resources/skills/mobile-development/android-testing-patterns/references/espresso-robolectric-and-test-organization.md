# Android Testing — Espresso, Robolectric & Test Organization

## Espresso Testing (View-based UI)

### Basic Espresso Test

```kotlin
@RunWith(AndroidJUnit4::class)
class LoginActivityTest {

    @get:Rule
    val activityRule = ActivityScenarioRule(LoginActivity::class.java)

    @Test
    fun loginWithValidCredentials_navigatesToHome() {
        // Enter username
        onView(withId(R.id.usernameEditText))
            .perform(typeText("testuser"), closeSoftKeyboard())

        // Enter password
        onView(withId(R.id.passwordEditText))
            .perform(typeText("password123"), closeSoftKeyboard())

        // Click login
        onView(withId(R.id.loginButton))
            .perform(click())

        // Verify navigation
        intended(hasComponent(HomeActivity::class.java.name))
    }

    @Test
    fun loginWithEmptyFields_showsError() {
        onView(withId(R.id.loginButton))
            .perform(click())

        onView(withId(R.id.errorTextView))
            .check(matches(isDisplayed()))
            .check(matches(withText("Please enter username and password")))
    }
}
```

### RecyclerView Testing

```kotlin
@Test
fun recyclerView_displaysItems() {
    // Verify item count
    onView(withId(R.id.recyclerView))
        .check(matches(hasChildCount(10)))

    // Verify specific item
    onView(withId(R.id.recyclerView))
        .perform(RecyclerViewActions.scrollToPosition<RecyclerView.ViewHolder>(5))

    onView(withRecyclerView(R.id.recyclerView).atPositionOnView(5, R.id.titleTextView))
        .check(matches(withText("Item 5")))

    // Click item
    onView(withId(R.id.recyclerView))
        .perform(RecyclerViewActions.actionOnItemAtPosition<RecyclerView.ViewHolder>(
            0, click()
        ))
}
```

### Idling Resources

```kotlin
class NetworkIdlingResource : IdlingResource {
    private var callback: IdlingResource.ResourceCallback? = null
    private var isIdle = true

    override fun getName(): String = "NetworkIdlingResource"

    override fun isIdleNow(): Boolean = isIdle

    override fun registerIdleTransitionCallback(callback: IdlingResource.ResourceCallback) {
        this.callback = callback
    }

    fun setIdle(idle: Boolean) {
        isIdle = idle
        if (idle) callback?.onTransitionToIdle()
    }
}

// In test
@Before
fun setup() {
    IdlingRegistry.getInstance().register(networkIdlingResource)
}

@After
fun teardown() {
    IdlingRegistry.getInstance().unregister(networkIdlingResource)
}
```

---

## Robolectric Testing

### Basic Robolectric Test

```kotlin
@RunWith(RobolectricTestRunner::class)
@Config(sdk = [Build.VERSION_CODES.TIRAMISU])
class UserActivityRobolectricTest {

    @Test
    fun `activity displays user name`() {
        val scenario = ActivityScenario.launch(UserActivity::class.java)

        scenario.onActivity { activity ->
            val textView = activity.findViewById<TextView>(R.id.nameTextView)
            assertEquals("John Doe", textView.text)
        }
    }

    @Test
    fun `button click updates text`() {
        val scenario = ActivityScenario.launch(UserActivity::class.java)

        scenario.onActivity { activity ->
            val button = activity.findViewById<Button>(R.id.updateButton)
            val textView = activity.findViewById<TextView>(R.id.nameTextView)

            button.performClick()

            assertEquals("Updated", textView.text)
        }
    }
}
```

### Testing with Context

```kotlin
@RunWith(RobolectricTestRunner::class)
class SharedPreferencesTest {

    private lateinit var context: Context

    @Before
    fun setup() {
        context = ApplicationProvider.getApplicationContext()
    }

    @Test
    fun `saves and retrieves value`() {
        val prefs = context.getSharedPreferences("test", Context.MODE_PRIVATE)

        prefs.edit().putString("key", "value").apply()

        assertEquals("value", prefs.getString("key", null))
    }
}
```

---

## Test Organization

### Test Naming Convention

```kotlin
// Pattern: methodName_condition_expectedBehavior
class UserViewModelTest {

    @Test
    fun `loadUsers_whenRepositorySucceeds_updatesStateWithUsers`() { }

    @Test
    fun `loadUsers_whenRepositoryFails_setsErrorState`() { }

    @Test
    fun `deleteUser_whenUserExists_removesFromList`() { }
}
```

### Test Fixtures

```kotlin
object TestFixtures {

    fun createUser(
        id: Long = 1,
        name: String = "Test User",
        email: String = "test@email.com"
    ) = User(id, name, email)

    fun createUserList(count: Int = 5) = (1..count).map { i ->
        createUser(id = i.toLong(), name = "User $i")
    }

    fun createTask(
        id: Long = 1,
        title: String = "Test Task",
        isCompleted: Boolean = false
    ) = Task(id, title, isCompleted)
}

// Usage
@Test
fun test() {
    val users = TestFixtures.createUserList(10)
    val task = TestFixtures.createTask(title = "Custom Title")
}
```

### Fake Implementations

```kotlin
class FakeUserRepository : UserRepository {

    private val users = MutableStateFlow<List<User>>(emptyList())
    private var shouldFail = false

    fun setUsers(userList: List<User>) {
        users.value = userList
    }

    fun setShouldFail(fail: Boolean) {
        shouldFail = fail
    }

    override fun getUsers(): Flow<List<User>> = users

    override suspend fun refreshUsers() {
        if (shouldFail) throw IOException("Fake network error")
    }

    override suspend fun saveUser(user: User) {
        users.update { it + user }
    }

    override suspend fun deleteUser(userId: Long) {
        users.update { it.filter { u -> u.id != userId } }
    }
}
```

---

## Common Issues

### Issue: Flaky Compose Tests

**Resolution:**
```kotlin
// Use waitUntil for async operations
composeTestRule.waitUntil(timeoutMillis = 5000) {
    composeTestRule
        .onAllNodesWithTag("user_item")
        .fetchSemanticsNodes().isNotEmpty()
}

// Use MainDispatcherRule for coroutine tests
@get:Rule
val mainDispatcherRule = MainDispatcherRule()

// Use advanceUntilIdle for pending coroutines
advanceUntilIdle()
```

### Issue: Tests Pass Individually but Fail Together

**Resolution:**
```kotlin
// Reset state in @Before and @After
@Before
fun setup() {
    clearAllMocks()
    repository = FakeUserRepository()
}

@After
fun teardown() {
    unmockkAll()
}

// Use unique test tags if needed
Modifier.testTag("user_card_${UUID.randomUUID()}")
```

### Issue: Espresso Timeout on Network Calls

**Resolution:**
```kotlin
// Use IdlingResource
IdlingRegistry.getInstance().register(OkHttp3IdlingResource.create("OkHttp", okHttpClient))

// Or mock network layer in tests
@BindValue
val fakeApiService: ApiService = FakeApiService()
```

---

## Best Practices Summary

1. **Test Pyramid:** Write more unit tests than integration tests, more integration than E2E
2. **Isolation:** Each test should be independent and not rely on test order
3. **AAA Pattern:** Arrange, Act, Assert structure for clarity
4. **Meaningful Names:** Test names should describe scenario and expected behavior
5. **Fakes over Mocks:** Prefer fake implementations for complex dependencies
6. **Test Public API:** Test behavior, not implementation details
7. **Coverage Goals:** Aim for 80%+ coverage on critical business logic
8. **CI Integration:** Run tests on every PR with clear failure reporting
9. **Flakiness:** Fix flaky tests immediately; they erode trust
10. **Performance:** Keep unit tests under 100ms each; use Robolectric wisely

## Related Skills

- `android-hilt-di` - DI testing with Hilt
- `jetpack-compose-patterns` - Compose UI development
- `android-room-database` - Database testing
