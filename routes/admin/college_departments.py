
from flask import Blueprint, render_template, request, session, jsonify, redirect, flash
import json
import api
import tools

admin_college_departments_bp = Blueprint("admin_college_departments", __name__, url_prefix="/admin")


# ---------------------------------------
# GET METHOD
# ---------------------------------------
@admin_college_departments_bp.route("/colleges/<int:college_id>/departments", methods=["GET"])
def admin_college_departments_get(college_id):
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
            "en_name": "Departments",
            "ar_name": "الاقسام",
            "url": f"/admin/colleges/{college_id}/departments"
        }
    ]
    return render_template(
        f"/admin/{tools.get_lang()}/college_departments.html",
        departments=departments,
        college=college,
        breadcrumbs=breadcrumbs
    )


# ---------------------------------------
# POST METHOD : ADD
# ---------------------------------------
@admin_college_departments_bp.route("/colleges/<int:college_id>/departments/add_department", methods=["POST"])
def admin_college_departments_post(college_id):
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
    
    department_name = request.form.get("department_name")
    department_abbreviation = request.form.get("department_abbreviation")
    
    data = {
        "name": department_name,
        "abbreviation": department_abbreviation,
        "college_id": college_id
    }
    res = api.AddDepartment(data)
    if res.status_code != 200:
        flash("Department name or abbreviation already exists." if tools.get_lang() == "en" else "اسم القسم أو الاختصار موجود بالفعل.", "red")
        return redirect(f"/admin/colleges/{college_id}/departments")
    
    flash("Department added successfully." if tools.get_lang() == "en" else "تمت إضافة القسم بنجاح.", "green")
    return redirect(f"/admin/colleges/{college_id}/departments")


# ---------------------------------------
# POST METHOD : UPDATE
# ---------------------------------------
@admin_college_departments_bp.route("/colleges/<int:college_id>/departments/update_department/<int:department_id>", methods=["POST"])
def admin_college_departments_put(college_id, department_id):
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
    
    res = api.GetDepartmentById(department_id)
    if res.status_code != 200:
        return render_template('/main/en/404.html'), 404
    
    department_name = request.form.get("department_name")
    department_abbreviation = request.form.get("department_abbreviation")
    
    tools.update_token()
    data = {
        "id": int(department_id),
        "name": department_name,
        "abbreviation": department_abbreviation,
        "college_id": college_id
    }
    res = api.EditDepartment(data)
    
    if res.status_code != 200:
        flash(res.json().get("message"), "red")
        return redirect(f"/admin/colleges/{college_id}/departments")
    
    flash("Department updated successfully." if tools.get_lang() == "en" else "تم تحديث القسم بنجاح.", "green")
    return redirect(f"/admin/colleges/{college_id}/departments")