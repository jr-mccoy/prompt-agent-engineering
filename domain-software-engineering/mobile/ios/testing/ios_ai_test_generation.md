---
title: "iOS AI-Assisted Test Generation"
category: mobile-development
description: "Generate high-quality XCTest code using AI-assisted patterns including mock generation, test data factories, coverage gap filling, and test quality review for Swift/iOS projects."
techniques:
  - ST-01
  - ST-02
difficulty: intermediate
tags:
  - ios
  - swift
  - testing
  - ai-agent
  - xctest
  - mobile-development
updated: "2026-03-20"
---

# iOS AI-Assisted Test Generation

**Objective:** Use AI-assisted patterns to generate production-quality XCTest code for Swift/iOS projects, including protocol-based mock generation, type-safe test data factories, systematic coverage gap identification, and automated test quality review to ensure tests are meaningful rather than superficial.

**When to Use:** Use this prompt when generating unit tests for existing Swift code, bootstrapping test suites for untested modules, creating mocks for protocol-heavy architectures, or reviewing AI-generated tests for quality. Best used when the source code under test is stable and well-defined.

**Prompt Type:** Modular (150-400 lines)

---

## Context Gathering

Before generating tests, gather essential context:

1. **Code Under Test:**
   - "What module, class, or function needs tests?"
   - "Are there protocol abstractions for dependencies (enables mocking)?"
   - "What are the critical code paths and edge cases?"

2. **Testing Infrastructure:**
   - "Is there an existing test target with helpers, factories, or base classes?"
   - "Are there established mocking patterns (manual mocks, protocol witnesses)?"
   - "Is there a CI pipeline running tests automatically?"

3. **Coverage Goals:**
   - "What is the current code coverage percentage?"
   - "Are there specific modules or files with zero coverage?"
   - "What coverage target is required (e.g., 80% line coverage)?"

4. **Constraints:**
   - "Are async/await tests needed (requires XCTest async support)?"
   - "Are there Core Data, SwiftData, or Keychain dependencies to mock?"
   - "Do tests need to run in parallel or have ordering dependencies?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before generating ANY test code, you MUST:**

1. **Read the source code under test** - Understand the public API, dependencies, error paths, and state transitions before writing tests.
2. **Check for existing test patterns** - Search the test target for existing mocks, factories, base classes, and naming conventions.
3. **Identify all dependencies** - List every protocol/class the code under test depends on; each needs a mock or stub.
4. **Verify testability** - Confirm dependencies are injected (not hardcoded singletons) before generating tests.
5. **Generate tests that fail first** - Ensure tests actually exercise the code path they claim to test.

### False-Positive Prevention

- Do NOT generate tests that only verify mock behavior without asserting real logic
- Do NOT create tests that pass regardless of implementation (tautological tests)
- Do NOT skip error path testing; happy path alone is insufficient
- Do NOT hardcode expected values that mirror implementation details rather than requirements
- Do NOT generate tests for trivial getters/setters without business logic
- DO test behavior, not implementation (what it does, not how)
- DO include edge cases: nil, empty, boundary values, concurrent access
- DO verify async behavior with proper expectations and timeouts
- DO name tests clearly: `test_[method]_[scenario]_[expectedResult]`
- DO generate one assertion per test for clear failure diagnosis

---

### Phase 1: Prompt Patterns for Test Generation

#### 1.1 The Analysis-First Pattern

When asking an AI agent to generate tests, structure the prompt to force analysis before generation:

```markdown
## Test Generation Request

### Step 1: Analyze (do not write code yet)
Read the source file at `[path]` and list:
1. All public methods and their signatures
2. All dependencies (protocols/classes injected or referenced)
3. All code paths per method (happy path, error cases, edge cases)
4. All guard/precondition checks that can fail

### Step 2: Plan
For each method, outline test cases:
- Method name → [scenario] → [expected outcome]
- Include at least: 1 happy path, 1 error path, 1 edge case per method

### Step 3: Generate
Write XCTest code following these rules:
- One test class per source class
- setUp/tearDown for shared state
- Async tests where the source is async
- Descriptive names: test_[method]_[scenario]_[expectedResult]
```

#### 1.2 Example: Generating Tests for a Service

