---
title: "Codebase Translation to Another Programming Language"
category: engineering-workflows/improvement
description: "Translate a codebase from one programming language to another while preserving functionality, adapting to target-language idioms, mapping dependencies, and documenting every non-obvious translation decision."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-03
  - QA-01
difficulty: advanced
tags:
  - language-migration
  - porting
  - translation
  - idiomatic-code
  - modernization
updated: "2026-06-07"
related_prompts:
  - domain-engineering-workflows/improvement/improvement_refactoring.md
  - domain-engineering-workflows/improvement/improvement_best_practice_analysis.md
  - domain-engineering-workflows/workflows/coding_problems_catalog.md
---

# Codebase Translation to Another Programming Language

**Objective:** Translate the provided codebase from a source language to a target language so that it preserves behavior, adapts to target-language idioms, maps dependencies to real equivalents, and documents every translation decision that is not a 1:1 mapping.

**When to use:**
- Migrating a legacy system or library to a modern language or platform.
- Porting a component to a second language for a polyglot stack.
- Unifying tech stacks across teams or services.
- Evaluating migration feasibility before committing (translate a representative slice).

**When NOT to use:**
- A within-language cleanup — use `improvement_refactoring.md`.
- A pure quality audit with no language change — use `improvement_best_practice_analysis.md`.
- When the source code is unavailable (this prompt requires real source to translate).

**Audience:** Engineers and tech leads executing or scoping a language migration.

---

## Inputs / Context

The user supplies:
1. **Source code** — wrap pasted source in a `<source_code>` tag (note source language, file paths); or a repo path.
2. **Source and target languages/runtimes** — e.g. Python 3.11 → TypeScript 5 / Node 20.
3. **Translation posture** — literal, idiomatic, or hybrid (default: idiomatic with preserved business logic).
4. **Constraints** — required target libraries, performance targets, precision requirements (money, dates), strict-mode/lint rules.
5. **Test assets** (optional) — existing tests to translate and use as a parity oracle.

If only a fragment is provided, translate what is visible and flag external symbols you cannot resolve.

---

## Constraints

### Must
- Preserve observable behavior; call out any place where exact parity is impossible (e.g. decimal precision, timezone semantics).
- Produce **idiomatic** target code by default (naming conventions, native features, community-standard libraries).
- Map each source dependency to a **real, named** target equivalent — or state that none exists.
- Document every non-obvious translation decision inline or in a decision log.
- Translate tests alongside code and state how parity will be verified.

### Must Not
- Invent target libraries, APIs, or version features that do not exist.
- Claim "all tests pass" or fabricate benchmark numbers unless the user actually ran them.
- Silently change behavior to suit the target language (e.g. float vs. decimal) without flagging it.
- Carry over source-language anti-idioms (Java-style loops in Kotlin, snake_case in TypeScript) when a native idiom exists.

---

## Instructions

1. **Analyze the source.** Identify core business logic, external integrations, language-specific idioms, and constructs with no direct target equivalent. Note available test coverage.
2. **Choose the translation strategy.** Literal / idiomatic / hybrid, plus incremental vs. big-bang. State the choice and why.
3. **Map language features.** Build correspondence tables for: type system & generics, error handling, concurrency model, memory management, standard-library equivalents, package/module system.
4. **Map dependencies.** For each third-party package, name the target equivalent (or "no direct equivalent — implement manually") with a one-line note.
5. **Translate systematically.** Data structures/types → core logic → utilities → tests → framework glue. Convert names and structure to target idioms as you go.
6. **Document differences and limitations.** Record where exact parity is impossible and the chosen compromise.
7. **Verify / self-check before reporting.** Confirm: every source dependency is mapped to something real; no invented APIs; behavior-changing differences are flagged; tests are translated; no fabricated pass/benchmark claims. Label any unverified parity claim as "needs to be run."

---

## False-Positive Prevention

❌ **DON'T:**
- Don't assert a library exists in the target ecosystem unless you are confident it does — say "verify availability" if unsure.
- Don't report a passing test suite or performance number you did not actually produce.
- Don't translate money as a float or dates without timezone handling and call it equivalent.
- Don't keep source-language naming/idioms when the target has a clear native convention.

✅ **DO:**
- Map every dependency to a real, named equivalent (or state none exists).
- Flag behavior-changing differences (precision, time, type narrowing) explicitly.
- Label parity claims as verified (ran tests) vs. expected (needs running).
- Provide both functional and class-based options where the idiomatic choice depends on context.

---

## Output Format

```markdown
# Translation Report: [Source] to [Target]

## Overview
- Source / Target: [versions/runtimes]
- Scope: [files / slice]
- Strategy: [literal | idiomatic | hybrid]

## Feature Mapping
[Type system / error handling / concurrency tables]

## Dependency Mapping
| Source Package | Target Equivalent | Notes |
|----------------|-------------------|-------|

## Translation Examples
### Example N: [construct]
**Source:** ```[lang] ... ```
**Target:** ```[lang] ... ```
**Translation notes:** [decisions, idiom changes]

## Known Differences and Limitations
- [precision / time / type narrowing / etc.]

## Verification Plan
- [how parity is/should be confirmed; what was actually run vs. pending]
```

## Example Output

