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

function updateProfilePictureInput(account_id) {
    const updateProfilePictureInputContainer = document.querySelector(`[update_profile_picture_input_container="${account_id}"]`)
    const updateProfilePictureInputTextContainer = updateProfilePictureInputContainer.children[0]
    const updateProfilePictureInput = updateProfilePictureInputContainer.querySelector("input")
    var updateProfilePictureFileName = updateProfilePictureInputContainer.querySelector("[file_name]")

    if ( ! updateProfilePictureInput.files.length ) {
        updateProfilePictureFileName.textContent = ""
        return updateProfilePictureInputTextContainer.classList.remove("hidden")
    }
    var filename = updateProfilePictureInput.files[0].name
    updateProfilePictureFileName.textContent = filename
    updateProfilePictureInputTextContainer.classList.add("hidden")
}

function updateSignaturePictureInput(account_id) {
    const updateSignaturePictureInputContainer = document.querySelector(`[update_signature_picture_input_container="${account_id}"]`)
    const updateSignaturePictureInputTextContainer = updateSignaturePictureInputContainer.children[0]
    const updateSignaturePictureInput = updateSignaturePictureInputContainer.querySelector("input")
    var updateSignaturePictureFileName = updateSignaturePictureInputContainer.querySelector("[file_name]")

    if ( ! updateSignaturePictureInput.files.length ) {
        updateSignaturePictureFileName.textContent = ""
        return updateSignaturePictureInputTextContainer.classList.remove("hidden")
    }
    var filename = updateSignaturePictureInput.files[0].name
    updateSignaturePictureFileName.textContent = filename
    updateSignaturePictureInputTextContainer.classList.add("hidden")
}