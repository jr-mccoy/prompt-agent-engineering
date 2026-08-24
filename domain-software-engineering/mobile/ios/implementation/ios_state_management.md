---
title: "iOS State Management"
category: mobile-development
description: "Implement state management with @Observable/@Bindable or Combine @Published, unidirectional data flow, and state restoration for SwiftUI applications."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-04
  - ST-03
  - NE-02
difficulty: intermediate
tags:
  - ios
  - swift
  - swiftui
  - state-management
  - observable
  - combine
  - mobile-development
updated: "2026-03-19"
---

# iOS State Management

**Objective:** Implement robust state management using @Observable/@Bindable (iOS 17+) or Combine @Published patterns with unidirectional data flow, proper state scoping, and state restoration for SwiftUI applications.

**When to Use:** Use this prompt when designing or refactoring the state management layer of an iOS app. Ideal for new feature development, migrating from ObservableObject to @Observable, or establishing state patterns for a new project. Best used after screen requirements are defined.

**Prompt Type:** Comprehensive (400-450 lines)

---

## Context Gathering

Before implementing state management, gather essential context:

1. **Project Setup:**
   - "What is the minimum deployment target (iOS 17+ for @Observable, iOS 15+ for Combine)?"
   - "Is there an existing state management pattern in place?"
   - "How many screens/features share state?"

2. **State Requirements:**
   - "What data needs to be shared across screens vs. local to one screen?"
   - "Are there async operations (network calls, database queries) that update state?"
   - "Does the app need state restoration (preserve state across app launches)?"

3. **Complexity:**
   - "How many distinct state mutations can occur per screen?"
   - "Are there complex state dependencies (state A depends on state B)?"
   - "Does state need to be undoable?"

4. **Architecture:**
   - "Is the project using MVVM, MV, or another pattern?"
   - "How is dependency injection handled?"
   - "Are there existing ViewModels to integrate with?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before implementing ANY code, you MUST:**

1. **Understand existing state patterns** - Check for existing @Observable, ObservableObject, or state management approaches.
2. **Verify deployment target** - @Observable requires iOS 17+; use Combine for earlier targets.
3. **Follow project conventions** - Match existing patterns rather than introducing conflicting approaches.
4. **Provide specific, working code** - All code must include file paths and be copy-paste ready.
5. **Include state restoration** - For user-facing state that should survive app termination.

### False-Positive Prevention

- ❌ Do NOT mix @Observable and ObservableObject in the same feature without migration strategy
- ❌ Do NOT create massive god-ViewModels that manage state for multiple unrelated features
- ❌ Do NOT use @State for data that should be shared across views (use @Observable)
- ❌ Do NOT perform heavy computation synchronously in state updates
- ❌ Do NOT ignore state consistency during concurrent async operations
- ✅ DO scope state to the smallest owning view possible
- ✅ DO use unidirectional data flow (state down, events up)
- ✅ DO separate UI state from domain state
- ✅ DO handle all state transitions explicitly (loading, success, error)

---

### Phase 1: @Observable Pattern (iOS 17+)

#### 1.1 Feature ViewModel with @Observable

