---
title: "iOS Code Modernization"
category: mobile-development
description: "Systematically modernize an iOS codebase to current Swift and platform best practices including Swift 6 strict concurrency, Observation framework, modern SwiftUI patterns, and replacement of deprecated APIs"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-04
  - AG-02
  - NE-02
difficulty: advanced
tags:
  - ios
  - swift
  - modernization
  - swift-6
  - observation
  - swiftui
updated: "2026-03-19"
---

# iOS Code Modernization

**Objective:** Systematically modernize an iOS codebase to current best practices, adopting Swift 6 strict concurrency checking, the Observation framework, modern SwiftUI patterns, and replacing deprecated UIKit and Foundation APIs with their current equivalents.

**When to Use:** Use this prompt when preparing a codebase for Swift 6 migration, replacing deprecated APIs flagged by Xcode warnings, adopting new Apple frameworks (Observation, SwiftData, etc.), or during planned tech debt reduction sprints. Ideal after an architecture review identifies modernization opportunities or before a major feature development cycle.

**Prompt Type:** Comprehensive (500-600 lines)

---

## Context Gathering

Before beginning modernization, understand the scope and constraints:

1. **Current State:**
   - "What Swift version and minimum deployment target does the project use?"
   - "Are there known areas that rely on deprecated APIs or legacy patterns?"
   - "Is the project primarily UIKit, SwiftUI, or a mix?"

2. **Constraints:**
   - "What is the minimum iOS deployment target?"
   - "Are there third-party dependencies that constrain Swift version adoption?"
   - "Is there a preference for incremental changes vs. larger refactors?"

3. **Priorities:**
   - "What matters most: compiler safety, performance, developer experience, or maintainability?"
   - "Are there specific modernization goals (e.g., Swift 6 strict concurrency, Observation adoption)?"

4. **Risk Tolerance:**
   - "Are there areas that are off-limits due to stability concerns?"
   - "What is the test coverage like for areas we might modernize?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Trace actual deprecation status** - Do not flag code based on age alone. Verify the API is deprecated in the current SDK.
2. **Check for existing modernization** - Search for migration work already in progress.
3. **Understand the context** - Consider WHY legacy patterns exist. Deployment target constraints and stability may justify older approaches.
4. **Confirm actual benefit** - Does modernizing this provide real value? Some older code works fine and does not need updating.
5. **Provide specific file:line locations** - Every finding MUST include exact code locations (e.g., `UserManager.swift:42`).

**Finding LIMITED modernization needs is an acceptable outcome.** If the code is reasonably modern and working, say so with confidence. Do not manufacture modernization urgency.

### False-Positive Prevention

- ❌ Do NOT flag working stable code as "must modernize"
- ❌ Do NOT assume all older patterns are wrong
- ❌ Do NOT recommend modernization without considering migration risk
- ❌ Do NOT report stylistic preferences as modernization requirements
- ❌ Do NOT suggest Observation framework adoption if deployment target is below iOS 17
- ✅ DO differentiate between deprecated APIs and merely older patterns
- ✅ DO consider test coverage before recommending changes
- ✅ DO verify deployment target supports the suggested modern API
- ✅ DO prioritize actual deprecations and compiler warnings over cosmetic updates

---

### Phase 1: Modernization Opportunity Discovery

#### 1.1 Swift Language Modernization

**Scan for outdated Swift patterns:**

```swift
// OUTDATED: Optional binding cascade
if let user = user {
    if let name = user.name {
        if let email = user.email {
            display(name: name, email: email)
        }
    }
}

// MODERN: Swift 5.7+ shorthand optional binding + multi-binding
if let user, let name = user.name, let email = user.email {
    display(name: name, email: email)
}

// OUTDATED: Stringly-typed selectors
button.addTarget(self, action: Selector("buttonTapped"), for: .touchUpInside)

// MODERN: #selector
button.addTarget(self, action: #selector(buttonTapped), for: .touchUpInside)

// OUTDATED: Any/AnyObject casting chains
guard let dict = json as? [String: Any],
      let name = dict["name"] as? String else { return }

// MODERN: Codable
struct User: Codable {
    let name: String
}
let user = try JSONDecoder().decode(User.self, from: data)
```

