
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
});

searchInput.addEventListener("input", function (e) {
    const value = e.target.value.toLowerCase();
    Rows.forEach(row => {
        const isVisible = row.name.toLowerCase().includes(value) || row.abbreviation.toLowerCase().includes(value);
        row.element.classList.toggle("hidden", !isVisible);
    }) 
    updatePagination()
});