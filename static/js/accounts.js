document.addEventListener('DOMContentLoaded', () => {
    for (let i = 0; i < rowsContainer.children.length; i++) {
        let row_element = rowsContainer.children[i]
        let row_name = row_element.querySelector("[data-name]").textContent
        let row_email = row_element.querySelector("[data-email]").textContent
        let row_role = row_element.querySelector("[data-role]").textContent
        let row_national_id = row_element.querySelector("[data-national-id]").textContent
        Rows.push({
            name: row_name,
            role: row_role,
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

function checkFileSize(file) {
    const maxSizeInMB = 1; // Maximum file size in MB
    if (file.size > maxSizeInMB * 1024 * 1024)
        return false
    return true
}

function updateProfilePictureInput(account_id) {
    const updateProfilePictureInputContainer = document.querySelector(`[update_profile_picture_input_container="${account_id}"]`)
    const updateProfilePictureInputTextContainer = updateProfilePictureInputContainer.children[0]
    const updateProfilePictureInput = updateProfilePictureInputContainer.querySelector("input")
    var updateProfilePictureFileName = updateProfilePictureInputContainer.querySelector("[file_name]")

    if ( ! updateProfilePictureInput.files.length ) {        
        updateProfilePictureFileName.textContent = ""
        return updateProfilePictureInputTextContainer.classList.remove("hidden")
    }

    if (!checkFileSize(updateProfilePictureInput.files[0])) {
        var alertTemplateContainer = document.querySelector("[alert-template-container]")
        var alertTemplate = document.createElement('div');
        alertTemplate.id = "toast-success";
        alertTemplate.setAttribute("alert-message", "File size exceeds the maximum limit of 2MB.");
        alertTemplate.setAttribute("role", "alert");
        alertTemplate.setAttribute("alert-template", "");
        alertTemplate.className = "flex items-center w-full max-w-xs p-4 mb-4 text-gray-500 bg-white rounded-lg shadow-lg dark:text-gray-400 dark:bg-gray-800 border border-1 dark:border-gray-500";
        alertTemplate.innerHTML = `
            <div class="inline-flex items-center justify-center shrink-0 w-8 h-8 text-orange-300 bg-orange-100 rounded-lg bg-orange-500">
                <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                    <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM10 15a1 1 0 1 1 0-2 1 1 0 0 1 0 2Zm1-4a1 1 0 0 1-2 0V6a1 1 0 0 1 2 0v5Z" />
                </svg>
                <span class="sr-only">Check icon</span>
            </div>
            <div class="ms-3 text-sm text-white font-normal">File size exceeds the maximum limit of 2MB.</div>
            <button type="button" onclick="closeAlertTemplate('File size exceeds the maximum limit of 2MB.')" data-dismiss-target="#toast-success" aria-label="Close"
                class="ms-auto -mx-1.5 -my-1.5 bg-white text-gray-400 hover:text-gray-900 rounded-lg focus:ring-2 focus:ring-gray-300 p-1.5 hover:bg-gray-100 inline-flex items-center justify-center h-8 w-8 dark:text-gray-500 dark:hover:text-white dark:bg-gray-800 dark:hover:bg-gray-700">
                <span class="sr-only">Close</span>
                <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6" />
                </svg>
            </button>
        `;
        updateProfilePictureInput.value = "";
        return alertTemplateContainer.appendChild(alertTemplate)
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

    if (!checkFileSize(updateSignaturePictureInput.files[0])) {
        var alertTemplateContainer = document.querySelector("[alert-template-container]")
        var alertTemplate = document.createElement('div');
        alertTemplate.id = "toast-success";
        alertTemplate.setAttribute("alert-message", "File size exceeds the maximum limit of 2MB.");
        alertTemplate.setAttribute("role", "alert");
        alertTemplate.setAttribute("alert-template", "");
        alertTemplate.className = "flex items-center w-full max-w-xs p-4 mb-4 text-gray-500 bg-white rounded-lg shadow-lg dark:text-gray-400 dark:bg-gray-800 border border-1 dark:border-gray-500";
        alertTemplate.innerHTML = `
            <div class="inline-flex items-center justify-center shrink-0 w-8 h-8 text-orange-300 bg-orange-100 rounded-lg bg-orange-500">
                <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                    <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM10 15a1 1 0 1 1 0-2 1 1 0 0 1 0 2Zm1-4a1 1 0 0 1-2 0V6a1 1 0 0 1 2 0v5Z" />
                </svg>
                <span class="sr-only">Check icon</span>
            </div>
            <div class="ms-3 text-sm text-white font-normal">File size exceeds the maximum limit of 2MB.</div>
            <button type="button" onclick="closeAlertTemplate('File size exceeds the maximum limit of 2MB.')" data-dismiss-target="#toast-success" aria-label="Close"
                class="ms-auto -mx-1.5 -my-1.5 bg-white text-gray-400 hover:text-gray-900 rounded-lg focus:ring-2 focus:ring-gray-300 p-1.5 hover:bg-gray-100 inline-flex items-center justify-center h-8 w-8 dark:text-gray-500 dark:hover:text-white dark:bg-gray-800 dark:hover:bg-gray-700">
                <span class="sr-only">Close</span>
                <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6" />
                </svg>
            </button>
        `;
        console.log(updateSignaturePictureInput.files);
        updateSignaturePictureInput.value = "";
        console.log(updateSignaturePictureInput.files);
        return alertTemplateContainer.appendChild(alertTemplate)
    }

    var filename = updateSignaturePictureInput.files[0].name
    updateSignaturePictureFileName.textContent = filename
    updateSignaturePictureInputTextContainer.classList.add("hidden")
}