---
title: "Unit Test Generation and Enhancement"
category: testing
description: "Generate comprehensive unit tests following best practices and AAA pattern for code correctness"
techniques:
  - ST-01
  - ST-02
  - ST-03
  - DT-01
  - QA-02
difficulty: beginner
tags:
  - testing
  - unit-tests
  - tdd
  - quality-assurance
  - automation
updated: "2026-01-25"
---

# Unit Test Generation and Enhancement

**Objective:** Generate comprehensive unit tests for functions, methods, and classes to ensure code correctness, prevent regressions, and maintain high code quality through automated testing.

**When to Use:** Use this prompt when adding tests to new code, improving coverage of existing code, implementing TDD (Test-Driven Development), or when refactoring code that lacks adequate tests. Essential for maintaining code quality and preventing bugs.

**Instructions:**

1. **Analyze Code Structure and Behavior**
   - Identify all functions, methods, and classes requiring tests
   - Understand the purpose and expected behavior of each unit
   - Document input parameters, return values, and side effects
   - Identify dependencies and external interactions
   - Note error handling and edge cases

2. **Design Test Coverage Strategy**
   Test different categories:
   - **Happy Path**: Normal, expected inputs producing successful outputs
   - **Edge Cases**: Boundary values (min, max, zero, empty, null)
   - **Error Cases**: Invalid inputs, exception handling, error messages
   - **State Changes**: Verify object state transitions
   - **Side Effects**: Database writes, API calls, file operations

3. **Select Testing Framework**
   Choose appropriate framework for your language:
   - **JavaScript/TypeScript**: Jest, Vitest, Mocha + Chai
   - **Python**: pytest, unittest
   - **Java**: JUnit 5, TestNG
   - **Ruby**: RSpec, Minitest
   - **Go**: testing package, Testify
   - **C#**: xUnit, NUnit, MSTest

4. **Write Test Cases Following AAA Pattern**
   Structure tests using Arrange-Act-Assert:
   - **Arrange**: Set up test data and preconditions
   - **Act**: Execute the function/method being tested
   - **Assert**: Verify the expected outcome

5. **Cover Edge Cases and Boundaries**
   Test boundary conditions:
   - Empty collections ([], {}, "")
   - Null/undefined values
   - Zero and negative numbers
   - Maximum values and overflow
   - Special characters in strings
   - Invalid data types

6. **Test Error Handling**
   - Verify exceptions are thrown for invalid inputs
   - Check error messages are meaningful
   - Test error recovery mechanisms
   - Validate that errors don't leave system in invalid state

7. **Ensure Test Independence**
   - Tests should not depend on execution order
   - Each test should set up its own data
   - Clean up after tests (teardown)
   - Mock external dependencies
   - Avoid shared mutable state

8. **Use Descriptive Test Names**
   Follow naming patterns:
   - `should_[expected behavior]_when_[condition]`
   - `test_[function]_[scenario]_[expected result]`
   - `it('should return true when input is valid')`

9. **CRITICAL: Verify Test Quality Before Completion**
   - Run all tests and verify they pass
   - Intentionally break the code to verify tests fail (mutation testing mindset)
   - Check that assertions are specific, not overly broad
   - Ensure tests exercise actual behavior, not just implementation
   - **Confidence level:** Assign High/Medium/Low to test coverage claims

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Write tests that pass regardless of implementation (tautological tests)
- Assert only that "no error was thrown" without checking actual output
- Mock so heavily that you're testing the mock, not the code
- Use `toBeTruthy()` or loose assertions when specific values are expected
- Copy implementation logic into tests (testing the same bug twice)
- Skip testing edge cases because "they probably work"
- Assume 100% code coverage means 100% behavior coverage

✅ **DO:**
- Verify tests fail when behavior is broken (mutation testing validation)
- Use specific assertions: `expect(result).toBe(42)` not `expect(result).toBeTruthy()`
- Test observable behavior, not internal implementation details
- Include at least one test per error path documented in the function
- Verify mocks are called with expected arguments AND in expected order
- Document test coverage confidence: High (verified with mutations), Medium (comprehensive), Low (basic paths only)
- Cross-reference tests with requirements to ensure completeness

**Expected Output:** A comprehensive unit test suite including:
- Test cases covering happy paths, edge cases, and error scenarios
- Clear test organization and structure
- Descriptive test names explaining what is being tested
- Proper use of mocking for dependencies
- High code coverage (aim for 80%+ on critical code)
- Example output format for each test
- **Coverage confidence rating:** High/Medium/Low for each test category
- **Verification notes:** How tests were validated to catch real bugs

**Example Output:**

