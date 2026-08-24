---
title: "Web Animation & Motion Performance Audit"
category: frontend-development/animation
description: "Audit and design web animations for 60fps: choosing CSS vs JS vs Framer Motion/GSAP, animating GPU-friendly properties, honoring reduced-motion, and eliminating jank from layout thrash and main-thread work."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: advanced
tags:
  - animation
  - performance
  - css-animation
  - framer-motion
  - gsap
  - reduced-motion
  - jank
updated: "2026-06-21"
related_prompts:
  - domain-frontend-development/performance/frontend_performance_core_web_vitals.md
  - domain-frontend-development/performance/frontend_performance_bundle_optimization.md
  - domain-frontend-development/react/frontend_react_performance.md
  - domain-frontend-development/accessibility/frontend_accessibility_wcag_audit.md
---

# Web Animation & Motion Performance Audit

**Objective:** Make animations smooth (target ~60fps / a ~16ms frame budget) and respectful of user preferences by choosing the right animation technique, animating compositor-friendly properties, and removing main-thread and layout-thrash bottlenecks.

**When to Use:**
- Use when: An animation looks janky, stutters, or drops frames, especially on mid/low-end devices.
- Use when: Choosing how to implement motion (CSS transitions/keyframes, the Web Animations API, Framer Motion, GSAP, or a spring library).
- Use when: Adding scroll-driven, drag, or layout-transition animations that risk reflow.
- Use when: Ensuring `prefers-reduced-motion` is honored for accessibility.
- Don't use when: There is no motion on the page, or a single opacity fade that is already smooth — a full audit is unwarranted.

## Instructions

1. **Inventory Animations and Triggers**
   - List each animation: what animates, what triggers it (load, hover, scroll, drag, route change), and its duration/easing.
   - Note which run continuously, which are interaction-driven, and which run during critical interactions (where jank is most visible).

2. **Classify Animated Properties**
   - For each animation, identify which CSS properties change and classify them:
     - **Compositor-friendly** (`transform`, `opacity`) — can be GPU-accelerated, no layout/paint.
     - **Paint-triggering** (`color`, `background`, `box-shadow`, `border-radius`) — repaint each frame.
     - **Layout-triggering** (`width`, `height`, `top`/`left`, `margin`) — reflow each frame; primary jank source.
   - Flag every layout-triggering animation as a high-priority issue; prefer `transform` equivalents.

3. **Audit for Layout Thrash and Main-Thread Work**
   - Look for read-then-write loops that force synchronous layout (reading `offsetWidth`/`getBoundingClientRect` then writing styles in the same frame).
   - Identify JS-driven animations updating layout per frame instead of using `transform`, and heavy per-frame work on the main thread.
   - Check whether `requestAnimationFrame` is used for JS animation rather than `setInterval`/`setTimeout`.

4. **Evaluate Technique Choice**
   - Map each animation to the lightest adequate tool:
     - **CSS transitions/keyframes** — simple state/enter-exit transitions; offloadable to compositor.
     - **Web Animations API** — programmatic control without a library.
     - **Framer Motion** — declarative React animations, layout/shared-element transitions (mind bundle cost and re-renders).
     - **GSAP** — complex timelines/sequencing/scroll; powerful but adds weight.
   - Note bundle-size tradeoffs and whether a library is justified by the complexity it removes.

5. **Audit `will-change` and Layer Promotion**
   - Confirm `will-change`/layer promotion is applied sparingly and removed after the animation — over-promotion wastes memory and can hurt performance.
   - Verify GPU layers aren't created for static elements.

6. **Audit Reduced-Motion Support**
   - Confirm a `@media (prefers-reduced-motion: reduce)` block (or JS equivalent) disables or tones down non-essential motion.
   - Ensure essential transitions remain understandable when motion is reduced (e.g., instant state changes, gentle cross-fades).

7. **Estimate Frame Budget Impact**
   - For continuous/interaction animations, reason about per-frame cost against the ~16ms budget; note where measurement (DevTools Performance panel) is needed rather than asserting numbers.

8. **CRITICAL: Verify findings before reporting**
   - Confirm jank causes by profiling (Performance panel: long tasks, forced reflow, dropped frames) rather than guessing.
   - Do not cite specific fps/ms gains you have not measured; phrase expected improvements qualitatively and recommend measuring.
   - **Confidence level** for each finding:
     - **High Confidence:** Confirmed in a profile trace (forced reflow, long task, dropped frames).
     - **Medium Confidence:** Property/technique strongly implies the cost but not yet profiled.
     - **Low Confidence:** Inferred from code; flagged to measure.

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Animate `width`, `height`, `top`/`left`, or `margin` when `transform: translate/scale` achieves the same visual.
- Slap `will-change` on everything "to make it faster" — over-promotion regresses performance and memory.
- Use `setInterval`/`setTimeout` for animation loops instead of `requestAnimationFrame`.
- Read layout (`offsetHeight`, `getBoundingClientRect`) and write styles in the same frame loop (forces reflow).
- Quote specific fps/ms improvements you have not measured.
- Reach for GSAP/Framer Motion for a simple fade that CSS handles for free.
- Ignore `prefers-reduced-motion` — non-essential motion must be reducible.

