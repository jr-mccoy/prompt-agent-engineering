# Islands Architecture Patterns

Deep dive into Astro's islands architecture for optimal performance.

## Core Concepts

### What is Islands Architecture?

Islands architecture treats interactive components as isolated "islands" in a sea of static HTML. Each island hydrates independently, enabling:

- **Zero JS by default:** Static HTML ships with no JavaScript
- **Selective hydration:** Only interactive parts load JS
- **Framework agnostic:** Mix React, Vue, Svelte in one page
- **Progressive enhancement:** Site works without JS

### The Hydration Spectrum

```
┌─────────────────────────────────────────────────────────────────┐
│                    HYDRATION STRATEGIES                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  NO HYDRATION          PROGRESSIVE           IMMEDIATE          │
│  (Static HTML)         HYDRATION             HYDRATION          │
│                                                                 │
│  ┌───────┐            ┌───────┐              ┌───────┐          │
│  │       │            │       │              │       │          │
│  │ <Nav> │  ────────► │client:│  ────────►   │client:│          │
│  │       │            │visible│              │load   │          │
│  └───────┘            └───────┘              └───────┘          │
│                                                                 │
│  Zero JS               JS when                JS on             │
│  Fastest               needed                 page load         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Hydration Directives Reference

### `client:load`
Hydrates immediately on page load.

```astro
<AuthButton client:load />
```

**Use when:**
- Component needs instant interactivity
- Above-the-fold interactive elements
- Critical user interactions (auth, cart)

**Avoid when:**
- Component is below the fold
- Interactivity isn't immediately needed
- Component can work without JS initially

### `client:idle`
Hydrates after page becomes idle (using `requestIdleCallback`).

```astro
<Newsletter client:idle />
```

**Use when:**
- Important but not critical interactivity
- Above-the-fold, non-urgent interactions
- Components that enhance but don't block usage

**Avoid when:**
- User might interact immediately
- Component handles critical functionality

### `client:visible`
Hydrates when component enters the viewport.

```astro
<Comments client:visible />
<RelatedPosts client:visible />
```

**Use when:**
- Below-the-fold content
- Heavy components (charts, maps)
- Content users may never scroll to

**This is often the best choice** for most interactive components.

### `client:media`
Hydrates when a media query matches.

```astro
<MobileMenu client:media="(max-width: 768px)" />
<DesktopSidebar client:media="(min-width: 769px)" />
```

**Use when:**
- Responsive interactivity
- Device-specific features
- Reducing mobile/desktop JS bloat

### `client:only`
Skips server rendering, hydrates only on client.

```astro
<ThirdPartyWidget client:only="react" />
<BrowserOnlyChart client:only="svelte" />
```

**Use when:**
- Component uses browser-only APIs
- Third-party widgets that don't SSR well
- Components with hydration issues

**Requires framework specification:** `"react"`, `"vue"`, `"svelte"`, etc.

## Pattern Library

### Pattern 1: Shell Pattern

Static shell with interactive core.

```astro
---
// Layout: entirely static
import Header from './Header.astro';
import Footer from './Footer.astro';
import InteractiveContent from './InteractiveContent.jsx';
---

<Header />  <!-- No client directive = static -->
<main>
  <InteractiveContent client:load />
</main>
<Footer />  <!-- No client directive = static -->
```

**Benefit:** Instant perceived load, interaction ready quickly.

### Pattern 2: Progressive Islands

Layer hydration by importance.

```astro
---
import CriticalCTA from './CriticalCTA.jsx';
import SecondaryNav from './SecondaryNav.jsx';
import Comments from './Comments.jsx';
import RelatedPosts from './RelatedPosts.jsx';
---

<!-- Critical: hydrate immediately -->
<CriticalCTA client:load />

<!-- Important: hydrate when browser is idle -->
<SecondaryNav client:idle />