**Swift Modernization Checklist:**

| Pattern | Current State | Modern Alternative |
|---------|--------------|-------------------|
| Optional binding | `if let x = x` | `if let x` (Swift 5.7+) |
| Existential any | `protocol P` as type | `any P` explicit (Swift 5.6+) |
| Primary associated types | `AnyPublisher<Out, Err>` | `some Publisher<Out>` |
| Regex | `NSRegularExpression` | Swift Regex `/.../` (Swift 5.7+) |
| Opaque parameters | `func f<T: P>(_ x: T)` | `func f(_ x: some P)` |
| if/switch expressions | Multi-line assignment | `let x = if cond { a } else { b }` (Swift 5.9+) |
| Noncopyable types | N/A | `~Copyable` where appropriate |
| Consuming/borrowing | Implicit copy | `consuming`, `borrowing` annotations |

#### 1.2 Swift 6 Strict Concurrency Adoption

**Identify concurrency safety gaps:**

```swift
// WARNING in Swift 6: Mutable global state
var sharedCache: [String: Data] = [:]

// MODERN: Actor-isolated state
actor CacheManager {
    private var cache: [String: Data] = [:]

    func get(_ key: String) -> Data? { cache[key] }
    func set(_ key: String, data: Data) { cache[key] = data }
}

// WARNING in Swift 6: Non-Sendable type crossing isolation boundary
class UserManager {
    var currentUser: User? // Not Sendable

    func fetchUser() async {
        let user = await api.getUser()
        self.currentUser = user // Data race potential
    }
}

// MODERN: Actor or MainActor isolation
@MainActor
class UserManager {
    var currentUser: User?

    func fetchUser() async {
        let user = await api.getUser()
        self.currentUser = user // Safe: MainActor-isolated
    }
}
```

#### 1.3 Observation Framework Migration

**Replace ObservableObject with @Observable (iOS 17+):**

```swift
// LEGACY: Combine-based ObservableObject
class UserViewModel: ObservableObject {
    @Published var name: String = ""
    @Published var email: String = ""
    @Published var isLoading: Bool = false

    func load() {
        isLoading = true
        Task {
            let user = try await api.fetchUser()
            name = user.name
            email = user.email
            isLoading = false
        }
    }
}

// MODERN: Observation framework
@Observable
class UserViewModel {
    var name: String = ""
    var email: String = ""
    var isLoading: Bool = false

    func load() {
        isLoading = true
        Task {
            let user = try await api.fetchUser()
            name = user.name
            email = user.email
            isLoading = false
        }
    }
}

// View usage changes:
// LEGACY:
struct UserView: View {
    @ObservedObject var viewModel: UserViewModel
    // or @StateObject var viewModel = UserViewModel()
}

// MODERN:
struct UserView: View {
    @State var viewModel = UserViewModel()
    // No wrapper needed for passed-in references - just use var
}
```

#### 1.4 Deprecated API Detection

**Search for deprecated APIs:**

```swift
// DEPRECATED: UIApplication.shared.open without completion
UIApplication.shared.openURL(url)
// MODERN:
await UIApplication.shared.open(url)

// DEPRECATED: UIActivityIndicatorView styles
let spinner = UIActivityIndicatorView(style: .whiteLarge)
// MODERN:
let spinner = UIActivityIndicatorView(style: .large)

// DEPRECATED: UITableViewCell accessory
cell.accessoryType = .detailDisclosureButton
// Still valid, but consider SwiftUI List instead

// DEPRECATED: NSKeyedUnarchiver unarchiveObject
let data = NSKeyedUnarchiver.unarchiveObject(with: archivedData)
// MODERN:
let data = try NSKeyedUnarchiver.unarchivedObject(ofClass: MyClass.self, from: archivedData)
```

