---
title: "iOS Swift Version Migration"
category: mobile-development
description: "Migrate to a new Swift version (5 to 6) with strict concurrency checking, Sendable conformance, actor isolation, data race safety, compiler migration mode, and incremental adoption strategy."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - NE-02
difficulty: advanced
tags:
  - ios
  - swift
  - swift-6
  - migration
  - concurrency
updated: "2026-03-20"
---

# iOS Swift Version Migration

**Objective:** Migrate an iOS project from Swift 5 to Swift 6 by enabling strict concurrency checking incrementally, adding Sendable conformance, resolving actor isolation issues, ensuring data race safety, and leveraging compiler migration modes for a controlled transition.

**When to Use:** Use this prompt when upgrading your project's Swift language version, particularly the Swift 5 to Swift 6 migration which introduces strict concurrency as a requirement. Best started well before a deadline, as concurrency fixes can require architectural changes.

**Prompt Type:** Comprehensive (450+ lines)

---

## Context Gathering

Before migrating, gather essential context:

1. **Current State:**
   - "What Swift version are you currently on (check Build Settings > Swift Language Version)?"
   - "What Xcode version are you using?"
   - "Have you enabled any Swift 6 upcoming features already (`StrictConcurrency`, `GlobalActorIsolatedTypesUsability`, etc.)?"

2. **Concurrency Usage:**
   - "Do you use async/await, actors, or structured concurrency?"
   - "Are there global mutable variables or singletons?"
   - "Do you use completion handlers, Combine, or delegate patterns for async work?"

3. **Codebase Scope:**
   - "How many Swift files / modules in the project?"
   - "Do you have separate Swift packages or frameworks?"
   - "What is your test coverage (concurrency bugs are hard to test)?"

4. **Dependencies:**
   - "Have your third-party dependencies been updated for Swift 6?"
   - "Are there dependencies that expose non-Sendable types you use across isolation boundaries?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before changing ANY Swift language version setting, you MUST:**

1. **Understand Swift 6 concurrency model** - Swift 6 enforces complete data race safety at compile time. Every warning becomes an error.
2. **Audit global state** - All global variables, singletons, and static properties must be audited for thread safety.
3. **Enable warnings first** - Use Swift 5 mode with strict concurrency checking before switching to Swift 6 mode.
4. **Migrate module by module** - Never flip the entire project to Swift 6 at once.
5. **Verify every `@unchecked Sendable`** - Each usage must have a documented justification and thread-safety audit.

**Swift 6 strict concurrency is the largest Swift language change since Swift 3. Plan for significant effort.**

### False-Positive Prevention

- ❌ Do NOT mark types as `@unchecked Sendable` without verifying thread safety
- ❌ Do NOT suppress warnings with `nonisolated(unsafe)` without understanding the data race risk
- ❌ Do NOT assume `@MainActor` fixes all concurrency issues (it only isolates to main thread)
- ❌ Do NOT switch to Swift 6 mode project-wide before resolving all warnings in Swift 5 strict mode
- ❌ Do NOT ignore warnings in test targets - they reveal real concurrency bugs
- ✅ DO enable strict concurrency checking incrementally (per-target)
- ✅ DO use the compiler's suggested fix-its as a starting point, then verify correctness
- ✅ DO document every `@unchecked Sendable` with a comment explaining why it is safe
- ✅ DO use `sending` parameter annotations where ownership transfer is intended
- ✅ DO test with Thread Sanitizer (TSan) enabled to catch runtime data races

---

### Phase 1: Concurrency Audit

#### 1.1 Enable Strict Concurrency Warnings

Start in Swift 5 mode with strict checking to see all issues as warnings (not errors):

**Per-target in Xcode:**
```
Build Settings > Swift Compiler - Upcoming Features > Strict Concurrency Checking = Complete
```

**In Package.swift:**
```swift
.target(
    name: "MyLibrary",
    dependencies: [],
    swiftSettings: [
        .enableUpcomingFeature("StrictConcurrency"),
    ]
)
```

**Per-file (for incremental adoption):**
```bash
# Check warning count by file
xcodebuild build -workspace MyApp.xcworkspace -scheme MyApp 2>&1 \
    | grep "warning:.*concurrency" \
    | sed 's/:.*$//' \
    | sort \
    | uniq -c \
    | sort -rn
```

#### 1.2 Categorize Concurrency Warnings

Common warning categories and their fixes:

