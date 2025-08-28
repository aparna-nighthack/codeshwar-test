
document.addEventListener('DOMContentLoaded', function() {
    // Initialize carousel
    initCarousel();

    // Attach form validation handler
    const form = document.querySelector('.contact-form');
    if(form) {
        form.addEventListener('submit', validateForm);
    }
});

function validateForm(event) {
    event.preventDefault();
    const form = event.currentTarget;
    const nameInput = document.querySelector('#name');
    const emailInput = document.querySelector('#email');
    const messageInput = document.querySelector('#message');
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    // Clear previous validation messages
    nameInput.setCustomValidity('');
    emailInput.setCustomValidity('');
    messageInput.setCustomValidity('');

    if (!nameInput.value.trim() || nameInput.value.length < 2 || !/^[a-zA-Z\s\-\'']+$/.test(nameInput.value)) {
        nameInput.setCustomValidity('Please enter a valid name (2 characters minimum; letters, spaces, hyphens, and apostrophes only).');
    }

    if (!emailPattern.test(emailInput.value)) {
        emailInput.setCustomValidity('Please enter a valid email address.');
    }

    if (!messageInput.value.trim() || messageInput.value.length < 10) {
        messageInput.setCustomValidity('Please enter a message with at least 10 characters.');
    }

    if (!nameInput.reportValidity() || !emailInput.reportValidity() || !messageInput.reportValidity()) {
        return; // Prevent submission if invalid
    }

    // Simulate form submission success
    alert('Form submitted successfully!');
    form.reset(); // Reset form after submission
}

function initCarousel() {
    const gallery = document.querySelector('.gallery');
    if (!gallery || gallery.querySelectorAll('img').length < 2) return;

    const images = gallery.querySelectorAll('img');
    let currentIndex = 0;
    images.forEach(img => img.style.display = 'none'); // Hide all images
    images[currentIndex].style.display = 'block'; // Show the first image

    gallery.addEventListener('click', () => {
        images[currentIndex].style.display = 'none'; // Hide current image
        currentIndex = (currentIndex + 1) % images.length;
        images[currentIndex].style.display = 'block'; // Show next image
    });

    document.addEventListener('keydown', (event) => {
        if(event.key === 'ArrowRight' || event.key === 'ArrowLeft') {
            images[currentIndex].style.display = 'none'; // Hide current image
            if(event.key === 'ArrowRight') {
                currentIndex = (currentIndex + 1) % images.length;
            } else {
                currentIndex = (currentIndex - 1 + images.length) % images.length; // Go to previous image, cycling back if at start
            }
            images[currentIndex].style.display = 'block'; // Show new current image
        }
    });

    gallery.setAttribute('tabindex', '0'); // Make gallery focusable

    images.forEach(img => {
        img.onerror = () => {
            img.src = 'https://via.placeholder.com/500?text=Image+Not+Found';
        };
    });
}