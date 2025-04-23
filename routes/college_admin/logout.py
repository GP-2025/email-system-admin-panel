from flask import Blueprint, render_template, session, redirect

logout_bp = Blueprint('logout', __name__)

@logout_bp.route('/logout', methods=["GET"])
def none():
    # Clear the session
    session.clear()
    # Redirect to the home page or login page
    return redirect('/')