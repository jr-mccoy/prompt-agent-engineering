---
title: "iOS Test Coverage Analysis"
category: mobile-development
description: "Analyze XCTest and XCUITest coverage across an iOS codebase, identify critical untested paths, assess mock quality, and provide a prioritized plan to close coverage gaps"
techniques:
  - ST-01
  - RT-02
difficulty: intermediate
tags:
  - ios
  - swift
  - testing
  - xctest
  - coverage
updated: "2026-03-20"
---

# iOS Test Coverage Analysis

**Objective:** Analyze test coverage across an iOS codebase — XCTest unit tests, XCUITest UI tests, and integration tests — to identify critical untested business logic, evaluate mock and stub quality, assess test architecture, and produce a prioritized gap-closure plan focused on risk reduction.

**When to Use:** Use this prompt when test coverage is unknown or perceived as insufficient, before major refactoring, after a series of production bugs that should have been caught by tests, or when establishing a testing strategy for the team.

**Prompt Type:** Modular (200-350 lines)

---

## Context Gathering

Before beginning the analysis, gather context:

1. **Current Testing State:**
   - "Do you have existing code coverage metrics (Xcode coverage reports, CI reports)?"
   - "What testing frameworks are in use beyond XCTest (Quick/Nimble, swift-testing, etc.)?"

2. **Testing Goals:**
   - "Is there a target coverage percentage or testing policy?"
   - "Are you focused on unit testing, UI testing, or both?"

3. **Pain Points:**
   - "Have there been recent production bugs that tests should have caught?"
   - "Are tests slow, flaky, or hard to maintain?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Check actual coverage data** - Don't estimate coverage by counting test files. Use Xcode's coverage report or inspect test targets.
2. **Assess test quality, not just quantity** - A file with 90% line coverage but no meaningful assertions has poor effective coverage.
3. **Identify what matters most** - Not all code needs equal coverage. Business logic and data handling need more than layout code.
4. **Verify mock correctness** - Mocks that don't match the protocol contract give false confidence.

**A codebase with focused, high-quality tests on critical paths is better than one with high overall coverage of trivial code.** Don't recommend coverage for coverage's sake.

### False-Positive Prevention

- ❌ Do NOT equate line coverage percentage with test quality
- ❌ Do NOT flag low coverage on pure UI layout code as critical
- ❌ Do NOT recommend testing auto-generated code or simple data models with no logic
- ❌ Do NOT count tests that always pass (no real assertions) as adequate
- ✅ DO prioritize coverage of business logic, data transformation, and error handling
- ✅ DO check that tests actually assert meaningful outcomes
- ✅ DO evaluate test isolation (tests that depend on order or state are fragile)
- ✅ DO distinguish between code that should be tested and code where testing adds minimal value

---

### Phase 1: Coverage Metrics Analysis

#### 1.1 Test Infrastructure Inventory

**Catalog existing test setup:**

```
// Test targets to locate
AppTests/              // Unit test target
AppUITests/            // UI test target
AppIntegrationTests/   // Integration test target (if separate)
AppSnapshotTests/      // Snapshot test target (if using)

// Testing frameworks in use
@testable import App   // Standard XCTest
import Testing         // Swift Testing framework (swift-testing)
import Quick           // BDD-style testing
import Nimble          // Matcher framework
import ViewInspector   // SwiftUI view testing
import SnapshotTesting // Point-Free snapshot tests
```

**Infrastructure Summary:**

| Aspect | Status | Details |
|--------|--------|---------|
| Unit test target | [Exists/Missing] | [Test count] |
| UI test target | [Exists/Missing] | [Test count] |
| CI test execution | [Yes/No] | [Platform: Xcode Cloud, GitHub Actions, etc.] |
| Coverage reporting | [Enabled/Disabled] | [Tool used] |
| Test schemes configured | [Yes/No] | [Which schemes] |

#### 1.2 Coverage Metrics by Module

**Break down coverage by logical module/feature:**

| Module/Feature | Files | Lines | Line Coverage | Branch Coverage | Test Count |
|---------------|-------|-------|--------------|----------------|------------|
| Networking | [N] | [N] | [%] | [%] | [N] |
| Authentication | [N] | [N] | [%] | [%] | [N] |
| Data Models | [N] | [N] | [%] | [%] | [N] |
| ViewModels | [N] | [N] | [%] | [%] | [N] |
| Repositories | [N] | [N] | [%] | [%] | [N] |
| Utilities | [N] | [N] | [%] | [%] | [N] |
| Views (UI) | [N] | [N] | [%] | [%] | [N] |

#### 1.3 Critical Path Coverage

**Identify business-critical paths and their test status:**

