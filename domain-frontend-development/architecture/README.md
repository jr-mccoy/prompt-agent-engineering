# Architecture Prompts

**Category:** Frontend Development / Architecture
**Prompts:** 3

---

## Overview

Production-grade prompts for cross-cutting frontend architecture concerns — client-side resilience and error handling, framework-agnostic state-management selection, and internationalization/localization. These are framework-neutral decisions that apply across React, Vue, Svelte, Angular, and beyond.

## Prompts

| Prompt | Description | Difficulty |
|--------|-------------|------------|
| [frontend_error_boundary_resilience.md](frontend_error_boundary_resilience.md) | Design/audit client resilience: error boundaries, fallback UI, retry/recovery, error reporting, graceful degradation, Suspense error states | Intermediate |
| [frontend_state_management_selection.md](frontend_state_management_selection.md) | Select state mechanism by category — local vs context vs store vs server-cache (React Query/SWR); decision matrix + over/under-engineering audit | Advanced |
| [frontend_i18n_localization.md](frontend_i18n_localization.md) | i18n/l10n: message extraction, ICU plural/gender, RTL, locale-aware formatting, lazy-loaded locale bundles, pseudo-localization testing | Intermediate |

## Key Concepts

- **Layered error boundaries**: One app-level boundary plus granular ones around independent regions; boundaries don't catch event-handler/async errors.
- **State by category**: Classify state (server, global client, local, URL, form) first, then let the category pick the mechanism.
- **Server-cache libraries**: React Query/SWR handle caching, refetch, invalidation, and mutations — don't hand-roll them in a global store.
- **ICU correctness**: Use `plural`/`select` for counts and gender; never concatenate translated sentence fragments.
- **RTL & expansion**: Use logical CSS properties and tolerate 30–40%+ text expansion.
- **Verify before reporting**: Reproduce a failure path or trace an access pattern before declaring a finding.

## Usage Examples

### Hardening an App Against Crashes
Use `frontend_error_boundary_resilience.md` to map error surfaces, place boundaries, and design fallback/retry/reporting.

### Right-Sizing State
Use `frontend_state_management_selection.md` to categorize state and detect over- or under-engineering.

### Going Multilingual
Use `frontend_i18n_localization.md` to externalize strings, add ICU plurals, and design RTL-safe, lazy-loaded locale bundles.

---

## Related Prompts

- [../react/frontend_react_component_patterns.md](../react/frontend_react_component_patterns.md) - Where error boundaries fit in component architecture
- [../react/frontend_react_state_management.md](../react/frontend_react_state_management.md) - React-specific state library comparison
- [../forms/frontend_forms_validation_design.md](../forms/frontend_forms_validation_design.md) - Form state within the broader architecture
- [../performance/frontend_performance_bundle_optimization.md](../performance/frontend_performance_bundle_optimization.md) - Code-splitting locale and feature bundles
