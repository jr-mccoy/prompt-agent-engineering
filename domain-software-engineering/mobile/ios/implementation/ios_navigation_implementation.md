---
title: "iOS Navigation Implementation"
category: mobile-development
description: "Implement NavigationStack and NavigationSplitView with type-safe routing, Universal Links deep linking, and programmatic navigation for SwiftUI apps."
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
  - swiftui
  - navigation
  - deep-linking
  - universal-links
  - mobile-development
updated: "2026-03-19"
---

# iOS Navigation Implementation

**Objective:** Implement robust navigation using NavigationStack and NavigationSplitView with type-safe routing, Universal Links deep linking, and programmatic navigation control for SwiftUI applications.

**When to Use:** Use this prompt when building or refactoring navigation in an iOS app. Ideal for new projects needing a navigation architecture, adding deep link support, or migrating from NavigationView to NavigationStack. Best used after screen inventory is defined.

**Prompt Type:** Modular (300-400 lines)

---

## Context Gathering

Before implementing navigation, gather essential context:

1. **App Structure:**
   - "Is the app tab-based, single-stack, or split-view?"
   - "How many top-level navigation flows exist?"
   - "Does the app need to support iPad split view?"

2. **Navigation Requirements:**
   - "Which screens can be reached from deep links or notifications?"
   - "Are there modal flows (sheets, full-screen covers)?"
   - "Does the navigation state need to be preserved across launches?"

3. **Existing Patterns:**
   - "Is NavigationStack or NavigationView currently used?"
   - "Is there a router or coordinator pattern in place?"
   - "How are deep links currently handled?"

4. **Deep Linking:**
   - "What Universal Link domains are configured?"
   - "What URL schemes does the app support?"
   - "What paths should map to which screens?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before implementing ANY code, you MUST:**

1. **Understand existing navigation** - Check for existing NavigationStack, routers, or coordinator patterns.
2. **Verify all destination screens exist** - Confirm every route has a corresponding view.
3. **Follow project conventions** - Match existing patterns rather than introducing conflicting navigation approaches.
4. **Provide specific, working code** - All code must include file paths and be copy-paste ready.

### False-Positive Prevention

- ❌ Do NOT use deprecated NavigationView for new code (use NavigationStack/NavigationSplitView)
- ❌ Do NOT create circular navigation paths
- ❌ Do NOT hardcode navigation paths as strings (use type-safe routes)
- ❌ Do NOT ignore deep link edge cases (app not running, already on target screen)
- ✅ DO use Hashable enums for route definitions
- ✅ DO handle navigation state restoration
- ✅ DO support programmatic pop-to-root and deep navigation
- ✅ DO test deep links from cold start and warm start

---

### Module 1: Type-Safe Router

```swift
// File: Navigation/AppRouter.swift

import SwiftUI

@Observable
final class AppRouter {
    var selectedTab: Tab = .home
    var homePath = NavigationPath()
    var taskPath = NavigationPath()
    var profilePath = NavigationPath()

    // Sheet state
    var presentedSheet: Sheet?
    var presentedFullScreenCover: FullScreenCover?

    enum Tab: String, Hashable, CaseIterable {
        case home, tasks, profile
    }

    enum Sheet: Identifiable, Hashable {
        case addTask
        case editTask(id: String)
        case settings

        var id: Int { hashValue }
    }

    enum FullScreenCover: Identifiable, Hashable {
        case onboarding
        case imageViewer(url: URL)

        var id: Int { hashValue }
    }

    // MARK: - Navigation Actions

    func navigate(to route: Route) {
        switch route {
        case .home(let destination):
            selectedTab = .home
            if let destination { homePath.append(destination) }
        case .tasks(let destination):
            selectedTab = .tasks
            if let destination { taskPath.append(destination) }
        case .profile(let destination):
            selectedTab = .profile
            if let destination { profilePath.append(destination) }
        }
    }

    func popToRoot(tab: Tab) {
        switch tab {
        case .home: homePath = NavigationPath()
        case .tasks: taskPath = NavigationPath()
        case .profile: profilePath = NavigationPath()
        }
    }

    func pop(tab: Tab) {
        switch tab {
        case .home: if !homePath.isEmpty { homePath.removeLast() }
        case .tasks: if !taskPath.isEmpty { taskPath.removeLast() }
        case .profile: if !profilePath.isEmpty { profilePath.removeLast() }
        }
    }

    func present(sheet: Sheet) {
        presentedSheet = sheet
    }

    func present(cover: FullScreenCover) {
        presentedFullScreenCover = cover
    }

    func dismissSheet() {
        presentedSheet = nil
    }

    func dismissCover() {
        presentedFullScreenCover = nil
    }
}
```

### Module 2: Route Definitions

