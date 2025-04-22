
const crudModelButton = document.getElementById("crud-modal-button");
const crudModelCloseButton = document.getElementById("crud-modal-close-button");
const crudModel = document.getElementById("crud-modal");

crudModelButton.addEventListener("click", function () {
    crudModel.classList.remove("hidden");
    crudModel.classList.add("flex");
});

crudModelCloseButton.addEventListener("click", function () {
    crudModel.classList.remove("flex");
    crudModel.classList.add("hidden");
});

const collegeRowTemplate = document.querySelector("[data-college-row-template]");
const collegesContainer = document.querySelector("[data-colleges-container]");
const searchInput = document.querySelector("[data-search]");

let colleges = [];

searchInput.addEventListener("input", function (e) {
    const value = e.target.value.toLowerCase();
    colleges.forEach(college => {
        const isVisible = college.name.toLowerCase().includes(value) || college.abbreviation.toLowerCase().includes(value);
        college.element.classList.toggle("hidden", !isVisible);
    });
});

fetch("https://jsonplaceholder.typicode.com/users")
    .then(res => res.json())
    .then(data => {
        colleges = data.map(user => {
            const row = collegeRowTemplate.content.cloneNode(true).children[0];
            const collegeName = row.querySelector("[data-college-name]");
            const collegeAbbreviation = row.querySelector("[data-college-abbreviation]");
            collegeName.textContent = user.name;
            collegeAbbreviation.textContent = user.email;
            collegesContainer.appendChild(row);
            return {
                name: user.name,
                abbreviation: user.email,
                element: row
            };
        });
    });