
const zoomContainer = document.getElementById('zoom-container');
const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        zoomContainer.classList.add('zoom-in', 'active');
      } else {
        zoomContainer.classList.remove('zoom-in', 'active');
      }
    });
  });

observer.observe(zoomContainer);

  const slider = document.querySelector('.slider');
  const slides = document.querySelectorAll('.slide');
  let currentSlide = 0;

  function showSlide(slideIndex) {
    slides.forEach((slide, index) => {
      slide.style.transform = `translateX(${100 * (index - slideIndex)}%)`;
    });
  };

  function nextSlide() {
    currentSlide = (currentSlide + 1) % slides.length;
    showSlide(currentSlide);
  }

  function prevSlide() {
    currentSlide = (currentSlide - 1 + slides.length) % slides.length;
    showSlide(currentSlide);
  }

  const nextButton = document.getElementById('next-button');
  const prevButton = document.getElementById('prev-button');

  if (nextButton && prevButton) {
    nextButton.addEventListener('click', nextSlide);
    prevButton.addEventListener('click', prevSlide);
  }

setInterval(nextSlide, 5000);
