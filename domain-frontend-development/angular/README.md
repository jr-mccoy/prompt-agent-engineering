# Angular Prompts

**Category:** Frontend Development / Angular
**Prompts:** 3

---

## Overview

Production-grade prompts for Angular development covering architecture, reactive patterns (Signals + RxJS), and testing strategies. All prompts support Angular 14+ with emphasis on modern Angular features.

## Prompts

| Prompt | Description | Difficulty |
|--------|-------------|------------|
| [frontend_angular_architecture.md](frontend_angular_architecture.md) | Analyze Angular codebases for architecture patterns, standalone components, DI design, and module organization | Intermediate |
| [frontend_angular_reactive_patterns.md](frontend_angular_reactive_patterns.md) | Evaluate RxJS usage, Signals adoption, state management, and subscription management | Intermediate |
| [frontend_angular_testing.md](frontend_angular_testing.md) | Review testing patterns, TestBed configuration, and test suite performance | Intermediate |

## Usage Examples

### Reviewing Angular Architecture
Use `frontend_angular_architecture.md` to analyze:
- Standalone vs NgModule adoption
- Component organization and change detection strategy
- Dependency injection design and service layering
- Routing and lazy loading patterns

### Evaluating Reactive Patterns
Use `frontend_angular_reactive_patterns.md` to identify:
- Subscription leaks and RxJS anti-patterns
- Signals adoption opportunities
- State management approach evaluation
- BehaviorSubject to Signal migration paths

### Auditing Test Quality
Use `frontend_angular_testing.md` to find:
- Over-configured TestBed slowing test suites
- Tests that pass but don't verify behavior
- Missing coverage on critical business logic
- Flaky async test patterns

---

## Related Prompts

- [../testing/frontend_testing_jest.md](../testing/frontend_testing_jest.md) - General Jest patterns
- [../testing/frontend_testing_playwright.md](../testing/frontend_testing_playwright.md) - E2E testing
- [../performance/frontend_performance_core_web_vitals.md](../performance/frontend_performance_core_web_vitals.md) - Performance optimization
