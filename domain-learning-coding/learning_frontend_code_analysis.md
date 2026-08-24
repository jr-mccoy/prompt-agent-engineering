---
title: "Frontend Code Analysis — Teach a Learner the Strengths, Risks, and Fixes in Frontend Code"
category: "learning-coding"
description: "Analyze supplied frontend code to teach a learner its architecture, component quality, performance, accessibility, and testing characteristics — surfacing accurate strengths, real issues with before/after fixes, and a prioritized improvement list grounded in the actual code."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - QA-01
difficulty: intermediate
tags:
  - learning-coding
  - frontend
  - code-analysis
  - accessibility
  - performance
updated: "2026-06-07"
related_prompts:
  - domain-learning-coding/learning_backend_code_analysis.md
  - domain-learning-coding/learning_code_style_readability_analysis.md
  - domain-frontend-development/performance/frontend_performance_core_web_vitals.md
  - domain-frontend-development/accessibility/frontend_accessibility_wcag_audit.md
---

# Frontend Code Analysis

**Objective:** Analyze supplied frontend code to teach a learner its quality, surfacing accurate strengths, real issues (with before/after fixes), and a prioritized improvement list across architecture, components, performance, accessibility, and testing — all grounded in the actual code.

**When to use:**
- Helping a learner understand an unfamiliar frontend codebase by walking its real patterns.
- Onboarding a new frontend developer to component architecture and risks.
- Preparing for a refactor or framework migration.
- Teaching performance and accessibility using concrete examples.

**When NOT to use:**
- A formal WCAG audit or Lighthouse performance audit — use the dedicated frontend prompts.
- Backend code — use `learning_backend_code_analysis.md`.
- When no code is supplied and feedback would be speculative.

**Audience:** Frontend learners (junior to mid-level), engineers onboarding, reviewers teaching standards.

---

## Inputs / Context

The user supplies:
1. **The frontend code** — pasted wrapped in a named tag, e.g. `<code>...</code>`, or a reference (framework + file paths).
2. **Framework** (React, Vue, Angular, Svelte) and styling approach.
3. **Learner level** to calibrate explanation depth.
4. **Learning goal** (architecture, performance, accessibility, testability).
5. **Optional:** bundle reports, known performance/a11y complaints, target metrics.

Reference the pasted code by its tag name (e.g. "the `ProductList` render in `<code>`") when citing issues.

---

## Constraints

### Must
- Analyze only what `<code>` shows; trace component data flow and render behavior before judging. If behavior is unclear, say so and ask.
- Cite a concrete location for every issue and every strength.
- For each issue, show a before/after with a level-appropriate explanation; confirm the fix preserves behavior.
- For accessibility, point to the specific element and the concrete user impact.
- Cover architecture, component quality, performance, accessibility, and testing.

### Must Not
- Invent re-render problems, bundle sizes, or a11y violations not evidenced by the code.
- Assume a framework behavior (memoization, reactivity) without confirming it in the code.
- State exact bundle figures unless provided; mark estimates as estimates.
- Flag style preferences as critical issues.

---

## Instructions

1. **Trace the code.** From `<code>`, map component hierarchy, state/data flow, and effects. Flag anything you cannot determine.
2. **Assess architecture.** Directory/component organization, state management, composition, routing — as they actually appear.
3. **Evaluate component quality.** Reusability, single responsibility, prop typing, state placement, effect cleanup — citing code.
4. **Review performance.** Unnecessary re-renders, missing memoization, unstable callbacks, list keys, lazy-loading, heavy dependencies. Mark bundle figures as estimates unless supplied.
5. **Check accessibility.** Semantic HTML, labels, ARIA, keyboard support, focus management — name the element and the user impact.
6. **Evaluate testing.** Coverage of components, user flows, and a11y, where evidenced.
7. **Write findings + prioritize.** Per-issue location/severity/why/fix; then a ranked action table.
8. **Self-check (verification).** Each finding traced to real code, severity honest, fix behavior-preserving, estimates labeled, uncertainty flagged.

---

## False-Positive Prevention

❌ **DON'T:**
- Claim a component re-renders unnecessarily without tracing why from the code.
- State a precise bundle size that wasn't provided.
- Assert an a11y violation without pointing to the specific element.
- Assume `memo`/`useMemo`/reactivity handles something the code doesn't show.
- Assume the learner knows "memoization," "prop drilling," or "WCAG" — define them.

