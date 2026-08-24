---
title: "Android Test Strategy Design"
category: mobile-development
description: "Designs comprehensive test strategy tailored to Android project architecture, risk profile, and team capabilities with prioritized roadmap"
tags:
  - android
  - mobile-development
  - testing
updated: "2026-03-19"
---

# Android Test Strategy Design

**Objective:** Design a comprehensive, practical test strategy tailored to an Android project's architecture, risk profile, and team capabilities, producing a prioritized testing roadmap.

**When to Use:** Use this prompt when starting a new project that needs a testing foundation, when existing test coverage is ad-hoc or insufficient, before major releases to ensure quality gates exist, or when establishing testing standards for a team. Best used after architecture is defined but before major feature implementation.

**Prompt Type:** Comprehensive (300-400 lines)

---

## Context Gathering

Before designing a test strategy, gather essential context:

1. **Project Context:**
   - "What type of app is this (consumer, enterprise, utility)?"
   - "What's the current architecture pattern (MVVM, MVI, Clean Architecture)?"
   - "Is this a new project or existing codebase?"

2. **Current Testing State:**
   - "What tests currently exist (unit, integration, UI)?"
   - "What frameworks/tools are currently in use?"
   - "What's the current test coverage (approximate)?"

3. **Team Context:**
   - "What's the team's testing experience level?"
   - "How much time can be allocated to writing/maintaining tests?"
   - "Is there CI/CD infrastructure in place?"

4. **Risk Profile:**
   - "What are the critical user flows that must never break?"
   - "Are there financial transactions, auth flows, or data-sensitive operations?"
   - "What's the cost of bugs reaching production?"

5. **Constraints:**
   - "Are there specific testing frameworks required or prohibited?"
   - "Any device/API level testing requirements?"
   - "Are there flaky test concerns from past experience?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before recommending ANY test strategy, you MUST:**

1. **Trace actual code structure** - Don't recommend testing approaches without understanding the codebase architecture.
2. **Check for existing tests** - Search for existing test coverage, frameworks, and patterns before suggesting new approaches.
3. **Understand the context** - Consider team size, experience, and time constraints when recommending test investment.
4. **Confirm actual risk areas** - Focus testing strategy on code that actually has high bug potential or business impact.
5. **Provide specific recommendations** - Every strategy recommendation should reference actual code areas (e.g., "test UserRepository.kt critically").

**A LIGHTWEIGHT strategy may be appropriate.** If the codebase is simple or the team is small, don't over-engineer the test approach.

### False-Positive Prevention

- ❌ Do NOT recommend 100% coverage as a goal without considering cost/benefit
- ❌ Do NOT recommend complex test infrastructure for simple projects
- ❌ Do NOT ignore existing test coverage when planning additions
- ❌ Do NOT recommend testing approaches the team can't maintain
- ✅ DO focus on critical paths and high-risk code first
- ✅ DO consider team testing experience when recommending tools
- ✅ DO understand the trade-off between test maintenance and coverage
- ✅ DO provide pragmatic, achievable testing milestones

---

### Phase 1: Codebase Analysis

#### 1.1 Architecture Assessment

Analyze the codebase structure to understand what needs testing:

```markdown
## Architecture Overview

### Layer Structure
| Layer | Components Found | Testability Assessment |
|-------|-----------------|----------------------|
| UI | [Composables/Activities/Fragments] | [Easy/Medium/Hard] |
| ViewModel | [ViewModels found] | [Easy/Medium/Hard] |
| Domain | [Use cases/Interactors] | [Easy/Medium/Hard] |
| Data | [Repositories, DataSources] | [Easy/Medium/Hard] |

### Dependency Injection
- **Framework:** [Hilt/Koin/Manual/None]
- **Test Injection Ready:** [Yes/No]

### External Dependencies
| Dependency Type | Examples | Testing Approach |
|-----------------|----------|------------------|
| REST APIs | [Services found] | Mock/Fake |
| Local Database | [Room DAOs] | In-memory DB |
| Shared Prefs/DataStore | [Preferences found] | Test implementation |
| Firebase | [Services used] | Emulator/Mock |
```

