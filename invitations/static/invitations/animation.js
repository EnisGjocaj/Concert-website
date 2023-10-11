const mainBtn = document.getElementById('mainButton');
const svgButtonGroup = document.getElementById('svgButtonGroup');


document.addEventListener("DOMContentLoaded", function () {
  const animatedDiv = document.querySelector(".animated-div");
  animatedDiv.classList.add("animate");
});


svgButtonGroup.style.display = "none";

let isHidden = true;

mainBtn.addEventListener('click', function () {
  if (isHidden) {

    svgButtonGroup.style.display = 'flex';
    setTimeout(function () {
      svgButtonGroup.style.transform = 'translateX(0)';
    }, 50); 
    isHidden = false; 
  } else {
    
    svgButtonGroup.style.transform = 'translateX(-100%)';
    setTimeout(function () {
      svgButtonGroup.style.display = 'none';
    }, 500);
    isHidden = true; 
  }
});
