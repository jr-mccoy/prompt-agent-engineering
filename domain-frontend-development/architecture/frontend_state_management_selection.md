---
title: "Framework-Agnostic State Management Selection"
category: frontend-development/architecture
description: "Select the right state-management approach by category — local state, context, a global store, or a server-cache library (React Query/SWR) — using a decision matrix and an over/under-engineering audit."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: advanced
tags:
  - state-management
  - architecture
  - server-cache
  - react-query
  - swr
  - decision-matrix
  - over-engineering
updated: "2026-06-21"
related_prompts:
  - domain-frontend-development/react/frontend_react_state_management.md
  - domain-frontend-development/architecture/frontend_error_boundary_resilience.md
  - domain-frontend-development/forms/frontend_forms_validation_design.md
  - domain-frontend-development/react/frontend_react_performance.md
---

# Framework-Agnostic State Management Selection

**Objective:** Decide where each piece of application state should live — local component state, context/provided state, a global store, or a server-cache library — and confirm the choice is neither over- nor under-engineered for the actual needs.

**When to Use:**
- Use when: Deciding the state architecture for a new app or feature.
- Use when: A codebase has "everything in the global store" or prop-drilling pain and you need to right-size it.
- Use when: Server data is being hand-managed (manual loading/error/caching) and a server-cache library may fit better.
- Use when: Migrating between approaches and you need a defensible decision, not a fashion choice.
- Don't use when: A single component's local `useState` clearly suffices — no selection process is needed.

## Instructions

1. **Categorize Every Piece of State**
   - Classify each state into one of:
     - **Server state** — data owned by the backend (lists, entities, search results) that must be fetched, cached, and synced.
     - **Global client/UI state** — shared across distant parts of the tree (theme, auth/session, feature flags, cross-page UI).
     - **Local UI state** — confined to one component or a small subtree (open/closed, hover, input focus).
     - **URL state** — filters, pagination, tabs that belong in the address bar.
     - **Form state** — input values and validation (often best owned by a form library).
   - Misclassification is the root cause of most state-management pain; do this carefully.

2. **Apply the Selection Matrix**
   - For each category, match to the appropriate mechanism:
     - **Server state → server-cache library** (React Query / SWR / equivalent): handles caching, refetch, staleness, mutations.
     - **Global client/UI state → context (low-frequency) or a store** (low boilerplate store for frequently-updated shared state).
     - **Local UI state → component state** (`useState`/`useReducer` or framework equivalent).
     - **URL state → router/query params.**
     - **Form state → form library** (see the forms prompts).
   - Record the decision and the reason for each.

3. **Evaluate Context vs Store for Shared State**
   - Use context for stable, infrequently-changing shared values (theme, locale, auth) where re-render cost is low.
   - Prefer a store with selectors for frequently-updated shared state to avoid re-rendering every consumer.
   - Flag context used as a high-frequency store (a common performance pitfall).

4. **Audit for Over-Engineering**
   - Flag global stores holding state only one component uses, server data manually mirrored in the store, or a heavy library introduced for trivial needs.
   - Quantify the cost: boilerplate lines, re-render breadth, and onboarding friction.

5. **Audit for Under-Engineering**
   - Flag deep prop drilling that signals a missing context/store, hand-rolled fetch caching with stale-data bugs, and duplicated server state across components.
   - Identify race conditions and missing cache invalidation in manual data layers.

6. **Account for Constraints**
   - Weigh SSR/hydration needs, team familiarity, bundle budget, testing complexity, and whether multiple mechanisms can coexist (they usually should: server-cache + small store + local state).
   - Avoid recommending a single tool for all categories.

7. **CRITICAL: Verify findings before reporting**
   - Confirm classifications by checking how each state is actually read/written (who consumes it, how often it changes).
   - Do not recommend a migration without a concrete benefit; state the expected payoff qualitatively and note where measurement is needed.
   - **Confidence level** for each recommendation:
     - **High Confidence:** Category and access pattern verified in code; clear mechanism fit.
     - **Medium Confidence:** Good fit with tradeoffs to weigh.
     - **Low Confidence:** Plausible but alternatives are comparable; flagged for team decision.

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Put server state in a global store and hand-manage loading/error/caching when a server-cache library is the right tool.
- Reach for a global store because of one instance of prop drilling.
- Treat context as a high-frequency state store (re-renders every consumer on each change).
- Recommend a single mechanism for all state categories.
- Push migration purely because a tool is newer or trendier.
- Assume "Redux/store everywhere" is bad without checking actual access patterns.
- Duplicate server data across components instead of a single cached source.

✅ **DO:**
- Classify state first; let the category pick the mechanism.
- Use a server-cache library for server state (caching, refetch, invalidation, mutations).
- Reserve context for stable shared values; use a store with selectors for hot shared state.
- Keep local state local and URL state in the URL.
- Let multiple mechanisms coexist by responsibility.
- Justify migrations by concrete reduction in boilerplate/re-renders/bugs.
- Verify access patterns before deciding.

