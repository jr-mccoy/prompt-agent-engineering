---
title: "Android Technical Debt Assessment"
category: mobile-development
description: "Systematically catalogs and prioritizes technical debt in Android codebases with effort estimates and remediation roadmap"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-06
difficulty: intermediate
tags:
  - android
  - mobile-development
updated: "2026-03-19"
related_prompts:
  - domain-software-engineering/mobile/android/analysis/android_codebase_health_assessment.md
  - domain-software-engineering/mobile/android/analysis/android_architecture_review.md
  - domain-software-engineering/mobile/android/maintenance/android_tech_debt_triage.md
---


# Android Technical Debt Assessment

**Objective:** Systematically catalog and prioritize technical debt in an Android codebase, providing a detailed inventory with effort estimates and a remediation roadmap.

**When to Use:** Use this prompt during sprint planning to identify tech debt items, before major feature work to clear blockers, for quarterly technical health reviews, or when the team feels slowed down by code quality issues. Ideal after a codebase health assessment identifies significant debt.

**Prompt Type:** Comprehensive (350-400 lines)

---

## Context Gathering

Before beginning the assessment, understand the debt context:

1. **Team Perception:**
   - "What areas of the codebase does the team find most frustrating to work with?"
   - "Are there known 'landmines' or areas people avoid?"

2. **History:**
   - "Have there been recent time crunches that might have introduced shortcuts?"
   - "Are there features that were 'temporary' but became permanent?"

3. **Constraints:**
   - "Is there a time budget for addressing debt (e.g., 20% of sprint)?"
   - "Are there areas that are 'frozen' and shouldn't be modified?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Trace actual impact** - Don't flag based on pattern matching alone. Verify that the suspected debt actually slows down development or causes problems.
2. **Check for existing solutions** - Search for workarounds, documentation, or planned refactoring that may already address the concern.
3. **Understand the context** - Consider WHY the code is written this way. Time constraints, library limitations, and business needs are valid factors.
4. **Confirm actual cost** - Does fixing this provide real benefit? Some "debt" is acceptable pragmatic code.
5. **Provide specific file:line locations** - Every finding MUST include exact code locations (e.g., `LegacyModule.kt:234`).

**Finding MINIMAL debt is an acceptable outcome.** If the codebase is reasonably clean, say so with confidence. Don't manufacture debt to fill a report.

### False-Positive Prevention

- ❌ Do NOT flag all TODO comments as debt (some are informational)
- ❌ Do NOT flag patterns that work well despite being "non-standard"
- ❌ Do NOT assume code is debt without understanding its purpose
- ❌ Do NOT report stylistic preferences as technical debt
- ✅ DO consider the cost/benefit of addressing each debt item
- ✅ DO understand that some "debt" is acceptable pragmatic code
- ✅ DO check if the "debt" actually causes problems in practice
- ✅ DO weigh team velocity impact against refactoring cost

---

### Phase 1: Debt Discovery

#### 1.1 Code Debt Detection

**TODO/FIXME/HACK Comments:**

```kotlin
// Search patterns:
// TODO: [description]
// FIXME: [description]
// HACK: [description]
// XXX: [description]
// WORKAROUND: [description]
// TEMP: [description]
// @Deprecated without replacement guidance
```

**Suppressed Warnings:**

```kotlin
// Find all suppression annotations
@Suppress("UNCHECKED_CAST")
@SuppressLint("NewApi")
@SuppressWarnings("deprecation")

// Lint baseline file
// Check lint-baseline.xml for suppressed issues
```

**Code Duplication:**

```kotlin
// Look for:
- Similar function implementations across classes
- Copy-pasted code blocks with minor variations
- Repeated boilerplate that could be extracted
```

**Dead Code:**

```kotlin
// Indicators:
- Unused functions (IDE warnings)
- Unused classes
- Unused resources (layouts, drawables, strings)
- Commented-out code blocks
- Unreachable code after returns
```

