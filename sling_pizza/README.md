# Sling Pizza Website Project

Welcome to the Sling Pizza website project! This README provides a comprehensive guide on how to set up the project locally, understand its structure, and contribute to its development. Whether you're looking to run the site locally for development purposes or interested in enhancing its features, you'll find all the necessary information here.

## Table of Contents

- [Project Structure](#project-structure)
- [Setting Up Locally](#setting-up-locally)
- [Future Enhancements](#future-enhancements)
- [External Resources](#external-resources)

## Project Structure

The project is structured into three main files, each serving a distinct purpose in the creation of the Sling Pizza website:

- `index.html` (root): This is the entry point of the website. It defines the structure of the webpage, including the header with the brand logo and navigation links, a main section showcasing a gallery of pizza images, and a footer containing a contact form for orders and product inquiries.

- `styles/main.css`: This stylesheet file is responsible for the visual appearance of the website. It includes styles for the header, the pizza image gallery in the main section, and the contact form in the footer. CSS variables are used to maintain a consistent color scheme and font styling across the site. Media queries ensure the website is responsive and provides a good user experience on devices of various sizes.

- `scripts/main.js`: This JavaScript file adds interactivity to the website. It includes form validation logic to ensure user input is correctly formatted, especially for the email field in the contact form. Additionally, it implements a simple image carousel for the pizza gallery in the main section, enhancing the user's interaction with the site.

### Key selectors and IDs

- The contact form uses the class `contact-form` and its fields are identified by the IDs `name`, `email`, and `message`.
- The “Contact” navigation link targets the footer with the ID `contact`.
- The pizza gallery is wrapped in a container element with the class `gallery` and each item/image block uses the class `gallery-item`.

## Setting Up Locally

To run the Sling Pizza website locally, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. If you don't have a simple HTTP server installed, you can use Python's built-in HTTP server. Run the following command in your terminal:

   For Python 3.x:
   ```bash
   python -m http.server
   ```

   For Python 2.x:
   ```bash
   python -m SimpleHTTPServer
   ```

4. Open your web browser and go to `http://localhost:8000` to view the site.

## Future Enhancements

While the initial setup of the Sling Pizza website provides a solid foundation, there are several potential enhancements that could be made to improve the site further:

- Implementing a backend to process orders and inquiries submitted through the contact form.
- Adding a dynamic menu page that allows users to browse the pizza offerings and place orders directly from the website.
- Integrating with social media platforms to allow users to share their favorite pizzas and experiences at Sling Pizza.
- Incorporating user reviews and ratings for different pizza varieties.

## External Resources

The following external resources were used in the development of this project:

- Pizza Images:
  - [Image 1](https://imgmediagumlet.lbb.in/media/2020/11/5fa17943d511fc4b649fcfc2_1604417859096.jpg)
  - [Image 2](https://curlytales.com/wp-content/uploads/2019/09/pizza-feature.jpg)
  - [Image 3](https://bhukkadcompany.com/wp/wp-content/uploads/2024/06/21-Best-Pizzas-in-Mumbai-You-Must-Try-A-Pizza-Lovers-Paradise-1-710x473.png)

No external libraries were used in the initial setup of this project.

Thank you for your interest in the Sling Pizza website project. Happy coding!