✅ **DO:**
- Trace render/data flow before judging performance.
- Cite the exact element/location for every claim.
- Label bundle figures as estimates unless measured data is supplied.
- Tie each a11y issue to a concrete user impact.
- Calibrate explanations and fixes to the stated learner level.

---

## Output Format

```
# Frontend Code Analysis — [module]

## Summary
- Health snapshot: [per-category one-liners]
- Top priorities: [each with location]

## Architecture
- Strengths / Issues [ID — severity — location — fix]

## Component Quality
## Performance
## Accessibility
## Testing

## Prioritized Recommendations
| Priority | Issue | Action | Effort |
```

---

## Example Output

```markdown
# Frontend Code Analysis — Storefront (React)

## Summary
| Category | Assessment |
|----------|------------|
| Architecture | Strong: clear ui/features/layouts split |
| Performance | Needs work: missing memoization, heavy deps |
| Accessibility | Critical gaps: unlabeled inputs, click-divs |
| Testing | Good foundation |

### Top Priorities
1. Accessibility: unlabeled email input + non-interactive click handlers.
2. Performance: unstable callbacks re-rendering `ProductCard`.
3. Heavy dependency (`moment`) inflating the bundle (estimate — verify with analyzer).

---

## Performance

**Issue P1: Missing memoization / unstable callbacks** — `ProductList` in `<code>`
```tsx
// BEFORE: new function each render → every ProductCard re-renders
{products.filter(p => matchesFilters(p, filters)).map(p =>
  <ProductCard key={p.id} product={p} onAddToCart={handleAddToCart} />)}

// AFTER: memoized filter + stable callback + memoized child
const filtered = useMemo(() => products.filter(p => matchesFilters(p, filters)), [products, filters]);
const handleAddToCart = useCallback((id) => dispatch(addToCart(id)), [dispatch]);
// const ProductCard = memo(function ProductCard(...) {...});
```
*Why it matters (intermediate):* a new `onAddToCart` function each render makes React think the prop changed, so children re-render even when their data didn't.

**Issue P2: Heavy dependency** — `moment` (~232KB) could be `date-fns` (~12KB). *(Sizes are estimates — verify with a bundle analyzer.)*

---

## Accessibility

**Issue A11Y-1: Unlabeled input** — email field
```tsx
// BEFORE
<input type="email" placeholder="Enter your email" />
// AFTER
<label htmlFor="email-input" className="sr-only">Email address</label>
<input id="email-input" type="email" aria-describedby="email-hint" />
<span id="email-hint" className="sr-only">We'll never share your email</span>
```
*User impact:* screen-reader users hear only "edit text," with no idea what to type. Placeholders are not labels.

**Issue A11Y-2: Click handler on a `div`** — product card
```tsx
// AFTER: real button semantics → keyboard + screen-reader support
<button className="card" onClick={handleClick} aria-label={`View details for ${product.name}`}>
  <img src={product.image} alt="" /><h3>{product.name}</h3>
</button>
```

---

## Prioritized Recommendations
| Priority | Issue | Action | Effort |
|----------|-------|--------|--------|
| High | Unlabeled/clickable-div a11y | Add labels, fix semantics | 3 days |
| High | Re-render/bundle | Memoize + replace moment | 2 days |
| Medium | Prop drilling | Introduce context | 1 day |
```

---

## Verification

- [ ] Every issue and strength cites a real location in the supplied code.
- [ ] Render/data flow was traced before performance claims.
- [ ] Bundle figures are labeled as estimates unless measured data was supplied.
- [ ] Each a11y issue names the element and the user impact.
- [ ] Each before/after preserves behavior.
- [ ] Explanations are calibrated to the stated learner level.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Frames the task as accurate, teaching-oriented frontend analysis.
- **ST-02 (Structured Sequential Instructions):** Trace → architecture → components → performance → a11y → testing → prioritize → verify.
- **RT-02 (Multi-Dimensional Analysis Framework):** Examines architecture, performance, accessibility, and testing together.
- **RT-05 (Evidence-Based Reasoning):** Requires a cited location for every claim.
- **QA-01 (Self-Verification):** Final pass checks accuracy, labels estimates, confirms fixes.

---

## Related Prompts

- `domain-learning-coding/learning_backend_code_analysis.md` — Backend counterpart.
- `domain-learning-coding/learning_code_style_readability_analysis.md` — Style-focused analysis.
- `domain-frontend-development/performance/frontend_performance_core_web_vitals.md` — Measured performance audit.
- `domain-frontend-development/accessibility/frontend_accessibility_wcag_audit.md` — Formal WCAG audit.