#### 1.2 Dependency Debt

**Outdated Dependencies:**

```kotlin
// Check for:
- Major versions behind (e.g., Kotlin 1.6 when 1.9 is current)
- Deprecated libraries
- Security vulnerabilities
- End-of-life libraries
```

**Dependency Conflicts:**

```kotlin
// Look in build output for:
- Version conflict warnings
- Duplicate class warnings
- Forced version resolutions
```

**Multiple Libraries for Same Purpose:**

```kotlin
// Common duplications:
- Multiple JSON parsers (Gson + Moshi)
- Multiple HTTP clients
- Multiple image loaders
- Multiple analytics SDKs
```

#### 1.3 Architecture Debt

**God Classes:**

```kotlin
// Indicators:
- Classes with 500+ lines
- Classes with 10+ public methods
- Classes with mixed responsibilities
- "Manager", "Helper", "Utils" classes that grew too large
```

**Tight Coupling:**

```kotlin
// Look for:
- Direct instantiation instead of injection
- Concrete dependencies instead of interfaces
- Circular dependencies between packages
- Feature modules depending on other features directly
```

**Pattern Violations:**

```kotlin
// Examples:
- Business logic in Activities/Fragments
- Data layer imports in UI layer
- Network calls not going through repository
- State mutations outside designated state holders
```

#### 1.4 Test Debt

**Missing Tests:**

```kotlin
// Check for:
- Business logic without unit tests
- ViewModels without tests
- Repository implementations without tests
- Complex algorithms without tests
```

**Flaky/Disabled Tests:**

```kotlin
// Search for:
@Ignore
@Disabled
@FlakyTest
// Tests that are skipped in CI
```

**Outdated Test Utilities:**

```kotlin
// Old patterns:
- Mockito instead of MockK
- JUnit 4 instead of JUnit 5
- Old Espresso patterns
- Missing Compose testing utilities
```

#### 1.5 Documentation Debt

**Missing Documentation:**

```kotlin
// Check for:
- README that doesn't explain setup
- Public APIs without KDoc
- Complex algorithms without comments
- Architecture decisions without ADRs
```

**Stale Documentation:**

```kotlin
// Look for:
- README referencing old build commands
- Comments that don't match code
- Diagrams that don't reflect current architecture
- Outdated API documentation
```

---

### Phase 2: Debt Categorization

**CHECKPOINT 1:** Present debt inventory summary.

```markdown
## Technical Debt Inventory Summary

### Total Debt Items: [X]

| Category | Items | High Severity | Medium | Low |
|----------|-------|---------------|--------|-----|
| Code Debt | [X] | [X] | [X] | [X] |
| Dependency Debt | [X] | [X] | [X] | [X] |
| Architecture Debt | [X] | [X] | [X] | [X] |
| Test Debt | [X] | [X] | [X] | [X] |
| Documentation Debt | [X] | [X] | [X] | [X] |

### Estimated Total Remediation Effort
- **Quick Fixes (< 1 hour each):** [X] items
- **Medium Effort (1-4 hours):** [X] items
- **Large Effort (1+ days):** [X] items

### Highest Risk Areas
1. [Area] - [Why it's risky]
2. [Area] - [Why it's risky]

### Questions
1. Does this match your team's perception of problem areas?
2. Are there categories you'd like me to explore more deeply?

**Shall I proceed with the detailed debt catalog?**
```

---

### Phase 3: Detailed Debt Report

