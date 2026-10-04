# Frontend Development Domain

**Purpose:** Comprehensive prompt collection for frontend development covering frameworks (React, Vue, Angular, Next.js, Svelte/SvelteKit, Astro, SolidJS, Qwik, Remix), cross-cutting craft (styling, TypeScript, forms, animation, architecture), build tooling, accessibility, performance, testing, and UX research methods.

**Total Resources:** 74 prompts across 20 categories

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
| [astro/](astro/) | 3 | Islands architecture & partial hydration, content collections, rendering modes & server islands |
| [solidjs/](solidjs/) | 3 | Fine-grained reactivity patterns, control flow & component API, SolidStart data loading & SSR |
| [qwik/](qwik/) | 3 | Resumability & lazy-execution, Qwik City loaders/actions/middleware, reactive state & tasks |
| [remix/](remix/) | 3 | Data loading & mutations, sessions/auth/caching, Remix → React Router v7 migration |

### Cross-Cutting Craft (framework-agnostic)

| Category | Prompts | Focus |
|----------|---------|-------|
| [styling/](styling/) | 3 | CSS architecture/scalability, Tailwind design system, CSS-in-JS runtime cost |
| [typescript/](typescript/) | 3 | Component/props typing, type-safety audit, API contract typing |
| [forms/](forms/) | 3 | Validation strategy, accessible form UX, multi-step wizard state |
| [animation/](animation/) | 3 | Motion performance, motion system design (tokens & choreography), motion safety audit |
| [architecture/](architecture/) | 3 | Error boundaries/resilience, state-management selection, i18n/localization |
| [build-tooling/](build-tooling/) | 3 | Vite optimization, micro-frontends/Module Federation, bundler migration |
| [design-direction/](design-direction/) | 5 | Visual design direction options, look-and-feel spec from a target "vibe", design-token architecture, design-system audit, component governance |

### Quality Concerns

| Category | Prompts | Focus |
|----------|---------|-------|
| [accessibility/](accessibility/) | 5 | WCAG audits, ARIA patterns, screen reader testing, accessible documents & slides, organisational accessibility program |
| [performance/](performance/) | 3 | Core Web Vitals, bundle optimization, field CWV regression triage |
| [testing/](testing/) | 3 | Jest unit testing, Playwright E2E, API mocking strategy |

### UX Research

