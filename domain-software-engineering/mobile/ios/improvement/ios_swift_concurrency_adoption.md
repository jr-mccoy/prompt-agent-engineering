---
title: "iOS Swift Concurrency Adoption"
category: mobile-development
description: "Convert completion handlers to async/await, introduce actors for shared state, add Sendable conformance, and resolve data race warnings for Swift 6 strict concurrency"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-04
  - AG-02
difficulty: advanced
tags:
  - ios
  - swift
  - concurrency
  - async-await
  - actors
  - sendable
updated: "2026-03-19"
---

# iOS Swift Concurrency Adoption

**Objective:** Convert an iOS codebase from callback/completion-handler patterns to Swift structured concurrency, introduce actors for shared mutable state, add Sendable conformance throughout, and resolve all data race warnings to achieve Swift 6 strict concurrency compliance.

**When to Use:** Use this prompt when migrating from completion handlers or Combine to async/await, when enabling Swift 6 strict concurrency checking, when Xcode shows data race warnings, when introducing actors for thread-safe shared state, or when preparing the codebase for the Swift 6 language mode.

**Prompt Type:** Comprehensive (500-600 lines)

---

## Context Gathering

Before beginning adoption, understand the current state:

1. **Current Concurrency Model:**
   - "What patterns are used? (GCD, OperationQueue, Combine, completion handlers)"
   - "Are there any existing async/await usage?"
   - "What threading issues have been encountered?"

2. **Swift Version:**
   - "What Swift version is the project using?"
   - "Is strict concurrency checking enabled? (none, targeted, complete)"
   - "Are there plans to adopt Swift 6 language mode?"

3. **Architecture:**
   - "Is there shared mutable state? (singletons, caches, managers)"
   - "How is UI updated from background work?"
   - "Are there third-party APIs that use callbacks?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Verify the race condition** - Not all non-Sendable types are unsafe. Check actual concurrent access.
2. **Check existing synchronization** - GCD serial queues and locks may already protect shared state.
3. **Test the conversion** - Ensure async/await behaves identically to the callback version.
4. **Verify cancellation behavior** - Structured concurrency has different cancellation semantics.
5. **Provide specific file:line locations** - Every finding MUST include exact code locations.

**Finding SAFE existing concurrency is an acceptable outcome.** Well-implemented GCD code is not inherently broken. Migration should improve clarity, not just change syntax.

### False-Positive Prevention

- ❌ Do NOT flag all GCD usage as needing migration (some is appropriate)
- ❌ Do NOT assume every class needs `@Sendable` conformance
- ❌ Do NOT convert Combine pipelines that work well just for the sake of async/await
- ❌ Do NOT add `@MainActor` to every class (only UI-bound ones)
- ✅ DO verify that converted code maintains the same threading guarantees
- ✅ DO check that Task cancellation is properly handled
- ✅ DO ensure actor isolation does not introduce deadlocks
- ✅ DO test that error propagation works correctly through async boundaries

---

### Phase 1: Completion Handler to Async/Await

#### 1.1 Simple Conversion

```swift
// BEFORE: Completion handler
func fetchUser(id: String, completion: @escaping (Result<User, Error>) -> Void) {
    URLSession.shared.dataTask(with: makeRequest(id: id)) { data, response, error in
        if let error = error {
            completion(.failure(error))
            return
        }
        guard let data = data else {
            completion(.failure(APIError.noData))
            return
        }
        do {
            let user = try JSONDecoder().decode(User.self, from: data)
            completion(.success(user))
        } catch {
            completion(.failure(error))
        }
    }.resume()
}

// Usage:
fetchUser(id: "123") { result in
    DispatchQueue.main.async {
        switch result {
        case .success(let user):
            self.updateUI(with: user)
        case .failure(let error):
            self.showError(error)
        }
    }
}

// AFTER: Async/await
func fetchUser(id: String) async throws -> User {
    let (data, _) = try await URLSession.shared.data(from: makeRequest(id: id))
    return try JSONDecoder().decode(User.self, from: data)
}

// Usage:
Task {
    do {
        let user = try await fetchUser(id: "123")
        updateUI(with: user) // Already on MainActor if view is @MainActor
    } catch {
        showError(error)
    }
}
```

#### 1.2 Wrapping Legacy Callbacks with Continuations