```swift
// File: Navigation/Routes.swift

import Foundation

enum Route: Hashable {
    case home(HomeRoute? = nil)
    case tasks(TaskRoute? = nil)
    case profile(ProfileRoute? = nil)
}

enum HomeRoute: Hashable {
    case featured(id: String)
    case category(name: String)
    case detail(id: String)
}

enum TaskRoute: Hashable, Codable {
    case detail(id: String)
    case edit(id: String)
    case history
}

enum ProfileRoute: Hashable {
    case editProfile
    case preferences
    case notifications
    case about
}
```

### Module 3: Root Navigation View

```swift
// File: Navigation/RootNavigationView.swift

import SwiftUI

struct RootNavigationView: View {
    @State private var router = AppRouter()

    var body: some View {
        TabView(selection: $router.selectedTab) {
            Tab("Home", systemImage: "house", value: .home) {
                NavigationStack(path: $router.homePath) {
                    HomeScreen()
                        .navigationDestination(for: HomeRoute.self) { route in
                            homeDestination(for: route)
                        }
                }
            }

            Tab("Tasks", systemImage: "checklist", value: .tasks) {
                NavigationStack(path: $router.taskPath) {
                    TaskListScreen()
                        .navigationDestination(for: TaskRoute.self) { route in
                            taskDestination(for: route)
                        }
                }
            }

            Tab("Profile", systemImage: "person", value: .profile) {
                NavigationStack(path: $router.profilePath) {
                    ProfileScreen()
                        .navigationDestination(for: ProfileRoute.self) { route in
                            profileDestination(for: route)
                        }
                }
            }
        }
        .environment(router)
        .sheet(item: $router.presentedSheet) { sheet in
            sheetContent(for: sheet)
        }
        .fullScreenCover(item: $router.presentedFullScreenCover) { cover in
            coverContent(for: cover)
        }
        .onOpenURL { url in
            handleDeepLink(url)
        }
    }

    // MARK: - Destination Builders

    @ViewBuilder
    private func homeDestination(for route: HomeRoute) -> some View {
        switch route {
        case .featured(let id): FeaturedDetailScreen(id: id)
        case .category(let name): CategoryScreen(name: name)
        case .detail(let id): ItemDetailScreen(id: id)
        }
    }

    @ViewBuilder
    private func taskDestination(for route: TaskRoute) -> some View {
        switch route {
        case .detail(let id): TaskDetailScreen(taskId: id)
        case .edit(let id): TaskEditScreen(taskId: id)
        case .history: TaskHistoryScreen()
        }
    }

    @ViewBuilder
    private func profileDestination(for route: ProfileRoute) -> some View {
        switch route {
        case .editProfile: EditProfileScreen()
        case .preferences: PreferencesScreen()
        case .notifications: NotificationSettingsScreen()
        case .about: AboutScreen()
        }
    }

    @ViewBuilder
    private func sheetContent(for sheet: AppRouter.Sheet) -> some View {
        switch sheet {
        case .addTask: AddTaskSheet()
        case .editTask(let id): EditTaskSheet(taskId: id)
        case .settings: SettingsSheet()
        }
    }

    @ViewBuilder
    private func coverContent(for cover: AppRouter.FullScreenCover) -> some View {
        switch cover {
        case .onboarding: OnboardingFlow()
        case .imageViewer(let url): ImageViewerScreen(url: url)
        }
    }
}
```

### Module 4: Universal Links & Deep Linking

```swift
// File: Navigation/DeepLinkHandler.swift

import Foundation

struct DeepLinkHandler {
    /// Parse URL into a Route
    static func route(from url: URL) -> Route? {
        // Universal Links: https://example.com/tasks/abc123
        if let host = url.host(), host.contains("example.com") {
            return parseUniversalLink(url)
        }

        // Custom URL Scheme: myapp://tasks/abc123
        if url.scheme == "myapp" {
            return parseCustomScheme(url)
        }

        return nil
    }

    private static func parseUniversalLink(_ url: URL) -> Route? {
        let pathComponents = url.pathComponents.filter { $0 != "/" }

        guard let first = pathComponents.first else {
            return .home()
        }

        switch first {
        case "tasks":
            if let id = pathComponents.dropFirst().first {
                return .tasks(.detail(id: id))
            }
            return .tasks()
        case "items":
            if let id = pathComponents.dropFirst().first {
                return .home(.detail(id: id))
            }
            return .home()
        case "profile":
            return .profile()
        default:
            return .home()
        }
    }

    private static func parseCustomScheme(_ url: URL) -> Route? {
        // myapp://tasks/detail?id=abc123
        guard let host = url.host() else { return nil }

        let queryItems = URLComponents(url: url, resolvingAgainstBaseURL: false)?.queryItems
        let params = Dictionary(
            uniqueKeysWithValues: (queryItems ?? []).compactMap {
                guard let value = $0.value else { return nil }
                return ($0.name, value)
            }
        )

        switch host {
        case "tasks":
            if let id = params["id"] {
                return .tasks(.detail(id: id))
            }
            return .tasks()
        case "profile":
            return .profile()
        default:
            return .home()
        }
    }
}

// Integration in RootNavigationView
extension RootNavigationView {
    func handleDeepLink(_ url: URL) {
        guard let route = DeepLinkHandler.route(from: url) else { return }

        // Reset navigation first for clean deep link navigation
        router.popToRoot(tab: router.selectedTab)

        // Small delay to ensure UI is ready
        DispatchQueue.main.asyncAfter(deadline: .now() + 0.1) {
            router.navigate(to: route)
        }
    }
}
```

