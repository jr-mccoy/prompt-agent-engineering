// vite.config.ts
// Complete example Vite configuration for a Qwik project

import { defineConfig, type UserConfig } from 'vite';
import { qwikVite } from '@builder.io/qwik/optimizer';
import { qwikCity } from '@builder.io/qwik-city/vite';
import tsconfigPaths from 'vite-tsconfig-paths';

export default defineConfig((): UserConfig => {
  return {
    // ===================
    // PLUGINS
    // ===================
    plugins: [
      // QwikCity plugin (routing, middleware, etc.)
      qwikCity(),

      // Qwik optimizer ($ transformations, lazy loading)
      qwikVite(),

      // TypeScript path aliases
      tsconfigPaths(),
    ],

    // ===================
    // DEV SERVER
    // ===================
    server: {
      port: 5173,
      host: true, // Listen on all interfaces

      // Enable HTTPS for local dev (optional)
      // https: {
      //   key: fs.readFileSync('localhost-key.pem'),
      //   cert: fs.readFileSync('localhost.pem'),
      // },

      // Proxy API requests (optional)
      proxy: {
        '/api/external': {
          target: 'https://api.example.com',
          changeOrigin: true,
          rewrite: (path) => path.replace(/^\/api\/external/, ''),
        },
      },

      // File watching
      watch: {
        // Ignore large directories
        ignored: ['**/node_modules/**', '**/dist/**'],
      },
    },

    // ===================
    // PREVIEW SERVER
    // ===================
    preview: {
      port: 4173,
      host: true,
      headers: {
        // Security headers for preview
        'X-Content-Type-Options': 'nosniff',
        'X-Frame-Options': 'DENY',
      },
    },

    // ===================
    // BUILD OPTIONS
    // ===================
    build: {
      // Target modern browsers
      target: 'es2020',

      // Enable module preloading
      modulePreload: {
        polyfill: true,
      },

      // Minification options
      minify: 'esbuild',

      // Source maps for production (optional)
      sourcemap: false,

      // Rollup options
      rollupOptions: {
        output: {
          // Manual chunk splitting for vendor code
          manualChunks: {
            // Example: Group specific packages
            // 'vendor': ['some-large-package'],
          },
        },
      },

      // Chunk size warnings
      chunkSizeWarningLimit: 500, // KB

      // Asset handling
      assetsInlineLimit: 4096, // 4KB - inline smaller assets
    },

    // ===================
    // OPTIMIZATION
    // ===================
    optimizeDeps: {
      // Force include packages that might not be detected
      include: [
        // Add packages that need pre-bundling
      ],

      // Exclude packages from pre-bundling
      exclude: [
        // Qwik handles its own optimization
      ],
    },

    // ===================
    // SSR OPTIONS
    // ===================
    ssr: {
      // Packages that should not be externalized in SSR
      noExternal: [
        // Add packages that don't work as externals
        // '@some-package',
      ],
    },

    // ===================
    // RESOLVE
    // ===================
    resolve: {
      alias: {
        // Path aliases (also defined in tsconfig.json)
        '~': '/src',
        '@components': '/src/components',
        '@routes': '/src/routes',
        '@utils': '/src/utils',
        '@hooks': '/src/hooks',
      },
    },

    // ===================
    // CSS
    // ===================
    css: {
      // PostCSS config
      postcss: './postcss.config.js',

      // CSS modules options
      modules: {
        localsConvention: 'camelCase',
        generateScopedName: '[name]__[local]___[hash:base64:5]',
      },

      // Preprocessor options
      preprocessorOptions: {
        scss: {
          additionalData: `@import "./src/styles/variables.scss";`,
        },
      },
    },

    // ===================
    // ENVIRONMENT
    // ===================
    envPrefix: 'PUBLIC_', // Only expose vars prefixed with PUBLIC_

    // ===================
    // LOGGING
    // ===================
    logLevel: 'info', // 'info' | 'warn' | 'error' | 'silent'

    // Clear console on dev server restart
    clearScreen: true,
  };
});
