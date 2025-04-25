

const profilePictureInputTextContainer = document.querySelector("[profile_picture_input_text_container]")
const profilePictureInput = document.getElementById("profile_picture")

const signaturePictureInputTextContainer = document.querySelector("[signature_picture_input_text_container]")
const signaturePictureInput = document.getElementById("signature_picture")



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

profilePictureInput.addEventListener("change", (e) => {
    var profilePictureFileName = document.querySelector("[profile_picture_file_name]")
    if ( ! profilePictureInput.files.length ) {
        profilePictureFileName.textContent = ""
        return profilePictureInputTextContainer.classList.remove("hidden")
    }
    var filename = profilePictureInput.files[0].name
    profilePictureFileName.textContent = filename
    profilePictureInputTextContainer.classList.add("hidden")
});

signaturePictureInput.addEventListener("change", (e) => {
    var signaturePictureFileName = document.querySelector("[signature_picture_file_name]")
    if ( ! signaturePictureInput.files.length ) {
        signaturePictureFileName.textContent = ""
        return signaturePictureInputTextContainer.classList.remove("hidden")
    }
    var filename = signaturePictureInput.files[0].name
    signaturePictureFileName.textContent = filename
    signaturePictureInputTextContainer.classList.add("hidden")
});