```markdown
# Technical Debt Assessment Report: [App Name]

## Executive Summary

### Debt Health Score: [A-F]

| Metric | Value | Assessment |
|--------|-------|------------|
| Total Debt Items | [X] | [Manageable/Concerning/Critical] |
| High Severity Items | [X] | [Immediate attention needed] |
| Estimated Remediation | [X hours/days] | [Realistic/Significant] |
| Debt Velocity | [Increasing/Stable/Decreasing] | [Based on TODO dates if available] |

### Critical Items Requiring Immediate Attention
1. [Item] - [Risk if not addressed]
2. [Item] - [Risk if not addressed]

---

## Detailed Debt Catalog

### 1. Code Debt

#### TODO/FIXME Inventory

| ID | Type | Description | Location | Age | Priority |
|----|------|-------------|----------|-----|----------|
| CD-001 | TODO | [Description] | [file:line] | [If dated] | [P1/P2/P3] |
| CD-002 | FIXME | [Description] | [file:line] | [If dated] | [P1/P2/P3] |
| CD-003 | HACK | [Description] | [file:line] | [If dated] | [P1/P2/P3] |

#### Suppressed Warnings

| Warning | Reason (if documented) | Location | Risk |
|---------|----------------------|----------|------|
| [Warning type] | [Reason or "Unknown"] | [file:line] | [High/Med/Low] |

#### Code Duplication

| Pattern | Occurrences | Files | Consolidation Effort |
|---------|-------------|-------|---------------------|
| [Duplicated code description] | [X] | [files] | [Low/Med/High] |

#### Dead Code

| Type | Item | Location | Confidence |
|------|------|----------|------------|
| Unused class | [ClassName] | [file] | [High/Med] |
| Unused function | [functionName] | [file:line] | [High/Med] |
| Unused resource | [resource_name] | [type/file] | [High/Med] |

---

### 2. Dependency Debt

#### Outdated Dependencies

| Library | Current | Latest | Versions Behind | Risk |
|---------|---------|--------|-----------------|------|
| Kotlin | [X.X.X] | [Y.Y.Y] | [X] | [Security/Compatibility/Features] |
| AGP | [X.X.X] | [Y.Y.Y] | [X] | [Risk] |
| [Library] | [X.X.X] | [Y.Y.Y] | [X] | [Risk] |

#### Deprecated Dependencies

| Library | Status | Replacement | Migration Effort |
|---------|--------|-------------|------------------|
| [Library] | [Deprecated/EOL] | [Alternative] | [Low/Med/High] |

#### Redundant Dependencies

| Functionality | Libraries Used | Recommendation |
|---------------|---------------|----------------|
| JSON Parsing | Gson, Moshi | Consolidate to Moshi |
| [Function] | [Libraries] | [Recommendation] |

---

### 3. Architecture Debt

#### God Classes

| Class | Lines | Methods | Responsibilities | Refactor Effort |
|-------|-------|---------|-----------------|-----------------|
| [ClassName] | [X] | [X] | [List] | [Hours/Days] |

#### Coupling Issues

| From | To | Type | Severity |
|------|-------|------|----------|
| [Module/Class] | [Module/Class] | [Direct/Circular] | [High/Med] |

#### Pattern Violations

| Violation | Location | Impact | Fix |
|-----------|----------|--------|-----|
| Business logic in Fragment | [file:line] | Testability | Move to ViewModel |
| [Violation] | [location] | [impact] | [fix] |

---

### 4. Test Debt

#### Coverage Gaps

| Component | Type | Tests Exist | Coverage | Priority |
|-----------|------|-------------|----------|----------|
| [Component] | ViewModel | No | 0% | High |
| [Component] | Repository | Partial | ~30% | Medium |

#### Disabled/Flaky Tests

| Test | Reason | Location | Action Needed |
|------|--------|----------|---------------|
| [TestName] | [Reason] | [file] | [Fix/Remove] |

#### Testing Infrastructure Debt

| Issue | Current | Recommended | Effort |
|-------|---------|-------------|--------|
| JUnit version | 4 | 5 | Medium |
| [Issue] | [Current] | [Target] | [Effort] |

---

### 5. Documentation Debt

#### Missing Documentation

| Item | Type | Priority | Effort |
|------|------|----------|--------|
| README setup instructions | README | High | Low |
| [Public API] | KDoc | Medium | Low |
| [Complex class] | Inline | Low | Low |

#### Stale Documentation

| Document | Issue | Location | Fix Effort |
|----------|-------|----------|------------|
| [Document] | [What's wrong] | [location] | [effort] |

---

## Risk Assessment

### High-Risk Debt Items

| Item | Risk Type | Probability | Impact | Mitigation |
|------|-----------|-------------|--------|------------|
| [Item] | [Security/Stability/Velocity] | [High/Med/Low] | [Description] | [Action] |

### Technical Risk Score: [1-10]

| Factor | Score | Notes |
|--------|-------|-------|
| Code fragility | [1-10] | [Assessment] |
| Security exposure | [1-10] | [Assessment] |
| Developer productivity | [1-10] | [Assessment] |
| Onboarding difficulty | [1-10] | [Assessment] |

---

## Remediation Roadmap

### Phase 1: Quick Wins (This Sprint)
*Items that can be fixed in < 1 hour each*

| Item | Category | Effort | Impact |
|------|----------|--------|--------|
| [Item] | [Category] | 30 min | [Impact] |

### Phase 2: Important Fixes (This Month)
*Items requiring 1-4 hours each*

| Item | Category | Effort | Impact |
|------|----------|--------|--------|
| [Item] | [Category] | 2 hours | [Impact] |

### Phase 3: Strategic Improvements (This Quarter)
*Items requiring 1+ days*

| Item | Category | Effort | Impact |
|------|----------|--------|--------|
| [Item] | [Category] | 3 days | [Impact] |

### Phase 4: Long-term Goals
*Items requiring significant planning*

| Item | Category | Effort | Impact |
|------|----------|--------|--------|
| [Item] | [Category] | 2 weeks | [Impact] |

---

## Debt Prevention Recommendations

### Process Improvements
1. [Recommendation for preventing future debt]
2. [Recommendation for catching debt early]

### Tooling Recommendations
1. **Lint Configuration:** Enforce rules to prevent new debt
2. **Pre-commit Hooks:** Block commits with new TODO without issue link
3. **Dependency Bot:** Automate dependency update PRs

### Team Practices
1. **Debt Budget:** Reserve [X]% of sprint for debt reduction
2. **Boy Scout Rule:** Leave code better than you found it
3. **Documentation Reviews:** Include docs in PR checklist
```

