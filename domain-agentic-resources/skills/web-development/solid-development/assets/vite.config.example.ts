import { defineConfig } from 'vite';
import solidPlugin from 'vite-plugin-solid';
import path from 'path';

export default defineConfig({
  plugins: [solidPlugin()],

  server: {
    port: 3000,
    host: true,
  },

  build: {
    target: 'esnext',
    minify: 'esbuild',
    sourcemap: true,
  },

  resolve: {
    alias: {
      '~': path.resolve(__dirname, './src'),
    },
  },

  // CSS configuration
  css: {
    modules: {
      localsConvention: 'camelCase',
    },
  },

  // Environment variables
  envPrefix: 'APP_',

  // Optimize dependencies
  optimizeDeps: {
    include: ['solid-js'],
  },
});
