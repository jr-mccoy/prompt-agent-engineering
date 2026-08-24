---
title: "Vue 3 Composition API Patterns Analysis"
category: frontend-development/vue
description: "Analyze Vue 3 applications for Composition API best practices, composable design, and migration from Options API patterns"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: intermediate
tags:
  - vue
  - vue3
  - composition-api
  - composables
  - reactivity
  - script-setup
updated: "2026-01-29"
related_prompts:
  - domain-frontend-development/vue/frontend_vue_pinia_state.md
  - domain-frontend-development/vue/frontend_vue_testing.md
  - domain-frontend-development/react/frontend_react_hooks_best_practices.md
---

# Vue 3 Composition API Patterns Analysis

**Objective:** Analyze a Vue 3 codebase for Composition API usage patterns, identify opportunities for composable extraction, and ensure proper reactivity and lifecycle handling.

**When to Use:**
- Use when: Reviewing Vue 3 codebases for pattern consistency
- Use when: Planning migration from Options API to Composition API
- Use when: Designing reusable composables for a Vue application
- Use when: Debugging reactivity issues in Vue 3
- Don't use when: Working with Vue 2 (requires different patterns)

## Instructions

1. **Assess Current Vue Patterns**
   - Which API style(s) are in use (Options, Composition, `<script setup>`)?
   - How are components organized?
   - Are composables extracted and reused?
   - What's the TypeScript integration level?

2. **Analyze Reactivity Usage**
   - Are `ref` and `reactive` used appropriately?
   - Check for reactivity loss (destructuring, passing to functions)
   - Verify computed properties are used for derived state
   - Check watchers for proper dependencies

3. **Evaluate Composable Design**
   - Are composables properly extracted and named (`use*`)?
   - Do composables follow single responsibility principle?
   - Is return value consistent (ref vs reactive)?
   - Are composables properly typed?

4. **Review Component Composition**
   - Proper use of props with validation
   - Event emission patterns (defineEmits)
   - Slot usage for flexible composition
   - Provide/inject for dependency injection

5. **CRITICAL: Validate Findings**
   - Test reactivity issues in actual runtime
   - Verify patterns match Vue 3 best practices
   - Consider team experience and codebase constraints
   - **Confidence level** for each finding:
     - **High Confidence**: Clear pattern violation with bug potential
     - **Medium Confidence**: Suboptimal but functional pattern
     - **Low Confidence**: Style preference

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Flag Options API as "wrong" (both APIs are supported)
- Report all prop destructuring as reactivity loss (only reactive refs matter)
- Suggest composable extraction for one-time logic
- Criticize `ref` vs `reactive` choice without context
- Flag watchers with immediate: true as problematic
- Assume all shared logic needs composables

✅ **DO:**
- Trace actual reactivity flow before flagging issues
- Consider migration effort vs benefit for Options API code
- Verify that "reactivity loss" actually causes bugs
- Acknowledge valid use cases for both ref and reactive
- Check if patterns align with Vue core team recommendations
- Test findings with Vue DevTools reactivity tracking

## Expected Output

A comprehensive Vue patterns analysis including:
- Current patterns inventory
- Reactivity issue identification
- Composable opportunities
- Migration recommendations (if applicable)
- Prioritized improvements

### Output Format

```markdown
## Vue Composition API Analysis

### Patterns Inventory
[Current usage of Options vs Composition vs script setup]

### Reactivity Analysis
[Issues with reactive state management]

### Composables Assessment
[Current composables and extraction opportunities]

### Recommendations
[Prioritized improvements]
```

## Example Output

```markdown
## Vue Composition API Analysis

### Executive Summary
The codebase uses a mix of Options API (40%), Composition API (35%), and `<script setup>` (25%). Found 3 critical reactivity bugs, 8 composable extraction opportunities, and inconsistent patterns across teams. Recommend standardizing on `<script setup>` with TypeScript and extracting 5 core composables for common patterns.

### Patterns Inventory

| Pattern | Usage | Files | Assessment |
|---------|-------|-------|------------|
| `<script setup>` + TypeScript | 25% | 38 | ✅ Target pattern |
| Composition API (setup function) | 35% | 52 | ⚠️ Migrate to script setup |
| Options API | 40% | 60 | ⚠️ Gradually migrate |

**Component Organization:**
- Feature-based folders: ✅
- Naming convention: PascalCase ✅
- Single File Components: 100% ✅
- TypeScript adoption: 65%

### Reactivity Analysis

#### Critical Issue 1: Reactivity Lost in Destructuring
- **Severity:** Critical
- **Confidence:** High
- **Location:** `src/composables/useUser.ts:15`
- **Problem:** Destructuring reactive object loses reactivity
```typescript
// ❌ Reactivity lost - name and email won't update
const useUser = () => {
  const user = reactive({ name: '', email: '' });

  async function fetchUser(id: string) {
    const data = await api.getUser(id);
    Object.assign(user, data);
  }

  // Destructuring breaks reactivity!
  const { name, email } = user;
  return { name, email, fetchUser };
};

