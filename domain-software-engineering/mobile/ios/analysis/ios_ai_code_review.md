---
title: "iOS AI-Assisted Code Review"
category: mobile-development
description: "AI-assisted code review for Swift/iOS covering Swift-specific patterns, memory management, concurrency safety, API usage correctness, and Apple framework best practices"
techniques:
  - ST-01
  - ST-02
difficulty: intermediate
tags:
  - ios
  - swift
  - code-review
  - ai-agent
updated: "2026-03-20"
---

# iOS AI-Assisted Code Review

**Objective:** Perform an AI-assisted code review of Swift/iOS code focusing on Swift-specific patterns and idioms, memory management and retain cycle prevention, Swift Concurrency safety, correct usage of Apple framework APIs, and adherence to iOS platform best practices to catch issues that standard linters miss.

**When to Use:** Use this prompt as part of the pull request review process, when reviewing code from new team members unfamiliar with iOS conventions, when auditing code quality across a feature or module, or when preparing code for production after rapid prototyping.

**Prompt Type:** Modular (200-350 lines)

---

## Context Gathering

Before beginning the review, gather context:

1. **Review Scope:**
   - "What files or feature should I review? (specific PR, module, or full codebase)"
   - "What is the minimum deployment target?"

2. **Project Standards:**
   - "Are there team coding guidelines or a Swift style guide in use?"
   - "Is there a linter configured (SwiftLint, SwiftFormat)? What rules?"

3. **Focus Areas:**
   - "Any specific concerns? (memory leaks, concurrency, performance, correctness)"
   - "Is this new code, refactored code, or legacy code being reviewed?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Read the full context** - Don't flag a pattern as wrong based on a single line. Understand the surrounding code, the class purpose, and the feature intent.
2. **Verify it's actually a bug, not a style preference** - Distinguish between "this will crash/leak/race" and "I would write it differently."
3. **Check if it's intentional** - Comments, documentation, or consistent patterns may explain unusual code.
4. **Categorize severity accurately** - A potential crash is not the same as a style nit.
5. **Provide specific file:line locations** - Every finding MUST include exact code locations.

**Code that works correctly, is readable, and follows the project's established patterns is good code.** Don't rewrite working code to match a different style preference.

### False-Positive Prevention

- ❌ Do NOT flag style differences as bugs (spaces vs tabs, trailing commas, brace style)
- ❌ Do NOT flag intentional force unwraps in tests or IBOutlets (common and acceptable)
- ❌ Do NOT flag every closure as a potential retain cycle without verifying the ownership graph
- ❌ Do NOT recommend rewriting working code to use newer APIs unless there's a concrete benefit
- ✅ DO focus on correctness, safety, and maintainability over style
- ✅ DO flag actual memory leaks with evidence of the retain cycle
- ✅ DO flag concurrency issues with explanation of the race condition
- ✅ DO flag API misuse that will cause runtime crashes or undefined behavior

---

### Review Area 1: Swift Language Patterns

#### 1.1 Value Types vs Reference Types

```swift
// CHECK: Appropriate type choice

// ❌ Class where struct would be better (unnecessary reference semantics)
class UserSettings {  // No inheritance, no identity, no shared mutation
    var theme: Theme
    var fontSize: Int
}
// ✅ Fix: Use struct
struct UserSettings {
    var theme: Theme
    var fontSize: Int
}

// ❌ Struct where class is needed (fighting value semantics)
struct NetworkManager {  // Needs shared state, identity
    var cache: [URL: Data]
    mutating func fetch(_ url: URL) { }  // Mutating everywhere = wrong type
}

// CHECK: Large structs passed by value repeatedly
// Structs with many properties or containing reference types (COW not automatic)
```

#### 1.2 Optional Handling

```swift
// CHECK: Force unwrap safety

// ❌ Dangerous force unwrap
let user = fetchUser()!  // Will crash if nil

// ✅ Safe alternatives
guard let user = fetchUser() else { return }
if let user = fetchUser() { /* use user */ }
let user = fetchUser() ?? defaultUser

// ❌ Pyramid of doom
if let a = optA {
    if let b = optB {
        if let c = optC {
            // ...
        }
    }
}

// ✅ Combined optional binding
if let a = optA, let b = optB, let c = optC {
    // ...
}

// CHECK: Implicit unwrap safety
// IBOutlets: @IBOutlet var label: UILabel! — acceptable in UIKit
// Other uses: Verify initialization guarantee before first access

// CHECK: Optional chaining depth
// foo?.bar?.baz?.qux — may indicate missing model design
```

