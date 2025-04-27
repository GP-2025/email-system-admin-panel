from flask import Blueprint, render_template, request, session, jsonify, redirect, flash
import json
import api
import tools

college_admin_dashboard_bp = Blueprint("college_admin_dashboard", __name__, url_prefix="/college_admin")


# ---------------------------------------
# GET METHOD
# ---------------------------------------
@college_admin_dashboard_bp.route("/dashboard", methods=["GET"])
def college_admin_dashboard_get():
    if not tools.check_session():
        flash("You are not logged in!" if tools.get_lang() == "en" else "لم يتم تسجيل دخول!", "red")
        return redirect("/login")
    
    if not tools.is_college_admin():
        flash("Your account is not authorized!" if tools.get_lang() == "en" else "أنت غير مصرح بالدخول!", "red")
        return redirect("/login")
    
    college_id = session.get("college_id")
    tools.update_token()
    
    res = api.GetCollegeById(college_id)
    if res.status_code != 200:
        return render_template('/main/en/404.html'), 404
    
    college = res.json()
    departments = college.get("departments")
    
    res = api.AllUsers()
    
    no_of_accounts = 0
    
    # getting only the accounts that are not college admins
    for account in res.json().get("data"):
        if account.get("role") == "CollegeAdmin":
            continue
        no_of_accounts += 1
    
    no_of_departments = len(departments)
    
    breadcrumbs = [
        {
            "en_name": f"{college.get('name')} | Dashboard",
            "ar_name": f"{college.get('name')} | الرئيسية",
            "url": "/college_admin/dashboard"
        }
    ]
    
    return render_template(
        f"/college_admin/{tools.get_lang()}/dashboard.html",
        no_of_departments=no_of_departments,
        no_of_accounts=no_of_accounts,
        college=college,
        breadcrumbs=breadcrumbs
    )