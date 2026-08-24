---
title: "iOS Integration Testing"
category: mobile-development
description: "Build integration tests for iOS apps using Core Data in-memory stores, URLProtocol-based network mocking, and repository integration patterns with proper setup and teardown"
techniques:
  - ST-01
  - RT-02
  - DS-02
difficulty: advanced
tags:
  - ios
  - swift
  - testing
  - integration-testing
  - core-data
  - networking
  - urlprotocol
updated: "2026-03-19"
---

# iOS Integration Testing

**Objective:** Build integration tests that verify how multiple components work together in an iOS app. Covers Core Data persistence with in-memory stores, network layer testing with URLProtocol mocking, repository integration verifying data flow from API to cache to UI, and setup/teardown patterns that ensure test isolation without sacrificing realism.

**When to Use:** Use this prompt when unit tests pass individually but the assembled components fail together, when persistence logic needs testing with a real Core Data stack, when network response handling needs end-to-end verification, or when data synchronization between local and remote sources must be validated.

**Prompt Type:** Modular (200-240 lines)

---

## Context Gathering

1. **Integration Boundaries:**
   - "Which components need to be tested together (API + Cache, Repository + Core Data, Service + Keychain)?"
   - "What persistence technology is used (Core Data, SwiftData, SQLite, Realm, UserDefaults)?"

2. **Network Layer:**
   - "How are network calls made (URLSession, Alamofire, custom client)?"
   - "Are there interceptors, retry logic, or auth token injection?"

3. **Data Flow:**
   - "Describe the data flow: API response -> parsing -> caching -> ViewModel."
   - "Is there offline support or sync conflict resolution?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before generating ANY integration test, you MUST:**

1. **Identify the integration boundary** - Be explicit about which components are real and which are mocked. An integration test that mocks everything is just a unit test in disguise.
2. **Verify state cleanup** - Each test must start with a clean database and no cached network responses. Leaking state between tests is the primary source of intermittent failures.
3. **Test realistic scenarios** - Use realistic data shapes and sizes. A test with a single-item array won't catch pagination bugs.
4. **Account for async operations** - Core Data contexts, network completions, and Combine publishers all run asynchronously. Use proper awaiting mechanisms.
5. **Validate the full round-trip** - Don't just test writes; verify that written data can be read back correctly with the right types and relationships.

**Integration tests are slower than unit tests by design.** If a test can be written as a unit test, it should be. Reserve integration tests for verifying component interactions.

### False-Positive Prevention

- ❌ Do NOT use the production persistent store in tests (data will leak between runs)
- ❌ Do NOT mock the component under integration (defeats the purpose)
- ❌ Do NOT assume Core Data operations are synchronous
- ❌ Do NOT skip testing error paths (network failures, corrupt data, migration issues)
- ❌ Do NOT ignore threading - use the correct managed object context
- ✅ DO use in-memory Core Data stores for fast, isolated tests
- ✅ DO use URLProtocol subclasses for deterministic network responses
- ✅ DO test the full save -> fetch -> display pipeline
- ✅ DO verify Core Data relationships and cascade deletes
- ✅ DO test concurrent access patterns if the app uses background contexts

---

### Module 1: Core Data In-Memory Store

```swift
import CoreData
@testable import MyApp

// MARK: - In-Memory Core Data Stack for Testing

final class TestCoreDataStack {

    let container: NSPersistentContainer

    init(modelName: String = "MyApp") {
        // Load the model from the app bundle
        guard let modelURL = Bundle(for: type(of: self)).url(
            forResource: modelName, withExtension: "momd"
        ),
        let model = NSManagedObjectModel(contentsOf: modelURL) else {
            fatalError("Failed to load Core Data model: \(modelName)")
        }

        container = NSPersistentContainer(name: modelName, managedObjectModel: model)

        // Use in-memory store for test isolation
        let description = NSPersistentStoreDescription()
        description.type = NSInMemoryStoreType
        description.shouldAddStoreAsynchronously = false
        container.persistentStoreDescriptions = [description]

        container.loadPersistentStores { _, error in
            if let error = error {
                fatalError("Failed to load in-memory store: \(error)")
            }
        }

        // Merge policy for concurrent access tests
        container.viewContext.mergePolicy = NSMergeByPropertyObjectTrumpMergePolicy
        container.viewContext.automaticallyMergesChangesFromParent = true
    }

    var viewContext: NSManagedObjectContext {
        container.viewContext
    }

    func newBackgroundContext() -> NSManagedObjectContext {
        container.newBackgroundContext()
    }

    /// Reset all data between tests
    func reset() throws {
        let entities = container.managedObjectModel.entities
        for entity in entities {
            guard let name = entity.name else { continue }
            let fetchRequest = NSFetchRequest<NSFetchRequestResult>(entityName: name)
            let deleteRequest = NSBatchDeleteRequest(fetchRequest: fetchRequest)
            try container.viewContext.execute(deleteRequest)
        }
        container.viewContext.reset()
    }
}
```

