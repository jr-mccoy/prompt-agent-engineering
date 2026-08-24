---
title: "Test Coverage Gap Analysis"
category: testing
description: "Analyze test suites to identify coverage gaps, untested scenarios, and areas of risk"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - QA-01
difficulty: intermediate
tags:
  - testing
  - coverage
  - quality-assurance
  - code-review
  - risk-assessment
updated: "2026-03-19"
---

# Test Coverage Gap Analysis

**Objective:** Analyze existing test suite to identify gaps in code coverage, untested scenarios, missing edge cases, and areas of risk that lack adequate testing.

**When to Use:** Use this prompt when you need to audit test quality, improve test coverage, prepare for production releases, or investigate areas with frequent bugs. Essential during code reviews, before major releases, or when establishing testing baselines for legacy code.

**Instructions:**

1. **Analyze Current Test Coverage Metrics**
   - Collect line coverage, branch coverage, and function coverage percentages
   - Identify files and modules with low or zero coverage
   - Review coverage trends over time
   - Use coverage tools: Istanbul/nyc (JavaScript), Coverage.py (Python), JaCoCo (Java), SimpleCov (Ruby)

2. **Identify Untested Code Paths**
   - Find functions and methods without any test coverage
   - Locate conditional branches (if/else, switch) that aren't tested
   - Identify exception handling code that lacks error scenario tests
   - Find edge cases and boundary conditions without tests
   - Look for untested integration points with external services

3. **Assess Test Quality Beyond Metrics**
   Coverage metrics alone don't guarantee quality. Evaluate:
   - **Assertion Quality**: Do tests actually verify behavior or just execute code?
   - **Edge Case Coverage**: Are boundary conditions tested (null, empty, max values)?
   - **Error Scenarios**: Are failure paths and exceptions tested?
   - **Integration Coverage**: Are component interactions tested?
   - **Data Variation**: Do tests cover different input types and combinations?

4. **Categorize Coverage Gaps by Risk**
   Prioritize gaps based on:
   - **Critical**: Business-critical features, payment/auth/security logic
   - **High**: Frequently used features, complex algorithms, data transformations
   - **Medium**: Standard features, simple CRUD operations
   - **Low**: Utility functions, deprecated code, display logic

5. **Identify Specific Gap Types**
   - **Functional Gaps**: Features without any tests
   - **Edge Case Gaps**: Missing boundary and extreme value tests
   - **Error Path Gaps**: Unvalidated exception handling and error conditions
   - **Integration Gaps**: Missing tests for component interactions
   - **Performance Gaps**: No tests for scalability or resource usage
   - **Security Gaps**: Untested authentication, authorization, input validation

6. **Analyze Test Distribution**
   - Compare unit vs integration vs E2E test balance
   - Identify over-tested or under-tested layers
   - Check for redundant tests providing no additional value
   - Verify test pyramid principles (many unit, some integration, few E2E)

7. **Create Prioritized Test Coverage Plan**
   - List specific functions/features needing tests
   - Prioritize by risk level and business impact
   - Estimate effort for each gap
   - Create actionable test scenarios for top gaps
   - Set coverage improvement targets

8. **CRITICAL: Validate Gap Analysis Before Reporting**
   - Verify each identified gap is a real testing need, not a false alarm
   - Cross-check coverage metrics against actual risk
   - Confirm untested code is actually reachable and used
   - **Confidence level** for each gap:
     - **High Confidence:** Gap confirmed through multiple methods (metrics + code review + historical bugs)
     - **Medium Confidence:** Gap identified through metrics, but code complexity may be acceptable
     - **Low Confidence:** Gap identified through metrics only, may be intentionally untested (dead code, generated code)

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Report low coverage on generated code, test utilities, or dead code as gaps
- Flag missing tests for trivial getters/setters or framework boilerplate
- Recommend testing code that's scheduled for deletion or deprecation
- Confuse line coverage with meaningful test quality
- Assume all branches need testing (some defensive code paths may never occur)
- Report gaps without checking if the code is actually reachable in production
- Create test requirements for third-party library code or framework internals

✅ **DO:**
- Focus on business-critical paths regardless of coverage metrics
- Distinguish between intentionally untested code and overlooked gaps
- Verify reported gaps by tracing code paths to actual user scenarios
- Consider the cost-benefit of testing vs. the actual risk
- Check git blame to see if low-coverage code is actively maintained
- Consult with developers about intentional testing exclusions
- Prioritize gaps that correlate with historical production bugs
- Validate that adding tests would actually catch real regressions

