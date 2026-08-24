# Vue Prompts

**Category:** Frontend Development / Vue
**Prompts:** 3

---

## Overview

Production-grade prompts for Vue 3 development covering Composition API patterns, Pinia state management, and testing strategies.

## Prompts

| Prompt | Description | Difficulty |
|--------|-------------|------------|
| [frontend_vue_composition_api.md](frontend_vue_composition_api.md) | Analyze Vue 3 codebases for Composition API patterns, composable design, and reactivity issues | Intermediate |
| [frontend_vue_pinia_state.md](frontend_vue_pinia_state.md) | Audit Pinia store architecture for design patterns and best practices | Intermediate |
| [frontend_vue_testing.md](frontend_vue_testing.md) | Design comprehensive testing strategies for Vue components and composables | Intermediate |

## Usage Examples

### Reviewing Vue 3 Code
Use `frontend_vue_composition_api.md` to identify:
- Reactivity bugs (lost refs, broken watchers)
- Composable extraction opportunities
- Migration paths from Options API
- Script setup adoption

### Auditing Pinia Stores
Use `frontend_vue_pinia_state.md` to find:
- God stores that need splitting
- Circular dependencies
- Missing `storeToRefs` usage
- Anti-patterns

### Setting Up Testing
Use `frontend_vue_testing.md` for:
- Vitest configuration
- Component testing patterns
- Composable testing
- Store testing

---

## Related Prompts

- [../testing/frontend_testing_jest.md](../testing/frontend_testing_jest.md) - General Jest patterns
- [../react/frontend_react_state_management.md](../react/frontend_react_state_management.md) - State management concepts
