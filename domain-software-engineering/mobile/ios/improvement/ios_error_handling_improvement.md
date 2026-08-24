---
title: "iOS Error Handling Improvement"
category: mobile-development
description: "Adopt typed throws (Swift 6), build domain-specific error types, implement user-facing error presentation, and integrate structured error reporting"
techniques:
  - ST-01
  - RT-02
  - RT-04
  - DS-02
difficulty: intermediate
tags:
  - ios
  - swift
  - error-handling
  - typed-throws
  - user-experience
updated: "2026-03-19"
---

# iOS Error Handling Improvement

**Objective:** Improve error handling throughout an iOS codebase by adopting Swift 6 typed throws, building domain-specific error hierarchies, implementing consistent user-facing error presentation, and integrating structured error reporting for diagnostics.

**When to Use:** Use this prompt when the codebase uses generic `Error` types without specificity, when error messages shown to users are unclear or developer-oriented, when debugging production errors is difficult due to insufficient error context, or when adopting Swift 6 typed throws.

**Prompt Type:** Modular (350-450 lines)

---

## Context Gathering

Before improving error handling, understand the current state:

1. **Current Patterns:**
   - "How are errors currently handled? (try/catch, Result, optional chaining, force unwrap)"
   - "Are there domain-specific error types or mostly generic Error?"
   - "How are errors presented to users?"

2. **Error Sources:**
   - "What are the main error sources? (network, persistence, validation, authentication)"
   - "Are there third-party SDKs with their own error types?"

3. **Goals:**
   - "Is the priority developer debugging, user experience, or both?"
   - "Is the project adopting Swift 6 typed throws?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Trace error propagation paths** - Understand how errors flow from source to user.
2. **Check existing error handling** - Some catch blocks may be intentionally broad for resilience.
3. **Verify user impact** - Not all internal errors need user-facing messages.
4. **Consider recovery options** - Error handling should enable recovery where possible.
5. **Provide specific file:line locations** - Every finding MUST include exact code locations.

**Finding ADEQUATE error handling is an acceptable outcome.** Not every codebase needs typed throws everywhere. Pragmatic error handling that serves users well is the goal.

### False-Positive Prevention

- ❌ Do NOT demand typed throws for every function (pragmatic use is fine)
- ❌ Do NOT flag `catch { }` blocks that intentionally swallow expected errors
- ❌ Do NOT require domain error types for simple utilities
- ❌ Do NOT expose technical details in user-facing error messages
- ✅ DO verify that critical error paths have adequate handling
- ✅ DO check that user-facing errors are actionable
- ✅ DO ensure errors carry enough context for debugging
- ✅ DO consider the error recovery story for each error type

---

### Module 1: Domain-Specific Error Types

#### 1.1 Error Type Hierarchy

```swift
// BEFORE: Generic error handling
func fetchUser() async throws -> User {
    let data = try await network.get("/user")
    let user = try JSONDecoder().decode(User.self, from: data)
    return user
}

// Caller has no idea what went wrong:
do {
    let user = try await fetchUser()
} catch {
    print("Something failed: \(error)") // Useless for recovery
}

// AFTER: Domain-specific error types
enum NetworkError: Error, LocalizedError {
    case noConnection
    case timeout(duration: TimeInterval)
    case serverError(statusCode: Int, message: String?)
    case unauthorized
    case rateLimited(retryAfter: TimeInterval)

    var errorDescription: String? {
        switch self {
        case .noConnection:
            return String(localized: "No internet connection. Check your network settings.")
        case .timeout(let duration):
            return String(localized: "Request timed out after \(Int(duration)) seconds.")
        case .serverError(let code, _):
            return String(localized: "Server error (\(code)). Please try again later.")
        case .unauthorized:
            return String(localized: "Your session has expired. Please sign in again.")
        case .rateLimited(let retryAfter):
            return String(localized: "Too many requests. Please wait \(Int(retryAfter)) seconds.")
        }
    }

    var recoverySuggestion: String? {
        switch self {
        case .noConnection: return String(localized: "Turn on Wi-Fi or cellular data.")
        case .unauthorized: return String(localized: "Tap Sign In to continue.")
        case .rateLimited: return String(localized: "The app will retry automatically.")
        default: return nil
        }
    }
}
```

