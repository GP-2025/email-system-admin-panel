
import os
import requests

os.environ["API_BASE_URL"] = "https://emailingsystemapi.runasp.net"
os.environ["API_ACCESS_TOKEN"] = ""

def login():
    try:
        response = requests.post(
            url = f"{os.environ.get("API_BASE_URL")}/api/Auth/Login",
            headers = {
                "accept": "text/plain",
                "Authorization": f"Bearer {os.environ.get("API_ACCESS_TOKEN")}",
                "Content-Type": "application/json",
            },
            json = {
                "email": "ismailcollege@gmail.com",
                "password": "helloworld"
            }
        )

        print("response status:", response.status_code)
        print("response body:", response.text)

        token = response.json()["accessToken"]

        if not response.ok:
            response.raise_for_status()

        os.environ["API_ACCESS_TOKEN"] = token
        
        return token

    except requests.exceptions.HTTPError as http_err:
        print("HTTP error occurred during token refresh:", http_err)
        if http_err.response is not None and http_err.response.status_code == 404:
            print("Refresh endpoint not found. Please check the API URL and path")
        raise
    except Exception as err:
        print("An error occurred during token refresh:", err)
        raise

# ----------------------------------------------------------------

def refresh_token():
    response = requests.get(
        f"{os.environ.get("API_BASE_URL")}/api/Auth/Refresh",
        headers = {
            "accept": "text/plain",
            "Authorization": f"Bearer {os.environ.get("API_ACCESS_TOKEN")}",
            "Content-Type": "application/json",
        }
    )

    print("Refresh response status:", response.status_code)
    print("Refresh response body:", response.text )

    if not response.ok:
        response.raise_for_status()

    new_token = response.json()["accessToken"]
    os.environ["API_ACCESS_TOKEN"] = new_token
    if not new_token:
        raise ValueError("No token received from refresh endpoint")
    
    return new_token

print("TOKEN:", os.environ.get("API_ACCESS_TOKEN"))
print("\n")

login()
print("\n")

print("TOKEN:", os.environ.get("API_ACCESS_TOKEN"))
print("\n")

# refresh_token()
print("\n")

print("TOKEN:", os.environ.get("API_ACCESS_TOKEN"))
print("\n")