```swift
// File: Features/Tasks/TaskListViewModel.swift

import SwiftUI

@Observable
final class TaskListViewModel {
    // MARK: - UI State
    enum ViewState: Equatable {
        case idle
        case loading
        case loaded
        case error(String)
    }

    private(set) var viewState: ViewState = .idle
    private(set) var tasks: [TaskItem] = []
    private(set) var filteredTasks: [TaskItem] = []
    var searchQuery: String = "" {
        didSet { applyFilters() }
    }
    var selectedFilter: TaskFilter = .all {
        didSet { applyFilters() }
    }
    var sortOrder: TaskSortOrder = .dateDescending {
        didSet { applyFilters() }
    }

    // Sheet/navigation state
    var isAddSheetPresented = false
    var selectedTask: TaskItem?
    var taskToDelete: TaskItem?

    // MARK: - Dependencies
    private let repository: TaskRepositoryProtocol
    private let analytics: AnalyticsProtocol

    init(
        repository: TaskRepositoryProtocol = TaskRepository(),
        analytics: AnalyticsProtocol = Analytics.shared
    ) {
        self.repository = repository
        self.analytics = analytics
    }

    // MARK: - Actions (unidirectional data flow)

    func loadTasks() async {
        viewState = .loading
        do {
            tasks = try await repository.fetchAll()
            applyFilters()
            viewState = .loaded
        } catch {
            viewState = .error(error.localizedDescription)
        }
    }

    func refresh() async {
        do {
            tasks = try await repository.fetchAll()
            applyFilters()
        } catch {
            // Keep existing data on refresh failure
        }
    }

    func addTask(title: String, notes: String) async {
        do {
            let task = try await repository.create(title: title, notes: notes)
            tasks.insert(task, at: 0)
            applyFilters()
            isAddSheetPresented = false
            analytics.track(.taskCreated)
        } catch {
            viewState = .error("Failed to create task")
        }
    }

    func toggleComplete(_ task: TaskItem) async {
        guard let index = tasks.firstIndex(where: { $0.id == task.id }) else { return }
        tasks[index].isCompleted.toggle()
        applyFilters()
        do {
            try await repository.update(tasks[index])
        } catch {
            // Revert on failure
            tasks[index].isCompleted.toggle()
            applyFilters()
        }
    }

    func deleteTask() async {
        guard let task = taskToDelete else { return }
        tasks.removeAll { $0.id == task.id }
        applyFilters()
        taskToDelete = nil
        do {
            try await repository.delete(task.id)
        } catch {
            // Re-fetch on failure
            await loadTasks()
        }
    }

    // MARK: - Private

    private func applyFilters() {
        var result = tasks

        // Apply filter
        switch selectedFilter {
        case .all: break
        case .active: result = result.filter { !$0.isCompleted }
        case .completed: result = result.filter { $0.isCompleted }
        }

        // Apply search
        if !searchQuery.isEmpty {
            result = result.filter {
                $0.title.localizedCaseInsensitiveContains(searchQuery) ||
                $0.notes.localizedCaseInsensitiveContains(searchQuery)
            }
        }

        // Apply sort
        switch sortOrder {
        case .dateDescending: result.sort { $0.createdAt > $1.createdAt }
        case .dateAscending: result.sort { $0.createdAt < $1.createdAt }
        case .alphabetical: result.sort { $0.title < $1.title }
        }

        filteredTasks = result
    }
}

// Supporting types
enum TaskFilter: String, CaseIterable, Identifiable {
    case all, active, completed
    var id: String { rawValue }
    var displayName: String { rawValue.capitalized }
}

enum TaskSortOrder: String, CaseIterable, Identifiable {
    case dateDescending, dateAscending, alphabetical
    var id: String { rawValue }
}
```

#### 1.2 View Integration

```swift
// File: Features/Tasks/TaskListScreen.swift

import SwiftUI

struct TaskListScreen: View {
    @State private var viewModel = TaskListViewModel()

    var body: some View {
        NavigationStack {
            TaskListContent(viewModel: viewModel)
                .navigationTitle("Tasks")
                .searchable(text: $viewModel.searchQuery)
                .toolbar {
                    ToolbarItem(placement: .topBarTrailing) {
                        Button("Add", systemImage: "plus") {
                            viewModel.isAddSheetPresented = true
                        }
                    }
                    ToolbarItem(placement: .topBarLeading) {
                        Menu {
                            Picker("Filter", selection: $viewModel.selectedFilter) {
                                ForEach(TaskFilter.allCases) { filter in
                                    Text(filter.displayName).tag(filter)
                                }
                            }
                        } label: {
                            Image(systemName: "line.3.horizontal.decrease.circle")
                        }
                    }
                }
                .task { await viewModel.loadTasks() }
                .refreshable { await viewModel.refresh() }
                .sheet(isPresented: $viewModel.isAddSheetPresented) {
                    AddTaskSheet { title, notes in
                        await viewModel.addTask(title: title, notes: notes)
                    }
                }
                .confirmationDialog(
                    "Delete Task",
                    isPresented: .init(
                        get: { viewModel.taskToDelete != nil },
                        set: { if !$0 { viewModel.taskToDelete = nil } }
                    )
                ) {
                    Button("Delete", role: .destructive) {
                        Task { await viewModel.deleteTask() }
                    }
                }
        }
    }
}

private struct TaskListContent: View {
    @Bindable var viewModel: TaskListViewModel

    var body: some View {
        Group {
            switch viewModel.viewState {
            case .idle, .loading:
                ProgressView()
                    .frame(maxWidth: .infinity, maxHeight: .infinity)
            case .loaded:
                if viewModel.filteredTasks.isEmpty {
                    ContentUnavailableView.search(text: viewModel.searchQuery)
                } else {
                    taskList
                }
            case .error(let message):
                ContentUnavailableView {
                    Label("Error", systemImage: "exclamationmark.triangle")
                } description: {
                    Text(message)
                } actions: {
                    Button("Retry") { Task { await viewModel.loadTasks() } }
                }
            }
        }
    }

    private var taskList: some View {
        List(viewModel.filteredTasks) { task in
            TaskRow(task: task) {
                Task { await viewModel.toggleComplete(task) }
            }
            .swipeActions(edge: .trailing) {
                Button("Delete", role: .destructive) {
                    viewModel.taskToDelete = task
                }
            }
        }
    }
}
```