#### 1.2 Risk-Based Analysis

Identify what's most critical to test:

```markdown
## Critical Path Analysis

### High-Risk Areas (Must Have 90%+ Coverage)
| Area | Reason | Current State |
|------|--------|---------------|
| [Area] | [Why critical] | [Tested/Untested] |

### Medium-Risk Areas (Target 70%+ Coverage)
| Area | Reason | Current State |
|------|--------|---------------|
| [Area] | [Why important] | [Tested/Untested] |

### Low-Risk Areas (Target 50%+ Coverage)
| Area | Reason | Current State |
|------|--------|---------------|
| [Area] | [Why lower priority] | [Tested/Untested] |
```

#### 1.3 Current Test Inventory

If tests exist, catalog them:

```markdown
## Existing Test Inventory

| Test Type | Location | Count | Quality |
|-----------|----------|-------|---------|
| Unit Tests | app/src/test/ | [X] | [Good/Mixed/Poor] |
| Integration Tests | app/src/androidTest/ | [X] | [Good/Mixed/Poor] |
| UI Tests | app/src/androidTest/ | [X] | [Good/Mixed/Poor] |

### Test Quality Issues
- [Issue 1: e.g., "Many tests use Thread.sleep()"]
- [Issue 2: e.g., "Mocking overuse, tests are brittle"]
```

---

### Phase 2: Strategy Design

**CHECKPOINT 1:** Present analysis findings before designing strategy.

```markdown
## Analysis Summary

I've analyzed the codebase. Here's what I found:

### Architecture Testability: [Good/Moderate/Challenging]
[Summary of how easy/hard the codebase is to test]

### Critical Gaps
1. [Gap 1]
2. [Gap 2]

### Key Risks
1. [Risk 1]
2. [Risk 2]

**Any specific areas you want to prioritize or concerns before I design the strategy?**
```

#### 2.1 Test Pyramid Design

```markdown
## Test Pyramid Strategy

```
                    /\
                   /  \
                  / UI \        (10-20% of tests)
                 /------\       Compose UI tests, E2E flows
                /        \
               / Integration\   (20-30% of tests)
              /--------------\  Repository tests, API integration
             /                \
            /    Unit Tests    \ (50-70% of tests)
           /--------------------\ViewModel, UseCase, Utilities
```

### Layer-by-Layer Strategy

#### Unit Tests (Foundation)
| Target | Framework | Approach | Priority |
|--------|-----------|----------|----------|
| ViewModels | JUnit5 + Turbine | Test state changes, event handling | P1 |
| Use Cases | JUnit5 + MockK | Pure function testing | P1 |
| Repositories | JUnit5 + MockK | Contract testing | P1 |
| Mappers/Utils | JUnit5 | Pure function testing | P2 |

#### Integration Tests (Verification)
| Target | Framework | Approach | Priority |
|--------|-----------|----------|----------|
| Database | Room + JUnit4 | In-memory SQLite | P1 |
| API Layer | MockWebServer | Contract testing | P1 |
| Repository → DB | AndroidJUnit | Real dependencies | P2 |

#### UI Tests (Confidence)
| Target | Framework | Approach | Priority |
|--------|-----------|----------|----------|
| Critical Flows | Compose Testing | Happy path verification | P1 |
| Screen States | Compose Testing | State rendering | P2 |
| Navigation | Compose Navigation Testing | Flow verification | P2 |
```

#### 2.2 Testing Toolchain

