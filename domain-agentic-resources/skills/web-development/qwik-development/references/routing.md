# QwikCity Routing Guide

Complete reference for file-based routing in QwikCity.

## Directory Structure

### Basic Routes

```
src/routes/
├── index.tsx              → /
├── about/
│   └── index.tsx          → /about
├── contact/
│   └── index.tsx          → /contact
└── blog/
    ├── index.tsx          → /blog
    └── [slug]/
        └── index.tsx      → /blog/:slug
```

### Naming Conventions

| File/Folder | URL | Notes |
|-------------|-----|-------|
| `index.tsx` | Route endpoint | Required for route to exist |
| `layout.tsx` | N/A | Wraps child routes |
| `[param]/` | Dynamic segment | `:param` in URL |
| `[...rest]/` | Catch-all | Matches remaining path |
| `(group)/` | Route group | No URL impact |

## Route Components

### Basic Route

```typescript
// src/routes/about/index.tsx
import { component$ } from '@builder.io/qwik';

export default component$(() => {
  return (
    <div>
      <h1>About Us</h1>
      <p>Welcome to our about page.</p>
    </div>
  );
});
```

### Route with Head

```typescript
// src/routes/about/index.tsx
import { component$ } from '@builder.io/qwik';
import { DocumentHead } from '@builder.io/qwik-city';

export default component$(() => {
  return <h1>About Us</h1>;
});

export const head: DocumentHead = {
  title: 'About Us | My Site',
  meta: [
    {
      name: 'description',
      content: 'Learn more about our company',
    },
  ],
  links: [
    {
      rel: 'canonical',
      href: 'https://example.com/about',
    },
  ],
};
```

### Dynamic Head

```typescript
import { DocumentHead, routeLoader$ } from '@builder.io/qwik-city';

export const usePost = routeLoader$(async ({ params }) => {
  return await getPost(params.slug);
});

export const head: DocumentHead = ({ resolveValue }) => {
  const post = resolveValue(usePost);
  return {
    title: `${post.title} | Blog`,
    meta: [
      { name: 'description', content: post.excerpt },
      { property: 'og:title', content: post.title },
      { property: 'og:image', content: post.image },
    ],
  };
};
```

## Dynamic Routes

### Single Parameter

```typescript
// src/routes/users/[userId]/index.tsx
import { component$ } from '@builder.io/qwik';
import { routeLoader$ } from '@builder.io/qwik-city';

export const useUser = routeLoader$(async ({ params, status }) => {
  const user = await getUser(params.userId);
  if (!user) {
    status(404);
  }
  return user;
});

export default component$(() => {
  const user = useUser();

  if (!user.value) {
    return <div>User not found</div>;
  }

  return <h1>{user.value.name}</h1>;
});
```

### Multiple Parameters

```typescript
// src/routes/[org]/[repo]/index.tsx
// Matches: /github/qwik, /vercel/next.js, etc.

export const useRepo = routeLoader$(async ({ params }) => {
  const { org, repo } = params;
  return await getRepo(org, repo);
});
```

### Catch-All Routes

```typescript
// src/routes/docs/[...slug]/index.tsx
// Matches: /docs/intro, /docs/getting-started/installation, etc.

export const useDoc = routeLoader$(async ({ params }) => {
  const slug = params.slug; // "intro" or "getting-started/installation"
  return await getDoc(slug);
});
```

### Optional Catch-All

```typescript
// src/routes/[[...path]]/index.tsx
// Matches: /, /any, /any/path/here
// Note: Double brackets make it optional

export default component$(() => {
  // This route handles all paths including root
  return <CatchAllComponent />;
});
```

## Layouts

### Root Layout

```typescript
// src/routes/layout.tsx
import { component$, Slot } from '@builder.io/qwik';

export default component$(() => {
  return (
    <html lang="en">
      <head>
        <meta charSet="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
      </head>
      <body>
        <Header />
        <main>
          <Slot /> {/* Child routes render here */}
        </main>
        <Footer />
      </body>
    </html>
  );
});
```

