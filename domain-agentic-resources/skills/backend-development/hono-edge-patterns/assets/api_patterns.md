# Hono API Design Patterns

## RESTful Resource Routes

```typescript
import { Hono } from 'hono';

const users = new Hono()
  // List all
  .get('/', async (c) => {
    const users = await db.users.findMany();
    return c.json(users);
  })

  // Get one
  .get('/:id', async (c) => {
    const user = await db.users.findUnique(c.req.param('id'));
    if (!user) return c.notFound();
    return c.json(user);
  })

  // Create
  .post('/', async (c) => {
    const data = await c.req.json();
    const user = await db.users.create(data);
    return c.json(user, 201);
  })

  // Update
  .put('/:id', async (c) => {
    const data = await c.req.json();
    const user = await db.users.update(c.req.param('id'), data);
    return c.json(user);
  })

  // Partial update
  .patch('/:id', async (c) => {
    const data = await c.req.json();
    const user = await db.users.patch(c.req.param('id'), data);
    return c.json(user);
  })

  // Delete
  .delete('/:id', async (c) => {
    await db.users.delete(c.req.param('id'));
    return c.body(null, 204);
  });
```

## Pagination Pattern

```typescript
import { z } from 'zod';
import { zValidator } from '@hono/zod-validator';

const paginationSchema = z.object({
  page: z.coerce.number().min(1).default(1),
  limit: z.coerce.number().min(1).max(100).default(20),
  sort: z.string().optional(),
  order: z.enum(['asc', 'desc']).default('asc'),
});

app.get('/users', zValidator('query', paginationSchema), async (c) => {
  const { page, limit, sort, order } = c.req.valid('query');
  const offset = (page - 1) * limit;

  const [users, total] = await Promise.all([
    db.users.findMany({ offset, limit, sort, order }),
    db.users.count(),
  ]);

  return c.json({
    data: users,
    pagination: {
      page,
      limit,
      total,
      totalPages: Math.ceil(total / limit),
    },
  });
});
```

## Search/Filter Pattern

```typescript
const searchSchema = z.object({
  q: z.string().optional(),
  status: z.enum(['active', 'inactive', 'pending']).optional(),
  minAge: z.coerce.number().optional(),
  maxAge: z.coerce.number().optional(),
  tags: z.string().transform(s => s.split(',')).optional(),
});

app.get('/users/search', zValidator('query', searchSchema), async (c) => {
  const filters = c.req.valid('query');

  const users = await db.users.search({
    text: filters.q,
    where: {
      status: filters.status,
      age: {
        gte: filters.minAge,
        lte: filters.maxAge,
      },
      tags: filters.tags ? { hasSome: filters.tags } : undefined,
    },
  });

  return c.json(users);
});
```

## Nested Resources

```typescript
// /users/:userId/posts
const userPosts = new Hono()
  .get('/', async (c) => {
    const userId = c.req.param('userId');
    const posts = await db.posts.findMany({ where: { userId } });
    return c.json(posts);
  })
  .post('/', async (c) => {
    const userId = c.req.param('userId');
    const data = await c.req.json();
    const post = await db.posts.create({ ...data, userId });
    return c.json(post, 201);
  })
  .get('/:postId', async (c) => {
    const { userId, postId } = c.req.param();
    const post = await db.posts.findFirst({
      where: { id: postId, userId },
    });
    return post ? c.json(post) : c.notFound();
  });

app.route('/users/:userId/posts', userPosts);
```

## Batch Operations

