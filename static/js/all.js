
openMainMenuButton = document.getElementById("open-main-menu-button");
closeMainMenuButton = document.getElementById("close-main-menu-button");
mainMenuMobile = document.getElementById("main-menu-mobile");

openMainMenuButton.addEventListener("click", function() {
    mainMenuMobile.classList.remove("hidden");
});

closeMainMenuButton.addEventListener("click", function() {
    mainMenuMobile.classList.add("hidden");
});