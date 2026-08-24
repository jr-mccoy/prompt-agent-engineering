---
title: "Test Refactoring and Maintenance"
category: testing
description: "Improve test code quality and maintainability through refactoring and best practices"
techniques:
  - ST-01
  - ST-02
  - QA-01
  - QA-02
  - RT-02
  - ST-03
  - OC-04
difficulty: intermediate
tags:
  - testing
  - refactoring
  - maintenance
  - code-quality
  - best-practices
updated: "2026-01-25"
---

# Test Refactoring and Maintenance

**Objective:** Improve test code quality, maintainability, and readability by refactoring tests to follow best practices, reduce duplication, and enhance clarity.

**When to Use:** Use this prompt when tests are difficult to understand or maintain, test code has significant duplication, test execution is slow, or when establishing testing standards for a team. Essential for long-term test suite health.

**Instructions:**

1. **Identify Test Code Smells**
   - Duplicated test setup code
   - Hard-coded test data scattered throughout tests
   - Tests that are difficult to understand
   - Slow test execution
   - Brittle tests that break with minor changes
   - Tests testing multiple concerns
   - Lack of meaningful test names

2. **Apply Test Refactoring Patterns**
   - **Extract Setup Methods**: Move common setup to beforeEach/beforeAll
   - **Test Data Builders**: Create factories for test data
   - **Page Object Model**: Encapsulate UI interactions (E2E tests)
   - **Custom Matchers**: Create domain-specific assertions
   - **Test Helpers**: Extract common assertions and utilities

3. **Improve Test Readability**
   - Use descriptive test names (Arrange-Act-Assert pattern)
   - Follow Given-When-Then structure
   - Keep tests focused on single behavior
   - Add comments for complex setup or assertions
   - Use meaningful variable names

4. **Reduce Test Duplication**
   - Extract common setup into shared fixtures
   - Use parameterized tests for similar scenarios
   - Create reusable test utilities
   - Share test data across test suites

5. **Optimize Test Performance**
   - Reduce unnecessary database operations
   - Mock external dependencies
   - Run tests in parallel where possible
   - Use test containers for integration tests
   - Cache expensive setup operations

6. **Enhance Test Maintainability**
   - Keep tests close to the code they test
   - Update tests when requirements change
   - Remove obsolete tests
   - Document complex test scenarios
   - Establish test coding standards

7. **CRITICAL: Verify Refactoring Doesn't Break Test Intent**
   - Ensure refactored tests still verify the same behaviors
   - Check that extracted helpers don't hide important assertions
   - Verify that parameterized tests cover all original scenarios
   - Confirm that DRY refactoring doesn't reduce test clarity
   - Validate that test names still accurately describe what's being tested

8. **For each refactoring recommendation, provide:**
   - Current code smell or issue
   - Proposed refactoring pattern
   - **Confidence level** (High/Medium/Low) for improvement value
   - Potential risks or trade-offs
   - Before/after comparison

## False-Positive Prevention (MUST follow)

Test refactoring can introduce subtle issues. Follow these rules rigorously:

❌ **DON'T:**
- Over-abstract test setup to the point where test intent is unclear
- Remove "duplicate" assertions that actually test different aspects
- Extract helpers that hide the arrange-act-assert structure
- Combine unrelated tests into parameterized tests (obscures failures)
- Delete tests that seem redundant without verifying they test different paths
- Refactor tests purely for code metrics (coverage, line count)
- Change test names during refactoring without reviewing intent
- Remove comments that explain complex test scenarios

✅ **DO:**
- Preserve test readability as the primary goal
- Keep assertions visible in the test body (not buried in helpers)
- Ensure each test still has a clear, single purpose after refactoring
- Verify behavior coverage is maintained after combining tests
- Document why seemingly redundant tests exist before removing
- Use descriptive helper names that reveal intent
- Update test names to match refactored behavior
- Keep critical setup steps visible even if duplicated

## Confidence Levels for Refactoring Recommendations

Rate each refactoring recommendation:

- **High Confidence:** Clear code smell, well-established pattern, minimal risk of breaking tests
- **Medium Confidence:** Improvement likely but some judgment required, may affect test clarity
- **Low Confidence:** Trade-offs exist, benefits may not outweigh costs, needs team discussion

## Test Refactoring Decision Framework

