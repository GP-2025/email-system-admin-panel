
const crudModelButton = document.getElementById("crud-modal-button");
const crudModelCloseButton = document.getElementById("crud-modal-close-button");
const crudModel = document.getElementById("crud-modal");

const prevPageButton = document.getElementById('prev-page');
const nextPageButton = document.getElementById('next-page');
const currentPageInput = document.getElementById('current-page');
const totalPagesSpan = document.getElementById('total-pages');

const collegeRowTemplate = document.querySelector("[data-college-row-template]");
const collegesContainer = document.querySelector("[data-colleges-container]");
const searchInput = document.querySelector("[data-search]");

const sortByInput = document.querySelector("[data-sort-by]");

let colleges = [];

const collegesPerPage = 10;
let currentPage = 1;
let totalColleges = 0;
let totalPages = 1;

crudModelButton.addEventListener("click", function () {
    crudModel.classList.remove("hidden");
    crudModel.classList.add("flex");
});

crudModelCloseButton.addEventListener("click", function () {
    crudModel.classList.remove("flex");
    crudModel.classList.add("hidden");
});


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
        totalColleges = colleges.length;
        totalPages = Math.ceil(totalColleges / collegesPerPage);
        updatePagination();
    });


sortByInput.addEventListener("change", function (e) {
    const value = e.target.value;
    colleges.sort((a, b) => {
        if (value === "college_name_asc") {
            return a.name.localeCompare(b.name);
        } else if (value === "college_name_desc") {
            return b.name.localeCompare(a.name);
        } else if (value === "college_abbreviation_asc") {
            return a.abbreviation.localeCompare(b.abbreviation);
        } else if (value === "college_abbreviation_desc") {
            return b.abbreviation.localeCompare(a.abbreviation);
        }
    });
    colleges.forEach(college => collegesContainer.appendChild(college.element));
    totalColleges = colleges.length;
    totalPages = Math.ceil(totalColleges / collegesPerPage);
    updatePagination();
});


function updatePagination() {
    totalPages = Math.ceil(totalColleges / collegesPerPage);
    totalPagesSpan.textContent = totalPages;
    currentPageInput.value = currentPage;

    prevPageButton.disabled = currentPage === 1;
    nextPageButton.disabled = currentPage === totalPages || totalPages === 0;

    loadColleges();
}

function loadColleges() {
    collegesContainer.innerHTML = "";
    const startIndex = (currentPage - 1) * collegesPerPage;
    const endIndex = startIndex + collegesPerPage;
    const collegesToDisplay = colleges.slice(startIndex, endIndex);
    collegesToDisplay.forEach(college => {
        collegesContainer.appendChild(college.element);
    });

    console.log(`Loaded colleges for page ${currentPage}`);
}


prevPageButton.addEventListener('click', () => {
    if (currentPage > 1) {
        currentPage--;
        updatePagination();
    }
});

nextPageButton.addEventListener('click', () => {
    if (currentPage < totalPages) {
        currentPage++;
        updatePagination();
    }
});

currentPageInput.addEventListener('change', () => {
    const newPage = parseInt(currentPageInput.value, 10);
    if (newPage >= 1 && newPage <= totalPages) {
        currentPage = newPage;
        updatePagination();
    } else {
        currentPageInput.value = currentPage;
    }
});