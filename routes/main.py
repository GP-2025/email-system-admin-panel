
from flask import Blueprint, render_template, request, jsonify, redirect, flash, session
import api
import tools

main_bp = Blueprint('main', __name__, url_prefix='')


# ---------------------------------------
# GET METHOD : main
# ---------------------------------------
@main_bp.route('/', methods=["GET"])
def main_home_get():
    
    return render_template(f"/main/{tools.get_lang()}/home.html")


# ---------------------------------------
# POST METHOD : language
# ---------------------------------------
@main_bp.route("/lang", methods=["POST"])
def main_language_post():
    lang = request.form.get("lang")
    url = request.referrer
    
    if lang not in ["en", "ar"]:
        lang = "en"
    
    tools.update_lang(lang)
    return redirect(url)


# ---------------------------------------
# GET METHOD : login
# ---------------------------------------
@main_bp.route("/login", methods=["GET"])
def main_login_get():
    if tools.check_session():
        flash("You are already logged in." if tools.get_lang() == "en" else "أنت مسجل دخول بالفعل.", "orange")
        return redirect("/admin")
    
    return render_template(f"/main/{tools.get_lang()}/login.html")


# ---------------------------------------
# POST METHOD : login
# ---------------------------------------
@main_bp.route("/login", methods=["POST"])
def main_login_post():    
    email = request.form.get("email")
    password = request.form.get("password")
    
    res = api.Login(email, password)
    if not res.get("userId"):
        flash(res.get("message"), "red")
        return redirect("/login")
    
    res["password"] = password
    is_session_set = tools.set_session(res)
    if not is_session_set:
        flash("Error setting account session." if tools.get_lang() == "en" else "خطأ في تسجيل جلسة الحساب.", "red")
        return redirect("/login")
    
    # checking if the logged in user is not a college admin or an admin
    if not tools.is_admin() and not tools.is_college_admin():
        flash("Your account is not authorized to enter this page!" if tools.get_lang() == "en" else "حسابك غير مصرح به!", "red")
        return redirect("/login")
    
    if tools.is_admin():
        flash(f"Welcome back, {session['name']}." if tools.get_lang() == "en" else f"مرحباً بعودتك, {session['name']}.", "green")
        return redirect("/admin/dashboard")
    
    if tools.is_college_admin():
        flash(f"Welcome back, {session['name']}." if tools.get_lang() == "en" else f"مرحباً بعودتك, {session['name']}.", "green")
        return redirect("/college_admin/dashboard")
    
    
    return redirect("/")


# ---------------------------------------
# GET METHOD : admin
# ---------------------------------------
@main_bp.route("/admin", methods=["GET"])
def main_admin_get():
    if not tools.check_session():
        flash("Your are not logged in!" if tools.get_lang() == "en" else "أنت غير مسجل دخول!", "red")
        return redirect("/login")
    
    if tools.is_admin():
        return redirect("/admin/dashboard")
    if tools.is_college_admin():
        return redirect("/college_admin/dashboard")
    
    return redirect("/")


# ---------------------------------------
# GET METHOD : college_admin
# ---------------------------------------
@main_bp.route("/college_admin", methods=["GET"])
def main_college_admin_get():
    if not tools.check_session():
        flash("Your are not logged in!" if tools.get_lang() == "en" else "أنت غير مسجل دخول!", "red")
        return redirect("/login")
    
    if tools.is_admin():
        return redirect("/admin/dashboard")
    if tools.is_college_admin():
        return redirect("/college_admin/dashboard")
    
    return redirect("/")


# ---------------------------------------
# GET METHOD : Logout
# ---------------------------------------
@main_bp.route("/logout", methods=["GET"])
def main_logout_get():
    tools.delete_session()
    return redirect("/login")

