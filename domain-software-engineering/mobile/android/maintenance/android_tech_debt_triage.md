---
title: "Android Technical Debt Triage and Paydown Planning"
category: mobile-development
description: "Systematically inventory, score, and prioritize technical debt in an Android codebase. Produces a severity-ranked debt register with interest calculations and a quarterly paydown plan allocating 20% of development time to high-leverage debt reduction."
techniques:
  - ST-01  # Clear Objective Statement
  - ST-02  # Structured Sequential Instructions
  - RT-02  # Multi-Dimensional Analysis
  - DS-06  # Prioritization Guidance
  - QA-02  # Adversarial Thinking
difficulty: intermediate
tags:
  - android
  - tech-debt
  - maintenance
  - solo-developer
  - kotlin
  - architecture
updated: "2026-02-11"
related_prompts:
  - domain-software-engineering/mobile/android/analysis/android_technical_debt_assessment.md
  - domain-software-engineering/mobile/android/analysis/android_codebase_health_assessment.md
  - domain-software-engineering/mobile/android/analysis/android_architecture_review.md
  - domain-software-engineering/mobile/android/maintenance/android_dependency_update.md
  - domain-software-engineering/mobile/android/improvement/android_code_modernization.md
---

# Android Technical Debt Triage and Paydown Planning

**Objective:** Perform a comprehensive technical debt inventory across an Android codebase, score each debt item by severity (impact x frequency x fix difficulty), calculate the ongoing "interest" cost of not addressing each item, and produce a quarterly paydown plan that allocates approximately 20% of development time to the highest-leverage debt reduction work.

## When to Use

- Use when: You suspect accumulated tech debt is slowing feature development but lack a structured view of what to fix first
- Use when: Starting a new quarter and need to decide which maintenance work to prioritize alongside feature work
- Use when: A solo developer or small team needs to make the most of limited maintenance time
- Use when: Preparing a case for stakeholders about why dedicated debt paydown time is necessary
- Do not use when: You need a quick code quality scan (use `android_codebase_health_assessment.md` instead)
- Do not use when: You are focused on a single area like dependencies (use `android_dependency_audit.md` instead)

**Important context:** Technical debt is not inherently bad. Deliberate, documented debt taken to meet a deadline is a valid engineering trade-off. The goal of this triage is not to eliminate all debt, but to identify which debt items are accruing the highest "interest" (ongoing cost in developer time, user impact, or risk) and retire those first. A healthy codebase carries some debt; an unhealthy one carries untracked debt.

---

## Context Gathering

Before starting the triage, gather the following information:

1. **Codebase Overview:**
   - "How many modules does your project have and what are their responsibilities?"
   - "What architecture pattern are you using (MVVM, MVI, Clean Architecture, or a mix)?"
   - "What is your approximate total line count and language split (Kotlin vs Java)?"

2. **Development Velocity Indicators:**
   - "What tasks consistently take longer than they should? Where do you feel friction?"
   - "Which files or modules do you dread touching?"
   - "How often do changes in one module break something in another?"

3. **Testing and CI State:**
   - "What is your approximate test coverage? Do you trust your tests?"
   - "How long does your CI pipeline take? Are there flaky tests?"
   - "Do you have any automated quality gates (lint, detekt, etc.)?"

4. **Known Pain Points:**
   - "Are there any modules or files you already know have significant debt?"
   - "Have you documented any TODOs, HACKs, or FIXMEs in the code?"
   - "Are there any deprecated API usages you have been postponing?"

5. **Time Budget:**
   - "How many developer-hours per week are available for this project?"
   - "What percentage of time can realistically go to maintenance (target: 20%)?"
   - "When is your next major release or deadline?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before classifying ANY item as technical debt, you MUST:**

1. **Confirm it actually causes harm** -- Code that looks messy but works reliably and rarely changes is low-priority debt at best. Verify there is a real cost: bugs, slowdowns, developer confusion, or blocked features.
2. **Distinguish deliberate from accidental debt** -- Deliberate debt with documentation ("we chose X because of deadline Y, plan to revisit") is lower urgency than accidental debt nobody intended.
3. **Check if the debt is already being addressed** -- Look for open PRs, TODO comments with issue links, or planned refactoring work.
4. **Validate the scope of impact** -- A pattern used in one file is different from a pattern used across 50 files. Quantify before scoring.
5. **Verify fix feasibility** -- Some debt items require API changes, data migrations, or coordinated releases. Factor this into scoring.

