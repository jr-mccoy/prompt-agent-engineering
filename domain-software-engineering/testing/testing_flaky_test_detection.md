---
title: "Flaky Test Detection and Resolution"
category: testing
description: "Identify, analyze, and fix flaky tests to improve test suite reliability"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
difficulty: intermediate
tags:
  - testing
  - flaky-tests
  - reliability
  - cicd
  - debugging
updated: "2026-03-19"
---

# Flaky Test Detection and Resolution

**Objective:** Identify, analyze, and fix flaky tests (tests that intermittently pass or fail without code changes) to improve test suite reliability and developer confidence.

**When to Use:** Use this prompt when experiencing inconsistent test results, investigating CI/CD failures that can't be reproduced locally, or when test suite reliability is causing deployment delays. Essential for maintaining high-quality automated testing.

**Instructions:**

1. **Identify Flaky Tests**
   - Review CI/CD test failure patterns over time
   - Look for tests that fail inconsistently (pass on retry)
   - Track test failure rates and patterns
   - Use test analytics tools to identify flakiness
   - Monitor tests that only fail in CI but pass locally

2. **Categorize Flakiness Causes**
   Common causes:
   - **Timing Issues**: Race conditions, insufficient waits, animations
   - **Test Isolation**: Shared state, database pollution, cache issues
   - **Environmental**: Network requests, system time, random data
   - **Concurrency**: Parallel test execution conflicts
   - **Resource Constraints**: Memory limits, CPU throttling in CI

3. **Analyze Flaky Test Patterns**
   - Document failure frequency and conditions
   - Identify common characteristics of flaky tests
   - Determine if failures are environment-specific (CI vs local)
   - Check for dependencies on external services
   - Review test execution order dependencies

4. **Fix Timing-Related Flakiness**
   - Replace arbitrary `sleep()` with explicit waits
   - Wait for specific conditions (element visible, API response)
   - Add retry logic for eventually consistent operations
   - Increase timeouts for slow operations
   - Handle animations and transitions properly

5. **Fix Test Isolation Issues**
   - Ensure proper test setup and teardown
   - Use unique test data for each test
   - Clear caches and reset state between tests
   - Avoid shared global state
   - Use database transactions or test containers

6. **Fix Environmental Flakiness**
   - Mock external API calls
   - Use fixed dates/times instead of Date.now()
   - Seed random number generators
   - Control test execution environment
   - Handle network instability

7. **Implement Flakiness Prevention**
   - Add flaky test detection to CI/CD
   - Quarantine known flaky tests
   - Track flakiness metrics over time
   - Set quality gates for test stability
   - Establish test reliability standards

8. **CRITICAL: Validate Flakiness Root Cause Before Fixing**
   - Confirm the test is actually flaky (not a real intermittent bug in production code)
   - Verify root cause through reproduction, not assumption
   - Check if the test is revealing actual race conditions in the code
   - **Confidence level** for each diagnosis:
     - **High Confidence:** Root cause reproduced consistently, fix verified over multiple runs
     - **Medium Confidence:** Root cause identified through pattern analysis, needs verification
     - **Low Confidence:** Root cause suspected but not confirmed, may mask real bugs

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Assume a failing test is flaky without investigating if it's catching a real bug
- Quarantine or skip tests without understanding why they fail
- Add arbitrary sleep/wait times as a "fix" without understanding the underlying timing issue
- Mark tests as flaky based on a single failure (may be transient environment issue)
- Disable retry logic that was intentionally added to handle eventual consistency
- Remove tests just because they're difficult to stabilize
- Assume local behavior matches CI behavior without verification

✅ **DO:**
- Run the test multiple times (10+) before classifying as flaky
- Investigate whether the flaky test is revealing a real production bug (race condition)
- Distinguish between test flakiness and infrastructure flakiness (CI runner issues)
- Keep a log of fixes and verify they actually reduce failure rate
- Consider that "flaky" test might be the only thing catching an intermittent production issue
- Document the root cause for each flaky test (not just the fix)
- Verify fixes by running the test many times in the same conditions that caused failures

**Expected Output:** A flaky test analysis and remediation plan including:
- List of identified flaky tests with failure rates
- Root cause analysis for each flaky test
- Categorization by flakiness type
- Specific fixes for each identified issue
- Code examples showing before/after improvements
- CI/CD configuration for flakiness detection
- Prevention strategies and best practices
- Flakiness tracking dashboard setup

**Example Output:**

