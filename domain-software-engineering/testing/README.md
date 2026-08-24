# Testing Prompts

Comprehensive prompts for test generation, coverage analysis, and quality assurance across all testing types.

**Total Prompts:** 16

---

## Prompts

| Prompt | When to Use |
|--------|-------------|
| `testing_unit_test_generation.md` | Generate unit tests for functions/classes |
| `testing_integration_test_design.md` | Design integration test suites |
| `testing_e2e_test_scenario_creation.md` | Create end-to-end test scenarios (Playwright, Cypress) |
| `testing_contract_test_design.md` | Design contract tests (OpenAPI / AsyncAPI / Pact) |
| `testing_property_based_fuzzing.md` | Design property-based + fuzz tests (Hypothesis, libFuzzer, AFL++) |
| `testing_chaos_engineering_plan.md` | Design chaos-engineering experiments (Chaos Mesh, AWS FIS) |
| `testing_coverage_gap_analysis.md` | Identify untested code paths |
| `testing_test_data_generation.md` | Generate test fixtures and mock data |
| `testing_accessibility_wcag.md` | WCAG accessibility testing with axe-core |
| `testing_visual_regression.md` | Visual regression testing setup |
| `testing_performance_load_test_planning.md` | Plan load and stress tests |
| `testing_security_testing.md` | Security-focused test cases |
| `testing_mutation_testing.md` | Mutation testing to verify test quality |
| `testing_flaky_test_detection.md` | Identify and fix flaky tests |
| `testing_refactoring_maintenance.md` | Maintain tests during refactoring |
| `testing_workflow_guide.md` | Overall testing workflow guide (reference) |

---

## By Testing Type

### Unit Testing
- `testing_unit_test_generation.md` - Generate unit tests with AAA pattern
- `testing_mutation_testing.md` - Verify test effectiveness

### Integration Testing
- `testing_integration_test_design.md` - API and service integration tests
- `testing_test_data_generation.md` - Create test fixtures

### End-to-End Testing
- `testing_e2e_test_scenario_creation.md` - Playwright/Cypress E2E tests
- `testing_visual_regression.md` - Screenshot comparison tests

### Specialized Testing
- `testing_accessibility_wcag.md` - WCAG compliance testing
- `testing_security_testing.md` - Security test cases
- `testing_performance_load_test_planning.md` - Load testing plans

### Test Maintenance
- `testing_coverage_gap_analysis.md` - Find missing coverage
- `testing_flaky_test_detection.md` - Fix unreliable tests
- `testing_refactoring_maintenance.md` - Update tests with code changes

---

## Quick Selection Guide

**"Generate tests for my code"** → `testing_unit_test_generation.md`

**"What's not tested?"** → `testing_coverage_gap_analysis.md`

**"E2E tests for user flows"** → `testing_e2e_test_scenario_creation.md`

**"Check accessibility"** → `testing_accessibility_wcag.md`

**"Tests keep failing randomly"** → `testing_flaky_test_detection.md`

**"Plan load testing"** → `testing_performance_load_test_planning.md`

**"Security test cases"** → `testing_security_testing.md`

---

## Related Categories

- **Code Analysis** - Analyze code before writing tests
- **[DevOps](../devops/)** - CI/CD pipeline integration
- **[Engineering](../../domain-agentic-resources/personas/engineering/)** - Development workflows
- **Mobile Development** - Mobile-specific testing

---

## Highlights

### testing_e2e_test_scenario_creation.md (10/10)
Complete Playwright code examples, Page Object Model patterns, and CI/CD configuration. Production-ready E2E testing.

### testing_accessibility_wcag.md (10/10)
WCAG 2.1 framework integration, axe-core test examples, and screen reader compatibility checklist.