**Finding a codebase with manageable, well-documented debt is an acceptable outcome.** Not every codebase needs aggressive debt paydown.

### False-Positive Prevention

- Do NOT flag idiomatic patterns as debt just because a newer pattern exists (e.g., XML layouts are not "debt" if Compose migration is not planned)
- Do NOT treat all TODO comments as debt -- many are aspirational improvements, not obligations
- Do NOT classify framework boilerplate as debt (Hilt modules, Room DAOs, Navigation graphs)
- Do NOT score aesthetic preferences as technical debt (naming conventions, file organization style)
- Do NOT assume "old code" equals "bad code" -- stability and reliability matter more than recency
- DO verify that each debt item has a measurable cost before including it
- DO distinguish between debt that blocks work and debt that merely annoys
- DO check if a "debt" item is actually a deliberate architectural decision
- DO consider whether fixing the debt could introduce new risks
- DO factor in the cost of the fix itself, not just the benefit

---

### Phase 1: Debt Inventory

Catalog all technical debt items across five categories.

#### 1.1 Architecture Debt

Scan for structural issues that make the codebase harder to understand, extend, or test.

```kotlin
// EXAMPLE: Architecture debt indicators to look for

// God Activity / Fragment (>500 lines with mixed concerns)
// Signal: Business logic mixed with UI logic
class OrderActivity : AppCompatActivity() {
    // Database queries directly in Activity
    // Network calls directly in Activity
    // Business validation directly in Activity
    // Navigation logic mixed with data processing
}

// Missing abstraction layers
// Signal: Repository calling API and doing business logic
class OrderRepository(private val api: OrderApi) {
    suspend fun placeOrder(order: Order): Result<Order> {
        // Validation here (should be in use case / domain layer)
        // Price calculation here (should be in domain layer)
        // API call here (correct)
        // Cache update here (correct)
    }
}

// Circular dependencies between modules
// Signal: Module A depends on Module B which depends on Module A
// Check: ./gradlew :app:dependencies | grep -E "project :"
```

**Inventory checklist for architecture:**
- [ ] God classes (Activities, Fragments, ViewModels > 500 lines)
- [ ] Missing layers (UI calling repository directly, repository doing business logic)
- [ ] Circular module dependencies
- [ ] Inconsistent architecture patterns across modules
- [ ] Tightly coupled components that should be independent
- [ ] Missing dependency injection (manual object creation)

#### 1.2 Testing Debt

Identify gaps in test coverage and test quality.

```kotlin
// EXAMPLE: Testing debt indicators

// Untestable code due to tight coupling
class PaymentProcessor {
    // Hard dependency - cannot mock in tests
    private val analytics = FirebaseAnalytics.getInstance(context)
    private val api = RetrofitClient.paymentApi  // Singleton access

    fun processPayment(amount: Double) {
        // No way to test this without real Firebase and real API
    }
}

// vs. Testable version (what the fix looks like)
class PaymentProcessor @Inject constructor(
    private val analytics: AnalyticsTracker,  // Interface
    private val api: PaymentApi               // Interface
) {
    fun processPayment(amount: Double) {
        // Easily testable with fakes/mocks
    }
}
```

**Inventory checklist for testing:**
- [ ] Critical paths without test coverage (payment, auth, data sync)
- [ ] Untestable code due to tight coupling or static dependencies
- [ ] Flaky tests that undermine CI reliability
- [ ] Missing integration tests for cross-module flows
- [ ] No UI tests for critical user journeys
- [ ] Test data setup that is brittle or hard to maintain

#### 1.3 Dependency Debt

Catalog outdated, vulnerable, or abandoned dependencies.

```bash
# Run dependency age analysis
./gradlew dependencyUpdates -Drevision=release

# Check for known vulnerabilities
./gradlew dependencyCheckAnalyze

# Count outdated dependencies
grep -c "The following dependencies have later" build/dependencyUpdates/report.txt
```

