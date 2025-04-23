
import os
import json
import requests

BASE_URL = os.environ["API_BASE_URL"]

## ----------------------------------------------------------------
## Getting New Token through Login
## ----------------------------------------------------------------

def getNewTokenFromLogin(email, password):
    try:
        response = requests.post(
            url = f"{BASE_URL}/api/Auth/Login",
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


## ----------------------------------------------------------------
## /api/Admin/AllUsers
## ----------------------------------------------------------------

def AllUsers():
    try:
        response = requests.get(
            f"{BASE_URL}/api/Admin/AllUsers",
            headers={
                "accept": "text/plain",
                "Authorization": f"Bearer {os.environ["API_ACCESS_TOKEN"]}",
            }
        )
        if not response.ok:
            response.raise_for_status()
        if not response.json():
            raise ValueError("Error getting all user from AllUsers endpoint")
        return response.json()
    
    except requests.exceptions.HTTPError as http_err:
        print("HTTP error occurred during getting AllUsers:", http_err)
        if http_err.response is not None and http_err.response.status_code == 404:
            print("AllUsers endpoint not found. Please check the API URL and path")
        raise
    except Exception as err:
        print("An error occurred during getting AllUsers:", err)
        raise


## ----------------------------------------------------------------
## /api/Admin/ResetPassowrd/{Email}
## ----------------------------------------------------------------

def ResetPassowrd(email):
    try:
        response = requests.get(
            f"{BASE_URL}/api/Admin/ResetPassowrd/{email}",
            headers={
                "accept": "text/plain",
                "Authorization": f"Bearer {os.environ["API_ACCESS_TOKEN"]}",
            }
        )
        if not response.ok:
            response.raise_for_status()
        if not response.json():
            raise ValueError("Error getting all user from ResetPassowrd endpoint")
        return response.json()
    
    except requests.exceptions.HTTPError as http_err:
        print("HTTP error occurred during getting ResetPassowrd:", http_err)
        if http_err.response is not None and http_err.response.status_code == 404:
            print("ResetPassowrd endpoint not found. Please check the API URL and path")
        raise
    except Exception as err:
        print("An error occurred during getting ResetPassowrd:", err)
        raise


## ----------------------------------------------------------------
## /api/Admin/EditAccount
## ----------------------------------------------------------------

def EditAccount(data, picture_file, signature_file):
    try:
        response = requests.put(
            f"{BASE_URL}/api/Admin/EditAccount?Email={data["email"]}&Name={data["name"]}&Role={data["role_id"]}&NationalId={data["national_id"]}&CollegeId={data["college_id"]}&DepartmentId={data["department_id"]}",
            headers={
                "accept": "text/plain",
                "Authorization": f"Bearer {os.environ["API_ACCESS_TOKEN"]}",
                "Content-Type": "multipart/form-data"
            },
            files={
                "Picture": picture_file,
                "Signature": signature_file,
            }
        )
        if not response.ok:
            response.raise_for_status()
        if not response.json():
            raise ValueError("Error getting all user from EditAccount endpoint")
        return response.json()
    
    except requests.exceptions.HTTPError as http_err:
        print("HTTP error occurred during getting EditAccount:", http_err)
        if http_err.response is not None and http_err.response.status_code == 404:
            print("EditAccount endpoint not found. Please check the API URL and path")
        raise
    except Exception as err:
        print("An error occurred during getting EditAccount:", err)
        raise


## ----------------------------------------------------------------
## /api/Admin/GetAccountByEmail
## ----------------------------------------------------------------

def GetAccountByEmail(email):
    try:
        response = requests.get(
            f"{BASE_URL}/api/Admin/GetAccountByEmail/{email}",
            headers={
                "accept": "text/plain",
                "Authorization": f"Bearer {os.environ["API_ACCESS_TOKEN"]}",
            }
        )
        if not response.ok:
            response.raise_for_status()
        if not response.json():
            raise ValueError("Error getting all user from GetAccountByEmail endpoint")
        return response.json()
    
    except requests.exceptions.HTTPError as http_err:
        print("HTTP error occurred during getting GetAccountByEmail:", http_err)
        if http_err.response is not None and http_err.response.status_code == 404:
            print("GetAccountByEmail endpoint not found. Please check the API URL and path")
        raise
    except Exception as err:
        print("An error occurred during getting GetAccountByEmail:", err)
        raise


## ----------------------------------------------------------------
## /api/Auth/Register
## ----------------------------------------------------------------

def Register(data, picture_file, signature_file):
    try:
        response = requests.post(
            f"{BASE_URL}/api/Admin/Register?Email={data["email"]}&Name={data["name"]}&Role={data["role_id"]}&NationalId={data["national_id"]}&CollegeId={data["college_id"]}&DepartmentId={data["department_id"]}",
            headers={
                "accept": "text/plain",
                "Authorization": f"Bearer {os.environ["API_ACCESS_TOKEN"]}",
                "Content-Type": "multipart/form-data"
            },
            files={
                "Picture": picture_file,
                "Signature": signature_file,
            }
        )
        if not response.ok:
            response.raise_for_status()
        if not response.json():
            raise ValueError("Error getting all user from Register endpoint")
        return response.json()
    
    except requests.exceptions.HTTPError as http_err:
        print("HTTP error occurred during getting Register:", http_err)
        if http_err.response is not None and http_err.response.status_code == 404:
            print("Register endpoint not found. Please check the API URL and path")
        raise
    except Exception as err:
        print("An error occurred during getting Register:", err)
        raise


## ----------------------------------------------------------------
## /api/Auth/LogIn
## ----------------------------------------------------------------

def Login(email, password):
    try:
        response = requests.post(
            url = f"{BASE_URL}/api/Auth/Login",
            headers = {
                "accept": "text/plain",
                "Content-Type": "application/json",
            },
            json = {
                "email": email,
                "password": password
            }
        )
        if not response.ok:
            response.raise_for_status()
        if not response.json():
            raise ValueError("Error getting all user from Register endpoint")
        return response.json()

    except requests.exceptions.HTTPError as http_err:
        print("HTTP error occurred during Login:", http_err)
        if http_err.response is not None and http_err.response.status_code == 404:
            print("Login endpoint not found. Please check the API URL and path")
        raise
    except Exception as err:
        print("An error occurred during Login:", err)
        raise


## ----------------------------------------------------------------
## /api/Auth/LogOut
## ----------------------------------------------------------------

def Logout():
    try:
        response = requests.get(
            f"{BASE_URL}/api/Admin/Logout",
            headers={
                "accept": "text/plain",
                "Authorization": f"Bearer {os.environ["API_ACCESS_TOKEN"]}",
            }
        )
        if not response.ok:
            response.raise_for_status()
        if not response.json():
            raise ValueError("Error getting all user from Logout endpoint")
        return response.json()
    
    except requests.exceptions.HTTPError as http_err:
        print("HTTP error occurred during getting Logout:", http_err)
        if http_err.response is not None and http_err.response.status_code == 404:
            print("Logout endpoint not found. Please check the API URL and path")
        raise
    except Exception as err:
        print("An error occurred during getting Logout:", err)
        raise


## ----------------------------------------------------------------
## /api/Auth/Refresh
## ----------------------------------------------------------------

def Refresh():
    try:
        response = requests.get(
            f"{BASE_URL}/api/Admin/Refresh",
            headers={
                "accept": "text/plain",
                "Authorization": f"Bearer {os.environ["API_ACCESS_TOKEN"]}",
            }
        )
        if not response.ok:
            response.raise_for_status()
        if not response.json():
            raise ValueError("Error getting all user from Refresh endpoint")
        return response.json()
    
    except requests.exceptions.HTTPError as http_err:
        print("HTTP error occurred during getting Refresh:", http_err)
        if http_err.response is not None and http_err.response.status_code == 404:
            print("Refresh endpoint not found. Please check the API URL and path")
        raise
    except Exception as err:
        print("An error occurred during getting Refresh:", err)
        raise


## ----------------------------------------------------------------
## /api/College/GetAllColleges
## ----------------------------------------------------------------

def GetAllColleges():
    try:
        response = requests.get(
            f"{BASE_URL}/api/Admin/GetAllColleges",
            headers={
                "accept": "text/plain",
                "Authorization": f"Bearer {os.environ["API_ACCESS_TOKEN"]}",
            }
        )
        if not response.ok:
            response.raise_for_status()
        if not response.json():
            raise ValueError("Error getting all user from GetAllColleges endpoint")
        return response.json()
    
    except requests.exceptions.HTTPError as http_err:
        print("HTTP error occurred during getting GetAllColleges:", http_err)
        if http_err.response is not None and http_err.response.status_code == 404:
            print("GetAllColleges endpoint not found. Please check the API URL and path")
        raise
    except Exception as err:
        print("An error occurred during getting GetAllColleges:", err)
        raise


## ----------------------------------------------------------------
## /api/College/UpdateCollege
## ----------------------------------------------------------------

def UpdateCollege(data):
    try:
        response = requests.post(
            f"{BASE_URL}/api/Admin/UpdateCollege?Id={data["id"]}",
            headers={
                "accept": "text/plain",
                "Authorization": f"Bearer {os.environ["API_ACCESS_TOKEN"]}",
                "Content-Type": "multipart/form-data"
            },
            files={
                "name": data["name"],
                "id": data["id"],
                "abbreviation": data["abbreviation"],
            }
        )
        if not response.ok:
            response.raise_for_status()
        if not response.json():
            raise ValueError("Error getting all user from UpdateCollege endpoint")
        return response.json()
    
    except requests.exceptions.HTTPError as http_err:
        print("HTTP error occurred during getting UpdateCollege:", http_err)
        if http_err.response is not None and http_err.response.status_code == 404:
            print("UpdateCollege endpoint not found. Please check the API URL and path")
        raise
    except Exception as err:
        print("An error occurred during getting UpdateCollege:", err)
        raise


## ----------------------------------------------------------------
## /api/College/AddCollege
## ----------------------------------------------------------------

def AddCollege(data):
    try:
        response = requests.post(
            f"{BASE_URL}/api/Admin/AddCollege",
            headers={
                "accept": "text/plain",
                "Authorization": f"Bearer {os.environ["API_ACCESS_TOKEN"]}",
            },
            data={
                "name": data["name"],
                "abbreviation": data["abbreviation"]
            }
        )
        if not response.ok:
            response.raise_for_status()
        if not response.json():
            raise ValueError("Error getting all user from AddCollege endpoint")
        return response.json()
    
    except requests.exceptions.HTTPError as http_err:
        print("HTTP error occurred during getting AddCollege:", http_err)
        if http_err.response is not None and http_err.response.status_code == 404:
            print("AddCollege endpoint not found. Please check the API URL and path")
        raise
    except Exception as err:
        print("An error occurred during getting AddCollege:", err)
        raise


## ----------------------------------------------------------------
## /api/College/GetById/{Id}
## ----------------------------------------------------------------

def GetCollegeById(college_id):
    try:
        response = requests.get(
            f"{BASE_URL}/api/Admin/GetById/{college_id}",
            headers={
                "accept": "text/plain",
                "Authorization": f"Bearer {os.environ["API_ACCESS_TOKEN"]}",
            }
        )
        if not response.ok:
            response.raise_for_status()
        if not response.json():
            raise ValueError("Error getting all user from GetById endpoint")
        return response.json()
    
    except requests.exceptions.HTTPError as http_err:
        print("HTTP error occurred during getting GetById:", http_err)
        if http_err.response is not None and http_err.response.status_code == 404:
            print("GetById endpoint not found. Please check the API URL and path")
        raise
    except Exception as err:
        print("An error occurred during getting GetById:", err)
        raise


## ----------------------------------------------------------------
## /api/Department/AddDepartment
## ----------------------------------------------------------------

def AddDepartment(data):
    try:
        response = requests.post(
            f"{BASE_URL}/api/Admin/AddDepartment",
            headers={
                "accept": "text/plain",
                "Authorization": f"Bearer {os.environ["API_ACCESS_TOKEN"]}",
                "Content-Type": "application/json"
            },
            json={
                "name": data["name"],
                "abbreviation": data["abbreviation"],
                "collegeId": data["college_id"]
            }
        )
        if not response.ok:
            response.raise_for_status()
        if not response.json():
            raise ValueError("Error getting all user from AddDepartment endpoint")
        return response.json()
    
    except requests.exceptions.HTTPError as http_err:
        print("HTTP error occurred during getting AddDepartment:", http_err)
        if http_err.response is not None and http_err.response.status_code == 404:
            print("AddDepartment endpoint not found. Please check the API URL and path")
        raise
    except Exception as err:
        print("An error occurred during getting AddDepartment:", err)
        raise


## ----------------------------------------------------------------
## /api/Department/EditDepartment/{Id}
## ----------------------------------------------------------------

def EditDepartment(data):
    try:
        response = requests.post(
            f"{BASE_URL}/api/Admin/EditDepartment/{data["id"]}",
            headers={
                "accept": "text/plain",
                "Authorization": f"Bearer {os.environ["API_ACCESS_TOKEN"]}",
                "Content-Type": "application/json"
            },
            data={
                "id": data["id"],
                "name": data["name"],
                "abbreviation": data["abbreviation"],
                "collegeId": data["college_id"],
            }
        )
        if not response.ok:
            response.raise_for_status()
        if not response.json():
            raise ValueError("Error getting all user from EditDepartment endpoint")
        return response.json()
    
    except requests.exceptions.HTTPError as http_err:
        print("HTTP error occurred during getting EditDepartment:", http_err)
        if http_err.response is not None and http_err.response.status_code == 404:
            print("EditDepartment endpoint not found. Please check the API URL and path")
        raise
    except Exception as err:
        print("An error occurred during getting EditDepartment:", err)
        raise


## ----------------------------------------------------------------
## /api/Department/GetById/{Id}
## ----------------------------------------------------------------

def GetDepartmentById(id):
    try:
        response = requests.get(
            f"{BASE_URL}/api/Admin/GetById/{id}",
            headers={
                "accept": "text/plain",
                "Authorization": f"Bearer {os.environ["API_ACCESS_TOKEN"]}",
            }
        )
        if not response.ok:
            response.raise_for_status()
        if not response.json():
            raise ValueError("Error getting all user from GetById endpoint")
        return response.json()
    
    except requests.exceptions.HTTPError as http_err:
        print("HTTP error occurred during getting GetById:", http_err)
        if http_err.response is not None and http_err.response.status_code == 404:
            print("GetById endpoint not found. Please check the API URL and path")
        raise
    except Exception as err:
        print("An error occurred during getting GetById:", err)
        raise


## ----------------------------------------------------------------
## ----------------------------------------------------------------