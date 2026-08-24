---
name: hono-edge-patterns
description: Master Hono framework for building ultra-fast, lightweight web applications on edge runtimes. Use this skill when building APIs for Cloudflare Workers, Deno Deploy, Bun, Vercel Edge, or when users mention "Hono", "edge runtime", "Cloudflare Workers", "Deno Deploy", "ultrafast API", or "edge functions".
metadata:
  tags:
    - backend
    - edge
    - hono
  updated: "2026-04-11"
---
# Hono Edge Patterns

Hono is an ultrafast, lightweight web framework built on web standards, designed to run on any JavaScript runtime — from Cloudflare Workers to Node.js, Deno, Bun, and Vercel Edge Functions.

## Purpose

This skill provides comprehensive guidance for building high-performance APIs and web applications with Hono, including middleware patterns, routing, validation, RPC-style APIs, and deployment to various edge platforms.

## When to Use This Skill

- Build APIs for edge runtimes (Cloudflare Workers, Deno, Bun, Vercel Edge)
- Create ultrafast, lightweight web services
- Build type-safe API clients with hono/client
- Develop microservices with minimal cold start
- Replace Express.js with a modern, type-safe alternative

## When NOT to Use This Skill

- Full-stack apps with SSR → consider `qwik-development` or Next.js
- Need extensive Express middleware ecosystem → stick with Express
- Building traditional Node.js monoliths → Express or Fastify may fit better

## Prerequisites

- **Runtime:** Node.js 18+, Deno, Bun, or Cloudflare Workers
- **TypeScript:** Recommended for full type safety

```bash
npm create hono@latest my-app
npm list hono  # Expected: hono@4.x.x
```

---

## Quick Reference

| Task | Command/Code | Notes |
|------|--------------|-------|
| Create project | `npm create hono@latest` | Interactive setup |
| Start dev server | `npm run dev` | Wrangler for CF Workers |
| Add middleware | `app.use('*', middleware)` | Global middleware |
| Define route | `app.get('/path', handler)` | HTTP method routing |
| Group routes | `app.route('/api', apiApp)` | Mount sub-applications |
| Deploy (CF Workers) | `npx wrangler deploy` | Production deployment |

| Concept | Description | Example |
|---------|-------------|---------|
| Context (c) | Request/response wrapper | `c.json()`, `c.text()` |
| Middleware | Request processing chain | `app.use(cors())` |
| Routing | HTTP method handlers | `app.get()`, `app.post()` |
| Validator | Request validation | `validator('json', schema)` |
| RPC | Type-safe client | `hc<AppType>(url)` |

---

## Core Concepts

### Web Standards API

```typescript
import { Hono } from 'hono';

const app = new Hono();

app.get('/', (c) => {
  const url = c.req.url;
  return c.json({ message: 'Hello' });
});

export default app;
```

### Multi-Runtime Support

Same code runs everywhere:

```typescript
// Cloudflare Workers
export default app;

// Node.js
import { serve } from '@hono/node-server';
serve(app);

// Deno
Deno.serve(app.fetch);

// Bun
export default app; // Bun auto-detects

// Vercel Edge
export const GET = app.fetch;
```

---

## Core Operations

### Operation: Create New Project

```bash
npm create hono@latest my-api -- --template cloudflare-workers
cd my-api && npm install && npm run dev
```

**Project structure (Cloudflare Workers):**
```
my-api/
├── src/
│   └── index.ts
├── wrangler.toml
├── package.json
└── tsconfig.json
```

---

### Operation: Define Routes

```typescript
import { Hono } from 'hono';

const app = new Hono();

app.get('/users', (c) => c.json([{ id: 1, name: 'John' }]));

app.post('/users', async (c) => {
  const body = await c.req.json();
  return c.json({ created: body }, 201);
});

app.get('/users/:id', (c) => {
  const id = c.req.param('id');
  return c.json({ id });
});

app.get('/search', (c) => {
  const q = c.req.query('q');
  const page = c.req.query('page') ?? '1';
  return c.json({ query: q, page });
});

app.get('/users/:userId/posts/:postId', (c) => {
  const { userId, postId } = c.req.param();
  return c.json({ userId, postId });
});

// Wildcard
app.get('/files/*', (c) => {
  const path = c.req.param('*');
  return c.text(`File: ${path}`);
});
```

---

### Operation: Middleware

**Built-in middleware:**
```typescript
import { cors } from 'hono/cors';
import { logger } from 'hono/logger';
import { prettyJSON } from 'hono/pretty-json';
import { secureHeaders } from 'hono/secure-headers';
import { compress } from 'hono/compress';
import { etag } from 'hono/etag';

app.use('*', logger());
app.use('*', cors());
app.use('*', secureHeaders());
app.use('*', compress());

app.use('/api/*', cors({
  origin: 'https://example.com',
  credentials: true,
}));
```

