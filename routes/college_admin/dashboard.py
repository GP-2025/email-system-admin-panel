
from flask import Blueprint, render_template, request, jsonify, redirect, flash
import api
import tools

dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/college_admin")


# ---------------------------------------
# GET METHOD
# ---------------------------------------
@dashboard_bp.route("/dashboard", methods=["GET"])
def dashboard_get():
    if not tools.check_session():
        flash("Your are not logged in!", "red")
        return redirect("/admin")
    
    if not tools.is_college_admin():
        flash("Your account is not authorized!", "red")
        return redirect("/login")
    
    return render_template(f"/college_admin/{tools.get_lang()}/dashboard.html")


# ---------------------------------------
# POST METHOD
# ---------------------------------------
@dashboard_bp.route("/dashboard", methods=["POST"])
def dashboard_post():
    return redirect("/admin/dashboard")