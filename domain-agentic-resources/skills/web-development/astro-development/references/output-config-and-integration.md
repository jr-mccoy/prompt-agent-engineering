# Astro — Output Mode, View Transitions, Configuration & Integration

## Operation: Configure Output Mode (SSG/SSR/Hybrid)

**Purpose:** Set rendering strategy for the site

**Configuration:**

Static Site Generation (default):
```javascript
// astro.config.mjs
export default defineConfig({
  output: 'static', // Pre-render all pages at build time
});
```

Server-Side Rendering:
```javascript
// astro.config.mjs
import vercel from '@astrojs/vercel/serverless';

export default defineConfig({
  output: 'server', // Render pages on-demand
  adapter: vercel(),
});
```

Hybrid (recommended for most sites):
```javascript
// astro.config.mjs
import vercel from '@astrojs/vercel/serverless';

export default defineConfig({
  output: 'hybrid', // Static by default, opt-in to SSR
  adapter: vercel(),
});
```

**Per-page configuration:**

Force static in hybrid mode:
```astro
---
export const prerender = true; // Pre-render at build time
---
```

Force SSR in hybrid mode:
```astro
---
export const prerender = false; // Render on each request
---
```

**Decision Guide:**

| Requirement | Recommended Mode |
|-------------|------------------|
| Blog, docs, marketing | `static` |
| User authentication | `server` or `hybrid` |
| Dynamic personalization | `server` |
| Mix of static + dynamic | `hybrid` |
| Highest performance | `static` |
| Fresh data on every request | `server` |

---

## Operation: Implement View Transitions

**Purpose:** Add smooth page transitions for SPA-like navigation

**Setup:**

1. Add ViewTransitions component to layout:
```astro
---
// src/layouts/Layout.astro
import { ViewTransitions } from 'astro:transitions';
---

<html lang="en">
  <head>
    <ViewTransitions />
  </head>
  <body>
    <slot />
  </body>
</html>
```

2. Add transition animations:
```astro
---
import { fade, slide } from 'astro:transitions';
---

<!-- Fade transition -->
<div transition:animate={fade({ duration: '0.4s' })}>
  Content
</div>

<!-- Slide transition -->
<aside transition:animate={slide({ duration: '0.3s' })}>
  Sidebar
</aside>

<!-- Persist element across pages -->
<video transition:persist id="hero-video" autoplay muted>
  <source src="/video.mp4" type="video/mp4" />
</video>
```

3. Name transitions for paired animations:
```astro
<!-- On list page -->
<img transition:name={`hero-${post.slug}`} src={post.heroImage} />

<!-- On detail page -->
<img transition:name={`hero-${post.slug}`} src={post.data.heroImage} />
```

**Lifecycle events:**
```javascript
document.addEventListener('astro:page-load', () => {
  // Runs on every page load (initial + navigation)
});

document.addEventListener('astro:before-preparation', () => {
  // Before new page is fetched
});

document.addEventListener('astro:after-swap', () => {
  // After DOM is updated, before new page renders
});
```

---

## Configuration Reference

### Configuration File Location

```bash
# Root of project
astro.config.mjs  # or .ts
```

### Configuration Structure

```javascript
// astro.config.mjs
import { defineConfig } from 'astro/config';
import react from '@astrojs/react';
import tailwind from '@astrojs/tailwind';
import vercel from '@astrojs/vercel/serverless';

export default defineConfig({
  // Site URL (required for sitemap, canonical URLs)
  site: 'https://example.com',

  // Base path if not at root
  base: '/docs',

  // Output mode: 'static' | 'server' | 'hybrid'
  output: 'hybrid',

  // Deployment adapter
  adapter: vercel(),

  // Framework integrations
  integrations: [
    react(),
    tailwind({
      applyBaseStyles: false,
    }),
  ],

  // Vite configuration
  vite: {
    plugins: [],
    ssr: {
      noExternal: ['package-name'],
    },
  },

  // Markdown configuration
  markdown: {
    syntaxHighlight: 'shiki',
    shikiConfig: {
      theme: 'github-dark',
    },
    remarkPlugins: [],
    rehypePlugins: [],
  },

  // Dev server configuration
  server: {
    port: 4321,
    host: true,
  },

  // Build configuration
  build: {
    inlineStylesheets: 'auto',
  },

  // Redirects
  redirects: {
    '/old-page': '/new-page',
    '/blog/[...slug]': '/articles/[...slug]',
  },

  // Experimental features
  experimental: {
    contentCollectionCache: true,
  },
});
```

### Essential Configuration Options

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `site` | string | - | Production URL for sitemap, canonical |
| `base` | string | `/` | Base path for deployment |
| `output` | string | `static` | Rendering mode |
| `adapter` | object | - | SSR deployment adapter |
| `integrations` | array | `[]` | Framework/tool integrations |
| `trailingSlash` | string | `ignore` | URL trailing slash handling |
| `compressHTML` | boolean | `true` | Minify HTML output |

