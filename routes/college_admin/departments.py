
from flask import Blueprint, render_template, request, session, jsonify, redirect, flash
import json
import api
import tools

college_admin_departments_bp = Blueprint("departments", __name__, url_prefix="/college_admin")


# ---------------------------------------
# GET METHOD
# ---------------------------------------
@college_admin_departments_bp.route("/departments", methods=["GET"])
def departments_get():
    if not tools.check_session():
        flash("Your are not logged in!", "red")
        return redirect("/login")
    
    if not tools.is_college_admin():
        flash("Your account is not authorized!", "red")
        return redirect("/login")
    
    college_id = session.get("college_id")
    tools.update_token()
    
    college = api.GetCollegeById(college_id)
    departments = college.get("departments")
    # departments = api.AllUsers().get("data")
    
    newdepartments = [
        {
            "id": 1,
            "email": "Email1@gmail.com",
            "name": "Email01",
            "role": "NormalUser",
            "pictureURL": "https://emailingsystemapi.runasp.net/Attachments/ProfileImages/20250424-453a18e0-3086-48ac-bfff-ea3b608e9a87-WhatsApp Image 2025-04-24 at 6.07.48 PM.jpeg",
            "signatureURL": "Empty",
            "collegeName": "Faculty of Computers and Artificial Intelligence",
            "collegeId": 7,
            "departmentName": None,
            "nationalId": "30309282403233"
        },
        {
            "id": 2,
            "email": "victornisem01@gmail.com",
            "name": "ghghg",
            "role": "Secretary",
            "pictureURL": "https://emailingsystemapi.runasp.net/Attachments/ProfileImages/20250424-e9e91351-8d79-4b65-8898-43e43584b8fb-WhatsApp Image 2025-04-24 at 6.07.48 PM.jpeg",
            "signatureURL": "https://emailingsystemapi.runasp.net/Attachments/Signatures/20250424-b329aafe-9678-4bc1-ba93-5c29d164a406-WhatsApp Image 2025-04-24 at 6.07.48 PM.jpeg",
            "collegeName": "Faculty of Computers and Artificial Intelligence",
            "collegeId": 7,
            "departmentName": None,
            "nationalId": "30310200200954"
        },
        {
            "id": 3,
            "email": "AhmedMahgoub@gmail.com",
            "name": "Ahmed Mahgoub",
            "role": "NormalUser",
            "pictureURL": "https://emailingsystemapi.runasp.net/Attachments/ProfileImages/20250119-664e73c4-8111-4b28-9c72-2008bd008cc1-82704776_2519931088116832_7267053509139234816_n.jpg",
            "signatureURL": "Empty",
            "collegeName": "Faculty of Computers and Artificial Intelligence",
            "collegeId": 7,
            "departmentName": "Student Affairs",
            "nationalId": "20201233212020"
        },
        {
            "id": 4,
            "email": "OsamaOmara@gmail.com",
            "name": "Osama Omara",
            "role": "Dean",
            "pictureURL": "Empty",
            "signatureURL": "Empty",
            "collegeName": "Faculty of Computers and Artificial Intelligence",
            "collegeId": 7,
            "departmentName": None,
            "nationalId": "10101010555101"
        },
        {
            "id": 5,
            "email": "AhmedSaad@gmail.com",
            "name": "Ahmed Saad",
            "role": "Secretary",
            "pictureURL": "https://emailingsystemapi.runasp.net/Attachments/ProfileImages/20250119-f3c06101-e49d-4c77-b215-10311ded90e2-468296341_954517489885131_7801765812482740396_n.jpg",
            "signatureURL": "Empty",
            "collegeName": "Faculty of Computers and Artificial Intelligence",
            "collegeId": 7,
            "departmentName": None,
            "nationalId": "50260405050505"
        },
        {
            "id": 6,
            "email": "ismailtestapi@gmail.com",
            "name": "Ismail",
            "role": "CollegeAdmin",
            "pictureURL": "Empty",
            "signatureURL": "Empty",
            "collegeName": "Faculty of Computers and Artificial Intelligence",
            "collegeId": 7,
            "departmentName": None,
            "nationalId": "30320160804274"
        },
        {
            "id": 7,
            "email": "ismail@gmail.com",
            "name": "helloworld",
            "role": "CollegeAdmin",
            "pictureURL": "https://emailingsystemapi.runasp.net/Attachments/ProfileImages/20250423-38a96c1c-acda-489e-b0ba-3824b28a8624-2-profile-picture.jpg",
            "signatureURL": "Empty",
            "collegeName": "Faculty of Computers and Artificial Intelligence",
            "collegeId": 7,
            "departmentName": None,
            "nationalId": "30220140204237"
        },
        {
            "id": 8,
            "email": "ismailcollege@gmail.com",
            "name": "Ismail Sherif College",
            "role": "CollegeAdmin",
            "pictureURL": "Empty",
            "signatureURL": "Empty",
            "collegeName": "Faculty of Computers and Artificial Intelligence",
            "collegeId": 7,
            "departmentName": None,
            "nationalId": "03239847237458"
        },
        {
            "id": 9,
            "email": "Emasdfasil1@gmail.com",
            "name": "Email01",
            "role": "NormalUser",
            "pictureURL": "https://emailingsystemapi.runasp.net/Attachments/ProfileImages/20250424-453a18e0-3086-48ac-bfff-ea3b608e9a87-WhatsApp Image 2025-04-24 at 6.07.48 PM.jpeg",
            "signatureURL": "Empty",
            "collegeName": "Faculty of Computers and Artificial Intelligence",
            "collegeId": 7,
            "departmentName": None,
            "nationalId": "30309282403233"
        },
        {
            "id": 10,
            "email": "victornisem01@gmail.com",
            "name": "ghghg",
            "role": "Secretary",
            "pictureURL": "https://emailingsystemapi.runasp.net/Attachments/ProfileImages/20250424-e9e91351-8d79-4b65-8898-43e43584b8fb-WhatsApp Image 2025-04-24 at 6.07.48 PM.jpeg",
            "signatureURL": "https://emailingsystemapi.runasp.net/Attachments/Signatures/20250424-b329aafe-9678-4bc1-ba93-5c29d164a406-WhatsApp Image 2025-04-24 at 6.07.48 PM.jpeg",
            "collegeName": "Faculty of Computers and Artificial Intelligence",
            "collegeId": 7,
            "departmentName": None,
            "nationalId": "30310200200954"
        },
        {
            "id": 11,
            "email": "AhmedMahgoub@gmail.com",
            "name": "Ahmed Mahgoub",
            "role": "NormalUser",
            "pictureURL": "https://emailingsystemapi.runasp.net/Attachments/ProfileImages/20250119-664e73c4-8111-4b28-9c72-2008bd008cc1-82704776_2519931088116832_7267053509139234816_n.jpg",
            "signatureURL": "Empty",
            "collegeName": "Faculty of Computers and Artificial Intelligence",
            "collegeId": 7,
            "departmentName": "Student Affairs",
            "nationalId": "20201233212020"
        },
        {
            "id": 12,
            "email": "OsamaOmara@gmail.com",
            "name": "Osama Omara",
            "role": "Dean",
            "pictureURL": "Empty",
            "signatureURL": "Empty",
            "collegeName": "Faculty of Computers and Artificial Intelligence",
            "collegeId": 7,
            "departmentName": None,
            "nationalId": "10101010555101"
        },
        {
            "id": 13,
            "email": "AhmedSaad@gmail.com",
            "name": "Ahmed Saad",
            "role": "Secretary",
            "pictureURL": "https://emailingsystemapi.runasp.net/Attachments/ProfileImages/20250119-f3c06101-e49d-4c77-b215-10311ded90e2-468296341_954517489885131_7801765812482740396_n.jpg",
            "signatureURL": "Empty",
            "collegeName": "Faculty of Computers and Artificial Intelligence",
            "collegeId": 7,
            "departmentName": None,
            "nationalId": "50260405050505"
        },
        {
            "id": 14,
            "email": "ismailtestapi@gmail.com",
            "name": "Ismail",
            "role": "CollegeAdmin",
            "pictureURL": "Empty",
            "signatureURL": "Empty",
            "collegeName": "Faculty of Computers and Artificial Intelligence",
            "collegeId": 7,
            "departmentName": None,
            "nationalId": "30320160804274"
        },
        {
            "id": 15,
            "email": "ismail@gmail.com",
            "name": "helloworld",
            "role": "CollegeAdmin",
            "pictureURL": "https://emailingsystemapi.runasp.net/Attachments/ProfileImages/20250423-38a96c1c-acda-489e-b0ba-3824b28a8624-2-profile-picture.jpg",
            "signatureURL": "Empty",
            "collegeName": "Faculty of Computers and Artificial Intelligence",
            "collegeId": 7,
            "departmentName": None,
            "nationalId": "30220140204237"
        },
        {
            "id": 16,
            "email": "ismailcollege@gmail.com",
            "name": "Ismail Sherif College",
            "role": "CollegeAdmin",
            "pictureURL": "Empty",
            "signatureURL": "Empty",
            "collegeName": "Faculty of Computers and Artificial Intelligence",
            "collegeId": 7,
            "departmentName": None,
            "nationalId": "03239847237458"
        }
    ]

    
    return render_template(
        f"/college_admin/{tools.get_lang()}/departments.html",
        departments=newdepartments,
        college=college
    )