```swift
// SOURCE: File: Services/OrderService.swift

protocol OrderServiceProtocol {
    func placeOrder(_ cart: Cart) async throws -> Order
    func cancelOrder(id: String) async throws
    func fetchOrder(id: String) async throws -> Order
}

final class OrderService: OrderServiceProtocol {
    private let apiClient: APIClientProtocol
    private let validator: OrderValidatorProtocol
    private let analytics: AnalyticsProtocol

    init(apiClient: APIClientProtocol, validator: OrderValidatorProtocol, analytics: AnalyticsProtocol) {
        self.apiClient = apiClient
        self.validator = validator
        self.analytics = analytics
    }

    func placeOrder(_ cart: Cart) async throws -> Order {
        guard !cart.items.isEmpty else {
            throw OrderError.emptyCart
        }
        try validator.validate(cart)
        let order = try await apiClient.post("/orders", body: cart)
        analytics.track(.orderPlaced(order.id))
        return order
    }

    func cancelOrder(id: String) async throws {
        let order = try await apiClient.get("/orders/\(id)")
        guard order.status == .pending else {
            throw OrderError.cannotCancel(reason: "Order is \(order.status)")
        }
        try await apiClient.delete("/orders/\(id)")
        analytics.track(.orderCancelled(id))
    }

    func fetchOrder(id: String) async throws -> Order {
        try await apiClient.get("/orders/\(id)")
    }
}
```

```swift
// GENERATED: File: Tests/Services/OrderServiceTests.swift

import XCTest
@testable import YourApp

final class OrderServiceTests: XCTestCase {
    private var sut: OrderService!
    private var mockAPI: MockAPIClient!
    private var mockValidator: MockOrderValidator!
    private var mockAnalytics: MockAnalytics!

    override func setUp() {
        super.setUp()
        mockAPI = MockAPIClient()
        mockValidator = MockOrderValidator()
        mockAnalytics = MockAnalytics()
        sut = OrderService(
            apiClient: mockAPI,
            validator: mockValidator,
            analytics: mockAnalytics
        )
    }

    override func tearDown() {
        sut = nil
        mockAPI = nil
        mockValidator = nil
        mockAnalytics = nil
        super.tearDown()
    }

    // MARK: - placeOrder

    func test_placeOrder_withValidCart_returnsOrder() async throws {
        let cart = Cart.fixture(items: [.fixture()])
        let expectedOrder = Order.fixture(id: "order-1")
        mockAPI.postResult = .success(expectedOrder)

        let result = try await sut.placeOrder(cart)

        XCTAssertEqual(result.id, "order-1")
        XCTAssertTrue(mockValidator.validateCalled)
        XCTAssertEqual(mockAnalytics.trackedEvents.count, 1)
    }

    func test_placeOrder_withEmptyCart_throwsEmptyCartError() async {
        let cart = Cart.fixture(items: [])

        do {
            _ = try await sut.placeOrder(cart)
            XCTFail("Expected OrderError.emptyCart")
        } catch {
            XCTAssertEqual(error as? OrderError, .emptyCart)
        }

        XCTAssertFalse(mockValidator.validateCalled)
        XCTAssertTrue(mockAnalytics.trackedEvents.isEmpty)
    }

    func test_placeOrder_whenValidationFails_throwsValidationError() async {
        let cart = Cart.fixture(items: [.fixture()])
        mockValidator.shouldThrow = OrderError.invalidItems

        do {
            _ = try await sut.placeOrder(cart)
            XCTFail("Expected validation error")
        } catch {
            XCTAssertEqual(error as? OrderError, .invalidItems)
        }

        XCTAssertFalse(mockAPI.postCalled)
    }

    func test_placeOrder_whenAPIFails_propagatesError() async {
        let cart = Cart.fixture(items: [.fixture()])
        mockAPI.postResult = .failure(APIError.serverError(500))

        do {
            _ = try await sut.placeOrder(cart)
            XCTFail("Expected API error")
        } catch {
            XCTAssertTrue(error is APIError)
        }
    }

    // MARK: - cancelOrder

    func test_cancelOrder_withPendingOrder_succeeds() async throws {
        mockAPI.getResult = .success(Order.fixture(status: .pending))

        try await sut.cancelOrder(id: "order-1")

        XCTAssertTrue(mockAPI.deleteCalled)
        XCTAssertEqual(mockAnalytics.trackedEvents.first, .orderCancelled("order-1"))
    }

    func test_cancelOrder_withShippedOrder_throwsCannotCancel() async {
        mockAPI.getResult = .success(Order.fixture(status: .shipped))

        do {
            try await sut.cancelOrder(id: "order-1")
            XCTFail("Expected cannotCancel error")
        } catch let error as OrderError {
            if case .cannotCancel = error {
                // Expected
            } else {
                XCTFail("Wrong error type: \(error)")
            }
        } catch {
            XCTFail("Unexpected error: \(error)")
        }

        XCTAssertFalse(mockAPI.deleteCalled)
    }
}
```

