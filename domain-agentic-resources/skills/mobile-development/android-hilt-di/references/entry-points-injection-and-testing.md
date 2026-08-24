# Android Hilt DI — Entry Points, Component Injection, Assisted Injection & Testing

## Entry Points

### For Non-Hilt Classes

```kotlin
@EntryPoint
@InstallIn(SingletonComponent::class)
interface AnalyticsEntryPoint {
    fun analyticsService(): AnalyticsService
}

// Usage in non-Hilt class (e.g., ContentProvider)
class MyContentProvider : ContentProvider() {
    override fun onCreate(): Boolean {
        val entryPoint = EntryPointAccessors.fromApplication(
            context!!.applicationContext,
            AnalyticsEntryPoint::class.java
        )
        val analyticsService = entryPoint.analyticsService()
        return true
    }
}
```

### For WorkManager

```kotlin
@HiltWorker
class SyncWorker @AssistedInject constructor(
    @Assisted context: Context,
    @Assisted workerParams: WorkerParameters,
    private val repository: UserRepository
) : CoroutineWorker(context, workerParams) {

    override suspend fun doWork(): Result {
        return try {
            repository.refreshUsers()
            Result.success()
        } catch (e: Exception) {
            Result.retry()
        }
    }
}

// WorkManager configuration in Application
@HiltAndroidApp
class MyApplication : Application(), Configuration.Provider {

    @Inject
    lateinit var workerFactory: HiltWorkerFactory

    override val workManagerConfiguration: Configuration
        get() = Configuration.Builder()
            .setWorkerFactory(workerFactory)
            .build()
}
```

---

## Android Component Injection

### Activity Injection

```kotlin
@AndroidEntryPoint
class MainActivity : AppCompatActivity() {

    @Inject
    lateinit var analyticsTracker: AnalyticsTracker

    private val viewModel: MainViewModel by viewModels()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        analyticsTracker.trackScreen("main")
    }
}
```

### Fragment Injection

```kotlin
@AndroidEntryPoint
class UserListFragment : Fragment() {

    @Inject
    lateinit var imageLoader: ImageLoader

    private val viewModel: UserListViewModel by viewModels()

    // For shared ViewModel with Activity
    private val sharedViewModel: SharedViewModel by activityViewModels()
}
```

### Compose Integration

```kotlin
@Composable
fun UserListScreen(
    viewModel: UserListViewModel = hiltViewModel()
) {
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()

    UserListContent(
        uiState = uiState,
        onRefresh = viewModel::refresh
    )
}

// Navigation with Hilt ViewModels
@Composable
fun AppNavHost() {
    val navController = rememberNavController()

    NavHost(navController = navController, startDestination = "home") {
        composable("home") {
            HomeScreen()  // Will get its own ViewModel instance
        }
        composable("profile/{userId}") { backStackEntry ->
            val userId = backStackEntry.arguments?.getString("userId")
            ProfileScreen(userId = userId)  // ViewModel scoped to this destination
        }
    }
}
```

---

## Assisted Injection

```kotlin
// For runtime parameters
class NotificationFactory @AssistedInject constructor(
    @Assisted private val notificationId: Int,
    private val context: Context,
    private val notificationManager: NotificationManager
) {
    @AssistedFactory
    interface Factory {
        fun create(notificationId: Int): NotificationFactory
    }

    fun show(title: String, message: String) {
        val notification = NotificationCompat.Builder(context, CHANNEL_ID)
            .setContentTitle(title)
            .setContentText(message)
            .build()
        notificationManager.notify(notificationId, notification)
    }
}

// Usage
@AndroidEntryPoint
class NotificationService : Service() {

    @Inject
    lateinit var notificationFactory: NotificationFactory.Factory

    fun showNotification(id: Int, title: String) {
        val factory = notificationFactory.create(id)
        factory.show(title, "Message")
    }
}
```

---

## Testing

### Unit Testing with Hilt

```kotlin
@HiltAndroidTest
@RunWith(AndroidJUnit4::class)
class UserRepositoryTest {

    @get:Rule
    var hiltRule = HiltAndroidRule(this)

    @Inject
    lateinit var repository: UserRepository

    @BindValue
    @JvmField
    val fakeApiService: ApiService = FakeApiService()

    @Before
    fun setup() {
        hiltRule.inject()
    }

    @Test
    fun getUsers_returnsExpectedData() = runTest {
        val users = repository.getUsers().first()
        assertEquals(2, users.size)
    }
}
```

### Replacing Modules in Tests