---

### Phase 2: Categorize Opportunities

**CHECKPOINT 1:** Present discovered modernization opportunities.

```markdown
## Modernization Opportunities Discovered

### Summary

| Category | Items Found | Effort | Impact |
|----------|-------------|--------|--------|
| Swift Language | [X] items | [Low/Med/High] | [Impact] |
| Swift 6 Concurrency | [X] items | [Low/Med/High] | [Impact] |
| Observation Migration | [X] items | [Low/Med/High] | [Impact] |
| Deprecated APIs | [X] items | [Low/Med/High] | [Impact] |

### Quick Wins (Low Effort, High Value)
1. [Opportunity] - [Location] - [Benefit]

### Strategic Improvements (Medium Effort)
1. [Opportunity] - [Files affected] - [Benefit]

### Major Migrations (High Effort)
1. [Migration] - [Scope] - [Risk level]

### Questions
1. Which categories would you like to prioritize?
2. Should I proceed with quick wins immediately?
```

---

### Phase 3: Detailed Modernization Plan

After user feedback, create a detailed implementation plan.

#### 3.1 Swift 6 Strict Concurrency Enablement

**Incremental enablement strategy:**

```swift
// Step 1: Enable per-target in Package.swift or build settings
// In Package.swift:
.target(
    name: "MyTarget",
    swiftSettings: [
        .enableUpcomingFeature("StrictConcurrency")
    ]
)

// Step 2: Add Sendable conformance to value types
struct UserDTO: Sendable {
    let id: String
    let name: String
    let email: String
}

// Step 3: Mark classes that need MainActor
@MainActor
final class ProfileViewController: UIViewController {
    // All properties and methods are MainActor-isolated
}

// Step 4: Convert shared mutable state to actors
// BEFORE:
class NetworkCache {
    static let shared = NetworkCache()
    private var store: [URL: Data] = [:]
    private let queue = DispatchQueue(label: "cache")

    func get(_ url: URL) -> Data? {
        queue.sync { store[url] }
    }
}

// AFTER:
actor NetworkCache {
    static let shared = NetworkCache()
    private var store: [URL: Data] = [:]

    func get(_ url: URL) -> Data? {
        store[url]
    }
}
```

#### 3.2 SwiftData Adoption (iOS 17+)

```swift
// LEGACY: Core Data model
class CDUser: NSManagedObject {
    @NSManaged var name: String?
    @NSManaged var email: String?
    @NSManaged var createdAt: Date?
}

// MODERN: SwiftData model
@Model
class User {
    var name: String
    var email: String
    var createdAt: Date

    init(name: String, email: String, createdAt: Date = .now) {
        self.name = name
        self.email = email
        self.createdAt = createdAt
    }
}
```

---

### Phase 4: Implementation

**CHECKPOINT 2:** Before making changes, confirm the plan.

```markdown
## Implementation Plan Confirmation

### Changes to Make

**Immediate (Will do now):**
1. [Specific change] - [X files affected]
2. [Specific change] - [X files affected]

**Deferred (After verification):**
1. [Change requiring more testing]

### Files to Modify

| File | Changes | Risk |
|------|---------|------|
| [file] | [description] | [Low/Med/High] |

### Verification Steps
1. Build project after changes
2. Run existing tests
3. Manual verification of [areas]

**Proceed with implementation? (yes/no)**
```

---

### Phase 5: Execute and Report

After approval, make changes systematically:

1. **Make changes incrementally** - One category at a time
2. **Preserve behavior** - Refactor, do not change functionality
3. **Document changes** - Track all modifications
4. **Verify after each change** - Ensure builds pass

**Final Report:**

```markdown
## Modernization Complete

### Changes Made

| Category | Files Modified | Changes |
|----------|---------------|---------|
| Swift Language | [X] | [Summary] |
| Swift 6 Concurrency | [X] | [Summary] |
| Observation | [X] | [Summary] |
| Deprecated APIs | [X] | [Summary] |

### Verification
- [ ] Project builds successfully
- [ ] All tests pass
- [ ] No new warnings introduced

### Remaining Opportunities
[Items not addressed in this session and why]
```

