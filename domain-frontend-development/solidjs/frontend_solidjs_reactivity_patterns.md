---
title: "SolidJS Fine-Grained Reactivity Patterns Analysis"
category: frontend-development/solidjs
description: "Audit a SolidJS codebase for correct use of fine-grained reactivity — signals, stores, derivations/memos, and effects — catching the common pitfalls that come from carrying over a Virtual-DOM / React mental model into Solid's no-VDOM, run-once-component world."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: advanced
tags:
  - solidjs
  - fine-grained-reactivity
  - signals
  - stores
  - memos
  - effects
updated: "2026-06-21"
related_prompts:
  - domain-frontend-development/svelte/frontend_svelte_component_patterns.md
  - domain-frontend-development/qwik/frontend_qwik_resumability.md
  - domain-frontend-development/architecture/frontend_state_management_selection.md
  - domain-frontend-development/performance/frontend_performance_core_web_vitals.md
---

# SolidJS Fine-Grained Reactivity Patterns Analysis

**Objective:** Analyze a SolidJS codebase for correct fine-grained reactivity — verifying that reactive reads happen in tracking scopes, that derivations use memos appropriately, that stores are updated immutably, and that effects are scoped and cleaned up — while flagging React-style patterns that break Solid's model.

**When to Use:**
- Use when: Reviewing a SolidJS app where UI fails to update or updates too often
- Use when: A developer coming from React is "losing reactivity" by destructuring props or signals
- Use when: Deciding between signals, stores, and memos for a piece of state
- Use when: Auditing effects for over-execution or missing cleanup
- Don't use when: Evaluating Solid vs other frameworks for selection (use a framework-comparison prompt)

## Instructions

1. **Establish the No-VDOM Mental Model Baseline**
   - Confirm reviewers understand the core Solid rule: **component function bodies run once**; reactivity lives in the tracking scopes (JSX, effects, memos), not in re-running the component.
   - Verify there is no expectation of "re-render on state change" — only the specific reactive computations that read a changed signal re-run.
   - Identify the reactive primitives in use (signal accessors, stores, memos, effects, resources) and verify their current names/signatures against docs.

2. **Audit Signal Access and the "Don't Destructure" Rule**
   - Confirm signals are read by **calling the accessor inside a tracking scope** (e.g., `count()` in JSX), not read once into a local variable at component top.
   - Flag destructuring of props (`const { value } = props`) — this snapshots the value and **breaks reactivity**; props must stay accessed as `props.value`.
   - Flag destructuring or early-reading a signal accessor's value outside a tracked context where live updates are expected.
   - Check that passing reactivity through component boundaries keeps it as a function/accessor, not a plucked primitive.

