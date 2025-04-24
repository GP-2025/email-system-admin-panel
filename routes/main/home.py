
from flask import Blueprint, render_template, request, jsonify, redirect
import api
import tools

home_bp = Blueprint('home', __name__, url_prefix='')


# ---------------------------------------
# GET METHOD
# ---------------------------------------
@home_bp.route('/', methods=["GET"])
def home_get():
    is_logged_in = tools.check_session()
    
    if not is_logged_in:
        return redirect("/login")
    
    return redirect("/admin")

