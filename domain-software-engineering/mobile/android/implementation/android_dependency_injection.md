---
title: "Android Dependency Injection"
category: mobile-development
description: ""
tags:
  - android
  - mobile-development
updated: "2026-03-19"
---

# Android Dependency Injection

**Objective:** Configure dependency injection using Hilt to manage dependencies throughout an Android application with proper scoping, testing support, and clean architecture alignment.

**When to Use:** Use this prompt when setting up DI for a new Android project, migrating from manual DI or another framework, or adding new modules to an existing Hilt setup. Ideal after architecture decisions are made and component interfaces are defined.

**Prompt Type:** Modular (120-150 lines)

---

## Context Gathering

Before configuring DI, gather essential context:

1. **Current Setup:**
   - "Is dependency injection already configured? Which framework?"
   - "Is the app single-module or multi-module?"
   - "Are there existing singleton instances to migrate?"

2. **Architecture:**
   - "What layers exist (UI, domain, data)?"
   - "What components need to be injected (ViewModels, repositories, APIs)?"
   - "Are there any scoped dependencies (per-activity, per-feature)?"

3. **Testing:**
   - "Do you need to replace dependencies in tests?"
   - "What testing frameworks are used (JUnit, Robolectric, Espresso)?"

---

## Instructions

### CRITICAL: Implementation Requirements

**Before implementing ANY code, you MUST:**

1. **Understand existing DI setup** - Check if Hilt, Dagger, Koin, or manual DI is already configured. Don't mix DI frameworks.
2. **Verify scope requirements** - Confirm the lifecycle requirements for each dependency before choosing scopes.
3. **Follow project conventions** - Match existing module organization, naming conventions, and injection patterns.
4. **Provide specific, working code** - All code samples MUST include file paths (e.g., `di/NetworkModule.kt`) and be copy-paste ready.
5. **Include proper testing setup** - Provide test module configurations where applicable.

**Adapting to existing DI patterns is preferred over introducing new approaches.** If DI is already configured, extend it rather than restructuring.

### Quality Requirements

