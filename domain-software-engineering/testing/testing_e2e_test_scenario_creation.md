---
title: "End-to-End Test Scenario Creation"
category: testing
description: "Create comprehensive E2E test scenarios validating critical user journeys through the entire application stack"
techniques:
  - ST-01
  - ST-02
  - DT-01
  - RT-02
  - ST-03
difficulty: intermediate
tags:
  - testing
  - e2e-tests
  - user-journeys
  - automation
  - cypress
  - playwright
updated: "2026-03-19"
---

# End-to-End Test Scenario Creation

**Objective:** Create comprehensive end-to-end test scenarios that validate critical user journeys through the entire application stack, from UI to database.

**When to Use:** Use this prompt when you need to verify complete user workflows across the full application, including frontend UI, backend APIs, databases, and third-party integrations. Essential for web applications, mobile apps, and systems where user experience depends on multiple components working together.

**Instructions:**

1. **Identify Critical User Journeys**
   - Analyze the application to identify the most important user workflows
   - Prioritize based on business value, user frequency, and risk
   - Consider both happy path and alternative/error scenarios
   - Examples: user registration, checkout process, data import/export, report generation

2. **Map Complete User Flows**
   For each critical journey:
   - List every step from user's perspective (what they see and do)
   - Identify all pages, screens, or views involved
   - Document expected UI states and transitions
   - Note data that flows through the system
   - Include all interactions: clicks, form inputs, file uploads, etc.

3. **Design Test Scenarios**
   For each user journey, create:
   - **Preconditions**: Initial state, test data requirements, user roles
   - **Test Steps**: Detailed step-by-step actions with locators
   - **Assertions**: What to verify at each step (UI state, data, messages)
   - **Postconditions**: Expected final state, cleanup requirements
   - **Edge Cases**: Alternative paths, error conditions, boundary cases

4. **Select Appropriate E2E Testing Framework**
   Recommend framework based on application type:
   - **Web Applications**: Playwright, Cypress, Selenium WebDriver, TestCafe
   - **Mobile Apps**: Appium, Detox (React Native), XCTest (iOS), Espresso (Android)
   - **Desktop Applications**: Electron with Spectron, WinAppDriver, PyAutoGUI
   - **API-Only E2E**: Postman/Newman, REST Assured, Karate

5. **Implement Test Data Strategy**
   - Define test data setup approach (fixtures, factories, API seeding)
   - Plan for data isolation between test runs
   - Handle dynamic data (timestamps, IDs, external service responses)
   - Consider using test user accounts with specific permissions

6. **Design Page Object Model (POM) Structure**
   - Create page objects for reusable UI interactions
   - Define selectors using stable strategies (data-testid, role-based, etc.)
   - Encapsulate page-specific logic and waits
   - Promote maintainability and reduce duplication

7. **Handle Asynchronous Operations**
   - Add appropriate waits for dynamic content loading
   - Wait for API calls to complete
   - Handle animations and transitions
   - Verify loading states and spinners

8. **Plan for CI/CD Integration**
   - Configure headless browser execution
   - Set up video/screenshot capture for failures
   - Define test parallelization strategy
   - Establish failure reporting and notifications

9. **CRITICAL: Validate Test Scenarios Before Finalization**
   - Review each scenario for completeness (all steps, assertions, data)
   - Verify scenarios cover real user behavior, not just technical paths
   - Confirm assertions test actual user value, not implementation details
   - Check for appropriate wait strategies and error handling
   - **Confidence level** for each scenario:
     - **High Confidence:** Covers a documented user journey with clear business value
     - **Medium Confidence:** Covers likely user behavior but may need validation with stakeholders
     - **Low Confidence:** Speculative scenario that needs user research to confirm

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Create tests that are tightly coupled to implementation details (internal component names, specific DOM structures that may change)
- Write tests that break on minor UI changes (button text changes, element repositioning)
- Use fragile selectors (CSS classes used for styling, nth-child, positional selectors)
- Test framework/library behavior instead of your application behavior
- Create scenarios that test the same functionality multiple times redundantly
- Write assertions that pass even when the feature is broken (e.g., checking element exists without verifying content)
- Assume test data will always be in a specific state without setting it up

