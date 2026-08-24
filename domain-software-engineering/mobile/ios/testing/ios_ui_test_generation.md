---
title: "iOS UI Test Generation"
category: mobile-development
description: "Generate XCUITest UI tests with accessibility identifier strategy, page object pattern, test data management, and screen navigation flow verification"
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
  - xcuitest
  - ui-testing
  - accessibility
updated: "2026-03-19"
---

# iOS UI Test Generation

**Objective:** Generate reliable, maintainable XCUITest UI tests for iOS applications. Covers accessibility identifier strategy for element queries, the Page Object pattern for reusable screen abstractions, test data management via launch arguments, and navigation flow verification across multi-screen journeys.

**When to Use:** Use this prompt when you need end-to-end flow verification (login, onboarding, checkout), when critical user journeys must be protected against regressions, when accessibility compliance needs to be validated through automation, or when manual QA time for repetitive smoke tests needs to be reduced.

**Prompt Type:** Comprehensive (220-260 lines)

---

## Context Gathering

1. **Application Structure:**
   - "What are the key user flows to test (login, onboarding, purchase, etc.)?"
   - "Is the app SwiftUI, UIKit, or hybrid?"
   - "How many screens are involved in the primary flow?"

2. **Accessibility Identifiers:**
   - "Are accessibility identifiers already set on interactive elements?"
   - "What naming convention is used (if any)?"

3. **Test Environment:**
   - "Does the app support launch arguments for test configuration (mock data, skip auth)?"
   - "Is there a test/staging backend, or do tests run against production?"

4. **CI/CD Constraints:**
   - "What's the acceptable UI test execution time?"
   - "Which simulator(s) should tests target?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before generating ANY UI test, you MUST:**

1. **Verify element accessibility** - Confirm that elements can be queried via accessibility identifiers, labels, or element type. If identifiers are missing, provide the production code additions needed.
2. **Identify state dependencies** - UI tests must not depend on previous test state. Each test must set up its own preconditions.
3. **Account for async loading** - Use `waitForExistence(timeout:)` for elements that appear after network calls or animations. Never use `sleep()`.
4. **Validate on real flows** - Don't test SwiftUI previews or isolated views. UI tests verify the assembled, navigable application.
5. **Check for flakiness vectors** - Animations, network timing, keyboard appearance, and system alerts all cause flaky tests. Address each explicitly.

**A small suite of reliable UI tests is vastly more valuable than a large suite of flaky ones.** Only automate flows that justify the maintenance cost.

### False-Positive Prevention

- ❌ Do NOT use `sleep()` for timing - use `waitForExistence(timeout:)` or `XCTNSPredicateExpectation`
- ❌ Do NOT query elements by text content that changes with localization
- ❌ Do NOT test visual styling or layout (use snapshot tests for that)
- ❌ Do NOT create tests that depend on execution order
- ❌ Do NOT hardcode test data that could conflict with other test runs
- ✅ DO use accessibility identifiers for all element queries
- ✅ DO use the Page Object pattern to encapsulate screen interactions
- ✅ DO reset app state before each test via launch arguments
- ✅ DO handle system alerts (notifications, location, camera permissions)
- ✅ DO set `continueAfterFailure = false` for flow tests

---

### Step 1: Define Accessibility Identifier Strategy

```swift
// MARK: - Production Code: Accessibility Identifier Constants

enum AccessibilityID {

    enum Login {
        static let emailField = "login_email_field"
        static let passwordField = "login_password_field"
        static let submitButton = "login_submit_button"
        static let errorLabel = "login_error_label"
        static let forgotPasswordButton = "login_forgot_password_button"
        static let signUpLink = "login_sign_up_link"
    }

    enum Home {
        static let welcomeLabel = "home_welcome_label"
        static let feedList = "home_feed_list"
        static let profileButton = "home_profile_button"
        static let searchField = "home_search_field"
        static let newPostButton = "home_new_post_button"
    }

    enum Profile {
        static let nameLabel = "profile_name_label"
        static let editButton = "profile_edit_button"
        static let logoutButton = "profile_logout_button"
        static let avatarImage = "profile_avatar_image"
    }
}

// SwiftUI Usage:
struct LoginView: View {
    var body: some View {
        TextField("Email", text: $email)
            .accessibilityIdentifier(AccessibilityID.Login.emailField)

        SecureField("Password", text: $password)
            .accessibilityIdentifier(AccessibilityID.Login.passwordField)

        Button("Log In") { login() }
            .accessibilityIdentifier(AccessibilityID.Login.submitButton)
    }
}

// UIKit Usage:
class LoginViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        emailField.accessibilityIdentifier = AccessibilityID.Login.emailField
        passwordField.accessibilityIdentifier = AccessibilityID.Login.passwordField
        submitButton.accessibilityIdentifier = AccessibilityID.Login.submitButton
    }
}
```

