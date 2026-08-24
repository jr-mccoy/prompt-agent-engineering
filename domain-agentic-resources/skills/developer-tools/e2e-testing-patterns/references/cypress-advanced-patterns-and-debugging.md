# E2E Testing Patterns — Cypress, Advanced Patterns, and Debugging

## Cypress Patterns

### Setup and Configuration

```typescript
// cypress.config.ts
import { defineConfig } from 'cypress';

export default defineConfig({
    e2e: {
        baseUrl: 'http://localhost:3000',
        viewportWidth: 1280,
        viewportHeight: 720,
        video: false,
        screenshotOnRunFailure: true,
        defaultCommandTimeout: 10000,
        requestTimeout: 10000,
        setupNodeEvents(on, config) {
            // Implement node event listeners
        },
    },
});
```

### Pattern 1: Custom Commands

```typescript
// cypress/support/commands.ts
declare global {
    namespace Cypress {
        interface Chainable {
            login(email: string, password: string): Chainable<void>;
            createUser(userData: UserData): Chainable<User>;
            dataCy(value: string): Chainable<JQuery<HTMLElement>>;
        }
    }
}

Cypress.Commands.add('login', (email: string, password: string) => {
    cy.visit('/login');
    cy.get('[data-testid="email"]').type(email);
    cy.get('[data-testid="password"]').type(password);
    cy.get('[data-testid="login-button"]').click();
    cy.url().should('include', '/dashboard');
});

Cypress.Commands.add('createUser', (userData: UserData) => {
    return cy.request('POST', '/api/users', userData)
        .its('body');
});

Cypress.Commands.add('dataCy', (value: string) => {
    return cy.get(`[data-cy="${value}"]`);
});

// Usage
cy.login('user@example.com', 'password');
cy.dataCy('submit-button').click();
```

### Pattern 2: Cypress Intercept

```typescript
// Mock API calls
cy.intercept('GET', '/api/users', {
    statusCode: 200,
    body: [
        { id: 1, name: 'John' },
        { id: 2, name: 'Jane' },
    ],
}).as('getUsers');

cy.visit('/users');
cy.wait('@getUsers');
cy.get('[data-testid="user-list"]').children().should('have.length', 2);

// Modify responses
cy.intercept('GET', '/api/users', (req) => {
    req.reply((res) => {
        // Modify response
        res.body.users = res.body.users.slice(0, 5);
        res.send();
    });
});

// Simulate slow network
cy.intercept('GET', '/api/data', (req) => {
    req.reply((res) => {
        res.delay(3000);  // 3 second delay
        res.send();
    });
});
```

---

## Advanced Patterns

### Pattern 1: Visual Regression Testing

```typescript
// With Playwright
import { test, expect } from '@playwright/test';

test('homepage looks correct', async ({ page }) => {
    await page.goto('/');
    await expect(page).toHaveScreenshot('homepage.png', {
        fullPage: true,
        maxDiffPixels: 100,
    });
});

test('button in all states', async ({ page }) => {
    await page.goto('/components');

    const button = page.getByRole('button', { name: 'Submit' });

    // Default state
    await expect(button).toHaveScreenshot('button-default.png');

    // Hover state
    await button.hover();
    await expect(button).toHaveScreenshot('button-hover.png');

    // Disabled state
    await button.evaluate(el => el.setAttribute('disabled', 'true'));
    await expect(button).toHaveScreenshot('button-disabled.png');
});
```

### Pattern 2: Parallel Testing with Sharding

```typescript
// playwright.config.ts
export default defineConfig({
    projects: [
        {
            name: 'shard-1',
            use: { ...devices['Desktop Chrome'] },
            grepInvert: /@slow/,
            shard: { current: 1, total: 4 },
        },
        {
            name: 'shard-2',
            use: { ...devices['Desktop Chrome'] },
            shard: { current: 2, total: 4 },
        },
        // ... more shards
    ],
});

// Run in CI
// npx playwright test --shard=1/4
// npx playwright test --shard=2/4
```

### Pattern 3: Accessibility Testing

```typescript
// Install: npm install @axe-core/playwright
import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test('page should not have accessibility violations', async ({ page }) => {
    await page.goto('/');

    const accessibilityScanResults = await new AxeBuilder({ page })
        .exclude('#third-party-widget')
        .analyze();

    expect(accessibilityScanResults.violations).toEqual([]);
});

test('form is accessible', async ({ page }) => {
    await page.goto('/signup');

    const results = await new AxeBuilder({ page })
        .include('form')
        .analyze();

    expect(results.violations).toEqual([]);
});
```

---

## Debugging Failing Tests

```typescript
// Playwright debugging
// 1. Run in headed mode
npx playwright test --headed

// 2. Run in debug mode
npx playwright test --debug

// 3. Use trace viewer
await page.screenshot({ path: 'screenshot.png' });
await page.video()?.saveAs('video.webm');

// 4. Add test.step for better reporting
test('checkout flow', async ({ page }) => {
    await test.step('Add item to cart', async () => {
        await page.goto('/products');
        await page.getByRole('button', { name: 'Add to Cart' }).click();
    });

    await test.step('Proceed to checkout', async () => {
        await page.goto('/cart');
        await page.getByRole('button', { name: 'Checkout' }).click();
    });
});

// 5. Inspect page state
await page.pause();  // Pauses execution, opens inspector
```

---

## Resources

- **references/playwright-best-practices.md**: Playwright-specific patterns
- **references/cypress-best-practices.md**: Cypress-specific patterns
- **references/flaky-test-debugging.md**: Debugging unreliable tests
- **assets/e2e-testing-checklist.md**: What to test with E2E
- **assets/selector-strategies.md**: Finding reliable selectors
- **scripts/test-analyzer.ts**: Analyze test flakiness and duration

---

## Verification

To validate your E2E test suite is production-ready:

1. **Flakiness**: Test suite passes >= 98% of the time on 10 consecutive CI runs
2. **Coverage**: All critical user journeys (login, checkout, signup) have E2E tests
3. **Speed**: Full E2E suite completes in < 10 minutes (parallelize if needed)
4. **Independence**: Tests pass in any order and don't depend on shared state
5. **Selectors**: All tests use stable selectors (data-testid, roles) not CSS/XPath
6. **CI Integration**: Tests run automatically on every PR and block merge on failure
7. **Debugging**: Failed tests produce screenshots, traces, or videos for triage

---

## Related Skills

- `qa-expert` - Complementary skill for QA processes, test strategy, bug tracking, and quality metrics. QA Expert defines *what* to test; this skill implements *how* to code it.
- `android-testing-patterns` - Android-specific E2E and integration testing
- `android-screenshot-testing` - Visual regression testing for Android
- `android-accessibility-testing` - Accessibility testing for Android
