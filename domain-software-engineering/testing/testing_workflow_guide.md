---
title: "Testing Workflow Guide"
category: testing
description: "Testing Workflow Guide."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - QA-01
difficulty: beginner
tags:
  - guide
  - testing
  - workflow
updated: "2026-04-03"
related_prompts: []
artifact_type: "reference"
---

# Testing Workflow Guide

**Purpose:** This guide shows how to use the testing prompts in combination to build a comprehensive testing strategy for your application.

---

## Testing Prompts Overview

The testing category includes 11 comprehensive prompts covering the entire testing lifecycle:

1. **testing_unit_test_generation.md** - Create unit tests for functions and classes
2. **testing_integration_test_design.md** - Design tests for component interactions
3. **testing_e2e_test_scenario_creation.md** - Create end-to-end user journey tests
4. **testing_performance_load_test_planning.md** - Plan performance and load testing
5. **testing_coverage_gap_analysis.md** - Identify untested code and scenarios
6. **testing_mutation_testing.md** - Verify test quality and effectiveness
7. **testing_visual_regression.md** - Detect unintended UI changes
8. **testing_accessibility_wcag.md** - Ensure WCAG accessibility compliance
9. **testing_flaky_test_detection.md** - Identify and fix unreliable tests
10. **testing_refactoring_maintenance.md** - Improve test code quality
11. **performance_test_scenario_generation.md** - (in code-analysis/performance/)

---

## Workflow 1: Building Tests for New Feature

**Scenario**: You're building a new checkout feature for an e-commerce site.

### Step 1: Start with Unit Tests
**Prompt**: `testing_unit_test_generation.md`

Create unit tests for individual components:
- Payment calculator functions
- Cart total calculation
- Discount application logic
- Tax calculation

**Output**: Comprehensive unit test suite with 80%+ coverage

### Step 2: Add Integration Tests
**Prompt**: `testing_integration_test_design.md`

Test component interactions:
- Cart service ↔ Product service
- Order service ↔ Payment service
- Order service ↔ Database

**Output**: Integration tests covering service interactions

### Step 3: Create E2E Test Scenarios
**Prompt**: `testing_e2e_test_scenario_creation.md`

Test complete user journeys:
- Browse products → Add to cart → Checkout → Payment
- Apply discount code during checkout
- Handle payment failure gracefully

**Output**: E2E test scenarios covering critical user flows

### Step 4: Add Accessibility Tests
**Prompt**: `testing_accessibility_wcag.md`

Ensure checkout is accessible:
- Keyboard navigation through checkout
- Screen reader announcements for errors
- Form label associations

**Output**: WCAG 2.1 AA compliant checkout flow

### Step 5: Check for Visual Regressions
**Prompt**: `testing_visual_regression.md`

Capture baseline screenshots:
- Checkout form in different states
- Payment confirmation page
- Error states

**Output**: Visual regression test suite

---

## Workflow 2: Improving Existing Test Suite

**Scenario**: Your test suite has low quality and reliability issues.

### Step 1: Analyze Coverage Gaps
**Prompt**: `testing_coverage_gap_analysis.md`

Identify what's not tested:
- Functions with no tests
- Missing edge cases
- Untested error paths

**Output**: Prioritized list of coverage gaps

### Step 2: Fix Flaky Tests
**Prompt**: `testing_flaky_test_detection.md`

Find and fix unreliable tests:
- Tests that fail intermittently
- Timing-related failures
- Test isolation issues

**Output**: Stable, reliable test suite

### Step 3: Improve Test Quality
**Prompt**: `testing_mutation_testing.md`

Verify tests actually catch bugs:
- Run mutation testing on critical code
- Identify weak tests
- Add missing assertions

**Output**: Higher quality tests with 80%+ mutation score

### Step 4: Refactor Tests
**Prompt**: `testing_refactoring_maintenance.md`

Improve test code:
- Remove duplication
- Extract test utilities
- Improve naming
- Add parameterized tests

**Output**: Clean, maintainable test code

---

## Workflow 3: Pre-Release Testing Checklist

**Scenario**: Preparing for a major production release.

### 1. Unit Test Coverage
- [ ] Run `testing_coverage_gap_analysis.md`
- [ ] Ensure critical code has 80%+ coverage
- [ ] No coverage gaps in business logic

