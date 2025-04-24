
document.addEventListener('DOMContentLoaded', () => {
    for (let i = 0; i < rowsContainer.children.length; i++) {
        let row_element = rowsContainer.children[i]
        let row_name = row_element.querySelector("[data-name]").textContent
        let row_email = row_element.querySelector("[data-email]").textContent
        let row_national_id = row_element.querySelector("[data-national-id]").textContent
        Rows.push({
            name: row_name,
            email: row_email,
            national_id: row_national_id,
            element: row_element,
        })
    }
    totalRows = Rows.length;
    totalPages = Math.ceil(totalRows / RowsPerPage);
    updatePagination();
});

searchInput.addEventListener("input", function (e) {
    const value = e.target.value.toLowerCase();
    Rows.forEach(row => {
        const isVisible = row.name.toLowerCase().includes(value) ||
        row.email.toLowerCase().includes(value) ||
        row.national_id.toLowerCase().includes(value);

        row.element.classList.toggle("hidden", !isVisible);
    }) 
    updatePagination()
});