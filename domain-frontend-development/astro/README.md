# Astro Prompts

**Category:** Frontend Development / Astro
**Prompts:** 2

---

## Overview

Production-grade prompts for Astro development, focused on Astro's server-first, ship-less-JavaScript philosophy. Coverage spans islands architecture and partial hydration (choosing the right `client:*` directive for each interactive component) and type-safe content collections (schemas, content-layer loaders, MDX, and build-time routing). Prompts describe concepts and mental models and flag version-specific APIs for verification, since Astro evolves quickly.

## Prompts

| Prompt | Description | Difficulty |
|--------|-------------|------------|
| [frontend_astro_islands_architecture.md](frontend_astro_islands_architecture.md) | Audit server-first rendering, island boundaries, and `client:load/idle/visible/media/only` directive selection; surface over- and under-hydration | Intermediate |
| [frontend_astro_content_collections.md](frontend_astro_content_collections.md) | Review content collections for schema/type safety, content-layer loaders, MDX, and build-time vs request-time data and routing | Intermediate |

## Usage Examples

### Auditing Partial Hydration
Use `frontend_astro_islands_architecture.md` to find:
- `client:*` directives stronger than the interaction requires
- `client:only` components causing layout shift / no-JS blankness
- Island bloat where static content is trapped inside a hydrated tree
- Attempts to share framework context across isolated islands

### Reviewing Content Modeling
Use `frontend_astro_content_collections.md` to find:
- Collections without schemas or relations using raw string IDs instead of `reference()`
- Drafts leaking because a filter is applied inconsistently
- Build-time data fetched at request time unnecessarily
- Over-hydrated interactive components embedded in MDX

## Key Concepts

- **Server-first default:** `.astro` components render to HTML with zero client JS unless a `client:*` directive opts in.
- **Client directives:** `client:load`, `client:idle`, `client:visible`, `client:media`, and `client:only` map to distinct hydration triggers — pick the lightest that satisfies the interaction.
- **Island isolation:** each island hydrates independently; cross-island shared state needs a framework-agnostic store, not framework context.
- **Type-safe content:** schema-validated collections, `reference()` relations, `image()` validation, and `getStaticPaths`-driven routing.
- **Build-time vs request-time:** resolve static, cacheable content at build; reserve request-time fetching for genuinely dynamic data.

---

## Related Prompts

- [../performance/frontend_performance_core_web_vitals.md](../performance/frontend_performance_core_web_vitals.md) - Measure JS/CLS impact of hydration choices
- [../react/frontend_react_server_components_streaming.md](../react/frontend_react_server_components_streaming.md) - Compare Astro islands with React server-first rendering
- [../svelte/frontend_svelte_component_patterns.md](../svelte/frontend_svelte_component_patterns.md) - Components for islands built on Svelte
- [../architecture/frontend_state_management_selection.md](../architecture/frontend_state_management_selection.md) - Cross-island shared-state selection