### Nested Layouts

```
src/routes/
├── layout.tsx              # Root layout (all pages)
├── index.tsx               # Home (/)
├── (marketing)/            # Route group (no URL impact)
│   ├── layout.tsx          # Marketing layout
│   ├── about/
│   │   └── index.tsx       # /about (marketing layout)
│   └── pricing/
│       └── index.tsx       # /pricing (marketing layout)
└── dashboard/
    ├── layout.tsx          # Dashboard layout
    ├── index.tsx           # /dashboard
    └── settings/
        └── index.tsx       # /dashboard/settings
```

```typescript
// src/routes/dashboard/layout.tsx
import { component$, Slot } from '@builder.io/qwik';

export default component$(() => {
  return (
    <div class="dashboard-layout">
      <aside class="sidebar">
        <DashboardNav />
      </aside>
      <div class="content">
        <Slot />
      </div>
    </div>
  );
});
```

### Layout Data

```typescript
// src/routes/dashboard/layout.tsx
import { component$, Slot } from '@builder.io/qwik';
import { routeLoader$ } from '@builder.io/qwik-city';

// Data available to all dashboard routes
export const useUser = routeLoader$(async ({ cookie, redirect }) => {
  const token = cookie.get('auth');
  if (!token) {
    throw redirect(302, '/login');
  }
  return await getUser(token.value);
});

export default component$(() => {
  const user = useUser();

  return (
    <div class="dashboard">
      <header>Welcome, {user.value.name}</header>
      <Slot />
    </div>
  );
});
```

## Navigation

### Link Component

```typescript
import { component$ } from '@builder.io/qwik';
import { Link } from '@builder.io/qwik-city';

export default component$(() => {
  return (
    <nav>
      <Link href="/">Home</Link>
      <Link href="/about">About</Link>
      <Link href="/blog" prefetch>Blog (prefetched)</Link>

      {/* Prefetch control */}
      <Link href="/heavy" prefetch={false}>Heavy Page</Link>

      {/* Reload instead of SPA navigation */}
      <Link href="/legacy" reload>Legacy Page</Link>
    </nav>
  );
});
```

### Active Link Styling

```typescript
import { component$ } from '@builder.io/qwik';
import { Link, useLocation } from '@builder.io/qwik-city';

export default component$(() => {
  const loc = useLocation();

  return (
    <nav>
      <Link
        href="/about"
        class={{ active: loc.url.pathname === '/about' }}
      >
        About
      </Link>
    </nav>
  );
});
```

### Programmatic Navigation

```typescript
import { component$ } from '@builder.io/qwik';
import { useNavigate } from '@builder.io/qwik-city';

export default component$(() => {
  const nav = useNavigate();

  return (
    <button
      onClick$={async () => {
        // Navigate with SPA behavior
        await nav('/dashboard');

        // Navigate with options
        await nav('/dashboard', {
          forceReload: true,     // Full page reload
          replaceState: true,   // Replace history entry
          scroll: false,        // Don't scroll to top
        });
      }}
    >
      Go to Dashboard
    </button>
  );
});
```

## Data Loading

### routeLoader$

```typescript
// src/routes/products/index.tsx
import { component$ } from '@builder.io/qwik';
import { routeLoader$ } from '@builder.io/qwik-city';

// Runs on server during SSR
export const useProducts = routeLoader$(async () => {
  const products = await db.products.findMany({
    orderBy: { createdAt: 'desc' },
    take: 20,
  });
  return products;
});

export default component$(() => {
  const products = useProducts();

  return (
    <ul>
      {products.value.map((p) => (
        <li key={p.id}>{p.name}</li>
      ))}
    </ul>
  );
});
```

### Parallel Loaders

