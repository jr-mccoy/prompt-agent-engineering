# Hono Middleware Reference

## Built-in Middleware

### CORS

```typescript
import { cors } from 'hono/cors';

app.use('/api/*', cors({
  origin: 'https://example.com',
  allowHeaders: ['Content-Type', 'Authorization'],
  allowMethods: ['GET', 'POST', 'PUT', 'DELETE'],
  exposeHeaders: ['X-Total-Count'],
  maxAge: 600,
  credentials: true,
}));
```

### Logger

```typescript
import { logger } from 'hono/logger';

app.use('*', logger());
// Output: GET /users 200 12ms
```

### Pretty JSON

```typescript
import { prettyJSON } from 'hono/pretty-json';

app.use('*', prettyJSON());
// Formats JSON with ?pretty query param
```

### Basic Auth

```typescript
import { basicAuth } from 'hono/basic-auth';

app.use('/admin/*', basicAuth({
  username: 'admin',
  password: 'secret',
  realm: 'Admin Area',
}));
```

### Bearer Auth

```typescript
import { bearerAuth } from 'hono/bearer-auth';

app.use('/api/*', bearerAuth({
  token: 'my-secret-token',
  // Or async verification
  verifyToken: async (token) => {
    return token === await getValidToken();
  },
}));
```

### JWT

```typescript
import { jwt } from 'hono/jwt';

app.use('/api/*', jwt({
  secret: 'my-secret',
  alg: 'HS256',
}));

app.get('/api/profile', (c) => {
  const payload = c.get('jwtPayload');
  return c.json(payload);
});
```

### Secure Headers

```typescript
import { secureHeaders } from 'hono/secure-headers';

app.use('*', secureHeaders({
  xFrameOptions: 'DENY',
  xXssProtection: '1',
  contentSecurityPolicy: {
    defaultSrc: ["'self'"],
    scriptSrc: ["'self'", 'https://cdn.example.com'],
  },
}));
```

### Compression

```typescript
import { compress } from 'hono/compress';

app.use('*', compress());
// Automatically compresses responses > 1KB
```

### ETag

```typescript
import { etag } from 'hono/etag';

app.use('*', etag());
// Adds ETag headers for caching
```

### Cache

```typescript
import { cache } from 'hono/cache';

app.use('/static/*', cache({
  cacheName: 'static-assets',
  cacheControl: 'max-age=3600',
  wait: true,
}));
```

### Timeout

```typescript
import { timeout } from 'hono/timeout';

app.use('/api/*', timeout(5000)); // 5 second timeout
```

### Rate Limiting (with KV)

```typescript
import { rateLimiter } from 'hono-rate-limiter';

app.use(rateLimiter({
  windowMs: 60 * 1000, // 1 minute
  max: 100, // 100 requests per window
  keyGenerator: (c) => c.req.header('CF-Connecting-IP') ?? 'unknown',
}));
```

## Third-Party Middleware

### Zod Validator

```typescript
import { zValidator } from '@hono/zod-validator';
import { z } from 'zod';

const schema = z.object({
  name: z.string(),
  email: z.string().email(),
});

app.post('/users', zValidator('json', schema), (c) => {
  const data = c.req.valid('json');
  return c.json(data);
});
```

### Sentry Integration

```typescript
import { sentry } from '@hono/sentry';

app.use('*', sentry({
  dsn: 'https://xxx@sentry.io/xxx',
}));
```

## Creating Custom Middleware

### Basic Pattern

```typescript
import { createMiddleware } from 'hono/factory';

const myMiddleware = createMiddleware(async (c, next) => {
  // Before handler
  console.log('Request:', c.req.url);

  await next();

  // After handler
  console.log('Response:', c.res.status);
});
```

### With Options

```typescript
type MiddlewareOptions = {
  header: string;
  required: boolean;
};

const apiKeyAuth = (options: MiddlewareOptions) => {
  return createMiddleware(async (c, next) => {
    const key = c.req.header(options.header);

    if (options.required && !key) {
      return c.json({ error: 'API key required' }, 401);
    }

    await next();
  });
};

app.use('/api/*', apiKeyAuth({ header: 'X-API-Key', required: true }));
```

### With Context Variables

```typescript
type Env = {
  Variables: {
    requestId: string;
    startTime: number;
  };
};

const requestIdMiddleware = createMiddleware<Env>(async (c, next) => {
  c.set('requestId', crypto.randomUUID());
  c.set('startTime', Date.now());

  await next();

  c.header('X-Request-Id', c.get('requestId'));
  c.header('X-Response-Time', `${Date.now() - c.get('startTime')}ms`);
});
```

## Middleware Composition

```typescript
import { compose } from 'hono/compose';

const apiMiddleware = compose([
  cors(),
  logger(),
  bearerAuth({ token: 'secret' }),
  rateLimiter({ max: 100 }),
]);

app.use('/api/*', apiMiddleware);
```

## Conditional Middleware

```typescript
import { every, some } from 'hono/combine';

// Run if ALL conditions pass
app.use('/admin/*', every(
  isAuthenticated,
  isAdmin,
  hasPermission('admin:write')
));

// Run if ANY condition passes
app.use('/content/*', some(
  isAuthenticated,
  hasApiKey
));
```