**Expected Output:** A comprehensive test coverage gap analysis report including:
- Current coverage metrics summary (overall and per-file)
- List of untested or under-tested modules/functions
- Categorized gaps by type and risk level
- Specific missing test scenarios with examples
- Prioritized recommendations for test creation
- Coverage improvement roadmap with targets
- Sample test cases for highest-priority gaps

**Example Output:**

```markdown
## Test Coverage Gap Analysis Report

**Project**: E-commerce Backend API
**Analysis Date**: 2025-12-08
**Test Framework**: Jest
**Coverage Tool**: Istanbul (nyc)

---

### Current Coverage Metrics

| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Line Coverage | 68.4% | 80% | 🔴 Below target |
| Branch Coverage | 54.2% | 75% | 🔴 Below target |
| Function Coverage | 71.8% | 85% | 🔴 Below target |
| Statement Coverage | 67.9% | 80% | 🔴 Below target |

**Trend**: Coverage decreased by 3.2% over last 2 months (new features added without tests)

---

### Coverage by Module

| Module | Lines | Branches | Functions | Risk Level | Priority |
|--------|-------|----------|-----------|------------|----------|
| `src/services/payment.ts` | 42% | 28% | 50% | Critical | 🔴 High |
| `src/services/order.ts` | 55% | 38% | 60% | Critical | 🔴 High |
| `src/auth/jwt.ts` | 61% | 45% | 71% | Critical | 🟡 Medium |
| `src/controllers/product.ts` | 78% | 62% | 85% | High | 🟢 Low |
| `src/utils/validation.ts` | 45% | 30% | 55% | High | 🟡 Medium |
| `src/models/user.ts` | 89% | 78% | 92% | Medium | 🟢 Low |
| `src/utils/email.ts` | 34% | 20% | 40% | Medium | 🟡 Medium |

---

### Critical Gap #1: Payment Service - Refund Processing

**File**: `src/services/payment.ts`
**Function**: `processRefund(orderId, amount, reason)`
**Current Coverage**: 0% (no tests)
**Risk Level**: Critical (handles money)
**Confidence**: High
- ✅ Verified through coverage metrics AND code review
- ✅ Historical bug data: 3 production incidents in past 6 months related to refunds
- ✅ Active development: 5 commits in last month
- ✅ Business impact: Financial transactions, audit requirements

**Missing Test Scenarios**:

1. **Full refund for completed order**
   ```javascript
   it('should process full refund for completed order', async () => {
     const order = await createTestOrder({ status: 'completed', total: 100 });
     const refund = await paymentService.processRefund(order.id, 100, 'customer_request');

     expect(refund.status).toBe('success');
     expect(refund.amount).toBe(100);
     expect(order.status).toBe('refunded');
     expect(mockStripe.refunds.create).toHaveBeenCalledWith({
       payment_intent: order.paymentIntentId,
       amount: 10000, // cents
     });
   });
   ```

2. **Partial refund validation**
   ```javascript
   it('should reject partial refund exceeding order total', async () => {
     const order = await createTestOrder({ status: 'completed', total: 100 });

     await expect(
       paymentService.processRefund(order.id, 150, 'customer_request')
     ).rejects.toThrow('Refund amount exceeds order total');
   });
   ```

3. **Refund failure handling**
   ```javascript
   it('should handle Stripe refund failure gracefully', async () => {
     mockStripe.refunds.create.mockRejectedValue(
       new Error('Insufficient funds')
     );

     const refund = await paymentService.processRefund(orderId, 100, 'test');

     expect(refund.status).toBe('failed');
     expect(refund.error).toBeDefined();
     // Should log error and notify admin
     expect(mockLogger.error).toHaveBeenCalled();
     expect(mockNotificationService.notifyAdmin).toHaveBeenCalled();
   });
   ```

4. **Edge case: Refund already processed order**
   ```javascript
   it('should prevent duplicate refunds', async () => {
     const order = await createTestOrder({ status: 'refunded' });

     await expect(
       paymentService.processRefund(order.id, 100, 'test')
     ).rejects.toThrow('Order already refunded');
   });
   ```

**Untested Code Paths**:
- Lines 142-156: Refund validation logic
- Lines 158-167: Stripe API integration
- Lines 169-175: Database update on refund success
- Lines 177-183: Error handling and rollback
- Branch: `if (refundAmount > order.total)` - not tested
- Branch: `if (order.status === 'refunded')` - not tested

---

### Critical Gap #2: Order Service - Inventory Validation

**File**: `src/services/order.ts`
**Function**: `validateInventoryAvailability(items)`
**Current Coverage**: 28% (basic happy path only)
**Risk Level**: Critical (can oversell inventory)
**Confidence**: High
- ✅ Verified through metrics + manual code review
- ✅ Race condition risk identified in architecture review
- ✅ Customer complaints about oversold items documented

**Missing Test Scenarios**:
- ❌ Concurrent order attempts for same product (race condition)
- ❌ Partial inventory availability (some items in stock, some out)
- ❌ Inventory reserved but payment fails (rollback)
- ❌ Edge case: Order quantity = 0
- ❌ Edge case: Order quantity > MAX_INT
- ❌ Distributed system: inventory check passes but stock updates elsewhere

**Sample Test for Concurrent Orders**:
```javascript
it('should handle concurrent orders without overselling', async () => {
  const product = await createTestProduct({ stock: 5 });

  // Simulate 10 concurrent orders for 1 item each
  const orderPromises = Array.from({ length: 10 }, () =>
    orderService.createOrder({
      items: [{ productId: product.id, quantity: 1 }]
    })
  );

  const results = await Promise.allSettled(orderPromises);

  // Exactly 5 should succeed, 5 should fail with "out of stock"
  const succeeded = results.filter(r => r.status === 'fulfilled');
  const failed = results.filter(r => r.status === 'rejected');

  expect(succeeded).toHaveLength(5);
  expect(failed).toHaveLength(5);
  expect(failed.every(r =>
    r.reason.message.includes('out of stock')
  )).toBe(true);

  // Verify final inventory is 0
  const finalProduct = await Product.findById(product.id);
  expect(finalProduct.stock).toBe(0);
});
```

---

### High Priority Gap #3: Input Validation - SQL Injection Vectors

**File**: `src/utils/validation.ts`
**Function**: `sanitizeSearchQuery(query)`
**Current Coverage**: 45%
**Risk Level**: High (security vulnerability)
**Confidence**: Medium
- ✅ Verified through coverage metrics
- ⚠️ Security audit recommended but not completed
- ⚠️ No known security incidents, but preventive testing needed

**Missing Security Tests**:
- ❌ SQL injection attempts: `' OR '1'='1`
- ❌ Special characters: `\x00`, `\n`, `\r`
- ❌ Unicode edge cases: emoji, RTL characters
- ❌ Very long input strings (DoS prevention)
- ❌ Script injection: `<script>alert('xss')</script>`

**Sample Security Test**:
```javascript
describe('sanitizeSearchQuery - Security', () => {
  const sqlInjectionPayloads = [
    "' OR '1'='1",
    "'; DROP TABLE users; --",
    "1' UNION SELECT * FROM passwords--",
    "admin'--",
  ];

  it.each(sqlInjectionPayloads)(
    'should sanitize SQL injection attempt: %s',
    (payload) => {
      const sanitized = sanitizeSearchQuery(payload);

      // Should not contain SQL keywords or special chars
      expect(sanitized).not.toMatch(/OR|UNION|DROP|--|;|'/gi);

      // Should be safe to use in query
      expect(() => {
        db.query(`SELECT * FROM products WHERE name LIKE '%${sanitized}%'`);
      }).not.toThrow();
    }
  );
});
```

---

### Coverage Gap Summary by Type

**Functional Gaps** (features with no tests):
- Payment refund processing
- Bulk order import
- Email notification retry logic
- User password reset flow
- Webhook signature verification

**Edge Case Gaps** (missing boundary tests):
- Empty cart checkout
- Order with negative quantity
- Product price = 0 or negative
- User email with invalid formats
- Date ranges (past dates, far future dates)

**Error Path Gaps** (untested exception handling):
- Database connection failures
- Third-party API timeouts
- File upload failures
- Rate limit exceeded scenarios
- Invalid authentication tokens

**Integration Gaps** (untested component interactions):
- Order service ↔ Payment service failure scenarios
- Email service unavailable during order confirmation
- Cache invalidation on product update
- Event publisher failures

---

### Prioritized Test Coverage Roadmap

**Phase 1: Critical Gaps (Week 1-2)**
1. Payment refund processing - 8 test scenarios
2. Order inventory validation - concurrent access tests
3. Authentication token validation - security edge cases
4. Input sanitization - SQL injection & XSS tests

**Phase 2: High Priority Gaps (Week 3-4)**
1. Order service error handling - all failure paths
2. Email notification retry logic - integration tests
3. Webhook processing - signature verification tests
4. User password reset - security flow tests

**Phase 3: Medium Priority Gaps (Month 2)**
1. Bulk operations - large dataset handling
2. Admin dashboard - authorization checks
3. Reporting service - data accuracy tests
4. File upload - size limits and validation

**Target Coverage Goals**:
- End of Phase 1: 75% line coverage, 65% branch coverage
- End of Phase 2: 82% line coverage, 72% branch coverage
- End of Phase 3: 88% line coverage, 78% branch coverage

---

### Test Quality Issues Beyond Coverage

**Weak Assertions Found**:
```javascript
// ❌ Bad: Test executes code but doesn't verify behavior
it('should create user', async () => {
  await userService.createUser({ email: 'test@test.com' });
  // No assertions! Test passes even if function fails silently
});

// ✅ Good: Verifies actual behavior
it('should create user with hashed password', async () => {
  const user = await userService.createUser({
    email: 'test@test.com',
    password: 'plaintext123'
  });

  expect(user.id).toBeDefined();
  expect(user.email).toBe('test@test.com');
  expect(user.password).not.toBe('plaintext123'); // Should be hashed
  expect(user.password).toMatch(/^\$2[aby]\$/); // bcrypt format
  expect(user.createdAt).toBeInstanceOf(Date);
});
```

**Redundant Tests** (can be removed):
- `product.test.ts` lines 45-89: 5 tests that verify same behavior
- `auth.test.ts` lines 120-145: Tests duplicate login scenarios
- Estimated: 15% of test suite provides no additional value

---

### Gap Validation Summary

| Gap | Confidence | Verification Method | False Positive Risk |
|-----|------------|---------------------|---------------------|
| Payment refund | High | Metrics + Code Review + Bug History | Low |
| Inventory validation | High | Metrics + Architecture Review + Complaints | Low |
| Input validation | Medium | Metrics only | Medium - needs security audit |
| Email notification | Low | Metrics only | High - may be intentionally simple |

**Excluded from Report (Intentional Low Coverage):**
- `src/utils/constants.ts` - 12% coverage, intentionally untested (static constants)
- `src/types/*.ts` - 0% coverage, TypeScript type definitions only
- `src/mocks/*.ts` - 5% coverage, test utilities not requiring tests
- `src/scripts/migrations/*.ts` - 20% coverage, one-time scripts with manual verification

---

### Recommendations

1. **Immediate Actions**:
   - Add tests for all payment and order processing logic
   - Implement security tests for input validation
   - Test all error handling and rollback scenarios

2. **Process Improvements**:
   - Require 80% coverage for new code in PR reviews
   - Add coverage diff reporting in CI/CD
   - Block PRs that decrease overall coverage
   - Generate coverage reports on each commit

3. **Tools & Automation**:
   - Enable branch coverage tracking (currently only line coverage)
   - Add mutation testing to verify test quality
   - Set up coverage badges in README
   - Configure coverage trending dashboard

4. **Team Practices**:
   - Conduct test writing workshop focusing on edge cases
   - Create test scenario checklist for common patterns
   - Establish "definition of done" including test requirements
   - Schedule monthly test coverage review meetings
```

**Techniques Used:**
- ST-01 (Clear Objective Statement)
- ST-02 (Sequential Step-by-Step Instructions)
- ST-07 (Prioritization and Ranking)
- RT-02 (Multi-Dimensional Analysis)
- RT-05 (Gap Analysis)
- ST-03 (Structured Output Templates)
- OC-04 (Comprehensive Example Outputs)
- TC-02 (Metrics and Quantification)

**Related Prompts:**
- testing_unit_test_generation.md - To create tests for identified gaps
- testing_integration_test_design.md - For integration gap coverage
- testing_mutation_testing.md - To verify test quality beyond coverage
- security_vulnerability_analysis.md - For security-focused gap analysis
- quality_code_review_checklist.md - To include coverage checks in reviews

**Customization Guide:**
- **For Legacy Code**: Focus on high-risk areas first, accept lower initial coverage targets, prioritize critical business logic
- **For New Projects**: Set strict coverage requirements from start (>80%), enforce in CI/CD, block low-coverage PRs
- **For Frontend Applications**: Include component coverage, user interaction coverage, visual regression gaps
- **For Microservices**: Analyze per-service coverage, emphasize integration test gaps, check contract test coverage
- **For Data Processing**: Add data validation coverage, edge case handling for malformed data, performance test gaps