### 2. Integration Testing
- [ ] Run `testing_integration_test_design.md`
- [ ] All service interactions tested
- [ ] Database operations tested
- [ ] External API integrations tested

### 3. E2E Testing
- [ ] Run `testing_e2e_test_scenario_creation.md`
- [ ] All critical user journeys covered
- [ ] Error scenarios tested
- [ ] Cross-browser testing complete

### 4. Performance Testing
- [ ] Run `testing_performance_load_test_planning.md`
- [ ] Load tests pass at expected traffic
- [ ] Response times meet SLAs
- [ ] No performance regressions

### 5. Accessibility Testing
- [ ] Run `testing_accessibility_wcag.md`
- [ ] WCAG 2.1 AA compliance verified
- [ ] Keyboard navigation works
- [ ] Screen reader tested

### 6. Visual Regression Testing
- [ ] Run `testing_visual_regression.md`
- [ ] No unintended UI changes
- [ ] All visual differences approved
- [ ] Baseline updated for intentional changes

### 7. Test Suite Health
- [ ] Run `testing_flaky_test_detection.md`
- [ ] All flaky tests fixed
- [ ] Test success rate > 99%
- [ ] CI/CD pipeline stable

---

## Workflow 4: Continuous Quality Improvement

**Schedule**: Ongoing maintenance activities

### Weekly
- Monitor test flakiness rate
- Review failed tests in CI/CD
- Update flaky test tracking

**Prompts**: `testing_flaky_test_detection.md`

### Bi-Weekly
- Review test coverage trends
- Add tests for new code
- Refactor poorly written tests

**Prompts**: `testing_coverage_gap_analysis.md`, `testing_refactoring_maintenance.md`

### Monthly
- Run mutation testing on critical modules
- Performance test against production-like data
- Accessibility audit of new features

**Prompts**: `testing_mutation_testing.md`, `testing_performance_load_test_planning.md`, `testing_accessibility_wcag.md`

### Quarterly
- Full test suite refactoring review
- Visual regression baseline updates
- Comprehensive E2E test review

**Prompts**: All testing prompts

---

## Testing Pyramid Strategy

Use prompts in this proportion:

```
        ╱╲
       ╱E2E╲         10% - testing_e2e_test_scenario_creation.md
      ╱─────╲                testing_visual_regression.md
     ╱Integr╲        20% - testing_integration_test_design.md
    ╱─────────╲
   ╱   Unit    ╲     70% - testing_unit_test_generation.md
  ╱─────────────╲
```

**Support Prompts** (applied across all levels):
- testing_coverage_gap_analysis.md
- testing_mutation_testing.md
- testing_accessibility_wcag.md
- testing_flaky_test_detection.md
- testing_refactoring_maintenance.md

---

## Prompt Combinations for Common Scenarios

### Scenario: Testing a REST API
1. `testing_unit_test_generation.md` - Controller and service logic
2. `testing_integration_test_design.md` - API routes with database
3. `testing_performance_load_test_planning.md` - API performance under load
4. `security_api_testing.md` - API security validation

### Scenario: Testing a React Component Library
1. `testing_unit_test_generation.md` - Component logic and hooks
2. `testing_visual_regression.md` - Component appearance (Storybook)
3. `testing_accessibility_wcag.md` - Component accessibility
4. `testing_refactoring_maintenance.md` - Maintain test quality

### Scenario: Testing a Data Processing Pipeline
1. `testing_unit_test_generation.md` - Transform functions
2. `testing_integration_test_design.md` - Pipeline stages
3. `testing_performance_load_test_planning.md` - Processing throughput
4. `testing_coverage_gap_analysis.md` - Edge cases and error handling

---

## Metrics and Success Criteria

Track these metrics using insights from the prompts:

| Metric | Target | Prompt to Use |
|--------|--------|---------------|
| Unit Test Coverage | 80%+ | testing_coverage_gap_analysis.md |
| Mutation Score | 75%+ | testing_mutation_testing.md |
| Test Flakiness Rate | <1% | testing_flaky_test_detection.md |
| E2E Test Coverage | 100% critical paths | testing_e2e_test_scenario_creation.md |
| WCAG Compliance | Level AA | testing_accessibility_wcag.md |
| Visual Regression | 0 unintended changes | testing_visual_regression.md |
| Performance SLA | <500ms p95 | testing_performance_load_test_planning.md |

---

