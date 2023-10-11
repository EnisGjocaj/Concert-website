const button1 = document.querySelector('.fixed-left-button');
const closeIcon = document.getElementById('closeIcon');

const toggleNavbar = () => {

    const navbar = document.getElementById('myNavbar');

    if (navbar.style.right === '0px') {
        navbar.style.right = '-100%';
    } else {
        navbar.style.right = '0px';
    }
};

button1.addEventListener('click', () => {
    closeIcon.classList.toggle('active');
});

button1.addEventListener('click', toggleNavbar);