---

### Phase 2: Mock Generation Patterns

**CHECKPOINT 1:** Confirm source code analysis is complete before generating mocks.

```markdown
## Code Analysis Summary

| Method | Happy Path | Error Paths | Edge Cases | Dependencies |
|--------|-----------|-------------|------------|--------------|
| placeOrder | Valid cart → Order | Empty cart, validation fail, API fail | Single item cart | API, Validator, Analytics |
| cancelOrder | Pending → success | Non-pending, API fail | Already cancelled | API, Analytics |
| fetchOrder | Valid ID → Order | Invalid ID, API fail | — | API |

**Proceed with mock generation?**
```

#### 2.1 Protocol-Based Mock Template

```swift
// File: Tests/Mocks/MockAPIClient.swift

@testable import YourApp

final class MockAPIClient: APIClientProtocol {
    // Track calls
    var getCalled = false
    var postCalled = false
    var deleteCalled = false
    var lastGetPath: String?
    var lastPostPath: String?

    // Configure results
    var getResult: Result<Any, Error> = .failure(APIError.notConfigured)
    var postResult: Result<Any, Error> = .failure(APIError.notConfigured)
    var deleteResult: Result<Void, Error> = .success(())

    func get<T: Decodable>(_ path: String) async throws -> T {
        getCalled = true
        lastGetPath = path
        switch getResult {
        case .success(let value):
            guard let typed = value as? T else {
                throw APIError.decodingFailed
            }
            return typed
        case .failure(let error):
            throw error
        }
    }

    func post<T: Decodable>(_ path: String, body: Encodable) async throws -> T {
        postCalled = true
        lastPostPath = path
        switch postResult {
        case .success(let value):
            guard let typed = value as? T else {
                throw APIError.decodingFailed
            }
            return typed
        case .failure(let error):
            throw error
        }
    }

    func delete(_ path: String) async throws {
        deleteCalled = true
        switch deleteResult {
        case .success: return
        case .failure(let error): throw error
        }
    }

    func reset() {
        getCalled = false
        postCalled = false
        deleteCalled = false
        lastGetPath = nil
        lastPostPath = nil
    }
}
```

#### 2.2 Mock Generation Prompt

When asking AI to generate mocks, use this pattern:

```markdown
Generate a mock for this protocol. Rules:
1. Track EVERY method call with a boolean `[method]Called` property
2. Store the LAST arguments passed to each method
3. Allow configuring return values via `[method]Result: Result<ReturnType, Error>`
4. Support async methods with the same async signature
5. Add a `reset()` method to clear all tracking state
6. Do NOT use any mocking library -- pure Swift manual mocks only
```

---

### Phase 3: Test Data Factories

#### 3.1 Fixture Pattern

```swift
// File: Tests/Fixtures/Order+Fixture.swift

@testable import YourApp

extension Order {
    static func fixture(
        id: String = "test-order-\(UUID().uuidString.prefix(8))",
        status: OrderStatus = .pending,
        items: [OrderItem] = [.fixture()],
        total: Decimal = 29.99,
        createdAt: Date = .now
    ) -> Order {
        Order(
            id: id,
            status: status,
            items: items,
            total: total,
            createdAt: createdAt
        )
    }
}

extension OrderItem {
    static func fixture(
        id: String = "item-\(UUID().uuidString.prefix(8))",
        name: String = "Test Item",
        price: Decimal = 9.99,
        quantity: Int = 1
    ) -> OrderItem {
        OrderItem(id: id, name: name, price: price, quantity: quantity)
    }
}

extension Cart {
    static func fixture(
        items: [CartItem] = [.fixture()]
    ) -> Cart {
        Cart(items: items)
    }
}
```

#### 3.2 Factory Generation Prompt

```markdown
Generate test fixtures for all models used in [SourceFile]. Rules:
1. Use `static func fixture(...)` with default parameters for ALL properties
2. Defaults should produce a valid, typical instance
3. Use UUID-based IDs to avoid test isolation issues
4. Each property should be overridable via parameter
5. Add fixtures for ALL nested types used as dependencies
6. Place in Tests/Fixtures/[ModelName]+Fixture.swift
```

---

### Phase 4: Coverage Gap Analysis & Test Quality Review

**CHECKPOINT 2:** Review generated tests before quality audit.

