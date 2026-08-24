---
title: "Code Refactoring Exercises — Generate Hands-On Practice from Real Code with Tests and Solutions"
category: "learning-coding"
description: "Generate behavior-preserving refactoring exercises from supplied code — each with a starting state, goals, passing tests, progressive hints, and a worked solution — so learners build refactoring skill on realistic patterns."
techniques:
  - ST-01
  - ST-02
  - ED-02
  - RT-05
  - QA-01
difficulty: intermediate
tags:
  - learning-coding
  - refactoring
  - exercises
  - testing
  - skill-building
updated: "2026-06-07"
related_prompts:
  - domain-learning-coding/learning_code_pattern_recognition.md
  - domain-learning-coding/learning_code_style_readability_analysis.md
  - domain-engineering-workflows/improvement/improvement_refactoring.md
  - domain-software-engineering/testing/testing_unit_test_generation.md
---

# Code Refactoring Exercises

**Objective:** Generate behavior-preserving refactoring exercises from supplied code — each with a starting state, explicit goals, tests that must keep passing, progressive hints, and a worked solution — so learners build refactoring muscle memory on realistic patterns.

**When to use:**
- Training junior developers or running a refactoring workshop.
- Building onboarding materials that use the team's actual patterns.
- Creating self-study practice for a specific refactoring technique.
- Turning a real code smell into a teaching exercise.

**When NOT to use:**
- Production refactoring itself — use `improvement_refactoring.md`.
- When no code is supplied and exercises would be generic and disconnected from the codebase.
- Teaching design from scratch (use lesson generation).

**Audience:** Learners (junior to senior, by difficulty tier), workshop facilitators, and self-studiers.

---

## Inputs / Context

The user supplies:
1. **Source code** with refactoring opportunities, pasted wrapped in a named tag, e.g. `<code>...</code>`, or a reference (file paths).
2. **Language / framework**.
3. **Target skill level(s)** (beginner / intermediate / advanced) for the exercises.
4. **Learning goal** (specific technique, e.g. Extract Method; or broad skill-building).
5. **Optional:** existing tests, time budget per exercise.

Reference the supplied code by its tag name when drawing the starting code for each exercise.

---

## Constraints

### Must
- Base the starting code on real smells present in `<code>` (or faithfully representative of them); do not invent unrelated code.
- Guarantee each refactoring is **behavior-preserving** — provide tests that pass both before and after, including edge cases.
- Name the refactoring technique(s) and the principle(s) (SOLID, DRY) each exercise teaches.
- Provide progressive hints (reveal-on-demand) and a complete worked solution.
- Calibrate scope and difficulty to the stated level(s).

### Must Not
- Provide tests that don't actually pass against the starting code or that change expected behavior.
- Present a "solution" that alters observable behavior (different outputs, removed validation).
- Use magic numbers or smells in the solution that the exercise was meant to remove.
- Over-scope a beginner exercise into an architectural rewrite.

---

## Instructions