---

### Phase 2: Combine Pattern (iOS 15+)

**CHECKPOINT 1:** Use this phase only if targeting iOS 15/16.

#### 2.1 ObservableObject ViewModel

```swift
// File: Features/Tasks/TaskListViewModelLegacy.swift

import Combine
import SwiftUI

final class TaskListViewModelLegacy: ObservableObject {
    @Published private(set) var viewState: ViewState = .idle
    @Published private(set) var filteredTasks: [TaskItem] = []
    @Published var searchQuery: String = ""
    @Published var selectedFilter: TaskFilter = .all
    @Published var isAddSheetPresented = false

    private var tasks: [TaskItem] = []
    private var cancellables = Set<AnyCancellable>()
    private let repository: TaskRepositoryProtocol

    init(repository: TaskRepositoryProtocol = TaskRepository()) {
        self.repository = repository
        setupBindings()
    }

    private func setupBindings() {
        // Debounce search and combine with filter
        Publishers.CombineLatest($searchQuery.debounce(for: .milliseconds(300), scheduler: RunLoop.main), $selectedFilter)
            .sink { [weak self] query, filter in
                self?.applyFilters(query: query, filter: filter)
            }
            .store(in: &cancellables)
    }

    @MainActor
    func loadTasks() async {
        viewState = .loading
        do {
            tasks = try await repository.fetchAll()
            applyFilters(query: searchQuery, filter: selectedFilter)
            viewState = .loaded
        } catch {
            viewState = .error(error.localizedDescription)
        }
    }

    private func applyFilters(query: String, filter: TaskFilter) {
        var result = tasks
        switch filter {
        case .all: break
        case .active: result = result.filter { !$0.isCompleted }
        case .completed: result = result.filter { $0.isCompleted }
        }
        if !query.isEmpty {
            result = result.filter {
                $0.title.localizedCaseInsensitiveContains(query)
            }
        }
        filteredTasks = result
    }

    enum ViewState: Equatable {
        case idle, loading, loaded, error(String)
    }
}
```

---

### Phase 3: Shared App State

#### 3.1 App-Level State

```swift
// File: App/AppState.swift

import SwiftUI

@Observable
final class AppState {
    var currentUser: User?
    var isAuthenticated: Bool { currentUser != nil }
    var theme: AppTheme = .system
    var hasCompletedOnboarding: Bool {
        get { UserDefaults.standard.bool(forKey: "hasCompletedOnboarding") }
        set { UserDefaults.standard.set(newValue, forKey: "hasCompletedOnboarding") }
    }

    static let shared = AppState()
    private init() {}
}

// Inject via Environment
extension EnvironmentValues {
    @Entry var appState: AppState = .shared
}

// Usage in App
@main
struct MyApp: App {
    @State private var appState = AppState.shared

    var body: some Scene {
        WindowGroup {
            RootView()
                .environment(appState)
        }
    }
}

// Access in any view
struct ProfileButton: View {
    @Environment(AppState.self) private var appState

    var body: some View {
        if let user = appState.currentUser {
            Text(user.displayName)
        }
    }
}
```

#### 3.2 State Restoration

```swift
// File: App/StateRestoration.swift

import SwiftUI

@Observable
final class NavigationState: Codable {
    var selectedTab: Tab = .home
    var taskListPath: [TaskRoute] = []

    enum Tab: String, Codable {
        case home, tasks, settings
    }

    // Persist to UserDefaults
    func save() {
        if let data = try? JSONEncoder().encode(self) {
            UserDefaults.standard.set(data, forKey: "navigationState")
        }
    }

    static func restore() -> NavigationState {
        guard let data = UserDefaults.standard.data(forKey: "navigationState"),
              let state = try? JSONDecoder().decode(NavigationState.self, from: data)
        else {
            return NavigationState()
        }
        return state
    }
}

enum TaskRoute: Hashable, Codable {
    case detail(id: String)
    case edit(id: String)
    case create
}

// Integration in root view
struct RootView: View {
    @State private var navState = NavigationState.restore()

    var body: some View {
        TabView(selection: $navState.selectedTab) {
            Tab("Home", systemImage: "house", value: .home) {
                HomeScreen()
            }
            Tab("Tasks", systemImage: "checklist", value: .tasks) {
                NavigationStack(path: $navState.taskListPath) {
                    TaskListScreen()
                        .navigationDestination(for: TaskRoute.self) { route in
                            switch route {
                            case .detail(let id): TaskDetailScreen(taskId: id)
                            case .edit(let id): TaskEditScreen(taskId: id)
                            case .create: AddTaskScreen()
                            }
                        }
                }
            }
            Tab("Settings", systemImage: "gear", value: .settings) {
                SettingsScreen()
            }
        }
        .onChange(of: navState.selectedTab) { _, _ in navState.save() }
        .onChange(of: navState.taskListPath) { _, _ in navState.save() }
    }
}
```