```markdown
## Unit Tests for Payment Calculator

**File to Test**: `src/utils/paymentCalculator.ts`

### Function: calculateTotalWithTax(amount, taxRate)

**Test Framework**: Jest (JavaScript/TypeScript)

```javascript
// src/utils/paymentCalculator.test.ts
import { calculateTotalWithTax, applyDiscount } from './paymentCalculator';

describe('calculateTotalWithTax', () => {
  // Happy path tests
  describe('Happy Path', () => {
    it('should calculate total with 10% tax correctly', () => {
      // Arrange
      const amount = 100;
      const taxRate = 0.10;

      // Act
      const result = calculateTotalWithTax(amount, taxRate);

      // Assert
      expect(result).toBe(110);
    });

    it('should calculate total with 0% tax', () => {
      expect(calculateTotalWithTax(100, 0)).toBe(100);
    });

    it('should handle decimal amounts', () => {
      expect(calculateTotalWithTax(99.99, 0.08)).toBeCloseTo(107.99, 2);
    });
  });

  // Edge cases
  describe('Edge Cases', () => {
    it('should handle $0.01 minimum amount', () => {
      expect(calculateTotalWithTax(0.01, 0.10)).toBeCloseTo(0.011, 3);
    });

    it('should handle very large amounts', () => {
      expect(calculateTotalWithTax(1000000, 0.10)).toBe(1100000);
    });

    it('should handle high tax rates', () => {
      expect(calculateTotalWithTax(100, 0.99)).toBe(199);
    });
  });

  // Error cases
  describe('Error Handling', () => {
    it('should throw error for negative amount', () => {
      expect(() => calculateTotalWithTax(-50, 0.10))
        .toThrow('Amount must be non-negative');
    });

    it('should throw error for negative tax rate', () => {
      expect(() => calculateTotalWithTax(100, -0.05))
        .toThrow('Tax rate must be between 0 and 1');
    });

    it('should throw error for tax rate > 1', () => {
      expect(() => calculateTotalWithTax(100, 1.5))
        .toThrow('Tax rate must be between 0 and 1');
    });

    it('should throw error for null amount', () => {
      expect(() => calculateTotalWithTax(null, 0.10))
        .toThrow('Amount must be a number');
    });

    it('should throw error for undefined tax rate', () => {
      expect(() => calculateTotalWithTax(100, undefined))
        .toThrow('Tax rate must be a number');
    });
  });
});

describe('applyDiscount', () => {
  it('should apply 20% discount correctly', () => {
    expect(applyDiscount(100, 0.20)).toBe(80);
  });

  it('should handle 100% discount (free)', () => {
    expect(applyDiscount(100, 1.0)).toBe(0);
  });

  it('should handle 0% discount', () => {
    expect(applyDiscount(100, 0)).toBe(100);
  });

  it('should round to 2 decimal places', () => {
    expect(applyDiscount(99.99, 0.15)).toBeCloseTo(84.99, 2);
  });

  it('should throw error for discount > 100%', () => {
    expect(() => applyDiscount(100, 1.5))
      .toThrow('Discount must be between 0 and 1');
  });
});
```

### Class Tests: ShoppingCart

```javascript
// src/models/ShoppingCart.test.ts
import { ShoppingCart } from './ShoppingCart';
import { Product } from './Product';

describe('ShoppingCart', () => {
  let cart;

  beforeEach(() => {
    // Arrange: Create fresh cart for each test
    cart = new ShoppingCart();
  });

  describe('addItem', () => {
    it('should add item to empty cart', () => {
      const product = new Product('Laptop', 999);

      cart.addItem(product, 1);

      expect(cart.items).toHaveLength(1);
      expect(cart.items[0].product).toBe(product);
      expect(cart.items[0].quantity).toBe(1);
    });

    it('should increment quantity when adding same item twice', () => {
      const product = new Product('Laptop', 999);

      cart.addItem(product, 1);
      cart.addItem(product, 2);

      expect(cart.items).toHaveLength(1);
      expect(cart.items[0].quantity).toBe(3);
    });

    it('should throw error when adding invalid quantity', () => {
      const product = new Product('Laptop', 999);

      expect(() => cart.addItem(product, 0))
        .toThrow('Quantity must be positive');
      expect(() => cart.addItem(product, -5))
        .toThrow('Quantity must be positive');
    });
  });

  describe('removeItem', () => {
    it('should remove item from cart', () => {
      const product = new Product('Laptop', 999);
      cart.addItem(product, 1);

      cart.removeItem(product.id);

      expect(cart.items).toHaveLength(0);
    });

    it('should do nothing when removing non-existent item', () => {
      expect(() => cart.removeItem('non-existent-id')).not.toThrow();
      expect(cart.items).toHaveLength(0);
    });
  });

  describe('getTotal', () => {
    it('should return 0 for empty cart', () => {
      expect(cart.getTotal()).toBe(0);
    });

    it('should calculate total for single item', () => {
      cart.addItem(new Product('Laptop', 999), 1);
      expect(cart.getTotal()).toBe(999);
    });

    it('should calculate total for multiple quantities', () => {
      cart.addItem(new Product('Laptop', 999), 2);
      expect(cart.getTotal()).toBe(1998);
    });

    it('should calculate total for multiple different items', () => {
      cart.addItem(new Product('Laptop', 999), 1);
      cart.addItem(new Product('Mouse', 29), 2);
      expect(cart.getTotal()).toBe(1057); // 999 + (29 * 2)
    });
  });

  describe('clear', () => {
    it('should remove all items from cart', () => {
      cart.addItem(new Product('Laptop', 999), 1);
      cart.addItem(new Product('Mouse', 29), 1);

      cart.clear();

      expect(cart.items).toHaveLength(0);
      expect(cart.getTotal()).toBe(0);
    });
  });
});
```

### Mocking External Dependencies

```javascript
// src/services/OrderService.test.ts
import { OrderService } from './OrderService';
import { PaymentGateway } from './PaymentGateway';
import { EmailService } from './EmailService';

