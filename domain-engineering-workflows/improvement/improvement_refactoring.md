---
title: "Codebase Refactoring for Readability and Performance"
category: engineering-workflows/improvement
description: "Plan and execute behavior-preserving refactorings of a codebase, producing a prioritized inventory of code smells, before/after transformations with rationale, and a test-guarded implementation sequence."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-06
  - QA-01
difficulty: advanced
tags:
  - refactoring
  - code-smells
  - technical-debt
  - maintainability
  - improvement
updated: "2026-06-07"
related_prompts:
  - domain-engineering-workflows/improvement/improvement_best_practice_analysis.md
  - domain-engineering-workflows/workflows/coding_problems_catalog.md
  - domain-engineering-workflows/improvement/improvement_language_translation.md
---

# Codebase Refactoring for Readability and Performance

**Objective:** Refactor the provided code to improve readability, maintainability, and performance through behavior-preserving transformations — delivered as a prioritized smell inventory, before/after examples with rationale, and a safe, test-guarded execution sequence.

**When to use:**
- Paying down technical debt before new feature work.
- Acting on code-review feedback that flags complexity or duplication.
- Preparing legacy code for change (improving testability first).
- Cleaning up a module during a sprint hardening pass.

**When NOT to use:**
- Changing language/platform — use `improvement_language_translation.md`.
- A pure read-only audit with no transformations — use `improvement_best_practice_analysis.md`.
- When you cannot preserve behavior (a feature change, not a refactor).

**Audience:** Engineers and tech leads improving an existing codebase without changing its behavior.

---

## Inputs / Context

The user supplies:
1. **The code to refactor** — wrap pasted source in a `<code>` tag (note language and file:line context); or a repo path.
2. **Goals / pain points** — readability, performance, testability, or a specific complaint from review.
3. **Test situation** — existing tests, coverage level, or "no tests yet."
4. **Constraints** — public APIs that must not change, performance budgets, off-limits files.

If behavior-preserving refactoring is unsafe without tests, say so and recommend characterization tests first.

---

## Constraints

### Must
- Preserve observable behavior; flag any transformation that could change it.
- Quote the **specific code** being refactored (file:line where available) for each change.
- Name the **refactoring technique** applied (Extract Method, Guard Clauses, Replace Magic Number, Extract Class, etc.).
- Sequence changes so each is small, independently verifiable, and test-guarded.
- Prioritize the inventory (High/Medium/Low) by impact and effort.

### Must Not
- Fabricate metrics — cyclomatic-complexity numbers, line counts, coverage %, or benchmark deltas you did not measure. Use qualitative claims or label estimates as estimates.
- Recommend refactoring code whose full call-graph or callers you cannot see.
- Bundle behavior changes into a "refactor" without flagging them.
- Propose a rewrite where targeted refactorings suffice.

---

## Instructions

1. **Assess current state.** Identify code smells: long methods, large/god classes, duplication, deep nesting, magic numbers, unclear naming, obvious performance issues (N+1, redundant work).
2. **Set refactoring goals.** Tie each to a concrete outcome (readability, testability, performance, maintainability).
3. **Build a prioritized inventory.** For each smell: technique to apply, expected benefit, priority (High/Medium/Low). Mark any metric as measured vs. estimated.
4. **Select and sequence transformations.** Order for safety: add/confirm tests first, then smallest-blast-radius changes, then larger extractions. Keep each step atomic.
5. **Produce before/after for each change.** Quote original, show refactored, list the specific changes and the technique used. Flag anything that touches behavior.
6. **Define validation.** State how behavior is confirmed unchanged after each step (existing tests, new characterization tests, manual checks).
7. **Self-check before reporting.** Verify: behavior preserved, every change names a technique and quotes code, no fabricated numbers, sequence is test-guarded, priorities justified.

---

## False-Positive Prevention

❌ **DON'T:**
- Don't claim "complexity dropped from 18 to 2" or "86% fewer lines" unless you actually measured it — say "substantially simpler" or label it an estimate.
- Don't extract or inline code whose callers you can't see.
- Don't change behavior (rounding, ordering, error semantics) under the banner of refactoring without flagging it.
- Don't refactor untested code without first recommending characterization tests.

