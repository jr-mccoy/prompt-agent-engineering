---
name: solid-development
description: Master SolidJS for building high-performance reactive web applications with fine-grained reactivity, no virtual DOM, and minimal overhead. Use this skill when building highly interactive applications, real-time dashboards, or when users mention "Solid", "SolidJS", "SolidStart", "createSignal", "createStore", "fine-grained reactivity", or "no virtual DOM".
metadata:
  tags:
    - development
    - performance
    - solid
    - web-development
  updated: "2026-04-11"
---
# SolidJS Development

SolidJS is a declarative JavaScript library for building user interfaces that combines the best of React's developer experience with true fine-grained reactivity and no virtual DOM overhead.

## Purpose

This skill provides comprehensive guidance for building high-performance web applications with SolidJS, including reactive primitives, store patterns, component composition, and SolidStart full-stack development. Mastery enables building applications with React-like syntax but with significantly better runtime performance.

## When to Use This Skill

Use this skill when you need to:
- Build highly interactive applications requiring fine-grained updates
- Achieve optimal performance without virtual DOM reconciliation
- Create real-time dashboards with frequent data updates
- Build applications where bundle size matters (smaller than React)
- Implement complex reactive data flows
- User mentions: Solid, SolidJS, SolidStart, createSignal, createStore, fine-grained reactivity

## When NOT to Use This Skill

Do NOT use this skill when:
- Team has deep React expertise and tight deadline → stick with React
- Need extensive third-party component ecosystem → React has more options
- Building content-heavy static sites → use `astro-development` instead
- Require React Native for mobile → Solid is web-only
- Need server components like Next.js → consider `qwik-development` or React

## Prerequisites

- **Node.js:** v18 or higher (v20+ recommended)
- **Package manager:** npm, pnpm, or yarn
- **Text editor:** VS Code with Solid extension recommended
- **Knowledge:** JavaScript/TypeScript, familiarity with reactive programming concepts

**Verify installation:**
```bash
node --version
# Expected: v18.0.0+

# Check existing Solid project
npm list solid-js
# Expected: solid-js@1.x.x
```

---

## Quick Reference

### Most Common Operations

| Task | Command | Notes |
|------|---------|-------|
| Create new project | `npm create solid@latest` | Interactive setup |
| Create SolidStart app | `npm create solid@latest -- --template bare` then add start | Full-stack |
| Start dev server | `npm run dev` | Hot reload at localhost:3000 |
| Build for production | `npm run build` | Outputs to `dist/` |
| Run tests | `npm run test` | Vitest integration |

### Essential Solid Concepts

| Concept | Function | Purpose |
|---------|----------|---------|
| Signal | `createSignal()` | Reactive primitive value |
| Memo | `createMemo()` | Derived/computed value |
| Effect | `createEffect()` | Side effects on signal changes |
| Store | `createStore()` | Reactive nested object |
| Resource | `createResource()` | Async data fetching |
| Context | `createContext()` | Dependency injection |

---

## Core Concepts

### Fine-Grained Reactivity vs Virtual DOM

**React (Virtual DOM):**
```
State changes → Re-render component tree →
Diff virtual DOM → Patch real DOM
= Extra work, potential unnecessary re-renders
```

**Solid (Fine-Grained Reactivity):**
```
Signal changes → Update only subscribed DOM nodes
= No intermediate step, surgical updates
```

**Key Insight:** In Solid, components only run once. Updates bypass components entirely and go straight to the DOM.

### Signals - The Foundation

Signals are the core reactive primitive:

```typescript
import { createSignal } from 'solid-js';

const [count, setCount] = createSignal(0);

// Reading
console.log(count()); // 0 - signals are functions

// Writing
setCount(1);
setCount(prev => prev + 1);
```

**Critical Difference from React:**
```typescript
// React - hooks re-run on every render
const [count, setCount] = useState(0);
return <div>{count}</div>;

// Solid - component body runs ONCE
const [count, setCount] = createSignal(0);
return <div>{count()}</div>; // count() creates subscription
```

---

## Core Operations

### Operation: Create New Project

**Purpose:** Initialize a new SolidJS application

**Command:**
```bash
npm create solid@latest my-app
```

**Interactive prompts:**
1. Project name
2. TypeScript (Yes/No)
3. Template (basic, ts, ts-vitest, ts-router, etc.)

**Examples:**

Basic TypeScript app:
```bash
npm create solid@latest my-app -- --template ts
cd my-app
npm install
npm run dev
```

With router:
```bash
npm create solid@latest my-app -- --template ts-router
```

