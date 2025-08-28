# Vivo Website Project Documentation

## Overview

The Vivo website project is designed to showcase Vivo's latest smartphones, highlighting their innovative features and elegant designs. The primary goal is to provide users with detailed information about Vivo's flagship devices, including the X100 Pro, V30, and T3 5G, and to present key features such as the Zeiss camera and 120W charging through an interactive carousel. The website aims to engage users with vibrant, brand-appropriate colors and a user-friendly interface that includes "Shop Now" and "Watch Demo" buttons for each product.

## Main Technologies Used

- **HTML**: Used for structuring the content of the website.
- **CSS**: Employed to style the website, ensuring responsiveness and alignment with Vivo's branding.
- **JavaScript**: Utilized for dynamic content interaction, especially in the carousel functionality.

## Project Setup

### Local Development

1. **Clone the repository**: Begin by cloning the repository to your local machine using `git clone <repository-url>`.
2. **Navigate to the project directory**: Change into the project directory with `cd vivo-website`.

### Running a Local Development Server

To view the website locally, you can use a simple HTTP server. If you have Python installed, you can quickly start a server with the following command:

```bash
# For Python 3.x
python -m http.server
```

Navigate to `http://localhost:8000/public/` in your web browser to view the project.

### Compiling SCSS (If Used)

This project uses plain CSS for styling. However, if SCSS were to be used, you would need to compile it to CSS using a tool like Sass:

```bash
sass --watch src/styles/main.scss:src/styles/main.css
```

### Deployment

To deploy the project to a live environment, you can use services like Netlify, Vercel, or GitHub Pages. Ensure you configure the project to point to the `public/` directory as the root.

## File Links and Descriptions

- **index.html** (`public/index.html`): The entry point of the website. It contains the HTML structure for showcasing Vivo's latest phones, their features, offers, testimonials, and a contact form.

- **main.css (source)** (`src/styles/main.css`): Source CSS file that styles the website, ensuring responsiveness and alignment with Vivo's branding. It styles elements like the navigation bar, hero section, device showcases, carousel, and footer.
- **main.css (public)** (`public/styles/main.css`): Deployable CSS file used in the production environment.

- **carousel.js (source)** (`src/scripts/carousel.js`): Source JavaScript file that implements the interactive carousel for showcasing key features of Vivo phones. Utilizes ES module imports & exports.
- **carousel.js (public)** (`public/scripts/carousel.js`): Deployable JavaScript file for the carousel functionality that must be loaded as a module.

- **utils.js (source)** (`src/scripts/utils.js`): Contains utility functions such as throttle, used by carousel.js for performance optimization.
- **utils.js (public)** (`public/scripts/utils.js`): Deployable version of utility functions available for carousel.js imports.

**Note**: The `public` directory is the site root for local viewing and deployment. The carousel script uses ES module imports, importing `throttle` from `utils.js`, requiring it to be loaded as a module in the browser with `utils.js` available at the correct relative path under `public/scripts/` for the import to work.

### Carousel Markup Requirements

- The carousel container must have the class "carousel".
- Each slide element must use the class "carousel-slide" (not "carousel-item") for the script to detect the slides.
- The script sets and toggles `aria-hidden` and `aria-current` on slides and will set an initial active slide if none is present.
- The carousel script programmatically injects Prev/Next controls into the carousel container. Do not manually add these controls in markup to avoid duplication. 

**Note:** If you keep a mention of `aria-controls` or the "feature-carousel" id in the README, clarify these are used only for accessibility in markup and not by the carousel script itself (which targets the container by ".carousel" and slides by ".carousel-slide").

## Adherence to Plan

### How files interact

- `index.html` is the entry point under `public/` and references assets under `public/styles` and `public/scripts`.
- `carousel.js` (ES module) imports `throttle` from `utils.js` and binds event listeners to the carousel container and controls; it also injects the control buttons automatically.
- `main.css` styles the classes used by the markup and the carousel; ensure styling also covers ".carousel-slide" since that is the class the script expects for slides.

### Project Structure

The project is structured into `public/` (deployable, server root) vs `src/` (source) directories. Files referenced by the page are under `public/`.

### Running a Local Development Server

You can open `public/index.html` directly in the browser or via `http://localhost:8000/public/`, and the assets should resolve from `public/styles` and `public/scripts`.

## Conclusion

This documentation provides an overview of the Vivo website project, including its purpose, technologies used, and setup instructions. By following the steps outlined, you can set up the project locally, run a development server, and deploy the website to a live environment.