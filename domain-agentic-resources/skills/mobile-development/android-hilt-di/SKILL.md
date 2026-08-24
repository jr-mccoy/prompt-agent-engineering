---
name: android-hilt-di
description: Master Hilt dependency injection for Android including module design, scoping, ViewModel integration, and testing with Hilt. Use this skill when setting up dependency injection, creating Hilt modules, scoping dependencies, integrating with ViewModel, or when users mention "Hilt", "dependency injection", "@Inject", "@Module", "@Provides", "@HiltViewModel", "Dagger", or "DI setup".
metadata:
  tags:
    - android
    - hilt
    - mobile
    - testing
  updated: "2026-04-11"
---
# Android Hilt Dependency Injection

Comprehensive guidance for implementing dependency injection with Hilt, covering module design, scoping strategies, ViewModel integration, testing, and common patterns.

## Purpose

This skill provides patterns and best practices for Hilt dependency injection, helping developers:
- Set up Hilt in Android projects correctly
- Design modules with proper scoping
- Integrate Hilt with ViewModel, WorkManager, and other Jetpack components
- Implement constructor injection and field injection
- Test components with Hilt test utilities
- Debug common Hilt configuration issues

## When to Use This Skill

Use this skill when you need to:
- Set up Hilt dependency injection in a new or existing project
- Create Hilt modules for different dependency scopes
- Inject dependencies into ViewModels, Activities, Fragments
- Configure Hilt with Room, Retrofit, or other libraries
- Write tests with Hilt dependency replacement
- Troubleshoot Hilt compilation or runtime errors
- Migrate from Dagger to Hilt

## When NOT to Use This Skill

Do NOT use this skill when:
- Working with non-Android Kotlin/Java projects (use Dagger or Koin)
- Building iOS or cross-platform apps (use platform-specific DI)
- Project uses Koin and migration isn't planned
- Simple apps where manual DI is sufficient

## Setup

### Gradle Configuration

**Project-level build.gradle.kts:**
```kotlin
plugins {
    id("com.google.dagger.hilt.android") version "2.50" apply false
}
```

**App-level build.gradle.kts:**
```kotlin
plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
    id("com.google.dagger.hilt.android")
    id("com.google.devtools.ksp")  // or kapt
}

android {
    // ...
}

dependencies {
    implementation("com.google.dagger:hilt-android:2.50")
    ksp("com.google.dagger:hilt-compiler:2.50")

    // For ViewModel integration
    implementation("androidx.hilt:hilt-navigation-compose:1.1.0")

    // For WorkManager integration
    implementation("androidx.hilt:hilt-work:1.1.0")
    ksp("androidx.hilt:hilt-compiler:1.1.0")

    // Testing
    testImplementation("com.google.dagger:hilt-android-testing:2.50")
    kspTest("com.google.dagger:hilt-compiler:2.50")
    androidTestImplementation("com.google.dagger:hilt-android-testing:2.50")
    kspAndroidTest("com.google.dagger:hilt-compiler:2.50")
}
```

### Application Setup

```kotlin
@HiltAndroidApp
class MyApplication : Application() {
    // Hilt generates the necessary component hierarchy
}
```

## Core Patterns

### Module Design

#### Network Module

```kotlin
@Module
@InstallIn(SingletonComponent::class)
object NetworkModule {

    @Provides
    @Singleton
    fun provideOkHttpClient(): OkHttpClient {
        return OkHttpClient.Builder()
            .connectTimeout(30, TimeUnit.SECONDS)
            .readTimeout(30, TimeUnit.SECONDS)
            .addInterceptor(HttpLoggingInterceptor().apply {
                level = HttpLoggingInterceptor.Level.BODY
            })
            .build()
    }

    @Provides
    @Singleton
    fun provideMoshi(): Moshi {
        return Moshi.Builder()
            .add(KotlinJsonAdapterFactory())
            .build()
    }

    @Provides
    @Singleton
    fun provideRetrofit(
        okHttpClient: OkHttpClient,
        moshi: Moshi
    ): Retrofit {
        return Retrofit.Builder()
            .baseUrl(BuildConfig.API_BASE_URL)
            .client(okHttpClient)
            .addConverterFactory(MoshiConverterFactory.create(moshi))
            .build()
    }

    @Provides
    @Singleton
    fun provideApiService(retrofit: Retrofit): ApiService {
        return retrofit.create(ApiService::class.java)
    }
}
```

#### Database Module

```kotlin
@Module
@InstallIn(SingletonComponent::class)
object DatabaseModule {

    @Provides
    @Singleton
    fun provideDatabase(
        @ApplicationContext context: Context
    ): AppDatabase {
        return Room.databaseBuilder(
            context,
            AppDatabase::class.java,
            "app_database"
        )
            .addMigrations(MIGRATION_1_2)
            .build()
    }

    @Provides
    fun provideUserDao(database: AppDatabase): UserDao {
        return database.userDao()
    }

    @Provides
    fun provideTaskDao(database: AppDatabase): TaskDao {
        return database.taskDao()
    }
}
```

