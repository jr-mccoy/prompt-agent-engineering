---
title: "iOS Dependency Injection"
category: mobile-development
description: "Implement dependency injection using Swift patterns including constructor injection with protocols, SwiftUI Environment values, and container libraries like Factory or Swinject."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-04
  - ST-03
difficulty: intermediate
tags:
  - ios
  - swift
  - dependency-injection
  - testing
  - architecture
  - mobile-development
updated: "2026-03-19"
---

# iOS Dependency Injection

**Objective:** Implement clean dependency injection using Swift-native patterns including constructor injection with protocols, SwiftUI Environment values, and optional container libraries (Factory or Swinject) for testable, modular iOS applications.

**When to Use:** Use this prompt when setting up or refactoring dependency injection in an iOS project. Ideal for new projects needing a DI strategy, improving testability of existing code, or migrating to a more modular architecture. Best used before implementing features.

**Prompt Type:** Modular (300-350 lines)

---

## Context Gathering

Before implementing dependency injection, gather essential context:

1. **Project Setup:**
   - "Is there an existing DI approach (manual, container, Environment)?"
   - "What architecture pattern is used (MVVM, MV, VIPER)?"
   - "Are there unit tests that need mock injection?"

2. **Scale:**
   - "How many services/dependencies exist?"
   - "Are there singleton services that need shared instances?"
   - "Do dependencies have scoped lifetimes (per-screen, per-session)?"

3. **Preferences:**
   - "Do you prefer no third-party dependencies for DI?"
   - "Is compile-time safety preferred over runtime flexibility?"
   - "Should the DI system integrate with SwiftUI previews?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before implementing ANY code, you MUST:**

1. **Understand existing patterns** - Check for existing DI, service locators, or singleton patterns.
2. **Verify testability needs** - Confirm which dependencies need mock injection for tests.
3. **Follow project conventions** - Match existing patterns rather than introducing a conflicting DI system.
4. **Provide specific, working code** - All code must include file paths and be copy-paste ready.

### False-Positive Prevention

- ❌ Do NOT over-engineer DI for small projects (constructor injection may suffice)
- ❌ Do NOT create circular dependencies between services
- ❌ Do NOT register concrete types when protocols should be used
- ❌ Do NOT use service locator pattern disguised as DI (hidden dependencies)
- ❌ Do NOT force every class to use a container when simple init injection works
- ✅ DO define protocols for all injectable dependencies
- ✅ DO support SwiftUI previews with mock dependencies
- ✅ DO document the dependency graph for complex setups
- ✅ DO use constructor injection as the default, containers as a supplement

---

### Module 1: Protocol-Based Constructor Injection

```swift
// File: Services/Protocols/ServiceProtocols.swift

import Foundation

protocol AuthServiceProtocol: Sendable {
    func signIn(email: String, password: String) async throws -> User
    func signOut() async throws
    var currentUser: User? { get async }
}

protocol TaskRepositoryProtocol: Sendable {
    func fetchAll() async throws -> [TaskItem]
    func create(title: String, notes: String) async throws -> TaskItem
    func update(_ task: TaskItem) async throws
    func delete(_ id: String) async throws
}

protocol AnalyticsProtocol: Sendable {
    func track(_ event: AnalyticsEvent)
    func setUserProperty(_ key: String, value: String)
}

protocol NotificationServiceProtocol: Sendable {
    func requestPermission() async throws -> Bool
    func scheduleLocal(title: String, body: String, at date: Date) async throws
}
```

```swift
// File: Features/Tasks/TaskListViewModel.swift

import SwiftUI

@Observable
final class TaskListViewModel {
    private(set) var tasks: [TaskItem] = []
    private(set) var isLoading = false

    private let repository: TaskRepositoryProtocol
    private let analytics: AnalyticsProtocol

    // Constructor injection - dependencies are explicit
    init(
        repository: TaskRepositoryProtocol,
        analytics: AnalyticsProtocol
    ) {
        self.repository = repository
        self.analytics = analytics
    }

    func loadTasks() async {
        isLoading = true
        defer { isLoading = false }
        do {
            tasks = try await repository.fetchAll()
            analytics.track(.tasksLoaded(count: tasks.count))
        } catch {
            analytics.track(.error(error.localizedDescription))
        }
    }
}
```

### Module 2: SwiftUI Environment Injection

```swift
// File: DI/EnvironmentDependencies.swift

import SwiftUI

// Define environment keys for each service
extension EnvironmentValues {
    @Entry var authService: AuthServiceProtocol = LiveAuthService()
    @Entry var taskRepository: TaskRepositoryProtocol = LiveTaskRepository()
    @Entry var analytics: AnalyticsProtocol = LiveAnalytics()
    @Entry var notificationService: NotificationServiceProtocol = LiveNotificationService()
}

// Usage in views - read from environment, inject into view models
struct TaskListScreen: View {
    @Environment(\.taskRepository) private var repository
    @Environment(\.analytics) private var analytics
    @State private var viewModel: TaskListViewModel?

    var body: some View {
        Group {
            if let viewModel {
                TaskListContent(viewModel: viewModel)
            } else {
                ProgressView()
            }
        }
        .onAppear {
            if viewModel == nil {
                viewModel = TaskListViewModel(
                    repository: repository,
                    analytics: analytics
                )
            }
        }
        .task { await viewModel?.loadTasks() }
    }
}

// Override in previews
#Preview {
    TaskListScreen()
        .environment(\.taskRepository, MockTaskRepository())
        .environment(\.analytics, MockAnalytics())
}

// Override in tests
struct TestableApp: View {
    var body: some View {
        RootView()
            .environment(\.authService, MockAuthService())
            .environment(\.taskRepository, MockTaskRepository())
            .environment(\.analytics, MockAnalytics())
    }
}
```

