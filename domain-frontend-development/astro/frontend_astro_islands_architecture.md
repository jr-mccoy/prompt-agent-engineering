---
title: "Astro Islands Architecture and Partial Hydration Audit"
category: frontend-development/astro
description: "Analyze an Astro project for server-first rendering, island boundaries, client directive selection (client:load/idle/visible/media/only), and partial-hydration tradeoffs to ship the least JavaScript that still meets interactivity needs."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: intermediate
tags:
  - astro
  - islands-architecture
  - partial-hydration
  - client-directives
  - server-first
  - ssr
updated: "2026-06-21"
related_prompts:
  - domain-frontend-development/astro/frontend_astro_content_collections.md
  - domain-frontend-development/performance/frontend_performance_core_web_vitals.md
  - domain-frontend-development/react/frontend_react_server_components_streaming.md
  - domain-frontend-development/architecture/frontend_state_management_selection.md
---

# Astro Islands Architecture and Partial Hydration Audit

**Objective:** Audit an Astro codebase to confirm it stays server-first by default, verify that every interactive island is justified and uses the correct `client:*` directive, and surface places where hydration is missing, excessive, or mis-triggered.

**When to Use:**
- Use when: Reviewing an Astro site for excess client-side JavaScript or hydration mistakes
- Use when: A content/marketing site feels heavy despite being "mostly static"
- Use when: Choosing between `client:load`, `client:idle`, `client:visible`, `client:media`, and `client:only`
- Use when: Migrating components from a SPA framework into Astro islands
- Don't use when: Building a fully interactive app where a SPA framework (Next.js, Remix, SvelteKit) is the better fit — see the framework-selection comparison prompts instead

## Instructions

1. **Confirm the Server-First Baseline**
   - Verify `.astro` components render to HTML with zero client JS unless a `client:*` directive is present.
   - Identify the rendering mode in `astro.config.*`: static (`output: 'static'`), server (`output: 'server'`), or hybrid/on-demand. Confirm it matches the site's needs and verify the exact option names against current docs.
   - Catalog UI-framework integrations in use (React, Vue, Svelte, Solid, Preact) and whether each is genuinely needed or could be a plain `.astro` component.
   - Establish a "JS budget" expectation: a content page should ship close to zero KB of framework runtime where possible.

2. **Inventory Every Island and Its Directive**
   - Grep for `client:` across the project. For each occurrence record: component, framework, directive, and what interaction justifies it.
   - Map the directive to its intended hydration trigger:
     - `client:load` — hydrate immediately on page load (use sparingly; above-the-fold critical interactivity only)
     - `client:idle` — hydrate when the main thread is idle (deferrable interactivity)
     - `client:visible` — hydrate when the element scrolls into view (below-the-fold widgets)
     - `client:media` — hydrate only when a media query matches (e.g., mobile-only menus)
     - `client:only` — skip SSR entirely; render only on the client (last resort; causes layout shift / no-JS blankness)
   - Flag directives that are stronger than needed (e.g., `client:load` on a footer newsletter form that could be `client:visible`).

3. **Analyze Island Boundaries and Granularity**
   - Check that islands are scoped to the smallest interactive unit, not whole page sections wrapping static content.
   - Look for "island bloat": a large component hydrated to make one button work — extract the interactive part.
   - Verify static content (headings, copy, images) lives in `.astro` or is passed as slotted children, not re-rendered inside a hydrated framework component.
   - Confirm islands do not duplicate framework runtimes unnecessarily (e.g., mixing React and Vue islands when one framework would suffice).