**Naming Convention:** `{screen}_{element}_{type}` (e.g., `login_email_field`, `home_feed_list`)

### Step 2: Implement Page Object Pattern

```swift
// MARK: - Page Objects

protocol Page {
    var app: XCUIApplication { get }
    init(app: XCUIApplication)
}

// --- Login Page ---
struct LoginPage: Page {
    let app: XCUIApplication

    init(app: XCUIApplication) {
        self.app = app
    }

    // MARK: - Elements

    var emailField: XCUIElement {
        app.textFields[AccessibilityID.Login.emailField]
    }

    var passwordField: XCUIElement {
        app.secureTextFields[AccessibilityID.Login.passwordField]
    }

    var submitButton: XCUIElement {
        app.buttons[AccessibilityID.Login.submitButton]
    }

    var errorLabel: XCUIElement {
        app.staticTexts[AccessibilityID.Login.errorLabel]
    }

    // MARK: - Actions

    @discardableResult
    func typeEmail(_ email: String) -> Self {
        emailField.tap()
        emailField.clearAndTypeText(email)
        return self
    }

    @discardableResult
    func typePassword(_ password: String) -> Self {
        passwordField.tap()
        passwordField.clearAndTypeText(password)
        return self
    }

    @discardableResult
    func tapSubmit() -> Self {
        submitButton.tap()
        return self
    }

    func login(email: String, password: String) -> HomePage {
        typeEmail(email)
            .typePassword(password)
            .tapSubmit()
        return HomePage(app: app)
    }

    // MARK: - Assertions

    func assertErrorVisible(message: String) -> Self {
        XCTAssertTrue(errorLabel.waitForExistence(timeout: 3))
        XCTAssertEqual(errorLabel.label, message)
        return self
    }

    func assertIsDisplayed() -> Self {
        XCTAssertTrue(emailField.waitForExistence(timeout: 5))
        return self
    }
}

// --- Home Page ---
struct HomePage: Page {
    let app: XCUIApplication

    init(app: XCUIApplication) {
        self.app = app
    }

    var welcomeLabel: XCUIElement {
        app.staticTexts[AccessibilityID.Home.welcomeLabel]
    }

    var profileButton: XCUIElement {
        app.buttons[AccessibilityID.Home.profileButton]
    }

    var feedList: XCUIElement {
        app.collectionViews[AccessibilityID.Home.feedList]
    }

    func assertIsDisplayed() -> Self {
        XCTAssertTrue(welcomeLabel.waitForExistence(timeout: 5))
        return self
    }

    func tapProfile() -> ProfilePage {
        profileButton.tap()
        return ProfilePage(app: app)
    }

    func assertFeedHasItems(minimum: Int) -> Self {
        XCTAssertTrue(feedList.waitForExistence(timeout: 5))
        XCTAssertGreaterThanOrEqual(feedList.cells.count, minimum)
        return self
    }
}

// --- Profile Page ---
struct ProfilePage: Page {
    let app: XCUIApplication

    init(app: XCUIApplication) {
        self.app = app
    }

    var nameLabel: XCUIElement {
        app.staticTexts[AccessibilityID.Profile.nameLabel]
    }

    var logoutButton: XCUIElement {
        app.buttons[AccessibilityID.Profile.logoutButton]
    }

    func assertNameEquals(_ name: String) -> Self {
        XCTAssertTrue(nameLabel.waitForExistence(timeout: 3))
        XCTAssertEqual(nameLabel.label, name)
        return self
    }

    func tapLogout() -> LoginPage {
        logoutButton.tap()
        return LoginPage(app: app)
    }
}
```

### Step 3: Configure Test Data Management

```swift
// MARK: - Launch Arguments for Test Configuration

extension XCUIApplication {

    enum TestLaunchArg: String {
        case uiTesting = "--uitesting"
        case resetState = "--reset-state"
        case mockNetwork = "--mock-network"
        case skipOnboarding = "--skip-onboarding"
        case useTestUser = "--test-user"
    }

    func configureForUITesting(
        resetState: Bool = true,
        mockNetwork: Bool = true,
        skipOnboarding: Bool = true
    ) {
        launchArguments = [TestLaunchArg.uiTesting.rawValue]
        if resetState { launchArguments.append(TestLaunchArg.resetState.rawValue) }
        if mockNetwork { launchArguments.append(TestLaunchArg.mockNetwork.rawValue) }
        if skipOnboarding { launchArguments.append(TestLaunchArg.skipOnboarding.rawValue) }

        // Pass test environment variables
        launchEnvironment["TEST_BASE_URL"] = "http://localhost:8080"
        launchEnvironment["TEST_USER_EMAIL"] = "test@example.com"
    }
}

// Production code check:
// In AppDelegate or @main App:
//   if CommandLine.arguments.contains("--uitesting") {
//       configureTestEnvironment()
//   }
```

