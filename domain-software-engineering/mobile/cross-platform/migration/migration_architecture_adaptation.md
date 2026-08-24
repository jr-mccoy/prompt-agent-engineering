---
title: "Architecture Adaptation - Clean Architecture to iOS"
category: mobile-development
description: "Adapt Clean Architecture with Hilt, Repository, and UseCase patterns from Android to iOS using protocol-oriented design, Swift concurrency, and native dependency injection"
techniques:
  - ST-01
  - RT-02
  - RT-04
  - DS-02
difficulty: advanced
tags:
  - ios
  - android
  - migration
  - clean-architecture
  - protocol-oriented-design
  - hilt
  - dependency-injection
updated: "2026-03-19"
---

# Architecture Adaptation - Clean Architecture to iOS

**Objective:** Systematically translate an Android Clean Architecture implementation (Hilt DI, Repository pattern, UseCase classes, ViewModel + LiveData/StateFlow) into an idiomatic iOS architecture using Swift protocols, @Observable, structured concurrency, and native or lightweight DI patterns.

**When to Use:** When migrating a well-structured Android app that follows Clean Architecture to iOS. This prompt assumes the Android codebase has clear layer separation (data, domain, presentation) and uses Hilt for dependency injection. It produces the iOS architectural blueprint that preserves the same separation of concerns.

**Prompt Type:** Comprehensive (~350 lines)

## Context Gathering

1. What are the architectural layers in the Android app? (e.g., data, domain, presentation, core)
2. What DI framework is used? (Hilt, Koin, manual)
3. How are ViewModels structured? (one per screen, shared ViewModels, SavedStateHandle usage)
4. What patterns do UseCase classes follow? (single invoke method, parameterized, streaming)
5. How is the Repository pattern implemented? (single source of truth, offline-first, cache strategy)
6. Are there any cross-cutting concerns? (logging, analytics, error handling middleware)
7. What reactive patterns are used? (StateFlow, SharedFlow, LiveData, Channel)
8. How is error handling structured? (sealed Result class, exceptions, Either)

## Instructions

### CRITICAL: Verification Requirements

- Architecture layer mapping MUST preserve the same dependency rules (inner layers cannot depend on outer layers)
- Protocol definitions MUST match the behavioral contract of their Kotlin interface counterparts
- ViewModel adaptation MUST account for SwiftUI's lifecycle differences
- DI patterns MUST support testability at the same level as Hilt

### False-Positive Prevention

- ❌ DO NOT create a God-object AppContainer that violates single responsibility
- ✅ DO create focused DI containers per feature module
- ❌ DO NOT use singletons for stateful dependencies
- ✅ DO use SwiftUI Environment or explicit injection for testable dependencies
- ❌ DO NOT replicate Android's Activity/Fragment lifecycle in iOS
- ✅ DO adapt to SwiftUI's view lifecycle (@State, .task, .onAppear)
- ❌ DO NOT force Kotlin-style sealed class Result into Swift without leveraging native error handling
- ✅ DO use Swift's native throws/Result type or typed errors (Swift 6)

### Step 1: Layer Mapping

```
Android Clean Architecture              iOS Clean Architecture
─────────────────────────               ──────────────────────
Presentation Layer                      Presentation Layer
├── Fragment/Activity       →           ├── SwiftUI View
├── ViewModel (AAC)         →           ├── @Observable ViewModel
├── LiveData/StateFlow      →           ├── @Published / @State
└── UI State sealed class   →           └── enum ViewState

Domain Layer                            Domain Layer
├── UseCase classes         →           ├── UseCase structs
├── Repository interfaces   →           ├── Repository protocols
├── Domain models           →           ├── Domain models (struct)
└── Kotlin interfaces       →           └── Swift protocols

Data Layer                              Data Layer
├── RepositoryImpl          →           ├── RepositoryImpl (class)
├── Room DAOs               →           ├── SwiftData / Core Data
├── Retrofit services       →           ├── URLSession services
├── Data models + mappers   →           ├── Codable models + mappers
└── DataStore               →           └── UserDefaults / Keychain
```

### Step 2: Repository Pattern Translation

