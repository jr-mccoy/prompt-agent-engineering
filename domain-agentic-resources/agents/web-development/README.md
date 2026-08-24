# Web Development Agents

Specialist agents for modern web frontend frameworks and cross-cutting concerns (performance, accessibility). Complements `frontend-mobile/` (which targets native iOS/Android) and the `skills/web-development/` skill bundle.

## Agents

| Agent | Model | Use For |
|-------|-------|---------|
| [`react-engineer`](react_engineer.md) | Sonnet | React 18+ idioms, hooks, Suspense, render perf, state management |
| [`nextjs-specialist`](nextjs_specialist.md) | Opus | App Router architecture, Server Components, caching, ISR/SSG/SSR strategy |
| [`vue-engineer`](vue_engineer.md) | Sonnet | Vue 3 Composition API, reactivity, Pinia, Nuxt 3 SSR |
| [`web-performance-engineer`](web_performance_engineer.md) | Opus | Core Web Vitals (LCP/INP/CLS), bundle optimization, perf budgets |
| [`accessibility-auditor`](accessibility_auditor.md) | Opus | WCAG 2.2 AA audits, ARIA patterns, screen reader testing |

## Companion Skills

These agents typically invoke skills from:

- `skills/web-development/` — framework-specific patterns (Next.js App Router, React state, Astro, Cloudflare)
- `skills/accessibility/` — WCAG audit, screen reader testing patterns
- `skills/seo-marketing/core-web-vitals-audit/` — performance audit workflow

## Selection Guide

- **Building a React app:** `react-engineer` (Sonnet) for component-level work; escalate to `nextjs-specialist` (Opus) for routing/caching/RSC decisions
- **Building a Vue app:** `vue-engineer` (Sonnet) covers Vue 3 + Nuxt 3
- **Performance issue or pre-launch perf gate:** `web-performance-engineer` (Opus)
- **Compliance, accessibility complaint, or pre-launch a11y gate:** `accessibility-auditor` (Opus)