### Step 4: Generate Flow Tests

```swift
import XCTest

final class LoginFlowUITests: XCTestCase {

    private var app: XCUIApplication!

    override func setUpWithError() throws {
        continueAfterFailure = false
        app = XCUIApplication()
        app.configureForUITesting()
        app.launch()
    }

    override func tearDownWithError() throws {
        app = nil
    }

    // MARK: - Happy Path

    func test_login_withValidCredentials_navigatesToHome() {
        LoginPage(app: app)
            .assertIsDisplayed()
            .login(email: "test@example.com", password: "Password1!")
            .assertIsDisplayed()
    }

    // MARK: - Error Handling

    func test_login_withInvalidEmail_showsError() {
        LoginPage(app: app)
            .typeEmail("not-an-email")
            .typePassword("Password1!")
            .tapSubmit()
            .assertErrorVisible(message: "Please enter a valid email")
    }

    func test_login_withWrongPassword_showsError() {
        LoginPage(app: app)
            .typeEmail("test@example.com")
            .typePassword("wrongpassword")
            .tapSubmit()
            .assertErrorVisible(message: "Invalid credentials")
    }

    func test_login_withEmptyFields_submitIsDisabled() {
        let loginPage = LoginPage(app: app)
        XCTAssertFalse(loginPage.submitButton.isEnabled)
    }

    // MARK: - Full User Journey

    func test_loginAndLogout_completeCycle() {
        LoginPage(app: app)
            .login(email: "test@example.com", password: "Password1!")
            .assertIsDisplayed()
            .tapProfile()
            .assertNameEquals("Test User")
            .tapLogout()
            .assertIsDisplayed()
    }

    // MARK: - Navigation

    func test_forgotPassword_navigatesToResetScreen() {
        let loginPage = LoginPage(app: app)
        loginPage.app.buttons[AccessibilityID.Login.forgotPasswordButton].tap()

        XCTAssertTrue(
            app.navigationBars["Reset Password"].waitForExistence(timeout: 3)
        )
    }
}
```

### Step 5: Handle System Alerts and Edge Cases

```swift
// MARK: - System Alert Handling

final class PermissionFlowUITests: XCTestCase {

    private var app: XCUIApplication!

    override func setUpWithError() throws {
        continueAfterFailure = false
        app = XCUIApplication()
        app.configureForUITesting()

        // Reset authorization status via launch argument
        app.launchArguments.append("--reset-permissions")
        app.launch()

        // Handle system alerts globally
        addUIInterruptionMonitor(withDescription: "System Alert") { alert in
            if alert.buttons["Allow"].exists {
                alert.buttons["Allow"].tap()
                return true
            }
            if alert.buttons["Allow While Using App"].exists {
                alert.buttons["Allow While Using App"].tap()
                return true
            }
            return false
        }
    }

    func test_cameraCapture_requestsPermission() {
        // Navigate to camera feature
        HomePage(app: app)
            .tapNewPost()

        // Trigger the interruption handler
        app.tap()

        // Verify camera view appears after permission granted
        XCTAssertTrue(
            app.otherElements["camera_capture_view"].waitForExistence(timeout: 5)
        )
    }
}

// MARK: - XCUIElement Helpers

extension XCUIElement {

    func clearAndTypeText(_ text: String) {
        guard let currentValue = value as? String, !currentValue.isEmpty else {
            typeText(text)
            return
        }
        let deleteString = String(repeating: XCUIKeyboardKey.delete.rawValue, count: currentValue.count)
        typeText(deleteString)
        typeText(text)
    }

    func waitAndTap(timeout: TimeInterval = 5) {
        XCTAssertTrue(waitForExistence(timeout: timeout), "Element \(identifier) not found")
        tap()
    }
}
```

---

## Expected Output

1. **Accessibility Identifier Constants** - Centralized enum with naming convention
2. **Page Object Classes** - Reusable screen abstractions with fluent API
3. **Launch Configuration** - Test data and environment setup via launch arguments
4. **Flow Tests** - Happy path, error handling, and full user journeys
5. **System Alert Handlers** - Permission dialogs and interruption monitors
6. **Helper Extensions** - Utilities for common XCUIElement operations

---

## Example Interaction

**User:** "Generate UI tests for our checkout flow: Cart -> Shipping Address -> Payment -> Confirmation"

**Agent Response:**

