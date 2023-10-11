const navBtn = document.getElementById('nav-btn');
const mobileMenu = document.getElementById('mobile-menu');
const elementToRemove = document.getElementById('movingElementExample');

navBtn.addEventListener('click', () => {
    setTimeout(() => {
        mobileMenu.classList.toggle('hidden');
    }, 400);
});