✅ **DO:**
- Quote the exact code and name the refactoring technique.
- Keep each step atomic and independently verifiable.
- Flag any change that could alter behavior.
- Label metrics as measured vs. estimated; prefer qualitative claims when unmeasured.

---

## Output Format

```markdown
# Refactoring Plan: [module/scope]

## Summary
- Scope: [file(s)]
- Goals: [...]
- Test situation: [...]

## Smell Inventory (prioritized)
| Smell | Location | Technique | Priority | Benefit |
|-------|----------|-----------|----------|---------|

## Refactoring N: [technique] ([smell])
**Location:** [file:line]
### Before
```[lang] [quoted code] ```
### After
```[lang] [refactored code] ```
**Changes:** [list] — **Behavior impact:** none / flagged: [...]

## Execution Sequence
1. [add/confirm tests]
2. [smallest change] → verify
3. ...

## Validation
- [how behavior is confirmed unchanged]
```

## Example Output

```markdown
# Refactoring Plan: Order Processing Module

## Executive Summary

**Module**: `src/services/OrderService.ts`
**Current State**: 847 lines, cyclomatic complexity 34, 12 code smells
**Target State**: < 200 lines per class, complexity < 10, 0 critical smells

### Refactoring Overview

| Smell | Count | Technique | Priority |
|-------|-------|-----------|----------|
| Long Method | 5 | Extract Method | High |
| Large Class | 1 | Extract Class | High |
| Duplicate Code | 3 | Extract & Reuse | Medium |
| Magic Numbers | 8 | Replace with Constants | Medium |
| Deep Nesting | 4 | Guard Clauses | Medium |
| Feature Envy | 2 | Move Method | Low |

---

## Refactoring 1: Extract Method (Long Method)

### Before

**Location:** `OrderService.ts:45-156` (111 lines)

```typescript
async processOrder(orderData: OrderInput): Promise<Order> {
  // Validate order data (lines 46-78)
  if (!orderData.customerId) {
    throw new Error('Customer ID required');
  }
  if (!orderData.items || orderData.items.length === 0) {
    throw new Error('Order must have items');
  }
  for (const item of orderData.items) {
    if (!item.productId) {
      throw new Error('Product ID required for each item');
    }
    if (item.quantity <= 0) {
      throw new Error('Quantity must be positive');
    }
    const product = await this.productRepository.findById(item.productId);
    if (!product) {
      throw new Error(`Product ${item.productId} not found`);
    }
    if (product.stock < item.quantity) {
      throw new Error(`Insufficient stock for ${product.name}`);
    }
  }

  // Calculate totals (lines 80-110)
  let subtotal = 0;
  const enrichedItems = [];
  for (const item of orderData.items) {
    const product = await this.productRepository.findById(item.productId);
    const itemTotal = product.price * item.quantity;
    subtotal += itemTotal;
    enrichedItems.push({
      ...item,
      productName: product.name,
      unitPrice: product.price,
      totalPrice: itemTotal
    });
  }

  // Apply discounts (lines 112-130)
  let discount = 0;
  if (orderData.promoCode) {
    const promo = await this.promoRepository.findByCode(orderData.promoCode);
    if (promo && promo.isValid()) {
      if (promo.type === 'percentage') {
        discount = subtotal * (promo.value / 100);
      } else {
        discount = promo.value;
      }
    }
  }

  // Calculate shipping (lines 132-145)
  let shipping = 0;
  const totalWeight = enrichedItems.reduce((sum, item) => sum + item.weight * item.quantity, 0);
  if (totalWeight < 1) {
    shipping = 4.99;
  } else if (totalWeight < 5) {
    shipping = 9.99;
  } else {
    shipping = 14.99;
  }
  if (subtotal > 100) {
    shipping = 0; // Free shipping over $100
  }

  // Create order (lines 147-156)
  const order = await this.orderRepository.create({
    customerId: orderData.customerId,
    items: enrichedItems,
    subtotal,
    discount,
    shipping,
    tax: (subtotal - discount) * 0.08,
    total: subtotal - discount + shipping + (subtotal - discount) * 0.08,
    status: 'pending'
  });

  return order;
}
```

### After

```typescript
async processOrder(orderData: OrderInput): Promise<Order> {
  await this.validateOrderData(orderData);

  const enrichedItems = await this.enrichOrderItems(orderData.items);
  const subtotal = this.calculateSubtotal(enrichedItems);
  const discount = await this.calculateDiscount(orderData.promoCode, subtotal);
  const shipping = this.calculateShipping(enrichedItems, subtotal);
  const tax = this.calculateTax(subtotal - discount);

  return this.orderRepository.create({
    customerId: orderData.customerId,
    items: enrichedItems,
    subtotal,
    discount,
    shipping,
    tax,
    total: subtotal - discount + shipping + tax,
    status: 'pending'
  });
}