// Mock dependencies
jest.mock('./PaymentGateway');
jest.mock('./EmailService');

describe('OrderService', () => {
  let orderService;
  let mockPaymentGateway;
  let mockEmailService;

  beforeEach(() => {
    // Create mock instances
    mockPaymentGateway = new PaymentGateway();
    mockEmailService = new EmailService();

    orderService = new OrderService(mockPaymentGateway, mockEmailService);
  });

  it('should create order and process payment', async () => {
    // Arrange
    const orderData = {
      userId: 'user123',
      items: [{ productId: 'prod1', quantity: 2 }],
      total: 100,
    };

    mockPaymentGateway.charge.mockResolvedValue({
      success: true,
      transactionId: 'txn123',
    });

    // Act
    const order = await orderService.createOrder(orderData);

    // Assert
    expect(order.status).toBe('confirmed');
    expect(mockPaymentGateway.charge).toHaveBeenCalledWith(100, 'user123');
    expect(mockEmailService.sendOrderConfirmation).toHaveBeenCalledWith(
      expect.objectContaining({
        userId: 'user123',
        total: 100,
      })
    );
  });

  it('should handle payment failure', async () => {
    // Arrange
    mockPaymentGateway.charge.mockRejectedValue(
      new Error('Insufficient funds')
    );

    // Act & Assert
    await expect(
      orderService.createOrder({ userId: 'user123', total: 100 })
    ).rejects.toThrow('Payment failed');

    // Verify email was not sent
    expect(mockEmailService.sendOrderConfirmation).not.toHaveBeenCalled();
  });
});
```

---

### Test Coverage Confidence Summary

| Category | Coverage | Confidence | Verification |
|----------|----------|------------|--------------|
| Happy Path | 100% | **High** | Mutation tested - tests fail when logic changes |
| Edge Cases | 90% | **High** | Boundary values verified with specific assertions |
| Error Handling | 85% | **Medium** | All documented errors tested; some implicit paths may exist |
| State Transitions | 80% | **Medium** | Key state changes covered; complex sequences need integration tests |
| Mock Interactions | 95% | **High** | Call verification includes argument matching |

**Verification Notes:**
- Tests validated by temporarily breaking implementation (e.g., changing `+` to `-` in calculateTotalWithTax)
- All assertions use specific values, no truthy/falsy checks
- Mock verification includes both call counts and argument matching
```

**Techniques Used:**
- ST-01 (Clear Objective Statement) - Defines purpose of generating comprehensive unit tests
- ST-02 (Sequential Step-by-Step Instructions) - Guides through analysis, design, and implementation
- RT-02 (Multi-Dimensional Analysis) - Covers happy paths, edge cases, errors, and state changes
- ST-03 (Structured Output Templates) - Provides consistent test organization patterns
- OC-04 (Comprehensive Example Outputs) - Demonstrates complete test suites with realistic code
- QA-02 (Adversarial Thinking) - False-positive prevention ensures tests catch real bugs

**Related Prompts:**
- testing_integration_test_design.md - For testing component interactions
- testing_coverage_gap_analysis.md - To identify areas needing tests
- testing_mutation_testing.md - To verify test quality
- testing_test_refactoring.md - To improve existing tests
- quality_code_review_checklist.md - For test quality standards

**Customization Guide:**
- **For TDD**: Write tests first before implementation, use red-green-refactor cycle
- **For Legacy Code**: Start with critical paths, add characterization tests, refactor incrementally
- **For Pure Functions**: Focus on input-output testing, extensive edge case coverage
- **For Stateful Classes**: Test state transitions, verify object behavior over time
- **For Async Code**: Use async/await patterns, test promise resolution/rejection, handle timeouts