---
title: "Next.js Performance Optimization Analysis"
category: frontend-development/nextjs
description: "Analyze Next.js applications for performance issues including bundle size, rendering strategy selection, image optimization, and Core Web Vitals improvements"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: advanced
tags:
  - nextjs
  - performance
  - core-web-vitals
  - bundle-size
  - ssr
  - ssg
  - isr
  - image-optimization
updated: "2026-03-19"
related_prompts:
  - domain-frontend-development/nextjs/frontend_nextjs_app_router.md
  - domain-frontend-development/nextjs/frontend_nextjs_data_fetching.md
  - domain-frontend-development/performance/frontend_performance_core_web_vitals.md
  - domain-frontend-development/performance/frontend_performance_bundle_optimization.md
---

# Next.js Performance Optimization Analysis

**Objective:** Analyze a Next.js application for performance bottlenecks specific to the framework, including rendering strategy selection, bundle composition, image and font optimization, and Core Web Vitals, providing Next.js-specific optimization strategies with measurable expected impact.

**When to Use:**
- Use when: Core Web Vitals are below targets (LCP > 2.5s, INP > 200ms, CLS > 0.1)
- Use when: Bundle size is growing beyond acceptable limits
- Use when: Page load feels slow despite server rendering
- Use when: Evaluating rendering strategy (SSR vs SSG vs ISR vs CSR) per route
- Don't use when: Performance issues are at the API/database level (not a Next.js concern)

## Instructions

1. **Measure Current Performance**
   - Core Web Vitals: LCP, INP, CLS from field data or Lighthouse
   - Bundle analysis: `@next/bundle-analyzer` output
   - Server response times: TTFB across routes
   - Client hydration time
   - Route-level performance breakdown

2. **Analyze Rendering Strategy Per Route**
   - Is each route using the optimal rendering strategy?
     - **Static (SSG)**: Content doesn't change between deployments
     - **ISR**: Content changes but can be slightly stale
     - **SSR**: Content must be fresh on every request
     - **CSR**: Content depends entirely on client state
   - Check for routes that are dynamically rendered but could be static
   - Evaluate `export const dynamic` and `export const revalidate` usage

3. **Audit Bundle Composition**
   - Client bundle size breakdown by route
   - Shared chunks and third-party library impact
   - `'use client'` components and their dependency trees
   - Dynamic imports (`next/dynamic`) usage
   - Tree-shaking effectiveness

4. **Review Next.js-Specific Optimizations**
   - **Images**: `next/image` usage, sizing, formats, priority
   - **Fonts**: `next/font` for zero-layout-shift font loading
   - **Scripts**: `next/script` with appropriate loading strategies
   - **Links**: `<Link>` prefetching behavior
   - **Middleware**: Performance impact of edge middleware

5. **CRITICAL: Validate Before Optimizing**
   - Measure in production builds, not dev mode (dev is always slower)
   - Use field data (RUM) when available, not just lab data (Lighthouse)
   - Profile on representative devices, not high-end machines
   - Verify that optimizations don't degrade UX or functionality
   - **Confidence level** for each finding:
     - **High Confidence**: Measured bottleneck with clear evidence
     - **Medium Confidence**: Pattern likely impactful based on bundle analysis
     - **Low Confidence**: Theoretical improvement, needs measurement

## False-Positive Prevention (MUST follow)

**DON'T:**
- Optimize rendering strategy without understanding data freshness needs
- Report SSR as "slow" without checking if the slowness is from the API/DB
- Flag missing `next/image` for images that genuinely need different handling
- Suggest converting dynamic routes to static without understanding content patterns
- Report large bundle without analyzing if the code is actually loaded
- Criticize middleware without measuring its latency impact
- Assume all third-party scripts should be deferred

**DO:**
- Compare lab data with field data before making recommendations
- Consider the deployment platform capabilities (Vercel, AWS, self-hosted)
- Profile hydration cost separately from initial render
- Check if "large" bundles are code-split and only loaded when needed
- Verify image optimization suggestions work with the content type
- Measure TTFB to distinguish server rendering time from network issues
- Test on mobile devices and slow connections

## Expected Output