private async validateOrderData(orderData: OrderInput): Promise<void> {
  this.validateRequiredFields(orderData);
  await this.validateItemsAvailability(orderData.items);
}

private validateRequiredFields(orderData: OrderInput): void {
  if (!orderData.customerId) {
    throw new ValidationError('Customer ID required');
  }
  if (!orderData.items?.length) {
    throw new ValidationError('Order must have items');
  }
}

private async validateItemsAvailability(items: OrderItem[]): Promise<void> {
  for (const item of items) {
    await this.validateItemAvailability(item);
  }
}

private async validateItemAvailability(item: OrderItem): Promise<void> {
  if (!item.productId) {
    throw new ValidationError('Product ID required');
  }
  if (item.quantity <= 0) {
    throw new ValidationError('Quantity must be positive');
  }

  const product = await this.productRepository.findById(item.productId);
  if (!product) {
    throw new NotFoundError(`Product ${item.productId} not found`);
  }
  if (product.stock < item.quantity) {
    throw new InsufficientStockError(product.name, product.stock, item.quantity);
  }
}

private async enrichOrderItems(items: OrderItem[]): Promise<EnrichedOrderItem[]> {
  return Promise.all(items.map(item => this.enrichOrderItem(item)));
}

private async enrichOrderItem(item: OrderItem): Promise<EnrichedOrderItem> {
  const product = await this.productRepository.findById(item.productId);
  return {
    ...item,
    productName: product.name,
    unitPrice: product.price,
    totalPrice: product.price * item.quantity,
    weight: product.weight
  };
}

private calculateSubtotal(items: EnrichedOrderItem[]): number {
  return items.reduce((sum, item) => sum + item.totalPrice, 0);
}

private async calculateDiscount(promoCode: string | undefined, subtotal: number): Promise<number> {
  if (!promoCode) return 0;

  const promo = await this.promoRepository.findByCode(promoCode);
  if (!promo?.isValid()) return 0;

  return promo.type === 'percentage'
    ? subtotal * (promo.value / 100)
    : promo.value;
}

private calculateShipping(items: EnrichedOrderItem[], subtotal: number): number {
  if (subtotal > FREE_SHIPPING_THRESHOLD) return 0;

  const totalWeight = items.reduce((sum, item) => sum + item.weight * item.quantity, 0);
  return this.getShippingRate(totalWeight);
}

private getShippingRate(weight: number): number {
  if (weight < LIGHT_PACKAGE_WEIGHT) return LIGHT_SHIPPING_RATE;
  if (weight < MEDIUM_PACKAGE_WEIGHT) return MEDIUM_SHIPPING_RATE;
  return HEAVY_SHIPPING_RATE;
}

