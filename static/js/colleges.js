
const crudModelButton = document.getElementById("crud-modal-button");
const crudModelCloseButton = document.getElementById("crud-modal-close-button");
const crudModelBackdrop = document.getElementById("crud-modal");

const updateCollegeModelButton = document.getElementById("update-college-modal-button");
const updateCollegeModelCloseButton = document.getElementById("update-college-close-button");
const updateCollegeModelBackdrop = document.getElementById("update-college-modal");

const prevPageButton = document.getElementById('prev-page');
const nextPageButton = document.getElementById('next-page');
const currentPageInput = document.getElementById('current-page');
const totalPagesSpan = document.getElementById('total-pages');

const collegeRowTemplate = document.querySelector("[data-college-row-template]");
const collegesContainer = document.querySelector("[data-colleges-container]");
const searchInput = document.querySelector("[data-search]");

const sortByInput = document.querySelector("[data-sort-by]");

let colleges = [];

const collegesPerPage = 8;
let currentPage = 1;
let totalColleges = 0;
let totalPages = 1;


document.addEventListener('DOMContentLoaded', () => {
    crudModelButton.addEventListener('click', () => {
        crudModelBackdrop.classList.remove('pointer-events-none', 'opacity-0');
    });

    crudModelCloseButton.addEventListener('click', () => {
        crudModelBackdrop.classList.add('pointer-events-none', 'opacity-0');
    });

    // todo: create foreach edit button an eventlister and make it to work with the college-id

    // updateCollegeModelButton.addEventListener('click', () => {
    //     updateCollegeModelBackdrop.classList.remove('pointer-events-none', 'opacity-0');
    // });

    // updateCollegeModelCloseButton.addEventListener('click', () => {
    //     updateCollegeModelBackdrop.classList.add('pointer-events-none', 'opacity-0');
    // });

    // todo: end create
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
        colleges = data.map((user, index) => {
            const row = collegeRowTemplate.content.cloneNode(true).children[0];
            const collegeName = row.querySelector("[data-college-name]");
            const collegeAbbreviation = row.querySelector("[data-college-abbreviation]");

            const updateCollegeModalOpenButton = row.querySelector("[update-college-modal-open-button]")
            const updateCollegeModalCloseButton = row.querySelector("[update-college-modal-close-button]")
            const updateCollegeModalBackdrop = row.querySelector("[update-college-modal-backdrop]")
            const updateCollegeModalForm = row.querySelector("[update-college-modal-form]")

            const currentCollegeName = row.querySelector(".current-college-name")
            const currentCollegeAbbreviation = row.querySelector(".current-college-abbreviation")

            const collegeIdInputField = row.querySelector(".college-id")
            const collegeNameInputField = row.querySelector(".college-name")
            const collegeAbbreviationInputField = row.querySelector(".college-abbreviation")
            
            var collegeId = index

            currentCollegeName.textContent = user.name
            currentCollegeAbbreviation.textContent = user.email // should be abbreviation

            collegeIdInputField.value = collegeId
            collegeNameInputField.value = user.name
            collegeAbbreviationInputField.value = user.email // should be abbreviation

            updateCollegeModalOpenButton.setAttribute("open-button-college-id", collegeId);
            updateCollegeModalCloseButton.setAttribute("close-button-college-id", collegeId);
            updateCollegeModalBackdrop.setAttribute("modal-backdrop-college-id", collegeId);
            updateCollegeModalForm.setAttribute("modal-form-college-id", collegeId);

            collegeName.textContent = user.name;
            collegeAbbreviation.textContent = user.email;
            collegesContainer.appendChild(row);

            return {
                id: collegeId,
                name: user.name,
                abbreviation: user.email,
                element: row,
            };
        });
        
        const updateCollegeModalOpenButtons = document.querySelectorAll("[update-college-modal-open-button]")
        const updateCollegeModalCloseButtons = document.querySelectorAll("[update-college-modal-close-button]")
        const updateCollegeModalForms = document.querySelectorAll("[update-college-modal-form]")
        
        updateCollegeModalOpenButtons.forEach(openButton => {
            const collegeId = openButton.getAttribute("open-button-college-id")
            const collegeModalBackdrop = document.querySelector(`[modal-backdrop-college-id="${collegeId}"]`);
            openButton.addEventListener('click', () => {
                collegeModalBackdrop.classList.remove('pointer-events-none', 'opacity-0');
            });
        });

        updateCollegeModalCloseButtons.forEach(closeButton => {
            const collegeId = closeButton.getAttribute("close-button-college-id")
            const collegeModalBackdrop = document.querySelector(`[modal-backdrop-college-id="${collegeId}"]`);
            closeButton.addEventListener('click', () => {
                collegeModalBackdrop.classList.add('pointer-events-none', 'opacity-0');
            });
        });

        updateCollegeModalForms.forEach(form => {
            form.addEventListener('submit', (e) => {
                e.preventDefault()
                const collegeId = form.getAttribute("modal-form-college-id")
                // const formData = new FormData(form);
                console.log(form);
            });
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