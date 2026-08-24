---
title: "JavaScript Bundle Optimization"
category: frontend-development/performance
description: "Analyze and optimize JavaScript bundle size through code splitting, tree shaking, and dependency management for faster load times"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: advanced
tags:
  - performance
  - bundle-size
  - webpack
  - vite
  - code-splitting
  - tree-shaking
updated: "2026-01-29"
related_prompts:
  - domain-frontend-development/performance/frontend_performance_core_web_vitals.md
  - domain-frontend-development/react/frontend_react_performance.md
  - domain-frontend-development/build-tooling/frontend_build_vite_optimization.md
  - domain-frontend-development/build-tooling/frontend_build_bundler_migration.md
---

# JavaScript Bundle Optimization

**Objective:** Analyze a web application's JavaScript bundle composition, identify bloat sources, and implement optimization strategies to reduce initial load time and improve performance.

**When to Use:**
- Use when: Initial bundle exceeds 200KB gzipped
- Use when: Time to Interactive (TTI) is slow
- Use when: Lighthouse performance score is low due to JavaScript
- Use when: Adding new features and concerned about bundle growth
- Don't use when: Bundle is already optimized and small

## Instructions

1. **Analyze Current Bundle**
   - Generate bundle analysis visualization
   - Identify total size (raw and gzipped)
   - Break down by entry point and chunk
   - Identify largest dependencies

2. **Identify Optimization Opportunities**
   - Duplicate dependencies
   - Unused exports (tree shaking failures)
   - Large dependencies with lighter alternatives
   - Code that should be lazy loaded
   - Polyfills not needed for target browsers

3. **Design Code Splitting Strategy**
   - Route-based splitting for SPAs
   - Component-based splitting for large components
   - Vendor chunk optimization
   - Dynamic imports for conditional features

4. **Implement Tree Shaking**
   - Verify ESM imports
   - Check sideEffects configuration
   - Optimize barrel file exports
   - Remove dead code

5. **CRITICAL: Measure Impact**
   - Compare before/after bundle sizes
   - Verify runtime behavior unchanged
   - Check for code splitting regressions
   - **Confidence level** for each optimization:
     - **High Confidence**: Measured savings, tested in production
     - **Medium Confidence**: Lab measurements only
     - **Low Confidence**: Theoretical savings

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Remove dependencies without verifying they're unused
- Assume tree shaking works without checking bundle
- Split code so aggressively it causes waterfall loading
- Optimize micro-bundles (< 5KB) before major ones
- Break functionality for bundle savings
- Ignore runtime performance for bundle size

✅ **DO:**
- Analyze actual bundle content, not just package.json
- Verify tree shaking with bundle analyzer
- Test lazy-loaded routes work correctly
- Consider loading patterns (prefetch, preload)
- Balance chunk count vs chunk size
- Measure real-world loading performance

## Expected Output

A comprehensive bundle analysis including:
- Bundle composition breakdown
- Specific optimization opportunities
- Code splitting recommendations
- Migration effort estimates
- Expected size reductions

### Output Format

```markdown
## Bundle Optimization Analysis

### Current State
[Bundle composition and sizes]

### Optimization Opportunities
[Specific findings with savings estimates]

### Code Splitting Strategy
[Recommended splitting approach]

### Implementation Plan
[Prioritized actions]
```

## Example Output

