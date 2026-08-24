---
title: "Playwright E2E Testing for Frontend"
category: frontend-development/testing
description: "Comprehensive Playwright end-to-end testing patterns for frontend applications including page objects, test organization, and CI integration"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - OC-01
  - QA-02
difficulty: intermediate
tags:
  - testing
  - playwright
  - e2e
  - end-to-end
  - automation
  - cross-browser
updated: "2026-01-29"
related_prompts:
  - domain-frontend-development/testing/frontend_testing_jest.md
  - domain-frontend-development/react/frontend_react_testing.md
  - domain-software-engineering/testing/testing_e2e_test_scenario_creation.md
---

# Playwright E2E Testing for Frontend

**Objective:** Design and implement comprehensive end-to-end tests with Playwright for frontend applications, covering critical user flows, cross-browser testing, and CI/CD integration.

**When to Use:**
- Use when: Testing critical user journeys (checkout, auth, etc.)
- Use when: Need cross-browser compatibility testing
- Use when: Testing complex interactions that unit tests can't cover
- Use when: Establishing regression test suite
- Don't use when: Unit testing individual components (use Jest/Vitest)

## Instructions

1. **Set Up Playwright**
   - Configure browsers and devices
   - Set up base URL and authentication
   - Configure retries and timeouts
   - Set up reporters and artifacts

2. **Design Test Architecture**
   - Page Object Model for maintainability
   - Fixture patterns for reusable setup
   - Test data management
   - Environment configuration

3. **Write Effective Tests**
   - Focus on user-visible behavior
   - Use resilient selectors
   - Handle async operations properly
   - Implement proper assertions

4. **Handle Test Reliability**
   - Avoid flaky tests
   - Use proper waits (not timeouts)
   - Isolate test data
   - Handle dynamic content

5. **CRITICAL: Maintain Test Quality**
   - Tests should catch real regressions
   - Balance coverage with execution time
   - Monitor and fix flaky tests immediately
   - **Confidence level** for tests:
     - **High Confidence**: Stable, catches regressions
     - **Medium Confidence**: Works but occasionally flaky
     - **Low Confidence**: Needs refactoring

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Use arbitrary sleep/timeout waits
- Test third-party services directly
- Create tests that depend on each other
- Use brittle selectors (nth-child, complex CSS)
- Ignore flaky tests
- Create slow test suites that never run

✅ **DO:**
- Use Playwright's auto-waiting
- Mock external APIs when needed
- Isolate tests with fresh data
- Use data-testid or accessible selectors
- Fix flaky tests immediately
- Keep test suites under 10 minutes

## Expected Output

Playwright testing guide including:
- Configuration recommendations
- Page Object patterns
- Test organization
- CI/CD integration
- Debugging strategies

## Example Output

```markdown
## Playwright E2E Testing Guide

### Playwright Configuration

```typescript
// playwright.config.ts
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests/e2e',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: [
    ['list'],
    ['html', { open: 'never' }],
    ['json', { outputFile: 'test-results/results.json' }],
  ],

  use: {
    baseURL: process.env.BASE_URL || 'http://localhost:3000',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
    video: 'on-first-retry',
  },

  projects: [
    // Desktop browsers
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
    {
      name: 'firefox',
      use: { ...devices['Desktop Firefox'] },
    },
    {
      name: 'webkit',
      use: { ...devices['Desktop Safari'] },
    },

    // Mobile browsers
    {
      name: 'Mobile Chrome',
      use: { ...devices['Pixel 5'] },
    },
    {
      name: 'Mobile Safari',
      use: { ...devices['iPhone 12'] },
    },
  ],

  webServer: {
    command: 'npm run dev',
    url: 'http://localhost:3000',
    reuseExistingServer: !process.env.CI,
    timeout: 120000,
  },
});
```

---

### Page Object Model

#### Base Page

```typescript
// tests/e2e/pages/BasePage.ts
import { Page, Locator } from '@playwright/test';

export abstract class BasePage {
  readonly page: Page;

  constructor(page: Page) {
    this.page = page;
  }

  async navigate(path: string = ''): Promise<void> {
    await this.page.goto(path);
  }

