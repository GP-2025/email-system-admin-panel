
from flask import Blueprint, render_template, request, session, jsonify, redirect, flash
import json
import api
import tools

admin_colleges_bp = Blueprint("admin_colleges", __name__, url_prefix="/admin")


# ---------------------------------------
# GET METHOD
# ---------------------------------------
@admin_colleges_bp.route("/colleges", methods=["GET"])
def admin_colleges_get():
    if not tools.check_session():
        flash("Your are not logged in!" if tools.get_lang() == "en" else "أنت غير مسجل دخول!", "red")
        return redirect("/login")
    
    if not tools.is_admin():
        flash("Your account is not authorized to enter this page!" if tools.get_lang() == "en" else "حسابك غير مصرح له بالدخول إلى هذه الصفحة!", "red")
        return redirect("/login")
    
    tools.update_token()
    res = api.GetAllColleges()
    colleges = res.json().get("data")
    if colleges:
        colleges = list(reversed(colleges))
        
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
        }
    ]
    
    return render_template(
        f"/admin/{tools.get_lang()}/colleges.html",
        colleges=colleges,
        breadcrumbs=breadcrumbs
    )


# ---------------------------------------
# POST METHOD : ADD
# ---------------------------------------
@admin_colleges_bp.route("/colleges/add_college", methods=["POST"])
def admin_colleges_post():
    if not tools.check_session():
        flash("Your are not logged in!" if tools.get_lang() == "en" else "أنت غير مسجل دخول!", "red")
        return redirect("/login")
    
    if not tools.is_admin():
        flash("Your account is not authorized to enter this page!" if tools.get_lang() == "en" else "حسابك غير مصرح له بالدخول إلى هذه الصفحة!", "red")
        return redirect("/login")
    
    college_name = request.form.get("college_name")
    college_abbreviation = request.form.get("college_abbreviation")
    
    tools.update_token()
    data = {
        "name": college_name,
        "abbreviation": college_abbreviation
    }
    res = api.AddCollege(data)
    if res.status_code != 200:
        flash("College name or abbreviation already exists!" if tools.get_lang() == "en" else "اسم الكلية أو الاختصار موجود بالفعل!", "red")
        return redirect("/admin/colleges")
    
    flash("College added successfully." if tools.get_lang() == "en" else "تمت إضافة الكلية بنجاح.", "green")
    return redirect("/admin/colleges")


# ---------------------------------------
# POST METHOD : UPDATE
# ---------------------------------------
@admin_colleges_bp.route("/colleges/update_college/<int:college_id>", methods=["POST"])
def admin_colleges_put(college_id):
    if not tools.check_session():
        flash("Your are not logged in!" if tools.get_lang() == "en" else "أنت غير مسجل دخول!", "red")
        return redirect("/login")
    
    if not tools.is_admin():
        flash("Your account is not authorized to enter this page!" if tools.get_lang() == "en" else "حسابك غير مصرح له بالدخول إلى هذه الصفحة!", "red")
        return redirect("/login")
    
    college_name = request.form.get("college_name")
    college_abbreviation = request.form.get("college_abbreviation")
    
    tools.update_token()
    data = {
        "Id": int(college_id),
        "Name": college_name,
        "Abbreviation": college_abbreviation,
    }
    print(json.dumps(data, indent=2))
    res = api.UpdateCollege(data)
    
    if res.status_code != 200:
        flash(res.json().get("message"), "red")
        return redirect("/admin/colleges")
    
    flash("College updated successfully." if tools.get_lang() == "en" else "تم تحديث الكلية بنجاح.", "green")
    return redirect("/admin/colleges")
