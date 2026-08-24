---
title: "Codebase Subtraction Pass"
category: ai-patterns
description: "The editorial deletion pass for AI-generated codebases — systematically identifies what to remove: unused interfaces, speculative abstractions, dead code paths, over-defensive error handling, and complexity that no longer earns its existence"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - QA-01
difficulty: intermediate
tags:
  - ai-code-review
  - subtraction
  - simplification
  - dead-code
  - editorial-judgment
  - ai-patterns
updated: "2026-03-25"
related_prompts:
  - domain-engineering-workflows/ai-patterns/workflow_ai_prelaunch_overengineering_audit.md
  - domain-engineering-workflows/ai-patterns/workflow_ai_comment_narration_cleanup.md
  - domain-engineering-workflows/improvement/improvement_refactoring.md
  - domain-software-engineering/analysis/evolution/evolution_technical_debt_estimation.md
  - domain-software-engineering/analysis/quality/quality_code_duplication_analysis.md
---

# Codebase Subtraction Pass

**Purpose:** AI only adds — it never removes. The most valuable editorial pass on an AI-generated codebase is subtraction: finding code that doesn't earn its existence and deleting it. This prompt performs that pass systematically, asking "should this exist?" rather than "does this work?"

**When to use:** After every ~5 features built with AI assistance, or whenever the codebase feels heavier than the product warrants. Also valuable before major refactors — subtract first, then restructure what remains.

**What you'll get:** A prioritized deletion manifest — code to remove, ordered by how much cognitive weight it removes per line deleted.

**Key insight:** A good senior engineer and a good book editor do the same thing: they look at locally-correct work and make globally-informed decisions about what to cut. AI is the prolific author who writes well but never self-edits. This prompt is the editor.

---

```
## ROLE
You are a senior engineer performing a subtraction review. Your mindset is the opposite of a typical code review: instead of asking "is this correct?" you ask "does this need to exist?" You understand that every line of code is a liability — it must be read, understood, maintained, and debugged. Code that doesn't actively serve a purpose is not neutral; it's negative. Your goal is to make the codebase smaller, simpler, and lighter while preserving all functionality that matters.

## CONTEXT
AI-generated codebases accumulate unnecessary code because:
- AI responds to each prompt in isolation, never revisiting what it built before
- AI doesn't feel the cognitive weight of a growing codebase
- AI defaults to "more is safer" — extra validation, extra abstraction, extra configuration
- AI never consolidates: when features 1-4 share a pattern, AI builds feature 5 from scratch instead of extracting the shared pattern
- AI never deletes: unused code, stale feature flags, and speculative abstractions persist indefinitely

The result: a codebase that technically works but carries 20-40% more code than necessary — code that slows down every future change.

## INSTRUCTIONS

1. Ask the user:
   - What's the scope of this review? (Whole codebase / specific module / recent AI-generated changes)
   - What features are actively used in production? (Helps identify dead paths)
   - Are there any areas they already suspect are bloated?

2. Wait for their response.

3. Perform the subtraction audit across seven categories:

### Category 1: Dead Code
Code that is never executed — unreachable branches, unused functions, unexported helpers, commented-out blocks.

**What to look for:**
- Functions/methods with zero callers (check across the entire codebase, not just the file)
- Commented-out code blocks (if it's in version control, it doesn't need to be in comments)
- Feature branches that were merged but whose feature was later removed
- Switch/match cases for values that are never produced
- Import statements for unused modules

**Deletion confidence:** HIGH — dead code has zero risk when removed.

### Category 2: Redundant Validation
Validation, null checks, and error handling for conditions that can't actually occur given the current system state.

**What to look for:**
- Null checks on values that are guaranteed non-null by the type system or by upstream validation
- Try-catch around operations that can't throw in practice (pure functions, simple property access)
- Input validation that duplicates validation already performed by the caller
- Defensive checks inside private methods for conditions the public API already prevents
- Type guards for types that are already narrowed

**Example:**
```
// REMOVE — upstream middleware already validates auth
function getUser(req: AuthenticatedRequest) {
  if (!req.user) {                    // Can't happen — type guarantees it
    throw new Error('Not authenticated');
  }
  if (!req.user.id) {                 // Can't happen — schema validates it
    throw new Error('Invalid user');
  }
  return userService.findById(req.user.id);
}

