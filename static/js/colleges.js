
crudModelButton = document.getElementById("crud-modal-button");
crudModelCloseButton = document.getElementById("crud-modal-close-button");
crudModel = document.getElementById("crud-modal");

crudModelButton.addEventListener("click", function () {
    crudModel.classList.remove("hidden");
    crudModel.classList.add("flex");
});

crudModelCloseButton.addEventListener("click", function () {
    crudModel.classList.remove("flex");
    crudModel.classList.add("hidden");
});