✅ **DO:**
- Use data-testid attributes or semantic roles for stable element selection
- Test user-observable outcomes, not internal state
- Verify the user can accomplish their goal, not just that code executed
- Create independent tests that don't rely on execution order
- Set up and tear down test data for each test to ensure isolation
- Include negative test cases (what happens when things go wrong)
- Validate that assertions would actually fail if the feature broke
- Prioritize testing critical user flows that impact business metrics

**Expected Output:** A comprehensive E2E testing strategy including:
- List of 5-10 critical user journeys to test
- Detailed test scenarios with step-by-step instructions
- Sample test code using recommended E2E framework
- Page Object Model examples for key pages
- Test data setup and management approach
- CI/CD pipeline configuration for E2E tests
- Best practices for test stability and maintainability

**Example Output:**

```markdown
## E2E Test Strategy for E-commerce Platform

### Critical User Journeys
| # | Journey | Priority | Confidence | Business Value |
|---|---------|----------|------------|----------------|
| 1 | User Registration and Email Verification | High | High | New user acquisition |
| 2 | Product Search and Add to Cart | High | High | Core shopping flow |
| 3 | Checkout with Payment Processing | Critical | High | Revenue generation |
| 4 | Order History and Tracking | Medium | Medium | Customer retention |
| 5 | Product Review Submission | Low | Medium | Social proof, SEO |

---

### Test Scenario: Complete Checkout Flow

**Journey**: Guest user browses products, adds items to cart, and completes purchase

**Framework**: Playwright (TypeScript)

**Preconditions**:
- Application is running and accessible
- Test products exist in database (SKU: TEST-001, TEST-002)
- Payment gateway is in test mode
- Email service is stubbed/mocked

**Test Steps**:

1. **Navigate to homepage**
   - Action: Visit base URL
   - Assert: Homepage loads, header and navigation visible

2. **Search for product**
   - Action: Enter "laptop" in search box, click search
   - Assert: Search results page displays, at least 1 product shown

3. **View product details**
   - Action: Click first product in results
   - Assert: Product detail page loads, price displayed, "Add to Cart" button visible

4. **Add product to cart**
   - Action: Click "Add to Cart" button
   - Assert: Cart badge updates to "1", success message appears

5. **Proceed to cart**
   - Action: Click cart icon in header
   - Assert: Cart page loads, product visible with correct price and quantity

6. **Update quantity**
   - Action: Change quantity to 2
   - Assert: Total price updates correctly, subtotal = unit price × 2

7. **Proceed to checkout**
   - Action: Click "Checkout" button
   - Assert: Checkout page loads, displays shipping form

8. **Fill shipping information**
   - Action: Enter name, email, address, phone
   - Assert: Form accepts inputs, no validation errors

9. **Select shipping method**
   - Action: Choose "Standard Shipping ($5.99)"
   - Assert: Shipping cost added to order total

10. **Enter payment information**
    - Action: Fill credit card details (test card: 4242424242424242)
    - Assert: Payment form accepts input, security indicators shown

11. **Complete purchase**
    - Action: Click "Place Order" button
    - Assert: Order confirmation page loads, order number displayed

12. **Verify order confirmation**
    - Assert: Confirmation includes order number, items, total, shipping address
    - Assert: Email confirmation sent (check test inbox)
    - Assert: Order saved in database with "confirmed" status

**Sample Test Code**:

```typescript
// tests/e2e/checkout-flow.spec.ts
import { test, expect } from '@playwright/test';
import { HomePage } from './pages/HomePage';
import { ProductPage } from './pages/ProductPage';
import { CartPage } from './pages/CartPage';
import { CheckoutPage } from './pages/CheckoutPage';

