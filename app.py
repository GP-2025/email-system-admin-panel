from flask import Flask, render_template
import os

app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = 'secret_key'

os.environ["API_BASE_URL"] = "https://emailingsystemapi.runasp.net"

import api

# ---------------------------------------
# Main Routes Blueprints
# ---------------------------------------
from routes.main import main_bp

app.register_blueprint(main_bp)


# ---------------------------------------
# Admin Routes Blueprints
# ---------------------------------------
from routes.admin.dashboard import admin_dashboard_bp
from routes.admin.colleges import admin_colleges_bp
from routes.admin.college_dashboard import admin_college_dashboard_bp
from routes.admin.college_departments import admin_college_departments_bp
from routes.admin.college_accounts import admin_college_accounts_bp
from routes.admin.colleges_admins import admin_colleges_admins_bp
from routes.admin.admins import admin_admins_bp

app.register_blueprint(admin_dashboard_bp)
app.register_blueprint(admin_colleges_bp)
app.register_blueprint(admin_college_dashboard_bp)
app.register_blueprint(admin_college_departments_bp)
app.register_blueprint(admin_college_accounts_bp)
app.register_blueprint(admin_colleges_admins_bp)
app.register_blueprint(admin_admins_bp)


# ---------------------------------------
# College Admin Routes Blueprints
# ---------------------------------------
from routes.college_admin.dashboard import college_admin_dashboard_bp
from routes.college_admin.departments import college_admin_departments_bp
from routes.college_admin.accounts import college_admin_accounts_bp

app.register_blueprint(college_admin_dashboard_bp)
app.register_blueprint(college_admin_departments_bp)
app.register_blueprint(college_admin_accounts_bp)


# ---------------------------------------
# 404 Error Handler
# ---------------------------------------
from tools import get_lang
@app.errorhandler(404)
def page_not_found(e):
    return render_template(f'/main/{get_lang()}/404.html'), 404


# ---------------------------------------
# Main
# ---------------------------------------

if __name__ == "__main__":
    app.run(port=4000, debug=True)