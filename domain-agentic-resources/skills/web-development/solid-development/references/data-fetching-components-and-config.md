# SolidJS — Data Fetching, Components, Configuration & Best Practices

## Operation: Data Fetching with Resources

**Purpose:** Handle async data loading with built-in states

**Basic resource:**
```typescript
import { createResource, Suspense } from 'solid-js';

async function fetchUser(id: string) {
  const response = await fetch(`/api/users/${id}`);
  return response.json();
}

function UserProfile(props: { userId: string }) {
  const [user] = createResource(() => props.userId, fetchUser);

  return (
    <Suspense fallback={<p>Loading...</p>}>
      <Show when={user()} fallback={<p>No user found</p>}>
        {(userData) => (
          <div>
            <h1>{userData().name}</h1>
            <p>{userData().email}</p>
          </div>
        )}
      </Show>
    </Suspense>
  );
}
```

**Resource with mutate and refetch:**
```typescript
function UserEditor() {
  const [userId, setUserId] = createSignal('1');
  const [user, { mutate, refetch }] = createResource(userId, fetchUser);

  const handleSave = async (newData) => {
    await saveUser(userId(), newData);

    // Option 1: Optimistic update
    mutate(prev => ({ ...prev, ...newData }));

    // Option 2: Refetch from server
    refetch();
  };

  return (
    <div>
      <p>Status: {user.state}</p> {/* "pending" | "ready" | "errored" | "refreshing" */}
      <Show when={!user.loading} fallback={<p>Loading...</p>}>
        <UserForm user={user()} onSave={handleSave} />
      </Show>
      <Show when={user.error}>
        <p>Error: {user.error.message}</p>
      </Show>
    </div>
  );
}
```

---

## Operation: Control Flow Components

**Purpose:** Efficient conditional and list rendering

**Show (conditional):**
```typescript
import { Show } from 'solid-js';

<Show
  when={isLoggedIn()}
  fallback={<LoginButton />}
>
  <UserDashboard />
</Show>

// With callback for narrowing types
<Show when={user()}>
  {(user) => <p>Hello, {user().name}</p>}
</Show>
```

**For (lists):**
```typescript
import { For } from 'solid-js';

<For each={items()}>
  {(item, index) => (
    <li>
      {index()}: {item.name}
    </li>
  )}
</For>

// With fallback for empty arrays
<For each={items()} fallback={<p>No items</p>}>
  {(item) => <Item data={item} />}
</For>
```

**Index (when index is key):**
```typescript
import { Index } from 'solid-js';

// Use when items change but order stays same
<Index each={items()}>
  {(item, index) => (
    <li>
      {index}: {item().name}
    </li>
  )}
</Index>
```

**Switch/Match (multiple conditions):**
```typescript
import { Switch, Match } from 'solid-js';

<Switch fallback={<p>Unknown status</p>}>
  <Match when={status() === 'loading'}>
    <Spinner />
  </Match>
  <Match when={status() === 'error'}>
    <ErrorMessage />
  </Match>
  <Match when={status() === 'success'}>
    <SuccessMessage />
  </Match>
</Switch>
```

**When to use which:**
| Component | Use For | Notes |
|-----------|---------|-------|
| `<Show>` | Boolean conditions | Best for presence/absence |
| `<For>` | Dynamic lists where items change | Keyed by reference |
| `<Index>` | Lists where index matters | Keyed by index |
| `<Switch>` | Multiple exclusive conditions | Like switch statement |
| `<Dynamic>` | Dynamic component type | `<Dynamic component={cmp} />` |

---

## Operation: Component Patterns

**Purpose:** Build reusable, composable components

**Props and children:**
```typescript
import { ParentComponent, JSX } from 'solid-js';

// With explicit children
const Card: ParentComponent<{ title: string }> = (props) => {
  return (
    <div class="card">
      <h2>{props.title}</h2>
      <div class="card-body">
        {props.children}
      </div>
    </div>
  );
};

// Usage
<Card title="Hello">
  <p>Card content here</p>
</Card>
```

**Splitting props:**
```typescript
import { splitProps } from 'solid-js';

function Button(props: {
  variant?: 'primary' | 'secondary';
  class?: string;
  // ...all button attributes
} & JSX.ButtonHTMLAttributes<HTMLButtonElement>) {
  const [local, buttonProps] = splitProps(props, ['variant', 'class']);

  return (
    <button
      class={`btn btn-${local.variant ?? 'primary'} ${local.class ?? ''}`}
      {...buttonProps}
    >
      {props.children}
    </button>
  );
}
```

**Merging defaults:**
```typescript
import { mergeProps } from 'solid-js';

function Greeting(props: { name?: string; greeting?: string }) {
  const merged = mergeProps(
    { name: 'World', greeting: 'Hello' },
    props
  );

  return <p>{merged.greeting}, {merged.name}!</p>;
}
```