3. **Review Derivations: Inline vs Memo**
   - Distinguish cheap inline derivations (just call the accessor in JSX) from expensive ones that should use a memo.
   - Confirm memos wrap computations that are expensive, read by multiple consumers, or used to prevent downstream recomputation — not trivial expressions.
   - Flag memos used merely to "store" a value where a plain derived function would do, and flag expensive recomputation that should be memoized.
   - Verify memo dependencies are tracked automatically by reading signals inside the memo (no manual dependency arrays — that's a React habit).

4. **Audit Stores for Nested/Collection State**
   - Confirm `createStore` (verify name) is used for nested objects/arrays rather than many independent signals, where fine-grained nested reactivity matters.
   - Check that store updates use the store setter with path/immutable-style updates (or the produce-style helper) — **not** direct mutation of the proxy in ways the docs don't sanction. Verify helper names against docs.
   - Flag replacing the whole store object when a path update would preserve fine-grained reactivity.
   - Verify list rendering uses the keyed control-flow primitive (e.g., `<For>`) rather than `.map()` so rows are not needlessly recreated; verify component names against docs.

5. **Evaluate Effects and Side Effects**
   - Confirm effects are used for *side effects* (DOM, subscriptions, logging), not for deriving state that should be a memo.
   - Check each effect reads exactly the signals it depends on and returns/registers cleanup for subscriptions, timers, and listeners.
   - Flag effects that write to signals they also read (potential loops) and effects that run more often than intended because they read an unrelated signal.
   - Verify untracking is used intentionally where a read should *not* create a dependency, and not as a band-aid over a structural bug. Verify the untrack/onCleanup names against docs.

6. **Check Async Reactivity (Resources)**
   - Confirm async data uses the resource primitive (verify name) so loading/error states and refetch integrate with the reactive graph, rather than ad-hoc effects setting signals.
   - Verify Suspense boundaries (if used) wrap resource reads correctly.
   - Flag manual loading-state signals duplicating what a resource already exposes.

7. **CRITICAL: Verify findings before reporting**
   - Trace the reactive chain for any "missing update": confirm the read happens in a tracking scope and the write actually changes the signal/store path.
   - Before flagging destructuring, confirm the value is expected to update live (destructuring a one-time config value is fine).
   - Confirm an "over-running effect" reads the extra signal rather than just appearing to.
   - Verify any primitive name/signature against current Solid docs before asserting it.
   - **Confidence level** for each finding:
     - **High Confidence:** Reactivity break or loop with a traced chain
     - **Medium Confidence:** Suboptimal primitive choice (memo vs inline, signals vs store)
     - **Low Confidence:** Style preference

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Expect components to "re-render" — Solid component bodies run once; that is not a bug
- Flag the absence of dependency arrays in memos/effects as missing — Solid tracks automatically
- Recommend `.map()` over the keyed control-flow primitive for dynamic lists
- Treat all prop destructuring as fatal — destructuring a non-reactive, one-time value is acceptable
- Flag inline JSX derivations as "needing a memo" unless they are expensive or widely reused
- Invent primitive names or signatures; label uncertain APIs "verify against current docs"
- Apply React rules (memoization to prevent re-renders, effect dependency arrays) to Solid

✅ **DO:**
- Keep props and signals accessed live (`props.value`, `signal()`) inside tracking scopes
- Use memos for expensive or multiply-consumed derivations; inline for cheap ones
- Use stores for nested/collection state with path-based or produce-style updates
- Reserve effects for side effects and ensure cleanup for subscriptions/timers
- Trace the reactive chain before claiming "missing reactivity"
- Use resources for async so loading/error/refetch integrate with the graph
- Phrase version-specific APIs neutrally and flag for verification

## Expected Output

A fine-grained reactivity analysis including:
- Mental-model and primitive baseline
- Signal-access and destructuring findings
- Derivation (memo vs inline) review
- Store-update correctness
- Effect scoping and cleanup
- Async/resource handling
- Prioritized recommendations

### Output Format

```markdown
## SolidJS Reactivity Patterns Analysis

### Executive Summary
[Reactivity health, headline pitfalls]

### Primitive Inventory
[Signals, stores, memos, effects, resources in use]

### Signal Access & Destructuring
[Reactivity breaks from snapshotting]

### Derivations
[Memo vs inline appropriateness]

### Stores
[Update correctness, list rendering]

### Effects
[Scoping, cleanup, loops]

### Async (Resources)
[Resource usage, Suspense]

### Recommendations
[Prioritized by impact/effort]
```

## Example Output

```markdown
## SolidJS Reactivity Patterns Analysis

### Executive Summary
The app shows three classic "React-brain" reactivity breaks: a child component destructures `props`, a filtered list is computed by reading a signal into a top-level variable, and an effect derives state that should be a memo. The first two cause stale UI; the third causes redundant work and a near-miss update loop. All are structural and quick to fix once the no-VDOM model is applied.

### Primitive Inventory

| Primitive | Usage | Assessment |
|-----------|-------|------------|
| Signals | 14 | Mostly correct |
| Stores | 1 (cart) | Updated immutably — good |
| Memos | 2 | One unnecessary, one missing |
| Effects | 5 | One should be a memo; one missing cleanup |
| Resources | 1 (products) | Correct |

### Signal Access & Destructuring

#### Finding 1: Destructured Props Break Reactivity
- **Severity:** Critical
- **Confidence:** High
- **Location:** `src/components/Badge.tsx`
- **Evidence:**
  ```tsx
  function Badge(props) {
    const { count } = props; // snapshots count at first run — never updates
    return <span>{count}</span>;
  }
  ```
- **Fix:** Keep the access live:
  ```tsx
  function Badge(props) {
    return <span>{props.count}</span>; // tracked on each change
  }
  ```

#### Finding 2: Signal Read Into a Variable Outside Tracking
- **Severity:** Critical
- **Confidence:** High
- **Location:** `src/pages/List.tsx`
- **Evidence:**
  ```tsx
  const items = data();            // read once at component-body run
  const visible = items.filter(i => i.active); // never recomputes
  return <ul>{visible.map(...)}</ul>;
  ```
- **Fix:** Derive inside a tracking scope (memo here, since it's reused/expensive):
  ```tsx
  const visible = createMemo(() => data().filter(i => i.active));
  return <ul><For each={visible()}>{i => <Row item={i} />}</For></ul>;
  ```
  (Verify `createMemo`/`<For>` against current docs.)

### Derivations

#### Finding 3: Effect Used to Derive State
- **Severity:** High
- **Confidence:** High
- **Location:** `src/pages/Cart.tsx`
- **Evidence:**
  ```tsx
  const [total, setTotal] = createSignal(0);
  createEffect(() => {
    setTotal(items().reduce((s, i) => s + i.price, 0)); // derive-via-effect
  });
  ```
- **Why it's wrong:** This creates an extra signal, runs an effect on every change, and risks loops if anything reads `total` and writes back. A memo expresses the derivation directly.
- **Fix:**
  ```tsx
  const total = createMemo(() => items().reduce((s, i) => s + i.price, 0));
  ```

### Stores

- The `cart` store updates via the store setter with path-style updates and uses `<For>` for rows. Fine-grained nested reactivity is preserved. No issues. (Verify setter/produce names against docs.)

### Effects

#### Finding 4: Missing Cleanup on Subscription
- **Severity:** Medium
- **Confidence:** High
- **Location:** `src/components/LiveFeed.tsx`
- **Evidence:**
  ```tsx
  createEffect(() => {
    const sub = feed.subscribe(onMsg);
    // no cleanup — leaks on re-run / disposal
  });
  ```
- **Fix:** Register cleanup:
  ```tsx
  createEffect(() => {
    const sub = feed.subscribe(onMsg);
    onCleanup(() => sub.unsubscribe());
  });
  ```
  (Verify `onCleanup` against current docs.)

### Async (Resources)
- Product data uses a resource with proper loading/error handling and a Suspense boundary. No duplicate loading signal. Good.

### Prioritized Recommendations

#### Critical (This Week)
| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 1 | Stop destructuring props in `Badge` | Fixes stale UI | 10 min |
| 2 | Move list filter into a memo in tracking scope | Fixes stale list | 20 min |
| 3 | Convert derive-via-effect to a memo (Cart total) | Removes loop risk + extra signal | 20 min |

#### Medium (This Month)
| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 1 | Add `onCleanup` to LiveFeed subscription | Stops leak | 15 min |
| 2 | Remove the unnecessary memo around a trivial expression | Simpler graph | 10 min |

#### Patterns to Preserve
- Store with path-based updates and `<For>` rows
- Resource-based async with Suspense
- Live signal/prop access in JSX
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Analysis scoped to Solid's fine-grained reactivity correctness.
- **ST-02 (Structured Sequential Instructions):** Mental model → signals → derivations → stores → effects → async → verification.
- **RT-02 (Multi-Dimensional Analysis Framework):** Evaluates access, derivation, store updates, effects, and async together.
- **RT-05 (Evidence-Based Reasoning):** Each finding traces the reactive chain with code evidence.
- **DS-06 (Prioritization Guidance):** Recommendations ranked by impact/effort with confidence levels.

## Related Prompts

- [../svelte/frontend_svelte_component_patterns.md](../svelte/frontend_svelte_component_patterns.md) - Compare with Svelte's compiler-based fine-grained reactivity
- [../qwik/frontend_qwik_resumability.md](../qwik/frontend_qwik_resumability.md) - Another no-VDOM, fine-grained model (with resumability)
- [../architecture/frontend_state_management_selection.md](../architecture/frontend_state_management_selection.md) - Choosing signals vs stores vs external state
- [../performance/frontend_performance_core_web_vitals.md](../performance/frontend_performance_core_web_vitals.md) - Performance impact of over-running effects
