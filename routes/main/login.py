
from flask import Blueprint, render_template, request, jsonify, redirect
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
    return redirect("/login")