```markdown
## Recommended Test Stack

### Unit Testing
```kotlin
// build.gradle.kts (app module)
dependencies {
    // JUnit 5
    testImplementation("org.junit.jupiter:junit-jupiter:5.10.1")
    testRuntimeOnly("org.junit.jupiter:junit-jupiter-engine:5.10.1")

    // Kotlin Coroutines Test
    testImplementation("org.jetbrains.kotlinx:kotlinx-coroutines-test:1.7.3")

    // MockK for mocking
    testImplementation("io.mockk:mockk:1.13.8")

    // Turbine for Flow testing
    testImplementation("app.cash.turbine:turbine:1.0.0")

    // Truth for assertions
    testImplementation("com.google.truth:truth:1.1.5")
}
```

### Integration Testing
```kotlin
dependencies {
    // AndroidX Test
    androidTestImplementation("androidx.test:core:1.5.0")
    androidTestImplementation("androidx.test:runner:1.5.2")
    androidTestImplementation("androidx.test:rules:1.5.0")

    // Room Testing
    androidTestImplementation("androidx.room:room-testing:2.6.1")

    // MockWebServer for API testing
    androidTestImplementation("com.squareup.okhttp3:mockwebserver:4.12.0")

    // Hilt Testing (if using Hilt)
    androidTestImplementation("com.google.dagger:hilt-android-testing:2.48.1")
    kspAndroidTest("com.google.dagger:hilt-compiler:2.48.1")
}
```

### UI Testing
```kotlin
dependencies {
    // Compose Testing
    androidTestImplementation("androidx.compose.ui:ui-test-junit4:1.5.4")
    debugImplementation("androidx.compose.ui:ui-test-manifest:1.5.4")

    // Espresso (for hybrid or View-based UI)
    androidTestImplementation("androidx.test.espresso:espresso-core:3.5.1")
}
```
```

#### 2.3 Test Organization

```markdown
## Test Organization Structure

```
app/src/
├── test/                           # Unit tests (JVM)
│   └── kotlin/com/example/app/
│       ├── feature1/
│       │   ├── viewmodel/
│       │   │   └── Feature1ViewModelTest.kt
│       │   └── usecase/
│       │       └── GetFeature1DataUseCaseTest.kt
│       ├── feature2/
│       │   └── ...
│       ├── data/
│       │   └── repository/
│       │       └── SomeRepositoryTest.kt
│       └── util/
│           └── UtilityTest.kt
│
├── androidTest/                    # Instrumented tests
│   └── kotlin/com/example/app/
│       ├── database/
│       │   └── AppDatabaseTest.kt
│       ├── api/
│       │   └── ApiServiceTest.kt
│       └── ui/
│           ├── feature1/
│           │   └── Feature1ScreenTest.kt
│           └── navigation/
│               └── NavigationTest.kt
│
└── sharedTest/                     # Shared test utilities
    └── kotlin/com/example/app/
        ├── fakes/
        │   ├── FakeRepository.kt
        │   └── FakeDataSource.kt
        ├── fixtures/
        │   └── TestFixtures.kt
        └── rules/
            └── MainDispatcherRule.kt
```

### Naming Conventions
- Test classes: `[ClassName]Test.kt`
- Test functions: `[functionName]_[scenario]_[expectedResult]`
- Example: `fetchUser_networkError_returnsFailure()`
```

---

### Phase 3: Implementation Roadmap

**CHECKPOINT 2:** Present strategy for approval before creating roadmap.

```markdown
## Strategy Summary

### Proposed Approach
[Summary of test pyramid and priorities]

### Tool Stack
[Summary of frameworks chosen and why]

### Coverage Targets
| Layer | Target Coverage | Rationale |
|-------|-----------------|-----------|
| ViewModels | 90%+ | Business logic, easy to test |
| Use Cases | 95%+ | Pure logic, must be reliable |
| Repositories | 80%+ | Data contracts |
| UI | Critical flows | High effort, focus on critical paths |

**Does this strategy align with your goals? Any adjustments needed?**
```

#### 3.1 Phased Implementation Plan