**Inventory checklist for dependencies:**
- [ ] Dependencies more than 2 major versions behind
- [ ] Dependencies with known CVEs
- [ ] Abandoned libraries (no updates in 18+ months with open issues)
- [ ] Duplicate functionality (two libraries doing the same thing)
- [ ] Pinned versions with no documented reason
- [ ] Java-only libraries where Kotlin alternatives exist

#### 1.4 UI/UX Debt

Identify UI implementation issues that cause user-facing problems or slow UI development.

```kotlin
// EXAMPLE: UI debt indicators

// Hardcoded dimensions and colors (not using theme/design system)
Text(
    text = "Hello",
    fontSize = 16.sp,          // Should use MaterialTheme.typography
    color = Color(0xFF333333)  // Should use MaterialTheme.colorScheme
)

// Inconsistent navigation patterns
// Some screens use Navigation Component, others use manual Fragment transactions

// Accessibility gaps
// Missing contentDescription on interactive elements
// Touch targets smaller than 48dp
```

**Inventory checklist for UI:**
- [ ] Hardcoded values instead of theme tokens
- [ ] Mixed UI frameworks (some Compose, some XML with no migration plan)
- [ ] Accessibility violations (missing labels, small touch targets)
- [ ] Inconsistent navigation patterns
- [ ] Missing loading/error/empty states
- [ ] UI code duplication (similar screens not sharing components)

#### 1.5 Build System Debt

Assess build configuration health.

```kotlin
// build.gradle.kts indicators of build debt

// Hardcoded versions scattered across files (not using version catalog)
dependencies {
    implementation("com.squareup.retrofit2:retrofit:2.9.0")  // Hardcoded
}

// Overly complex build logic
// Custom Gradle plugins with no tests
// Build times > 3 minutes for incremental builds
```

**Inventory checklist for build system:**
- [ ] Build times (clean build, incremental build, test execution)
- [ ] Hardcoded versions not in version catalog
- [ ] Deprecated Gradle features or plugins
- [ ] Missing build cache configuration
- [ ] No modularization (single monolithic app module)
- [ ] Custom Gradle logic without tests or documentation

---

### Phase 2: Severity Scoring

Score each debt item using three dimensions, each rated 1-5.

#### Scoring Matrix

| Dimension | 1 (Low) | 2 | 3 (Medium) | 4 | 5 (High) |
|-----------|---------|---|------------|---|-----------|
| **Impact** | Cosmetic only | Minor inconvenience | Slows development | Causes bugs/outages | Blocks features or risks data loss |
| **Frequency** | Encountered yearly | Encountered quarterly | Encountered monthly | Encountered weekly | Encountered daily |
| **Fix Difficulty** | < 1 hour | 1-4 hours | 1-2 days | 3-5 days | 1+ weeks |

**Severity Score = Impact x Frequency x Fix Difficulty**

```
Score Range:    1-10  = Low priority (track but don't schedule)
Score Range:   11-30  = Medium priority (address within 2 quarters)
Score Range:   31-60  = High priority (address this quarter)
Score Range:  61-125  = Critical (address this sprint)
```

**Example scoring:**

```markdown
| Debt Item | Impact | Freq | Fix Diff | Score | Priority |
|-----------|--------|------|----------|-------|----------|
| God Activity: OrderActivity (847 lines) | 4 | 5 | 3 | 60 | High |
| No unit tests for PaymentProcessor | 5 | 3 | 2 | 30 | Medium |
| Retrofit 2.6 (current: 2.11) | 2 | 1 | 2 | 4 | Low |
| Hardcoded colors in 23 Compose files | 3 | 4 | 2 | 24 | Medium |
| Build time: 4.5 min clean build | 3 | 5 | 4 | 60 | High |
```

---

### Phase 3: Interest Calculation

For each debt item, calculate the ongoing "interest" -- the cost you pay every period for NOT fixing it.

#### Interest Categories

```markdown
**Developer Time Interest:**
How many hours/week does this debt cost in:
- Extra debugging time
- Working around the issue
- Explaining it to new team members
- Context switching due to complexity

**Risk Interest:**
What is the probability and impact of:
- Production bugs caused by this debt
- Security vulnerabilities
- Data loss scenarios
- App store rejection

**Opportunity Cost Interest:**
What features or improvements are blocked or slowed by:
- This architectural limitation
- This missing test coverage
- This outdated dependency
```