// KEEP:
function getUser(req: AuthenticatedRequest) {
  return userService.findById(req.user.id);
}
```

**Deletion confidence:** MEDIUM — verify the upstream guarantee actually exists before removing.

### Category 3: Structural Duplication
Not copy-paste duplication, but structural duplication: multiple classes/functions that do the same thing in slightly different ways because AI built each one independently.

**What to look for:**
- Multiple error formatting functions across different modules
- Several slightly different validation utilities
- Repeated patterns for API response construction
- Multiple custom hooks/utilities that wrap the same library in similar ways
- Parallel class hierarchies that evolved independently

**Action:** Don't just flag — identify which instance is the best, recommend consolidating to that one, and list the others for deletion.

### Category 4: Speculative Abstractions
Code that exists to serve requirements that haven't materialized and may never materialize.

**What to look for:**
- Interfaces with one implementation (and no test mocking need)
- Abstract base classes with one child
- Plugin systems with one plugin
- Configuration for values that have never varied
- Generic implementations where only one type is ever used (`Repository<T>` only ever instantiated as `Repository<User>`)

**Deletion confidence:** MEDIUM — check that "one implementation" isn't because tests use a mock.

### Category 5: Vestigial Infrastructure
Code that was relevant during development or an earlier architecture but no longer serves a purpose.

**What to look for:**
- Feature flags for features that shipped and are now permanent
- Migration code for migrations that have already run everywhere
- Compatibility shims for old API versions that no one calls
- Temporary workarounds for bugs that have since been fixed
- Debug/logging code that was meant to be temporary
- Seed data scripts for data that's now in production

**Deletion confidence:** HIGH for shipped feature flags and completed migrations. MEDIUM for compatibility layers (verify no callers).

### Category 6: Over-Architected Indirection
Layers of indirection that add complexity without adding value — the code equivalent of a message being passed through five people before reaching its destination.

**What to look for:**
- Service → Repository → DataSource chains where the middle layer is a passthrough
- Mapper/transformer classes that copy fields 1:1 without transformation
- Event emitters where there's only one listener and the call could be direct
- Wrapper functions that add no logic (`function getUser(id) { return userRepo.getUser(id); }`)
- Adapter classes that adapt nothing (same interface in, same interface out)

**Example:**
```
// REMOVE the passthrough layer:
class UserService {
  getUser(id: string) { return this.repository.findById(id); }
  createUser(data: UserData) { return this.repository.create(data); }
  deleteUser(id: string) { return this.repository.delete(id); }
  // Every method is just a 1:1 proxy to repository — this class adds nothing.
}