### Module 2: Core Data Repository Integration Tests

```swift
import XCTest
import CoreData
@testable import MyApp

final class UserRepositoryIntegrationTests: XCTestCase {

    private var stack: TestCoreDataStack!
    private var sut: CoreDataUserRepository!

    override func setUp() {
        super.setUp()
        stack = TestCoreDataStack()
        sut = CoreDataUserRepository(context: stack.viewContext)
    }

    override func tearDown() {
        try? stack.reset()
        stack = nil
        sut = nil
        super.tearDown()
    }

    // MARK: - CRUD Operations

    func test_save_andFetchById_roundTrips() async throws {
        // Given
        let user = User(id: "u1", name: "Alice", email: "alice@test.com")

        // When
        try await sut.save(user)
        let fetched = try await sut.fetchUser(id: "u1")

        // Then
        XCTAssertEqual(fetched.id, "u1")
        XCTAssertEqual(fetched.name, "Alice")
        XCTAssertEqual(fetched.email, "alice@test.com")
    }

    func test_save_duplicate_updatesExistingRecord() async throws {
        // Given
        let original = User(id: "u1", name: "Alice", email: "alice@test.com")
        try await sut.save(original)

        // When
        let updated = User(id: "u1", name: "Alice Updated", email: "alice2@test.com")
        try await sut.save(updated)

        // Then
        let all = try await sut.fetchAllUsers()
        XCTAssertEqual(all.count, 1, "Should update, not duplicate")
        XCTAssertEqual(all.first?.name, "Alice Updated")
    }

    func test_delete_removesFromStore() async throws {
        // Given
        try await sut.save(User(id: "u1", name: "Alice", email: "a@test.com"))

        // When
        try await sut.deleteUser(id: "u1")

        // Then
        let all = try await sut.fetchAllUsers()
        XCTAssertTrue(all.isEmpty)
    }

    func test_fetchAll_returnsSortedByName() async throws {
        // Given
        try await sut.save(User(id: "u3", name: "Charlie", email: "c@test.com"))
        try await sut.save(User(id: "u1", name: "Alice", email: "a@test.com"))
        try await sut.save(User(id: "u2", name: "Bob", email: "b@test.com"))

        // When
        let all = try await sut.fetchAllUsers()

        // Then
        XCTAssertEqual(all.map(\.name), ["Alice", "Bob", "Charlie"])
    }

    // MARK: - Relationships

    func test_saveUserWithPosts_cascadesFetch() async throws {
        // Given
        var user = User(id: "u1", name: "Alice", email: "a@test.com")
        user.posts = [
            Post(id: "p1", title: "First Post", body: "Hello"),
            Post(id: "p2", title: "Second Post", body: "World"),
        ]

        // When
        try await sut.save(user)
        let fetched = try await sut.fetchUser(id: "u1")

        // Then
        XCTAssertEqual(fetched.posts?.count, 2)
    }

    func test_deleteUser_cascadesDeletePosts() async throws {
        // Given
        var user = User(id: "u1", name: "Alice", email: "a@test.com")
        user.posts = [Post(id: "p1", title: "Post", body: "Body")]
        try await sut.save(user)

        // When
        try await sut.deleteUser(id: "u1")

        // Then
        let postCount = try stack.viewContext.count(
            for: NSFetchRequest<NSFetchRequestResult>(entityName: "PostEntity")
        )
        XCTAssertEqual(postCount, 0, "Posts should be cascade-deleted with user")
    }

    // MARK: - Concurrent Access

    func test_concurrentWrites_doNotCorruptData() async throws {
        let iterations = 50

        try await withThrowingTaskGroup(of: Void.self) { group in
            for i in 0..<iterations {
                group.addTask {
                    let bgContext = self.stack.newBackgroundContext()
                    let repo = CoreDataUserRepository(context: bgContext)
                    let user = User(id: "u\(i)", name: "User \(i)", email: "u\(i)@test.com")
                    try await repo.save(user)
                }
            }
            try await group.waitForAll()
        }

        let all = try await sut.fetchAllUsers()
        XCTAssertEqual(all.count, iterations)
    }
}
```