```markdown
## Bundle Optimization Analysis

### Executive Summary

**Analysis Date:** 2026-01-29
**Build Tool:** Vite 5.0 / Rollup
**Framework:** React 18

| Metric | Current | Target | Potential Savings |
|--------|---------|--------|-------------------|
| Total Bundle | 1.8MB | 500KB | 72% reduction |
| Initial JS | 850KB | 200KB | 76% reduction |
| Gzipped Initial | 285KB | 65KB | 77% reduction |
| Chunks | 3 | 15-20 | Code split |

**Key Finding:** 60% of initial bundle is unused on first load. Moment.js alone accounts for 18% of bundle.

---

### Current Bundle Composition

```
┌─────────────────────────────────────────────────────────────┐
│                  Bundle Analysis (1.8MB)                     │
├─────────────────────────────────────────────────────────────┤
│ ████████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░ React     │
│ ██████████████████████████████░░░░░░░░░░░░░░░░░░░ moment.js  │
│ ████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ lodash     │
│ ██████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ chart.js   │
│ ████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ @mui       │
│ ██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ react-dom  │
│ █████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ App code   │
│ ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ Other deps │
└─────────────────────────────────────────────────────────────┘
```

| Package | Size | % of Bundle | Usage |
|---------|------|-------------|-------|
| moment.js | 320KB | 18% | Date formatting (3 places) |
| lodash | 180KB | 10% | 5 functions used |
| chart.js | 250KB | 14% | Dashboard only |
| @mui/material | 280KB | 15% | Full library imported |
| react + react-dom | 145KB | 8% | Required |
| App code | 120KB | 7% | Core application |
| Other deps | 505KB | 28% | Various utilities |

---

### Optimization Opportunities

#### Opportunity 1: Replace moment.js with date-fns
- **Current Size:** 320KB (uncompressed)
- **Replacement Size:** 35KB (with 5 functions)
- **Savings:** 285KB (89% reduction)
- **Confidence:** High
- **Effort:** Medium (8h)

**Current Usage (3 files):**
```javascript
import moment from 'moment';

// Usage 1: OrderList.tsx
moment(date).format('MMM D, YYYY');

// Usage 2: DatePicker.tsx
moment(date).isBefore(moment());

// Usage 3: Analytics.tsx
moment(date).startOf('month');
```

**Recommended Migration:**
```javascript
import { format, isBefore, startOfMonth } from 'date-fns';

// Usage 1
format(date, 'MMM d, yyyy');

// Usage 2
isBefore(date, new Date());

// Usage 3
startOfMonth(date);
```

**Migration Script:**
```bash
# Install date-fns
npm install date-fns
npm uninstall moment

# Update imports (manual review needed)
npx jscodeshift -t date-fns-codemod/src/transforms/moment.js src/
```

---

#### Opportunity 2: Cherry-Pick lodash Imports
- **Current Size:** 180KB
- **After Optimization:** 15KB
- **Savings:** 165KB (92% reduction)
- **Confidence:** High
- **Effort:** Low (2h)

**Current Usage (found via grep):**
```javascript
import _ from 'lodash';

_.debounce(fn, 300);
_.throttle(fn, 100);
_.cloneDeep(obj);
_.get(obj, 'path.to.value');
_.isEqual(a, b);
```

**Recommended Fix:**
```javascript
// Option A: Individual imports
import debounce from 'lodash/debounce';
import throttle from 'lodash/throttle';
import cloneDeep from 'lodash/cloneDeep';
import get from 'lodash/get';
import isEqual from 'lodash/isEqual';

// Option B: Replace with native or lighter alternatives
// debounce/throttle: Use custom hooks or use-debounce (1KB)
// cloneDeep: structuredClone() (native)
// get: Optional chaining (native)
// isEqual: fast-deep-equal (2KB)
```

**Native Replacements:**
```javascript
// Instead of _.get(obj, 'a.b.c')
obj?.a?.b?.c

// Instead of _.cloneDeep(obj)
structuredClone(obj)

// For debounce, use a simple hook
function useDebounce(value, delay) {
  const [debouncedValue, setDebouncedValue] = useState(value);
  useEffect(() => {
    const handler = setTimeout(() => setDebouncedValue(value), delay);
    return () => clearTimeout(handler);
  }, [value, delay]);
  return debouncedValue;
}
```

---

#### Opportunity 3: Lazy Load Chart.js
- **Current Size:** 250KB (in initial bundle)
- **After Lazy Loading:** 0KB (initial), 250KB (on-demand)
- **Initial Bundle Savings:** 250KB
- **Confidence:** High
- **Effort:** Low (2h)

**Current (always loaded):**
```javascript
// App.tsx
import Dashboard from './pages/Dashboard'; // Contains Chart.js

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/dashboard" element={<Dashboard />} />
    </Routes>
  );
}
```

**Recommended (lazy loaded):**
```javascript
import { lazy, Suspense } from 'react';

const Dashboard = lazy(() => import('./pages/Dashboard'));

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route
        path="/dashboard"
        element={
          <Suspense fallback={<DashboardSkeleton />}>
            <Dashboard />
          </Suspense>
        }
      />
    </Routes>
  );
}
```

**With Prefetching:**
```javascript
// Prefetch on hover
<Link
  to="/dashboard"
  onMouseEnter={() => import('./pages/Dashboard')}
