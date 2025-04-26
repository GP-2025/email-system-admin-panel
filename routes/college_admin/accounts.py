
from flask import Blueprint, render_template, request, session, jsonify, redirect, flash
import json
import api
import tools
import tempfile

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
    
    account_department_id = request.form.get("account_department_id", None)
    account_email = request.form.get("account_email")
    account_national_id = request.form.get("account_national_id")

    if account_department_id:
        res = api.GetDepartmentById(account_department_id)
        if res.status_code != 200:
            flash("Error checking for chosen department!", "red")
        department = res.json()
        if department.get("userId"):
            flash("Department already has an account!", "red")
            return redirect("/college_admin/accounts")
    
    accounts = api.AllUsers().get("data")
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
        "DepartmentId": account_department_id,
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
        flash(res.json().get("message", "Error registering account!"), "red")
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
    
    account_department_id = request.form.get("account_department_id", "")
    account_email = request.form.get("account_email")
    account_national_id = request.form.get("account_national_id")

    if account_department_id:
        res = api.GetDepartmentById(account_department_id)
        if res.status_code != 200:
            flash("Error checking for chosen department!", "red")
        department = res.json()
        if department.get("userId") and department.get("userId") != account_id:
            flash("Department already has an account!", "red")
            return redirect("/college_admin/accounts")
    
    accounts = api.AllUsers().get("data")
    for account in accounts:
        if account["email"] == account_email and account.get("id") != account_id:
            flash("Email already exists!", "red")
            return redirect("/college_admin/accounts")
        if account["nationalId"] == account_national_id and account.get("id") != account_id:
            flash("National ID already exists!", "red")
            return redirect("/college_admin/accounts")
    
    college_id = session.get("college_id")
    tools.update_token()
    
    data = {
        "Email": request.form.get("account_email"),
        "Password": request.form.get("account_password"),
        "Name": request.form.get("account_name"),
        "DepartmentId": account_department_id,
        "CollegeId": int(college_id),
        "Role": int(request.form.get("account_role_id")),
        "NationalId": request.form.get("account_national_id"),
    }
    
    files = {}
    
    current_profile_picture_url = request.form.get('account_profile_picture_url')
    current_profile_picture_file = tools.download_file_from_url(current_profile_picture_url)
    
    current_signature_picture_url = request.form.get('account_signature_picture_url')
    current_signature_picture_file = tools.download_file_from_url(current_signature_picture_url)
    
    # Picture File
    if request.files['account_profile_picture']:
        files["Picture"] = (
            request.files['account_profile_picture'].filename,
            request.files['account_profile_picture'].stream,
            request.files['account_profile_picture'].mimetype
        )
        
    elif current_profile_picture_file:
        files["Picture"] = (
            current_profile_picture_file["filename"],
            current_profile_picture_file["stream"],
            current_profile_picture_file["mimetype"]
        )
    else:
        with open("static\images\profile.jpg", "rb") as default_picture_file:
            temp_picture_file = tempfile.SpooledTemporaryFile()
            temp_picture_file.write(default_picture_file.read())
            temp_picture_file.seek(0)
            files["Picture"] = ("profile.jpg", temp_picture_file, "image/jpg")
    
    # Signature File
    if request.files['account_signature_picture']:
        files["Signature"] = (
            request.files['account_signature_picture'].filename,
            request.files['account_signature_picture'].stream,
            request.files['account_signature_picture'].mimetype
        )
    elif current_signature_picture_file:
        files["Signature"] = (
            current_signature_picture_file["filename"],
            current_signature_picture_file["stream"],
            current_signature_picture_file["mimetype"]
        )
    else:
        with open("static\images\signature-default.png", "rb") as default_signature_file:
            temp_signature_file = tempfile.SpooledTemporaryFile()
            temp_signature_file.write(default_signature_file.read())
            temp_signature_file.seek(0)
            files["Signature"] = ("signature-default.jpg", temp_signature_file, "image/jpg")
        
    print(files)
    
    tools.update_token()
    res = api.EditAccount(data, files)
    
    if res.status_code != 200:
        flash(f"Error editing {request.form.get("account_name")} account!", "red")
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