---
title: "Android Test Coverage Analysis"
category: mobile-development
description: "Analyzes existing test coverage and quality in Android codebases, identifying critical gaps and improvement recommendations"
techniques:
  - ST-01
  - ST-02
  - ST-03
  - DS-06
difficulty: intermediate
tags:
  - analysis
  - android
  - mobile-development
  - testing
updated: "2026-03-19"
related_prompts:
  - domain-software-engineering/mobile/android/analysis/android_codebase_health_assessment.md
  - domain-software-engineering/mobile/android/testing/android_test_strategy_design.md
  - domain-software-engineering/mobile/android/testing/android_mutation_testing_effectiveness_review.md
---


# Android Test Coverage Analysis

**Objective:** Analyze existing test coverage and quality in an Android codebase, identify critical coverage gaps, and provide recommendations for improving the test suite.

**When to Use:** Use this prompt when planning testing improvements, before major refactoring to ensure safety nets exist, during sprint planning to identify test debt, when test failures are frequent and unreliable, or as a release-readiness input before Play Store submission.

**Prompt Type:** Modular (120-150 lines)

---

## Context Gathering

1. **Current Testing State:**
   - "Does the project have unit tests, integration tests, UI tests, or a mix?"
   - "Are tests run in CI/CD pipeline?"

2. **Goals:**
   - "What's driving this analysis (confidence for refactoring, quality gates, etc.)?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Trace actual test coverage** - Don't flag based on file counts alone. Verify that the suspected coverage gaps actually leave important code untested.
2. **Check for existing quality assurance** - Search for integration tests, manual testing, or other QA that may compensate for unit test gaps.
3. **Understand the context** - Consider WHY certain areas may lack tests. Stable code, UI code, or generated code may not need extensive testing.
4. **Confirm actual risk** - Is the untested code actually risky? Trivial code or well-understood patterns may not need exhaustive tests.
5. **Provide specific file:line locations** - Every finding MUST include exact code locations (e.g., `UserRepository.kt` lacks tests).

**Finding ADEQUATE coverage is an acceptable outcome.** If the test suite effectively covers critical paths, say so with confidence. Don't manufacture coverage concerns.

### False-Positive Prevention

- ❌ Do NOT flag low coverage percentage without understanding what's tested
- ❌ Do NOT assume missing tests mean missing quality assurance
- ❌ Do NOT report untested trivial/generated code as a gap
- ❌ Do NOT demand 100% coverage as a goal
- ✅ DO identify actually risky untested code paths
- ✅ DO consider test quality over quantity
- ✅ DO check for integration/E2E tests that cover unit-level gaps
- ✅ DO understand that different code needs different test strategies

---

### Phase 1: Test Inventory

#### 1.1 Scan Test Directories

```
app/src/
├── test/                 # Unit tests (JVM)
│   └── kotlin/
├── androidTest/          # Instrumented tests
│   └── kotlin/
└── sharedTest/          # Shared test utilities (if present)
```

#### 1.2 Test Classification

| Test Type | Directory | Count | Frameworks Used |
|-----------|-----------|-------|-----------------|
| Unit Tests | test/ | [X] | JUnit4/5, MockK, Mockito |
| Integration Tests | test/ or androidTest/ | [X] | [Frameworks] |
| UI Tests | androidTest/ | [X] | Espresso, Compose Testing |

#### 1.3 Coverage Analysis

**Components to Assess:**

| Component Type | Total | With Tests | Coverage |
|----------------|-------|------------|----------|
| ViewModels | [X] | [X] | [%] |
| Repositories | [X] | [X] | [%] |
| Use Cases | [X] | [X] | [%] |
| Utilities | [X] | [X] | [%] |
| Composables | [X] | [X] | [%] |

---

### Phase 2: Coverage Gap Analysis

#### 2.1 Critical Gaps

```markdown
## High-Priority Missing Tests

### Business Logic Without Tests
| Component | Complexity | Risk | Priority |
|-----------|------------|------|----------|
| [Class/Function] | [High/Med/Low] | [Impact if broken] | P1 |

### Untested Edge Cases
| Area | Missing Test | Risk |
|------|--------------|------|
| [Area] | [Scenario] | [Risk] |
```

#### 2.2 Test Quality Assessment

| Aspect | Assessment | Issues |
|--------|------------|--------|
| Naming conventions | [Good/Inconsistent] | [Examples] |
| Assertion quality | [Thorough/Weak] | [Examples] |
| Test isolation | [Good/Coupled] | [Examples] |
| Mock vs Fake usage | [Appropriate/Overuse] | [Examples] |
| Flaky tests | [None/Some/Many] | [List if any] |

---

### Phase 3: Test Coverage Report

```markdown
## Test Coverage Analysis Report

### Summary

| Metric | Value | Target | Gap |
|--------|-------|--------|-----|
| Overall Coverage | [%] | 70%+ | [X%] |
| Critical Paths | [%] | 90%+ | [X%] |
| Unit Test Count | [X] | - | - |
| Integration Tests | [X] | - | - |
| UI Tests | [X] | - | - |

### Coverage Gaps by Priority

**P1 - Must Have**
- [ ] [Component] - [Why critical]
- [ ] [Component] - [Why critical]

**P2 - Should Have**
- [ ] [Component] - [Benefit]

**P3 - Nice to Have**
- [ ] [Component] - [Benefit]

### Test Quality Issues

| Issue | Occurrences | Recommendation |
|-------|-------------|----------------|
| [Issue] | [X] | [Fix] |

### Recommended Test Strategy

1. **Unit Tests:** [Focus areas]
2. **Integration Tests:** [Focus areas]
3. **UI Tests:** [Focus areas]

### Quick Wins
- [Test that would add most value with least effort]
```

---

## Expected Output

1. **Test Inventory** - All existing tests categorized
2. **Coverage Assessment** - What's tested vs what should be
3. **Gap Prioritization** - Critical missing tests
4. **Quality Evaluation** - Test suite health
5. **Recommendations** - Prioritized testing roadmap

---

## Techniques Used

- **ST-01** (Clear Objective): Testing focus
- **ST-03** (Output Format Templates): Structured analysis
- **DS-06** (Prioritization Guidance): Priority levels

---

## Related Prompts

- [android_codebase_health_assessment.md](android_codebase_health_assessment.md) - Overall health
- [android_technical_debt_assessment.md](android_technical_debt_assessment.md) - Test debt section
- [../testing/android_ci_test_pipeline_optimization.md](../testing/android_ci_test_pipeline_optimization.md) - Align coverage goals with CI gates
- [../testing/android_device_api_test_matrix_design.md](../testing/android_device_api_test_matrix_design.md) - Validate coverage across supported devices/APIs
- [../testing/android_contract_testing_network_data_boundaries.md](../testing/android_contract_testing_network_data_boundaries.md) - Close network/data boundary gaps
- [../testing/android_mutation_testing_effectiveness_review.md](../testing/android_mutation_testing_effectiveness_review.md) - Evaluate whether tests detect real defects
- [../publishing/play_store_pre_launch_checklist.md](../publishing/play_store_pre_launch_checklist.md) - Feed coverage outcomes into release go/no-go
