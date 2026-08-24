---
title: "Svelte Component Patterns and Runes Analysis"
category: frontend-development/svelte
description: "Analyze Svelte applications for component architecture, Svelte 5 runes adoption, reactivity patterns, and migration from stores to modern Svelte idioms"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: intermediate
tags:
  - svelte
  - svelte5
  - runes
  - reactivity
  - component-patterns
  - stores
updated: "2026-03-19"
related_prompts:
  - domain-frontend-development/svelte/frontend_sveltekit_fullstack.md
  - domain-frontend-development/svelte/frontend_svelte_state_management.md
  - domain-frontend-development/vue/frontend_vue_composition_api.md
  - domain-frontend-development/react/frontend_react_component_patterns.md
---

# Svelte Component Patterns and Runes Analysis

**Objective:** Analyze a Svelte codebase for component architecture, reactivity patterns, and adoption of modern Svelte features (Svelte 5 runes), identifying opportunities to improve code quality, performance, and developer experience.

**When to Use:**
- Use when: Reviewing existing Svelte applications for pattern improvements
- Use when: Planning migration from Svelte 4 stores to Svelte 5 runes
- Use when: Evaluating reactivity patterns for correctness and efficiency
- Use when: Onboarding to a Svelte codebase
- Don't use when: Evaluating Svelte vs other frameworks (use comparison prompts)

## Instructions

1. **Assess Svelte Version and Feature Adoption**
   - Identify Svelte version (check `package.json`)
   - Determine runes mode: `<svelte:options runes={true} />` or runes by default (Svelte 5)
   - Check for legacy patterns:
     - `$:` reactive declarations (Svelte 4 and below)
     - `export let` props vs `$props()` rune
     - Writable/readable stores vs `$state`/`$derived`
     - `$$props`/`$$restProps` vs `$props()`
   - Review `svelte.config.js` configuration

2. **Analyze Component Architecture**
   - Component organization and file structure
   - Component composition patterns (slots, snippets, component injection)
   - Props design: types, defaults, spreading
   - Event handling: `on:event` (legacy) vs callback props or `$host()` events
   - Component sizing and responsibility boundaries
   - Two-way binding usage (`bind:`) — appropriate vs overused

3. **Evaluate Reactivity Patterns**
   - **Svelte 5 Runes** (if applicable):
     - `$state()` for reactive state
     - `$derived()` for computed values
     - `$effect()` for side effects
     - `$props()` for component inputs
     - `$bindable()` for two-way binding props
   - **Svelte 4 patterns** (if applicable):
     - `$:` reactive declarations
     - Store subscriptions (`$store` auto-subscription)
     - Reactive statements and blocks
   - Identify reactivity bugs:
     - Mutations not triggering updates (object/array mutations in Svelte 4)
     - Over-reactive computations
     - Missing cleanup in effects
     - Circular reactive dependencies

4. **Review State Management**
   - Local component state patterns
   - Shared state: stores (writable, readable, derived) or rune-based
   - Context API usage (`setContext`/`getContext`)
   - When stores/state is global vs scoped
   - State serialization for SSR (SvelteKit compatibility)

5. **CRITICAL: Verify findings before reporting**
   - Check Svelte version before suggesting runes or legacy patterns
   - Test reactivity issues by tracing the reactive chain
   - Consider that Svelte's compiler-based reactivity differs fundamentally from runtime frameworks
   - Verify that "missing reactivity" isn't just Svelte 4's array/object mutation behavior
   - **Confidence level** for each finding:
     - **High Confidence**: Clear bug or anti-pattern with evidence
     - **Medium Confidence**: Suboptimal but functional
     - **Low Confidence**: Style preference

## False-Positive Prevention (MUST follow)

