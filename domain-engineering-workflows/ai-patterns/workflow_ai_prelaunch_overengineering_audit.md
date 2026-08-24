---
title: "Pre-Launch Over-Engineering Audit"
category: ai-patterns
description: "Detects premature abstractions, unnecessary migration paths, feature flags for zero users, backwards-compatibility shims, and speculative architecture that AI builds for codebases with no production users yet"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - QA-01
difficulty: beginner
tags:
  - ai-code-review
  - over-engineering
  - yagni
  - premature-abstraction
  - ai-patterns
  - pre-launch
updated: "2026-03-25"
related_prompts:
  - domain-software-engineering/analysis/evolution/evolution_technical_debt_estimation.md
  - domain-software-engineering/analysis/quality/quality_code_duplication_analysis.md
  - domain-engineering-workflows/ai-patterns/workflow_agent_footgun_detector.md
  - domain-engineering-workflows/improvement/improvement_refactoring.md
---

# Pre-Launch Over-Engineering Audit

**Purpose:** Detects the specific kind of over-engineering that AI produces: code built for scale, migration, and backwards-compatibility before the product has any users. AI treats every change as though it might break someone, because in its training data, that's what "professional" code does. On a pre-launch project, this adds weight without value.

**When to use:** On any codebase that hasn't shipped to real users yet — or has a very small user base where breaking changes are trivial. Especially valuable after extended AI-assisted development where layers of "enterprise" architecture have accumulated without anyone questioning whether they're needed yet.

**What you'll get:** An inventory of speculative complexity — code that exists to serve hypothetical future requirements rather than current ones — with concrete recommendations for what to simplify or delete.

---

```
## ROLE
You are a pragmatic tech lead reviewing a pre-launch (or early-stage) codebase. You believe in YAGNI (You Aren't Gonna Need It) and understand that premature abstraction is a form of technical debt — it adds cognitive overhead, increases surface area for bugs, and makes the codebase harder to change, not easier. Your job is to find complexity that doesn't earn its keep.

## CONTEXT
AI-generated codebases accumulate speculative complexity because:
- AI defaults to "textbook best practices" regardless of project stage
- AI has no sense of whether the project has 0 users or 10 million users
- AI treats every class as if it needs an interface, every config as if it needs a feature flag, and every schema change as if it needs a migration path
- AI never asks "do I need this yet?" — it just builds the "correct" version

The result: pre-launch projects that look like enterprise systems serving millions, with all the complexity cost and none of the benefit.

## INSTRUCTIONS

1. Ask the user:
   - How many real users does this project currently serve? (0, <10, <100, <1000, 1000+)
   - Is this a greenfield project or does it have legacy constraints?
   - Are there external consumers of any APIs or data formats?

2. Wait for their response.

3. Scan the codebase for these over-engineering patterns:

**Pattern 1: Interfaces with One Implementation**
Interfaces, abstract classes, or protocols that have exactly one concrete implementation and no realistic prospect of a second.
```
// Over-engineered:
interface IUserRepository { ... }
class UserRepository implements IUserRepository { ... }
// Nothing else implements IUserRepository. Delete the interface.

// Right-sized:
class UserRepository { ... }
// Add the interface when you actually need a second implementation.
```

**Pattern 2: Factory Patterns Wrapping Single Constructors**
Factory classes, builder patterns, or creation functions that only ever produce one type.
```
// Over-engineered:
class NotificationFactory {
  create(type: string): Notification {
    switch(type) {
      case 'email': return new EmailNotification();
      default: throw new Error('Unknown type');
    }
  }
}

// Right-sized:
const notification = new EmailNotification();
// Add the factory when you have 3+ notification types.
```

**Pattern 3: Feature Flags for Features That Don't Exist**
Feature toggle infrastructure for code paths that have never been toggled off, or flags that gate features that haven't launched yet and have no users to break.
```
// Over-engineered (pre-launch):
if (featureFlags.isEnabled('new-dashboard')) {
  renderNewDashboard();
} else {
  renderLegacyDashboard(); // "Legacy" dashboard is 2 weeks old
}

// Right-sized:
renderDashboard(); // Just ship it. There's no one to break.
```

**Pattern 4: Migration and Backwards-Compatibility Layers**
Database migration scaffolding, API versioning, deprecation annotations, or compatibility shims in a project with no users to migrate.
```
// Over-engineered (0 users):
/** @deprecated Use getUserV2 instead */
function getUser(id: string) { return getUserV2(id); }
function getUserV2(id: string) { ... }

// Right-sized:
function getUser(id: string) { ... }
// Just change the function. No one is calling the old version.
```

**Pattern 5: Dependency Injection for Things That Won't Be Swapped**
DI containers, service locators, or constructor injection for dependencies that will never realistically have alternate implementations (the database, the one cache layer, the single auth provider).
```
// Over-engineered:
class OrderService {
  constructor(
    @Inject('IPaymentGateway') private payment: IPaymentGateway,
    @Inject('ICacheProvider') private cache: ICacheProvider,
    @Inject('ILogger') private logger: ILogger,
    @Inject('IMetrics') private metrics: IMetrics,
  ) {}
}

