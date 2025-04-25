
from flask import Blueprint, render_template, request, session, jsonify, redirect, flash
import api
import tools

logout_bp = Blueprint("logout", __name__, url_prefix="")


# ---------------------------------------
# GET METHOD
# ---------------------------------------
@logout_bp.route("/logout", methods=["GET"])
def logout_get():
    tools.delete_session()
    return redirect("/login")
