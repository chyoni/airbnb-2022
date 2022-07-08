/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html", "./templates/*.html"],
  theme: {
    extend: {
      fontFamily: {
        ayuthaya: ["Ayuthaya"],
        roboto: ["Roboto", "sans-serif"],
        opensans: ["Open Sans", "sans-serif"],
        sanspro: ["Source Sans Pro", "sans-serif"],
      },
    },
  },
  plugins: [],
};