| Warning | Meaning | Fix Strategy |
|---------|---------|--------------|
| "Sending value of non-Sendable type" | Type crosses isolation boundary | Make type Sendable or use `sending` |
| "Capture of non-Sendable type in @Sendable closure" | Closure captures non-thread-safe value | Make captured type Sendable |
| "Global variable is not concurrency-safe" | Mutable global state | Use actor, `nonisolated(unsafe)` (if truly safe), or eliminate |
| "Call to main actor-isolated method in non-isolated context" | Missing `await` or `@MainActor` | Add proper isolation annotation |
| "Non-Sendable type passed across isolation boundary" | Actor boundary crossing with unsafe type | Make type Sendable or restructure |
| "Static property is not concurrency-safe" | Static mutable state | Use actor or `nonisolated(unsafe)` with justification |

#### 1.3 Audit Global State

```bash
# Find global mutable variables
grep -rn "^var " --include="*.swift" Sources/
grep -rn "static var " --include="*.swift" Sources/
grep -rn "static let.*=" --include="*.swift" Sources/ | grep -v "private"

# Find singletons
grep -rn "shared\|instance\|default" --include="*.swift" Sources/ | grep "static"

# Find classes with mutable state (potential Sendable issues)
grep -rn "^class " --include="*.swift" Sources/
```

Create a global state inventory:

```markdown
## Global State Inventory

| Location | Type | Mutable | Thread-Safe | Fix |
|----------|------|---------|-------------|-----|
| `AppConfig.shared` | Singleton class | Yes | No - bare properties | Wrap in actor |
| `Logger.instance` | Singleton struct | No | Yes - immutable | Mark Sendable |
| `var currentTheme` | Global var | Yes | No | Move to @MainActor |
| `Cache.imageCache` | Static var | Yes | Yes - NSCache is thread-safe | @unchecked Sendable + document |
```

---

### Phase 2: Sendable Conformance

**CHECKPOINT 1:** Confirm concurrency audit complete and warning count documented before making changes.

```markdown
## Concurrency Warning Summary

| Target | Warning Count | Category Breakdown |
|--------|--------------|-------------------|
| MyApp | [N] | [N] Sendable, [N] actor isolation, [N] global state |
| MyLibrary | [N] | [N] Sendable, [N] actor isolation |
| MyAppTests | [N] | [N] Sendable |

**Total warnings to resolve: [N]**
**Proceed with Sendable conformance phase?**
```

#### 2.1 Making Types Sendable

**Value types (structs, enums):**
```swift
// Most value types composed of Sendable properties are automatically Sendable
struct UserProfile: Sendable {
    let id: UUID
    let name: String
    let email: String
    let createdAt: Date
}

// Enums with Sendable associated values
enum NetworkResult: Sendable {
    case success(Data)
    case failure(NetworkError)  // NetworkError must also be Sendable
}
```

**Reference types (classes) - three strategies:**

```swift
// Strategy 1: Immutable class - all stored properties are let
final class AppConfiguration: Sendable {
    let apiBaseURL: URL
    let environment: Environment
    let featureFlags: [String: Bool]  // Dictionary of Sendable types is Sendable

    init(apiBaseURL: URL, environment: Environment, featureFlags: [String: Bool]) {
        self.apiBaseURL = apiBaseURL
        self.environment = environment
        self.featureFlags = featureFlags
    }
}

// Strategy 2: Actor - state is protected by actor isolation
actor UserSessionManager {
    private var currentUser: User?
    private var authToken: String?

    func login(user: User, token: String) {
        self.currentUser = user
        self.authToken = token
    }

    func currentUserProfile() -> User? {
        currentUser
    }
}

// Strategy 3: @unchecked Sendable - you guarantee thread safety manually
// USE SPARINGLY and always document why it is safe
final class ThreadSafeCache: @unchecked Sendable {
    // THREAD SAFETY: All access to `storage` is protected by `lock`.
    // NSLock is used instead of actor because this is called from
    // synchronous contexts in performance-critical paths.
    private let lock = NSLock()
    private var storage: [String: Any] = [:]

    func get(_ key: String) -> Any? {
        lock.lock()
        defer { lock.unlock() }
        return storage[key]
    }

    func set(_ key: String, value: Any) {
        lock.lock()
        defer { lock.unlock() }
        storage[key] = value
    }
}
```

#### 2.2 Handling Non-Sendable Third-Party Types

