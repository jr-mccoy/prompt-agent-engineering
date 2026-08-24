# Styling Prompts

**Category:** Frontend Development / Styling
**Prompts:** 3

---

## Overview

Production-grade prompts for auditing and improving frontend styling layers — whether the codebase uses plain/Sass CSS with a methodology, utility-first Tailwind, or CSS-in-JS. Each prompt is an evidence-based review that distinguishes intentional patterns from debt and produces prioritized, low-regression-risk recommendations.

## Prompts

| Prompt | Description | Difficulty |
|--------|-------------|------------|
| [frontend_styling_css_architecture.md](frontend_styling_css_architecture.md) | Audit CSS architecture (BEM/ITCSS/utility-first), cascade layers, specificity, and design-token discipline for scalability | Intermediate |
| [frontend_styling_tailwind_design_system.md](frontend_styling_tailwind_design_system.md) | Review a Tailwind config as a design system: token mapping, theme extension, component extraction, purge/JIT correctness, consistency | Intermediate |
| [frontend_styling_css_in_js_review.md](frontend_styling_css_in_js_review.md) | Review CSS-in-JS (styled-components/Emotion/vanilla-extract) for runtime cost, SSR correctness, re-renders, and zero-runtime alternatives | Advanced |

## Usage Examples

### Untangling CSS Debt
Use `frontend_styling_css_architecture.md` when you have specificity wars, `!important` proliferation, suspected dead CSS, or no consistent methodology — it maps the cascade strategy and recommends layers and token coverage.

### Treating Tailwind as a Design System
Use `frontend_styling_tailwind_design_system.md` when arbitrary values and copy-pasted class strings have crept in, or when `content`/purge misconfiguration is dropping or bloating styles.

### Deciding Optimize vs Migrate in CSS-in-JS
Use `frontend_styling_css_in_js_review.md` when hydration is slow, styles flash, or styling is re-render-heavy — it separates static (cheap) from dynamic (costly) styles and reasons about a zero-runtime move.

---

## Key Concepts

| Concept | Where it applies |
|---------|------------------|
| Cascade layers (`@layer`) & specificity | CSS architecture |
| Design tokens (custom properties, config) | All three |
| Purge / JIT / content scanning | Tailwind |
| Runtime cost & SSR style registry | CSS-in-JS |
| Component/variant extraction | Tailwind, CSS-in-JS |

> Anti-fabrication note: these prompts deliberately avoid asserting fixed benchmark numbers or version-specific library behavior; they recommend measurement and verification against current docs.

---

## Related Prompts

- [../performance/frontend_performance_bundle_optimization.md](../performance/frontend_performance_bundle_optimization.md) - Reducing CSS/JS payload size
- [../react/frontend_react_component_patterns.md](../react/frontend_react_component_patterns.md) - Component boundaries that styling should follow
- [../typescript/frontend_typescript_component_typing.md](../typescript/frontend_typescript_component_typing.md) - Typing styled/variant component APIs