### Module 3: URLProtocol Network Mocking

```swift
// MARK: - URLProtocol Mock for Deterministic Network Tests

final class MockURLProtocol: URLProtocol {

    /// Map of URL path -> (response data, status code, headers)
    static var stubbedResponses: [String: (Data, Int, [String: String])] = [:]

    /// Track requests for verification
    static var capturedRequests: [URLRequest] = []

    /// Simulated network delay
    static var responseDelay: TimeInterval = 0

    /// Error to return instead of a response
    static var stubbedError: Error?

    static func reset() {
        stubbedResponses = [:]
        capturedRequests = []
        responseDelay = 0
        stubbedError = nil
    }

    override class func canInit(with request: URLRequest) -> Bool {
        true
    }

    override class func canonicalRequest(for request: URLRequest) -> URLRequest {
        request
    }

    override func startLoading() {
        MockURLProtocol.capturedRequests.append(request)

        if let error = MockURLProtocol.stubbedError {
            client?.urlProtocol(self, didFailWithError: error)
            return
        }

        guard let path = request.url?.path,
              let (data, statusCode, headers) = MockURLProtocol.stubbedResponses[path] else {
            client?.urlProtocol(self, didFailWithError: URLError(.resourceUnavailable))
            return
        }

        let response = HTTPURLResponse(
            url: request.url!,
            statusCode: statusCode,
            httpVersion: "HTTP/2",
            headerFields: headers
        )!

        if MockURLProtocol.responseDelay > 0 {
            Thread.sleep(forTimeInterval: MockURLProtocol.responseDelay)
        }

        client?.urlProtocol(self, didReceive: response, cacheStoragePolicy: .notAllowed)
        client?.urlProtocol(self, didLoad: data)
        client?.urlProtocolDidFinishLoading(self)
    }

    override func stopLoading() {}
}

// MARK: - Test URLSession Factory

extension URLSession {
    static var mocked: URLSession {
        let config = URLSessionConfiguration.ephemeral
        config.protocolClasses = [MockURLProtocol.self]
        return URLSession(configuration: config)
    }
}
```

### Module 4: Network Integration Tests

