
from flask import Blueprint, render_template, request, session, jsonify, redirect, flash
import json
import api
import tools

admin_colleges_admins_bp = Blueprint("admin_colleges_admins", __name__, url_prefix="/admin")


# ---------------------------------------
# GET METHOD
# ---------------------------------------
@admin_colleges_admins_bp.route("/colleges_admins", methods=["GET"])
def admin_colleges_admins_get():
    if not tools.check_session():
        flash("Your are not logged in!" if tools.get_lang() == "en" else "أنت غير مسجل دخول!", "red")
        return redirect("/login")
    
    if not tools.is_admin():
        flash("Your account is not authorized to enter this page!" if tools.get_lang() == "en" else "حسابك غير مصرح له بالدخول إلى هذه الصفحة!", "red")
        return redirect("/login")
    
    tools.update_token()
    
    res = api.AllUsers()
    accounts_data = res.json().get("data")
    accounts = []
    for acc in accounts_data:
        if acc.get("role") == "CollegeAdmin":
            accounts.append(acc)
    
    if accounts:
        accounts = list(reversed(accounts))
    
    tools.update_token()
    res = api.GetAllColleges()
    colleges = res.json().get("data")
    if colleges:
        colleges = list(reversed(colleges))
        
    roles = tools.get_roles(tools.get_lang())
    
    breadcrumbs = [
        {
            "en_name": "Hurghada University | Dashboard",
            "ar_name": "جامعة الغردقة | الرئيسية",
            "url": "/admin/dashboard"
        },
        {
            "en_name": "Colleges Admins",
            "ar_name": "مديرين الكليات",
            "url": "/admin/colleges_admins"
        }
    ]
    
    return render_template(
        f"/admin/{tools.get_lang()}/colleges_admins.html",
        accounts=accounts,
        roles=roles,
        colleges=colleges,
        breadcrumbs=breadcrumbs
    )