#### Repository Module

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
    abstract fun bindTaskRepository(
        impl: TaskRepositoryImpl
    ): TaskRepository
}
```

### Constructor Injection

#### Repository with Constructor Injection

```kotlin
class UserRepositoryImpl @Inject constructor(
    private val apiService: ApiService,
    private val userDao: UserDao,
    @IoDispatcher private val ioDispatcher: CoroutineDispatcher
) : UserRepository {

    override fun getUsers(): Flow<List<User>> =
        userDao.observeAll()
            .flowOn(ioDispatcher)

    override suspend fun refreshUsers() {
        withContext(ioDispatcher) {
            val users = apiService.getUsers()
            userDao.insertAll(users)
        }
    }
}
```

#### ViewModel with Hilt

```kotlin
@HiltViewModel
class UserListViewModel @Inject constructor(
    private val userRepository: UserRepository,
    private val savedStateHandle: SavedStateHandle
) : ViewModel() {

    private val _uiState = MutableStateFlow(UserListUiState())
    val uiState: StateFlow<UserListUiState> = _uiState.asStateFlow()

    init {
        loadUsers()
    }

    private fun loadUsers() {
        viewModelScope.launch {
            userRepository.getUsers()
                .collect { users ->
                    _uiState.update { it.copy(users = users, isLoading = false) }
                }
        }
    }

    fun refresh() {
        viewModelScope.launch {
            _uiState.update { it.copy(isLoading = true) }
            try {
                userRepository.refreshUsers()
            } catch (e: Exception) {
                _uiState.update { it.copy(error = e.message, isLoading = false) }
            }
        }
    }
}

data class UserListUiState(
    val users: List<User> = emptyList(),
    val isLoading: Boolean = true,
    val error: String? = null
)
```

### Scoping

#### Component Hierarchy and Scopes

```
SingletonComponent (@Singleton)
    └── ActivityRetainedComponent (@ActivityRetainedScoped)
        └── ViewModelComponent (@ViewModelScoped)
        └── ActivityComponent (@ActivityScoped)
            └── FragmentComponent (@FragmentScoped)
                └── ViewComponent (@ViewScoped)
            └── ViewComponent (@ViewScoped)
    └── ServiceComponent (@ServiceScoped)
```

#### Custom Scope Example

```kotlin
// Define a custom scope for feature modules
@Scope
@Retention(AnnotationRetention.RUNTIME)
annotation class FeatureScoped

// Use in module
@Module
@InstallIn(ActivityRetainedComponent::class)
object FeatureModule {

    @Provides
    @ActivityRetainedScoped
    fun provideFeatureManager(): FeatureManager {
        return FeatureManager()
    }
}
```

#### ViewModelScoped Dependencies

```kotlin
@Module
@InstallIn(ViewModelComponent::class)
object ViewModelModule {

    @Provides
    @ViewModelScoped
    fun provideAnalyticsTracker(
        @ApplicationContext context: Context
    ): AnalyticsTracker {
        return AnalyticsTracker(context)
    }
}
```

### Qualifiers

#### Dispatcher Qualifiers

```kotlin
@Qualifier
@Retention(AnnotationRetention.BINARY)
annotation class IoDispatcher

@Qualifier
@Retention(AnnotationRetention.BINARY)
annotation class MainDispatcher

@Qualifier
@Retention(AnnotationRetention.BINARY)
annotation class DefaultDispatcher

@Module
@InstallIn(SingletonComponent::class)
object DispatcherModule {

    @Provides
    @IoDispatcher
    fun provideIoDispatcher(): CoroutineDispatcher = Dispatchers.IO

    @Provides
    @MainDispatcher
    fun provideMainDispatcher(): CoroutineDispatcher = Dispatchers.Main

    @Provides
    @DefaultDispatcher
    fun provideDefaultDispatcher(): CoroutineDispatcher = Dispatchers.Default
}
```

#### API URL Qualifiers

```kotlin
@Qualifier
@Retention(AnnotationRetention.BINARY)
annotation class BaseUrl

@Qualifier
@Retention(AnnotationRetention.BINARY)
annotation class AuthUrl

@Module
@InstallIn(SingletonComponent::class)
object UrlModule {

    @Provides
    @BaseUrl
    fun provideBaseUrl(): String = BuildConfig.API_BASE_URL

    @Provides
    @AuthUrl
    fun provideAuthUrl(): String = BuildConfig.AUTH_URL
}
```

## Entry Points, Android Component Injection, Assisted Injection, Testing & Common Issues

Entry Points (AnalyticsEntryPoint/ContentProvider via EntryPointAccessors + HiltWorker/SyncWorker @AssistedInject with WorkManager configuration), Android Component Injection (Activity/Fragment field injection + `viewModels()`/`activityViewModels()`, Compose `hiltViewModel()` + NavHost scoping), Assisted Injection (NotificationFactory @AssistedFactory for runtime parameters), Testing (@HiltAndroidTest/@BindValue for fakes, @UninstallModules with FakeNetworkModule, HiltTestRunner extending AndroidJUnitRunner), Common Issues (MissingBinding/ViewModel injection not working/Scope Mismatch/Late Initialization in Tests), Best Practices Summary (10 points), Related Skills.

See [references/entry-points-injection-and-testing.md](references/entry-points-injection-and-testing.md)

---

## Reference Files

| Resource | Purpose |
|----------|---------|
| `references/entry-points-injection-and-testing.md` | Entry points, component injection, assisted injection, testing, common issues, best practices |