// Right-sized:
class OrderService {
  constructor(
    private payment: StripeClient,
    private cache: RedisCache,
  ) {}
  // Logger and metrics are module-level singletons, not injected.
  // Add interfaces when you actually need to swap an implementation.
}
```

**Pattern 6: Speculative Configuration**
Config files, environment variables, or admin panels for values that have never been changed and have no realistic reason to change.
```
// Over-engineered:
MAX_RETRY_ATTEMPTS=3          # Has never been anything but 3
ENABLE_RATE_LIMITING=true     # Has never been false
CACHE_TTL_SECONDS=300         # Has never been changed
DEFAULT_PAGE_SIZE=20          # Has never been changed

// Right-sized:
const MAX_RETRIES = 3;        // Constant in code until you actually need to tune it
```

**Pattern 7: Abstract Base Classes with One Child**
Inheritance hierarchies where the base class exists purely for "extensibility" and only one class extends it.
```
// Over-engineered:
abstract class BaseProcessor {
  abstract process(data: any): Result;
  protected validate(data: any): boolean { ... }
  protected log(msg: string): void { ... }
}
class DataProcessor extends BaseProcessor {
  process(data: any): Result { ... }
}

// Right-sized:
class DataProcessor {
  process(data: any): Result { ... }
  private validate(data: any): boolean { ... }
}
```

**Pattern 8: Event Systems with One Subscriber**
Pub/sub, event bus, or observer patterns where each event has exactly one handler. The indirection adds complexity without the decoupling benefit.
```
// Over-engineered:
eventBus.emit('user.created', user);
// ... in another file:
eventBus.on('user.created', sendWelcomeEmail);

// Right-sized:
await createUser(data);
await sendWelcomeEmail(user);
// Direct call until you actually need multiple handlers or async decoupling.
```

4. For each finding, assess:
   - **What it costs**: Cognitive overhead, files to navigate, indirection to trace
   - **What it buys**: What future scenario would justify this complexity
   - **Likelihood**: How likely is that scenario in the next 6 months
   - **Verdict**: SIMPLIFY (reduce to direct implementation) or KEEP (justified by current needs) or DEFER (remove now, easy to add back later)

5. Provide a prioritized simplification plan.

## FALSE-POSITIVE PREVENTION (MUST follow)
- Do NOT flag abstractions required by the framework (e.g., Spring's @Service, Angular's dependency injection, protocol conformance in Swift)
- Do NOT flag interfaces used for testing (mock injection for unit tests is a valid reason for an interface)
- Do NOT flag DI in projects that explicitly use DI as an architectural pattern with team buy-in
- Do NOT flag feature flags in projects that are live with real users
- Do NOT flag migration infrastructure if there's a production database with real data
- Do NOT flag API versioning if external consumers exist
- Do NOT flag configuration for values that genuinely vary across environments (dev/staging/prod)
- Do NOT flag event systems if there are already 2+ subscribers or if async decoupling is genuinely needed
- DO ask about user count and project stage before flagging anything
- DO verify that each flagged abstraction has exactly one implementation before calling it premature
- DO check whether "speculative" code was added by AI or was a deliberate human decision

## OUTPUT FORMAT

### Pre-Launch Over-Engineering Audit

**Project Stage:** [Pre-launch / Early-stage / Growth]
**User Count:** [from user input]
**External API Consumers:** [Yes/No]

### Summary

**Total over-engineering instances found:** [count]
**Estimated cognitive overhead:** [Low / Medium / High]
**Simplification effort:** [hours/days estimate]

### Findings

#### Pattern: [Pattern Name]

**Location:** `[file path]:[line numbers]`

**What exists:**
[Brief description of the over-engineered structure]

**What it costs:**
[Cognitive overhead, files to navigate, indirection to trace]

**What it buys:**
[The hypothetical future scenario this prepares for]

**Likelihood that scenario matters in 6 months:** [Low / Medium / High]

**Verdict:** SIMPLIFY / KEEP / DEFER

**Simplification:**
```
[Concrete code showing what the simplified version looks like]
```

---

### Simplification Priority

| # | Location | Pattern | Effort | Impact | Verdict |
|---|----------|---------|--------|--------|---------|
| 1 | ... | ... | ... | ... | ... |

### Recommendations
[2-4 sentences on the overall architectural posture and when it would be appropriate to add back the removed complexity]

## IMPORTANT
- This audit is specifically for pre-launch or early-stage projects. For mature projects with real users, most of these patterns ARE appropriate.
- The goal is not to write "bad" code — it's to write right-sized code for the current stage.
- Every abstraction you remove can be added back in 15 minutes when you actually need it. Every abstraction you keep costs cognitive overhead every day.
- Some of these patterns are genuinely useful in the right context. The question is always: "does this earn its existence RIGHT NOW?"
- If the user's project turns out to be mature with real users, say so and skip the audit — this prompt isn't for them.
```

**Techniques Used:**
- ST-01 (Clear Objective Statement) - Opens with specific, stage-aware objective
- ST-02 (Structured Sequential Instructions) - Numbered steps with conversational discovery
- RT-02 (Multi-Dimensional Analysis Framework) - Eight distinct pattern categories
- RT-05 (Before/After Comparative Examples) - Over-engineered/right-sized pairs for each pattern
- QA-01 (False-Positive Prevention) - Extensive guards against flagging legitimate architecture
- OC-01 (Output Format Templates) - Structured findings with cost/benefit analysis
- DS-06 (Prioritization and Severity Guidance) - Verdict system with priority ranking
- CM-01 (Conversational Discovery) - Asks about project stage before auditing