```swift
final class UserAPIIntegrationTests: XCTestCase {

    private var sut: UserAPIClient!

    override func setUp() {
        super.setUp()
        MockURLProtocol.reset()
        sut = UserAPIClient(session: .mocked, baseURL: URL(string: "https://api.test.com")!)
    }

    override func tearDown() {
        MockURLProtocol.reset()
        sut = nil
        super.tearDown()
    }

    // MARK: - Successful Responses

    func test_fetchUser_parsesJSONCorrectly() async throws {
        // Given
        let json = """
        {"id": "u1", "name": "Alice", "email": "alice@test.com", "created_at": "2025-01-15T10:30:00Z"}
        """.data(using: .utf8)!

        MockURLProtocol.stubbedResponses["/users/u1"] = (json, 200, ["Content-Type": "application/json"])

        // When
        let user = try await sut.fetchUser(id: "u1")

        // Then
        XCTAssertEqual(user.id, "u1")
        XCTAssertEqual(user.name, "Alice")
        XCTAssertEqual(user.email, "alice@test.com")
        XCTAssertNotNil(user.createdAt)
    }

    func test_fetchUsers_parsesArrayResponse() async throws {
        // Given
        let json = """
        [
            {"id": "u1", "name": "Alice", "email": "a@test.com"},
            {"id": "u2", "name": "Bob", "email": "b@test.com"}
        ]
        """.data(using: .utf8)!

        MockURLProtocol.stubbedResponses["/users"] = (json, 200, ["Content-Type": "application/json"])

        // When
        let users = try await sut.fetchAllUsers()

        // Then
        XCTAssertEqual(users.count, 2)
    }

    // MARK: - Error Handling

    func test_fetchUser_with404_throwsNotFound() async {
        // Given
        MockURLProtocol.stubbedResponses["/users/missing"] = (Data(), 404, [:])

        // When/Then
        do {
            _ = try await sut.fetchUser(id: "missing")
            XCTFail("Expected notFound error")
        } catch {
            XCTAssertEqual(error as? APIError, .notFound)
        }
    }

    func test_fetchUser_withNetworkFailure_throwsConnectionError() async {
        // Given
        MockURLProtocol.stubbedError = URLError(.notConnectedToInternet)

        // When/Then
        do {
            _ = try await sut.fetchUser(id: "u1")
            XCTFail("Expected connection error")
        } catch {
            XCTAssertTrue(error is URLError)
        }
    }

    func test_fetchUser_withMalformedJSON_throwsDecodingError() async {
        // Given
        let badJSON = "not valid json".data(using: .utf8)!
        MockURLProtocol.stubbedResponses["/users/u1"] = (badJSON, 200, ["Content-Type": "application/json"])

        // When/Then
        do {
            _ = try await sut.fetchUser(id: "u1")
            XCTFail("Expected decoding error")
        } catch {
            XCTAssertTrue(error is DecodingError)
        }
    }

    // MARK: - Request Verification

    func test_fetchUser_sendsCorrectHeaders() async throws {
        // Given
        let json = """
        {"id": "u1", "name": "Alice", "email": "a@test.com"}
        """.data(using: .utf8)!
        MockURLProtocol.stubbedResponses["/users/u1"] = (json, 200, [:])

        // When
        _ = try await sut.fetchUser(id: "u1")

        // Then
        let request = MockURLProtocol.capturedRequests.first
        XCTAssertEqual(request?.httpMethod, "GET")
        XCTAssertEqual(request?.value(forHTTPHeaderField: "Accept"), "application/json")
    }

    func test_createUser_sendsPostWithBody() async throws {
        // Given
        let responseJSON = """
        {"id": "u1", "name": "Alice", "email": "a@test.com"}
        """.data(using: .utf8)!
        MockURLProtocol.stubbedResponses["/users"] = (responseJSON, 201, [:])

        let newUser = CreateUserRequest(name: "Alice", email: "a@test.com")

        // When
        _ = try await sut.createUser(newUser)

        // Then
        let request = MockURLProtocol.capturedRequests.first
        XCTAssertEqual(request?.httpMethod, "POST")

        let body = try XCTUnwrap(request?.httpBody)
        let decoded = try JSONDecoder().decode(CreateUserRequest.self, from: body)
        XCTAssertEqual(decoded.name, "Alice")
    }
}
```

### Module 5: Repository Integration (API + Cache)