#### 1.3 Error Handling

```swift
// CHECK: Error handling patterns

// ❌ Swallowing errors silently
do {
    try saveData()
} catch {
    // Empty catch — data loss with no indication
}

// ❌ Generic catch without logging
do {
    try saveData()
} catch {
    print("error")  // No context, not actionable
}

// ✅ Proper error handling
do {
    try saveData()
} catch {
    Logger.error("Failed to save user data: \(error.localizedDescription)", context: error)
    throw DataError.saveFailed(underlying: error)
}

// CHECK: Result type usage
// Are Result types used consistently?
// Are errors mapped to meaningful app-specific types?

// CHECK: try? usage
let data = try? JSONDecoder().decode(User.self, from: responseData)
// Is silently returning nil acceptable here, or should the error propagate?
```

#### 1.4 Protocol Conformance

```swift
// CHECK: Equatable / Hashable correctness
struct User: Hashable {
    let id: UUID
    let name: String
    let profileImageURL: URL?

    // ❌ Default Hashable hashes ALL properties — inefficient for collections
    // ✅ If id uniquely identifies, hash only id:
    func hash(into hasher: inout Hasher) {
        hasher.combine(id)
    }
    static func == (lhs: User, rhs: User) -> Bool {
        lhs.id == rhs.id
    }
}

// CHECK: Codable correctness
struct APIResponse: Codable {
    let items: [Item]
    let nextPageToken: String?

    // CHECK: Do CodingKeys match actual API field names?
    // CHECK: Are optional fields truly optional in the API?
    // CHECK: Are date decoding strategies configured correctly?
}

// CHECK: Sendable conformance (Swift 6)
// Are types shared across concurrency boundaries marked Sendable?
// Are non-Sendable types used correctly with actors?
```

---

### Review Area 2: Memory Management

#### 2.1 Retain Cycle Detection

```swift
// CHECK: Closure capture lists

// ❌ Strong self in closure stored by self
class ViewModel {
    var onUpdate: (() -> Void)?

    func setup() {
        onUpdate = {
            self.refresh()  // Strong capture → retain cycle
        }
    }
}

// ✅ Weak capture
onUpdate = { [weak self] in
    self?.refresh()
}

// CHECK: Common retain cycle patterns:
// 1. Timer closures:    Timer.scheduledTimer { self.tick() }
// 2. NotificationCenter: .addObserver(forName:) { _ in self.handle() }
// 3. Combine sinks:     .sink { self.process($0) }
// 4. Delegate cycles:   child.delegate = self (delegate should be weak)
// 5. Closure properties: self.completion = { self.finish() }

// CHECK: Appropriate weak vs unowned
// weak  — Use when captured object may become nil during closure lifetime
// unowned — Use ONLY when you guarantee captured object outlives the closure
// unowned is a crash if wrong; prefer weak unless performance-critical
```

#### 2.2 Deallocation Verification

```swift
// CHECK: Resources cleaned up in deinit
class StreamManager {
    private var connection: WebSocketConnection?
    private var timer: Timer?
    private var cancellables = Set<AnyCancellable>()

    deinit {
        connection?.close()    // ✅ Close connections
        timer?.invalidate()     // ✅ Invalidate timers
        // cancellables automatically cancelled when Set deallocates ✅
    }
}

// CHECK: Observation cleanup
// KVO: invalidate observation tokens
// NotificationCenter: removeObserver if using selector-based API
// Combine: cancel subscriptions or let AnyCancellable deinit
```

#### 2.3 Collection Memory

```swift
// CHECK: Large collection handling
// - Arrays of images loaded all at once (use lazy loading)
// - Caches without eviction (NSCache preferred over Dictionary)
// - Unbounded growth (append without limit)

// CHECK: Image memory
// UIImage(named:) caches permanently — use UIImage(contentsOfFile:) for large images
// Ensure image resizing before display (not loading 4K image into 44pt cell)

// CHECK: Core Data fault handling
// Fetching large result sets without batching
// Not using fetchBatchSize
```

---

### Review Area 3: Concurrency Safety

#### 3.1 Swift Concurrency Patterns