  async waitForPageLoad(): Promise<void> {
    await this.page.waitForLoadState('networkidle');
  }

  // Common elements
  get header(): Locator {
    return this.page.locator('header');
  }

  get footer(): Locator {
    return this.page.locator('footer');
  }

  // Common actions
  async clickLink(text: string): Promise<void> {
    await this.page.getByRole('link', { name: text }).click();
  }

  async clickButton(text: string): Promise<void> {
    await this.page.getByRole('button', { name: text }).click();
  }
}
```

#### Login Page

```typescript
// tests/e2e/pages/LoginPage.ts
import { Page, Locator, expect } from '@playwright/test';
import { BasePage } from './BasePage';

export class LoginPage extends BasePage {
  readonly emailInput: Locator;
  readonly passwordInput: Locator;
  readonly submitButton: Locator;
  readonly errorMessage: Locator;

  constructor(page: Page) {
    super(page);
    this.emailInput = page.getByLabel('Email');
    this.passwordInput = page.getByLabel('Password');
    this.submitButton = page.getByRole('button', { name: 'Sign in' });
    this.errorMessage = page.getByRole('alert');
  }

  async navigate(): Promise<void> {
    await super.navigate('/login');
  }

  async login(email: string, password: string): Promise<void> {
    await this.emailInput.fill(email);
    await this.passwordInput.fill(password);
    await this.submitButton.click();
  }

  async expectError(message: string): Promise<void> {
    await expect(this.errorMessage).toContainText(message);
  }

  async expectLoggedIn(): Promise<void> {
    await expect(this.page).toHaveURL(/\/dashboard/);
  }
}
```

#### Product Page

```typescript
// tests/e2e/pages/ProductPage.ts
import { Page, Locator, expect } from '@playwright/test';
import { BasePage } from './BasePage';

export class ProductPage extends BasePage {
  readonly productTitle: Locator;
  readonly price: Locator;
  readonly addToCartButton: Locator;
  readonly quantityInput: Locator;
  readonly sizeSelector: Locator;
  readonly cartNotification: Locator;

  constructor(page: Page) {
    super(page);
    this.productTitle = page.getByRole('heading', { level: 1 });
    this.price = page.getByTestId('product-price');
    this.addToCartButton = page.getByRole('button', { name: 'Add to cart' });
    this.quantityInput = page.getByLabel('Quantity');
    this.sizeSelector = page.getByLabel('Size');
    this.cartNotification = page.getByRole('status');
  }

  async navigate(productId: string): Promise<void> {
    await super.navigate(`/products/${productId}`);
  }

  async selectSize(size: string): Promise<void> {
    await this.sizeSelector.selectOption(size);
  }

  async setQuantity(quantity: number): Promise<void> {
    await this.quantityInput.fill(quantity.toString());
  }

  async addToCart(): Promise<void> {
    await this.addToCartButton.click();
  }

  async expectAddedToCart(): Promise<void> {
    await expect(this.cartNotification).toContainText('Added to cart');
  }

  async getPrice(): Promise<string> {
    return await this.price.textContent() || '';
  }
}
```

#### Cart Page

```typescript
// tests/e2e/pages/CartPage.ts
import { Page, Locator, expect } from '@playwright/test';
import { BasePage } from './BasePage';

export class CartPage extends BasePage {
  readonly cartItems: Locator;
  readonly subtotal: Locator;
  readonly checkoutButton: Locator;
  readonly emptyCartMessage: Locator;

  constructor(page: Page) {
    super(page);
    this.cartItems = page.getByTestId('cart-item');
    this.subtotal = page.getByTestId('cart-subtotal');
    this.checkoutButton = page.getByRole('button', { name: 'Checkout' });
    this.emptyCartMessage = page.getByText('Your cart is empty');
  }

  async navigate(): Promise<void> {
    await super.navigate('/cart');
  }

  async getItemCount(): Promise<number> {
    return await this.cartItems.count();
  }

  async removeItem(index: number): Promise<void> {
    await this.cartItems
      .nth(index)
      .getByRole('button', { name: 'Remove' })
      .click();
  }

  async updateQuantity(index: number, quantity: number): Promise<void> {
    await this.cartItems
      .nth(index)
      .getByLabel('Quantity')
      .fill(quantity.toString());
  }