>
  Dashboard
</Link>
```

---

#### Opportunity 4: Optimize MUI Imports
- **Current Size:** 280KB
- **After Optimization:** 180KB
- **Savings:** 100KB (36% reduction)
- **Confidence:** Medium
- **Effort:** Medium (4h)

**Current (importing full library):**
```javascript
import { Button, TextField, Dialog, ... } from '@mui/material';
```

**Recommended (path imports + tree shaking):**
```javascript
// vite.config.js / next.config.js
import { defineConfig } from 'vite';

export default defineConfig({
  resolve: {
    alias: {
      '@mui/material': '@mui/material/esm',
    },
  },
  optimizeDeps: {
    include: ['@mui/material'],
  },
});
```

**Or use modular imports:**
```javascript
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
```

---

#### Opportunity 5: Remove Duplicate React Versions
- **Issue:** 2 versions of React in bundle (17.0.2 and 18.2.0)
- **Cause:** Dependency requires React 17
- **Savings:** 45KB
- **Confidence:** High
- **Effort:** Low (1h)

**Diagnosis:**
```bash
npm ls react
# Shows two versions installed
```

**Fix:**
```json
// package.json
{
  "overrides": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  }
}
```

```bash
rm -rf node_modules package-lock.json
npm install
```

---

### Code Splitting Strategy

#### Current State: 3 Chunks
```
main.js ─────────────────────────────── 850KB
vendor.js ────────────────────────────── 890KB
styles.css ───────────────────────────── 60KB
```

#### Recommended: Route-Based Splitting

```
┌─────────────────────────────────────────────────────────────┐
│                    Chunk Strategy                            │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────┐                                           │
│  │ Critical Path │ ◄── Initial load (< 200KB gzipped)       │
│  │  - React      │                                          │
│  │  - Router     │                                          │
│  │  - App shell  │                                          │
│  │  - Home page  │                                          │
│  └──────────────┘                                           │
│         │                                                    │
│         ▼                                                    │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐        │
│  │  Dashboard   │ │   Checkout   │ │   Account    │        │
│  │  - Chart.js  │ │  - Stripe    │ │  - Settings  │        │
│  │  - Analytics │ │  - Forms     │ │  - Profile   │        │
│  │  ~180KB      │ │  ~120KB      │ │  ~80KB       │        │
│  └──────────────┘ └──────────────┘ └──────────────┘        │
│                                                              │
│  ┌──────────────┐                                           │
│  │   Vendor     │ ◄── Shared dependencies (cached)          │
│  │  - date-fns  │                                          │
│  │  - MUI core  │                                          │
│  │  ~150KB      │                                          │
│  └──────────────┘                                           │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

#### Vite Configuration

```javascript
// vite.config.js
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { visualizer } from 'rollup-plugin-visualizer';

export default defineConfig({
  plugins: [
    react(),
    visualizer({ filename: 'bundle-analysis.html' }),
  ],
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          // Vendor chunks
          'vendor-react': ['react', 'react-dom', 'react-router-dom'],
          'vendor-ui': ['@mui/material', '@emotion/react', '@emotion/styled'],

          // Feature chunks (will also be lazy loaded)
          'feature-charts': ['chart.js', 'react-chartjs-2'],
          'feature-forms': ['react-hook-form', 'yup'],
        },
      },
    },
    chunkSizeWarningLimit: 500,
  },
});
```

#### Route Configuration

```javascript
// routes.tsx
import { lazy, Suspense } from 'react';
import { Routes, Route } from 'react-router-dom';
import { PageLoader } from './components/PageLoader';

// Eager load - critical path
import Home from './pages/Home';
import ProductList from './pages/ProductList';

// Lazy load - secondary paths
const Dashboard = lazy(() =>
  import(/* webpackChunkName: "dashboard" */ './pages/Dashboard')
);
const Checkout = lazy(() =>
  import(/* webpackChunkName: "checkout" */ './pages/Checkout')
);
const Account = lazy(() =>
  import(/* webpackChunkName: "account" */ './pages/Account')
);
const Admin = lazy(() =>
  import(/* webpackChunkName: "admin" */ './pages/Admin')
);

function AppRoutes() {
  return (
    <Suspense fallback={<PageLoader />}>
      <Routes>
        {/* Critical path - no lazy loading */}
        <Route path="/" element={<Home />} />
        <Route path="/products" element={<ProductList />} />

        {/* Secondary paths - lazy loaded */}
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/checkout" element={<Checkout />} />
        <Route path="/account/*" element={<Account />} />
        <Route path="/admin/*" element={<Admin />} />
      </Routes>
    </Suspense>
  );
}
```