**Interest calculation template:**

```markdown
| Debt Item | Dev Time (hrs/quarter) | Risk (probability x impact) | Opportunity Cost | Total Interest/Quarter |
|-----------|----------------------|---------------------------|-----------------|----------------------|
| God Activity: OrderActivity | 12 hrs | 15% x High = Medium | Blocks feature X | ~16 hrs equivalent |
| No PaymentProcessor tests | 4 hrs | 5% x Critical = Medium | None directly | ~8 hrs equivalent |
| Hardcoded colors | 6 hrs | 0% x None = None | Blocks dark theme | ~6 hrs + feature block |
```

**Key insight:** Items with high interest should be fixed even if their severity score is moderate, because the cumulative cost exceeds the fix cost within 1-2 quarters.

#### Break-Even Analysis

For each high-interest item, calculate when the fix pays for itself:

```
Break-even = Fix Cost (hours) / Interest per Quarter (hours)

Example:
  OrderActivity refactor: 24 hrs fix / 16 hrs per quarter interest = 1.5 quarters to break even
  PaymentProcessor tests: 8 hrs fix / 8 hrs per quarter interest = 1 quarter to break even
  Hardcoded colors:       8 hrs fix / 6 hrs per quarter interest = 1.3 quarters to break even
```

Items that break even in less than 2 quarters should be prioritized regardless of severity score.

---

### Phase 4: Paydown Plan

Build a quarterly plan that allocates approximately 20% of available development time to debt reduction.

#### 4.1 Calculate Time Budget

```markdown
**Available development time:**
- Developer-hours per week: [X]
- Weeks in quarter: 13
- Total quarter hours: [X * 13]
- 20% debt budget: [X * 13 * 0.20]

**Example for solo developer (40 hrs/week):**
- Total quarter hours: 520
- 20% debt budget: 104 hours
- Per sprint (2 weeks): 16 hours = 2 full days
```

#### 4.2 Prioritization Algorithm

Rank debt items by combining severity score and interest:

```
Priority Score = (Severity Score / Max Severity) * 0.4
               + (Interest per Quarter / Max Interest) * 0.4
               + (Break-Even Speed: 1/break-even quarters) * 0.2
```

**Selection rules:**
1. All Critical severity items (score 61+) go into the plan first
2. Fill remaining budget with highest Priority Score items
3. Group related items (e.g., refactor OrderActivity AND add its tests together)
4. Leave 15% buffer for unexpected maintenance
5. Never schedule more than 85% of the debt budget

#### 4.3 Quarter Plan Template

```markdown
## Q[N] 2026 Tech Debt Paydown Plan

**Budget:** [X] hours (20% of [total] development hours)
**Buffer:** [Y] hours (15% of budget reserved for unexpected issues)
**Plannable:** [Z] hours

### Sprint 1 (Weeks 1-2): [Theme]
| Item | Category | Hours | Depends On |
|------|----------|-------|------------|
| [Debt item 1] | Architecture | 8 | None |
| [Debt item 2] | Testing | 4 | Item 1 |
| **Sprint subtotal** | | **12** | |

### Sprint 2 (Weeks 3-4): [Theme]
| Item | Category | Hours | Depends On |
|------|----------|-------|------------|
| [Debt item 3] | Dependencies | 6 | None |
| [Debt item 4] | Build | 8 | None |
| **Sprint subtotal** | | **14** | |

[Continue for all sprints in the quarter...]

### Quarter Summary
| Category | Items | Hours | % of Budget |
|----------|-------|-------|-------------|
| Architecture | 3 | 32 | 36% |
| Testing | 2 | 16 | 18% |
| Dependencies | 2 | 12 | 14% |
| UI | 1 | 8 | 9% |
| Build | 1 | 8 | 9% |
| Buffer | - | 12 | 14% |
| **Total** | **9** | **88** | **100%** |
```

---

### Phase 5: Tracking

Set up lightweight tracking to measure progress and adjust priorities.

