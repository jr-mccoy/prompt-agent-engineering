# Next.js Prompts

**Category:** Frontend Development / Next.js
**Prompts:** 3

---

## Overview

Production-grade prompts for Next.js development covering App Router architecture, data fetching and caching strategies, and performance optimization. All prompts focus on the App Router (Next.js 13.4+) with awareness of Pages Router migration paths.

## Prompts

| Prompt | Description | Difficulty |
|--------|-------------|------------|
| [frontend_nextjs_app_router.md](frontend_nextjs_app_router.md) | Analyze App Router architecture, server/client component boundaries, routing patterns, and layouts | Intermediate |
| [frontend_nextjs_data_fetching.md](frontend_nextjs_data_fetching.md) | Audit data fetching patterns, caching strategies, Server Actions, and revalidation | Intermediate |
| [frontend_nextjs_performance.md](frontend_nextjs_performance.md) | Profile and optimize Next.js performance including rendering strategy, bundle size, and images | Advanced |

## Usage Examples

### Reviewing App Router Architecture
Use `frontend_nextjs_app_router.md` to analyze:
- Server vs client component boundaries
- Route organization and convention usage
- Layout and streaming patterns
- Metadata and SEO configuration

### Auditing Data Fetching
Use `frontend_nextjs_data_fetching.md` to identify:
- Sequential waterfall patterns
- Missing or incorrect caching configuration
- Server Actions without revalidation
- Client-side fetching that should be server-side

### Optimizing Performance
Use `frontend_nextjs_performance.md` to find:
- Routes using SSR that could be static/ISR
- Large client bundles from unnecessary `'use client'`
- Missing `next/image`, `next/font`, and `next/script` optimizations
- Core Web Vitals improvements

---

## Related Prompts

- [../react/frontend_react_component_patterns.md](../react/frontend_react_component_patterns.md) - React patterns (Next.js builds on React)
- [../react/frontend_react_performance.md](../react/frontend_react_performance.md) - React performance
- [../performance/frontend_performance_core_web_vitals.md](../performance/frontend_performance_core_web_vitals.md) - Core Web Vitals
- [../performance/frontend_performance_bundle_optimization.md](../performance/frontend_performance_bundle_optimization.md) - Bundle optimization
