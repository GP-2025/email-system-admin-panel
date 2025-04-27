from flask import Blueprint, render_template, request, session, jsonify, redirect, flash
import json
import api
import tools

admin_dashboard_bp = Blueprint("admin_dashboard", __name__, url_prefix="/admin")


# ---------------------------------------
# GET METHOD
# ---------------------------------------
@admin_dashboard_bp.route("/dashboard", methods=["GET"])
def admin_dashboard_get():
    if not tools.check_session():
        flash("Your are not logged in!" if tools.get_lang() == "en" else "أنت غير مسجل دخول!", "red")
        return redirect("/login")
    
    if not tools.is_admin():
        flash("Your account is not authorized to enter this page!" if tools.get_lang() == "en" else "حسابك غير مصرح له بالدخول إلى هذه الصفحة!", "red")
        return redirect("/login")
    
    
    tools.update_token()
    res = api.GetAllColleges()
    no_of_colleges = res.json().get("count")
    
    res = api.AllUsers()
    no_of_all_accounts = res.json().get("count")
    
    no_of_college_admins = 0
    no_of_admins = 1 # counting the already logged-in user
    
    accounts = res.json().get("data")
    for acc in accounts:
        if acc.get("role").lower() == "collegeadmin":
            no_of_college_admins += 1
        if acc.get("role").lower() == "admin":
            no_of_admins += 1
    
    breadcrumbs = [
        {
            "en_name": "Hurghada University | Dashboard",
            "ar_name": "[جامعة الغردقة] | الرئيسية",
            "url": "/admin/dashboard"
        }
    ]
    
    return render_template(
        f"/admin/{tools.get_lang()}/dashboard.html",
        no_of_colleges=no_of_colleges,
        no_of_college_admins=no_of_college_admins,
        no_of_all_accounts=no_of_all_accounts,
        no_of_admins=no_of_admins,
        breadcrumbs=breadcrumbs
    )