**Kotlin (Android repository):**
```kotlin
// Domain layer — interface
interface UserRepository {
    suspend fun getUser(id: String): Result<User>
    fun observeUser(id: String): Flow<User>
    suspend fun updateUser(user: User): Result<Unit>
}

// Data layer — implementation
class UserRepositoryImpl @Inject constructor(
    private val api: UserApi,
    private val dao: UserDao,
    private val dispatcher: CoroutineDispatcher
) : UserRepository {

    override suspend fun getUser(id: String): Result<User> =
        withContext(dispatcher) {
            try {
                val remote = api.getUser(id)
                dao.upsert(remote.toEntity())
                Result.success(remote.toDomain())
            } catch (e: Exception) {
                val cached = dao.getUser(id)
                if (cached != null) Result.success(cached.toDomain())
                else Result.failure(e)
            }
        }

    override fun observeUser(id: String): Flow<User> =
        dao.observeUser(id).map { it.toDomain() }

    override suspend fun updateUser(user: User): Result<Unit> =
        withContext(dispatcher) {
            runCatching { api.updateUser(user.toRequest()) }
        }
}
```

**Swift (iOS repository):**
```swift
// Domain layer — protocol
protocol UserRepository: Sendable {
    func getUser(id: String) async throws -> User
    func observeUser(id: String) -> AsyncStream<User>
    func updateUser(_ user: User) async throws
}

// Data layer — implementation
final class UserRepositoryImpl: UserRepository {
    private let apiService: UserAPIService
    private let localStore: UserLocalStore

    init(apiService: UserAPIService, localStore: UserLocalStore) {
        self.apiService = apiService
        self.localStore = localStore
    }

    func getUser(id: String) async throws -> User {
        do {
            let remote = try await apiService.getUser(id: id)
            try await localStore.upsert(remote)
            return remote.toDomain()
        } catch {
            if let cached = try? await localStore.getUser(id: id) {
                return cached.toDomain()
            }
            throw error
        }
    }

    func observeUser(id: String) -> AsyncStream<User> {
        AsyncStream { continuation in
            let task = Task {
                for await entity in localStore.observe(id: id) {
                    continuation.yield(entity.toDomain())
                }
                continuation.finish()
            }
            continuation.onTermination = { _ in task.cancel() }
        }
    }

    func updateUser(_ user: User) async throws {
        try await apiService.updateUser(user.toRequest())
    }
}
```

### Step 3: UseCase Translation

**Kotlin (Android use case):**
```kotlin
class GetUserProfileUseCase @Inject constructor(
    private val userRepository: UserRepository,
    private val settingsRepository: SettingsRepository
) {
    suspend operator fun invoke(userId: String): Result<UserProfile> {
        return try {
            val user = userRepository.getUser(userId).getOrThrow()
            val settings = settingsRepository.getSettings(userId).getOrThrow()
            Result.success(UserProfile(user, settings))
        } catch (e: Exception) {
            Result.failure(e)
        }
    }
}
```

**Swift (iOS use case):**
```swift
struct GetUserProfileUseCase: Sendable {
    private let userRepository: any UserRepository
    private let settingsRepository: any SettingsRepository

    init(
        userRepository: any UserRepository,
        settingsRepository: any SettingsRepository
    ) {
        self.userRepository = userRepository
        self.settingsRepository = settingsRepository
    }

    func callAsFunction(userId: String) async throws -> UserProfile {
        async let user = userRepository.getUser(id: userId)
        async let settings = settingsRepository.getSettings(userId: userId)
        return try await UserProfile(user: user, settings: settings)
    }
}
```

> **Key Difference:** Swift's `callAsFunction` enables the same `useCase(userId)` invocation syntax as Kotlin's `operator fun invoke`. `async let` enables concurrent fetching (like `coroutineScope { async {} }`).

### Step 4: ViewModel Translation

**Kotlin (Android ViewModel):**
```kotlin
@HiltViewModel
class ProfileViewModel @Inject constructor(
    private val getUserProfile: GetUserProfileUseCase,
    private val savedStateHandle: SavedStateHandle
) : ViewModel() {

    private val userId = savedStateHandle.get<String>("userId")!!

    private val _state = MutableStateFlow<ProfileState>(ProfileState.Loading)
    val state: StateFlow<ProfileState> = _state.asStateFlow()

    init { loadProfile() }

    fun loadProfile() {
        viewModelScope.launch {
            _state.value = ProfileState.Loading
            getUserProfile(userId).fold(
                onSuccess = { _state.value = ProfileState.Success(it) },
                onFailure = { _state.value = ProfileState.Error(it.message) }
            )
        }
    }
}

sealed interface ProfileState {
    data object Loading : ProfileState
    data class Success(val profile: UserProfile) : ProfileState
    data class Error(val message: String?) : ProfileState
}
```

