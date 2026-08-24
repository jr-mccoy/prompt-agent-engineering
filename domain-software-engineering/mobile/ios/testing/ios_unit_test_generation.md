---
title: "iOS Unit Test Generation"
category: mobile-development
description: "Generate comprehensive unit tests for iOS ViewModels, services, and repositories using XCTest with async/await patterns, protocol-based mocks, and consistent naming conventions"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-02
difficulty: intermediate
tags:
  - ios
  - swift
  - testing
  - xctest
  - unit-testing
  - mocking
updated: "2026-03-19"
---

# iOS Unit Test Generation

**Objective:** Generate thorough, maintainable unit tests for iOS Swift codebases using XCTest. Covers ViewModel testing, service layer testing, repository testing, model validation, and utility functions with proper async/await patterns, protocol-based mocking/stubbing, and naming conventions that clearly communicate intent.

**When to Use:** Use this prompt when adding unit tests to an existing codebase, writing tests for new features, improving test coverage for business-critical logic, or establishing testing patterns for a team to follow. Best suited for testing pure logic, state transitions, data transformations, and service interactions.

**Prompt Type:** Comprehensive (220-260 lines)

---

## Context Gathering

1. **Code Under Test:**
   - "Paste the Swift file(s) you want to generate tests for."
   - "What architecture pattern is used (MVVM, TCA, VIPER, Clean)?"

2. **Dependency Injection:**
   - "Are dependencies injected via protocols, init parameters, or a DI framework (Swinject, Factory)?"
   - "Are there existing mock/stub implementations?"

3. **Async Patterns:**
   - "Does the code use async/await, Combine, or completion handlers?"

4. **Testing Goals:**
   - "What's the priority: happy paths, error handling, edge cases, or full coverage?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before generating ANY test, you MUST:**

1. **Read the actual source code** - Generate tests based on real behavior, not assumed behavior. Every assertion must trace to actual implementation logic.
2. **Identify all code paths** - Map happy paths, error paths, edge cases, and boundary conditions from the source.
3. **Verify dependency boundaries** - Only mock direct dependencies. Do not mock the system under test itself.
4. **Check for side effects** - Identify state mutations, notifications, analytics calls, and persistence operations that should be verified.
5. **Confirm testability** - If the code is not testable (tight coupling, static calls, singletons), flag the issue and suggest a minimal refactor.

**Generating tests that pass but don't actually verify behavior is worse than no tests.** Every assertion must validate a meaningful behavior.

### False-Positive Prevention

- ❌ Do NOT generate tests that only verify mock setup (testing the test, not the code)
- ❌ Do NOT assert on implementation details (private property values, internal method calls)
- ❌ Do NOT create tests that pass regardless of implementation correctness
- ❌ Do NOT mock value types or simple data models
- ❌ Do NOT generate redundant tests that verify the same behavior differently
- ✅ DO test observable behavior: return values, state changes, published properties
- ✅ DO verify error handling paths with specific error types
- ✅ DO test boundary conditions (empty arrays, nil optionals, max values)
- ✅ DO use protocol-based mocks for external dependencies only
- ✅ DO name tests to describe the scenario and expected outcome

---

### Step 1: Establish Mock Infrastructure

```swift
// MARK: - Protocol-Based Mock Pattern

// Source protocol (from production code):
protocol UserRepository {
    func fetchUser(id: String) async throws -> User
    func saveUser(_ user: User) async throws
    func deleteUser(id: String) async throws
}

// Mock implementation for tests:
final class MockUserRepository: UserRepository {

    // Track calls for verification
    var fetchUserCallCount = 0
    var fetchUserLastId: String?
    var saveUserCallCount = 0
    var saveUserLastUser: User?
    var deleteUserCallCount = 0

    // Stubbed responses
    var stubbedUser: User?
    var stubbedError: Error?

    func fetchUser(id: String) async throws -> User {
        fetchUserCallCount += 1
        fetchUserLastId = id
        if let error = stubbedError { throw error }
        guard let user = stubbedUser else {
            throw TestError.notStubbed
        }
        return user
    }

    func saveUser(_ user: User) async throws {
        saveUserCallCount += 1
        saveUserLastUser = user
        if let error = stubbedError { throw error }
    }

    func deleteUser(id: String) async throws {
        deleteUserCallCount += 1
        if let error = stubbedError { throw error }
    }
}

enum TestError: Error {
    case notStubbed
}
```

