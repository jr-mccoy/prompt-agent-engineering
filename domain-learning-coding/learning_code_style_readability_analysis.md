---
title: "Code Style and Readability Analysis — Teach Maintainability with Before/After Fixes"
category: "learning-coding"
description: "Evaluate supplied code for naming, structure, documentation, and consistency, and produce prioritized, before/after readability improvements grounded in the actual code — plus linter/formatter configs to enforce them."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - QA-01
difficulty: intermediate
tags:
  - learning-coding
  - readability
  - code-style
  - maintainability
  - refactoring
updated: "2026-06-07"
related_prompts:
  - domain-learning-coding/learning_code_review_checklist.md
  - domain-learning-coding/learning_code_refactoring_exercises.md
  - domain-software-engineering/analysis/quality/quality_code_complexity_analysis.md
  - domain-software-engineering/improvement/improvement_refactoring.md
---

# Code Style and Readability Analysis

**Objective:** Evaluate supplied code for naming, structure, documentation, and consistency, and produce prioritized before/after readability improvements grounded in the actual code — plus linter/formatter settings to enforce them.

**When to use:**
- Establishing or teaching coding standards for a team.
- Reviewing a codebase before a refactor.
- Helping a learner understand why some code is hard to read and how to fix it.
- Reducing cognitive load and onboarding friction.

**When NOT to use:**
- Deep complexity metrics or architecture review (use the dedicated analysis prompts).
- Production refactoring execution (use `improvement_refactoring.md`).
- When no code is supplied and feedback would be generic.

**Audience:** Learners and engineers improving maintainability; team leads setting standards.

---

## Inputs / Context

The user supplies:
1. **The code** to analyze, pasted wrapped in a named tag, e.g. `<code>...</code>`, or a reference (file paths).
2. **Language / framework** (so idiomatic conventions, e.g. PEP 8 vs gofmt, apply).
3. **Learner/team level** to calibrate explanation depth.
4. **Existing style guide** if one is in force.
5. **Optional:** specific files or areas reported as hard to read.

Reference the pasted code by its tag name when citing each issue.

---

## Constraints

### Must
- Cite a concrete location (function/line or quoted snippet) for every finding, drawn from `<code>`.
- Provide before/after for each recommendation, and confirm the "after" preserves behavior.
- Apply the language's idiomatic conventions (don't impose camelCase on idiomatic Python).
- Prioritize by impact (high/medium/low) and note effort.
- Acknowledge genuine strengths, not only problems.

### Must Not
- Invent code that isn't in the supplied source.
- Flag subjective preferences as objective defects.
- Change behavior in a "readability" rewrite (e.g., dropping a guard).
- Recommend a convention that conflicts with the language's norms or the supplied style guide.

---

## Instructions

1. **Assess naming.** From `<code>`, evaluate variable/function/class/constant/file naming for clarity, consistency, and convention. Cite examples.
2. **Analyze structure.** Function length, nesting depth, parameter counts, cohesion — citing real locations.
3. **Evaluate documentation.** Comment relevance, doc completeness, self-documenting code vs over-commenting, stale comments.
4. **Check consistency.** Formatting, import organization, error-handling style, async style — note where the code diverges from itself.
5. **Identify readability blockers.** Magic numbers/strings, deep nesting, long parameter lists, cryptic abbreviations, dense one-liners.
6. **Recommend.** For each, give before/after, impact, and effort; verify behavior is preserved.
7. **Suggest tooling.** Linter/formatter config that would enforce the recommendations.
8. **Self-check (verification).** Is every finding from real code? Does each "after" preserve behavior and respect language norms?

---

## False-Positive Prevention

❌ **DON'T:**
- Report a naming or structure issue using code you invented.
- Treat a personal style preference as a defect.
- Drop validation, error handling, or edge-case logic in a readability rewrite.
- Impose conventions from one language onto another.
- Assume the reader knows terms like "cyclomatic complexity" — define them at their level.

✅ **DO:**
- Cite the exact location for every finding.
- Provide before/after and confirm identical behavior.
- Respect the language's idioms and the supplied style guide.
- Rank by impact and note effort.
- Call out real strengths to calibrate the picture.

---

## Output Format

```
# Code Style & Readability Analysis — [module]

## Summary
- Readability snapshot: [per-category one-liners]
- Top 3 priority improvements

## Findings
### Naming
- Strengths: [location]
- Issue [ID] ([priority]): [location] — before/after

### Structure
### Documentation
### Consistency
### Readability Blockers

## Tooling Recommendations
[linter + formatter config]
```

