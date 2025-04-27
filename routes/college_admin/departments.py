
from flask import Blueprint, render_template, request, session, jsonify, redirect, flash
import json
import api
import tools

college_admin_departments_bp = Blueprint("college_admin_departments", __name__, url_prefix="/college_admin")


# ---------------------------------------
# GET METHOD
# ---------------------------------------
@college_admin_departments_bp.route("/departments", methods=["GET"])
def college_admin_departments_get():
    if not tools.check_session():
        flash("Your are not logged in!", "red")
        return redirect("/login")
    
    if not tools.is_college_admin():
        flash("Your account is not authorized!", "red")
        return redirect("/login")
    
    college_id = session.get("college_id")
    
    tools.update_token()
    res = api.GetCollegeById(college_id)
    if res.status_code != 200:
        return render_template('/main/en/404.html'), 404
    
    college = res.json()
    
    departments = college.get("departments")
    if departments:
        departments = list(reversed(departments))
    
    breadcrumbs = [
        {
            "en_name": f"{college.get('name')} | Dashboard",
            "ar_name": f"{college.get('name')} | الرئيسية",
            "url": "/college_admin/dashboard"
        },
        {
            "en_name": f"Departments",
            "ar_name": f"الاقسام",
            "url": "/college_admin/departments"
        }
    ]
    return render_template(
        f"/college_admin/{tools.get_lang()}/departments.html",
        departments=departments,
        college=college,
        breadcrumbs=breadcrumbs
    )


# ---------------------------------------
# POST METHOD : ADD
# ---------------------------------------
@college_admin_departments_bp.route("/departments/add_department", methods=["POST"])
def college_admin_departments_post():
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
def college_admin_departments_put(department_id):
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
        "id": int(department_id),
        "name": department_name,
        "abbreviation": department_abbreviation,
        "college_id": session.get("college_id")
    }
    res = api.EditDepartment(data)
    
    if res.status_code != 200:
        flash(res.json().get("message"), "red")
        return redirect("/college_admin/departments")
    
    flash("Department updated successfully.", "green")
    return redirect("/college_admin/departments")