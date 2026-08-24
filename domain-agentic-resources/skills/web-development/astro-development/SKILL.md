---
name: astro-development
description: Master Astro for building fast, content-focused web applications with islands architecture, multi-framework integration, and optimal performance. Use this skill when building static sites, content-heavy websites, documentation, blogs, marketing pages, or when users mention "Astro", "islands architecture", "partial hydration", "content collections", or "static site generator".
metadata:
  tags:
    - astro
    - development
    - performance
    - web-development
  updated: "2026-04-11"
---
# Astro Development

Astro is a modern web framework for building fast, content-focused websites using an islands architecture that ships zero JavaScript by default, hydrating only interactive components.

## Purpose

This skill provides comprehensive guidance for building high-performance websites with Astro, including islands architecture patterns, multi-framework component integration, content collections, and deployment optimization. Mastery enables building sites that are 40% faster than traditional SPA frameworks while maintaining rich interactivity where needed.

## When to Use This Skill

Use this skill when you need to:
- Build content-focused websites (blogs, docs, marketing, portfolios)
- Implement islands architecture for optimal performance
- Integrate multiple UI frameworks (React, Vue, Svelte, Solid) in one project
- Set up type-safe content collections with MDX
- Configure SSR vs SSG output modes
- Implement View Transitions for smooth page navigation
- Optimize Core Web Vitals scores
- User mentions: Astro, astro.build, islands architecture, partial hydration, content collections

## When NOT to Use This Skill

Do NOT use this skill when:
- Building highly interactive SPA applications → use `react-development` or `vue-development`
- Need real-time features with WebSockets → consider SvelteKit or Next.js
- Building native mobile apps → use `mobile-development` skills
- Simple static HTML without build step → plain HTML/CSS suffices

## Prerequisites

- **Node.js:** v18.17.1 or v20.3.0 or higher (v19 not supported)
- **Package manager:** npm, pnpm, or yarn
- **Text editor:** VS Code with Astro extension recommended
- **Knowledge:** Basic HTML, CSS, JavaScript; familiarity with component-based frameworks helpful

**Verify installation:**
```bash
node --version
# Expected: v18.17.1+ or v20.3.0+

npm create astro@latest --version
# Or check existing project:
npx astro --version
# Expected: astro@4.x.x
```

---

## Quick Reference

### Most Common Operations

| Task | Command | Notes |
|------|---------|-------|
| Create new project | `npm create astro@latest` | Interactive setup wizard |
| Start dev server | `npm run dev` | Hot reload at localhost:4321 |
| Build for production | `npm run build` | Outputs to `dist/` |
| Preview production build | `npm run preview` | Test production build locally |
| Add integration | `npx astro add react` | Auto-configures framework |
| Check for issues | `npx astro check` | TypeScript validation |
| Sync content schemas | `npx astro sync` | Generate content types |

### Essential CLI Flags

| Flag | Purpose | Example |
|------|---------|---------|
| `--host` | Expose to network | `npm run dev -- --host` |
| `--port` | Custom port | `npm run dev -- --port 3000` |
| `--open` | Open browser on start | `npm run dev -- --open` |
| `--config` | Custom config file | `astro build --config ./my.config.mjs` |

---

## Core Operations

### Operation: Create New Project

**Purpose:** Initialize a new Astro project with optimal defaults

**Command:**
```bash
npm create astro@latest [project-name]
```

**Parameters:**
| Parameter | Required | Description | Default |
|-----------|----------|-------------|---------|
| `project-name` | No | Directory name for project | Prompts interactively |
| `--template` | No | Starter template to use | `basics` |
| `--typescript` | No | TypeScript strictness | `strict` |
| `--install` | No | Auto-install dependencies | Prompts |
| `--git` | No | Initialize git repo | Prompts |

**Examples:**

Basic project:
```bash
npm create astro@latest my-site
```

With specific template:
```bash
npm create astro@latest my-blog -- --template blog
npm create astro@latest my-docs -- --template starlight
npm create astro@latest my-portfolio -- --template portfolio
```

Non-interactive setup:
```bash
npm create astro@latest my-site -- --template basics --typescript strict --install --git
```

**Available Templates:**
| Template | Use Case |
|----------|----------|
| `basics` | Minimal starter |
| `blog` | Blog with MDX support |
| `docs` | Documentation (Starlight) |
| `portfolio` | Personal portfolio |
| `minimal` | Bare minimum |

---

### Operation: Add Framework Integration

**Purpose:** Add UI framework support (React, Vue, Svelte, Solid, Preact, Alpine, Lit)

**Command:**
```bash
npx astro add [integration]
```