---

## Example Output

```markdown
# Code Style & Readability Analysis — Order Module

## Summary
| Category | Assessment |
|----------|------------|
| Naming | Good, with mixed conventions in one file |
| Structure | `processOrder` too long / deeply nested |
| Documentation | Inconsistent doc coverage on public methods |
| Consistency | Several error-handling styles |

### Top 3 Priority Improvements
1. Split `OrderService.processOrder` (111 lines, deeply nested).
2. Unify error handling (4 styles found).
3. Add docs to public API methods.

---

## Findings

### Naming

**Strength:** clear boolean prefixes — `isUserAuthenticated`, `hasPermission`.

**Issue 1.1 (medium): Mixed conventions in one file** — `<code>` user module
```typescript
// BEFORE
const user_data = fetchUser();   // snake_case
const orderHistory = getOrders(); // camelCase
const APIURL = 'https://...';     // unclear

// AFTER (consistent camelCase; constant uppercased)
const userData = fetchUser();
const orderHistory = getOrders();
const API_URL = 'https://...';
```

### Structure

**Issue 2.1 (high): Function too long** — `OrderService.processOrder` (~111 lines)
```typescript
// AFTER: extracted into focused steps (behavior unchanged)
async function processOrder(order: Order): Promise<OrderResult> {
  validateOrder(order);
  const totals = calculateOrderTotals(order);
  const finalAmount = applyDiscounts(totals, order.discountCodes);
  const payment = await processPayment(order.userId, finalAmount);
  await updateInventory(order.items);
  await sendOrderNotifications(order, payment);
  return { orderId: order.id, status: 'completed', payment };
}
```

**Issue 2.2 (medium): Deep nesting** — `permissions.ts` (5 levels)
```typescript
// AFTER: guard clause + flattened
function checkAccess(user, resource, action) {
  if (!user?.roles) return false;
  return user.roles.flatMap(r => r.permissions ?? [])
    .some(p => p.resource === resource && p.actions.includes(action));
}
```

### Readability Blockers

**Issue 3.1 (medium): Magic numbers**
```typescript
// BEFORE
if (password.length < 8) {}
setTimeout(cb, 86400000);
// AFTER
const MIN_PASSWORD_LENGTH = 8;
const ONE_DAY_MS = 24 * 60 * 60 * 1000;
if (password.length < MIN_PASSWORD_LENGTH) {}
setTimeout(cb, ONE_DAY_MS);
```

## Tooling Recommendations

### ESLint
```json
{ "rules": {
  "max-lines-per-function": ["warn", { "max": 50 }],
  "complexity": ["warn", { "max": 10 }],
  "max-depth": ["warn", { "max": 3 }],
  "no-magic-numbers": ["warn", { "ignore": [0, 1, -1] }]
}}
```
### Prettier
```json
{ "printWidth": 100, "tabWidth": 2, "singleQuote": true, "trailingComma": "es5" }
```
```

---

## Verification

- [ ] Every finding cites a real location in the supplied code.
- [ ] Each before/after preserves behavior.
- [ ] Recommendations respect the language's idioms and any supplied style guide.
- [ ] Findings are prioritized by impact with effort noted.
- [ ] Subjective preferences aren't presented as defects.
- [ ] At least one genuine strength is acknowledged.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Frames the goal as grounded, teachable readability analysis.
- **ST-02 (Structured Sequential Instructions):** Naming → structure → docs → consistency → blockers → recommend → tooling → verify.
- **RT-02 (Multi-Dimensional Analysis Framework):** Examines naming, structure, documentation, and consistency together.
- **RT-05 (Evidence-Based Reasoning):** Requires a cited location for every finding.
- **QA-01 (Self-Verification):** Final pass confirms grounding, behavior preservation, and idiom-fit.

---

## Related Prompts

- `domain-learning-coding/learning_code_review_checklist.md` — Encode these standards into a review checklist.
- `domain-learning-coding/learning_code_refactoring_exercises.md` — Turn findings into practice exercises.
- `domain-software-engineering/analysis/quality/quality_code_complexity_analysis.md` — Quantitative complexity metrics.
- `domain-software-engineering/improvement/improvement_refactoring.md` — Execute the refactors in production.
