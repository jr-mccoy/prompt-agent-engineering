# Qwik Component Patterns

Common patterns for building components in Qwik.

## Basic Patterns

### Stateful Component

```typescript
import { component$, useSignal } from '@builder.io/qwik';

export const Counter = component$(() => {
  const count = useSignal(0);

  return (
    <div>
      <p>Count: {count.value}</p>
      <button onClick$={() => count.value++}>+</button>
      <button onClick$={() => count.value--}>-</button>
    </div>
  );
});
```

### Component with Props

```typescript
import { component$ } from '@builder.io/qwik';

interface ButtonProps {
  label: string;
  variant?: 'primary' | 'secondary';
  disabled?: boolean;
  onClick$?: () => void;
}

export const Button = component$<ButtonProps>(
  ({ label, variant = 'primary', disabled = false, onClick$ }) => {
    return (
      <button
        class={`btn btn-${variant}`}
        disabled={disabled}
        onClick$={onClick$}
      >
        {label}
      </button>
    );
  }
);

// Usage
<Button
  label="Submit"
  variant="primary"
  onClick$={() => console.log('clicked')}
/>
```

### Component with Children (Slot)

```typescript
import { component$, Slot } from '@builder.io/qwik';

export const Card = component$(() => {
  return (
    <div class="card">
      <Slot /> {/* Children render here */}
    </div>
  );
});

// Usage
<Card>
  <h2>Title</h2>
  <p>Content goes here</p>
</Card>
```

### Named Slots

```typescript
import { component$, Slot } from '@builder.io/qwik';

export const Layout = component$(() => {
  return (
    <div class="layout">
      <header>
        <Slot name="header" />
      </header>
      <main>
        <Slot /> {/* Default slot */}
      </main>
      <footer>
        <Slot name="footer" />
      </footer>
    </div>
  );
});

// Usage
<Layout>
  <div q:slot="header">Header content</div>
  <p>Main content (default slot)</p>
  <div q:slot="footer">Footer content</div>
</Layout>
```

## Form Patterns

### Controlled Input

```typescript
import { component$, useSignal } from '@builder.io/qwik';

export const TextInput = component$(() => {
  const value = useSignal('');

  return (
    <input
      type="text"
      value={value.value}
      onInput$={(e) => {
        value.value = (e.target as HTMLInputElement).value;
      }}
    />
  );
});
```

### Form with Validation

```typescript
import { component$, useStore, $ } from '@builder.io/qwik';

interface FormState {
  email: string;
  password: string;
  errors: {
    email?: string;
    password?: string;
  };
}

export const LoginForm = component$(() => {
  const form = useStore<FormState>({
    email: '',
    password: '',
    errors: {},
  });

  const validate = $(() => {
    form.errors = {};

    if (!form.email.includes('@')) {
      form.errors.email = 'Invalid email';
    }
    if (form.password.length < 8) {
      form.errors.password = 'Password must be 8+ characters';
    }

    return Object.keys(form.errors).length === 0;
  });

  const handleSubmit = $(async () => {
    if (await validate()) {
      // Submit form
      console.log('Submitting:', form.email, form.password);
    }
  });

  return (
    <form preventdefault:submit onSubmit$={handleSubmit}>
      <div>
        <input
          type="email"
          value={form.email}
          onInput$={(e) => {
            form.email = (e.target as HTMLInputElement).value;
          }}
        />
        {form.errors.email && <span class="error">{form.errors.email}</span>}
      </div>

      <div>
        <input
          type="password"
          value={form.password}
          onInput$={(e) => {
            form.password = (e.target as HTMLInputElement).value;
          }}
        />
        {form.errors.password && (
          <span class="error">{form.errors.password}</span>
        )}
      </div>

      <button type="submit">Login</button>
    </form>
  );
});
```

## Async Data Patterns

### useResource$ for Client Data

