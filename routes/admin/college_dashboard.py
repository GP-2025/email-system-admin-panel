
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
        flash("Your are not logged in!", "red")
        return redirect("/login")
    
    if not tools.is_admin():
        flash("Your account is not authorized!", "red")
        return redirect("/login")
    
    tools.update_token()
    
    res = api.GetCollegeById(college_id)
    if res.status_code != 200:
        return render_template('/main/en/404.html'), 404
        
    college = res.json()
    departments = college.get("departments")
    
    res = api.AllUsers()
    accounts = []
    for account in res.get("data", []):
        if account.get("collegeId") == college_id:
            accounts.append(account)
    
    no_of_departments = len(departments)
    no_of_accounts = len(accounts)
    
    return render_template(
        f"/admin/{tools.get_lang()}/college_dashboard.html",
        no_of_departments=no_of_departments,
        no_of_accounts=no_of_accounts,
        college=college
    )

