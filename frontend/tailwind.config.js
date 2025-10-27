/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        // Palette inspirée ANCAR
        primary: {
          DEFAULT: '#2E7D32',
          50: '#E8F5E9',
          100: '#C8E6C9',
          200: '#A5D6A7',
          300: '#81C784',
          400: '#66BB6A',
          500: '#4CAF50',
          600: '#43A047',
          700: '#388E3C',
          800: '#2E7D32',
          900: '#1B5E20',
        },
        secondary: {
          DEFAULT: '#4CAF50',
          light: '#81C784',
          dark: '#388E3C',
        },
        earth: {
          DEFAULT: '#8D6E63',
          50: '#EFEBE9',
          100: '#D7CCC8',
          200: '#BCAAA4',
          300: '#A1887F',
          400: '#8D6E63',
          500: '#795548',
          600: '#6D4C41',
          700: '#5D4037',
          800: '#4E342E',
          900: '#3E2723',
        },
        charcoal: '#2C2C2C',
      },
      fontFamily: {
        sans: ['Open Sans', 'Source Sans Pro', 'sans-serif'],
        heading: ['Roboto', 'Montserrat', 'sans-serif'],
      },
      fontSize: {
        'h1': '2.5rem',
        'h2': '2rem',
        'h3': '1.5rem',
      },
      spacing: {
        '18': '4.5rem',
        '88': '22rem',
        '128': '32rem',
      },
      borderRadius: {
        'xl': '1rem',
        '2xl': '1.5rem',
      },
      boxShadow: {
        'soft': '0 2px 15px rgba(0, 0, 0, 0.1)',
        'medium': '0 4px 20px rgba(0, 0, 0, 0.15)',
      },
    },
  },
  plugins: [],
}