#### 5.1 Debt Register

Create a living document that tracks all identified debt:

```markdown
## Tech Debt Register (Last Updated: YYYY-MM-DD)

### Active Debt Items
| ID | Item | Category | Severity | Interest/Q | Status | Target Sprint |
|----|------|----------|----------|-----------|--------|---------------|
| TD-001 | OrderActivity god class | Architecture | 60 | 16 hrs | In Progress | Sprint 3 |
| TD-002 | PaymentProcessor no tests | Testing | 30 | 8 hrs | Scheduled | Sprint 4 |
| TD-003 | Retrofit 2.6 outdated | Dependencies | 4 | 0.5 hrs | Backlog | - |

### Retired Debt (Completed This Quarter)
| ID | Item | Hours Spent | Date Completed |
|----|------|-------------|----------------|
| TD-005 | Hardcoded colors | 6 | 2026-01-15 |

### Metrics
- Total active debt items: [N]
- Total severity points: [sum]
- Total interest/quarter: [sum hrs]
- Items retired this quarter: [N]
- Hours invested this quarter: [N]
```

#### 5.2 Quarterly Review Template

```markdown
## Quarterly Debt Review: Q[N] 2026

### What We Planned vs What We Did
| Planned | Actual | Variance | Reason |
|---------|--------|----------|--------|
| 9 items | 7 items | -2 | Feature deadline pulled in sprint 5 |
| 88 hours | 72 hours | -16 hours | Buffer absorbed production bug |

### Impact Assessment
- Developer velocity change: [faster/same/slower]
- Bugs attributable to debt: [count]
- Feature work unblocked by debt paydown: [list]

### New Debt Added This Quarter
| Item | Category | Why Added | Deliberate? |
|------|----------|-----------|-------------|
| [New item] | [Cat] | [Reason] | Yes/No |

### Next Quarter Priorities
1. [Top priority with rationale]
2. [Second priority with rationale]
3. [Third priority with rationale]
```

---

## Expected Output

The analysis should produce a complete debt triage report with the following structure:

### Output Format

```markdown
# Android Tech Debt Triage Report
**Project:** [Project Name]
**Date:** [Date]
**Analyst:** AI-assisted review

## Executive Summary
- Total debt items identified: [N]
- Critical items requiring immediate attention: [N]
- Estimated total interest per quarter: [N] hours
- Recommended Q[N] budget: [N] hours (20% of available time)

## Debt Inventory by Category

### Architecture Debt ([N] items)
[Detailed findings with evidence]

### Testing Debt ([N] items)
[Detailed findings with evidence]

### Dependency Debt ([N] items)
[Detailed findings with evidence]

### UI/UX Debt ([N] items)
[Detailed findings with evidence]

### Build System Debt ([N] items)
[Detailed findings with evidence]

## Severity Scoring Matrix
| ID | Item | Impact | Freq | Fix Diff | Score | Priority |
|----|------|--------|------|----------|-------|----------|
[All items scored and ranked]

## Interest Analysis
| ID | Item | Dev Time/Q | Risk | Opportunity Cost | Total Interest/Q | Break-Even |
|----|------|-----------|------|-----------------|-----------------|------------|
[All high-severity items with interest calculation]

## Quarterly Paydown Plan
[Sprint-by-sprint plan with time allocations]

## Debt Register
[Living document template populated with findings]

## Recommendations
1. [Highest-impact recommendation with rationale]
2. [Second recommendation]
3. [Third recommendation]

## Appendix: Debt Inventory Detail
[Full details for each debt item including file paths, code examples, and evidence]
```

---

## Example Output (Abbreviated)