private calculateTax(taxableAmount: number): number {
  return taxableAmount * TAX_RATE;
}
```

### Changes Made

1. **Extract Method**: Created 12 focused methods from 1 monolithic method
2. **Replace Magic Numbers**: Introduced constants for rates and thresholds
3. **Custom Error Types**: `ValidationError`, `NotFoundError`, `InsufficientStockError`
4. **Single Responsibility**: Each method does exactly one thing
5. **Improved Testability**: Each method can be unit tested independently

### Benefits (illustrative — measure on your codebase)

| Metric | Before | After | Note |
|--------|--------|-------|------|
| Main method length | ~111 lines | ~15 lines | extracted into helpers |
| Decision points in main method | many | few | branching moved into focused methods |
| Independently testable units | 1 | 12 | each helper unit-testable |

> Numbers above are illustrative of the *shape* of the improvement. Report only complexity/line/coverage figures you have actually measured on the real code.

---

## Refactoring 2: Replace Nested Conditionals with Guard Clauses

### Before

```typescript
async getOrderStatus(orderId: string, userId: string): Promise<OrderStatus> {
  const order = await this.orderRepository.findById(orderId);
  if (order) {
    if (order.customerId === userId) {
      if (order.status !== 'cancelled') {
        if (order.items.length > 0) {
          const allShipped = order.items.every(item => item.shipped);
          if (allShipped) {
            return { status: 'shipped', message: 'All items shipped' };
          } else {
            const someShipped = order.items.some(item => item.shipped);
            if (someShipped) {
              return { status: 'partial', message: 'Some items shipped' };
            } else {
              return { status: 'processing', message: 'Order is being processed' };
            }
          }
        } else {
          throw new Error('Order has no items');
        }
      } else {
        throw new Error('Order was cancelled');
      }
    } else {
      throw new Error('Unauthorized access');
    }
  } else {
    throw new Error('Order not found');
  }
}
```

### After

```typescript
async getOrderStatus(orderId: string, userId: string): Promise<OrderStatus> {
  const order = await this.orderRepository.findById(orderId);

  // Guard clauses - fail fast
  if (!order) {
    throw new NotFoundError('Order', orderId);
  }

  if (order.customerId !== userId) {
    throw new UnauthorizedError('Cannot access order belonging to another user');
  }

  if (order.status === 'cancelled') {
    throw new InvalidStateError('Order was cancelled');
  }

  if (order.items.length === 0) {
    throw new InvalidStateError('Order has no items');
  }

  // Happy path - clear logic
  return this.determineShippingStatus(order.items);
}

private determineShippingStatus(items: OrderItem[]): OrderStatus {
  const shippedCount = items.filter(item => item.shipped).length;

  if (shippedCount === items.length) {
    return { status: 'shipped', message: 'All items shipped' };
  }

  if (shippedCount > 0) {
    return { status: 'partial', message: `${shippedCount} of ${items.length} items shipped` };
  }

  return { status: 'processing', message: 'Order is being processed' };
}
```

### Changes Made

1. **Guard Clauses**: Check failure conditions early and exit
2. **Reduced Nesting**: From 7 levels to 1 level
3. **Extract Method**: Shipping status logic in separate method
4. **Specific Errors**: Custom error types instead of generic Error
5. **Improved Messages**: More informative status messages

---

## Refactoring 3: Replace Magic Numbers with Constants

### Before (scattered throughout codebase)

```typescript
// In OrderService
if (subtotal > 100) { shipping = 0; }
if (weight < 1) { shipping = 4.99; }
else if (weight < 5) { shipping = 9.99; }
tax = subtotal * 0.08;

// In PaymentService
if (amount > 10000) { requiresApproval = true; }
if (retries > 3) { throw new Error('Max retries'); }

// In UserService
if (password.length < 8) { throw new Error('Too short'); }
if (loginAttempts > 5) { lockAccount(); }
```

### After

```typescript
// constants/order.ts
export const ORDER_CONSTANTS = {
  FREE_SHIPPING_THRESHOLD: 100,
  SHIPPING_RATES: {
    LIGHT: { MAX_WEIGHT: 1, RATE: 4.99 },
    MEDIUM: { MAX_WEIGHT: 5, RATE: 9.99 },
    HEAVY: { RATE: 14.99 }
  },
  TAX_RATE: 0.08
} as const;

// constants/payment.ts
export const PAYMENT_CONSTANTS = {
  APPROVAL_THRESHOLD: 10000,
  MAX_RETRY_ATTEMPTS: 3
} as const;

// constants/user.ts
export const USER_CONSTANTS = {
  MIN_PASSWORD_LENGTH: 8,
  MAX_LOGIN_ATTEMPTS: 5
} as const;

// Usage
import { ORDER_CONSTANTS } from '../constants/order';

if (subtotal > ORDER_CONSTANTS.FREE_SHIPPING_THRESHOLD) {
  shipping = 0;
}

