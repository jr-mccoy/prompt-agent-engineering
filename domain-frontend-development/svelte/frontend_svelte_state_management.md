---
title: "Svelte State Management Analysis"
category: frontend-development/svelte
description: "Analyze Svelte applications for state management patterns including rune-based state, stores, context API, and shared state architecture"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: intermediate
tags:
  - svelte
  - state-management
  - stores
  - runes
  - context
  - shared-state
updated: "2026-03-19"
related_prompts:
  - domain-frontend-development/svelte/frontend_svelte_component_patterns.md
  - domain-frontend-development/svelte/frontend_sveltekit_fullstack.md
  - domain-frontend-development/react/frontend_react_state_management.md
  - domain-frontend-development/vue/frontend_vue_pinia_state.md
---

# Svelte State Management Analysis

**Objective:** Analyze a Svelte application's state management architecture, evaluate the mix of local state, shared state, stores, and context usage, and recommend the optimal state strategy for the application's complexity and requirements.

**When to Use:**
- Use when: State management feels tangled or inconsistent across the app
- Use when: Choosing between stores, runes, and context for new features
- Use when: Migrating from Svelte stores to Svelte 5 rune-based state
- Use when: Debugging state synchronization issues or stale state bugs
- Don't use when: Application has minimal shared state (local state is fine)

## Instructions

1. **Inventory State Management Approaches**
   - Local component state (`let` variables, `$state()` runes)
   - Svelte stores (`writable`, `readable`, `derived`)
   - Rune-based shared state (`$state` in `.svelte.ts` modules)
   - Context API (`setContext`/`getContext`)
   - URL state (search params, route params via SvelteKit)
   - External state (localStorage, sessionStorage, cookies)
   - Server state (SvelteKit load function data)

2. **Evaluate State Architecture**
   - Is state stored at the right level? (component vs shared vs global)
   - Are there "god stores" handling too many concerns?
   - Is derived/computed state properly computed or duplicated?
   - State synchronization: is there a single source of truth?
   - State serialization: does state survive SSR correctly?

3. **Analyze Store Patterns (if using stores)**
   - Custom store patterns (get/set encapsulation)
   - Derived store chains and performance
   - Store subscription cleanup
   - Auto-subscription (`$store`) vs manual subscription
   - Store initialization and reset patterns

4. **Analyze Rune-Based State (if Svelte 5)**
   - `$state()` usage and granularity
   - `$derived()` for computed values
   - `$effect()` for side effects (avoid overuse)
   - Class-based state modules (`.svelte.ts` files)
   - Deep reactivity behavior with objects and arrays

5. **CRITICAL: Verify findings before reporting**
   - Test state behavior during SSR and client navigation
   - Verify that "stale state" isn't a SvelteKit invalidation issue
   - Check that store cleanup happens correctly
   - Ensure suggestions don't break SSR (singleton state on server is shared across requests!)
   - **Confidence level** for each finding:
     - **High Confidence**: State bug or security issue with evidence
     - **Medium Confidence**: Architecture concern likely to cause issues at scale
     - **Low Confidence**: Style preference

## False-Positive Prevention (MUST follow)