---

## Expected Output

1. **Debt Inventory** - Complete catalog of all identified debt
2. **Severity Ratings** - Prioritized by risk and impact
3. **Effort Estimates** - Time to remediate each item
4. **Remediation Roadmap** - Phased plan for addressing debt
5. **Prevention Guide** - How to avoid new debt

---

## Techniques Used

- **ST-01** (Clear Objective): Focused debt assessment
- **ST-02** (Sequential Instructions): Phased discovery and reporting
- **RT-02** (Multi-Dimensional Analysis): Five debt categories
- **RT-05** (Evidence-Based Reasoning): Specific locations and counts
- **DS-06** (Prioritization Guidance): Severity and effort ratings
- **ST-03** (Output Format Templates): Structured catalog
- **OC-05** (Severity Classification): Priority levels
- **AG-12** (Quantitative Metrics): Counts and effort estimates

---

## Related Prompts

- [android_codebase_health_assessment.md](android_codebase_health_assessment.md) - Overall health check
- [android_code_modernization.md](../improvement/android_code_modernization.md) - Address modernization debt
- [android_dependency_audit.md](android_dependency_audit.md) - Deep dependency analysis
- [android_test_coverage_analysis.md](android_test_coverage_analysis.md) - Test debt details

---

## Customization Guide

### For Sprint Planning
- Focus on items completable within sprint
- Group by effort level
- Provide clear acceptance criteria

### For New Team Members
- Use as onboarding documentation
- Highlight "landmine" areas
- Explain historical context

### For Executive Reporting
- Summarize into business risk terms
- Provide cost of inaction
- Recommend investment level
