
from flask import Blueprint, render_template, request, jsonify, redirect
import api

get_started_bp = Blueprint('get_started', __name__, url_prefix='')


# ---------------------------------------
# GET METHOD
# ---------------------------------------
@get_started_bp.route('/get_started', methods=["GET"])
def get_started_get():
    return render_template('/main/en/get_started.html')

