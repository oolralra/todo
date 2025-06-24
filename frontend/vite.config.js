import { svelte } from '@sveltejs/vite-plugin-svelte';

export default {
  plugins: [svelte()],
  server: {
    host: true,
    port: 5173,
    proxy: {
      '/api': {
        target: 'http://backend:8000',
        changeOrigin: true,
        rewrite: path => path.replace(/^\/api/, '')
      }
    }
  }
};

