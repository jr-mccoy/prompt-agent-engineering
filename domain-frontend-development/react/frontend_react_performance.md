---
title: "React Performance Optimization Analysis"
category: frontend-development/react
description: "Analyze React applications for performance issues including unnecessary re-renders, bundle size, and rendering bottlenecks with actionable optimization strategies"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: advanced
tags:
  - react
  - performance
  - optimization
  - re-renders
  - profiling
  - memoization
updated: "2026-01-29"
related_prompts:
  - domain-frontend-development/performance/frontend_performance_core_web_vitals.md
  - domain-frontend-development/performance/frontend_performance_bundle_optimization.md
  - domain-frontend-development/react/frontend_react_hooks_best_practices.md
---

# React Performance Optimization Analysis

**Objective:** Analyze a React application for performance issues, identify bottlenecks causing slow renders or poor user experience, and provide specific optimization strategies with measurable impact.

**When to Use:**
- Use when: Application feels slow or janky during interactions
- Use when: React DevTools Profiler shows unexpected re-renders
- Use when: Bundle size is growing beyond acceptable limits
- Use when: Core Web Vitals are below targets
- Don't use when: Optimizing prematurely without measured problems

## Instructions

1. **Profile the Application**
   - Use React DevTools Profiler to identify slow components
   - Measure initial load time (LCP, FCP)
   - Measure interaction responsiveness (INP)
   - Identify render counts per interaction

2. **Analyze Re-render Patterns**
   For components that render frequently:
   - What state changes trigger the re-render?
   - Is the component receiving new object/array references?
   - Are child components memoized appropriately?
   - Is context usage causing broad re-renders?

3. **Review Bundle Size**
   - Analyze bundle with webpack-bundle-analyzer or similar
   - Identify large dependencies
   - Check for duplicate packages
   - Evaluate code splitting opportunities

4. **Check Rendering Patterns**
   - List virtualization for long lists
   - Lazy loading for below-the-fold content
   - Suspense boundaries for code splitting
   - Image optimization and lazy loading

5. **CRITICAL: Validate Before Optimizing**
   - Profile before and after each change
   - Don't optimize without measured problems
   - Verify optimizations don't break functionality
   - Consider maintenance cost of optimizations
   - **Confidence level** for each issue:
     - **High Confidence**: Profiler shows clear bottleneck
     - **Medium Confidence**: Pattern likely causes issues at scale
     - **Low Confidence**: Theoretical concern, needs measurement

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Wrap every component in React.memo without profiling
- Add useMemo/useCallback to everything "just in case"
- Optimize components that render quickly (<16ms)
- Assume large components are slow (profile first!)
- Virtualize lists with fewer than 100 items
- Break functionality for performance gains
- Optimize without measuring the impact

✅ **DO:**
- Profile before making any optimizations
- Focus on components with high render time × render count
- Measure before/after for every optimization
- Consider the cost of memoization (memory, complexity)
- Start with biggest impact optimizations first
- Test on low-end devices, not just developer machines
- Document why each optimization was added

## Expected Output

A comprehensive performance analysis including:
- Profiling results and bottleneck identification
- Re-render analysis with causes
- Bundle size analysis
- Prioritized optimization recommendations
- Before/after metrics for suggested changes

### Output Format

```markdown
## React Performance Analysis

### Performance Profile Summary
[Key metrics and bottlenecks]

### Re-render Analysis
[Components with excessive re-renders and causes]

### Bundle Analysis
[Size breakdown and optimization opportunities]

### Optimization Recommendations
[Prioritized list with expected impact]

### Measurement Plan
[How to verify improvements]
```

## Example Output

