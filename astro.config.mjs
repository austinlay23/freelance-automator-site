// @ts-check
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
  site: 'https://austinlay23.github.io/freelance-automator-site',
  base: '/freelance-automator-site/',
  integrations: [mdx(), sitemap()],
});