### Module 3: Factory Container Pattern

```swift
// File: DI/DependencyContainer.swift

import Foundation

/// Lightweight DI container using Factory pattern (no third-party dependency)
@Observable
final class DependencyContainer {
    static let shared = DependencyContainer()

    // MARK: - Service Registrations

    lazy var authService: AuthServiceProtocol = LiveAuthService()

    lazy var apiClient: APIClient = APIClient(
        baseURL: URL(string: "https://api.example.com")!,
        authProvider: authService as? AuthTokenProvider
    )

    lazy var taskRepository: TaskRepositoryProtocol = LiveTaskRepository(
        apiClient: apiClient,
        persistence: persistenceController
    )

    lazy var analytics: AnalyticsProtocol = LiveAnalytics()

    lazy var notificationService: NotificationServiceProtocol = LiveNotificationService()

    lazy var persistenceController: PersistenceController = PersistenceController()

    // MARK: - ViewModel Factories

    func makeTaskListViewModel() -> TaskListViewModel {
        TaskListViewModel(
            repository: taskRepository,
            analytics: analytics
        )
    }

    func makeTaskDetailViewModel(taskId: String) -> TaskDetailViewModel {
        TaskDetailViewModel(
            taskId: taskId,
            repository: taskRepository,
            notificationService: notificationService
        )
    }

    // MARK: - Test Support

    static func forTesting() -> DependencyContainer {
        let container = DependencyContainer()
        container.authService = MockAuthService()
        container.taskRepository = MockTaskRepository()
        container.analytics = MockAnalytics()
        container.notificationService = MockNotificationService()
        return container
    }

    static func forPreviews() -> DependencyContainer {
        let container = DependencyContainer()
        container.taskRepository = PreviewTaskRepository()
        container.analytics = MockAnalytics()
        return container
    }
}

// Inject container via Environment
extension EnvironmentValues {
    @Entry var container: DependencyContainer = .shared
}

// Usage
struct TaskListScreen: View {
    @Environment(\.container) private var container
    @State private var viewModel: TaskListViewModel?

    var body: some View {
        Group {
            if let viewModel {
                TaskListContent(viewModel: viewModel)
            } else {
                ProgressView()
            }
        }
        .onAppear {
            viewModel = viewModel ?? container.makeTaskListViewModel()
        }
    }
}
```

### Module 4: Mock Implementations

```swift
// File: DI/Mocks/MockServices.swift

import Foundation

// MARK: - Mock Task Repository

final class MockTaskRepository: TaskRepositoryProtocol, @unchecked Sendable {
    var stubbedTasks: [TaskItem] = [
        TaskItem(id: "1", title: "Buy groceries", notes: "Milk, eggs, bread", isCompleted: false, createdAt: .now),
        TaskItem(id: "2", title: "Write tests", notes: "Unit + integration", isCompleted: true, createdAt: .now),
    ]
    var createCallCount = 0
    var deleteCallCount = 0
    var shouldThrowError = false

    func fetchAll() async throws -> [TaskItem] {
        if shouldThrowError { throw MockError.fetchFailed }
        return stubbedTasks
    }

    func create(title: String, notes: String) async throws -> TaskItem {
        createCallCount += 1
        let task = TaskItem(id: UUID().uuidString, title: title, notes: notes, isCompleted: false, createdAt: .now)
        stubbedTasks.append(task)
        return task
    }

    func update(_ task: TaskItem) async throws {
        guard let index = stubbedTasks.firstIndex(where: { $0.id == task.id }) else { return }
        stubbedTasks[index] = task
    }

    func delete(_ id: String) async throws {
        deleteCallCount += 1
        stubbedTasks.removeAll { $0.id == id }
    }
}

// MARK: - Mock Analytics

final class MockAnalytics: AnalyticsProtocol, @unchecked Sendable {
    var trackedEvents: [AnalyticsEvent] = []

    func track(_ event: AnalyticsEvent) {
        trackedEvents.append(event)
    }

    func setUserProperty(_ key: String, value: String) {}
}

// MARK: - Mock Auth Service

final class MockAuthService: AuthServiceProtocol, @unchecked Sendable {
    var mockUser: User? = User(id: "test", displayName: "Test User", email: "test@example.com")

    func signIn(email: String, password: String) async throws -> User {
        guard let user = mockUser else { throw MockError.authFailed }
        return user
    }

    func signOut() async throws { mockUser = nil }

    var currentUser: User? { mockUser }
}

final class MockNotificationService: NotificationServiceProtocol, @unchecked Sendable {
    func requestPermission() async throws -> Bool { true }
    func scheduleLocal(title: String, body: String, at date: Date) async throws {}
}

enum MockError: Error {
    case fetchFailed, authFailed
}
```

