const loader = document.querySelector(".loader");
const submitButtons = document.querySelectorAll('button[type="submit"]')

// Page loader 
window.addEventListener("load", () => {
  loader.classList.add("loader-hidden");
  loader.addEventListener("transitionend", () => {
    loader.remove();
  })
});