test.describe('Complete Checkout Flow', () => {
  test('guest user can search, add to cart, and complete purchase', async ({ page }) => {
    // Setup: Navigate to homepage
    const homePage = new HomePage(page);
    await homePage.goto();
    await expect(page).toHaveTitle(/E-commerce Store/);

    // Step 1: Search for product
    await homePage.searchFor('laptop');
    await expect(page.locator('[data-testid="search-results"]')).toBeVisible();
    const resultCount = await page.locator('[data-testid="product-card"]').count();
    expect(resultCount).toBeGreaterThan(0);

    // Step 2: View product details
    await page.locator('[data-testid="product-card"]').first().click();
    const productPage = new ProductPage(page);
    await expect(productPage.productTitle).toBeVisible();
    await expect(productPage.addToCartButton).toBeEnabled();

    // Step 3: Add to cart
    const productName = await productPage.productTitle.textContent();
    const productPrice = await productPage.price.textContent();
    await productPage.addToCart();

    // Verify cart badge updated
    await expect(page.locator('[data-testid="cart-badge"]')).toHaveText('1');
    await expect(page.locator('[data-testid="success-toast"]'))
      .toContainText('Added to cart');

    // Step 4: Go to cart
    await page.locator('[data-testid="cart-icon"]').click();
    const cartPage = new CartPage(page);
    await expect(cartPage.cartItems).toHaveCount(1);
    await expect(cartPage.cartItems.first()).toContainText(productName!);

    // Step 5: Update quantity
    await cartPage.updateQuantity(0, 2);
    await expect(cartPage.subtotal).toContainText(
      (parseFloat(productPrice!) * 2).toFixed(2)
    );

    // Step 6: Proceed to checkout
    await cartPage.proceedToCheckout();
    const checkoutPage = new CheckoutPage(page);
    await expect(checkoutPage.shippingForm).toBeVisible();

    // Step 7: Fill shipping information
    await checkoutPage.fillShippingInfo({
      firstName: 'John',
      lastName: 'Doe',
      email: 'john.doe@test.com',
      address: '123 Test Street',
      city: 'Test City',
      state: 'CA',
      zip: '90210',
      phone: '555-123-4567'
    });

    // Step 8: Select shipping method
    await checkoutPage.selectShippingMethod('standard');
    await expect(checkoutPage.shippingCost).toContainText('$5.99');

    // Step 9: Enter payment information
    await checkoutPage.fillPaymentInfo({
      cardNumber: '4242424242424242',
      expiry: '12/25',
      cvv: '123',
      name: 'John Doe'
    });

    // Step 10: Place order
    await checkoutPage.placeOrder();

    // Step 11: Verify order confirmation
    await expect(page).toHaveURL(/\/order-confirmation/);
    await expect(page.locator('[data-testid="order-number"]')).toBeVisible();

    const orderNumber = await page.locator('[data-testid="order-number"]').textContent();
    expect(orderNumber).toMatch(/^ORD-\d{8}$/);

    // Verify order details on confirmation page
    await expect(page.locator('[data-testid="order-items"]')).toContainText(productName!);
    await expect(page.locator('[data-testid="order-total"]')).toBeVisible();
    await expect(page.locator('[data-testid="shipping-address"]')).toContainText('123 Test Street');

    // Verify order in database (via API)
    const orderResponse = await page.request.get(`/api/orders/${orderNumber}`);
    expect(orderResponse.ok()).toBeTruthy();
    const order = await orderResponse.json();
    expect(order.status).toBe('confirmed');
    expect(order.items).toHaveLength(1);
  });

  test('should show error when payment fails', async ({ page }) => {
    // Test error scenario with failing payment
    // Use test card 4000000000000002 for declined payment
    // ...
  });
});
```

**Page Object Example**:

```typescript
// tests/e2e/pages/CheckoutPage.ts
import { Page, Locator } from '@playwright/test';

export class CheckoutPage {
  readonly page: Page;
  readonly shippingForm: Locator;
  readonly shippingCost: Locator;
  readonly placeOrderButton: Locator;

  constructor(page: Page) {
    this.page = page;
    this.shippingForm = page.locator('[data-testid="shipping-form"]');
    this.shippingCost = page.locator('[data-testid="shipping-cost"]');
    this.placeOrderButton = page.locator('[data-testid="place-order-button"]');
  }

  async fillShippingInfo(info: {
    firstName: string;
    lastName: string;
    email: string;
    address: string;
    city: string;
    state: string;
    zip: string;
    phone: string;
  }) {
    await this.page.fill('[name="firstName"]', info.firstName);
    await this.page.fill('[name="lastName"]', info.lastName);
    await this.page.fill('[name="email"]', info.email);
    await this.page.fill('[name="address"]', info.address);
    await this.page.fill('[name="city"]', info.city);
    await this.page.selectOption('[name="state"]', info.state);
    await this.page.fill('[name="zip"]', info.zip);
    await this.page.fill('[name="phone"]', info.phone);
  }

  async selectShippingMethod(method: 'standard' | 'express' | 'overnight') {
    await this.page.click(`[data-testid="shipping-${method}"]`);
  }