---

### Implementation Plan

#### Phase 1: Quick Wins (Week 1)
| Action | Savings | Effort | Priority |
|--------|---------|--------|----------|
| Replace moment.js | 285KB | 8h | 1 |
| Cherry-pick lodash | 165KB | 2h | 2 |
| Fix duplicate React | 45KB | 1h | 3 |
| Lazy load Dashboard | 250KB (deferred) | 2h | 4 |

**Total Phase 1 Savings:** 495KB (initial), 250KB deferred

#### Phase 2: Code Splitting (Week 2)
| Action | Savings | Effort | Priority |
|--------|---------|--------|----------|
| Implement route splitting | 300KB (deferred) | 8h | 1 |
| Configure vendor chunks | Better caching | 4h | 2 |
| Add prefetch for routes | UX improvement | 4h | 3 |

#### Phase 3: Deep Optimization (Week 3)
| Action | Savings | Effort | Priority |
|--------|---------|--------|----------|
| Optimize MUI imports | 100KB | 4h | 1 |
| Audit remaining deps | ~50KB | 4h | 2 |
| Add bundle size CI check | Prevention | 2h | 3 |

---

### Monitoring & Prevention

#### Bundle Size CI Check

```yaml
# .github/workflows/bundle-size.yml
name: Bundle Size

on: pull_request

jobs:
  size:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - run: npm ci
      - run: npm run build

      - uses: preactjs/compressed-size-action@v2
        with:
          build-script: 'build'
          pattern: './dist/**/*.{js,css}'
          compression: 'gzip'
```

#### bundlesize Configuration

```json
// package.json
{
  "bundlesize": [
    {
      "path": "./dist/assets/index-*.js",
      "maxSize": "80 kB",
      "compression": "gzip"
    },
    {
      "path": "./dist/assets/vendor-*.js",
      "maxSize": "150 kB",
      "compression": "gzip"
    }
  ]
}
```

---

### Expected Final State

| Chunk | Before | After | Savings |
|-------|--------|-------|---------|
| Initial JS | 850KB | 180KB | 79% |
| Vendor | 890KB | 320KB | 64% |
| Dashboard (lazy) | - | 180KB | n/a |
| Checkout (lazy) | - | 120KB | n/a |
| Account (lazy) | - | 80KB | n/a |
| **Total** | **1.74MB** | **880KB** | **49%** |
| **Initial (gzipped)** | **285KB** | **60KB** | **79%** |

**Performance Impact:**
- TTI improvement: ~2.5s → ~0.8s (on 3G)
- LCP improvement: ~3.2s → ~1.8s
- Lighthouse Performance: 45 → 85
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Focused on bundle optimization
- **ST-02 (Structured Sequential Instructions):** Step-by-step analysis
- **RT-02 (Multi-Dimensional Analysis):** Multiple optimization types
- **RT-05 (Evidence-Based Reasoning):** Size measurements for each
- **DS-06 (Prioritization Guidance):** Phased implementation

## Related Prompts

- [frontend_performance_core_web_vitals.md](frontend_performance_core_web_vitals.md) - CWV optimization
- [frontend_react_performance.md](../react/frontend_react_performance.md) - React-specific
- [frontend_build_vite_optimization.md](../build-tooling/frontend_build_vite_optimization.md) - Build tool config & optimization
- [frontend_build_bundler_migration.md](../build-tooling/frontend_build_bundler_migration.md) - Migrating bundlers

## Customization Guide

- **For Webpack**: Adjust config examples to webpack syntax
- **For Next.js**: Include next/dynamic and next-bundle-analyzer
- **For Nuxt**: Include Nuxt-specific chunking strategies
- **For Micro-Frontends**: Consider module federation chunking