| Code Smell | Refactoring Pattern | When to Apply | When to Skip |
|------------|-------------------|---------------|--------------|
| Duplicate setup | beforeEach/fixtures | >3 tests with same setup | Setup documents test context |
| Similar test cases | Parameterized tests | Tests differ only by input/output | Tests verify different behaviors |
| Complex assertions | Custom matchers | Same assertion pattern >3 times | Assertion is unique/specific |
| UI interaction duplication | Page Object Model | >2 tests with same UI flows | Simple, one-off interactions |
| Hard-coded data | Test Data Builders | Data used across test files | Data is test-specific constant |

## Validation Checklist

Before applying test refactoring:
- [ ] Current tests pass (establish baseline)
- [ ] All assertions are preserved (none removed or weakened)
- [ ] Test coverage is maintained or improved
- [ ] Each test still has clear, single purpose
- [ ] Refactored tests are still readable without jumping to helpers
- [ ] Test names accurately describe refactored behavior
- [ ] Team agrees on new patterns/conventions
- [ ] Documentation updated for new helpers/utilities

**Expected Output:**
- Analysis of test code quality issues with severity ratings
- Refactored test examples with before/after comparisons
- Reusable test utilities and helpers with documentation
- Performance improvement measurements
- Maintainability guidelines and team standards
- Risk assessment for each refactoring

**Example Output:**

```markdown
## Test Refactoring Report

### Before: Duplicated Setup Code

```javascript
describe('Order Processing', () => {
  it('should create order', async () => {
    // ❌ Duplicated setup
    const user = await User.create({ email: 'test@example.com' });
    const product = await Product.create({ name: 'Laptop', price: 999 });
    const cart = await Cart.create({ userId: user.id });
    await cart.addItem({ productId: product.id, quantity: 1 });

    const order = await createOrder(cart.id);
    expect(order.total).toBe(999);
  });

  it('should calculate tax', async () => {
    // ❌ Same setup repeated
    const user = await User.create({ email: 'test@example.com' });
    const product = await Product.create({ name: 'Laptop', price: 999 });
    const cart = await Cart.create({ userId: user.id });
    await cart.addItem({ productId: product.id, quantity: 1 });

    const order = await createOrder(cart.id);
    expect(order.tax).toBe(99.90);
  });
});
```

### After: Extracted Setup with Test Data Builder

```javascript
describe('Order Processing', () => {
  let testData;

  beforeEach(async () => {
    // ✅ Shared setup
    testData = await createTestOrder({
      userEmail: 'test@example.com',
      products: [{ name: 'Laptop', price: 999, quantity: 1 }],
    });
  });

  afterEach(async () => {
    await cleanupTestData(testData);
  });

  it('should create order with correct total', async () => {
    const order = await createOrder(testData.cart.id);
    expect(order.total).toBe(999);
  });

  it('should calculate 10% tax', async () => {
    const order = await createOrder(testData.cart.id);
    expect(order.tax).toBe(99.90);
  });
});

// Test Data Builder
async function createTestOrder({ userEmail, products }) {
  const user = await User.create({ email: userEmail });
  const cart = await Cart.create({ userId: user.id });

  const createdProducts = [];
  for (const p of products) {
    const product = await Product.create({ name: p.name, price: p.price });
    await cart.addItem({ productId: product.id, quantity: p.quantity });
    createdProducts.push(product);
  }

  return { user, cart, products: createdProducts };
}
```

### Refactoring Pattern: Custom Matchers

```javascript
// Before: Verbose assertions
expect(response.status).toBe(200);
expect(response.body).toHaveProperty('id');
expect(response.body).toHaveProperty('email');
expect(response.body.email).toBe('test@example.com');

// After: Custom matcher
expect(response).toBeSuccessfulUserResponse({
  email: 'test@example.com',
});

// Custom matcher implementation
expect.extend({
  toBeSuccessfulUserResponse(received, expected) {
    const pass =
      received.status === 200 &&
      received.body.id &&
      received.body.email === expected.email;

    return {
      pass,
      message: () => `Expected successful user response with email ${expected.email}`,
    };
  },
});
```

### Parameterized Tests

```javascript
// Before: Multiple similar tests
it('should validate email - missing @', () => {
  expect(validateEmail('testexample.com')).toBe(false);
});

it('should validate email - missing domain', () => {
  expect(validateEmail('test@')).toBe(false);
});

it('should validate email - empty', () => {
  expect(validateEmail('')).toBe(false);
});

// After: Parameterized test
const invalidEmails = [
  'testexample.com',
  'test@',
  '',
  '@example.com',
  'test@.com',
  'test..test@example.com',
];

describe.each(invalidEmails)('Email validation', (email) => {
  it(`should reject invalid email: ${email}`, () => {
    expect(validateEmail(email)).toBe(false);
  });
});
```
```

---

### Test Code Smell Analysis Summary