```swift
// Legacy API that cannot be changed (third-party, ObjC, etc.)
class LegacyLocationService {
    func requestLocation(callback: @escaping (CLLocation?, Error?) -> Void)
}

// Wrap with continuation
extension LegacyLocationService {
    func requestLocation() async throws -> CLLocation {
        try await withCheckedThrowingContinuation { continuation in
            requestLocation { location, error in
                if let error = error {
                    continuation.resume(throwing: error)
                } else if let location = location {
                    continuation.resume(returning: location)
                } else {
                    continuation.resume(throwing: LocationError.unknown)
                }
            }
        }
    }
}

// IMPORTANT: Each continuation must be resumed exactly once
// Use withCheckedContinuation/withCheckedThrowingContinuation during development
// Switch to withUnsafeContinuation for performance in production if needed
```

#### 1.3 Converting Delegate Patterns

```swift
// BEFORE: Delegate-based async work
protocol ImageDownloaderDelegate: AnyObject {
    func downloader(_ downloader: ImageDownloader, didFinish image: UIImage)
    func downloader(_ downloader: ImageDownloader, didFail error: Error)
}

class ImageDownloader {
    weak var delegate: ImageDownloaderDelegate?
    func download(url: URL) { /* ... calls delegate ... */ }
}

// AFTER: AsyncSequence for streaming or async for one-shot
class ImageDownloader {
    func download(url: URL) async throws -> UIImage {
        let (data, response) = try await URLSession.shared.data(from: url)
        guard let httpResponse = response as? HTTPURLResponse,
              httpResponse.statusCode == 200 else {
            throw DownloadError.httpError
        }
        guard let image = UIImage(data: data) else {
            throw DownloadError.invalidData
        }
        return image
    }
}

// For streaming delegates, use AsyncStream:
class ProgressDownloader {
    func download(url: URL) -> AsyncThrowingStream<DownloadProgress, Error> {
        AsyncThrowingStream { continuation in
            let task = URLSession.shared.downloadTask(with: url)
            let observer = task.progress.observe(\.fractionCompleted) { progress, _ in
                continuation.yield(.progress(progress.fractionCompleted))
            }

            task.completionHandler = { localURL, response, error in
                observer.invalidate()
                if let error = error {
                    continuation.finish(throwing: error)
                } else if let localURL = localURL {
                    continuation.yield(.completed(localURL))
                    continuation.finish()
                }
            }

            continuation.onTermination = { _ in
                task.cancel()
            }

            task.resume()
        }
    }
}
```

---

### Phase 2: Actor Introduction

#### 2.1 Converting Shared Mutable State

```swift
// BEFORE: GCD-protected shared state
class ImageCache {
    static let shared = ImageCache()
    private var cache: [URL: UIImage] = [:]
    private let queue = DispatchQueue(label: "com.app.imageCache", attributes: .concurrent)

    func image(for url: URL) -> UIImage? {
        queue.sync { cache[url] }
    }

    func store(_ image: UIImage, for url: URL) {
        queue.async(flags: .barrier) { [weak self] in
            self?.cache[url] = image
        }
    }
}

// AFTER: Actor
actor ImageCache {
    static let shared = ImageCache()
    private var cache: [URL: UIImage] = [:]

    func image(for url: URL) -> UIImage? {
        cache[url]
    }

    func store(_ image: UIImage, for url: URL) {
        cache[url] = image
    }

    // Bulk operations are naturally atomic
    func clearExpired(olderThan date: Date, metadata: [URL: Date]) {
        for (url, cachedDate) in metadata where cachedDate < date {
            cache.removeValue(forKey: url)
        }
    }
}

// Usage changes:
// Before: let image = ImageCache.shared.image(for: url)
// After:  let image = await ImageCache.shared.image(for: url)
```

#### 2.2 Global Actor Isolation

```swift
// BEFORE: Manual main thread dispatch everywhere
class ProfileViewModel: ObservableObject {
    @Published var name: String = ""

    func load() {
        repository.fetchProfile { [weak self] profile in
            DispatchQueue.main.async {
                self?.name = profile.name
            }
        }
    }
}

// AFTER: MainActor isolation
@MainActor
class ProfileViewModel: ObservableObject {
    @Published var name: String = ""

    func load() async {
        let profile = try? await repository.fetchProfile()
        name = profile?.name ?? "" // Safe: already on MainActor
    }
}

// For methods that should NOT run on MainActor:
@MainActor
class DataProcessor: ObservableObject {
    @Published var results: [ProcessedItem] = []

    func processData(_ raw: [RawItem]) async {
        // Heavy work off the main actor
        let processed = await Task.detached {
            raw.map { ProcessedItem(from: $0) } // Runs on cooperative pool
        }.value

        results = processed // Back on MainActor (automatic)
    }
}
```