**Swift (iOS ViewModel):**
```swift
@Observable
final class ProfileViewModel {
    private(set) var state: ProfileState = .loading

    private let getUserProfile: GetUserProfileUseCase
    private let userId: String

    init(userId: String, getUserProfile: GetUserProfileUseCase) {
        self.userId = userId
        self.getUserProfile = getUserProfile
    }

    func loadProfile() async {
        state = .loading
        do {
            let profile = try await getUserProfile(userId: userId)
            state = .success(profile)
        } catch {
            state = .error(error.localizedDescription)
        }
    }
}

enum ProfileState {
    case loading
    case success(UserProfile)
    case error(String)
}
```

### Step 5: DI Container Translation

**Kotlin (Hilt module):**
```kotlin
@Module
@InstallIn(SingletonComponent::class)
abstract class RepositoryModule {
    @Binds
    abstract fun bindUserRepository(impl: UserRepositoryImpl): UserRepository
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

**Swift (protocol-based DI container):**
```swift
// DI Container using protocol + factory
protocol DependencyContainer: Sendable {
    var userRepository: any UserRepository { get }
    var settingsRepository: any SettingsRepository { get }
    func makeGetUserProfileUseCase() -> GetUserProfileUseCase
    func makeProfileViewModel(userId: String) -> ProfileViewModel
}

final class AppContainer: DependencyContainer {
    let userRepository: any UserRepository
    let settingsRepository: any SettingsRepository

    init() {
        let apiService = URLSessionUserAPIService()
        let localStore = SwiftDataUserStore()
        self.userRepository = UserRepositoryImpl(
            apiService: apiService, localStore: localStore
        )
        self.settingsRepository = SettingsRepositoryImpl()
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
}

// SwiftUI integration via Environment
struct ContainerKey: EnvironmentKey {
    static let defaultValue: any DependencyContainer = AppContainer()
}

extension EnvironmentValues {
    var container: any DependencyContainer {
        get { self[ContainerKey.self] }
        set { self[ContainerKey.self] = newValue }
    }
}
```

## Expected Output

1. **Layer-by-layer architecture mapping** with clear dependency rules
2. **Protocol definitions** for all domain layer contracts
3. **ViewModel pattern** adapted for SwiftUI observation
4. **DI container design** supporting both production and test configurations
5. **Error handling strategy** using Swift-native patterns

## Example Interaction

**User:** Our Android app has 3 layers (data/domain/presentation), uses Hilt, has 15 UseCases, and 8 ViewModels with StateFlow.

**Assistant:**

### Architecture Translation Summary

| Component | Count | Android | iOS | Notes |
|-----------|-------|---------|-----|-------|
| Repositories | ~6 | Hilt `@Binds` interfaces | Protocol + concrete class | Same pattern, Swift protocols |
| UseCases | 15 | `@Inject` constructor, `operator fun invoke` | Struct with `callAsFunction` | Lighter weight in Swift |
| ViewModels | 8 | `@HiltViewModel`, `StateFlow` | `@Observable`, direct properties | SwiftUI observes automatically |
| DI Modules | ~4 | `@Module @InstallIn` | `DependencyContainer` protocol | Feature-scoped containers |

## Techniques Used

| Technique | Application |
|-----------|-------------|
| **ST-01: Structured Task Decomposition** | Layer-by-layer translation approach |
| **RT-02: Contextual Reference Integration** | Android AAC and SwiftUI documentation |
| **RT-04: Comparative Analysis Framework** | Side-by-side Kotlin/Swift architecture |
| **DS-02: Output Specification Framework** | Architecture blueprint deliverables |

## Related Prompts

- `migration_hilt_to_swift_di.md` — Deep dive on dependency injection patterns
- `migration_coroutines_to_swift_concurrency.md` — Async pattern translation
- `migration_compose_to_swiftui.md` — UI layer migration
- `migration_room_to_core_data.md` — Data layer persistence migration

## Customization Guide

- **MVI Architecture:** If using MVI on Android, map Intent→Action, Reducer→State mutation, and SideEffect→SwiftUI `.task` effects.
- **Coordinator Pattern:** If the iOS team prefers Coordinator pattern for navigation, add a navigation layer between ViewModel and View.
- **Third-Party DI:** If using Swinject or Factory instead of manual DI, adjust the container pattern accordingly.
- **UIKit Target:** If building for UIKit instead of SwiftUI, replace `@Observable` with `Combine` publishers and `UIViewController` lifecycle.
