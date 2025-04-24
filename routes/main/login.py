
from flask import Blueprint, render_template, request, jsonify, redirect, flash
import api
import tools

login_bp = Blueprint("login", __name__, url_prefix="")


# ---------------------------------------
# GET METHOD
# ---------------------------------------
@login_bp.route("/login", methods=["GET"])
def login_get():
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
    if is_session_set:
        flash("Error setting session.", "red")
        return redirect("/login")
    
    return redirect("/admin/dashboard")
    