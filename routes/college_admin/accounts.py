
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
     
    account_email = request.form.get("account_email")
    account_national_id = request.form.get("account_national_id")
    account_department_id = int(request.form.get("account_department_id"))

    accounts = api.AllUsers().get("data")
    
    department = api.GetDepartmentById(account_department_id)
    if department.get("userId"):
        flash("Department already has an account!", "red")
        return redirect("/college_admin/accounts")
    
    for account in accounts:        
        if account["email"] == account_email:
            flash("Email already exists!", "red")
            return redirect("/college_admin/accounts")
        if account["nationalId"] == account_national_id:
            flash("National ID already exists!", "red")
            return redirect("/college_admin/accounts")
    
    college_id = session.get("college_id")
    tools.update_token()
    
    data = {
        "Email": request.form.get("account_email"),
        "Password": request.form.get("account_password"),
        "Name": request.form.get("account_name"),
        "DepartmentId": int(request.form.get("account_department_id")),
        "CollegeId": int(college_id),
        "Role": int(request.form.get("account_role_id")),
        "NationalId": request.form.get("account_national_id"),
    }

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
    
    res = api.Register(data, files)
    if res.status_code != 200:
        flash("error adding new account.", "red")
        return redirect("/college_admin/accounts")
    
    flash("Account added successfully.", "green")
    return redirect("/college_admin/accounts")



# ---------------------------------------
# POST METHOD
# ---------------------------------------
@college_admin_accounts_bp.route("/accounts/edit_account/<int:account_id>", methods=["POST"])
def accounts_edit_account(account_id):
    if not tools.check_session():
        flash("Your are not logged in!", "red")
        return redirect("/login")
    
    if not tools.is_college_admin():
        flash("Your account is not authorized!", "red")
        return redirect("/login")
    
    print(account_id)
    print(json.dumps(request.form, indent=2))
    print(request.files["account_profile_picture"])
    print(request.files["account_signature_picture"])
    return redirect("/college_admin/accounts")
    
    account_email = request.form.get("account_email")
    account_national_id = request.form.get("account_national_id")
    account_department_id = int(request.form.get("account_department_id"))

    accounts = api.AllUsers().get("data")
    
    department = api.GetDepartmentById(account_department_id)
    if department.get("userId"):
        flash("Department already has an account!", "red")
        return redirect("/college_admin/accounts")
    
    for account in accounts:
        if account["id"] == account_id:
            continue
        if account["email"] == account_email:
            flash("Email already exists!", "red")
            return redirect("/college_admin/accounts")
        if account["nationalId"] == account_national_id:
            flash("National ID already exists!", "red")
            return redirect("/college_admin/accounts")
    
    college_id = session.get("college_id")
    tools.update_token()
    
    data = {
        "Email": request.form.get("account_email"),
        "Password": request.form.get("account_password"),
        "Name": request.form.get("account_name"),
        "DepartmentId": int(request.form.get("account_department_id")),
        "CollegeId": int(college_id),
        "Role": int(request.form.get("account_role_id")),
        "NationalId": request.form.get("account_national_id"),
    }

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
    
    res = api.Register(data, files)
    if res.status_code != 200:
        flash("error adding new account.", "red")
        return redirect("/college_admin/accounts")
    
    flash("Account updated successfully.", "green")
    return redirect("/college_admin/accounts")



# ---------------------------------------
# POST METHOD
# ---------------------------------------
@college_admin_accounts_bp.route("/accounts/reset_password/<string:email>", methods=["POST"])
def accounts_reset_password(email):
    if not tools.check_session():
        flash("Your are not logged in!", "red")
        return redirect("/login")
    
    if not tools.is_college_admin():
        flash("Your account is not authorized!", "red")
        return redirect("/login")
    
    tools.update_token()
    res = api.ResetPassword(email)
    
    if res.status_code != 200:
        flash("Error reseting  account password!", "red")
        return redirect("/college_admin/accounts")
    
    flash("Account password reset successfully.", "green")
    return redirect("/college_admin/accounts")