
from flask import Blueprint, render_template, request, session, jsonify, redirect, flash
import json
import api
import tools

admin_admins_bp = Blueprint("admin_admins", __name__, url_prefix="/admin")


# ---------------------------------------
# GET METHOD
# ---------------------------------------
@admin_admins_bp.route("/admins", methods=["GET"])
def admin_admins_get():
    if not tools.check_session():
        flash("Your are not logged in!", "red")
        return redirect("/login")
    
    if not tools.is_admin():
        flash("Your account is not authorized!", "red")
        return redirect("/login")
    
    tools.update_token()
    
    res = api.AllUsers()
    accounts_data = res.json().get("data")
    accounts = []
    for acc in accounts_data:
        if acc.get("role") == "Admin":
            accounts.append(acc)
    
    if accounts:
        accounts = list(reversed(accounts))
    
    return render_template(
        f"/admin/{tools.get_lang()}/admins.html",
        accounts=accounts,
    )
    