| Category | Prompts | Focus |
|----------|---------|-------|
| [ux-research/](ux-research/) | 7 | Usability test plans and moderation scripts, heuristic evaluation, card sort / tree test, findings severity, SUS/UMUX-Lite/SEQ scoring, design critique |

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
| Decide prerender vs on-demand and server islands in Astro | [frontend_astro_rendering_modes_server_islands.md](astro/frontend_astro_rendering_modes_server_islands.md) |
| Analyze SolidJS reactivity | [frontend_solidjs_reactivity_patterns.md](solidjs/frontend_solidjs_reactivity_patterns.md) |
| Review SolidJS control flow & component APIs | [frontend_solidjs_control_flow_components.md](solidjs/frontend_solidjs_control_flow_components.md) |
| Review SolidStart data loading & SSR | [frontend_solidjs_solidstart_data_ssr.md](solidjs/frontend_solidjs_solidstart_data_ssr.md) |
| Audit Qwik resumability | [frontend_qwik_resumability.md](qwik/frontend_qwik_resumability.md) |
| Review Qwik City loaders, actions & middleware | [frontend_qwik_city_loaders_actions.md](qwik/frontend_qwik_city_loaders_actions.md) |
| Debug Qwik signals, stores & tasks | [frontend_qwik_reactive_state_tasks.md](qwik/frontend_qwik_reactive_state_tasks.md) |
| Review Remix/React Router data loading | [frontend_remix_data_loading.md](remix/frontend_remix_data_loading.md) |
| Review Remix/React Router route auth, sessions & caching | [frontend_remix_sessions_auth_caching.md](remix/frontend_remix_sessions_auth_caching.md) |
| Plan a Remix v2 → React Router v7 migration | [frontend_remix_react_router_v7_migration.md](remix/frontend_remix_react_router_v7_migration.md) |
| Audit CSS architecture & scalability | [frontend_styling_css_architecture.md](styling/frontend_styling_css_architecture.md) |
| Treat Tailwind config as a design system | [frontend_styling_tailwind_design_system.md](styling/frontend_styling_tailwind_design_system.md) |
| Review CSS-in-JS runtime cost | [frontend_styling_css_in_js_review.md](styling/frontend_styling_css_in_js_review.md) |
| Type components & props well | [frontend_typescript_component_typing.md](typescript/frontend_typescript_component_typing.md) |
| Audit frontend type safety | [frontend_typescript_type_safety_audit.md](typescript/frontend_typescript_type_safety_audit.md) |
| Design API contract typing & runtime validation | [frontend_typescript_api_contract_typing.md](typescript/frontend_typescript_api_contract_typing.md) |
| Design form validation | [frontend_forms_validation_design.md](forms/frontend_forms_validation_design.md) |
| Audit accessible form UX | [frontend_forms_accessibility_ux.md](forms/frontend_forms_accessibility_ux.md) |
| Design multi-step form / wizard state | [frontend_forms_multi_step_wizard_state.md](forms/frontend_forms_multi_step_wizard_state.md) |
| Audit animation & motion performance | [frontend_animation_motion_performance.md](animation/frontend_animation_motion_performance.md) |
| Design a motion system (tokens, choreography) | [frontend_animation_motion_system_design.md](animation/frontend_animation_motion_system_design.md) |
| Audit motion safety (vestibular, flashing, WCAG) | [frontend_animation_motion_safety_audit.md](animation/frontend_animation_motion_safety_audit.md) |
| Design error boundaries & resilience | [frontend_error_boundary_resilience.md](architecture/frontend_error_boundary_resilience.md) |
| Select a state-management approach | [frontend_state_management_selection.md](architecture/frontend_state_management_selection.md) |
| Architect i18n / localization | [frontend_i18n_localization.md](architecture/frontend_i18n_localization.md) |
| Optimize a Vite build | [frontend_build_vite_optimization.md](build-tooling/frontend_build_vite_optimization.md) |
| Design micro-frontends / Module Federation | [frontend_build_micro_frontends_module_federation.md](build-tooling/frontend_build_micro_frontends_module_federation.md) |
| Plan a bundler migration | [frontend_build_bundler_migration.md](build-tooling/frontend_build_bundler_migration.md) |
| Conduct WCAG audit | [frontend_accessibility_wcag_audit.md](accessibility/frontend_accessibility_wcag_audit.md) |
| Implement ARIA patterns | [frontend_accessibility_aria_patterns.md](accessibility/frontend_accessibility_aria_patterns.md) |
| Test with screen readers | [frontend_accessibility_screen_reader.md](accessibility/frontend_accessibility_screen_reader.md) |
| Make published PDFs, documents and slides accessible | [frontend_accessibility_documents_slides.md](accessibility/frontend_accessibility_documents_slides.md) |
| Set up an accessibility program (policy, VPAT/ACR, procurement, training) | [frontend_accessibility_program_governance.md](accessibility/frontend_accessibility_program_governance.md) |
| Audit a design system's components, tokens and adoption | [frontend_design_system_audit.md](design-direction/frontend_design_system_audit.md) |
| Design token tiers, theming and naming | [frontend_design_token_architecture.md](design-direction/frontend_design_token_architecture.md) |
| Govern component APIs, versioning, deprecation and contributions | [frontend_design_system_component_governance.md](design-direction/frontend_design_system_component_governance.md) |
| Optimize Core Web Vitals | [frontend_performance_core_web_vitals.md](performance/frontend_performance_core_web_vitals.md) |
| Reduce bundle size | [frontend_performance_bundle_optimization.md](performance/frontend_performance_bundle_optimization.md) |
| Triage a field Core Web Vitals regression | [frontend_performance_field_vitals_regression.md](performance/frontend_performance_field_vitals_regression.md) |
| Set up Jest testing | [frontend_testing_jest.md](testing/frontend_testing_jest.md) |
| Create E2E tests | [frontend_testing_playwright.md](testing/frontend_testing_playwright.md) |
| Design an API mocking strategy | [frontend_testing_api_mocking_strategy.md](testing/frontend_testing_api_mocking_strategy.md) |
| Plan a usability test | [frontend_ux_usability_test_plan.md](ux-research/frontend_ux_usability_test_plan.md) |
| Script a moderated usability session | [frontend_ux_moderated_session_script.md](ux-research/frontend_ux_moderated_session_script.md) |
| Run a heuristic evaluation | [frontend_ux_heuristic_evaluation.md](ux-research/frontend_ux_heuristic_evaluation.md) |
| Run a card sort / tree test | [frontend_ux_card_sort_tree_test.md](ux-research/frontend_ux_card_sort_tree_test.md) |
| Rate usability findings by severity | [frontend_ux_usability_findings_severity_log.md](ux-research/frontend_ux_usability_findings_severity_log.md) |
| Score SUS / UMUX-Lite / SEQ | [frontend_ux_standardized_survey_sus.md](ux-research/frontend_ux_standardized_survey_sus.md) |
| Facilitate a design critique | [frontend_ux_design_critique_facilitator.md](ux-research/frontend_ux_design_critique_facilitator.md) |