**DON'T:**
- Flag local `let` state as "unmanaged" (it's the simplest valid approach)
- Suggest stores/rune modules for state used in a single component
- Report missing derived stores when a simple `$:` or `$derived` suffices
- Criticize Svelte stores in Svelte 5 (they still work and are valid for Observable patterns)
- Flag context API as "prop drilling alternative" (it has different semantics)
- Suggest moving all state to global stores (component-local state is preferred in Svelte)
- Report "missing state management library" (Svelte's built-in tools are sufficient)

**DO:**
- Respect Svelte's philosophy: local state first, shared state only when needed
- Consider SSR implications for all shared state recommendations
- Verify store subscriptions are cleaned up (auto-subscription handles this in components)
- Check if rune-based state handles deep reactivity correctly for the use case
- Test that state suggestions work with SvelteKit's navigation lifecycle
- Acknowledge that Svelte doesn't need Redux/MobX/Zustand equivalents
- Consider the team's Svelte version before recommending runes patterns

## Expected Output

A comprehensive state management analysis including:
- State inventory across the application
- Architecture assessment
- Pattern-specific issues
- Migration recommendations (if applicable)
- Prioritized improvements

### Output Format

```markdown
## Svelte State Management Analysis

### State Inventory
[All state approaches cataloged]

### Architecture Assessment
[Level, scope, and organization]

### Issues and Anti-Patterns
[Problems found with evidence]

### Migration Path (if applicable)
[Store to runes migration plan]

### Recommendations
[Prioritized improvements]
```

## Example Output

```markdown
## Svelte State Management Analysis

### Executive Summary
The application uses 8 Svelte stores, 3 context providers, and local state across 40 components. Main issues: (1) a `globalStore` handling 7 unrelated concerns should be split, (2) two stores create shared state on the server which leaks between requests in SSR, and (3) derived state is manually synchronized instead of using `$derived` or derived stores. Recommend splitting the god store, fixing the SSR state leak, and migrating to rune-based state classes.

### State Inventory

| Approach | Count | Assessment |
|----------|-------|------------|
| Local `$state()` | 22 components | Good - appropriate for local UI |
| Local `let` (legacy) | 18 components | Migrate to `$state` |
| Svelte writable stores | 6 stores | 2 need splitting, 2 have SSR issues |
| Svelte derived stores | 4 stores | Good |
| Context API | 3 providers | Good scoping |
| Rune-based shared state (`.svelte.ts`) | 2 modules | Modern, expand |
| URL state (SvelteKit) | 4 routes | Good |
| localStorage | 3 uses | 1 missing SSR guard |

### Architecture Assessment

**State Location Map:**

```
Global (singleton)
├── authStore (writable)      → User auth state
├── themeStore (writable)     → Theme preference
├── globalStore (writable)    → ⚠️ God store: notifications, sidebar,
│                               modal, breadcrumbs, locale, feature flags,
│                               onboarding state
└── cartState (.svelte.ts)    → Cart items (rune-based)

Scoped (context)
├── FormContext               → Form state within multi-step forms
├── TableContext              → Table column/sort config
└── WizardContext             → Wizard step state

Route-level (SvelteKit)
├── +layout.server.ts         → User data, permissions
└── +page.server.ts           → Page-specific data
```

### Issues and Anti-Patterns

#### Issue 1: God Store (7 Unrelated Concerns)
- **Severity:** High
- **Confidence:** High
- **Location:** `src/lib/stores/global.ts`
- **Evidence:**
  ```typescript
  // One store handling 7 unrelated concerns
  import { writable, derived } from 'svelte/store';

  interface GlobalState {
    notifications: Notification[];
    sidebarOpen: boolean;
    activeModal: string | null;
    breadcrumbs: Breadcrumb[];
    locale: string;
    featureFlags: Record<string, boolean>;
    onboardingStep: number;
  }

  export const globalStore = writable<GlobalState>({
    notifications: [],
    sidebarOpen: true,
    activeModal: null,
    breadcrumbs: [],
    locale: 'en',
    featureFlags: {},
    onboardingStep: 0,
  });

  // Consumers must subscribe to everything to read one field
  // Changing notifications triggers re-render in sidebar observer
  ```
- **Impact:** Every subscriber re-renders on any state change. Tight coupling. Hard to test.
- **Recommendation:** Split into focused state modules:
  ```typescript
  // lib/state/notifications.svelte.ts
  class NotificationState {
    items = $state<Notification[]>([]);
    unreadCount = $derived(this.items.filter(n => !n.read).length);

    add(notification: Notification) {
      this.items.push(notification);
    }

    markRead(id: string) {
      const item = this.items.find(n => n.id === id);
      if (item) item.read = true;
    }

    dismiss(id: string) {
      this.items = this.items.filter(n => n.id !== id);
    }
  }
  export const notifications = new NotificationState();

  // lib/state/ui.svelte.ts
  class UIState {
    sidebarOpen = $state(true);
    activeModal = $state<string | null>(null);
    breadcrumbs = $state<Breadcrumb[]>([]);

    toggleSidebar() { this.sidebarOpen = !this.sidebarOpen; }
    openModal(id: string) { this.activeModal = id; }
    closeModal() { this.activeModal = null; }
  }
  export const ui = new UIState();

  // lib/state/preferences.svelte.ts
  class PreferencesState {
    locale = $state('en');
    featureFlags = $state<Record<string, boolean>>({});

    setLocale(locale: string) { this.locale = locale; }
    isEnabled(flag: string) { return this.featureFlags[flag] ?? false; }
  }
  export const preferences = new PreferencesState();
  ```

#### Issue 2: SSR State Leak (Critical)
- **Severity:** Critical (Security)
- **Confidence:** High
- **Location:** `src/lib/stores/cart.ts`, `src/lib/stores/global.ts`
- **Evidence:**
  ```typescript
  // cart.ts - Module-level singleton
  import { writable } from 'svelte/store';

  // This is created ONCE on the server and shared across ALL requests!
  export const cartStore = writable<CartItem[]>([]);

  // User A adds items → User B sees User A's cart!
  ```
- **Impact:** In SSR, module-level state persists across requests. One user's state leaks to another.
- **Fix Option A:** Use SvelteKit's context for request-scoped state:
  ```typescript
  // In +layout.server.ts - per-request data
  export const load: LayoutServerLoad = async ({ cookies }) => {
    const cart = await getCartFromSession(cookies);
    return { cart };
  };
  ```
- **Fix Option B:** Use context API for component-scoped state:
  ```svelte
  <!-- +layout.svelte -->
  <script>
    import { setContext } from 'svelte';
    import { CartState } from '$lib/state/cart.svelte';

    // New instance per component tree (per request in SSR)
    const cart = new CartState();
    setContext('cart', cart);
  </script>
  ```
- **Fix Option C:** Guard with `browser` check:
  ```typescript
  import { browser } from '$app/environment';

  class CartState {
    items = $state<CartItem[]>([]);

    constructor() {
      if (browser) {
        // Only initialize from localStorage on client
        const saved = localStorage.getItem('cart');
        if (saved) this.items = JSON.parse(saved);
      }
    }
  }

  // Only export singleton for client-side usage
  export const cart = browser ? new CartState() : null;
  ```

#### Issue 3: Manual State Synchronization
- **Severity:** Medium
- **Confidence:** High
- **Found:** 5 instances of manually keeping derived state in sync
- **Evidence:**
  ```svelte
  <script>
    let items = $state([]);
    let total = $state(0);
    let itemCount = $state(0);

    // Manually syncing derived values - error prone!
    function addItem(item) {
      items.push(item);
      total = items.reduce((sum, i) => sum + i.price, 0);
      itemCount = items.length;
    }

    function removeItem(id) {
      items = items.filter(i => i.id !== id);
      total = items.reduce((sum, i) => sum + i.price, 0);
      itemCount = items.length;
      // What if we forget to update total in a new function?
    }
  </script>
  ```
- **Fix:** Use `$derived` for computed values:
  ```svelte
  <script>
    let items = $state([]);

    // Automatically computed - always correct
    let total = $derived(items.reduce((sum, i) => sum + i.price, 0));
    let itemCount = $derived(items.length);

    function addItem(item) {
      items.push(item);
      // total and itemCount update automatically
    }

    function removeItem(id) {
      items = items.filter(i => i.id !== id);
      // total and itemCount update automatically
    }
  </script>
  ```

#### Issue 4: Missing SSR Guard for localStorage
- **Severity:** Medium
- **Confidence:** High
- **Location:** `src/lib/stores/theme.ts`
- **Evidence:**
  ```typescript
  import { writable } from 'svelte/store';

  // Crashes during SSR: localStorage is not defined
  const stored = localStorage.getItem('theme');
  export const themeStore = writable(stored ?? 'light');
  ```
- **Fix:**
  ```typescript
  import { writable } from 'svelte/store';
  import { browser } from '$app/environment';

  const stored = browser ? localStorage.getItem('theme') : null;
  export const themeStore = writable(stored ?? 'light');

  // Persist on change (client-only)
  if (browser) {
    themeStore.subscribe(value => {
      localStorage.setItem('theme', value);
    });
  }
  ```

### State Strategy Recommendation

**Decision guide for this application:**

| State Type | Approach | Example |
|-----------|----------|---------|
| Component UI state | `$state()` locally | Dropdown open, form inputs |
| Derived values | `$derived()` | Totals, filtered lists, counts |
| Side effects | `$effect()` sparingly | Sync to localStorage, analytics |
| Shared app state | Rune class in `.svelte.ts` | Cart, notifications, UI |
| Auth/user data | SvelteKit load + context | User session, permissions |
| Theme/preferences | Rune class + localStorage | Theme, locale |
| Form wizard state | Context API | Multi-step form state |
| URL-driven state | SvelteKit `$page`, searchParams | Filters, pagination, sort |
| Server data | SvelteKit load functions | DB queries, API data |
| Real-time data | Svelte store (Observable interop) | WebSocket streams |

### Store to Runes Migration Guide

**Phase 1: New code uses runes (Immediate)**
- All new components use `$state`, `$derived`, `$effect`
- New shared state uses `.svelte.ts` rune classes

**Phase 2: Simple store conversions (1 week)**
```typescript
// Before: Svelte store
import { writable, derived } from 'svelte/store';

export const count = writable(0);
export const doubled = derived(count, $count => $count * 2);

// After: Rune-based
// counter.svelte.ts
export const count = $state(0);  // Not valid at module level!

// Correct: Use a class
class CounterState {
  count = $state(0);
  doubled = $derived(this.count * 2);

  increment() { this.count++; }
  decrement() { this.count--; }
  reset() { this.count = 0; }
}
export const counter = new CounterState();
```

**Phase 3: Complex store conversions (2 weeks)**
- Convert stores with async operations
- Update all consumer components
- Test SSR behavior

**Phase 4: Remove store imports (1 week)**
- Remove `svelte/store` imports
- Clean up `$store` auto-subscriptions
- Verify no regressions

### Prioritized Recommendations

#### Critical (Fix Immediately)
| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 1 | Fix SSR state leak in cart and global stores | Security — data leaks between users | 2 hours |
| 2 | Add `browser` guard to localStorage access | Fix SSR crashes | 30 min |

#### High Priority (This Week)
| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 1 | Split global store into focused modules | Maintainability, performance | 4 hours |
| 2 | Replace 5 manual sync patterns with `$derived` | Correctness, less code | 2 hours |
| 3 | Establish rune-first convention for new code | Consistency | Ongoing |

#### Medium Priority (This Month)
| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 1 | Migrate 6 stores to rune-based state classes | Modern patterns | 1 week |
| 2 | Migrate 18 `let` components to `$state` | Consistency | 3 days |
| 3 | Add TypeScript to all state modules | Type safety | 2 days |

### Patterns to Preserve
- **Context API for scoped state**: Form wizard, table config
- **SvelteKit load functions for server data**: Proper SSR data flow
- **URL state for shareable/bookmarkable state**: Filters, pagination
- **Local state for UI-only concerns**: Dropdowns, toggles, hover
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Focused on state management evaluation
- **ST-02 (Structured Sequential Instructions):** Systematic audit of state layers
- **RT-02 (Multi-Dimensional Analysis):** Covers stores, runes, context, SSR, URL state
- **RT-05 (Evidence-Based Reasoning):** Code evidence for each issue
- **DS-06 (Prioritization Guidance):** Security-first prioritization

## Related Prompts

- [frontend_svelte_component_patterns.md](frontend_svelte_component_patterns.md) - Component reactivity patterns
- [frontend_sveltekit_fullstack.md](frontend_sveltekit_fullstack.md) - SvelteKit load functions and server state
- [../react/frontend_react_state_management.md](../react/frontend_react_state_management.md) - State management concepts in React
- [../vue/frontend_vue_pinia_state.md](../vue/frontend_vue_pinia_state.md) - State management in Vue

## Customization Guide

- **For Svelte 4**: Focus on store patterns, `$:` declarations, and context API
- **For Svelte 5**: Emphasize rune-based state classes and migration from stores
- **For SvelteKit SSR**: Focus on SSR safety, request-scoped state, and load function patterns
- **For Real-time Apps**: Keep Svelte stores for Observable/WebSocket interop
- **For Simple Apps**: Emphasize local state; avoid over-engineering with shared state