**Project structure:**
```
my-app/
├── public/
│   └── favicon.ico
├── src/
│   ├── App.tsx           # Root component
│   ├── App.module.css    # CSS Modules
│   └── index.tsx         # Entry point
├── index.html            # HTML template
├── package.json
├── tsconfig.json
├── vite.config.ts        # Vite configuration
└── vitest.config.ts      # Test configuration
```

---

### Operation: Create Reactive State

**Purpose:** Manage component state with signals and stores

**Signals (primitive values):**
```typescript
import { createSignal } from 'solid-js';

function Counter() {
  const [count, setCount] = createSignal(0);

  return (
    <div>
      <p>Count: {count()}</p>
      <button onClick={() => setCount(c => c + 1)}>Increment</button>
    </div>
  );
}
```

**Stores (nested objects):**
```typescript
import { createStore } from 'solid-js/store';

interface User {
  name: string;
  email: string;
  preferences: {
    theme: 'light' | 'dark';
    notifications: boolean;
  };
}

function UserProfile() {
  const [user, setUser] = createStore<User>({
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
      <button onClick={() =>
        setUser('preferences', 'theme',
          t => t === 'light' ? 'dark' : 'light')
      }>
        Toggle Theme
      </button>
    </div>
  );
}
```

**Memos (derived values):**
```typescript
import { createSignal, createMemo } from 'solid-js';

function FullName() {
  const [firstName, setFirstName] = createSignal('John');
  const [lastName, setLastName] = createSignal('Doe');

  // Recomputes only when dependencies change
  const fullName = createMemo(() => {
    return `${firstName()} ${lastName()}`;
  });

  return <p>Full name: {fullName()}</p>;
}
```

**When to use which:**
| Type | Use For | Example |
|------|---------|---------|
| `createSignal` | Primitives, simple values | `count`, `isOpen`, `name` |
| `createStore` | Nested objects/arrays | `user`, `items`, `formData` |
| `createMemo` | Expensive derived values | `filteredList`, `total`, `isValid` |

---

### Operation: Handle Side Effects

**Purpose:** Run code in response to signal changes

**createEffect (tracks automatically):**
```typescript
import { createSignal, createEffect } from 'solid-js';

function SearchComponent() {
  const [query, setQuery] = createSignal('');
  const [results, setResults] = createSignal([]);

  // Runs whenever query() changes
  createEffect(async () => {
    if (query().length > 2) {
      const response = await fetch(`/api/search?q=${query()}`);
      setResults(await response.json());
    }
  });

  return (
    <div>
      <input
        value={query()}
        onInput={(e) => setQuery(e.currentTarget.value)}
      />
      <ul>
        <For each={results()}>
          {(result) => <li>{result.name}</li>}
        </For>
      </ul>
    </div>
  );
}
```

**onMount and onCleanup:**
```typescript
import { onMount, onCleanup } from 'solid-js';

function Timer() {
  const [time, setTime] = createSignal(0);

  onMount(() => {
    // Runs once when component mounts
    console.log('Component mounted');
  });

  // Effect with cleanup
  createEffect(() => {
    const interval = setInterval(() => {
      setTime(t => t + 1);
    }, 1000);

    onCleanup(() => {
      clearInterval(interval);
    });
  });

  return <p>Time: {time()}</p>;
}
```

**on() for explicit dependencies:**
```typescript
import { createSignal, createEffect, on } from 'solid-js';

function ExplicitDeps() {
  const [a, setA] = createSignal(1);
  const [b, setB] = createSignal(2);

  // Only tracks 'a', ignores 'b' reads inside
  createEffect(on(a, (aValue) => {
    console.log('a changed to:', aValue);
    console.log('b is:', b()); // Not tracked
  }));

  // Track multiple signals
  createEffect(on([a, b], ([aVal, bVal]) => {
    console.log('a or b changed:', aVal, bVal);
  }));
}
```

---

## Data Fetching, Components, Configuration & Best Practices

`createResource` with Suspense and mutate/refetch, control flow components (Show/For/Index/Switch/Match), component patterns (ParentComponent/splitProps/mergeProps/createContext), Vite/TypeScript configuration, best practices with code examples, troubleshooting, and integration patterns.

See [references/data-fetching-components-and-config.md](references/data-fetching-components-and-config.md)

---

## Reference Files

| Resource | Purpose |
|----------|---------|
| `references/data-fetching-components-and-config.md` | Data fetching, components, config, best practices, integration |
| `assets/vite.config.example.ts` | Working Vite configuration |
| `assets/component_patterns.md` | Common component patterns |

## Related Skills

- `qwik-development` - When resumability is priority
- `astro-development` - When content-focused sites suit better
- `react-development` - When ecosystem matters more than performance
