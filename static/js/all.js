
const alertTemplate = document.querySelector("[role='alert']")
const alertTimeExpiration = 7 // in seconds

if (alertTemplate) {
    const alertTemplateCloseButton = alertTemplate.querySelector("button")
    
    setTimeout(() => { alertTemplate.remove() }, alertTimeExpiration*1000);
    
    alertTemplateCloseButton.addEventListener("click", () => {
        alertTemplate.remove()
    })
}


function setLanguage(lang) {
    // Logic to set the language
    console.log("Language set to:", lang);
}