#### 1.2 Layered Error Types

```swift
// Domain layer errors
enum UserError: Error {
    case notFound(id: String)
    case validationFailed(field: String, reason: String)
    case insufficientPermissions(required: Permission)
    case accountDeactivated

    // Wrap lower-level errors with context
    case networkFailure(NetworkError)
    case persistenceFailure(PersistenceError)
}

// Persistence layer errors
enum PersistenceError: Error {
    case saveFailed(entity: String, underlying: Error)
    case fetchFailed(entity: String, predicate: String?)
    case migrationFailed(from: Int, to: Int, reason: String)
    case corruptData(entity: String)
}
```

---

### Module 2: Swift 6 Typed Throws

#### 2.1 Basic Typed Throws Adoption

```swift
// BEFORE: Untyped throws - caller does not know what errors to expect
func loadProfile() async throws -> Profile {
    let data = try await networkService.fetch("/profile")
    return try JSONDecoder().decode(Profile.self, from: data)
}

// AFTER: Typed throws (Swift 6) - compiler-checked error handling
func loadProfile() async throws(ProfileError) -> Profile {
    let data: Data
    do {
        data = try await networkService.fetch("/profile")
    } catch let error as NetworkError {
        throw .networkFailure(error)
    } catch {
        throw .unexpected(error)
    }

    do {
        return try JSONDecoder().decode(Profile.self, from: data)
    } catch {
        throw .decodingFailed(error)
    }
}

enum ProfileError: Error {
    case networkFailure(NetworkError)
    case decodingFailed(Error)
    case notFound
    case unexpected(Error)
}

// Caller gets exhaustive switch:
do {
    let profile = try await loadProfile()
} catch {
    switch error {
    case .networkFailure(let networkError):
        handleNetworkError(networkError)
    case .decodingFailed:
        showCorruptDataAlert()
    case .notFound:
        showProfileNotFoundView()
    case .unexpected(let underlying):
        logUnexpectedError(underlying)
    }
}
```

#### 2.2 Typed Throws in Protocols

```swift
// Define protocol with typed throws
protocol UserRepository {
    func fetch(id: String) async throws(RepositoryError) -> User
    func save(_ user: User) async throws(RepositoryError)
    func delete(id: String) async throws(RepositoryError)
}

enum RepositoryError: Error {
    case notFound(entity: String, id: String)
    case conflict(entity: String, reason: String)
    case storageFull
    case accessDenied
}
```

---

### Module 3: User-Facing Error Presentation

#### 3.1 Error Presenter Pattern

```swift
// BEFORE: Ad-hoc alert creation scattered everywhere
func handleError(_ error: Error) {
    let alert = UIAlertController(
        title: "Error",
        message: error.localizedDescription, // Often technical gibberish
        preferredStyle: .alert
    )
    alert.addAction(UIAlertAction(title: "OK", style: .default))
    present(alert, animated: true)
}

// AFTER: Centralized error presentation with recovery actions
@MainActor
struct ErrorPresenter {
    static func present(
        _ error: Error,
        in context: UIViewController,
        retryAction: (() async -> Void)? = nil
    ) {
        let (title, message, actions) = classify(error, retryAction: retryAction)

        let alert = UIAlertController(title: title, message: message, preferredStyle: .alert)
        for action in actions {
            alert.addAction(action)
        }
        context.present(alert, animated: true)
    }

    private static func classify(
        _ error: Error,
        retryAction: (() async -> Void)?
    ) -> (String, String, [UIAlertAction]) {
        var actions: [UIAlertAction] = []

        switch error {
        case let networkError as NetworkError:
            if let retry = retryAction {
                actions.append(UIAlertAction(title: "Retry", style: .default) { _ in
                    Task { await retry() }
                })
            }
            actions.append(UIAlertAction(title: "OK", style: .cancel))
            return ("Connection Issue", networkError.localizedDescription, actions)

        case let userError as UserError where userError == .accountDeactivated:
            actions.append(UIAlertAction(title: "Contact Support", style: .default) { _ in
                // Open support
            })
            actions.append(UIAlertAction(title: "OK", style: .cancel))
            return ("Account Issue", "Your account has been deactivated.", actions)

        default:
            actions.append(UIAlertAction(title: "OK", style: .cancel))
            return ("Something Went Wrong",
                    "An unexpected error occurred. Please try again.",
                    actions)
        }
    }
}
```

