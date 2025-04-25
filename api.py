
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

def ResetPassowrd(email):
    response = requests.get(
        f"{BASE_URL}/api/Admin/ResetPassowrd/{email}",
        headers={
            "accept": "text/plain",
            "Authorization": f"Bearer {session.get("access_token")}",
        }
    )
    return response.json()


## ----------------------------------------------------------------
## /api/Admin/EditAccount
## ----------------------------------------------------------------

def EditAccount(data, picture_file, signature_file):
    response = requests.put(
        f"{BASE_URL}/api/Admin/EditAccount?Email={data["email"]}&Name={data["name"]}&Role={data["role_id"]}&NationalId={data["national_id"]}&CollegeId={data["college_id"]}&DepartmentId={data["department_id"]}",
        headers={
            "accept": "text/plain",
            "Authorization": f"Bearer {session.get("access_token")}",
            "Content-Type": "multipart/form-data"
        },
        files={
            "Picture": picture_file,
            "Signature": signature_file,
        }
    )
    return response.json()


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

def Register(data, submitted_files):
        # f"{BASE_URL}/api/Auth/Register?Email={data["email"]}&Name={data["name"]}&Password={data["password"]}&Role={data["role_id"]}&NationalId={data["national_id"]}&CollegeId={data["college_id"]}&DepartmentId={data["department_id"]}",
        # f"{BASE_URL}/api/Auth/Register?Email=testtest%40gmail.test&Password=testtest&Name=testtest&DepartmentId=6&CollegeId=7&Role=0&NationalId=30303030303030",
        
        # headers={
        #     "accept": "text/plain",
        #     "Authorization": f"Bearer {session.get("access_token")}",
        #     "Content-Type": "multipart/form-data"
        # },
        
    response = requests.post(
        url = (
            "https://emailingsystemapi.runasp.net/api/Auth/Register"
            f"?Email={data["email"]}"
            f"&Password={data["password"]}"
            f"&Name={data["name"]}"
            f"&DepartmentId={data["department_id"]}"
            f"&CollegeId={data["college_id"]}"
            f"&Role={data["role_id"]}"
            f"&NationalId={data["national_id"]}"
        ),
        headers = {
            "accept": "text/plain",
            "Authorization": f"Bearer {session.get("access_token")}",
        },
        files=submitted_files
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
        f"{BASE_URL}/api/College/UpdateCollege?Id={data["id"]}",
        headers={
            "accept": "text/plain",
            "Authorization": f"Bearer {session.get("access_token")}",
            "Content-Type": "multipart/form-data"
        },
        files={
            "name": data["name"],
            "id": data["id"],
            "abbreviation": data["abbreviation"],
        }
    )
    return response.json()


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
    return response.json()


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
            "accept": "text/plain",
            "Authorization": f"Bearer {session.get("access_token")}",
            "Content-Type": "application/json"
        },
        data={
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
    return response.json()


## ----------------------------------------------------------------
## ----------------------------------------------------------------