```swift
import XCTest

// MARK: - Page Objects

struct CartPage: Page {
    let app: XCUIApplication
    init(app: XCUIApplication) { self.app = app }

    var checkoutButton: XCUIElement { app.buttons["cart_checkout_button"] }
    var itemCount: XCUIElement { app.staticTexts["cart_item_count"] }
    var totalLabel: XCUIElement { app.staticTexts["cart_total_label"] }

    func assertItemCount(_ count: Int) -> Self {
        XCTAssertEqual(itemCount.label, "\(count) items")
        return self
    }

    func tapCheckout() -> ShippingPage {
        checkoutButton.waitAndTap()
        return ShippingPage(app: app)
    }
}

struct ShippingPage: Page {
    let app: XCUIApplication
    init(app: XCUIApplication) { self.app = app }

    func fillAddress(street: String, city: String, zip: String) -> Self {
        app.textFields["shipping_street_field"].clearAndTypeText(street)
        app.textFields["shipping_city_field"].clearAndTypeText(city)
        app.textFields["shipping_zip_field"].clearAndTypeText(zip)
        return self
    }

    func tapContinue() -> PaymentPage {
        app.buttons["shipping_continue_button"].waitAndTap()
        return PaymentPage(app: app)
    }
}

struct PaymentPage: Page {
    let app: XCUIApplication
    init(app: XCUIApplication) { self.app = app }

    func enterCard(number: String, exp: String, cvv: String) -> Self {
        app.textFields["payment_card_number"].clearAndTypeText(number)
        app.textFields["payment_expiry"].clearAndTypeText(exp)
        app.secureTextFields["payment_cvv"].clearAndTypeText(cvv)
        return self
    }

    func tapPay() -> ConfirmationPage {
        app.buttons["payment_pay_button"].waitAndTap()
        return ConfirmationPage(app: app)
    }
}

struct ConfirmationPage: Page {
    let app: XCUIApplication
    init(app: XCUIApplication) { self.app = app }

    var orderNumber: XCUIElement { app.staticTexts["confirmation_order_number"] }
    var successIcon: XCUIElement { app.images["confirmation_success_icon"] }

    func assertOrderConfirmed() -> Self {
        XCTAssertTrue(successIcon.waitForExistence(timeout: 10))
        XCTAssertTrue(orderNumber.exists)
        return self
    }
}

// MARK: - Checkout Flow Tests

final class CheckoutFlowUITests: XCTestCase {

    private var app: XCUIApplication!

    override func setUpWithError() throws {
        continueAfterFailure = false
        app = XCUIApplication()
        app.configureForUITesting()
        app.launchEnvironment["PRELOAD_CART"] = "true"
        app.launch()
    }

    func test_completeCheckout_happyPath() {
        CartPage(app: app)
            .assertItemCount(2)
            .tapCheckout()
            .fillAddress(street: "123 Main St", city: "Cupertino", zip: "95014")
            .tapContinue()
            .enterCard(number: "4242424242424242", exp: "12/28", cvv: "123")
            .tapPay()
            .assertOrderConfirmed()
    }

    func test_checkout_withInvalidZip_showsError() {
        CartPage(app: app)
            .tapCheckout()
            .fillAddress(street: "123 Main St", city: "Test", zip: "000")
            .tapContinue()

        XCTAssertTrue(
            app.staticTexts["shipping_zip_error"].waitForExistence(timeout: 3)
        )
    }
}
```

---

## Techniques Used

- **ST-01** (Clear Objective): Focused on generating reliable, maintainable UI tests
- **ST-02** (Structured Decomposition): Separated concerns into Page Objects, test data, and flow tests
- **RT-02** (Step-by-Step Reasoning): Sequential build from identifiers to pages to tests
- **DS-02** (Domain Expertise): XCUITest framework patterns, accessibility identifiers, iOS UI testing best practices

---

## Related Prompts

- [ios_test_strategy_design.md](ios_test_strategy_design.md) - Overall test strategy including UI test ratio
- [ios_unit_test_generation.md](ios_unit_test_generation.md) - Unit tests for logic that should not be UI-tested
- [ios_snapshot_testing.md](ios_snapshot_testing.md) - Visual regression testing as complement to UI tests
- [ios_ai_test_generation.md](ios_ai_test_generation.md) - AI-assisted test generation

---

## Customization Guide

| Aspect | How to Customize |
|--------|-----------------|
| **UI Framework** | For UIKit-only apps, add `accessibilityIdentifier` in `viewDidLoad` instead of SwiftUI modifiers |
| **Test Data** | Replace launch arguments with a local mock server (Swifter, Embassy) for complex API mocking |
| **Page Objects** | Add protocol conformance (`Verifiable`, `Navigable`) for consistent page behaviors |
| **Localization** | Query elements by `accessibilityIdentifier` only, never by displayed text strings |
| **Device Matrix** | Run tests across `iPhone SE`, `iPhone 15 Pro Max`, and `iPad` for size class coverage |
| **Parallel Execution** | Enable "Execute in parallel" in Xcode test plan for independent tests, keep flow tests sequential |