**Context for dependency injection:**
```typescript
import { createContext, useContext, ParentComponent } from 'solid-js';

interface ThemeContext {
  theme: () => 'light' | 'dark';
  toggleTheme: () => void;
}

const ThemeContext = createContext<ThemeContext>();

export const ThemeProvider: ParentComponent = (props) => {
  const [theme, setTheme] = createSignal<'light' | 'dark'>('light');

  const value: ThemeContext = {
    theme,
    toggleTheme: () => setTheme(t => t === 'light' ? 'dark' : 'light'),
  };

  return (
    <ThemeContext.Provider value={value}>
      {props.children}
    </ThemeContext.Provider>
  );
};

export function useTheme() {
  const context = useContext(ThemeContext);
  if (!context) {
    throw new Error('useTheme must be used within ThemeProvider');
  }
  return context;
}
```

---

## Configuration Reference

### Vite Configuration

```typescript
// vite.config.ts
import { defineConfig } from 'vite';
import solidPlugin from 'vite-plugin-solid';

export default defineConfig({
  plugins: [solidPlugin()],

  server: {
    port: 3000,
  },

  build: {
    target: 'esnext',
  },

  resolve: {
    conditions: ['development', 'browser'],
  },
});
```

### TypeScript Configuration

```json
// tsconfig.json
{
  "compilerOptions": {
    "target": "ESNext",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "jsxImportSource": "solid-js",
    "jsx": "preserve",
    "strict": true,
    "noEmit": true,
    "types": ["vite/client"]
  }
}
```

---

## Best Practices

### Do

- **Access signals in JSX for reactivity:**
  ```typescript
  // Good: count() called in JSX creates subscription
  <p>Count: {count()}</p>
  ```

- **Use stores for nested state:**
  ```typescript
  // Good: Granular updates to nested properties
  const [state, setState] = createStore({ user: { name: '' } });
  setState('user', 'name', 'John');
  ```

- **Leverage untrack for non-reactive reads:**
  ```typescript
  // Good: Read value without creating subscription
  createEffect(() => {
    console.log('a changed:', a());
    console.log('b value (not tracked):', untrack(() => b()));
  });
  ```

### Don't

- **Don't destructure props:**
  ```typescript
  // Bad: Loses reactivity
  function Bad({ name }) {
    return <p>{name}</p>;
  }

  // Good: Keep props object
  function Good(props) {
    return <p>{props.name}</p>;
  }
  ```

- **Don't call signals outside reactive contexts:**
  ```typescript
  // Bad: count() read during component init, not tracked
  function Bad() {
    const message = `Count is ${count()}`; // Runs once
    return <p>{message}</p>;
  }

  // Good: Signal read in JSX
  function Good() {
    return <p>Count is {count()}</p>;
  }
  ```

### Performance Tips

1. **Use `<Index>` for primitive lists** - when array items are primitives
2. **Wrap expensive computations in `createMemo`**
3. **Use `batch()` for multiple signal updates**
4. **Leverage `untrack()` to prevent unnecessary subscriptions**
5. **Use `lazy()` for code splitting**

---

## Troubleshooting

### Common Issues

| Symptom | Cause | Solution |
|---------|-------|----------|
| Value doesn't update | Destructured props | Access via `props.value` |
| Effect runs multiple times | Multiple signal reads | Use `on()` for explicit deps |
| Memory leak | Missing cleanup | Add `onCleanup()` in effect |
| TypeScript JSX error | Wrong tsconfig | Set `jsxImportSource: "solid-js"` |
| Component runs multiple times | Incorrect mental model | Components run once in Solid |

### Diagnostic Commands

```bash
# Check for reactivity issues
console.log(createRoot(() => count())); // Test signal outside component

# Debug re-renders (should be rare in Solid)
createEffect(() => console.log('Effect ran'));

# Check bundle size
npm run build -- --report
```

---

## Integration Patterns

### With Tailwind CSS

```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

### With Solid Router

```bash
npm install @solidjs/router
```

```typescript
import { Router, Route } from '@solidjs/router';

<Router>
  <Route path="/" component={Home} />
  <Route path="/about" component={About} />
  <Route path="/users/:id" component={User} />
</Router>
```

### With SolidStart (Full-Stack)

```bash
npm create solid@latest my-app -- --template hackernews
```

---

## Version Compatibility

| Version | Status | Notable Changes |
|---------|--------|-----------------|
| v1.8.x | Current | Improved TypeScript, better SSR |
| v1.7.x | Supported | Hydration improvements |
| v1.6.x | Supported | Store improvements |
