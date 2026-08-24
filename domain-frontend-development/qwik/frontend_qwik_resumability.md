---
title: "Qwik Resumability and Lazy-Execution Audit"
category: frontend-development/qwik
description: "Audit a Qwik application's use of resumability versus hydration — verifying $-boundaries create correct lazy-load segments, that state and handlers serialize, and that the app stays resumable instead of eagerly executing JavaScript on load."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: advanced
tags:
  - qwik
  - resumability
  - lazy-execution
  - serialization
  - hydration
  - dollar-boundaries
updated: "2026-06-21"
related_prompts:
  - domain-frontend-development/solidjs/frontend_solidjs_reactivity_patterns.md
  - domain-frontend-development/react/frontend_react_server_components_streaming.md
  - domain-frontend-development/performance/frontend_performance_core_web_vitals.md
  - domain-frontend-development/architecture/frontend_state_management_selection.md
---

# Qwik Resumability and Lazy-Execution Audit

**Objective:** Audit a Qwik app to confirm it leverages resumability — verifying `$`-boundaries split code into lazy-loadable segments, that component state and event handlers serialize into the HTML, and that nothing forces eager execution that would collapse Qwik's "no upfront hydration" advantage.

**When to Use:**
- Use when: Reviewing a Qwik app for unexpectedly large/early JS execution
- Use when: Serialization errors appear (non-serializable values captured across a `$`-boundary)
- Use when: Deciding where resumability genuinely pays off vs adds complexity
- Use when: Porting components from a hydration framework and they "feel" eager
- Don't use when: Choosing whether to adopt Qwik at all (use a framework-comparison/selection prompt)

## Instructions

1. **Establish the Resumability Mental Model**
   - Confirm the distinction: **hydration** re-executes component code on the client to re-attach state and listeners; **resumability** serializes that state/listener wiring into the HTML so the client *resumes* without re-running everything upfront.
   - Verify the team understands that the win is *time-to-interactive that is roughly independent of app size*, because handlers download/execute only on interaction.
   - Identify the `$`-suffixed APIs in use (component, event-handler, lazy, and lifecycle boundaries) and verify current names/signatures against docs.

2. **Audit `$`-Boundaries and Code Segmentation**
   - Confirm interactive components are defined with the component-`$` boundary and that event handlers are wrapped in `$` so the optimizer can split them into separately downloadable segments.
   - Flag inline handlers or imported functions used as handlers **without** the `$` wrapper, which can force eager inclusion or break lazy splitting.
   - Check that expensive logic lives inside `$` segments that only load on the relevant interaction, not in the synchronous module top-level.
   - Verify the build/optimizer is configured so segments are actually emitted as separate chunks (verify config against docs).

3. **Verify Serialization Across Boundaries**
   - Confirm values captured by a `$` closure are **serializable** (plain data, signals, stores) — not class instances, closures over DOM nodes, functions, or other non-serializable references.
   - Flag captured variables that would throw serialization errors or silently break resume.
   - Check that shared/reactive state uses the framework's signal/store primitives (verify names) so it serializes and re-wires automatically, rather than module-level mutable variables that don't survive resume.
   - Verify large captured data is fetched lazily or kept out of the serialized payload where possible (serialization has a size cost).

4. **Check Lazy Execution and Eager-Execution Leaks**
   - Look for patterns that defeat laziness: top-of-module side effects, eager imports of heavy libraries at component module scope, and `useVisibleTask$`/eager-task equivalents used where a lazier trigger would do (verify task API names against docs).
   - Distinguish tasks that legitimately must run (e.g., a measurement that needs the DOM) from tasks used as a hydration-style "run on load" crutch.
   - Confirm third-party widgets are loaded behind interaction or visibility rather than at startup.