| Code Smell | Severity | Files Affected | Confidence | Recommended Pattern |
|------------|----------|----------------|------------|---------------------|
| Duplicate setup code | High | 15 test files | High | Extract to beforeEach + fixtures |
| Hard-coded test data | Medium | 23 test files | High | Test Data Builders |
| Verbose assertions | Medium | 8 test files | Medium | Custom matchers |
| Similar test cases | Medium | 12 test files | Medium | Parameterized tests |
| UI interaction duplication | High | 6 E2E test files | High | Page Object Model |
| Missing error messages | Low | All test files | High | Add assertion messages |

---

### Refactoring Pattern: Page Object Model for E2E Tests

**Before: Duplicated UI Interactions**

```javascript
// ❌ Multiple E2E tests with duplicated selectors and interactions
describe('Checkout Flow', () => {
  it('should complete checkout with credit card', async () => {
    await page.goto('/products/laptop');
    await page.click('[data-testid="add-to-cart"]');
    await page.waitForSelector('[data-testid="cart-notification"]');
    await page.click('[data-testid="go-to-cart"]');
    await page.click('[data-testid="proceed-to-checkout"]');
    await page.fill('[data-testid="email-input"]', 'test@example.com');
    await page.fill('[data-testid="card-number"]', '4111111111111111');
    await page.fill('[data-testid="card-expiry"]', '12/25');
    await page.fill('[data-testid="card-cvc"]', '123');
    await page.click('[data-testid="place-order"]');
    await expect(page.locator('[data-testid="order-confirmation"]')).toBeVisible();
  });

  it('should complete checkout with PayPal', async () => {
    // ❌ Same setup duplicated
    await page.goto('/products/laptop');
    await page.click('[data-testid="add-to-cart"]');
    await page.waitForSelector('[data-testid="cart-notification"]');
    await page.click('[data-testid="go-to-cart"]');
    await page.click('[data-testid="proceed-to-checkout"]');
    await page.fill('[data-testid="email-input"]', 'test@example.com');
    // Different payment method
    await page.click('[data-testid="paypal-button"]');
    // PayPal iframe interaction...
  });
});
```

**After: Page Object Model**

```javascript
// ✅ Page Objects encapsulate UI interactions
// tests/pages/ProductPage.ts
export class ProductPage {
  constructor(private page: Page) {}

  async goto(productSlug: string) {
    await this.page.goto(`/products/${productSlug}`);
  }

  async addToCart() {
    await this.page.click('[data-testid="add-to-cart"]');
    await this.page.waitForSelector('[data-testid="cart-notification"]');
  }

  async goToCart() {
    await this.page.click('[data-testid="go-to-cart"]');
    return new CartPage(this.page);
  }
}

// tests/pages/CartPage.ts
export class CartPage {
  constructor(private page: Page) {}

  async proceedToCheckout() {
    await this.page.click('[data-testid="proceed-to-checkout"]');
    return new CheckoutPage(this.page);
  }
}

// tests/pages/CheckoutPage.ts
export class CheckoutPage {
  constructor(private page: Page) {}

  async fillEmail(email: string) {
    await this.page.fill('[data-testid="email-input"]', email);
  }

  async payWithCreditCard(card: { number: string; expiry: string; cvc: string }) {
    await this.page.fill('[data-testid="card-number"]', card.number);
    await this.page.fill('[data-testid="card-expiry"]', card.expiry);
    await this.page.fill('[data-testid="card-cvc"]', card.cvc);
    await this.page.click('[data-testid="place-order"]');
  }

  async payWithPayPal() {
    await this.page.click('[data-testid="paypal-button"]');
    // Handle PayPal iframe...
  }

  async verifyOrderConfirmation() {
    await expect(this.page.locator('[data-testid="order-confirmation"]')).toBeVisible();
  }
}

// ✅ Clean, readable E2E tests
describe('Checkout Flow', () => {
  let productPage: ProductPage;

  beforeEach(async () => {
    productPage = new ProductPage(page);
  });

  it('should complete checkout with credit card', async () => {
    await productPage.goto('laptop');
    await productPage.addToCart();
    const cartPage = await productPage.goToCart();
    const checkoutPage = await cartPage.proceedToCheckout();

    await checkoutPage.fillEmail('test@example.com');
    await checkoutPage.payWithCreditCard({
      number: '4111111111111111',
      expiry: '12/25',
      cvc: '123',
    });
    await checkoutPage.verifyOrderConfirmation();
  });

  it('should complete checkout with PayPal', async () => {
    await productPage.goto('laptop');
    await productPage.addToCart();
    const cartPage = await productPage.goToCart();
    const checkoutPage = await cartPage.proceedToCheckout();

    await checkoutPage.fillEmail('test@example.com');
    await checkoutPage.payWithPayPal();
    await checkoutPage.verifyOrderConfirmation();
  });
});
```

