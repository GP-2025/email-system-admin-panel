
from flask import Blueprint, render_template, request, session, jsonify, redirect, flash
import json
import api
import tools

college_admin_accounts_bp = Blueprint("accounts", __name__, url_prefix="/college_admin")


# ---------------------------------------
# GET METHOD
# ---------------------------------------
@college_admin_accounts_bp.route("/accounts", methods=["GET"])
def accounts_get():
    if not tools.check_session():
        flash("Your are not logged in!", "red")
        return redirect("/login")
    
    if not tools.is_college_admin():
        flash("Your account is not authorized!", "red")
        return redirect("/login")
    
    college_id = session.get("college_id")
    tools.update_token()
    
    college = api.GetCollegeById(college_id)
    accounts = api.AllUsers().get("data")
    departments = college.get("departments")
    roles = tools.get_roles({tools.get_lang()})
    
    return render_template(
        f"/college_admin/{tools.get_lang()}/accounts.html",
        accounts=accounts,
        roles=roles,
        departments=departments,
        college=college,
    )


# ---------------------------------------
# POST METHOD
# ---------------------------------------
@college_admin_accounts_bp.route("/accounts/add_account", methods=["POST"])
def accounts_post():
    if not tools.check_session():
        flash("Your are not logged in!", "red")
        return redirect("/login")
    
    if not tools.is_college_admin():
        flash("Your account is not authorized!", "red")
        return redirect("/login")
    
    print(request.form)
    
    # college_id = session.get("college_id")
    # tools.update_token()
    return redirect("/college_admin/accounts")