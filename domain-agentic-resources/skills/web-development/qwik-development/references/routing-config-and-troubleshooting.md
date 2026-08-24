# Qwik — Routing, Configuration, Best Practices & Troubleshooting

## Operation: Configure Routing (QwikCity)

**Purpose:** Set up file-based routing with layouts

**Basic routes:**
```
src/routes/
├── index.tsx              → /
├── about/
│   └── index.tsx          → /about
├── blog/
│   ├── index.tsx          → /blog
│   └── [slug]/
│       └── index.tsx      → /blog/:slug
└── products/
    ├── index.tsx          → /products
    └── [...catchall]/
        └── index.tsx      → /products/*
```

**Dynamic routes:**
```typescript
// src/routes/blog/[slug]/index.tsx
import { component$ } from '@builder.io/qwik';
import { routeLoader$ } from '@builder.io/qwik-city';

export const usePost = routeLoader$(async ({ params }) => {
  const slug = params.slug;
  return await getPostBySlug(slug);
});

export default component$(() => {
  const post = usePost();
  return <article>{post.value.content}</article>;
});
```

**Layouts:**
```typescript
// src/routes/layout.tsx (root layout)
import { component$, Slot } from '@builder.io/qwik';

export default component$(() => {
  return (
    <div class="app">
      <header>
        <nav>...</nav>
      </header>
      <main>
        <Slot /> {/* Child routes render here */}
      </main>
      <footer>...</footer>
    </div>
  );
});
```

**Nested layouts:**
```typescript
// src/routes/dashboard/layout.tsx
import { component$, Slot } from '@builder.io/qwik';

export default component$(() => {
  return (
    <div class="dashboard">
      <aside class="sidebar">
        <DashboardNav />
      </aside>
      <section class="content">
        <Slot />
      </section>
    </div>
  );
});
```

---

## Configuration Reference

### Configuration File Location

```bash
# Root of project
vite.config.ts      # Vite + Qwik config
qwik.config.ts      # Qwik-specific (if exists)
```

### Vite Configuration

```typescript
// vite.config.ts
import { defineConfig } from 'vite';
import { qwikVite } from '@builder.io/qwik/optimizer';
import { qwikCity } from '@builder.io/qwik-city/vite';
import tsconfigPaths from 'vite-tsconfig-paths';

export default defineConfig(() => {
  return {
    plugins: [
      qwikCity(),
      qwikVite(),
      tsconfigPaths(),
    ],

    // Dev server
    server: {
      port: 5173,
      host: true,
    },

    // Preview server
    preview: {
      port: 4173,
    },

    // Build options
    build: {
      // Optimize output
      target: 'es2020',
      modulePreload: true,
    },

    // SSR options
    ssr: {
      // Packages to not externalize
      noExternal: ['@some-package'],
    },
  };
});
```

### TypeScript Configuration

```json
// tsconfig.json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ES2020",
    "moduleResolution": "bundler",
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "jsx": "react-jsx",
    "jsxImportSource": "@builder.io/qwik",
    "strict": true,
    "paths": {
      "~/*": ["./src/*"]
    }
  },
  "include": ["src/**/*.ts", "src/**/*.tsx"]
}
```

---

## Best Practices

### Do

- **Use signals for reactive state:** Fine-grained reactivity, optimal performance
  ```typescript
  // Good: Only re-renders what uses this signal
  const count = useSignal(0);
  ```

- **Leverage $ for lazy loading:** Every $ creates a code-splitting point
  ```typescript
  // Good: handleClick only loads when button is clicked
  const handleClick = $(() => {
    doExpensiveOperation();
  });
  ```

- **Use routeLoader$ for data fetching:** Parallel loading, SSR-ready
  ```typescript
  // Good: Data loads on server, no client fetch needed
  export const useData = routeLoader$(async () => {
    return await fetchData();
  });
  ```

- **Prefer server$ for sensitive operations:** Secrets stay on server
  ```typescript
  // Good: API key never reaches client
  const callApi = server$(async () => {
    const key = process.env.API_KEY;
    return fetch(url, { headers: { auth: key } });
  });
  ```

### Don't

- **Don't use useEffect patterns:** Qwik has different mental model
  ```typescript
  // Bad: React pattern doesn't work
  useEffect(() => {
    fetchData();
  }, []);

  // Good: Use routeLoader$ or useTask$
  export const useData = routeLoader$(async () => {
    return await fetchData();
  });
  ```

- **Don't forget $ on callbacks:** Required for lazy loading
  ```typescript
  // Bad: Not lazy-loadable
  <button onClick={() => doSomething()}>

  // Good: Lazy-loadable
  <button onClick$={() => doSomething()}>
  ```

- **Don't access window/document in components directly:** Use useVisibleTask$
  ```typescript
  // Bad: Breaks SSR
  const width = window.innerWidth;

  // Good: Client-only code in useVisibleTask$
  const width = useSignal(0);
  useVisibleTask$(() => {
    width.value = window.innerWidth;
  });
  ```

### Performance Tips

1. **Minimize useVisibleTask$:** Most code can stay server-side
2. **Use track() wisely:** Only track what you need
3. **Leverage prefetching:** QwikCity automatically prefetches on hover
4. **Keep components small:** Smaller components = smaller lazy chunks
5. **Use serialize: 'never' for secrets:** Prevent accidental client exposure

---

## Troubleshooting

### Common Issues

| Symptom | Cause | Solution |
|---------|-------|----------|
| "Cannot use X outside component" | Hook outside component$ | Move hook inside component$ |
| Stale closure | Missing track() in useTask$ | Add track() for dependencies |
| Hydration error | Browser API in component render | Move to useVisibleTask$ |
| "$ required" error | Missing $ on callback | Add $ suffix: `onClick$` |
| Server data not available | Using loader in non-route | Only use routeLoader$ in routes |

### Diagnostic Commands

```bash
# Check for build issues
npm run build

# Verbose build output
DEBUG=true npm run build

# Check bundle sizes
npm run build -- --analyze

# Type checking
npx tsc --noEmit
```

### Issue: Serialization Error

**Symptoms:** Runtime error about non-serializable value

**Quick Diagnosis:**
```typescript
// Check what's in your signals/stores
console.log(JSON.stringify(myStore)); // If this fails, it's not serializable
```

**Root Causes:**
1. Functions in store (not serializable)
2. DOM elements in state
3. Circular references

**Resolution:**
```typescript
// Bad: Function in store
const store = useStore({
  handler: () => {} // Can't serialize
});

// Good: Use $ for functions
const handler = $(() => {});
const store = useStore({
  data: 'value'
});
```

---

## Integration Patterns

### With Tailwind CSS

```bash
npm run qwik add tailwind
```

### With Authentication

```typescript
// src/routes/layout.tsx
import { routeLoader$ } from '@builder.io/qwik-city';

export const useSession = routeLoader$(async ({ cookie }) => {
  const token = cookie.get('session');
  if (!token) return null;
  return await validateSession(token.value);
});

// In any component
const session = useSession();
if (!session.value) {
  return <LoginPrompt />;
}
```

### With Forms (Modular Forms)

```bash
npm install @modular-forms/qwik
```

```typescript
import { useForm } from '@modular-forms/qwik';

const [loginForm, { Form, Field }] = useForm<LoginForm>({
  loader: useFormLoader(),
});
```

---

## Version Compatibility

| Version | Status | Notable Changes |
|---------|--------|-----------------|
| v1.x | Current | Stable API, production ready |
| v0.x | Deprecated | Breaking changes from v1 |