  async proceedToCheckout(): Promise<void> {
    await this.checkoutButton.click();
  }

  async expectEmpty(): Promise<void> {
    await expect(this.emptyCartMessage).toBeVisible();
  }
}
```

---

### Fixtures

```typescript
// tests/e2e/fixtures/index.ts
import { test as base, expect } from '@playwright/test';
import { LoginPage } from '../pages/LoginPage';
import { ProductPage } from '../pages/ProductPage';
import { CartPage } from '../pages/CartPage';
import { CheckoutPage } from '../pages/CheckoutPage';

// Test user types
export interface TestUser {
  email: string;
  password: string;
}

// Extend base test with fixtures
export const test = base.extend<{
  loginPage: LoginPage;
  productPage: ProductPage;
  cartPage: CartPage;
  checkoutPage: CheckoutPage;
  testUser: TestUser;
  authenticatedPage: void;
}>({
  // Page fixtures
  loginPage: async ({ page }, use) => {
    await use(new LoginPage(page));
  },

  productPage: async ({ page }, use) => {
    await use(new ProductPage(page));
  },

  cartPage: async ({ page }, use) => {
    await use(new CartPage(page));
  },

  checkoutPage: async ({ page }, use) => {
    await use(new CheckoutPage(page));
  },

  // Test data fixtures
  testUser: async ({}, use) => {
    // Create unique user for test isolation
    const user = await createTestUser();
    await use(user);
    // Cleanup after test
    await deleteTestUser(user.email);
  },

  // Authentication fixture
  authenticatedPage: async ({ page, testUser }, use) => {
    // Login before test
    const loginPage = new LoginPage(page);
    await loginPage.navigate();
    await loginPage.login(testUser.email, testUser.password);
    await loginPage.expectLoggedIn();

    await use();

    // Logout after test
    await page.goto('/logout');
  },
});

export { expect };
```

---

### Test Examples

#### Authentication Flow

```typescript
// tests/e2e/specs/auth.spec.ts
import { test, expect } from '../fixtures';

test.describe('Authentication', () => {
  test('should login with valid credentials', async ({ loginPage, testUser }) => {
    await loginPage.navigate();
    await loginPage.login(testUser.email, testUser.password);
    await loginPage.expectLoggedIn();
  });

  test('should show error for invalid credentials', async ({ loginPage }) => {
    await loginPage.navigate();
    await loginPage.login('invalid@example.com', 'wrongpassword');
    await loginPage.expectError('Invalid email or password');
  });

  test('should redirect to login when accessing protected page', async ({ page }) => {
    await page.goto('/dashboard');
    await expect(page).toHaveURL(/\/login/);
  });

  test('should persist login across pages', async ({
    page,
    authenticatedPage,
  }) => {
    // authenticatedPage fixture already logged in
    await page.goto('/dashboard');
    await expect(page.getByRole('heading')).toContainText('Dashboard');

    await page.goto('/profile');
    await expect(page.getByRole('heading')).toContainText('Profile');
  });
});
```

#### E-commerce Purchase Flow

```typescript
// tests/e2e/specs/purchase.spec.ts
import { test, expect } from '../fixtures';

