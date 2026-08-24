# Qwik — Side Effects, Server Functions & Data Loading

## Operation: Implement Side Effects

**Purpose:** Run code in response to state changes

**useTask$ (runs on server and client):**
```typescript
import { component$, useSignal, useTask$ } from '@builder.io/qwik';

export default component$(() => {
  const query = useSignal('');
  const results = useSignal<string[]>([]);

  // Runs whenever query changes (with automatic cleanup)
  useTask$(({ track, cleanup }) => {
    track(() => query.value); // Track this dependency

    const controller = new AbortController();

    if (query.value.length > 2) {
      fetch(`/api/search?q=${query.value}`, {
        signal: controller.signal,
      })
        .then((res) => res.json())
        .then((data) => {
          results.value = data;
        });
    }

    cleanup(() => controller.abort());
  });

  return (
    <div>
      <input
        value={query.value}
        onInput$={(e) => {
          query.value = (e.target as HTMLInputElement).value;
        }}
      />
      <ul>
        {results.value.map((r) => (
          <li key={r}>{r}</li>
        ))}
      </ul>
    </div>
  );
});
```

**useVisibleTask$ (client-only):**
```typescript
import { component$, useVisibleTask$, useSignal } from '@builder.io/qwik';

export default component$(() => {
  const elementRef = useSignal<HTMLElement>();

  // Only runs on client when element is visible
  useVisibleTask$(({ track }) => {
    track(() => elementRef.value);

    if (elementRef.value) {
      // Browser-only APIs safe here
      const observer = new IntersectionObserver((entries) => {
        // Handle intersection
      });
      observer.observe(elementRef.value);

      return () => observer.disconnect();
    }
  });

  return <div ref={elementRef}>Observed element</div>;
});
```

**Eager vs lazy execution:**
```typescript
// Eager: runs immediately on client
useVisibleTask$(
  () => {
    // Initialize immediately
  },
  { strategy: 'document-ready' }
);

// Lazy (default): runs when component is visible
useVisibleTask$(() => {
  // Initialize when visible
});
```

---

## Operation: Create Server Functions

**Purpose:** Execute code exclusively on the server

**Basic server function:**
```typescript
import { component$ } from '@builder.io/qwik';
import { server$ } from '@builder.io/qwik-city';

// This code ONLY runs on the server
const getSecretData = server$(async function () {
  // Access environment variables, databases, etc.
  const apiKey = this.env.get('API_KEY');
  const data = await fetch('https://api.example.com', {
    headers: { Authorization: `Bearer ${apiKey}` },
  });
  return data.json();
});

export default component$(() => {
  return (
    <button
      onClick$={async () => {
        const data = await getSecretData();
        console.log(data);
      }}
    >
      Load Secret Data
    </button>
  );
});
```

**Server function with arguments:**
```typescript
const saveUser = server$(async function (user: User) {
  // Access request context
  const cookie = this.cookie;
  const headers = this.headers;

  // Database operation
  await db.users.insert(user);
  return { success: true };
});

// Usage
await saveUser({ name: 'John', email: 'john@example.com' });
```

**Form actions (alternative pattern):**
```typescript
// src/routes/contact/index.tsx
import { component$ } from '@builder.io/qwik';
import { routeAction$, Form, zod$, z } from '@builder.io/qwik-city';

export const useContactAction = routeAction$(
  async (data) => {
    // Server-side form handling
    await sendEmail(data);
    return { success: true };
  },
  zod$({
    name: z.string().min(1),
    email: z.string().email(),
    message: z.string().min(10),
  })
);

export default component$(() => {
  const action = useContactAction();

  return (
    <Form action={action}>
      <input name="name" />
      <input name="email" type="email" />
      <textarea name="message" />
      <button type="submit">Send</button>
      {action.value?.success && <p>Message sent!</p>}
    </Form>
  );
});
```

---

## Operation: Data Loading with routeLoader$

**Purpose:** Load data on the server before rendering

**Basic loader:**
```typescript
// src/routes/products/index.tsx
import { component$ } from '@builder.io/qwik';
import { routeLoader$ } from '@builder.io/qwik-city';

export const useProducts = routeLoader$(async () => {
  const products = await db.products.findMany();
  return products;
});

export default component$(() => {
  const products = useProducts();

  return (
    <ul>
      {products.value.map((product) => (
        <li key={product.id}>{product.name}</li>
      ))}
    </ul>
  );
});
```

**Loader with request context:**
```typescript
export const useUserData = routeLoader$(async (requestEvent) => {
  // Access cookies, headers, params
  const token = requestEvent.cookie.get('auth_token');
  const userId = requestEvent.params.userId;

  if (!token) {
    throw requestEvent.redirect(302, '/login');
  }

  const user = await getUserById(userId);

  if (!user) {
    throw requestEvent.error(404, 'User not found');
  }

  return user;
});
```

**Multiple loaders:**
```typescript
export const useUser = routeLoader$(async () => {
  return await getUser();
});

export const usePosts = routeLoader$(async () => {
  return await getPosts();
});

export default component$(() => {
  const user = useUser();
  const posts = usePosts();

  // Both load in parallel on server
  return (
    <div>
      <h1>{user.value.name}</h1>
      <PostList posts={posts.value} />
    </div>
  );
});
```
