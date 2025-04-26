const loader = document.querySelector(".loader");
const forms = document.querySelectorAll('form')

// Page loader 
window.addEventListener("load", () => {
  loader.classList.add("loader-hidden");
  loader.addEventListener("transitionend", () => {
    loader.remove();
  })
});

// page loader on form submission
forms.forEach(form => {
  form.addEventListener("submit", () => {
    loader.classList.remove("loader-hidden");
    document.body.insertBefore(loader, document.body.firstChild)
  })
});