### Step 2: Generate ViewModel Tests

```swift
import XCTest
import Combine
@testable import MyApp

final class UserProfileViewModelTests: XCTestCase {

    private var sut: UserProfileViewModel!
    private var mockRepository: MockUserRepository!
    private var cancellables: Set<AnyCancellable>!

    // MARK: - Lifecycle

    override func setUp() {
        super.setUp()
        mockRepository = MockUserRepository()
        sut = UserProfileViewModel(repository: mockRepository)
        cancellables = []
    }

    override func tearDown() {
        sut = nil
        mockRepository = nil
        cancellables = nil
        super.tearDown()
    }

    // MARK: - Loading State

    func test_loadUser_setsLoadingState_beforeFetch() {
        // Given
        var states: [UserProfileViewModel.State] = []
        sut.$state
            .sink { states.append($0) }
            .store(in: &cancellables)

        // When
        Task { await sut.loadUser(id: "1") }

        // Then - initial state is idle
        XCTAssertEqual(states.first, .idle)
    }

    func test_loadUser_whenSuccess_updatesUserAndState() async {
        // Given
        let expectedUser = User(id: "1", name: "Alice", email: "alice@test.com")
        mockRepository.stubbedUser = expectedUser

        // When
        await sut.loadUser(id: "1")

        // Then
        XCTAssertEqual(sut.state, .loaded)
        XCTAssertEqual(sut.user, expectedUser)
        XCTAssertEqual(mockRepository.fetchUserCallCount, 1)
        XCTAssertEqual(mockRepository.fetchUserLastId, "1")
    }

    func test_loadUser_whenNotFound_setsErrorState() async {
        // Given
        mockRepository.stubbedError = APIError.notFound

        // When
        await sut.loadUser(id: "999")

        // Then
        XCTAssertEqual(sut.state, .error("User not found"))
        XCTAssertNil(sut.user)
    }

    func test_loadUser_whenNetworkError_setsRetryableError() async {
        // Given
        mockRepository.stubbedError = URLError(.notConnectedToInternet)

        // When
        await sut.loadUser(id: "1")

        // Then
        if case .error(let message) = sut.state {
            XCTAssertTrue(message.contains("network"), "Error should mention network issue")
        } else {
            XCTFail("Expected error state, got \(sut.state)")
        }
    }

    // MARK: - User Actions

    func test_updateName_validatesNonEmpty() async {
        // Given
        mockRepository.stubbedUser = User(id: "1", name: "Alice", email: "alice@test.com")
        await sut.loadUser(id: "1")

        // When
        let result = await sut.updateName("")

        // Then
        XCTAssertFalse(result.isSuccess)
        XCTAssertEqual(sut.validationError, "Name cannot be empty")
        XCTAssertEqual(mockRepository.saveUserCallCount, 0, "Should not save invalid data")
    }

    func test_updateName_whenValid_savesAndUpdatesLocal() async {
        // Given
        mockRepository.stubbedUser = User(id: "1", name: "Alice", email: "alice@test.com")
        await sut.loadUser(id: "1")

        // When
        let result = await sut.updateName("Bob")

        // Then
        XCTAssertTrue(result.isSuccess)
        XCTAssertEqual(sut.user?.name, "Bob")
        XCTAssertEqual(mockRepository.saveUserCallCount, 1)
        XCTAssertEqual(mockRepository.saveUserLastUser?.name, "Bob")
    }

    // MARK: - Formatting

    func test_displayName_formatsFullName() {
        // Given
        sut.user = User(id: "1", name: "alice jones", email: "a@test.com")

        // Then
        XCTAssertEqual(sut.displayName, "Alice Jones")
    }

    func test_memberSince_formatsDate() {
        // Given
        let date = Date(timeIntervalSince1970: 1672531200) // Jan 1, 2023
        sut.user = User(id: "1", name: "Alice", email: "a@test.com", joinDate: date)

        // Then
        XCTAssertEqual(sut.memberSince, "January 2023")
    }
}
```

