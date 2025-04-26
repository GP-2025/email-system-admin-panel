
from flask import Blueprint, render_template, session, request, jsonify, redirect, flash
import api
import tools

colleges_bp = Blueprint("colleges", __name__, url_prefix="/admin")


# ---------------------------------------
# GET METHOD
# ---------------------------------------
@colleges_bp.route("/colleges", methods=["GET"])
def colleges_get():
    return render_template(f"/main/{tools.get_lang()}/colleges.html")


# ---------------------------------------
# POST METHOD
# ---------------------------------------
@colleges_bp.route("/colleges", methods=["POST"])
def colleges_post():
    return redirect("/colleges")