---

## Expected Output

### File Structure

```
Features/Tasks/
├── TaskListViewModel.swift         # @Observable view model
├── TaskListScreen.swift            # SwiftUI screen
└── TaskListViewModelLegacy.swift   # Combine fallback (if needed)

App/
├── AppState.swift                  # Shared app-level state
└── StateRestoration.swift          # Navigation state persistence
```

### Implementation Checklist

- [ ] @Observable ViewModel with explicit state enum
- [ ] Unidirectional data flow (state down, events up)
- [ ] @Bindable for two-way bindings in child views
- [ ] Async action handling with optimistic updates
- [ ] Error state with user-facing messages
- [ ] Search/filter with debounced reactivity
- [ ] App-level shared state via Environment
- [ ] State restoration across app launches
- [ ] Combine fallback for iOS 15/16 (if needed)

---

## Example Interaction

**User:** "I need state management for a shopping cart that persists across screens and app launches."

**Assistant:**
```swift
@Observable
final class CartState: Codable {
    var items: [CartItem] = []

    var totalPrice: Decimal {
        items.reduce(0) { $0 + ($1.price * Decimal($1.quantity)) }
    }

    var itemCount: Int {
        items.reduce(0) { $0 + $1.quantity }
    }

    func addItem(_ product: Product, quantity: Int = 1) {
        if let index = items.firstIndex(where: { $0.productId == product.id }) {
            items[index].quantity += quantity
        } else {
            items.append(CartItem(product: product, quantity: quantity))
        }
        save()
    }

    func removeItem(_ productId: String) {
        items.removeAll { $0.productId == productId }
        save()
    }

    private func save() {
        if let data = try? JSONEncoder().encode(items) {
            UserDefaults.standard.set(data, forKey: "cart")
        }
    }

    static func restore() -> CartState {
        let state = CartState()
        if let data = UserDefaults.standard.data(forKey: "cart"),
           let items = try? JSONDecoder().decode([CartItem].self, from: data) {
            state.items = items
        }
        return state
    }
}
```

---

## Techniques Used

- **ST-01** (Clear Objective): Focused on state management patterns
- **ST-02** (Sequential Instructions): Phased from @Observable to restoration
- **RT-02** (Multi-Dimensional Analysis): Covers modern and legacy patterns
- **RT-04** (Best Practice Review): Unidirectional data flow best practices
- **ST-03** (Output Format Templates): Code templates for state patterns
- **NE-02** (Phased Workflow): Progressive disclosure of complexity

---

## Related Prompts

- [ios_swiftui_screen_builder.md](ios_swiftui_screen_builder.md) - Build screens that consume state
- [ios_swiftui_state_patterns.md](ios_swiftui_state_patterns.md) - Advanced state ownership patterns
- [ios_navigation_implementation.md](ios_navigation_implementation.md) - Navigation state
- [ios_data_layer_implementation.md](ios_data_layer_implementation.md) - Persistence for state

---

## Customization Guide

### For Redux-Style Architecture

Implement a store with reducers:
```swift
@Observable
final class Store<State, Action> {
    private(set) var state: State
    private let reducer: (inout State, Action) -> Void

    init(initial: State, reducer: @escaping (inout State, Action) -> Void) {
        self.state = initial
        self.reducer = reducer
    }

    func dispatch(_ action: Action) {
        reducer(&state, action)
    }
}
```

### For Feature-Scoped State

Isolate state per feature module:
```swift
@Observable
final class FeatureState {
    var items: [Item] = []
    var isLoading = false
}

// Inject per-feature, not globally
struct FeatureScreen: View {
    @State private var featureState = FeatureState()
    var body: some View {
        ChildView()
            .environment(featureState)
    }
}
```