```markdown
# Translation Report: Python to TypeScript

## Overview

**Source**: Payment Processing Library (Python 3.11)
**Target**: TypeScript 5.0 (Node.js 20)
**Scope**: 24 source files, 18 test files
**Strategy**: Idiomatic with preserved business logic

---

## Feature Mapping

### Type System

| Python | TypeScript | Notes |
|--------|------------|-------|
| `Optional[str]` | `string \| null` | Using union types |
| `List[Payment]` | `Payment[]` | Array syntax preferred |
| `Dict[str, Any]` | `Record<string, unknown>` | Strict typing |
| `TypedDict` | `interface` | More powerful in TS |
| `@dataclass` | `class` or `interface` | Depends on mutability |
| `Enum` | `enum` or union types | Prefer union for string enums |

### Error Handling

| Python | TypeScript |
|--------|------------|
| `try/except` | `try/catch` |
| `raise ValueError` | `throw new Error` |
| Custom exceptions | Custom error classes |
| `assert` | Runtime checks or assertions library |

---

## Translation Examples

### Example 1: Data Class to Interface

**Source (Python):**
```python
from dataclasses import dataclass
from typing import Optional
from datetime import datetime
from enum import Enum

class PaymentStatus(Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"
    REFUNDED = "refunded"

@dataclass
class Payment:
    id: str
    amount: float
    currency: str
    status: PaymentStatus
    customer_id: str
    created_at: datetime
    metadata: Optional[dict] = None

    def is_refundable(self) -> bool:
        return self.status == PaymentStatus.COMPLETED

    def total_in_cents(self) -> int:
        return int(self.amount * 100)
```

**Target (TypeScript):**
```typescript
// Using union type for enum (more idiomatic in TS)
type PaymentStatus = 'pending' | 'completed' | 'failed' | 'refunded';

interface Payment {
  id: string;
  amount: number;
  currency: string;
  status: PaymentStatus;
  customerId: string;  // camelCase per TS convention
  createdAt: Date;
  metadata?: Record<string, unknown>;
}

// Functional helpers
function isRefundable(payment: Payment): boolean {
  return payment.status === 'completed';
}

function totalInCents(payment: Payment): number {
  return Math.round(payment.amount * 100);
}
```

**Translation notes:**
- Union type instead of enum for better inference on string values.
- `snake_case` → `camelCase` per TypeScript convention.
- `Optional` → optional property with `?`.
- `int(amount * 100)` truncates in Python; `Math.round` chosen to match expected money rounding — **flagged as a behavior decision** (see Known Differences).

---

### Example 2: Async Concurrency with a Limit

**Source (Python):**
```python
import asyncio

async def process_batch(self, requests):
    semaphore = asyncio.Semaphore(10)
    async def process_with_limit(request):
        async with semaphore:
            return await self.process_payment(request)
    return await asyncio.gather(*[process_with_limit(r) for r in requests])
```

**Target (TypeScript):**
```typescript
import pLimit from 'p-limit';

async processBatch(requests: PaymentRequest[]): Promise<Payment[]> {
  const limit = pLimit(10);
  return Promise.all(requests.map(r => limit(() => this.processPayment(r))));
}
```

**Translation notes:**
- `asyncio.Semaphore` has no native TS equivalent; mapped to the widely-used `p-limit` library (verify version availability before adding).
- `asyncio.gather` → `Promise.all`.

---

## Dependency Mapping

| Source Package | Target Equivalent | Notes |
|----------------|-------------------|-------|
| `requests` | `fetch` (built-in) or `axios` | fetch native in Node 20 |
| `pydantic` | `zod` | Verify version; preferred for new TS projects |
| `pytest` | `vitest` or `jest` | Choose per team standard |
| `asyncio` | Native Promises | Built into language |
| `dataclasses` | interfaces/classes | Idiom choice per mutability |
| `decimal.Decimal` | `decimal.js` | No native exact-decimal type — see Known Differences |

---

## Known Differences and Limitations

1. **Decimal precision** — Python `decimal.Decimal` has no native JS equivalent. Use `decimal.js` or integer cents. Float-based money will diverge; flagged in Example 1.
2. **Date/time** — JS `Date` lacks robust timezone handling; recommend `luxon` or `date-fns` for parity with Python `datetime`.
3. **Type narrowing** — Python `isinstance` is runtime; TS narrowing is compile-time via type guards.

---

## Verification Plan

- Translated tests: 18 files ported; **not yet executed** — run `vitest` to confirm parity (do not assume pass).
- Recommended oracle: run source and target suites against the same fixtures and diff outputs.
- Strict mode and lint to be enabled before sign-off.
```

---

## Verification

- [ ] Strategy (literal/idiomatic/hybrid) stated with rationale.
- [ ] Feature-mapping tables cover types, errors, concurrency.
- [ ] Every source dependency mapped to a real named equivalent or marked "none."
- [ ] No invented libraries, APIs, or version features.
- [ ] Behavior-changing differences (precision, time, narrowing) flagged.
- [ ] Tests translated; parity claims labeled verified vs. pending.
- [ ] Target code uses target-language idioms and naming.
- [ ] No fabricated test-pass or benchmark numbers.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Frames the parity-preserving translation goal.
- **ST-02 (Structured Sequential Instructions):** Analyze → strategy → feature map → dependency map → translate → document → verify.
- **RT-02 (Multi-Dimensional Analysis):** Maps types, errors, concurrency, dependencies in parallel.
- **RT-03 (Comparative Evaluation):** Source-vs-target side-by-side examples and option comparisons.
- **QA-01 (Self-Verification):** Pre-report check guards against invented libraries and fabricated parity claims.

---

## Related Prompts

- `domain-engineering-workflows/improvement/improvement_refactoring.md` — Clean up before or after translating.
- `domain-engineering-workflows/improvement/improvement_best_practice_analysis.md` — Verify quality of the translated target code.
- `domain-engineering-workflows/workflows/coding_problems_catalog.md` — Reference taxonomy of issues to avoid in the target.