```swift
// CHECK: MainActor annotation
// UI updates MUST happen on main thread/actor

// ❌ Missing MainActor
class ViewModel: ObservableObject {
    @Published var items: [Item] = []

    func fetch() async {
        let items = try await api.fetchItems()
        self.items = items  // May not be on MainActor!
    }
}

// ✅ Correct MainActor usage
@MainActor
class ViewModel: ObservableObject {
    @Published var items: [Item] = []

    func fetch() async {
        let items = try await api.fetchItems()
        self.items = items  // Guaranteed on MainActor
    }
}

// CHECK: Task cancellation handling
func fetchData() async throws -> Data {
    let data = try await URLSession.shared.data(from: url).0
    try Task.checkCancellation()  // Check before expensive processing
    return try process(data)
}

// CHECK: Task lifecycle
// Are tasks stored and cancelled when views disappear?
// task modifier in SwiftUI handles this automatically
// Manual Task { } instances need manual cancellation
```

#### 3.2 Actor Isolation

```swift
// CHECK: Actor usage correctness

// ❌ Shared mutable state without protection
class DataCache {
    var cache: [String: Data] = [:]  // Data race!

    func store(_ data: Data, for key: String) {
        cache[key] = data
    }
}

// ✅ Actor protection
actor DataCache {
    var cache: [String: Data] = [:]

    func store(_ data: Data, for key: String) {
        cache[key] = data
    }
}

// CHECK: Sendable compliance
// Types passed across actor boundaries must be Sendable
// Check for @unchecked Sendable (verify thread safety manually)
// Check for nonisolated(unsafe) usage (Swift 5.10+)
```

#### 3.3 Legacy Concurrency

```swift
// CHECK: DispatchQueue safety (if not using Swift Concurrency)

// ❌ Accessing shared state from multiple queues without sync
var results: [Result] = []
queue1.async { results.append(result1) }  // Race condition
queue2.async { results.append(result2) }

// ❌ Deadlock risk
serialQueue.sync {
    serialQueue.sync { }  // Deadlock!
}

// CHECK: Main thread violations
// Network calls on main thread
// File I/O on main thread
// Heavy computation on main thread
// Core Data access from wrong queue
```

---

### Review Area 4: Apple Framework Best Practices

#### 4.1 SwiftUI Patterns

```swift
// CHECK: View body complexity
var body: some View {
    // Bodies > 50 lines should be decomposed into subviews
    // Extract into computed properties or separate View structs
}

// CHECK: State management correctness
@State var user: User           // Only for view-local, simple state
@StateObject var viewModel      // For ObservableObject owned by this view
@ObservedObject var viewModel   // For ObservableObject passed in (not owned)
@EnvironmentObject var store    // For shared app state
@Binding var isPresented        // For two-way binding from parent

// ❌ Common mistakes:
@ObservedObject var vm = ViewModel()  // Re-created every view update!
@State var viewModel = ViewModel()     // Won't observe @Published changes

// CHECK: Performance
// - Unnecessary view re-renders (use Equatable conformance)
// - Heavy computation in body (use .task or onAppear)
// - Large ForEach without identifiable IDs
```

#### 4.2 UIKit Patterns

```swift
// CHECK: View controller lifecycle
// - Heavy work in viewDidLoad blocking launch
// - Not handling viewWillAppear/viewDidDisappear symmetrically
// - Missing trait collection change handling

// CHECK: Table/Collection view
// - Cell reuse identifier typos (use constants or enums)
// - Missing prepareForReuse cleanup
// - Blocking main thread in cellForRowAt

// CHECK: Auto Layout
// - Conflicting constraints (check for console warnings)
// - Missing translatesAutoresizingMaskIntoConstraints = false
// - Ambiguous layout conditions
```

#### 4.3 API Usage Correctness

```swift
// CHECK: Common API misuse

// URLSession
// ❌ Not handling both data and error
URLSession.shared.dataTask(with: url) { data, response, error in
    let result = try! JSONDecoder().decode(T.self, from: data!)
    // Ignoring error, force-unwrapping data
}

// Core Data
// ❌ Accessing managed objects across contexts
let object = mainContext.fetch(request).first!
backgroundContext.perform {
    object.name = "new"  // CRASH — wrong context
}

// UserDefaults
// ❌ Synchronous access on main thread for complex data
let largeData = UserDefaults.standard.data(forKey: "bigCache")

// Keychain
// ❌ Not checking SecItemAdd return status
SecItemAdd(query as CFDictionary, nil)  // May fail silently (duplicate, etc.)
```

