---
name: core-web-vitals-audit
description: Audit a page or site for Core Web Vitals (LCP, INP, CLS) using field and lab data, then produce a prioritized fix plan. Use when CWV regressed, before launching a major content push, or when SEO suspects performance is capping rankings.
metadata:
  tags:
    - seo
    - performance
    - core-web-vitals
    - lcp
    - inp
    - cls
  updated: "2026-05-05"
---

# Core Web Vitals Audit

Performance is a ranking factor and a conversion factor. This skill produces a structured CWV audit grounded in both field data (real users) and lab data (controlled measurement), with a fix plan ordered by user impact, not Lighthouse score.

## When to Use This Skill

- Search Console reports a "Poor" or "Needs Improvement" CWV status
- Pre-launch performance check before a content push or paid traffic campaign
- Conversion rate dropped after a redesign — performance suspected
- Performance budget needs to be defined for CI gating

## Audit Pipeline

### Step 1: Get Field Data

Field data (CrUX) reflects what real users experienced over the last 28 days. This is the data Google uses for ranking signals.

**Sources:**
- **Search Console → Core Web Vitals report** (per-URL group, mobile/desktop)
- **PageSpeed Insights** (single URL, shows CrUX 75th percentile)
- **CrUX BigQuery** (raw data, custom slicing)
- **CrUX API** (programmatic per-origin or per-URL)

**Output of this step:**
- LCP at 75th percentile (target: ≤ 2.5s)
- INP at 75th percentile (target: ≤ 200ms)
- CLS at 75th percentile (target: ≤ 0.1)
- Status: Good / Needs Improvement / Poor for each
- Mobile vs. desktop breakdown
- Pass rate (% of URLs with all three metrics in "Good")

### Step 2: Reproduce in Lab

Lab data lets you isolate causes. Run with realistic throttling.

**Lighthouse settings:**
- Mobile emulation
- Slow 4G network throttling
- 4× CPU slowdown
- Run 3-5 times, take median (single runs are noisy)

**WebPageTest settings:**
- Moto G4 or Pixel 4a (real device)
- 3G or Slow 4G
- Multiple test locations

### Step 3: Diagnose Per Metric

#### LCP — Largest Contentful Paint

**Identify the LCP element:**
- DevTools Performance panel → Timings → LCP marker
- Lighthouse → "Largest Contentful Paint element"
- Web Vitals extension shows it overlaid

**Common causes (in order of frequency):**

1. **Slow server response** (TTFB > 600ms)
2. **Render-blocking CSS or JS** (head-of-document scripts, large CSS)
3. **Slow LCP resource load** (unoptimized hero image, no priority hint)
4. **Client-side rendering** (LCP element rendered after JS executes)

**Fix patterns:**
- Add `fetchpriority="high"` and `loading="eager"` to the LCP image
- `preload` the LCP image with `<link rel="preload" as="image">`
- Serve the LCP image in next-gen format (AVIF/WebP) at appropriate size
- Inline critical CSS, defer non-critical
- Move to SSR or static rendering for LCP-critical content
- CDN edge caching for repeat visitors

#### INP — Interaction to Next Paint

INP replaced FID in March 2024 and is harder to fix because it covers all interactions, not just the first.

**Diagnose:**
- DevTools Performance panel → record an interaction → look for long tasks
- Web Vitals extension shows INP per interaction
- DebugBear / SpeedCurve / Calibre offer per-interaction breakdowns

**Common causes:**

1. **Long JavaScript tasks** blocking the main thread during interaction
2. **Heavy event handlers** (e.g., sync rendering of a large list on click)
3. **Excessive third-party scripts** (analytics, A/B testing, ads)
4. **Layout thrashing** (read-write-read of layout properties in a loop)
5. **Hydration overhead** in SSR frameworks

**Fix patterns:**
- Break long tasks with `scheduler.yield()` or `setTimeout(..., 0)` in loops
- Move heavy work to Web Workers
- Defer or remove low-value third-party scripts
- React: `useTransition` or `startTransition` for non-urgent updates
- Vue: `v-memo` or `defineAsyncComponent` for expensive components
- Audit hydration: islands architecture or selective hydration

#### CLS — Cumulative Layout Shift

**Diagnose:**
- DevTools Performance Insights → Layout Shift Culprits
- Web Vitals extension highlights shifting elements

**Common causes:**

1. **Images without dimensions** — reserved space changes when image loads
2. **Web fonts swap-in** (FOUT) — text reflows when custom font loads
3. **Dynamically injected content** (ads, embeds, late-loading components)
4. **Animations on layout properties** (top, left, width, height) instead of transform/opacity

