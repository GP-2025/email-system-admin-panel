
from flask import Blueprint, render_template, request, session, jsonify, redirect, flash
import json
import api
import tools

admin_all_accounts_bp = Blueprint("admin_all_accounts", __name__, url_prefix="/admin")


# ---------------------------------------
# GET METHOD
# ---------------------------------------
@admin_all_accounts_bp.route("/all_accounts", methods=["GET"])
def admin_all_accounts_get():
    if not tools.check_session():
        flash("Your are not logged in!", "red")
        return redirect("/login")
    
    if not tools.is_admin():
        flash("Your account is not authorized!", "red")
        return redirect("/login")
    
    tools.update_token()
    
    res = api.AllUsers()
    accounts_data = res.json().get("data")
    accounts = []
    for acc in accounts_data:
        if acc.get("role") == "CollegeAdmin":
            accounts.append(acc)
    
    if accounts:
        accounts = list(reversed(accounts))
    
    tools.update_token()
    res = api.GetAllColleges()
    colleges = res.json().get("data")
    if colleges:
        colleges = list(reversed(colleges))
        
    roles = tools.get_roles({tools.get_lang()})
    
    return render_template(
        f"/admin/{tools.get_lang()}/all_accounts.html",
        accounts=accounts,
        roles=roles,
        colleges=colleges,
    )


# ---------------------------------------
# POST METHOD
# ---------------------------------------
@admin_all_accounts_bp.route("/all_accounts/add_account", methods=["POST"])
def admin_all_accounts_post():
    if not tools.check_session():
        flash("Your are not logged in!", "red")
        return redirect("/login")
    
    if not tools.is_admin():
        flash("Your account is not authorized!", "red")
        return redirect("/login")

    tools.update_token()
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
            return redirect(f"/admin/all_accounts")
    
    res = api.AllUsers()
    accounts = res.json().get("data")
    for account in accounts:        
        if account["email"] == account_email:
            flash("Email already exists!", "red")
            return redirect(f"/admin/all_accounts")
        if account["nationalId"] == account_national_id:
            flash("National ID already exists!", "red")
            return redirect(f"/admin/all_accounts")
    
    data = {
        "Email": request.form.get("account_email"),
        "Password": request.form.get("account_password"),
        "Name": request.form.get("account_name"),
        "CollegeId": int(request.form.get("account_college_id")),
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
        return redirect(f"/admin/all_accounts")
    
    flash("Account added successfully.", "green")
    return redirect(f"/admin/all_accounts")



# ---------------------------------------
# POST METHOD
# ---------------------------------------
@admin_all_accounts_bp.route("/all_accounts/edit_account/<int:account_id>", methods=["POST"])
def admin_all_accounts_edit_account(account_id):
    if not tools.check_session():
        flash("Your are not logged in!", "red")
        return redirect("/login")
    
    if not tools.is_admin():
        flash("Your account is not authorized!", "red")
        return redirect("/login")
    
    tools.update_token()
    
    account_department_id = request.form.get("account_department_id", None)
    account_email = request.form.get("account_email")
    account_national_id = request.form.get("account_national_id")
    
    if account_department_id:
        res = api.GetDepartmentById(account_department_id)
        if res.status_code != 200:
            flash("Error checking for chosen department!", "red")
        department = res.json()
        if department.get("userId") and department.get("userId") != account_id:
            flash("Department already has an account!", "red")
            return redirect(f"/admin/all_accounts")
    
    res = api.AllUsers()
    accounts = res.json().get("data")
    for account in accounts:
        if account["email"] == account_email and account.get("id") != account_id:
            flash("Email already exists!", "red")
            return redirect(f"/admin/all_accounts")
        if account["nationalId"] == account_national_id and account.get("id") != account_id:
            flash("National ID already exists!", "red")
            return redirect(f"/admin/all_accounts")
    
    data = {
        "Email": request.form.get("account_email"),
        "Name": request.form.get("account_name"),
        "DepartmentId": int(account_department_id) if account_department_id else None,
        "CollegeId": int(request.form.get("account_college_id")),
        "Role": int(request.form.get("account_role_id")),
        "NationalId": request.form.get("account_national_id"),
    }
    
    files = {}
    
    # Picture File
    if request.files['account_profile_picture']:
        files["Picture"] = (
            request.files['account_profile_picture'].filename,
            request.files['account_profile_picture'].stream,
            request.files['account_profile_picture'].mimetype
        )
    # Signature File
    if request.files['account_signature_picture']:
        files["Signature"] = (
            request.files['account_signature_picture'].filename,
            request.files['account_signature_picture'].stream,
            request.files['account_signature_picture'].mimetype
        )

    tools.update_token()
    res = api.EditAccount(data, files)
    
    if res.status_code != 200:
        print(json.dumps(res.json(), indent=2))
        flash(res.json().get("message", "Error editing account!"), "red")
        return redirect(f"/admin/all_accounts")
    
    flash("Account updated successfully.", "green")
    return redirect(f"/admin/all_accounts")


# ---------------------------------------
# POST METHOD
# ---------------------------------------
@admin_all_accounts_bp.route("/all_accounts/reset_password/<string:email>", methods=["POST"])
def admin_all_accounts_reset_password(email):
    if not tools.check_session():
        flash("Your are not logged in!", "red")
        return redirect("/login")
    
    if not tools.is_admin():
        flash("Your account is not authorized!", "red")
        return redirect("/login")
    
    tools.update_token()
    res = api.ResetPassword(email)
    
    if res.status_code != 200:
        flash("Error reseting  account password!", "red")
        return redirect(f"/admin/all_accounts")
    
    flash("Account password reset successfully.", "green")
    return redirect(f"/admin/all_accounts")