```markdown
## Implementation Roadmap

### Phase 1: Foundation (Week 1-2)
**Goal:** Establish testing infrastructure and patterns

| Task | Description | Deliverable |
|------|-------------|-------------|
| Setup dependencies | Add all test dependencies | Updated build.gradle.kts |
| Create test utilities | Dispatcher rule, fixtures | sharedTest/ module |
| Create fakes | Fake implementations for core interfaces | FakeRepository, FakeDataSource |
| Document patterns | Test style guide | TESTING.md |

### Phase 2: Unit Test Coverage (Week 3-4)
**Goal:** Cover core business logic

| Target | Tests to Write | Priority |
|--------|---------------|----------|
| [ViewModel 1] | State changes, event handling | P1 |
| [ViewModel 2] | State changes, event handling | P1 |
| [UseCase 1] | All scenarios | P1 |
| [Repository 1] | Contract tests | P1 |

### Phase 3: Integration Tests (Week 5-6)
**Goal:** Verify component integration

| Target | Tests to Write | Priority |
|--------|---------------|----------|
| Room Database | CRUD operations, migrations | P1 |
| API Service | Response parsing, error handling | P1 |
| Repository Integration | End-to-end data flow | P2 |

### Phase 4: UI Tests (Week 7-8)
**Goal:** Protect critical user flows

| Flow | Screens Covered | Priority |
|------|-----------------|----------|
| [Critical Flow 1] | [Screens] | P1 |
| [Critical Flow 2] | [Screens] | P1 |
| [Secondary Flow] | [Screens] | P2 |

### Phase 5: CI/CD Integration (Week 9)
**Goal:** Automate quality gates

| Task | Description |
|------|-------------|
| Unit tests in CI | Run on every PR |
| Integration tests | Run nightly |
| UI tests | Run before release |
| Coverage reporting | Integrate with PR reviews |
```

#### 3.2 Quality Gates

```markdown
## Quality Gates

### PR Requirements
- [ ] All existing tests pass
- [ ] New code has tests (minimum 80% coverage)
- [ ] No new lint warnings
- [ ] Test naming follows conventions

### Pre-Release Checklist
- [ ] All unit tests pass
- [ ] All integration tests pass
- [ ] Critical flow UI tests pass
- [ ] No regression in coverage percentage

### Coverage Thresholds
| Metric | Minimum | Target |
|--------|---------|--------|
| Line coverage | 60% | 80% |
| Branch coverage | 50% | 70% |
| Critical paths | 90% | 95% |
```

#### 3.3 Maintenance Guidelines

```markdown
## Test Maintenance

### Preventing Flakiness
1. **No Thread.sleep()** - Use Turbine, TestDispatcher, IdlingResources
2. **Deterministic data** - Use fixed test fixtures, not random data
3. **Isolated tests** - Each test independent, no shared mutable state
4. **Retry budgets** - Max 1 retry in CI, investigate any retried test

### Test Review Checklist
- [ ] Tests are independent and isolated
- [ ] Assertions are specific and meaningful
- [ ] Test names describe the scenario and expectation
- [ ] No logic in tests (no if/else, loops in assertions)
- [ ] Appropriate use of mocks vs fakes

### Dealing with Flaky Tests
1. Tag as `@FlakyTest` immediately
2. Create ticket to investigate
3. Disable after 3 failures in one week
4. Fix or delete within 2 weeks
```

---

## Expected Output

### Complete Test Strategy Document

```markdown
# Test Strategy: [App Name]

## 1. Executive Summary
- Testing philosophy and approach
- Key metrics and targets
- Resource requirements

## 2. Test Architecture
- Test pyramid definition
- Layer-by-layer strategy
- Tool stack and rationale

## 3. Test Organization
- Directory structure
- Naming conventions
- Shared utilities

## 4. Implementation Roadmap
- Phased plan with priorities
- Effort estimates
- Dependencies

## 5. Quality Gates
- PR requirements
- Release checklist
- Coverage thresholds

## 6. Maintenance Guidelines
- Flakiness prevention
- Review checklist
- Escalation process

## 7. Appendix
- Test patterns library
- Fixture templates
- Common scenarios
```

---

## Example Interaction

**User:** I need a test strategy for my e-commerce app. It uses MVVM with Clean Architecture, Hilt for DI, and Jetpack Compose for UI. Currently, we have almost no tests.

