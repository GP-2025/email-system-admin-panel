
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
    
    college = api.GetCollegeById(college_id)
    departments = college.get("departments")
    print(departments)
    
    return render_template(
        f"/college_admin/{tools.get_lang()}/departments.html",
        departments=departments,
        college=college
    )


# ---------------------------------------
# POST METHOD : ADD
# ---------------------------------------
@college_admin_departments_bp.route("/departments/add_department", methods=["POST"])
def departments_post():
    if not tools.check_session():
        flash("Your are not logged in!", "red")
        return redirect("/login")
    
    if not tools.is_college_admin():
        flash("Your account is not authorized!", "red")
        return redirect("/login")
    
    department_name = request.form.get("department_name")
    department_abbreviation = request.form.get("department_abbreviation")
    
    tools.update_token()
    data = {
        "name": department_name,
        "abbreviation": department_abbreviation,
        "college_id": session.get("college_id")
    }
    res = api.AddDepartment(data)
    if res.status_code != 200:
        flash("Department name or abbreviation already exists.", "red")
        return redirect("/college_admin/departments")
    
    flash("Department added successfully.", "green")
    return redirect("/college_admin/departments")


# ---------------------------------------
# POST METHOD : UPDATE
# ---------------------------------------
@college_admin_departments_bp.route("/departments/update_department/<int:department_id>", methods=["POST"])
def departments_put(department_id):
    if not tools.check_session():
        flash("Your are not logged in!", "red")
        return redirect("/login")
    
    if not tools.is_college_admin():
        flash("Your account is not authorized!", "red")
        return redirect("/login")
    
    department_name = request.form.get("department_name")
    department_abbreviation = request.form.get("department_abbreviation")
    
    tools.update_token()
    data = {
        "id": department_id,
        "name": department_name,
        "abbreviation": department_abbreviation,
        "college_id": session.get("college_id")
    }
    res = api.EditDepartment(data)
    if res.status_code != 200:
        flash("Department name or abbreviation already exists.", "red")
        return redirect("/college_admin/departments")
    
    flash("Department added successfully.", "green")
    return redirect("/college_admin/departments")