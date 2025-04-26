
from flask import session
import os
import requests

BASE_URL = os.environ["API_BASE_URL"]

## ----------------------------------------------------------------
## Getting New Token through Login
## ----------------------------------------------------------------

def getNewTokenFromLogin(email, password):
    response_json = Login(email, password)
    return response_json.get("accessToken")


## ----------------------------------------------------------------
## /api/Admin/AllUsers
## ----------------------------------------------------------------

def AllUsers():
    response = requests.get(
        f"{BASE_URL}/api/Admin/AllUsers",
        headers={
            "accept": "text/plain",
            "Authorization": f"Bearer {session.get("access_token")}",
        }
    )
    return response.json()


## ----------------------------------------------------------------
## /api/Admin/ResetPassowrd/{Email}
## ----------------------------------------------------------------

def ResetPassword(email):
    response = requests.get(
        f"{BASE_URL}/api/Admin/ResetPassword/{email}",
        headers={
            "accept": "*/*",
            "Authorization": f"Bearer {session.get("access_token")}",
        }
    )
    return response


## ----------------------------------------------------------------
## /api/Admin/EditAccount
## ----------------------------------------------------------------
def EditAccount(data, files):
    response = requests.put(
        url = f"{BASE_URL}/api/Admin/EditAccount",
        headers = {
            "accept": "*/*",
            "Authorization": f"Bearer {session.get("access_token")}",
        },
        params=data,
        files=files
    )
    return response


## ----------------------------------------------------------------
## /api/Admin/GetAccountByEmail
## ----------------------------------------------------------------

def GetAccountByEmail(email):
    response = requests.get(
        f"{BASE_URL}/api/Admin/GetAccountByEmail/{email}",
        headers={
            "accept": "text/plain",
            "Authorization": f"Bearer {session.get("access_token")}",
        }
    )
    return response.json()


## ----------------------------------------------------------------
## /api/Auth/Register
## ----------------------------------------------------------------

def Register(data, files):
    response = requests.post(
        url = f"{BASE_URL}/api/Auth/Register",
        headers = {
            "accept": "text/plain",
            "Authorization": f"Bearer {session.get("access_token")}",
        },
        data=data,
        files=files
    )
    return response


## ----------------------------------------------------------------
## /api/Auth/LogIn
## ----------------------------------------------------------------

def Login(email, password):
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
    return response.json()


## ----------------------------------------------------------------
## /api/Auth/LogOut
## ----------------------------------------------------------------

def Logout():
    response = requests.get(
        f"{BASE_URL}/api/Auth/Logout",
        headers={
            "accept": "text/plain",
            "Authorization": f"Bearer {session.get("access_token")}",
        }
    )
    return response.json()


## ----------------------------------------------------------------
## /api/Auth/Refresh
## ----------------------------------------------------------------

def Refresh():
    response = requests.get(
        f"{BASE_URL}/api/Auth/Refresh",
        headers={
            "accept": "text/plain",
            "Authorization": f"Bearer {session.get("access_token")}",
        }
    )
    return response.json()


## ----------------------------------------------------------------
## /api/College/GetAllColleges
## ----------------------------------------------------------------

def GetAllColleges():
    response = requests.get(
        f"{BASE_URL}/api/College/GetAllColleges",
        headers={
            "accept": "text/plain",
            "Authorization": f"Bearer {session.get("access_token")}",
        }
    )
    return response.json()


## ----------------------------------------------------------------
## /api/College/UpdateCollege
## ----------------------------------------------------------------

def UpdateCollege(data):
    response = requests.post(
        f"{BASE_URL}/api/College/UpdateCollege?Id={data["Id"]}",
        headers={
            "accept": "*/*",
            "Authorization": f"Bearer {session.get("access_token")}",
        },
        data=data,
    )
    return response


## ----------------------------------------------------------------
## /api/College/AddCollege
## ----------------------------------------------------------------

def AddCollege(data):
    response = requests.post(
        f"{BASE_URL}/api/College/AddCollege",
        headers={
            "accept": "application/json",
            "Authorization": f"Bearer {session.get('access_token')}",
            "Content-Type": "application/json"
        },
        json={
            "name": data["name"],
            "abbreviation": data["abbreviation"]
        }
    )
    return response


## ----------------------------------------------------------------
## /api/College/GetById/{Id}
## ----------------------------------------------------------------

def GetCollegeById(college_id):
    response = requests.get(
        f"{BASE_URL}/api/College/GetById/{college_id}",
        headers={
            "Authorization": f"Bearer {session.get('access_token')}",
            "Content-Type": "application/json"
        }
    )
    return response.json()


## ----------------------------------------------------------------
## /api/Department/AddDepartment
## ----------------------------------------------------------------

def AddDepartment(data):
    response = requests.post(
        f"{BASE_URL}/api/Department/AddDepartment",
        headers={
            "Authorization": f"Bearer {session.get("access_token")}",
            "Content-Type": "application/json"
        },
        json={
            "name": data["name"],
            "abbreviation": data["abbreviation"],
            "collegeId": data["college_id"]
        }
    )
    return response


## ----------------------------------------------------------------
## /api/Department/EditDepartment/{Id}
## ----------------------------------------------------------------

def EditDepartment(data):
    response = requests.post(
        f"{BASE_URL}/api/Department/EditDepartment/{data["id"]}",
        headers={
            "accept": "*/*",
            "Authorization": f"Bearer {session.get("access_token")}",
            "Content-Type": "application/json"
        },
        json={
            "id": data["id"],
            "name": data["name"],
            "abbreviation": data["abbreviation"],
            "collegeId": data["college_id"],
        }
    )
    return response


## ----------------------------------------------------------------
## /api/Department/GetById/{Id}
## ----------------------------------------------------------------

def GetDepartmentById(id):
    response = requests.get(
        f"{BASE_URL}/api/Department/GetById/{id}",
        headers={
            "accept": "text/plain",
            "Authorization": f"Bearer {session.get("access_token")}",
        }
    )
    return response


## ----------------------------------------------------------------
## ----------------------------------------------------------------