// Component using this:
const { name, email } = useUser();
// name and email are static strings, not reactive
```
- **Fix:**
```typescript
// ✅ Option A: Return refs
const useUser = () => {
  const name = ref('');
  const email = ref('');

  async function fetchUser(id: string) {
    const data = await api.getUser(id);
    name.value = data.name;
    email.value = data.email;
  }

  return { name, email, fetchUser };
};

// ✅ Option B: Return reactive and use toRefs
const useUser = () => {
  const user = reactive({ name: '', email: '' });

  return { ...toRefs(user), fetchUser };
};

// ✅ Option C: Return whole reactive object
const useUser = () => {
  const user = reactive({ name: '', email: '' });
  return { user, fetchUser };
};
```

#### Critical Issue 2: Watch Missing Dependencies
- **Severity:** Critical
- **Confidence:** High
- **Location:** `src/views/ProductList.vue:42`
- **Problem:** Watch depends on reactive value not in dependencies
```typescript
// ❌ category changes won't trigger refetch
const category = ref('all');
const page = ref(1);

watch(page, () => {
  // Uses category.value but doesn't watch it!
  fetchProducts(category.value, page.value);
});
```
- **Fix:**
```typescript
// ✅ Watch both dependencies
watch([page, category], ([newPage, newCategory]) => {
  fetchProducts(newCategory, newPage);
});

// Or use watchEffect for automatic dependency tracking
watchEffect(() => {
  fetchProducts(category.value, page.value);
});
```

#### Critical Issue 3: Computed Without Dependencies
- **Severity:** Medium
- **Confidence:** High
- **Location:** `src/components/CartTotal.vue:28`
- **Problem:** Computed uses non-reactive value, never updates
```typescript
// ❌ priceMap is plain object, not reactive
const priceMap = { USD: 1, EUR: 0.85 };

const total = computed(() => {
  return items.value.reduce((sum, item) =>
    sum + item.price * priceMap[currency.value], 0
  );
});
// If priceMap changes, computed won't update (but works if currency changes)
```
- **Fix:**
```typescript
// ✅ Make priceMap reactive if it needs to update
const priceMap = reactive({ USD: 1, EUR: 0.85 });

// Or fetch dynamically in the computed
const total = computed(async () => {
  const rate = await getExchangeRate(currency.value);
  return items.value.reduce((sum, item) => sum + item.price * rate, 0);
});
```

### Composables Assessment

#### Existing Composables

| Composable | Location | Quality | Issues |
|------------|----------|---------|--------|
| `useAuth` | `/composables/useAuth.ts` | Good | Missing TypeScript |
| `useApi` | `/composables/useApi.ts` | Good | Error handling inconsistent |
| `useForm` | `/composables/useForm.ts` | Needs work | Reactivity issue (above) |
| `useLocalStorage` | `/composables/useLocalStorage.ts` | Good | SSR unsafe |

#### Composable Extraction Opportunities

**Opportunity 1: Extract `useDebounce`**
- **Location:** Pattern repeated in 8 files
- **Evidence:**
```typescript
// Same pattern in ProductSearch, UserSearch, FilterPanel, etc.
const searchQuery = ref('');
let timeout: number;

watch(searchQuery, (value) => {
  clearTimeout(timeout);
  timeout = setTimeout(() => {
    search(value);
  }, 300);
});
```
- **Recommendation:**
```typescript
// composables/useDebounce.ts
export function useDebounce<T>(value: Ref<T>, delay = 300) {
  const debounced = ref(value.value) as Ref<T>;

  watch(value, (newValue) => {
    const timeout = setTimeout(() => {
      debounced.value = newValue;
    }, delay);

    onUnmounted(() => clearTimeout(timeout));
  });

  return debounced;
}

// Usage
const query = ref('');
const debouncedQuery = useDebounce(query, 300);
watch(debouncedQuery, (value) => search(value));
```

**Opportunity 2: Extract `useAsyncState`**
- **Pattern:** Loading/error/data state repeated 12 times
- **Files:** Various data-fetching components
```typescript
// Current pattern repeated everywhere
const data = ref(null);
const loading = ref(false);
const error = ref(null);

async function fetchData() {
  loading.value = true;
  error.value = null;
  try {
    data.value = await api.getData();
  } catch (e) {
    error.value = e;
  } finally {
    loading.value = false;
  }
}
```
- **Recommendation:** Use VueUse's `useAsyncState` or create custom:
```typescript
// composables/useAsyncState.ts
export function useAsyncState<T>(
  asyncFn: () => Promise<T>,
  initialState: T
) {
  const state = ref(initialState) as Ref<T>;
  const isLoading = ref(false);
  const error = ref<Error | null>(null);

  async function execute() {
    isLoading.value = true;
    error.value = null;
    try {
      state.value = await asyncFn();
    } catch (e) {
      error.value = e as Error;
    } finally {
      isLoading.value = false;
    }
  }

  return { state, isLoading, error, execute };
}
```

**Opportunity 3: Extract `usePagination`**
- **Pattern:** Pagination logic in 6 list components
- **Recommendation:** Create shared pagination composable

### Script Setup Migration Guide

**Current (Composition API with setup function):**
```vue
<script lang="ts">
import { defineComponent, ref, computed } from 'vue';
import type { PropType } from 'vue';