```kotlin
@Module
@InstallIn(SingletonComponent::class)
object FakeNetworkModule {

    @Provides
    @Singleton
    fun provideFakeApiService(): ApiService {
        return FakeApiService()
    }
}

@HiltAndroidTest
@UninstallModules(NetworkModule::class)
@RunWith(AndroidJUnit4::class)
class IntegrationTest {

    @get:Rule
    var hiltRule = HiltAndroidRule(this)

    @Inject
    lateinit var apiService: ApiService

    @Test
    fun testWithFakeService() {
        // apiService is FakeApiService
    }
}
```

### Custom Test Runner

```kotlin
class HiltTestRunner : AndroidJUnitRunner() {
    override fun newApplication(
        cl: ClassLoader?,
        className: String?,
        context: Context?
    ): Application {
        return super.newApplication(cl, HiltTestApplication::class.java.name, context)
    }
}

// In build.gradle.kts
android {
    defaultConfig {
        testInstrumentationRunner = "com.example.HiltTestRunner"
    }
}
```

---

## Common Issues

### Issue: Hilt Compilation Error - Missing Binding

**Error:**
```
error: [Dagger/MissingBinding] SomeClass cannot be provided without an @Inject constructor or an @Provides-annotated method.
```

**Resolution:**
```kotlin
// Option 1: Add @Inject constructor
class SomeClass @Inject constructor(
    private val dependency: Dependency
)

// Option 2: Create @Provides method in module
@Module
@InstallIn(SingletonComponent::class)
object SomeModule {
    @Provides
    fun provideSomeClass(dependency: Dependency): SomeClass {
        return SomeClass(dependency)
    }
}

// Option 3: For interfaces, use @Binds
@Module
@InstallIn(SingletonComponent::class)
abstract class SomeModule {
    @Binds
    abstract fun bindSomeInterface(impl: SomeClassImpl): SomeInterface
}
```

### Issue: ViewModel Injection Not Working

**Error:**
```
Cannot create an instance of class SomeViewModel
```

**Resolution:**
```kotlin
// Ensure ViewModel has @HiltViewModel annotation
@HiltViewModel
class SomeViewModel @Inject constructor(
    private val repository: Repository
) : ViewModel()

// Ensure Activity/Fragment has @AndroidEntryPoint
@AndroidEntryPoint
class SomeActivity : AppCompatActivity() {
    private val viewModel: SomeViewModel by viewModels()
}

// For Compose, use hiltViewModel()
@Composable
fun SomeScreen(viewModel: SomeViewModel = hiltViewModel())
```

### Issue: Scope Mismatch

**Error:**
```
error: [Dagger/IncompatiblyScopedBindings] ActivityComponent scoped bindings cannot depend on SingletonComponent
```

**Resolution:**
```kotlin
// Ensure dependencies flow from broader to narrower scopes
// SingletonComponent -> ActivityRetainedComponent -> ActivityComponent

// If ActivityScoped needs Singleton, inject it directly
@Module
@InstallIn(ActivityComponent::class)
object ActivityModule {
    @Provides
    @ActivityScoped
    fun provideActivityFeature(
        singletonDep: SingletonDependency  // This is fine
    ): ActivityFeature {
        return ActivityFeature(singletonDep)
    }
}
```

### Issue: Late Initialization in Tests

**Resolution:**
```kotlin
@HiltAndroidTest
class SomeTest {
    @get:Rule(order = 0)
    var hiltRule = HiltAndroidRule(this)

    @get:Rule(order = 1)
    var activityRule = ActivityScenarioRule(MainActivity::class.java)

    @Inject
    lateinit var dependency: Dependency

    @Before
    fun setup() {
        hiltRule.inject()  // Must call before using @Inject fields
    }
}
```

---

## Best Practices Summary

1. **Use Constructor Injection:** Prefer constructor injection over field injection
2. **Scope Appropriately:** Only scope when truly needed; unscoped is often fine
3. **Module Organization:** Group related bindings in focused modules
4. **Interface Abstraction:** Bind implementations to interfaces for testability
5. **Qualifiers:** Use qualifiers to distinguish same-type dependencies
6. **Assisted Injection:** Use for runtime parameters
7. **Test Replacement:** Use @UninstallModules and @BindValue for test fakes
8. **Entry Points:** Use sparingly; prefer constructor injection
9. **Lifecycle Awareness:** Match scope to component lifecycle
10. **Error Messages:** Read Hilt error messages carefully; they're descriptive

## Related Skills

- `android-room-database` - Room database module configuration
- `android-testing-patterns` - Testing with Hilt
- `jetpack-compose-patterns` - ViewModel injection in Compose
