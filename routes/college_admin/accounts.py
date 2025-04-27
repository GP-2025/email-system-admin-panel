
from flask import Blueprint, render_template, request, session, jsonify, redirect, flash
import json
import api
import tools
import tempfile

college_admin_accounts_bp = Blueprint("college_admin_accounts", __name__, url_prefix="/college_admin")


# ---------------------------------------
# GET METHOD
# ---------------------------------------
@college_admin_accounts_bp.route("/accounts", methods=["GET"])
def college_admin_accounts_get():
    if not tools.check_session():
        flash("You are not logged in!" if tools.get_lang() == "en" else "أنت غير مسجل دخول!", "red")
        return redirect("/login")
    
    if not tools.is_college_admin():
        flash("Your account is not authorized to enter this page!" if tools.get_lang() == "en" else "حسابك غير مصرح له بالدخول إلى هذه الصفحة!", "red")
        return redirect("/login")
    
    college_id = session.get("college_id")
    tools.update_token()
    
    res = api.GetCollegeById(college_id)
    college = res.json()
    
    res = api.AllUsers()
    accounts = []
    
    # getting only the accounts that are not college admins
    for account in res.json().get("data"):
        if account.get("role") == "CollegeAdmin":
            continue
        accounts.append(account)
        
    if accounts:
        accounts = list(reversed(accounts))
    
    departments = college.get("departments")
    if departments:
        departments = list(reversed(departments))
    
    roles = tools.get_roles(tools.get_lang())
    
    breadcrumbs = [
        {
            "en_name": f"{college.get('name')} | Dashboard",
            "ar_name": f"{college.get('name')} | الرئيسية",
            "url": "/college_admin/dashboard"
        },
        {
            "en_name": "Accounts",
            "ar_name": "الحسابات",
            "url": "/college_admin/accounts"
        }
    ]
    
    return render_template(
        f"/college_admin/{tools.get_lang()}/accounts.html",
        accounts=accounts,
        roles=roles,
        departments=departments,
        college=college,
        breadcrumbs=breadcrumbs
    )


# ---------------------------------------
# POST METHOD
# ---------------------------------------
@college_admin_accounts_bp.route("/accounts/add_account", methods=["POST"])
def college_admin_accounts_post():
    if not tools.check_session():
        flash("You are not logged in!" if tools.get_lang() == "en" else "أنت غير مسجل دخول!", "red")
        return redirect("/login")
    
    if not tools.is_college_admin():
        flash("Your account is not authorized to enter this page!" if tools.get_lang() == "en" else "حسابك غير مصرح له بالدخول إلى هذه الصفحة!", "red")
        return redirect("/login")
    
    tools.update_token()
    
    account_department_id = request.form.get("account_department_id", None)
    account_email = request.form.get("account_email")
    account_national_id = request.form.get("account_national_id")

    if account_department_id:
        res = api.GetDepartmentById(account_department_id)
        if res.status_code != 200:
            flash("Error checking for chosen department!" if tools.get_lang() == "en" else "خطأ في التحقق من القسم المختار!", "red")
        department = res.json()
        if department.get("userId"):
            flash("Department already has an account!" if tools.get_lang() == "en" else "القسم لديه حساب بالفعل!", "red")
            return redirect("/college_admin/accounts")
    
    res = api.AllUsers()
    accounts = res.json().get("data")
    for account in accounts:        
        if account["email"] == account_email:
            flash("Email already exists!" if tools.get_lang() == "en" else "البريد الإلكتروني موجود بالفعل!", "red")
            return redirect("/college_admin/accounts")
        if account["nationalId"] == account_national_id:
            flash("National ID already exists!" if tools.get_lang() == "en" else "رقم الهوية موجود بالفعل!", "red")
            return redirect("/college_admin/accounts")
    
    college_id = session.get("college_id")
    
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
        flash(res.json().get("message", "Error registering account!" if tools.get_lang() == "en" else "خطأ في تسجيل الحساب!"), "red")
        return redirect("/college_admin/accounts")
    
    flash("Account added successfully." if tools.get_lang() == "en" else "تمت إضافة الحساب بنجاح.", "green")
    return redirect("/college_admin/accounts")



# ---------------------------------------
# POST METHOD
# ---------------------------------------
@college_admin_accounts_bp.route("/accounts/edit_account/<int:account_id>", methods=["POST"])
def college_admin_accounts_edit_account(account_id):
    if not tools.check_session():
        flash("You are not logged in!" if tools.get_lang() == "en" else "أنت غير مسجل دخول!", "red")
        return redirect("/login")
    
    if not tools.is_college_admin():
        flash("Your account is not authorized to enter this page!" if tools.get_lang() == "en" else "حسابك غير مصرح له بالدخول إلى هذه الصفحة!", "red")
        return redirect("/login")
    
    tools.update_token()
    
    account_department_id = request.form.get("account_department_id", "")
    account_email = request.form.get("account_email")
    account_national_id = request.form.get("account_national_id")
    
    if account_department_id:
        res = api.GetDepartmentById(account_department_id)
        if res.status_code != 200:
            flash("Error checking for chosen department!" if tools.get_lang() == "en" else "خطأ في التحقق من القسم المختار!", "red")
        department = res.json()
        if department.get("userId") and department.get("userId") != account_id:
            flash("Department already has an account!" if tools.get_lang() == "en" else "القسم لديه حساب بالفعل!", "red")
            return redirect("/college_admin/accounts")
    
    res = api.AllUsers()
    accounts = res.json().get("data")
    for account in accounts:
        if account["email"] == account_email and account.get("id") != account_id:
            flash("Email already exists!" if tools.get_lang() == "en" else "البريد الإلكتروني موجود بالفعل!", "red")
            return redirect("/college_admin/accounts")
        if account["nationalId"] == account_national_id and account.get("id") != account_id:
            flash("National ID already exists!" if tools.get_lang() == "en" else "رقم الهوية موجود بالفعل!", "red")
            return redirect("/college_admin/accounts")
    
    college_id = session.get("college_id")
    
    data = {
        "Email": request.form.get("account_email"),
        "Name": request.form.get("account_name"),
        "DepartmentId": int(account_department_id) if account_department_id else None,
        "CollegeId": int(college_id),
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
        flash(res.json().get("message", "Error editing account!" if tools.get_lang() == "en" else "خطأ في تعديل الحساب!"), "red")
        return redirect("/college_admin/accounts")
    
    flash("Account updated successfully." if tools.get_lang() == "en" else "تم تحديث الحساب بنجاح.", "green")
    return redirect("/college_admin/accounts")



# ---------------------------------------
# POST METHOD
# ---------------------------------------
@college_admin_accounts_bp.route("/accounts/reset_password/<string:email>", methods=["POST"])
def college_admin_accounts_reset_password(email):
    if not tools.check_session():
        flash("You are not logged in!" if tools.get_lang() == "en" else "أنت غير مسجل دخول!", "red")
        return redirect("/login")
    
    if not tools.is_college_admin():
        flash("Your account is not authorized to enter this page!" if tools.get_lang() == "en" else "حسابك غير مصرح له بالدخول إلى هذه الصفحة!", "red")
        return redirect("/login")
    
    tools.update_token()
    res = api.ResetPassword(email)
    
    if res.status_code != 200:
        flash("Error resetting account password!" if tools.get_lang() == "en" else "خطأ في إعادة تعيين كلمة المرور!", "red")
        return redirect("/college_admin/accounts")
    
    flash("Account password reset successfully." if tools.get_lang() == "en" else "تم إعادة تعيين كلمة المرور بنجاح.", "green")
    return redirect("/college_admin/accounts")