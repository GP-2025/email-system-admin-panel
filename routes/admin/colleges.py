
from flask import Blueprint, render_template, request, session, jsonify, redirect, flash
import json
import api
import tools

admin_colleges_bp = Blueprint("admin_colleges", __name__, url_prefix="/admin")


# ---------------------------------------
# GET METHOD
# ---------------------------------------
@admin_colleges_bp.route("/colleges", methods=["GET"])
def departments_get():
    if not tools.check_session():
        flash("Your are not logged in!", "red")
        return redirect("/login")
    
    if not tools.is_admin():
        flash("Your account is not authorized!", "red")
        return redirect("/login")
    
    college_id = session.get("college_id")
    
    tools.update_token()
    college = api.GetCollegeById(college_id)
    
    departments = college.get("departments")
    if departments:
        departments = list(reversed(departments))
    
    return render_template(
        f"/admin/{tools.get_lang()}/departments.html",
        departments=departments,
        college=college
    )


# ---------------------------------------
# POST METHOD : ADD
# ---------------------------------------
@admin_colleges_bp.route("/colleges/add_department", methods=["POST"])
def departments_post():
    if not tools.check_session():
        flash("Your are not logged in!", "red")
        return redirect("/login")
    
    if not tools.is_admin():
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
        return redirect("/admin/departments")
    
    flash("Department added successfully.", "green")
    return redirect("/admin/departments")


# ---------------------------------------
# POST METHOD : UPDATE
# ---------------------------------------
@admin_colleges_bp.route("/colleges/update_college/<int:college_id>", methods=["POST"])
def departments_put(department_id):
    if not tools.check_session():
        flash("Your are not logged in!", "red")
        return redirect("/login")
    
    if not tools.is_admin():
        flash("Your account is not authorized!", "red")
        return redirect("/login")
    
    department_name = request.form.get("department_name")
    department_abbreviation = request.form.get("department_abbreviation")
    
    tools.update_token()
    data = {
        "id": int(department_id),
        "name": department_name,
        "abbreviation": department_abbreviation,
        "college_id": session.get("college_id")
    }
    print(json.dumps(data, indent=2))
    res = api.EditDepartment(data)
    
    if res.status_code != 200:
        flash(res.json().get("message"), "red")
        return redirect("/admin/departments")
    
    flash("Department updated successfully.", "green")
    return redirect("/admin/departments")