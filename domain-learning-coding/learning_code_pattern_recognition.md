---
title: "Code Pattern Recognition and Explanation — Identify and Teach the Patterns in a Codebase"
category: "learning-coding"
description: "Identify the design, architectural, and idiomatic patterns actually present in supplied code, then explain each one's problem, trade-offs, and usage guidelines with real snippets — so learners can recognize and apply patterns consistently."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - QA-01
difficulty: intermediate
tags:
  - learning-coding
  - design-patterns
  - architecture
  - code-analysis
  - teaching
updated: "2026-06-07"
related_prompts:
  - domain-learning-coding/learning_code_analogies_metaphors.md
  - domain-learning-coding/learning_code_refactoring_exercises.md
  - domain-software-engineering/analysis/architecture/architecture_design_pattern_identification.md
  - domain-learning-coding/learning_algorithmic_storytelling.md
---

# Code Pattern Recognition and Explanation

**Objective:** Identify the design, architectural, and idiomatic patterns actually present in supplied code, and explain each one's problem, benefits, trade-offs, and usage guidelines with real snippets — so a learner can recognize and apply patterns consistently.

**When to use:**
- Onboarding a learner who needs to recognize the patterns a codebase relies on.
- Documenting architecture for knowledge sharing.
- Preparing for a refactor that depends on understanding existing structure.
- Helping a developer understand unfamiliar code by naming its patterns.

**When NOT to use:**
- Force-fitting named patterns onto code that doesn't use them.
- A full architecture review (use the architecture analysis prompts).
- When you have no code and would be cataloging patterns from imagination.

**Audience:** Developers learning patterns (junior to mid-level), engineers onboarding, reviewers documenting architecture.

---

## Inputs / Context

The user supplies:
1. **The code** to analyze, pasted wrapped in a named tag, e.g. `<code>...</code>`, or a reference (module + file paths).
2. **Language / framework**.
3. **Learner level** so explanation depth can be calibrated.
4. **Learning goal** (recognize patterns, document, prep for refactor, apply consistently).
5. **Optional:** specific patterns the user suspects are present.

Reference the pasted code by its tag name when locating each pattern instance.

---

## Constraints

### Must
- Identify only patterns genuinely present in `<code>`; cite the exact location (classes/functions) for each.
- Name the pattern correctly, including when the implementation deviates from the canonical form — note the deviation.
- For each pattern, explain the problem it solves, benefits in this codebase, trade-offs accepted, and when (not) to use it.
- Distinguish confirmed patterns from "looks like X but isn't quite."
- Include real snippets, not idealized textbook versions.

### Must Not
- Claim a pattern exists because the code superficially resembles it (e.g. calling any callback an "Observer").
- Invent participating classes or relationships not in the code.
- Present a textbook implementation as if it were the codebase's actual code.
- Oversimplify trade-offs into "always good."

---

## Instructions

1. **Scan for patterns.** Read `<code>` and identify candidate creational, structural, behavioral, and architectural patterns. For each candidate, decide: confirmed, partial/deviated, or false match.
2. **Locate instances.** For each confirmed pattern, record location, participating classes/functions, and relationships — citing the code.
3. **Explain purpose.** State the problem solved, benefits realized here, trade-offs accepted, and alternatives that were available.
4. **Show implementation.** Extract the real interface and concrete snippets; mark any deviation from the canonical pattern.
5. **Write usage guidelines.** When to use, when not to, common mistakes, and how to test it.
6. **Map relationships.** Note patterns that collaborate (e.g. Repository + Unit of Work + DI) as evidenced in the code.
7. **Self-check (verification).** For each pattern: is it really present, is the location real, is the deviation noted, are the snippets actual code?

---

## False-Positive Prevention

❌ **DON'T:**
- Label code with a pattern name just because it has a similar shape (callbacks ≠ Observer, any class with `create` ≠ Factory).
- Invent classes, interfaces, or relationships not in the supplied code.
- Substitute a textbook implementation for the codebase's real code.
- Claim benefits without checking the code actually realizes them.
- Assume the learner knows what each pattern is — define it at their level.

✅ **DO:**
- Confirm each pattern's defining characteristics are present before naming it.
- Cite the exact location and show real snippets.
- Note deviations from the canonical form explicitly.
- Flag "resembles but isn't" cases honestly.
- Calibrate explanation depth to the stated learner level.

---

## Output Format

