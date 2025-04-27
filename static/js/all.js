
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


if (document.getElementById("toggle-password")) {
    document.getElementById("toggle-password").addEventListener("click", function () {
        const passwordInput = document.getElementById("password");
        const eyeIcon = document.getElementById("eye-icon");
    const eyeIconPath = eyeIcon.querySelector("path")
    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        eyeIconPath.setAttribute("d", "M38.8 5.1C28.4-3.1 13.3-1.2 5.1 9.2S-1.2 34.7 9.2 42.9l592 464c10.4 8.2 25.5 6.3 33.7-4.1s6.3-25.5-4.1-33.7L525.6 386.7c39.6-40.6 66.4-86.1 79.9-118.4c3.3-7.9 3.3-16.7 0-24.6c-14.9-35.7-46.2-87.7-93-131.1C465.5 68.8 400.8 32 320 32c-68.2 0-125 26.3-169.3 60.8L38.8 5.1zM223.1 149.5C248.6 126.2 282.7 112 320 112c79.5 0 144 64.5 144 144c0 24.9-6.3 48.3-17.4 68.7L408 294.5c8.4-19.3 10.6-41.4 4.8-63.3c-11.1-41.5-47.8-69.4-88.6-71.1c-5.8-.2-9.2 6.1-7.4 11.7c2.1 6.4 3.3 13.2 3.3 20.3c0 10.2-2.4 19.8-6.6 28.3l-90.3-70.8zM373 389.9c-16.4 6.5-34.3 10.1-53 10.1c-79.5 0-144-64.5-144-144c0-6.9 .5-13.6 1.4-20.2L83.1 161.5C60.3 191.2 44 220.8 34.5 243.7c-3.3 7.9-3.3 16.7 0 24.6c14.9 35.7 46.2 87.7 93 131.1C174.5 443.2 239.2 480 320 480c47.8 0 89.9-12.9 126.2-32.5L373 389.9z");
    } else {
        passwordInput.type = "password";
        eyeIconPath.setAttribute("d", "M288 32c-80.8 0-145.5 36.8-192.6 80.6C48.6 156 17.3 208 2.5 243.7c-3.3 7.9-3.3 16.7 0 24.6C17.3 304 48.6 356 95.4 399.4C142.5 443.2 207.2 480 288 480s145.5-36.8 192.6-80.6c46.8-43.5 78.1-95.4 93-131.1c3.3-7.9 3.3-16.7 0-24.6c-14.9-35.7-46.2-87.7-93-131.1C433.5 68.8 368.8 32 288 32zM144 256a144 144 0 1 1 288 0 144 144 0 1 1 -288 0zm144-64c0 35.3-28.7 64-64 64c-7.1 0-13.9-1.2-20.3-3.3c-5.5-1.8-11.9 1.6-11.7 7.4c.3 6.9 1.3 13.8 3.2 20.7c13.7 51.2 66.4 81.6 117.6 67.9s81.6-66.4 67.9-117.6c-11.1-41.5-47.8-69.4-88.6-71.1c-5.8-.2-9.2 6.1-7.4 11.7c2.1 6.4 3.3 13.2 3.3 20.3z");
        }
    });
}

document.addEventListener('DOMContentLoaded', () => {
    addModalOpenButton.addEventListener('click', () => {
        addModalBackdrop.classList.remove('pointer-events-none', 'opacity-0');
    });

    addModalCloseButton.addEventListener('click', () => {
        addModalBackdrop.classList.add('pointer-events-none', 'opacity-0');
    });

    const alertTemplates = document.querySelectorAll("[alert-template]")

    const alertTimeExpiration = 10 // in seconds
    alertTemplates.forEach(alertTemplate => {
        setTimeout(() => { alertTemplate.remove() }, alertTimeExpiration*1000);
    });
});


function closeAlertTemplate (message) {
    var alertTemplate = document.querySelector(`[alert-message="${message}"]`)
    alertTemplate.remove()
}

function setLanguage(lang) {
    // Logic to set the language
    console.log("Language set to:", lang);
}

function updateModalOpenButton(row_id) {
    const updateModalBackdrop = document.querySelector(`[data-modal-row-id="${row_id}"]`);
    updateModalBackdrop.classList.remove('pointer-events-none', 'opacity-0');
}

function updateModalCloseButton(row_id) {
    const updateModalBackdrop = document.querySelector(`[data-modal-row-id="${row_id}"]`);
    updateModalBackdrop.classList.add('pointer-events-none', 'opacity-0');
}

function accountModalOpenButton(account_id) {
    const accountModalBackdrop = document.querySelector(`[data-modal-account-id="${account_id}"]`);
    accountModalBackdrop.classList.remove('pointer-events-none', 'opacity-0');
}

function accountModalCloseButton(account_id) {
    const accountModalBackdrop = document.querySelector(`[data-modal-account-id="${account_id}"]`);
    accountModalBackdrop.classList.add('pointer-events-none', 'opacity-0');
}

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