```markdown
# Android Tech Debt Triage Report
**Project:** HealthTracker
**Date:** 2026-02-11
**Analyst:** AI-assisted review

## Executive Summary
- Total debt items identified: 14
- Critical items requiring immediate attention: 2
- Estimated total interest per quarter: 48 hours
- Recommended Q1 budget: 104 hours (20% of 520 available hours)

## Severity Scoring Matrix
| ID | Item | Impact | Freq | Fix Diff | Score | Priority |
|----|------|--------|------|----------|-------|----------|
| TD-001 | DashboardFragment (923 lines, mixed concerns) | 4 | 5 | 4 | 80 | Critical |
| TD-002 | No tests for SyncEngine | 5 | 3 | 3 | 45 | High |
| TD-003 | OkHttp 4.9 with CVE-2023-0XXX | 4 | 1 | 2 | 8 | Low* |
| TD-004 | 47 hardcoded color values | 3 | 4 | 2 | 24 | Medium |
| TD-005 | 6-minute clean build time | 4 | 5 | 4 | 80 | Critical |

*TD-003 scored Low on frequency but the CVE is actively exploited. Override to High.

## Interest Analysis
| ID | Dev Time/Q | Risk | Opp Cost | Total/Q | Break-Even |
|----|-----------|------|----------|---------|------------|
| TD-001 | 20 hrs | Med | Blocks dashboard redesign | 28 hrs | 1.1 Q |
| TD-005 | 26 hrs (waiting) | None | Slows all development | 26 hrs | 1.2 Q |
| TD-002 | 8 hrs | High (data corruption risk) | None | 16 hrs | 0.9 Q |

## Q1 2026 Paydown Plan
**Budget:** 104 hours | **Buffer:** 16 hours | **Plannable:** 88 hours

### Sprint 1: Build Performance
| Item | Hours | Notes |
|------|-------|-------|
| TD-005: Modularize build | 24 | Enable parallel compilation |
| TD-007: Add build cache | 8 | Complement modularization |

### Sprint 2: Architecture
| Item | Hours | Notes |
|------|-------|-------|
| TD-001: Extract DashboardViewModel | 16 | Phase 1 of refactor |
| TD-001: Extract DashboardRepository | 8 | Phase 2 of refactor |

### Sprint 3: Safety Net
| Item | Hours | Notes |
|------|-------|-------|
| TD-002: SyncEngine unit tests | 12 | Focus on conflict resolution paths |
| TD-003: OkHttp upgrade | 4 | Security patch |
```

---

## Customization Guide

- **For teams (not solo):** Add a "Team Impact" column to the severity matrix scoring how many developers are affected. Weight team-wide friction higher than individual friction.
- **For apps with legacy Java:** Add a "Java to Kotlin Migration" debt category. Score Java files by how often they are modified (high churn + Java = high priority for conversion).
- **For apps approaching Compose migration:** Create a separate "Compose Migration" debt category. Do NOT score existing XML layouts as debt unless you have committed to migration. Track migration readiness separately.
- **For monetized apps:** Add "Revenue Impact" to the interest calculation. Debt that affects purchase flows, ad rendering, or subscription management gets a multiplier.
- **For apps with CI/CD:** Add "CI Impact" as an interest dimension. Flaky tests, slow builds, and broken pipelines have compounding costs across every PR.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** The objective precisely defines the output: a scored debt register with interest calculations and a quarterly paydown plan.
- **ST-02 (Structured Sequential Instructions):** Five phases build on each other: inventory feeds scoring, scoring feeds interest calculation, interest feeds prioritization, prioritization feeds the plan.
- **RT-02 (Multi-Dimensional Analysis):** Each debt item is analyzed across three scoring dimensions (impact, frequency, fix difficulty) and three interest dimensions (developer time, risk, opportunity cost).
- **DS-06 (Prioritization Guidance):** The combined severity + interest scoring produces a clear priority ranking with actionable cutoffs (Critical/High/Medium/Low).
- **QA-02 (Adversarial Thinking):** The False-Positive Prevention section explicitly guards against scoring aesthetic preferences or stable legacy code as debt.

---

## Related Prompts

- [android_technical_debt_assessment.md](../analysis/android_technical_debt_assessment.md) - Broader assessment without the paydown planning focus
- [android_codebase_health_assessment.md](../analysis/android_codebase_health_assessment.md) - Overall health check including debt indicators
- [android_architecture_review.md](../analysis/android_architecture_review.md) - Deep dive on architecture-specific issues
- [android_dependency_update.md](android_dependency_update.md) - Focused guide for updating dependencies safely
- [android_code_modernization.md](../improvement/android_code_modernization.md) - Converting legacy patterns to modern Kotlin/Compose