#### 3.2 SwiftUI Error Handling

```swift
// BEFORE: No error presentation
struct ProfileView: View {
    @State private var profile: Profile?

    var body: some View {
        Text(profile?.name ?? "Loading...")
            .task {
                profile = try? await loadProfile() // Silently swallowed
            }
    }
}

// AFTER: Proper error state and presentation
struct ProfileView: View {
    @State private var profile: Profile?
    @State private var error: ProfileError?
    @State private var showError = false

    var body: some View {
        Group {
            if let profile {
                ProfileContent(profile: profile)
            } else {
                ProgressView()
            }
        }
        .task { await load() }
        .alert(
            "Unable to Load Profile",
            isPresented: $showError,
            presenting: error
        ) { error in
            if error.isRetryable {
                Button("Retry") { Task { await load() } }
            }
            Button("OK", role: .cancel) {}
        } message: { error in
            Text(error.userMessage)
        }
    }

    private func load() async {
        do {
            profile = try await loadProfile()
        } catch let profileError as ProfileError {
            error = profileError
            showError = true
        } catch {
            self.error = .unexpected(error)
            showError = true
        }
    }
}
```

---

### Module 4: Error Reporting and Diagnostics

#### 4.1 Structured Error Logging

```swift
// Error context for debugging
struct ErrorContext {
    let file: String
    let function: String
    let line: Int
    let timestamp: Date
    let additionalInfo: [String: String]

    init(
        file: String = #file,
        function: String = #function,
        line: Int = #line,
        additionalInfo: [String: String] = [:]
    ) {
        self.file = (file as NSString).lastPathComponent
        self.function = function
        self.line = line
        self.timestamp = Date()
        self.additionalInfo = additionalInfo
    }
}

// Logging service
actor ErrorReporter {
    static let shared = ErrorReporter()

    func report(_ error: Error, context: ErrorContext, severity: Severity = .error) {
        let entry = ErrorEntry(
            error: String(describing: error),
            domain: String(describing: type(of: error)),
            context: context,
            severity: severity
        )

        // Local log
        logger.log(level: severity.osLogType, "\(entry.formatted)")

        // Remote reporting (non-fatal)
        if severity >= .warning {
            CrashReporter.shared.recordNonFatal(entry)
        }
    }

    enum Severity: Int, Comparable {
        case debug, info, warning, error, critical

        static func < (lhs: Severity, rhs: Severity) -> Bool {
            lhs.rawValue < rhs.rawValue
        }

        var osLogType: OSLogType {
            switch self {
            case .debug: return .debug
            case .info: return .info
            case .warning, .error: return .error
            case .critical: return .fault
            }
        }
    }
}
```

---

## Expected Output

1. **Error Audit** - Current error handling patterns and gaps
2. **Error Type Hierarchy** - Domain-specific error types with user-facing messages
3. **Typed Throws Adoption Plan** - Functions to convert with priority order
4. **Presentation Layer** - Consistent error UI with recovery actions
5. **Reporting Integration** - Structured error logging for diagnostics

---

## Example Interaction

**User provides a networking layer with generic error handling:**