```typescript
// Both run in parallel on server
export const useUser = routeLoader$(async () => {
  return await getUser();
});

export const usePosts = routeLoader$(async () => {
  return await getPosts();
});

export default component$(() => {
  const user = useUser();
  const posts = usePosts();

  return (
    <div>
      <h1>{user.value.name}'s Posts</h1>
      <PostList posts={posts.value} />
    </div>
  );
});
```

### Dependent Loaders

```typescript
// First loader
export const useUser = routeLoader$(async () => {
  return await getUser();
});

// Second loader depends on first
export const useUserPosts = routeLoader$(async ({ resolveValue }) => {
  const user = await resolveValue(useUser);
  return await getPostsByUser(user.id);
});
```

## Error Handling

### Error Response

```typescript
export const usePost = routeLoader$(async ({ params, status }) => {
  const post = await getPost(params.slug);

  if (!post) {
    status(404);
    return null;
  }

  return post;
});
```

### Redirects

```typescript
export const useProtectedData = routeLoader$(async ({ redirect, cookie }) => {
  const token = cookie.get('auth');

  if (!token) {
    // Redirect to login
    throw redirect(302, '/login');
  }

  // Redirect with query params
  throw redirect(302, '/login?returnTo=/dashboard');
});
```

### Error Pages

```typescript
// src/routes/404.tsx
import { component$ } from '@builder.io/qwik';

export default component$(() => {
  return (
    <div>
      <h1>404 - Page Not Found</h1>
      <Link href="/">Go Home</Link>
    </div>
  );
});
```

## Route Groups

### Organizing Without URL Impact

```
src/routes/
├── (auth)/                # Group: no URL impact
│   ├── login/
│   │   └── index.tsx      # /login
│   └── register/
│       └── index.tsx      # /register
├── (marketing)/
│   ├── layout.tsx         # Marketing layout
│   ├── about/
│   │   └── index.tsx      # /about
│   └── pricing/
│       └── index.tsx      # /pricing
└── (app)/
    ├── layout.tsx         # App layout
    └── dashboard/
        └── index.tsx      # /dashboard
```

## Middleware

### Route-Level Middleware

```typescript
// src/routes/dashboard/layout.tsx
import { component$, Slot } from '@builder.io/qwik';
import { routeLoader$ } from '@builder.io/qwik-city';
import type { RequestHandler } from '@builder.io/qwik-city';

// Middleware runs before loaders
export const onRequest: RequestHandler = async ({ cookie, redirect }) => {
  const token = cookie.get('auth');
  if (!token) {
    throw redirect(302, '/login');
  }
};

export default component$(() => {
  return <Slot />;
});
```

### Global Middleware

```typescript
// src/routes/plugin@auth.ts
import type { RequestHandler } from '@builder.io/qwik-city';

export const onRequest: RequestHandler = async ({ cookie, sharedMap }) => {
  const token = cookie.get('auth');
  if (token) {
    const user = await validateToken(token.value);
    sharedMap.set('user', user);
  }
};
```

## API Routes

### Endpoint Files

```typescript
// src/routes/api/users/index.ts
import type { RequestHandler } from '@builder.io/qwik-city';

export const onGet: RequestHandler = async ({ json }) => {
  const users = await db.users.findMany();
  json(200, users);
};

export const onPost: RequestHandler = async ({ request, json }) => {
  const body = await request.json();
  const user = await db.users.create({ data: body });
  json(201, user);
};
```

### Dynamic API Routes

```typescript
// src/routes/api/users/[id]/index.ts
import type { RequestHandler } from '@builder.io/qwik-city';

export const onGet: RequestHandler = async ({ params, json, status }) => {
  const user = await db.users.findUnique({ where: { id: params.id } });

  if (!user) {
    json(404, { error: 'User not found' });
    return;
  }

  json(200, user);
};

export const onDelete: RequestHandler = async ({ params, json }) => {
  await db.users.delete({ where: { id: params.id } });
  json(204, null);
};
```
