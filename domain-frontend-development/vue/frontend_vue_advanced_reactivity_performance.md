---
title: "Vue 3 Advanced Reactivity & Performance Analysis"
category: frontend-development/vue
description: "Audit Vue 3 reactivity usage — ref vs reactive, shallowRef/markRaw, computed/watch pitfalls, render-tracking, and large-list rendering — to find unnecessary reactivity and performance bottlenecks."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: advanced
tags:
  - vue
  - reactivity
  - performance
  - computed
  - watchers
  - virtualization
updated: "2026-06-21"
related_prompts:
  - domain-frontend-development/vue/frontend_vue_composition_api.md
  - domain-frontend-development/vue/frontend_vue_pinia_state.md
  - domain-frontend-development/vue/frontend_vue_testing.md
  - domain-frontend-development/performance/frontend_performance_core_web_vitals.md
---

# Vue 3 Advanced Reactivity & Performance Analysis

**Objective:** Audit a Vue 3 application's reactivity usage — `ref`/`reactive` choices, `shallowRef`/`markRaw` opportunities, `computed`/`watch` pitfalls, render-tracking overhead, and large-list rendering — to eliminate unnecessary reactivity and resolve performance bottlenecks.

**When to Use:**
- Use when: Components feel sluggish during interactions and the Vue DevTools "Highlight updates" / performance panel shows excessive re-rendering.
- Use when: Large datasets are stored in deeply reactive `reactive()`/`ref()` and proxy overhead is suspected.
- Use when: `watch`/`watchEffect` callbacks fire more often than expected or create infinite/redundant cycles.
- Use when: Long lists (hundreds/thousands of rows) render slowly or scroll poorly.
- Don't use when: There is no measured performance problem — converting refs to `shallowRef` prematurely can introduce subtle reactivity bugs.

## Instructions

1. **Inventory Reactive State**
   - List each piece of reactive state and how it's declared (`ref`, `reactive`, `shallowRef`, `shallowReactive`, `readonly`, plain non-reactive).
   - Note which state is deeply nested and large (big arrays, nested object trees, third-party class instances).
   - Flag state that never changes after initialization but is still wrapped reactively.

2. **Audit `ref` vs `reactive` Choices**
   - Confirm `reactive()` is only used for objects that benefit from deep reactivity, and that primitives use `ref`.
   - Flag destructuring of `reactive()` objects that silently drops reactivity (recommend `toRefs`/`toRef` where appropriate).
   - Flag reassignment of a whole `reactive()` object (which breaks the original proxy reference) where a `ref` holding an object would be clearer.

3. **Identify `shallowRef` / `markRaw` Opportunities**
   - For large data structures where only top-level replacement matters (e.g. an entire dataset swapped on fetch), evaluate `shallowRef`.
   - For non-reactive third-party instances (chart objects, map instances, large class instances), evaluate `markRaw` to skip proxy creation.
   - Verify any such change against intended mutation patterns — `shallowRef` will not react to nested mutation; confirm code replaces rather than mutates.

4. **Analyze `computed` Pitfalls**
   - Confirm computeds are pure (no side effects) and used for derived values rather than `watch`-style work.
   - Flag computeds that depend on large reactive structures and recompute expensively on unrelated changes.
   - Flag derived values implemented as methods (recomputing every render) where a cached `computed` would be cheaper.
   - Check for computeds that return new object/array references each time, defeating downstream memoization.

5. **Analyze `watch` / `watchEffect` Pitfalls**
   - For each watcher, identify the exact dependencies and whether `deep: true` is genuinely needed (deep watching large structures is costly).
   - Flag watchers that mutate state they also depend on (potential loops).
   - Confirm `flush` timing and cleanup (`onCleanup`/returned cleanup) are correct for async work.
   - Flag `watchEffect` that tracks more dependencies than intended; recommend explicit `watch` sources where precision matters.