<!-- Below fold: hydrate when visible -->
<Comments client:visible />
<RelatedPosts client:visible />
```

**Benefit:** Prioritizes critical interactivity, defers the rest.

### Pattern 3: Framework Boundaries

Use frameworks strategically.

```astro
---
// Static Astro components
import StaticHero from './Hero.astro';
import StaticFeatures from './Features.astro';

// Interactive React island
import PricingCalculator from './PricingCalculator.jsx';
---

<StaticHero />
<StaticFeatures />
<PricingCalculator client:visible />  <!-- Only this loads React -->
```

**Benefit:** React only loads for the calculator, not the whole page.

### Pattern 4: Shared State Islands

Multiple islands sharing state.

```astro
---
import CartIcon from './CartIcon.jsx';
import ProductGrid from './ProductGrid.jsx';
import CartDrawer from './CartDrawer.jsx';
// Use nanostores for cross-island state
---

<CartIcon client:load />
<ProductGrid client:visible />
<CartDrawer client:idle />
```

```javascript
// src/stores/cart.js
import { atom } from 'nanostores';

export const $cart = atom([]);

export function addToCart(item) {
  $cart.set([...$cart.get(), item]);
}
```

**Benefit:** Islands communicate without framework overhead.

### Pattern 5: Conditional Islands

Render islands based on data.

```astro
---
import { getCollection } from 'astro:content';
import Comments from './Comments.jsx';

const post = Astro.props.post;
const hasComments = post.data.enableComments;
---

<article>
  <Content />
</article>

{hasComments && <Comments client:visible postId={post.id} />}
```

**Benefit:** Only loads comment system when enabled.

## Anti-Patterns

### Anti-Pattern 1: Over-Hydration

```astro
<!-- BAD: Everything hydrates -->
<Header client:load />
<Nav client:load />
<Sidebar client:load />
<Content client:load />
<Footer client:load />
```

**Fix:** Default to no hydration, add selectively:
```astro
<!-- GOOD: Only interactive parts hydrate -->
<Header />  <!-- Static -->
<Nav />  <!-- Static -->
<Sidebar />  <!-- Static -->
<InteractiveWidget client:idle />  <!-- Interactive -->
<Footer />  <!-- Static -->
```

### Anti-Pattern 2: Wrong Directive

```astro
<!-- BAD: Comments hydrate immediately but are below fold -->
<Comments client:load />
```

**Fix:** Use visibility-based hydration:
```astro
<!-- GOOD: Only hydrates when scrolled to -->
<Comments client:visible />
```

### Anti-Pattern 3: Framework Mixing Without Purpose

```astro
<!-- BAD: Three frameworks, one page -->
<ReactHeader client:load />
<VueContent client:idle />
<SvelteFooter client:visible />
```

**Fix:** Stick to one framework unless there's a specific need:
```astro
<!-- GOOD: Consistent framework -->
<Header />  <!-- Astro, static -->
<ReactContent client:idle />
<Footer />  <!-- Astro, static -->
```

## Performance Metrics

### Measuring Island Performance

```javascript
// Track hydration timing
if (typeof window !== 'undefined') {
  const observer = new PerformanceObserver((list) => {
    for (const entry of list.getEntries()) {
      console.log(`${entry.name}: ${entry.duration}ms`);
    }
  });
  observer.observe({ entryTypes: ['measure'] });
}
```

### Expected Improvements

| Metric | Traditional SPA | Islands Architecture |
|--------|-----------------|---------------------|
| FCP | 1.5-3s | 0.5-1s |
| LCP | 2-4s | 0.8-1.5s |
| TTI | 3-6s | 1-2s |
| Total JS | 200-500KB | 20-100KB |

## Decision Matrix

| Scenario | Recommended Directive |
|----------|----------------------|
| Navigation menu (mobile) | `client:media="(max-width: 768px)"` |
| Search autocomplete | `client:idle` |
| Image carousel (hero) | `client:load` |
| Comments section | `client:visible` |
| Share buttons | `client:visible` |
| Authentication UI | `client:load` |
| Charts/graphs | `client:visible` |
| Form validation | `client:idle` |
| Third-party embed | `client:only` |
| Static content | No directive |
