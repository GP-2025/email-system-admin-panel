
import os
import json
import requests

# ----------------------------------------------------------------
# Getting New Token through Login
# ----------------------------------------------------------------

def getNewTokenFromLogin(email, password):
    try:
        response = requests.post(
            url = f"{os.environ["API_BASE_URL"]}/api/Auth/Login",
            headers = {
                "accept": "text/plain",
                "Content-Type": "application/json",
            },
            json = {
                "email": email,
                "password": password
            }
        )
        token = response.json()["accessToken"]
        if not response.ok:
            response.raise_for_status()
        
        # setting new token
        os.environ["API_ACCESS_TOKEN"] = token

        return token

    except requests.exceptions.HTTPError as http_err:
        print("HTTP error occurred during login:", http_err)
        if http_err.response is not None and http_err.response.status_code == 404:
            print("Endpoint not found. Please check the API URL and path")
        raise
    except Exception as err:
        print("An error occurred during login:", err)
        raise

# ----------------------------------------------------------------
# /api/Admin/AllUsers
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# /api/Admin/ResetPassowrd/{Email}
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# /api/Admin/EditAccount
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# /api/Admin/GetAccountByEmail
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# /api/Auth/Register
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# /api/Auth/LogIn
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# /api/Auth/LogOut
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# /api/Auth/Refresh
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# /api/College/GetAllColleges
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# /api/College/UpdateCollege
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# /api/College/AddCollege
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# /api/College/GetById/{Id}
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# /api/Department/AddDepartment
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# /api/Department/EditDepartment/{Id}
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# /api/Department/GetById{Id}
# ----------------------------------------------------------------

def AllUsers():
    try:
        response = requests.get(
            f"{os.environ["API_BASE_URL"]}/api/Admin/AllUsers",
            headers={
                "accept": "text/plain",
                "Authorization": f"Bearer {os.environ["API_ACCESS_TOKEN"]}",
            }
        )

        # Add debugging
        print("all response status:", response.status_code)
        print("all response body:", json.dumps(response.json(), indent=2))

        if not response.ok:
            response.raise_for_status()

        if not response.json():
            raise ValueError("Error getting all user from AllUsers endpoint")

        return response.json()

    except requests.exceptions.HTTPError as http_err:
        print("HTTP error occurred during token refresh:", http_err)
        if http_err.response is not None and http_err.response.status_code == 404:
            print("Refresh endpoint not found. Please check the API URL and path")
        raise
    except Exception as err:
        print("An error occurred during token refresh:", err)
        raise


# ----------------------------------------------------------------