```swift
// Critical paths that MUST have test coverage:

// 1. Authentication flows
func login(email: String, password: String) async throws -> User
func refreshToken() async throws -> Token
func logout() async

// 2. Payment / transaction flows
func processPayment(_ payment: Payment) async throws -> Receipt
func validateCart(_ cart: Cart) -> [ValidationError]

// 3. Data persistence and sync
func saveUserData(_ data: UserData) throws
func syncWithServer() async throws -> SyncResult

// 4. Error handling paths
func handleNetworkError(_ error: NetworkError) -> UserMessage
func recoverFromCorruptedData() throws
```

| Critical Path | Has Tests | Coverage | Edge Cases Covered | Assertion Quality |
|--------------|-----------|---------|-------------------|-------------------|
| [Path name] | [Yes/No] | [%] | [Yes/Partial/No] | [Strong/Weak/None] |

---

### Phase 2: Test Quality Assessment

#### 2.1 Assertion Quality Audit

**Evaluate whether tests make meaningful assertions:**

```swift
// WEAK: Test runs but asserts nothing meaningful
func testFetchUsers() async throws {
    let viewModel = UsersViewModel(repository: mockRepo)
    await viewModel.fetchUsers()
    XCTAssertNotNil(viewModel)  // This always passes
}

// STRONG: Tests specific behavior and edge cases
func testFetchUsers_success_populatesUsersAndStopsLoading() async throws {
    let mockRepo = MockUserRepository(result: .success([.stub]))
    let viewModel = UsersViewModel(repository: mockRepo)

    await viewModel.fetchUsers()

    XCTAssertEqual(viewModel.users.count, 1)
    XCTAssertEqual(viewModel.users.first?.name, "Test User")
    XCTAssertFalse(viewModel.isLoading)
    XCTAssertNil(viewModel.errorMessage)
}

func testFetchUsers_networkError_setsErrorMessage() async throws {
    let mockRepo = MockUserRepository(result: .failure(.networkUnavailable))
    let viewModel = UsersViewModel(repository: mockRepo)

    await viewModel.fetchUsers()

    XCTAssertTrue(viewModel.users.isEmpty)
    XCTAssertFalse(viewModel.isLoading)
    XCTAssertEqual(viewModel.errorMessage, "Network unavailable. Please try again.")
}
```

**Assertion Quality Metrics:**

| Category | Tests | Avg Assertions/Test | Weak Tests | No-Assert Tests |
|----------|-------|-------------------|------------|-----------------|
| ViewModel | [N] | [N] | [N] | [N] |
| Repository | [N] | [N] | [N] | [N] |
| Utility | [N] | [N] | [N] | [N] |
| Model | [N] | [N] | [N] | [N] |

#### 2.2 Mock and Stub Quality

**Evaluate test doubles:**

```swift
// GOOD: Mock that tracks interactions and validates contracts
class MockNetworkService: NetworkServiceProtocol {
    var fetchCallCount = 0
    var lastRequest: URLRequest?
    var stubbedResult: Result<Data, Error> = .success(Data())

    func fetch(_ request: URLRequest) async throws -> Data {
        fetchCallCount += 1
        lastRequest = request
        return try stubbedResult.get()
    }
}

// BAD: Mock that doesn't match protocol evolution
class MockNetworkService: NetworkServiceProtocol {
    func fetch(_ request: URLRequest) async throws -> Data {
        return Data()  // Always succeeds, never validates
    }
    // Missing: new protocol method added last month
}

// BAD: Mock with real side effects
class MockAnalytics: AnalyticsProtocol {
    func track(_ event: String) {
        RealAnalytics.shared.track(event)  // Actually sends events!
    }
}
```

**Mock Quality Checklist:**

| Check | Status |
|-------|--------|
| Mocks conform to protocols (not subclassing concrete types) | [Yes/No] |
| Mocks allow configurable return values / errors | [Yes/No] |
| Mocks track call counts and arguments for verification | [Yes/No] |
| Mocks stay in sync with protocol changes | [Yes/No] |
| No mocks with real side effects | [Yes/No] |

#### 2.3 Test Isolation and Reliability

**Check for flaky or order-dependent tests:**

```swift
// RED FLAG: Tests sharing mutable state
class UserTests: XCTestCase {
    static var sharedUser: User!  // Shared across tests — order-dependent

    // RED FLAG: setUp not resetting state
    override func setUp() {
        // Missing: state reset
    }
}

// RED FLAG: Tests depending on timing
func testDebounce() {
    viewModel.search("query")
    Thread.sleep(forTimeInterval: 0.5)  // Flaky on slow CI machines
    XCTAssertEqual(viewModel.results.count, 3)
}

// GOOD: Deterministic async testing
func testDebounce() async {
    let clock = TestClock()
    let viewModel = SearchViewModel(clock: clock)
    viewModel.search("query")
    await clock.advance(by: .milliseconds(500))
    XCTAssertEqual(viewModel.results.count, 3)
}
```

| Issue | Occurrences | Impact |
|-------|-------------|--------|
| Shared mutable state between tests | [N] | Flaky results |
| Time-dependent assertions | [N] | CI failures |
| Network-dependent tests | [N] | Offline failures |
| File system dependencies | [N] | Environment-specific failures |