**Agent:** I'll help design a comprehensive test strategy. Let me ask a few clarifying questions:

1. What are the critical user flows? (e.g., checkout, payment, login)
2. Are there any specific quality concerns that prompted this? (bugs in production, refactoring plans)
3. What CI/CD platform are you using or planning to use?

**User:** Checkout and payment are critical. We've had bugs slip into production, and we want to refactor the cart module. We use GitHub Actions.

**Agent:**

## Analysis Summary

Based on your Clean Architecture + MVVM setup with Hilt, you have excellent testability potential. Here's my analysis:

### Architecture Testability: Good
- Clean Architecture provides clear boundaries for unit testing
- Hilt enables easy test dependency injection
- Compose UI supports isolated component testing

### Critical Gaps
1. **No test infrastructure** - Need to establish patterns and utilities
2. **Cart module at risk** - Planned refactoring without tests is dangerous
3. **Payment flow unprotected** - Highest-risk area has no safety net

### Recommended Approach

**Immediate Priority:** Create cart module tests before refactoring
**Short-term:** Cover checkout and payment flows with unit + integration tests
**Medium-term:** Establish UI tests for critical paths

### Proposed Test Pyramid
- 70% Unit tests: ViewModels, UseCases, Repositories
- 20% Integration tests: Cart repository, Payment API, Database
- 10% UI tests: Checkout flow, Payment flow

Shall I proceed with the detailed strategy and implementation roadmap?

---

## Techniques Used

- **ST-01** (Clear Objective): Focused on practical test strategy design
- **ST-02** (Sequential Instructions): Phased approach from analysis to roadmap
- **RT-02** (Multi-Dimensional Analysis): Coverage of architecture, risk, and maintenance
- **RT-04** (Best Practice Review): Android testing best practices and patterns
- **ST-03** (Output Format Templates): Structured strategy document format
- **DS-06** (Prioritization Guidance): Risk-based prioritization
- **NE-01** (Single-Question Pacing): Context gathering before analysis
- **NE-02** (Phased Workflow): Clear phases with checkpoint approvals
- **NE-07** (Discussion Before Action): Checkpoints for user feedback
- **AG-12** (Quantitative Metrics): Coverage targets and quality gates

---

## Related Prompts

- [android_codebase_health_assessment.md](../analysis/android_codebase_health_assessment.md) - Assess overall codebase before testing
- [android_test_coverage_analysis.md](../analysis/android_test_coverage_analysis.md) - Analyze existing test coverage
- [android_unit_test_generation.md](android_unit_test_generation.md) - Generate unit tests from strategy
- [android_compose_ui_testing.md](android_compose_ui_testing.md) - Implement Compose UI tests
- [android_integration_testing.md](android_integration_testing.md) - Implement integration tests

---

## Customization Guide

### For Different Project Sizes

**Small Project (1-3 developers):**
- Simplify to unit + critical UI tests only
- Skip formal documentation, focus on patterns
- Lighter quality gates

**Large Project (10+ developers):**
- Add contract testing for module boundaries
- Include mutation testing for critical paths
- Formal review process for test changes

### For Different Risk Profiles

**High Risk (fintech, health):**
- Higher coverage targets (90%+ overall)
- Mandatory UI tests for all flows
- Include security testing layer

**Low Risk (utility, content apps):**
- Focus on unit tests for business logic
- UI tests only for happy paths
- Lighter integration testing

### For Legacy Codebases

**High Technical Debt:**
- Start with characterization tests
- Focus on refactoring targets first
- Incremental coverage improvement
- Consider seams for testability

### For Different CI Environments

**GitHub Actions:**
- Parallel test execution
- Matrix testing for API levels
- Coverage upload to Codecov

**GitLab CI:**
- Similar parallel execution
- Built-in coverage visualization
- Integration with merge requests

**Local Only:**
- Pre-commit hooks for unit tests
- Manual checklists for integration/UI
- Local coverage reports