---

## Best Practices

### Do

- **Ship zero JS by default:** Only add `client:*` directives when interactivity is essential
  ```astro
  <!-- Good: Static by default -->
  <Header />
  <Footer />

  <!-- Good: Only hydrate what needs interaction -->
  <SearchBar client:idle />
  ```

- **Use content collections for structured data:** Type-safe querying with validation
  ```typescript
  // Good: Validated, type-safe content
  const posts = await getCollection('blog');
  ```

- **Leverage `client:visible` for below-fold content:** Reduces initial JS bundle
  ```astro
  <!-- Good: Only loads when scrolled into view -->
  <Comments client:visible postId={post.id} />
  ```

- **Use hybrid mode for mixed requirements:** Static by default, SSR when needed
  ```javascript
  // Good: Best of both worlds
  output: 'hybrid',
  ```

### Don't

- **Don't use `client:load` everywhere:** Defeats the purpose of islands architecture
  ```astro
  <!-- Bad: Loads all JS immediately -->
  <Header client:load />
  <Footer client:load />
  <Sidebar client:load />

  <!-- Better: No hydration for static components -->
  <Header />
  <Footer />
  <Sidebar />
  ```

- **Don't mix multiple frameworks unnecessarily:** Increases bundle size
  ```astro
  <!-- Bad: Three frameworks for one page -->
  <ReactNav client:load />
  <VueContent client:idle />
  <SvelteFooter client:visible />

  <!-- Better: Stick to one framework per project when possible -->
  <ReactNav client:load />
  <ReactContent client:idle />
  <ReactFooter />  <!-- No hydration needed -->
  ```

- **Don't skip content collection schemas:** Lose type safety and validation

### Performance Tips

1. **Minimize client directives:** Each hydrated island adds JS weight
2. **Use `client:visible` over `client:idle`:** Better for CLS and INP
3. **Inline critical CSS:** Use `<style is:inline>` for above-fold styles
4. **Optimize images:** Use `@astrojs/image` or `<Image />` component
5. **Enable content collection cache:** Set `experimental.contentCollectionCache: true`

---

## Troubleshooting

### Common Issues

| Symptom | Cause | Solution |
|---------|-------|----------|
| Component not interactive | Missing `client:*` directive | Add appropriate hydration directive |
| TypeScript errors in content | Types not synced | Run `npx astro sync` |
| Build fails with framework error | Missing integration | Run `npx astro add <framework>` |
| Styles not applying | CSS scope issues | Use `:global()` or `is:global` |
| 404 in production | Trailing slash mismatch | Configure `trailingSlash` option |
| Hydration mismatch | Server/client render differs | Check for browser-only code |

### Diagnostic Commands

```bash
# Check for TypeScript issues
npx astro check

# Sync content types
npx astro sync

# Build with verbose output
npx astro build --verbose

# Check Astro version
npx astro --version
```

### Issue: Hydration Mismatch

**Symptoms:** Console warning about hydration mismatch, flickering UI

**Quick Diagnosis:**
```bash
# Check for browser-only APIs used during SSR
grep -r "window\." src/components/
grep -r "document\." src/components/
grep -r "localStorage" src/components/
```

**Root Causes:**
1. Using browser APIs without guards
2. Random values generated differently on server/client
3. Date/time formatting differences

**Resolution:**
```typescript
// Wrap browser-only code
if (typeof window !== 'undefined') {
  // Browser-only code
}

// Or use client:only for browser-only components
<BrowserOnlyComponent client:only="react" />
```

---

## Integration Patterns

### With React

```bash
npx astro add react
```

```astro
---
import Counter from '../components/Counter.jsx';
---

<Counter client:load />
```

### With Tailwind CSS

```bash
npx astro add tailwind
```

```astro
<div class="bg-slate-900 text-white p-4 rounded-lg">
  Styled with Tailwind
</div>
```

### With MDX

```bash
npx astro add mdx
```

```mdx
---
title: "My MDX Post"
---

import Chart from '../components/Chart.jsx';

# Hello from MDX

<Chart client:visible data={chartData} />
```

### With Deployment Platforms

```bash
# Vercel
npx astro add vercel

# Netlify
npx astro add netlify

# Cloudflare Pages
npx astro add cloudflare
```

---

## Version Compatibility

| Version | Status | Notable Changes |
|---------|--------|-----------------|
| v4.x | Current | Content collections v2, View Transitions stable |
| v3.x | Supported | View Transitions experimental, Image component |
| v2.x | Deprecated | Content collections v1, hybrid mode introduced |
