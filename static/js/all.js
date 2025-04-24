
const alertTemplates = document.querySelectorAll("[alert-template]")
const alertTimeExpiration = 7 // in seconds

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