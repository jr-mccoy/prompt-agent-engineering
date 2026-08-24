---
title: "Hilt/Dagger to Swift Dependency Injection"
category: mobile-development
description: "Migrate Hilt and Dagger dependency injection to Swift patterns including constructor injection, Environment, Factory/Swinject, scope mapping, and testing support"
techniques:
  - ST-01
  - RT-02
  - DS-02
difficulty: intermediate
tags:
  - ios
  - android
  - migration
  - hilt
  - dagger
  - dependency-injection
  - swinject
  - testing
updated: "2026-03-19"
---

# Hilt/Dagger to Swift Dependency Injection

**Objective:** Translate Hilt/Dagger dependency injection patterns to Swift equivalents, covering constructor injection, scope management, module organization, and testing support. The output enables building a testable iOS app with the same separation of concerns that Hilt provides on Android.

**When to Use:** When migrating an Android app that uses Hilt or Dagger for dependency injection. iOS does not have a standard DI framework, so this prompt helps choose and implement the right pattern for the team's needs.

**Prompt Type:** Modular (~280 lines)

## Context Gathering

1. How many Hilt modules does the app define?
2. What scopes are used? (SingletonComponent, ViewModelComponent, ActivityComponent, FragmentComponent)
3. Are there `@Binds` vs. `@Provides` patterns?
4. How complex is the dependency graph? (depth, number of transitive dependencies)
5. Is assisted injection used? (`@AssistedInject`, `@AssistedFactory`)
6. Are there any multi-bindings? (`@IntoSet`, `@IntoMap`)
7. What is the team's preference — manual DI, lightweight library (Factory), or full framework (Swinject)?

## Instructions

### CRITICAL: Verification Requirements

- Every Hilt-injected dependency MUST have an iOS equivalent injection path
- Scope mapping MUST correctly translate Hilt component lifecycles to iOS
- Test configurations MUST allow swapping every dependency with a mock/fake
- Singleton scope MUST guarantee single instance across the app

### False-Positive Prevention

- ❌ DO NOT create a complex annotation-based DI system mimicking Hilt on iOS
- ✅ DO use Swift's native features (protocols, initializers, Environment) for simple DI
- ❌ DO NOT make everything a singleton — over-scoping is a common DI mistake
- ✅ DO match the original Hilt scopes: Singleton → app-wide, ViewModel → per-screen
- ❌ DO NOT inject ViewModels into other ViewModels
- ✅ DO inject UseCases/Repositories into ViewModels, keeping the same dependency direction
- ❌ DO NOT use service locator pattern (global access) when constructor injection works
- ✅ DO prefer explicit constructor injection for testability

### Step 1: Scope Mapping

| Hilt Component | Lifecycle | iOS Equivalent | Pattern |
|---------------|-----------|----------------|---------|
| `SingletonComponent` | App lifetime | `AppContainer` (single instance) | Static or Environment |
| `ActivityRetainedComponent` | Activity rotation-safe | N/A (iOS has no config changes) | Same as singleton |
| `ViewModelComponent` | ViewModel lifetime | Per-screen factory | Factory method |
| `ActivityComponent` | Activity lifecycle | Per-scene/window | SceneDelegate injection |
| `FragmentComponent` | Fragment lifecycle | Per-view | View initializer |
| `ServiceComponent` | Service lifecycle | N/A | Background task scope |

### Step 2: Module Translation

