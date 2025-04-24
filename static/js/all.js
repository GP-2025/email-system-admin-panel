
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

const RowsPerPage = 10;
let currentPage = 1;
let totalRows = 0;
let totalPages = 1;
let Rows = [];

const alertTemplates = document.querySelectorAll("[alert-template]")
const alertTimeExpiration = 7 // in seconds


document.addEventListener('DOMContentLoaded', () => {
    for (let i = 0; i < rowsContainer.children.length; i++) {
        let row_element = rowsContainer.children[i]
        let row_name = row_element.querySelector("[data-name]").textContent
        let row_abbreviation = row_element.querySelector("[data-abbreviation]").textContent
        Rows.push({
            name: row_name,
            abbreviation: row_abbreviation,
            element: row_element,
        })
    }
    totalRows = Rows.length;
    totalPages = Math.ceil(totalRows / RowsPerPage);
    updatePagination();

    addModalOpenButton.addEventListener('click', () => {
        addModalBackdrop.classList.remove('pointer-events-none', 'opacity-0');
    });

    addModalCloseButton.addEventListener('click', () => {
        addModalBackdrop.classList.add('pointer-events-none', 'opacity-0');
    });
});

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

searchInput.addEventListener("input", function (e) {
    const value = e.target.value.toLowerCase();
    Rows.forEach(row => {
        const isVisible = row.name.toLowerCase().includes(value) || row.abbreviation.toLowerCase().includes(value);
        row.element.classList.toggle("hidden", !isVisible);
    }) 
    updatePagination()
});

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
    Rows.sort((a, b) => {
        if (value === "asc") {
            return a.name.localeCompare(b.name);
        } else if (value === "desc") {
            return b.name.localeCompare(a.name);
        }
    });
    Rows.forEach(row => rowsContainer.appendChild(row.element));
    updatePagination();
});

function updatePagination() {
    totalPages = Math.ceil(totalRows / RowsPerPage);
    totalPagesSpan.textContent = totalPages;
    currentPageInput.value = currentPage;

    prevPageButton.disabled = currentPage === 1;
    nextPageButton.disabled = currentPage === totalPages || totalPages === 0;

    loadRows();
}

function loadRows() {
    var tempRows = []
    Rows.forEach(row => {
        if ( !row.element.classList.contains("hidden") )
            tempRows.push(row)
    });
    console.log(tempRows)
    rowsContainer.innerHTML = "";
    const startIndex = (currentPage - 1) * RowsPerPage;
    const endIndex = startIndex + RowsPerPage;
    const RowsToDisplay = tempRows.slice(startIndex, endIndex);
    RowsToDisplay.forEach(row => {
        rowsContainer.appendChild(row.element);
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