---

### Phase 3: Sendable Conformance

#### 3.1 Value Types

```swift
// Value types are implicitly Sendable if all stored properties are Sendable
struct UserDTO: Sendable {
    let id: String
    let name: String
    let email: String
    // All properties are String (Sendable) - this conformance is correct
}

// Enums with Sendable associated values
enum AppState: Sendable {
    case idle
    case loading
    case loaded(UserDTO)  // UserDTO is Sendable
    case error(String)    // String is Sendable
}
```

#### 3.2 Reference Types

```swift
// Classes need explicit Sendable conformance
// Option 1: Immutable class (all let properties)
final class Configuration: Sendable {
    let apiBaseURL: URL
    let apiKey: String
    let timeout: TimeInterval

    init(apiBaseURL: URL, apiKey: String, timeout: TimeInterval) {
        self.apiBaseURL = apiBaseURL
        self.apiKey = apiKey
        self.timeout = timeout
    }
}

// Option 2: @unchecked Sendable (when you manage synchronization)
final class ThreadSafeCounter: @unchecked Sendable {
    private var _count = 0
    private let lock = NSLock()

    var count: Int {
        lock.withLock { _count }
    }

    func increment() {
        lock.withLock { _count += 1 }
    }
}

// Option 3: Convert to actor (preferred)
actor Counter {
    private var count = 0

    func increment() -> Int {
        count += 1
        return count
    }
}
```

#### 3.3 Sendable Closures

```swift
// BEFORE: Non-sendable closure crossing isolation boundary
func processInBackground(items: [Item], completion: @escaping ([Result]) -> Void) {
    DispatchQueue.global().async {
        let results = items.map { process($0) }
        DispatchQueue.main.async {
            completion(results)
        }
    }
}

// AFTER: @Sendable closure
func processInBackground(items: [Item]) async -> [Result] {
    await withTaskGroup(of: Result.self) { group in
        for item in items {
            group.addTask { // Closure is implicitly @Sendable
                process(item)
            }
        }
        return await group.reduce(into: []) { $0.append($1) }
    }
}
```

---

### Phase 4: Resolving Data Race Warnings

#### 4.1 Common Warning Patterns

```swift
// WARNING: "Capture of 'self' with non-sendable type 'ViewController' in a `@Sendable` closure"
class ViewController: UIViewController {
    var data: [String] = []

    func load() {
        Task {
            let items = await fetchItems()
            self.data = items // Warning: ViewController is not Sendable
        }
    }
}

// FIX: Add @MainActor to the class
@MainActor
class ViewController: UIViewController {
    var data: [String] = []

    func load() {
        Task {
            let items = await fetchItems()
            self.data = items // Safe: MainActor isolated
        }
    }
}

// WARNING: "Passing argument of non-sendable type 'MyModel' outside of main actor-isolated context"
// FIX: Make MyModel Sendable or use actor isolation
struct MyModel: Sendable {
    let id: String
    let value: Int
}
```

#### 4.2 Enabling Strict Concurrency Incrementally

```swift
// In build settings or Package.swift:
// Start with "targeted" then move to "complete"

// Package.swift:
.target(
    name: "MyModule",
    swiftSettings: [
        // Step 1: Targeted (warnings for new concurrency features)
        .enableUpcomingFeature("StrictConcurrency"),
        // Step 2: After fixing all warnings, enable Swift 6 mode
        // .swiftLanguageMode(.v6)
    ]
)

// Or in Xcode build settings:
// SWIFT_STRICT_CONCURRENCY = complete
```

---

## Expected Output

1. **Concurrency Audit** - Current patterns and data race risks
2. **Conversion Plan** - Functions to convert, prioritized by risk and impact
3. **Actor Design** - Shared state to convert to actors
4. **Sendable Audit** - Types needing Sendable conformance
5. **Warning Resolution** - All strict concurrency warnings addressed

---

## Example Interaction

**User provides a networking layer with callbacks and GCD:**

