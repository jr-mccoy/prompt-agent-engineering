# Astro Configuration Reference

Complete reference for `astro.config.mjs` options.

## Configuration Schema

```typescript
interface AstroUserConfig {
  // Core
  root?: string;
  srcDir?: string;
  publicDir?: string;
  outDir?: string;
  cacheDir?: string;
  site?: string;
  compressHTML?: boolean;
  base?: string;
  trailingSlash?: 'always' | 'never' | 'ignore';
  output?: 'static' | 'server' | 'hybrid';
  adapter?: AstroIntegration;

  // Integrations
  integrations?: AstroIntegration[];

  // Build
  build?: {
    format?: 'file' | 'directory';
    client?: string;
    server?: string;
    assets?: string;
    serverEntry?: string;
    redirects?: boolean;
    inlineStylesheets?: 'always' | 'auto' | 'never';
    assetsPrefix?: string;
  };

  // Server
  server?: {
    host?: boolean | string;
    port?: number;
    headers?: Record<string, string>;
  };

  // Image
  image?: {
    endpoint?: string;
    service?: ImageService;
    domains?: string[];
    remotePatterns?: RemotePattern[];
  };

  // Markdown
  markdown?: {
    drafts?: boolean;
    syntaxHighlight?: 'shiki' | 'prism' | false;
    shikiConfig?: ShikiConfig;
    remarkPlugins?: RemarkPlugin[];
    rehypePlugins?: RehypePlugin[];
    gfm?: boolean;
    smartypants?: boolean;
  };

  // Vite
  vite?: ViteUserConfig;

  // Redirects
  redirects?: Record<string, string | RedirectConfig>;

  // i18n
  i18n?: {
    defaultLocale: string;
    locales: string[];
    routing?: {
      prefixDefaultLocale?: boolean;
      redirectToDefaultLocale?: boolean;
    };
    fallback?: Record<string, string>;
  };

  // Prefetch
  prefetch?: boolean | {
    prefetchAll?: boolean;
    defaultStrategy?: 'tap' | 'hover' | 'viewport' | 'load';
  };

  // Experimental
  experimental?: {
    contentCollectionCache?: boolean;
    directRenderScript?: boolean;
    globalRoutePriority?: boolean;
  };
}
```

## Detailed Options

### Core Options

#### `site`
**Type:** `string`

Your deployed site URL. Used for generating canonical URLs, sitemaps, and RSS feeds.

```javascript
export default defineConfig({
  site: 'https://example.com',
});
```

#### `base`
**Type:** `string` | **Default:** `/`

Base path for deployment. Required when deploying to a subdirectory.

```javascript
export default defineConfig({
  base: '/docs', // Site deployed at example.com/docs/
});
```

#### `output`
**Type:** `'static' | 'server' | 'hybrid'` | **Default:** `'static'`

| Mode | Description | Use Case |
|------|-------------|----------|
| `static` | Pre-render all pages at build | Blogs, docs, marketing |
| `server` | Render on demand | Dynamic apps, personalization |
| `hybrid` | Static default, opt-in SSR | Mixed requirements |

```javascript
import vercel from '@astrojs/vercel/serverless';

export default defineConfig({
  output: 'hybrid',
  adapter: vercel(),
});
```

#### `trailingSlash`
**Type:** `'always' | 'never' | 'ignore'` | **Default:** `'ignore'`

Control trailing slashes in URLs:

```javascript
export default defineConfig({
  trailingSlash: 'always', // /about/
  // trailingSlash: 'never', // /about
  // trailingSlash: 'ignore', // Both work
});
```

### Build Options

#### `build.format`
**Type:** `'file' | 'directory'` | **Default:** `'directory'`

```javascript
export default defineConfig({
  build: {
    format: 'file', // /about.html
    // format: 'directory', // /about/index.html
  },
});
```

#### `build.inlineStylesheets`
**Type:** `'always' | 'auto' | 'never'` | **Default:** `'auto'`

```javascript
export default defineConfig({
  build: {
    inlineStylesheets: 'always', // Inline all CSS
  },
});
```

### Server Options

#### Development server configuration

```javascript
export default defineConfig({
  server: {
    port: 4321,
    host: true, // Listen on all addresses
    headers: {
      'Access-Control-Allow-Origin': '*',
    },
  },
});
```

### Markdown Options

#### Syntax Highlighting

```javascript
export default defineConfig({
  markdown: {
    syntaxHighlight: 'shiki',
    shikiConfig: {
      theme: 'github-dark',
      themes: {
        light: 'github-light',
        dark: 'github-dark',
      },
      wrap: true,
    },
  },
});
```

#### Remark/Rehype Plugins

```javascript
import remarkToc from 'remark-toc';
import rehypeSlug from 'rehype-slug';

export default defineConfig({
  markdown: {
    remarkPlugins: [
      remarkToc,
      [remarkPlugin, { option: true }],
    ],
    rehypePlugins: [
      rehypeSlug,
    ],
  },
});
```

### i18n Options

```javascript
export default defineConfig({
  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'es', 'fr'],
    routing: {
      prefixDefaultLocale: false, // /about (en), /es/about, /fr/about
    },
    fallback: {
      es: 'en',
      fr: 'en',
    },
  },
});
```

### Redirects

```javascript
export default defineConfig({
  redirects: {
    '/old-page': '/new-page',
    '/blog/[...slug]': '/articles/[...slug]',
    '/external': {
      status: 302,
      destination: 'https://external.com',
    },
  },
});
```

### Prefetch Options

```javascript
export default defineConfig({
  prefetch: {
    prefetchAll: false,
    defaultStrategy: 'hover', // 'tap' | 'hover' | 'viewport' | 'load'
  },
});
```

## Environment Variables

### Built-in Variables

| Variable | Description |
|----------|-------------|
| `import.meta.env.MODE` | `development` or `production` |
| `import.meta.env.PROD` | `true` in production |
| `import.meta.env.DEV` | `true` in development |
| `import.meta.env.SITE` | `site` value from config |
| `import.meta.env.BASE_URL` | `base` value from config |

### Custom Variables

Create `.env` files:
```bash
# .env
PUBLIC_API_URL=https://api.example.com
SECRET_API_KEY=secret123
```

Access in code:
```typescript
// Public (available on client)
const apiUrl = import.meta.env.PUBLIC_API_URL;

// Secret (server-only)
const apiKey = import.meta.env.SECRET_API_KEY;
```

## TypeScript Configuration

Recommended `tsconfig.json`:

```json
{
  "extends": "astro/tsconfigs/strict",
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"],
      "@components/*": ["src/components/*"],
      "@layouts/*": ["src/layouts/*"]
    }
  }
}
```
