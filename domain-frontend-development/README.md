# Frontend Development Domain

**Purpose:** Comprehensive prompt collection for frontend development covering frameworks (React, Vue, Angular, Next.js, Svelte/SvelteKit, Astro, SolidJS, Qwik, Remix), cross-cutting craft (styling, TypeScript, forms, animation, architecture), build tooling, accessibility, performance, and testing.

**Total Resources:** 47 prompts across 18 categories

---

## Overview

This domain provides production-grade prompts for modern frontend development, organized by technology and concern. All prompts follow Tier 1 quality standards with false-positive prevention, confidence levels, detailed examples, and cross-references.

## Categories

### Frameworks

| Category | Prompts | Focus |
|----------|---------|-------|
| [react/](react/) | 6 | Component patterns, hooks, state, testing, performance, Server Components & streaming |
| [vue/](vue/) | 4 | Composition API, Pinia state, testing, advanced reactivity & performance |
| [angular/](angular/) | 4 | Architecture, Signals/RxJS reactive patterns, testing, advanced signals |
| [nextjs/](nextjs/) | 4 | App Router, data fetching/caching, performance, Server Actions & mutations |
| [svelte/](svelte/) | 3 | Component patterns/runes, SvelteKit full-stack, state management |
| [astro/](astro/) | 2 | Islands architecture & partial hydration, content collections |
| [solidjs/](solidjs/) | 1 | Fine-grained reactivity patterns |
| [qwik/](qwik/) | 1 | Resumability & lazy-execution |
| [remix/](remix/) | 1 | Data loading & mutations (Remix / React Router) |

### Cross-Cutting Craft (framework-agnostic)

| Category | Prompts | Focus |
|----------|---------|-------|
| [styling/](styling/) | 3 | CSS architecture/scalability, Tailwind design system, CSS-in-JS runtime cost |
| [typescript/](typescript/) | 2 | Component/props typing, type-safety audit |
| [forms/](forms/) | 2 | Validation strategy, accessible form UX |
| [animation/](animation/) | 1 | Motion & animation performance |
| [architecture/](architecture/) | 3 | Error boundaries/resilience, state-management selection, i18n/localization |
| [build-tooling/](build-tooling/) | 3 | Vite optimization, micro-frontends/Module Federation, bundler migration |

### Quality Concerns

| Category | Prompts | Focus |
|----------|---------|-------|
| [accessibility/](accessibility/) | 3 | WCAG audits, ARIA patterns, screen reader testing |
| [performance/](performance/) | 2 | Core Web Vitals, bundle optimization |
| [testing/](testing/) | 2 | Jest unit testing, Playwright E2E |

---

## Quick Reference

### By Task