```swift
final class UserRepositoryIntegrationTests: XCTestCase {

    private var sut: UserRepository!
    private var stack: TestCoreDataStack!

    override func setUp() {
        super.setUp()
        MockURLProtocol.reset()
        stack = TestCoreDataStack()

        let apiClient = UserAPIClient(session: .mocked, baseURL: URL(string: "https://api.test.com")!)
        let cache = CoreDataUserRepository(context: stack.viewContext)
        sut = UserRepositoryImpl(api: apiClient, cache: cache)
    }

    override func tearDown() {
        MockURLProtocol.reset()
        try? stack.reset()
        stack = nil
        sut = nil
        super.tearDown()
    }

    func test_fetchUser_cachesAPIResponse() async throws {
        // Given - API returns user
        let json = """
        {"id": "u1", "name": "Alice", "email": "alice@test.com"}
        """.data(using: .utf8)!
        MockURLProtocol.stubbedResponses["/users/u1"] = (json, 200, [:])

        // When - First fetch (from API)
        let user = try await sut.fetchUser(id: "u1")
        XCTAssertEqual(user.name, "Alice")

        // Then - Second fetch should use cache (even with API unavailable)
        MockURLProtocol.stubbedError = URLError(.notConnectedToInternet)
        let cached = try await sut.fetchUser(id: "u1")
        XCTAssertEqual(cached.name, "Alice")
    }

    func test_fetchUser_whenOffline_returnsCachedData() async throws {
        // Given - Pre-populate cache
        let cache = CoreDataUserRepository(context: stack.viewContext)
        try await cache.save(User(id: "u1", name: "Cached Alice", email: "a@test.com"))

        // And - Network is unavailable
        MockURLProtocol.stubbedError = URLError(.notConnectedToInternet)

        // When
        let user = try await sut.fetchUser(id: "u1")

        // Then
        XCTAssertEqual(user.name, "Cached Alice")
    }

    func test_fetchUser_apiResponseOverwritesStaleCache() async throws {
        // Given - Stale cache
        let cache = CoreDataUserRepository(context: stack.viewContext)
        try await cache.save(User(id: "u1", name: "Old Name", email: "old@test.com"))

        // And - API returns updated data
        let json = """
        {"id": "u1", "name": "New Name", "email": "new@test.com"}
        """.data(using: .utf8)!
        MockURLProtocol.stubbedResponses["/users/u1"] = (json, 200, [:])

        // When
        let user = try await sut.fetchUser(id: "u1")

        // Then
        XCTAssertEqual(user.name, "New Name")
        XCTAssertEqual(user.email, "new@test.com")
    }
}
```

---

## Expected Output

1. **In-Memory Core Data Stack** - Reusable test stack with reset capability
2. **Persistence Tests** - CRUD, relationships, cascade deletes, concurrency
3. **URLProtocol Mock** - Deterministic network response stubbing with request capture
4. **Network Tests** - Response parsing, error handling, request verification
5. **Repository Integration** - Full API-to-cache-to-ViewModel data flow verification

---

## Example Interaction

**User:** "We have a SwiftData-based app. How would the Core Data patterns differ?"

**Agent Response:**

```swift
import SwiftData
import XCTest
@testable import MyApp

final class SwiftDataUserRepositoryTests: XCTestCase {

    private var container: ModelContainer!
    private var context: ModelContext!
    private var sut: SwiftDataUserRepository!

    override func setUp() {
        super.setUp()
        // SwiftData in-memory configuration
        let config = ModelConfiguration(isStoredInMemoryOnly: true)
        container = try! ModelContainer(
            for: UserModel.self, PostModel.self,
            configurations: config
        )
        context = ModelContext(container)
        sut = SwiftDataUserRepository(context: context)
    }

    override func tearDown() {
        container = nil
        context = nil
        sut = nil
        super.tearDown()
    }

    func test_saveAndFetch_roundTrips() async throws {
        let user = UserModel(id: "u1", name: "Alice", email: "a@test.com")
        try await sut.save(user)

        let fetched = try await sut.fetch(id: "u1")

        XCTAssertEqual(fetched?.name, "Alice")
    }
}
```

---

## Techniques Used

- **ST-01** (Clear Objective): Focused on verifying component interactions at integration boundaries
- **RT-02** (Step-by-Step Reasoning): Modular progression from isolated components to full integration
- **DS-02** (Domain Expertise): Core Data in-memory stores, URLProtocol mocking, iOS data layer patterns

---

## Related Prompts

- [ios_unit_test_generation.md](ios_unit_test_generation.md) - Unit tests for individual components before integration
- [ios_test_strategy_design.md](ios_test_strategy_design.md) - Where integration tests fit in the overall strategy
- [ios_performance_testing.md](ios_performance_testing.md) - Performance testing for data layer operations

---

## Customization Guide

| Aspect | How to Customize |
|--------|-----------------|
| **Persistence** | Replace Core Data with SwiftData `ModelContainer(isStoredInMemoryOnly: true)` or Realm `inMemoryIdentifier` |
| **Networking** | Replace URLProtocol with a local mock server (Swifter) for WebSocket or streaming tests |
| **Auth Integration** | Add token injection via `MockURLProtocol` headers to test authenticated endpoints |
| **Migration Testing** | Use versioned Core Data models with `NSMappingModel` to test schema migrations |
| **Sync Conflicts** | Add tests for last-write-wins, merge, or manual conflict resolution strategies |
