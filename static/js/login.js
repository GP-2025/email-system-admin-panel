
loginForm = document.getElementById("login-form");

loginForm.addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent the default form submission

    window.location.href = "/dashboard";

    // const formData = new FormData(loginForm);
    // const data = Object.fromEntries(formData.entries());

    // fetch("/login", {
    //     method: "POST",
    //     headers: {
    //         "Content-Type": "application/json",
    //     },
    //     body: JSON.stringify(data),
    // })
    //     .then((response) => {
    //         if (response.ok) {
    //             window.location.href = "/"; // Redirect to the home page on success
    //         } else {
    //             alert("Login failed. Please check your credentials.");
    //         }
    //     })
    //     .catch((error) => {
    //         console.error("Error:", error);
    //     });
});