**Benefits:**
- Selector changes only need updating in one place
- Tests read like user stories
- Easier to maintain as UI evolves
- Encourages consistent interactions

---

### Refactoring Pattern: Test Data Builders

**Before: Hard-coded Data**

```javascript
// ❌ Hard-coded data makes tests brittle and unclear
it('should calculate order total', () => {
  const order = {
    id: '12345',
    userId: 'user-1',
    items: [
      { productId: 'prod-1', name: 'Laptop', price: 999.99, quantity: 1 },
      { productId: 'prod-2', name: 'Mouse', price: 29.99, quantity: 2 },
    ],
    status: 'pending',
    createdAt: new Date('2025-01-01'),
  };

  expect(calculateTotal(order)).toBe(1059.97);
});
```

**After: Test Data Builder**

```javascript
// ✅ Fluent builder makes test intent clear
import { OrderBuilder, ItemBuilder } from './builders';

it('should calculate order total', () => {
  const order = new OrderBuilder()
    .withItem(new ItemBuilder().withPrice(999.99).withQuantity(1).build())
    .withItem(new ItemBuilder().withPrice(29.99).withQuantity(2).build())
    .build();

  expect(calculateTotal(order)).toBe(1059.97);
});

it('should apply 10% discount for orders over $500', () => {
  const order = new OrderBuilder()
    .withItem(new ItemBuilder().withPrice(600).build())
    .build();

  expect(calculateTotal(order)).toBe(540); // 600 - 10%
});

// builders/OrderBuilder.ts
export class OrderBuilder {
  private order: Partial<Order> = {
    id: `order-${Date.now()}`,
    userId: 'default-user',
    items: [],
    status: 'pending',
    createdAt: new Date(),
  };

  withId(id: string) { this.order.id = id; return this; }
  withUserId(userId: string) { this.order.userId = userId; return this; }
  withItem(item: OrderItem) { this.order.items!.push(item); return this; }
  withStatus(status: OrderStatus) { this.order.status = status; return this; }

  build(): Order {
    return this.order as Order;
  }
}
```

---

### Test Performance Improvements

| Optimization | Before | After | Improvement |
|--------------|--------|-------|-------------|
| Database setup per test → per suite | 45s | 12s | 73% faster |
| Real API calls → mocked responses | 120s | 8s | 93% faster |
| Sequential tests → parallel execution | 180s | 45s | 75% faster |
| Full page loads → component mounting | 60s | 15s | 75% faster |

---

### Test Maintainability Guidelines

1. **One Assertion Concept Per Test** (even if multiple `expect` statements)
2. **Test Names Should Complete the Sentence** "It should..."
3. **Arrange-Act-Assert Structure** with clear visual separation
4. **No Logic in Tests** - no conditionals, loops, or try-catch
5. **Test Behavior, Not Implementation** - focus on outcomes
6. **Keep Tests Fast** - < 100ms for unit, < 2s for integration
7. **Independent Tests** - no test should depend on another
8. **Descriptive Failure Messages** - include expected vs actual

---

### Refactoring Risk Assessment

| Refactoring | Risk Level | Mitigation |
|-------------|------------|------------|
| Extract beforeEach | Low | Verify all tests still pass |
| Parameterized tests | Medium | Review edge cases aren't lost |
| Custom matchers | Low | Test the matchers themselves |
| Page Objects | Medium | Maintain visibility of key steps |
| Remove "duplicate" tests | High | Trace to requirements first |
```

**Techniques Used:**
- **ST-01** (Clear Objective Statement): Clear purpose for test improvement
- **ST-02** (Sequential Step-by-Step Instructions): Structured refactoring process
- **RT-02** (Multi-Dimensional Analysis): Multiple code smell categories
- **ST-03** (Structured Output Templates): Tables and code comparisons
- **OC-04** (Comprehensive Example Outputs): Detailed before/after examples
- **QA-02** (Adversarial Thinking): False-positive prevention for refactoring

**Related Prompts:**
- `testing_coverage_gap_analysis.md` - Identify what needs testing before refactoring
- `testing_flaky_test_detection.md` - Fix flaky tests as part of maintenance
- `testing_mutation_testing.md` - Verify test quality after refactoring
- `quality_code_complexity_analysis.md` - Apply similar patterns to production code
