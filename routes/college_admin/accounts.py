
from flask import Blueprint, render_template, request, session, jsonify, redirect, flash
import json
import api
import tools

college_admin_accounts_bp = Blueprint("accounts", __name__, url_prefix="/college_admin")


# ---------------------------------------
# GET METHOD
# ---------------------------------------
@college_admin_accounts_bp.route("/accounts", methods=["GET"])
def accounts_get():
    if not tools.check_session():
        flash("Your are not logged in!", "red")
        return redirect("/login")
    
    if not tools.is_college_admin():
        flash("Your account is not authorized!", "red")
        return redirect("/login")
    
    college_id = session.get("college_id")
    tools.update_token()
    
    college = api.GetCollegeById(college_id)
    
    accounts = api.AllUsers().get("data")
    if accounts:
        accounts = list(reversed(accounts))
    
    departments = college.get("departments")
    if departments:
        departments = list(reversed(departments))
    
    roles = tools.get_roles({tools.get_lang()})
    
    return render_template(
        f"/college_admin/{tools.get_lang()}/accounts.html",
        accounts=accounts,
        roles=roles,
        departments=departments,
        college=college,
    )


# ---------------------------------------
# POST METHOD
# ---------------------------------------
@college_admin_accounts_bp.route("/accounts/add_account", methods=["POST"])
def accounts_post():
    if not tools.check_session():
        flash("Your are not logged in!", "red")
        return redirect("/login")
    
    if not tools.is_college_admin():
        flash("Your account is not authorized!", "red")
        return redirect("/login")
    
    college_id = session.get("college_id")
    tools.update_token()
    
    # data = {
    #     "email": request.form["account_email"],
    #     "password": request.form["account_password"],
    #     "name": request.form["account_name"],
    #     "role_id": request.form["account_role_id"],
    #     "national_id": request.form["account_national_id"],
    #     "department_id": request.form["account_department_id"],
    #     "college_id": college_id,
    # }
    # files = {
    #     "Picture": (
    #         request.files['account_profile_picture'].filename,
    #         request.files['account_profile_picture'].stream,
    #         request.files['account_profile_picture'].mimetype
    #     ),
    #     "SignatureFile": (
    #         request.files['account_signature_picture'].filename,
    #         request.files['account_signature_picture'].stream,
    #         request.files['account_signature_picture'].mimetype
    #     ),
    # }
    
    
    # Extract form data
    form_data = {
        "Email": request.form.get("account_email"),
        "Password": request.form.get("account_password"),
        "Name": request.form.get("account_name"),
        "DepartmentId": int(request.form.get("account_department_id")),
        "CollegeId": int(college_id),
        "Role": int(request.form.get("account_role_id")),
        "NationalId": request.form.get("account_national_id"),
    }

    # Extract files
    files = {
        "Picture": (
            request.files['account_profile_picture'].filename,
            request.files['account_profile_picture'].stream,
            request.files['account_profile_picture'].mimetype
        ),
        "SignatureFile": (
            request.files['account_signature_picture'].filename,
            request.files['account_signature_picture'].stream,
            request.files['account_signature_picture'].mimetype
        ),
    }

    # Headers
    headers = {
        "accept": "text/plain",
        "Authorization": f"Bearer {session.get("access_token")}",
        "Authorization": f"Bearer {session.get("access_token")}",
    }

    # Send POST request
    import requests
    url = "https://emailingsystemapi.runasp.net/api/Auth/Register"
    response = requests.post(url, headers=headers, data=form_data, files=files)
    print(response.json())
    
    # res = api.Register(data, files)
    # if res.status_code != 200:
    #     print(res.json())
    #     flash("error adding new account.", "red")
    #     return redirect("/college_admin/accounts")
    
    # flash("Account added successfully.", "green")
    return redirect("/college_admin/accounts")