A comprehensive performance analysis including:
- Current performance metrics
- Rendering strategy evaluation per route
- Bundle analysis with optimization opportunities
- Next.js feature adoption assessment
- Prioritized optimizations with expected impact

### Output Format

```markdown
## Next.js Performance Analysis

### Current Metrics
[Key performance indicators]

### Rendering Strategy Evaluation
[Per-route rendering assessment]

### Bundle Analysis
[Size breakdown, optimization opportunities]

### Next.js Feature Optimization
[Image, font, script, link optimizations]

### Recommendations
[Prioritized with expected impact]
```

## Example Output

```markdown
## Next.js Performance Analysis

### Executive Summary
The application serves 42 routes with an average LCP of 3.8s and a total client bundle of 1.4MB. Three main issues drive poor performance: (1) 8 routes use SSR that could be ISR/static, adding 200-500ms TTFB per request, (2) `next/image` is not used for product images (14 routes), causing 800ms+ LCP regression, and (3) three large client-side libraries (chart.js, date-fns full, lodash) contribute 450KB unnecessarily. Fixing these should bring LCP under 2.5s and reduce server load by ~60%.

### Current Metrics

| Metric | Current (p75) | Target | Status |
|--------|---------------|--------|--------|
| LCP | 3.8s | < 2.5s | Poor |
| INP | 180ms | < 200ms | Needs Improvement |
| CLS | 0.15 | < 0.1 | Needs Improvement |
| TTFB | 800ms | < 500ms | Poor |
| FCP | 1.9s | < 1.8s | Needs Improvement |
| Total Client JS | 1.4MB | < 500KB | Poor |
| Total Transfer (gzipped) | 420KB | < 200KB | Poor |

### Rendering Strategy Evaluation

| Route | Current | Recommended | TTFB Savings | Rationale |
|-------|---------|-------------|-------------|-----------|
| `/` | SSR | SSG | 400ms | Content changes rarely |
| `/about` | SSR | SSG | 350ms | Static content |
| `/pricing` | SSR | ISR (3600s) | 300ms | Changes weekly |
| `/blog` | ISR (60s) | ISR (3600s) | N/A | Blog updates aren't urgent |
| `/blog/[slug]` | ISR (60s) | ISR + on-demand | N/A | Good, add webhook revalidation |
| `/dashboard` | SSR | SSR | N/A | Correct - user-specific |
| `/projects` | SSR | SSR | N/A | Correct - user-specific |
| `/products` | SSR | ISR (300s) | 250ms | Catalog rarely changes |
| `/products/[id]` | SSR | ISR (600s) | 200ms | Product details rarely change |

**Impact:** Moving 5 routes to static/ISR eliminates ~3,000 SSR requests/hour at current traffic.

#### Finding 1: Static Pages Rendered Dynamically
- **Severity:** High
- **Confidence:** High
- **Location:** `app/page.tsx`, `app/about/page.tsx`, `app/pricing/page.tsx`
- **Evidence:**
  ```typescript
  // app/page.tsx - fetches CMS data on every request
  export default async function HomePage() {
    const content = await fetch(`${CMS_URL}/homepage`, {
      cache: 'no-store',  // Forces SSR on every request
    });
    return <LandingPage content={await content.json()} />;
  }
  ```
- **Fix:**
  ```typescript
  // Cache with ISR - regenerate every hour
  export default async function HomePage() {
    const content = await fetch(`${CMS_URL}/homepage`, {
      next: { revalidate: 3600, tags: ['homepage'] },
    });
    return <LandingPage content={await content.json()} />;
  }

  // Or force static generation
  export const dynamic = 'force-static';
  export const revalidate = 3600;
  ```
- **Expected Impact:** TTFB from 800ms → 50ms for these routes (cache hit)

### Bundle Analysis

**Bundle Breakdown (client JS):**

| Chunk | Size | Gzipped | Routes | Assessment |
|-------|------|---------|--------|------------|
| Framework (React, Next.js) | 180KB | 58KB | All | Baseline |
| `chart.js` | 250KB | 80KB | Dashboard only | Lazy load |
| `lodash` (full) | 120KB | 35KB | 3 routes | Use individual imports |
| `date-fns` (full) | 80KB | 25KB | All | Tree-shake |
| App components | 450KB | 130KB | Various | Audit `'use client'` |
| Shared chunks | 320KB | 92KB | Various | Review splitting |

#### Finding 2: Large Libraries in Main Bundle
- **Severity:** High
- **Confidence:** High
- **Evidence:** `chart.js` (250KB) loaded in the main bundle despite only being used on `/dashboard/analytics`
  ```typescript
  // components/AnalyticsChart.tsx
  'use client';
  import { Chart } from 'chart.js/auto';  // Imports everything
  ```
- **Fix:**
  ```typescript
  // Dynamic import - only loads when component renders
  import dynamic from 'next/dynamic';

  const AnalyticsChart = dynamic(
    () => import('@/components/AnalyticsChart'),
    {
      loading: () => <ChartSkeleton />,
      ssr: false,  // Chart.js needs browser APIs
    }
  );

  // In AnalyticsChart.tsx - register only needed chart types
  import { Chart, LineController, LineElement, PointElement, LinearScale, CategoryScale } from 'chart.js';
  Chart.register(LineController, LineElement, PointElement, LinearScale, CategoryScale);
  ```
- **Expected Impact:** 250KB removed from main bundle

#### Finding 3: Full Lodash Import
- **Severity:** Medium
- **Confidence:** High
- **Evidence:**
  ```typescript
  import _ from 'lodash';           // 120KB entire library
  const sorted = _.sortBy(items, 'name');
  const grouped = _.groupBy(items, 'category');
  ```
- **Fix:**
  ```typescript
  // Individual imports - tree-shakeable
  import sortBy from 'lodash/sortBy';    // ~2KB
  import groupBy from 'lodash/groupBy';  // ~2KB
  ```
- **Expected Impact:** 116KB saved

### Next.js Feature Optimization

#### Finding 4: Product Images Not Using next/image
- **Severity:** High
- **Confidence:** High
- **Found:** 14 routes using `<img>` for product images
- **Evidence:**
  ```tsx
  // Product images - raw <img> tags
  <img
    src={product.imageUrl}
    alt={product.name}
    width="400"
    height="300"
  />
  ```
- **Impact:** No automatic WebP/AVIF conversion, no responsive sizing, no lazy loading, causes CLS
- **Fix:**
  ```tsx
  import Image from 'next/image';

  <Image
    src={product.imageUrl}
    alt={product.name}
    width={400}
    height={300}
    sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
    placeholder="blur"
    blurDataURL={product.blurHash}
  />

  // For hero/LCP images, add priority
  <Image
    src={product.imageUrl}
    alt={product.name}
    width={800}
    height={600}
    priority  // Preload for LCP
    sizes="100vw"
  />
  ```
- **Expected Impact:** 40-60% smaller image payloads, CLS reduction, LCP improvement

#### Finding 5: Fonts Causing Layout Shift
- **Severity:** Medium
- **Confidence:** High
- **Evidence:**
  ```html
  <!-- Google Fonts loaded via <link> - causes FOUT and CLS -->
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap" rel="stylesheet">
  ```
- **Fix:**
  ```typescript
  // app/layout.tsx - use next/font for zero-CLS font loading
  import { Inter } from 'next/font/google';

  const inter = Inter({
    subsets: ['latin'],
    display: 'swap',
    variable: '--font-inter',
  });

  export default function RootLayout({ children }) {
    return (
      <html lang="en" className={inter.variable}>
        <body>{children}</body>
      </html>
    );
  }
  ```
- **Expected Impact:** CLS improvement from 0.15 → < 0.05 for font-related shifts

#### Finding 6: Third-Party Scripts Blocking Render
- **Severity:** Medium
- **Confidence:** Medium
- **Evidence:**
  ```html
  <!-- Analytics and chat widget loaded synchronously -->
  <script src="https://analytics.example.com/tracker.js"></script>
  <script src="https://chat.example.com/widget.js"></script>
  ```
- **Fix:**
  ```typescript
  import Script from 'next/script';

  // Analytics: load after page is interactive
  <Script
    src="https://analytics.example.com/tracker.js"
    strategy="afterInteractive"
  />

  // Chat widget: load when browser is idle
  <Script
    src="https://chat.example.com/widget.js"
    strategy="lazyOnload"
  />
  ```

### Expected Impact Summary

| Optimization | LCP Impact | Bundle Impact | Effort |
|-------------|-----------|---------------|--------|
| Static/ISR for 5 routes | -500ms TTFB | None | 2 hours |
| `next/image` for products | -400ms | None | 4 hours |
| Dynamic import chart.js | -100ms | -250KB | 1 hour |
| Individual lodash imports | Minimal | -116KB | 1 hour |
| `next/font` for Inter | CLS fix | None | 30 min |
| Script loading strategies | -200ms FCP | None | 30 min |

**Combined estimated improvement:**
- LCP: 3.8s → ~2.1s
- CLS: 0.15 → ~0.05
- Client JS: 1.4MB → ~850KB
- TTFB (static pages): 800ms → ~50ms

### Prioritized Recommendations

#### Quick Wins (< 1 day each)
| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 1 | Switch 5 routes to ISR/static | Major TTFB improvement | 2 hours |
| 2 | Add `next/image` to product pages | LCP + CLS improvement | 4 hours |
| 3 | Switch to `next/font` | CLS elimination | 30 min |
| 4 | Dynamic import chart.js | 250KB less JS | 1 hour |
| 5 | Use lodash individual imports | 116KB less JS | 1 hour |
| 6 | Optimize script loading | Faster FCP | 30 min |

#### Medium Effort
| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 1 | Audit and reduce `'use client'` boundaries | Less client JS | 1-2 days |
| 2 | Add `@next/bundle-analyzer` to CI | Prevent regression | 2 hours |
| 3 | Implement `priority` on LCP images | Faster LCP | 2 hours |

#### Major Improvements
| # | Action | Impact | Effort | Dependencies |
|---|--------|--------|--------|--------------|
| 1 | Implement Suspense streaming for dashboard | Progressive loading | 1 week | RSC migration |
| 2 | Add edge middleware for geo-routing | Lower latency | 3 days | Edge runtime compat |
| 3 | Implement partial prerendering (PPR) | Best of static + dynamic | 1 week | Next.js 15+ |

### Monitoring Setup

```typescript
// app/layout.tsx - report Core Web Vitals
import { SpeedInsights } from '@vercel/speed-insights/next';