```markdown
## Generated Test Summary

| Source File | Test File | Test Count | Paths Covered |
|-------------|-----------|------------|---------------|
| OrderService.swift | OrderServiceTests.swift | 6 | Happy, error, edge for placeOrder + cancelOrder |
| — | MockAPIClient.swift | — | Mock with call tracking |
| — | Order+Fixture.swift | — | Fixtures for Order, OrderItem, Cart |

**Ready for coverage gap analysis and quality review?**
```

#### 4.1 Coverage Gap Identification Prompt

```markdown
## Coverage Gap Analysis Request

Analyze the test file at `[test path]` against the source at `[source path]`.

Identify:
1. **Untested methods** - Public methods with zero test cases
2. **Untested branches** - if/else, switch, guard paths not exercised
3. **Missing error scenarios** - throws/catch paths without tests
4. **Missing edge cases** - nil, empty, max/min, concurrent access
5. **Missing interaction tests** - Dependencies called with wrong arguments

For each gap, write:
- Gap: [description]
- Risk: [what could break without this test]
- Test: [complete test method code]
```

#### 4.2 Test Quality Review Checklist

Use this checklist to evaluate AI-generated tests:

```markdown
## Test Quality Review

### Meaningfulness (tests exercise real logic)
- [ ] Tests fail when implementation logic is removed
- [ ] Tests verify BEHAVIOR, not implementation sequence
- [ ] No tautological assertions (comparing a value to itself)
- [ ] Error paths tested with specific error type assertions

### Isolation (tests are independent)
- [ ] Each test creates its own state in setUp
- [ ] No test depends on another test's execution order
- [ ] Mocks are reset or recreated per test
- [ ] No shared mutable state between tests

### Clarity (tests are readable)
- [ ] Test names follow: test_[method]_[scenario]_[expected]
- [ ] Arrange-Act-Assert structure is clear
- [ ] One logical assertion per test
- [ ] No magic numbers; values relate to the scenario

### Completeness (tests cover the contract)
- [ ] All public methods have at least one test
- [ ] Happy path, error path, and edge case per method
- [ ] Async methods tested with async/await
- [ ] Thrown errors verified by type and associated value

### Robustness (tests don't break from valid changes)
- [ ] Tests don't verify internal method call order
- [ ] Tests don't depend on exact string formatting
- [ ] Tests use fixture factories, not hardcoded literals
- [ ] Tests survive refactoring that preserves behavior
```

#### 4.3 Anti-Pattern Detection Prompt

```markdown
Review these test files for anti-patterns:

1. **Assertion-free tests** - Tests that run code but never assert
2. **Always-passing tests** - Tests with assertions that can never fail
3. **Over-mocking** - Tests that mock the class under test itself
4. **Fragile ordering** - Tests that assert mock call order unnecessarily
5. **Copy-paste tests** - Duplicated test bodies with minimal variation
6. **Missing async handling** - Async code tested synchronously
7. **Ignored errors** - try? in tests hiding failures

For each anti-pattern found:
- File:Line — [Pattern Name] — [Fix]
```

---

## Expected Output

### File Structure

```
Tests/
├── Services/
│   └── OrderServiceTests.swift        # Test class for OrderService
├── Mocks/
│   ├── MockAPIClient.swift            # API client mock
│   ├── MockOrderValidator.swift       # Validator mock
│   └── MockAnalytics.swift            # Analytics mock
└── Fixtures/
    ├── Order+Fixture.swift            # Order test data factory
    ├── Cart+Fixture.swift             # Cart test data factory
    └── OrderItem+Fixture.swift        # OrderItem test data factory
```

### Implementation Checklist

- [ ] Source code analyzed before test generation
- [ ] All dependencies identified and mocked
- [ ] Test data factories created for all models
- [ ] Happy path tests for every public method
- [ ] Error path tests for every throwable method
- [ ] Edge case tests (nil, empty, boundary)
- [ ] Async tests use async/await properly
- [ ] Test names follow naming convention
- [ ] Quality review checklist passed
- [ ] Coverage gaps identified and filled
- [ ] No test anti-patterns present

---

## Techniques Used

- **ST-01** (Clear Objective): Focused on AI-assisted test generation patterns
- **ST-02** (Sequential Instructions): Progressive from analysis through generation to quality review

---

## Related Prompts

- [ios_unit_test_generation.md](../testing/ios_unit_test_generation.md) - Manual unit test writing patterns
- [ios_integration_testing.md](../testing/ios_integration_testing.md) - Integration testing strategies
- [ios_test_strategy_design.md](../testing/ios_test_strategy_design.md) - Overall test strategy planning
- [ios_performance_testing.md](../testing/ios_performance_testing.md) - Performance test generation
