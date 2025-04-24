
const addModalOpenButton = document.getElementById("add-modal-open-button");
const addModalCloseButton = document.getElementById("add-modal-close-button");
const addModalBackdrop = document.getElementById("add-modal");

const prevPageButton = document.getElementById('prev-page');
const nextPageButton = document.getElementById('next-page');
const currentPageInput = document.getElementById('current-page');
const totalPagesSpan = document.getElementById('total-pages');

const rowsContainer = document.querySelector("[data-rows-container]");
const searchInput = document.querySelector("[data-search]");

const sortByInput = document.querySelector("[data-sort-by]");

const collegesPerPage = 4;
let currentPage = 1;
let totalColleges = 0;
let totalPages = 1;

const alertTemplates = document.querySelectorAll("[alert-template]")
const alertTimeExpiration = 7 // in seconds


alertTemplates.forEach(alertTemplate => {
    setTimeout(() => { alertTemplate.remove() }, alertTimeExpiration*1000);
});

function closeAlertTemplate (message) {
    var alertTemplate = document.querySelector(`[alret-message='${message}']`)
    alertTemplate.remove()
}


function setLanguage(lang) {
    // Logic to set the language
    console.log("Language set to:", lang);
}


document.addEventListener('DOMContentLoaded', () => {
    addModalOpenButton.addEventListener('click', () => {
        addModalBackdrop.classList.remove('pointer-events-none', 'opacity-0');
    });

    addModalCloseButton.addEventListener('click', () => {
        addModalBackdrop.classList.add('pointer-events-none', 'opacity-0');
    });
});


searchInput.addEventListener("input", function (e) {
    const value = e.target.value.toLowerCase();
    colleges.forEach(college => {
        const isVisible = college.name.toLowerCase().includes(value) || college.abbreviation.toLowerCase().includes(value);
        college.element.classList.toggle("hidden", !isVisible);
    });
});

let colleges = document.querySelectorAll("[data-row-template]");
console.log(colleges.length);


totalColleges = colleges.length;
totalPages = Math.ceil(totalColleges / collegesPerPage);
updatePagination();

function updateModalOpenButton(row_id) {
    const updateModalBackdrop = document.querySelector(`[data-modal-row-id="${row_id}"]`);
    updateModalBackdrop.classList.remove('pointer-events-none', 'opacity-0');
}

function updateModalCloseButton(row_id) {
    const updateModalBackdrop = document.querySelector(`[data-modal-row-id="${row_id}"]`);
    updateModalBackdrop.classList.add('pointer-events-none', 'opacity-0');
}

sortByInput.addEventListener("change", function (e) {
    const value = e.target.value;
    colleges.sort((a, b) => {
        if (value === "asc") {
            return a.name.localeCompare(b.name);
        } else if (value === "desc") {
            return b.name.localeCompare(a.name);
        }
    });
    colleges.forEach(college => rowsContainer.appendChild(college.element));
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
    rowsContainer.innerHTML = "";
    const startIndex = (currentPage - 1) * collegesPerPage;
    const endIndex = startIndex + collegesPerPage;
    const collegesToDisplay = colleges.slice(startIndex, endIndex);
    collegesToDisplay.forEach(college => {
        rowsContainer.appendChild(college.element);
    });
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