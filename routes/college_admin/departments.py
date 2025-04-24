
from flask import Blueprint, render_template, request, session, jsonify, redirect, flash
import json
import api
import tools

college_admin_departments_bp = Blueprint("departments", __name__, url_prefix="/college_admin")


# ---------------------------------------
# GET METHOD
# ---------------------------------------
@college_admin_departments_bp.route("/departments", methods=["GET"])
def departments_get():
    if not tools.check_session():
        flash("Your are not logged in!", "red")
        return redirect("/login")
    
    if not tools.is_college_admin():
        flash("Your account is not authorized!", "red")
        return redirect("/login")
    
    college_id = session.get("college_id")
    tools.update_token()
    
    # departments = api.GetCollegeById(college_id).get("departments")
    departments = api.AllUsers().get("data")
    print(departments)
    
    return render_template(
        f"/college_admin/{tools.get_lang()}/departments.html",
        departments=departments
    )