4. **Evaluate Data and State Across Islands**
   - Confirm build-time / request-time data is fetched in the Astro frontmatter (server) and passed as props, not refetched client-side inside islands.
   - Identify cross-island shared state. Astro islands are isolated by design; flag attempts to share React/Vue context across separate islands (it won't work) and recommend nano-store-style shared state or lifting state into a single island. Verify any named state library against current docs.
   - Check for prop serialization issues: only serializable values cross the server→island boundary (no functions, class instances, or non-JSON data).

5. **Assess Performance and UX Impact**
   - Estimate the JS shipped per route and whether `client:only` components cause Cumulative Layout Shift or flashes of empty content.
   - Check `client:visible` widgets near the fold that may hydrate immediately anyway, negating the benefit.
   - Verify View Transitions / persistent islands (if used) don't re-run expensive hydration on navigation. Confirm feature names against current docs.

6. **CRITICAL: Verify findings before reporting**
   - Re-read the component to confirm a `client:*` directive is actually present (or absent) before flagging.
   - Distinguish "no hydration" that is correct (static content) from a genuine missing-interactivity bug.
   - Confirm a directive downgrade preserves required behavior (e.g., a search box that must work before scroll cannot be `client:visible`).
   - **Confidence level** for each finding:
     - **High Confidence:** Clear over-hydration or wrong directive with evidence in the source
     - **Medium Confidence:** Plausibly suboptimal directive that depends on UX intent
     - **Low Confidence:** Stylistic / budget preference

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Flag a static `.astro` component as "missing hydration" — zero JS is the goal, not a defect
- Recommend `client:only` to "fix" SSR mismatches without weighing the layout-shift and no-JS cost
- Treat every `client:load` as wrong; some above-the-fold widgets genuinely need it
- Assume React/Vue context will share state across separate islands — and don't flag the absence of sharing as a bug
- Invent directive names or config keys; if unsure, write "verify against current Astro docs"
- Recommend merging islands when isolation is intentional (independent hydration is a feature)
- Assume Astro should behave like a SPA framework or that all interactivity must be client-rendered

✅ **DO:**
- Default to "the right amount of JS is the least that satisfies the interaction"
- Match each directive to a concrete hydration trigger and verify the interaction needs it
- Verify data is fetched server-side in frontmatter and passed as serializable props
- Confirm a recommended directive downgrade still meets the UX requirement
- Treat `client:only` as a last resort and document its tradeoffs when recommending it
- Keep islands scoped to the smallest interactive unit
- Phrase version- or API-specific claims neutrally and flag them for verification

## Expected Output

A partial-hydration audit including:
- Rendering-mode and integration baseline
- A full island inventory with directive justification
- Boundary/granularity findings
- Data-flow and cross-island state assessment
- Prioritized recommendations with impact/effort

### Output Format

```markdown
## Astro Islands Architecture Audit

### Executive Summary
[Server-first posture, JS budget, headline findings]

### Rendering Baseline
[Output mode, integrations, expected JS budget]

### Island Inventory
[Table: component | framework | directive | justification | assessment]

### Boundary & Granularity Findings
[Over-hydration, island bloat, static-in-island]

### Data & Cross-Island State
[Server fetching, serialization, shared-state issues]

### Recommendations
[Prioritized by impact/effort]
```

## Example Output

```markdown
## Astro Islands Architecture Audit

### Executive Summary
The site is correctly static-first (`output: 'static'`) and most pages ship near-zero JS. However, 5 of 11 islands use directives stronger than required, one widget uses `client:only` and causes visible layout shift, and a "shared cart count" relies on React context across two separate islands — which silently does not work. Downgrading directives and consolidating the cart island would cut framework JS on the product page roughly in half.

### Rendering Baseline

**Output mode:** `static` (verify config key against current docs)
**Integrations:** `@astrojs/react`, `@astrojs/tailwind`
**Expected JS budget:** content/marketing pages ~0 KB framework runtime; product page = sum of hydrated islands only

| Page type | Static content | Interactive islands | Notes |
|-----------|----------------|---------------------|-------|
| Blog post | 100% | 0 | Ideal — pure HTML |
| Landing | ~95% | 1 (newsletter form) | Acceptable |
| Product | ~70% | 4 (gallery, add-to-cart, reviews, cart badge) | Over-hydrated; see findings |

### Island Inventory

| Component | Framework | Directive | Justification | Assessment |
|-----------|-----------|-----------|---------------|------------|
| `ImageGallery.tsx` | React | `client:load` | Needs swipe + zoom | Downgrade → `client:visible` (below fold) |
| `AddToCart.tsx` | React | `client:load` | Above-fold buy button | Keep |
| `ReviewList.tsx` | React | `client:load` | Lazy-loaded reviews | Downgrade → `client:visible` |
| `CartBadge.tsx` | React | `client:load` | Header count | Keep, but see state bug |
| `NewsletterForm.tsx` | React | `client:load` | Footer signup | Downgrade → `client:visible` |
| `ThemeToggle.tsx` | React | `client:idle` | Theme switch | Correct |
| `LiveSearch.tsx` | React | `client:only` | Typeahead | Causes CLS — see finding |

### Boundary & Granularity Findings

#### Finding 1: `client:only` Search Causes Layout Shift
- **Severity:** High
- **Confidence:** High
- **Location:** `src/components/LiveSearch.tsx` used in `src/layouts/Base.astro`
- **Evidence:**
  ```astro
  ---
  import LiveSearch from '../components/LiveSearch.tsx';
  ---
  <header>
    <LiveSearch client:only="react" />
  </header>
  ```
  Because `client:only` skips SSR, the header search renders blank until React hydrates, shifting the nav.
- **Recommendation:** Render a static input shell server-side, then enhance:
  ```astro
  <header>
    <!-- SSR'd shell keeps layout stable -->
    <LiveSearch client:idle />
  </header>
  ```
  Use `client:only` only if the component genuinely cannot render without browser APIs; otherwise prefer an SSR-able directive. (Verify directive behavior against current docs.)

#### Finding 2: Island Bloat in Product Gallery
- **Severity:** Medium
- **Confidence:** High
- **Location:** `src/components/ImageGallery.tsx`
- **Evidence:** The gallery hydrates the entire product description block because the static copy is passed as children *inside* the hydrated React tree.
- **Recommendation:** Keep static description in `.astro` and scope the island to the carousel only:
  ```astro
  <ImageGallery client:visible images={product.images} />
  <p class="prose">{product.description}</p> <!-- stays static -->
  ```

### Data & Cross-Island State

#### Finding 3: React Context Cannot Cross Islands
- **Severity:** High
- **Confidence:** High
- **Location:** `CartBadge.tsx` (header) and `AddToCart.tsx` (product) both consume a `CartContext`
- **Evidence:** Each `client:*` island is hydrated independently; a React Provider in one island does not wrap the other. The badge never updates when "Add to cart" fires.
- **Recommendation:** Use a framework-agnostic shared store (e.g., a nano-store-style atom) imported by both islands, or consolidate both into one island. Verify the store library name/API against current docs.
  ```ts
  // store/cart.ts  (illustrative)
  import { atom } from 'nanostores'; // verify against current docs
  export const cartCount = atom(0);
  ```

#### Data Fetching
- Product data is correctly fetched in `.astro` frontmatter and passed as serializable props. No client-side refetch detected. Good.

### Prioritized Recommendations

#### Critical (This Week)
| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 1 | Replace `client:only` search with SSR shell + `client:idle` | Removes header CLS | 1 hr |
| 2 | Move cart state to a shared store across islands | Fixes broken badge | 2 hrs |

#### High (This Month)
| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 1 | Downgrade gallery/reviews/newsletter to `client:visible` | Defers ~half product-page JS | 1 hr |
| 2 | Scope gallery island to carousel only | Less hydrated DOM | 1 hr |

#### Patterns to Preserve
- Static-first default with `.astro` components
- Server-side data fetching in frontmatter
- `client:idle` on the theme toggle
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Audit scoped to islands, directives, and partial-hydration tradeoffs.
- **ST-02 (Structured Sequential Instructions):** Baseline → inventory → boundaries → data/state → performance → verification.
- **RT-02 (Multi-Dimensional Analysis Framework):** Evaluates directives, granularity, data flow, and UX impact together.
- **RT-05 (Evidence-Based Reasoning):** Every finding cites the directive/source and the interaction it does or doesn't justify.
- **DS-06 (Prioritization Guidance):** Recommendations ranked by impact and effort with confidence levels.

## Related Prompts

- [frontend_astro_content_collections.md](frontend_astro_content_collections.md) - Type-safe content and build-time data that feeds island props
- [../performance/frontend_performance_core_web_vitals.md](../performance/frontend_performance_core_web_vitals.md) - Measure the JS/CLS impact of hydration choices
- [../react/frontend_react_server_components_streaming.md](../react/frontend_react_server_components_streaming.md) - Compare Astro islands with React server-first rendering
- [../architecture/frontend_state_management_selection.md](../architecture/frontend_state_management_selection.md) - Choose a cross-island shared-state approach
