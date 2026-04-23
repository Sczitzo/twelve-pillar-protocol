import type { Config } from 'tailwindcss'

export default {
  content: ['./index.html', './src/**/*.{ts,tsx}'],
  theme: {
    extend: {
      fontFamily: {
        mono: ['"IBM Plex Mono"', '"SFMono-Regular"', 'Menlo', 'monospace'],
        sans: ['"Aptos"', '"Avenir Next"', '"Segoe UI"', 'sans-serif'],
        serif: ['"Iowan Old Style"', '"Palatino Linotype"', '"Book Antiqua"', '"Baskerville"', 'Georgia', 'serif'],
      },
    },
  },
  plugins: [],
} satisfies Config