## Integration with Development Workflow

### Pull Request Checklist
- [ ] Unit tests added for new code (`testing_unit_test_generation.md`)
- [ ] Integration tests for new interactions (`testing_integration_test_design.md`)
- [ ] No coverage decrease (`testing_coverage_gap_analysis.md`)
- [ ] All tests passing and stable (`testing_flaky_test_detection.md`)

### Code Review Focus
- [ ] Test quality and readability (`testing_refactoring_maintenance.md`)
- [ ] Accessibility tested if UI change (`testing_accessibility_wcag.md`)
- [ ] Visual regression checked (`testing_visual_regression.md`)
- [ ] Edge cases covered (`testing_coverage_gap_analysis.md`)

### CI/CD Pipeline
```
┌─────────────────────┐
│  Unit Tests (Fast)  │ → testing_unit_test_generation.md
├─────────────────────┤
│ Integration Tests   │ → testing_integration_test_design.md
├─────────────────────┤
│   E2E Tests (PR)    │ → testing_e2e_test_scenario_creation.md
├─────────────────────┤
│ Visual Regression   │ → testing_visual_regression.md
├─────────────────────┤
│ Accessibility Audit │ → testing_accessibility_wcag.md
├─────────────────────┤
│ Performance Tests   │ → testing_performance_load_test_planning.md
│   (Nightly)         │
└─────────────────────┘
```

---

## Quick Reference

**Need to test a function?**
→ `testing_unit_test_generation.md`

**Need to test service interactions?**
→ `testing_integration_test_design.md`

**Need to test user workflows?**
→ `testing_e2e_test_scenario_creation.md`

**Tests passing but bugs still appear?**
→ `testing_mutation_testing.md`

**Low code coverage?**
→ `testing_coverage_gap_analysis.md`

**Tests failing randomly?**
→ `testing_flaky_test_detection.md`

**Tests hard to maintain?**
→ `testing_refactoring_maintenance.md`

**Need to verify performance?**
→ `testing_performance_load_test_planning.md`

**Need to check accessibility?**
→ `testing_accessibility_wcag.md`

**UI changes to verify?**
→ `testing_visual_regression.md`

---

## Getting Started

**New Project** (no tests yet):
1. Start with `testing_unit_test_generation.md` for core business logic
2. Add `testing_integration_test_design.md` for API/database tests
3. Create `testing_e2e_test_scenario_creation.md` for critical flows
4. Establish quality baseline with `testing_coverage_gap_analysis.md`

**Existing Project** (improving tests):
1. Run `testing_coverage_gap_analysis.md` to find gaps
2. Use `testing_flaky_test_detection.md` to stabilize suite
3. Apply `testing_refactoring_maintenance.md` to clean up tests
4. Verify quality with `testing_mutation_testing.md`

**Production System** (comprehensive testing):
- Use all prompts in the Testing Pyramid strategy
- Schedule regular quality audits
- Integrate into CI/CD pipeline
- Track metrics over time

---

## Techniques Used

This guide demonstrates the following prompting techniques:

- **ST-01** (Clear Objective Statement) - Clear purpose statement explaining guide objectives
- **ST-02** (Structured Sequential Instructions) - Multiple workflows with numbered steps
- **DT-02** (Specific Focus Areas with Examples) - Concrete scenarios for different use cases
- **DS-02** (Metric Specification) - Metrics table with targets and tracking methods
- **DS-06** (Prioritization and Severity Guidance) - Testing pyramid strategy showing test distribution
- **ST-03** (Output Format Templates) - Checklists for PRs, code reviews, and CI/CD integration
- **DS-03** (Tool and Methodology Suggestions) - Prompt recommendations for different testing scenarios


## AI Coding Agent Adaptation (Prompt-Only Mode)

When using this guide with coding agents (for example Codex or Claude Code), keep each prompt invocation bounded:

- Provide a **target scope** (`src/payments/**` not the whole monorepo).
- Require **failing tests first** before patch generation.
- Require **minimal diffs** and explicit non-goals.
- Require command output for every claimed fix.

Suggested wrapper to prepend before any testing prompt:

```
You are operating as a coding agent in prompt-only mode (not a reusable skill).
Work only in: <paths>.
First produce a plan, then implement the smallest safe change set.
After edits, run: <commands>.
Return: changed files, test evidence, residual risk.
```
