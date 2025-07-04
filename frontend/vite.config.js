// frontend/vite.config.js
import { defineConfig } from 'vite';
import svelte from '@sveltejs/vite-plugin-svelte';

export default defineConfig({
  plugins: [svelte()],
  server: {
    proxy: {
      '/api/login': {
        target: 'http://auth:8000',
        changeOrigin: true,
        rewrite: path => path.replace(/^\/api\/login/, '/login'),
      },
      '/api/todos': {
        target: 'http://todo:8000',
        changeOrigin: true,
        rewrite: path => path.replace(/^\/api\/todos/, '/todos'),
      },
      '/api/posts': {
        target: 'http://board:8000',
        changeOrigin: true,
        rewrite: path => path.replace(/^\/api\/posts/, '/posts'),
      }
    }
  }
});