---

## Expected Output

1. **Discovery Report** - All modernization opportunities found with file:line locations
2. **Prioritized Plan** - Categorized by effort and impact
3. **Implementation Details** - Specific code changes with before/after
4. **Change Log** - Record of all modifications made
5. **Verification Report** - Build and test status after changes

---

## Example Interaction

**User provides a ViewModel file:**

```swift
// BEFORE: ProfileViewModel.swift
class ProfileViewModel: ObservableObject {
    @Published var name: String = ""
    @Published var isLoading = false

    private var cancellables = Set<AnyCancellable>()

    func load() {
        isLoading = true
        URLSession.shared.dataTaskPublisher(for: url)
            .map(\.data)
            .decode(type: Profile.self, decoder: JSONDecoder())
            .receive(on: DispatchQueue.main)
            .sink(receiveCompletion: { _ in },
                  receiveValue: { [weak self] profile in
                self?.name = profile.name
                self?.isLoading = false
            })
            .store(in: &cancellables)
    }
}
```

**Agent produces:**

```swift
// AFTER: ProfileViewModel.swift (iOS 17+, Swift 6)
@Observable
@MainActor
final class ProfileViewModel {
    var name: String = ""
    var isLoading = false

    func load() async throws {
        isLoading = true
        defer { isLoading = false }

        let (data, _) = try await URLSession.shared.data(from: url)
        let profile = try JSONDecoder().decode(Profile.self, from: data)
        name = profile.name
    }
}
```

**Changes explained:**
- `ObservableObject` + `@Published` replaced with `@Observable` (Observation framework)
- Combine pipeline replaced with `async/await`
- `@MainActor` added for thread safety
- `final` added to enable compiler optimizations
- `[weak self]` no longer needed (no retain cycle with structured concurrency)
- `defer` for consistent loading state cleanup

---

## Techniques Used

- **ST-01** (Clear Objective): Focused modernization objective
- **ST-02** (Sequential Instructions): Phased discovery, plan, implement
- **RT-02** (Multi-Format Output): Tables, code, and markdown reports
- **RT-04** (Best Practice Review): Modern Swift and iOS standards
- **AG-02** (Iterative Refinement): Checkpoint-based approval gates
- **NE-02** (Phased Workflow): Clear phases with validation between each

---

## Related Prompts

- [ios_swift_concurrency_adoption.md](ios_swift_concurrency_adoption.md) - Deep dive on async/await migration
- [ios_swiftui_migration.md](ios_swiftui_migration.md) - UIKit to SwiftUI migration
- [ios_error_handling_improvement.md](ios_error_handling_improvement.md) - Typed throws adoption
- [ios_memory_leak_detection.md](ios_memory_leak_detection.md) - Retain cycle detection

---

## Customization Guide

### For Swift 6 Migration Only

Focus exclusively on concurrency:
- Enable `StrictConcurrency` upcoming feature flag
- Add `Sendable` conformances
- Convert shared state to actors
- Add `@MainActor` to UI-bound types
- Resolve all `-strict-concurrency=complete` warnings

### For Observation Framework Only

Focus on the data flow layer:
- Replace `ObservableObject` with `@Observable`
- Replace `@StateObject` with `@State`
- Remove `@ObservedObject` wrappers
- Update `@EnvironmentObject` to `@Environment`
- Verify fine-grained view updates

### For Legacy Codebase (iOS 15+)

Skip iOS 17+ features and focus on:
- Swift language modernization (5.7+ features)
- Deprecated UIKit API replacement
- Structured concurrency adoption
- Combine to async/await bridge patterns

### For SwiftData Migration

Focus on persistence layer:
- Core Data model to `@Model` conversion
- `NSFetchRequest` to `@Query` migration
- `NSManagedObjectContext` to `ModelContext`
- Migration plan for existing persistent stores