6. **Review Render-Tracking Overhead**
   - Identify components whose template reads many reactive properties, causing broad re-render on small changes.
   - Evaluate `v-memo` for expensive sub-trees with stable inputs (verify the memo key correctly captures all inputs).
   - Confirm `key` usage in `v-for` is stable and unique (not array index for reorderable lists).

7. **Assess Large-List Rendering**
   - For long lists, evaluate virtualization (render only visible rows) versus rendering all rows.
   - Confirm row components are not each subscribing to broad reactive state.
   - Check for inline object/function creation in `v-for` that allocates per row on every render.

8. **CRITICAL: Verify findings before reporting**
   - For each finding, confirm the actual reactivity declaration and mutation pattern in code before recommending a change. Assign a Confidence level:
     - **High:** The pitfall is directly visible (e.g. `deep: true` on a large array, a computed with side effects) and the fix is safe given observed mutation patterns.
     - **Medium:** The pattern is likely costly but its impact depends on data size or change frequency you cannot fully see.
     - **Low:** A heuristic optimization (e.g. "consider `shallowRef` here") that requires the author to confirm nested mutations don't occur.
   - Do not assert a performance gain as a number; describe the mechanism and flag measurement as the verification step. Where behavior is Vue-version-dependent, note "verify against current docs."

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Don't recommend `shallowRef`/`markRaw` without confirming the code replaces (not nested-mutates) the value — it will silently break reactivity otherwise.
- Don't flag `reactive()` as wrong simply for being used; deep reactivity is appropriate for many forms/objects.
- Don't claim a `computed` is "unnecessary" without confirming it's actually read and that its result is reused.
- Don't recommend removing `deep: true` when the watcher genuinely needs nested change detection.
- Don't assert proxy overhead is the bottleneck without evidence that the structure is large and frequently accessed.
- Don't invent before/after performance numbers or frame-rate figures.
- Don't state version-specific reactivity internals as fact — phrase as "verify against current docs."

✅ **DO:**
- Trace how each reactive value is mutated before recommending a shallower wrapper.
- Distinguish "derived value" (use `computed`) from "side effect" (use `watch`).
- Cite the exact declaration, watcher source, or template binding as evidence.
- Recommend stable, unique `:key` values for reorderable `v-for` lists.
- Suggest virtualization only when list size and row cost justify the added complexity.
- Pair each recommendation with the verification step (DevTools highlight updates / performance panel).
- Prioritize fixes by measured/likely user-visible impact, not theoretical purity.

## Expected Output

A structured reactivity-and-performance report with a state inventory, per-finding detail (severity, confidence, location, evidence, recommendation), and a prioritized remediation list.

- Reactive state inventory table
- Per-finding analysis tied to a concrete reactivity mechanism
- Prioritized recommendations ordered by likely user-visible impact

### Output Format

```markdown
## Vue Reactivity & Performance Report

### Summary
- Reactivity hygiene: <good | mixed | over-reactive>
- Hot paths identified: <n>
- Total findings: <n> (High: <n>, Medium: <n>, Low: <n>)

### Reactive State Inventory
| State | Declaration | Size/Depth | Mutation pattern | Concern |
|-------|-------------|------------|------------------|---------|
| ... | ref/reactive/shallowRef | ... | replace/mutate | ... |

### Findings
#### [SEVERITY] <Title>
- **Severity:** Critical | High | Medium | Low
- **Confidence:** High | Medium | Low
- **Location:** <file:line / component>
- **Evidence:** <exact code construct>
- **Mechanism:** <why it costs render/compute time>
- **Recommendation:** <specific fix + verification step>

### Prioritized Recommendations
1. ...
```

## Example Output