### Module 5: Unit Test Integration

```swift
// File: Tests/TaskListViewModelTests.swift

import XCTest
@testable import MyApp

final class TaskListViewModelTests: XCTestCase {
    private var mockRepository: MockTaskRepository!
    private var mockAnalytics: MockAnalytics!
    private var sut: TaskListViewModel!

    override func setUp() {
        super.setUp()
        mockRepository = MockTaskRepository()
        mockAnalytics = MockAnalytics()
        sut = TaskListViewModel(
            repository: mockRepository,
            analytics: mockAnalytics
        )
    }

    func testLoadTasksFetchesFromRepository() async {
        await sut.loadTasks()

        XCTAssertEqual(sut.tasks.count, 2)
        XCTAssertFalse(sut.isLoading)
    }

    func testLoadTasksTracksAnalytics() async {
        await sut.loadTasks()

        XCTAssertEqual(mockAnalytics.trackedEvents.count, 1)
    }

    func testLoadTasksHandlesError() async {
        mockRepository.shouldThrowError = true

        await sut.loadTasks()

        XCTAssertTrue(sut.tasks.isEmpty)
        XCTAssertFalse(sut.isLoading)
    }
}
```

---

## Expected Output

### File Structure

```
DI/
├── EnvironmentDependencies.swift   # SwiftUI @Entry keys
├── DependencyContainer.swift       # Factory container
└── Mocks/
    └── MockServices.swift          # Test doubles

Services/
└── Protocols/
    └── ServiceProtocols.swift      # Protocol definitions

Tests/
└── TaskListViewModelTests.swift    # Tests with injected mocks
```

### Implementation Checklist

- [ ] Protocol definitions for all injectable services
- [ ] Constructor injection in ViewModels
- [ ] SwiftUI Environment keys for dependency propagation
- [ ] DependencyContainer with factory methods
- [ ] Mock implementations for all protocols
- [ ] Preview support with mock dependencies
- [ ] Unit tests using injected mocks

---

## Example Interaction

**User:** "I need to inject a payment service that can be mocked in tests."

**Assistant:**
```swift
protocol PaymentServiceProtocol: Sendable {
    func processPayment(amount: Decimal, currency: String) async throws -> PaymentResult
    func fetchTransactions() async throws -> [Transaction]
}

// Live implementation
final class LivePaymentService: PaymentServiceProtocol {
    private let apiClient: APIClient
    init(apiClient: APIClient) { self.apiClient = apiClient }

    func processPayment(amount: Decimal, currency: String) async throws -> PaymentResult {
        try await apiClient.request(
            PaymentEndpoints.charge(amount: amount, currency: currency),
            responseType: PaymentResult.self
        )
    }

    func fetchTransactions() async throws -> [Transaction] {
        try await apiClient.request(
            PaymentEndpoints.transactions,
            responseType: [Transaction].self
        )
    }
}

// Register in container
extension DependencyContainer {
    lazy var paymentService: PaymentServiceProtocol = LivePaymentService(apiClient: apiClient)
}
```

---

## Techniques Used

- **ST-01** (Clear Objective): Focused on DI patterns and testability
- **ST-02** (Sequential Instructions): Modular approach from protocols to testing
- **RT-02** (Multi-Dimensional Analysis): Constructor injection, Environment, containers
- **RT-04** (Best Practice Review): Swift DI and testing best practices
- **ST-03** (Output Format Templates): Code templates for each DI approach

---

## Related Prompts

- [ios_state_management.md](ios_state_management.md) - ViewModels that receive injected dependencies
- [ios_api_integration.md](ios_api_integration.md) - Network services to inject
- [ios_data_layer_implementation.md](ios_data_layer_implementation.md) - Repositories to inject
- [ios_swiftui_screen_builder.md](ios_swiftui_screen_builder.md) - Views that consume dependencies

---

## Customization Guide

### For Swinject Integration

Use Swinject for complex dependency graphs:
```swift
import Swinject

let container = Container()
container.register(TaskRepositoryProtocol.self) { r in
    LiveTaskRepository(apiClient: r.resolve(APIClient.self)!)
}
container.register(APIClient.self) { _ in
    APIClient(baseURL: URL(string: "https://api.example.com")!)
}.inObjectScope(.container)
```

### For @PropertyWrapper Injection

Create a custom property wrapper:
```swift
@propertyWrapper
struct Injected<T> {
    let wrappedValue: T
    init() {
        wrappedValue = DependencyContainer.shared.resolve()
    }
}

// Usage: @Injected var repository: TaskRepositoryProtocol
```

### For Module-Based DI

Organize by feature module:
```swift
protocol TaskModule {
    var repository: TaskRepositoryProtocol { get }
    var viewModelFactory: () -> TaskListViewModel { get }
}
```
