
const addModalOpenButton = document.getElementById("add-modal-open-button");
const addModalCloseButton = document.getElementById("add-modal-close-button");
const addModalBackdrop = document.getElementById("add-modal");


function updateModalOpenButton(row_id) {
    const updateModalBackdrop = document.querySelector(`[data-modal-row-id="${row_id}"]`);
    updateModalBackdrop.classList.remove('pointer-events-none', 'opacity-0');
}

function updateModalCloseButton(row_id) {
    const updateModalBackdrop = document.querySelector(`[data-modal-row-id="${row_id}"]`);
    updateModalBackdrop.classList.add('pointer-events-none', 'opacity-0');
}


document.addEventListener('DOMContentLoaded', () => {
    if (addModalOpenButton) {
        addModalOpenButton.addEventListener('click', () => {
            addModalBackdrop.classList.remove('pointer-events-none', 'opacity-0');
        });
    }
    if (addModalCloseButton) {
        addModalCloseButton.addEventListener('click', () => {
            addModalBackdrop.classList.add('pointer-events-none', 'opacity-0');
        });
    }
});