---

### Review Summary Format

**Present findings in this structure:**

```markdown
## Code Review Summary

### Statistics
- Files reviewed: [N]
- Issues found: [N] (Critical: [N], High: [N], Medium: [N], Low: [N], Nit: [N])

### Critical Issues (Must Fix)
| # | File:Line | Issue | Category | Fix |
|---|-----------|-------|----------|-----|
| 1 | [Location] | [Description] | [Memory/Concurrency/Correctness] | [How to fix] |

### High Issues (Should Fix)
| # | File:Line | Issue | Category | Fix |
|---|-----------|-------|----------|-----|

### Medium Issues (Recommended)
| # | File:Line | Issue | Category | Fix |
|---|-----------|-------|----------|-----|

### Positive Observations
- [Good patterns observed]
- [Well-implemented areas]
```

---

## Expected Output

1. **Issue Catalog** - All findings with file:line locations and severity
2. **Category Breakdown** - Issues organized by review area (patterns, memory, concurrency, frameworks)
3. **Fix Recommendations** - Specific code changes for each finding
4. **Positive Observations** - Well-implemented patterns worth maintaining

---

## Example Interaction

**User:** Review this pull request for our iOS shopping app. It adds a new wishlist feature.

**Agent:** I'll review the wishlist feature code focusing on Swift patterns, memory safety, concurrency, and framework usage.

*[Agent reviews all files in the PR]*

**Agent:**

## Code Review — Wishlist Feature

### Statistics
- Files reviewed: 8
- Issues found: 11 (Critical: 1, High: 3, Medium: 4, Low: 2, Nit: 1)

### Critical Issues

| # | Location | Issue | Fix |
|---|----------|-------|-----|
| 1 | `WishlistViewModel.swift:67` | Retain cycle: `onUpdate` closure captures `self` strongly, stored as property on `self` | Add `[weak self]` to capture list |

### High Issues

| # | Location | Issue | Fix |
|---|----------|-------|-----|
| 2 | `WishlistViewModel.swift:34` | Missing `@MainActor` — `@Published` properties updated from background async context | Add `@MainActor` to class or `await MainActor.run { }` |
| 3 | `WishlistRepository.swift:89` | `try!` on JSONDecoder in production code — will crash on malformed server response | Replace with `do/catch` and proper error handling |
| 4 | `WishlistCell.swift:23` | UIImage(named:) used for product images — permanently caches, will consume memory | Use async image loading with UIImage(contentsOfFile:) or Kingfisher |

### Positive Observations
- Clean separation between WishlistViewModel and WishlistRepository
- Good use of Swift enums for wishlist state
- Proper use of `@FetchRequest` for Core Data integration in WishlistView

---

## Techniques Used

- **ST-01** (Clear Objective): Focused code review with defined review areas
- **ST-02** (Sequential Instructions): Structured review areas from language patterns through framework usage

---

## Related Prompts

- [ios_architecture_review.md](ios_architecture_review.md) - Architecture-level review
- [ios_performance_audit.md](ios_performance_audit.md) - Performance-focused analysis
- [ios_codebase_health_assessment.md](ios_codebase_health_assessment.md) - Broader health check
- [ios_test_coverage_analysis.md](ios_test_coverage_analysis.md) - Test quality assessment

---

## Customization Guide

### For SwiftUI-Heavy Codebase
- Add focus on @Observable vs ObservableObject patterns
- Check for proper use of @Environment and custom EnvironmentKeys
- Verify .task modifier usage for async work
- Check for NavigationStack / NavigationSplitView patterns
- Assess preview quality and coverage

### For Swift 6 Strict Concurrency
- Enable strict concurrency warnings assessment
- Check all @Sendable conformances
- Verify actor isolation boundaries
- Flag `@unchecked Sendable` for manual verification
- Check for `nonisolated(unsafe)` usage patterns

### For Team Onboarding
- Include explanations with each finding (educational)
- Reference Apple documentation links
- Highlight patterns the team should adopt as conventions
- Create a "common mistakes" summary from review findings

### For Performance-Critical Code
- Add Instruments profiling recommendations for flagged areas
- Check for main thread blocking in critical paths
- Assess collection algorithm complexity (O(n^2) in loops)
- Flag synchronous I/O on the main thread
