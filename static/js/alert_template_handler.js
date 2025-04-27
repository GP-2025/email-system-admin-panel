
const alertTemplates = document.querySelectorAll("[alert-template]")

const alertTimeExpiration = 10 // in seconds
alertTemplates.forEach(alertTemplate => {
    setTimeout(() => { alertTemplate.remove() }, alertTimeExpiration*1000);
});

function closeAlertTemplate (message) {
    var alertTemplate = document.querySelector(`[alert-message="${message}"]`)
    alertTemplate.remove()
}