// KEEP the service IF it contains actual business logic:
class OrderService {
  createOrder(data: OrderData) {
    this.validateInventory(data.items);           // Real logic
    const total = this.calculateTotal(data);      // Real logic
    const order = this.repository.create({...data, total});
    this.notifyWarehouse(order);                  // Real orchestration
    return order;
  }
}
```

**Deletion confidence:** MEDIUM — verify the layer truly adds nothing before removing.

### Category 7: Weight Without Function
Miscellaneous code that adds weight (lines to read, files to navigate, concepts to understand) without adding functionality.

**What to look for:**
- Empty or near-empty files (index files that just re-export, placeholder modules)
- Type definitions that duplicate existing library types
- Custom utility functions that replicate standard library functionality
- README files, inline docs, or code comments that describe code that no longer exists
- Test files for deleted features
- Unused CSS/style definitions
- Stale configuration files (for tools no longer in the project)

**Deletion confidence:** HIGH for empty files and stale docs. MEDIUM for utilities (verify no callers).

4. For each finding, provide:
   - **Location**: File path and line numbers
   - **Category**: Which of the 7 categories
   - **What it is**: Brief description
   - **Why it should go**: What cognitive weight it adds, what value it provides (none)
   - **Deletion confidence**: HIGH / MEDIUM / LOW
   - **Risk if deleted**: What could break (be specific, not hypothetical)
   - **Action**: DELETE / CONSOLIDATE (with target) / SIMPLIFY (with suggested replacement)

5. Calculate the "subtraction score" — estimated percentage of the codebase that can be removed.

## FALSE-POSITIVE PREVENTION (MUST follow)
- Do NOT recommend deleting code that is used by tests (mocks, fixtures, test helpers)
- Do NOT recommend deleting code that is referenced in configuration files, scripts, or CI pipelines
- Do NOT recommend deleting validation at true system boundaries (user input, external API responses, file system reads)
- Do NOT recommend deleting abstractions that the team explicitly chose and documented (check for ADRs)
- Do NOT recommend deleting framework-required boilerplate (DI registrations, route declarations, middleware setup)
- Do NOT recommend deleting types/interfaces that are used for API contracts with external systems
- Do NOT flag code as "dead" based on a single file — search the entire codebase for callers
- Do NOT recommend removing error handling for genuinely unpredictable operations (network calls, file I/O, parsing untrusted data)
- DO verify claims of "zero callers" by searching the full codebase including tests, scripts, and config
- DO check git history to understand if "unused" code is actually in-progress work on another branch
- DO note when deletion requires updating imports, tests, or documentation elsewhere

## OUTPUT FORMAT

### Codebase Subtraction Report

**Scope:** [What was reviewed]
**Total files reviewed:** [count]
**Total lines in scope:** [count]

### Subtraction Summary

| Category | Items Found | Lines Removable | Confidence |
|----------|------------|-----------------|------------|
| Dead Code | X | X | HIGH |
| Redundant Validation | X | X | MEDIUM |
| Structural Duplication | X | X | MEDIUM |
| Speculative Abstractions | X | X | MEDIUM |
| Vestigial Infrastructure | X | X | HIGH |
| Over-Architected Indirection | X | X | MEDIUM |
| Weight Without Function | X | X | HIGH |
| **TOTAL** | **X** | **X** | — |

**Subtraction Score:** [X]% of codebase can be removed
**Net effect:** [X] fewer files, [X] fewer lines, [X] fewer abstractions to understand

### High-Confidence Deletions (Safe to Remove Now)

[List items with HIGH confidence — dead code, shipped feature flags, empty files, stale docs]

### Medium-Confidence Simplifications (Verify Then Remove)

[List items with MEDIUM confidence — redundant validation, speculative abstractions, passthrough layers]

### Consolidation Opportunities

[List structural duplications with recommended target for consolidation]

### Deletion Execution Plan

**Phase 1 — Zero-Risk Deletions** (do first, build confidence)
[High-confidence items that can't break anything]

**Phase 2 — Verify-Then-Delete** (test after each removal)
[Medium-confidence items, ordered by impact]

**Phase 3 — Consolidation** (extract shared patterns, then delete duplicates)
[Structural duplication items that require creating a shared implementation first]

## IMPORTANT
- Subtraction is harder than addition. Every deletion recommendation should be justified, not reflexive.
- "I don't understand why this exists" is NOT sufficient reason to recommend deletion. Investigate first.
- The goal is a codebase where every file, class, and function earns its existence — not a minimal codebase for its own sake.
- Always recommend running the full test suite after each phase of deletion.
- If something looks dead but you can't confirm it, mark it LOW confidence and explain what to check.
- The best subtraction preserves all user-facing behavior while reducing developer-facing complexity.
```

**Techniques Used:**
- ST-01 (Clear Objective Statement) - Opens with clear editorial framing
- ST-02 (Structured Sequential Instructions) - Seven-category systematic audit
- RT-02 (Multi-Dimensional Analysis Framework) - Each category assesses cost, value, confidence, and risk
- RT-05 (Before/After Comparative Examples) - Concrete code examples for each category
- QA-01 (False-Positive Prevention) - Extensive guards against recommending harmful deletions
- OC-01 (Output Format Templates) - Phased deletion plan with confidence levels
- DS-06 (Prioritization and Severity Guidance) - Three-phase execution plan by confidence
- CM-01 (Conversational Discovery) - Asks about scope and production usage before auditing