export default defineComponent({
  props: {
    items: {
      type: Array as PropType<Item[]>,
      required: true
    }
  },
  emits: ['select'],
  setup(props, { emit }) {
    const selected = ref<Item | null>(null);
    const itemCount = computed(() => props.items.length);

    function selectItem(item: Item) {
      selected.value = item;
      emit('select', item);
    }

    return { selected, itemCount, selectItem };
  }
});
</script>
```

**Target (`<script setup>`):**
```vue
<script setup lang="ts">
import { ref, computed } from 'vue';

interface Item {
  id: string;
  name: string;
}

const props = defineProps<{
  items: Item[];
}>();

const emit = defineEmits<{
  select: [item: Item];
}>();

const selected = ref<Item | null>(null);
const itemCount = computed(() => props.items.length);

function selectItem(item: Item) {
  selected.value = item;
  emit('select', item);
}
</script>
```

**Benefits:**
- 40% less boilerplate
- Better TypeScript inference
- Cleaner template bindings
- Better tree-shaking

### Provide/Inject Patterns

**Current Issue:** Props drilling through 4 levels
**Location:** `ThemeContext` → `Layout` → `Sidebar` → `NavItem`

**Recommendation:**
```typescript
// composables/useTheme.ts
import { provide, inject, ref, type Ref, type InjectionKey } from 'vue';

interface ThemeContext {
  theme: Ref<'light' | 'dark'>;
  toggleTheme: () => void;
}

export const ThemeKey: InjectionKey<ThemeContext> = Symbol('theme');

export function provideTheme() {
  const theme = ref<'light' | 'dark'>('light');

  function toggleTheme() {
    theme.value = theme.value === 'light' ? 'dark' : 'light';
  }

  provide(ThemeKey, { theme, toggleTheme });

  return { theme, toggleTheme };
}

export function useTheme() {
  const context = inject(ThemeKey);
  if (!context) {
    throw new Error('useTheme must be used within ThemeProvider');
  }
  return context;
}
```

### Prioritized Recommendations

#### Critical (Fix This Week)
| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 1 | Fix useUser reactivity loss | Bug fix | 30 min |
| 2 | Fix watch dependencies in ProductList | Bug fix | 30 min |
| 3 | Make priceMap reactive in CartTotal | Bug fix | 15 min |

#### High Priority (This Month)
| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 1 | Extract useDebounce composable | DRY, maintainability | 2h |
| 2 | Extract useAsyncState composable | DRY, consistency | 3h |
| 3 | Add TypeScript to remaining composables | Type safety | 4h |
| 4 | Standardize on script setup for new code | Consistency | Ongoing |

#### Medium Priority (This Quarter)
| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 1 | Migrate 60 Options API components | Consistency | 2 weeks |
| 2 | Implement provide/inject for theme | Clean architecture | 4h |
| 3 | Add composable unit tests | Reliability | 1 week |

### VueUse Integration

Consider adopting VueUse for common composables instead of writing custom:

| Pattern | Custom Effort | VueUse Equivalent |
|---------|---------------|-------------------|
| Debounce | 2h | `useDebounceFn`, `useDebounce` |
| LocalStorage | 3h | `useLocalStorage` |
| Window size | 1h | `useWindowSize` |
| Async state | 3h | `useAsyncState` |
| Intersection | 2h | `useIntersectionObserver` |

**Installation:** `npm install @vueuse/core`
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Focused on Composition API patterns
- **ST-02 (Structured Sequential Instructions):** Systematic analysis process
- **RT-02 (Multi-Dimensional Analysis):** Covers reactivity, composables, organization
- **RT-05 (Evidence-Based Reasoning):** Code examples for each finding
- **DS-06 (Prioritization Guidance):** Priority ranking for recommendations

## Related Prompts

- [frontend_vue_pinia_state.md](frontend_vue_pinia_state.md) - State management
- [frontend_vue_testing.md](frontend_vue_testing.md) - Testing Vue components
- [frontend_react_hooks_best_practices.md](../react/frontend_react_hooks_best_practices.md) - Similar patterns in React

## Customization Guide

- **For Nuxt 3**: Include auto-imports, server composables, `useAsyncData`
- **For Vue 2**: Focus on Options API patterns (Composition API via plugin)
- **For Large Apps**: Emphasize composable organization and module boundaries
- **For TypeScript Heavy**: Focus on type inference and generic composables