- ❌ Do NOT mix DI frameworks (e.g., don't add Koin modules to a Hilt project)
- ❌ Do NOT use overly broad scopes (@Singleton) without justification
- ❌ Do NOT generate placeholder bindings without proper implementation
- ❌ Do NOT skip interface abstractions for testable dependencies
- ✅ DO follow the existing component hierarchy
- ✅ DO provide proper scope annotations based on actual lifecycle needs
- ✅ DO include companion @TestInstallIn modules for testing
- ✅ DO specify exact file paths for all code changes

---

### Phase 1: Hilt Setup

#### 1.1 Dependencies Configuration

```kotlin
// build.gradle.kts (Project)
plugins {
    id("com.google.dagger.hilt.android") version "2.51" apply false
    id("com.google.devtools.ksp") version "1.9.0-1.0.13" apply false
}

// build.gradle.kts (App Module)
plugins {
    id("com.google.dagger.hilt.android")
    id("com.google.devtools.ksp")
}

dependencies {
    implementation("com.google.dagger:hilt-android:2.51")
    ksp("com.google.dagger:hilt-android-compiler:2.51")

    // For ViewModel injection
    implementation("androidx.hilt:hilt-navigation-compose:1.2.0")

    // For testing
    testImplementation("com.google.dagger:hilt-android-testing:2.51")
    kspTest("com.google.dagger:hilt-android-compiler:2.51")
    androidTestImplementation("com.google.dagger:hilt-android-testing:2.51")
    kspAndroidTest("com.google.dagger:hilt-android-compiler:2.51")
}
```

#### 1.2 Application Setup

```kotlin
@HiltAndroidApp
class MyApplication : Application() {
    // Hilt generates the DI container
}

// MainActivity.kt
@AndroidEntryPoint
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            AppTheme {
                AppNavigation()
            }
        }
    }
}
```

---

### Phase 2: Module Configuration

#### 2.1 Network Module

```kotlin
@Module
@InstallIn(SingletonComponent::class)
object NetworkModule {

    @Provides
    @Singleton
    fun provideJson(): Json = Json {
        ignoreUnknownKeys = true
        coerceInputValues = true
    }

    @Provides
    @Singleton
    fun provideOkHttpClient(
        authInterceptor: AuthInterceptor
    ): OkHttpClient = OkHttpClient.Builder()
        .addInterceptor(authInterceptor)
        .connectTimeout(30, TimeUnit.SECONDS)
        .build()

    @Provides
    @Singleton
    fun provideRetrofit(
        okHttpClient: OkHttpClient,
        json: Json
    ): Retrofit = Retrofit.Builder()
        .baseUrl(BuildConfig.API_BASE_URL)
        .client(okHttpClient)
        .addConverterFactory(json.asConverterFactory("application/json".toMediaType()))
        .build()

    @Provides
    @Singleton
    fun provideApiService(retrofit: Retrofit): ApiService =
        retrofit.create(ApiService::class.java)
}
```

#### 2.2 Database Module

```kotlin
@Module
@InstallIn(SingletonComponent::class)
object DatabaseModule {

    @Provides
    @Singleton
    fun provideDatabase(
        @ApplicationContext context: Context
    ): AppDatabase = Room.databaseBuilder(
        context,
        AppDatabase::class.java,
        "app_database"
    ).build()

    @Provides
    fun provideUserDao(database: AppDatabase): UserDao =
        database.userDao()

    @Provides
    fun provideItemDao(database: AppDatabase): ItemDao =
        database.itemDao()
}
```

#### 2.3 Repository Module

```kotlin
@Module
@InstallIn(SingletonComponent::class)
abstract class RepositoryModule {

    @Binds
    @Singleton
    abstract fun bindUserRepository(
        impl: UserRepositoryImpl
    ): UserRepository

    @Binds
    @Singleton
    abstract fun bindItemRepository(
        impl: ItemRepositoryImpl
    ): ItemRepository
}

// Alternative: Using @Provides for more control
@Module
@InstallIn(SingletonComponent::class)
object RepositoryModule {

    @Provides
    @Singleton
    fun provideUserRepository(
        localDataSource: UserLocalDataSource,
        remoteDataSource: UserRemoteDataSource,
        dispatchers: DispatcherProvider
    ): UserRepository = UserRepositoryImpl(
        localDataSource,
        remoteDataSource,
        dispatchers
    )
}
```

#### 2.4 Dispatcher Module

```kotlin
@Module
@InstallIn(SingletonComponent::class)
object DispatcherModule {

    @Provides
    @Singleton
    fun provideDispatcherProvider(): DispatcherProvider =
        DefaultDispatcherProvider()
}

interface DispatcherProvider {
    val main: CoroutineDispatcher
    val io: CoroutineDispatcher
    val default: CoroutineDispatcher
}

class DefaultDispatcherProvider : DispatcherProvider {
    override val main: CoroutineDispatcher = Dispatchers.Main
    override val io: CoroutineDispatcher = Dispatchers.IO
    override val default: CoroutineDispatcher = Dispatchers.Default
}
```

---

### Phase 3: Component Injection

#### 3.1 ViewModel Injection

```kotlin
@HiltViewModel
class UserViewModel @Inject constructor(
    private val userRepository: UserRepository,
    private val savedStateHandle: SavedStateHandle
) : ViewModel() {
    // ViewModel implementation
}

// In Compose
@Composable
fun UserScreen(
    viewModel: UserViewModel = hiltViewModel()
) {
    // Use viewModel
}

// For scoped ViewModel (shared between screens)
@Composable
fun FeatureNavGraph() {
    val navController = rememberNavController()

    NavHost(navController, startDestination = "list") {
        composable("list") { backStackEntry ->
            val parentEntry = remember(backStackEntry) {
                navController.getBackStackEntry("feature_graph")
            }
            val sharedViewModel: SharedViewModel = hiltViewModel(parentEntry)
            ListScreen(sharedViewModel)
        }

        composable("detail") { backStackEntry ->
            val parentEntry = remember(backStackEntry) {
                navController.getBackStackEntry("feature_graph")
            }
            val sharedViewModel: SharedViewModel = hiltViewModel(parentEntry)
            DetailScreen(sharedViewModel)
        }
    }
}
```

#### 3.2 Constructor Injection

```kotlin
// Automatically injectable (no module needed)
class UserRepositoryImpl @Inject constructor(
    private val localDataSource: UserLocalDataSource,
    private val remoteDataSource: UserRemoteDataSource,
    private val mapper: UserMapper
) : UserRepository {
    // Implementation
}

class UserLocalDataSource @Inject constructor(
    private val dao: UserDao
) {
    // Implementation
}

class UserMapper @Inject constructor() {
    // Implementation
}
```

#### 3.3 Qualifiers

```kotlin
@Qualifier
@Retention(AnnotationRetention.BINARY)
annotation class IoDispatcher

@Qualifier
@Retention(AnnotationRetention.BINARY)
annotation class DefaultDispatcher

@Module
@InstallIn(SingletonComponent::class)
object DispatcherModule {

    @IoDispatcher
    @Provides
    fun provideIoDispatcher(): CoroutineDispatcher = Dispatchers.IO

    @DefaultDispatcher
    @Provides
    fun provideDefaultDispatcher(): CoroutineDispatcher = Dispatchers.Default
}

// Usage
class UserRepository @Inject constructor(
    @IoDispatcher private val ioDispatcher: CoroutineDispatcher
) { ... }
```

---

### Phase 4: Testing Setup

#### 4.1 Test Module Replacement

```kotlin
@Module
@TestInstallIn(
    components = [SingletonComponent::class],
    replaces = [NetworkModule::class]
)
object FakeNetworkModule {

    @Provides
    @Singleton
    fun provideApiService(): ApiService = FakeApiService()
}

// Or use @UninstallModules in specific tests
@HiltAndroidTest
@UninstallModules(NetworkModule::class)
class UserRepositoryTest {

    @Module
    @InstallIn(SingletonComponent::class)
    object TestModule {
        @Provides
        @Singleton
        fun provideApiService(): ApiService = mockk()
    }

    @get:Rule
    var hiltRule = HiltAndroidRule(this)

    @Inject
    lateinit var repository: UserRepository

    @Before
    fun setup() {
        hiltRule.inject()
    }

    @Test
    fun testGetUser() = runTest {
        // Test implementation
    }
}
```

---

## Expected Output

### File Structure

```
di/
├── NetworkModule.kt
├── DatabaseModule.kt
├── RepositoryModule.kt
├── DispatcherModule.kt
└── Qualifiers.kt
```

### Implementation Checklist

- [ ] Hilt Gradle plugin configured
- [ ] Application class annotated with @HiltAndroidApp
- [ ] Activity annotated with @AndroidEntryPoint
- [ ] NetworkModule for API dependencies
- [ ] DatabaseModule for Room dependencies
- [ ] RepositoryModule binding interfaces to implementations
- [ ] DispatcherModule for coroutine dispatchers
- [ ] ViewModels annotated with @HiltViewModel
- [ ] Test modules for dependency replacement

---

## Techniques Used

- **ST-01** (Clear Objective): Single-sentence objective for DI setup
- **ST-02** (Sequential Instructions): Phased approach from setup to testing
- **RT-04** (Best Practice Review): Hilt best practices
- **ST-03** (Output Format Templates): Module templates

---

## Related Prompts

- [android_data_layer_implementation.md](android_data_layer_implementation.md) - Inject data layer components
- [android_api_integration.md](android_api_integration.md) - Inject network components
- [android_unit_test_generation.md](../testing/android_unit_test_generation.md) - Test with DI
- [android_module_design.md](../planning/android_module_design.md) - Multi-module DI setup

---

## Customization Guide

### For Multi-Module Projects

Configure Hilt in feature modules:
```kotlin
// Feature module build.gradle.kts
plugins {
    id("com.google.dagger.hilt.android")
    id("com.google.devtools.ksp")
}

// Feature-specific module
@Module
@InstallIn(SingletonComponent::class)
abstract class FeatureModule {
    @Binds
    abstract fun bindFeatureRepository(impl: FeatureRepositoryImpl): FeatureRepository
}
```

### For Koin Migration

Hilt equivalents of Koin concepts:
- `single { }` → `@Provides @Singleton`
- `factory { }` → `@Provides` (no scope)
- `viewModel { }` → `@HiltViewModel`
- `get()` → `@Inject constructor()`

### For Manual DI Migration

Replace manual factories:
- ServiceLocator → Hilt modules
- Factory classes → `@Provides` functions
- Singleton holders → `@Singleton` scope