```markdown
## React Performance Analysis

### Executive Summary
The application suffers from two main performance issues: (1) ProductList component re-renders 47 times during filter changes when it should render 3 times, causing 400ms+ jank, and (2) initial bundle is 2.1MB with 800KB of unused code. Implementing the top 3 recommendations will reduce interaction delay by ~70% and initial load by ~40%.

### Performance Profile Summary

| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| LCP (Largest Contentful Paint) | 3.2s | < 2.5s | ❌ Needs Work |
| FCP (First Contentful Paint) | 1.8s | < 1.8s | ✅ Good |
| INP (Interaction to Next Paint) | 320ms | < 200ms | ❌ Poor |
| Bundle Size (gzipped) | 2.1MB | < 500KB | ❌ Critical |
| Initial JS | 2.1MB | < 300KB | ❌ Critical |

### Bottleneck Identification

#### Bottleneck 1: ProductList Re-renders (Critical)
- **Component:** `src/features/products/ProductList.tsx`
- **Render Time:** 45ms average
- **Render Count:** 47 per filter change (expected: 3)
- **Total Impact:** 2,115ms of blocking work
- **Confidence:** High (measured via React Profiler)

**Root Cause Analysis:**
```typescript
// Parent creates new filter object every render
function ProductPage() {
  const [category, setCategory] = useState('all');
  const [sort, setSort] = useState('price');

  // ❌ New object created every render
  const filters = { category, sort };

  return (
    <ProductList filters={filters} /> // Re-renders even when values unchanged
  );
}
```

**Cascade Effect:**
- ProductList re-renders → 50 ProductCard children re-render
- Each ProductCard runs price calculation (~5ms each)
- Total: 47 × (45ms + 50 × 5ms) = ~14 seconds of cumulative render time

#### Bottleneck 2: Unvirtualized Order History (High)
- **Component:** `src/features/orders/OrderHistory.tsx`
- **Issue:** Renders 500+ order rows without virtualization
- **Render Time:** 1.2s initial, 300ms on updates
- **Confidence:** High (measured)

```typescript
// ❌ Renders all 500 items
function OrderHistory({ orders }) {
  return (
    <div>
      {orders.map(order => (
        <OrderRow key={order.id} order={order} /> // 500 DOM nodes
      ))}
    </div>
  );
}
```

#### Bottleneck 3: Context Re-render Cascade (Medium)
- **Component:** `src/contexts/CartContext.tsx`
- **Issue:** Cart state changes re-render entire app subtree
- **Affected Components:** 34 components subscribed to CartContext
- **Confidence:** Medium (pattern analysis, not fully profiled)

```typescript
// ❌ All cart data in one context = all consumers re-render
const CartContext = createContext({
  items: [],
  total: 0,
  itemCount: 0,
  addItem: () => {},
  removeItem: () => {},
  updateQuantity: () => {},
});

// Header only needs itemCount, but re-renders when items change
function Header() {
  const { itemCount } = useContext(CartContext);
  // ...
}
```

### Bundle Analysis

**Total Bundle Size:** 2.1MB (gzipped: 580KB)

| Package | Size | % of Bundle | Issue |
|---------|------|-------------|-------|
| moment.js | 320KB | 15% | Replace with date-fns (35KB) |
| lodash (full) | 180KB | 8.5% | Import specific functions |
| react-icons (all) | 150KB | 7% | Import specific icons |
| chart.js | 250KB | 12% | Lazy load, used on 1 page |
| Duplicate React | 145KB | 7% | Fix peer dependency |
| Unused code | 400KB | 19% | Tree shaking issues |

**Code Splitting Opportunities:**
- Dashboard page (450KB) - Only 10% of users visit
- Admin section (380KB) - Only admins need this
- PDF generator (200KB) - On-demand only

### Optimization Recommendations

#### Priority 1: Fix ProductList Re-renders (Impact: High, Effort: Low)

**Problem:** Filter object recreated every render
**Solution:** Memoize filter object or split into individual props

```typescript
// Option A: useMemo for filter object
function ProductPage() {
  const [category, setCategory] = useState('all');
  const [sort, setSort] = useState('price');

  // ✅ Stable reference when values unchanged
  const filters = useMemo(
    () => ({ category, sort }),
    [category, sort]
  );

  return <ProductList filters={filters} />;
}

// Option B: Individual props (preferred)
function ProductPage() {
  const [category, setCategory] = useState('all');
  const [sort, setSort] = useState('price');

  return (
    <ProductList
      category={category}
      sort={sort}
    />
  );
}
```

**Plus: Memoize ProductList and ProductCard**
```typescript
const ProductList = React.memo(function ProductList({ category, sort }) {
  // Memoize expensive filtering/sorting
  const filteredProducts = useMemo(
    () => products.filter(...).sort(...),
    [products, category, sort]
  );

  return filteredProducts.map(p => (
    <ProductCard key={p.id} product={p} />
  ));
});

const ProductCard = React.memo(function ProductCard({ product }) {
  // Only re-renders when product changes
  return <div>{product.name}</div>;
});
```

**Expected Impact:**
- Re-renders: 47 → 3 (93% reduction)
- Interaction time: 320ms → 95ms
- INP improvement: Critical → Good

#### Priority 2: Virtualize Order History (Impact: High, Effort: Medium)

**Solution:** Use @tanstack/react-virtual or react-window

```typescript
import { useVirtualizer } from '@tanstack/react-virtual';

function OrderHistory({ orders }) {
  const parentRef = useRef(null);

  const virtualizer = useVirtualizer({
    count: orders.length,
    getScrollElement: () => parentRef.current,
    estimateSize: () => 60, // Row height
  });

  return (
    <div ref={parentRef} style={{ height: '600px', overflow: 'auto' }}>
      <div style={{ height: virtualizer.getTotalSize() }}>
        {virtualizer.getVirtualItems().map((virtualItem) => (
          <OrderRow
            key={orders[virtualItem.index].id}
            order={orders[virtualItem.index]}
            style={{
              position: 'absolute',
              top: virtualItem.start,
              height: virtualItem.size,
            }}
          />
        ))}
      </div>
    </div>
  );
}
```

**Expected Impact:**
- DOM nodes: 500 → ~15 visible
- Initial render: 1.2s → 50ms
- Memory usage: ~40% reduction

#### Priority 3: Bundle Size Reduction (Impact: High, Effort: Medium)

**3a: Replace moment.js with date-fns**
```typescript
// Before
import moment from 'moment';
const formatted = moment(date).format('MMM D, YYYY');