**Custom middleware:**
```typescript
import { createMiddleware } from 'hono/factory';

const timing = createMiddleware(async (c, next) => {
  const start = Date.now();
  await next();
  c.header('X-Response-Time', `${Date.now() - start}ms`);
});

const auth = (secret: string) =>
  createMiddleware(async (c, next) => {
    const token = c.req.header('Authorization')?.replace('Bearer ', '');
    if (!token || token !== secret) {
      return c.json({ error: 'Unauthorized' }, 401);
    }
    await next();
  });

app.use('*', timing);
app.use('/admin/*', auth('my-secret'));
```

**Middleware with context variables:**
```typescript
type Env = {
  Variables: { user: { id: string; role: string } };
};

const authMiddleware = createMiddleware<Env>(async (c, next) => {
  const token = c.req.header('Authorization');
  const user = await validateToken(token);

  if (!user) return c.json({ error: 'Unauthorized' }, 401);

  c.set('user', user);
  await next();
});

const app = new Hono<Env>();
app.use('/api/*', authMiddleware);

app.get('/api/profile', (c) => {
  const user = c.get('user'); // Type-safe
  return c.json(user);
});
```

---

### Operation: Request Validation

**With Zod:**
```typescript
import { zValidator } from '@hono/zod-validator';
import { z } from 'zod';

const createUserSchema = z.object({
  name: z.string().min(1),
  email: z.string().email(),
  age: z.number().min(0).optional(),
});

app.post(
  '/users',
  zValidator('json', createUserSchema),
  (c) => {
    const data = c.req.valid('json'); // Fully typed
    return c.json({ created: data }, 201);
  }
);

const searchSchema = z.object({
  q: z.string().min(1),
  page: z.coerce.number().default(1),
  limit: z.coerce.number().default(10),
});

app.get(
  '/search',
  zValidator('query', searchSchema),
  (c) => {
    const { q, page, limit } = c.req.valid('query');
    return c.json({ query: q, page, limit });
  }
);

// Custom error handling
app.post(
  '/users',
  zValidator('json', createUserSchema, (result, c) => {
    if (!result.success) {
      return c.json({ error: 'Validation failed', details: result.error.flatten() }, 400);
    }
  }),
  (c) => c.json(c.req.valid('json'))
);
```

---

## Best Practices

### Do
- **Use type-safe environment bindings:**
  ```typescript
  type Bindings = { DB: D1Database; CACHE: KVNamespace; API_KEY: string };
  const app = new Hono<{ Bindings: Bindings }>();
  app.get('/', (c) => { const db = c.env.DB; }); // Type-safe
  ```
- **Leverage RPC for type-safe clients** — full end-to-end type safety
- **Use built-in middleware** — optimized for performance
- **Return early in middleware** — avoid unnecessary processing

### Don't
- **Don't use heavy ORMs** — prefer lightweight clients for edge
- **Don't block the event loop** — use async/await properly
- **Don't store state in memory** — edge functions are stateless
- **Don't forget to handle errors** — global error handler is essential

### Performance Tips

1. Use streaming responses for large payloads
2. Leverage edge caching (Cache API, KV)
3. Minimize cold starts by keeping dependencies light
4. Use connection pooling for databases (Hyperdrive for CF)
5. Implement proper caching headers

---

## Troubleshooting

| Symptom | Cause | Solution |
|---------|-------|----------|
| `c.env` is undefined | Wrong Hono type | Use `Hono<{ Bindings: Env }>` |
| Types not working | Missing export | Export `AppType` for client |
| CORS errors | Missing middleware | Add `cors()` middleware |
| 502 errors | Cold start timeout | Reduce dependencies |
| DB connection fails | Wrong binding | Check wrangler.toml config |

```bash
npx wrangler dev       # Local development
npx wrangler deploy    # Deploy to Cloudflare
npx wrangler tail      # View logs
```

---

## Reference Files

| Resource | Purpose |
|----------|---------|
| `references/rpc-error-routing-and-integration.md` | Type-safe RPC client, error handling, route groups, CF D1/KV/OpenAPI integration, version compatibility |
| `references/middleware.md` | Complete middleware catalog |
| `references/deployment.md` | Platform deployment guides |

## Related Skills

- `cloudflare-troubleshooting` - Cloudflare Workers debugging
- `serverless-patterns` - General serverless architecture
- `express-to-hono-migration` - Migration from Express
