# Svelte / SvelteKit Prompts

**Category:** Frontend Development / Svelte
**Prompts:** 3

---

## Overview

Production-grade prompts for Svelte and SvelteKit development covering component patterns with Svelte 5 runes, SvelteKit full-stack architecture, and state management strategies. All prompts support both Svelte 4 and Svelte 5 with clear migration guidance.

## Prompts

| Prompt | Description | Difficulty |
|--------|-------------|------------|
| [frontend_svelte_component_patterns.md](frontend_svelte_component_patterns.md) | Analyze Svelte codebases for component architecture, runes adoption, reactivity patterns, and composition | Intermediate |
| [frontend_sveltekit_fullstack.md](frontend_sveltekit_fullstack.md) | Review SvelteKit routing, load functions, form actions, server hooks, and security | Intermediate |
| [frontend_svelte_state_management.md](frontend_svelte_state_management.md) | Evaluate state management patterns including stores, rune-based state, context, and SSR safety | Intermediate |

## Usage Examples

### Reviewing Svelte Component Patterns
Use `frontend_svelte_component_patterns.md` to analyze:
- Svelte 5 runes adoption progress
- Reactivity bugs (object mutations, missing cleanup)
- Component composition (slots vs snippets)
- Store-to-runes migration opportunities

### Auditing SvelteKit Architecture
Use `frontend_sveltekit_fullstack.md` to identify:
- Load function waterfalls and data exposure issues
- Missing server-side form validation
- Auth hook vulnerabilities
- Progressive enhancement gaps

### Evaluating State Management
Use `frontend_svelte_state_management.md` to find:
- God stores handling too many concerns
- SSR state leaks between requests
- Manual state synchronization that should use `$derived`
- Missing SSR guards for browser-only APIs

---

## Related Prompts

- [../react/frontend_react_component_patterns.md](../react/frontend_react_component_patterns.md) - React component patterns
- [../vue/frontend_vue_composition_api.md](../vue/frontend_vue_composition_api.md) - Vue composition patterns
- [../nextjs/frontend_nextjs_app_router.md](../nextjs/frontend_nextjs_app_router.md) - Similar full-stack analysis for Next.js
- [../performance/frontend_performance_core_web_vitals.md](../performance/frontend_performance_core_web_vitals.md) - Performance optimization