```swift
// When a dependency exposes non-Sendable types you cannot modify:

// Option 1: Wrap in a Sendable container
struct SendableImageWrapper: @unchecked Sendable {
    // THREAD SAFETY: UIImage is safe to read from any thread once created.
    // Only the creation/mutation of UIImage is not thread-safe.
    let image: UIImage
}

// Option 2: Use `sending` to transfer ownership
func processImage(sending image: UIImage) async -> ProcessedResult {
    // Compiler ensures `image` is not used after this point by the caller
    await processor.process(image)
}

// Option 3: Isolate to an actor
@MainActor
final class ImageProcessor {
    private var currentImage: UIImage?  // UIImage confined to main actor

    func process() async -> Data? {
        guard let image = currentImage else { return nil }
        return image.pngData()
    }
}
```

---

### Phase 3: Actor Isolation

#### 3.1 MainActor Isolation

```swift
// BEFORE: Implicit main thread assumptions
class HomeViewController: UIViewController {
    var items: [Item] = []  // Mutated from multiple threads

    func loadItems() {
        apiClient.fetchItems { [weak self] result in
            // This may not be on the main thread!
            self?.items = result.items
            self?.tableView.reloadData()
        }
    }
}

// AFTER: Explicit MainActor isolation
@MainActor
class HomeViewController: UIViewController {
    var items: [Item] = []  // Protected by MainActor

    func loadItems() async {
        do {
            let result = try await apiClient.fetchItems()
            // Already on MainActor due to class annotation
            self.items = result.items
            self.tableView.reloadData()
        } catch {
            showError(error)
        }
    }
}
```

#### 3.2 Custom Actor Isolation

```swift
// BEFORE: Singleton with lock-based thread safety
class DatabaseManager {
    static let shared = DatabaseManager()
    private let queue = DispatchQueue(label: "db.queue")
    private var connection: SQLiteConnection?

    func execute(_ query: String) -> [Row] {
        queue.sync {
            connection?.execute(query) ?? []
        }
    }
}

// AFTER: Actor-based isolation
actor DatabaseManager {
    static let shared = DatabaseManager()
    private var connection: SQLiteConnection?

    func execute(_ query: String) -> [Row] {
        // Actor isolation guarantees mutual exclusion
        connection?.execute(query) ?? []
    }
}

// Callers now must use await:
let rows = await DatabaseManager.shared.execute("SELECT * FROM users")
```

#### 3.3 Resolving Actor Isolation Errors

Common patterns:

```swift
// ERROR: "Cannot access property 'name' on actor-isolated instance"
// When accessing actor properties from outside:
let name = await userActor.name  // Add await

// ERROR: "Call to MainActor-isolated method in non-isolated context"
// When calling UI code from non-isolated async context:
Task { @MainActor in
    self.label.text = newValue  // Explicitly on MainActor
}

// ERROR: "Actor-isolated property cannot be referenced from non-isolated context"
// When protocol conformance requires synchronous access:
actor MyActor: CustomStringConvertible {
    let id: String

    // Use nonisolated for properties that don't need isolation
    nonisolated var description: String {
        "MyActor(\(id))"  // Only accesses `let` property - safe
    }
}
```

---

### Phase 4: Incremental Migration Strategy

**CHECKPOINT 2:** Confirm Sendable and actor isolation patterns established before project-wide migration.

```markdown
## Migration Progress

| Target | Warnings Before | Warnings After | Status |
|--------|----------------|----------------|--------|
| SharedModels | 12 | 0 | Ready for Swift 6 |
| Networking | 28 | 3 | In progress |
| MyApp | 156 | 156 | Not started |

**Proceed with incremental Swift 6 enablement?**
```

#### 4.1 Migration Order

Migrate bottom-up through your dependency graph:

```
1. Leaf modules (no internal dependencies)
   └── SharedModels, Constants, Extensions
2. Service modules
   └── Networking, Persistence, Analytics
3. Feature modules
   └── HomeFeature, ProfileFeature, SettingsFeature
4. App target
   └── MyApp (depends on everything)
```

#### 4.2 Per-Module Swift 6 Enablement

```swift
// Package.swift: Enable Swift 6 per target
.target(
    name: "SharedModels",
    dependencies: [],
    swiftSettings: [
        .swiftLanguageMode(.v6),  // This module uses Swift 6
    ]
)

.target(
    name: "Networking",
    dependencies: ["SharedModels"],
    swiftSettings: [
        .swiftLanguageMode(.v5),  // Still on Swift 5
        .enableUpcomingFeature("StrictConcurrency"),  // But with warnings
    ]
)
```

**For Xcode project targets:**
```
Build Settings > Swift Language Version = Swift 6  (per target)
```

#### 4.3 Common Migration Patterns