### Module 5: NavigationSplitView for iPad

```swift
// File: Navigation/AdaptiveNavigationView.swift

import SwiftUI

struct AdaptiveTaskView: View {
    @State private var selectedTask: TaskItem?
    @State private var columnVisibility: NavigationSplitViewVisibility = .all

    var body: some View {
        NavigationSplitView(columnVisibility: $columnVisibility) {
            // Sidebar
            TaskCategoryList(onSelect: { _ in })
        } content: {
            // List
            TaskListForSplitView(selectedTask: $selectedTask)
        } detail: {
            // Detail
            if let task = selectedTask {
                TaskDetailScreen(taskId: task.id)
            } else {
                ContentUnavailableView(
                    "Select a Task",
                    systemImage: "checklist",
                    description: Text("Choose a task from the list to view details.")
                )
            }
        }
        .navigationSplitViewStyle(.balanced)
    }
}
```

---

## Expected Output

### File Structure

```
Navigation/
├── AppRouter.swift              # Centralized router
├── Routes.swift                 # Type-safe route enums
├── RootNavigationView.swift     # Tab + navigation setup
├── DeepLinkHandler.swift        # URL → Route parsing
└── AdaptiveNavigationView.swift # iPad split view
```

### Implementation Checklist

- [ ] Type-safe route enums with Hashable conformance
- [ ] NavigationStack with path binding per tab
- [ ] Programmatic navigation (push, pop, popToRoot)
- [ ] Sheet and full-screen cover management
- [ ] Universal Links deep link parsing
- [ ] Custom URL scheme support
- [ ] NavigationSplitView for iPad
- [ ] onOpenURL handler in root view
- [ ] Navigation state restoration (if required)

---

## Example Interaction

**User:** "I need deep linking support where tapping a notification opens a specific task."

**Assistant:**
```swift
// In your AppDelegate or notification handler:
func userNotificationCenter(
    _ center: UNUserNotificationCenter,
    didReceive response: UNNotificationResponse
) async {
    let userInfo = response.notification.request.content.userInfo
    guard let taskId = userInfo["task_id"] as? String else { return }

    // Navigate using the router
    await MainActor.run {
        let router = AppRouter.shared // or inject via environment
        router.popToRoot(tab: .tasks)
        router.navigate(to: .tasks(.detail(id: taskId)))
    }
}
```

---

## Techniques Used

- **ST-01** (Clear Objective): Single-sentence objective for navigation implementation
- **ST-02** (Sequential Instructions): Modular approach from router to deep links
- **RT-02** (Multi-Dimensional Analysis): Covers stacks, tabs, sheets, split views, deep links
- **RT-04** (Best Practice Review): NavigationStack and type-safe routing best practices
- **ST-03** (Output Format Templates): Code templates for each module

---

## Related Prompts

- [ios_swiftui_screen_builder.md](ios_swiftui_screen_builder.md) - Build screens that plug into navigation
- [ios_state_management.md](ios_state_management.md) - State restoration for navigation
- [ios_push_notifications.md](ios_push_notifications.md) - Notification-triggered navigation
- [ios_app_clips.md](ios_app_clips.md) - App Clip invocation and transition

---

## Customization Guide

### For Coordinator Pattern

Wrap navigation in coordinators:
```swift
@Observable
final class TaskCoordinator {
    var path = NavigationPath()

    func showDetail(id: String) { path.append(TaskRoute.detail(id: id)) }
    func showEdit(id: String) { path.append(TaskRoute.edit(id: id)) }
    func pop() { if !path.isEmpty { path.removeLast() } }
    func popToRoot() { path = NavigationPath() }
}
```

### For Animated Transitions

Add custom navigation transitions:
```swift
.navigationTransition(.zoom(sourceID: item.id, in: namespace))
```

### For State Persistence

Save NavigationPath to disk:
```swift
// NavigationPath supports Codable when all routes are Codable
func savePath() {
    if let data = try? JSONEncoder().encode(taskPath.codable) {
        UserDefaults.standard.set(data, forKey: "taskNavPath")
    }
}
```
