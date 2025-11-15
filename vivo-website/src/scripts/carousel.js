
class Carousel {
  constructor(selector) {
    this.carouselContainer = document.querySelector(selector);
    if (!this.carouselContainer) {
      console.warn(`Carousel container "${selector}" not found.`);
      return;
    }
    this.slides = this.carouselContainer.querySelectorAll('.carousel-slide');
    if (this.slides.length === 0) {
      console.warn("No slides found for the carousel.");
      return;
    }
    this.currentIndex = 0;
    this.isPlaying = true;
    this.initCarouselControls();
    this.initEventListeners();
    this.setInitialActiveSlide();
    this.adjustToScreenSize();
    this.play();
  }

  initCarouselControls() {
    const controlsHTML = `
      <button class="carousel-control prev" aria-label="Previous slide" type="button">&#10094;</button>
      <button class="carousel-control next" aria-label="Next slide" type="button">&#10095;</button>
    `;
    this.carouselContainer.insertAdjacentHTML('beforeend', controlsHTML);
  }

  initEventListeners() {
    const nextButton = this.carouselContainer.querySelector('.carousel-control.next');
    const prevButton = this.carouselContainer.querySelector('.carousel-control.prev');

    nextButton.addEventListener('click', () => this.pause() || this.nextSlide());
    prevButton.addEventListener('click', () => this.pause() || this.prevSlide());

    this.carouselContainer.addEventListener('mouseenter', () => this.pause(), {passive: true});
    this.carouselContainer.addEventListener('mouseleave', () => this.play(), {passive: true});

    window.addEventListener('resize', throttle(() => this.adjustToScreenSize(), 100), {passive: true});
    document.addEventListener('visibilitychange', () => {
      if (document.visibilityState === 'hidden') {
        this.pause();
      } else {
        this.play();
      }
    }, {passive: true});
  }

  setInitialActiveSlide() {
    const hasActiveSlide = Array.from(this.slides).some(slide => slide.classList.contains('active'));
    if (!hasActiveSlide) {
      this.slides[0].classList.add('active');
    }
  }

  play() {
    if (!this.isPlaying) {
      this.isPlaying = true;
      this.slideInterval = setInterval(() => this.nextSlide(), 3000);
    }
  }

  pause() {
    if (this.isPlaying) {
      this.isPlaying = false;
      clearInterval(this.slideInterval);
    }
  }

  nextSlide() {
    this.pause();
    this.goToSlide(this.currentIndex + 1);
    setTimeout(() => this.play(), 500); // Debounce next slide
  }

  prevSlide() {
    this.pause();
    this.goToSlide(this.currentIndex - 1);
    setTimeout(() => this.play(), 500); // Debounce previous slide
  }

  goToSlide(index) {
    if (index < 0) index = this.slides.length - 1;
    if (index >= this.slides.length) index = 0;
    this.slides.forEach((slide, i) => {
      slide.classList.toggle('active', i === index);
      slide.setAttribute('aria-hidden', i !== index);
      slide.setAttribute('aria-current', i === index ? 'true' : 'false');
    });
    this.currentIndex = index;
  }

  adjustToScreenSize() {
    const slideWidth = this.carouselContainer.clientWidth;
    const activeSlideHeight = this.slides[this.currentIndex].offsetHeight;
    this.carouselContainer.style.height = `${activeSlideHeight}px`;
    this.slides.forEach(slide => {
      slide.style.width = `${slideWidth}px`;
    });
  }
}

document.addEventListener('DOMContentLoaded', () => {
  const carousel = new Carousel('.carousel');
});