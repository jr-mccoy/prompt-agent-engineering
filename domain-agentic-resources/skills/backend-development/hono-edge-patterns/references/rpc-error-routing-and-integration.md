# Hono Edge Patterns — RPC, Error Handling, Routing & Integration

## Operation: Type-Safe RPC Client

Generate type-safe API clients using `hono/client`.

**Server-side:**
```typescript
import { Hono } from 'hono';
import { zValidator } from '@hono/zod-validator';
import { z } from 'zod';

const app = new Hono()
  .get('/users', (c) => {
    return c.json([
      { id: '1', name: 'John' },
      { id: '2', name: 'Jane' },
    ]);
  })
  .get('/users/:id', (c) => {
    const id = c.req.param('id');
    return c.json({ id, name: 'John' });
  })
  .post(
    '/users',
    zValidator('json', z.object({
      name: z.string(),
      email: z.string().email(),
    })),
    (c) => {
      const data = c.req.valid('json');
      return c.json({ id: '3', ...data }, 201);
    }
  );

export type AppType = typeof app;
export default app;
```

**Client-side:**
```typescript
import { hc } from 'hono/client';
import type { AppType } from './server';

const client = hc<AppType>('http://localhost:8787');

// Fully typed API calls
const users = await client.users.$get();
const json = await users.json(); // User[]

const user = await client.users[':id'].$get({
  param: { id: '1' },
});

const created = await client.users.$post({
  json: {
    name: 'New User',
    email: 'new@example.com',
  },
});
```

---

## Operation: Error Handling

Handle errors globally with typed responses.

**Global error handler:**
```typescript
import { Hono } from 'hono';
import { HTTPException } from 'hono/http-exception';

const app = new Hono();

app.onError((err, c) => {
  console.error(err);

  if (err instanceof HTTPException) {
    return err.getResponse();
  }

  return c.json({
    error: 'Internal Server Error',
    message: err.message,
  }, 500);
});

app.notFound((c) => {
  return c.json({
    error: 'Not Found',
    path: c.req.path,
  }, 404);
});

app.get('/protected', (c) => {
  const authorized = checkAuth(c);

  if (!authorized) {
    throw new HTTPException(401, {
      message: 'Unauthorized',
    });
  }

  return c.json({ secret: 'data' });
});
```

**Typed error responses:**
```typescript
import { HTTPException } from 'hono/http-exception';

class APIError extends HTTPException {
  constructor(
    status: number,
    public code: string,
    message: string
  ) {
    super(status, { message });
  }
}

app.onError((err, c) => {
  if (err instanceof APIError) {
    return c.json({
      error: err.code,
      message: err.message,
    }, err.status);
  }

  return c.json({ error: 'INTERNAL_ERROR' }, 500);
});
```

---

## Operation: Route Groups and Mounting

Organize routes into modules with base path support.

```typescript
import { Hono } from 'hono';

// users.ts
const users = new Hono()
  .get('/', (c) => c.json([]))
  .get('/:id', (c) => c.json({ id: c.req.param('id') }))
  .post('/', (c) => c.json({ created: true }));

// posts.ts
const posts = new Hono()
  .get('/', (c) => c.json([]))
  .get('/:id', (c) => c.json({ id: c.req.param('id') }));

// index.ts — mount sub-apps
const app = new Hono()
  .route('/users', users)
  .route('/posts', posts);

// Results in: GET /users, GET /users/:id, POST /users, GET /posts, GET /posts/:id

// Base path
const v1 = new Hono().basePath('/api/v1');
v1.get('/users', handler); // /api/v1/users
```

---

## Configuration Reference

### Cloudflare Workers (wrangler.toml)

```toml
name = "my-api"
main = "src/index.ts"
compatibility_date = "2024-01-01"

[vars]
API_KEY = "development-key"

[[kv_namespaces]]
binding = "CACHE"
id = "your-kv-namespace-id"

[[d1_databases]]
binding = "DB"
database_name = "my-database"
database_id = "your-d1-database-id"

[env.production]
vars = { API_KEY = "production-key" }
```

### TypeScript Configuration

```json
{
  "compilerOptions": {
    "target": "ESNext",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "strict": true,
    "lib": ["ESNext"],
    "types": ["@cloudflare/workers-types"]
  }
}
```

---

## Integration Patterns

### With Cloudflare D1 (SQLite)

```typescript
import { Hono } from 'hono';
import { drizzle } from 'drizzle-orm/d1';

type Env = { Bindings: { DB: D1Database } };

const app = new Hono<Env>();

app.get('/users', async (c) => {
  const db = drizzle(c.env.DB);
  const users = await db.select().from(usersTable);
  return c.json(users);
});
```

### With Cloudflare KV

```typescript
type Env = { Bindings: { CACHE: KVNamespace } };

app.get('/cached/:key', async (c) => {
  const key = c.req.param('key');
  let value = await c.env.CACHE.get(key);

  if (!value) {
    value = await fetchExpensiveData(key);
    await c.env.CACHE.put(key, value, { expirationTtl: 3600 });
  }

  return c.json({ value });
});
```

### With OpenAPI/Swagger

```typescript
import { OpenAPIHono, createRoute } from '@hono/zod-openapi';

const app = new OpenAPIHono();

const route = createRoute({
  method: 'get',
  path: '/users',
  responses: {
    200: {
      content: { 'application/json': { schema: UserSchema } },
      description: 'List users',
    },
  },
});

app.openapi(route, (c) => {
  return c.json(users);
});

// GET /doc — Swagger UI
app.doc('/doc', { openapi: '3.0.0', info: { title: 'API', version: '1' } });
```

---

## Version Compatibility

| Version | Status | Notable Changes |
|---------|--------|-----------------|
| v4.x | Current | Improved types, streaming, new middleware |
| v3.x | Supported | Stable, RPC client |
| v2.x | Deprecated | Migration guide available |
