# Performance Prompts

**Category:** Frontend Development / Performance
**Prompts:** 2

---

## Overview

Production-grade prompts for frontend performance optimization covering Core Web Vitals and JavaScript bundle size analysis.

## Prompts

| Prompt | Description | Difficulty |
|--------|-------------|------------|
| [frontend_performance_core_web_vitals.md](frontend_performance_core_web_vitals.md) | Analyze and optimize LCP, INP, and CLS for improved user experience | Intermediate |
| [frontend_performance_bundle_optimization.md](frontend_performance_bundle_optimization.md) | Reduce JavaScript bundle size through code splitting and dependency management | Advanced |

## Usage Examples

### Core Web Vitals Optimization
Use `frontend_performance_core_web_vitals.md` for:
- Diagnosing slow LCP (images, fonts, CSS)
- Fixing high INP (JavaScript execution, event handlers)
- Eliminating CLS (layout shifts, dynamic content)
- SEO performance improvements

### Bundle Size Reduction
Use `frontend_performance_bundle_optimization.md` for:
- Identifying bloated dependencies
- Implementing code splitting
- Optimizing tree shaking
- Setting up bundle size monitoring

---

## Key Metrics

| Metric | Good | Needs Improvement | Poor |
|--------|------|-------------------|------|
| LCP | ≤ 2.5s | 2.5s - 4s | > 4s |
| INP | ≤ 200ms | 200ms - 500ms | > 500ms |
| CLS | ≤ 0.1 | 0.1 - 0.25 | > 0.25 |

---

## Related Prompts

- [../react/frontend_react_performance.md](../react/frontend_react_performance.md) - React-specific optimization
- [../../domain-software-engineering/analysis/performance/performance_bottleneck_identification.md](../../domain-software-engineering/analysis/performance/performance_bottleneck_identification.md) - General performance