test.describe('Purchase Flow', () => {
  test('should complete full purchase', async ({
    page,
    productPage,
    cartPage,
    checkoutPage,
    authenticatedPage,
  }) => {
    // Browse to product
    await productPage.navigate('product-123');
    await expect(productPage.productTitle).toContainText('Blue T-Shirt');

    // Add to cart
    await productPage.selectSize('M');
    await productPage.setQuantity(2);
    await productPage.addToCart();
    await productPage.expectAddedToCart();

    // View cart
    await cartPage.navigate();
    expect(await cartPage.getItemCount()).toBe(1);

    // Checkout
    await cartPage.proceedToCheckout();

    // Fill shipping
    await checkoutPage.fillShipping({
      firstName: 'John',
      lastName: 'Doe',
      address: '123 Main St',
      city: 'New York',
      zip: '10001',
      country: 'US',
    });

    // Fill payment
    await checkoutPage.fillPayment({
      cardNumber: '4242424242424242',
      expiry: '12/25',
      cvc: '123',
    });

    // Complete order
    await checkoutPage.placeOrder();
    await checkoutPage.expectOrderConfirmation();
  });

  test('should update cart quantity', async ({
    productPage,
    cartPage,
    authenticatedPage,
  }) => {
    // Add product
    await productPage.navigate('product-123');
    await productPage.addToCart();

    // Update quantity in cart
    await cartPage.navigate();
    await cartPage.updateQuantity(0, 3);

    // Verify subtotal updated
    await expect(cartPage.subtotal).toContainText('$89.97');
  });

  test('should remove item from cart', async ({
    productPage,
    cartPage,
    authenticatedPage,
  }) => {
    // Add product
    await productPage.navigate('product-123');
    await productPage.addToCart();

    // Remove from cart
    await cartPage.navigate();
    await cartPage.removeItem(0);

    // Verify empty
    await cartPage.expectEmpty();
  });
});
```

#### Search and Filter

```typescript
// tests/e2e/specs/search.spec.ts
import { test, expect } from '../fixtures';

test.describe('Search and Filter', () => {
  test('should search for products', async ({ page }) => {
    await page.goto('/');

    // Search
    await page.getByRole('searchbox').fill('blue shirt');
    await page.keyboard.press('Enter');

    // Verify results
    await expect(page).toHaveURL(/search\?q=blue\+shirt/);
    await expect(page.getByTestId('search-results')).toBeVisible();

    const results = page.getByTestId('product-card');
    expect(await results.count()).toBeGreaterThan(0);
  });

  test('should filter by category', async ({ page }) => {
    await page.goto('/products');

    // Apply filter
    await page.getByRole('button', { name: 'Category' }).click();
    await page.getByRole('checkbox', { name: 'T-Shirts' }).check();

    // Wait for filter to apply
    await page.waitForURL(/category=t-shirts/);

    // Verify filtered results
    const products = page.getByTestId('product-card');
    for (const product of await products.all()) {
      await expect(product).toContainText(/t-shirt/i);
    }
  });

  test('should sort by price', async ({ page }) => {
    await page.goto('/products');

    // Sort
    await page.getByLabel('Sort by').selectOption('price-low');
    await page.waitForURL(/sort=price-low/);

    // Verify sorted
    const prices = await page.getByTestId('product-price').allTextContents();
    const priceValues = prices.map(p => parseFloat(p.replace('$', '')));

    for (let i = 1; i < priceValues.length; i++) {
      expect(priceValues[i]).toBeGreaterThanOrEqual(priceValues[i - 1]);
    }
  });
});
```

---

### API Mocking

```typescript
// tests/e2e/specs/with-mocks.spec.ts
import { test, expect } from '../fixtures';

test.describe('with API mocks', () => {
  test('should handle API error gracefully', async ({ page }) => {
    // Mock API to return error
    await page.route('/api/products', route => {
      route.fulfill({
        status: 500,
        body: JSON.stringify({ error: 'Server error' }),
      });
    });

    await page.goto('/products');

    await expect(page.getByRole('alert')).toContainText(
      'Unable to load products'
    );
    await expect(page.getByRole('button', { name: 'Retry' })).toBeVisible();
  });

  test('should show loading state', async ({ page }) => {
    // Delay API response
    await page.route('/api/products', async route => {
      await new Promise(r => setTimeout(r, 2000));
      await route.fulfill({
        status: 200,
        body: JSON.stringify({ products: [] }),
      });
    });

    await page.goto('/products');

    // Should show loading initially
    await expect(page.getByTestId('loading-skeleton')).toBeVisible();

    // Should show content after load
    await expect(page.getByTestId('loading-skeleton')).not.toBeVisible({
      timeout: 5000,
    });
  });

  test('should display mock data', async ({ page }) => {
    const mockProducts = [
      { id: '1', name: 'Test Product', price: 29.99 },
      { id: '2', name: 'Another Product', price: 49.99 },
    ];

    await page.route('/api/products', route => {
      route.fulfill({
        status: 200,
        body: JSON.stringify({ products: mockProducts }),
      });
    });

    await page.goto('/products');

    await expect(page.getByText('Test Product')).toBeVisible();
    await expect(page.getByText('Another Product')).toBeVisible();
  });
});
```

---

### Visual Regression Testing

```typescript
// tests/e2e/specs/visual.spec.ts
import { test, expect } from '@playwright/test';