1. **Find opportunities.** From `<code>`, identify real smells: long methods, duplication, large switch/conditionals, magic numbers, mixed concerns, hard-to-test code.
2. **Design exercises by tier.** Beginner = single technique, small scope; Intermediate = multiple techniques; Advanced = structural/architectural.
3. **Write the starting code.** Present the smelly code as the exercise input.
4. **Define goals and constraints.** State exactly what to achieve and the rules (e.g., don't change the signature, all tests pass).
5. **Provide the test harness.** Write tests that pass against the starting code and must still pass after refactoring; include edge cases.
6. **Write progressive hints.** 2–4 reveal-on-demand hints from gentle nudge to near-solution.
7. **Write the worked solution.** Show the refactored code and explain each transformation; note alternative valid solutions.
8. **Add learning points.** Name techniques, principles, and the "why."
9. **Self-check (verification).** Do the tests pass against both starting and solution code? Is behavior preserved? Is the difficulty right for the tier?

---

## False-Positive Prevention

❌ **DON'T:**
- Ship tests you haven't mentally executed against the starting code.
- Call a transformation "refactoring" if it changes observable behavior.
- Leave a smell in the solution that the exercise targets.
- Assume the learner knows the technique's name — define it.
- Mismatch difficulty (an "Extract Method" beginner task that requires designing a class hierarchy).

✅ **DO:**
- Trace the starting code so the tests genuinely pass against it.
- Verify the solution produces identical observable behavior.
- Make the solution clean by the exercise's own standards.
- Provide hints that scaffold without giving everything away at once.
- Match scope and technique count to the tier.

---

## Output Format

```
# Refactoring Exercise Collection

## Exercise N: [name] ([tier])
**Time:** [...] | **Techniques:** [...] | **Principles:** [...]

### Problem Statement
### Starting Code
```[language]
[smelly code]
```
### Goals
### Constraints
### Test Cases
```[language]
[tests that must pass before and after]
```
### Hints (reveal progressively)
<details><summary>Hint 1</summary>...</details>
### Solution
```[language]
[refactored code]
```
### Learning Points

## Exercise Catalog Summary
| # | Name | Difficulty | Time | Techniques |
```

---

## Example Output

```markdown
# Refactoring Exercise Collection

## Exercise 1: Extract Method (Beginner)
**Time:** 15–20 min | **Techniques:** Extract Method, Replace Magic Number | **Principles:** Single Responsibility, DRY

### Problem Statement
`processOrder` does validation, calculation, and side effects in one function. Break it into focused functions without changing behavior.

### Starting Code
```javascript
function processOrder(order) {
  if (!order) throw new Error('Order is required');
  if (!order.items || order.items.length === 0) throw new Error('Order must have at least one item');
  if (!order.customerId) throw new Error('Customer ID is required');

  let subtotal = 0;
  for (let i = 0; i < order.items.length; i++) {
    let item = order.items[i];
    let itemTotal = item.price * item.quantity;
    if (item.discount) itemTotal = itemTotal - (itemTotal * item.discount / 100);
    subtotal = subtotal + itemTotal;
  }

  let shipping = subtotal < 50 ? 5.99 : subtotal < 100 ? 2.99 : 0;
  let tax = subtotal * 0.08;

  return {
    orderId: 'ORD-' + Date.now(), customerId: order.customerId, items: order.items,
    subtotal, shipping, tax, total: subtotal + shipping + tax, status: 'pending', createdAt: new Date()
  };
}
```

### Goals
1. Extract `validateOrder`, `calculateSubtotal`, `calculateShipping`.
2. Replace magic numbers with named constants.
3. Each function does one thing.

### Constraints
- All tests must pass. Don't change `processOrder`'s signature. No new dependencies.

### Test Cases
```javascript
test('calculates total for simple order', () => {
  const r = processOrder({ customerId: 'C123', items: [{ price: 10, quantity: 2 }] });
  expect(r.subtotal).toBe(20);
  expect(r.shipping).toBe(5.99);
  expect(r.tax).toBeCloseTo(1.6, 2);
});
test('applies item discount', () => {
  const r = processOrder({ customerId: 'C123', items: [{ price: 100, quantity: 1, discount: 10 }] });
  expect(r.subtotal).toBe(90);
});
test('free shipping over $100', () => {
  const r = processOrder({ customerId: 'C123', items: [{ price: 50, quantity: 3 }] });
  expect(r.shipping).toBe(0);
});
test('throws for missing order', () => { expect(() => processOrder(null)).toThrow('Order is required'); });
```

### Hints (reveal progressively)
<details><summary>Hint 1</summary>Start with validation: a function that takes the order and throws the same errors.</details>
<details><summary>Hint 2</summary>The subtotal loop can become `calculateSubtotal(items)` returning a number.</details>
<details><summary>Hint 3</summary>Shipping depends only on subtotal: `calculateShipping(subtotal)`.</details>

### Solution
```javascript
const TAX_RATE = 0.08;
const FREE_SHIPPING_THRESHOLD = 100;
const REDUCED_SHIPPING_THRESHOLD = 50;
const STANDARD_SHIPPING = 5.99;
const REDUCED_SHIPPING = 2.99;

function validateOrder(order) {
  if (!order) throw new Error('Order is required');
  if (!order.items || order.items.length === 0) throw new Error('Order must have at least one item');
  if (!order.customerId) throw new Error('Customer ID is required');
}
function calculateItemTotal(item) {
  const base = item.price * item.quantity;
  return item.discount ? base - (base * item.discount / 100) : base;
}
function calculateSubtotal(items) { return items.reduce((s, i) => s + calculateItemTotal(i), 0); }
function calculateShipping(subtotal) {
  if (subtotal >= FREE_SHIPPING_THRESHOLD) return 0;
  if (subtotal >= REDUCED_SHIPPING_THRESHOLD) return REDUCED_SHIPPING;
  return STANDARD_SHIPPING;
}
function processOrder(order) {
  validateOrder(order);
  const subtotal = calculateSubtotal(order.items);
  const shipping = calculateShipping(subtotal);
  const tax = subtotal * TAX_RATE;
  return {
    orderId: 'ORD-' + Date.now(), customerId: order.customerId, items: order.items,
    subtotal, shipping, tax, total: subtotal + shipping + tax, status: 'pending', createdAt: new Date()
  };
}
```

### Learning Points
1. **Extract Method** — break large functions into focused ones.
2. **Replace Magic Number** — named constants document intent.
3. **Single Responsibility** — each function does one thing.
4. **Testability** — small pure functions are trivial to unit test.

---

## Exercise 2: Replace Conditional with Polymorphism (Intermediate)
**Time:** 30–45 min | **Techniques:** Strategy + Factory/Registry | **Principles:** Open/Closed, Liskov

### Problem Statement
`processPayment` uses a growing switch over payment types. Refactor so a new payment type can be added without modifying existing code.

### Solution Pattern
```typescript
interface PaymentProcessor { validate(p: PaymentData): void; process(p: PaymentData): PaymentResult; getFee(amount: number): number; }

class CreditCardProcessor implements PaymentProcessor {
  validate(p) { if (!p.cardNumber || p.cardNumber.length !== 16) throw new Error('Invalid card number'); }
  process(p) { this.validate(p); return { success: true, transactionId: 'CC-' + Date.now(), fee: this.getFee(p.amount) }; }
  getFee(amount) { return amount * 0.029; }
}

class PaymentProcessorRegistry {
  private processors = new Map<string, PaymentProcessor>();
  register(type, processor) { this.processors.set(type, processor); }
  get(type) { const p = this.processors.get(type); if (!p) throw new Error(`Unknown payment type: ${type}`); return p; }
}

const registry = new PaymentProcessorRegistry();
registry.register('credit_card', new CreditCardProcessor());
function processPayment(payment) { return registry.get(payment.type).process(payment); }
```

---

## Exercise Catalog Summary
| # | Name | Difficulty | Time | Techniques |
|---|------|------------|------|------------|
| 1 | Extract Method | Beginner | 15–20 min | Extract Method, Constants |
| 2 | Replace Conditional w/ Polymorphism | Intermediate | 30–45 min | Strategy, Factory |
| 3 | Remove Duplicate Code | Beginner | 20–25 min | Extract Method, Template Method |
| 4 | Replace Nested Conditionals | Intermediate | 30–35 min | Guard Clauses, Early Return |
| 5 | Extract Class | Advanced | 45–60 min | Extract Class, Move Method |
```

---

## Verification

- [ ] Starting code reflects real smells from the supplied code.
- [ ] Tests pass against both the starting code and the solution.
- [ ] Each solution preserves observable behavior.
- [ ] No targeted smell remains in the solution.
- [ ] Hints scaffold progressively; a full worked solution is included.
- [ ] Difficulty and technique count match each exercise's tier.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Frames the goal as behavior-preserving practice exercises.
- **ST-02 (Structured Sequential Instructions):** Find → tier → start → goals → tests → hints → solution → verify.
- **ED-02 (Progressive Exercise Generation):** Builds exercises matched to each skill level with scaffolded hints.
- **RT-05 (Evidence-Based Reasoning):** Tests anchor every claim that behavior is preserved.
- **QA-01 (Self-Verification):** Final pass confirms tests pass and behavior is unchanged.

---

## Related Prompts

- `domain-learning-coding/learning_code_pattern_recognition.md` — Identify the patterns to refactor toward.
- `domain-learning-coding/learning_code_style_readability_analysis.md` — Find the readability issues to fix.
- `domain-engineering-workflows/improvement/improvement_refactoring.md` — Production refactoring guidance.
- `domain-software-engineering/testing/testing_unit_test_generation.md` — Generate the tests that lock behavior.