```typescript
import { component$, useSignal, useResource$, Resource } from '@builder.io/qwik';

interface User {
  id: number;
  name: string;
}

export const UserSearch = component$(() => {
  const query = useSignal('');

  const usersResource = useResource$<User[]>(async ({ track, cleanup }) => {
    track(() => query.value);

    const controller = new AbortController();
    cleanup(() => controller.abort());

    if (query.value.length < 2) return [];

    const res = await fetch(`/api/users?q=${query.value}`, {
      signal: controller.signal,
    });
    return res.json();
  });

  return (
    <div>
      <input
        value={query.value}
        onInput$={(e) => {
          query.value = (e.target as HTMLInputElement).value;
        }}
      />

      <Resource
        value={usersResource}
        onPending={() => <p>Loading...</p>}
        onRejected={(error) => <p>Error: {error.message}</p>}
        onResolved={(users) => (
          <ul>
            {users.map((user) => (
              <li key={user.id}>{user.name}</li>
            ))}
          </ul>
        )}
      />
    </div>
  );
});
```

### Infinite Scroll

```typescript
import { component$, useSignal, useVisibleTask$ } from '@builder.io/qwik';

interface Item {
  id: number;
  title: string;
}

export const InfiniteList = component$(() => {
  const items = useSignal<Item[]>([]);
  const page = useSignal(1);
  const loading = useSignal(false);
  const hasMore = useSignal(true);
  const sentinelRef = useSignal<HTMLElement>();

  const loadMore = $(async () => {
    if (loading.value || !hasMore.value) return;

    loading.value = true;
    const res = await fetch(`/api/items?page=${page.value}`);
    const newItems = await res.json();

    if (newItems.length === 0) {
      hasMore.value = false;
    } else {
      items.value = [...items.value, ...newItems];
      page.value++;
    }
    loading.value = false;
  });

  useVisibleTask$(({ track }) => {
    track(() => sentinelRef.value);

    if (!sentinelRef.value) return;

    const observer = new IntersectionObserver(
      (entries) => {
        if (entries[0].isIntersecting) {
          loadMore();
        }
      },
      { threshold: 0.1 }
    );

    observer.observe(sentinelRef.value);
    return () => observer.disconnect();
  });

  return (
    <div>
      <ul>
        {items.value.map((item) => (
          <li key={item.id}>{item.title}</li>
        ))}
      </ul>

      {hasMore.value && (
        <div ref={sentinelRef}>
          {loading.value ? 'Loading...' : 'Load more'}
        </div>
      )}
    </div>
  );
});
```

## Context Pattern

### Creating Context

```typescript
// src/context/theme.tsx
import {
  component$,
  createContextId,
  useContext,
  useContextProvider,
  useStore,
  Slot,
} from '@builder.io/qwik';

interface ThemeStore {
  mode: 'light' | 'dark';
  toggle: () => void;
}

export const ThemeContext = createContextId<ThemeStore>('theme');

export const ThemeProvider = component$(() => {
  const store = useStore<ThemeStore>({
    mode: 'light',
    toggle: $(function (this: ThemeStore) {
      this.mode = this.mode === 'light' ? 'dark' : 'light';
    }),
  });

  useContextProvider(ThemeContext, store);

  return <Slot />;
});

export const useTheme = () => useContext(ThemeContext);
```

### Using Context

```typescript
// src/components/ThemeToggle.tsx
import { component$ } from '@builder.io/qwik';
import { useTheme } from '~/context/theme';

export const ThemeToggle = component$(() => {
  const theme = useTheme();

  return (
    <button onClick$={() => theme.toggle()}>
      Current: {theme.mode}
    </button>
  );
});
```

## Render Patterns

### Conditional Rendering

```typescript
import { component$, useSignal } from '@builder.io/qwik';

export const Conditional = component$(() => {
  const isLoggedIn = useSignal(false);
  const count = useSignal(0);

  return (
    <div>
      {/* Boolean condition */}
      {isLoggedIn.value && <p>Welcome back!</p>}

      {/* Ternary */}
      {isLoggedIn.value ? <Dashboard /> : <LoginPrompt />}

      {/* Multiple conditions */}
      {count.value === 0 && <p>No items</p>}
      {count.value === 1 && <p>One item</p>}
      {count.value > 1 && <p>{count.value} items</p>}
    </div>
  );
});
```

