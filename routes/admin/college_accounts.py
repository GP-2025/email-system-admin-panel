
from flask import Blueprint, render_template, request, session, jsonify, redirect, flash
import json
import api
import tools

admin_college_accounts_bp = Blueprint("admin_college_accounts", __name__, url_prefix="/admin")


# ---------------------------------------
# GET METHOD
# ---------------------------------------
@admin_college_accounts_bp.route("/colleges/<int:college_id>/accounts", methods=["GET"])
def admin_college_accounts_get(college_id):
    if not tools.check_session():
        flash("Your are not logged in!" if tools.get_lang() == "en" else "أنت غير مسجل دخول!", "red")
        return redirect("/login")
    
    if not tools.is_admin():
        flash("Your account is not authorized to enter this page!" if tools.get_lang() == "en" else "حسابك غير مصرح له بالدخول إلى هذه الصفحة!", "red")
        return redirect("/login")
    
    tools.update_token()
    res = api.GetCollegeById(college_id)
    if res.status_code != 200:
        return render_template('/main/en/404.html'), 404
    college = res.json()
    
    departments = college.get("departments")
    if departments:
        departments = list(reversed(departments))
    
    res = api.AllUsers()
    accounts_data = res.json().get("data")
    accounts = []
    for acc in accounts_data:
        if acc.get("collegeId") == college_id:
            accounts.append(acc)
    
    if accounts:
        accounts = list(reversed(accounts))
    
    tools.update_token()
    res = api.GetAllColleges()
    colleges = res.json().get("data")
    if colleges:
        colleges = list(reversed(colleges))
        
    roles = tools.get_roles(tools.get_lang())
    
    breadcrumbs = [
        {
            "en_name": "Hurghada University | Dashboard",
            "ar_name": "جامعة الغردقة | الرئيسية",
            "url": "/admin/dashboard"
        },
        {
            "en_name": "Colleges",
            "ar_name": "الكليات",
            "url": "/admin/colleges"
        },
        {
            "en_name": f"{college.get('name')}",
            "ar_name": f"{college.get('name')}",
            "url": f"/admin/colleges/{college_id}"
        },
        {
            "en_name": "Accounts",
            "ar_name": "الحسابات",
            "url": f"/admin/colleges/{college_id}/accounts"
        }
    ]
    return render_template(
        f"/admin/{tools.get_lang()}/college_accounts.html",
        accounts=accounts,
        roles=roles,
        departments=departments,
        college=college,
        colleges=colleges,
        breadcrumbs=breadcrumbs
    )


# ---------------------------------------
# POST METHOD
# ---------------------------------------
@admin_college_accounts_bp.route("/colleges/<int:college_id>/accounts/add_account", methods=["POST"])
def admin_college_accounts_post(college_id):
    if not tools.check_session():
        flash("Your are not logged in!" if tools.get_lang() == "en" else "أنت غير مسجل دخول!", "red")
        return redirect("/login")
    
    if not tools.is_admin():
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
            return redirect(f"/admin/colleges/{college_id}/accounts")
    
    res = api.AllUsers()
    accounts = res.json().get("data")
    for account in accounts:        
        if account["email"] == account_email:
            flash("Email already exists!" if tools.get_lang() == "en" else "البريد الإلكتروني موجود بالفعل!", "red")
            return redirect(f"/admin/colleges/{college_id}/accounts")
        if account["nationalId"] == account_national_id:
            flash("National ID already exists!" if tools.get_lang() == "en" else "الرقم القومي موجود بالفعل!", "red")
            return redirect(f"/admin/colleges/{college_id}/accounts")
    
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
        return redirect(f"/admin/colleges/{college_id}/accounts")
    
    flash("Account added successfully." if tools.get_lang() == "en" else "تمت إضافة الحساب بنجاح.", "green")
    return redirect(f"/admin/colleges/{college_id}/accounts")



# ---------------------------------------
# POST METHOD
# ---------------------------------------
@admin_college_accounts_bp.route("/colleges/<int:college_id>/accounts/edit_account/<int:account_id>", methods=["POST"])
def admin_college_accounts_edit_account(college_id, account_id):
    if not tools.check_session():
        flash("Your are not logged in!" if tools.get_lang() == "en" else "أنت غير مسجل دخول!", "red")
        return redirect("/login")
    
    if not tools.is_admin():
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
        if department.get("userId") and department.get("userId") != account_id:
            flash("Department already has an account!" if tools.get_lang() == "en" else "القسم لديه حساب بالفعل!", "red")
            return redirect(f"/admin/colleges/{college_id}/accounts")
    
    res = api.AllUsers()
    accounts = res.json().get("data")
    for account in accounts:
        if account["email"] == account_email and account.get("id") != account_id:
            flash("Email already exists!" if tools.get_lang() == "en" else "البريد الإلكتروني موجود بالفعل!", "red")
            return redirect(f"/admin/colleges/{college_id}/accounts")
        if account["nationalId"] == account_national_id and account.get("id") != account_id:
            flash("National ID already exists!" if tools.get_lang() == "en" else "الرقم القومي موجود بالفعل!", "red")
            return redirect(f"/admin/colleges/{college_id}/accounts")
    
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
        flash(res.json().get("message", "Error editing account!" if tools.get_lang() == "en" else "خطأ في تعديل الحساب!"), "red")
        return redirect(f"/admin/colleges/{college_id}/accounts")
    
    flash("Account updated successfully." if tools.get_lang() == "en" else "تم تحديث الحساب بنجاح.", "green")
    return redirect(f"/admin/colleges/{college_id}/accounts")



# ---------------------------------------
# POST METHOD
# ---------------------------------------
@admin_college_accounts_bp.route("/colleges/<int:college_id>/accounts/reset_password/<string:email>", methods=["POST"])
def admin_college_accounts_reset_password(college_id, email):
    if not tools.check_session():
        flash("Your are not logged in!" if tools.get_lang() == "en" else "أنت غير مسجل دخول!", "red")
        return redirect("/login")
    
    if not tools.is_admin():
        flash("Your account is not authorized to enter this page!" if tools.get_lang() == "en" else "حسابك غير مصرح له بالدخول إلى هذه الصفحة!", "red")
        return redirect("/login")
    
    tools.update_token()
    res = api.ResetPassword(email)
    
    if res.status_code != 200:
        flash("Error reseting account password!" if tools.get_lang() == "en" else "خطأ في إعادة تعيين كلمة المرور!", "red")
        return redirect(f"/admin/colleges/{college_id}/accounts")
    
    flash("Account password reset successfully." if tools.get_lang() == "en" else "تم إعادة تعيين كلمة المرور بنجاح.", "green")
    return redirect(f"/admin/colleges/{college_id}/accounts")