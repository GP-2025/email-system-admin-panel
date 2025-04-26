
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
        flash("Your are not logged in!", "red")
        return redirect("/login")
    
    if not tools.is_admin():
        flash("Your account is not authorized!", "red")
        return redirect("/login")
    
    tools.update_token()
    res = api.GetAllColleges()
    colleges = res.get("data")
    if colleges:
        colleges = list(reversed(colleges))
        
    return render_template(
        f"/admin/{tools.get_lang()}/colleges.html",
        colleges=colleges,
    )


# ---------------------------------------
# POST METHOD : ADD
# ---------------------------------------
@admin_colleges_bp.route("/colleges/add_college", methods=["POST"])
def admin_colleges_post():
    if not tools.check_session():
        flash("Your are not logged in!", "red")
        return redirect("/login")
    
    if not tools.is_admin():
        flash("Your account is not authorized!", "red")
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
        flash("College name or abbreviation already exists.", "red")
        return redirect("/admin/colleges")
    
    flash("College added successfully.", "green")
    return redirect("/admin/colleges")


# ---------------------------------------
# POST METHOD : UPDATE
# ---------------------------------------
@admin_colleges_bp.route("/colleges/update_college/<int:college_id>", methods=["POST"])
def admin_colleges_put(college_id):
    if not tools.check_session():
        flash("Your are not logged in!", "red")
        return redirect("/login")
    
    if not tools.is_admin():
        flash("Your account is not authorized!", "red")
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
    print(res.text)
    
    if res.status_code != 200:
        flash(res.json().get("message"), "red")
        return redirect("/admin/colleges")
    
    flash("college updated successfully.", "green")
    return redirect("/admin/colleges")
