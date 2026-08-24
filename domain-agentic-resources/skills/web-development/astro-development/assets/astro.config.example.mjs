// astro.config.mjs
// Complete example configuration for a production Astro site

import { defineConfig } from 'astro/config';

// Framework integrations
import react from '@astrojs/react';
import tailwind from '@astrojs/tailwind';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';

// Deployment adapter (choose one)
import vercel from '@astrojs/vercel/serverless';
// import netlify from '@astrojs/netlify';
// import cloudflare from '@astrojs/cloudflare';
// import node from '@astrojs/node';

// Remark/Rehype plugins
import remarkToc from 'remark-toc';
import rehypeSlug from 'rehype-slug';
import rehypeAutolinkHeadings from 'rehype-autolink-headings';

export default defineConfig({
  // ===================
  // CORE CONFIGURATION
  // ===================

  // Production site URL (required for sitemap, canonical URLs)
  site: 'https://example.com',

  // Base path if deploying to subdirectory
  // base: '/docs',

  // Output mode: 'static' | 'server' | 'hybrid'
  output: 'hybrid',

  // Deployment adapter (required for 'server' or 'hybrid' output)
  adapter: vercel({
    // Vercel-specific options
    webAnalytics: { enabled: true },
    imageService: true,
    // functionPerRoute: true, // For individual serverless functions
  }),

  // Trailing slash behavior: 'always' | 'never' | 'ignore'
  trailingSlash: 'never',

  // Compress HTML output
  compressHTML: true,

  // ===================
  // INTEGRATIONS
  // ===================

  integrations: [
    // React support
    react({
      // Include React DevTools in dev
      // experimentalReactChildren: true,
    }),

    // Tailwind CSS
    tailwind({
      // Don't apply Tailwind's base styles
      applyBaseStyles: false,
      // Path to Tailwind config
      configFile: './tailwind.config.mjs',
    }),

    // MDX support
    mdx({
      // Inherit markdown config
      extendMarkdownConfig: true,
      // Additional remark plugins for MDX only
      remarkPlugins: [],
      rehypePlugins: [],
    }),

    // Sitemap generation
    sitemap({
      // Filter pages from sitemap
      filter: (page) => !page.includes('/admin/'),
      // Custom serialization
      serialize: (item) => ({
        ...item,
        changefreq: 'weekly',
        priority: 0.7,
      }),
    }),
  ],

  // ===================
  // BUILD CONFIGURATION
  // ===================

  build: {
    // Output format: 'file' (/about.html) or 'directory' (/about/index.html)
    format: 'directory',

    // Inline CSS stylesheets: 'always' | 'auto' | 'never'
    inlineStylesheets: 'auto',

    // Assets directory name
    assets: '_assets',

    // Redirects handling
    redirects: true,
  },

  // ===================
  // DEV SERVER
  // ===================

  server: {
    port: 4321,
    host: true, // Listen on all network interfaces

    // Custom headers for dev server
    headers: {
      'Access-Control-Allow-Origin': '*',
    },
  },

  // ===================
  // MARKDOWN
  // ===================

  markdown: {
    // Syntax highlighting: 'shiki' | 'prism' | false
    syntaxHighlight: 'shiki',

    shikiConfig: {
      // Theme for code blocks
      theme: 'github-dark',

      // Dual themes for light/dark mode
      themes: {
        light: 'github-light',
        dark: 'github-dark',
      },

      // Wrap long lines
      wrap: true,

      // Additional languages
      langs: [],
    },

    // Remark plugins (Markdown processing)
    remarkPlugins: [
      [remarkToc, { heading: 'contents', maxDepth: 3 }],
    ],

    // Rehype plugins (HTML processing)
    rehypePlugins: [
      rehypeSlug,
      [rehypeAutolinkHeadings, { behavior: 'wrap' }],
    ],

    // GitHub Flavored Markdown
    gfm: true,

    // Smart quotes and dashes
    smartypants: true,
  },

  // ===================
  // IMAGE OPTIMIZATION
  // ===================

  image: {
    // Allowed remote image domains
    domains: ['images.unsplash.com', 'cdn.example.com'],

    // Remote patterns for more control
    remotePatterns: [
      {
        protocol: 'https',
        hostname: '**.cloudinary.com',
      },
    ],
  },

  // ===================
  // INTERNATIONALIZATION
  // ===================

  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'es', 'fr', 'de'],

    routing: {
      // Don't prefix default locale: /about (en), /es/about
      prefixDefaultLocale: false,
    },

    // Fallback locales for missing translations
    fallback: {
      es: 'en',
      fr: 'en',
      de: 'en',
    },
  },

  // ===================
  // PREFETCHING
  // ===================

  prefetch: {
    // Don't prefetch all links by default
    prefetchAll: false,

    // Default strategy: 'tap' | 'hover' | 'viewport' | 'load'
    defaultStrategy: 'hover',
  },

  // ===================
  // REDIRECTS
  // ===================

  redirects: {
    // Simple redirects
    '/old-blog': '/blog',
    '/posts/[...slug]': '/blog/[...slug]',

    // With status codes
    '/legacy': {
      status: 301,
      destination: '/new-location',
    },

    // External redirects
    '/github': {
      status: 302,
      destination: 'https://github.com/example',
    },
  },

  // ===================
  // VITE CONFIGURATION
  // ===================

  vite: {
    // Custom Vite plugins
    plugins: [],

    // Build optimizations
    build: {
      // Rollup options
      rollupOptions: {
        output: {
          // Manual chunk splitting
          manualChunks: {
            'react-vendor': ['react', 'react-dom'],
          },
        },
      },
    },

    // SSR configuration
    ssr: {
      // Packages to not externalize in SSR
      noExternal: ['@radix-ui/*'],
    },

    // Optimization
    optimizeDeps: {
      // Force include packages
      include: ['lodash-es'],
      // Force exclude packages
      exclude: ['fsevents'],
    },

    // Resolve aliases
    resolve: {
      alias: {
        '@': '/src',
        '@components': '/src/components',
        '@layouts': '/src/layouts',
        '@utils': '/src/utils',
      },
    },
  },

  // ===================
  // EXPERIMENTAL FEATURES
  // ===================

  experimental: {
    // Cache content collections for faster builds
    contentCollectionCache: true,

    // Direct script rendering (improved script handling)
    directRenderScript: true,
  },
});
