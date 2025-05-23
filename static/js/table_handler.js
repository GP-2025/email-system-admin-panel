
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


sortByInput.addEventListener("change", function (e) {
    const value = e.target.value;
    Rows.sort((a, b) => {
        if (value === "name_asc") {
            return a.name.localeCompare(b.name);
        } else if (value === "name_desc") {
            return b.name.localeCompare(a.name);
        } else if (value === "role_asc") {
            return a.role.localeCompare(b.role);
        } else if (value === "role_desc") {
            return b.role.localeCompare(a.role);
        } else if (value === "college_asc") {
            return a.college.localeCompare(b.college);
        } else if (value === "college_desc") {
            return b.college.localeCompare(a.college);
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