**Kotlin (Hilt modules):**
```kotlin
@Module
@InstallIn(SingletonComponent::class)
object NetworkModule {
    @Provides
    @Singleton
    fun provideOkHttpClient(): OkHttpClient =
        OkHttpClient.Builder()
            .addInterceptor(AuthInterceptor())
            .connectTimeout(30, TimeUnit.SECONDS)
            .build()

    @Provides
    @Singleton
    fun provideRetrofit(client: OkHttpClient): Retrofit =
        Retrofit.Builder()
            .baseUrl(BuildConfig.API_BASE_URL)
            .client(client)
            .addConverterFactory(MoshiConverterFactory.create())
            .build()

    @Provides
    @Singleton
    fun provideUserApi(retrofit: Retrofit): UserApi =
        retrofit.create(UserApi::class.java)
}

@Module
@InstallIn(SingletonComponent::class)
abstract class RepositoryModule {
    @Binds
    abstract fun bindUserRepository(impl: UserRepositoryImpl): UserRepository

    @Binds
    abstract fun bindSettingsRepository(impl: SettingsRepositoryImpl): SettingsRepository
}

@Module
@InstallIn(ViewModelComponent::class)
object UseCaseModule {
    @Provides
    fun provideGetUserProfile(
        userRepo: UserRepository,
        settingsRepo: SettingsRepository
    ): GetUserProfileUseCase = GetUserProfileUseCase(userRepo, settingsRepo)
}
```

**Swift (Protocol-based DI container):**
```swift
// MARK: - Container Protocol (enables test swapping)
protocol AppDependencies: Sendable {
    var userRepository: any UserRepository { get }
    var settingsRepository: any SettingsRepository { get }
    var userAPIService: any UserAPIService { get }

    func makeGetUserProfileUseCase() -> GetUserProfileUseCase
    func makeProfileViewModel(userId: String) -> ProfileViewModel
    func makeHomeViewModel() -> HomeViewModel
}

// MARK: - Production Container (equivalent to Hilt modules)
final class AppContainer: AppDependencies {
    // Singleton scope — equivalent to @Singleton @Provides
    let userAPIService: any UserAPIService
    let userRepository: any UserRepository
    let settingsRepository: any SettingsRepository

    init(baseURL: URL) {
        let session = URLSession(configuration: .default)
        self.userAPIService = URLSessionUserAPIService(
            session: session, baseURL: baseURL
        )
        self.userRepository = UserRepositoryImpl(
            apiService: userAPIService,
            localStore: SwiftDataUserStore()
        )
        self.settingsRepository = SettingsRepositoryImpl()
    }

    // Factory scope — equivalent to @Provides in ViewModelComponent
    func makeGetUserProfileUseCase() -> GetUserProfileUseCase {
        GetUserProfileUseCase(
            userRepository: userRepository,
            settingsRepository: settingsRepository
        )
    }

    func makeProfileViewModel(userId: String) -> ProfileViewModel {
        ProfileViewModel(
            userId: userId,
            getUserProfile: makeGetUserProfileUseCase()
        )
    }

    func makeHomeViewModel() -> HomeViewModel {
        HomeViewModel(userRepository: userRepository)
    }
}

// MARK: - SwiftUI Environment Integration
private struct DependenciesKey: EnvironmentKey {
    static let defaultValue: any AppDependencies = AppContainer(
        baseURL: URL(string: "https://api.example.com")!
    )
}

extension EnvironmentValues {
    var dependencies: any AppDependencies {
        get { self[DependenciesKey.self] }
        set { self[DependenciesKey.self] = newValue }
    }
}

// MARK: - Usage in SwiftUI
struct ProfileScreen: View {
    @Environment(\.dependencies) private var deps
    @State private var viewModel: ProfileViewModel?
    let userId: String

    var body: some View {
        Group {
            if let viewModel {
                ProfileContent(viewModel: viewModel)
            } else {
                ProgressView()
            }
        }
        .onAppear {
            viewModel = deps.makeProfileViewModel(userId: userId)
        }
    }
}
```

### Step 3: Test Container

**Kotlin (Hilt test replacement):**
```kotlin
@HiltAndroidTest
class ProfileViewModelTest {
    @get:Rule val hiltRule = HiltAndroidRule(this)

    @BindValue
    val userRepository: UserRepository = FakeUserRepository()

    @Inject
    lateinit var viewModel: ProfileViewModel
}
```

