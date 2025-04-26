
from flask import Blueprint, render_template, request, session, jsonify, redirect, flash
import json
import api
import tools

admin_dashboard_bp = Blueprint("admin_dashboard", __name__, url_prefix="/admin")


# ---------------------------------------
# GET METHOD
# ---------------------------------------
@admin_dashboard_bp.route("/dashboard", methods=["GET"])
def dashboard_get():
    if not tools.check_session():
        flash("Your are not logged in!", "red")
        return redirect("/login")
    
    if not tools.is_admin():
        flash("Your account is not authorized!", "red")
        return redirect("/login")
    
    tools.update_token()
    
    res = api.GetAllColleges()
    colleges = res.get("data")
    
    
    return render_template(
        f"/admin/{tools.get_lang()}/dashboard.html",
        colleges=colleges
    )