✅ **DO:**
- Prefer animating `transform` and `opacity` (compositor-only) wherever possible.
- Promote layers with `will-change` only during the animation, then remove it.
- Batch DOM reads then writes to avoid layout thrashing.
- Use `requestAnimationFrame` for any JS-driven animation.
- Honor `prefers-reduced-motion` with a tested fallback.
- Justify any animation library by the complexity it actually removes, and account for its bundle cost.
- Profile in the Performance panel before and after changes.

## Expected Output

A motion-performance audit/design report including:
- An animation inventory with animated-property classification.
- Identified jank sources (layout thrash, layout-triggering props, main-thread work).
- Technique recommendations per animation with bundle tradeoffs.
- `will-change`/layer findings.
- Reduced-motion assessment.
- Prioritized remediations.

### Output Format

```markdown
## Animation Performance Audit: [Page/Feature]

### Animation Inventory

| Animation | Trigger | Properties Animated | Property Class | Technique |
|-----------|---------|---------------------|----------------|-----------|

### Findings

| ID | Issue | Severity | Confidence | Location | Evidence | Recommendation |
|----|-------|----------|------------|----------|----------|----------------|

### Technique Recommendations
[Per animation]

### Reduced-Motion
[Assessment]

### Prioritized Remediations
1. ...
```

## Example Output

```markdown
## Animation Performance Audit: Product Card Grid + Hero

### Animation Inventory

| Animation | Trigger | Properties Animated | Property Class | Technique |
|-----------|---------|---------------------|----------------|-----------|
| Card hover lift | hover | `top`, `box-shadow` | layout + paint | CSS transition |
| Hero parallax | scroll | `top` (per frame, JS) | layout | JS `scroll` listener |
| Grid reveal on load | load | `opacity`, `transform` | compositor | Framer Motion |
| Drawer open | click | `left` | layout | CSS transition |

### Findings

| ID | Issue | Severity | Confidence | Location | Evidence | Recommendation |
|----|-------|----------|------------|----------|----------|----------------|
| M1 | Card hover animates `top` (reflow each frame) | High | High | `Card.css` `.card:hover { top: -8px }` | Performance trace shows "Layout" on each hover frame | Use `transform: translateY(-8px)` |
| M2 | Hero parallax reads scroll + writes `top` per frame on main thread | High | High | `Hero.tsx` scroll handler | Forced reflow + long tasks while scrolling | Use `transform: translate3d` driven by `requestAnimationFrame`, or a scroll-driven CSS animation |
| M3 | `will-change: transform` left on all 60 cards permanently | Medium | High | `Card.css` | 60 promoted layers regardless of interaction | Apply `will-change` on hover only, remove after |
| M4 | Drawer animates `left` instead of `transform` | Medium | High | `Drawer.css` | Reflow during open/close | Animate `transform: translateX` |
| M5 | No `prefers-reduced-motion` handling | Medium | High | global styles | Grid reveal + parallax run regardless of OS setting | Add reduced-motion block disabling parallax and shortening reveal |
| M6 | Framer Motion imported for a single fade-in | Low | Medium | grid component | Library bundled for one simple animation | Consider CSS keyframes; keep Framer Motion only if richer transitions are planned |

### Technique Recommendations
- **Card hover (M1, M3):** Pure CSS with `transform` + opacity; promote layer only on hover.
- **Hero parallax (M2):** Move off the scroll handler to `transform` updated in `requestAnimationFrame`, or a CSS scroll-driven animation; verify with a profile.
- **Drawer (M4):** `transform: translateX(-100%) → 0`.
- **Grid reveal (M6):** Already compositor-friendly; re-evaluate whether the library is justified.

### Reduced-Motion
No `prefers-reduced-motion` support today. Add:
```css
@media (prefers-reduced-motion: reduce) {
  .hero-parallax { transform: none !important; }
  .grid-item { transition: opacity 0.01ms; }
}
```
Essential state changes (drawer) should become near-instant rather than removed.

### Prioritized Remediations
1. **M1 & M4 — Replace layout-triggering props with `transform`.** Direct, high-impact jank fixes.
2. **M2 — Rework parallax off the main-thread scroll loop.** Biggest scroll-jank source; measure before/after.
3. **M3 — Scope `will-change` to the interaction.** Removes 60 needless GPU layers.
4. **M5 — Add reduced-motion support.** Accessibility + perf for motion-sensitive users.
5. **M6 — Reassess library cost.** Trim bundle if Framer Motion isn't earning its weight.
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Sets the goal — smooth, budget-respecting, preference-aware motion.
- **ST-02 (Structured Sequential Instructions):** Orders inventory → property class → thrash → technique → layers → reduced-motion → budget.
- **RT-02 (Multi-Dimensional Analysis Framework):** Analyzes each animation across property class, technique, layer promotion, and accessibility.
- **RT-05 (Evidence-Based Reasoning):** Ties findings to profile traces and concrete property usage rather than assumptions.
- **DS-06 (Prioritization Guidance):** Ranks fixes by frame-budget impact and visibility.

## Related Prompts

- [../performance/frontend_performance_core_web_vitals.md](../performance/frontend_performance_core_web_vitals.md) - How animation jank affects INP/CLS and overall responsiveness
- [../performance/frontend_performance_bundle_optimization.md](../performance/frontend_performance_bundle_optimization.md) - Bundle cost of animation libraries
- [../react/frontend_react_performance.md](../react/frontend_react_performance.md) - Re-render cost of animation libraries in React
- [../accessibility/frontend_accessibility_wcag_audit.md](../accessibility/frontend_accessibility_wcag_audit.md) - Reduced-motion as a WCAG concern
