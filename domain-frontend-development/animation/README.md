# Animation Prompts

**Category:** Frontend Development / Animation
**Prompts:** 1

---

## Overview

Production-grade prompts for web animation and motion performance — choosing the right technique (CSS, Web Animations API, Framer Motion, GSAP), animating compositor-friendly properties, honoring reduced-motion preferences, and eliminating jank from layout thrash and main-thread work.

## Prompts

| Prompt | Description | Difficulty |
|--------|-------------|------------|
| [frontend_animation_motion_performance.md](frontend_animation_motion_performance.md) | Audit/design animations for ~60fps: CSS vs JS vs Framer Motion/GSAP, GPU-accelerated properties, reduced-motion, jank/layout-thrash audit, frame-budget reasoning | Advanced |

## Key Concepts

- **Compositor-friendly properties**: Prefer animating `transform` and `opacity`; avoid layout-triggering props (`width`, `height`, `top`/`left`, `margin`).
- **Frame budget**: Target ~60fps (~16ms per frame); profile rather than assert numbers.
- **Layout thrash**: Don't read layout and write styles in the same frame loop.
- **`will-change` discipline**: Promote layers only during the animation, then remove — over-promotion regresses performance.
- **`requestAnimationFrame`**: Drive JS animation with rAF, never `setInterval`/`setTimeout`.
- **Reduced motion**: Honor `prefers-reduced-motion` for non-essential animation.

## Usage Examples

### Fixing a Janky Animation
Use `frontend_animation_motion_performance.md` to classify animated properties, find layout thrash, and replace layout-triggering animations with `transform` equivalents.

### Choosing an Animation Approach
Use the same prompt to map each animation to the lightest adequate tool and weigh library bundle costs.

---

## Related Prompts

- [../performance/frontend_performance_core_web_vitals.md](../performance/frontend_performance_core_web_vitals.md) - How animation jank affects INP/CLS
- [../performance/frontend_performance_bundle_optimization.md](../performance/frontend_performance_bundle_optimization.md) - Bundle cost of animation libraries
- [../react/frontend_react_performance.md](../react/frontend_react_performance.md) - Re-render cost of animation libraries in React
- [../accessibility/frontend_accessibility_wcag_audit.md](../accessibility/frontend_accessibility_wcag_audit.md) - Reduced-motion as a WCAG concern