  async fillPaymentInfo(payment: {
    cardNumber: string;
    expiry: string;
    cvv: string;
    name: string;
  }) {
    // Wait for payment form to be ready
    await this.page.waitForSelector('[data-testid="payment-form"]');

    // May need to handle iframe for payment processor
    const paymentFrame = this.page.frameLocator('[data-testid="payment-iframe"]');
    await paymentFrame.locator('[name="cardNumber"]').fill(payment.cardNumber);
    await paymentFrame.locator('[name="expiry"]').fill(payment.expiry);
    await paymentFrame.locator('[name="cvv"]').fill(payment.cvv);
    await paymentFrame.locator('[name="cardName"]').fill(payment.name);
  }

  async placeOrder() {
    await this.placeOrderButton.click();
    // Wait for navigation to confirmation page
    await this.page.waitForURL(/\/order-confirmation/);
  }
}
```

**CI/CD Configuration**:

```yaml
# .github/workflows/e2e-tests.yml
name: E2E Tests
on:
  push:
    branches: [main, develop]
  pull_request:

jobs:
  e2e-tests:
    runs-on: ubuntu-latest
    timeout-minutes: 30

    steps:
      - uses: actions/checkout@v3

      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Install Playwright browsers
        run: npx playwright install --with-deps

      - name: Start application
        run: |
          npm run build
          npm run start &
          npx wait-on http://localhost:3000 -t 60000

      - name: Run E2E tests
        run: npm run test:e2e
        env:
          CI: true
          BASE_URL: http://localhost:3000

      - name: Upload test artifacts
        if: failure()
        uses: actions/upload-artifact@v3
        with:
          name: playwright-report
          path: playwright-report/
          retention-days: 7

      - name: Upload videos
        if: failure()
        uses: actions/upload-artifact@v3
        with:
          name: test-videos
          path: test-results/
          retention-days: 7
```

**Test Scenario Validation Checklist**:

Before finalizing, verify each scenario passes these quality checks:

| Check | Checkout Flow | Registration | Search |
|-------|---------------|--------------|--------|
| Tests user-visible outcome? | ✅ Yes | ✅ Yes | ✅ Yes |
| Uses stable selectors (data-testid)? | ✅ Yes | ✅ Yes | ✅ Yes |
| Independent of other tests? | ✅ Yes | ✅ Yes | ✅ Yes |
| Has data setup/teardown? | ✅ Yes | ✅ Yes | ✅ Yes |
| Includes error scenario? | ✅ Yes | ⚠️ Partial | ❌ Needs work |
| Assertions would fail if broken? | ✅ Yes | ✅ Yes | ✅ Yes |
| Business stakeholder validated? | ✅ Yes | ✅ Yes | ⚠️ Pending |

**Confidence Assessment**:
- Checkout Flow: **High Confidence** - Well-documented business process, payment integration thoroughly covered
- Registration: **High Confidence** - Standard flow, covers email verification edge cases
- Search: **Medium Confidence** - Needs validation that search algorithm behavior matches user expectations

**Best Practices**:
- Use data-testid attributes for stable selectors
- Implement retry logic for flaky operations
- Run tests in parallel for faster execution
- Capture screenshots/videos on failures
- Use test fixtures for consistent data
- Keep tests independent and isolated
- Mock external services when appropriate
```

**Techniques Used:**
- ST-01 (Clear Objective Statement)
- ST-02 (Sequential Step-by-Step Instructions)
- ST-07 (Prioritization and Ranking)
- RT-02 (Multi-Dimensional Analysis)
- ST-03 (Structured Output Templates)
- OC-04 (Comprehensive Example Outputs)
- TC-03 (Framework-Based Analysis)

**Related Prompts:**
- testing_integration_test_design.md - For testing component interactions
- testing_unit_test_generation.md - For component-level testing
- testing_visual_regression_testing.md - For UI visual consistency testing
- testing_accessibility_testing.md - For WCAG compliance in E2E flows
- testing_test_coverage_gap_analysis.md - To identify untested user journeys

**Customization Guide:**
- **For Mobile Apps**: Replace Playwright with Appium/Detox, adjust for native mobile gestures and navigation
- **For SPAs (React/Vue/Angular)**: Focus on client-side routing, state management, and component loading patterns
- **For Multi-Step Forms**: Add detailed form validation testing at each step, test save/resume functionality
- **For Real-Time Features**: Include WebSocket connection testing, live updates, and concurrent user scenarios
- **For PWAs**: Add offline functionality testing, service worker verification, and install flow testing