### List Rendering

```typescript
import { component$ } from '@builder.io/qwik';

interface Item {
  id: string;
  name: string;
}

export const List = component$<{ items: Item[] }>(({ items }) => {
  return (
    <ul>
      {items.map((item) => (
        <li key={item.id}>{item.name}</li>
      ))}
    </ul>
  );
});
```

### Dynamic Component

```typescript
import { component$, useSignal } from '@builder.io/qwik';

const Tab1 = component$(() => <div>Tab 1 Content</div>);
const Tab2 = component$(() => <div>Tab 2 Content</div>);
const Tab3 = component$(() => <div>Tab 3 Content</div>);

const tabs = {
  tab1: Tab1,
  tab2: Tab2,
  tab3: Tab3,
};

export const DynamicTabs = component$(() => {
  const activeTab = useSignal<keyof typeof tabs>('tab1');
  const ActiveComponent = tabs[activeTab.value];

  return (
    <div>
      <nav>
        <button onClick$={() => (activeTab.value = 'tab1')}>Tab 1</button>
        <button onClick$={() => (activeTab.value = 'tab2')}>Tab 2</button>
        <button onClick$={() => (activeTab.value = 'tab3')}>Tab 3</button>
      </nav>
      <ActiveComponent />
    </div>
  );
});
```

## Style Patterns

### Scoped Styles

```typescript
import { component$, useStylesScoped$ } from '@builder.io/qwik';
import styles from './Button.module.css';

export const Button = component$(() => {
  // Option 1: CSS Modules
  return <button class={styles.button}>Click</button>;
});

export const ButtonInline = component$(() => {
  // Option 2: Scoped inline styles
  useStylesScoped$(`
    .button {
      padding: 8px 16px;
      border-radius: 4px;
    }
  `);

  return <button class="button">Click</button>;
});
```

### Dynamic Classes

```typescript
import { component$, useSignal } from '@builder.io/qwik';

export const DynamicStyles = component$(() => {
  const isActive = useSignal(false);

  return (
    <div
      class={{
        card: true,
        'card--active': isActive.value,
        'card--inactive': !isActive.value,
      }}
    >
      Content
    </div>
  );
});
```

## Ref Pattern

### DOM Reference

```typescript
import { component$, useSignal, $ } from '@builder.io/qwik';

export const FocusInput = component$(() => {
  const inputRef = useSignal<HTMLInputElement>();

  const focusInput = $(() => {
    inputRef.value?.focus();
  });

  return (
    <div>
      <input ref={inputRef} type="text" />
      <button onClick$={focusInput}>Focus Input</button>
    </div>
  );
});
```

## Composition Patterns

### Compound Components

```typescript
import { component$, Slot, createContextId, useContext, useContextProvider } from '@builder.io/qwik';

// Context
const AccordionContext = createContextId<{ activeIndex: number }>('accordion');

// Parent
export const Accordion = component$<{ defaultIndex?: number }>(
  ({ defaultIndex = 0 }) => {
    const store = useStore({ activeIndex: defaultIndex });
    useContextProvider(AccordionContext, store);

    return (
      <div class="accordion">
        <Slot />
      </div>
    );
  }
);

// Child
export const AccordionItem = component$<{ index: number }>(({ index }) => {
  const ctx = useContext(AccordionContext);
  const isOpen = ctx.activeIndex === index;

  return (
    <div class={{ 'accordion-item': true, open: isOpen }}>
      <button onClick$={() => (ctx.activeIndex = index)}>
        <Slot name="header" />
      </button>
      {isOpen && <Slot />}
    </div>
  );
});

// Usage
<Accordion>
  <AccordionItem index={0}>
    <span q:slot="header">Section 1</span>
    <p>Content 1</p>
  </AccordionItem>
  <AccordionItem index={1}>
    <span q:slot="header">Section 2</span>
    <p>Content 2</p>
  </AccordionItem>
</Accordion>
```
