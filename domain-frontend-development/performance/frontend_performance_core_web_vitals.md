---
title: "Core Web Vitals Optimization"
category: frontend-development/performance
description: "Analyze and optimize Core Web Vitals (LCP, INP, CLS) for improved user experience and search ranking"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: intermediate
tags:
  - performance
  - core-web-vitals
  - lcp
  - inp
  - cls
  - lighthouse
updated: "2026-01-29"
related_prompts:
  - domain-frontend-development/performance/frontend_performance_bundle_optimization.md
  - domain-frontend-development/react/frontend_react_performance.md
  - domain-software-engineering/analysis/performance/performance_bottleneck_identification.md
---

# Core Web Vitals Optimization

**Objective:** Analyze a web application's Core Web Vitals performance, identify specific bottlenecks affecting LCP, INP, and CLS, and provide actionable optimization strategies with measurable impact.

**When to Use:**
- Use when: Core Web Vitals scores are below targets (failing Google's assessment)
- Use when: Users complain about slow or janky experience
- Use when: Preparing for performance-sensitive launch
- Use when: SEO ranking is affected by performance
- Don't use when: Micro-optimizing already-good performance

## Instructions

1. **Measure Current Performance**
   - Run Lighthouse in incognito mode
   - Check PageSpeed Insights for field data
   - Analyze Chrome DevTools Performance panel
   - Review Real User Monitoring (RUM) data if available

2. **Analyze LCP (Largest Contentful Paint)**
   - Identify the LCP element
   - Measure time to first byte (TTFB)
   - Check resource loading priority
   - Evaluate render-blocking resources

3. **Analyze INP (Interaction to Next Paint)**
   - Identify slow interactions
   - Measure main thread blocking time
   - Check JavaScript execution time
   - Evaluate event handler efficiency

4. **Analyze CLS (Cumulative Layout Shift)**
   - Identify elements causing shifts
   - Check for dimension-less images/embeds
   - Look for dynamically injected content
   - Evaluate font loading behavior

5. **CRITICAL: Validate with Real Metrics**
   - Use field data (CrUX) not just lab data
   - Test on representative devices (not just fast dev machines)
   - Consider 75th percentile performance
   - **Confidence level** for each issue:
     - **High Confidence**: Confirmed by both lab and field data
     - **Medium Confidence**: Lab data only, field data pending
     - **Low Confidence**: Theoretical, needs measurement

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Optimize based solely on Lighthouse scores (lab data only)
- Assume your fast dev machine represents user experience
- Over-optimize at cost of functionality or maintainability
- Chase 100 scores when 90 is sufficient
- Ignore mobile performance (most CWV issues are mobile)
- Make changes without measuring impact

✅ **DO:**
- Use Chrome User Experience Report (CrUX) for field data
- Test on throttled network and CPU
- Focus on 75th percentile (p75) metrics
- Measure before and after every change
- Consider the tradeoff of each optimization
- Test on real devices when possible

## Expected Output

A comprehensive Core Web Vitals analysis including:
- Current metric values vs targets
- Root cause analysis for each failing metric
- Prioritized optimization recommendations
- Expected impact and implementation effort

### Output Format

```markdown
## Core Web Vitals Analysis

### Current Performance
[Metrics with pass/fail status]

### LCP Analysis
[Root causes and optimizations]

### INP Analysis
[Root causes and optimizations]

### CLS Analysis
[Root causes and optimizations]

### Optimization Roadmap
[Prioritized actions]
```

## Example Output

```markdown
## Core Web Vitals Analysis

### Executive Summary

**Assessment Date:** 2026-01-29
**URL Tested:** https://example.com/product/123
**Data Source:** PageSpeed Insights + CrUX (Jan 2026)

| Metric | Mobile | Desktop | Target | Status |
|--------|--------|---------|--------|--------|
| LCP | 4.2s | 2.1s | < 2.5s | ❌ Mobile Fails |
| INP | 380ms | 120ms | < 200ms | ❌ Mobile Fails |
| CLS | 0.18 | 0.05 | < 0.1 | ❌ Mobile Fails |

**Overall:** Poor (Mobile), Good (Desktop)
**Estimated Impact:** Fixing mobile issues could improve bounce rate by 20-30% and SEO ranking.

---

### LCP Analysis (4.2s → Target: 2.5s)

#### LCP Element Identified
- **Element:** Hero product image
- **Size:** 2.4 MB (uncompressed), 1.8 MB (current compression)
- **Dimensions:** 1920x1080px
- **Format:** JPEG

#### Root Causes

##### Cause 1: Large Unoptimized Image (Impact: ~1.5s)
- **Confidence:** High
- **Evidence:** Network waterfall shows 1.2s download time for hero image
- **Problem:** Image is 1920px wide but container is 375px on mobile

**Current:**
```html
<img src="/images/product-hero.jpg" alt="Product">
```

**Recommended Fix:**
```html
<img
  src="/images/product-hero-375.webp"
  srcset="
    /images/product-hero-375.webp 375w,
    /images/product-hero-768.webp 768w,
    /images/product-hero-1200.webp 1200w,
    /images/product-hero-1920.webp 1920w
  "
  sizes="(max-width: 768px) 100vw, 50vw"
  alt="Product"
  loading="eager"
  fetchpriority="high"
  decoding="async"
>
```

**Expected Improvement:** ~1.0-1.5s

##### Cause 2: Render-Blocking CSS (Impact: ~0.5s)
- **Confidence:** High
- **Evidence:** 3 CSS files blocking render (420ms)
- **Files:**
  - `styles.css` (85KB)
  - `vendor.css` (120KB)
  - `theme.css` (45KB)

**Recommended Fix:**
1. Inline critical CSS for above-the-fold content
2. Async load non-critical CSS

```html
<head>
  <style>
    /* Critical CSS inlined */
    .hero { ... }
    .nav { ... }
  </style>
  <link rel="preload" href="/styles.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link rel="stylesheet" href="/styles.css"></noscript>
</head>
```

**Expected Improvement:** ~0.3-0.5s

##### Cause 3: Slow Server Response (Impact: ~0.8s)
- **Confidence:** High
- **Evidence:** TTFB is 1.2s (should be < 0.6s)
- **Server Location:** US East, users in EU

**Recommended Fix:**
- Implement CDN for static assets
- Consider edge caching for HTML
- Optimize server-side rendering

**Expected Improvement:** ~0.5-0.8s

##### Cause 4: No Preload Hint (Impact: ~0.4s)
- **Confidence:** Medium
- **Evidence:** LCP image discovered late in parsing

**Recommended Fix:**
```html
<link rel="preload" as="image" href="/images/product-hero-375.webp"
      imagesrcset="..." imagesizes="...">
```

**Expected Improvement:** ~0.2-0.4s

---

### INP Analysis (380ms → Target: 200ms)

#### Slow Interactions Identified

| Interaction | INP Time | Location |
|-------------|----------|----------|
| Add to Cart | 380ms | Product page |
| Filter toggle | 320ms | Category page |
| Menu open | 280ms | Global header |

#### Root Causes

##### Cause 1: Synchronous Cart Update (Impact: ~200ms)
- **Confidence:** High
- **Evidence:** Main thread blocked during localStorage + fetch
- **Location:** `addToCart()` function

**Current Code:**
```javascript
function addToCart(product) {
  // Blocking: runs synchronously
  const cart = JSON.parse(localStorage.getItem('cart') || '[]');
  cart.push(product);
  localStorage.setItem('cart', JSON.stringify(cart));

  // Blocking: synchronous fetch
  fetch('/api/cart', { method: 'POST', body: JSON.stringify(cart) })
    .then(updateUI);
}
```

**Recommended Fix:**
```javascript
async function addToCart(product) {
  // Optimistic UI update first
  updateCartUI(product);

  // Defer heavy work
  requestIdleCallback(async () => {
    const cart = JSON.parse(localStorage.getItem('cart') || '[]');
    cart.push(product);
    localStorage.setItem('cart', JSON.stringify(cart));

    try {
      await fetch('/api/cart', { method: 'POST', body: JSON.stringify(cart) });
    } catch (e) {
      // Rollback optimistic update
      rollbackCartUI(product);
    }
  });
}
```

**Expected Improvement:** ~150-200ms

##### Cause 2: Heavy Event Handler (Impact: ~120ms)
- **Confidence:** High
- **Evidence:** Filter handler recalculates and re-renders entire product list
- **Location:** Product filter click handler

**Current:**
```javascript
filterButton.addEventListener('click', () => {
  // All synchronous
  const filtered = products.filter(p => p.category === selected);
  const sorted = filtered.sort((a, b) => a.price - b.price);
  renderProducts(sorted); // Blocks for 80ms
});
```

**Recommended Fix:**
```javascript
filterButton.addEventListener('click', () => {
  // Show loading state immediately
  showLoadingIndicator();

  // Defer heavy computation
  setTimeout(() => {
    const filtered = products.filter(p => p.category === selected);
    const sorted = filtered.sort((a, b) => a.price - b.price);
    renderProducts(sorted);
    hideLoadingIndicator();
  }, 0);
});
```

**Expected Improvement:** ~80-120ms (perceived)

##### Cause 3: Third-Party Script Blocking (Impact: ~60ms)
- **Confidence:** Medium
- **Evidence:** Analytics script runs synchronously on interaction
- **Script:** Google Tag Manager + custom events

**Recommended Fix:**
```javascript
// Defer analytics to after paint
button.addEventListener('click', () => {
  performAction();

  // Analytics after next paint
  requestAnimationFrame(() => {
    requestAnimationFrame(() => {
      gtag('event', 'button_click', {...});
    });
  });
});
```

**Expected Improvement:** ~40-60ms

---

### CLS Analysis (0.18 → Target: 0.1)

#### Layout Shifts Identified

| Element | Shift Score | Cause |
|---------|-------------|-------|
| Hero image | 0.08 | Missing dimensions |
| Ad banner | 0.06 | Late injection |
| Web font | 0.04 | FOIT/FOUT |

#### Root Causes

##### Cause 1: Image Without Dimensions (Impact: 0.08)
- **Confidence:** High
- **Evidence:** Image loads after text, pushing content down
- **Location:** Product hero image

**Current:**
```html
<img src="/hero.jpg" alt="Hero">
```

**Recommended Fix:**
```html
<img
  src="/hero.jpg"
  alt="Hero"
  width="1200"
  height="630"
  style="aspect-ratio: 1200/630; width: 100%; height: auto;"
>
```

Or with CSS:
```css
.hero-image {
  aspect-ratio: 16/9;
  width: 100%;
  height: auto;
}
```

**Expected Improvement:** CLS -0.08

##### Cause 2: Dynamically Injected Ad Banner (Impact: 0.06)
- **Confidence:** High
- **Evidence:** Ad loads 2s after page load, pushes content
- **Location:** Above the fold ad placement

**Recommended Fix:**
```html
<!-- Reserve space for ad -->
<div class="ad-container" style="min-height: 250px;">
  <div id="ad-slot"></div>
</div>
```

```css
.ad-container {
  min-height: 250px; /* Leaderboard ad height */
  background: #f0f0f0; /* Placeholder color */
  contain: layout;
}
```

**Expected Improvement:** CLS -0.06

##### Cause 3: Font Loading Causes Shift (Impact: 0.04)
- **Confidence:** High
- **Evidence:** Text reflows when custom font loads
- **Font:** 'Roboto' web font

**Current:**
```css
@font-face {
  font-family: 'Roboto';
  src: url('/fonts/roboto.woff2') format('woff2');
}
```

**Recommended Fix:**
```css
@font-face {
  font-family: 'Roboto';
  src: url('/fonts/roboto.woff2') format('woff2');
  font-display: optional; /* Prevent layout shift */
  size-adjust: 100%;
  ascent-override: 90%;
  descent-override: 20%;
}
```

Plus preload:
```html
<link rel="preload" href="/fonts/roboto.woff2" as="font" type="font/woff2" crossorigin>
```

**Expected Improvement:** CLS -0.02 to -0.04

---

### Optimization Roadmap

#### Phase 1: Quick Wins (Week 1)
| Action | Metric | Impact | Effort |
|--------|--------|--------|--------|
| Add image dimensions | CLS | -0.08 | 1h |
| Reserve ad space | CLS | -0.06 | 1h |
| Preload LCP image | LCP | -0.4s | 30min |
| Add `font-display: optional` | CLS | -0.04 | 30min |
| Inline critical CSS | LCP | -0.3s | 4h |

**Expected Result After Phase 1:**
- LCP: 4.2s → 3.5s
- CLS: 0.18 → 0.02 ✅
- INP: 380ms (unchanged)

#### Phase 2: Image Optimization (Week 2)
| Action | Metric | Impact | Effort |
|--------|--------|--------|--------|
| Implement responsive images | LCP | -1.0s | 8h |
| Convert to WebP/AVIF | LCP | -0.3s | 4h |
| Implement image CDN | LCP | -0.5s | 4h |

**Expected Result After Phase 2:**
- LCP: 3.5s → 2.2s ✅
- CLS: 0.02 ✅
- INP: 380ms (unchanged)

#### Phase 3: JavaScript Optimization (Week 3)
| Action | Metric | Impact | Effort |
|--------|--------|--------|--------|
| Defer cart update | INP | -150ms | 4h |
| Optimize filter handler | INP | -100ms | 4h |
| Defer analytics | INP | -50ms | 2h |
| Code-split heavy modules | INP | -30ms | 8h |

**Expected Result After Phase 3:**
- LCP: 2.2s ✅
- CLS: 0.02 ✅
- INP: 380ms → 180ms ✅

---

### Monitoring Setup

```javascript
// web-vitals library
import { onLCP, onINP, onCLS } from 'web-vitals';

function sendToAnalytics(metric) {
  const body = JSON.stringify({
    name: metric.name,
    value: metric.value,
    delta: metric.delta,
    id: metric.id,
    navigationType: metric.navigationType,
  });

  navigator.sendBeacon('/analytics', body);
}

onLCP(sendToAnalytics);
onINP(sendToAnalytics);
onCLS(sendToAnalytics);
```

### CI/CD Integration

```yaml
# .github/workflows/lighthouse.yml
- name: Lighthouse CI
  uses: treosh/lighthouse-ci-action@v10
  with:
    urls: |
      https://example.com/
      https://example.com/product/123
    budgetPath: ./lighthouse-budget.json
    uploadArtifacts: true

# lighthouse-budget.json
{
  "performance": [
    { "metric": "largest-contentful-paint", "budget": 2500 },
    { "metric": "interaction-to-next-paint", "budget": 200 },
    { "metric": "cumulative-layout-shift", "budget": 0.1 }
  ]
}
```

---

### Success Criteria

| Metric | Current | Target | Deadline |
|--------|---------|--------|----------|
| LCP (mobile p75) | 4.2s | < 2.5s | Week 3 |
| INP (mobile p75) | 380ms | < 200ms | Week 3 |
| CLS (mobile p75) | 0.18 | < 0.1 | Week 1 |

**Validation:** Check PageSpeed Insights and CrUX after 28 days of field data collection.
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Focused on CWV optimization
- **ST-02 (Structured Sequential Instructions):** Metric-by-metric analysis
- **RT-02 (Multi-Dimensional Analysis):** LCP, INP, CLS breakdown
- **RT-05 (Evidence-Based Reasoning):** Measurements for each finding
- **DS-06 (Prioritization Guidance):** Phased roadmap

## Related Prompts

- [frontend_performance_bundle_optimization.md](frontend_performance_bundle_optimization.md) - Bundle size focus
- [frontend_react_performance.md](../react/frontend_react_performance.md) - React-specific performance
- [performance_bottleneck_identification.md](../../domain-software-engineering/analysis/performance/performance_bottleneck_identification.md) - General performance

## Customization Guide

- **For SPAs**: Focus on route change INP and dynamic content CLS
- **For E-commerce**: Prioritize product page LCP, add-to-cart INP
- **For News Sites**: Focus on article page LCP, ad-related CLS
- **For Mobile-First**: Weight mobile metrics 3x over desktop