**Fix patterns:**
- Set `width` and `height` on every `<img>` and `<video>`
- Use `aspect-ratio` CSS for responsive media
- `font-display: optional` or `swap` with sizing matched to web font
- Reserve space for ad slots and embeds with min-height
- Animate transform/opacity, never width/height/top/left

### Step 4: Prioritize Fixes

Score each fix by:

| Factor | Weight |
|---|---|
| User impact (% of sessions affected) | High |
| Metric severity (poor > needs improvement) | High |
| Implementation effort | Medium |
| Risk of regression | Medium |
| Affects ranking-critical pages | High |

Output a ranked list:

```markdown
## Fix Priority

1. **[Critical, 1d effort] LCP image not preloaded on /products/*** (35% of sessions, P75 LCP 4.1s → est. 2.4s)
2. **[Critical, 2d effort] Hydration cost on /checkout** (12% of sessions, P75 INP 412ms → est. 180ms)
3. **[Major, 4h effort] Hero image dimensions missing on /blog/*** (28% of sessions, P75 CLS 0.18 → est. 0.04)
4. **[Minor, 1d effort] Tree-shake unused lodash** (savings: 84KB)
```

### Step 5: Set Budgets and Monitoring

Once fixed, prevent regression:

```json
// budgets.json (Lighthouse CI)
[{
  "path": "/*",
  "timings": [
    {"metric": "largest-contentful-paint", "budget": 2500},
    {"metric": "interactive", "budget": 5000}
  ],
  "resourceSizes": [
    {"resourceType": "script", "budget": 200},
    {"resourceType": "image", "budget": 500},
    {"resourceType": "total", "budget": 1500}
  ]
}]
```

Production monitoring:
- web-vitals library reporting to your analytics
- CrUX dashboard refreshed weekly
- Lighthouse CI in PR pipeline
- Alerts on regression > 10% week-over-week

## Audit Report Template

```markdown
# CWV Audit: {site or page group}

**Date:** YYYY-MM-DD
**Scope:** {URLs or path patterns}
**Data sources:** CrUX (28 days, mobile), Lighthouse (median of 5 runs, mobile)

## Field Data (CrUX, P75)

| Metric | Mobile | Desktop | Status (mobile) |
|---|---|---|---|
| LCP | 3.4s | 1.9s | Needs Improvement |
| INP | 285ms | 110ms | Needs Improvement |
| CLS | 0.05 | 0.02 | Good |

## Per-Page Breakdown

| URL pattern | LCP | INP | CLS | Sessions/month |
|---|---|---|---|---|
| /products/* | 4.1s | 320ms | 0.08 | 850K |
| /blog/* | 2.8s | 195ms | 0.18 | 220K |
| /home | 2.1s | 140ms | 0.03 | 1.2M |

## Diagnosis

{per-metric findings, with screenshots, flamegraphs, waterfall}

## Recommendations (Prioritized)

{ranked list as in Step 4}

## Performance Budget Proposal

{budgets.json or equivalent}

## Monitoring Plan

{RUM setup, CI integration, review cadence}
```

## Implementation Checklist

- [ ] Field data pulled from CrUX or RUM (not just Lighthouse)
- [ ] Lab tests run with mobile emulation, Slow 4G, 4× CPU throttling
- [ ] Lab tests use median of 3-5 runs
- [ ] LCP element identified per page group
- [ ] INP diagnosed against actual user interactions, not just synthetic
- [ ] CLS root cause identified (which element shifts and why)
- [ ] Fixes ranked by user impact, not Lighthouse score
- [ ] Budgets defined and committed to repo
- [ ] CI gate on regression
- [ ] RUM monitoring deployed and dashboard linked

## Anti-Patterns to Avoid

- **Lighthouse score as the goal** — score conflates many things; CWV are the actual ranking signals
- **Auditing only on a fast laptop** — the bug isn't there
- **Optimizing without field data** — you don't know what real users see
- **"Preload everything"** — preloading too many resources hurts more than it helps
- **Treating CLS as solved at launch** — late-loading ads and embeds reintroduce it
- **One-time audit** — without monitoring, regression is invisible until Search Console reports it 28 days later

## Companion Skills

- `keyword-cluster-generation` — performance audit before launching cluster pages
- `content-brief-scaffolding` — page brief should include performance budget
- `schema-org-markup` — rich results require performance to actually appear

## Related Resources

- ../../../domain-frontend-development/performance/frontend_performance_core_web_vitals.md
- ../../../domain-frontend-development/performance/frontend_performance_bundle_optimization.md
- web.dev: https://web.dev/articles/vitals
