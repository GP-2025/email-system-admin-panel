
from flask import Blueprint, render_template, request, jsonify, redirect
import api
import tools

home_bp = Blueprint('home', __name__, url_prefix='')


# ---------------------------------------
# GET METHOD
# ---------------------------------------
@home_bp.route('/', methods=["GET"])
def home_get():
    
    return render_template(f"/main/{tools.get_lang()}/home.html")


