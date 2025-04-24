
from flask import Blueprint, render_template, request, session, jsonify, redirect, flash
import api
import tools

login_bp = Blueprint("login", __name__, url_prefix="")


# ---------------------------------------
# GET METHOD
# ---------------------------------------
@login_bp.route("/login", methods=["GET"])
def login_get():
    if tools.check_session():
        flash("You are already logged in.", "orange")
        flash("You are already logged in.", "red")
        return redirect("/admin")
    
    return render_template(f"/main/{tools.get_lang()}/login.html")


# ---------------------------------------
# POST METHOD
# ---------------------------------------
@login_bp.route("/login", methods=["POST"])
def login_post():    
    email = request.form.get("email")
    password = request.form.get("password")
    
    res = api.Login(email, password)
    if not res.get("userId"):
        flash(res.get("message"), "red")
        return redirect("/login")
    
    is_session_set = tools.set_session(res)
    if not is_session_set:
        flash("Error setting account session.", "red")
        return redirect("/login")
    
    # checking if the logged in user is not a college admin or an admin
    if not tools.is_admin() and not tools.is_college_admin():
        flash("Your account is not authorized!", "red")
        return redirect("/login")
    
    if tools.is_admin():
        return redirect("/admin/dashboard")
    
    if tools.is_college_admin():
        return redirect("/college_admin/dashboard")
    
    return redirect("/")