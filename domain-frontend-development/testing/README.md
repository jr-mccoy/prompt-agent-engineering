# Testing Prompts

**Category:** Frontend Development / Testing
**Prompts:** 3

---

## Overview

Production-grade prompts for frontend testing covering Jest unit testing patterns, Playwright end-to-end testing, and the API mocking strategy shared across test layers.

## Prompts

| Prompt | Description | Difficulty |
|--------|-------------|------------|
| [frontend_testing_jest.md](frontend_testing_jest.md) | Comprehensive Jest testing patterns including mocking, async testing, and organization | Intermediate |
| [frontend_testing_playwright.md](frontend_testing_playwright.md) | Playwright E2E testing with page objects, fixtures, and CI/CD integration | Intermediate |
| [frontend_testing_api_mocking_strategy.md](frontend_testing_api_mocking_strategy.md) | One network-level mock layer across unit, component, Storybook, dev and E2E; handlers typed and fixtures validated against the API contract; unhandled requests fail; error-state coverage; which journeys stay real | Intermediate |

## Usage Examples

### Jest Unit Testing
Use `frontend_testing_jest.md` for:
- Jest configuration setup
- Mocking strategies (modules, fetch, timers)
- Async testing patterns
- Test organization and naming
- Common anti-patterns to avoid

### Playwright E2E Testing
Use `frontend_testing_playwright.md` for:
- Page Object Model implementation
- Cross-browser testing configuration
- Test fixtures and data management
- Visual regression testing
- CI/CD pipeline integration

### API Mocking Strategy
Use `frontend_testing_api_mocking_strategy.md` when tests pass but production breaks on API shape changes, or the same endpoint is mocked several different ways.

---

## Testing Pyramid

```
                    ▲
                   ╱ ╲
                  ╱ E2E╲              5%  - Playwright
                 ╱ (10) ╲
                ╱─────────╲
               ╱Integration╲          25% - Component + API
              ╱   (50+)     ╲
             ╱───────────────╲
            ╱   Component      ╲       40% - React/Vue Testing Library
           ╱     (100+)         ╲
          ╱─────────────────────╲
         ╱       Unit             ╲    30% - Jest/Vitest
        ╱        (80+)              ╲
       ╱─────────────────────────────╲
```

---

## Related Prompts

- [../react/frontend_react_testing.md](../react/frontend_react_testing.md) - React-specific testing
- [../vue/frontend_vue_testing.md](../vue/frontend_vue_testing.md) - Vue-specific testing
- [../../domain-software-engineering/testing/](../../domain-software-engineering/testing/) - Additional testing prompts
