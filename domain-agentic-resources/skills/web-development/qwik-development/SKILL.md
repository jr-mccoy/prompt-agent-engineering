---
name: qwik-development
description: Master Qwik for building instant-loading web applications with resumability, fine-grained lazy loading, and zero hydration cost. Use this skill when building highly interactive apps requiring instant interactivity, e-commerce sites, dashboards, or when users mention "Qwik", "QwikCity", "resumability", "resumable apps", or "$" dollar sign functions.
metadata:
  tags:
    - development
    - qwik
    - web-development
  updated: "2026-04-11"
---
# Qwik Development

Qwik is a next-generation web framework that achieves instant-on interactivity through resumability - the ability to continue execution on the client from where the server left off, without hydration.

## Purpose

This skill provides comprehensive guidance for building high-performance web applications with Qwik, including resumability patterns, fine-grained lazy loading, QwikCity routing, and server functions. Mastery enables building applications that achieve near-zero JavaScript on initial load while maintaining full interactivity.

## When to Use This Skill

Use this skill when you need to:
- Build highly interactive applications with instant interactivity
- Achieve near-perfect Lighthouse scores (100/100 performance)
- Implement fine-grained lazy loading at the function level
- Use server functions for secure data operations
- Build e-commerce sites with optimal conversion rates
- Create dashboards with complex interactivity
- User mentions: Qwik, QwikCity, resumability, $, useSignal, useStore

## When NOT to Use This Skill

Do NOT use this skill when:
- Building simple static sites → use `astro-development` instead
- Team has deep React/Vue expertise and tight deadline → stick with familiar stack
- Need extensive third-party component ecosystem → React has more options
- Building native mobile apps → use `mobile-development` skills

## Prerequisites

- **Node.js:** v18.17 or higher (v20+ recommended)
- **Package manager:** npm, pnpm, or yarn
- **Text editor:** VS Code with Qwik City extension recommended
- **Knowledge:** JavaScript/TypeScript, basic understanding of reactive programming

**Verify installation:**
```bash
node --version
# Expected: v18.17.0+

# Check existing Qwik project
npx qwik --version
# Expected: qwik@1.x.x
```

---

## Quick Reference

### Most Common Operations

| Task | Command | Notes |
|------|---------|-------|
| Create new project | `npm create qwik@latest` | Interactive setup |
| Start dev server | `npm run dev` | Hot reload at localhost:5173 |
| Build for production | `npm run build` | Outputs to `dist/` |
| Preview production | `npm run preview` | Test production locally |
| Add integration | `npm run qwik add` | Add adapters/features |
| Generate route | `npm run qwik new` | Scaffold new routes |

### Essential Qwik Concepts

| Concept | Symbol | Purpose |
|---------|--------|---------|
| Lazy-load function | `$()` | Marks function for lazy loading |
| Component | `component$()` | Defines lazy-loaded component |
| Signal | `useSignal()` | Reactive primitive value |
| Store | `useStore()` | Reactive object |
| Computed | `useComputed$()` | Derived reactive value |
| Task | `useTask$()` | Side effects |
| Server function | `server$()` | Server-only code |
| Resource | `useResource$()` | Async data loading |

---

## Core Concepts

### Resumability vs Hydration

**Traditional Hydration (React, Vue, Svelte):**
```
Server renders HTML → Client downloads ALL JS →
Re-executes ALL components → Attaches event handlers
= Duplicated work, delayed interactivity
```

**Qwik Resumability:**
```
Server renders HTML + serializes state → Client loads ONLY needed JS →
Resumes from serialized state → No re-execution
= Zero duplicated work, instant interactivity
```

**Key Insight:** Hydration replays application logic. Resumability continues from where the server stopped.

### The Dollar Sign (`$`)

The `$` suffix is Qwik's marker for lazy-loadable boundaries:

```typescript
// This function is lazy-loaded only when needed
const handleClick = $(() => {
  console.log('Clicked!');
});

// This component is lazy-loaded
const MyComponent = component$(() => {
  return <div>Hello</div>;
});
```

**What `$` does:**
1. Creates a lazy-loading boundary
2. Enables code splitting at function level
3. Marks code for serialization
4. Allows Qwik optimizer to extract code

---

## Core Operations

### Operation: Create New Project

**Purpose:** Initialize a new Qwik application

**Command:**
```bash
npm create qwik@latest
```

**Interactive prompts:**
1. Project name
2. Starter template (Basic, Empty, Playground)
3. Install dependencies
4. Initialize git

**Examples:**

Basic app:
```bash
npm create qwik@latest my-app
cd my-app
npm run dev
```

With specific template:
```bash
# Empty starter (minimal)
npm create qwik@latest my-app -- --template empty

# With Express adapter
npm create qwik@latest my-app -- --template express
```