**DON'T:**
- Flag `$:` reactive declarations as wrong in Svelte 4 codebases
- Report stores as outdated if the project isn't on Svelte 5
- Criticize two-way `bind:` usage for form inputs (that's idiomatic Svelte)
- Flag component files as "too large" when Svelte components naturally contain template + script + style
- Assume Svelte patterns should match React or Vue conventions
- Report `on:click` event syntax as wrong in Svelte 4 (only deprecated in Svelte 5)
- Suggest extracting tiny components that would lose Svelte's co-location benefits

**DO:**
- Respect Svelte's philosophy of minimal boilerplate and co-located concerns
- Consider that Svelte's compiler handles many optimizations automatically
- Verify reactivity bugs by understanding Svelte's compile-time reactive model
- Acknowledge that Svelte intentionally differs from React/Vue patterns
- Check if stores are still appropriate even in Svelte 5 (for Observable interop)
- Test that suggested runes migrations maintain the same behavior
- Consider the migration path when recommending Svelte 5 features

## Expected Output

A comprehensive Svelte patterns analysis including:
- Version and feature adoption assessment
- Component architecture review
- Reactivity pattern audit
- State management evaluation
- Prioritized recommendations

### Output Format

```markdown
## Svelte Component Patterns Analysis

### Executive Summary
[High-level assessment]

### Version & Feature Adoption
[Svelte version, runes mode, legacy patterns]

### Component Architecture
[Organization, composition, props design]

### Reactivity Audit
[Pattern correctness, bugs, optimization]

### State Management
[Stores, runes, context usage]

### Recommendations
[Prioritized improvements]
```

## Example Output

```markdown
## Svelte Component Patterns Analysis

### Executive Summary
The application is on Svelte 5 but only 30% of components use runes. Found 4 reactivity bugs related to object mutations in legacy `$:` blocks, 6 components with duplicated state management logic that should use shared rune-based state, and inconsistent prop patterns mixing `export let` with `$props()`. Recommend completing the runes migration and extracting 3 shared state modules.

### Version & Feature Adoption

**Svelte Version:** 5.1.3
**SvelteKit Version:** 2.8.1
**Runes Mode:** Opt-in (`runes: true` on 12/40 components)

| Feature | Available | Adopted | Assessment |
|---------|-----------|---------|------------|
| `$state()` rune | Yes | 30% (12 components) | Migration in progress |
| `$derived()` rune | Yes | 25% (10 components) | Partial adoption |
| `$effect()` rune | Yes | 20% (8 components) | Underused |
| `$props()` rune | Yes | 30% (12 components) | Inconsistent |
| Snippets (`{#snippet}`) | Yes | 5% (2 components) | Not adopted |
| `$bindable()` | Yes | 0% | Not adopted |
| Legacy `$:` declarations | N/A | 70% (28 components) | Needs migration |
| Svelte stores | N/A | 60% (8 store files) | Evaluate for runes migration |

### Component Architecture

**File Structure:**
```
src/
├── lib/
│   ├── components/
│   │   ├── ui/          # Reusable UI components (Button, Modal, etc.)
│   │   ├── features/    # Feature-specific components
│   │   └── layout/      # Layout components (Header, Sidebar)
│   ├── stores/          # Svelte stores (8 files)
│   ├── utils/           # Utility functions
│   └── types/           # TypeScript types
├── routes/              # SvelteKit routes
└── app.html
```

**Component Inventory:**

| Pattern | Count | Assessment |
|---------|-------|------------|
| `$props()` rune components | 12 | Modern, good |
| `export let` prop components | 28 | Legacy, migrate |
| Components using slots | 15 | Good composition |
| Components using snippets | 2 | Underadopted |
| Components with `bind:` | 18 | 12 appropriate (forms), 6 overused |

### Reactivity Audit

#### Bug 1: Object Mutation Not Triggering Update (Svelte 4 Pattern)
- **Severity:** Critical
- **Confidence:** High
- **Location:** `src/lib/components/features/TaskBoard.svelte:45`
- **Evidence:**
  ```svelte
  <script>
    // Svelte 4 pattern - mutation doesn't trigger reactivity
    let tasks = [];

    function moveTask(taskId, newColumn) {
      const task = tasks.find(t => t.id === taskId);
      task.column = newColumn;  // Mutation! Svelte 4 won't detect this
      // Missing: tasks = tasks; (reassignment trigger)
    }

    $: columnTasks = tasks.filter(t => t.column === currentColumn);
    // columnTasks won't update because tasks reference didn't change
  </script>
  ```
- **Fix (Svelte 5 runes):**
  ```svelte
  <script>
    let tasks = $state([]);

    function moveTask(taskId, newColumn) {
      const task = tasks.find(t => t.id === taskId);
      task.column = newColumn;  // Deep reactivity in Svelte 5 - this works!
    }

    let columnTasks = $derived(tasks.filter(t => t.column === currentColumn));
  </script>
  ```
- **Fix (Svelte 4 compatible):**
  ```svelte
  <script>
    let tasks = [];

    function moveTask(taskId, newColumn) {
      tasks = tasks.map(t =>
        t.id === taskId ? { ...t, column: newColumn } : t
      );  // Immutable update triggers reactivity
    }
  </script>
  ```

#### Bug 2: `$effect` Missing Cleanup
- **Severity:** High
- **Confidence:** High
- **Location:** `src/lib/components/features/LiveFeed.svelte:22`
- **Evidence:**
  ```svelte
  <script>
    let messages = $state([]);

    $effect(() => {
      const ws = new WebSocket('wss://api.example.com/feed');
      ws.onmessage = (e) => {
        messages.push(JSON.parse(e.data));
      };
      // Missing cleanup! WebSocket stays open after component unmounts
    });
  </script>
  ```
- **Fix:**
  ```svelte
  <script>
    let messages = $state([]);

    $effect(() => {
      const ws = new WebSocket('wss://api.example.com/feed');
      ws.onmessage = (e) => {
        messages.push(JSON.parse(e.data));
      };

      // Cleanup function - runs when effect re-runs or component unmounts
      return () => {
        ws.close();
      };
    });
  </script>
  ```

#### Bug 3: Circular Reactive Dependency
- **Severity:** Medium
- **Confidence:** High
- **Location:** `src/lib/components/features/PriceCalculator.svelte`
- **Evidence:**
  ```svelte
  <script>
    let price = $state(100);
    let tax = $state(0);
    let total = $state(0);

    // Circular: total depends on price+tax, but tax depends on total
    $effect(() => {
      total = price + tax;
    });

    $effect(() => {
      tax = total * 0.1;  // Circular! Updates total, which updates tax...
    });
  </script>
  ```
- **Fix:**
  ```svelte
  <script>
    let price = $state(100);
    let taxRate = $state(0.1);

    // Use $derived for computed values - no circular dependency
    let tax = $derived(price * taxRate);
    let total = $derived(price + tax);
  </script>
  ```

#### Issue 4: Overuse of Two-Way Binding
- **Severity:** Low
- **Confidence:** Medium
- **Found:** 6 non-form components using `bind:` for parent-child communication
- **Evidence:**
  ```svelte
  <!-- Parent -->
  <FilterPanel bind:selectedFilters bind:sortOrder bind:viewMode />

  <!-- FilterPanel.svelte - exposes internal state via binding -->
  <script>
    export let selectedFilters = [];
    export let sortOrder = 'asc';
    export let viewMode = 'grid';
  </script>
  ```
- **Impact:** Makes data flow bidirectional, harder to trace state changes
- **Recommendation:** Use callback props for explicit data flow:
  ```svelte
  <!-- Parent -->
  <FilterPanel
    {selectedFilters}
    {sortOrder}
    {viewMode}
    onFilterChange={(filters) => selectedFilters = filters}
    onSortChange={(sort) => sortOrder = sort}
    onViewChange={(view) => viewMode = view}
  />

  <!-- FilterPanel.svelte (Svelte 5) -->
  <script>
    let { selectedFilters, sortOrder, viewMode,
          onFilterChange, onSortChange, onViewChange } = $props();
  </script>
  ```
  Note: `bind:` is perfectly appropriate for form inputs (`bind:value`, `bind:checked`).

### State Management

**Current Approach:** Mix of Svelte stores and `$state` runes

| Store | Location | Type | Consumers | Migrate to Runes? |
|-------|----------|------|-----------|-------------------|
| `authStore` | `stores/auth.ts` | writable | 12 components | Yes - `$state` class |
| `cartStore` | `stores/cart.ts` | writable + derived | 8 components | Yes - `$state` class |
| `themeStore` | `stores/theme.ts` | writable | 4 components | Yes - simple `$state` |
| `notificationStore` | `stores/notifications.ts` | writable | 3 components | Yes - `$state` class |
| `websocketStore` | `stores/websocket.ts` | readable | 5 components | Keep - Observable pattern |

#### Recommended: Rune-Based State Classes

```typescript
// lib/state/cart.svelte.ts
class CartState {
  items = $state<CartItem[]>([]);

  get count() {
    return this.items.length;
  }

  get total() {
    return this.items.reduce((sum, item) => sum + item.price * item.quantity, 0);
  }

  add(item: CartItem) {
    const existing = this.items.find(i => i.id === item.id);
    if (existing) {
      existing.quantity += 1;  // Deep reactivity handles this
    } else {
      this.items.push({ ...item, quantity: 1 });
    }
  }

  remove(id: string) {
    this.items = this.items.filter(i => i.id !== id);
  }

  clear() {
    this.items = [];
  }
}

export const cart = new CartState();
```

```svelte
<!-- Usage in component - clean and simple -->
<script>
  import { cart } from '$lib/state/cart.svelte';
</script>

<p>Items: {cart.count}, Total: ${cart.total.toFixed(2)}</p>
<button onclick={() => cart.add(product)}>Add to Cart</button>
```

### Snippets vs Slots Migration

**Svelte 5 replaces slots with snippets for more flexible composition:**

```svelte
<!-- Svelte 4: Slots -->
<Card>
  <span slot="header">Title</span>
  <p>Content here</p>
  <span slot="footer">Footer</span>
</Card>

<!-- Svelte 5: Snippets -->
<Card>
  {#snippet header()}
    <span>Title</span>
  {/snippet}
  {#snippet footer()}
    <span>Footer</span>
  {/snippet}
  <p>Content here</p>
</Card>

<!-- Card.svelte (Svelte 5) -->
<script>
  let { header, footer, children } = $props();
</script>

<div class="card">
  <div class="card-header">{@render header()}</div>
  <div class="card-body">{@render children()}</div>
  <div class="card-footer">{@render footer()}</div>
</div>
```

### Prioritized Recommendations

#### Critical (Fix This Week)
| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 1 | Fix object mutation bug in TaskBoard | Data correctness | 30 min |
| 2 | Add cleanup to LiveFeed `$effect` | Memory leak fix | 15 min |
| 3 | Fix circular dependency in PriceCalculator | Infinite loop risk | 30 min |

#### High Priority (This Month)
| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 1 | Migrate 28 components from `export let` to `$props()` | Consistency | 1 week |
| 2 | Migrate `$:` declarations to `$derived`/`$effect` | Modern patterns | 1 week |
| 3 | Convert 4 stores to rune-based state classes | Simpler state | 3 days |
| 4 | Enable runes mode project-wide | Consistency | 1 hour + testing |

#### Medium Priority (This Quarter)
| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 1 | Replace 6 overused `bind:` with callback props | Clearer data flow | 3 hours |
| 2 | Adopt snippets for complex slot patterns | More flexible composition | 2 days |
| 3 | Add TypeScript to remaining untyped components | Type safety | 1 week |

### Patterns to Preserve
- **Component co-location**: Template, script, and style in single files
- **Context API for theme/auth**: Well-scoped, avoids global state
- **`bind:` for form inputs**: Idiomatic and ergonomic
- **Feature-based folder structure**: Clear organization
- **SvelteKit route conventions**: Proper use of `+page.svelte`, `+layout.svelte`
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Focused on Svelte component patterns
- **ST-02 (Structured Sequential Instructions):** Systematic review of Svelte concerns
- **RT-02 (Multi-Dimensional Analysis):** Covers components, reactivity, state, and composition
- **RT-05 (Evidence-Based Reasoning):** Code evidence for each finding
- **DS-06 (Prioritization Guidance):** Impact/effort ranking

## Related Prompts

- [frontend_sveltekit_fullstack.md](frontend_sveltekit_fullstack.md) - SvelteKit routing and server patterns
- [frontend_svelte_state_management.md](frontend_svelte_state_management.md) - Deep dive on state management
- [../vue/frontend_vue_composition_api.md](../vue/frontend_vue_composition_api.md) - Similar reactivity analysis in Vue
- [../react/frontend_react_component_patterns.md](../react/frontend_react_component_patterns.md) - Component patterns in React

## Customization Guide

- **For Svelte 4**: Focus on store patterns, `$:` declarations, and slot composition
- **For Svelte 5 Migration**: Emphasize runes adoption roadmap and store-to-runes migration
- **For SvelteKit Apps**: Include route-level patterns, server-side considerations
- **For Component Libraries**: Focus on prop design, slot/snippet flexibility, accessibility
- **For Small Projects**: De-emphasize complex state patterns; Svelte's simplicity is the feature
