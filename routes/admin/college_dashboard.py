
from flask import Blueprint, render_template, request, session, jsonify, redirect, flash
import json
import api
import tools

admin_college_dashboard_bp = Blueprint("admin_college_dashboard", __name__, url_prefix="/admin")


# ---------------------------------------
# GET METHOD
# ---------------------------------------
@admin_college_dashboard_bp.route("/colleges/<int:college_id>", methods=["GET"])
def admin_college_dashboard_get(college_id):
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
    
    res = api.AllUsers()
    accounts = []
    for account in res.json().get("data", []):
        if account.get("collegeId") == college_id:
            accounts.append(account)
    
    no_of_departments = len(departments)
    no_of_accounts = len(accounts)
    
    breadcrumbs = [
        {
            "en_name": "Hurghada University | Dashboard",
            "ar_name": "[جامعة الغردقة] | الرئيسية",
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
        }
    ]
    return render_template(
        f"/admin/{tools.get_lang()}/college_dashboard.html",
        no_of_departments=no_of_departments,
        no_of_accounts=no_of_accounts,
        college=college,
        breadcrumbs=breadcrumbs
    )