```markdown
## Flaky Test Analysis Report

**Period**: Last 30 days
**Total Test Runs**: 2,847
**Flaky Tests Identified**: 12
**Most Common Cause**: Timing issues (58%)

---

### Flaky Test #1: User Login E2E Test

**Test**: `tests/e2e/auth.spec.ts - should log in user successfully`
**Failure Rate**: 23% (65 failures out of 283 runs)
**Pattern**: Fails primarily in CI, passes locally
**Root Cause**: Race condition - clicking submit before form validation completes
**Confidence**: High
- ✅ Reproduced locally by adding artificial delay to validation
- ✅ Fix verified over 50 runs with 0 failures
- ✅ Confirmed test is not catching a real bug (UI-only race condition)

**Current Implementation** (Flaky):
```javascript
test('should log in user successfully', async ({ page }) => {
  await page.goto('/login');

  await page.fill('[name="email"]', 'test@example.com');
  await page.fill('[name="password"]', 'password123');

  // ❌ Immediately clicks without waiting for validation
  await page.click('[data-testid="submit-button"]');

  // Sometimes button is disabled due to async validation
  await expect(page).toHaveURL('/dashboard');
});
```

**Fixed Implementation**:
```javascript
test('should log in user successfully', async ({ page }) => {
  await page.goto('/login');

  await page.fill('[name="email"]', 'test@example.com');
  await page.fill('[name="password"]', 'password123');

  // ✅ Wait for button to become enabled (validation complete)
  await page.waitForSelector('[data-testid="submit-button"]:not([disabled])');

  await page.click('[data-testid="submit-button"]');

  // ✅ Wait for navigation to complete
  await page.waitForURL('/dashboard');
  await page.waitForLoadState('networkidle');

  await expect(page).toHaveURL('/dashboard');
});
```

**Result**: 0 failures in 50 subsequent test runs

---

### Flaky Test #2: Product Search Results

**Test**: `tests/integration/search.test.ts - should return search results`
**Failure Rate**: 15% (42 failures out of 280 runs)
**Pattern**: Random failures, no consistent pattern
**Root Cause**: Test isolation - shared database state from previous tests
**Confidence**: High
- ✅ Reproduced by running tests in different orders
- ✅ Fix verified over 45 runs with 0 failures
- ✅ Not a production bug - test setup issue only

**Current Implementation** (Flaky):
```javascript
describe('Product Search', () => {
  beforeEach(async () => {
    // ❌ Creates products but doesn't clean up
    await Product.create({ name: 'Laptop', category: 'Electronics' });
  });

  it('should return search results', async () => {
    const results = await searchProducts('Laptop');
    expect(results).toHaveLength(1); // ❌ May be more if previous test created products
  });
});
```

**Fixed Implementation**:
```javascript
describe('Product Search', () => {
  beforeEach(async () => {
    // ✅ Clean database before each test
    await Product.deleteMany({});

    // ✅ Create test data
    await Product.create({ name: 'Laptop', category: 'Electronics' });
  });

  afterEach(async () => {
    // ✅ Clean up after test
    await Product.deleteMany({});
  });

  it('should return search results', async () => {
    const results = await searchProducts('Laptop');
    expect(results).toHaveLength(1);
    expect(results[0].name).toBe('Laptop');
  });
});
```

**Result**: 0 failures in 45 subsequent test runs

---

### Flaky Test #3: Date-Dependent Test

**Test**: `tests/unit/discount.test.ts - should apply early bird discount`
**Failure Rate**: 100% after midnight
**Pattern**: Fails at specific times
**Root Cause**: Test uses Date.now() which changes
**Confidence**: High
- ✅ Root cause obvious from code inspection
- ✅ Fix is standard best practice (mock time)
- ✅ Not masking a production bug

**Current Implementation** (Flaky):
```javascript
it('should apply early bird discount before 10 AM', () => {
  // ❌ Uses actual system time - fails after 10 AM
  const discount = getEarlyBirdDiscount();

  if (new Date().getHours() < 10) {
    expect(discount).toBe(0.15);
  } else {
    expect(discount).toBe(0);
  }
});
```

**Fixed Implementation**:
```javascript
it('should apply early bird discount before 10 AM', () => {
  // ✅ Mock the time
  const mockDate = new Date('2025-12-08T09:00:00Z');
  jest.useFakeTimers().setSystemTime(mockDate);

  const discount = getEarlyBirdDiscount();
  expect(discount).toBe(0.15);

  jest.useRealTimers();
});