## Expected Output

A state-architecture decision document including:
- A categorized state inventory.
- A selection matrix mapping each category to a mechanism with rationale.
- Over-engineering and under-engineering findings.
- A target architecture (and migration notes if changing).
- Prioritized recommendations.

### Output Format

```markdown
## State Management Selection: [App/Feature]

### State Inventory & Categorization

| State | Category | Current Mechanism | Access Pattern | Recommended Mechanism |
|-------|----------|-------------------|----------------|-----------------------|

### Selection Rationale
[Per category: mechanism + why]

### Over/Under-Engineering Findings

| ID | Issue | Type | Severity | Confidence | Location | Evidence | Recommendation |
|----|-------|------|----------|------------|----------|----------|----------------|

### Target Architecture
[How state is partitioned across mechanisms]

### Prioritized Recommendations
1. ...
```

## Example Output

```markdown
## State Management Selection: SaaS Dashboard

### State Inventory & Categorization

| State | Category | Current Mechanism | Access Pattern | Recommended Mechanism |
|-------|----------|-------------------|----------------|-----------------------|
| Projects/tasks/users | Server | Global store (manual) | fetched, cached, mutated | Server-cache library |
| Auth/session | Global client | Global store | read widely, rarely changes | Context (or thin store) |
| Theme | Global client | Context | rarely changes | Context (keep) |
| Sidebar collapsed | Local UI | Global store | one layout component | Component state |
| Table filters/page | URL | Global store (duplicated) | shareable, bookmarkable | URL params |
| Settings form values | Form | Global store | one form | Form library |

### Selection Rationale
- **Server state → server-cache library:** Eliminates hand-written loading/error/cache; gives refetch + invalidation + mutation handling. ~60% of current store is server data.
- **Auth/theme → context:** Stable, low-frequency; re-render cost negligible.
- **Sidebar/local → component state:** Single-consumer; no reason to globalize.
- **Filters → URL:** Enables sharing/bookmarking and removes a sync bug.
- **Form → form library:** Validation + dirty/touched tracking belong with the form.

### Over/Under-Engineering Findings

| ID | Issue | Type | Severity | Confidence | Location | Evidence | Recommendation |
|----|-------|------|----------|------------|----------|----------|----------------|
| S1 | Server data manually cached in global store | Over | High | High | `store/entities.ts` | Manual `loading/error/data` per entity; stale-data bug reports | Move to server-cache library |
| S2 | Filters in both URL and store, kept in sync | Over/bug | High | High | `FiltersProvider.tsx` | Two sources of truth drift on back/forward | Make URL the single source |
| S3 | Sidebar-collapsed flag in global store | Over | Medium | High | `store/ui.ts` | Only `<Layout>` reads it | Component `useState` |
| S4 | Prop drilling auth 5 levels deep in reports area | Under | Medium | Medium | `reports/*` | `user` passed through 5 components | Provide via context |
| S5 | Duplicate fetch of the same user list in 3 widgets | Under/bug | Medium | High | three widgets | Three independent fetches, inconsistent results | Single cached query key |

### Target Architecture
- **Server-cache library:** all backend entities (projects, tasks, users) — single cache, keyed queries, mutations invalidate.
- **Context:** auth/session, theme, locale.
- **Component state:** sidebar, modals, hovers, local toggles.
- **URL:** filters, pagination, active tab.
- **Form library:** settings and other forms.

### Prioritized Recommendations
1. **S1 — Adopt a server-cache library for server state.** Removes the largest source of boilerplate and stale-data bugs.
2. **S2 — Make URL the single source for filters.** Fixes a real correctness bug and simplifies state.
3. **S5 — Consolidate duplicate fetches behind one query key.** Removes inconsistency.
4. **S4 — Provide auth via context.** Cures deep prop drilling.
5. **S3 — Demote single-consumer flags to local state.** Trims the global store.
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Sets the goal — right-sized state placement by category.
- **ST-02 (Structured Sequential Instructions):** Sequences categorize → matrix → context-vs-store → over/under-engineering → constraints.
- **RT-02 (Multi-Dimensional Analysis Framework):** Weighs each category across access pattern, re-render cost, boilerplate, and constraints.
- **RT-05 (Evidence-Based Reasoning):** Recommendations are grounded in observed access patterns and concrete bug evidence.
- **DS-06 (Prioritization Guidance):** Orders changes by correctness and boilerplate impact.

## Related Prompts

- [../react/frontend_react_state_management.md](../react/frontend_react_state_management.md) - React-specific library comparison (Redux/Zustand/Jotai)
- [frontend_error_boundary_resilience.md](frontend_error_boundary_resilience.md) - Error/retry states that server-cache libraries provide
- [../forms/frontend_forms_validation_design.md](../forms/frontend_forms_validation_design.md) - Where form state belongs in the architecture
- [../react/frontend_react_performance.md](../react/frontend_react_performance.md) - Re-render impact of context-as-store