export default function RootLayout({ children }) {
  return (
    <html>
      <body>
        {children}
        <SpeedInsights />
      </body>
    </html>
  );
}

// Or custom reporting
export function reportWebVitals(metric) {
  if (metric.label === 'web-vital') {
    analytics.track('Web Vital', {
      name: metric.name,
      value: Math.round(metric.value),
      rating: metric.rating,
    });
  }
}
```
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Focused on Next.js-specific performance
- **ST-02 (Structured Sequential Instructions):** Systematic performance profiling
- **RT-02 (Multi-Dimensional Analysis):** Covers rendering, bundle, images, fonts, scripts
- **RT-05 (Evidence-Based Reasoning):** Measurements and code evidence for each issue
- **DS-06 (Prioritization Guidance):** Impact/effort ranking with expected improvements

## Related Prompts

- [frontend_nextjs_app_router.md](frontend_nextjs_app_router.md) - Architecture analysis
- [frontend_nextjs_data_fetching.md](frontend_nextjs_data_fetching.md) - Data fetching patterns
- [../performance/frontend_performance_core_web_vitals.md](../performance/frontend_performance_core_web_vitals.md) - General CWV optimization
- [../performance/frontend_performance_bundle_optimization.md](../performance/frontend_performance_bundle_optimization.md) - Bundle analysis

## Customization Guide

- **For Vercel**: Leverage Speed Insights, Analytics, ISR, and Edge Functions natively
- **For AWS/Self-Hosted**: Focus on CDN configuration, `output: 'standalone'`, custom caching headers
- **For E-commerce**: Prioritize product image optimization, ISR for catalog, edge personalization
- **For Content Sites**: Maximize static generation, implement on-demand revalidation from CMS webhooks
- **For SaaS**: Focus on dashboard streaming, client bundle reduction, authenticated route optimization