it('should not apply discount after 10 AM', () => {
  // ✅ Test both scenarios with controlled time
  const mockDate = new Date('2025-12-08T11:00:00Z');
  jest.useFakeTimers().setSystemTime(mockDate);

  const discount = getEarlyBirdDiscount();
  expect(discount).toBe(0);

  jest.useRealTimers();
});
```

---

### Flakiness Analysis Validation Summary

| Test | Confidence | Is This Masking a Real Bug? | Verification Method |
|------|------------|----------------------------|---------------------|
| User Login E2E | High | No - UI timing only | Added validation delay, verified in production |
| Product Search | High | No - Test isolation issue | Ran tests in isolation, passed 100/100 |
| Date-Dependent | High | No - Standard time-mock issue | Obvious from code |

**Important Caveat**: One test originally classified as "flaky" was actually catching a real race condition in the checkout process. After investigation, we discovered:
- Test failure rate: 8%
- Production incident rate: ~0.5% of checkouts had duplicate orders
- **Conclusion**: Test was not flaky - it was correctly detecting an intermittent production bug
- **Action**: Fixed the production code, not the test

---

### Flakiness Prevention Strategies

**1. Explicit Waits Instead of Sleep**
```javascript
// ❌ Bad: Arbitrary timeout
await page.waitForTimeout(3000); // May be too short or too long

// ✅ Good: Wait for specific condition
await page.waitForSelector('[data-testid="results"]', { state: 'visible' });
```

**2. Deterministic Test Data**
```javascript
// ❌ Bad: Random data
const testEmail = `test${Math.random()}@example.com`;

// ✅ Good: Predictable data with unique identifiers
const testId = Date.now(); // Or use test-specific ID
const testEmail = `test-${testId}@example.com`;
```

**3. Proper Test Isolation**
```javascript
// ✅ Use database transactions
beforeEach(async () => {
  await db.beginTransaction();
});

afterEach(async () => {
  await db.rollback();
});
```

**4. Mock External Dependencies**
```javascript
// ✅ Mock API calls
beforeEach(() => {
  jest.spyOn(apiClient, 'get').mockResolvedValue({ data: mockData });
});
```

---

### CI/CD Flakiness Detection

```yaml
# .github/workflows/flaky-test-detection.yml
name: Flaky Test Detection

on:
  schedule:
    - cron: '0 2 * * *'  # Run nightly

jobs:
  detect-flaky-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Run tests 10 times
        run: |
          for i in {1..10}; do
            npm test -- --json --outputFile=test-results-$i.json || true
          done

      - name: Analyze flakiness
        run: node scripts/analyze-flakiness.js

      - name: Create issue for flaky tests
        if: failure()
        uses: actions/github-script@v6
        with:
          script: |
            // Create GitHub issue listing flaky tests
```

```javascript
// scripts/analyze-flakiness.js
const fs = require('fs');

const runs = 10;
const testResults = {};

// Parse all test run results
for (let i = 1; i <= runs; i++) {
  const results = JSON.parse(fs.readFileSync(`test-results-${i}.json`));

  results.testResults.forEach(suite => {
    suite.assertionResults.forEach(test => {
      const key = `${suite.name}::${test.title}`;

      if (!testResults[key]) {
        testResults[key] = { passes: 0, failures: 0 };
      }

      if (test.status === 'passed') {
        testResults[key].passes++;
      } else {
        testResults[key].failures++;
      }
    });
  });
}

// Identify flaky tests (passed sometimes, failed sometimes)
const flakyTests = [];

Object.entries(testResults).forEach(([test, results]) => {
  if (results.passes > 0 && results.failures > 0) {
    const flakeRate = (results.failures / runs * 100).toFixed(1);
    flakyTests.push({ test, flakeRate, ...results });
  }
});

// Report findings
if (flakyTests.length > 0) {
  console.log('Flaky tests detected:');
  flakyTests.forEach(t => {
    console.log(`- ${t.test}: ${t.flakeRate}% failure rate`);
  });
  process.exit(1);
} else {
  console.log('No flaky tests detected');
}
```
```

**Techniques Used:**
- ST-01, ST-02, RT-02, RT-05, ST-03, OC-04, TC-02

**Related Prompts:**
- testing_integration_test_design.md
- testing_e2e_test_scenario_creation.md
- testing_test_refactoring.md

**Customization Guide:**
- **For E2E Tests**: Focus on timing and wait strategies
- **For Unit Tests**: Emphasize test isolation and mocking
- **For Integration Tests**: Address database state and test containers