```swift
// BEFORE: APIClient.swift
class APIClient {
    func request<T: Decodable>(_ endpoint: String) async throws -> T {
        let url = URL(string: baseURL + endpoint)!
        let (data, response) = try await URLSession.shared.data(from: url)
        guard let http = response as? HTTPURLResponse,
              http.statusCode == 200 else {
            throw NSError(domain: "API", code: -1)
        }
        return try JSONDecoder().decode(T.self, from: data)
    }
}
```

**Agent produces:**

```swift
// AFTER: APIClient.swift
class APIClient {
    func request<T: Decodable>(_ endpoint: String) async throws(APIError) -> T {
        guard let url = URL(string: baseURL + endpoint) else {
            throw .invalidEndpoint(endpoint)
        }

        let data: Data
        let response: URLResponse
        do {
            (data, response) = try await URLSession.shared.data(from: url)
        } catch let urlError as URLError {
            throw urlError.toAPIError()
        } catch {
            throw .transportFailure(error)
        }

        guard let http = response as? HTTPURLResponse else {
            throw .invalidResponse
        }

        guard (200...299).contains(http.statusCode) else {
            throw .httpError(
                statusCode: http.statusCode,
                body: String(data: data, encoding: .utf8)
            )
        }

        do {
            return try JSONDecoder().decode(T.self, from: data)
        } catch {
            throw .decodingFailed(type: String(describing: T.self), error: error)
        }
    }
}

enum APIError: Error, LocalizedError {
    case invalidEndpoint(String)
    case noConnection
    case timeout
    case httpError(statusCode: Int, body: String?)
    case decodingFailed(type: String, error: Error)
    case transportFailure(Error)
    case invalidResponse

    var errorDescription: String? {
        switch self {
        case .noConnection:
            return String(localized: "No internet connection.")
        case .timeout:
            return String(localized: "The request timed out. Please try again.")
        case .httpError(let code, _) where code == 401:
            return String(localized: "Please sign in again.")
        case .httpError(let code, _) where (500...599).contains(code):
            return String(localized: "Server error. Please try again later.")
        case .decodingFailed:
            return String(localized: "Received unexpected data. Please update the app.")
        default:
            return String(localized: "Something went wrong. Please try again.")
        }
    }

    var isRetryable: Bool {
        switch self {
        case .noConnection, .timeout, .httpError(let code, _) where code >= 500:
            return true
        default:
            return false
        }
    }
}

extension URLError {
    func toAPIError() -> APIError {
        switch code {
        case .notConnectedToInternet, .networkConnectionLost:
            return .noConnection
        case .timedOut:
            return .timeout
        default:
            return .transportFailure(self)
        }
    }
}
```

---

## Techniques Used

- **ST-01** (Clear Objective): Focused error handling improvement
- **RT-02** (Multi-Format Output): Code examples with multiple patterns
- **RT-04** (Best Practice Review): Swift error handling best practices
- **DS-02** (Decision Support): When to use typed throws vs generic throws

---

## Related Prompts

- [ios_code_modernization.md](ios_code_modernization.md) - Modernize error patterns alongside other code
- [ios_swift_concurrency_adoption.md](ios_swift_concurrency_adoption.md) - Error handling in async contexts
- [ios_ui_polish_audit.md](ios_ui_polish_audit.md) - Error UI presentation polish

---

## Customization Guide

### For Network-Heavy Apps

Emphasize:
- HTTP status code mapping to domain errors
- Retry strategies per error type
- Offline error queuing and resolution
- Certificate pinning error handling

### For Data-Intensive Apps

Focus on:
- Persistence error hierarchies (Core Data, SwiftData, Realm)
- Migration failure recovery
- Data corruption detection and repair
- Sync conflict resolution errors

### For Swift 5 Compatibility

Skip typed throws and focus on:
- `Result` type adoption
- `LocalizedError` conformance
- Consistent error presentation
- Error logging infrastructure
