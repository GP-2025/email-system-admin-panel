const accessToken = "eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9lbWFpbGFkZHJlc3MiOiJNTzdBTUVENjEwMjAwM0BHTUFJTC5DT00iLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3JvbGUiOiJBZG1pbiIsImV4cCI6MTc0NTY1MDE2MSwiaXNzIjoiRW1haWwiLCJhdWQiOiJFbWFpbGluZ1N5c3RlbUF1ZGllbmNlIn0.1isRuWD5eCzU_nbmdKxvaBPLzOONIYfFR9m6AJtvZuM"
const BASE_URL = "https://emailingsystemapi.runasp.net"

fetch(`${BASE_URL}/api/Auth/LogIn`, {
    method: 'POST',
    headers: {
        'accept': 'text/plain',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        email: "mo7amed6102003@gmail.com",
        password: "12345678"
    })
})
    .then(response => response.json())
    .then(data => {
        console.log("First Request")
        console.log(data)
        registerUser(data.accessToken)
    })
    .catch(error => console.error('Error:', error));

function registerUser(token) {
    var formData = new FormData()
    
    // fetch(`${BASE_URL}/api/Auth/Register?email=ismailtestapi@gmail.com&password=helloworld&name=Ismail&nationalid=30320160804274&role=10&collegeid=7`, {
    fetch(`${BASE_URL}/api/Admin/EditAccount`, {
        method: 'PUT',
        headers: {
            'accept': 'text/plain',
            'Content-Type': 'multipart/form-data',
            'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({
            Picture: null,
            SignatureFile: null,
        })
    })
        .then(response => response.json())
        .then(data => {
            console.log("\nSecond Request")
            console.log(data)
        })
}