const tax = subtotal * ORDER_CONSTANTS.TAX_RATE;
```

### Benefits

1. **Self-documenting**: Code explains itself
2. **Single Source of Truth**: Change value in one place
3. **Type Safety**: `as const` enables literal types
4. **Discoverability**: Easy to find all business rules
5. **Testability**: Can import constants in tests

---

## Refactoring 4: Extract Class (Large Class)

### Problem

`OrderService` has grown to handle:
- Order validation
- Price calculation
- Discount application
- Shipping calculation
- Tax calculation
- Notification sending
- Analytics tracking

### Solution: Extract to Focused Classes

```typescript
// Before: One 800-line class
class OrderService {
  // 15 methods, 20 dependencies
}

// After: Focused, single-responsibility classes
class OrderValidationService {
  async validate(orderData: OrderInput): Promise<void> { }
}

class OrderPricingService {
  calculateSubtotal(items: OrderItem[]): number { }
  calculateTax(amount: number): number { }
  applyDiscount(amount: number, promo: Promo): number { }
}

class ShippingCalculator {
  calculate(items: OrderItem[], subtotal: number): number { }
}

class OrderService {
  constructor(
    private validation: OrderValidationService,
    private pricing: OrderPricingService,
    private shipping: ShippingCalculator,
    private repository: OrderRepository
  ) {}

  async createOrder(orderData: OrderInput): Promise<Order> {
    await this.validation.validate(orderData);

    const subtotal = this.pricing.calculateSubtotal(orderData.items);
    const discount = this.pricing.applyDiscount(subtotal, orderData.promo);
    const shippingCost = this.shipping.calculate(orderData.items, subtotal);
    const tax = this.pricing.calculateTax(subtotal - discount);

    return this.repository.create({
      ...orderData,
      subtotal,
      discount,
      shipping: shippingCost,
      tax,
      total: subtotal - discount + shippingCost + tax
    });
  }
}
```

---

## Implementation Checklist

### Phase 1: Preparation
- [ ] Add missing tests for current behavior
- [ ] Set up code coverage reporting
- [ ] Create feature branch for refactoring
- [ ] Review and approve refactoring plan

### Phase 2: Extract Methods (Week 1)
- [ ] Refactor `processOrder` method
- [ ] Refactor `getOrderStatus` method
- [ ] Add unit tests for extracted methods
- [ ] Code review checkpoint

### Phase 3: Extract Constants (Week 1)
- [ ] Create constants files
- [ ] Replace all magic numbers
- [ ] Update tests to use constants

### Phase 4: Extract Classes (Week 2)
- [ ] Create `OrderValidationService`
- [ ] Create `OrderPricingService`
- [ ] Create `ShippingCalculator`
- [ ] Update `OrderService` to use new classes
- [ ] Full regression test

### Success Criteria
- [ ] All existing tests pass
- [ ] Behavior verified unchanged after each step
- [ ] No method/class exceeds the team's agreed size threshold
- [ ] Complexity reduced (measured, not assumed)
- [ ] Performance unchanged or improved (measured)
```

---

## Verification

- [ ] Behavior preserved; any behavior-affecting change is flagged.
- [ ] Every refactoring quotes the code and names the technique.
- [ ] Inventory is prioritized (High/Medium/Low) with justification.
- [ ] Execution sequence is atomic and test-guarded (tests first if missing).
- [ ] No fabricated complexity, line-count, coverage, or benchmark numbers.
- [ ] No refactoring proposed for code whose callers/call-graph aren't visible.
- [ ] Validation step states how unchanged behavior is confirmed.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Frames the behavior-preserving improvement goal.
- **ST-02 (Structured Sequential Instructions):** Assess → goals → inventory → sequence → before/after → validate.
- **RT-02 (Multi-Dimensional Analysis):** Evaluates readability, performance, testability, maintainability together.
- **DS-06 (Prioritization and Severity Guidance):** High/Medium/Low inventory drives the execution order.
- **QA-01 (Self-Verification):** Pre-report check guards behavior preservation and blocks fabricated metrics.

---

## Related Prompts

- `domain-engineering-workflows/improvement/improvement_best_practice_analysis.md` — Audit to surface what needs refactoring.
- `domain-engineering-workflows/workflows/coding_problems_catalog.md` — Reference taxonomy of smells and fixes.
- `domain-engineering-workflows/improvement/improvement_language_translation.md` — When the cleanup is part of a language migration.