### Step 3: Generate Service Layer Tests

```swift
final class AuthServiceTests: XCTestCase {

    private var sut: AuthService!
    private var mockKeychain: MockKeychainStorage!
    private var mockAPIClient: MockAPIClient!

    override func setUp() {
        super.setUp()
        mockKeychain = MockKeychainStorage()
        mockAPIClient = MockAPIClient()
        sut = AuthService(apiClient: mockAPIClient, keychain: mockKeychain)
    }

    override func tearDown() {
        sut = nil
        mockKeychain = nil
        mockAPIClient = nil
        super.tearDown()
    }

    func test_login_withValidCredentials_storesTokenInKeychain() async throws {
        // Given
        mockAPIClient.stubbedResponse = LoginResponse(
            token: "abc123",
            refreshToken: "refresh456",
            expiresIn: 3600
        )

        // When
        try await sut.login(email: "user@test.com", password: "pass123")

        // Then
        XCTAssertEqual(mockKeychain.storedValues["auth_token"], "abc123")
        XCTAssertEqual(mockKeychain.storedValues["refresh_token"], "refresh456")
        XCTAssertTrue(sut.isAuthenticated)
    }

    func test_login_withInvalidCredentials_throwsUnauthorized() async {
        // Given
        mockAPIClient.stubbedError = APIError.unauthorized

        // When/Then
        do {
            try await sut.login(email: "user@test.com", password: "wrong")
            XCTFail("Expected unauthorized error")
        } catch {
            XCTAssertEqual(error as? APIError, .unauthorized)
            XCTAssertFalse(sut.isAuthenticated)
            XCTAssertNil(mockKeychain.storedValues["auth_token"])
        }
    }

    func test_logout_clearsKeychainAndResets() async {
        // Given
        mockKeychain.storedValues["auth_token"] = "abc123"
        mockKeychain.storedValues["refresh_token"] = "refresh456"

        // When
        await sut.logout()

        // Then
        XCTAssertTrue(mockKeychain.storedValues.isEmpty)
        XCTAssertFalse(sut.isAuthenticated)
    }

    func test_refreshToken_whenExpired_refreshesAutomatically() async throws {
        // Given
        mockKeychain.storedValues["refresh_token"] = "refresh456"
        mockAPIClient.stubbedResponses = [
            APIError.tokenExpired,    // First call fails
            LoginResponse(token: "new_token", refreshToken: "new_refresh", expiresIn: 3600)
        ]

        // When
        try await sut.authenticatedRequest { /* some request */ }

        // Then
        XCTAssertEqual(mockKeychain.storedValues["auth_token"], "new_token")
    }
}
```

### Step 4: Generate Model Validation Tests

