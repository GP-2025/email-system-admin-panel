
from flask import Blueprint, render_template, session, request, jsonify, redirect, flash
import api
import tools

holder_bp = Blueprint("holder", __name__, url_prefix="")


# ---------------------------------------
# GET METHOD
# ---------------------------------------
@holder_bp.route("/holder", methods=["GET"])
def holder_get():
    return render_template(f"/main/{tools.get_lang()}/holder.html")


# ---------------------------------------
# POST METHOD
# ---------------------------------------
@holder_bp.route("/holder", methods=["POST"])
def holder_post():
    return redirect("/holder")