---

### Phase 3: Gap Analysis and Prioritization

#### 3.1 Coverage Gap Prioritization

**Prioritize gaps by risk, not just by coverage percentage:**

| Untested Area | Risk Level | Business Impact | Ease of Testing | Priority |
|--------------|------------|-----------------|-----------------|----------|
| [Area] | [High/Med/Low] | [Revenue/Safety/UX/Dev] | [Easy/Medium/Hard] | [P1-P4] |

**Priority Logic:**
- **P1:** High risk + High business impact (payment flows, auth, data integrity)
- **P2:** High risk + Medium impact OR Medium risk + High impact
- **P3:** Medium risk + Medium impact
- **P4:** Low risk or low impact (UI layout, logging, analytics)

#### 3.2 Recommended Test Additions

```markdown
### P1: Must-Have Tests (Next Sprint)

| Test | Type | Target Coverage | Estimated Effort |
|------|------|----------------|-----------------|
| [Description] | [Unit/Integration/UI] | [What to assert] | [Hours] |

### P2: Should-Have Tests (This Quarter)

| Test | Type | Target Coverage | Estimated Effort |
|------|------|----------------|-----------------|
| [Description] | [Unit/Integration/UI] | [What to assert] | [Hours] |

### P3: Nice-to-Have Tests (Next Quarter)

| Test | Type | Target Coverage | Estimated Effort |
|------|------|----------------|-----------------|
| [Description] | [Unit/Integration/UI] | [What to assert] | [Hours] |
```

---

## Expected Output

1. **Coverage Metrics Dashboard** - Quantitative coverage by module and critical path
2. **Test Quality Assessment** - Assertion quality, mock quality, test isolation report
3. **Gap Prioritization** - Untested areas ranked by risk and business impact
4. **Recommended Test Plan** - Prioritized list of tests to add with effort estimates

---

## Example Interaction

**User:** Analyze the test coverage of our iOS fitness tracking app. We have some tests but keep finding bugs in production.

**Agent:** I'll analyze your test suite comprehensively. Let me start by scanning test targets and coverage data.

*[Agent scans test targets, coverage reports, and test quality]*

**Agent:**

## Test Coverage Summary

**Overall Line Coverage:** 34% (below recommended 60% minimum for mobile apps)

### Coverage by Module

| Module | Coverage | Critical Gaps |
|--------|----------|---------------|
| Workout Tracking | 12% | Core business logic untested — `WorkoutCalculator` has 0 tests |
| HealthKit Sync | 0% | Entire sync pipeline untested |
| User Auth | 67% | Login tested; password reset and token refresh untested |
| Social Feed | 45% | Post creation tested; comment threading and blocking untested |
| Notifications | 8% | Only scheduling tested; delivery handling untested |

### Root Cause of Production Bugs

Analyzing your last 5 production bugs against test coverage:
1. **Calorie calculation off by 10%** — `WorkoutCalculator.swift` has 0% coverage
2. **HealthKit sync lost data** — No tests for conflict resolution in `HealthKitSyncManager.swift`
3. **Crash on workout completion** — Force unwrap at `WorkoutSession.swift:89` untested with nil data

All 3 bugs occur in code with less than 15% coverage. **Your production bugs are concentrated in untested code.**

**Shall I provide the prioritized test plan to close these gaps?**

---

## Techniques Used

- **ST-01** (Clear Objective): Focused coverage analysis with quality emphasis
- **RT-02** (Multi-Dimensional Analysis): Coverage metrics, test quality, mock quality, gap prioritization

---

## Related Prompts

- [ios_technical_debt_assessment.md](ios_technical_debt_assessment.md) - Testing debt as part of broader assessment
- [ios_codebase_health_assessment.md](ios_codebase_health_assessment.md) - Overall codebase evaluation
- [ios_ai_code_review.md](ios_ai_code_review.md) - AI-assisted code review including testability

---

## Customization Guide

### For SwiftUI Apps
- Add ViewInspector or snapshot testing assessment
- Check `@Preview` usage as informal test coverage
- Evaluate View vs ViewModel testing balance
- Assess whether SwiftUI navigation is testable

### For TCA (The Composable Architecture) Apps
- Check `TestStore` usage for Reducer testing
- Verify Effect testing with test dependencies
- Assess `@Dependency` test override coverage
- Check exhaustive vs non-exhaustive test store usage

### For CI/CD Integration
- Verify coverage gates in CI pipeline
- Check test execution time and parallelization
- Assess test result reporting (JUnit XML, Xcode results)
- Evaluate flaky test detection and quarantine process

### For Legacy UIKit Apps
- Focus on ViewModel extraction to enable unit testing
- Assess UITest coverage for critical user flows
- Check for testability blockers (singletons, tight coupling)
- Evaluate whether introducing protocols for DI is feasible