**Parameters:**
| Parameter | Required | Description | Default |
|-----------|----------|-------------|---------|
| `integration` | Yes | Framework name | - |
| `--yes` | No | Skip confirmation prompts | `false` |

**Examples:**

Add React:
```bash
npx astro add react
```

Add multiple frameworks:
```bash
npx astro add react vue svelte
```

Add Tailwind CSS:
```bash
npx astro add tailwind
```

Add SSR adapter:
```bash
npx astro add vercel
npx astro add netlify
npx astro add cloudflare
npx astro add node
```

**What it does:**
1. Installs required npm packages
2. Updates `astro.config.mjs` with integration
3. Adds TypeScript definitions if needed

---

### Operation: Create Content Collection

**Purpose:** Set up type-safe content with schema validation

**Command/Setup:**

1. Create content directory:
```bash
mkdir -p src/content/blog
```

2. Define schema in `src/content/config.ts`:
```typescript
import { defineCollection, z } from 'astro:content';

const blog = defineCollection({
  type: 'content', // 'content' for Markdown/MDX, 'data' for JSON/YAML
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
    heroImage: z.string().optional(),
    draft: z.boolean().default(false),
    tags: z.array(z.string()).default([]),
  }),
});

export const collections = { blog };
```

3. Add content files:
```markdown
---
title: "My First Post"
description: "Learn about Astro"
pubDate: 2024-01-15
tags: ["astro", "web"]
---

# My First Post

Content here...
```

4. Query content in pages:
```astro
---
import { getCollection } from 'astro:content';

const posts = await getCollection('blog', ({ data }) => {
  return data.draft !== true; // Filter out drafts
});

const sortedPosts = posts.sort(
  (a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf()
);
---

<ul>
  {sortedPosts.map((post) => (
    <li>
      <a href={`/blog/${post.slug}`}>{post.data.title}</a>
      <time datetime={post.data.pubDate.toISOString()}>
        {post.data.pubDate.toLocaleDateString()}
      </time>
    </li>
  ))}
</ul>
```

**Common errors:**
| Error | Cause | Fix |
|-------|-------|-----|
| `Cannot find module 'astro:content'` | Types not synced | Run `npx astro sync` |
| Schema validation failed | Frontmatter doesn't match schema | Check required fields |

---

### Operation: Implement Islands Architecture

**Purpose:** Add client-side interactivity with selective hydration

**Hydration Directives:**

| Directive | When Hydrates | Use Case |
|-----------|---------------|----------|
| `client:load` | Immediately on page load | Critical interactive elements |
| `client:idle` | After page becomes idle | Lower priority interactivity |
| `client:visible` | When enters viewport | Below-the-fold content |
| `client:media` | When media query matches | Responsive interactivity |
| `client:only` | Client only, no SSR | Browser-only APIs |

**Examples:**

React component with immediate hydration:
```astro
---
import Counter from '../components/Counter.jsx';
---

<Counter client:load initialCount={0} />
```

Vue component when visible:
```astro
---
import Gallery from '../components/Gallery.vue';
---

<Gallery client:visible images={images} />
```

Mobile-only interaction:
```astro
---
import MobileMenu from '../components/MobileMenu.svelte';
---

<MobileMenu client:media="(max-width: 768px)" />
```

Framework-specific rendering (no SSR):
```astro
---
// Component uses browser APIs like localStorage
import ThemePicker from '../components/ThemePicker.jsx';
---

<ThemePicker client:only="react" />
```

**Best Practices:**
1. Default to no hydration (static) when possible
2. Use `client:visible` for below-fold content
3. Use `client:idle` for non-critical interactivity
4. Reserve `client:load` for immediately needed interactions

---

## Output Mode, Configuration, Best Practices & Integration

SSG/SSR/hybrid output mode configuration with per-page `prerender` overrides, View Transitions with lifecycle events, full `astro.config.mjs` reference, best practices with code examples, troubleshooting table with hydration mismatch resolution, and React/Tailwind/MDX/deployment integration patterns.

See [references/output-config-and-integration.md](references/output-config-and-integration.md)

---

## Reference Files

| Resource | Purpose |
|----------|---------|
| `references/output-config-and-integration.md` | Output mode, view transitions, config, best practices, troubleshooting |
| `scripts/validate_project.sh` | Validates Astro project structure |
| `scripts/migrate_to_v4.sh` | Migration helper for v3 to v4 |
| `assets/astro.config.example.mjs` | Working configuration example |
| `assets/content_schema.example.ts` | Content collection schema examples |

## Related Skills

- `react-development` - When building React-heavy SPAs instead of content sites
- `vue-development` - When using Vue as primary framework
- `cloudflare-troubleshooting` - When deploying to Cloudflare Pages
- `ui-designer` - When extracting design systems for Astro components
