
from flask import Blueprint, render_template, request, session, jsonify, redirect, flash
import json
import api
import tools

admin_dashboard_bp = Blueprint("admin_dashboard", __name__, url_prefix="/admin")


# ---------------------------------------
# GET METHOD
# ---------------------------------------
@admin_dashboard_bp.route("/dashboard", methods=["GET"])
def admin_dashboard_get():
    if not tools.check_session():
        flash("Your are not logged in!", "red")
        return redirect("/login")
    
    if not tools.is_admin():
        flash("Your account is not authorized!", "red")
        return redirect("/login")
    
    
    tools.update_token()
    res = api.GetAllColleges()
    no_of_colleges = res.get("count")
    
    res = api.AllUsers()
    no_of_all_accounts = res.get("count")
    
    no_of_college_admins = 0
    no_of_admins = 1 # counting the already logged-in user
    
    accounts = res.get("data")
    for acc in accounts:
        if acc.get("role").lower() == "collegeadmin":
            no_of_college_admins += 1
        if acc.get("role").lower() == "admin":
            no_of_admins += 1
    
    return render_template(
        f"/admin/{tools.get_lang()}/dashboard.html",
        no_of_colleges=no_of_colleges,
        no_of_college_admins=no_of_college_admins,
        no_of_all_accounts=no_of_all_accounts,
        no_of_admins=no_of_admins,
           
    )