// After
import { format } from 'date-fns';
const formatted = format(date, 'MMM d, yyyy');
```
**Savings:** 285KB (320KB → 35KB for date functions used)

**3b: Import lodash functions individually**
```typescript
// Before
import _ from 'lodash';
_.debounce(fn, 300);

// After
import debounce from 'lodash/debounce';
debounce(fn, 300);
```
**Savings:** ~160KB

**3c: Lazy load heavy pages**
```typescript
// Before
import Dashboard from './pages/Dashboard';
import Admin from './pages/Admin';

// After
const Dashboard = React.lazy(() => import('./pages/Dashboard'));
const Admin = React.lazy(() => import('./pages/Admin'));

function App() {
  return (
    <Suspense fallback={<PageSkeleton />}>
      <Routes>
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/admin" element={<Admin />} />
      </Routes>
    </Suspense>
  );
}
```
**Savings:** 830KB from initial bundle

**Expected Impact:**
- Initial bundle: 2.1MB → 850KB (60% reduction)
- LCP: 3.2s → 1.8s
- TTI (Time to Interactive): 4.5s → 2.5s

#### Priority 4: Split Cart Context (Impact: Medium, Effort: Low)

**Solution:** Create selector hooks or split context

```typescript
// Option A: Selector pattern with useSyncExternalStore
const useCartItemCount = () => {
  return useSyncExternalStore(
    cartStore.subscribe,
    () => cartStore.getState().items.length
  );
};

// Option B: Split into multiple contexts
const CartItemsContext = createContext<CartItem[]>([]);
const CartActionsContext = createContext<CartActions>({} as CartActions);

// Components subscribe only to what they need
function Header() {
  const items = useContext(CartItemsContext);
  return <span>Cart ({items.length})</span>;
}

function CartActions() {
  const actions = useContext(CartActionsContext);
  // Won't re-render when items change
  return <button onClick={actions.checkout}>Checkout</button>;
}
```

**Expected Impact:**
- Affected re-renders: 34 components → only components that need the data
- ~20% reduction in total render work for cart operations

### Additional Quick Wins

| Optimization | Impact | Effort | Priority |
|--------------|--------|--------|----------|
| Add loading="lazy" to images | Medium | 5 min | Do now |
| Preconnect to API domain | Low | 5 min | Do now |
| Enable gzip/brotli compression | High | 30 min | Do now |
| Move to dynamic imports for icons | Medium | 2h | Next sprint |
| Implement skeleton loading | Medium | 4h | Next sprint |

### Measurement Plan

**Before/After Metrics to Track:**

| Metric | Tool | Frequency |
|--------|------|-----------|
| LCP, FCP, CLS, INP | Lighthouse CI | Every PR |
| Bundle size | bundlesize package | Every PR |
| Re-render counts | React DevTools | Manual for perf PRs |
| Real User Metrics | Web Vitals library | Production monitoring |

**Profiling Script:**
```typescript
// Add to development for ongoing monitoring
import { Profiler } from 'react';

function onRender(
  id: string,
  phase: 'mount' | 'update',
  actualDuration: number
) {
  if (actualDuration > 16) {
    console.warn(`Slow render: ${id} took ${actualDuration.toFixed(2)}ms`);
  }
}

// Wrap suspicious components
<Profiler id="ProductList" onRender={onRender}>
  <ProductList {...props} />
</Profiler>
```

### Summary of Expected Improvements

| Area | Current | After Optimizations | Improvement |
|------|---------|---------------------|-------------|
| Initial Bundle | 2.1MB | 850KB | 60% smaller |
| LCP | 3.2s | 1.8s | 44% faster |
| INP | 320ms | 95ms | 70% faster |
| ProductList Renders | 47/interaction | 3/interaction | 93% fewer |
| Order History Render | 1.2s | 50ms | 96% faster |
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Focused performance analysis goal
- **ST-02 (Structured Sequential Instructions):** Systematic profiling approach
- **RT-02 (Multi-Dimensional Analysis):** Covers renders, bundle, patterns
- **RT-05 (Evidence-Based Reasoning):** All recommendations backed by measurements
- **DS-06 (Prioritization Guidance):** Priority ranking by impact/effort

## Related Prompts

- [frontend_performance_core_web_vitals.md](../performance/frontend_performance_core_web_vitals.md) - Core Web Vitals focus
- [frontend_performance_bundle_optimization.md](../performance/frontend_performance_bundle_optimization.md) - Bundle deep dive
- [frontend_react_hooks_best_practices.md](frontend_react_hooks_best_practices.md) - Hook optimization

## Customization Guide

- **For Next.js**: Add SSR/ISR performance considerations, image optimization with next/image
- **For React Native**: Focus on list performance (FlatList), bridge overhead
- **For Large Apps**: Add module federation, micro-frontend considerations
- **For E-commerce**: Emphasize product list, cart, checkout performance