**Swift (test container swapping):**
```swift
// Test container — swap all dependencies with fakes
final class TestContainer: AppDependencies {
    let userRepository: any UserRepository
    let settingsRepository: any SettingsRepository
    let userAPIService: any UserAPIService

    init(
        userRepository: any UserRepository = FakeUserRepository(),
        settingsRepository: any SettingsRepository = FakeSettingsRepository(),
        userAPIService: any UserAPIService = FakeUserAPIService()
    ) {
        self.userRepository = userRepository
        self.settingsRepository = settingsRepository
        self.userAPIService = userAPIService
    }

    func makeGetUserProfileUseCase() -> GetUserProfileUseCase {
        GetUserProfileUseCase(
            userRepository: userRepository,
            settingsRepository: settingsRepository
        )
    }

    func makeProfileViewModel(userId: String) -> ProfileViewModel {
        ProfileViewModel(
            userId: userId,
            getUserProfile: makeGetUserProfileUseCase()
        )
    }

    func makeHomeViewModel() -> HomeViewModel {
        HomeViewModel(userRepository: userRepository)
    }
}

// Unit test
@Test func profileLoadsSuccessfully() async {
    let fakeRepo = FakeUserRepository()
    fakeRepo.stubbedUser = User(id: "1", name: "Alice")
    let container = TestContainer(userRepository: fakeRepo)
    let viewModel = container.makeProfileViewModel(userId: "1")

    await viewModel.loadProfile()

    #expect(viewModel.state == .success)
}

// SwiftUI preview with test dependencies
#Preview {
    ProfileScreen(userId: "1")
        .environment(\.dependencies, TestContainer())
}
```

### Step 4: Alternative — Factory Library

For teams that prefer a lighter approach similar to Hilt's annotation feel:

```swift
// Using Factory library (https://github.com/hmlongco/Factory)
import Factory

extension Container {
    var userAPIService: Factory<any UserAPIService> {
        self { URLSessionUserAPIService(baseURL: .apiBase) }
            .singleton
    }

    var userRepository: Factory<any UserRepository> {
        self { UserRepositoryImpl(
            apiService: self.userAPIService(),
            localStore: SwiftDataUserStore()
        )}
        .singleton
    }

    var getUserProfileUseCase: Factory<GetUserProfileUseCase> {
        self { GetUserProfileUseCase(
            userRepository: self.userRepository(),
            settingsRepository: self.settingsRepository()
        )}
    }
}

// Usage in ViewModel
@Observable
final class ProfileViewModel {
    @ObservationIgnored @Injected(\.getUserProfileUseCase)
    private var getUserProfile
}
```

## Expected Output

1. **DI container protocol** defining all injectable dependencies
2. **Production container** with singleton and factory scopes
3. **Test container** with configurable fakes
4. **SwiftUI Environment integration** for view-level injection
5. **Scope mapping table** from Hilt components to iOS patterns

## Example Interaction

**User:** Our Android app has 3 Hilt modules (Network, Repository, UseCase) with 12 singletons and 8 ViewModel-scoped providers. We want manual DI on iOS.

**Assistant:** Create a single `AppContainer` protocol with 12 stored properties (singletons) and 8 factory methods (ViewModel scope). Use SwiftUI Environment for injection into views.

## Techniques Used

| Technique | Application |
|-----------|-------------|
| **ST-01: Structured Task Decomposition** | Scope mapping, module translation, test support |
| **RT-02: Contextual Reference Integration** | Hilt, Dagger, SwiftUI Environment documentation |
| **DS-02: Output Specification Framework** | Container protocol, implementations, test patterns |

## Related Prompts

- `migration_architecture_adaptation.md` — Overall architecture including DI
- `migration_coroutines_to_swift_concurrency.md` — Async dependencies
- `migration_testing_strategy_adaptation.md` — Testing with DI

## Customization Guide

- **Swinject:** For large apps, Swinject provides a full-featured DI container with assembly pattern similar to Dagger modules.
- **Factory Library:** For a lightweight approach with property wrapper injection, use Factory (most popular Swift DI library).
- **Pure Manual DI:** For simplest approach, use initializer injection throughout and pass dependencies explicitly.
- **Modular Apps:** For multi-module iOS apps, create per-feature containers that compose into the root container.