```markdown
## Vue Reactivity & Performance Report

### Summary
- Reactivity hygiene: over-reactive (large dataset deeply reactive, deep watcher present)
- Hot paths identified: 2
- Total findings: 4 (High: 1, Medium: 2, Low: 1)

### Reactive State Inventory
| State        | Declaration | Size/Depth        | Mutation pattern | Concern |
|--------------|-------------|-------------------|------------------|---------|
| rows         | ref([])     | ~5,000 deep objs  | replaced on fetch| Deep proxy on full swap |
| chartInstance| ref(null)   | 3rd-party object  | replaced once    | Proxied unnecessarily |
| filters      | reactive({})| small             | mutated          | OK |

### Findings

#### [HIGH] Large dataset held in deep ref, then deep-watched
- **Severity:** High
- **Confidence:** High
- **Location:** components/DataGrid.vue:22
- **Evidence:**
  ```js
  const rows = ref([])               // ~5,000 nested objects
  watch(rows, recompute, { deep: true })
  ```
- **Mechanism:** Each fetch replaces `rows` wholesale, yet deep reactivity proxies every nested object and `deep: true` traverses the entire tree on change — large allocation and traversal cost.
- **Recommendation:** Use `shallowRef([])` since rows are replaced (not nested-mutated), and watch `rows` without `deep` (the reference change triggers it). Verify no code mutates `rows[i].field` in place; if it does, keep deep reactivity for those paths only. Confirm with DevTools update highlighting.

#### [MEDIUM] Third-party chart instance is reactive
- **Severity:** Medium
- **Confidence:** Medium
- **Location:** components/Chart.vue:15
- **Evidence:** `const chartInstance = ref(null); chartInstance.value = new Chart(...)`
- **Mechanism:** Wrapping a large external instance in a reactive proxy adds overhead and can break the library's internal identity checks.
- **Recommendation:** `chartInstance.value = markRaw(new Chart(...))` to skip proxying. Verify the instance is never expected to drive template reactivity.

#### [MEDIUM] Derived value computed in template as a method
- **Severity:** Medium
- **Confidence:** Medium
- **Location:** components/Summary.vue:31
- **Evidence:** `{{ computeTotals(rows) }}` called directly in template.
- **Mechanism:** The method re-runs on every render regardless of whether `rows` changed.
- **Recommendation:** Move to `const totals = computed(() => computeTotals(rows.value))` so the result is cached until dependencies change.

#### [LOW] Array index used as :key in a reorderable list
- **Severity:** Low
- **Confidence:** Low
- **Location:** components/DataGrid.vue:40
- **Evidence:** `<tr v-for="(r, i) in rows" :key="i">`
- **Mechanism:** Index keys cause incorrect DOM reuse when rows reorder, leading to subtle render bugs and wasted patches.
- **Recommendation:** Use a stable unique id: `:key="r.id"`. Confirm `r.id` is unique.

### Prioritized Recommendations
1. Convert the large replaced dataset to `shallowRef` and drop `deep: true` watching (largest render/compute win) — verify no in-place nested mutation first.
2. `markRaw` the chart instance to remove proxy overhead.
3. Replace the template method call with a cached `computed`.
4. Switch index keys to stable ids in reorderable lists.
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** States a single objective scoping the audit to reactivity choices, watchers/computeds, render tracking, and list rendering.
- **ST-02 (Structured Sequential Instructions):** Proceeds from a state inventory → declaration audits → computed/watch pitfalls → render and list overhead.
- **RT-02 (Multi-Dimensional Analysis Framework):** Separates proxy/allocation cost, recompute cost, render-tracking breadth, and list-rendering cost as distinct dimensions.
- **RT-05 (Evidence-Based Reasoning):** Requires citing the exact declaration or binding and confirming the mutation pattern before recommending a shallower wrapper.
- **DS-06 (Prioritization Guidance):** Orders recommendations by likely user-visible impact, with verification (DevTools) as the gate.

## Related Prompts
- [frontend_vue_composition_api.md](frontend_vue_composition_api.md) - Establish sound Composition API patterns underlying these reactivity choices.
- [frontend_vue_pinia_state.md](frontend_vue_pinia_state.md) - Apply the same reactivity discipline to store state.
- [frontend_vue_testing.md](frontend_vue_testing.md) - Add tests that lock in correct reactivity behavior after refactors.
- [../performance/frontend_performance_core_web_vitals.md](../performance/frontend_performance_core_web_vitals.md) - Tie reactivity fixes to measurable interaction metrics.