| Task | Prompt |
|------|--------|
| Review React component architecture | [frontend_react_component_patterns.md](react/frontend_react_component_patterns.md) |
| Audit hooks for bugs | [frontend_react_hooks_best_practices.md](react/frontend_react_hooks_best_practices.md) |
| Choose React state management | [frontend_react_state_management.md](react/frontend_react_state_management.md) |
| Design React test strategy | [frontend_react_testing.md](react/frontend_react_testing.md) |
| Optimize React performance | [frontend_react_performance.md](react/frontend_react_performance.md) |
| Audit React Server Components & streaming | [frontend_react_server_components_streaming.md](react/frontend_react_server_components_streaming.md) |
| Review Vue 3 patterns | [frontend_vue_composition_api.md](vue/frontend_vue_composition_api.md) |
| Audit Pinia stores | [frontend_vue_pinia_state.md](vue/frontend_vue_pinia_state.md) |
| Test Vue components | [frontend_vue_testing.md](vue/frontend_vue_testing.md) |
| Audit Vue reactivity & performance | [frontend_vue_advanced_reactivity_performance.md](vue/frontend_vue_advanced_reactivity_performance.md) |
| Review Angular architecture | [frontend_angular_architecture.md](angular/frontend_angular_architecture.md) |
| Evaluate Angular Signals/RxJS | [frontend_angular_reactive_patterns.md](angular/frontend_angular_reactive_patterns.md) |
| Audit Angular tests | [frontend_angular_testing.md](angular/frontend_angular_testing.md) |
| Audit advanced Angular signals / zoneless | [frontend_angular_signals_advanced.md](angular/frontend_angular_signals_advanced.md) |
| Review Next.js App Router | [frontend_nextjs_app_router.md](nextjs/frontend_nextjs_app_router.md) |
| Audit Next.js data fetching | [frontend_nextjs_data_fetching.md](nextjs/frontend_nextjs_data_fetching.md) |
| Optimize Next.js performance | [frontend_nextjs_performance.md](nextjs/frontend_nextjs_performance.md) |
| Audit Next.js Server Actions & mutations | [frontend_nextjs_server_actions_mutations.md](nextjs/frontend_nextjs_server_actions_mutations.md) |
| Review Svelte/runes patterns | [frontend_svelte_component_patterns.md](svelte/frontend_svelte_component_patterns.md) |
| Audit SvelteKit architecture | [frontend_sveltekit_fullstack.md](svelte/frontend_sveltekit_fullstack.md) |
| Evaluate Svelte state management | [frontend_svelte_state_management.md](svelte/frontend_svelte_state_management.md) |
| Audit Astro islands & hydration | [frontend_astro_islands_architecture.md](astro/frontend_astro_islands_architecture.md) |
| Review Astro content collections | [frontend_astro_content_collections.md](astro/frontend_astro_content_collections.md) |
| Analyze SolidJS reactivity | [frontend_solidjs_reactivity_patterns.md](solidjs/frontend_solidjs_reactivity_patterns.md) |
| Audit Qwik resumability | [frontend_qwik_resumability.md](qwik/frontend_qwik_resumability.md) |
| Review Remix/React Router data loading | [frontend_remix_data_loading.md](remix/frontend_remix_data_loading.md) |
| Audit CSS architecture & scalability | [frontend_styling_css_architecture.md](styling/frontend_styling_css_architecture.md) |
| Treat Tailwind config as a design system | [frontend_styling_tailwind_design_system.md](styling/frontend_styling_tailwind_design_system.md) |
| Review CSS-in-JS runtime cost | [frontend_styling_css_in_js_review.md](styling/frontend_styling_css_in_js_review.md) |
| Type components & props well | [frontend_typescript_component_typing.md](typescript/frontend_typescript_component_typing.md) |
| Audit frontend type safety | [frontend_typescript_type_safety_audit.md](typescript/frontend_typescript_type_safety_audit.md) |
| Design form validation | [frontend_forms_validation_design.md](forms/frontend_forms_validation_design.md) |
| Audit accessible form UX | [frontend_forms_accessibility_ux.md](forms/frontend_forms_accessibility_ux.md) |
| Audit animation & motion performance | [frontend_animation_motion_performance.md](animation/frontend_animation_motion_performance.md) |
| Design error boundaries & resilience | [frontend_error_boundary_resilience.md](architecture/frontend_error_boundary_resilience.md) |
| Select a state-management approach | [frontend_state_management_selection.md](architecture/frontend_state_management_selection.md) |
| Architect i18n / localization | [frontend_i18n_localization.md](architecture/frontend_i18n_localization.md) |
| Optimize a Vite build | [frontend_build_vite_optimization.md](build-tooling/frontend_build_vite_optimization.md) |
| Design micro-frontends / Module Federation | [frontend_build_micro_frontends_module_federation.md](build-tooling/frontend_build_micro_frontends_module_federation.md) |
| Plan a bundler migration | [frontend_build_bundler_migration.md](build-tooling/frontend_build_bundler_migration.md) |
| Conduct WCAG audit | [frontend_accessibility_wcag_audit.md](accessibility/frontend_accessibility_wcag_audit.md) |
| Implement ARIA patterns | [frontend_accessibility_aria_patterns.md](accessibility/frontend_accessibility_aria_patterns.md) |
| Test with screen readers | [frontend_accessibility_screen_reader.md](accessibility/frontend_accessibility_screen_reader.md) |
| Optimize Core Web Vitals | [frontend_performance_core_web_vitals.md](performance/frontend_performance_core_web_vitals.md) |
| Reduce bundle size | [frontend_performance_bundle_optimization.md](performance/frontend_performance_bundle_optimization.md) |
| Set up Jest testing | [frontend_testing_jest.md](testing/frontend_testing_jest.md) |
| Create E2E tests | [frontend_testing_playwright.md](testing/frontend_testing_playwright.md) |

### By Technology

**React:** component patterns, hooks, state management (Redux/Zustand/Jotai/Context), Testing Library, performance, Server Components & streaming SSR.

**Vue:** Composition API, composables, Pinia stores, Vue Test Utils, advanced reactivity (`ref`/`reactive`/`shallowRef`) and render performance.

**Angular:** standalone components, Signals & RxJS, dependency injection, TestBed, advanced signals interop and zoneless change detection.

**Next.js:** App Router server/client boundaries, data fetching/caching/revalidation, rendering strategy, Server Actions & mutations.

**Svelte / SvelteKit:** runes & reactivity, composition, routing/load/form-actions, state management, SSR safety.

**Astro / SolidJS / Qwik / Remix:** server-first islands & partial hydration, type-safe content collections, fine-grained reactivity, resumability vs hydration, loader/action data flows with progressive enhancement.

**Styling:** CSS architecture (BEM/ITCSS/utility-first, cascade layers, tokens), Tailwind as a design system, CSS-in-JS runtime cost and SSR.

**TypeScript:** precise component/props/generics typing across frameworks, and codebase-wide type-safety audits.

**Forms / Animation / Architecture:** schema validation and accessible form UX; GPU-friendly, reduced-motion animation; error boundaries, state-management selection, and i18n/localization.

**Build Tooling:** Vite config optimization, micro-frontends / Module Federation, and bundler migration.

**Accessibility / Performance / Testing:** WCAG/ARIA/screen-reader audits; Core Web Vitals and bundle optimization; Jest and Playwright.

---

## Prompt Quality

All prompts in this domain follow **Tier 1 (Production-Grade)** standards:

- Clear objective and instructions
- False-Positive Prevention sections
- Confidence levels for findings
- 100+ line example outputs
- Techniques documented
- `related_prompts` cross-references in frontmatter and body

---

## Getting Started

1. **Identify your need** using the task table above
2. **Read the prompt** and understand the methodology
3. **Execute** the prompt with your codebase context
4. **Follow cross-references** in each prompt's Related Prompts section

---

## Related Resources

- [domain-software-engineering/testing/](../domain-software-engineering/testing/) - Additional testing prompts
- [domain-agentic-resources/skills/frontend-mobile/](../domain-agentic-resources/agents/frontend-mobile/) - Frontend skills for Claude Code
- [techniques/MASTER_TECHNIQUE_INDEX.md](../techniques/MASTER_TECHNIQUE_INDEX.md) - Prompt engineering techniques

---

**Last Updated:** 2026-06-21
**Version:** 3.0.0