**Project structure:**
```
my-app/
├── public/                 # Static assets
├── src/
│   ├── components/        # Reusable components
│   ├── routes/            # File-based routing
│   │   ├── index.tsx      # Homepage (/)
│   │   ├── layout.tsx     # Root layout
│   │   └── about/
│   │       └── index.tsx  # About page (/about)
│   ├── entry.dev.tsx      # Dev entry point
│   ├── entry.preview.tsx  # Preview entry point
│   ├── entry.ssr.tsx      # SSR entry point
│   ├── global.css         # Global styles
│   └── root.tsx           # Root component
├── adapters/              # Deployment adapters
├── qwik.config.ts         # Qwik configuration
├── vite.config.ts         # Vite configuration
└── tsconfig.json          # TypeScript config
```

---

### Operation: Create Reactive State

**Purpose:** Manage component state with signals and stores

**Signals (primitive values):**
```typescript
import { component$, useSignal } from '@builder.io/qwik';

export default component$(() => {
  // Reactive primitive
  const count = useSignal(0);

  return (
    <div>
      <p>Count: {count.value}</p>
      <button onClick$={() => count.value++}>Increment</button>
    </div>
  );
});
```

**Stores (objects):**
```typescript
import { component$, useStore } from '@builder.io/qwik';

interface User {
  name: string;
  email: string;
  preferences: {
    theme: 'light' | 'dark';
    notifications: boolean;
  };
}

export default component$(() => {
  // Reactive object (deep reactivity)
  const user = useStore<User>({
    name: 'John',
    email: 'john@example.com',
    preferences: {
      theme: 'light',
      notifications: true,
    },
  });

  return (
    <div>
      <p>Name: {user.name}</p>
      <button onClick$={() => {
        user.preferences.theme =
          user.preferences.theme === 'light' ? 'dark' : 'light';
      }}>
        Toggle Theme
      </button>
    </div>
  );
});
```

**Computed values:**
```typescript
import { component$, useSignal, useComputed$ } from '@builder.io/qwik';

export default component$(() => {
  const firstName = useSignal('John');
  const lastName = useSignal('Doe');

  // Derived value (recomputes when dependencies change)
  const fullName = useComputed$(() => {
    return `${firstName.value} ${lastName.value}`;
  });

  return <p>Full name: {fullName.value}</p>;
});
```

**When to use which:**
| Type | Use For | Example |
|------|---------|---------|
| `useSignal` | Primitives | `count`, `isOpen`, `name` |
| `useStore` | Objects/arrays | `user`, `items`, `formData` |
| `useComputed$` | Derived values | `fullName`, `total`, `isValid` |

---

### Operation: Handle Events

**Purpose:** Attach event handlers with lazy loading

**Basic event handling:**
```typescript
import { component$, $ } from '@builder.io/qwik';

export default component$(() => {
  // Inline handler (lazy-loaded)
  return (
    <button onClick$={() => console.log('Clicked!')}>
      Click me
    </button>
  );
});
```

**Named handlers:**
```typescript
import { component$, $ } from '@builder.io/qwik';

export default component$(() => {
  // Extracted for reuse or testing
  const handleClick = $(() => {
    console.log('Clicked!');
  });

  const handleInput = $((event: InputEvent) => {
    const target = event.target as HTMLInputElement;
    console.log('Input:', target.value);
  });

  return (
    <div>
      <button onClick$={handleClick}>Click</button>
      <input onInput$={handleInput} />
    </div>
  );
});
```

**Prevent default:**
```typescript
<form
  preventdefault:submit
  onSubmit$={() => {
    // Form submission without page reload
  }}
>
  <button type="submit">Submit</button>
</form>
```

**Common events:**
| Event | Handler | Notes |
|-------|---------|-------|
| Click | `onClick$` | |
| Input | `onInput$` | Fires on every change |
| Change | `onChange$` | Fires on blur |
| Submit | `onSubmit$` | Use with `preventdefault:submit` |
| Focus | `onFocus$` | |
| Blur | `onBlur$` | |
| Keydown | `onKeyDown$` | |

---

## Side Effects, Server Functions & Data Loading

`useTask$`/`useVisibleTask$` side effects, `server$` functions with request context, `routeAction$` with zod$ validation, and `routeLoader$` for parallel server-side data loading with redirect/error handling.

See [references/side-effects-server-data-loading.md](references/side-effects-server-data-loading.md)

## Routing, Configuration & Troubleshooting

QwikCity file-based routing with dynamic routes and nested layouts, Vite/TypeScript configuration, best practices with examples, troubleshooting table and serialization error resolution, Tailwind/Auth/Forms integration, and version compatibility.

See [references/routing-config-and-troubleshooting.md](references/routing-config-and-troubleshooting.md)

---

## Reference Files

| Resource | Purpose |
|----------|---------|
| `references/side-effects-server-data-loading.md` | Side effects, server functions, and data loading |
| `references/routing-config-and-troubleshooting.md` | Routing, configuration, best practices, troubleshooting |
| `scripts/validate_project.sh` | Validates Qwik project structure |
| `assets/vite.config.example.ts` | Working Vite configuration |
| `assets/component_patterns.md` | Common component patterns |

## Related Skills

- `astro-development` - When content-focused sites suit better
- `react-development` - When team prefers React ecosystem
- `cloudflare-troubleshooting` - When deploying to Cloudflare Workers