test.describe('Visual Regression', () => {
  test('homepage matches snapshot', async ({ page }) => {
    await page.goto('/');
    await page.waitForLoadState('networkidle');

    // Hide dynamic content
    await page.evaluate(() => {
      document.querySelectorAll('[data-dynamic]').forEach(el => {
        (el as HTMLElement).style.visibility = 'hidden';
      });
    });

    await expect(page).toHaveScreenshot('homepage.png', {
      fullPage: true,
      maxDiffPixels: 100,
    });
  });

  test('product card matches snapshot', async ({ page }) => {
    await page.goto('/products');

    const productCard = page.getByTestId('product-card').first();
    await expect(productCard).toHaveScreenshot('product-card.png');
  });

  test('mobile navigation matches snapshot', async ({ page }) => {
    await page.setViewportSize({ width: 375, height: 667 });
    await page.goto('/');

    // Open mobile menu
    await page.getByRole('button', { name: 'Menu' }).click();

    await expect(page.getByRole('navigation')).toHaveScreenshot(
      'mobile-nav.png'
    );
  });
});
```

---

### CI/CD Integration

```yaml
# .github/workflows/playwright.yml
name: Playwright Tests

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    timeout-minutes: 60
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Install Playwright Browsers
        run: npx playwright install --with-deps

      - name: Build application
        run: npm run build

      - name: Run Playwright tests
        run: npx playwright test
        env:
          BASE_URL: http://localhost:3000

      - uses: actions/upload-artifact@v4
        if: always()
        with:
          name: playwright-report
          path: playwright-report/
          retention-days: 30

      - uses: actions/upload-artifact@v4
        if: failure()
        with:
          name: test-results
          path: test-results/
          retention-days: 7
```

---

### Debugging

```typescript
// Debug mode
test('debug example', async ({ page }) => {
  await page.goto('/');

  // Pause for manual inspection
  await page.pause();

  // Continue test
  await page.click('button');
});

// Trace viewer (run with --trace on)
// npx playwright test --trace on
// npx playwright show-trace trace.zip

// Slow down for observation
test.use({ launchOptions: { slowMo: 500 } });

// Take screenshot at specific point
await page.screenshot({ path: 'debug-screenshot.png' });

// Log page content
console.log(await page.content());

// Enable verbose logging
DEBUG=pw:api npx playwright test
```

---

### Best Practices Summary

| Practice | Do | Don't |
|----------|-----|--------|
| Selectors | Use `getByRole`, `getByLabel`, `getByTestId` | Use CSS selectors, XPath |
| Waits | Use auto-waiting, `waitFor` | Use `page.waitForTimeout` |
| Data | Isolate test data, clean up | Share data between tests |
| Assertions | Use `expect` with specific matchers | Use `.toBeTruthy()` generically |
| Structure | Page Object Model | Inline selectors |
| Speed | Parallelize, minimize setup | Run serially without reason |
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Focused on Playwright E2E testing
- **ST-02 (Structured Sequential Instructions):** Pattern-by-pattern guide
- **RT-02 (Multi-Dimensional Analysis):** Multiple testing scenarios
- **OC-01 (Output Format Templates):** Clear code examples
- **QA-02 (Adversarial Stress-Test):** Anti-patterns highlighted

## Related Prompts

- [frontend_testing_jest.md](frontend_testing_jest.md) - Unit testing
- [frontend_react_testing.md](../react/frontend_react_testing.md) - React component testing
- [testing_e2e_test_scenario_creation.md](../../domain-software-engineering/testing/testing_e2e_test_scenario_creation.md) - General E2E patterns

## Customization Guide

- **For Cypress Migration**: Show equivalent patterns and migration path
- **For Mobile Testing**: Emphasize device emulation and touch gestures
- **For API Testing**: Include Playwright API testing capabilities
- **For Accessibility**: Combine with axe-playwright for a11y testing