```
# Pattern Catalog — [module]

## Summary
| Category | Patterns Found | Locations |

## Pattern: [name]
### Classification
- Category / GoF (if applicable) / Location
### Problem Solved
### Implementation in This Codebase
[real interface + concrete snippet; note deviations]
### Benefits Here
### Trade-offs
### When to Use / When to Avoid
### Related Patterns in Codebase

## Candidates Rejected (looks like X but isn't)
- [pattern] at [location] — why it's not a true instance
```

---

## Example Output

```markdown
# Pattern Catalog — Order/User Modules

## Summary
| Category | Patterns Found | Locations |
|----------|----------------|-----------|
| Architectural | Repository | `/src/repositories/` |
| Behavioral | Observer (Event Emitter) | `/src/events/` |

---

## Pattern: Repository Pattern

### Classification
- **Category:** Architectural / Data Access
- **Location:** `/src/repositories/` (confirmed)

### Problem Solved
Decouples business logic from data-access logic, so the database can change without touching business code, and services can be tested with mock repositories.

### Implementation in This Codebase
```typescript
// Interface
interface IUserRepository {
  findById(id: string): Promise<User | null>;
  save(user: User): Promise<User>;
}

// Concrete
class PostgresUserRepository implements IUserRepository {
  constructor(private db: DatabaseConnection) {}
  async findById(id: string): Promise<User | null> {
    const r = await this.db.query('SELECT * FROM users WHERE id = $1', [id]);
    return r.rows[0] ? this.mapToUser(r.rows[0]) : null;
  }
}
```
*Conforms to the canonical form (interface + swappable concrete implementation).*

### Benefits Here
- Services accept `IUserRepository`, so they're testable with a mock.
- Could swap Postgres for Mongo by adding another implementation.

### Trade-offs
- Extra interfaces and entity↔row mapping to maintain.
- Complex queries may not fit the interface cleanly.

### When to Use / When to Avoid
✅ Multiple data sources possible; testing is a priority; domain model ≠ schema.
❌ Simple CRUD where direct ORM use suffices; highly dynamic queries.

### Related Patterns in Codebase
- **Dependency Injection** — repositories injected via constructor.
- **Factory** (`RepositoryFactory.ts`) — creates repository instances.

---

## Pattern: Observer (Event Emitter)

### Classification
- **Category:** Behavioral (GoF Observer) — **partial:** a typed in-process emitter, not a full subject/observer hierarchy.
- **Location:** `/src/events/EventEmitter.ts`

### Implementation in This Codebase
```typescript
orderEvents.on('order.created', async (d) => emailService.sendOrderConfirmation(d.userId, d.orderId));
orderEvents.on('order.created', async (d) => analyticsService.trackPurchase(d));
```

### Usage Guidelines
- Use for cross-cutting concerns (logging, analytics, notifications).
- Avoid for core logic needing transactional consistency.
- Always handle errors inside subscribers to prevent cascade failures.

---

## Candidates Rejected (looks like X but isn't)
- `UserMapper` at `/src/mappers/` looks like a Factory but only transforms shapes — it's a Mapper/Translator, not a creational Factory.
```

---

## Verification

- [ ] Every named pattern is genuinely present and located in the supplied code.
- [ ] Deviations from canonical forms are noted.
- [ ] Snippets are real code, not textbook idealizations.
- [ ] "Resembles but isn't" candidates are listed and explained.
- [ ] Benefits claimed are actually realized by the code.
- [ ] Explanations are calibrated to the stated learner level.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Frames the goal as accurate pattern identification and teaching.
- **ST-02 (Structured Sequential Instructions):** Scan → locate → explain → show → guidelines → map → verify.
- **RT-02 (Multi-Dimensional Analysis Framework):** Examines problem, benefits, trade-offs, and alternatives per pattern.
- **RT-05 (Evidence-Based Reasoning):** Requires a cited location and real snippet for each pattern.
- **QA-01 (Self-Verification):** Final pass rejects false matches and confirms each instance.

---

## Related Prompts

- `domain-learning-coding/learning_code_analogies_metaphors.md` — Explain identified patterns via analogy.
- `domain-learning-coding/learning_code_refactoring_exercises.md` — Refactor toward (or away from) patterns.
- `domain-software-engineering/analysis/architecture/architecture_design_pattern_identification.md` — Broader architecture analysis.
- `domain-learning-coding/learning_algorithmic_storytelling.md` — Narrate the algorithms behind the patterns.