```swift
final class UserValidationTests: XCTestCase {

    // MARK: - Email Validation

    func test_isValidEmail_withStandardEmail_returnsTrue() {
        XCTAssertTrue(User.isValidEmail("user@example.com"))
    }

    func test_isValidEmail_withSubdomain_returnsTrue() {
        XCTAssertTrue(User.isValidEmail("user@mail.example.com"))
    }

    func test_isValidEmail_withoutAtSymbol_returnsFalse() {
        XCTAssertFalse(User.isValidEmail("userexample.com"))
    }

    func test_isValidEmail_withEmptyString_returnsFalse() {
        XCTAssertFalse(User.isValidEmail(""))
    }

    func test_isValidEmail_withSpaces_returnsFalse() {
        XCTAssertFalse(User.isValidEmail("user @example.com"))
    }

    // MARK: - Password Strength

    func test_passwordStrength_weak() {
        XCTAssertEqual(User.passwordStrength("abc"), .weak)
    }

    func test_passwordStrength_medium() {
        XCTAssertEqual(User.passwordStrength("abc12345"), .medium)
    }

    func test_passwordStrength_strong() {
        XCTAssertEqual(User.passwordStrength("Abc123!@#xyz"), .strong)
    }

    // MARK: - Equatable & Codable

    func test_user_codable_roundTrips() throws {
        let user = User(id: "1", name: "Alice", email: "alice@test.com")
        let data = try JSONEncoder().encode(user)
        let decoded = try JSONDecoder().decode(User.self, from: data)
        XCTAssertEqual(user, decoded)
    }
}
```

### Step 5: Test Naming Convention Reference

```
Pattern: test_[unitOfWork]_[scenario]_[expectedBehavior]

Examples:
  test_loadUser_whenSuccess_updatesState
  test_login_withInvalidCredentials_throwsUnauthorized
  test_formatPrice_withZeroCents_omitsDecimal
  test_validateEmail_withEmptyString_returnsFalse
  test_saveRecord_whenOffline_queuesForSync
```

---

## Expected Output

1. **Mock/Stub Implementations** - Protocol-based mocks for all dependencies
2. **ViewModel Tests** - State transitions, user actions, formatting, error handling
3. **Service Tests** - API interactions, token management, error propagation
4. **Model Tests** - Validation rules, encoding/decoding, computed properties
5. **Test Organization** - Files grouped by source file under test
6. **Naming Conventions** - Consistent, descriptive test names

---

## Example Interaction

**User:** "Generate unit tests for this ViewModel:"
```swift
@MainActor
class CartViewModel: ObservableObject {
    @Published private(set) var items: [CartItem] = []
    @Published private(set) var total: Decimal = 0

    private let cartService: CartServiceProtocol

    init(cartService: CartServiceProtocol) {
        self.cartService = cartService
    }

    func addItem(_ product: Product, quantity: Int) async {
        guard quantity > 0 else { return }
        let item = CartItem(product: product, quantity: quantity)
        items.append(item)
        recalculateTotal()
        try? await cartService.syncCart(items: items)
    }

    func removeItem(at index: Int) async {
        guard items.indices.contains(index) else { return }
        items.remove(at: index)
        recalculateTotal()
        try? await cartService.syncCart(items: items)
    }

    private func recalculateTotal() {
        total = items.reduce(Decimal.zero) { $0 + $1.subtotal }
    }
}
```

**Agent Response:**

