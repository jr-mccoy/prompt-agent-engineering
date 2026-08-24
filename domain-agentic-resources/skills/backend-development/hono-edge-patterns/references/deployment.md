# Hono Deployment Guide

## Cloudflare Workers

### Setup

```bash
npm create hono@latest my-api -- --template cloudflare-workers
```

### Configuration (wrangler.toml)

```toml
name = "my-api"
main = "src/index.ts"
compatibility_date = "2024-01-01"
compatibility_flags = ["nodejs_compat"]

[vars]
ENVIRONMENT = "production"

[env.staging]
name = "my-api-staging"
vars = { ENVIRONMENT = "staging" }
```

### Deploy

```bash
# Development
npx wrangler dev

# Production
npx wrangler deploy

# Staging
npx wrangler deploy --env staging
```

### Type-safe Bindings

```typescript
type Bindings = {
  DB: D1Database;
  KV: KVNamespace;
  BUCKET: R2Bucket;
  API_KEY: string;
};

const app = new Hono<{ Bindings: Bindings }>();
```

---

## Cloudflare Pages (with Functions)

### Setup

```bash
npm create hono@latest my-site -- --template cloudflare-pages
```

### Configuration

```toml
# wrangler.toml
name = "my-site"
pages_build_output_dir = "./dist"

[[d1_databases]]
binding = "DB"
database_name = "my-db"
database_id = "xxx"
```

### File Structure

```
my-site/
├── app/
│   ├── routes/
│   │   ├── index.tsx
│   │   └── api/
│   │       └── users.ts
│   └── server.ts
├── public/
└── wrangler.toml
```

---

## Deno / Deno Deploy

### Setup

```bash
npm create hono@latest my-api -- --template deno
```

### Entry Point

```typescript
// main.ts
import { Hono } from 'https://deno.land/x/hono/mod.ts';

const app = new Hono();

app.get('/', (c) => c.text('Hello Deno!'));

Deno.serve(app.fetch);
```

### Deploy

```bash
# Local
deno run --allow-net main.ts

# Deno Deploy
deployctl deploy --project=my-project main.ts
```

---

## Bun

### Setup

```bash
npm create hono@latest my-api -- --template bun
```

### Entry Point

```typescript
// src/index.ts
import { Hono } from 'hono';

const app = new Hono();

app.get('/', (c) => c.text('Hello Bun!'));

export default app;
```

### Run

```bash
bun run src/index.ts
```

---

## Node.js

### Setup

```bash
npm create hono@latest my-api -- --template nodejs
```

### Entry Point

```typescript
// src/index.ts
import { serve } from '@hono/node-server';
import { Hono } from 'hono';

const app = new Hono();

app.get('/', (c) => c.text('Hello Node!'));

serve({
  fetch: app.fetch,
  port: 3000,
});

console.log('Server running at http://localhost:3000');
```

### Run

```bash
npx tsx src/index.ts
```

---

## Vercel Edge Functions

### Setup

```bash
npm create hono@latest my-api -- --template vercel
```

### File Structure

```
my-api/
├── api/
│   └── index.ts
├── package.json
└── vercel.json
```

### Entry Point

```typescript
// api/index.ts
import { Hono } from 'hono';
import { handle } from 'hono/vercel';

const app = new Hono().basePath('/api');

app.get('/', (c) => c.json({ message: 'Hello Vercel!' }));

export const GET = handle(app);
export const POST = handle(app);
```

### Configuration

```json
// vercel.json
{
  "rewrites": [
    { "source": "/api/(.*)", "destination": "/api" }
  ]
}
```

---

## AWS Lambda

### Setup

```bash
npm create hono@latest my-api -- --template aws-lambda
```

### Entry Point

```typescript
// src/index.ts
import { Hono } from 'hono';
import { handle } from 'hono/aws-lambda';

const app = new Hono();

app.get('/', (c) => c.json({ message: 'Hello Lambda!' }));

export const handler = handle(app);
```

### With AWS CDK

```typescript
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as nodejs from 'aws-cdk-lib/aws-lambda-nodejs';

new nodejs.NodejsFunction(this, 'HonoApi', {
  entry: 'src/index.ts',
  handler: 'handler',
  runtime: lambda.Runtime.NODEJS_20_X,
});
```

---

## Docker

### Dockerfile (Node.js)

```dockerfile
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:20-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
EXPOSE 3000
CMD ["node", "dist/index.js"]
```

### Dockerfile (Bun)

```dockerfile
FROM oven/bun:1 AS builder
WORKDIR /app
COPY package.json bun.lockb ./
RUN bun install --frozen-lockfile
COPY . .
RUN bun build src/index.ts --outdir ./dist --target bun

FROM oven/bun:1
WORKDIR /app
COPY --from=builder /app/dist ./dist
EXPOSE 3000
CMD ["bun", "run", "dist/index.js"]
```