```swift
// BEFORE: NetworkService.swift
class NetworkService {
    static let shared = NetworkService()
    private let session = URLSession.shared
    private var activeRequests: [UUID: URLSessionTask] = [:]
    private let queue = DispatchQueue(label: "network", attributes: .concurrent)

    func fetch<T: Decodable>(_ endpoint: String,
                              completion: @escaping (Result<T, Error>) -> Void) {
        let id = UUID()
        guard let url = URL(string: baseURL + endpoint) else {
            completion(.failure(NetworkError.invalidURL))
            return
        }

        let task = session.dataTask(with: url) { [weak self] data, response, error in
            self?.queue.async(flags: .barrier) {
                self?.activeRequests.removeValue(forKey: id)
            }

            if let error = error {
                DispatchQueue.main.async { completion(.failure(error)) }
                return
            }
            guard let data = data else {
                DispatchQueue.main.async { completion(.failure(NetworkError.noData)) }
                return
            }
            do {
                let result = try JSONDecoder().decode(T.self, from: data)
                DispatchQueue.main.async { completion(.success(result)) }
            } catch {
                DispatchQueue.main.async { completion(.failure(error)) }
            }
        }

        queue.async(flags: .barrier) { [weak self] in
            self?.activeRequests[id] = task
        }
        task.resume()
    }

    func cancelAll() {
        queue.async(flags: .barrier) { [weak self] in
            self?.activeRequests.values.forEach { $0.cancel() }
            self?.activeRequests.removeAll()
        }
    }
}
```

**Agent produces:**

```swift
// AFTER: NetworkService.swift
actor NetworkService {
    static let shared = NetworkService()
    private let session = URLSession.shared
    private var activeRequests: [UUID: URLSessionTask] = [:]

    func fetch<T: Decodable>(_ endpoint: String) async throws -> T {
        guard let url = URL(string: baseURL + endpoint) else {
            throw NetworkError.invalidURL
        }

        let id = UUID()
        let (data, response) = try await withTaskCancellationHandler {
            try await session.data(from: url)
        } onCancel: {
            Task { await self.cancelRequest(id: id) }
        }

        activeRequests.removeValue(forKey: id)

        guard let httpResponse = response as? HTTPURLResponse,
              (200...299).contains(httpResponse.statusCode) else {
            throw NetworkError.httpError(response)
        }

        return try JSONDecoder().decode(T.self, from: data)
    }

    func cancelAll() {
        activeRequests.values.forEach { $0.cancel() }
        activeRequests.removeAll()
    }

    private func cancelRequest(id: UUID) {
        activeRequests[id]?.cancel()
        activeRequests.removeValue(forKey: id)
    }
}

// Usage:
// Before:
// NetworkService.shared.fetch("/users") { (result: Result<[User], Error>) in ... }
// After:
// let users: [User] = try await NetworkService.shared.fetch("/users")
```

**Changes:**
- Class converted to actor (thread-safe without GCD)
- Completion handler replaced with async throws
- Manual DispatchQueue synchronization eliminated
- Task cancellation handled via withTaskCancellationHandler
- Result type eliminated (async throws is the equivalent)

---

## Techniques Used

- **ST-01** (Clear Objective): Focused concurrency adoption
- **ST-02** (Sequential Instructions): Phased callback-to-async migration
- **RT-02** (Multi-Format Output): Code examples with migration patterns
- **RT-04** (Best Practice Review): Swift concurrency best practices
- **AG-02** (Iterative Refinement): Incremental strict concurrency enablement

---

## Related Prompts

- [ios_code_modernization.md](ios_code_modernization.md) - Broader modernization including concurrency
- [ios_memory_leak_detection.md](ios_memory_leak_detection.md) - Structured concurrency reduces retain cycles
- [ios_error_handling_improvement.md](ios_error_handling_improvement.md) - Typed throws with async

---

## Customization Guide

### For Combine-Heavy Codebases

Migration strategy:
- Keep Combine for reactive streams (publishers that emit multiple values)
- Convert one-shot Combine chains to async/await
- Use `.values` to bridge Publisher to AsyncSequence
- Keep `@Published` properties (work with both paradigms)

### For GCD-Heavy Codebases

Conversion priorities:
- Serial dispatch queues become actors
- Concurrent queues with barriers become actors
- DispatchGroup becomes TaskGroup
- DispatchWorkItem becomes Task with cancellation
- DispatchSemaphore: avoid in async context (deadlock risk)

### For Server-Side Swift

Additional considerations:
- Avoid `@MainActor` (no main actor in server context)
- Use custom global actors for isolation domains
- Leverage TaskGroup for request parallelism
- Consider Sendable for request/response types