```swift
import XCTest
@testable import MyApp

@MainActor
final class CartViewModelTests: XCTestCase {

    private var sut: CartViewModel!
    private var mockService: MockCartService!

    override func setUp() {
        super.setUp()
        mockService = MockCartService()
        sut = CartViewModel(cartService: mockService)
    }

    override func tearDown() {
        sut = nil
        mockService = nil
        super.tearDown()
    }

    // MARK: - Add Item

    func test_addItem_appendsToItems() async {
        let product = Product.stub(price: 9.99)

        await sut.addItem(product, quantity: 2)

        XCTAssertEqual(sut.items.count, 1)
        XCTAssertEqual(sut.items.first?.product, product)
        XCTAssertEqual(sut.items.first?.quantity, 2)
    }

    func test_addItem_updatesTotal() async {
        let product = Product.stub(price: 10.00)

        await sut.addItem(product, quantity: 3)

        XCTAssertEqual(sut.total, 30.00)
    }

    func test_addItem_syncsWithService() async {
        await sut.addItem(Product.stub(), quantity: 1)

        XCTAssertEqual(mockService.syncCartCallCount, 1)
    }

    func test_addItem_withZeroQuantity_doesNothing() async {
        await sut.addItem(Product.stub(), quantity: 0)

        XCTAssertTrue(sut.items.isEmpty)
        XCTAssertEqual(mockService.syncCartCallCount, 0)
    }

    func test_addItem_withNegativeQuantity_doesNothing() async {
        await sut.addItem(Product.stub(), quantity: -1)

        XCTAssertTrue(sut.items.isEmpty)
    }

    // MARK: - Remove Item

    func test_removeItem_removesAtIndex() async {
        await sut.addItem(Product.stub(name: "A"), quantity: 1)
        await sut.addItem(Product.stub(name: "B"), quantity: 1)

        await sut.removeItem(at: 0)

        XCTAssertEqual(sut.items.count, 1)
        XCTAssertEqual(sut.items.first?.product.name, "B")
    }

    func test_removeItem_recalculatesTotal() async {
        await sut.addItem(Product.stub(price: 10.00), quantity: 1)
        await sut.addItem(Product.stub(price: 20.00), quantity: 1)

        await sut.removeItem(at: 0)

        XCTAssertEqual(sut.total, 20.00)
    }

    func test_removeItem_withInvalidIndex_doesNothing() async {
        await sut.addItem(Product.stub(), quantity: 1)

        await sut.removeItem(at: 5)

        XCTAssertEqual(sut.items.count, 1)
    }

    func test_removeItem_fromEmptyCart_doesNothing() async {
        await sut.removeItem(at: 0)

        XCTAssertTrue(sut.items.isEmpty)
    }

    // MARK: - Total Calculation

    func test_total_withMultipleItems_sumsCorrectly() async {
        await sut.addItem(Product.stub(price: 5.50), quantity: 2)  // 11.00
        await sut.addItem(Product.stub(price: 3.25), quantity: 4)  // 13.00

        XCTAssertEqual(sut.total, 24.00)
    }

    func test_total_afterRemovingAllItems_isZero() async {
        await sut.addItem(Product.stub(price: 10.00), quantity: 1)
        await sut.removeItem(at: 0)

        XCTAssertEqual(sut.total, Decimal.zero)
    }
}

// MARK: - Test Helpers

extension Product {
    static func stub(
        name: String = "Test Product",
        price: Decimal = 9.99
    ) -> Product {
        Product(id: UUID().uuidString, name: name, price: price)
    }
}
```

---

## Techniques Used

- **ST-01** (Clear Objective): Focused goal of generating correct, meaningful unit tests
- **ST-02** (Structured Decomposition): Tests organized by layer (ViewModel, Service, Model)
- **RT-02** (Step-by-Step Reasoning): Sequential approach from mocks to test cases
- **DS-02** (Domain Expertise): XCTest framework patterns, async testing, Swift conventions

---

## Related Prompts

- [ios_test_strategy_design.md](ios_test_strategy_design.md) - Overall test strategy and pyramid design
- [ios_integration_testing.md](ios_integration_testing.md) - Integration tests for Core Data and networking
- [ios_ai_test_generation.md](ios_ai_test_generation.md) - AI-assisted test generation for coverage gaps
- [ios_ui_test_generation.md](ios_ui_test_generation.md) - XCUITest UI test generation

---

## Customization Guide

| Aspect | How to Customize |
|--------|-----------------|
| **Architecture** | For TCA, test reducers with `TestStore`; for VIPER, test interactors/presenters |
| **Async Pattern** | Replace `async/await` with Combine `XCTExpectation` or `sink`-based assertions |
| **Mocking Library** | Replace manual mocks with Mockolo, Sourcery-generated mocks, or swift-macro mocks |
| **Test Data** | Replace `.stub()` helpers with factory patterns or Faker-style generators |
| **Assertion Style** | Swap XCTAssert for Nimble matchers (`expect(x).to(equal(y))`) if preferred |
| **CI Integration** | Add `XCTSkipIf` for tests requiring specific OS versions or entitlements |
