
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
        flash("Your are not logged in!", "red")
        return redirect("/login")
    
    if not tools.is_college_admin():
        flash("Your account is not authorized!", "red")
        return redirect("/login")
    
    college_id = session.get("college_id")
    tools.update_token()
    
    college = api.GetCollegeById(college_id)
    departments = college.get("departments")
    accounts = api.AllUsers().get("data")
    
    no_of_departments = len(departments)
    no_of_accounts = len(accounts)
    
    return render_template(
        f"/college_admin/{tools.get_lang()}/dashboard.html",
        no_of_departments=no_of_departments,
        no_of_accounts=no_of_accounts,
        college=college
    )