### By Technology

**React:** component patterns, hooks, state management (Redux/Zustand/Jotai/Context), Testing Library, performance, Server Components & streaming SSR.

**Vue:** Composition API, composables, Pinia stores, Vue Test Utils, advanced reactivity (`ref`/`reactive`/`shallowRef`) and render performance.

**Angular:** standalone components, Signals & RxJS, dependency injection, TestBed, advanced signals interop and zoneless change detection.

**Next.js:** App Router server/client boundaries, data fetching/caching/revalidation, rendering strategy, Server Actions & mutations.

**Svelte / SvelteKit:** runes & reactivity, composition, routing/load/form-actions, state management, SSR safety.

**Astro / SolidJS / Qwik / Remix:** server-first islands & partial hydration, type-safe content collections, per-route prerender vs on-demand rendering and server islands; fine-grained reactivity, control flow and SolidStart data/SSR; resumability vs hydration, Qwik City loaders/actions and reactive tasks; loader/action data flows with progressive enhancement, route-level auth/sessions/caching, and the React Router v7 migration.

**Styling:** CSS architecture (BEM/ITCSS/utility-first, cascade layers, tokens), Tailwind as a design system, CSS-in-JS runtime cost and SSR.

**TypeScript:** precise component/props/generics typing across frameworks, codebase-wide type-safety audits, and API contract typing with runtime validation at the boundary.

**Forms / Animation / Architecture:** schema validation, accessible form UX and multi-step wizard state; GPU-friendly animation, motion tokens and choreography, and vestibular/flash motion safety; error boundaries, state-management selection, and i18n/localization.

**Build Tooling:** Vite config optimization, micro-frontends / Module Federation, and bundler migration.

**Design Direction & Design Systems:** visual direction and look-and-feel specs; primitive/semantic/component token tiers and theming; design-system inventory, token coverage and adoption metrics; component API, versioning, deprecation and contribution governance.

**Accessibility / Performance / Testing:** WCAG/ARIA/screen-reader audits, accessible published documents and slides (PDF/UA, captions), and organisation-wide accessibility programs (policy, VPAT/ACR, procurement, training); Core Web Vitals, bundle optimization and field-data regression triage; Jest, Playwright and a shared, contract-checked API mocking layer.

**UX Research:** usability test planning and moderation, heuristic evaluation, card sorting and tree testing, severity-rated findings, standardized questionnaires (SUS, UMUX-Lite, SEQ), and design critique.

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

**Last Updated:** 2026-10-03
**Version:** 3.3.0