```typescript
const batchSchema = z.object({
  ids: z.array(z.string()).min(1).max(100),
});

// Batch get
app.post('/users/batch', zValidator('json', batchSchema), async (c) => {
  const { ids } = c.req.valid('json');
  const users = await db.users.findMany({ where: { id: { in: ids } } });
  return c.json(users);
});

// Batch delete
app.delete('/users/batch', zValidator('json', batchSchema), async (c) => {
  const { ids } = c.req.valid('json');
  await db.users.deleteMany({ where: { id: { in: ids } } });
  return c.json({ deleted: ids.length });
});

// Batch update
const batchUpdateSchema = z.object({
  ids: z.array(z.string()),
  data: z.object({
    status: z.string().optional(),
    tags: z.array(z.string()).optional(),
  }),
});

app.patch('/users/batch', zValidator('json', batchUpdateSchema), async (c) => {
  const { ids, data } = c.req.valid('json');
  await db.users.updateMany({ where: { id: { in: ids } }, data });
  return c.json({ updated: ids.length });
});
```

## File Upload Pattern

```typescript
app.post('/upload', async (c) => {
  const body = await c.req.parseBody();
  const file = body['file'] as File;

  if (!file || !(file instanceof File)) {
    return c.json({ error: 'No file provided' }, 400);
  }

  // Validate file
  const maxSize = 10 * 1024 * 1024; // 10MB
  if (file.size > maxSize) {
    return c.json({ error: 'File too large' }, 400);
  }

  const allowedTypes = ['image/jpeg', 'image/png', 'image/webp'];
  if (!allowedTypes.includes(file.type)) {
    return c.json({ error: 'Invalid file type' }, 400);
  }

  // Upload to R2/S3
  const key = `uploads/${Date.now()}-${file.name}`;
  await c.env.BUCKET.put(key, file.stream(), {
    httpMetadata: { contentType: file.type },
  });

  return c.json({ url: `/files/${key}` }, 201);
});
```

## Streaming Response

```typescript
import { stream } from 'hono/streaming';

app.get('/stream', (c) => {
  return stream(c, async (stream) => {
    for (let i = 0; i < 10; i++) {
      await stream.write(`data: ${i}\n`);
      await stream.sleep(100);
    }
  });
});

// SSE (Server-Sent Events)
app.get('/events', (c) => {
  return stream(c, async (stream) => {
    c.header('Content-Type', 'text/event-stream');
    c.header('Cache-Control', 'no-cache');

    while (true) {
      const event = await getNextEvent();
      await stream.write(`data: ${JSON.stringify(event)}\n\n`);
    }
  });
});
```

## Webhook Handler

```typescript
import { createHmac } from 'crypto';

const verifyWebhook = (secret: string) => {
  return createMiddleware(async (c, next) => {
    const signature = c.req.header('X-Signature-256');
    const body = await c.req.text();

    const expected = createHmac('sha256', secret)
      .update(body)
      .digest('hex');

    if (signature !== `sha256=${expected}`) {
      return c.json({ error: 'Invalid signature' }, 401);
    }

    // Re-parse body for handler
    c.set('webhookBody', JSON.parse(body));
    await next();
  });
};

app.post('/webhooks/stripe', verifyWebhook(STRIPE_SECRET), async (c) => {
  const event = c.get('webhookBody');

  switch (event.type) {
    case 'payment_intent.succeeded':
      await handlePaymentSuccess(event.data);
      break;
    case 'customer.subscription.deleted':
      await handleSubscriptionCanceled(event.data);
      break;
  }

  return c.json({ received: true });
});
```

## Health Check Endpoints

```typescript
app.get('/health', (c) => {
  return c.json({ status: 'ok' });
});

app.get('/health/ready', async (c) => {
  try {
    // Check dependencies
    await db.$queryRaw`SELECT 1`;
    await cache.ping();

    return c.json({
      status: 'ready',
      checks: {
        database: 'ok',
        cache: 'ok',
      },
    });
  } catch (error) {
    return c.json({
      status: 'not ready',
      error: error.message,
    }, 503);
  }
});

app.get('/health/live', (c) => {
  return c.json({
    status: 'live',
    timestamp: new Date().toISOString(),
    version: process.env.VERSION ?? 'unknown',
  });
});
```