**Completion handlers to async/await:**
```swift
// BEFORE
func fetchUser(id: String, completion: @escaping (Result<User, Error>) -> Void) {
    urlSession.dataTask(with: request) { data, response, error in
        // Parse and call completion
    }.resume()
}

// AFTER
func fetchUser(id: String) async throws -> User {
    let (data, response) = try await urlSession.data(for: request)
    // Parse and return
}

// BRIDGE: Keep both during migration
func fetchUser(id: String, completion: @escaping (Result<User, Error>) -> Void) {
    Task {
        do {
            let user = try await fetchUser(id: id)
            completion(.success(user))
        } catch {
            completion(.failure(error))
        }
    }
}
```

**Delegate patterns with actors:**
```swift
// BEFORE
class LocationManager: NSObject, CLLocationManagerDelegate {
    var lastLocation: CLLocation?  // Data race: set on delegate queue, read from anywhere

    func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
        lastLocation = locations.last
    }
}

// AFTER
@MainActor
class LocationManager: NSObject, CLLocationManagerDelegate {
    var lastLocation: CLLocation?  // Protected by MainActor

    nonisolated func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
        let location = locations.last
        Task { @MainActor in
            self.lastLocation = location
        }
    }
}
```

#### 4.4 Thread Sanitizer Verification

```bash
# Run tests with Thread Sanitizer enabled
xcodebuild test \
    -workspace MyApp.xcworkspace \
    -scheme MyApp \
    -sdk iphonesimulator \
    -destination 'platform=iOS Simulator,name=iPhone 16' \
    -enableThreadSanitizer YES
```

---

## Expected Output

### Migration Report

```markdown
# Swift 6 Migration Report

## Summary
- Previous Swift version: 5.x
- Target Swift version: 6
- Modules migrated: [N] / [Total]
- Concurrency warnings resolved: [N]
- `@unchecked Sendable` usages: [N] (each documented)
- Actors introduced: [N]
- `@MainActor` annotations added: [N]

## Module Migration Status
| Module | Swift Version | Warnings | Status |
|--------|--------------|----------|--------|
| SharedModels | 6 | 0 | Complete |
| Networking | 6 | 0 | Complete |
| MyApp | 5 (strict) | 12 | In progress |

## Patterns Applied
| Pattern | Count | Example |
|---------|-------|---------|
| Struct Sendable conformance | [N] | `UserProfile: Sendable` |
| Actor conversion | [N] | `DatabaseManager` -> actor |
| @MainActor annotation | [N] | `HomeViewController` |
| @unchecked Sendable | [N] | `ThreadSafeCache` (documented) |
| async/await conversion | [N] | `fetchUser()` |
| sending parameters | [N] | `processImage(sending:)` |

## Remaining Work
| Item | Effort | Blocking? |
|------|--------|-----------|
| [description] | [hours] | [Yes/No] |

## Thread Sanitizer Results
- TSan enabled test run: [PASS / N issues found]
- Issues found and fixed: [list]
```

### Implementation Checklist

- [ ] Strict concurrency warnings enabled in Swift 5 mode
- [ ] All concurrency warnings categorized and counted
- [ ] Global state audited and inventoried
- [ ] Sendable conformance added to value types
- [ ] Actors created for shared mutable state
- [ ] @MainActor applied to UI-layer classes
- [ ] @unchecked Sendable usages documented with thread-safety justification
- [ ] Completion handlers bridged to async/await where applicable
- [ ] Modules migrated bottom-up through dependency graph
- [ ] Thread Sanitizer run with no new issues
- [ ] All tests pass in Swift 6 mode
- [ ] Dependencies verified compatible with Swift 6

---

## Techniques Used

- **ST-01** (Clear Objective): Focused objective on Swift 5 to 6 migration
- **ST-02** (Sequential Instructions): Phased approach from audit to incremental enablement
- **RT-02** (Multi-Dimensional Analysis): Covers Sendable, actor isolation, global state, and migration patterns
- **NE-02** (Phased Workflow): Module-by-module migration with checkpoints

---

## Related Prompts

- [ios_version_upgrade.md](ios_version_upgrade.md) - Upgrade iOS deployment target (often paired with Swift upgrade)
- [ios_dependency_update.md](ios_dependency_update.md) - Update dependencies for Swift 6 compatibility
- [ios_tech_debt_triage.md](ios_tech_debt_triage.md) - Prioritize concurrency tech debt
- [ios_performance_regression_detective.md](ios_performance_regression_detective.md) - Detect performance regressions after migration
