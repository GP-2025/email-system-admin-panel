
from flask import Blueprint, render_template, request, jsonify, redirect, flash
import api
import tools

admin_bp = Blueprint("admin", __name__, url_prefix="")


# ---------------------------------------
# GET METHOD
# ---------------------------------------
@admin_bp.route("/admin", methods=["GET"])
def admin_get():
    if not tools.check_session():
        flash("Your are not logged in!", "red")
        return redirect("/login")
    
    if tools.is_admin():
        return redirect("/admin/dashboard")
    if tools.is_college_admin():
        return redirect("/college_admin/dashboard")
    
    return redirect("/")

# ---------------------------------------
# GET METHOD
# ---------------------------------------
@admin_bp.route("/college_admin", methods=["GET"])
def college_admin_get():
    if not tools.check_session():
        flash("Your are not logged in!", "red")
        return redirect("/login")
    
    if tools.is_admin():
        return redirect("/admin/dashboard")
    if tools.is_college_admin():
        return redirect("/college_admin/dashboard")
    
    return redirect("/")