5. **Assess Where Resumability Pays Off (and Where It Doesn't)**
   - Confirm resumability's benefit is realized: content-rich pages with deferred interactivity, large apps where TTI must stay flat.
   - Note diminishing returns: a tiny app, or one that must execute most logic immediately on load, gains less and pays the segmentation/serialization complexity tax.
   - Check that the serialized state payload size is reasonable relative to the interactivity gained.

6. **Review SSR/Streaming and Routing Integration**
   - Verify server rendering streams HTML with serialized state and that routing (verify the router name/version) integrates with resumability rather than triggering full client re-execution on navigation.
   - Confirm prefetching of likely-needed segments is configured so interaction feels instant without eager loading everything.

7. **CRITICAL: Verify findings before reporting**
   - Confirm a handler actually lacks a `$` wrapper (or that a value is genuinely non-serializable) by reading the source, not by assumption.
   - Distinguish a required eager task from an avoidable one before flagging it.
   - Verify any `$` API, task name, or config key against current Qwik docs; if unsure, label it "verify against current docs."
   - **Confidence level** for each finding:
     - **High Confidence:** Missing `$` boundary, non-serializable capture, or eager-execution leak confirmed in source
     - **Medium Confidence:** Task/trigger that is probably too eager depending on intent
     - **Low Confidence:** Complexity/style preference

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Describe Qwik as "just faster hydration" — it is resumability, a different model
- Flag every eager task as wrong; some genuinely require running on load (e.g., DOM measurement)
- Assume module-level mutable state will survive resume — and don't recommend it as shared state
- Invent `$` API names, task names, or config keys; label uncertain APIs "verify against current docs"
- Recommend Qwik patterns for a tiny app where the complexity outweighs the TTI benefit
- Treat a serialized state payload as a defect by default — weigh its size against the interactivity it enables
- Apply hydration-framework habits (run-on-mount effects everywhere) to a resumable model

✅ **DO:**
- Verify handlers and lazy logic are wrapped in `$` so the optimizer can segment them
- Confirm values crossing `$`-boundaries are serializable (data, signals, stores)
- Use framework signals/stores for shared state so it serializes and re-wires
- Reserve eager tasks for work that truly must run on load
- Weigh where resumability pays off vs adds tax for the given app
- Verify SSR/streaming and routing integrate without forcing client re-execution
- Phrase version-specific APIs neutrally and flag for verification

## Expected Output

A resumability audit including:
- Mental-model and `$`-API baseline
- `$`-boundary / segmentation findings
- Serialization correctness
- Eager-execution leak review
- Payoff assessment (where it helps/hurts)
- SSR/routing integration
- Prioritized recommendations

### Output Format

```markdown
## Qwik Resumability Audit

### Executive Summary
[Resumability posture, eager-execution leaks, headline findings]

### $-Boundary & Segmentation
[Handlers/logic wrapped correctly?]

### Serialization
[Non-serializable captures, state primitives]

### Eager-Execution Leaks
[Top-level side effects, over-eager tasks, heavy imports]

### Payoff Assessment
[Where resumability helps vs adds tax]

### SSR & Routing
[Streaming, navigation, prefetch]

### Recommendations
[Prioritized by impact/effort]
```

## Example Output

```markdown
## Qwik Resumability Audit

### Executive Summary
The app is mostly resumable, but two handlers are imported plain functions used without a `$` wrapper (forcing their module to load eagerly), a cart object captured across a boundary includes a class instance that fails serialization, and a `useVisibleTask$` runs an analytics call on every page load that could be deferred to first interaction. Fixing the boundaries and serialization restores flat TTI; deferring the task removes startup work.

### $-Boundary & Segmentation

#### Finding 1: Handler Used Without `$` Wrapper
- **Severity:** High
- **Confidence:** High
- **Location:** `src/components/Toolbar.tsx`
- **Evidence:**
  ```tsx
  import { saveDraft } from '../lib/draft'; // plain function
  // ...
  <button onClick$={saveDraft}>Save</button> // not wrapped → eager inclusion
  ```
- **Fix:** Wrap so the optimizer can split it into a lazy segment:
  ```tsx
  <button onClick$={() => saveDraft()}>Save</button>
  // or define saveDraft as a $() segment
  ```
  (Verify `onClick$`/`$()` against current docs.)

### Serialization

#### Finding 2: Non-Serializable Value Crosses a Boundary
- **Severity:** Critical
- **Confidence:** High
- **Location:** `src/routes/cart/index.tsx`
- **Evidence:**
  ```tsx
  const cart = new Cart();              // class instance — not serializable
  return <button onClick$={() => cart.add(item)}>Add</button>;
  // captured `cart` cannot serialize → resume breaks
  ```
- **Fix:** Hold state in a serializable store and keep methods as pure functions:
  ```tsx
  const cart = useStore({ items: [] }); // serializable
  const add$ = $(() => cart.items.push(item));
  return <button onClick$={add$}>Add</button>;
  ```
  (Verify `useStore`/`$` against current docs.)

### Eager-Execution Leaks

#### Finding 3: Analytics Task Runs Eagerly on Load
- **Severity:** Medium
- **Confidence:** Medium
- **Location:** `src/routes/layout.tsx`
- **Evidence:**
  ```tsx
  useVisibleTask$(() => { trackPageView(); }); // runs on load, defeating laziness
  ```
- **Recommendation:** Defer non-critical analytics to first interaction or an idle trigger, or confirm the eager run is intentional. (Verify task API name against docs.)

### Payoff Assessment

| Area | Resumability benefit | Notes |
|------|----------------------|-------|
| Content/blog routes | High | Deferred interactivity; flat TTI |
| Product pages | High | Many handlers, downloaded on demand |
| Admin dashboard | Moderate | Heavy logic runs early anyway; less upside |

### SSR & Routing
- SSR streams HTML with serialized state; client navigation resumes without full re-execution. Segment prefetch is configured for likely next routes. No issues found. (Verify router/prefetch behavior against docs.)

### Prioritized Recommendations

#### Critical (This Week)
| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 1 | Replace `new Cart()` capture with serializable store | Fixes broken resume | 1 hr |
| 2 | Wrap `saveDraft` handler in `$` | Restores lazy segmentation | 20 min |

#### Medium (This Month)
| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 1 | Defer analytics task off the eager path | Less startup work | 30 min |
| 2 | Audit remaining imported-function handlers for `$` wrapping | Smaller initial graph | 2 hrs |

#### Patterns to Preserve
- SSR streaming with serialized state
- Segment prefetch for likely routes
- Store-based serializable state
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Audit scoped to resumability, `$`-boundaries, and serialization.
- **ST-02 (Structured Sequential Instructions):** Mental model → boundaries → serialization → eager leaks → payoff → SSR → verification.
- **RT-02 (Multi-Dimensional Analysis Framework):** Evaluates segmentation, serialization, laziness, and payoff together.
- **RT-05 (Evidence-Based Reasoning):** Each finding cites the boundary/capture/task in source.
- **DS-06 (Prioritization Guidance):** Recommendations ranked by impact/effort with confidence levels.

## Related Prompts

- [../solidjs/frontend_solidjs_reactivity_patterns.md](../solidjs/frontend_solidjs_reactivity_patterns.md) - Another no-VDOM, fine-grained model for comparison
- [../react/frontend_react_server_components_streaming.md](../react/frontend_react_server_components_streaming.md) - Compare resumability with React server-first/streaming hydration
- [../performance/frontend_performance_core_web_vitals.md](../performance/frontend_performance_core_web_vitals.md) - Measure TTI/JS-execution impact
- [../architecture/frontend_state_management_selection.md](../architecture/frontend_state_management_selection.md) - Choosing serializable state that survives resume
